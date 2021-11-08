from dataclasses import dataclass
from werkzeug.security import check_password_hash

@dataclass(frozen=True)
class User:
    email: str
    password: str
    
    def is_authenticated(self) -> bool:
        return True
    
    def is_active(self) -> bool:
        return True
    
    def is_anonymous(self) -> bool:
        return False
    
    def get_id(self) -> str:
        return self.email
    
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)