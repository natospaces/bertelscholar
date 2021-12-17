xpoints = [2,5,-4,-7,8]
ypoints = [-2,6,-4,1,14]

list_points = [(2,-2), (5,6), (-4,-4), (-7, 1), (8,14)]
slope = 1.2
intercept = 2
total_absolute_errors = 0

#calculating Mean Absolute Error given list_points
for point in list_points:
    print(f'absolute differences {abs(((slope * point[0])+intercept)-point[1])}')
    total_absolute_errors = total_absolute_errors + abs(((slope * point[0])+intercept)-point[1])
    
mae = total_absolute_errors/len(list_points)
print(f'total_absolute_errors {total_absolute_errors}')
print(mae)

total_squared_errors = 0
#calculating Mean Square Error given list_points
for point in list_points:
    print(f'squared differences {abs(((slope * point[0])+intercept)-point[1])**2}')    
    total_squared_errors = total_squared_errors + abs(((slope * point[0])+intercept)-point[1])**2
    
mse = total_squared_errors/(len(list_points) )
print(f'total_squared_errors {total_squared_errors}')
print(mse)
