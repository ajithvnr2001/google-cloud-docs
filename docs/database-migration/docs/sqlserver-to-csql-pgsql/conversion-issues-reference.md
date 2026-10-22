---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/conversion-issues-reference/
title: Conversion issues and patterns reference \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:49.639505+00:00
---

# Conversion issues and patterns reference  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/conversion-issues-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Conversion issues and patterns reference Stay organized with collections  Save and categorize content based on your preferences. 

Conversion workspaces aggregate all conversion issues into groups and categories to help you plan for fixing conversion errors and warnings. Each category represents the type of work you might need to perform to fix the issues (review, refactor, adjust data types). Groups provide further aggregation, as they differentiate between specific cases at a lower level:

![Conversion workspace overview screen that shows conversion issue groups and categories.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/cw_issue_groups_sqlserver.png) **Figure 1.** Conversion workspace overview screen with conversion issue groups and categories. ![Conversion workspace overview screen that shows conversion issue groups and categories.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/cw_issue_groups_sqlserver.png)

The following table lists all conversion issue groups you can encounter during schema conversion:

Issue group ID | Description  
---|---  
  
## Input issues (`CW_01`)  
  
### CW_SP0101

| Invalid source code  
**Potential root cause** Errors in this group often occur when Database Migration Service encounters unknown syntax, or when the SQL Server source code isn't valid.   
**Possible mitigation** Correct the invalid objects in the source SQL Server database. Then, refresh the source schema snapshot in Database Migration Service and re-try the schema conversion process. Alternatively, you can exclude the object from the migration.   
  
### CW_SP0102

| Missing referenced objects  
**Potential root cause** Database Migration Service uses metadata of objects in the source tree to improve the code conversion quality of dependent objects. If your code refers to objects that aren't included in the source schema, you might experience conversion issues because Database Migration Service can't determine the structure or data types for the missing referenced columns, attributes, or objects.   
**Possible mitigation** Ensure that all objects you depend on in the migrated code are included in the source tree. You can add the referenced objects to the Database Migration Service source tree, or manually adjust the references in the PostgreSQL code based on your knowledge of the source data model.  If your object refers to an object in another database and uses the three-part entity name, refactor your queries to account for the differences in how SQL Server code and PostgreSQL handle three-part names. Consider the following approaches: 

  * Modify the application code to connect directly to the other database instead of using three-part names. 
  * Move the relevant objects to the main database, or create synchronisation mechanism between these databases. 
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0103

| Missing primary key  
**Potential root cause** Database Migration Service requires all tables to have a primary key. For tables without primary keys, Database Migration Service adds a string (hash) column named `md5_hash` to the target PostgreSQL table.   
**Possible mitigation** You can either retain or remove the `md5_hash` column after the migration.   
  
## Source functionality not supported (`CW_02`)  
  
### CW_SP0200

| Source functionality not supported  
**Potential root cause** You might be using built-in SQL Server functionality that isn't supported.   
**Possible mitigation** Find similar functionality in PostgreSQL and modify the converted code accordingly. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
### CW_SP0201

| SQL Server system view not supported  
**Potential root cause** Database Migration Service doesn't support certain SQL Server system views. For example, you might receive this error for system views related to schema information, such as `sys.procedures`.   
**Possible mitigation** Consider creating an extension in PostgreSQL to provide the missing system view.   
  
### CW_SP0202

| SQL Server SQL function not supported  
**Potential root cause** Some SQL Server built-in functions are unsupported by Database Migration Service for conversion. Certain functions might have their equivalents in PostgreSQL (for example, `ASCII`), others might share the same name but have different specifications (for example, global system functions starting with `@@`). Some functions might not exist at all.   
**Possible mitigation** Inspect which SQL Server function raised the error.

  * If the function exists with the same behavior in PostgreSQL, you can disregard the error message as the converted code should work the same after the migration. 
  * If a function has the same name but works differently or just doesn't exist in PostgreSQL, you can try to fix the converted code: 
    * Create a User-Defined Function (UDF) of the same name in the destination database. 
    * Replace the function call in the source with an equivalent expression.
    * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0203

| SQL Server object not supported  
**Potential root cause** Some SQL Server built-in objects are unsupported or only partially supported by Database Migration Service for conversion.   
**Possible mitigation** Try to adjust your converted code to replicate the unsupported functionality:

  * Create a User-Defined Function (UDF) with the same name as the object in the destination database. 
  * Replace the object in the source with an equivalent expression.
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0205

