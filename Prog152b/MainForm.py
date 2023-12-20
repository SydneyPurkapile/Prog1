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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ControlDark
		self._button1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 244)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ControlDark
		self._button2.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(117, 244)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 32)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlDark
		self._button3.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(223, 244)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 32)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._textBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(190, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(65, 30)
		self._textBox1.TabIndex = 3
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._listBox1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(12, 42)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(310, 196)
		self._listBox1.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(83, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(77, 24)
		self._label1.TabIndex = 5
		self._label1.Text = "Input:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(334, 283)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog152b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		Sum = 0
		nums = 0
		heading = "Even Integers\tSum"
		self._listBox1.Items.Add(heading)
		while Sum < num:
			nums += 2
			Sum += nums
			msg = str(nums) + "\t\t" + str(Sum)
			self._listBox1.Items.Add(msg)
		#for nums in range(2, num + 2, 2):
			#Sum += nums
			#msg = str(nums) + "\t\t" + str(Sum)
			#self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()