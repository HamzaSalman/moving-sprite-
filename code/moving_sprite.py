# Created by: Hamza Salman
# Created on: September 2016
# Course: ICS3U
# Program moves a sprite by dragging it

import ui
from scene import *

class FirstScene(Scene):
    def setup(self):
    # add MT blue background color
        self.background = SpriteNode(position = self.size / 2,
                                     color = (0.61, 0.78, 0.87),
                                     parent = self,
                                     size = self.size)
        self.school_crest = SpriteNode('./assets/sprites/school_crest.jpg',
                                       position = self.size / 2,
                                       parent = self)
                                   
    def touch_moved(self, touch):
        # Moves the image by dragging
        self.school_crest.position = touch.location
        
        
main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH')
main_view.add_subview(scene_view)
scene_view.scene = FirstScene()
main_view.present(hide_title_bar = True, animated = False)
