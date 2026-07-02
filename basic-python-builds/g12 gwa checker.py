### Grade 12 NEU First Semester Honor Checker
## If grade_subject > 88 and/or GWA > 92 and/or 
## has OSD kaso, no Honor
## For MIDTERM USE ONLY... YET

print("Do you have any OSD cases?")
print("1 --> Received a warning \n2 --> Uniform/Haircut Violations Only \n3 --> Undergo a Hearing / Suspended")
osd_case = int(input("Input Here:"))

if osd_case == 3:
    print("Not Qualified for Honors Anymore")
    raise SystemExit
    
print("What term are you in right now?")
print("1 --> Midterms")
print("2 --> Finals")
what_term = int(input("Input Here: "))

if what_term == 1:
    
    print("First Semester, Midterms")
    first_mid = [
    int(input("HOPE III: ")),
    int(input("Intro to Philo: ")),
    int(input("MIL: ")),
    int(input("UCSP: ")),
    int(input("RDL 2: ")),
    int(input("FPL: ")),
    int(input("General Bio 1: ")),
    int(input("General Physics 1: ")),
    int(input("Work Immersion: "))
]
    midterms_overall_gwa = sum(first_mid) / len(first_mid)
    
    if any(grade < 88 for grade in first_mid):
        print("\n\tNot Qualified for Honors Anymore")
        print("\n\tMidterms GWA:", midterms_overall_gwa)
    else:
        print("\n\tStill Qualified for Honors")
        print("\n\tMidterms GWA:", midterms_overall_gwa)
        
if what_term == 2:
    
    print("First Semester, Finals")
    first_final = [
        int(input("HOPE III: ")),
        int(input("Intro to Philo: ")),
        int(input("MIL: ")),
        int(input("UCSP: ")),
        int(input("RDL 2: ")),
        int(input("FPL: ")),
        int(input("General Bio 1: ")),
        int(input("General Physics 1: ")),
        int(input("Work Immersion: "))
    ]
    
    finals_overall_gwa = sum(first_final) / len(first_final)
    
    if any(grade < 88 for grade in first_final) or finals_overall_gwa < 92:
        print("\n\tNot Qualified for Honors")
        print("\n\tFinals GWA:", finals_overall_gwa)

    else:
        print("\n\tStill Qualified for Honors")
        print("\n\tFinals GWA:", finals_overall_gwa)
        print("\n\tOverall GWA:", (finals_overall_gwa + midterms_overall_gwa) / 2)
