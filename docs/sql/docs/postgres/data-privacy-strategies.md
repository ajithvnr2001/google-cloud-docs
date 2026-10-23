---
url: https://docs.cloud.google.com/sql/docs/postgres/data-privacy-strategies/
title: Data privacy strategies \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:12.342548+00:00
---

# Data privacy strategies  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/data-privacy-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Data privacy strategies Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

_Data privacy_ is protecting data such as personally identifiable information (PII) from those who shouldn't have access to it. This page describes several approaches to data privacy that you can use to protect your PII in Cloud SQL.

You can use Cloud SQL to store your PII securely. You want to ensure that this information is processed with the highest privacy protection so that it isn't made accessible inadvertently. For example, if you store credit card information or healthcare data in your databases, then you can use Cloud SQL to hide or mask PII from unprivileged users.

Use the following strategies to help you secure your PII in Cloud SQL:

  * Column-level security
  * View-based approach
  * Row-level security
  * Mask and anonymize data
  * Encrypt data



## Column-level security

_Column-level security_ lets you restrict who can see the content in specific columns of database tables. Column-level privileges are applicable for `INSERT`, `UPDATE`, `SELECT`, and `REFERENCES` statements.

For example, consider a retail website where you want to govern PII for two users: Jack and Alice.
    
    
    --User: "admin"
    
    CREATE SCHEMA secure_schema;
    
    CREATE TABLE secure_schema.user_details(id bigint, name text, age smallint, email_id text, password text);
    
    --For this example, passwords are stored in plain text for demonstration
    --purposes only. In production, never store passwords in plain text.
    
    INSERT INTO secure_schema.user_details VALUES(1,'jack',34,'jack@example.com','testpass');
    INSERT INTO secure_schema.user_details VALUES(2,'alice',37,'alice@example.com','testpass');
    
    GRANT USAGE ON SCHEMA secure_schema TO analyst_ro;
    
    --Grant read permissions on specific columns only.
    
    GRANT SELECT (id, name, age) ON secure_schema.user_details TO analyst_ro;
    
    --User: "analyst_ro"
    
    SELECT * FROM secure_schema.user_details;
    ERROR:  permission denied for table user_details
    
    SELECT name, age, password FROM secure_schema.user_details;
    ERROR:  permission denied for table user_details
    
    SELECT id, name,age FROM secure_schema.user_details;
     id | name  | age
    ----+-------+----
      1 | jack  |  34
      2 | alice |  37
    

If you include the restricted columns in the `SELECT` statement or you enter `SELECT *`, then an error message appears. Cloud SQL secures the PII for Jack and Alice in these columns.

You can also use a single `GRANT` statement to combine different privileges.
    
    
    GRANT SELECT (id,name,age), UPDATE (name) ON secure_schema.user_details TO analyst_ro;
    

## View-based approach

You can also achieve column-level security by creating a view on a table, excluding or masking columns that you want to hide from other users, and providing access to the view instead of to the table.

The following example shows how to use a view-based approach for the retail website to secure the PII for Jack and Alice:
    
    
    --User: "admin"
    
    CREATE SCHEMA analyst_ro;
    CREATE VIEW analyst_ro.user_details AS SELECT id, name, age FROM secure_schema.user_details;
    GRANT USAGE ON SCHEMA analyst_ro TO analyst_ro;
    GRANT SELECT ON analyst_ro.user_details TO analyst_ro;
    
    --User: "analyst_ro"
    
    SELECT id,name,age FROM user_details;
     id | name  | age
    ----+-------+----
      1 | jack  |  34
      2 | alice |  37
    
    SELECT * FROM user_details;
     id | name  | age
    ----+-------+----
      1 | jack  |  34
      2 | alice |  37
    

In this example, a separate schema is created for the view to keep its name the same as the table. With the view-based approach, you can use `SELECT *`.

You can also create a view and mask the columns of the database table so that unprivileged users can't see the PII that's masked.
    
    
    CREATE OR REPLACE VIEW analyst_ro.user_details AS SELECT id, name, age, 'redacted@example.com' as email_id,'*****'::text as password FROM secure_schema.user_details;
    
    SELECT * FROM user_details;
     id | name  | age |     email_id         | password
    ----+-------+-----+----------------------+---------
      1 | jack  |  34 | redacted@example.com | *****
      2 | alice |  37 | redacted@example.com | *****
    
    

## Row-level security

