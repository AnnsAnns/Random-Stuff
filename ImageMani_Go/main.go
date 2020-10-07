package main

import (
	"image"
	"image/color"
	"image/png"
	"os"
)

func main() {
	width := 1000
	height := 1000
	xAx := width/1.5 + 140
	yAx := height / 2
	scale := 400
	iterations := 50

	for iy := 0; iy < height/2+1; iy++ {
		for ix := 0; ix < width; ix++ {
			z := 0
			c := complex(float64(ix-xAx)/float64(scale), float64(iy-yAx)/float64(scale))
			x := real(c)
			y := imag(c)
			q := (x-0.25)**2 + y ^ 2
			if !(q*(q+(x-0.25)) < y^2/4) || (x+1)**2+y^2 < 0.0625 {
				for i := 0; i < iterations; i++ {
					z := z**
				}
			}

		}
	}

	upLeft := image.Point{0, 0}
	lowRight := image.Point{width, height}

	img := image.NewRGBA(image.Rectangle{upLeft, lowRight})

	// Colors are defined by Red, Green, Blue, Alpha uint8 values.
	cyan := color.RGBA{100, 200, 200, 0xff}

	// Set color for each pixel.
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {

			switch {
			case x < width/2 && y < height/2: // upper left quadrant
				img.Set(x, y, cyan)
			case x >= width/2 && y >= height/2: // lower right quadrant
				img.Set(x, y, color.White)
			default:
				// Use zero value.
			}
		}
	}

	// Encode as PNG.
	f, _ := os.Create("image.png")
	png.Encode(f, img)
}
