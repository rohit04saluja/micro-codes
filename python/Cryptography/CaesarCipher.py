# import the base class
import ShiftCipher

class CaesarCipher( ShiftCipher.ShiftCipher ) :
	# default constructor
	def __init__( self ) :
		super(CaesarCipher, self).__init__( 3 )