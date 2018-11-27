# A.3 3D 그래픽과 애니메이션

from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # environment model을 불러온다.
        self.environ = self.loader.loadModel("models/environment")
        # model에서 부모를 render로 바꾼다(reparent).
        self.environ.reparentTo(self.render)
        # scale과 position의 변화를 model에 적용한다.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

app = MyApp()
app.run()
