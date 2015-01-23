# assignment 1 solution

def seconds_difference(x1,x2):
    h1_str,m1_str,s1_str = str.split(x1,":")
    h2_str,m2_str,s2_str = str.split(x2,":")
    h1,m1,s1 = int(h1_str),int(m1_str),int(s1_str)
    h2,m2,s2 = int(h2_str),int(m2_str),int(s2_str)
    total_sec_1 = h1*3600 + m1*60 + s1
    total_sec_2 = h2*3600 + m2*60 + s2
    return abs(total_sec_2 - total_sec_1)

# testing out the assignment
print( seconds_difference("23:00:1","24:00:00") )
    
print( seconds_difference("23:00:1","23:00:00") )
    
    