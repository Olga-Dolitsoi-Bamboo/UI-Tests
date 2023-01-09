DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'EC2AMAZ-QI33B5S'
DATABASE_NAME = 'Bamboo'
USERNAME = 'usrbamboo'
PASSWORD = 'DJ7xaAYY2vNMn8MygXK2'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid={USERNAME};
    pwd={PASSWORD};
"""
