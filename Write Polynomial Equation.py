import math
import cmath
from fractions import Fraction

unicode_characters_for_exponents={0:8304,1:185,2:178,3:179,4:8308,5:8309,6:8310,7:8311,8:8312,9:8313}

#Get zeroes and create list of zeroes.
def get_zeroes():
    global zero_list
    zeroes=input('Enter zeroes separated by spaces. For complex zeroes, attach j at the end of the imaginary part and omit parentheses around a fraction. For square roots, use sqrt(number).:')
    
    #Zeroes is one string.  Convert it to a list of strings.
    zero_list=zeroes.split()
    print ('zeroes are',zero_list)
    return zero_list

def two_parts(str_zero):                                                            
                                                                                          
    #Is zero in two parts?  If so, identify the two parts.                                  
    #If not, assign '0' to the first part and the original zero to the second part.         
    global first_part, sec_part                                                             
    add_sign=str_zero.find('+')                                                     
    sub_sign=str_zero.find('-',1)                                                       
                                                                                           
    #There is an addition sign between them.                                                
    if add_sign!=-1:
        first_part=str_zero[:add_sign]
        sec_part=str_zero[add_sign:]
    #There is a subtraction sign between them.               
    elif add_sign==-1 and sub_sign!=-1:
        first_part=str_zero[:sub_sign]
        sec_part=str_zero[sub_sign:]
    #The zero is not in two parts.
    #Turn it into two parts with 0 as the first part.    
    elif add_sign==-1 and sub_sign==-1:
        first_part='0'
        sec_part=str_zero
        #Each part should have a sign with it.  If the zero is only one part and
        #there is no negative sign, then a positive sign should be given to it.
        if sec_part.find('-')==-1:
            sec_part='+'+sec_part
    #Each part should have a sign with it.
    if first_part.find('-')==-1:
        first_part='+'+first_part
    
    return first_part, sec_part
    
    
def eval_sq_rt():
    global rt_par,new_zero_part
    
    #Isolate argument of the sqrt.
    left_par=zero_part.find('(')
    rt_par=zero_part.find(')')
    sq_rt_arg=zero_part[left_par+1:rt_par]

    #Check for fraction bar in the square root argument.
    #Evaluate fraction first.
    if sq_rt_arg.find('/')!=-1:
        frctn=Fraction(sq_rt_arg).limit_denominator()
        num_for_sq_rt_arg=float(frctn.numerator)/float(frctn.denominator)
    else:
        num_for_sq_rt_arg=float(sq_rt_arg)
    num_for_sq_rt=math.sqrt(num_for_sq_rt_arg)
        
    #Check for number in front of the square root.
    #Multiply the number and the square root.
    zero_part_stripped=zero_part.strip('-')
    zero_part_stripped=zero_part.strip('+')
    zero_part_stripped=zero_part.rstrip('j')
    coef_of_sq_rt=zero_part_stripped[1:zero_part_stripped.find('sqrt')]
    if coef_of_sq_rt=='':
        coef_of_sq_rt=1
    zero_so_far=float(coef_of_sq_rt)*num_for_sq_rt
        
    #Check for number under the square root.
    #Divide these two.
    if zero_part.find('/',rt_par)!=-1:
        zero_so_far=zero_so_far/float(zero_part[zero_part.find('/',rt_par)+1])

    #Replace the part of the zero after the sign
    #with the floating point equivalent zero_so_far.
    if zero_part.find('j')!=-1:
        new_zero_part=zero_part.replace(zero_part[1:zero_part.find('j')],str(zero_so_far))
    elif zero_part.find('j')==-1:
        new_zero_part=zero_part.replace(zero_part[1:],str(zero_so_far))
    
    return new_zero_part
    
    
        
def find_and_eval_fraction(zero_part):
    global new_zero_part
    
    zero_part_stripped=zero_part.strip('-')
    zero_part_stripped=zero_part.strip('+')
    zero_part_stripped=zero_part.rstrip('j')
    frctn=Fraction(zero_part_stripped).limit_denominator()
    zero_so_far=float(frctn.numerator)/float(frctn.denominator)
    
    #Replace the part of the zero after the sign
    #with the floating point equivalent zero_so_far.
    if zero_part.find('j')!=-1 and zero_part.find('+')!=-1:
        new_zero_part=zero_part.replace(zero_part[1:zero_part.find('j')],str(zero_so_far))
        
    elif zero_part.find('j')!=-1 and zero_part.find('-')!=-1:
        new_zero_part=zero_part.replace(zero_part[0:zero_part.find('j')],str(zero_so_far))
                                        
    elif zero_part.find('j')==-1:
        new_zero_part=zero_part.replace(zero_part[0:],str(zero_so_far))
        
    return new_zero_part          

