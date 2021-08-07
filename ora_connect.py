import cx_Oracle as orax
import config as config
# dsn_tns = orax.makedsn(config.host, config.port, service_name=config.sid) # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
# conn = orax.connect(user=config.user, password=config.password, dsn=dsn_tns)
# connection = orax.connect(config.user, config.password, config.dsn)
# print(connection)
orax.init_oracle_client(lib_dir=r'<path_to_\\instantclient_19_6')
conn = orax.connect(config.user, config.password, config.dsn)
c = conn.cursor()
print("Executing.........")
c.execute('select * from table_name')
print(c.fetchone())
print("Connected")
