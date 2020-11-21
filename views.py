from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
import pymysql
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime

def ViewPurchase(request):
    if request.method == 'GET':
        
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Inventory ID</th><th>Product Ecode</th><th>Supplier Or Purchaser Name</th>'
        output+='<th>Supplier Or Purchaser Address</th><th>Received Or Sold Quantity</th><th>Available Quantity</th>'
        output+='<th>Manufacture Date</th><th>Received Or Sold Date</th><th>Inventory Type</th><th>Image</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM inventory")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                ids = row[0]
                code = row[1]
                name = row[2]
                address = row[3]
                quantity = str(row[4])
                avail = str(row[5])
                date1 = str(row[6])
                date2 = str(row[7])
                inventory_type = row[8]
                if inventory_type == 'Received':
                    output+='<td><font size="" color="black">'+str(ids)+'</td><td><font size="" color="black">'+code+'</td><td><font size="" color="black">'+name+'</td><td><font size="" color="black">'+address+'</td><td><font size="" color="black">'+quantity+'</td>'
                    output+='<td><font size="" color="black">'+avail+'</td><td><font size="" color="black">'+date1+'</td><td><font size="" color="black">'+date2+'</td><td><font size="" color="black">'+inventory_type+'</td>'
                    output+='<td><img src=/static/products/'+code+'.png width=200 height=200></img></td></tr>'
        
        #print(output)        
        context= {'data':output}
        return render(request, 'ViewPurchase.html', context) 

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Login(request):
    if request.method == 'GET':
       return render(request, 'Login.html', {})

def Admin(request):
    if request.method == 'GET':
       return render(request, 'Admin.html', {})    

def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})   

def AddProduct(request):
    if request.method == 'GET':
       return render(request, 'AddProduct.html', {})

def ViewInventory(request):
    if request.method == 'GET':
        
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Inventory ID</th><th>Product Ecode</th><th>Supplier Or Purchaser Name</th>'
        output+='<th>Supplier Or Purchaser Address</th><th>Received Or Sold Quantity</th><th>Available Quantity</th>'
        output+='<th>Manufacture Date</th><th>Received Or Sold Date</th><th>Inventory Type</th><th>Image</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM inventory")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                ids = row[0]
                code = row[1]
                name = row[2]
                address = row[3]
                quantity = str(row[4])
                avail = str(row[5])
                date1 = str(row[6])
                date2 = str(row[7])
                inventory_type = row[8]
                output+='<td><font size="" color="black">'+str(ids)+'</td><td><font size="" color="black">'+code+'</td><td><font size="" color="black">'+name+'</td><td><font size="" color="black">'+address+'</td><td><font size="" color="black">'+quantity+'</td>'
                output+='<td><font size="" color="black">'+avail+'</td><td><font size="" color="black">'+date1+'</td><td><font size="" color="black">'+date2+'</td><td><font size="" color="black">'+inventory_type+'</td>'
                output+='<td><img src=/static/products/'+code+'.png width=200 height=200></img></td></tr>'
        
        #print(output)        
        context= {'data':output}
        return render(request, 'ViewInventory.html', context)    

def UpdateInventory(request):
    if request.method == 'GET':
        output = ''
        output+='<tr><td><b>Product&nbsp;Ecode</b></td><td><select name="t1">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select Product_Ecode FROM addproduct")
            rows = cur.fetchall()
            for row in rows:
                output+='<option value='+row[0]+'>'+row[0]+'</option>'
        output+='</select></td></tr>'
        output+='<tr><td><b>Supplier&nbsp;Or&nbsp;Purchaser&nbsp;Name</b></td><td><input type="text" name="t2" style="font-family: Comic Sans MS" size="30"/></td></tr>'
        output+='<tr><td><b>Supplier&nbsp;Or&nbsp;Purchaser&nbsp;Address</b></td><td><input type="text" name="t3" style="font-family: Comic Sans MS" size="40"/></td></tr>'
        output+='<tr><td><b>Quantity</b></td><td><input type="text" name="t4" style="font-family: Comic Sans MS" size="10"/></td></tr>'
        output+='<tr><td><b>Inventory Type</b></td><td><select name="t5"><option value=Received>Received</option><option value=Supplied></option></select></td></tr>'
        output+='<tr><td></td><td><input type="submit" value="Submit"></table><br/><br/><br/></body></html>'
        context= {'data':output}
        return render(request, 'UpdateInventory.html', context)

