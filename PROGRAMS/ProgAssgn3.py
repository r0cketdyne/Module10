patient_bloodtype = input("What is the donor's bloodtype\n")

if (patient_bloodtype == ('O+' or 'O-')):
    print("They're able to donate Double Red Cells and Whole Blood")
elif (patient_bloodtype == ('A+')):
    print("They're able to donate Plasma and Platelets")
elif (patient_bloodtype == ('A-')):
    print("They're able to donate Double Red Cells and Platelets")
elif (patient_bloodtype == ('B+')):
        print("They're able to donate Plasma and Platelets")
elif (patient_bloodtype == ('B-')):
    print("They're able to donate Double Red Cells and Platelets")
elif (patient_bloodtype == ('AB+' or "AB-")):
    print("They're able to donate plasma and platelets")
else :
    print("They don't have what we're looking for. Program Terminated.")
    
    
    
    