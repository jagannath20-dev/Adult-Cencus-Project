from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class Connector():
    def __init__(self):
        """
        Description : Creates a connection with Database when backend thread runs.
        """
        self.Client_id ='lpkcPpBicnbGibOGzUDwcQjQ'
        self.Client_secret = 'b4Ok+BJWuX,sSdK,++Z_97W+HEkBQZy-+levpn,bPop1qSt.sdkSB_86vcm9r4Up_I0xxqLkMt6NUjbPl+jZxNJpxmdRRWtfwWKJ7T3Pqk,py+Zt5Apk4Jnx4,HAul6G'
        cloud_config = {'secure_connect_bundle': 'secure-connect-adult-cencus-prediction.zip'}
        auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
    def master(self):
        """
        Description : Creates table in the database.
        """
        self.session.execute("adult_cencus")
        self.session.execute("select release version from system.local")
        self.session.execute("Create Table Data(id PRIMARY KEY ,workclass text,fnlwgt int,education text,education_num int,Age int,Sex text,capital-gain int,capital-loss int,Hours-Per-Week int,Country text,,occupation text,relationship text,marital-status text,race text);")

    def add_data(self,result):
        """
          Parameters result : Get Data from user and put it into database

        """

        column = "id,Age,Sex,fnlwgt,workclass,education,education_num,marital-status,occupation,relationship,race,capital-gain,capital-loss,Hours-Per-Week,Country"
        value = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format('id', result['Age'], result['Sex'],
                                                             result['capital-gain'], result['capital-loss'],
                                                             result['Hours-Per-Week'], result['Country'],
                                                             result['fnlwgt'],result['workclass'],['education_num'],
                                                             result['education'],result['marital-status'],result['occupation'],
                                                             result['relationship'],result['race'])
        custom = "Insert into Data({}); ".format(column,value)

        self.session.execute("USE adult_cencus")

        output = self.session.execute(custom)

    def get_data(self):
        """
         Description : Retrieve the data from database


        """
        self.session.execute("use adult_cencus")
        row = self.session.execute("SELECT * FROM Data;")
        collection = []
        for i in row:
            collection.append(tuple(i))
            return tuple(collection)







