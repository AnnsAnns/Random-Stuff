CXX = g++
CXXFLAGS = -std=c++0x -g -O3 -w -Wl,-subsystem,windows
INCLFLAGS = -IC:C:\SDL2-w64\include\SDL2
LDFLAGS = -LC:\SDL2-w64\lib -lmingw32 -lSDL2main -lSDL2
OBJECTS = main.o
TARGET = 1_hellosdl

$(TARGET) : $(OBJECTS)
    $(CXX) $(INCLFLAGS) $(LDFLAGS) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

main.o :

clean:
    rm -rf $(OBJECTS) $(TARGET)

remake:
    clean $(TARGET)