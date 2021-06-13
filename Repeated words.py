##To check number of repeated words
def most_frequent(my_dict):
    a=dict()
    for key in my_dict:
        if key not in a:
            a[key]=1
        else:
            a[key]+=1
    return a
output=most_frequent("mississippi")
print(output)
