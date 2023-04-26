#!usr/home/student/mycode python3
sam_winchester = {
    'Nickname': ['Sam', 'Sammy', 'B---h', 'Moose'],
    'Species': ['Human', 'Ghost', 'Rabid'],
    'Gender': 'Male',
    'Occupation': ['Hunter', 'Witch-in-training',
                   ['Former Undergraduate',
                   'Former law school applicant']],
    'Family Members': {'Parents': {'Mother': 'Mary Winchester',
                       'Father': 'John Winchester'},
                       'Siblings': {'Younger Brother': 'Adam Milligan'}},
    }

sam_winchester['Family Members']['Siblings']['Older Brother'] = 'Dean Winchester'
sam_winchester.update({'Family Members': {'Siblings': {'Older Brother': 'Dean Winchester'}}})


print(sam_winchester)
print(sam_winchester.keys())

#choice= input("choose a key:\n> ")

#value= sam_winchester.get[choice, "No Value Found"]

