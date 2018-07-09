using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;
using System.Data.OleDb;

namespace server
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public int i = 0;
        public void refresh()
        { textBox3.Text = i.ToString(); i++; }

        public TcpListener myList;
        IPAddress ipAd;
        public string tcp_msg;
        void insert_tcp_message_values()
        {

         DateTime dtr = DateTime.Now;          
         con.Open();
         command.CommandText = "insert into cam_data VALUES (  'cam" + tcp_msg[0] + "', 'location" + tcp_msg[0] + "', " + tcp_msg[1] + ", " + tcp_msg[2] + ", " + tcp_msg[3] + "," + tcp_msg[4] + "," + yesorno( tcp_msg[5] ) + "," + yesorno(tcp_msg[6]) + "," + yesorno(tcp_msg[7]) + "," + yesorno(tcp_msg[8]) + ",'" + dtr + "');";
         command.ExecuteNonQuery();
         con.Close();
                
           // MessageBox.Show("inserted");
        }
        public string yesorno(char s)
        {
            if (s == '1')
                return "Yes";
            else
                return "No";
        }


        public void server_func_sing()
        {
            try
            {
                IPAddress ipAd = IPAddress.Parse(textBox1.Text);
                TcpListener myList = new TcpListener(IPAddress.Any, int.Parse(textBox2.Text));
                myList.Start();

               
               while (true)        {

                Socket s = myList.AcceptSocket();
                byte[] b = new byte[1000];
                int k = s.Receive(b);
                string str = "";
                for (int i = 0; i < k; i++)
                    str += Convert.ToChar(b[i]);

                tcp_msg = str;
                if (str != "")
                    textBox3.Text = str;
               
                ASCIIEncoding asen = new ASCIIEncoding();
                s.Send(asen.GetBytes("SERVER: Data Recieved"));
                s.Close();
                    if (tcp_msg.Length == 9)
                        insert_tcp_message_values();

               //*
                        if (str == "QUIT")
                        break;
                }//*/

                myList.Stop();
                //MessageBox.Show(tcp_msg.Length.ToString());
            }
            catch (Exception e)
            {
                MessageBox.Show("Error.\n" + e.StackTrace);
            }
           
        }
        
        public void db_connect() { 

        string s = "";
        ofd.Filter = "Access DataBase (*.accdb) | *.accdb";

            if (ofd.ShowDialog() == DialogResult.OK)
                s = ofd.FileName;
            
            // string s = AppDomain.CurrentDomain.BaseDirectory + @"Rubber_Hoses.accdb";

            try
            { 
                con.ConnectionString = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + s + ";Jet OLEDB:Database Password=12345678";
                command.Connection = con;
            }
            catch (Exception)
            {             MessageBox.Show("DB error!");            }
            
        }

    public void db_function(string str, int n)
    { /*
    con.Open();
    OleDbDataReader res;
    command.CommandText = "Select Machine from Billet_Heating";
    res = command.ExecuteReader();
    while (res.Read())
    {
        billet_heating_machine_type.Items.Add(res["Machine"]);
    }
    con.Close();
    // */
    con.Open();
    command.CommandText = "UPDATE test_data SET msg =" + "'" + str + "'" + ",num = " + n + " where ID=" + 1+ ";";
    command.ExecuteNonQuery();
    con.Close();

        }


private void button1_Click(object sender, EventArgs e)
        {
            server_func_sing();
            
        }
        public OleDbConnection con = new OleDbConnection();
        public OleDbCommand command = new OleDbCommand();
        public OpenFileDialog ofd = new OpenFileDialog();
        private void Form1_Load(object sender, EventArgs e)
        {
            db_connect();
        }
}
}
