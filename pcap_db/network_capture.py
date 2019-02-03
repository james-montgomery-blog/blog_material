import sys
import database

conn = database.create_connection("./network_data.db")

table_name = "pcap_data"

sql_str = """
CREATE TABLE IF NOT EXISTS {} (
    id integer PRIMARY KEY,
    protocol text NOT NULL,
    epoch_time text NOT NULL
);
""".format(table_name)

database.create_table(conn, sql_str)

for row in sys.stdin:

    if row != "Capturing on 'Wi-Fi'\n" and "packets" not in row:
        entry = row.replace("\n","").split(",")
        fields = ['protocol', 'epoch_time']
        entry_id = database.create_entry(conn, table_name, fields, entry)

database.select_all(conn, table_name)
