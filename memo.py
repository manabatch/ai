def solve_memo(x,y,target,curr_x,curr_y,memo):
    if(curr_x==target or curr_y==target):
        return [(curr_x,curr_y)]
    if (curr_x,curr_y) in memo:
        return None
    memo.add((curr_x,curr_y))
    operations=[
        ('Fill X',x,curr_y),
        ('Fill Y',curr_x,y),
        ('Empty X',0,curr_y),
        ('Empty Y',curr_x,0),
        ('Pour X into Y',max(0,curr_y+curr_x-y),min(y,curr_x+curr_y)),
        ('Pour Y into X',min(x,curr_x+curr_y),max(0,curr_x+curr_y-y))
        ]
    for operation,next_x,next_y in operations:
        result=solve_memo(x,y,target,next_x,next_y,memo)
        if result:
            return result+[(curr_x,curr_y,operation)]
    return None

memo_sol=solve_memo(4,3,2,0,0,set())
if memo_sol:
    print("\n MEMO Solution:\n")
    for state in memo_sol:
        print(state)
