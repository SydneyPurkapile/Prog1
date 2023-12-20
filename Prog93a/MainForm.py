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
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 305)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(80, 345)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 34)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(136, 385)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(130, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "KWH used:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(151, 5)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(87, 30)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Base Rate:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 102)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(130, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Surcharge:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 141)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(130, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Citytax:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 193)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(130, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Amount Due:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlDark
		self._label6.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 232)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(130, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Pay if Late:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlDark
		self._label7.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(148, 232)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(90, 23)
		self._label7.TabIndex = 14
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlDark
		self._label8.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(148, 193)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(90, 23)
		self._label8.TabIndex = 13
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlDark
		self._label9.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(148, 141)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(90, 23)
		self._label9.TabIndex = 12
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ControlDark
		self._label10.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(148, 102)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(90, 23)
		self._label10.TabIndex = 11
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ControlDark
		self._label11.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(148, 64)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(90, 23)
		self._label11.TabIndex = 10
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(250, 431)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		KWH = int(self._textBox1.Text)
		BR = KWH * .0475
		BR = round(BR,2)
		SC = BR * .10
		SC = round(SC,2)
		CT = BR * .03
		CT = round(CT,2)
		PA = BR + SC + CT
		PA = round(PA,2)
		LP = PA * 1.04
		LP = round(LP,2)
		self._label11.Text = "$" + str(BR)
		self._label10.Text = "$" + str(SC)
		self._label9.Text = "$" + str(CT)
		self._label8.Text = "$" + str(PA)
		self._label7.Text = "$" + str(LP)

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()