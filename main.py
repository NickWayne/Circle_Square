import pygame,math

def run():
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    SIZE = 20

    class ani (object):

        def __init__(self,pos):
            self.circles = []
            self.center = (320,240)
            self.circles.append(layer())
            self.circles[0].container.append(circle(self.center,True))
            self.num = 1

        def add_layer(self):
            stepx = -1
            stepy = -1
            self.circles.append(layer())
            x = self.num
            y = 2*self.num
            for i in xrange(self.num*4+1):
                self.circles[self.num].container.append(circle((self.center[0]+(SIZE*(self.num-x)),self.center[1]+(SIZE*(self.num-y)))))
                perc = float((i+1))/float((self.num*4))
                x += stepx
                y += stepy
                if perc == 1./4.:
                    stepx = 1
                    stepy = -1
                if perc == 1./2.:
                    stepx = 1
                    stepy = 1
                if perc == 3./4.:
                    stepx = -1
                    stepy = 1



            self.num += 1

        def radius_plus(self):
            rad = 0
            for i in self.circles:
                for j in i.container:
                    j.radius_plus()
                    rad = j.radius

            if rad >= int(SIZE*(1./5.)):
                self.add_layer()



        def radius_minus(self):
            rad = 0
            for i in self.circles[-1].container:
                i.radius_minus()
                rad = i.radius
            try:
                if rad < int(SIZE*(4./5.)):
                    for i in self.circles[-2].container:
                        i.radius_minus()
                if rad < int(SIZE*(3./5.)):
                    for i in self.circles[-3].container:
                        i.radius_minus()
                if rad < int(SIZE*(1./2.)):
                    for i in self.circles[-4].container:
                        i.radius_minus()
                if rad < int(SIZE*(2./5.)):
                    for i in self.circles[-5].container:
                        i.radius_minus()
            except Exception:
                pass


            if rad <= int(SIZE*(1./5.)) and self.circles[-1].container[0].first != True:
                del self.circles[-1]
                self.num -= 1



        def render(self,surface):
            for i in self.circles:
                for j in i.container:
                    j.render(surface)

    class layer (object):

        def __init__(self):
            self.container = []
            self.radius = 0


    class circle (object):

        def __init__(self,center,first = False):
            self.surf = pygame.Surface((SIZE,SIZE))
            self.color = (200,100,100)
            self.center = center
            self.radius = 4
            self.first = first

        def radius_plus(self):
            self.radius += 2
            if self.radius > int(SIZE*(4./5.)) :
                self.radius = int(SIZE*(4./5.))
            if self.radius < 10 and self.first == True:
                self.radius = 10



        def radius_minus(self):
            self.radius -= 2
            if self.radius <= int(SIZE*(1./5.)) and self.first == True:
                self.radius = int(SIZE*(1./5.))

            elif self.radius < 0:
                self.radius = 0

        def render(self,surface):
            self.surf.fill((0,0,0))
            pygame.draw.circle(self.surf,self.color,((SIZE/2),(SIZE/2)),self.radius)
            surface.blit(self.surf,(self.center[0]-(SIZE/2),self.center[1]-(SIZE/2)))




    circles = ani((320,240))
    done = False
    pygame.key.set_repeat(50,50)
    while not done:
        time_passed_seconds = clock.tick(120)/1000.0
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     circles = ani(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_LEFT:
                    try:
                        circles.radius_minus()
                    except Exception:
                        pass
                if event.key == pygame.K_RIGHT:
                    try:
                        circles.radius_plus()
                    except Exception:
                        pass


        screen.fill((0, 0, 0))
        try:
            circles.render(screen)
            # circles.drag(mouse_pos)
        except Exception:
            pass
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()