CC=gcc
CFLAGS=-c -g
LDFLAGS= -lm
FILE=

all: ${FILE}

${FILE}: ${FILE}_wrapper.o ${FILE}.o
	$(CC) $(LDFLAGS) ${FILE}_wrapper.o ${FILE}.o -o ${FILE}

${FILE}_wrapper.o: ${FILE}_wrapper.c
	$(CC) $(CFLAGS) ${FILE}_wrapper.c

${FILE}.o: ${FILE}.c
	$(CC) $(CFLAGS) ${FILE}.c

clean:
	rm -rf *o ${FILE}
