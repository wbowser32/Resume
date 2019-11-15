import pandas as pd
import teradata

host, username, password = 'HOST', 'UID', 'PWD'
# Make a connection
udaExec = teradata.UdaExec(appName="test", version="1.0", logConsole=False)

with udaExec.connect(method="odbc", system="", username='', password='', authentication="LDAP", driver="Teradata Database ODBC Driver 16.10") as connect:

    query = "SELECT * FROM PRD_MRDR_DMV.SKU_MASTER WHERE Staples_Sku in (2439452, 24401599);"

# Reading query to df
    df = pd.read_sql(query, connect)
    cols = ['staples_Item_No', 'Shipped_Item_Id']
    for col in cols:
        df[col] = df[col].str.replace('-','')
# do something with df,e.g.
#df['staples_Item_No'] = df['staples_Item_No'].map(lambda x: re.sub(r'\W+', '', x))
#print(df)
    df.to_csv(r'C:\Users\')
