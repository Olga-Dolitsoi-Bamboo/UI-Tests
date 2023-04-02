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

CLIENT_QUERY = """ DELETE FROM [Bamboo].[dbo].[Clients] 
        WHERE Clients.Name='Olga UI autotests1' or Clients.Name='Olga UI autotests2' 
        or Clients.Name='Olga UI autotests4'"""

BRANDS_QUERY = """  DELETE FROM [Bamboo].[dbo].[Brands]
  WHERE Name='Olga UI test brand'"""

PRODUCTS_QUERY = """DELETE FROM [Bamboo].[dbo].[Products]
        WHERE Products.Name='UI test NI product 1'"""
CATALOG_QUERY = """DELETE FROM [Bamboo].[dbo].[Catalogs]
        WHERE Catalogs.Name='UI test Catalog 1'"""

CATALOG_CLIENT_QUERY = """UPDATE [Bamboo].[dbo].[Clients]
        SET CatalogId=NULL
        WHERE Clients.Name='UI test do not change'"""
