---
url: https://docs.cloud.google.com/sql/docs/mysql/charset-collation/
title: Update the character set and collation for a database \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:40.206801+00:00
---

# Update the character set and collation for a database  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/charset-collation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Update the character set and collation for a database Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to update the character set and collation of Cloud SQL databases.

## Overview

When you create a database in Cloud SQL for MySQL, you can specify the [character set and collation](https://dev.mysql.com/doc/refman/8.0/en/charset-general.html) configuration for a database. If you don't specify custom values for these settings, then the database uses the default value. In MySQL, you can specify custom values for the character set and collation at different object levels, including databases, tables, and columns. For more information about using character set and collation configurations in MySQL, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/8.0/en/charset.html).

If you want to change the character set or collation of your database after you've already created the database and some objects in the database, then you can do so by following the procedure in this document.

This procedure consists of the following steps:

  1. Check current character set and collation values.
  2. Determine what level of update to perform.
  3. Take a backup of the instance.
  4. Generate rebuild commands for stored database objects.
  5. Perform updates to your databases, and if necessary, tables and columns.
  6. Validate the updates and look for errors.
  7. Recreate your stored database objects.
  8. Take another backup of the instance.



## Check the current character set and collation values

Check the existing values that are configured for character set and collation for your database and database objects. When you check your database, you also need to check the configuration of its tables, columns, and stored objects. You can use the following statements to check your databases and its database objects.

### Check your instance configuration

To check the default global values on the instance (server) level, start a MySQL shell and enter the following command:
    
    
    mysql> SELECT @@character_set_server,@@collation_server;

Example output:
    
    
    +------------------------+--------------------+
    | @@character_set_server | @@collation_server |
    +------------------------+--------------------+
    | utf8mb4                | utf8mb4_0900_ai_ci |
    +------------------------+--------------------+
    1 row in set (0.00 sec)
    

You can check that the default global values are different from the custom values that you'll provide for your database later.

### Check your database configuration

To check the existing character set and collation values on the database level, use the following statement. After you run each statement, make a list of all the databases and database objects that you need to update with new character sets or collation values. The list depends on which databases you want to change and how many tables, columns, and database objects require configuration updates.
    
    
    SELECT * FROM INFORMATION_SCHEMA.SCHEMATA
    WHERE schema_name
    NOT IN ('performance_schema', 'mysql', 'sys', 'information_schema');

For example, you receive the following output:
    
    
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    | CATALOG_NAME | SCHEMA_NAME | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH | DEFAULT_ENCRYPTION |
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    | def          | test1       | utf8mb4                    | utf8mb4_0900_ai_ci     |     NULL | NO                 |
    | def          | test2       | utf8mb4                    | utf8mb4_0900_ai_ci     |     NULL | NO                 |
    | def          | test3       | utf8mb4                    | utf8mb4_0900_ai_ci     |     NULL | NO                 |
    | def          | test4       | utf8mb4                    | utf8mb4_0900_ai_ci     |     NULL | NO                 |
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    

However, you want to change the databases to the following custom character set values:
    
    
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    | CATALOG_NAME | SCHEMA_NAME | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH | DEFAULT_ENCRYPTION |
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    | def          | test1       | ascii                      | ascii_general_ci       |     NULL | NO                 |
    | def          | test2       | latin1                     | latin1_swedish_ci      |     NULL | NO                 |
    | def          | test3       | utf16                      | utf16_general_ci       |     NULL | NO                 |
    | def          | test4       | ucs2                       | ucs2_general_ci        |     NULL | NO                 |
    +--------------+-------------+----------------------------+------------------------+----------+--------------------+
    

Then, in this case, for each database that has a value that you want to change, you need to update each object that resides in the database.

### Check the configuration of your tables

To check the existing values for the tables, use the following statement:
    
    
    SELECT T.table_name, T.table_schema, CCSA.character_set_name, CCSA.collation_name
    FROM information_schema.`tables` T,
      information_schema.`collation_character_set_applicability` CCSA
    WHERE CCSA.collation_name = T.table_collation
    AND T.table_schema
    NOT IN ('performance_schema', 'mysql', 'sys','information_schema');

Example output:
    
    
    +------------+--------------+--------------------+-------------------+
    | TABLE_NAME | TABLE_SCHEMA | CHARACTER_SET_NAME | COLLATION_NAME    |
    +------------+--------------+--------------------+-------------------+
    | t1         | test1        | ascii              | ascii_general_ci  |
    | t2         | test2        | latin1             | latin1_swedish_ci |
    | t3         | test3        | utf16              | utf16_general_ci  |
    | t4         | test4        | ucs2               | ucs2_general_ci   |
    +------------+--------------+--------------------+-------------------+
    

### Check the configuration of your table columns

To check the values for columns, use the following statement:
    
    
    SELECT table_schema, table_name, column_name, character_set_name, collation_name
    FROM information_schema.columns
    WHERE table_schema NOT IN ('information_schema', 'performance_schema', 'sys', 'mysql');

Example output:
    
    
    +--------------+------------+-------------+--------------------+------------------+
    | TABLE_SCHEMA | TABLE_NAME | COLUMN_NAME | CHARACTER_SET_NAME | COLLATION_NAME   |
    +--------------+------------+-------------+--------------------+------------------+
    | test1        | t1         | c           | ascii              | ascii_general_ci |
    | test1        | t1         | i           | NULL               | NULL             |
    | test2        | t2         | j           | NULL               | NULL             |
    | test2        | t2         | v           | ascii              | ascii_general_ci |
    | test3        | t3         | k           | NULL               | NULL             |
    | test3        | t3         | summary     | utf16              | utf16_general_ci |
    | test4        | t4         | col         | ucs2               | ucs2_general_ci  |
    | test4        | t4         | p           | NULL               | NULL             |
    +--------------+------------+-------------+--------------------+------------------+
    

**Note:** Character set and collation configuration applies only to string-based columns (for example, `char`, `varchar`, `enum`, `text`, `mediumtext`, `longtext`, and `set`). For all other column types, character set and collation configuration appears as `NULL`.

### Check the active schema or database

To check the details for the active schema or database, use the following statement.
    
    
    SELECT TABLE_SCHEMA, TABLE_NAME, CCSA.CHARACTER_SET_NAME AS DEFAULT_CHAR_SET,
           COLUMN_NAME, COLUMN_TYPE, C.CHARACTER_SET_NAME
    FROM information_schema.TABLES AS T
    JOIN information_schema.COLUMNS AS C USING (TABLE_SCHEMA, TABLE_NAME)
    JOIN information_schema.COLLATION_CHARACTER_SET_APPLICABILITY AS CCSA
    ON (T.TABLE_COLLATION = CCSA.COLLATION_NAME)
    WHERE TABLE_SCHEMA=SCHEMA()
    AND C.DATA_TYPE IN ('enum', 'varchar', 'char', 'text', 'mediumtext', 'longtext', 'set' )
    ORDER BY TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME;

Example output:
    
    
    +------------+
    | DATABASE() |
    +------------+
    | test3      |
    +------------+
    +--------------+------------+------------------+-------------+-------------+--------------------+
    | TABLE_SCHEMA | TABLE_NAME | DEFAULT_CHAR_SET | COLUMN_NAME | COLUMN_TYPE | CHARACTER_SET_NAME |
    +--------------+------------+------------------+-------------+-------------+--------------------+
    | test3        | t3         | utf16            | summary     | text        | utf16              |
    +--------------+------------+------------------+-------------+-------------+--------------------+
    

**Note:** The output includes only the character set and collation configuration for applicable string-based columns for the current active database.

### Check the configuration of your stored procedures

To check the values for stored procedures, use the following statement:
    
    
    SHOW PROCEDURE STATUS WHERE db = 'DB_NAME';

Replace DB_NAME with the name of the database.

Example output:
    
    
    +-------+------+-----------+---------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
    | Db    | Name | Type      | Definer | Modified            | Created             | Security_type | Comment | character_set_client | collation_connection | Database Collation |
    +-------+------+-----------+---------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
    | test2 | p1   | PROCEDURE | root@%  | 2024-08-09 11:47:05 | 2024-08-09 11:47:05 | DEFINER       |         | utf8mb4              | utf8mb4_0900_ai_ci   | latin1_swedish_ci  |
    | test2 | p2   | PROCEDURE | root@%  | 2024-08-09 11:48:36 | 2024-08-09 11:48:36 | DEFINER       |         | utf8mb4              | utf8mb4_0900_ai_ci   | latin1_swedish_ci  |
    +-------+------+-----------+---------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
    

To get the definition of a stored procedure, use the following statement:
    
    
    SHOW CREATE PROCEDURE DB_NAME.SP_NAME;

Replace the following:

  * DB_NAME: the name of the MySQL database
  * SP_NAME: the name of the stored procedure



If a stored procedure isn't using your intended character set or collation value, then you might need to drop and recreate it with the new character set or collation.

#### Check database collation mapping

In the previous example output, the stored procedure is created with `latin1_swedish_ci` as the default collation and the corresponding character set is `latin1`. This means all processing happens using the `latin1` character set (unless specific parameters of the procedure are tagged with a custom character set.) If you change only the database-level character set and collation, then the database-level update doesn't update the stored procedure automatically. The procedure continues to operate with the `latin1` character set and the respective collation. Dropping and recreating the stored procedure ensures that the procedure starts to use the new character set and new collation of the database that you just updated.

You can find out the mapping between database collation and character set by querying the `information_schema.COLLATION_CHARACTER_SET_APPLICABILITY` table.

Use the following statement as an example:
    
    
    SELECT CHARACTER_SET_NAME
    FROM information_schema.COLLATION_CHARACTER_SET_APPLICABILITY
    WHERE COLLATION_NAME = (SELECT database_collation FROM information_schema.ROUTINES
                            WHERE ROUTINE_SCHEMA = "test2" and ROUTINE_NAME = "p1");
    

Example output:
    
    
    +--------------------+
    | CHARACTER_SET_NAME |
    +--------------------+
    | latin1             |
    +--------------------+
    

### Check the configuration of your triggers

To check the values for triggers, use the following statement as an example.
    
    
    SHOW TRIGGERS FROM DB_NAME;

Replace DB_NAME with the name of the MySQL database.

To get the definition of a trigger, use the following example statement.
    
    
    SHOW CREATE trigger DB_NAME.TRIGGER_NAME;

Replace the following:

  * DB_NAME: the name of the MySQL database
  * TRIGGER_NAME: the name of the trigger



If the trigger isn't using your intended character set or collation value, then you might need to drop and recreate it with the new character set or collation. Check that the trigger is using the correct database collation mapping. For more information about checking database collation, see Check database collation mapping.

### Check the configuration of your events

To check the values for events, use the following statement as an example.
    
    
    SHOW EVENTS FROM DB_NAME;

Replace DB_NAME with the name of the database.

To get the definition of an event, use the following example statement.
    
    
    SHOW CREATE EVENT DB_NAME.EVENT_NAME;

Replace the following:

  * DB_NAME: the name of the database
  * EVENT_NAME: the name of the event



If the event isn't using your intended character set or collation value, then you might need to drop and recreate it with the new character set or collation. Check that the event is using the correct database collation mapping. For more information about checking database collation, see Check database collation mapping.

**Caution:** Recreating events can cause events to miss their scheduled turn.

### Check the configuration of your functions

To check the values for functions, use the following statement as an example.
    
    
    SHOW FUNCTION STATUS WHERE db = 'DB_NAME';

Replace DB_NAME with the name of the database.

To get the definition of a function, use the following example statement.
    
    
    SHOW CREATE FUNCTION DB_NAME.FUNCTION_NAME;

Replace the following:

  * DB_NAME: the name of the MySQL database
  * FUNCTION_NAME: the name of the function



If the function isn't using your intended character set or collation value, then you might need to drop and recreate it with the new character set or collation. Check that the function is using the correct database collation mapping. For more information about checking database collation, see Check database collation mapping.

I character set or collation. Check that the function is using the correct database collation mapping. For more information about checking database collation, see Check database collation mapping.

## Determine what level of updates to perform

After you have checked the character set and collation configuration of your database, you have a list of databases and possibly a list of database objects that you need to update.

The number of tasks you'll need to perform depend on the type of the database objects that require configuration changes.

  * Perform database-level updates. You need to update MySQL metadata only.
  * Perform database and table-level updates. You need to update MySQL metadata only.
  * Perform database, table, and column-level updates. You must update the metadata and rebuild tables and database objects. These updates can take the most amount of time; however, you can use one of the provided example scripts to update all of the tables and columns in a given database.



## Take a backup of the instance

**Important:** Do NOT skip this step.

Before you do any of these updates, take a backup of your instance. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up). We recommend that you take the backup without any DDL operations running on the instance.

