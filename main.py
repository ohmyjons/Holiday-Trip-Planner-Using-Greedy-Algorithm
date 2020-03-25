from daftarkota import daftarkota
from greedy import Greedy
def main():
	
	print('============================================')
	print('This program shows cities that can be visited \nSo by using this program you can get some cities for stop by \nor multiply your destination for your trip\n')
	print('-------------------------------------------')
	print(' \non your family trip and help you to get the list of cities that have shortest distance between them.\n')
	print('============================================')
	print('Here the list of the cities that we provide:\n')    
	
	#List Kota
	kota = set(['Cilegon', 'Tangerang', 'Jakarta', 'Bogor',
		'Cikampek', 'Bekasi', 'Bandung', 'Cirebon', 'Cimahi', 'Cianjur', 'Garut', 'Sumedang', 'Subang', 'Tasikmalaya',	
		'Purwokerto', 'Magelang', 'Semarang', 'Jogja', 'Surabaya',
		'Malang'])

	#adjacency list city in Java
	jarak = {		
        'Cilegon' : {'Tanggerang' : 84},
		'Tanggerang' : {'Jakarta' : 35, 'Cilegon' : 84},
		'Jakarta' : {'Bogor' : 54, 'Cikampek' : 76, 'Bekasi' : 50, 'Tanggerang' : 35},
		'Bekasi' : {'Cikampek' : 41, 'Jakarta' : 50},
		'Cikampek' : {'Bandung' : 80, 'Cirebon' : 146, 'Jakarta' : 76, 'Bekasi' : 41},
		'Bogor' : {'Bandung' : 182, 'Jakarta' : 54},
		'Bandung' : {'Tasikmalaya' : 124, 'Cimahi' : 14, 'Cianjur' : 67, 'Garut' : 71, 'Sumedang' : 76, 'Subang': 54, 'Cikampek' : 80, 'Bogor' : 182},
		'Tasikmalaya' : {'Purwokerto' : 144, 'Bandung' : 124, 'Garut' : 53},
		'Cimahi' : {'Bandung' : 14},
		'Cianjur' : {'Bandung' : 67},
		'Garut' : {'Bandung' : 71, 'Tasikmalaya' : 53},
		'Sumedang' : {'Bandung' : 76},
		'Subang' : {'Bandung' : 54},
		'Purwokerto' : {'Magelang' : 145, 'Tasikmalaya' : 144},
		'Magelang' : {'Semarang' : 72, 'Jogja' : 53, 'Surabaya' : 339, 'Purwokerto' : 145},
		'Cirebon' : {'Tegal' : 88, 'Cikampek' : 146},
		'Tegal' : {'Semarang' : 160, 'Cirebon' : 88},
		'Semarang' : {'Jogja' : 129, 'Surabaya' : 348, 'Magelang' : 72, 'Tegal' : 160},
		'Jogja' : {'Surabaya' : 324, 'Magelang' : 53, 'Semarang' : 129},
		'Surabaya' : {'Malang' : 94, 'Magelang' : 339, 'Semarang' : 348, 'Jogja' : 324},		
		'Malang' : {'Surabaya' : 94}
	}

	finish = ' '
	daftarkota(kota)
	print('============================================')
	print('Please write your departure city and destination with a capital letter in the first letter (example: Bekasi)')
	print('-------------------------------------------')

	
	start = input('Your Current City : ').strip()
	start = start.lower()
	start = ''.join(start[0].upper() + start[1:])
	if start not in kota:
		print('\n The Format Name of City You Enter is Incorrect or Unregistered')
		
    
	finish = input('Your Destination City : ')
	path = Greedy(jarak, start, finish)
	print('Current City = ',start)
	if (path):
		print('City Order Based On Algoritma Greedy : ', end='')
		for i in path:
			print(i, end='>')

	else:
		print('Path Not Found')
	

if __name__ == '__main__':
	main()
