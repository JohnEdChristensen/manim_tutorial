from manimlib.imports import *
#create animation with the following command:
#manim tutorial.py lattice -pl --media_dir ./
class lattice(Scene):

    def construct(self):
        self.play(ShowCreation(Dot()))
        self.wait()

        hexagonal = [2*RIGHT,np.sqrt(3)*UP + RIGHT]
        
        points = []
        for x in range(-10,10,1):
            for y in range(-10,10,1):
                points.append(Dot().shift(x*hexagonal[0]+y*hexagonal[1]))

        pointsGroup = VGroup(*points)        
        
        self.play(ShowCreation(pointsGroup)) 


        bzv = np.array([
            [ -5.92119e-16 , -1.1547 ,0],
            [  1.0         , -0.57735,0],
            [  1.0         ,  0.57735,0],
            [  1.4803e-16  ,  1.1547 ,0],
            [ -1.0         ,  0.57735,0],
            [ -1.0         , -0.57735,0]])
        
        bzp = Polygon(*bzv,Color = BLUE,fill_opacity=.2)
        self.play(ShowCreation(bzp))
        self.wait()

        bzs = []
        for x in range(-10,10,1):
            for y in range(-10,10,1):
                bzs.append(Polygon(*bzv,Color = BLUE,fill_opacity=.2).shift(x*hexagonal[0]+y*hexagonal[1]))

        bzGroup = VGroup(*bzs)
        #self.play(ShowCreation(bzGroup,run_time=3))

        self.play(*[ShowCreation(t) for t in bzs])
        self.wait()