Column-level security and a view-based approach let you hide PII in columns of database tables from specific users. However, sometimes you want to filter this data and grant access to specific rows of a table. This table contains the PII that only certain users can access, based on qualifying user conditions. This is known as _row-level security_.

Row-level security is useful for multi-tenant applications where users have read-access and write-access privileges to their own PII only. In Cloud SQL, tables can have row-level security policies that restrict, on a per-user basis, which rows users can view by creating queries, or the rows that users can insert, update, or delete by running data modification commands.

For the retail website example, you can implement row-level security for Jack and Alice so that each user can access only their own PII.
    
    
    --User: "admin"
    --Create and enable a policy for row-level security
    
    CREATE POLICY user_details_rls_pol ON secure_schema.user_details FOR ALL TO PUBLIC USING (name=current_user);
    ALTER TABLE secure_schema.user_details ENABLE ROW LEVEL SECURITY;
    
    SELECT * FROM secure_schema.user_details;
     id | name  | age |     email_id      | password
    ----+-------+-----+-------------------+---------
      1 | jack  |  34 | jack@example.com  | testpass
      2 | alice |  37 | alice@example.com | testpass
    
    --User: "jack"
    
    SELECT * FROM secure_schema.user_details;
     id | name | age |    email_id      | password
    ----+------+-----+------------------+---------
      1 | jack |  34 | jack@example.com | testpass
    
    --User: "alice"
    
    SELECT * FROM secure_schema.user_details;
     id | name  | age |    email_id       | password
    ----+-------+-----+-------------------+---------
      2 | alice |  37 | alice@example.com | testpass
    
    

Users who are assigned to roles that have the `BYPASSRLS` attribute can bypass row-level security when they're accessing a table. Table owners can also bypass row-level security. If you want to subject a table owner to row-level security, then use the `ALTER TABLE ... FORCE ROW LEVEL SECURITY` command.

Sometimes, you don't want to apply row-level security to rows of a database table. For example, if you use [pg_dump](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp) to take a backup of the table, then you don't want any rows to be omitted from the backup. To prevent this from occurring, for the user who takes the backup, set the [`row_security`](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-ROW-SECURITY) configuration parameter to `OFF`. If any rows are filtered based on row-level security, then an error message appears.

## Mask and anonymize data

