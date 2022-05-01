import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Hells Cowboy Arcade",
    options={"build_exe": {"packages":["pygame", "random", "sys"],
                           "include_files": ["img/baddge1.png", "img/baddge2.png", "img/baddge3.png", "img/baddge4.png", "img/brick.png",
                                              "img/fl0.png", "img/fl1.png", "img/fl2.png", "img/fl3.png", "img/fl4.png","img/fl5.png",
                                              "img/fl6.png", "img/fl7.png", "img/fl8.png", "img/fl9.png", "img/fl10.png", "img/fl11.png",
                                              "img/fl12.png","img/fw5.png", "img/heart.png", "img/horse1.png", "img/horse2.png", "img/horse3.png",
                                              "img/horse4.png", "img/horse5.png", "img/horse6.png", "img/horse7.png", "img/horse8.png",
                                              "img/player0.png", "img/player1.png", "img/player2.png", "img/player3.png", "img/player4.png",
                                              "img/player5.png", "img/player6.png", "img/player7.png", "img/player8.png", "img/player9.png",
                                              "img/skull(b).png", "img/skull(w).png", "img/skull5.png", "img/skull20.png", "img/skull40.png",
                                              "img/skull60.png","txt/highscore.txt"]}},
    executables = executables
)