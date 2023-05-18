def solve_dfs(x,y,target,curr_x,curr_y,path,visited):
    if(curr_x==target or curr_y==target):
        return path + [(curr_x,curr_y)]
    if (curr_x,curr_y) in visited:
        return None
    visited.add((curr_x,curr_y))
    operations=[
        ('Fill X',x,curr_y),
        ('Fill Y',curr_x,y),
        ('Empty X',0,curr_y),
        ('Empty Y',curr_x,0),
        ('Pour X into Y',max(0,curr_y+curr_x-y),min(y,curr_x+curr_y)),
        ('Pour Y into X',min(x,curr_x+curr_y),max(0,curr_x+curr_y-y))
        ]
    for operation,next_x,next_y in operations:
        result=solve_dfs(x,y,target,next_x,next_y,path+[(curr_x,curr_y,operation)],visited)
        if result:
            return result
    return None

dfs_sol=solve_dfs(4,3,2,0,0,[],set())
if dfs_sol:
    print("\n DFS Solution:\n")
    for state in dfs_sol:
        print(state)

