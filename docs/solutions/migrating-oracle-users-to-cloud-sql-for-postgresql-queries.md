---
url: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-queries/
title: Migrating Oracle\u00ae users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:56.900769+00:00
---

# Migrating Oracle® users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle® users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres) version 12. In addition to the [introductory setup part](https://docs.cloud.google.com/solutions/setting-up-cloud-sql-for-postgresql-for-production), the series includes the following parts:

  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Terminology and functionality](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-terminology)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Data types, users, and tables](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-data-types)
  * Migrating Oracle users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers (this document)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-security)
  * [Migrating Oracle Database users and schemas to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/solutions/migrating-oracle-database-to-cloud-sql-for-postgresql)



## Queries

Oracle and Cloud SQL for PostgreSQL support the ANSI SQL standard. So it's generally straightforward to migrate SQL statements by using only basic syntax elements (for example, not specifying any scalar functions or any other Oracle extended feature). The following section discusses common Oracle query elements and their corresponding Cloud SQL for PostgreSQL equivalents.

### Basic SELECT and FROM syntax

Oracle feature name or syntax name | Oracle overview or implementation | Cloud SQL for PostgreSQL support | Cloud SQL for PostgreSQL corresponding or alternative solution  
---|---|---|---  
**SQL basic syntax for data retrieval** | `SELECT  
FROM  
WHERE  
GROUP BY  
HAVING  
ORDER BY` | Yes | `SELECT  
FROM  
WHERE  
GROUP BY  
HAVING  
ORDER BY`  
**`SELECT` **  
**for output print** | `SELECT 1 FROM DUAL` | Yes | `SELECT 1`  
**Column aliases** | `SELECT COL1 AS C1` | Yes | `SELECT COL1 AS C1  
OR  
SELECT COL1 C1`  
**Table name case sensitivity** | No case sensitivity  
(for example, table name can be `orders` and/or `ORDERS`). | Yes | Names are case insensitive unless quoted (for example, `orders` and `ORDERS` are treated as the same while `"orders" `and `"ORDERS"` are treated differently)  
  
For more details on Cloud SQL for PostgreSQL's `SELECT` syntax, see the [documentation](https://www.postgresql.org/docs/12/sql-select.html).

#### In-line views

  * In-line views (also known as _derived tables_) are `SELECT` statements, located in the `FROM` clause and used as subqueries.
  * In-line views can help make complex queries simpler by removing compound calculations or eliminating join operations, while condensing several separate queries into a single, simplified query.
  * **Conversion note** : Oracle in-line views do not require the use of aliases, while Cloud SQL for PostgreSQL requires specific aliases for each in-line view.



The following table presents a conversion example from Oracle to Cloud SQL for PostgreSQL, as an in-line view.

Oracle 11g/12c | Cloud SQL for PostgreSQL 12  
---|---  
`SQL> SELECT FIRST_NAME,  
DEPARTMENT_ID,  
SALARY,  
DATE_COL  
FROM EMPLOYEES,  
(SELECT SYSDATE AS DATE_COL FROM DUAL);`   
  
The output is similar to the following:  
  
` FIRST_NAME DEPARTMENT_ID SALARY DATE_COL  
-------------------- ------------- ---------- ---------  
Steven 90 24000 30-JUL-19  
Neena 90 17000 30-JUL-19  
Lex 90 17000 30-JUL-19` |  **Without alias for the in-line view:** `postgres=> SELECT FIRST_NAME,  
postgres-> DEPARTMENT_ID,  
postgres-> SALARY,  
postgres-> DATE_COL  
postgres-> FROM EMPLOYEES, (SELECT NOW() AS DATE_COL);  
  
ERROR: subquery in FROM must have an alias  
LINE 5: FROM EMPLOYEES, (SELECT NOW() AS DATE_COL);  
  
HINT: For example, FROM (SELECT ...) [AS] foo. ` **Adding an alias to the in-line view:** `postgres=> SELECT FIRST_NAME,  
postgres-> DEPARTMENT_ID,  
postgres-> SALARY,  
postgres-> DATE_COL  
postgres-> FROM EMPLOYEES, (SELECT NOW() AS DATE_COL) AS C1;` The output is similar to the following: ` first_name | department_id | salary | date_col  
-------------+---------------+----------+--------------------------------  
Steven | 90 | 24000.00 | 10/16/2020 08:35:18.470089 UTC  
Neena | 90 | 17000.00 | 10/16/2020 08:35:18.470089 UTC  
Lex | 90 | 17000.00 | 10/16/2020 08:35:18.470089 UTC`  
  
### JOIN statements

Oracle `JOIN` statements are supported by Cloud SQL for PostgreSQL `JOIN` statements. However, the use of the Oracle join operator `(+)` is not supported by Cloud SQL for PostgreSQL. To achieve the same result, you would need to convert to the standard SQL syntax for outer joins.

The following table presents a JOIN conversion example.

