""" Provides a class to interact with the database """
import os
from google.auth.credentials import AnonymousCredentials
from google.cloud.firestore import Client
from database.database_abstract import DatabaseAbstract

class LocalDatabase(DatabaseAbstract):
    """ Write to local database"""
    def __init__(self):
        super().__init__()
        project_id = 'dummy-project-id'
        os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8080"

        cred = AnonymousCredentials()
        self.db = Client(project=project_id, credentials=cred)

        self._init_database_handlers()
