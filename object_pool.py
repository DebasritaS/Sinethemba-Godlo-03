class DBConnection:
    def __init__(self, id):
        self.id = id

class ConnectionPool:
    def __init__(self, size):
        self.pool = [DBConnection(i) for i in range(size)]
        self.in_use = []

    def acquire(self):
        conn = self.pool.pop()
        self.in_use.append(conn)
        return conn

    def release(self, conn):
        self.in_use.remove(conn)
        self.pool.append(conn)
        
class Connection:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Connection(id={self.id})"



class ConnectionPool:
    def __init__(self, size):
        self.size = size
        self.connections = []  # You can initialize the pool as a list or any other structure
        self._initialize_connections()

    
    def _initialize_connections(self):
        # Pre-fill the pool with 'size' number of connections
        for i in range(self.size):
            self.connections.append(f"Connection {i+1}")

    def acquire(self):
        if self.connections:
            return self.connections.pop()
        else:
            raise Exception("No available connections")

    def release(self, connection):
        self.connections.append(connection)


    def get_connection(self):
        if len(self.connections) > 0:
            return self.connections.pop()
        else:
            # Logic for creating a new connection
            return "New connection"

    def return_connection(self, connection):
        self.connections.append(connection)
class Connection:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Connection(id={self.id})"  # This represents the connection as a string


class ConnectionPool:
    def __init__(self, size):
        self.size = size
        self.connections = [Connection(i) for i in range(size)]  # Creating connection objects
        self.available_connections = self.connections.copy()

    def acquire(self):
        if self.available_connections:
            connection = self.available_connections.pop()  # This should be a Connection object
            return connection
        else:
            return None

    def release(self, connection):
        if connection not in self.available_connections:
            self.available_connections.append(connection)

# Usage
pool = ConnectionPool(size=10)
conn1 = pool.acquire()
conn2 = pool.acquire()
pool.release(conn1)
conn3 = pool.acquire()
print(conn3.id)  # Should be reused connection
