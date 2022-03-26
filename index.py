from audioop import avg
from itertools import count
from re import I
from dataset import users, countries
from pprint import pprint

# -------------------------------------------------------------------------------------------- #
# !!!ALL CODE!!!
# users_wrong_password = []
# girls_drivers = []
# best_occupation = {}
# max_salary = 0
# vip_user = ''
# max_sum = 0
# avg_flights = 0
# sum_fly = 0
# sum_car = 0

# !!!!!!!!!!!!!
# for user in users:
#     for friends in user.get('friends', []):
#         if friends.get('cars'):
#             sum_car += 1
#             for fly in friends.get('flights', []):
#                 sum_fly += 1           
# avg_flights = sum_fly / sum_car
# !!!!!!!!!!!!!!!!

# print(round(avg_flights, 5))

# for user in users:
#     if user['password'].isdigit():
#         users_wrong_password.append({'name': user['name'] , 'mail': user['mail']})

#     for friends in user.get('friends', []):  
#         if friends['sex'] == 'F' and friends.get('cars'):
#             girls_drivers.append(friends['name'])

#     friend = user.get('friends', [])
#     for job in friend:                    
#         jobs = job['job']
#         if jobs['salary'] >= max_salary:
#             max_salary = jobs['salary']
#             if max_salary == jobs['salary']:
#                 best_occupation = {'occupation': jobs['occupation'], 'salary': jobs['salary']}               

#         salar = {
#             'salary': jobs['salary']
#         }
#         if sum(salar.values()) > max_sum:
#             max_sum = sum(salar.values())
#             vip_user = user['name']
# #  
#         if friends.get('cars'):
#             sum_car += 1
#             for fly in friends.get('flights', []):
#                 sum_fly += 1           
#             avg_flights = sum_fly / sum_car


# print('Люди с плохим паролем:', users_wrong_password)
# print('Друзья, которые имели машину(F пол):', girls_drivers)  
# print(f'Вот у кого самая большая зп: {best_occupation}')
# print(vip_user)
# print('avg кол-во путешествий среди друганов:', round(avg_flights, 5)) 
# -------------------------------------------------------------------------------------------- #
# pprint(users)

# Point 1 - done!!!
# users_wrong_password = []


# for user in users:
#     if user['password'].isdigit():
#         users_wrong_password.append({'name': user['name'] , 'mail': user['mail']})
#     friend = user.get('friends')

# print(users_wrong_password)
  

# Point 2 - done!!!
# girls_drivers = []

# for user in users:
#     for friends in user.get('friends'):  
#         if friend['sex'] == 'F' and friends.get('cars'):
#             girls_drivers.append(friends['name'])

# print(girls_drivers)
          

# Point 3 - done!!!
# best_occupation = {}
# max_salary = 0

# for user in users:
#     friend = user.get('friends', [])
#     for job in friend:                    
#         jobs = job['job']
#         if jobs['salary'] >= max_salary:
#             max_salary = jobs['salary']
#             if max_salary == jobs['salary']:
#                 best_occupation = {'occupation': jobs['occupation'], 'salary': jobs['salary']}               
# print(best_occupation)               


# Point 4 - done!!!
# vip_user = ''
# max_sum = 0




# for user in users:
#     friend = user.get('friends', [])
#     for job in friend:
#         job = job['job']
#         salar = {
#             'salary': job['salary']
#         }
#         if sum(salar.values()) > max_sum:
#             max_sum = sum(salar.values())
#             vip_user = user['name']

# print(vip_user)


# Point 5 - done!!!
# avg_flights = 0
# sum_fly = 0
# sum_car = 0


# for user in users:
#     for friends in user.get('friends', []):
#         if friends.get('cars'):
#             sum_car += 1
#             for fly in friends.get('flights', []):
#                 sum_fly += 1           
# avg_flights = sum_fly / sum_car

# print(round(avg_flights, 5))
        
# Point 6 - in process

# pprint(users)
for user in users:
    # pprint(user['name'])
    for friends in user.get('friends', []):
        for fly in friends.get('flights', []):
            if fly['country'] in countries:
                print(fly['country'], friends['name'])
                users.remove(user['name'])
            #     print(friends['name'])               
                
                
                
