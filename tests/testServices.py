import unittest
# from mongomock import MongoClient as MongoClientMock
from src.repository.database import repository


class TestStringMethods(unittest.TestCase):

    def test_the_returned_is_the_expedted_one(self):
        return True


        # p_send_message(123,321,11,"Hollo")
        # from_to = p_chat_history(123,321)
        # self.assertEqual(
        #     { "chats": [
        #         {"user_from": 123, "user_to":321, "timestamp":11, "message":"Hollo"}
        #     ] },
        #     from_to
        # )
    