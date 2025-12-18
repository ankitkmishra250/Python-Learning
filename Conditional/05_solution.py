password = input(" Enter You Password ");
password_strength = None;

if len(password) == 5:
    password_strength = "Too Short";
elif len(password) == 7:
    password_strength = "Weak";
else:
    password_strength = "Strong Password";

print(password_strength);