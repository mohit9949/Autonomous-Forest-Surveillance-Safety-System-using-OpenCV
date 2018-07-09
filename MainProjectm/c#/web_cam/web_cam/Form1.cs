using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Video;
using AForge.Video.DirectShow;
using AForge;

namespace web_cam
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            stream = new MJPEGStream("http://192.168.1.104:8081/");
            stream.NewFrame += Stream_NewFrame;
            
        }

        private void Stream_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            Bitmap bmp = (Bitmap)eventArgs.Frame.Clone();
            pictureBox1.Image = bmp;
        }

        MJPEGStream stream;
       

        private void cam1TItem_Click(object sender, EventArgs e)
        {
            menu_click("cam1");
            cam1TItem.BackColor = Color.LightSteelBlue;
            stream.Start();
            

        }
        public void menu_click(string cm)
        {
          
            this.Text = "Live Cam ( " + cm + " )";

            cam1TItem.BackColor = Color.White;
            cam2TItem.BackColor = Color.White;
            cam3TItem.BackColor = Color.White;
           

        }

        private void cam2TItem_Click(object sender, EventArgs e)
        {
            menu_click("cam2");
            stream.Stop();
            cam2TItem.BackColor = Color.LightSteelBlue;
        }

        private void cam3TItem_Click(object sender, EventArgs e)
        {
           menu_click("cam3");
            cam3TItem.BackColor = Color.LightSteelBlue;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
