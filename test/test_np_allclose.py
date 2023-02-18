# This is no real test, rather a short investigation to understand np.allclose

# See the docs: https://numpy.org/doc/stable/reference/generated/numpy.allclose.html
# Defaults: numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
# Algorithm:  np.allclose calculates for each coefficients of two given matrices "a" and "b" this:
#             absolute(a - b) <= (atol + rtol * absolute(b))


def test_compare_two_small_numbers(a, b, atol, rtol):
    lhs = abs(a - b)
    rhs = atol + rtol * abs(b)
    print(f"{lhs} !<= {rhs} is {lhs<= rhs}")


if __name__ == "__main__":
    cases = [
        dict(
            atol=1e-8,
            rtol=1e-5,
            a=1e-10,
            b=1e-6,
        ),
        dict(
            atol=1e-8,
            rtol=1e-5,
            a=1e-6,
            b=1e-10,
        ),
    ]
    for case in cases:
        test_compare_two_small_numbers(**case)
