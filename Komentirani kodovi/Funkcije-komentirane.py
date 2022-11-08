#Uklanja duple zapise vremena
#Sa svakim poslanim podatkom uvijek se ponovno ispišu vremena, tj. svaki microbit zabilježi vrijeme, no vremena su ista kada svi šalju u isto vrijeme. Stoga ova funkcija služi kako bi se rješila tog ponavljanja.
def my_function(x):
  return list(dict.fromkeys(x))
vremena = my_function(vremena)
