#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging 

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger( __name__ )

'''
def update_db_indexes(cursor):
    commands = (
        """REINDEX DATABASE transactional""",
    )
    try:
        for command in commands:
            cursor.execute(command)
    except Exception as e:
        logger.exception("Error in update_db_indexes: %s", e)
        return -1
    else:
        logger.info("update_db_indexes run successfully")
        return 0

def move_data_archives(cursor):
    commands = (
        """INSERT INTO archive_orders SELECT * from orders
        WHERE order_date < '2017-01-01' """,
        """DELETE from orders WHERE order_date < '2017-01-01'
        """,
    )
    try:
        for command in commands:
            cursor.execute(command)
    except Exception as e:
        logger.exception("Error in move_data_archives: %s", e)
        return -1
    else:
        logger.info("move_data_archives run successfully")
        return 0
'''


def db_status_handler(db_script_function):
    def inner(cursor):
        commands = db_script_function(cursor)
        function_name = db_script_function.__qualname__
        try:
            for command in commands:
                cursor.execute(command)
        except Exception as e:
            logger.exception("Error in %s: %s", function_name, e)
            return -1
        else:
            logger.info("%s run successfully", function_name)
            return 0
    return inner


@db_status_handler
def update_db_indexes(cursor):
    return (
        """REINDEX DATABASE transactional""",
    )


@db_status_handler
def move_data_archives(cursor):
    return (
        """INSERT INTO archive_orders SELECT * from orders
        WHERE order_date < '2017-01-01' """,
        """DELETE from orders WHERE order_date < '2017-01-01'
        """,
    )
