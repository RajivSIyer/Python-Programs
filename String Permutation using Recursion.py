def permute(s):

    print('String= ',s)

    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):

            print('i= ', i, 'let= ', let, 's= ', s)
        
            comblist = permute(s[:i] + s[i+1:])
            print('Combinational List= ', comblist)
            # For every permutation resulting from Step 2 and 3 described above
            for perm in comblist:
                
                # Add it to output
                out += [let + perm]
                print('Perm= ', perm, 'Let= ', let, 'Out= ', let+perm)

    return out

print('\n', permute('abc'))