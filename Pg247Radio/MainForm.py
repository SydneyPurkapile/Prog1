import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 226)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(70, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Okay"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(171, 226)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(70, 32)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(12, 12)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Choice 1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(12, 42)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Choice 2"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(12, 72)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 4
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Choice 3"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(137, 13)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 5
		self._checkBox1.Text = "Choice 4"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(137, 43)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 6
		self._checkBox2.Text = "Choice 5"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(137, 73)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 7
		self._checkBox3.Text = "Choice 6"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._listBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(12, 103)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(224, 100)
		self._listBox1.TabIndex = 8
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(89, 226)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(70, 32)
		self._button3.TabIndex = 9
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(248, 270)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg247Radio"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			words = "Choice 1"
			self._listBox1.Items.Add(words)
		if self._radioButton2.Checked == True:
			words = "Choice 2"
			self._listBox1.Items.Add(words)
		if self._radioButton3.Checked == True:
			words = "Choice 3"
			self._listBox1.Items.Add(words)
		if self._checkBox1.Checked == True:
			words = "Choice 4"
			self._listBox1.Items.Add(words)
		if self._checkBox2.Checked == True:
			words = "Choice 5"
			self._listBox1.Items.Add(words)
		if self._checkBox3.Checked == True:
			words = "Choice 6"
			self._listBox1.Items.Add(words)
		else:
			words = "No Options Checked"
			self._listBox1.Items.Add(words)

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		pass