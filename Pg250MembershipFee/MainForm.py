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
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._checkBox7 = System.Windows.Forms.CheckBox()
		self._checkBox8 = System.Windows.Forms.CheckBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(70, 232)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(194, 232)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 32)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(325, 232)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 32)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(225, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Type of Membership"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(12, 35)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(225, 24)
		self._checkBox1.TabIndex = 4
		self._checkBox1.Text = "Standard Adult"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(12, 56)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(225, 24)
		self._checkBox2.TabIndex = 5
		self._checkBox2.Text = "Child(12 and Under)"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.Location = System.Drawing.Point(12, 77)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(225, 24)
		self._checkBox3.TabIndex = 6
		self._checkBox3.Text = "Student"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox4.Location = System.Drawing.Point(12, 98)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(225, 24)
		self._checkBox4.TabIndex = 7
		self._checkBox4.Text = "Senior Citizen"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox6
		# 
		self._checkBox6.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox6.Location = System.Drawing.Point(255, 77)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(225, 24)
		self._checkBox6.TabIndex = 11
		self._checkBox6.Text = "Personal Trainer"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# checkBox7
		# 
		self._checkBox7.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox7.Location = System.Drawing.Point(256, 56)
		self._checkBox7.Name = "checkBox7"
		self._checkBox7.Size = System.Drawing.Size(225, 24)
		self._checkBox7.TabIndex = 10
		self._checkBox7.Text = "Karate"
		self._checkBox7.UseVisualStyleBackColor = True
		# 
		# checkBox8
		# 
		self._checkBox8.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox8.Location = System.Drawing.Point(256, 35)
		self._checkBox8.Name = "checkBox8"
		self._checkBox8.Size = System.Drawing.Size(225, 24)
		self._checkBox8.TabIndex = 9
		self._checkBox8.Text = "Yoga"
		self._checkBox8.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(256, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(225, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "Options"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(256, 129)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(225, 23)
		self._label3.TabIndex = 13
		self._label3.Text = "Membership Fees"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 129)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(225, 23)
		self._label4.TabIndex = 12
		self._label4.Text = "Membership Length"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(137, 158)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 28)
		self._textBox1.TabIndex = 14
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(256, 160)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(119, 23)
		self._label5.TabIndex = 17
		self._label5.Text = "Monthly Fee:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlDark
		self._label6.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(256, 194)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(119, 23)
		self._label6.TabIndex = 18
		self._label6.Text = "Total:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlDark
		self._label7.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 160)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(119, 23)
		self._label7.TabIndex = 19
		self._label7.Text = "# of Months:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlDark
		self._label8.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(381, 194)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 21
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlDark
		self._label9.Font = System.Drawing.Font("Modern No. 20", 14.249999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(381, 160)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 20
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(492, 273)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._checkBox6)
		self.Controls.Add(self._checkBox7)
		self.Controls.Add(self._checkBox8)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg250MembershipFee"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		NM = int(self._textBox1.Text)
		totalcost = 0
		if self._checkBox1.Checked == True:
			TC = 40
		if self._checkBox2.Checked == True:
			TC = 20
		if self._checkBox3.Checked == True:
			TC = 25
		if self._checkBox4.Checked == True:
			TC = 30
		if self._checkBox8.Checked == True:
			OC = 10
		if self._checkBox7.Checked == True:
			OC = 30
		if self._checkBox6.Checked == True:
			OC = 50
		pass
		if NM < 4:
			DC = 0
		elif NM > 3 and NM < 7:
			DC = .05
		elif NM > 6 and NM > 10:
			DC = .08
		else:
			DC = .10
		c = (OC + TC) * DC
		cost = OC + TC + c
		totalcost = int(cost) * int(NM)
		pass
		self._label8.Text = str(totalcost)
		self._label9.Text =  str(cost)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def MainFormLoad(self, sender, e):
		pass