def checkStatus(order_id):
    status = 0
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select order_id FROM payment where order_id='"+str(order_id)+"'")
        rows = cur.fetchall()
        for row in rows:
            status = 1
            break
    return status

def getAddress(name):
    address = "none"
    contact = "none"
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select address,contact FROM register where username='"+name+"'")
        rows = cur.fetchall()
        for row in rows:
            address = row[0]
            contact = row[1]
            break
    return address,contact
    
def CompleteOrderAction(request):
    if request.method == 'POST':
        order = request.POST.get('t1', False)
        total = request.POST.get('t2', False)
        paying = request.POST.get('t3', False)
        discount = request.POST.get('t4', False)
        mode = request.POST.get('t5', False)
        cheque = request.POST.get('t6', False)
        bank = request.POST.get('t7', False)
        status = request.POST.get('t8', False)
        code = request.POST.get('t9', False)
        pname = request.POST.get('t10', False)
        address = request.POST.get('t11', False)
        qty = request.POST.get('t12', False)

        status = updateInventory(code,pname,address,qty,'Supplied')
        if status == 1:
            now = datetime.datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")

            ids = getId('payment')

            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO payment(payment_id,order_id,total_amount,paid_amount,discount_amount,payment_mode,cheque_no,bank_name,payment_date,status) VALUES('"
            student_sql_query+=str(ids)+"','"+str(order)+"','"+str(total)+"','"+str(paying)+"','"+str(discount)+"','"+str(mode)+"','"+str(cheque)+"','"+str(bank)+"','"+str(current_time)+"','"+str(status)+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                context= {'data':'Order Completed Successfully'}
                return render(request, 'ViewOrders.html', context)
            else:
                context= {'data':'Error in completing order'}
                return render(request, 'ViewOrders.html', context)
        else:
            context= {'data':'Insufficient Quantity in Inventory'}
            return render(request, 'ViewOrders.html', context)
    
def CompleteOrder(request):
    if request.method == 'GET':
        order = request.GET['order']
        amt = request.GET['amt']
        code = request.GET['code']
        pname = request.GET['pname']
        address = request.GET['address']
        qty = request.GET['qty']
        output = ''
        output+='<tr><td><b>Order&nbsp;ID</b></td><td><input type="text" name="t1" value="'+order+'" style="font-family: Comic Sans MS" size="15" readonly/></td></tr>'
        output+='<tr><td><b>Total&nbsp;Amount</b></td><td><input type="text" name="t2" value="'+amt+'" style="font-family: Comic Sans MS" size="20" readonly/></td></tr>'
        output+='<tr><td><b>Product&nbsp;Ecode</b></td><td><input type="text" name="t9" value="'+code+'" style="font-family: Comic Sans MS" size="20" readonly/></td></tr>'
        output+='<tr><td><b>Purchaser</b></td><td><input type="text" name="t10" value="'+pname+'" style="font-family: Comic Sans MS" size="20" readonly/></td></tr>'
        output+='<tr><td><b>Purchaser&nbsp;Address</b></td><td><input type="text" name="t11" value="'+address+'" style="font-family: Comic Sans MS" size="20" readonly/></td></tr>'
        output+='<tr><td><b>Quantity</b></td><td><input type="text" name="t12" value="'+qty+'" style="font-family: Comic Sans MS" size="20" readonly/></td></tr>'
        context= {'data':output}
        return render(request, 'CompleteOrder.html', context)
        
    

def ViewOrders(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=1 align=center width=100%><tr><th>Order ID</th><th>Purchaser Name</th><th>Product Ecode</th><th>Order Date</th>'
        output+='<th>Quantity</th><th>Amount</th><th>Address</th><th>Contact No</th><th>Image</th><th>Complete Order</th></tr>'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM customer_order")
            rows = cur.fetchall()
            output+='<tr>'
            for row in rows:
                order = row[0]
                pname = row[1]
                code = row[2]
                date = str(row[3])
                qty = str(row[4])
                amt = str(row[5])
                address,contact = getAddress(pname)
                output+='<td><font size="" color="black">'+str(order)+'</td><td><font size="" color="black">'+pname+'</td><td><font size="" color="black">'+str(code)+'</td><td><font size="" color="black">'+date+'</td><td><font size="" color="black">'+qty+'</td>'
                output+='<td><font size="" color="black">'+amt+'</td><td><font size="" color="black">'+address+'</td><td><font size="" color="black">'+contact+'</td>'
                output+='<td><img src=/static/products/'+code+'.png width=200 height=200></img></td>'
                if checkStatus(order) == 0:
                    output+='<td><a href=\'CompleteOrder?order='+str(order)+'&amt='+amt+'&code='+code+'&pname='+pname+'&address='+address+'&qty='+qty+'\'>Click Here</a></td></tr>'
                else:
                    output+='<td><font size="" color="black">Order Completed</td></tr>'
        #print(output)        
        context= {'data':output}
        return render(request, 'ViewOrders.html', context)
    
def BookOrder(request):
    if request.method == 'GET':
        output = ''
        output+='<table border=0 align=center ><tr><td><b>Product Ecode</b></td><td><select name="t1">'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select Product_Ecode FROM addproduct")
            rows = cur.fetchall()
            for row in rows:
                output+='<option value='+row[0]+'>'+row[0]+'</option>'
        output+='</select></td></tr>'
        output+='<tr><td><b>Quantity</b></td><td><input type="text" name="t2" style="font-family: Comic Sans MS" size="10"/></td></tr>'
        output+='<tr><td></td><td><input type="submit" value="Submit"></table><br/><br/><br/></body></html>'
        context= {'data':output}
        return render(request, 'BookOrder.html', context)
        
def getPrice(name):
    price = 0
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select Recommended_Price FROM addproduct where Product_Ecode='"+name+"'")
        rows = cur.fetchall()
        for row in rows:
            price = row[0]
            break
    return price        

def BookOrderAction(request):
    if request.method == 'POST':
        ecode = request.POST.get('t1', False)
        quantity = request.POST.get('t2', False)
        user = ''
        with open("session.txt", "r") as file:
            for line in file:
                user = line.strip('\n')
        ids = getId('customer_order');
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        price = getPrice(ecode);
        amount = price * float(quantity)
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO customer_order(order_id,purchaser_name,Product_Ecode,purchase_date,quantity,amount) VALUES('"+str(ids)+"','"+user+"','"+ecode+"','"+current_time+"','"+quantity+"','"+str(amount)+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        print(db_cursor.rowcount, "Record Inserted")
        if db_cursor.rowcount == 1:
            context= {'data':'Order Confirmed'}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Error in confirming order'}
            return render(request, 'UserScreen.html', context)
        
        


def getId(name):
    ids = 0
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select count(*) from "+name)
        rows = cur.fetchall()
        for row in rows:
            ids = row[0]
    return ids + 1          
    

def updateInventory(ecode,name,address,quantity,inventory_type):
    avail = 0
    con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
    with con:
        cur = con.cursor()
        cur.execute("select available_quantity FROM inventory where Product_Ecode='"+ecode+"'")
        rows = cur.fetchall()
        for row in rows:
            avail = row[0]
    status = 0
    if avail > float(quantity):
        avail = avail - float(quantity)
        status = 1
    if status == 1:
        ids = getId("inventory")
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d")
        db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO inventory(id,Product_Ecode,supplier_or_purchaser_name,supplier_or_purchaser_address,received_or_sold_quantity,"
        student_sql_query+="available_quantity,manufacture_date,received_or_sold_date,inventory_type) VALUES('"+str(ids)+"','"
        student_sql_query+=ecode+"','"+name+"','"+address+"','"+quantity+"','"+str(avail)+"','"
        student_sql_query+=str(current_time)+"','"+str(current_time)+"','"+inventory_type+"')"
        db_cursor.execute(student_sql_query)
        db_connection.commit()
    return status        
    

def UpdateInventoryAction(request):
    if request.method == 'POST':
      ecode = request.POST.get('t1', False)
      name = request.POST.get('t2', False)
      address = request.POST.get('t3', False)
      quantity = request.POST.get('t4', False)
      inventory_type= request.POST.get('t5', False)

      avail = 0

      con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
      with con:
          cur = con.cursor()
          cur.execute("select available_quantity FROM inventory where Product_Ecode='"+ecode+"'")
          rows = cur.fetchall()
          for row in rows:
              avail = row[0]
      status = 0        
      if inventory_type == 'Received':
          avail = avail + float(quantity)
          status = 1
      if inventory_type == 'Supplied':
          if avail > float(quantity):
              avail = avail - float(quantity)
              status = 1

      if status == 1:
          ids = getId("inventory")
          now = datetime.datetime.now()
          current_time = now.strftime("%Y-%m-%d")
          db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
          db_cursor = db_connection.cursor()
          student_sql_query = "INSERT INTO inventory(id,Product_Ecode,supplier_or_purchaser_name,supplier_or_purchaser_address,received_or_sold_quantity,"
          student_sql_query+="available_quantity,manufacture_date,received_or_sold_date,inventory_type) VALUES('"+str(ids)+"','"
          student_sql_query+=ecode+"','"+name+"','"+address+"','"+quantity+"','"+str(avail)+"','"
          student_sql_query+=str(current_time)+"','"+str(current_time)+"','"+inventory_type+"')"
          db_cursor.execute(student_sql_query)
          db_connection.commit()
          print(db_cursor.rowcount, "Record Inserted")
          if db_cursor.rowcount == 1:
              status = 2
      if status == 2:
          context= {'data':'Inventory Details Updated'}
          return render(request, 'AdminScreen.html', context)
      else:
          context= {'data':'Insufficient Quantity in Inventory. Available Quantity : '+str(avail)}
          return render(request, 'AdminScreen.html', context)  
              

      

def AddProductData(request):
    if request.method == 'POST':
      ecode = request.POST.get('t1', False)
      horse = request.POST.get('t2', False)
      stages = request.POST.get('t3', False)
      pumpset_model = request.POST.get('t4', False)
      old_model= request.POST.get('t5', False)
      outlet_size = request.POST.get('t6', False)
      starting_method = request.POST.get('t7', False)
      price = request.POST.get('t8', False)
      price_type = request.POST.get('t9', False)
      myfile = request.FILES['t10']

      fs = FileSystemStorage()
      filename = fs.save('C:/Python/BMS/BMSApp/static/products/'+str(ecode)+'.png', myfile)

      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO addproduct(Product_Ecode,HP_KW,Num_Stages,Pumpset_Model,Old_Model,Outlet_Size_MM ,method_Starting,Recommended_Price,"
      student_sql_query+="Price_Type,image) VALUES('"+str(ecode)+"','"+horse+"','"+stages+"','"+pumpset_model+"','"+old_model+"','"+outlet_size+"','"
      student_sql_query+=starting_method+"','"+price+"','"+price_type+"','"+str(ecode)+".png')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Product Details Added'}
       return render(request, 'AddProduct.html', context)
      else:
       context= {'data':'Error in adding product details'}
       return render(request, 'AddProduct.html', context)
    
    
    
def Signup(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      contact = request.POST.get('contact', False)
      email = request.POST.get('email', False)
      address = request.POST.get('address', False)
      utype = request.POST.get('type', False)
      db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
      db_cursor = db_connection.cursor()
      student_sql_query = "INSERT INTO register(username,password,contact,email,address,usertype) VALUES('"+username+"','"+password+"','"+contact+"','"+email+"','"+address+"','"+utype+"')"
      db_cursor.execute(student_sql_query)
      db_connection.commit()
      print(db_cursor.rowcount, "Record Inserted")
      if db_cursor.rowcount == 1:
       context= {'data':'Signup Process Completed'}
       return render(request, 'Register.html', context)
      else:
       context= {'data':'Error in signup process'}
       return render(request, 'Register.html', context)

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'Admin.html', context)          
        
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        utype = 'none'
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'BMS',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and row[1] == password:
                    utype = 'success'
                    break
        if utype == 'success':
            file = open('session.txt','w')
            file.write(username)
            file.close()
            context= {'data':'welcome '+username}
            return render(request, 'UserScreen.html', context)
        if utype == 'none':
            context= {'data':'Invalid login details'}
            return render(request, 'Login.html', context)        
        
        
