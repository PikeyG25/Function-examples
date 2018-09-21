# Parker Gowans
# 9/18
# Change sorter

def change():
    #1 Get input from user find out how much change
    total_change = int(input("How much change do you have in your pocket: "))
    #2 Calculate total for q n d p
    q = total_change // 25
    whats_left = total_change % 25
    
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left
    #3 Display it back to user
    print("Quarter: ",q,"\nDimes: ",d,"\nNickels: ",n,"\nPennies: ",p)

##change()


def change2(total_change):
    #1 Get input from user find out how much change
    total_change = total_change
    #2 Calculate total for q n d p
    dol = total_change //100
    whats_left = total_change % 100
    q = total_change // 25
    whats_left = total_change % 25
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left
    return dol,q,d,n,p


    
    
total_change = int(input("How much change do you have in your pocket: "))
dol,q,d,n,p = change2(total_change)


#3 Display it back to user

print("$",dol,"Quarter: ",q,"\nDimes: ",d,"\nNickels: ",n,"\nPennies: ",p)
