def kwargs_function(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}");
    

kwargs_function(firstname = "Ankit" , lastname = "Mishra" , gender = "male");
kwargs_function(firstname = "suhani" , lastname = "ahuja" );
kwargs_function(firstname = "Santosh" , lastname = "Baba" , gender = "male");
kwargs_function(firstname = "Nikhil"  , profession= "Student");

