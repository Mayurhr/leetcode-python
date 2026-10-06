class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False

        for i in range(1,len(password)):
            if password[i]== password[i-1]:
                return False

        has_upper=any(c.islower() for c in password)
        has_lower=any(c.isupper() for c in password)
        has_digit=any(c.isdigit() for c in password)

        sp=set("!@#$%^&*()-+")
        has_special=any(c in sp for c in password)

        return has_upper and has_lower and has_digit and has_special