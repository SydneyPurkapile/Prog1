﻿require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(110, 219)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(110, 45)
		@button1.TabIndex = 0
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 20.2499981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(242, 219)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(108, 45)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ActiveBorder
		@label1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(95, 51)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(271, 151)
		@label1.TabIndex = 2
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(468, 331)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "AboutMe"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "I have 2 sibling, 6 cats, 2 guinea pigs, 1 bearded dragon, 1 mouse, and a fishtank full of fish."
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

