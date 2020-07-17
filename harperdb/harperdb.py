from .harperdb_base import *


class HarperDB(HarperDBBase):

    """ Each instance of HarperDB represents a running HarperDB instance at a
    URL, passed to the constructor. Optionally implement Basic Auth as keyword
    arguments.  HarperDB API functions are exposed as instance methods, which
    produce and consume JSON following the API documentation.

    Instance Parameters:
      - url (string): Full URL of HarperDB instance
      - username (string): (optional) Basic Auth username
      - password (string): (optional) Basic Auth password
      - timeout (float): Seconds to wait for a server response, default 10

    Instance Attributes:
      - token (string): Value used in Authorization header, or None. The value
        is generated automatically when instantiated with both username and
        password
      - timeout (float): Seconds to wait for a server response
      - url (string): Full URL of HarperDB instance

    Instance Methods:
    These methods expose the HarperDB API functions, and return JSON from the
    target database instance at HarperDB.url
      Schemas and Tables:
        - describe_all()
        - create_schema(schema)
        - describe_schema(schema)
        - drop_schema(schema)
        - create_table(schema, table, hash_attribute)
        - describe_table(schema, table)
        - drop_table(schema, table)
        - drop_attribute(schema, table, attribute)
      NoSQL Operations:
        - insert(schema, table, [records])
        - update(schema, table, [records])
        - delete(schema, table, [hashes])
        - search_by_hash(schema, table, [hashes], get_attributes=['*'])
        - search_by_value(schema,
                          table,
                          search_attribute,
                          search_value,
                          get_attributes=['*'])
      SQL Operations:
        - sql(SQL)
      CSV Operations:
        - csv_data_load(schema, table, path, action="insert")
        - csv_file_load(schema, table, file_path, action="insert")
        - csv_url_load(schema, table, csv_url, action="insert")
      Users and Roles:
        - add_user(role id, username, password, active=True)
        - add_role(name, permission)
        - alter_user(role, username, password, active=True)
        - alter_role(id, permission)
        - drop_role(id)
        - drop_user(username)
        - user_info(username)
        - list_roles()
        - list_users()
      Clustering:
        - add_node(name, host, port, subscriptions)
        - update_node(name, host, port, subscriptions)
        - remove_node(name)
        - cluster_status()
      Jobs:
        - get_job(id)
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_schema = self._create_schema
        self.drop_schema = self._drop_schema
        self.describe_schema = self._describe_schema
        self.create_table = self._create_table
        self.describe_table = self._describe_table
        self.describe_all = self._describe_all
        self.drop_table = self._drop_table
        self.drop_attribute = self._drop_attribute
        self.insert = self._insert
        self.update = self._update
        self.delete = self._delete
        self.search_by_hash = self._search_by_hash
        self.search_by_value = self._search_by_value
        self.sql = self._sql
        self.csv_data_load = self._csv_data_load
        self.csv_file_load = self._csv_file_load
        self.csv_url_load = self._csv_url_load
        self.get_job = self._get_job
        self.add_user = self._add_user
        self.add_role = self._add_role
        self.alter_user = self._alter_user
        self.alter_role = self._alter_role
        self.drop_role = self._drop_role
        self.drop_user = self._drop_user
        self.user_info = self._user_info
        self.list_roles = self._list_roles
        self.list_users = self._list_users
        self.add_node = self._add_node
        self.update_node = self._update_node
        self.remove_node = self._remove_node
        self.cluster_status = self._cluster_status
