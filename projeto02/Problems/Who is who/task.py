class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


my_angel, my_demon = Angel(), Demon()
print(f'{my_angel.color}\n{my_angel.feature}\n{my_angel.home}\n'
      f'{my_demon.color}\n{my_demon.feature}\n{my_demon.home}')