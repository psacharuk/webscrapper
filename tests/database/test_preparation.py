import unittest
from unittest.mock import Mock, MagicMock, patch
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, String
from app.database.preparation import prepare_db, add_column
from app.model.webpage.schema import Webpage

class TestDatabasePreparation(unittest.TestCase):

    @patch('app.database.preparation.add_column')
    @patch('app.database.preparation.inspect', autospec=True)
    def test_prepare_db_when_model_is_created(self, mock_inspect, mock_add_column):
        mock_session = Mock()
        mock_engine = create_engine('sqlite:///:memory:')
        mock_session.get_bind.return_value = mock_engine
        mock_inspected_engine = MagicMock()
        mock_inspect.side_effect = [mock_inspected_engine]

        mock_table_names = ['webpages']
        mock_inspected_engine.get_table_names.return_value = mock_table_names
        mock_model_columns = [{'name': 'webpage.sample'}]
        mock_inspected_engine.get_columns.return_value = mock_model_columns

        mock_mapper = MagicMock()
        mock_mapper.attrs = [MagicMock()]
        mock_columns = [Column('webpage.sample', String(256)), Column('webpage.sample2', Integer)]
        mock_mapper.attrs[0].columns = mock_columns

        mock_inspect.side_effect.append(mock_mapper)

        prepare_db(mock_session)

        self.assertEqual(mock_add_column.call_count, len(mock_columns) - len(mock_model_columns))

    @patch('app.database.preparation.inspect', autospec=True)
    def test_prepare_db_when_model_is_not_created(self, mock_inspect):
        mock_session = Mock()
        mock_engine = create_engine('sqlite:///:memory:')
        mock_session.get_bind.return_value = mock_engine
        mock_inspected_engine = MagicMock()
        mock_inspect.return_value = mock_inspected_engine

        mock_inspected_engine.get_table_names.return_value = []

        mock_create = MagicMock()
        Webpage.__table__ = MagicMock(create=mock_create)

        prepare_db(mock_session)
        mock_create.assert_called_once_with(mock_engine)

    def test_add_column(self):
        mock_engine = create_engine('sqlite:///:memory:')
        mock_engine.execute = Mock()
        mock_metadata = MetaData()
        mock_table = Table('test_table', mock_metadata, Column('id', Integer, primary_key=True))

        add_column(mock_engine, 'test_table', Column('new_column', Integer))
        mock_table.append_column(Column('new_column', Integer))
        self.assertIn('new_column', mock_table.columns.keys())
        mock_engine.execute.assert_called_once()
