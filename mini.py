name = input("enter your name")
c=input("enter your class")
section=input("enter your section")
school=input("enter your school")
techer=input("enter your teacher name")
date = str(input("enter date"))
subject=input("enter subject")
dateofleave=input("enter date of leave")
reason=input("enter your reason")

letter=f'''
Date: {date}
To,
the {techer}
{school}
My self {name} from {section} studying {c}
due to {reason} grant me a leave on {dateofleave}
{name} from {c},{school}
Thankyou sir/madam
yours sincerely,
    {name}
'''
print(letter)