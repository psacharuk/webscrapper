import unittest
from unittest.mock import Mock, patch
from app.database.connection import select_all, select_from_db, insert_into_db, update_db, delete_from_db

select_expected_result = ['result1', 'result2']

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.mock_session = Mock()
        self.mock_obj = Mock()

    def __assert_commit_and_close_called_once(self):
        self.mock_session.commit.assert_called_once()
        self.mock_session.close.assert_called_once()

    def test_select_all_with_success(self):
        mock_query = Mock()
        mock_result = select_expected_result
        mock_query.all.return_value = mock_result

        result = select_all(mock_query)
        mock_query.all.assert_called_once()
        self.assertEqual(result, mock_result)

    def test_select_all_with_failed(self):
        mock_query = Mock()
        mock_query.all.side_effect = Exception()

        result = select_all(mock_query)
        mock_query.all.assert_called_once()
        self.assertEqual(result, None)

    def test_select_from_db(self):
        self.mock_session.query.return_value = self.mock_session
        self.mock_session.all.return_value = select_expected_result

        result = select_from_db(self.mock_obj, session=self.mock_session)
        self.mock_session.query.assert_called_once_with(self.mock_obj)
        self.mock_session.all.assert_called_once()
        self.mock_session.close.assert_called_once()
        self.assertEqual(result, select_expected_result)

    @patch('app.database.connection.session_factory')
    def test_insert_into_db(self, mock_session_factory):
        mock_session_factory.return_value = self.mock_session
        self.__run_insert_into_db(None)

    def test_insert_into_db_with_custom_session(self):
        self.__run_insert_into_db(self.mock_session)

    def __run_insert_into_db(self, mock_session):
        insert_into_db(self.mock_obj, session=mock_session)
        self.mock_session.add.assert_called_once_with(self.mock_obj)
        self.__assert_commit_and_close_called_once()

    @patch('app.database.connection.session_factory')
    def test_update_db(self, mock_session_factory):
        mock_session_factory.return_value = self.mock_session
        self.__run_update_db(None)

    def test_update_db_with_custom_session(self):
        self.__run_update_db(self.mock_session)

    def __run_update_db(self, mock_session):
        attrs_to_update = {'attribute1': 'value1', 'attribute2': 'value2'}
        update_db(self.mock_obj, attrs_to_update=attrs_to_update, session=mock_session)

        for key, value in attrs_to_update.items():
            self.assertEqual(getattr(self.mock_obj, key), value)
        self.__assert_commit_and_close_called_once()

    @patch('app.database.connection.session_factory')
    def test_delete_from_db(self, mock_session_factory):
        mock_session_factory.return_value = self.mock_session
        self.__run_delete_from_db(None)

    def test_delete_from_db_with_custom_session(self):
        self.__run_delete_from_db(self.mock_session)

    def __run_delete_from_db(self, mock_session):
        delete_from_db(self.mock_obj, mock_session)
        self.mock_session.delete.assert_called_once_with(self.mock_obj)
        self.__assert_commit_and_close_called_once()