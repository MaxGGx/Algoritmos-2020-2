all: alist.o cqueue.o main clean

alist.o: alist.cpp
	g++ -W -c alist.cpp -o alist.o

cqueue.o: cqueue.cpp 
	g++ -W -c cqueue.cpp -o cqueue.o

main: main.o
	g++ main.o alist.o cqueue.o -o a.out

main.o: main.cpp
	g++ -W -c main.cpp -o main.o

clean:
	rm *.o