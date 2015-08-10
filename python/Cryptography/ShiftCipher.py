# import Cryptography base class
import Cryptography

# class for shift cipher
class ShiftCipher(Cryptography.Cryptography) :
	# constructor for the function
	def __init__( self , key ) :
		self.__key = key
	
	# function to encrypt given text
	def encrypt ( self , text ) :
		# prepare text for conversion
		text = self._prepareInputText( text )
		
		# convert text to int
		text = self._stringToInt( text )
		
		# add encrypt key to every character
		for i in range( 0 , len( text ) ) :
			text[i] = ( text[i] + self.__key ) % 26
		
		# convert int to text
		return ''.join( self._intToString( text ) )
	
	# function to decrypt given text
	def decrypt ( self , text ) :
		# prepare text for conversion
		text = self._prepareInputText( text )
		
		# convert text to int
		text = self._stringToInt( text )
		
		# add decypt key to every character
		for i in range( 0, len( text ) ) :
			text[i] = (text[i] + ( 26 - self.__key ) ) % 26
		
		# convert int to text
		return ''.join( self._intToString( text ) )
	
	def updateKey (self , key ) :
		self.__key = key
