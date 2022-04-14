current_x = 2
current_y = 2
epsilon = 10**-5
stopping = 10**-8
differnce = 1
max_iters = 10**7
iters = 0
def function(x,y):
    value = 9 - 6*x + x**2 +100*(y**2) + (200*x**2)*y + 100*(x**4)
    return value

def gradient(x,y):
    new_x = -6 +(2*x)+(400*x*y)+(400*(x**3))
    new_y = (200*y)+(200*(x**2))
    return(new_x,new_y)

while differnce > stopping and iters < max_iters:
    gradx,grady = gradient(current_x,current_y)
    prev_x = current_x
    prev_y = current_y
    current_x = current_x - epsilon * gradx
    current_y = current_y - epsilon * grady
    old_value = function(prev_x,prev_y)
    new_value = function(current_x,current_y)
    differnce = abs(old_value-new_value)
    iters = iters + 1
    
    print(iters)


print("The local minimum occurs at", current_x,current_y)
print(new_value)
