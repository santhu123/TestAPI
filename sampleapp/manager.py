from django.contrib.auth.base_user import BaseUserManager 

class CustomUserManager(BaseUserManager):
    use_in_migrations=True 
    def _create_user(self,email,password,**extrafields):
        if not email:
            raise ValueError("the Email must be set")
        email=self.normalize_email(email)
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_user(self,email,name,contact,password=None):
        return self._create_user(email,password,name=name,contact=contact)