def upper(matrix, row, col): 
    for i in range(0, row): 
        for j in range(0, col):   
            if (i > j): 
                print("0", end = " ");     
            else: 
                print(matrix[i][j],  
                       end = " " );         
        print(" "); 
  
# Driver Code 
matrix = [[3, 2, 9, 8, 9],  
          [0,-1, 6, 7, 3],  
          [0, 0, 2, 9, 9],
          [0, 0, 0, 5, 2],
          [0, 0, 0, 0,-1]]
          
row = 5; 
col = 5; 
      
      
print("Upper triangular matrix: "); 
upper(matrix, row, col)