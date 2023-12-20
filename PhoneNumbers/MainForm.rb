require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.Control
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 21.7499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(103, 234)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(114, 55)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.Control
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(89, 39)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(257, 28)
		@label1.TabIndex = 1
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.Control
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 21.7499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(223, 234)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(114, 55)
		@button2.TabIndex = 2
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.Control
		@label2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(89, 77)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(257, 28)
		@label2.TabIndex = 3
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.Control
		@label3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(89, 114)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(257, 28)
		@label3.TabIndex = 4
		@label3.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.Control
		@label4.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(89, 151)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(257, 28)
		@label4.TabIndex = 5
		@label4.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		@label5.BackColor = System::Drawing::SystemColors.Control
		@label5.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label5.Location = System::Drawing::Point.new(89, 189)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(257, 28)
		@label5.TabIndex = 6
		@label5.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(433, 336)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@button2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "(608)-756-5511"
		@label2.Text = "(608)-754-3095"
		@label3.Text = "(608)-756-2611"
		@label4.Text = "(608)-754-8331"
		@label5.Text = "(608)-758-0268"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end

	def Label1Click(sender, e)
		
	end
end

