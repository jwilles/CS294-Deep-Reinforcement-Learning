import pickle


expert = pickle.load( open( "expert_data.pkl", "rb" ) )

#print (expert['actions'])


print (expert['observations'][0][0])
print (len(expert['observations'][0]))
print (expert['actions'][0])
print (len(expert['actions'][0][0]))

