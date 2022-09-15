'''
    Module File for different type of database connection
'''

import psycopg2
import pymongo
import pyodbc
import mysql.connector

class MySqlConnection:
    '''
        Class for MsSql Connection
    '''
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        '''
            Create and return connection object
        '''
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )


class SybaseASEConnecion:
    '''
        Class for Sybase ASE Connection
    '''
    def __init__(self, server, port, user, password):
        self.server = server
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        '''
            Create and return connection object
        '''
        return pyodbc.connect(f'''DRIVER={{Devart ODBC Driver for ASE}};
                Server={self.server};Port={self.port};Database=master;
                User ID={self.user};Password={self.password};
                String Types=Unicode
            ''')


class PostgreSqlConnecion:
    '''
        Class for PostgreSQL Connection
    '''
    def __init__(self, host, port, database, user, password, sslmode='disable'):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.sslmode = sslmode

    def connect(self):
        '''
            Create and return connection object
        '''
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password,
            sslmode=self.sslmode
        )


class MongoDbConnection:
    '''
        Class for Mongo DB Connection
    '''
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        '''
            Create and return connection object
        '''
        return pymongo.MongoClient(
            host=self.host,
            port=self.port
        )
