"""
Resistor color code calculator.
Xuanye Zhu
"""

while True:
            def get_input(Rmin, Rmax):
                ''' Prompt user to enter desired resistance and tolerance'''
                while True:
                    try:
                        Rdes = float(input(f'Enter desired resistance from {Rmin} to {Rmax/1e9} G ohm (examples: 11000 or 1.1e4): '))
                        if Rdes >= Rmin and Rdes <= Rmax:
                            break
                        else:
                            print('Invalid resistance, out of range')
                    except ValueError:
                        print('Invalid resistance, must be a number')

                while True:
                    try:
                        tol = int(input('Enter desired tolerance of 5, 10, or 20 percent: '))
                        if tol == 5 or tol == 10 or tol == 20:
                            break
                        else:
                            print('Invalid tolerance, must be an integer 5, 10, or 20')
                    except:
                        print('Invalid tolerance, must be an integer 5, 10, or 20')
                return Rdes, tol

            # Define min and max resistance values for user input, in ohms
            Rmin = 0.1
            Rmax = 70e9

            Rdes, tol = get_input(Rmin, Rmax)
            print(f'Finding closest nominal resistance value to {Rdes:g} ohm with tolerance {tol}%:')

            # Define nominal resistance values for the given tolerance.
            # Add 100 at the end of the list so that the rightmost tolerance band is included.
            # All of them start with 10 and ends with 100
            if tol == 5:
                Rnom = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91, 100]
            #elif tol == 10:
            elif tol == 10:
                Rnom=[10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100]
            #else:  # tol == 20 case
            else:
                Rnom=[10, 15, 22, 33, 47, 68, 100]


            ## Assume we have 4 color bands: A B C tol. The ABC_color is indexed by an integer in this version. A and B are the first and second color bands. C is the multipler
            ABC_color = {-2:'silver', -1:'gold', 0:'black', 1:'brown', 2:'red', 3:'orange',
                4:'yellow', 5:'green', 6:'blue', 7:'violet', 8:'grey', 9:'white'}
            tol_color = {5:'gold', 10:'silver', 20:'No 4th band'}  # No color band for 20% tol


            ## Convert to Rdes = M x 10^C with 10 <= M < 100
            #C=
            #M=
            import math
            C = math.floor(math.log10(Rdes)) - 1
            M = Rdes / (10 ** C)
            ## Find closest nominal value in terms of A B ( Percent Error = |R_actual − R_nominal| / R_nominal  × 100% ) R_actual=Rdes, R_nominal=Rcandidate
            k_min = -3
            k_max = 9

            best_error = float('inf')
            Rclosest = None
            m_closest = None
            k_closest = None

            for k in range(k_min, k_max + 1):
                for m in Rnom:
                    Rcandidate = m * (10 ** k)

                    # Only consider candidates within the input range
                    if Rcandidate < Rmin or Rcandidate > Rmax:
                        continue

                    percent_error = abs(Rdes - Rcandidate) / Rcandidate * 100

                    if percent_error < best_error:
                        best_error = percent_error
                        Rclosest = Rcandidate
                        m_closest = m
                        k_closest = k

            # Get the A and B values with integer division and mod operations
            #A =
            #B =
            if m_closest == 100:
                m_closest = 10
                k_closest = k_closest + 1

            A = m_closest // 10
            B = m_closest % 10

            # Rclosest = AB*10**C  # Closest nominal resistance in ohms
            AB = 10 * A + B
            C = k_closest
            Rclosest = AB * (10 ** C)

            # Find the % error between the desired and nominal resistances
            # percent_error =
            percent_error = (Rdes - Rclosest) / Rclosest * 100
            #  print(f'Error between desired and nominal resistance values = {percent_error:.2f}%') also warning

            print(f'Error between desired and nominal resistance values = {percent_error:+.2f}%')

            if percent_error > tol:
                print('Warning: percent error exceeds tolerance')

            # Get colors and print color code# Write your code here :-)  :-(
            #print(f'Color code for {Rclosest:.1e} ohm with {tol}% tolerance is "{ABC_color[A]} {ABC_color[B]} {ABC_color[C]} {tol_color[tol]}"')

            band1 = ABC_color[A]
            band2 = ABC_color[B]
            band3 = ABC_color[C]
            band4 = tol_color[tol]

            print(f'Color code for {Rclosest:.1e} ohm with {tol}% tolerance is "{band1} {band2} {band3} {band4}"')































