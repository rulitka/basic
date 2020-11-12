def UFO(N, data, octal):
    new = []
    if octal == True: 
        for i in data:
            int_value = str(i)
            new_data = int(int_value, base = 8)
            new.append(new_data)
        return new
            
    if octal == False:
        for i in data:
            int_value = str(i)
            new_data = int(int_value, base = 16)
            new.append(new_data)
        return new
