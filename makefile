MNISTDemoBits: MultiClassTsetlinMachineBits.c MultiClassTsetlinMachineBits.h TsetlinMachineBits.c TsetlinMachineBitsConfig.h TsetlinMachineBits.h MNISTDemoBits.c
	gcc -Wall -O3 -ffast-math -o MNISTDemoBits MNISTDemoBits.c MultiClassTsetlinMachineBits.c TsetlinMachineBits.c 

clean:
	rm *.o MNISTDemoBits

pythonWrapper: MultiClassTsetlinMachineBits.c MultiClassTsetlinMachineBits.h TsetlinMachineBits.c TsetlinMachineBitsConfig.h TsetlinMachineBits.h MNISTDemoBits.c
	gcc -fPIC -shared -Wall -O3 -ffast-math -o MNISTDemoBitsDynamicallyLoadable.so MNISTDemoBits.c MultiClassTsetlinMachineBits.c TsetlinMachineBits.c 