| Naming conflict  
**Potential root cause** This group captures issues where multiple database objects (such as tables, materialized views) are converted to use the same name in the destination database. For example, this issue can occur when you have source objects whose names differ only by case. SQL Server object names are case insensitive, but PostgreSQL *is* case sensitive, so object names convert to use the same string.   
**Possible mitigation** Rename one of the conflicting objects directly in the source database, or in the converted schema in the conversion workspace editor. You can also use [ a conversion mapping file with the `RENAME_*` directive](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#conversion-directives-reference).   
  
## Source feature not supported (`CW_03`)  
  
### CW_SP0300

| Source feature not supported  
**Potential root cause** This group captures all generic issues that relate to SQL Server features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation** Identify the specific SQL Server feature that triggers the error.

  * Restructure your code to avoid using the unsupported feature, if possible.
  * Replace the unsupported feature with an equivalent that is supported in PostgreSQL.
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0302

| T-SQL feature not supported  
**Potential root cause** This group captures all generic issues that relate to T-SQL features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation** Review and examine the unsupported T-SQL feature that raised the error. Adjust the code based on your knowledge of the T-SQL feature and behavior.  You can also explore Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
### CW_SP0306

| Dynamic SQL options not supported  
**Potential root cause** Database Migration Service has partial support for dynamic SQL conversion. SQL Server `EXEC` and `sp_executesql` commands are correctly converted to their PostgreSQL equivalents, but the actual dynamic SQL, DML, or DDL strings aren't converted.   
**Possible mitigation** You need to modify the converted code to match your requirements. We highly recommend that you use [ Gemini-powered conversion assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion) to handle dynamic SQL.   
  
### CW_SP0308

| JSON not supported  
**Potential root cause** Database Migration Service code conversion doesn't support SQL Server JSON functions such as `JSON_VALUE` and `JSON_QUERY`.   
**Possible mitigation** You can rewrite the code to avoid the use of JSON functions or create User-Defined Functions (UDFs) to handle JSON data.  Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
### CW_SP0309

| Locking and transactions issues  
**Potential root cause** Database Migration Service code conversion doesn't support the conversion of `TRANSACTION` and `LOCKING` statements.   
**Possible mitigation**

  * Verify that transactions are handled appropriately in the rewritten code. 
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0310

| XML not supported  
**Potential root cause** Database Migration Service doesn't support SQL Server XML features for conversion.  
**Possible mitigation** You must manually convert the XML code in your PostgreSQL schema.  
  
### CW_SP0311

| `MERGE` not supported  
**Potential root cause** The SQL `MERGE` command is not yet supported by Database Migration Service for conversion.  
**Possible mitigation** Modify the converted code to achieve functionally equivalent result. For example, you can:

  * Use the [ `INSERT ... ON CONFLICT`](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT). 
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
### CW_SP0312

| `PIVOT` not supported  
**Potential root cause** Database Migration Service doesn't support the `PIVOT` and `UNPIVOT` transpose operators for code conversion.   
**Possible mitigation** You can achieve `PIVOT` transposition in PostgreSQL by using the `tablefunc` extension or by rewriting the source `PIVOT` expression to conditional aggregations. For example: 

  * `SUM(CASE WHEN <condition> THEN <value> ELSE 0 END)`
  * `COUNT(CASE WHEN <condition> THEN 1 END)`

You can create `UNPIVOT` transpositions, which create key-value pairs from a set of columns, in PostgreSQL in a variety of ways: 

  * Combining a `LATERAL` join with a set of `VALUES`. For example: `SELECT ... FROM <table> CROSS JOIN LATERAL (VALUES ('<column1-name>', <column1>), ('<column2-name>', <column2>) AS u(column_name, column_value))`
  * Using `UNNEST` with `ARRAY`s. For example: `SELECT ..., UNNEST(ARRAY['<column1-name>', '<column2-name>']) AS column_name, UNNEST(ARRAY[column1, column2]) AS column_value FROM <table>`

  
  
### CW_SP0313

| ALTER statement option not supported  
**Potential root cause** Database Migration Service doesn't support `ALTER` statements for code conversion. Objects that contain such statements can raise conversion exceptions.   
**Possible mitigation** Replace the SQL Server `ALTER` statements with the `SET` command in PostgreSQL. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
### CW_SP0314

| SQL feature not supported  
**Potential root cause** This group captures all generic issues that relate to SQL features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation** Adjust the converted code to cover your requirements. You can explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
## Unsupported syntax (`CW_04`)  
  
### CW_SP0400

| Unsupported syntax  
**Potential root cause** This group captures all generic issues that relate to unsupported SQL or T-SQL syntax. Issues in this group don't fall under any other, more precise, issue groups.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source syntax and behavior, and adjust the converted code. You can also explore Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
### CW_SP0401

| Unsupported SQL syntax  
**Potential root cause** Your source code uses SQL syntax or elements that are unsupported by Database Migration Service.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source syntax and behavior, and adjust the converted code. You can also explore Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
### CW_SP0402

| Unsupported T-SQL syntax  
**Potential root cause** Your source code uses T-SQL syntax or elements that are unsupported by Database Migration Service.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source syntax and behavior, and adjust the converted code. You can also explore Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
### CW_SP0403

| Unsupported date and timestamp syntax  
**Potential root cause** Database Migration Service might raise errors or warnings for unsupported date or timestamp syntax, operations, or expressions, for example in comparisons between mismatched data types. For more information on supported objects and data types, see [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces).   
**Possible mitigation** You can re-create most date and timestamp expressions using PostgreSQL equivalents. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
### CW_SP0404

| Unsupported exceptions syntax  
**Potential root cause** Database Migration Service doesn't support some elements of SQL Server exception handling syntax.   
**Possible mitigation** You must manually resolve these issues in the converted code. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
### CW_SP0405

| Unsupported collation syntax  
**Potential root cause** In SQL Server, the `COLLATE` clause specifies both the code page and sorting rules. Collation rules in PostgreSQL use similar syntax, but are mainly configured through locale settings. This functional discrepancy might cause issues in your converted code.   
**Possible mitigation** Inspect the `COLLATE` clause that raised the error, and verify that the sorting behavior is as you expect in PostgreSQL.  If you need to adjust the code, for newer PostgreSQL versions you can try the [ `CREATE COLLATION`](https://www.postgresql.org/docs/current/sql-createcollation.html) command. You can also explore Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion).   
  
## Data types and conversion (`CW_05`)  
  
### CW_SP0500

| Data types and conversion issues  
**Potential root cause** Database Migration Service can group conversion issues based on the context (for example,  conversion issues that occur in type comparison expressions). The `CW_SP0500` group captures all generic data type conversion problems that don't fall under other issue groups.   
**Possible mitigation** In most cases, Database Migration Service emits an `ERROR_UNIMPLEMENTED` message in the converted PostgreSQL code. Resolve this error based on your knowledge of the data types involved.   
  
### CW_SP0501

| Date format model issues  
**Potential root cause** You might encounter warnings or errors when converting date or timestamp expressions to or from strings based on a format model. You might also see these issues if your data is likely to be affected by the differences between how SQL Server [ `FORMAT()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/format-transact-sql), [ `CAST()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql), and [ `CONVERT()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql) functions work for dates compared to the [ PostgreSQL `TO_CHAR()` function](https://www.postgresql.org/docs/current/functions-formatting.html).  The format model in SQL Server is determined by the `dateformat` setting. You can use the [ `DBCC USEROPTIONS` command](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-useroptions-transact-sql) on the source database to check your format model.   
**Possible mitigation** Review and validate the converted PostgreSQL expressions in the conversion workspace.   
  
### CW_SP0502

| Numeric format model issues  
**Potential root cause** You might encounter issues or warnings with code that converts strings to numbers based on SQL Server format models. You might also see this issue if your data is likely to be affected by the differences between how SQL Server [ `FORMAT()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/format-transact-sql), [ `CAST()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql), and [ `CONVERT()`](https://learn.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql) functions work for dates compared to the [ PostgreSQL `TO_CHAR()` function](https://www.postgresql.org/docs/current/functions-formatting.html).   
**Possible mitigation** For format models that have no equivalent in PostgreSQL, you might need to refactor your expressions or format models. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
### CW_SP0503

| Casting issues  
**Potential root cause** You might encounter errors due to unsupported or inaccurate data type casting. This is usually because of missing or incomplete metadata. Database Migration Service might not have enough information to cast a type, for example in function arguments or procedure parameters.   
**Possible mitigation** Adjust the PostgreSQL code to ensure correct data type conversions. These corrections require that you are familiar with your referenced attributes, variables, and columns.   
  
### CW_SP0504

| Comparison issues  
**Potential root cause** Database Migration Service might not have enough metadata or information about data types when converting data comparison expressions. For example, this can happen when a user-defined type (UDT) is compared with `NULL`.   
**Possible mitigation** Review the converted PostgreSQL expressions and resolve the issues. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
## Potential functional nuances (`CW_06`)  
  
Issues in this category represent cases where your source code is correctly converted to the closest PostgreSQL equivalent, but the resulting code might behave in unexpected ways. This happens because of the functional differences in how SQL Server and PostgreSQL handle data types, formats, or objects.  At first glance, this category might appear to overlap with issues in the  Data types and conversion (`CW_05`) category, but note that they represent different problems. `CW_05` contains known issues where Database Migration Service can't convert SQL Server code to its PostgreSQL equivalent.   
  
### CW_SP0601

| Review date format model  
**Potential root cause** Most SQL Server date and timestamp format models have appropriate equivalents in PostgreSQL, so the converted code has no semantic or functional differences. Some format models don't have an exact match, and their behavior varies.   
**Possible mitigation** Review and validate expressions with format model conversions to make sure that the converted code behaves as expected.   
  
### CW_SP0602

| Review numeric format model  
**Potential root cause** Most source numeric format models have an equivalent in PostgreSQL, and the converted code therefore has no semantic or functional differences. However, some format models might have no exact match or behave slightly differently.   
**Possible mitigation** Review and validate expressions with format model conversions to make sure that the converted code works as expected.   
  
### CW_SP0604

| Review exception message  
**Potential root cause** If you use the SQL Server `@@ERROR` function for error handling, keep in mind that the return number might differ from the converted PostgreSQL `SQLERRM`. `RAISERROR` might also cause similar issues and should be replaced by `RAISE` in most cases. `ERROR_NUMBER()` and `ERROR_MESSAGE()` return different numbers, even when replaced by `SQLSTATE` and `SQLERRM`.   
**Possible mitigation** If your application, support infrastructure, or documentation depends on the error text or error number, a review of the conversion is recommended. Otherwise, you can ignore this message.   
  
##  Functional review recommended (`CW_07`)  
  
### CW_SP0701

| Functional review recommended  
**Potential root cause** This group captures all generic issues that relate to potential functional differences in SQL Server and PostgreSQL code. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source database behvaior, and adjust the code as needed. You can also explore Gemini-powered auto-conversion features for expediting your fixes. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini).   
  
##  Refactoring required (`CW_08`)  
  
### CW_SP0802

| Database links refactoring required  
**Potential root cause** Database Migration Service doesn't support the conversion of [ SQL Server linked servers](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-database-engine).   
**Possible mitigation** Refactor the converted code to achieve similar functionality in your destination database. One possible approach is to re-create your database links with the [ `dblink` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#dblink).   
  
### CW_SP0807

| Synonyms  
**Potential root cause** PostgreSQL doesn't support synonyms. For code objects, Database Migration Service automatically replaces synonym references with their source schema and object name.   
**Possible mitigation** For synonym usage outside of code objects, you can use the PostgreSQL [ `SEARCH_PATH` parameter](https://www.postgresql.org/docs/17/ddl-schemas.html#DDL-SCHEMAS-PATH), or refactor your code to use views for query objects.  If the synonym object refers to an object in another database and uses the three-part entity name, refactor your queries to account for the differences in how SQL Server code and PostgreSQL handle three-part names. Consider the following approaches: 

  * Modify the application code to connect directly to the other database instead of using three-part names. 
  * Move the relevant objects to the main database, or create synchronisation mechanism between these databases. 
  * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion). 

  
  
## General conversion issues (`CW_00`)  
  
### CW_SP0000

| General conversion issues  
**Potential root cause** This group contains all issues that don't fall under any other, more precise, issue categories or groups.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source data model and database behavior, and adjust the code as needed.   
  
### CW_SP0001

| Metadata conversion issues  
**Potential root cause** : This group captures all metadata-tracking issues that don't fall under any other, more specific, issue groups.   
**Possible mitigation** : Examples of issues in this group are usually related to compilation errors or warnings that can lead to problems with data types in the converted PostgreSQL. We recommend that you review the converted code based on your knowledge of the source database behavior and adjust the faulty references.   
  
### CW_SP0002

| Contact your support team  
**Potential root cause** In special edge cases, you might encounter an internal error with a valid SQL Server source object. If you do, contact your support team for additional assistance.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