In addition to masking data by using a view-based approach, you can mask data by using the [`postgresql_anonymizer`](https://docs.cloud.google.com/sql/docs/postgres/extensions) extension. This extension masks or replaces PII or commercially sensitive data from a PostgreSQL database.

Using the extension over a view-based approach provides you with the following benefits:

  * You have various [masking functions](https://postgresql-anonymizer.readthedocs.io/en/stable/masking_functions/) such as substitution, randomization, faking, pseudonymization, partial scrambling, shuffling, noise addition, and generalization.

  * You can generate meaningful masked data that you can use for functional testing and data processing.

  * You can use the PostgreSQL Data Definition Language (DDL) to [declare masking rules](https://postgresql-anonymizer.readthedocs.io/en/stable/declare_masking_rules/) and specify the anonymization strategy inside the table definition.




### Install and configure the `postgresql_anonymizer` extension

To use this extension on a Cloud SQL instance, complete the following steps:

  1. Edit the instance and then set the `cloudsql.enable_anon` flag to `on`. For information about setting flags, and to review the flags supported for the extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

  2. If you plan to use dynamic masks and the tables that you want to mask aren't in the `public` schema, then set the `anon.sourceschema` flag to the name of the schema that contains these tables. For the examples on this page, set the flag to `secure_schema`.

**Note:** Dynamic masks apply only to tables in the schema that's set by the `anon.sourceschema` flag. The default value is `public`. You can set only one source schema at a time.
  3. Create the extension in the database by running the following command:
         
         --Connect to the PostgreSQL database
         
         CREATE EXTENSION IF NOT EXISTS anon CASCADE;
         SELECT anon.init();
         




After you install and configure the extension, use it on the instance to implement dynamic mask, static mask, and anonymous dump anonymization strategies.

### Dynamic mask

Use dynamic masks to define masking rules for specific users. These users can't see PII. Instead, they see masked data. All other users see the unmasked data. This is useful in production environments when you don't want to alter the PII, but only hide it from certain users.

For the retail website example, you can implement dynamic masks so that the administrator can view the unmasked email addresses and passwords for Jack and Alice, but the analyst can view only masked data.
    
    
    --Activate the dynamic masking engine
    
    SELECT anon.start_dynamic_masking();
    
    --Declare the masking user and masking rules
    --analyst_ro is the masked user with select privileges on the
    --user_details table
    
    SECURITY LABEL FOR anon ON ROLE analyst_ro IS 'MASKED';
    
    SECURITY LABEL FOR anon ON COLUMN secure_schema.user_details.email_id IS 'MASKED WITH FUNCTION anon.fake_email()';
    SECURITY LABEL FOR anon ON COLUMN secure_schema.user_details.password  IS 'MASKED WITH FUNCTION anon.hash(password)';
    
    --Verify that the masked user is configured. The search_path must include
    --the mask schema followed by the schema set in the anon.sourceschema flag.
    
    SELECT rolconfig FROM pg_roles WHERE rolname = 'analyst_ro';
                  rolconfig
    --------------------------------------
     {"search_path=mask, secure_schema"}
    
    --User: "admin" (can see all unmasked data)
    
    SELECT * FROM secure_schema.user_details;
     id | name  | age |    email_id       | password
    ----+-------+-----+-------------------+---------
      1 | jack  |  34 | jack@example.com  | testpass
      2 | alice |  37 | alice@example.com | testpass
    
    --User: "analyst_ro" (open a new connection; note that the "email_id" and
    --"password" columns are replaced with masked data)
    --Data in the password column is truncated for better formatting.
    
    SELECT * FROM user_details;
     id | name  | age |       email_id         |    password
    ----+-------+-----+------------------------+-----------------
      1 | jack  |  34 | alisontodd@example.com | 13d249f2cb4127b
      2 | alice |  37 | amanda35@example.com   | 13d249f2cb4127b
    
    --The masked user can't query the source table directly.
    
    SELECT * FROM secure_schema.user_details;
    ERROR:  permission denied for schema secure_schema
    

When you start dynamic masking, the extension creates a view in the `mask` schema for each table in the schema that's set by the `anon.sourceschema` flag. When you label a role as `MASKED`, the extension does the following:

  * Revokes the privileges that are granted directly to the role on the source schema.
  * Grants the role the `USAGE` privilege on the `mask` schema and the `SELECT` privilege on every view in it, including views of tables that the role couldn't query before.
  * Sets the `search_path` of the role to the `mask` schema, followed by the source schema.



The masked user sees masked data only when the user queries a table without specifying the schema name, so that the name resolves to the view in the `mask` schema. Queries that specify the schema name, such as `SELECT * FROM secure_schema.user_details`, bypass the `mask` schema and fail with a permission error. The `search_path` setting is applied when the user connects, so masked users must open a new connection after you label the role.

**Warning:** Dynamic masks don't prevent access to the source table if the masked user receives privileges on the source schema in another way. For example, if the masked user is a member of a role that has the `USAGE` privilege on the source schema, or if this privilege is granted to `PUBLIC`, then the masked user can view unmasked data by specifying the schema name in the query, such as `SELECT * FROM secure_schema.user_details`. By default, `PUBLIC` has the `USAGE` privilege on the `public` schema, so if you mask tables in `public`, masked users can still query them by schema name. Use a dedicated schema for tables that you mask. Labels on a group role don't apply to the members of the role, so you must label each masked user individually. Masked views run with the privileges of the view owner, which is typically the table owner, so row-level security policies on the source table don't apply to masked users. To verify that a masked user can't access the source schema, run `SELECT has_schema_privilege('analyst_ro', 'secure_schema', 'USAGE');`. The query must return `false`.

### Static mask

Use static masks to remove the PII in a table, according to the criteria defined in the masking rules, and replace this information with masked data. Users can't retrieve the unmasked data. This is useful in test environments when you want to alter the PII and you don't want any users to view this information.

**Note:** Because static masks replace unmasked data with masked data in a table, depending on the size of the table, this process can take a long time.

For the retail website example, you can implement static masks so that no users can view the unmasked email addresses and passwords for Jack and Alice. Instead, they view only masked data.
    
    
    --User: "admin"
    
    SELECT * FROM secure_schema.user_details;
     id | name  | age |    email_id       | password
    ----+-------+-----+-------------------+---------
      1 | jack  |  34 | jack@example.com  | testpass
      2 | alice |  37 | alice@example.com | testpass
    
    --Apply earlier defined masking rules to the table permanently.
    --Now all users see masked data only.
    
    SELECT anon.anonymize_table('secure_schema.user_details');
     anonymize_table
    -----------------
     t
    
    --User: "analyst_ro"
    --Data in the password column is truncated for better formatting.
    
    select * from secure_schema.user_details;
     id | name  | age |            email_id             |    password
    ----+-------+-----+---------------------------------+-----------------
      1 | jack  |  34 | christophercampbell@example.com | 13d249f2cb4127b
      2 | alice |  37 | annebenitez@example.com         | 13d249f2cb4127b
    

### Anonymous dump

Use anonymous dumps to export masked data into a SQL file. For the retail website example, you can create a dump file for the masked data that's contained in the `user_details` table.
    
    
    --Launch pg_dump_anon to apply earlier defined masking rules. pg_dump_anon
    --reads the source table directly, so connect as a user that has the SELECT
    --privilege on the table and that isn't labeled as MASKED.
    
    pg_dump_anon -h HOSTIP -p 5432 -d DATABASE_NAME -U admin --table=secure_schema.user_details --file=user_details_anonymized.sql
    

## Encrypt data

Although you can mask PII, the information is stored in the database as plain text. An administrator can view this information.

Use the [`pgcrypto`](https://docs.cloud.google.com/sql/docs/postgres/extensions) extension to encrypt the PII before you store it. This way, only users that have a valid encryption key can decrypt the information and view it as plain text.

The `pgcrypto` extension has a number of hash and encrypt functions.

### Hash

A _hash_ is a one-way cryptographic function where you care only about encrypting the PII. This is useful for storing passwords in a hashed format and matching the user-entered passwords with the hashed passwords. Hashed passwords are never decrypted in plain text.

For the retail website example, you can use the `pgcrypto` extension to hash Jack's password before storing it in the `user_details` table.
    
    
    --Hash passwords before storing them in the user_details table.
    
    TRUNCATE TABLE secure_schema.user_details;
    INSERT INTO secure_schema.user_details VALUES(1,'jack',34,'jack@example.com',crypt('testpassword', gen_salt('bf')));
    
    --Match the hashed data with user entered password
    
    SELECT id, name FROM secure_schema.user_details WHERE email_id = 'jack@example.com' AND password = crypt('testpassword', password);
     id | name
    ----+-----
      1 | jack
    
    

### Encrypt

Use an _encryption_ cryptographic function to encrypt PII with a key. Users then need this key to decrypt the information into plain text. This is useful for storing credit card information and bank details where applications want to retrieve the PII in a readable format.

For the retail website example, Jack's password and email address are encrypted. Users who have the encryption key can decrypt this information and view it as plain text. For all other users, an error message appears.
    
    
    --"user_acc_key" is the encryption key
    
    TRUNCATE TABLE secure_schema.user_details;
    INSERT INTO secure_schema.user_details VALUES(1,'jack',34,pgp_sym_encrypt('jack@example.com','user_acc_key'),pgp_sym_encrypt('testpassword','user_acc_key'));
    
    --User: "admin" (queries without an encryption key)
    --Data in the email_id and password columns are truncated for better
    --formatting.
    
    SELECT * FROM secure_schema.user_details;
     id | name | age |     email_id     |      password
    ----+------+-----+------------------+--------------------
      1 | jack |  34 | \xc30d0407030209 | \xc30d040703028962
    
    --User: "app_user" (queries with a valid encryption key)
    
    SELECT name,pgp_sym_decrypt(email_id::bytea,'user_acc_key'),pgp_sym_decrypt(password::bytea,'user_acc_key') FROM secure_schema.user_details;
     name | pgp_sym_decrypt   | pgp_sym_decrypt
    ------+-------------------+----------------
     jack | jack@example.com  | testpassword
    
    --If a user uses the wrong encryption key, then the following error message appears:
    
    SELECT name,pgp_sym_decrypt(email_id::bytea,'user_bad_key'),
    pgp_sym_decrypt(password::bytea,'user_bad_key') FROM secure_schema.user_details;
    ERROR:  Wrong key or corrupt data
    

**Note:** With the `pgcrypto` extension, all encryption and decryption processing happens within the database. However, you might want to control the encryption and decryption logic within an application. To do this, use [client-side encryption](https://docs.cloud.google.com/sql/docs/postgres/client-side-encryption) to encrypt PII before writing it to Cloud SQL. You can encrypt this information in such a way that only applications can decrypt it.

## What's next

Learn about the following additional controls that you can use to protect PII from unwarranted access:

  * [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication)

  * [Authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks)

  * [SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance)

  * [Roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions)

  * [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
