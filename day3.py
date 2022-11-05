 # importing images
        self.images = {
            "plain": PhotoImage(file = "Images_mine/tile_plain.gif"),
            "clicked": PhotoImage(file = "Images_mine/tile_clicked.gif"),
            "mine": PhotoImage(file = "Images_mine/tile_mine.gif"),
            "flag": ImageTk.PhotoImage(Image.open("Images_mine/tile_flag.jpg")),
            "wrong": PhotoImage(file = "Images_mine/tile_wrong.gif"),
            "numbers": []
        }
        for i in range(1, 4):
            self.images["numbers"].append(PhotoImage(file = "Images_mine/tile_"+str(i)+".gif"))

        # set up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # set up labels/UI(creating time, mine and flag labels)
        self.labels = {
            "time": Label(self.frame, text = "00:00:00"),
            "mines": Label(self.frame, text = "Mines: 0"),
            "flags": Label(self.frame, text = "Flags: 0")
        }
        #setting position for labels in the frame
        
        self.labels["time"].grid(row = 0, column = 0, columnspan = SIZE_Y) # top full width
        self.labels["mines"].grid(row = SIZE_X+1, column = 0, columnspan = int(SIZE_Y/2)) # bottom left
        self.labels["flags"].grid(row = SIZE_X+1, column = int(SIZE_Y/2)-1, columnspan = int(SIZE_Y/2)) # bottom right

        self.restart() # start game
        self.updateTimer() # init timer

    def setup(self):
        # create flag and clicked tile variables
        self.flagCount = 0
        self.correctFlagCount = 0
        self.clickedCount = 0
        self.startTime = None

        # create buttons(creating each and every square by placing mines randomly)
        self.tiles = dict({})
        self.mines = 0
        for x in range(0, SIZE_X):
            for y in range(0, SIZE_Y):
                if y == 0:
                    self.tiles[x] = {}

                id = str(x) + "_" + str(y)
                isMine = False
