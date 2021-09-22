g++ -c -fPIC booster.cpp -o booster.o
g++ -shared -Wl,-soname,libbooster.so -o libbooster.so booster.o