## Generate rebuild commands for the stored database objects in your database

If you need to drop and recreate any stored database objects in your databases with the new character set and collation, then use the `mysqldump` tool to generate the commands now. After you update your database and table columns, you'll use the generated `mysqldump` file to rebuild the stored database objects in your database. This command generates statements for all stored procedures, functions, triggers, and events.

Run the following command so you can use the output to recreate all the stored procedures, functions, and events of a particular database later (when you recreate stored database objects).
    
    
    $ mysqldump -uDBAuser -p -h IP_ADDRESS \
       -P 3306 DB_NAME --no-data --no-create-db \
       --no-create-info --routines --triggers --events \
       --set-gtid-purged=OFF --events > dump_objects.sql

Replace the following:

  * IP_ADDRESS: IP address of the Cloud SQL for MySQL instance
  * DB_NAME: the name of the MySQL database



## Perform updates to your databases, and if necessary, tables and columns.

In this step, you update the character set and collation values of your databases. Also, you might need to rebuild your tables and columns.

### Perform database-level updates

If you are performing database-level updates only, then run the following statement to update your database:
    
    
    ALTER DATABASE DB_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

  * DB_NAME: the name of the database to update
  * NEW_CHARSET: the new character set to apply to the database
  * NEW_COLLATION: the new collation to apply to the database



