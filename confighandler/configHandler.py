import configparser as cp

class configHandler:

    def __init__(self,filename):
        self.filename = filename

    def __str__(self):
        return self.filename

    def generateConfigFile(self):
        # This is a hardcoded schema with default values
        write_config = cp.ConfigParser()

        write_config.add_section("mongodb")
        write_config.set("mongodb", "dbserver", "mongodb://localhost:27017/")

        write_config.add_section("mysql")
        write_config.set("mysql", "dbserver", "localhost")
        write_config.set("mysql", "user", "root")
        write_config.set("mysql", "passwd", "mysql")

        write_config.add_section("cassandra")
        write_config.set("cassandra", "user", "atulgaikwad")

        if('.ini' in self.filename):
            configFile = self.filename
        else:
            configFile = self.filename + ".ini"

        fw = open(configFile, 'w')
        write_config.write(fw)
        fw.close()

    def readConfigFile(self,section):
        read_config = cp.ConfigParser()

        if ('.ini' in self.filename):
            configFile = self.filename
        else:
            configFile = self.filename + ".ini"

        read_config.read(configFile)

        if(section == "mongodb"):
            return read_config.get(section,"dbserver")
        elif(section == "mysql"):
            return read_config.get(section,"dbserver"),read_config.get(section, "user"),read_config.get(section, "passwd")
        elif (section == "cassandra"):
            return read_config.get(section, "user"),read_config.get(section, "passwd")
        else:
            return 'No section found'




if (__name__ == "__main__"):
    ch = configHandler("dbconnections.ini")
    #Uncomment below line to generate ini file
    #ch.generateConfigFile()
    res = ch.readConfigFile("mongodb")
    print(res)
    print(type(res))