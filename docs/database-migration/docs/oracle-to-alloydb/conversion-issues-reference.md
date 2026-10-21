---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/conversion-issues-reference/
title: Conversion issues and patterns reference \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:13.921789+00:00
---

# Conversion issues and patterns reference  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/conversion-issues-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Conversion issues and patterns reference Stay organized with collections  Save and categorize content based on your preferences. 

Conversion workspaces aggregate all conversion issues into groups and categories to help you plan for fixing conversion errors and warnings. Each category represents the type of work you might need to perform to fix the issues (review, refactor, adjust data types). Groups provide further aggregation, as they differentiate between specific cases at a lower level:

![Conversion workspace overview screen that shows conversion issue groups and categories.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/cw_issue_groups_oracle.png) **Figure 1.** Conversion workspace overview screen with conversion issue groups and categories. ![Conversion workspace overview screen that shows conversion issue groups and categories.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/cw_issue_groups_oracle.png)

The following table lists all conversion issue groups you can encounter during schema conversion:

Issue group ID | Description  
---|---  
  
## Input issues (`CW_01`)  
  
### CW_OP0101

| Invalid source code  
**Potential root cause** Errors in this group often occur when Database Migration Service encounters unknown syntax, or when the Oracle source code isn't valid (for example, a stored procedure is missing the `END;` keyword.)   
**Possible mitigation** Correct the invalid objects in the source Oracle database. Then, refresh the source schema snapshot in Database Migration Service and re-try the schema conversion process. Alternatively, you can exclude the object from the migration.   
  
### CW_OP0102

|  Missing referenced objects  
**Potential root cause** Database Migration Service uses metadata of objects in the source tree to improve the code conversion quality of dependent objects. If your code refers to objects that aren't included in the source schema, you might experience conversion issues because Database Migration Service can't determine the structure or data types for the missing referenced columns, attributes, or objects.  Possible errors in this group include incorrect data types for user-defined types (UDTs) or default `VARCHAR` data types for columns, parameters, or variables.   
**Possible mitigation** Either ensure that all referenced objects are added to the Database Migration Service source tree, or manually adjust the PostgreSQL code based on your knowledge of the source data model for the missing dependencies.   
  
### CW_OP0103

|  Tables without primary key  
**Potential root cause** Database Migration Service requires all tables to have a primary key. For tables without primary keys, Database Migration Service adds a `NUMERIC` column named `rowid` to the target PostgreSQL table. This column is populated with corresponding numeric values from the source Oracle `ROWID` pseudocolumn. To ensure that `INSERT` statements don't fail after the migration, Database Migration Service creates a sequence and uses it to auto-increment the `rowid` column.   
**Possible mitigation** You can either retain or remove the `rowid` column after the migration.   
  
## Source functionality not supported (`CW_02`)  
  
### CW_OP0200

