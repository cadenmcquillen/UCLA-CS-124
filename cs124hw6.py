import math
sigma1 = 1.05
sigma2 = 0.95
pi1 = .6
pi2 = .4
u1 = 5.6
u2 = 4.5


with open("/Users/Caden/Downloads/ml_genomics_hw6_data.txt") as f:
    x_list = []
    for line in f:
        line = line.split()
        for i in line:
            x_list.append(float(i))


#x_list = (1,2,3,3,5) #read in X values here
def f_of_x1(x,sigma, u):
    constant = 1/math.sqrt((2*(math.pi)*(sigma**2)))
    exponent = -((x-u)**2)/(2*(sigma**2))
    final_val = constant*(math.exp(exponent))
    return final_val



def a_pi1(x,pi1,sigma1, u1,pi2,sigma2, u2):
    numerator = pi1*f_of_x1(x,sigma1,u1)

    temp1 = pi1*f_of_x1(x,sigma1,u1)
    temp2 = pi2*f_of_x1(x,sigma2,u2)
    denominator = temp1+temp2
    final = numerator/denominator
    return final

def new_p1(pi1,sigma1,u1,p2,sigma2,u2):
    total = 0
    n = len(x_list)
    for i in x_list:
        temp = a_pi1(i,pi1,sigma1, u1,p2,sigma2,u2)
        total += temp

    return total/n


def new_u1(pi1,sigma1,u1,pi2,sigma2,u2):
    num_total = 0
    denom_total = 0
    for i in x_list:
        temp = a_pi1(i,pi1,sigma1,u1,pi2,sigma2,u2)*i
        num_total += temp
    for i in x_list:
        temp = a_pi1(i,pi1,sigma1,u1,pi2,sigma2,u2)
        denom_total += temp
    return num_total/denom_total

def new_sigma1(updated_u,pi1,sigma1,u1,pi2,sigma2,u2):
    num_total = 0
    denom_total = 0
    for i in x_list:
        temp = a_pi1(i,pi1,sigma1,u1,pi2,sigma2,u2)
        denom_total += temp
    for i in x_list:
        temp = a_pi1(i,pi1,sigma1,u1,pi2,sigma2,u2)*((i-updated_u)**2)
        num_total += temp
    return math.sqrt(num_total/denom_total)

def run_GMM1():
    current_pi1 = pi1
    current_sigma1 = sigma1
    current_u1 = u1

    current_pi2 = pi2
    current_sigma2 = sigma2
    current_u2 = u2
    while(current_pi1>0):
        temp_new_u1 = new_u1(current_pi1,current_sigma1,current_u1,current_pi2,current_sigma2,current_u2)
        temp_new_u2 = new_u1(current_pi2, current_sigma2, current_u2, current_pi1, current_sigma1, current_u1)
        temp_new_sigma1 = new_sigma1(temp_new_u1,current_pi1,current_sigma1,current_u1,current_pi2,current_sigma2,current_u2)
        temp_new_sigma2 = new_sigma1(temp_new_u2, current_pi2, current_sigma2, current_u2, current_pi1, current_sigma1, current_u1)
        temp_new_pi1 = new_p1(current_pi1,current_sigma1, current_u1,current_pi2,current_sigma2,current_u2)
        temp_new_pi2 = new_p1(current_pi2, current_sigma2, current_u2,current_pi1,current_sigma1,current_u1)

        if(abs(current_pi1-temp_new_pi1) < 0.000001):
            break

        current_u1 = temp_new_u1
        current_sigma1 = temp_new_sigma1
        current_pi1 = temp_new_pi1
        current_u2 = temp_new_u2
        current_sigma2 = temp_new_sigma2
        current_pi2 = temp_new_pi2

    return temp_new_pi1,temp_new_pi2


get_pi1 = run_GMM1()

print(get_pi1)