def zero_part_list():
        
    #Store the floating point equivalent of the zero_part
    if complex_zero==-1:
        list_of_zero_parts.append(float(new_zero_part))

    #It is a complex zero.  Store the string.
    elif complex_zero!=-1:  
        list_of_zero_parts.append(new_zero_part)
    print('In zero_part_list(); list_of_zero_parts is',list_of_zero_parts)      
    return list_of_zero_parts

def convert_each_zero_string_to_float(zero_list):
    #Create empty list for converted zeroes.
    global complex_zero,zero_part,new_zero,zerolst,str_zero,list_of_zero_parts
    zerolst=[]
    for i in range(len(zero_list)):
        str_zero=zero_list[i]
        two_parts(str_zero)
        complex_zero=sec_part.find('j')
        list_of_zero_parts=[]
        for name in (first_part,sec_part):
            zero_part=name
            print('The zero is',str_zero,'.  The zero_part is:',zero_part,' and complex_zero is',complex_zero)
            
            #Check for a square root in the zero part.
            radical=zero_part.find('sqrt')
            if radical!=-1:
                eval_sq_rt()
                zero_part_list()
            
            #Check for a fraction in the zero part.
            fraction_bar=zero_part.find('/')    
            if fraction_bar!=-1 and radical==-1:
                print('going to find_and_eval_fraction')
                find_and_eval_fraction(zero_part)
                zero_part_list()
            
            #The zero part has no square root and no fraction bar.    
            elif radical==-1 and fraction_bar==-1 and complex_zero==-1:
                list_of_zero_parts.append(float(zero_part))
                print('at first elif and list of zero parts is',list_of_zero_parts)
                
            elif radical==-1 and fraction_bar==-1 and complex_zero!=-1:
                list_of_zero_parts.append(zero_part)
                print('at second elif and list of zero parts is',list_of_zero_parts)
    
        if complex_zero!=-1:
            new_zero=complex(list_of_zero_parts[0]+list_of_zero_parts[1])           
        else:
            new_zero=list_of_zero_parts[0]+list_of_zero_parts[1]
        zerolst.append(new_zero)

    print('list of floating point zeroes is',zerolst)
    return new_zero, zerolst

def calculate_coefficients():
    global clist
    coefficients=[1]
    coef1=(-1)*sum(zerolst)
    coefficients.append(coef1.real)
       
    #Now the coefficient list contains the leading coefficient and the coefficient of the next term.
    #Create a variable to hold the list of numbers used to calculate the current coefficient. 
    temp=zerolst
    for k in range(len(zerolst)-1): 
        newlst=[]
        
        #newlst will be filled with the numbers to be summed for the new coefficient. 
        for i in range(len(zerolst)-1):
            A=zerolst[i]*sum(temp[i+1:])
            newlst.append(A)
        temp=newlst
        newcoef=((-1)**k)*sum(temp)
        #Calculate the new coefficient from the temporary list of numbers and put it into the coefficients list.
        coefficients.append(newcoef.real)

    #Convert decimal coefficients to fractions.
    clist=[]
    from fractions import Fraction
    for coef in coefficients:
        coefstr=str(coef)
        c=Fraction(coefstr).limit_denominator()
        #clist.append(str(c))
        clist.append(c)
    #Coefficient list is ordered from leading coefficient to the constant term.
    print ('Coefficient list is ',clist)
    return clist

#Make a list of exponents to be paired with the coefficients.
def make_exp_list():
    global explst
    explst=[]
    for i in range(len(zerolst)+1):
        explst.append(i)
    explst.reverse()


#Make a list of tuples that pairs exponents with coefficients.

def match_exp_coef():
    global tuplst
    tuplst=[]
    for k in range(len(zerolst)+1):
        tempair=(clist[k],explst[k])
        tuplst.append(tempair)
    return tuplst

#Print equation.
def print_equation():
    s=""
    for i in range(len(tuplst)):
        term="+(%s)x^%d"%tuplst[i]
        s+=term
    print (s)


#Pretty Print the equation."
def print_equation2():
    for i in range(len(clist)):
        term="+(%s)"%clist[i]+"x"+explst[i]
        s+=term
    print(s)

get_zeroes()
convert_each_zero_string_to_float(zero_list)
calculate_coefficients()
make_exp_list()
#match_exp_coef()
#print_equation()

class Term:
    def __init__(self,variable,exponent):
        self.variable=variable
        self.exponent=exponent
        char=unicode_characters_for_exponents[self.exponent]
        self.term=self.variable+chr(char)

term_list=[]
for i in explst:
    if i>1:
        t1=Term('x',i)
        
        term_list.append(t1.term)
        i=i-1
term_list.append('x')
term_list.append('')
print('term_list is',term_list)
print('clist is',clist)
#Print equation formed from pairing coefficients in the clist with terms in term list.
s=''
for i in range(len(term_list)):
    term=str(clist[i])+term_list[i]
    if term[0]!='-':
        term='+'+term
    s+=term
print(s)
        
