import pygame
import random
from gl import *
from BMP_Writer import GenerateBMP
from model import Model
from OBJLoader import OBJ
from figures import *
from lights import *
from material import REFLECTIVE, OPAQUE, TRANSPARENT, Material
from BMPTexture import BMPTexture

width = 550
height = 550

screen = pygame.display.set_mode((width, height), pygame.SCALED)
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.envMap = None

cuarzo = Material(diffuse=[1.0, 0.6, 0.8], spec=120, ks=0.5, matType=OPAQUE)
wood = Material(diffuse=[0.6, 0.3, 0.1], spec=8, ks=0.1, matType=OPAQUE)
yellow = Material(diffuse=[1.0, 1.0, 0.2], spec=16, ks=0.1, matType=OPAQUE)



silver = Material(diffuse= [0.9, 0.9, 0.9], spec = 150, ks = 0.92, matType = REFLECTIVE)
gold = Material(diffuse = [1.0, 0.8, 0.2], spec = 120, ks = 0.85, matType = REFLECTIVE)
emerald = Material(diffuse=[0.0, 0.6, 0.3], spec=100, ks=0.8, matType=REFLECTIVE)



zafiro = Material(diffuse = [1.0, 0.7, 0.85], ior = 1.78, matType= TRANSPARENT)
water = Material(diffuse = [0.9, 0.95, 1.0], ior = 1.33, matType= TRANSPARENT)
ruby = Material(diffuse=[1.0, 0.2, 0.3], ior=1.77, matType=TRANSPARENT)


brick = Material(diffuse = [1, 0, 0])
grass = Material(diffuse = [0, 1, 0], spec = 32, ks = 0.4)
mirror = Material(diffuse= [0.9, 0.9, 0.9], spec = 128, ks = 0.5, matType = REFLECTIVE)
blueMirror = Material(diffuse = [0, 0, 0.9], spec = 64, ks = 0.2, matType = REFLECTIVE)

glass = Material(diffuse = [1, 1, 1], ior = 1.5, matType= TRANSPARENT)


white_wall = Material(diffuse=[0.95, 0.95, 0.95], spec=16, ks=0.1, matType=OPAQUE)
dark_floor = Material(diffuse=[0.3, 0.3, 0.4], spec=32, ks=0.2, matType=OPAQUE)

#rend.scene.append(Sphere(position=[-2, 0, -5], radius=1.0, material=brick))

rend.scene.append(Plane(position=[0, -2.5, 0], normal=[0, 1, 0], material=dark_floor))
rend.scene.append (Plane(position=[0, 2.5, 0], normal=[0, -1, 0], material=white_wall))
rend.scene.append(Plane(position=[0, 0, -10], normal=[0, 0, 1], material=white_wall))
rend.scene.append(Plane(position=[-4, 0, 0], normal=[1, 0, 0], material=white_wall))
rend.scene.append(Plane(position=[4, 0, 0], normal=[-1, 0, 0], material=white_wall))


# rend.scene.append(Disk(position=[0, -2, -4], normal = [0, 1, 0], radius= 0.5, material = brick))

# rend.scene.append(AABB(position=[-2, -1.5, -6], sizes=[1.5, 2, 1.2], material= cuarzo))

# rend.scene.append(Triangle(A = [-1.2, 0.5, -7.8], B = [0, 2, -7.8], C = [1.2, 0.5, -7.8], material= gold))

rend.scene.append(Cilindro(position=[0, -1.5, -6], height=1, radius=0.4, material= yellow))
rend.scene.append(Elipsoide(position=[0, 0.5, -6], radius=[0.25, 0.5, 0.25], material= cuarzo))

rend.scene.append(Cilindro(position=[-2, -1.4, -6], height=1.5, radius=0.75, material= gold))
rend.scene.append(Elipsoide(position=[-1, 0.5, -6], radius=[0.5, 0.2, 0.5], material= emerald))

rend.scene.append(Cilindro(position=[2, -1.4, -6], height=2, radius=0.4, material= zafiro))
rend.scene.append(Elipsoide(position=[1, 0.5, -6], radius=[0.4, 0.3, 0.4], material= ruby))

rend.lights.append(AmbientLight(intensity=0.25))
rend.lights.append(PointLight(position=[0, 2, -5], intensity=0.5))
rend.lights.append(PointLight(position=[0, 0, -3], intensity=0.2))
#rend.lights.append(DirectionalLight(direction=[1, -1, -1], intensity=0.2))

#rend.lights.append(SpotLight(intensity= 1.2, position = [0, 2, -4], direction = [0, -1, 0]))

                   

# rend.glRender()

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rend.camera.translation[0] += 0.1
            elif event.key == pygame.K_LEFT:
                rend.camera.translation[0] -= 0.1

            elif event.key == pygame.K_UP:
                rend.camera.translation[1] += 0.1
            elif event.key == pygame.K_DOWN:
                rend.camera.translation[1] -= 0.1


            elif event.key == pygame.K_q:
                rend.camera.translation[2] += 2 * deltaTime  
            elif event.key == pygame.K_e:
                rend.camera.translation[2] -= 2 * deltaTime


            elif event.key == pygame.K_a:
                rend.camera.rotation[1] -= 45 * deltaTime
            elif event.key == pygame.K_d:
                rend.camera.rotation[1] += 45 * deltaTime
            elif event.key == pygame.K_w:
                rend.camera.rotation[0] -= 45 * deltaTime
            elif event.key == pygame.K_s:
                rend.camera.rotation[0] += 45 * deltaTime
        

    

    #rend.glClearBackground()
    rend.glRender()


GenerateBMP("output.bmp", width, height, 3, rend.frameBuffer)

pygame.quit()
