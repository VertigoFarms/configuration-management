import sqlite3

class DB:
    __FILENAME__ = "data.db"
    __TABLE__ = "DEVICES"

    def __init__(self):
        self.connection = sqlite3.connect(DB.__FILENAME__)
        self.__create_table()

    def __execute(self, statement):
        with self.connection as con:
            data = con.execute(statement)
            return data

    def __create_table(self):
        return self.__execute(f"""
            CREATE TABLE IF NOT EXISTS {DB.__TABLE__} (
                device INTEGER NOT NULL PRIMARY KEY,
                type TEXT,
                status TEST,
                configuration TEXT,
                UNIQUE(device)
            );
        """)


    def __find_device(self, device):
        return self.__execute(f"SELECT * FROM {DB.__TABLE__} WHERE device == {device}")

    def read_status(self, device):
        return self.__execute(f"""
            SELECT status
            FROM {DB.__TABLE__}
            WHERE device = {device}
        """)

    def write_status(self, device, status):
        return self.__execute(f"""
            UPDATE {DB.__TABLE__}
            SET status = {status}
            WHERE device = {device};
        """)
