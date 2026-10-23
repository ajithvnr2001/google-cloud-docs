---
url: https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions/
title: Create Cloud SQL for PostgreSQL read-only sessions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:09.594909+00:00
---

# Create Cloud SQL for PostgreSQL read-only sessions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Create Cloud SQL for PostgreSQL read-only sessions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

You can create a read-only Cloud SQL for PostgreSQL session using the `cloudsql_session_read_only` session parameter. This approach is a more robust way to prevent data modification during a session than the standard PostgreSQL read-only options. Using the `cloudsql_session_read_only` parameter, you can make the session read-only temporarily, or permanently for the duration of the session. You can use read-only sessions of this kind to help protect data integrity in various contexts, including sessions where you're using Model Context Protocol (MCP) tools, reporting tools, and auditing tools.

By default, `cloudsql_session_read_only` is set to `off`, which allows data modification.

## What read-only mode prevents

In a read-only session, the database can't modify any data. Specifically, read-only mode prevents the following:

  * **Read-only mode prevents the generation of new transaction IDs.** No writable transactions can be started, and as a result no data manipulation language (DML) or data definition language (DDL) instructions can be executed. However, if the flag is set in the middle of an active writable transaction, then basic DML and DDL instructions can be executed until the transaction terminates.

  * **Read-only mode prevents the following kinds of statements and calls:**

    * Statements like `VACUUM` and `NOTIFY`.
    * Functions with side effects. This means that you can't call a `FUNCTION` or execute a `PROCEDURE` that is defined as both `VOLATILE` and `LANGUAGE C` or `LANGUAGE internal`, because some of their side effects don't require a transaction ID. Examples are `pg_promote()`, `pg_cancel_backend()`, and `pg_terminate_backend()`.
    * Foreign data wrappers.
    * Any function or procedure that you created in a SQL procedural language (PL).



## Configure read-only status

During a Cloud SQL for PostgreSQL session, you can use the `SET` statement to change the value of the `cloudsql_session_read_only` flag as follows:

  * `SET cloudsql_session_read_only = 'on'`

This statement makes the session read-only, preventing anyone from modifying data for as long as the flag remains set to `on`. To resume modifying data later in the session, change the value back to `off`:

  * `SET cloudsql_session_read_only = 'off'`

Setting the flag back to `off` restores write access in the session except when the flag is set to `locked`.

  * `SET cloudsql_session_read_only = 'locked'`

Setting the flag to `locked` makes the session permanently read-only. After the flag is set to `locked`, you can't change the flag to any other value for the duration of the session.




To make a session permanently read-only as soon as you connect to the database, embed the `cloudsql_session_read_only` flag in the session's connection string:
    
    
    postgresql://USER:PASSWORD@HOST:PORT/DATABASE?options=-ccloudsql_session_read_only=locked

Make the following replacements:

  * USER: the username of the user creating the session.
  * PASSWORD: the user's password.
  * HOST: the host URL.
  * PORT: the port number.
  * DATABASE: the database name.



This approach has the added advantage that if you're trying to connect to an older version of Cloud SQL that lacks support for read-only sessions, then the connection fails.

You can also deny write access to a specific database user for all future connections, like this:
    
    
    ALTER USER USERNAME SET cloudsql_session_read_only = 'locked';

Replace USERNAME with the username of the user whose access you want to restrict to read-only.

### Enable specific functions in read-only sessions

  * You can enable use of a particular `FUNCTION` or `PROCEDURE` defined as both `VOLATILE` and `LANGUAGE C` or `LANGUAGE internal`. Do this by attaching a `SECURITY LABEL` to the function or procedure that is set to `allow`.
  * To disallow a particular function in the session, set a `SECURITY LABEL` statement to `deny`.
  * To allowlist functions that don't affect global state, create a predefined group of security labels:
        
        CREATE EXTENSION "google_read_only_session"
        

The `google_read_only_session` extension enables the following:

    * All built-in volatile C functions that are allowed for read-only mode.
    * All functions allowed for read-only mode that are from extensions loaded in the database, including the handler functions for `pl/pgsql` and `pl/v8` languages.

If you install one or more new extensions afterwards, then to apply group labels, drop and recreate the `google_read_only_session` extension:
    
    > DROP EXTENSION google_read_only_session;
    > CREATE EXTENSION google_read_only_session;
    

The `DROP` command doesn't remove any existing labels. The second `CREATE` command just adds labels for the volatile C functions in the new extension.




## What's next

  * Learn more about [ Cloud SQL for PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags).
  * Learn more about [ Cloud SQL for PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
