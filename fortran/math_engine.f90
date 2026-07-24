module math_engine
    use iso_c_binding, only: c_double, c_int
    implicit none

contains

    ! Expose this function directly to C / Python as "fortran_matmul"
    subroutine fortran_matmul(A, B, C, n, k, m) bind(c, name="fortran_matmul")
        integer(c_int), value, intent(in) :: n, k, m
        real(c_double), intent(in)  :: A(n, k)
        real(c_double), intent(in)  :: B(k, m)
        real(c_double), intent(out) :: C(n, m)

        integer :: i, j, l
        real(c_double) :: temp

        ! Initialize output matrix
        C = 0.0_c_double

        ! Fortran is Column-Major: Outer loop over columns (j) and middle loop (l) 
        ! yields optimal hardware cache locality and vectorization.
        !$omp parallel do collapse(2) private(i, l, temp) schedule(static)
        do j = 1, m
            do l = 1, k
                temp = B(l, j)
                ! SIMD vector loop across contiguous memory rows
                !$omp simd
                do i = 1, n
                    C(i, j) = C(i, j) + A(i, l) * temp
                end do
            end do
        end do
        !$omp end parallel do

    end subroutine fortran_matmul

end module math_engine
