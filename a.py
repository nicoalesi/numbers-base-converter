def add_one(a: str) -> str:
        '''
        add 1 to a binary number 

        a: binary number
        '''

        res = ''

        b =  '1'.zfill(len(a)) # binary number 1

        carry = '0' # carried bit during sum

        for i, j in zip(a[::-1], b[::-1]):
            if i == '1' and j == '1' and carry == '0':
                res += '0'

                carry = '1'
            elif i == '1' and j == '1' and carry == '1':
                res += '1'

                carry = '1'
            elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '0':
                res += '1'
            elif ((i == '1' and j == '0') or (i == '0' and j == '1')) and carry == '1':
                res += '0'

                carry = '1'
            elif i == '0' and j == '0':
                res += carry

                carry = '0'
  
        res = res[::-1]

        return res
    
def dec_part_to_bin(x: int):
        ''''
        convert decimal part to binary (first method that doesn't work for very small numbers)

        x: decimal number 
        '''

        res = ''
        viewed = [] # list of numbers already seen, used to understand when there is a cycle 

        while x != 0 and x not in viewed:
            viewed.append(x)
       
            x *= 2

            if x < 1:
                res += '0'
            else:
                res += '1'

                x -= 1

        return res
    
def dec_part_to_bin_2(x: int, prec: int):
        ''''
        convert decimal part to binary (second method that work for very small numbers)

        x: decimal number
        '''

        res = ''

        close_x = 0 # number that has to be as close as possible to x
        count_ones = 0

        len_m = {
            16: 10,
            32: 23,
            64: 55
        }
        
        prec_m = len_m[prec] # precison of mantissa, for very small fractions like 0.000002341, until when calculate bits

        i = 1
        
        while count_ones < prec_m:
            power = pow(2, -i)

            if power + close_x < x:
                res += '1'

                close_x += power

                count_ones += 1
            elif power + close_x > x:
                res += '0'
            else:
                if i == 1:
                    return '1'
                else:
                    return res + '1'
        
            i += 1
    
        return res

    
def bit_ext(self, x: str, type: str):
        '''
        does a binary extension

        x: binary number
        type: s(igned) or u(nsigned)
        '''

        bit_to_ext = self.n - len(x) 

        pre = '1' * bit_to_ext if type == 's' else '0' * bit_to_ext

        x = pre + x

        return x

def dec_to_ieee754(from_base, prec) -> str:
        '''
        convert dec to bin

        type: u(nsigned), s(igned) or f(raction)
        '''

        res = ''

        len_e = {
                16: 5,
                32: 8,
                64: 11
            }

        len_m = {
                16: 10,
                32: 23,
                64: 55
            }

        # check if its a special case inf or -inf
        if from_base in ['inf', '-inf']:
                s = '1' if from_base == '-inf' else '0'
                e = '1' * len_e[prec]
                m = '0' * len_m[prec]

                return s + e + m
    
        str_from_base = str(abs(from_base))
          
        # if number is too small or too big
        if 'e' in str_from_base:
                idx_e = str_from_base.index('e')

                str_exp = str_from_base[idx_e + 1:]
            
                if str_exp[0] == '-':
                    if '.' not in str_from_base:
                        str_from_base = format(from_base, f'.{int(str_from_base[idx_e + 2:])}f')
                    else:
                        idx_point = str_from_base.index('.')

                        x = len(str_from_base[idx_point + 1:idx_e])
            
                        str_from_base = format(from_base, f'.{int(str_from_base[idx_e + 2:]) + x}f')
                else:
                    str_from_base = format(from_base, '.0f')

        int_part, dec_part = str_from_base.split('.')

            # check special cases
        if int(int_part) == 0 and int(dec_part) == 0:
                s = '1' if str(from_base)[0] == '-' else '0'
                e = '0' * len_e[prec]
                m = '0' * len_m[prec]
        else:
                # convert integer part and decimal part to binary
                bin_int_part = bin(int(int_part))[2:]
                
                dec_part_sn = float(dec_part) * pow(10, -len(str(dec_part))) # decimal part in scientific notation from 0001 -> 1e-4
              
                if int(int_part) >= 1:
                    bin_dec_part = dec_part_to_bin(dec_part_sn)
                else:
                    bin_dec_part = dec_part_to_bin_2(dec_part_sn, prec)
       
                bin_num = bin_int_part + '.' + bin_dec_part
                
                if bin_num[0] == '1':
                    idx_dot = bin_num.index('.')

                    moves = idx_dot - 1

                    bin_num = bin_num.replace('.', '')

                    shifted_bin_num = bin_num[0] + '.' +  bin_num[1:]
                else:
                    idx_dot = bin_num.index('.')
                    idx_one = bin_num.index('1')

                    moves = idx_one - idx_dot
             
                    shifted_bin_num = bin_num[moves + 1] + '.' +  bin_num[moves + 2:]

                    moves = -moves
    
                bias = {
                    16: 5,
                    32: 127,
                    64: 1023
                }

                # s(ign), e(xponent) and m(antissa)
                s = '1' if from_base < 0 else '0'
            
                e = moves

                e += bias[prec]
     
        if e <= 0:
                    # check denormal number, special case
                if -(len_m[prec] + bias[prec]) <= e - 127 < -bias[prec] - 1:
                        pass
                else:
                        print('ERROR: Maximum normal number representable 2^-126')

                        return False
                
        e = bin(e)[2:]
     
        if len(e) < len_e[prec]:
                    bit_to_add = len_e[prec] - len(e)

                    e = '0' * bit_to_add + e
        elif len(e) > len_e[prec]:
                    print('ERROR: Exponent too large')

                    return False
            
        m = shifted_bin_num[2:]
              
                # round mantissa
        if len(m) > len_m[prec]:
                    m = m[:len_m[prec] + 1]

                    if m[-1] == '0':
                        m = m[:-1]
                    else:
                        m = add_one(m[:-1])

        # fill with 0's the mantissa   
        m = m + ('0' * (len_m[prec] - len(m)))

        #res = s + '|' + e + '|' + m
        res += s + e + m
        
        return res

print(dec_to_ieee754(0.023, 32))