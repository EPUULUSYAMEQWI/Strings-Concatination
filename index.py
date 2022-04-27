y=[z*5 for z in x]
print(y)
def divisible_by_seven():
    value =range(100,201)
    my_list =[]
    for i in value:
        if i%7==0:
            my_list.append(i)
    #print(my_list)
    return my_list
print(divisible_by_seven())
def divisible_by_three(n):
    values= range(1,n+1)
    for nums in values:
        if n%3==0:
            print(nums)
divisible_by_three(20)
student =[{'name':"tessa",'age':20},{'name':"tessa",'age':20},{'name':"tessa",'age':20},{'name':"tessa",'age':20}]
for i in student:
    name =i['name']
    age =i['age']
    birthyear = 2022 - age
    print(f"Hello ,{ name} you were born in the year {birthyear}")
x =[[1,2],[3,4],[5,6]]
y= [w for sublist in x for w in sublist]
print(y)
def smallest(int_list):
    int_list.sort()
    min_value = int_list[0]
    return min_value
    #return min(int_list)
   
    # Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates
print(smallest([8,2,4,1,9,54]))
def remove_dups(x):
    x = set(x)
    return list(x)
print(remove_dups([1,2,3,1,1,1,2,2]))

