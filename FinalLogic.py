import random
def start():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2

def get_current_state(mat):
    #Check if 2048 is present anywhere in the matrix
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON"
            
    #Check if 0 is present anywhere in the matrix
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "GAME NOT OVER"
            
    #Check if mat[i][j] is equal to mat[i][j+1] or mat[i+1][j]
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return 'GAME NOT OVER'
    #Check for column
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"
    #Check for row
    for i in range(3):
        if mat[3][i]==mat[3][i+1]:
            return 'GAME NOT OVER'
        
    return "LOST"

# Adding Compress Function
def compress_mat(mat):
    new_mat=[]
    changed=False
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                pos+=1
                if j!=pos:
                    changed=True
    return new_mat,changed

# Adding merge function
def merge_mat(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                changed=True
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
    return mat,changed

# Adding reverse matrix function
def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat
# Adding transpose matrix function
def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
# Adding all the possible moves
def move_left(grid):
    new_grid,changed1=compress_mat(grid)
    new_grid,changed2=merge_mat(new_grid)
    changed=changed1 or changed2
    final_grid,temp=compress_mat(new_grid)
    return final_grid,changed

def move_right(grid):
    reversed_grid=reverse(grid)
    new_grid,changed1=compress_mat(reversed_grid)
    new_grid,changed2=merge_mat(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress_mat(new_grid)
    final_grid=reverse(new_grid)
    return final_grid,changed

def move_up(grid):
    transpose_grid=transpose(grid)
    new_grid,changed1=compress_mat(transpose_grid)
    new_grid,changed2=merge_mat(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress_mat(new_grid)
    final_grid=transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transpose_grid=transpose(grid)
    reverse_grid=reverse(transpose_grid)
    new_grid,changed1=compress_mat(reverse_grid)
    new_grid,changed2=merge_mat(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress_mat(new_grid)
    new_grid=reverse(new_grid)
    final_grid=transpose(new_grid)
    return final_grid,changed