### Perform database and table-level updates

If you are performing database and table-level updates, then do the following:

  1. Run the following statement to update your database:
         
         ALTER DATABASE DB_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

     * DB_NAME: the name of the database to update
     * NEW_CHARSET: the new character set to apply to the database
     * NEW_COLLATION: the new collation to apply to the database
  2. For each table that you want to update, run the following statement:
         
         ALTER TABLE TABLE_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

     * TABLE_NAME: the name of the table to update
     * NEW_CHARSET: the new character set to apply to the table
     * NEW_COLLATION: the new collation to apply to the table



### Perform database, table, and column-level updates

At this level, you need to re-encode existing data to comply with the new character set and collation settings. If you are performing a database, table, and column-level updates, then do the following:

  1. Before proceeding with updates to the table columns, review the following considerations:

     * The `ALTER TABLE` character set and collation conversion causes the table to rebuild and locks the table. As a result, any active query that tries to access the table is blocked.
     * The `ALTER TABLE` character set and collation conversion takes time because it fetches the complete table in memory. This operation might increase the latency of any workload running in parallel because the buffer pool pages are being used for the updated table.
     * If there are queries accessing multiple tables and some of the tables are being updated while others are not yet updated, then the queries might produce inconsistent results during this transaction time.
     * The process of running an `ALTER TABLE` character set and collation conversion creates a shadow table, so plan disk usage accordingly.
     * The `ALTER TABLE` character set and collation conversion also causes any indexes on the table to rebuild.
     * You don't need to update replica instances separately. `ALTER`, `DROP`, and `CREATE` commands are replicated automatically. However, running DDL commands can cause replica lag time to increase during the operation.
     * If you restore any of the databases from a backup taken from before you applied these updates, then you'll need to re-apply the updates.
  2. Check your table for any data tuples that might be incompatible with the new character set. If there are any incompatibilities, then you need to fix them before you update the character set. Otherwise, you'll encounter errors during the conversion process. You can use the following `SELECT CONVERT` statement to validate your data with new character set.
         
         SELECT COLUMN_NAME,CONVERT(COLUMN_NAME USING NEW_CHARSET)
         FROM TABLE_NAME
         WHERE COLUMN_NAME != CONVERT(COLUMN_NAME USING NEW_CHARSET);