Oracle JOIN type | Supported by Cloud SQL for PostgreSQL | Cloud SQL for PostgreSQL JOIN syntax  
---|---|---  
`INNER JOIN` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E JOIN DEPARTMENTS D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;`  
`CROSS JOIN` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E CROSS JOIN DEPARTMENTS D;`  
`FULL JOIN [ OUTER ]` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E FULL JOIN DEPARTMENTS D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;`  
`LEFT JOIN [ OUTER ]` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;`  
`RIGHT JOIN [ OUTER ]` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E RIGHT JOIN DEPARTMENTS D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;`  
`SUBQUERY` | Yes | `SELECT E.FIRST_NAME, D.DEPARTMENT_NAME  
FROM EMPLOYEES E JOIN (SELECT * FROM DEPARTMENTS)D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;`  
  
#### UNION, UNION ALL, INTERSECT, and MINUS

Cloud SQL for PostgreSQL supports Oracle `UNION`, `UNION` `ALL`, and `INTERSECT` operators. The `MINUS` operator is not supported. However, Cloud SQL for PostgreSQL implements the `EXCEPT` operator, which is equivalent to the `MINUS` operator in Oracle. In addition, Cloud SQL for PostgreSQL supports the `INTERSECT ALL` and `EXCEPT ALL` operators, which are not supported by Oracle.

  * `UNION`: Attaches the result sets of two or more `SELECT` statements and eliminates duplicate records.
  * `UNION ALL`: Attaches the result sets of two or more `SELECT` statements without eliminating duplicate records.
  * `INTERSECT`: Returns the intersection of two or more `SELECT` statements only if a record exists in both data sets. Duplicate records are not eliminated.
  * `INTERSECT ALL` (Cloud SQL for PostgreSQL only): Returns the intersection of two or more `SELECT` statements only if a record exists in both data sets.
  * `MINUS (EXCEPT` in Cloud SQL for PostgreSQL): Compares two or more `SELECT` statements, returning only distinct rows from the first query that are not returned by the other statements.
  * `EXCEPT ALL` (Cloud SQL for PostgreSQL only): Compares two or more `SELECT` statements, returning only rows from the first query that are not returned by the other statements without eliminating duplicate records.



**Conversion notes**

When converting from Oracle `MINUS` operators into Cloud SQL for PostgreSQL, use `EXCEPT` operators instead.

**Examples**

Oracle function | Oracle implementation | Cloud SQL for PostgreSQL support | Cloud SQL for PostgreSQL corresponding or alternative solution  
---|---|---|---  
`UNION` | `SELECT COL1 FROM TBL1  
UNION  
SELECT COL1 FROM TBL2` | Yes | `SELECT COL1 FROM TBL1  
UNION  
SELECT COL1 FROM TBL2`  
`UNION ALL` | `SELECT COL1 FROM TBL1  
UNION ALL  
SELECT COL1 FROM TBL2` | Yes | `SELECT COL1 FROM TBL1  
UNION ALL  
SELECT COL1 FROM TBL2`  
`INTERSECT` | `SELECT COL1 FROM TBL1  
INTERSECT  
SELECT COL1 FROM TBL2` | Yes | `SELECT COL1 FROM TBL1  
INTERSECT  
SELECT COL1 FROM TBL2`  
`MINUS` | `SELECT COL1 FROM TBL1  
MINUS  
SELECT COL1 FROM TBL2` | Yes (`Convert MINUS` to `EXCEPT` in PostgreSQL) | `SELECT COL1 FROM TBL1  
EXCEPT  
SELECT COL1 FROM TBL2`  
  
#### Scalar (single-row) and group functions

Cloud SQL for PostgreSQL provides an extensive list of scalar (single-row) and aggregation functions. Some Cloud SQL for PostgreSQL functions are similar to their Oracle counterparts (by name and functionality, or under a different name but with similar functionality). Although Cloud SQL for PostgreSQL functions can have identical names to their Oracle counterparts, they sometimes exhibit different functionality.

The following tables describe where Oracle and Cloud SQL for PostgreSQL are equivalent by name and functionality (specified by "Yes") and where a conversion is recommended (all cases other than "Yes").

##### Character functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`CONCAT` | Returns _str1_ concatenated with _str2_ :   
  
`CONCAT('A', 1) = A1` | Yes | `CONCAT` | Equivalent to Oracle:  
  
`CONCAT('A', 1) = A1`  
`LOWER/UPPER` | Returns _char_ , with all letters lowercase or uppercase:  
  
`LOWER('SQL') = sql` | Yes | `LOWER/UPPER` | Equivalent to Oracle:  
  
`LOWER('SQL') = sql`  
`LPAD/RPAD` | Returns _expr1_ , left or right padded to length _n_ characters with the sequence of characters in _expr2_ :  
  
`LPAD('A',3,'*') = **A` | Yes | `LPAD/RPAD` | Equivalent to Oracle:  
  
`LPAD('A',3,'*') = **A`  
`SUBSTR` | Return a portion of _char_ , beginning at character position, substring-  
length characters long:   
  
`SUBSTR('PostgreSQL', 8, 3)  
= SQL` | Partially | `SUBSTR` | Equivalent to Oracle when the beginning position is a positive number.  
  
`SUBSTR('PostgreSQL', 8, 3)  
= SQL `   
When a negative number is supplied as a beginning position in Oracle, it performs a substring operation from the end of the string, which is different from Cloud SQL for PostgreSQL. Use the `RIGHT` function as a replacement if Oracle's behavior is desired.  
`INSTR` | Returns the position (index) of a specific string from a given string:  
  
`INSTR('PostgreSQL', 'e')  
= 7` | No | N/A | Cloud SQL for PostgreSQL does not have a built-in `instr` function. An Oracle-compatible `instr` function could be [implemented using PL/pgSQL](https://www.postgresql.org/docs/12/plpgsql-porting.html#PLPGSQL-PORTING-APPENDIX).  
`REPLACE` | Returns char with every occurrence of a search string replaced with a  
replacement string:   
  
`REPLACE('ORADB', 'ORA', 'PostgreSQL')  
= PostgreSQLDB` | Partially | `REPLACE` | The replacement string parameter is optional in Oracle while it is mandatory in Cloud SQL for PostgreSQL. When the parameter is omitted, Oracle removes all occurrences of the search strings. The same behavior could be achieved in Cloud SQL for PostgreSQL by supplying an empty string as the replacement string.  
  
`REPLACE('ORADB', 'ORA', 'PostgreSQL')  
= PostgreSQLDB`  
`TRIM` | Trim leading or trailing characters (or both) from a string:  
  
`TRIM(both '-' FROM '-PostgreSQL-')  
= PostgreSQL  
TRIM(' PostgreSQL ')  
= PostgreSQL` | Yes | `TRIM` | Equivalent to Oracle:  
  
`TRIM(both '-' FROM '-PostgreSQL-')  
= PostgreSQL  
TRIM(' PostgreSQL ')  
= PostgreSQL`  
`LTRIM/RTRIM` | Removes from the string's left or right end all of the characters that  
appear in the search:  
  
`LTRIM(' PostgreSQL', ' ')  
= PostgreSQL` | Yes | `LTRIM/RTRIM` | Equivalent to Oracle:  
  
`LTRIM(' PostgreSQL', ' ') = PostgreSQL`  
`ASCII` | Returns the decimal representation in the database character set of the first character of char:   
  
`ASCII('A') = 65` | Yes | `ASCII` | Equivalent to Oracle:  
  
`ASCII('A') = 65`  
`CHR` | Returns the ASCII code value, which is a numeric value between 0 and 225, to a character:  
  
`CHR(65) = A` | Yes | `CHAR` | Equivalent to Oracle:  
  
`CHR(65) = A`  
`LENGTH` | Return the length of a given string:  
  
`LENGTH ('PostgreSQL') = 10` | Yes | `LENGTH` | Equivalent to Oracle:  
  
`LENGTH ('PostgreSQL') = 10`  
`REGEXP_REPLACE` | Search a string for a regular expression pattern:  
  
`REGEXP_REPLACE('John', '[hn].', '1') = Jo1` | Yes | `REGEXP_REPLACE` | Equivalent to Oracle:  
  
`REGEXP_REPLACE('John', '[hn].', '1') = Jo1`  
`REGEXP_SUBSTR` | Extends the functionality of the SUBSTR function by searching a  
string for a regular expression pattern:  
  
`REGEXP_SUBSTR('https://console.cloud.google.com/sql/instances','https://([[:alnum:]]+\.?){3,4}/?')  
= https://console.cloud.google.com/` | No | N/A | Use PostgreSQL's `REGEXP_MATCH` to achieve similar functionalities.  
`REGEXP_COUNT` | Returns the number of times a pattern occurs in a source string. | No | N/A | Use PostgreSQL's `REGEXP_MATCH` to achieve similar functionalities.  
`REGEXP_INSTR` | Search a string position (index) for a regular  
expression pattern. | No | N/A | Convert the functionality to the application layer.  
`REVERSE` | Return a reversed string.  
  
`REVERSE('PostgreSQL') = LQSergtsoP` | Yes | `REVERSE` | Equivalent to Oracle:  
  
`REVERSE('PostgreSQL') = LQSergtsoP`  
  
##### Numeric functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`ABS` | Absolute value of n:   
  
`ABS(-4.6) = 4.6` | Yes | `ABS` | Equivalent to Oracle:  
  
`ABS(-4.6) = 4.6`  
`CEIL` | Returns the smallest integer that is greater than or equal to n:   
  
`CEIL(21.4) = 22` | Yes | `CEIL` | Equivalent to Oracle:  
  
`CEIL(21.4) = 22`  
`FLOOR` | Returns the largest integer equal to or less than n:   
  
`FLOOR(-23.7) = -24` | Yes | `FLOOR` | Equivalent to Oracle:  
  
`FLOOR(-23.7) = -24`  
`MOD` | Returns the remainder of `m` divided by `n`:  
  
`MOD(10, 3) = 1` | Yes | `MOD` | Equivalent to Oracle:  
  
`MOD(10, 3) = 1`  
`ROUND` | Returns n rounded to integer places to the right of the decimal point:  
  
`ROUND(1.39, 1) = 1.4` | Yes | `ROUND` | Equivalent to Oracle:  
  
`ROUND(1.39, 1) = 1.4`  
`TRUNC`   
(number) | Returns n1 truncated to n2 decimal places:  
  
`TRUNC(99.999) = 99  
TRUNC(99.999, 0) = 99` | Yes | `TRUNCATE`   
(number) | Equivalent to Oracle:  
  
`TRUNC(99.999) = 99  
TRUNC(99.999, 0) = 99`  
  
##### DateTime functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`SYSDATE` | Returns the current date and time set for the operating system on which the database server resides:  
  
`SELECT SYSDATE FROM DUAL   
= 31-JUL-2019` | Partially with different function name and formatting | `CURRENT_TIMESTAMP` | The `CURRENT_TIMESTAMP` will return a different datetime format than Oracle SYSDATE function:  
  
`SELECT CURRENT_TIMESTAMP   
= 2019-07-31 06:46:40.171477+00`  
`SYSTIMESTAMP` | Returns the system date, including fractional seconds and time zone:  
  
`SELECT SYSTIMESTAMP FROM DUAL   
= 01-JAN-19 07.37.11.622187000 AM +00:00` | Partially with different function name | `CURRENT_TIMESTAMP` | Cloud SQL for PostgreSQL returns a different date/time format than Oracle. Date formatting is required to match the original date/time formats:  
  
`SELECT CURRENT_TIMESTAMP   
= 2019-01-31 07:37:11.622187+00`  
`LOCAL TIMESTAMP` | Returns the current date and time in the session time zone in a value of data type `TIMESTAMP`:   
  
`SELECT LOCALTIMESTAMP FROM DUAL   
= 01-JAN-19 10.01.10.123456 PM` | Partially with different date/time formatting | `LOCAL TIMESTAMP` | Cloud SQL for PostgreSQL returns a different date/time format than Oracle. Date formatting is required to match the original date/time format:  
  
`SELECT LOCALTIMESTAMP   
= 2019-01-31 07:37:11.622187+00`  
`CURRENT_DATE` | Returns the current date in the session time zone:   
  
`SELECT CURRENT_DATE FROM DUAL   
= 31-JAN-19` | Partially with different date/time formatting | `CURRENT_ DATE` | Cloud SQL for PostgreSQL returns a different date/time format than Oracle. Date formatting is required to match the original date/time format:  
  
`SELECT CURRENT_DATE   
= 2019-01-31`  
`CURRENT_TIMESTAMP` | Returns the current date and time in the session time zone:   
  
`SELECT CURRENT_TIMESTAMP FROM DUAL   
= 31-JAN-19 06.54.35.543146 AM +00:00` | Partially with different datetime formatting | `CURRENT_TIMESTAMP` | Cloud SQL for PostgreSQL returns a different datetime format than Oracle. Date formatting will be required to match the original datetime format:  
  
`SELECT CURRENT_TIMESTAMP FROM DUAL   
= 2019-01-31 07:37:11.622187+00s`  
`ADD_MONTHS` | Returns the date plus integer months:  
  
`ADD_MONTHS(SYSDATE, 1)   
= 31-JAN-19` | No | N/A  | To achieve the same functionality in Cloud SQL for PostgreSQL, use the `+ / -` operators and specify the time interval:  
  
`SELECT CURRENT_TIMESTAMP + INTERVAL '1 MONTH'   
= 2019-01-31 07:37:11.622187+00s`  
`EXTRACT`   
(date part) | Returns the value of a specified date/time field from a date/time or interval expression:   
  
`EXTRACT(YEAR FROM DATE '2019-01-31')  
= 2019` | Yes | `EXTRACT`   
(date part) | Equivalent to Oracle:  
  
`EXTRACT(YEAR FROM DATE '2019-01-31')  
= 2019`  
`LAST_DAY` | Returns the date of the last day of the month that contains the specified date:  
  
`LAST_DAY('01-JAN-2019')   
= 31-JAN-19` | No | N/A  | As a workaround, use `DATE_TRUNC` and a `+` operator to compute the last day of the month. A date formatting is required to match the original date/time formatting:  
  
`SELECT DATE_TRUNC('MONTH', DATE '01-JAN-2019') + INTERVAL '1 MONTH -1 DAY'   
= 2019-01-31`  
`MONTH_BETWEEN` | Returns the number of months between dates date1 and date2:  
  
`MONTHS_BETWEEN(SYSDATE, SYSDATE-60)   
= 1.96` | Partially  
with   
Function different datetime formatting | `AGE` | The Cloud SQL for PostgreSQL `AGE` function returns the interval between two timestamps:  
  
`AGE(DATE '01-JAN-2019', DATE '01-JAN-2019' - 60)   
= 1 mon 29 days `   
To achieve the same values as Oracle `MONTH_BETWEEN` function, a more specific conversion is required.  
`TO_CHAR` (date/time) | Converts a datetime or timestamp to data type to a value of `VARCHAR2`  
data type in the format specified by the date format:   
  
`TO_CHAR(SYSDATE,'DD-MM-YYYY HH24:MI:SS')   
= 01-01-2019 10:01:01` | Yes | `To_CHAR` | Equivalent to Oracle:  
  
`TO_CHAR(CURRENT_TIMESTAMP,'DD-MM-YYYY HH24:MI:SS');   
01-01-2019 10:01:01`  
  
##### Encoding and decoding functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`DECODE` | Compares the expression to each search value one by one using an `IF-THEN-ELSE` statement. | No | `CASE` | Use the Cloud SQL for PostgreSQL `CASE` statement to achieve similar functionality.  
`DUMP` | Returns a `VARCHAR2` value containing the data type code, length in bytes, and internal representation of expression. | No | N/A | Not supported.  
`ORA_HASH` | Computes a hash value for a given expression. | No | `MD5 / SHA224 / SHA256 / SHA385 / SHA512` | Use the Cloud SQL for PostgreSQL `MD5` function for 128-bit checksum or the `SHA` function for 160-bit  
checksum in order to generate hash values.  
  
##### Conversion functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`CAST` | Converts one built-in data type or collection-typed value into another built-in data type or collection-typed value:   
  
`CAST('1' as int) + 1   
= 2` | Partially | `CAST` | The Cloud SQL for PostgreSQL `CAST` function is similar to Oracle's `CAST `functionality, but in certain cases it must be adjusted due to data type differences between the two databases:  
  
`CAST('1' as int) + 1   
= 2`  
`CONVERT` | Converts a character string from one character set to another:   
  
`CONVERT ( 'Ä Ê Í Õ Ø A B C D E ', 'US7ASCII', 'WE8ISO8859P1')   
= ?? ?? ?? A B C` | Partially | `CONVERT` | The Cloud SQL for PostgreSQL `CONVERT` function returns a `bytea` value, which is a binary string instead of `VARCHAR` or `TEXT`. The [character sets supported by PostgreSQL](https://www.postgresql.org/docs/12/multibyte.html) are also different from Oracle.  
  
`CONVERT('Ä Ê Í Õ Ø A B C D E', 'UTF8', 'LATIN1')   
= [Binary representation of the string in LATIN1 encoding]`  
`TO_CHAR`   
(string/numeric) | The function converts a number or date to a string:   
  
`TO_CHAR(22.73,'$99.9')   
= $22.7` | Partially | `TO_CHAR` | The Cloud SQL for PostgreSQL `TO_CHAR` function is functionality similar to Oracle. Cloud SQL for PostgreSQL supports a slightly different [list of formatting strings](https://www.postgresql.org/docs/12/functions-formatting.html#FUNCTIONS-FORMATTING-NUMERIC-TABLE). By default, Cloud SQL for PostgreSQL reserves one column for the sign, so there will be a space before positive numbers. This can be suppressed by using the `FM` prefix:  
  
`TO_CHAR(22.73,'FM$99.9')   
= $22.7`  
`TO_DATE` | The Oracle `TO_DATE` function converts a string to a date by the source-specific date/time format:  
  
`TO_DATE('2019/01/01', 'yyyy-mm-dd')   
= 01-JAN-2019` | Partially | `TO_DATE` | The Cloud SQL for PostgreSQL `TO_DATE` function is functionality similar to Oracle. Cloud SQL for PostgreSQL supports a slightly different [list of formatting strings](https://www.postgresql.org/docs/12/functions-formatting.html#FUNCTIONS-FORMATTING-DATETIME-TABLE):  
  
`TO_DATE('2019/01/01', 'yyyy-mm-dd')   
= 2019-01-01`  
`TO_NUMBER` | Converts the expression to a value of a `NUMBER` data type:   
  
`TO_NUMBER('01234')   
= 1234` | Partially | `TO_NUMBER` | The Cloud SQL for PostgreSQL `TO_NUMBER` function requires a formatting string as an input, while it is optional in Oracle:  
  
`TO_NUMBER('01234','99999')   
= 1234`   
An alternative is to use the `CAST` function for conversions that do not require complex formatting strings:  
  
`CAST('01234' AS NUMERIC)   
= 1234`  
  
##### Conditional SELECT functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`CASE` | The `CASE` statement chooses from a sequence of conditions and runs a  
corresponding statement with the following syntax:   
  
`CASE WHEN condition THEN result [WHEN ...] [ELSE result] END` | Yes | `CASE` | Equivalent to Oracle:  
  
`CASE WHEN condition THEN result [WHEN ...] [ELSE result] END`  
  
##### Null functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`COALESCE` | Returns the first non-null expression in the expression list:   
  
`COALESCE(null, '1', 'a')   
= a` | Yes | `COALESCE` | Equivalent to Oracle:  
  
`COALESCE(null, '1', 'a')   
= 1`  
`NULLIF` | Compare _expr1_ and _expr2_. If they are equal, the function returns null. If they are not equal, the function returns _expr1_ :   
  
`NULLIF('1', '2')   
= 1` | Yes | `NULLIF` | Equivalent to Oracle:  
  
`NULLIF('1', '2')   
= 1`  
`NVL` | Replace null (returned as a blank) with a string in the results of a query:   
  
`NVL(null, 'a')   
= a` | No | `COALESCE` | As an alternative, use the `COALESCE` function:  
  
`COALESCE(null, 'a')   
= a`  
`NVL2` | Determine the value returned by a query based on whether a specified  
expression is null or not null. | No | `COALESCE` | As an alternative, use the `COALESCE` function:  
  
`COALESCE(null, 1, 'a')   
= 1`  
  
##### Environment and identifier functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`SYS_GUID` | Generates and returns a globally unique identifier (RAW value) made  
up of 16 bytes:   
  
`SELECT SYS_GUID() FROM DUAL   
= 8EFA4A31468B4C6DE05011AC0200009E` | Partially with different function name and format | `UUID_GENERATE_V4` | CloudSQL for Cloud SQL for PostgreSQL supports the [uuid-ossp extension](https://www.postgresql.org/docs/12/uuid-ossp.html) which provides a list of UUID generating functions such as `UUID_GENERATE_V4`:  
  
`SELECT UUID_GENERATE_v4()`   
= eaf356a6-2847-478d-af3b-6883f5ac6af2  
`UID` | Returns an integer that uniquely identifies the session user (the user  
who logged on):   
  
`SELECT UID FROM DUAL   
= 43` | No | N/A | N/A  
`USER` | Returns the name of the current session user name:  
  
`SELECT USER FROM DUAL   
= UserName` | Yes | `USER` | Equivalent to Oracle:  
  
`SELECT USER;   
= postgres`  
`USERENV` | Returns information about the current user session with the current parameter configuration:  
  
`SELECT USERENV('LANGUAGE') FROM DUAL   
= ENGLISH_AMERICA.AL32UTF8` | No | N/A  | While there is not an equivalent `USERENV` function in Cloud SQL for PostgreSQL, individual parameters such as `USERENV('SID')` can be retrieved using [system information functions](https://www.postgresql.org/docs/12/functions-info.html) such as `PG_BACKGROUND_PID()`.  
`ROWID` | The Oracle server assigns each row in each table a unique `ROWID` to identify the row in the table. The `ROWID` is the address of the row that contains the data object number, the data block of the row, the row position, and the data file. | Partially with different function name | `ctid` | `ctid` in Cloud SQL for PostgreSQL identifies the physical location of the row version within its table, which is similar to Oracle's `ROWID`.  
`ROWNUM` | Returns a number that represents the order that a row is selected by Oracle from a table or joined tables. | No | `LIMIT or ROW_NUMBER()` | Instead of limiting the number of results returned by queries using `ROWNUM`, Cloud SQL for PostgreSQL supports [`LIMIT` and `OFFSET`](https://www.postgresql.org/docs/12/queries-limit.html) for similar purposes.  
  
`ROW_NUMBER()` [window function](https://www.postgresql.org/docs/12/functions-window.html) could be a workaround replacement for Oracle's `ROWNUM` for other scenarios. However, result ordering and performance deltas must be considered before using it as a replacement.  
  
##### Aggregate (group) functions

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`AVG` | Returns the average value of the column or expression. | Yes | `AVG` | Equivalent to Oracle  
`COUNT` | Returns the number of rows returned by a query. | Yes | `COUNT` | Equivalent to Oracle  
`COUNT (DISTINCT)` | Returns the number of unique values in the column or expression. | Yes | `COUNT  
(DISTINCT)` | Equivalent to Oracle  
`MAX` | Returns the maximum value of the column or expression. | Yes | `MAX` | Equivalent to Oracle  
`MIN` | Returns the minimum value of the column or expression. | Yes | `MIN` | Equivalent to Oracle  
`SUM` | Returns the sum of values of the column or expression. | Yes | `SUM` | Equivalent to Oracle  
`LISTAGG` | Displays the data within each group by a single row specified in the `ORDER BY` clause by concatenating the values of the measure column:   
  
`SELECT LISTAGG(  
DEPARTMENT_NAME, ', ')  
WITHIN GROUP  
(ORDER BY DEPARTMENT_NAME) DEPT  
FROM DEPARTMENTS;  
  
-- Single line results   
= Accounting, Administration, Benefits, Construction` | No | `STRING_AGG` | Use the Cloud SQL for PostgreSQL `STRING_AGG` function to return similar results as Oracle, expect syntax differences with certain cases:  
  
`SELECT STRING_AGG(DEPARTMENT_NAME, ', ' order by DEPARTMENT_NAME) FROM DEPARTMENTS;  
  
-- Single line results   
= Accounting, Administration, Benefits, Construction`  
  
##### Oracle 12c Fetch

Oracle function | Oracle function specification or implementation | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---|---  
`FETCH` | Retrieves rows of data from the result set of a multi-row query:  
  
`SELECT * FROM  
EMPLOYEES  
FETCH FIRST 10 ROWS ONLY;` | No | LIMIT | Use the Cloud SQL for PostgreSQL [`LIMIT`](https://www.postgresql.org/docs/12/queries-limit.html) clause to retrieve only a specific set of records:  
  
`SELECT * FROM EMPLOYEES LIMIT 10;`  
  
#### Basic filtering, operators, and subqueries

During conversion, basic filtering, operator functions, and subqueries are relatively straightforward, requiring minimal to no added effort.

**Conversion notes**

Examine and address date formats because Oracle and Cloud SQL for PostgreSQL formats return different default results:

  * Oracle `SYSDATE` function by default returns `01-AUG-19`.
  * PostgreSQL `CURRENT_DATE` function by default returns `2019-08-01` (no time of day even with formatting). To retrieve the current date and time, use the `CURRENT_TIMESTAMP` function which by default returns 2019-08-01 00:00:00.000000+00.
  * Date and time formats can be set using the Cloud SQL for PostgreSQL [`TO_CHAR`](https://www.postgresql.org/docs/12/functions-formatting.html) functions.

Oracle function or subquery | Cloud SQL for PostgreSQL equivalent | Cloud SQL for PostgreSQL corresponding function or subquery | Cloud SQL for PostgreSQL function specification or implementation  
---|---|---|---  
`EXISTS/ NOT EXISTS` | Yes | `EXISTS/ NOT EXISTS` | `SELECT * FROM DEPARTMENTS D  
WHERE EXISTS (SELECT 1  
FROM EMPLOYEES E  
WHERE  
E.DEPARTMENT_ID =  
D.DEPARTMENT_ID);`  
`IN/NOT IN` | Yes | `IN/NOT IN` | `SELECT * FROM DEPARTMENTS D  
WHERE DEPARTMENT_ID IN  
(SELECT DEPARTMENT_ID  
FROM EMPLOYEES E);  
  
-- OR   
SELECT * FROM EMPLOYEES  
WHERE (EMPLOYEE_ID, DEPARTMENT_ID)  
IN((100, 90));`  
`LIKE/NOT LIKE` | Yes | `LIKE/NOT LIKE` | `SELECT * FROM EMPLOYEES  
WHERE FIRST_NAME LIKE '_e_n%';`  
`BETWEEN/ NOT BETWEEN` | Yes | `BETWEEN/  
NOT BETWEEN` | `SELECT * FROM EMPLOYEES  
WHERE EXTRACT(YEAR FROM HIRE_DATE)  
NOT BETWEEN 2001 and 2004;`  
`AND/OR` | Yes | `AND/OR` | `SELECT * FROM EMPLOYEES  
WHERE DEPARTMENT_ID IN(100, 101)  
AND (SALARY >= 1000 OR HIRE_DATE <= '2006-02-05');`  
`SubQuery` | Yes | `SubQuery` | Cloud SQL for PostgreSQL supports subqueries in the `SELECT` level, for `JOIN` statements and for filtering in the `WHERE/AND` clauses:  
  
`-- SELECT SubQuery  
SELECT D.DEPARTMENT_NAME,  
(SELECT AVG(SALARY) AS AVG_SAL  
FROM EMPLOYEES E  
WHERE E.DEPARTMENT_ID =  
D.DEPARTMENT_ID) AVG_SAL  
FROM DEPARTMENTS D;  
  
-- JOIN SubQuery  
SELECT FIRST_NAME, LAST_NAME, SALARY  
FROM EMPLOYEES E JOIN  
(SELECT *  
FROM DEPARTMENTS  
WHERE LOCATION_ID = 2700) D  
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;  
  
-- Filtering Subquery  
SELECT FIRST_NAME,  
LAST_NAME,  
SALARY  
FROM EMPLOYEES  
WHERE SALARY < (SELECT AVG(SALARY)  
FROM EMPLOYEES);`  
Operators | Yes | Operators | Cloud SQL for PostgreSQL supports all the basic operators:  
  
`> | >= | < | <= | = | <> | !=`  
  
#### Analytical functions (or window and ranking functions)

Oracle analytical functions extend the functionality of standard SQL operations by providing capabilities to compute aggregate values on a group of rows (for example, `RANK()`, `ROW_NUMBER()`, `FIRST_VALUE()`). These functions are applied to logically partitioned records within the scope of a single query expression. They are commonly used in data warehousing, in conjunction with business intelligence reports and analytics.

**Conversion notes**

Cloud SQL for PostgreSQL supports many analytical functions They are known in Postgres as [aggregate functions](https://www.postgresql.org/docs/12/functions-aggregate.html) and [window functions](https://www.postgresql.org/docs/12/functions-window.html). If your application is using a less common function not supported in Postgres, you'll need to look for a [supported extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#postgresql-extensions-supported-by-cloud-sql) or move the logic to the application layer.

The following table lists Oracle's most common analytical functions.

Function family | Related functions | Supported by Cloud SQL for PostgreSQL  
---|---|---  
Analytical and ranking | `RANK  
AVERAGE_RANK  
DENSE_RANK  
ROW_NUMBER  
PERCENT_RANK  
CUME_DIST  
NTILE  
FIRST_VALUE  
LAST_VALUE  
OVER (PARTITION BY...)` | Yes (Except `AVERAGE_RANK`)  
Hierarchical | `CONNECT BY  
HIER_ANCESTOR  
HIER_CHILD_COUNT  
HIER_DEPTH  
HIER_LEVEL  
HIER_ORDER  
HIER_PARENT  
HIER_TOP` | No  
Lag | `LAG  
LAG_VARIANCE LAG_VARIANCE_PERCENT LEAD  
LEAD_VARIANCE LEAD_VARIANCE_PERCENT` | Yes (`LAG` and `LEAD` only)  
  
#### Common table expression (CTE)

CTEs provide a way to implement the logic of sequential code to reuse SQL code that might be too complex or not efficient for multiple use. CTEs can be named and then used multiple times in different parts of a SQL statement using the `WITH` clause. CTEs are supported by both Oracle and Cloud SQL for PostgreSQL.

##### Examples

Oracle and Cloud SQL for PostgreSQL |   
---|---  
`WITH DEPT_COUNT  
(DEPARTMENT_ID, DEPT_COUNT) AS  
(SELECT DEPARTMENT_ID,  
COUNT(*)  
FROM EMPLOYEES  
GROUP BY DEPARTMENT_ID)  
  
SELECT E.FIRST_NAME ||' '|| E.LAST_NAME AS EMP_NAME,  
D.DEPT_COUNT AS EMP_DEPT_COUNT  
FROM EMPLOYEES E JOIN DEPT_COUNT D  
USING (DEPARTMENT_ID)  
ORDER BY 2 DESC;` |   
  
#### MERGE statement

The `MERGE` (or `UPSERT`) statement provides a means to specify single SQL statements that conditionally perform DML operations in one `MERGE` operation, as opposed to a single DML operation, running separately. It selects records from the source table and then, by specifying a logical structure, automatically performs multiple DML operations on the target table. This feature helps you avoid using multiple inserts, updates, or deletes. Note that `MERGE` is a deterministic statement, meaning that once a row has been processed by the `MERGE` statement, it cannot be processed again using the same `MERGE` statement.

##### Conversion notes

Cloud SQL for PostgreSQL does not support the `MERGE` functionality, unlike Oracle. To partially simulate the `MERGE` functionality, Cloud SQL for PostgreSQL provides the [`INSERT ... ON CONFLICT DO UPDATE`](https://www.postgresql.org/docs/12/sql-insert.html) statements:

  * `INSERT… ON CONFLICT DO UPDATE`: If an inserted row would cause a unique violation or exclusion constraint violation error, the alternative action specified in the `ON CONFLICT DO UPDATE` clause is taken, for example:


    
    
    INSERT INTO tbl (a,b,c) VALUES (1,2,3)
      ON CONFLICT (a) DO UPDATE SET b = 2, c = 3;
    

Another solution would be to convert the `MERGE` functionality into a stored procedure to manage DML operations, using `INSERT`, `UPDATE`, and `DELETE` commands with exceptions and duplications handling.

#### SQL statement hints

Oracle provides a large collection of SQL query hints that lets users influence optimizer behavior, aiming to produce more efficient query execution plans. Cloud SQL for PostgreSQL does not offer a comparable, SQL statement level, hinting mechanism to influencing the optimizer.

To influence the query plans chosen by the query planner, Cloud SQL for PostgreSQL provides [a set of configuration parameters](https://www.postgresql.org/docs/12/runtime-config-query.html) that can be applied at the session level. The effects of these configuration parameters range from enabling/disabling a certain access method, to adjusting the planner cost constants. For example, the following statement disables the query planner's use of sequential scan plan types such as full table scans:
    
    
    SET ENABLE_SEQSCAN=FALSE;
    

To adjust planner's cost estimate of a random disk page fetch (default is 4.0), use the following statement:
    
    
    SET RANDOM_PAGE_COST=2.0;
    

Reducing this value causes Cloud SQL for PostgreSQL to prefer index scans. Enlarging it does the opposite.

##### Conversion notes

Because there are fundamental differences between the Oracle and Cloud SQL for PostgreSQL optimizers, and the fact that Cloud SQL for PostgreSQL does not support Oracle-style SQL query hints, we recommend that you remove any query hints during your migration to Cloud SQL for PostgreSQL. Then, perform rigorous performance testing through Cloud SQL for PostgreSQL tools, examine queries using execution plans and adjust the instance or session parameters according to the use case.

#### Execution plans

The main purpose of execution plans is to provide an inside look at the choices made by the query optimizer for accessing database data. The query optimizer generates execution plans for `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements for database users, also letting administrators have a better view on specific queries and DML operations. They are especially useful when you need to do performance tuning of queries—for example, to determine index performance or or to determine if there are missing indexes that need to be created.

Execution plans can be affected by data volumes, data statistics, and instance parameters (global or session parameters).

##### Conversion considerations

Execution plans are not database objects that need to be migrated; instead, they are a tool to analyze performance differences between Oracle and Cloud SQL for PostgreSQL running the same statement on identical data sets.

Cloud SQL for PostgreSQL does not support the same execution plan syntax, functionality, or output as Oracle.

Here's an example of an execution plan:

Oracle execution plan | Cloud SQL for PostgreSQL execution plan  
---|---  
`SQL> EXPLAIN PLAN FOR  
SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = 105;  
  
SQL> SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY (FORMAT=>'ALL +OUTLINE'));  
  
Plan hash value: 1833546154  
  
---------------------------------------------------------------------------------------------  
| Id | Operation | Name | Rows | Bytes | Cost (%CPU)| Time |  
---------------------------------------------------------------------------------------------  
| 0 | SELECT STATEMENT | | 1 | 69 | 1 (0)| 00:00:01 |  
| 1 | TABLE ACCESS BY INDEX ROWID| EMPLOYEES | 1 | 69 | 1 (0)| 00:00:01 |  
|* 2 | INDEX UNIQUE SCAN | EMP_EMP_ID_PK | 1 | | 0 (0)| 00:00:01 |  
---------------------------------------------------------------------------------------------` | `postgres=> EXPLAIN SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = 105; QUERY PLAN -------------------------------------------------------------------------------- Index Scan using emp_emp_id_pk on employees (cost=0.14..8.16 rows=1 width=71) Index Cond: (employee_id = '105'::numeric) (2 rows)`  
  
## Stored procedures, functions and triggers

PL/SQL is the Oracle extended procedural language for creating, storing, and applying code-based solutions within the database. In general, database stored procedures and functions are code elements consisting of ANSI SQL and SQL extended procedural language—for example, PL/SQL for Oracle and MySQL procedural language for MySQL. PL/pgSQL is for PostgreSQL's own extended procedural language.

The purpose of these stored procedures and functions is to provide solutions for requirements that are more suitable to run from within the database and not from the application (for example, performance, compatibility, and security). Although both stored procedures and functions use PL/SQL, stored procedures are used primarily to perform DDL/DML operations, and functions are primarily used to perform calculations to return specific results.

### PL/SQL to PL/pgSQL

From the Oracle PL/SQL to Cloud SQL for PostgreSQL migration perspective, PL/pgSQL is similar to Oracle PL/SQL in terms of its structure and syntax. However, there are a few main differences that necessitate a code migration. For example, data types are different between Oracle and Cloud SQL for PostgreSQL and a translation is often needed to make sure that the migrated code uses the corresponding data type names supported by Cloud SQL for PostgreSQL. For a detailed discussion of the differences between the two languages, see [Porting from Oracle PL/SQL](https://www.postgresql.org/docs/12/plpgsql-porting.html).

### Code object privileges and security

In Oracle, in order to create a stored procedure or function, the user must have the `CREATE PROCEDURE` system privilege (to create procedures or functions under other different users, the database users must have the `CREATE ANY PROCEDURE` privilege). To execute a stored procedure or a function, the database users must have the `EXECUTE` privilege.

In PostgreSQL, in order to create a code procedure or a function, the user must have the `USAGE` privilege. To execute a procedure or a function, the user must have `EXECUTE` privilege on the procedure or function.

By default, a PL/pgSQL procedure or function is defined as `SECURITY INVOKER`, which means the procedure or function is to be executed with the privileges of the user that calls it. Alternatively, `SECURITY DEFINER` could be specified so that the function is executed with the privileges of the user that owns it.

### Cloud SQL for PostgreSQL stored procedure and function syntax

The following example shows the Cloud SQL for PostgreSQL stored [procedure](https://www.postgresql.org/docs/12/sql-createprocedure.html) and [function](https://www.postgresql.org/docs/12/sql-createfunction.html) syntax:
    
    
    CREATE [ OR REPLACE ] PROCEDURE
        name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
      { LANGUAGE lang_name
        | TRANSFORM { FOR TYPE type_name } [, ... ]
        | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
        | SET configuration_parameter { TO value | = value | FROM CURRENT }
        | AS 'definition'
        | AS 'obj_file', 'link_symbol'
      } ...
    
    CREATE [ OR REPLACE ] FUNCTION
        name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
        [ RETURNS rettype
          | RETURNS TABLE ( column_name column_type [, ...] ) ]
      { LANGUAGE lang_name
        | TRANSFORM { FOR TYPE type_name } [, ... ]
        | WINDOW
        | IMMUTABLE | STABLE | VOLATILE | [ NOT ] LEAKPROOF
        | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
        | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
        | PARALLEL { UNSAFE | RESTRICTED | SAFE }
        | COST execution_cost
        | ROWS result_rows
        | SUPPORT support_function
        | SET configuration_parameter { TO value | = value | FROM CURRENT }
        | AS 'definition'
        | AS 'obj_file', 'link_symbol'
      } ...
    

### Triggers

A trigger is a stored procedure that gets fired when a specific event occurs. In Oracle, the triggering event is associated with either a table, a view, a schema, or the database. The type of triggering events include:

  * Data Manipulation Language (DML) statements (for example, `INSERT`, `UPDATE`, `DELETE`)
  * Data Definition Language (DDL) statements (for example, `CREATE`, `ALTER`, `DROP`)
  * Database Events (for example, `LOGON`, `STARTUP`, `SHUTDOWN`)



Oracle triggers could be of the following types:

  * Simple trigger: Fired exactly once, either before or after the specified triggering event
  * Compound trigger: Fired at multiple events
  * `INSTEAD OF` trigger: A special type of DML trigger to provide a transparent update mechanism for complex, non-editable views
  * System trigger: Fired at specific database events



In Cloud SQL for PostgreSQL, a trigger is fired before or after a DML operation on a specific table, view, or foreign table. The `INSTEAD OF` trigger is supported to provide an update mechanism to views. A trigger on DDL operations is called an [event trigger](https://www.postgresql.org/docs/12/event-trigger-definition.html). Cloud SQL for PostgreSQLdoes not support Oracle's system triggers based on database events.

Unlike Oracle triggers, Cloud SQL for PostgreSQL triggers do not support the use of an anonymous PL/pgSQL block as the trigger body. A named function that takes zero or more arguments and returns a type trigger must be supplied in the trigger declaration. This function is executed when the trigger fires.

### Cloud SQL for PostgreSQL trigger and event trigger syntax

The following example shows the Cloud SQL for PostgreSQL [trigger](https://www.postgresql.org/docs/12/sql-createtrigger.html) and [event trigger](https://www.postgresql.org/docs/12/sql-createeventtrigger.html) syntax:
    
    
    CREATE [ CONSTRAINT ] TRIGGER name { BEFORE | AFTER | INSTEAD OF } { event [ OR ... ] }
        ON table_name
        [ FROM referenced_table_name ]
        [ NOT DEFERRABLE | [ DEFERRABLE ] [ INITIALLY IMMEDIATE | INITIALLY DEFERRED ] ]
        [ REFERENCING { { OLD | NEW } TABLE [ AS ] transition_relation_name } [ ... ] ]
        [ FOR [ EACH ] { ROW | STATEMENT } ]
        [ WHEN ( condition ) ]
        EXECUTE { FUNCTION | PROCEDURE } function_name ( arguments )
    

`event` can be one of: `INSERT`, `UPDATE [ OF column_name [, ... ] ]`, `DELETE`, `TRUNCATE`
    
    
    CREATE EVENT TRIGGER name
        ON event
        [ WHEN filter_value IN (filter_value [, ... ]) [ AND ... ] ]
        EXECUTE { FUNCTION | PROCEDURE } function_name()
    

`event` can be one of: `ddl_command_start`, `ddl_command_end`, `table_rewrite`, `sql_drop`

`filter_value` can only be: `TAG`

`filter_value` can be one of the supported [command tags](https://www.postgresql.org/docs/12/event-trigger-matrix.html).

## What's next

  * Explore more about [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/users) user accounts.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
