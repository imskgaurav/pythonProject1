class User:
     def __init__(self, user_email, name, password, current_job_title):
          self.email= user_email
          self.name= name
          self.password= password
          self.current_job_title= current_job_title
  
     def get_user_info(self):
           print(f"User {self.name} is currently working as {self.current_job_title} on.")
     
     def change_jobTitle(self, new_job_title):
          self.current_job_title = new_job_title
          
          
               
           
           
first_user = User("test@click.com", "First User", "one", "Devops")
first_user.get_user_info()
first_user.change_jobTitle("Trainer")
first_user.get_user_info()


     
           
   
          
          
    