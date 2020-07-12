import tkinter as tk
import time

root = tk.Tk()

class Entscheider():

    def __init__(self):
        
        self.Quickplay_Button = tk.Button(text= "Competitiv", width=20, height=5, command=self.play_quickplay)
        self.Quickplay_Button.grid(row=0, column=0)
        
        self.Competitiv_Button = tk.Button(text= "Quickplay", width=20, height=5, command=self.play_competitiv)
        self.Competitiv_Button.grid(row=0, column=1)

    def play_competitiv(self):
        
        clickerGame = Kompetitiv()

    def play_quickplay(self):
        
        qpGame = Quickplay()


class Kompetitiv:

    def __init__(self):
         
        self.remaining_time = 10
        self.click_force = 1
        self.clicks = 0
        self.bf = 0
        self.the_button = tk.Button(text="Click the Button!", width=20, height=5,
                                    command=lambda: self.increment(self.clicks))
        self.the_button.grid(row=0, column=0)
        self.the_aimbot = tk.Button(text="Bot Current: 0", width=20, height=5,
                                    command=lambda: self.Bot(self.bf, self.clicks))
        self.the_aimbot.grid(row=1, column=0)
        self.clicker_update = tk.Button(text="Clicker Upgrade: %d" % self.click_force, width=20, height=5,
                                        command=self.clickerUpgrade)
        self.clicker_update.grid(row=0, column=1)

    def Bot(self, bf, clicks):
        if self.clicks >= 15:
            self.clicks = self.clicks - 15
            self.bf = self.bf + 1

        while self.remaining_time > 0:
            self.remaining_time = self.remaining_time - 1
            time.sleep(1)
            self.clicks = self.clicks + self.bf

    def increment(self, clicks):
        self.clicks = self.clicks + self.click_force
        self.Current_clicks = tk.Label(text="Du hast %d" % self.clicks)
        self.Current_clicks.grid(row=1, column=1)

    def clickerUpgrade(self):
        if self.clicks >= 15:
            self.clicks = self.clicks - 15
            self.click_force = self.click_force + 1


class Quickplay():

    def __init__(self):
        self.clicks = 0
        self.highest_clicks = 0
        self.remaining = 10

        
        self.the_button = tk.Button(text="Click the Button !", width=20, height=5, command=self.increment)
        self.the_button.grid(row=0, column=0)
        
        self.current_click_label = tk.Label(text="You have %d" % self.clicks, font="none 16 bold")
        self.current_click_label.grid(row=0, column=1)
        
        self.reset_button = tk.Button(text="Reset Game", width=20, height=5, command=self.restart)
        self.reset_button.grid(row=1, column=0)
        
        self.timer_label = tk.Label(text="", width=10, font="none 16 bold")
        self.timer_label.grid(row=1, column=1)
        
        self.countdown(10)

        self.settings = tk.Button(text="Settings", width=20, height=3, command=self.settingss)
        self.settings.grid(row=2, column=0)
        
        self.zurucksetzten = tk.Button(text="Reset All",width=20, height=3, command=self.reset_all)
        self.zurucksetzten.grid(row=2, column=1)

    def settingss(self):

        self.dark_light_mode = tk.Button(text="Dark/Light_Mode", width=20,height=3,command=self.darkmode)
        self.dark_light_mode.grid(row = 3, column=0)
        
    def darkmode(self):
        darkmode = False

        if darkmode:
            Quickplay.configure(__init__, background='blank',)

        if not darkmode:
            darkmode = True
            root.configure(background='darkgray')        
    def reset_all(self):
        pass

    def increment(self):

        self.clicks = self.clicks + 1
        
        self.current_click_label = tk.Label(text="You have %d" % self.clicks,  font="none 16 bold")
        self.current_click_label.grid(row=0, column=1)

    def restart(self):

        self.clicks = 0
        
        self.current_click_label = tk.Label(text="You have %d" % self.clicks,  font="none 16 bold")
        self.current_click_label.grid(row=0, column=1)
        
        newQuickplayGame = Quickplay()

    def countdown(self, remaining):


        if remaining is not None:
            
            self.remaining = remaining
            
        if remaining <= 0:
            
            self.timer_label.configure(text="time's up!",  font="none 16 bold")
            self.endGame()
            
        else:
            
            self.timer_label.configure(text="%d" % remaining)
            self.remaining = remaining - 1
            
            root.after(1000, self.countdown, self.remaining)
            

    def endGame(self):
        highscore  = 0

        self.the_button = tk.Button(text="Your score: %d" % self.clicks, width=20, height=5)
        self.the_button.grid(row=0, column=0)

        score = self.clicks
        
        if score > highscore:
            
            highscore = score
            f = open("highscore_list", "w+")
            pasthighscore = f.readline();
            pasthighscore = str(pasthighscore)
            pasthighscore = float(pasthighscore)
            allhighscore = f.read()
            #allhighscore = int(allhighscore)
            
            if pasthighscore <= highscore:
                strinng = str(highscore)
                f.write(strinng)
                time.sleep(2)
                f.close()





app = Entscheider()
root.mainloop()