**Note:** If you have a very large dataset, then the `SELECT CONVERT` query might take a longer time to run. For example, if you have a table `t` with a char column `c`, then you can run the following `SELECT CONVERT` statement to check the data tuples before converting to the ASCII character set.
         
         SELECT c,CONVERT(c USING 'ascii')
         FROM t WHERE c != CONVERT(c USING ascii);
         

Example output:
         
         +------+--------------------------+
         | c    | convert(c using 'ascii') |
         +------+--------------------------+
         | é    | ?                        |
         | é    | ?                        |
         | £    | ?                        |
         +------+--------------------------+
         

In this example, since the output returns these three tuples, there are three inconsistent values that need to be fixed. Before moving to the next step, examine the output of your query, and fix the data until your query returns zero tuples for all the columns that need conversion. You can also combine multiple columns in the same `SELECT` query.

  3. Choose an option for updating the character set and collation for your tables at the column level.

  4. If you want to update the character set for a very specific table column, then follow the steps in the Column-level tab where you only have to re-encode selected columns. Otherwise, follow the steps in the Table-level tab which re-encode the full table.

### Table-level

**Tip:** If you have many tables, then you can also use the script to update multiple tables.
     1. Run the following statement to update your database:
            
            ALTER DATABASE DB_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

        * DB_NAME: the name of the database to update
        * NEW_CHARSET: the new character set to apply to the database
        * NEW_COLLATION: the new collation to apply to the database
     2. For each affected table, run the following statement to update your table:
            
            ALTER TABLE TABLE_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

        * TABLE_NAME: the name of the table to update
        * NEW_CHARSET: the new character set to apply to the table
        * NEW_COLLATION: the new collation to apply to the table
     3. Update at table level so that all columns that are part of the table are updated with the new character set and collation. This option rebuilds the table completely. To use this option, run the following statement:
            
            ALTER TABLE DB_NAME.TABLE_NAME
            CONVERT TO CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

        * TABLE_NAME: the name of the table to update
        * NEW_CHARSET: the new character set to apply to the table
        * NEW_COLLATION: the new collation to apply to the table
