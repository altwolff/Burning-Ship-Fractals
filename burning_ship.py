# altwolff 2025
import numpy as np
import matplotlib.pyplot as plt

def burning_ship(width, height, max_iterations):

    # Edit these four values to edit fractal zoom
    min_x = -1.80
    max_x = -1.70
    min_y = -0.10
    max_y = 0.02

    image = np.zeros((height, width))
    
    for y in range(height):
        for x in range(width):
            real = min_x + (x / width) * (max_x - min_x)
            imag = min_y + (y / height) * (max_y - min_y)
            c = real + imag * 1j
            z = 0 +0j
            iter = 0

            while abs(z) <= 2.0 and iter < max_iterations:
                z = (abs(z.real) + abs(z.imag) * 1j) ** 2 + c
                iter += 1
                
            if iter == max_iterations:
                image[y, x] = 0  
            else:
                image[y, x] = iter  
       
    return image

# Edit these three parameters
width = 5000
height = 5000
max_iterations = 100

image = burning_ship(width, height, max_iterations)

plt.imshow(image, cmap='plasma', extent=(-1.80, -1.70, -0.10, 0.02)) # Edit fractal zoom
plt.axis('off')
plt.savefig("burning_ship.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.show()