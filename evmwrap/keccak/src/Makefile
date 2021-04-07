OBJS = keccak.o keccakf800.o

all : ${OBJS}

%.o : %.c
	gcc -O3 -fPIC -c  -I ../include -o $@ -c $<

clean:
	rm *.o
