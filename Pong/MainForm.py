import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("Pong.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblball = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self._hello = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.White
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to Start Multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.Color.White
		self._leftscore.Location = System.Drawing.Point(78, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(166, 109)
		self._leftscore.TabIndex = 1
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.Color.White
		self._rightscore.Location = System.Drawing.Point(734, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(166, 109)
		self._rightscore.TabIndex = 2
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.Color.White
		self._lblball.Location = System.Drawing.Point(479, 304)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(20, 20)
		self._lblball.TabIndex = 3
		self._lblball.Click += self.LblballClick
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 4
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 5
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# hello
		# 
		self._hello.BackColor = System.Drawing.Color.Transparent
		self._hello.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._hello.ForeColor = System.Drawing.Color.White
		self._hello.Location = System.Drawing.Point(219, 427)
		self._hello.Name = "hello"
		self._hello.Size = System.Drawing.Size(554, 171)
		self._hello.TabIndex = 6
		self._hello.Text = "HELLO"
		self._hello.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button1.Location = System.Drawing.Point(113, 460)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(49, 46)
		self._button1.TabIndex = 7
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.BackgroundImage = resources.GetObject("button2.BackgroundImage")
		self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button2.Location = System.Drawing.Point(671, 229)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(49, 46)
		self._button2.TabIndex = 8
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.BackgroundImage = resources.GetObject("button3.BackgroundImage")
		self._button3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button3.Location = System.Drawing.Point(865, 518)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(49, 46)
		self._button3.TabIndex = 9
		self._button3.UseVisualStyleBackColor = True
		# 
		# button4
		# 
		self._button4.BackgroundImage = resources.GetObject("button4.BackgroundImage")
		self._button4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button4.Location = System.Drawing.Point(851, 80)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(49, 46)
		self._button4.TabIndex = 10
		self._button4.UseVisualStyleBackColor = True
		# 
		# button5
		# 
		self._button5.BackgroundImage = resources.GetObject("button5.BackgroundImage")
		self._button5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button5.Location = System.Drawing.Point(58, 67)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(49, 46)
		self._button5.TabIndex = 11
		self._button5.UseVisualStyleBackColor = True
		# 
		# button6
		# 
		self._button6.BackgroundImage = resources.GetObject("button6.BackgroundImage")
		self._button6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button6.Location = System.Drawing.Point(309, 180)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(49, 46)
		self._button6.TabIndex = 12
		self._button6.UseVisualStyleBackColor = True
		# 
		# button7
		# 
		self._button7.BackgroundImage = resources.GetObject("button7.BackgroundImage")
		self._button7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button7.Location = System.Drawing.Point(490, 427)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(49, 46)
		self._button7.TabIndex = 13
		self._button7.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(988, 607)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._hello)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._lblball)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)


	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		pass
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
		pass
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		if ball.Bottom >= self.Height:
			self.balld = 1
			ball.Top += 5 * self.balld
		pass
		if ball.Location.X <= 0 or (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
			rscore += 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._rightscore.Text = str(rscore)
		if ball.Location.X >= self.Width or (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
			lscore += 1
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self._leftscore.Text = str(lscore)
		pass
		if lscore == 10:
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to Restart"
		elif rscore == 10:
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Right Player Wins! Press R to Restart"
		pass
		if ball.Top <= 0:
			self.ballup *= -1
		elif ball.Bottom >= self.Height - 50:
			self.ballup *= -1
		pass
		if ball.Top <= self.Top + 10:
			self.ballup = 1
		elif ball.Top >= self.Height - 50:
			self.ballup = -1
		pass
		if self._timerboolean.Enabled == True:
			lpdl.Top = ball.Top - self.R.Next(-30, 31)
		pass

	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblball
		lblf = self._lblleft
		lblrt = self._lblright
		pass
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to Start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + self._lblleft.Height
			lblrt.Top = (self.Height // 2) - 100 + self._lblright.Height
			bl.BackColor = Color.White
			self.BackColor = Color.Black
			self._hello.Visible = False
			self._button1.Visible = False
			self._button2.Visible = False
			self._button3.Visible = False
			self._button4.Visible = False
			self._button5.Visible = False
			self._button6.Visible = False
			self._button7.Visible = False
		
		if e.KeyCode == Keys.R:
			reset()
		
		if e.KeyCode == Keys.H:
			self._hello.Visible = True
			
		if e.KeyCode == Keys.N:
			self._button1.Visible = True
			self._button2.Visible = True
			self._button3.Visible = True
			self._button4.Visible = True
			self._button5.Visible = True
			self._button6.Visible = True
			self._button7.Visible = True
			
		if e.KeyCode == Keys.P:
			rscore = 5
			self._rightscore.Text = str(rscore)
		if e.KeyCode == Keys.O:
			lscore = 5
			self._leftscore.Text = str(lscore)
		
		if e.KeyCode == Keys.Enter:
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			self._lbltitle.Visible = False
			
		if e.KeyCode == Keys.M:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move to left paddle; hit Enter to begin!"
			tmult.Enabled = True
			if e.KeyCode == Keys.Enter:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmult.Enabled = True
				tdum.Enabled = True
				tball.Enabled = True
		if tdum.Enabled == True:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
			
		if tmult.Enabled and tball.Enabled:
			tbool.Enabled = False
			if e.KeyCode == Keys.W:
				self.flagleft = False
				tleft.Enabled = True
			if e.KeyCode == Keys.S:
				self.flagleft = True
				tleft.Enabled = True
			
		pass

	def MainFormLoad(self, sender, e):
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
		self._hello.Visible = False
		self._button1.Visible = False
		self._button2.Visible = False
		self._button3.Visible = False
		self._button4.Visible = False
		self._button5.Visible = False
		self._button6.Visible = False
		self._button7.Visible = False
		pass
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		if flagd == False:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enabled = False
		if pdl.Bottom >= self.Height - 50:
			tmr.Enabled = False
		pass

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)
		pass

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)
		pass

	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Blue
		self.BackColor = Color.Yellow
		pass

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._lblball.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width
		pass