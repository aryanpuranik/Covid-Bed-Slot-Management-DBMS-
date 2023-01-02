import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pes1ug20cs081_lab10"
)
c = mydb.cursor()



def create_bookingpatient_table():
    c.execute('CREATE TABLE IF NOT EXISTS `bookingpatient` ( `id` int(11) NOT NULL,srfid varchar(50) NOT NULL,bedtype varchar(50) NOT NULL,hcode varchar(50) NOT NULL,spo2 int(11) NOT NULL,pname varchar(50) NOT NULL,pphone varchar(12) NOT NULL,paddress text NOT NULL);')  
    # c.execute('CREATE TABLE IF NOT EXISTS `hospitaldata` (`id` int(11) NOT NULL,`hcode` varchar(200) NOT NULL,`hname` varchar(200) NOT NULL,`normalbed` int(11) NOT NULL,`hicubed` int(11) NOT NULL,`icubed` int(11) NOT NULL,`vbed` int(11) NOT NULL);')  
    # c.execute('CREATE TABLE IF NOT EXISTS `hospitaluser` (`id` int(11) NOT NULL,`hcode` varchar(20) NOT NULL,`email` varchar(100) NOT NULL,`password` varchar(1000) NOT NULL);')  
    # c.execute('CREATE TABLE IF NOT EXISTS `test` (`id` int(11) NOT NULL,`name` varchar(50) NOT NULL);')  
    # c.execute('CREATE TABLE IF NOT EXISTS `trig` (`id` int(11) NOT NULL,`hcode` varchar(50) NOT NULL,`normalbed` int(11) NOT NULL,`hicubed` int(11) NOT NULL,`icubed` int(11) NOT NULL,`vbed` int(11) NOT NULL,`querys` varchar(50) NOT NULL,`date` date NOT NULL);')  
    # c.execute('CREATE TABLE IF NOT EXISTS `user` (`id` int(11) NOT NULL,`srfid` varchar(20) NOT NULL,`email` varchar(100) NOT NULL,`dob` varchar(1000) NOT NULL);')  

