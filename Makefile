CXX = g++
CXXFLAGS = `pkg-config --cflags opencv`
TARGET = sampling
SOURCE = $(TARGET).cpp
LDFLAGS = `pkg-config --libs opencv` -lm

TARGET:
	$(CXX) -o $(TARGET) $(SOURCE) $(CXXFLAGS) $(LDFLAGS)

.PHONY: clean
	clean:
		rm -f *.o *~
