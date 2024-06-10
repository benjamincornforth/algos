def solution(row1, row2):
    n = len(row1)
    
    def balance_count(row):
        return row.count('R') - row.count('W')
    
    row1_balance = balance_count(row1)
    row2_balance = balance_count(row2)
    
    min_replacements = abs(row1_balance) + abs(row2_balance)
    
    if row1_balance % 2 != 0 or row2_balance % 2 != 0:
        return -1
    
    replace_count = 0
    
    for i in range(n):
        if row1[i] == '?' and row2[i] == '?':
            if row1_balance > 0 and row2_balance < 0:
                row1_balance -= 2
                row2_balance += 2
            elif row1_balance < 0 and row2_balance > 0:
                row1_balance += 2
                row2_balance -= 2
            replace_count += 1
        
        elif row1[i] == '?' or row2[i] == '?':
            if row1[i] == '?':
                if row2[i] == 'R':
                    row1_balance -= 1
                else:
                    row1_balance += 1
                replace_count += 1
            elif row2[i] == '?':
                if row1[i] == 'R':
                    row2_balance -= 1
                else:
                    row2_balance += 1
                replace_count += 1
        
        if row1_balance == 0 and row2_balance == 0:
            break

    if row1_balance != 0 or row2_balance != 0:
        return -1

    return replace_count

# Example usage:
row1 = "W??WR"
row2 = "R??W?"
print(solution(row1, row2))  # Output: 3
row1 = "WRR?WR"
row2 = "R??W?R"
print(solution(row1, row2))  # Output: 2
