
# The following prefixes extend the sequence of valid Fibonacci numbers
FIB_PRE = {"1", "2"}

import sys


class Fibba:
    """Calculate the nth Fibonacci number"""
    f = [1, 1]

    def __getitem__(self, n):
        """Dynamically grow the Fibonacci sequence on demand"""
        cur = len(self.f)
        if n < cur:
            return self.f[n]
        else:
            while cur < n + 1:
                self.f.append(self.f[cur - 1] + self.f[cur - 2])
                cur += 1
            return self.f[n]

def num_decodings(s: str) -> int:
    """A message is encoded by converting ASCII characters A-Z into their
    positional index 1-26.
    
    However, once encoded, there are multiple possible decodings depending on
    where character breaks are inserted.
    
    Calculate the number of possible decodings for a given message s where
    len(s) > 0.
    
    """

    fibba = Fibba()

    # A leading zero indicates no possible decoding.  Testing for the special
    # case outside the loop (that looks for 00, 30, 40, etc.) saves a comparison
    # during each loop to see if s[i-1] exists.
    if s[0] == "0":
        return 0

    # The number of consecutive characters contributing to the Fibonacci sequence.
    fib = 0
    # The running total of possible decodings.
    total = 1

    # Walk through the string forwards
    for i in range(len(s)):

        # Encountering a 0 will capture a 1 or 2 before it and prevent it from 
        # contributing to the sequence.
        if s[i] == "0":
            # Any other value preceding it means there is no possible decoding.
            if s[i-1] not in FIB_PRE:
                return 0
            fib -= 1

        # Track the sequence getting longer, but do not adjust the total until 
        # the sequence terminates.
        elif s[i] in FIB_PRE:
            fib += 1
            continue

        # The sequence terminated, so adjust the total.  Depending on how it
        # terminated, the terminating character may or may not contribute to 
        # the sequence.
        # 
        # e.g.:
        # 11-19 and 21-26 MAY be split and so increase the sequence length.
        # 27+ MUST be split and so do not increase the sequence length.
        else:
            if s[i-1] == "1" or (s[i-1] == "2" and s[i] in {"1", "2", "3", "4", "5", "6"}):
                fib += 1
            
        # Because the sequence terminated, multiply the total existing decodings
        # by the additional decodings possible with this sequence, and reset the 
        # sequence length.
        total *= fibba[fib]
        fib = 0

    # When the end of string is reached, if there is an in-progress sequence,
    # include it in the total as well.
    if fib > 0:
        total *= fibba[fib]

    return total
    

if __name__ == "__main__":
    total = num_decodings(s=sys.argv[1])
    print(total)
