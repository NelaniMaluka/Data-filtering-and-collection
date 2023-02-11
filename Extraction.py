# opens the data.txt file
# iterates over each line and splits each line with commas

with open ("Costomer Orders.txt") as f:
    for line in f:
        a = line.split(",")
        z = " "
        ItemsBought = []
        b = a[4:-1]
        
        #this loop collects the items bought and removes their reference numbers 
        for i in b:
            itemRef = i[-10:-1]
            item = i.replace( itemRef +"*", " ")
            ItemsBought.append(item)
        
        #this loop turns the ItemsBought from a list into a sting wich we can concatenate to the text-format later
        for item in ItemsBought:
            z +=  item + ","
        
        #This removes the comma from the last item in the sting(of items bought) and then adds the sting to the text-format    
        z = z.rstrip(",")
        textFormat = "Order Number: " + a[0] + ", Customer: " + a[2] + ", Items: {" + z + "}"

        print(textFormat)