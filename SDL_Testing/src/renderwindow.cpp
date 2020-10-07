#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <iostream>

#include "RenderWindow.hpp"

RenderWindow::RenderWindow(const char* p_ititle, int p_w, int p_h) 
	:window(NULL), renderer(NULL)
{
	SDL_CreateWindow(p_title, SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, p_w, p_h, SDL_WINDOW_SHOWN);

	if (window == NULL) {
		std::cout << "Window F: " << SDL_GetError() << std::endl;
	}

	renderer = SDL_CreateRenderer(window, -1, SDL_RENDER_ACCELERATED);
}

void RenderWindow::cleanUp() {
	SDL_DestroyWindow(window)
}