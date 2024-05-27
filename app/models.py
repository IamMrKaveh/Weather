from django.db import models

class Search:
  city = ""
  temperature= ""
  description= ""
  year = ""
  month = ""
  day = ""
  hour = ""
  minute = ""
  second = ""

class User:
  username = ""
  password = ""
  gmail = ""
  
  def __init__(this, _username = "", _password = "", _gmail = ""):
    this.username = _username
    this.password = _password
    this.gmail = _gmail

  def read_users(this):
    user_list = {}
  
    username_list = open("app/Database/users/usernames.txt", "r").read().split("-")
    passwords_list = open("app/Database/users/passwords.txt", "r").read().split("-")  
  
    for number in range(username_list.__len__()):
      user_list[f"{username_list[number]}"] = f"{passwords_list[number]}"  
    
    return user_list

  def exist_user(this, username = ""):
    user_list = User().read_users()
  
    if username in user_list:
      return True
    else:
      return False
  