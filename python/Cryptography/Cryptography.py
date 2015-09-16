# base class for cryptography
class Cryptography :
	# function to prepare text for conversion
	def _prepareInputText ( self , text ) :
		# remove all special characters
		text = ''.join( e for e in text if e.isalpha() )
		
		# convert all text in lower
		return text.lower()
	
	def _stringToInt ( self , text ) :
		# initialize the output variable
		out = []
		# convert the text into integer
		for char in text :
			out.append( ord( char ) % 97 )
		# return the output
		return out
	
	def _intToString ( self , text ) :
		# initializw the output variable
		out = []
		# convert the int into text
		for char in text :
			out.append( chr( char + 65 ) )
		# return the output
		return out
