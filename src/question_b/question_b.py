#write functions here, don't add input('') statements here!

#Part 2.1
def get_miles_per_hour(km,mins):
    
    kmpm = float(km) / float(mins)
    kmph = kmpm * 60
    mph = kmph * 0.621371
        
    return mph
