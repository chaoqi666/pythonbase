from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map    #初始化scene_map,刚开始的时候传入输入的场景名，完成当前场景的时候，传入返回的场景

    def play(self):
        current_scene = self.scene_map.opening_scene()    #opening_scene是class Map中的方法，会返回当前的场景类
        last_scene = self.scene_map.next_scene('finished')   #返回名为finish的场景类

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()     #通过Enter方法执行场景中的指令，并返回下一个场景给next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)   #将当前场景变为下一场景，继续while的判断

        current_scene.enter()   #当到最后一个场景的时候，直接执行到游戏结束

class Death(Scene):

    quips = [
        "你死了，世界被火星人占领，游戏结束...\n",
        "你被火星人击中，游戏结束...\n",
        "任务失败...\n",
        "你太弱了，任务结束...\n",
        "你就是一个笑话，世界正在毁灭，任务失败...\n",
        "任务失败，任务对你来说太难了，你还是回家玩泥巴吧...\n"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        return 'try_it_again'


class CentralCorridor(Scene):

    def enter(self):
        print("""
火星人的飞船占领了地球，将所有的人都囚禁起来
你因为在河边玩泥巴逃过一劫
但拯救地球的任务就落在你的身上...
你需要从军火库取出中子弹
炸毁火星人的飞船
然后从逃生通道逃出，拯救世界

现在你正处于一个长长的走廊上，迎面走来一个火星人
            """)

        action = input("选择一个数字: 1.射击,2.快速躲起来,3.讲一个笑话\n>>")
        if action == "1":
            print("""
火星人发现了你，它躲过你的子弹，并快速的向你射击
一大群火星人听到枪声赶来...
                  """)
            return 'death'

        elif action == "2":
            print("不幸的是火星人还是发现了你...")
            return 'death'

        elif action == "3":
            print("""
火星人控制不住自己，
连武器都笑得掉在地上，
你乘机将他击倒，
并夺得武器

走过长廊，你进入武器库...
                  """)
            return 'laser_weapon_armory'

        else:
            print("请认真选择，命运在于选择!")
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    def enter(self):
        print("""
现在你进入到武器库，在武器库的中央保险柜中存放着中子弹
但是你必须正确输入密码
            """)
        password = f"{randint(0,9)}{randint(0,9)}"
        action = input("请输入两位数的密码\n>>")
        counts = 1
        while action != password and counts < 10:
            if int(action) < int(password):
                print('数字小了...')
            else:
                print('数字大了...')
            counts += 1
            action = input("请重新输入密码\n>>")

        if action == password:
            print("""
恭喜你，被你蒙对了！你获得中子弹！
                    """)
            return 'the_bridge'

        else:
            print("""
错误次数太多，中子弹爆炸
                    """)
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print("""
一扇门开启，你进入到飞船中控室
现在你需要炸毁这艘飞船
                """)
        action = input("""
请选择一个处理中子弹的方法：
1. 向中控室扔出中子弹
2. 将中子弹设置在控制台下
>>""")
        if action == '1':
            print("中子弹无法引爆，火星人发现了你\n")
            return 'death'
        elif action == '2':
            print("中子弹被正确设置，十分钟内将引爆\n")
            return 'escape_pod'
        else:
            print('火星人正在赶来，请尽快作出决定！\n')
            return 'the_bridge'



class EscapePod(Scene):

    def enter(self):
        print("""
现在你需要在爆炸发生前离开飞船
你可以通过逃生通道逃生
但五条逃生通道中只有一条是安全的通道
                """)
        safe_pod = str(randint(1, 5))
        action = input('请选择一条逃生通道：1. 通道A；2. 通道B；3. 通道C；4. 通道D；5. 通道E\n>>')
        count = 1
        while action != safe_pod and count < 3:
            action = input('请重新选择\n>>')
            count += 1
        if action != safe_pod:
            print(f"正确的逃生通道应该选择{safe_pod},你落入火星人之手")
            return 'death'
        else:
            print("选择正确，你顺利逃出\n")
            return 'finished'

class TryItAgain():

    def enter(self):
        choose = input("再来一次吗：Y/N\n>>").upper()
        if choose == 'Y':
           return 'central_corridor'
        elif choose == 'N':
           exit(1)
        else:
            print('请输入Y或N')
            return 'try_it_again'

class Finished(Scene):

    def enter(self):
        print("火星人的飞船被炸毁，你拯救了地球！\n")
        print('任务完成')
        return 'finished'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'try_it_again': TryItAgain(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
