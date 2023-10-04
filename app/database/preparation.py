from sqlalchemy import inspect
from app.model.webpage.schema import Webpage

Models = [Webpage]

def prepare_db(session):
    engine = session.get_bind()
    inspected_engine = inspect(engine)

    db_tables_names = inspected_engine.get_table_names()

    for model in Models:
        model_table_name = model.__tablename__
        if model_table_name in db_tables_names:
            model_columns = inspected_engine.get_columns(model_table_name)
            model_columns_names = [c["name"] for c in model_columns]

            mapper = inspect(model)

            for column_prop in mapper.attrs:
                    for model_column in column_prop.columns:
                        if model_column.key not in model_columns_names:
                            add_column(engine, model_table_name, model_column)
        else:
            model.__table__.create(engine)


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)

    command = 'ALTER TABLE %s ADD COLUMN %s %s' % (table_name, colu mn_name, column_type)

    if column.default is not None:
        is_int = isinstance(column.default.arg, int)
        if is_int:
            command = command + " DEFAULT {0}".format(column.default.arg)
        else:
            command = command + " DEFAULT '{0}'".format(column.default.arg)

    engine.execute(command)