import pickle


expert = pickle.load( open( "expert_data.pkl", "rb" ) )

print (expert['actions'])
