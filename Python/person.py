def build_person(first_name, last_name, middle_name='', age='', instrument=''):
	"""Return a full name, neatly formatted."""
	person = {'first': first_name, 'last': last_name}	
	if age:
		person['age'] = age
	else:
		person['age']= 'unknown'
	if middle_name:
		person = first_name + ' ' + middle_name + ' ' +last_name+ ', age:'+str(age)+'\n Instrument: '+instrument
		
	else:
		person = first_name + ' '+ last_name+', age:'+str(age)+'\n Instrument: '+ instrument
	return person.title()
	
musician = build_person('jimi', 'hendrix', age=27, instrument='guitar')
print(musician)

musician = build_person('johnny', 'hooker', 'lee', age=27, instrument='guitar')
print(musician)
		
