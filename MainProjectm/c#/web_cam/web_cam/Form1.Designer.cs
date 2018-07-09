namespace web_cam
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.cam1TItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cam2TItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cam3TItem = new System.Windows.Forms.ToolStripMenuItem();
            this.moreToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cam4ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.cam5ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // cam1TItem
            // 
            this.cam1TItem.BackColor = System.Drawing.Color.White;
            this.cam1TItem.Name = "cam1TItem";
            this.cam1TItem.Size = new System.Drawing.Size(53, 20);
            this.cam1TItem.Text = "Cam 1";
            this.cam1TItem.Click += new System.EventHandler(this.cam1TItem_Click);
            // 
            // cam2TItem
            // 
            this.cam2TItem.Name = "cam2TItem";
            this.cam2TItem.Size = new System.Drawing.Size(53, 20);
            this.cam2TItem.Text = "Cam 2";
            this.cam2TItem.Click += new System.EventHandler(this.cam2TItem_Click);
            // 
            // cam3TItem
            // 
            this.cam3TItem.Name = "cam3TItem";
            this.cam3TItem.Size = new System.Drawing.Size(53, 20);
            this.cam3TItem.Text = "Cam 3";
            this.cam3TItem.Click += new System.EventHandler(this.cam3TItem_Click);
            // 
            // moreToolStripMenuItem
            // 
            this.moreToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cam4ToolStripMenuItem,
            this.toolStripSeparator1,
            this.cam5ToolStripMenuItem});
            this.moreToolStripMenuItem.Name = "moreToolStripMenuItem";
            this.moreToolStripMenuItem.Size = new System.Drawing.Size(47, 20);
            this.moreToolStripMenuItem.Text = "More";
            // 
            // cam4ToolStripMenuItem
            // 
            this.cam4ToolStripMenuItem.Name = "cam4ToolStripMenuItem";
            this.cam4ToolStripMenuItem.Size = new System.Drawing.Size(108, 22);
            this.cam4ToolStripMenuItem.Text = "Cam 4";
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(105, 6);
            // 
            // cam5ToolStripMenuItem
            // 
            this.cam5ToolStripMenuItem.Name = "cam5ToolStripMenuItem";
            this.cam5ToolStripMenuItem.Size = new System.Drawing.Size(108, 22);
            this.cam5ToolStripMenuItem.Text = "Cam 5";
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cam1TItem,
            this.cam2TItem,
            this.cam3TItem,
            this.moreToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(674, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(0, 27);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(672, 336);
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(674, 370);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.menuStrip1);
            this.Name = "Form1";
            this.Text = "Live Cam ( No Cam )";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ToolStripMenuItem cam1TItem;
        private System.Windows.Forms.ToolStripMenuItem cam2TItem;
        private System.Windows.Forms.ToolStripMenuItem cam3TItem;
        private System.Windows.Forms.ToolStripMenuItem moreToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cam4ToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem cam5ToolStripMenuItem;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}

