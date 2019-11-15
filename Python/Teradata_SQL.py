import pandas as pd
import teradata
import re

host, username, password = 'HOST', 'UID', 'PWD'
# Make a connection
udaExec = teradata.UdaExec(appName="test", version="1.0", logConsole=False)

with udaExec.connect(method="odbc", system="", username='', password='', authentication="LDAP", driver="Teradata Database ODBC Driver 16.10") as connect:

    #query = "SELECT TOP 3 order_no As Staples_order_no, bill_to_id AS Sell FROM PRD_USD_OPV.SOMS_YFS_ORDER_HEADER_V as oh INNER JOIN PRD_USD_OPV.SOMS_YFS_ORDER_LINE_V as ol ON oh.order_header_key = ol.order_header_key;"
    #query = open(r'C:\Users\BowDa001\Desktop\Ruchi.sql','r')
    #query = open(r'C:\Users\BowDa001\Desktop\GDW PROD LATEST QUERY BY USHA.sql','r')
    query = "SELECT TOP 3 \
oh.order_no As Staples_order_no, \
oh.CUSTOMER_PO_NO AS External_Document_No, \
oh.bill_to_id AS Sell_to_Customer_no, \
oh.EXTN_CUST_COMPANY_NAME AS customer_name, \
opi.state AS Ship_To_State, \
opi.zip_code AS ZipCode, \
yp.payment_Type AS method_of_payment, \
orstat.status AS status, \
ys.description as Status_Description, \
ol.original_ordered_qty, \
orstat.status_quantity AS status_quantity, \
ssd.ship_node as Ship_Node, \
ol.unit_price, \
ol.unit_price*ol.Ordered_Qty  AS MerchandizeDollar, \
ole.decimal_3 AS Marketplace_TAX, \
ol.tax AS staples_TAX, \
ssd.shipment_type AS Shipment_Type, \
ysn.description AS WhoelsalerName_Vendor#_FC#, \
ol.item_id AS staples_Item_No, \
ssd.Shipped_Item_Id,\
ol.extn_vendor_part_number AS Vendor_Part_No,\
ol.customer_item AS EXTERNAL_ITEM_NO, \
ol.Unit_Cost, unit_cost * ol.ordered_Qty AS Ext_Cost, \
ol.ordered_Qty AS Quantity, \
ol.extn_accounting_loc AS Accounting_location, \
oh.createts AS Create_date, \
ssd.ship_date AS SHIP_Date, \
ssd.del_date AS Delivery_date \
FROM PRD_USD_OPV.SOMS_YFS_ORDER_HEADER_V as oh \
INNER JOIN PRD_USD_OPV.SOMS_YFS_ORDER_LINE_V as ol ON oh.order_header_key = ol.order_header_key \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_ORDER_release_status_V as orstat ON ol.order_line_key = orstat.order_line_key AND orstat.status_quantity>0 \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_PERSON_INFO_V as opi ON oh.ship_to_key = opi.person_info_key \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_SPLS_SHIPMENT_DETAILS_V as ssd ON ol.order_line_key=ssd.orderline_key and ssd.status NOT IN('InActive') \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_ORDER_LINE_EXTENSION_V as ole ON ol.order_line_key=ole.order_line_key \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_PAYMENT_V as yp ON oh.order_header_key=yp.order_header_key \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_STATUS_V as ys ON orstat.status=ys.status \
LEFT OUTER JOIN PRD_USD_OPV.SOMS_YFS_SHIP_NODE_V as ysn ON ssd.ship_node=trim(ysn.ship_node) \
WHERE oh.extn_order_channel = 'HITOUCH' AND oh.document_type = '0001' AND ys.process_type_key= 'ORDER_FULFILLMENT' and oh.order_header_key >= '20191104' order by oh.order_no;"
    # Reading query to df
    #query.read()
    df = pd.read_sql(query, connect)
    df['staples_Item_No'] = df['staples_Item_No'].map(lambda x: re.sub(r'\W+', '', x))
    df['Shipped_Item_Id'] = df['Shipped_Item_Id'].map(lambda x: re.sub(r'\W+', '', x))
# do something with df,e.g.
    #print(df)
    df.to_csv(r'C:\Users\')


#-- ((unit_price * Ordered_Qty) - (Unit_Cost * Ordered_Qty)) / (unit_price * Ordered_Qty)ASGross_Margin, \
#-- (((unit_price * Ordered_Qty) - (Unit_Cost * Ordered_Qty)) / (unit_price * Ordered_Qty)) * 100ASGross_Mar_Perc, \