**Note:** With this option, if MySQL can't fit the data in the new character set, then MySQL might change its data type. This change is unlikely, but we recommend that you check your tables after the conversion update.

### Column-level

Update at the column level. This option also rebuilds the table completely. If multiple columns are updated, then this option can cause multiple rebuilds.

**Tip** : If you have many columns, then you can also use the Script to update multiple columns in a table.

To use this option, run the following statement:

     1. Run the following statement to update your database:
    
    ALTER DATABASE DB_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

Replace the following:

        * DB_NAME: the name of the database to update
        * NEW_CHARSET: the new character set to apply to the database
        * NEW_COLLATION: the new collation to apply to the database
     2. For each affected table, run the following statement to update your table:
    
    ALTER TABLE TABLE_NAME CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;
     

Replace the following:

        * TABLE_NAME: the name of the table to update
        * NEW_CHARSET: the new character set to apply to the table
        * NEW_COLLATION: the new collation to apply to the table
     3. Run the following statement to update at the column level:
    
    ALTER TABLE DB_NAME.TABLE_NAME
    MODIFY COLUMN_DEFINITION CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;

**Note** : You must obtain the exact column definition. To obtain the exact column definition, use `SHOW CREATE TABLE TABLE_NAME`. 

Replace the following:

        * DB_NAME: the name of the database to update
        * TABLE_NAME: the name of the table to update
        * COLUMN_DEFINITION: specify an _exact column definition_ that includes constraints. The column definition might carry the old character set and collation values. You must update the column definition with the new values.
        * NEW_CHARSET: the new character set to apply to the table column
        * NEW_COLLATION: the new collation to apply to the table column

Repeat this statement for all string columns present in the table that need a character set or collation update.




## Validate the updates and look for errors

During the `ALTER TABLE` operation, look for any errors that indicate that existing data in the table isn't compatible with the new character set. For example:
    
    
    ERROR 1366 (HY000): Incorrect string value: '\xC3\xA9' for column 'c' at row 1
    

If you encounter any data compatibility errors, then we recommend that you check your tables again for any data compatibility errors and fix them before re-running the `ALTER TABLE` statements to re-encode the data.

In addition, during the `ALTER TABLE` operation, the tables (the foreign key table and the referenced table), a foreign key check might fail while the column undergoes re-encoding. If this happens, then you can disable the foreign key check (`SET FOREIGN_KEY_CHECKS=0;`) and run the update again.

## Recreate your stored database objects

After you have updated your database successfully, you can use the generated `mysqldump` file to recreate the stored database objects with the character set and collation values.

To recreate your stored database objects, do the following:

  1. Verify that the stored database objects are present on the database.
  2. Make sure that there's no parallel load that expects the stored database objects to be present during this drop and recreate time.
  3. The `mysqldump` file that you generated with the `mysqldump` tool doesn't include the statement for dropping triggers. If you need to drop triggers, then open a MySQL terminal to generate the `DROP` statement for triggers.
         
         mysql> SELECT CONCAT('DROP TRIGGER ', TRIGGER_NAME, ';') AS
         drop_trigger_statements FROM information_schema.TRIGGERS
         WHERE TRIGGER_SCHEMA = DB_NAME;

  4. Copy the output.

  5. Run the statement to drop the triggers for your database, either in a MySQL shell or in a script.

  6. After you drop the triggers, apply the dump file that you generated with the `mysqldump` tool. To apply the dump file and recreate the objects, enter the following:
         
         $ mysql -uDBAuser -p -h IP_ADDRESS \
           -P 3306 DB_NAME < dump_objects.sql

