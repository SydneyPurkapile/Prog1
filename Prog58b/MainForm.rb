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
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlDark
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(12, 131)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(119, 45)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlDark
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(141, 131)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(119, 45)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlDark
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(266, 131)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(119, 45)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(74, 35)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(36, 30)
		@textBox1.TabIndex = 6
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ControlDark
		@label4.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(32, 82)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(159, 33)
		@label4.TabIndex = 11
		@label4.Text = "Square Root:"
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.ControlDark
		@label5.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(197, 82)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(159, 33)
		@label5.TabIndex = 12
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label5.Click { |sender, e| self.Label5Click(sender, e) }
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(116, 42)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(55, 23)
		@label1.TabIndex = 13
		@label1.Text = "x^2 + "
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(219, 42)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(41, 23)
		@label2.TabIndex = 14
		@label2.Text = "x + "
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(177, 35)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(36, 30)
		@textBox2.TabIndex = 15
		@textBox2.TextChanged { |sender, e| self.TextBox2TextChanged(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(266, 35)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(36, 30)
		@textBox3.TabIndex = 16
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(398, 193)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		
	end

	def Button2Click(sender, e)
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Label3Click(sender, e)
		
	end

	def Label5Click(sender, e)
		
	end

	def TextBox2TextChanged(sender, e)
		
	end

	def Button2Click(sender, e)
		@label5.Text = ""
	end

	def Button3Click(sender, e)
		
	end
end

