require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@label6 = System::Windows::Forms::Label.new()
		@label7 = System::Windows::Forms::Label.new()
		@label8 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.Control
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(69, 29)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(219, 31)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.Control
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(69, 69)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(219, 31)
		@label2.TabIndex = 1
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.Control
		@label3.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(69, 110)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(219, 31)
		@label3.TabIndex = 2
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.Control
		@label4.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(69, 151)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(219, 31)
		@label4.TabIndex = 3
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.Control
		@label5.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(69, 191)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(219, 31)
		@label5.TabIndex = 4
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		@label6.BackColor = System::Drawing::SystemColors.Control
		@label6.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label6.Location = System::Drawing::Point.new(69, 234)
		@label6.Name = "label6"
		@label6.Size = System::Drawing::Size.new(219, 31)
		@label6.TabIndex = 5
		@label6.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		@label7.BackColor = System::Drawing::SystemColors.Control
		@label7.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label7.Location = System::Drawing::Point.new(69, 277)
		@label7.Name = "label7"
		@label7.Size = System::Drawing::Size.new(219, 31)
		@label7.TabIndex = 6
		@label7.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		@label8.BackColor = System::Drawing::SystemColors.Control
		@label8.Font = System::Drawing::Font.new("Modern No. 20", 15.749999, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label8.Location = System::Drawing::Point.new(69, 320)
		@label8.Name = "label8"
		@label8.Size = System::Drawing::Size.new(219, 31)
		@label8.TabIndex = 7
		@label8.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.Control
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 21.7499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(52, 364)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(111, 50)
		@button1.TabIndex = 8
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.Control
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 21.7499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(192, 364)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(111, 50)
		@button2.TabIndex = 9
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(371, 447)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label8)
		self.Controls.Add(@label7)
		self.Controls.Add(@label6)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Biology"
		@label2.Text = "9/10 English Honors"
		@label3.Text = "Computor Programing"
		@label4.Text = "Algebra 2"
		@label5.Text = "Art 1"
		@label6.Text = "Chinese 2"
		@label7.Text = "Concert Band"
		@label8.Text = "AP Human Geography"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
		@label6.Text = ""
		@label7.Text = ""
		@label8.Text = ""
	end
end

