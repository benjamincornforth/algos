def solution(skills):
    from collections import deque
    
    n = len(skills)
    results = [0] * n
    rounds = 0
    
    players = deque([(i, skills[i]) for i in range(n)])
    
    while len(players) > 1:
        rounds += 1
        next_round = deque()
        
        while players:
            p1 = players.popleft()
            p2 = players.popleft()
            
            if p1[1] > p2[1]:
                results[p2[0]] = rounds
                next_round.append(p1)
            else:
                results[p1[0]] = rounds
                next_round.append(p2)
        
        players = next_round
    
    results[players[0][0]] = rounds
    return results

# Example usage:
skills = [4, 2, 7, 3, 1, 8, 6, 5]
print(solution(skills))  # Output: [2, 1, 3, 1, 1, 3, 2, 1]
skills = [4, 2, 1, 3]
print(solution(skills))  # Output: [2, 1, 1, 2]
