# Game Settings
FrameRate = 60

level_map_1 = [
'                                        ',
'X             P              XX        X',
'XX    XXX            XX             XX X',
'XX                            XX       X',
'XXXX                                   X',
'XXXX         XX    XX      XX          X',
'XX                                 XX  X',
'X     XX    XX        XX               X',
'X                XX          X  XX     X',
'X                                  XX  X',
'                                        '
]

level_list = [level_map_1]

# Window Settings
game_name = "Platformer"
tile_size= 54
screen_width = 1000
screen_height = len(level_map_1 ) * tile_size

# Player Settings
player_jump_height = 15
player_gravity = 0.8
player_speed = 8
double_jumps = 3
