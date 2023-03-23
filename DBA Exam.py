list = [5,1,4,6,7,3,5,7,3]
duplicates = []
for value in list:
    if list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print("\nExam 1: duplicate set of number: " + str(duplicates))
print() 
print("Exam 2: ")
for x in range(1,7):
    for y in range (1, x+1):
        print(x,end=" ")
    print() 
print("\nExam 3: ") 
NHM = int(input("Enter number of newly hired males: "))
NHF = int(input("Enter number of newly hired Female: "))
PPM = int(input("Enter number of Permanent position male:"))
PPF = int(input("Enter number of Permanent position female:"))
RM = int(input("Enter number of resigned male:"))
RF = int(input("Enter number of resigned female:"))

TNOE = NHM + NHF
TNOPE = PPM + PPF
TNORE = RM + RF


print("\nNumber of hired employee: " + str(TNOE))
Mpercent = (NHM / TNOE)*100
print("Hired male: " + str(round(Mpercent,2)))
Fpercent = (NHF / TNOE)*100
print("Hired female: " + str(round(Fpercent,2)))

print("\nNumber of Permanent employee: " + str(TNOPE))
PMpercent = (PPM / TNOPE)*100
print("Permanent male: " + str(round(PMpercent,2)))
PFpercent = (PPF / TNOPE)*100
print("Permanent Female: " + str(round(PFpercent,2)))

print("\nNumber of Resigned employee: " + str(TNORE))
RMpercent = (RM / TNORE)*100
print("Resigned Male: " + str(round(PMpercent,2)))
RFpercent = (RF / TNORE)*100
print("Resigned Female: " + str(round(PFpercent,2)))

TNE = TNOE + TNOPE + TNORE
print("\nNumber of Total employee you had : " + str(TNE))
RE = RM + RF
print("which " + str(round((RE/TNE)*100,2)) + " Resigned")
TF = NHF + PPF + RF 
print("\nNumber of Total Female: " + str(TF)) 
TM = NHM + PPM + RM 
print("\nNumber of Total Male: " + str(TM)) 

print("Made by truly yours JULIAN MARCHAN \n Associate Software Engineer")

