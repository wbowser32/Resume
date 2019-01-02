alien_0 = {'color':'green','points':5,'x_position':0, 'y_position':25,'speed':'slow'}
alien_1 = {'color':'yellow','points':10,'x_position':0, 'y_position':15,'speed':'medium'}
alien_2 = {'color':'red','points':15,'x_position':0, 'y_position':5,'speed':'fast'}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

alien_color = (alien_0['color'])
new_points = alien_0['points']
print('You destroyed a '+alien_color+' alien! You earned '+str(new_points)+' points!')

print('\nOriginal x-position: ' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))
