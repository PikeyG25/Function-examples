from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

bg_img = games.load_image("images/homerdonut.png", transparent= False)
games.screen.background = bg_img

games.screen.mainloop()


