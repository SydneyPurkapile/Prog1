import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 119)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 33)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(118, 119)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 33)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.SystemColors.ControlDark
		self._button4.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(224, 4)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(36, 33)
		self._button4.TabIndex = 3
		self._button4.Text = "+"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.SystemColors.ControlDark
		self._button5.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(266, 5)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(36, 33)
		self._button5.TabIndex = 4
		self._button5.Text = "-"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.SystemColors.ControlDark
		self._button6.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(224, 43)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(36, 33)
		self._button6.TabIndex = 5
		self._button6.Text = "*"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.SystemColors.ControlDark
		self._button7.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(266, 43)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(36, 33)
		self._button7.TabIndex = 6
		self._button7.Text = "/"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.SystemColors.ControlDark
		self._button8.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(308, 5)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(36, 33)
		self._button8.TabIndex = 7
		self._button8.Text = "^"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.SystemColors.ControlDark
		self._button9.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(308, 43)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(36, 33)
		self._button9.TabIndex = 8
		self._button9.Text = "//"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(118, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 30)
		self._textBox1.TabIndex = 9
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(118, 44)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 30)
		self._textBox2.TabIndex = 10
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 11
		self._label1.Text = "Enter #:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 48)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 12
		self._label2.Text = "Enter #:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 82)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(206, 23)
		self._label3.TabIndex = 13
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(224, 80)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(36, 33)
		self._button1.TabIndex = 14
		self._button1.Text = "%"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(353, 161)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Name = "MainForm"
		self.Text = "Pg140SimpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button4Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(why) + int(wow)
		self._label3.Text = str(w)

	def Button5Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(wow) - int(why)
		self._label3.Text = str(w)

	def Button6Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(wow) * int(why)
		self._label3.Text = str(w)

	def Button7Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(wow) / int(why)
		self._label3.Text = str(w)

	def Button8Click(self, sender, e):
		 wow = str(self._textBox1.Text)
		 why = str(self._textBox2.Text)
		 w = int(wow) ** int(why)
		 self._label3.Text = str(w)

	def Button9Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(wow) // int(why)
		self._label3.Text = str(w)

	def Button1Click(self, sender, e):
		wow = str(self._textBox1.Text)
		why = str(self._textBox2.Text)
		w = int(wow) % int(why)
		self._label3.Text = str(w)