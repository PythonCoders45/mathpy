class Series:
  def __init__(self, data, index=None, name=None):
        if not isinstance(data, list):
            data = list(data)
        self.data = data
        self.name = name
        
        if index is None:
            self.index = list(range(len(data)))
        else:
            if len(index) != len(data):
                raise ValueError("Length of index must match length of data.")
            self.index = list(index)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        if key in self.index:
            # Labeled lookup
            idx = self.index.index(key)
            return self.data[idx]
        elif isinstance(key, int) and 0 <= key < len(self.data):
            # Positional lookup backup
            return self.data[key]
        elif isinstance(key, list):
            # Fancy indexing / Boolean masking
            if len(key) == len(self.data) and all(isinstance(x, bool) for x in key):
                new_data = [d for d, m in zip(self.data, key) if m]
                new_idx = [i for i, m in zip(self.index, key) if m]
                return Series(new_data, index=new_idx, name=self.name)
            else:
                new_data = [self[k] for k in key]
                return Series(new_data, index=key, name=self.name)
        raise KeyError(f"Key '{key}' not found in Series.")

    # --------------------------------------------------------------------------
    # MISSING DATA HANDLING
    # --------------------------------------------------------------------------
    def isna(self):
        """Returns a boolean Series marking None / missing values as True."""
        flags = [x is None or (isinstance(x, float) and x != x) for x in self.data]
        return Series(flags, index=self.index, name=self.name)

    def dropna(self):
        """Returns a new Series with missing values removed."""
        mask = [not is_missing for is_missing in self.isna().data]
        return self[mask]

    def fillna(self, value):
        """Returns a new Series with missing values replaced by value."""
        new_data = [value if is_m else x for x, is_m in zip(self.data, self.isna().data)]
        return Series(new_data, index=self.index, name=self.name)

    # --------------------------------------------------------------------------
    # STATISTICAL REDUCTIONS
    # --------------------------------------------------------------------------
    def _valid_data(self):
        return [x for x in self.dropna().data if isinstance(x, (int, float))]

    def sum(self):
        valid = self._valid_data()
        return sum(valid) if valid else 0

    def mean(self):
        valid = self._valid_data()
        return sum(valid) / len(valid) if valid else 0.0

    def std(self):
        valid = self._valid_data()
        if len(valid) <= 1:
            return 0.0
        m = self.mean()
        var = sum((x - m) ** 2 for x in valid) / (len(valid) - 1)
        return var ** 0.5

    def min(self):
        valid = self._valid_data()
        return min(valid) if valid else None

    def max(self):
        valid = self._valid_data()
        return max(valid) if valid else None

    def value_counts(self):
        """Returns counts of unique values as a Series."""
        counts = {}
        for x in self.data:
            counts[x] = counts.get(x, 0) + 1
        return Series(list(counts.values()), index=list(counts.keys()), name="count")

    # --------------------------------------------------------------------------
    # ELEMENT-WISE ARITHMETIC & MAPPING
    # --------------------------------------------------------------------------
    def apply(self, func):
        """Applies a scalar function element-wise."""
        new_data = [func(x) if x is not None else None for x in self.data]
        return Series(new_data, index=self.index, name=self.name)

    def __add__(self, other):
        if isinstance(other, (int, float, str)):
            return self.apply(lambda x: x + other)
        elif isinstance(other, Series):
            aligned = [self[idx] + other[idx] if (idx in self.index and idx in other.index) else None for idx in self.index]
            return Series(aligned, index=self.index, name=self.name)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.apply(lambda x: x - other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.apply(lambda x: x * other)

    def __eq__(self, value): return Series([x == value for x in self.data], index=self.index)
    def __gt__(self, value): return Series([x > value if x is not None else False for x in self.data], index=self.index)
    def __lt__(self, value): return Series([x < value if x is not None else False for x in self.data], index=self.index)

    def __repr__(self):
        lines = [f"{k}\t{v}" for k, v in zip(self.index, self.data)]
        if self.name:
            lines.append(f"Name: {self.name}, ")
        lines.append(f"Length: {len(self.data)}")
        return "\n".join(lines)


# ==============================================================================
# SECTION 2: DATAFRAME CLASS (LABELED 2D TABULAR STRUCTURE)
# ==============================================================================

class DataFrame:
    """
    A pure Python 2D tabular data structure with column names, row indices,
    querying, joins, and group-by aggregations.
    """
    def __init__(self, data_dict, index=None):
        if not isinstance(data_dict, dict):
            raise TypeError("Data must be provided as a dictionary of lists/Series.")
        
        self.columns = list(data_dict.keys())
        
        # Check uniform length
        col_lengths = [len(v) for v in data_dict.values()]
        if len(set(col_lengths)) > 1:
            raise ValueError("All columns must have the same length.")
        
        num_rows = col_lengths[0] if col_lengths else 0
        self.index = list(index) if index is not None else list(range(num_rows))
        
        self._columns = {}
        for col, vals in data_dict.items():
            if isinstance(vals, Series):
                self._columns[col] = Series(vals.data, index=self.index, name=col)
            else:
                self._columns[col] = Series(list(vals), index=self.index, name=col)

    @property
    def shape(self):
        return (len(self.index), len(self.columns))

    def __getitem__(self, key):
        if isinstance(key, str):
            # Select column -> Returns Series
            return self._columns[key]
        elif isinstance(key, list):
            if all(isinstance(k, str) for k in key):
                # Select subset of columns -> Returns DataFrame
                sub_dict = {k: self._columns[k].data for k in key}
                return DataFrame(sub_dict, index=self.index)
            elif all(isinstance(k, bool) for k in key):
                # Boolean row mask
                sub_dict = {col: self._columns[col][key].data for col in self.columns}
                new_idx = [i for i, m in zip(self.index, key) if m]
                return DataFrame(sub_dict, index=new_idx)
        elif isinstance(key, Series) and all(isinstance(k, bool) for k in key.data):
            return self[key.data]
        raise KeyError(f"Invalid index key: {key}")

    def __setitem__(self, col_name, value):
        if isinstance(value, Series):
            vals = value.data
        elif isinstance(value, list):
            vals = value
        else:
            vals = [value] * len(self.index)
            
        if len(vals) != len(self.index):
            raise ValueError("Length of new column does not match DataFrame index length.")
            
        if col_name not in self.columns:
            self.columns.append(col_name)
        self._columns[col_name] = Series(vals, index=self.index, name=col_name)

    # --------------------------------------------------------------------------
    # LOC & ILOC INDEXING HELPERS
    # --------------------------------------------------------------------------
    def iloc(self, row_idx):
        """Positional row selection returning a dictionary or Series."""
        row_dict = {col: self._columns[col].data[row_idx] for col in self.columns}
        return Series(list(row_dict.values()), index=self.columns, name=self.index[row_idx])

    def loc(self, row_label):
        """Label-based row selection."""
        idx = self.index.index(row_label)
        return self.iloc(idx)

    # --------------------------------------------------------------------------
    # HEAD & TAIL
    # --------------------------------------------------------------------------
    def head(self, n=5):
        n = min(n, len(self.index))
        sub_dict = {col: self._columns[col].data[:n] for col in self.columns}
        return DataFrame(sub_dict, index=self.index[:n])

    def tail(self, n=5):
        n = min(n, len(self.index))
        start = len(self.index) - n
        sub_dict = {col: self._columns[col].data[start:] for col in self.columns}
        return DataFrame(sub_dict, index=self.index[start:])

    # --------------------------------------------------------------------------
    # MISSING DATA & CLEANING
    # --------------------------------------------------------------------------
    def dropna(self):
        """Drops any row containing at least one missing value."""
        valid_rows = []
        for i in range(len(self.index)):
            row_vals = [self._columns[col].data[i] for col in self.columns]
            if not any(v is None or (isinstance(v, float) and v != v) for v in row_vals):
                valid_rows.append(i)
        
        mask = [i in valid_rows for i in range(len(self.index))]
        return self[mask]

    def fillna(self, value):
        """Fills missing values across all columns."""
        filled = {col: self._columns[col].fillna(value).data for col in self.columns}
        return DataFrame(filled, index=self.index)

    # --------------------------------------------------------------------------
    # STATISTICAL SUMMARY
    # --------------------------------------------------------------------------
    def describe(self):
        """Generates descriptive statistics for numeric columns."""
        summary = {}
        metrics = ["count", "mean", "std", "min", "max"]
        for col in self.columns:
            s = self._columns[col]
            valid = s._valid_data()
            if valid:
                summary[col] = [
                    len(valid),
                    s.mean(),
                    s.std(),
                    s.min(),
                    s.max()
                ]
        return DataFrame(summary, index=metrics)

    # --------------------------------------------------------------------------
    # GROUPBY & AGGREGATION ENGINE
    # --------------------------------------------------------------------------
    def groupby(self, by_column):
        """Splits DataFrame into groups based on key column values."""
        if by_column not in self.columns:
            raise KeyError(f"Column '{by_column}' not found.")
        return GroupBy(self, by_column)

    # --------------------------------------------------------------------------
    # DISPLAY FORMATTER
    # --------------------------------------------------------------------------
    def __repr__(self):
        header = "\t" + "\t".join(self.columns)
        rows = []
        for i, idx in enumerate(self.index):
            r_vals = [str(self._columns[col].data[i]) for col in self.columns]
            rows.append(f"{idx}\t" + "\t".join(r_vals))
        return header + "\n" + "\n".join(rows)


# ==============================================================================
# SECTION 3: GROUPBY SPLIT-APPLY-COMBINE ENGINE
# ==============================================================================

class GroupBy:
    """Group-By helper class executing split-apply-combine aggregations."""
    def __init__(self, df, by_column):
        self.df = df
        self.by_column = by_column
        self.groups = {}
        
        # Split step
        for i, val in enumerate(df[by_column].data):
            if val not in self.groups:
                self.groups[val] = []
            self.groups[val].append(i)

    def sum(self):
        """Computes column-wise sums per group."""
        return self._aggregate(lambda s: s.sum())

    def mean(self):
        """Computes column-wise means per group."""
        return self._aggregate(lambda s: s.mean())

    def _aggregate(self, func):
        res_dict = {self.by_column: list(self.groups.keys())}
        target_cols = [c for c in self.df.columns if c != self.by_column]

        for col in target_cols:
            col_res = []
            for group_key, row_indices in self.groups.items():
                group_data = [self.df[col].data[idx] for idx in row_indices]
                sub_series = Series(group_data)
                col_res.append(func(sub_series))
            res_dict[col] = col_res

        return DataFrame(res_dict)


# ==============================================================================
# SECTION 4: FILE I/O - PURE PYTHON CSV PARSER & WRITER
# ==============================================================================

def read_csv(file_content_str, delimiter=","):
    """
    Parses a raw CSV text string into a DataFrame without using standard csv module.
    Automatically casts numbers to float/int and empty strings to None.
    """
    lines = [line.strip() for line in file_content_str.strip().split("\n") if line.strip()]
    if not lines:
        return DataFrame({})

    header = [h.strip() for h in lines[0].split(delimiter)]
    col_data = {h: [] for h in header}

    for line in lines[1:]:
        parts = [p.strip() for p in line.split(delimiter)]
        for h, part in zip(header, parts):
            if part == "" or part.lower() == "null" or part.lower() == "nan":
                val = None
            else:
                # Attempt automatic numerical type conversion
                try:
                    val = int(part)
                except ValueError:
                    try:
                        val = float(part)
                    except ValueError:
                        val = part
            col_data[h].append(val)

    return DataFrame(col_data)

def to_csv(df, delimiter=","):
    """Converts a DataFrame back into a formatted CSV string."""
    header_str = delimiter.join(df.columns)
    lines = [header_str]

    for i in range(len(df.index)):
        row_vals = [str(df[col].data[i]) if df[col].data[i] is not None else "" for col in df.columns]
        lines.append(delimiter.join(row_vals))

    return "\n".join(lines)


# ==============================================================================
# SECTION 5: RELATIONAL JOIN / MERGE ENGINE
# ==============================================================================

def merge(left_df, right_df, on_column, how="inner"):
    """
    Executes relational database joins (inner, left, right) between two DataFrames.
    """
    if on_column not in left_df.columns or on_column not in right_df.columns:
        raise KeyError(f"Join column '{on_column}' must exist in both DataFrames.")

    left_keys = left_df[on_column].data
    right_keys = right_df[on_column].data

    merged_data = {}
    all_cols = [on_column] + [c for c in left_df.columns if c != on_column] + [c for c in right_df.columns if c != on_column]
    for c in all_cols:
        merged_data[c] = []

    for l_idx, l_key in enumerate(left_keys):
        matches = [r_idx for r_idx, r_key in enumerate(right_keys) if r_key == l_key]
        if matches:
            for r_idx in matches:
                merged_data[on_column].append(l_key)
                for c in left_df.columns:
                    if c != on_column:
                        merged_data[c].append(left_df[c].data[l_idx])
                for c in right_df.columns:
                    if c != on_column:
                        merged_data[c].append(right_df[c].data[r_idx])
        elif how == "left":
            merged_data[on_column].append(l_key)
            for c in left_df.columns:
                if c != on_column:
                    merged_data[c].append(left_df[c].data[l_idx])
            for c in right_df.columns:
                if c != on_column:
                    merged_data[c].append(None)

    return DataFrame(merged_data)
