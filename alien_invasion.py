# coding=utf-8

#导入模块sys（用来退出游戏）
import sys

#导入模块pygame(包含游戏开发所具有的功能）
import pygame

# 从创建的设置类导入模块
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	
	# 初始化pygame,设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	         (ai_settings.screen_width , ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
	# 创建一艘飞船
	ship = Ship(screen)
		
	# 开始游戏的主循环
	while True:
		gf.check_events(ship)
		gf.update_screen(ai_settings,screen, ship)
		
		# 让最近绘制的屏幕可见
		pygame.display.flip()
		
run_game()