|  Unsupported Oracle built-in functionality  
**Potential root cause** You might be using built-in Oracle functionality that isn't supported.   
**Possible mitigation** Find similar functionality in PostgreSQL and modify the converted code accordingly. In some cases, the missing functionality might be provided by the [ Orafce extension](https://github.com/orafce/orafce), available for both Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL migrations.   
  
### CW_OP0201

| `SQLCODE` not supported  
**Potential root cause** The Oracle `SQLCODE` function isn't supported for conversion. `SQLCODE` returns an `INTEGER`, whereas the closest equivalent in PostgreSQL is the `SQLSTATE` function that returns `TEXT` values.   
**Possible mitigation** If your source code doesn't rely on `SQLCODE` returning an integer (for example, `SQLCODE` is only ever logged in a `VARCHAR2` column or with a `DBMS_OUTPUT` message), then `SQLSTATE` can be safely used in the PostgreSQL code.  If your source code relies on `SQLCODE` returning an integer (for example, you use it with `NUMBER` or `INTEGER` variables, or save `SQLCODE` return values as parameters or columns), you need to refactor the converted code.   
  
### CW_OP0203

| Oracle SQL function not supported  
**Potential root cause** Some Oracle built-in functions are unsupported by Database Migration Service for conversion.  Certain functions might have their equivalents in PostgreSQL (for example, `ASCII`), others might share the same name but have different specifications (for example, `REGEXP%` functions). Some functions might not exist at all.   
**Possible mitigation** Inspect which Oracle function raised the error.

  * If the function exists with the same behavior in PostgreSQL, you can disregard the error message as the converted code should work the same after the migration. 
  * If a function has the same name but works differently or just doesn't exist in PostgreSQL, you can try to fix the converted code: 
    * Create a User-Defined Function (UDF) of the same name in the destination database. 
    * Replace the function call in the source with an equivalent expression.
    * Use Gemini-enhanced conversion assistance. For more information, see [ Convert SQL Server code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#ai-conversion). 
    * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 

  
  
### CW_OP0204

|  Oracle built-in packages not fully supported  
**Potential root cause** Database Migration Service supports certain Oracle built-in packages, but many don't have full conversion support, for example `DBMS_STATS`, `DBMS_UTILITY`, or `DBMS_SQL`.   
**Possible mitigation** If you use any unsupported packages, you might need to:

  * Change your code. For example, instead of using `DBMS_STATS.GATHER_TABLE_STATS`, you might use a simpler command such as `ANALYZE`.  Packages such as `UTL_FILE` and `DBMS_AQ` might require refactoring because they can't be easily replicated in PostgreSQL. 
  * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 

  
  
### CW_OP0205

| Oracle data type not supported for conversion  
**Potential root cause** Some Oracle data types aren't currently supported for conversion or data movement.   
**Possible mitigation** In most cases, PostgreSQL has an equivalent data type. You can [ use conversion mapping files to customize conversion logic](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-conversion-workspaces#use-custom-mappings) and transform the unsupported Oracle data type to the required PostgreSQL data type.  For more information on data type support, see [ Conversion workspaces - overview and supported objects](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces).   
  
### CW_OP0206

| Naming conflict  
**Potential root cause** This group captures issues where multiple database objects (such as tables, materialized views) are converted to use the same name in the destination database. For example, this issue can occur when you have source objects whose names differ only by case. Oracle object names are case insensitive, but PostgreSQL *is* case sensitive, so object names convert to use the same string.   
**Possible mitigation** Rename the conflicting objects directly in the source database, or in the converted schema in the conversion workspace editor. You can also use [ a conversion mapping file with the `RENAME_*` directive](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#conversion-directives-reference).   
  
## Source feature not supported (`CW_03`)  
  
### CW_OP0300

| Source feature not supported  
**Potential root cause** This group captures all generic issues that relate to Oracle features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation**

  * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 
  * Explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  
  
### CW_OP0301

|  Schema object type not supported  
**Potential root cause** Database Migration Service doesn't support certain Oracle schema object types for code conversion because PostgreSQL doesn't have appropriate equivalents. Examples include Index-Organized Tables (IOTs), text search indexes, or bodies for user-defined types (UDTs).   
**Possible mitigation** Database Migration Service converts unsupported objects into the closest PostgreSQL equivalent. For example, IOTs become regular tables with a primary key constraint, text search indexes convert into B-tree indexes. Keep in mind that these conversions might lead to loss of functionality specific to the original object type.   
  
### CW_OP0302

| PL/SQL feature not supported  
**Potential root cause** This group captures all generic issues that relate to PL/SQL features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation**

  * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 
  * Explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  
  
### CW_OP0303

|  Bulk binding not supported  
**Potential root cause** Database Migration Service code conversion doesn't currently support Oracle bulk binding features such as `BULK COLLECT`, `FORALL` or `SAVE EXCEPTIONS`.   
**Possible mitigation** To fix the issue, you need to modify the code that uses bulk binding features. You might want to consider the differences in PostgreSQL and Oracle architecture and whether array processing is necessary in PostgreSQL for your use case.  There are several strategies for approaching Oracle bulk binding operations in PostgreSQL. Their usage depends on your specific scenario, so we recommend that you use [ Gemini-powered conversion assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#ai-conversion) to handle your specific needs. Here are some other example recommendations to help get you started: 

  * For a full `BULK COLLECT` (no `LIMIT`), you can try to use the `ARRAY_AGG` function. 
  * For `BULK COLLECT` with `LIMIT`, you can try to use a `CURSOR FOR LOOP` to load and process batches of rows in arrays. But, if your case allows for functional changes, a possibly simpler alternative would be to use the `CURSOR FOR LOOP` to process one row at a time (rather than load them into arrays). 
  * For `FORALL` operations, you can try set-based DML with `UNNEST` if you choose to use array processing. 
  * For `SAVE EXCEPTIONS`, you might need to write an exception handler within a row-based `CURSOR FOR LOOP` as there is no equivalent clause in PostgreSQL. 

  
  
### CW_OP0304

|  Collections not supported  
**Potential root cause** Database Migration Service code conversion has partial support for Oracle collections.   
**Possible mitigation** You need to modify the converted PostgreSQL code accordingly. When resolving issues with collections, remember that PostgreSQL arrays are never sparse. If you assign elements sparsely, PostgreSQL arrays might return different results and cardinality counts than Oracle arrays.  Because PostgreSQL doesn't support string-indexed arrays, depending on the nature of the data, you might find `JSON`/`JSONB` or the `hstore` extensions to be suitable.   
  
### CW_OP0305

| Pipelined functions not supported  
**Potential root cause** Pipelined functions are not supported by Database Migration Service.   
**Possible mitigation** You can replace Oracle pipelined functions with PostgreSQL set returning functions. We recommend that you adjust the code in a way that is relevant to your use-case. Here are some examples to help get you started: 

  1. Reference the PostgreSQL type (UDT) that is converted from the source Oracle object or record type that defines the pipelined function's rowtype. Then, modify the PostgreSQL function's return clause to be `RETURNS SETOF <type name>` or `RETURNS TABLE`, depending on your specific case. 
  2. Replace the return value in the converted `PIPE ROW` code with `RETURN NEXT <row or record variable>`. 

The source pipelined function's collection type, used in the Oracle function's `RETURN` clause, isn't needed in PostgreSQL.   
  
### CW_OP0306

| Dynamic SQL not supported  
**Potential root cause** Database Migration Service provides partial support for converting dynamic SQL. Oracle `EXECUTE IMMEDIATE`, `OPEN FOR`, and `USING`/`INTO` keywords are correctly converted to their PostgreSQL equivalents, but the actual dynamic SQL, DML, or DDL strings aren't converted.   
**Possible mitigation** You need to modify the converted code to match your requirements. We highly recommend that you use [ Gemini-powered conversion assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#ai-conversion) to handle dynamic SQL.   
  
### CW_OP0307

|  `CONNECT BY` option not supported  
**Potential root cause** Most `CONNECT BY` operators, functions, and pseudocolumns are supported by Database Migration Service and converted to PostgreSQL recursive Common Table Expressions (CTEs). But there are certain exceptions that might require your attention. For example, the `ORDER SIBLINGS BY` clause is supported for ascending order only.   
**Possible mitigation** It's not possible to replicate the `ORDER SIBLINGS BY` clause for descending order in a simple manner, so you might need to re-structure your code to work with ascending order.  Review the reported issues with `CONNECT BY` operators, and adjust the code where necessary. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0308

| JSON not supported  
**Potential root cause** There are certain limitations in how Database Migration Service supports `JSON` for data movement and code conversion: 

  * `JSONB` isn't supported for data movement.
  * Code conversion doesn't support the `JSON` query functions or operators in Oracle (such as `JSON_TABLE`, `JSON_QUERY`, `JSON_OBJECT[AGG]`, `JSON_ARRAYAGG`, `JSON_PATCH`). 
  * In Oracle versions earlier than `21c`, you can store `JSON` data in `VARCHAR2`, `CLOB`, or `BLOB` columns, and verify it with the `IS JSON` condition. Database Migration Service doesn't support converting this condition. 

  
**Possible mitigation**

  * To move `JSON` data stored in `VARCHAR2`, `CLOB`, or `BLOB` columns to PostgreSQL, you might need to write a conversion mapping file with the `MODIFY_TYPE` directive.  For example:
        
        MODIFY_TYPE SOURCE_TABLE_NAME:BLOB_COLUMN_NAME_WITH_JSON_DATA:JSON

For more information on conversion mapping files, see [ Conversion mapping files](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#conversion-mapping-files). 
  * To convert the Oracle `JSON` functions and operators to PostgreSQL, you can use PostgreSQL functions such as `JSONB_ARRAY_ELEMENTS`, `JSON_AGG`. For more information, see [ JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html) in the PostgreSQL documentation. 

  
  
### CW_OP0309

| Locking and transactions issues  
**Potential root cause** Database Migration Service code conversion doesn't support `LOCK` or `SAVEPOINT` statements. PostgreSQL doesn't support `SAVEPOINT`.   
**Possible mitigation**

  * Break the `SAVEPOINT` blocks in Oracle to separate transaction blocks in PostgreSQL that utilize the `ROLLBACK` statement. 
  * To implement `DBMS_LOCK`, use the PostgreSQL `pg_dbms_lock` extension. This extension simplifies the migration of Oracle user-defined locks to PostgreSQL by emulating the functionality of the Oracle `DBMS_LOCK` package. 

  
  
### CW_OP0310

| XML not supported  
**Potential root cause** Database Migration Service doesn't support Oracle `XMLTYPE` or the associated XML functions and operators.   
**Possible mitigation** Although Database Migration Service doesn't directly support `XMLTYPE`, you can customize `BLOB`, `CLOB`, `NVARCHAR2`, or `VARCHAR2` columns to XML for data movement. PostgreSQL supports XML functionality.  To migrate your XML data, follow these steps:

  1. Create a conversion mapping file with the `MODIFY_TYPE` directive for XML data. For example: 
         
         MODIFY_TYPE SOURCE_TABLE_NAME:BLOB_COLUMN_NAME_WITH_XML_DATA:XML

For more information on conversion mapping files, see [ Conversion mapping files](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#conversion-mapping-files). 
  2. Start the migration job. This process migrates all data from Oracle to PostgreSQL, except for data in columns of type `XMLTYPE`. These columns are filled with `NULL` values in PostgreSQL.t 
  3. Create a foreign table in PostgreSQL by selecting only the `XMLTYPE` column from Oracle. Include the primary key column from the source table. 
  4. Merge the XML data from the foreign table into the original PostgreSQL table. 

For more information on how PostgreSQL works with `XMLTYPE`, see [ XML Functions](https://www.postgresql.org/docs/current/functions-xml.html) in the PostgreSQL documentation.   
  
### CW_OP0312

| `PIVOT` not supported  
**Potential root cause** Database Migration Service doesn't support the `PIVOT` and `UNPIVOT` transpose operators for code conversion.  
**Possible mitigation** You can achieve `PIVOT` transposition in PostgreSQL by using the `tablefunc` extension or by rewriting the source `PIVOT` expression to conditional aggregations. For example: 

  * `SUM(CASE WHEN <condition> THEN <value> ELSE 0 END)`
  * `COUNT(CASE WHEN <condition> THEN 1 END)`

You can create `UNPIVOT` transpositions, which create key-value pairs from a set of columns, in PostgreSQL in a variety of ways: 

  * Combining a `LATERAL` join with a set of `VALUES`. For example: `SELECT ... FROM <table> CROSS JOIN LATERAL (VALUES ('<column1-name>', <column1>), ('<column2-name>', <column2>) AS u(column_name, column_value))`
  * Using `UNNEST` with `ARRAY`s. For example: `SELECT ..., UNNEST(ARRAY['<column1-name>', '<column2-name>']) AS column_name, UNNEST(ARRAY[column1, column2]) AS column_value FROM <table>`

  
  
### CW_OP0313

| `ALTER`statement option not supported  
**Potential root cause** Database Migration Service doesn't `ALTER` statements (that are often executed in dynamic SQL) for conversion.   
**Possible mitigation** Replace the Oracle `ALTER` statements with the `SET` command in PostgreSQL. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0314

| SQL feature not supported  
**Potential root cause** This group captures all generic issues that relate to SQL features that aren't supported for conversion. Issues in this group don't fall under any other, more specific, issue groups. Examples include database event triggers, `GRANT` statements, multi-table `INSERT` operations, DML on inline views (`INSERT INTO (SELECT ... FROM ...)`), lateral views.   
**Possible mitigation**

  * Try to replicate the functionality with the [ Orafce extension](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 
  * Explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  
  
## Unsupported syntax (`CW_04`)  
  
### CW_OP0400

| Unsupported syntax  
**Potential root cause** This group captures all generic issues that relate to unsupported Oracle SQL or PL/SQL syntax. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation** Change your code to use PostgreSQL functionally-equivalent PostgreSQL syntax. We recommend that you explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0401

| Unsupported SQL syntax  
**Potential root cause** Your source code uses SQL syntax or elements that are unsupported by Database Migration Service. For example, the `NLS_LANG` parameter in the Oracle `TO_DATE` function is not supported.   
**Possible mitigation**

  * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 
  * Explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  
  
### CW_OP0402

| Unsupported PL/SQL syntax  
**Potential root cause** Your source code uses PL/SQL syntax or elements that are unsupported by Database Migration Service. For example, record-based `INSERT` statements (such as `INSERT INTO table VALUES r_variable`) and `PRAGMA RESTRICT_REFERENCES` are unsupported.   
**Possible mitigation** Change your code to use PostgreSQL functionally-equivalent PostgreSQL syntax. We recommend that you explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0403

|  Unsupported date and timestamp syntax  
**Potential root cause** Database Migration Service might raise errors or warnings for unsupported date or timestamp syntax, operations, or expressions. Examples of these issues include comparisons between mismatched data types or the use of `TZH:TZM` format model in timestamps. For more information on supported objects and data types, see [ About conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces).   
**Possible mitigation** You can re-create most date and timestamp expressions using PostgreSQL equivalents. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0404

| Unsupported elements of Oracle's exception handling syntax  
**Potential root cause** Database Migration Service code conversion doesn't support the following Oracle `PL/SQL` exception syntax elements: 

  * The use of `RAISE_APPLICATION_ERROR` with variable error codes instead of literal `-20nnn` codes. 
  * The use of `SQLERRM` with an error code argument, as this syntax is unsupported in PostgreSQL. 

  
**Possible mitigation** You must manually resolve these issues in the converted code. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
## Data types and conversion (`CW_05`)  
  
### CW_OP0500

|  Data types and conversion issues  
**Potential root cause** Database Migration Service can group conversion issues based on the context (for example,  conversion issues that occur in type comparison expressions). The `CW_OP0500` group captures all generic data type conversion problems that don't fall under other issue groups.   
**Possible mitigation** In most cases, Database Migration Service emits an `ERROR_UNIMPLEMENTED` or `ERROR_TYPE` message in the converted PostgreSQL code. Resolve this error based on your knowledge of the data types involved.   
  
### CW_OP0501

| Date format model issues  
**Potential root cause** You might encounter warnings or issues when converting date or timestamp expressions to or from strings based on a format model. Database Migration Service uses a default model (currently `DD-MON-RR`) when casts in the Oracle source code exclude an explicit date or timestamp format model.  This can sometimes cause issues in the converted code if the format model emitted for the implicit cast conflicts with an explicit format model in the same expression. You might also see this issue if your data is likely to be affected by the differences between [ Oracle `RR` format](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Format-Models.html#GUID-6C75461E-2E18-4C35-9EB4-038A7E1C9C1F) and [ PostgreSQL `YY` format.](https://www.postgresql.org/docs/current/functions-formatting.html)  
**Possible mitigation** Review and validate the converted PostgreSQL expressions in the conversion workspace.   
  
### CW_OP0502

|  Numeric format model issues  
**Potential root cause** Database Migration Service doesn't support all [ Oracle format models](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Format-Models.html). For example `'L'` or `'X'` aren't supported. You might encounter issues or warnings with code that converts strings to numbers based on Oracle format models.   
**Possible mitigation** For Oracle format models that have no equivalent in PostgreSQL, you might need to refactor your expressions or format models. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
### CW_OP0503

|  Data type casting issues  
**Potential root cause** You might encounter errors due to unsupported or inaccurate data type casting. Database Migration Service usually emits `ERROR_UNIMPLEMENTED`. This is usually because of missing or incomplete metadata. Database Migration Service might not have enough information to cast a type, for example in function arguments or procedure parameters.   
**Possible mitigation** Adjust the PostgreSQL code to ensure correct data type conversions. These corrections require that you are familiar with your referenced attributes, variables, and columns.   
  
### CW_OP0504

| Comparison issues  
**Potential root cause** Database Migration Service might not have enough metadata or information about data types when converting data comparison expressions. For example, this can happen when a user-defined type (UDT) is compared with `NULL`.   
**Possible mitigation** Review the converted PostgreSQL expressions and resolve the issues. We recommend that you explore Gemini-powered auto-conversion features for expediting such fixes. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini).   
  
## Potential functional nuances (`CW_06`)  
  
Issues in this category represent cases where Oracle source code is correctly converted to the closest PostgreSQL equivalent, but the resulting code might have minor semantic or functional differences that require your review. This happens because of the differences in how Oracle and PostgreSQL handle data types, formats, or objects.  At first glance, this category might appear to overlap with issues in the  Data types and conversion (`CW_05`) category, but note that they represent different problems. `CW_05` contains known issues where Database Migration Service can't convert Oracle code to its PostgreSQL equivalent.   
  
### CW_OP0601

| Review date format model  
**Potential root cause** Most [ Oracle date and timestamp format models](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Format-Models.html#GUID-49B32A81-0904-433E-B7FE-51606672183A) have appropriate equivalents in PostgreSQL, so the converted code has no semantic or functional differences. Some models don't have an exact match, and their behavior varies. One example is the [ Oracle `RR` format](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Format-Models.html#GUID-6C75461E-2E18-4C35-9EB4-038A7E1C9C1F) that is converted to the [ PostgreSQL `YY` format](https://www.postgresql.org/docs/current/functions-formatting.html).   
**Possible mitigation** Review and validate expressions with format model conversions to make sure that the converted code behaves as expected.   
  
### CW_OP0602

| Review numeric format model  
**Potential root cause** Most source numeric format models have an equivalent in PostgreSQL, and the converted code therefore has no semantic or functional differences. However, some format models might have no exact match or behave slightly differently.   
**Possible mitigation** Review and validate expressions with format model conversions to make sure that the converted code works as expected.   
  
### CW_OP0603

|  Review exception code   
**Potential root cause** When you use [ `RAISE_APPLICATION_ERROR`](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/raising-exceptions-explicitly.html#GUID-48F88C61-8CE9-4821-91CB-48A8F1BC09E1) with an error code in the range of `-20000` to `-20999`, Database Migration Service converts it to PostgreSQL `RAISE EXCEPTION` with a `SQLSTATE` in the range of `CW0000` to `CW999`. The conversion retains the last 3 digits of the source error code and prefixes it with `CW`.   
**Possible mitigation** Review this behavior to determine whether it's suitable for your needs. This review is necessary only if the source error codes are meaningful to your application, support teams, or documentation. If the error code value itself isn't meaningful, you can ignore this warning.   
  
### CW_OP0604

|  Review exception message  
**Potential root cause** The `SQLERRM` function exists both in Oracle PL/SQL and in PostgreSQL, but it might return different error text in each engine. For example, dividing by zero in Oracle returns error text `ORA-01476: divisor is equal to zero` but `ERROR: division by zero` in PostgreSQL.   
**Possible mitigation** If your application, support infrastructure, or documentation depends on the error text, review the conversion. Otherwise, you can ignore this difference.   
  
### CW_OP0605

| Review Oracle built-in function emulation  
**Potential root cause** Database Migration Service code and schema conversion aims to provide Oracle function behavior with PostgreSQL equivalents, but the results might not always be satisfactory for your scenario. As such, conversion workspaces always provide advisory warning with function conversions that might require your review.   
**Possible mitigation** We recommend you review objects where conversion workspaces emit warnings in the `CW_OP0605` issue group.   
  
### CW_OP0606

| Review foreign key column data type  
**Potential root cause** Database Migration Service identified mismatched data type specifications in between parent and child objects (for example, when a parent column is `NUMBER(4)` and the child column is `NUMBER(10)`).   
**Possible mitigation** Most of the time, slight data type mismatches don't cause problems in database functionality. However, we recommend that you review the converted data model for inconsistencies.   
  
##  Functional review recommended (`CW_07`)  
  
### CW_OP0701

| Functional review recommended  
**Potential root cause** This group captures all generic issues that relate to potential functional differences in Oracle and PostgreSQL code. Issues in this group don't fall under any other, more specific, issue groups.   
**Possible mitigation**

  * Some Oracle database functions or features may be replicated with extensions, such as [ Orafce](https://github.com/orafce/orafce). For more information on extensions supported in your destination database, see [ Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions). 
  * Explore Gemini-powered auto-conversion features to adjust the code. For more information, see [ Convert Oracle code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  
  
### CW_OP0702

| Review Oracle built-in function emulation  
**Potential root cause** Many Oracle built-in functions don't have a direct equivalent in PostgreSQL. To help mitigate that problem for migrations, Database Migration Service converts your code by using different SQL expressions to produce equivalent functional behavior in PostgreSQL.  In some cases, the converted expressions might be complex. Database Migration Service emits warnings in the `CW_OP0702` group to highlight possible problems and advise that a function was emulated with an expression.   
**Possible mitigation** Review the converted code to make sure that the converted functions behave as expected in your PostgreSQL environment.   
  
##  Refactoring required (`CW_08`)  
  
### CW_OP0801

| Autonomous transactions refactoring required  
**Potential root cause** PostgreSQL doesn't support [ autonomous transactions](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/AUTONOMOUS_TRANSACTION-pragma.html).   
**Possible mitigation** You can achieve autonomous transactions in PostgreSQL by using the [ `dblink`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#dblink), [ `pg_background`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#pg_background), or [ PL/Proxy](https://docs.cloud.google.com/alloydb/docs/reference/extensions#plproxy) extension. Database calls made with any one of these extensions execute in a different session, and therefore generate an autonomous transaction.   
  
### CW_OP0802

| Database links refactoring required  
**Potential root cause** Database Migration Service doesn't support [ Oracle database links](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/distributed-database-concepts.html#GUID-36A35EC6-D3BA-4284-ADA0-732E10F3425E). Objects that use links require refactoring.   
**Possible mitigation** Depending on the target of your database link, you can implement equivalent functionality in PostgreSQL with database extensions, such as [ `dblink`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#dblink), [ `postgres_fdw`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#postgres_fdw), [ `oracle_fdw`](https://docs.cloud.google.com/alloydb/docs/reference/extensions#oracle_fdw), or [ PL/Proxy](https://docs.cloud.google.com/alloydb/docs/reference/extensions#plproxy).   
  
### CW_OP0803

| Advanced queuing refactoring required  
**Potential root cause** Oracle Advanced Queuing packages (`DBMS_AQ`, `DBMS_AQADM`) don't have PostgreSQL equivalents and require refactoring.   
**Possible mitigation** Consider the following options: 

  * Refactor the queueing functionality away from the database and into the application tier. 
  * Use PostgreSQL tables, alerts, and triggers to implement equivalent behavior. 
  * Consult your technical solutions team representative for additional assistance. 

  
  
### CW_OP0804

|  Database email refactoring required  
**Potential root cause** AlloyDB for PostgreSQL doesn't support sending emails directly from the database. Extensions that enable this functionality are also unsupported. As such, Database Migration Service doesn't convert uses of the [ `UTL_SMTP` package](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_SMTP.html).   
**Possible mitigation** Refactor your database email code, and move the responsibility for sending emails to the application tier. You can still use the database to capture the conditions under which sending out email is required.  An example implementation could be to write email details to a dedicated table. This table can also act as an email queue that you poll with a Cloud Run functions function and handle the actual SMTP processing.   
  
### CW_OP0805

| Jobs and scheduling refactoring required  
**Potential root cause** The [ `DBMS_JOB`](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_JOB.html) and [ `DBMS_SCHEDULER`](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SCHEDULER.html) Oracle packages aren't converted by Database Migration Service. You need to refactor the code that references these packages.   
**Possible mitigation** For simple jobs without dependencies, you can manually create scheduled jobs in the target PostgreSQL database with the [ `pg_cron` extension](https://docs.cloud.google.com/alloydb/docs/reference/extensions#pg_cron).  For more complicated schedules that `pg_cron` doesn't support, you might need to use an application-level or third-party scheduler.   
  
### CW_OP0806

|  File I/O refactoring required  
**Potential root cause** Database Migration Service doesn't support the Oracle [ `UTL_FILE` package](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html). You need to refactor the code that references this packages.  The Orafce extension includes `UTL_FILE` emulation, but might not work in a Google managed PostgreSQL environment due to restricted file I/O capabilities.   
**Possible mitigation**

  * Refactor your code to remove dependencies on `UTL_FILE`.
  * AlloyDB for PostgreSQL has certain restrictions on file I/O capabilities, so it's not possible to implement this behavior directly in the destination database.  A possible alternative could be to install PostgreSQL with the [ `orafce` extension](https://github.com/orafce/orafce) on a Compute Engine VM in your VPC. You can then use the [ `PL/Proxy` extension](https://docs.cloud.google.com/alloydb/docs/reference/extensions#plproxy) in your destination database to call the [ PostgreSQL-compatible `UTL_FILE` version](https://github.com/orafce/orafce/blob/master/doc/orafce_documentation/Orafce_Documentation_06.md) that runs in the database on the Compute Engine VM. 

  
  
### CW_OP0807

| Synonyms  
**Potential root cause** PostgreSQL doesn't support synonyms. For code objects, Database Migration Service automatically replaces synonym references with their source schema and object name. If you use synonyms outside of code objects, for example in read-only schemas for database application users, you need to convert them manually.   
**Possible mitigation** For synonym usage outside of code objects, you can use the PostgreSQL [ `SEARCH_PATH` parameter](https://www.postgresql.org/docs/17/ddl-schemas.html#DDL-SCHEMAS-PATH), or refactor your code to use views for query objects.   
  
### CW_OP0808

| Global temporary tables refactoring required  
**Potential root cause** This issue group is a warning that Database Migration Service detected a global temporary table in your Oracle source code. Migrating global temporary tables requires that you have the pgtt PostgreSQL extension installed and created on the destination database.   
**Possible mitigation** We recommend that you verify that you have the pgtt PostgreSQL extension installed and created on the destination database.   
  
## Gemini review recommendations (`CW_99`)  
  
### CW_AI9900

| Review Gemini suggestions  
**Potential root cause** : This issue group captures all generic errors and warnings related to Gemini-enhanced code conversion.   
**Possible mitigation** : Issues found here might not always point to real problems, but we strongly recommend that you review all Gemini-enhanced conversions to make sure they match your expectations.   
  
### CW_AI9901

| Review AI-augmented code  
**Potential root cause** : This DDL code was converted with Gemini-enhanced features and might need your review for accuracy.   
**Possible mitigation** We recommend that you carefully review code converted with AI augmentations to make sure the end result matches the functionality of your source schema.   
  
### CW_AI9902

| Citations  
**Potential root cause** : Gemini-enhanced suggestions can include content cited from multiple sources. Certain citations might be subject to license restrictions. We recommend that you review the converted code for citations.   
  
## General conversion issues (`CW_00`)  
  
### CW_OP0000

| Metadata conversion issues  
**Potential root cause** : This group captures all conversion issues that don't fall under any other, more specific, issue groups.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source data model and adjust the code as needed.   
  
### CW_OP0001

| Metadata conversion issues  
**Potential root cause** : This group captures all metadata-tracking issues that don't fall under any other, more specific, issue groups.   
**Possible mitigation** : Examples of issues in this group are usually related to compilation errors or warnings that can lead to problems with data types in the converted PostgreSQL. We recommend that you review the converted code based on your knowledge of the source data model and adjust the faulty references.   
  
### CW_OP0002

| Contact your support team  
**Potential root cause** In special edge cases, you might encounter an internal error with a valid Oracle source object. If you do, contact your support team for additional assistance.   
  
### CW_OP0003

| General conversion issues  
**Potential root cause** This group contains all issues that don't fall under any other, more specific, issue categories or groups.   
**Possible mitigation** We recommend that you review the converted code based on your knowledge of the source data model and code, and adjust as needed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
