import pickle

Gachon_students_dict = {"Achieng" : "20170041" , "Awino" : "20160001" , "Auma" : "20170052"}

pickle_out = open("dict.pickle", "wb")

pickle.dump(Gachon_students_dict, pickle_out)

pickle_out.close()

pickle_in = open("dict.pickle", "rb")

example_dict = pickle.load (pickle_in)

print(Gachon_students_dict)