require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlDark
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(449, 235)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(118, 45)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlDark
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(449, 286)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(118, 45)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlDark
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(449, 337)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(118, 45)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ControlLight
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(51, 52)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(97, 32)
		@label1.TabIndex = 3
		@label1.Text = "Radius"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(140, 54)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(158, 30)
		@textBox1.TabIndex = 4
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ControlDark
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(95, 118)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(384, 32)
		@label2.TabIndex = 5
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ControlDark
		@label3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(95, 177)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(384, 32)
		@label3.TabIndex = 6
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(579, 394)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label2Click(sender, e)
		
	end
	
	def Button1Click(sender, e)
		radius = float(@textBox1.Text)
		pi = 3.14159
		area = pi * radius ** 2
		area = round(area, 3)
		circum = radius * 2 * pi
		circum = round(circum, 3)
		@label2.Text = "Area: " + str(area)
		@label3.Text = "Circumference: " + str(circum)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

