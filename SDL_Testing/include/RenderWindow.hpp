#pragma once
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>

class RenderWindow {
public:
	RenderWindow(const char* p_title, int p_y, int p_h);
	void CleanUp();
private:
	SDL_Window* window;
	SDL_Renderer* renderer;
};