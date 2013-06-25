try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program."

playername="Anon"
class getName(wx.App):
    def OnInit(self):
        # Args below are: parent, question, dialog title, default answer
        dlg=wx.TextEntryDialog(None,'What is your name ?','Vocabulate Master', '<name>')

        # This function returns the button pressed to close the dialog
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            print('Welcome %s\n' % dlg.GetValue())
            playername=dlg.GetValue()
        else:
            print('Welcome to Vocabulate-Master\n' % dlg.GetValue())
            print('You chose to remain Anonymous')
        dlg.Destroy()
        return True

class mainPanel(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent

        #-----------------
        
        # Pick an image file you have in the working folder
        # You can load .jpg  .png  .bmp  or .gif files
        image_file = "bg.jpg"
        self.bmp = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        # Image's upper left corner anchors at panel coordinates (0, 0)
        self.bitmap1 = wx.StaticBitmap(self, -1, self.bmp, (0, 0))
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
                
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)

        # Simplified init method
        self.CreateButtons()
        self.DoLayout()

        
    def CreateButtons(self):
        # Button goes on the image --> self.bitmap1 is the parent
        self.btn1 = wx.Button(self.bitmap1, id=-1, label='New Game')
        self.btn2 = wx.Button(self.bitmap1, id=-1, label="High Scores")
        self.btn3 = wx.Button(self.bitmap1, id=-1, label="Options")
        self.btn4 = wx.Button(self.bitmap1, id=-1, label="Quit")
        #bind buttons to functions here 
        self.Bind(wx.EVT_BUTTON, self.OnNewGame, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.btn4)

        self.btn1.SetFocus()
    
    def OnQuit(self, e):
        self.frame.Close()
    def OnNewGame(self, e):
        #code for initiating new game
        wx.MessageBox('Under Construction !', 'New Game',wx.OK | wx.ICON_INFORMATION)
    
    def OnResize(self, event):
        self.btn1.Refresh(), self.btn2.Refresh(),
        self.btn3.Refresh(), self.btn4.Refresh()
        event.Skip()

    def OnEraseBackground(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)

    def Draw(self, dc):
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        self.Draw(dc)

    def DoLayout(self):     
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn1, 0, wx.ALL, 5)
        sizer.Add(self.btn2, 0, wx.ALL, 5)
        sizer.Add(self.btn3, 0, wx.ALL, 5)
        sizer.Add(self.btn4, 0, wx.ALL, 5)
        
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 50)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer(hSizer)

class mainFrame(wx.Frame):

    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(500, 333),style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER 
    | wx.SYSTEM_MENU | wx.CAPTION |  wx.CLOSE_BOX)
        panel = mainPanel(self)            
        self.SetMaxSize((1024, 768))
        self.Center()

        #menu related code
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        
        fileNewGame = fileMenu.Append(-1, 'New Game', 'New Game')
        fileHighScores = fileMenu.Append(-1, 'High Scores', 'View Highscores')
        fileQuit = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        
        menubar.Append(fileMenu, '&File')
        
        helpInstr=helpMenu.Append(-1, 'Instructions', 'Game Play Information')
        menubar.Append(helpMenu, '&Help')
       
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)
        self.Bind(wx.EVT_MENU, self.OnInstr, helpInstr)
        self.Bind(wx.EVT_MENU, self.OnNewGame, fileNewGame)
        self.Bind(wx.EVT_MENU, self.OnHighScore, fileHighScores)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 0,0)

    def OnQuit(self, e):
        self.Close()
    def OnInstr(self, e):
        #code for Game Instructions 
        wx.MessageBox('Under Construction !', 'Instructions',wx.OK | wx.ICON_INFORMATION)

    def OnNewGame(self, e):
        #code for initiating new game
        wx.MessageBox('Under Construction !', 'New Game',wx.OK | wx.ICON_INFORMATION)
    def OnHighScore(self, e):
        #code for viewing high scores
        wx.MessageBox('Under Construction !', 'High Scores',wx.OK | wx.ICON_INFORMATION)
    

app=getName(redirect=0)
frame = mainFrame(None, -1, 'Vocabulator v1.0')
frame.Show()
app.MainLoop()


#---------------------untouched original CUI code--------------------------
## Add sentence usage
## Add synonyms
## Add choice of vocab list
## Add type of word (noun/adj/etc.)
import random

db = {}
vocab = open('vocab.txt', 'r')
for line in vocab:
    if len(line) < 5: continue
    name = line[:line.find(' ')]
    line = line[line.find(' ')+1:]
    type = line[:line.find(' ')]
    line = line[line.find(' ')+1:]
    defn = line
    if type not in ['n.', 'ad.', 'conj.', 'inter.', 'interj.', 'prep.', 'v.', 'adj.', 'adv.'] or len(defn) < 4: continue
    db[name] = defn
vocab.close()

## Get the highscore
score = open('data', 'rb')
high_score = score.readline()
score.close()

def write_highscore(new_score):
    score = open('data', 'wb')
    score.write(str(high_score))
    score.close()

def guess(word, multiple):
    score = 0
    round_no = 0
    limit = 1
    if multiple:
        limit = 4
    while round_no < 10:
        ## Disallow same words in the ten rounds?
        definitions = []
        term = random.sample(db.keys(), limit)
        for question_word in term:
            definitions.append(db[question_word])
        if word:
            q = term
            a = definitions
        else:
            a = term
            q = definitions
        print "Q: " + q[0]
        print
        poss = a[:]
        random.shuffle(poss)
        if multiple:
            print "Options"
            for ind, option in enumerate(poss):
                print ind+1, 
                print option
            print "Enter answer number"
            ans = input()
            if poss[ans-1] == a[0]:
                print "CORRECT"
                score+=1
            else:
                print "WRONG!" + " The correct answer was: " + a[0]
        else:
            ans = raw_input()
            print a[0]
            print "Did you get it right? (1 - Yes, 0 - No)"
            ans = input()
            score+=ans
        print "SCORE: " + str(score)
        print 
        round_no+=1
    print "Your score was: ", score
    if score > int(high_score):
        print "You achieved a new high_score!"
    write_highscore(score)

def run_game(choice):
    if choice == 1:
        guess(True, False)
    elif choice == 2:
        guess(False, False)
    elif choice == 3:
        guess(True, True)
    elif choice == 4:
        guess(False, True)
    elif choice == 5:
        print "Your high score is ", high_score

choice = 2
while choice < 10:
    print "1. Guess what the word means"
    print "2. Guess what word the definition corresponds to"
    print "3. Match (Given: word)"
    print "4. Match (Given: definition)"
    print "5. Check high score"
    print "10. Exit"

    choice = input()
    run_game(choice)

