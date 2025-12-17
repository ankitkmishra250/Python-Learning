from list1 import country
print(country); #['india', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'ukrane']

print(country.pop()); # ukrane
country.append("bhutan");
print(country); #['india', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan']
country.append("Srilanka");
print(country); #['india', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan', 'Srilanka']
country.remove("Srilanka");
print(country); #['india', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan', 'Srilanka']
country.insert(1,"Australia");
print(country); #['india', 'Australia', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan']
country.insert(2,["south Africa" , "Newzeland"]);
print(country); #['india', 'Australia', ['south Africa', 'Newzeland'], 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan']
country.remove( ['south Africa', 'Newzeland']);
print(country);#['india', 'Australia', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan']
print(country);

country_copy = country ;
print(country_copy is country); # True
country_copy2 = country.copy();
print(country_copy2); #['india', 'Australia', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan']
print(country_copy2 is country); # False

country_copy.append("France");
print(country_copy); #['india', 'Australia', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan', 'France']
print(country); #['india', 'Australia', 'bangladesh', 'afganishtan', 'russia', 'Italy', 'bhutan', 'France']

country_copy2.insert(3,"USA");
print(country_copy2);
print(country);
