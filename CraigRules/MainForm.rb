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
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.Control
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 23.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(86, 207)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(114, 48)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ButtonFace
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 47.9999962, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(74, 34)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(276, 162)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.Control
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 23.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(221, 207)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(114, 48)
		@button3.TabIndex = 3
		@button3.Text = "Clear"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(433, 313)
		self.Controls.Add(@button3)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "CraigRules"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Craig Rules!!!"
	end

	def Button3Click(sender, e)
		@label1.Text = ""
	end
end