def add_bookingpatient_table(q,w,e,r,t,y,u,i):
    c.execute('INSERT INTO bookingpatient (id, srfid, bedtype, hcode, spo2, pname, pphone, paddress) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(q,w,e,r,t,y,u,i))
    #,(3, 'KA20210011', 'ICUBed', 'MAT123', 85, 'ARK', '9986786453', 'bangalore'),(4, 'KA20210022', 'Normal Bed', 'BBH01', 92, 'kartik', '8088131784', 'bangalore '),(5 'KA20210033 'ICUBed', 'MAT123', 81, 'amogh', '8088828292', 'bangalore '),(6 'KA20210044 'HICUBed', 'BBH01', 95, 'chinmay', '9987728913', 'bangalore '),(7 'KA20210055 'ICUBed', 'BBH01', 88, 'Rida', '7348991204', 'bangalore '))
    mydb.commit()

def create_hospitaldata_table():
    c.execute('CREATE TABLE IF NOT EXISTS `hospitaldata` (`id` int(11) NOT NULL,`hcode` varchar(200) NOT NULL,`hname` varchar(200) NOT NULL,`normalbed` int(11) NOT NULL,`hicubed` int(11) NOT NULL,`icubed` int(11) NOT NULL,`vbed` int(11) NOT NULL);')  

def add_hospitaldata_table(q,w,e,r,t,y,u):
    c.execute('INSERT INTO `hospitaldata` (id, hcode, hname, normalbed, hicubed, icubed, vbed) VALUES(%s,%s,%s,%s,%s,%s,%s)',(q,w,e,r,t,y,u))
        #(3, 'MAT123', 'Matha Hospital', 40, 4, 4, 1),(4, 'BBH01', 'Apollo Hospital', 30, 3, 3, 1),(5, 'MAT123', 'Matha Hospital', 50, 2 , 4, 1),(6, 'BBH01', 'Apollo Hospital', 60, 4, 3, 1),(7, 'MAT123', 'Matha Hospital', 20, 5, 4, 2)")
    mydb.commit()

def create_hospitaluser_table():
    c.execute('CREATE TABLE IF NOT EXISTS `hospitaluser` (`id` int(11) NOT NULL,`hcode` varchar(20) NOT NULL,`email` varchar(100) NOT NULL,`password` varchar(1000) NOT NULL);')  


def add_hospitaluser_table(q,w,e,r):
    c.execute('INSERT INTO `hospitaluser` (id, hcode, email, password) VALUES (%s,%s,%s,%s)',(q,w,e,r))
    #(7, 'BBH01', 'aryanpuranik@gmail.com', 'abchs2:abs256:720000$im6PllE9qrd0asQY$3e62fcb9697d2b048acd83cb3658bac8ae5edb5ff58086699d134fb0ed41d788'),(9, 'MAT123', 'arkprocoder@gmail.com', 'pahff2:sha256:260000$CPDXGkSY1z3e62fcb9697dbec84d1b2c32e521c7048acd83cbaaa4f7a53e567eff580866944c53b11'),(11, 'BBH01', 'bdbdbb@gmail.com', 'pjadf2:cab256:260000$im6PllE9qrd0asQY$3e62fcb9697d2b048acd83cb3658bac8ae5edb5ff5d83cb3658134fb0ed41d2548'),(12, 'MAT123', 'dbmsdbms@gmail.com', 'pkjsd2:run256:260000$im6PllE9qrd0asQY$3e62fcb9697d2b04QY$3e62fcb9697cd83cb3658bac8086699d134fb0ed41d8943'),(15, 'BBH01', 'aryanpuar@gmail.com', 'sjkfn2:cla256:260000$im6PllE9qrd0asQY$3e62fcb9697d2b048acd83cb3658babac8ae5edb5fff58086699d134fb0ed41d24321')")
    mydb.commit()

def create_test_table():
    c.execute('CREATE TABLE IF NOT EXISTS `test` (`id` int(11) NOT NULL,`name` varchar(50) NOT NULL);')  

def add_test_table(q,w):
    c.execute('INSERT INTO `test` (id, name) VALUES (%s,%s)' ,(q,w) )
    #(1, 'aryan'), (2, 'ramesh'), (3, 'suresh'), (4, 'abhay'), (5, 'sumanth')")
    mydb.commit()
def create_trig_table():
    c.execute('CREATE TABLE IF NOT EXISTS `test` (`id` int(11) NOT NULL,`name` varchar(50) NOT NULL);') 
     
def add_trig_table(q,w,e,r,t,y,u,i):
    c.execute('INSERT INTO  `trig` (id, hcode, normalbed, hicubed, icubed, vbed, querys, date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (id, hcode, normalbed, hicubed, icubed, vbed, querys, date))
    #(1, 'BBH01', 50, 9, 4, 1, ' UPDATED', '2021-11-26'),(2, 'MAT123', 60, 2, 3, 2, ' DELETED', '2021-10-23'),(3, 'BBH01', 30, 7, 2, 1, ' DELETED', '2021-09-10'),(4, 'MAT123', 40, 8, 5, 3, ' UPDATED', '2021-10-15'),(5, 'BBH01', 50, 5, 3, 1, ' DELETED', '2021-11-12')")
    mydb.commit()   
def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS `user` (`id` int(11) NOT NULL,`srfid` varchar(20) NOT NULL,`email` varchar(100) NOT NULL,`dob` varchar(1000) NOT NULL);')  
   

def add_user_table(q,w,e,r):

    c.execute('INSERT INTO  `user` (id, srfid, email, dob) VALUES (%s,%s,%s,%s)' , (q,w,e,r))
    #(3, 'KA20210011', 'aryanpuranik@gmail.com', '2021-11-26'),(4, 'KA20210022', 'arkprocoder@gmail.com', '2021-10-23'),(5, 'KA20210033', 'bdbdbb@gmail.com', '2021-10-12'),(6, 'KA20210044', 'dbmsdbms@gmail.com', '2021-09-18'),(7, 'KA20210055', 'aryanpuar@gmail.com', '2021-11-12')")
    mydb.commit()




# def add_data(id, srfid, bedtype, hcode, spo2, pname,pphone, paddress):
#     c.execute("INSERT INTO bookingpatient (id, srfid, bedtype, hcode, spo2, pname, pphone, paddress) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)(3, 'KA20210011', 'ICUBed', 'MAT123', 85, 'ARK', '9986786453', 'bangalore'),(4, 'KA20210022', 'Normal Bed', 'BBH01', 92, 'kartik', '8088131784', 'bangalore '),(5 'KA20210033 'ICUBed', 'MAT123', 81, 'amogh', '8088828292', 'mangalore '),(6 'KA20210044 'HICUBed', 'BBH01', 95, 'chinmay', '9987728913', 'bangalore '),(7 'KA20210055 'ICUBed', 'MAT123', 88, 'Rida', '7348991204', 'mangalore ')")
#     c.execute("INSERT INTO `hospitaldata` (`id`, `hcode`, `hname`, `normalbed`, `hicubed`, `icubed`, `vbed`) VALUES(3, 'MAT123', 'Matha Hospital', 40, 4, 4, 1),(4, 'BBH01', 'Apollo Hospital', 30, 3, 3, 1),(5, 'MAT123', 'Matha Hospital', 50, 2 , 4, 1),(6, 'BBH01', 'Apollo Hospital', 60, 4, 3, 1),(7, 'MAT123', 'Matha Hospital', 20, 5, 4, 2)")
#     c.execute("INSERT INTO `hospitaluser` (`id`, `hcode`, `email`, `password`) VALUES (3, 'MAT123', 'aryanpuranik@gmail.com', 'abcd'),(4, 'BBH01', 'arkprocoder@gmail.com', 'mnop'),(5, 'MAT123', 'bdbdbb@gmail.com', 'qwerty'),(6, 'BBH01', 'dbmsdbms@gmail.com', 'asdfg'),(7, 'MAT123', 'aryanpuar@gmail.com', 'zxcvc')")
#     c.execute("INSERT INTO `test` (`id`, `name`) VALUES (3, 'ARK'), (4, 'kartik'), (5, 'amogh'), (6, 'chinmmay'), (7, 'Rida')")
#     c.execute("INSERT INTO  `trig` (`id`, `hcode`, `normalbed`, `hicubed`, `icubed`, `vbed`, `querys`, `date`) VALUES(1, 'BBH01', 50, 9, 4, 1, ' UPDATED', '2021-11-26'),(2, 'MAT123', 60, 2, 3, 2, ' DELETED', '2021-10-23'),(3, 'BBH01', 30, 7, 2, 1, ' DELETED', '2021-09-10'),(4, 'MAT123', 40, 8, 5, 3, ' UPDATED', '2021-10-15'),(5, 'BBH01', 50, 5, 3, 1, ' DELETED', '2021-11-12')")
#     c.execute("INSERT INTO  `user` (`id`, `srfid`, `email`, `dob`) VALUES (3, 'KA20210011', 'dbmsproj@gmail.com', '2021-11-26'),(4, 'KA20210022', 'rehman@gmail.com', '2021-10-23'),(5, 'KA20210033', 'bdbdbb@gmail.com.com', '2021-10-23'),(6, 'KA20210044', 'aryan@gmail.com', '2021-10-23'),(7, 'KA20210055', 'puranik@gmail.com', '2021-10-23')")

    #    mydb.commit()





def view_bookingpatient_data():
    c.execute('SELECT * FROM bookingpatient')
    data = c.fetchall()
    return data

def view_hospitaldata_data():
    c.execute('SELECT * FROM hospitaldata')
    data = c.fetchall()
    return data

def view_hospitaluser_data():
    c.execute('SELECT * FROM hospitaluser')
    data = c.fetchall()
    return data

def view_test_data():
    c.execute('SELECT * FROM test')
    data = c.fetchall()
    return data

def view_trig_data():
    c.execute('SELECT * FROM trig')
    data = c.fetchall()
    return data

def view_user_data():
    c.execute('SELECT * FROM user')
    data = c.fetchall()
    return data








def view_only_bookingpatient_id():
    c.execute('SELECT id FROM bookingpatient')
    data = c.fetchall()
    return data

def view_only_hospitaldata_id():
    c.execute('SELECT id FROM hospitaldata')
    data = c.fetchall()
    return data

def view_only_hospitaluser_id():
    c.execute('SELECT id FROM hospitaluser')
    data = c.fetchall()
    return data

def view_only_test_id():
    c.execute('SELECT id FROM test')
    data = c.fetchall()
    return data

def view_only_trig_id():
    c.execute('SELECT id FROM trig')
    data = c.fetchall()
    return data


def view_only_user_id():
    c.execute('SELECT id FROM user')
    data = c.fetchall()
    return data















def get_bookingpatient(id):
    c.execute('SELECT * FROM bookingpatient WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_hospitaldata(id):
    c.execute('SELECT * FROM hospitaldata WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_hospitaluser(id):
    c.execute('SELECT * FROM hospitaluser WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_test(id):
    c.execute('SELECT * FROM test WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_trig(id):
    c.execute('SELECT * FROM trig WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data

def get_user(id):
    c.execute('SELECT * FROM user WHERE id="{}"'.format(id))
    data = c.fetchall()
    return data














def update_bookingpatient_data( new_id, new_srfid, new_bedtype, new_hcode, new_spo2, new_pname, new_pphone, new_paddress, id ):
    c.execute("UPDATE bookingpatient SET id=%s,srfid=%s,bedtype=%s,hcode=%s,spo2=%s,pname=%s, pphone=%s,paddress=%s WHERE id=%s ", (new_id, new_srfid, new_bedtype, new_hcode, new_spo2,new_pname,new_pphone,new_paddress, id))
    mydb.commit()


def update_hospitaldata_data( new_id, new_hcode, new_hname, new_normalbed, new_hicubed, new_icubed, new_vbed , id ):
    c.execute("UPDATE hospitaldata SET id=%s,hcode=%s,hname=%s,normalbed=%s,hicubed=%s,icubed=%s , vbed=%s WHERE id=%s", (new_id, new_hcode, new_hname, new_normalbed, new_hicubed, new_icubed, new_vbed , id))
    mydb.commit()

def update_hospitaluser_data( new_id,new_hcode, new_email , new_password , id ):
    c.execute("UPDATE hospitaluser SET id=%s,hcode=%s , email=%s , password=%s WHERE id=%s", (new_id , new_hcode, new_email , new_password, id))
    mydb.commit()

def update_test_data( new_id, new_name , id ):
    c.execute("UPDATE test SET id=%s, name=%s WHERE id=%s", (new_id, new_name, id))
    mydb.commit()


# def update_trig_data( new_id, new_hcode, new_hname, new_normalbed, new_hicubed, new_icubed, new_vbed , id ):
#     c.execute("UPDATE trig SET id=%s,hcode=%s,hname=%s,normalbed=%s,hicubed=%s,icubed=%s , vbed=%s WHERE id=%s", (new_id, new_hcode, new_hname, new_normalbed, new_hicubed, new_icubed, new_vbed , id))
#     mydb.commit()



def update_user_data( new_id, new_srfid, new_email , new_dob , id ):
    c.execute("UPDATE user SET id=%s,srfid=%s,email=%s,dob=%s WHERE id=%s", (new_id, new_srfid, new_email , new_dob , id ))
    mydb.commit()










def delete_bookingpatient_data(id):
    c.execute('DELETE FROM bookingpatient WHERE id="{}"'.format(id))
    mydb.commit()


def delete_hospitaldata_data(id):
    c.execute('DELETE FROM hospitaldata WHERE id="{}"'.format(id))
    mydb.commit()


def delete_hospitaluser_data(id):
    c.execute('DELETE FROM hospitaluser WHERE id="{}"'.format(id))
    mydb.commit()


def delete_test_data(id):
    c.execute('DELETE FROM test WHERE id="{}"'.format(id))
    mydb.commit()


def delete_trig_data(id):
    c.execute('DELETE FROM trig WHERE id="{}"'.format(id))
    mydb.commit()


def delete_user_data(id):
    c.execute('DELETE FROM user WHERE id="{}"'.format(id))
    mydb.commit()









def procedure_call(id):
    c.callproc('hospital_name',[id])
    x=[]
    for result in c.stored_results():
        mission= result.fetchall()
        for launch in mission:
            x.append(launch)
    return x