student_data={'id1':
              {'name':['Sara'],
               'class':['V'],
               'subject':['english,math,science']
               },
        'id2':
            {'name':['David'],
               'class':['V'],
               'subject':['english,math,science']
               },
        'id2':
            {'name':['Sara'],
               'class':['V'],
               'subject':['english,math,science']
               },
        'id2':
            {'name':['Surya'],
               'class':['V'],
               'subject':['english,math,science']
               },
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]= value
print(result)