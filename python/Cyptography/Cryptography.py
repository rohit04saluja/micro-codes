# base class for cryptography
class Cryptography :
	# function to prepare text for conversion
	def _prepareText ( text ) :
		# remove all special characters
		text = ''.join( e for e in text if e.isalpha() )
		
		# convert all text in lower
		return text.lower()
	
	def _stringToInt ( text ) :
		# convert the text into integer
		for char in text :
			yield ord(char)%97
	
	def _intToString ( text ) :
		for char in text :
			return ''.join( yield( chr( char ) ) )