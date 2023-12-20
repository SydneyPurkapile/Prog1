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
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlDark
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(35, 303)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(115, 53)
		@button1.TabIndex = 1
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlDark
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(206, 303)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(115, 53)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlDark
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(370, 303)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(115, 53)
		@button3.TabIndex = 3
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(23, 21)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(127, 33)
		@label1.TabIndex = 4
		@label1.Text = "Number1:"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(23, 54)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(127, 33)
		@label2.TabIndex = 10
		@label2.Text = "Number2:"
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(23, 87)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(127, 33)
		@label3.TabIndex = 11
		@label3.Text = "Number3:"
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		@label4.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(23, 120)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(127, 33)
		@label4.TabIndex = 12
		@label4.Text = "Number4:"
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(144, 21)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(115, 30)
		@textBox1.TabIndex = 13
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(144, 57)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(115, 30)
		@textBox2.TabIndex = 14
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(144, 90)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(115, 30)
		@textBox3.TabIndex = 15
		# 
		# textBox4
		# 
		@textBox4.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(144, 123)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(115, 30)
		@textBox4.TabIndex = 16
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.ControlDark
		@label5.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(88, 187)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(355, 28)
		@label5.TabIndex = 17
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::SystemColors.ControlDark
		@label6.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(88, 232)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(355, 28)
		@label6.TabIndex = 18
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(526, 394)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def TextBox1TextChanged(sender, e)
		
	end

	def Label2Click(sender, e)
		
	end

	def Button1Click(sender, e)
	
	end

	def Button1Click(sender, e)
		num1 = int(@textBox1.Text)
		num2 = int(@textBox2.Text)
		num3 = int(@textBox3.Text)
		num4 = int(@textBox4.Text)
		S = num1 + num2 + num3 + num4
		average = S / 4.0
		@label5.Text = "Sum: " + str(S)
		@label6.Text = "Average: " + str(average)
	end

	def Button2Click(sender, e)
		@label5.Text = ""
		@label6.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

