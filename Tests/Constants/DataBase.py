DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'bamboodev.chf1hdgo2dts.us-east-2.rds.amazonaws.com'
DATABASE_NAME = 'Bamboo'
USERNAME = 'usrbamboo'
PASSWORD = 'gwoGakxhxdswxorGpFwE'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid={USERNAME};
    pwd={PASSWORD};
"""

CLIENT_QUERY = """DELETE FROM [Bamboo].[dbo].[Clients] 
        WHERE Clients.Name='Olga UI autotests1' and Clients.Name='Olga UI autotests2' 
        and Clients.Name='Olga UI autotests4'"""
