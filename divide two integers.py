class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract large powers of 2 at a time
        while dividend >= divisor:
            value = divisor
            multiple = 1

            while dividend >= (value << 1):
                value <<= 1
                multiple <<= 1

            dividend -= value
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Handle 32-bit integer limits
        if quotient > INT_MAX:
            return INT_MAX

        if quotient < INT_MIN:
            return INT_MIN

        return quotient
        