Replace the following:

     * IP_ADDRESS: IP address of the Cloud SQL for MySQL instance
     * DB_NAME: the name of the database



## Take another backup of the instance

After you complete your updates, take another backup of your instance. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up).

## Example scripts

If you need to update databases, tables, and columns, then this section provides example scripts to help re-encode your data.

**Tip:** You can try testing the data conversion on a clone instance before re-encoding data in production.

### Script to update multiple tables

The following script generates a statement for all the tables in the given database. The statement lets you re-encode existing data to comply with the new character set and collation settings.
    
    
    SELECT CONCAT("ALTER TABLE ",TABLE_SCHEMA,".",TABLE_NAME," CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;  ",
    "ALTER TABLE ",TABLE_SCHEMA,".",TABLE_NAME," CONVERT TO CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION; ")
    AS alter_sql FROM information_schema.TABLES
    WHERE TABLE_SCHEMA = 'DB_NAME' AND TABLE_TYPE='BASE TABLE';

Replace the following:

  * DB_NAME: the name of the database to update
  * NEW_CHARSET: the new character set to apply to the table
  * NEW_COLLATION: the new collation to apply to the table



Example output:
    
    
    +--------------------------------------------------------------------------------------------+
    |alter_sql
    +--------------------------------------------------------------------------------------------+
    | ALTER TABLE test1.t1 CHARACTER SET <new-charset> COLLATE <new-collation>;
      ALTER TABLE test1.t1 CONVERT TO CHARACTER SET <new-charset> COLLATE <new-collation>;       |
    +--------------------------------------------------------------------------------------------+
    

### Script to update multiple columns in a table

The following script generates a statement for all the columns in a given table. The statement lets you re-encode existing data to comply with the new character set and collation settings.

  1. Generate `ALTER TABLE` statements for all tables in the database
         
         SELECT CONCAT("ALTER TABLE ",TABLE_SCHEMA,".",TABLE_NAME," CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION;  ")
         AS alter_table_statements
         FROM information_schema.TABLES
         WHERE TABLE_SCHEMA = 'DB_NAME' AND TABLE_TYPE='BASE TABLE';

Replace the following:

     * DB_NAME: the name of the database to update
     * NEW_CHARSET: the new character set to apply to the table
     * NEW_COLLATION: the new collation to apply to the table

Example output:
    
    +------------------------------------------------------------------------------+
    | alter_table_statements                                                       |
    +------------------------------------------------------------------------------+
    | ALTER TABLE test1.t1 CHARACTER SET <new-charset> COLLATE <new-collation>;    |
    +------------------------------------------------------------------------------+
    

  2. For every table, generate `ALTER TABLE MODIFY` commands.
         
         SELECT CONCAT( "ALTER TABLE ", table_name, " MODIFY ", column_name, 'COLUMN_DEFINITION' , " CHARACTER SET NEW_CHARSET COLLATE NEW_COLLATION ")
         AS alter_table_column_statements FROM information_schema.columns
         WHERE table_schema = 'DB_NAME' AND table_name = 'TABLE_NAME'
         AND data_type IN ('char', 'varchar', 'tinytext', 'text', 'mediumtext', 'longtext','set','enum');

Replace the following:

     * DB_NAME: the name of the database to update
     * TABLE_NAME: the name of the table to update
     * COLUMN_DEFINITION: after obtaining results from each query, replace with the column definition for each column (column definitions can differ across columns)
     * NEW_CHARSET: the new character set to apply to the table column
     * NEW_COLLATION: the new collation to apply to the table column

Example output:
    
    +-------------------------------------------------------------------------------------------------------------------------------------+
    |alter_table_column_statements                                                                                                        |
    +-------------------------------------------------------------------------------------------------------------------------------------+
    | ALTER TABLE t1 MODIFY c <column-definition-replaced-after-obtaining-result-set> CHARACTER SET <new-charset> COLLATE <new-collation>  |
    +-------------------------------------------------------------------------------------------------------------------------------------+
    




## What's next

  * [Monitor Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance)
  * [View instance logs](https://docs.cloud.google.com/sql/docs/mysql/logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
