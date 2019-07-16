# try:
#     print(100/1)
# except:
#     print("Inside Exception Handler")
# print(Hello I am after exception)

a= {'Name':'khizra'}
try:
    with open('data.csv', 'w'):
        pass
    print('after open file')
    print(a['Name'])
except KeyError:
    print('This key does not exists in this ADT')
except FileNotFoundError as e:
    print(e)
print('file does not exist')
# except Exception:
#     print('this is not an unknown exception')
finally:
    print('Im finally Block!!')
print('ending')