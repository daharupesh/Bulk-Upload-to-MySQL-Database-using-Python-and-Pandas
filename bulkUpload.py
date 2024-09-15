import mysql.connector
import pandas as pd


def db_connect():
    '''Database connectivity'''
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ecommerce')
        if conn.is_connected():
            print('Database connected successfully.')
            return conn
        else:
            raise "Error while creating Database"
        
    except Exception as e:
        print(e)
        return None  

    

def create_table():
    '''Create_table use to create Table '''
    try:
        queryCreateTable= """
        CREATE TABLE IF NOT EXISTS Product (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2),
            image_url VARCHAR(255))
        """
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute(queryCreateTable)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table Product Created Successfully!")
    except:
        print('Error occur during creating table')    


def upload_Bulk_file(file_path):
    '''Uploads data from a bulk or csv file to the MySQL database one row at a time'''

    data = pd.read_csv(file_path)
    conn = db_connect()
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO product(name,description,price,image_url) VALUES (%s, %s, %s, %s)
    '''
    for index,row in data.iterrows():
         data_tuple = (row['name'], row['description'], row['price'], row['image_url'])
         cursor.execute(insert_query,data_tuple)
    
    
    conn.commit()    
    cursor.close()
    conn.close() 

    print("Data upload successfully!")
# Program start from here
if __name__ == '__main__':
    file_path = 'F:\BulkUploadingDatabase\dataset\product.csv' 
    create_table()
    print('---------------------------------------------')
    upload_Bulk_file(file_path)
   
    
