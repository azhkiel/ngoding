Imports System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel
Imports MySql.Data.MySqlClient
Imports Mysqlx
Imports Mysqlx.Crud

Public Class Form2
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        InsertOrder()
    End Sub
    
    Public Function GenerateOrderID() As String
        Dim newOrderID As String = ""
        Dim lastOrderID As String = ""

        ' Step 1: Get the last Order ID from the database
        Dim query As String = "SELECT order_id FROM orders ORDER BY order_id DESC LIMIT 1"
        Dim conn As MySqlConnection = GetConnection()
        Using command As New MySqlCommand(query, conn)
            Try
                Dim reader As MySqlDataReader = command.ExecuteReader()
                If reader.Read() Then
                    lastOrderID = reader("order_id").ToString()
                End If
                reader.Close()
            Catch ex As MySqlException
                MessageBox.Show("Error : " & ex.Message)
            Finally
                'Pastikan koneksi ditutup
                conn.Close()
            End Try
        End Using

        ' Step 2: Generate new Order ID based on the last Order ID
        If lastOrderID = "" Then
            ' If no records found, start with a base ID
            newOrderID = "ORD1001"
        Else
            ' Extract the numeric part and increment it
            Dim numericPart As Integer = Integer.Parse(lastOrderID.Substring(3)) ' Extracts the number after "ORD"
            numericPart += 1
            newOrderID = "ORD" & numericPart.ToString("D4") ' Formats to ensure 4 digits, e.g., ORD1002
        End If

        Return newOrderID
    End Function

    Public Sub InsertOrder()
        Dim orderID As String = txtOrderId.Text
        Dim orderDate As Date = DateTimePicker1.Value
        Dim customerName As String = txtCustomer.Text

        Dim query As String = "INSERT INTO orders (order_id, order_date, customer_name) VALUES (@orderID, @orderDate, @customerName)"
        'Panggil koneksi dari modul modKoneksi
        Dim conn As MySqlConnection = GetConnection()
        Using command As New MySqlCommand(query, conn)
            command.Parameters.AddWithValue("@orderID", orderID)
            command.Parameters.AddWithValue("@orderDate", orderDate)
            command.Parameters.AddWithValue("@customerName", customerName)

            Try
                command.ExecuteNonQuery()
                MessageBox.Show("Order successfully added with Order ID: " & orderID)
                RefreshForm()
            Catch ex As MySqlException
                MessageBox.Show("Error : " & ex.Message)
            Finally
                'Pastikan koneksi ditutup
                conn.Close()
            End Try
        End Using
    End Sub

    'Sub to clear form fields and reset components
    Private Sub RefreshForm()
        txtCustomer.Clear() ' Clear the customer name input
        txtCustomer.Focus() ' Set focus back to the customer name TextBox
        txtOrderId.Text = GenerateOrderID()
    End Sub

    Private Sub Form2_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        txtOrderId.Text = GenerateOrderID()
    End Sub
End Class
form9.txt
Displaying form9.txt.