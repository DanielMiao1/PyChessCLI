# -*- coding: utf8 -*-
import time

print(f"\033[96mLoading fonts... ", end="")
start = time.time()
from Font import *
print(f"{Font.neutral + Color.green}complete, took {time.time() - start}s{Color.cyan}\nImporting chess module... ", end="")

try:
	start = time.time()
	import chess
	end = time.time()
	chess.Game
	print(f"{Font.neutral + Color.green}complete, took {end - start}s")
except (ModuleNotFoundError, AttributeError) as error:
	print(f"\n{Font.neutral}{Background.darkred}ERROR{Font.neutral} {Color.darkred}{str(error).title()}{Font.neutral}")
	def install():
		input_ = input(f"{Color.purple}Install chess(y/n)? {Font.neutral}")
		if input_.lower() == "y":
			import os
			os.system("pip3 install git+https://github.com/DanielMiao1/PyChess")
		elif input_.lower() == "n":
			print(f"{Color.cyan}You can manually install the chess module by running {Background.gray}pip3 install git+https://github.com/DanielMiao1/PyChess{Font.neutral}")
			exit()
		else:
			print(f"{Background.darkred}ERROR{Font.neutral} {Color.darkred}You did not enter a valid choice: '{input_}'{Font.neutral}")
			install()
	install()
	
import chess

class Game_:
	def __init__(self):
		"""Initilize the Game"""
		print(f"{Color.cyan}Initializing game... ", end="")
		start = time.time()
		self.game = chess.Game()
		print(f"{Color.green}complete, took {time.time() - start}s{Font.neutral}")
		self.print_board = True

	def run(self):
		"""Main Loop"""
		print()
		while True:
			print(f"{self.game.visualized()}\n{Background.white if self.game.turn == 'black' else ''}{Color.black if self.game.turn == 'black' else Color.white}{self.game.turn.title()}{Font.neutral}{Font.bold} to move{Font.neutral}") if self.print_board else None
			move = input(f"{Color.purple}Enter your move: {Font.neutral}")
			if move.lower() in ["m", "moves"]:
				print(f"{Color.cyan}Legal moves are: {Font.underline}{', '.join(self.game.legal_moves())}{Font.neutral}")
				self.print_board = False
				continue
			elif move.lower() in ["l", "ml", "movelist", "move list", "list"]:
				print(f"{Color.cyan}The current move list is: {Font.underline}{self.game.move_list}{Font.neutral}")
				self.print_board = False
				continue
			elif move.lower() in ["t", "takeback"]:
				print(f"{Color.cyan}Takeback{Font.neutral}")
				self.game.takeback()
				continue
			elif move.lower() in ["o", "opening"]:
				print(f"{Color.cyan}Current opening: {self.game.opening}{Font.neutral}")
				self.print_board = False
				continue
			elif move not in self.game.legal_moves():
				print(f"{Background.darkred}ERROR{Font.neutral} {Color.darkred}You did not enter a valid move: '{move}'{Font.neutral}")
				self.print_board = False
				continue
			self.game.move(move)
			self.print_board = True


game_ = Game_()
game_.run()


# Game
# Player
# Board
# Pieces

# Pawns, Knights, Bishops, Rooks, Queens, and Kings

# Actions: Castle, En Passant, Stalemate, Repetition, Check, Checkmate, Pawns First Move, Captures, Movement, Resign, Offer Draw