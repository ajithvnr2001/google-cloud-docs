---
url: https://docs.cloud.google.com/solutions/converting-optimizing-queries-oracle-database-cloud-sql-mysql/
title: Converting and optimizing queries from Oracle Database to Cloud SQL for MySQL \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:31.801865+00:00
---

# Converting and optimizing queries from Oracle Database to Cloud SQL for MySQL  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/converting-optimizing-queries-oracle-database-cloud-sql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Converting and optimizing queries from Oracle Database to Cloud SQL for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses the basic query differences between Oracle® and Cloud SQL for MySQL, and how features in Oracle map to features in Cloud SQL for MySQL. It also outlines performance considerations for Cloud SQL for MySQL and ways to analyze and optimize query performance on Google Cloud. While this document touches on techniques to optimize stored procedures and triggers for Cloud SQL for MySQL, it does not cover how to translate PL/SQL code to MySQL stored procedures and functions.

When converting queries from Oracle Database to Cloud SQL for MySQL, there are certain SQL dialect differences to consider. There are also several built-in functions that are different or incompatible between the two database platforms.

## Basic query differences

While both Oracle and Cloud SQL for MySQL support ANSI SQL, there are several fundamental differences when querying data, mainly around the use of system functions.

The following table highlights the differences in the `SELECT` and `FROM` syntax for Oracle and Cloud SQL for MySQL.

Oracle feature name | Oracle implementation | Cloud SQL for MySQL support | Cloud SQL for MySQL equivalent  
---|---|---|---  
SQL basic syntax for data retrieval  |  `SELECT`  
`FROM`  
`WHERE`  
`GROUP BY`  
`HAVING`  
`ORDER BY` | Yes |  `SELECT`  
`FROM`  
`WHERE`  
`GROUP BY`  
`HAVING`  
`ORDER BY`  
`SELECT` for output print | ` SELECT 1 FROM DUAL ` | Yes |  `SELECT 1`  
or  
`SELECT 1 FROM DUAL`  
Column aliases | `SELECT COL1 AS C1` | Yes |  `SELECT COL1 AS C1`  
or  
`SELECT COL1 C1`  
Table name case sensitivity | No case sensitivity (for example, table name can be `orders` and `ORDERS`) | No | Case sensitive according to the defined table name (for example table name can be only `orders` or `ORDERS`)  
  
### Inline views

[Inline views](https://www.oracletutorial.com/oracle-view/inline-view-in-oracle/) (also known as derived tables) are `SELECT` statements, located in the `FROM` clause, and used as a subquery. Inline views can help make complex queries simpler by removing compound calculations or eliminating join operations, while condensing multiple separate queries into a single, simplified query.

**Note:** Oracle's inline views do not require the use of aliases, while Cloud SQL for MySQL inline views require a specific alias for each one.

The following example outlines a conversion example from Oracle 11g/12c to Cloud SQL for MySQL for an inline view.

An inline view in Oracle 11g/12c:
    
    
     SELECT FIRST_NAME,
                DEPARTMENT_ID,
                SALARY,
                DATE_COL
         FROM EMPLOYEES,
              (SELECT SYSDATE AS DATE_COL FROM DUAL);
    

A working view in Cloud SQL for MySQL 5.7 with an alias:
    
    
    SELECT FIRST_NAME,
                  DEPARTMENT_ID,
                  SALARY,
                  DATE_COL
           FROM EMPLOYEES, (SELECT SYSDATE() AS DATE_COL FROM DUAL) AS A1;
    

### Joins

Oracle's [join](https://www.oracletutorial.com/oracle-basics/oracle-joins/) types are supported by Cloud SQL for MySQL except for the `FULL JOIN`. Cloud SQL for MySQL joins support the use of alternate syntax, such as the `USING` clause, the `WHERE` clause instead of the `ON` clause, and the `SUBQUERY` in the `JOIN` statement.

The following table shows a `JOIN` conversion example.

Oracle `JOIN` type | Cloud SQL for MySQL support | Cloud SQL for MySQL `JOIN` syntax   
---|---|---  
`INNER JOIN` | Yes | ` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; `  
`CROSS JOIN` | Yes | ` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E CROSS JOIN DEPARTMENTS D `  
`FULL JOIN` | No | Consider using `UNION` with `LEFT` and `RIGHT JOINS:`  
` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID UNION SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E RIGHT JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; `  
` LEFT JOIN [ OUTER ] ` | Yes | ` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; `  
` RIGHT JOIN [ OUTER ] ` | Yes | ` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E RIGHT JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; `  
`SUBQUERY` | Yes | ` SELECT E.FIRST_NAME, D.DEPARTMENT_NAME FROM EMPLOYEES E JOIN (SELECT * FROM DEPARTMENTS)D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; `  
  
While Cloud SQL for MySQL supports both `UNION` and `UNION ALL` functions, it does not support Oracle's `INTERSECT` and `MINUS` functions:

  * `UNION` attaches the result sets of two `SELECT` statements after eliminating duplicate records.
  * `UNION ALL` attaches the result sets of two `SELECT` statements without eliminating duplicate records.
  * `INTERSECT` returns the intersection of two `SELECT` statements, only if a record exists in the result sets from both queries.
  * `MINUS` compares two or more `SELECT` statements, returning only distinct rows from the first query that are not returned by the second query.

**Note:** Use `JOIN`, `IN,`or `EXISTS` functions as a workaround when converting from the Oracle `INTERSECT` or `MINUS` functions to Cloud SQL for MySQL.

The following table shows some Oracle to Cloud SQL for MySQL conversion examples.

Oracle function | Oracle implementation | Cloud SQL for MySQL support | Cloud SQL for MySQL equivalent  
---|---|---|---  
`UNION` | `SELECT COL1 FROM TBL1`  
`UNION`  
`SELECT COL1 FROM TBL2` | Yes | `SELECT COL1 FROM TBL1`  
`UNION`  
`SELECT COL1 FROM TBL2`  
`UNION ALL` | `SELECT COL1 FROM TBL1`  
`UNION ALL`  
`SELECT COL1 FROM TBL2` | Yes | `SELECT COL1 FROM TBL1`  
`UNION ALL`  
`SELECT COL1 FROM TBL2`  
`INTERSECT` | `SELECT COL1 FROM TBL1`  
`INTERSECT`  
`SELECT COL1 FROM TBL2` | No |  `SELECT COL1 FROM TBL1`  
`WHERE COL1 IN`  
`(SELECT COL1 FROM TBL2)`  
`MINUS` | `SELECT COL1 FROM TBL1`  
`MINUS`  
`SELECT COL1 FROM TBL2` | No | `SELECT A.COL1 FROM TBL1 A LEFT JOIN TBL2 B ON USING(COL1) WHERE B.COL1 IS NULL `  
  
### Scalar and group functions

Cloud SQL for MySQL provides an extensive list of scalar (single-row) and aggregation functions. Some of Cloud SQL for MySQL functions are similar to their Oracle counterparts (by name and functionality, or under a different name but with similar functionality). While some Cloud SQL for MySQL functions can have identical names to their Oracle counterparts, they can also exhibit different functionalities.

The following table describes where Oracle and Cloud SQL for MySQL character functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`CONCAT` | Returns the first string concatenated with the second string:   
`CONCAT('A', 1) = A1` | Yes | `CONCAT` | `CONCAT('A', 1) = A1`  
`CONCAT USING PIPE` | `FNAME |' '| LNAME` | No | `CONCAT` | `CONCAT(FNAME, ' ', LNAME)`  
`LOWER` or `UPPER` | Returns the string, with all letters in lowercase or in uppercase:  
`LOWER('SQL') = sql` | Yes | `LOWER` or `UPPER` | `LOWER('SQL') = sql`  
`LPAD/RPAD` | Returns `expression1`, left or right padded to length `n` characters with the sequence of characters in `expression2`:  
`LPAD('A',3,'*') = **A` | Yes | `LPAD` or `RPAD` | `LPAD('A',3,'*') = **A`  
`SUBSTR` | Returns a portion of the string, starting at position `x` (in this case 3), with a length of `y`. The first position in the string is 1.   
` SUBSTR('MySQL', 3, 3) = SQL ` | Yes | `SUBSTR` | ` SUBSTR('MySQL', 3, 3) = SQL `  
`INSTR` | Returns the position (index) of a string from a given string:  
` INSTR('MySQL', 'y') = 2 ` | Yes | `INSTR` | ` INSTR('MySQL', 'y') = 2 `  
`REPLACE` | Returns a string with every occurrence of a search string replaced with a replacement string:   
` REPLACE('ORADB', 'ORA', 'MySQL') = MySQLDB ` | Yes | `REPLACE` | ` REPLACE('ORADB', 'ORA', 'MySQL') = MySQLDB `  
`TRIM` | Trim leading or trailing characters (or both) from a string:  
` TRIM(both '-' FROM '-MySQL-') = MySQL TRIM(' MySQL ') = MySQL ` | Yes | `TRIM` | ` TRIM(both '-' FROM '-MySQL-') = MySQL TRIM(' MySQL ') = MySQL `  
`LTRIM/RTRIM` | Removes from the left side or right side of a string all characters that appear in the search:  
` LTRIM(' MySQL', ' ') = MySQL ` | Partially | `LTRIM or RTRIM` | Oracle `LTRIM` and `RTRIM` functions take a second parameter that specifies which leading or trailing characters to remove from the string. Cloud SQL for MySQL functions only remove leading and trailing whitespaces from the given string:  
` LTRIM(' MySQL') = MySQL `  
`ASCII` | Takes a single character and returns its numeric ASCII code:   
`ASCII('A') = 65` | Yes | `ASCII` | `ASCII('A') = 65`  
`CHR` | Returns the ASCII code value, which is a numeric value from 0 through 225, to a character:  
`CHR(65) = A` | Requires a different function name | `CHAR` | Cloud SQL for MySQL uses the `CHAR` function for the same functionality, so you need to change the function name:  
`CHAR(65) = A`  
`LENGTH` | Returns the length of a given string:  
`LENGTH('MySQL') = 5` | Yes | `LENGTH` | `LENGTH('MySQL') = 5`  
`REGEXP_REPLACE` | Searches a string for a regular expression pattern:   
`REGEXP_REPLACE('John', '[hn].', 'e') = Joe` | No | N/A | Supported as of MySQL version 8. As a workaround, use the `REPLACE` function if possible or move the logic to the application layer.  
`REGEXP_SUBSTR` | Extends the functionality of the `SUBSTR` function by searching a string for a regular expression pattern:  
` REGEXP_SUBSTR('https://console.cloud.google.com/sql/instances','https://([[:alnum:]]+\.?){3,4}/?') = https://console.cloud.google.com/ ` | No | N/A | Supported as of MySQL version 8. As a workaround, use the `SUBSTR` function if possible or move the logic to the application layer  
`REGEXP_COUNT` | Returns the number of times a pattern occurs in a source string | No | N/A | No equivalent function available for Cloud SQL for MySQL. Move this logic to the application layer.  
`REGEXP_INSTR` | Search a string position (index) for a regular expression pattern | No | N/A | Supported as of MySQL version 8. If on an older version, move this logic to the application layer.  
`REVERSE` | Returns the reversed string for a given string:  
` REVERSE('MySQL') = LQSyM ` | Yes | `REVERSE` | ` REVERSE('MySQL') = LQSyM `  
  
The following table describes where Oracle and Cloud SQL for MySQL numeric functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`ABS` | Returns the absolute value of a given number:   
`ABS(-4.6) = 4.6` | Yes | `ABS` | `ABS(-4.6) = 4.6`  
`CEIL` | Returns the smallest integer that is greater than or equal to the given number:   
`CEIL(21.4) = 22` | Yes | `CEIL` | `CEIL(21.4) = 22`  
`FLOOR` | Returns the largest integer equal to or less than the given number:   
`FLOOR(-23.7) = -24` | Yes | `FLOOR` | `FLOOR(-23.7) = -24`  
`MOD` | Returns the remainder of `m` divided by `n`:  
`MOD(10, 3) = 1` | Yes | `MOD` | `MOD(10, 3) = 1`  
`ROUND` | Returns `n` rounded to integer places to the right of the decimal point:  
`ROUND(1.39, 1) = 1.4` | Yes | `ROUND` | `ROUND(1.39, 1) = 1.4`  
`TRUNC`(number) | Returns `n1` truncated to `n2` decimal places. The second parameter is optional.   
` TRUNC(99.999) = 99 TRUNC(99.999, 0) = 99 ` | Requires a different function name | `TRUNCATE`(number) | Cloud SQL for MySQL function has a different name and the second parameter is mandatory.   
`TRUNCATE(99.999, 0) = 99`  
  
The following table describes where Oracle and Cloud SQL for MySQL `datetime` functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`SYSDATE` | Returns the current date and time set for the operating system on which the database server resides:  
` SELECT SYSDATE FROM DUAL; = 31-JUL-2019 ` | Yes | `SYSDATE()` | Cloud SQL for MySQL `SYSDATE()` must include parentheses and returns by default a different `datetime` format than the Oracle `SYSDATE` function: ` SELECT SYSDATE() FROM DUAL; = 2019-01-31 10:01:01.0 ` You can change the `datetime` format at the session level  
`SYSTIMESTAMP` | Returns the system date, including fractional seconds and time zone:  
` SELECT SYSTIMESTAMP FROM DUAL = 01-JAN-19 07.37.11.622187000 AM +00:00 ` | Requires a different function name | ` CURRENT_ TIMESTAMP ` | Cloud SQL for MySQL function returns a different `datetime` format by default. To reformat the output, use the `DATE_FORMAT()` function.  
` SELECT CURRENT_TIMESTAMP FROM DUAL; = 2019-01-31 06:55:07 `  
` LOCAL_ TIMESTAMP ` | Returns the current date and time as a `TIMESTAMP` type:  
` SELECT LOCALTIMESTAMP FROM DUAL = 01-JAN-19 10.01.10.123456 PM ` | Returns a different `datetime` format | ` LOCAL_ TIMESTAMP ` | Cloud SQL for MySQL function returns a different `datetime` format than the default format for Oracle. To reformat the output, use the `DATE_FORMAT()` function.   
` SELECT LOCAL_TIMESTAMP FROM DUAL = 2019-01-01 10:01:01.0 `  
`CURRENT_DATE` | Returns the current date:  
` SELECT CURRENT_DATE FROM DUAL = 31-JAN-19 ` | Returns a different `datetime` format | ` CURRENT_ DATE ` | Cloud SQL for MySQL function returns a different `datetime` format. To reformat the output, use the `DATE_FORMAT()` function.  
` SELECT CURRENT_DATE FROM DUAL = 2019-01-31 `  
` CURRENT_ TIMESTAMP ` | Returns the current date and time:  
` SELECT CURRENT_TIMESTAMP FROM DUAL = 31-JAN-19 06.54.35.543146 AM +00:00 ` `` | Returns a different `datetime` format | ` CURRENT_ TIMESTAMP ` | Cloud SQL for MySQL function returns a different `datetime` format. To reformat the output, use the `DATE_FORMAT()` function.  
` SELECT CURRENT_TIMESTAMP FROM DUAL = 2019-01-31 06:55:07 `  
`ADD_MONTHS` | Returns the date plus integer months:  
` ADD_MONTHS(SYSDATE, 1) = 31-JAN-19 ` | Requires a different function name | `ADDDATE` | Cloud SQL for MySQL function returns a different `datetime` format. To reformat the output, use the `DATE_FORMAT()` function.  
` ADDDATE(SYSDATE(), 1) = 2019-08-01 06:42:49.0 `  
`EXTRACT` (date part) | Returns the value of a `datetime` field based on an interval expression:  
` EXTRACT(YEAR FROM DATE '2019-01-31') = 2019 ` | Yes | `EXTRACT` (date part) | ` EXTRACT(YEAR FROM DATE '2019-01-31') = 2019 `  
`LAST_DAY` | Returns the last day of the month for a given date:  
` LAST_DAY('01-JAN-2019') = 31-JAN-19 ` | Partially | `LAST_DAY` | Cloud SQL for MySQL function returns a different `datetime` format than default format for Oracle. To reformat the output, use the `DATE_FORMAT()` function.  
` LAST_DAY('2019-01-01') = 2019-01-31 `  
` MONTH_ BETWEEN ` | Returns the number of months between the given dates `date1` and `date2`:  
` MONTHS_BETWEEN( SYSDATE, SYSDATE-60) = 1.96 ` | Partially | ` PERIOD_DIFF ` | Cloud SQL for MySQL `PERIOD_DIFF` function returns the difference in months as an integer number between two periods (formatted as `YYMM` or `YYYYMM`):  
` PERIOD_DIFF( '201903', '201901') = 2 `  
`TO_CHAR (Datetime)` | Converts a number, `datetime`, or timestamp type to a string type  
` TO_CHAR( SYSDATE,'DD-MM-YYYY HH24:MI:SS') = 01-01-2019 10:01:01 ` | Requires a different function name | `DATE_FORMAT` | Cloud SQL for MySQL `DATE_FORMAT` function formats a date value according to a format string:  
` DATE_FORMAT( SYSDATE(),'%d-%m-%Y %H:%i:%s') 01-01-2019 10:01:01 `  
  
The following table describes where Oracle and Cloud SQL for MySQL encoding and decoding functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent  | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`DECODE` | Compares the expression to each search value one by one using the functionality of an `IF-THEN-ELSE` statement | No | `CASE` | Use Cloud SQL for MySQL `CASE` statement for similar functionality  
`DUMP` | Returns a `VARCHAR2` value containing the data type code, length in bytes, and internal representation of expression | No | N/A | Not supported  
`ORA_HASH` | Computes a hash value for a given expression | No | `MD5 or SHA` | Use the `MD5` function for 128-bit checksums or the `SHA` function for 160-bit checksums  
  
The following table describes where Oracle and Cloud SQL for MySQL conversion functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`CAST` | Converts one built-in data type or collection-typed value into another built-in data type or collection-typed value:   
` CAST('1' as int) + 1 = 2 ` | Partially | `CAST` | Adjust depending on if an explicit or implicit conversion is required:  
` CAST('1' AS SIGNED) + 1 = 2 `  
`CONVERT` | Converts a character string from one-character set to another:   
` CONVERT ( 'Ä Ê Í Õ Ø A B C D E ', 'US7ASCII', 'WE8ISO8859P1') = ?? ?? ?? A B C ` | Partially | `CONVERT` | Cloud SQL for MySQL `CONVERT` function requires some adjustments to the syntax and parameters:  
` CONVERT( 'Ä Ê Í A B C ' USING utf8) = Ä Ê Í A B C `  
`TO_CHAR` (string/numeric) | The function converts a number or date to a string:   
` TO_CHAR(22.73,'$99.9') = $22.7 ` | No | `FORMAT` | Cloud SQL for MySQL `FORMAT` function converts a number to a format like `#,###,###.##`, rounding it to a decimal place and then returning the result as a string:  
` CONCAT('$', FORMAT(22.73, 1)) = $22.7 `  
`TO_DATE` | Oracle's `TO_DATE` function converts a string to a date based on a `datetimecode` format:  
` TO_DATE( '2019/01/01', 'yyyy-mm-dd') = 01-JAN-2019 ` | Requires a different function name | `STR_TO_DATE` | Cloud SQL for MySQL `STR_TO_DATE` function takes a string and returns a date based on a `datetime` format:  
` STR_TO_DATE( '2019/01/01', '%Y/%m/%d') = 2019-01-01 `  
`TO_NUMBER` | Converts expression to a value of a `NUMBER` data type:   
` TO_NUMBER('01234') = 1234 ` | Requires a different function name | `CAST` | Use the Cloud SQL for MySQL `CAST` function to return the same result as the Oracle `TO_NUMBER` function:  
` CAST('01234' as SIGNED) = 1234 `  
  
The following table describes where Oracle and Cloud SQL for MySQL conditional `SELECT` functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`CASE` | The `CASE` statement chooses from a sequence of conditions and runs a corresponding statement with the following syntax:   
` CASE WHEN condition THEN result [WHEN ...] [ELSE result] END ` | Yes | `CASE` | In addition to the `CASE` function, Cloud SQL for MySQL supports the use of `[IF/ELSE](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html)` conditional handling inside the `SELECT` statement:  
` CASE WHEN condition THEN result [WHEN ...] [ELSE result] END `  
  
The following table describes where Oracle and Cloud SQL for MySQL null functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`COALESCE` | Returns the first non-null expression in the expression list:  
` COALESCE( null, '1', 'a') = a ` | Yes | `COALESCE` | ` COALESCE( null, '1', 'a') = 1 `  
`NULLIF` | Performs a comparison between `expression1` and `expression2`. If they are equal, the function returns `null`. If they are not equal, the function returns `expression1`:   
` NULLIF('1', '2') = a ` | Yes | `NULLIF` | ` NULLIF('1', '2') = a `  
`NVL` | Replaces a `null` value with a string in the results of a query:  
` NVL(null, 'a') = a ` | No | `IFNULL` | ` IFNULL(null, 'a') = a `  
`NVL2` | Determines the value returned by a query based on whether an expression is null or not null | No | `CASE` | The `CASE` statement chooses from a sequence of conditions and runs a corresponding statement:  
` CASE WHEN condition THEN result [WHEN ...] [ELSE result] END `  
  
The following table describes where Oracle and Cloud SQL for MySQL environment and identifier functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`SYS_GUID` | Generates and returns a globally unique identifier (`RAW` value) made up of 16 bytes:  
` SELECT SYS_GUID() FROM DUAL = 8EFA4A31468B4C6DE05011AC0200009E ` | No | `REPLACE` and `UUID` | As a workaround, use the `REPLACE` and `UUID` functions to simulate the `SYS_GUID` function:  
` REPLACE( UUID(), '-', '') `  
`UID` | Returns an integer that uniquely identifies the session user (the user who is logged on):  
` SELECT UID FROM DUAL = 43 ` | No | N/A | N/A  
`USER` | Returns the username of the user who is connected to the current session:  
` SELECT USER FROM DUAL = username ` | Yes | `USER + INSTR + SUBSTR` | The Cloud SQL for MySQL `USER` function returns the username and host name (`root@IP_ADDRESS`) for the connection. To retrieve only the username, use the additional supporting functions:  
` SELECT SUBSTR(USER(), 1, INSTR(USER(), '@') -1) FROM DUAL = root `  
`USERENV` | Returns information about the current Oracle session, such as the language of the session:  
` SELECT USERENV('LANGUAGE') FROM DUAL = ENGLISH_AMERICA. AL32UTF8 ` | No | ` SHOW SESSION VARIABLES ` | Cloud SQL for MySQL `SHOW SESSION VARIABLES` statement returns the settings for the current session:  
` SHOW SESSION VARIABLES LIKE '%collation%'; = utf8_general_ci `  
`ROWID` | Oracle assigns each row of a table a unique `ROWID` to identify the row in the table. The `ROWID` is the address of the row that contains the data object number, the data block of the row, the row position, and the data file. | Partially | N/A |  `ROW_NUMBER()` is available starting in MySQL 8.0. If you're using an earlier version, emulate the same functionality by using a session variable `@row_number`.  
`ROWNUM` | Returns a number that represents the order that a row is returned by an Oracle table | Partially | N/A | `ROW_NUMBER()` is available starting in MySQL 8.0. If you're using an earlier version, emulate the same functionality by using a session variable `@row_number`.  
  
The following table describes where Oracle and Cloud SQL for MySQL aggregate (group) functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`AVG` | Returns the average value of a column or expression | Yes | `AVG` | Equivalent to Oracle  
`COUNT` | Returns the number of rows returned by a query | Yes | `COUNT` | Equivalent to Oracle  
` COUNT (DISTINCT) ` | Returns the number of unique values in the column or expression | Yes | ` COUNT (DISTINCT) ` | Equivalent to Oracle  
`MAX` | Returns the maximum value of a column or expression | Yes | MAX | Equivalent to Oracle  
`MIN` | Returns the minimum value of a column or expression | Yes | `MIN` | Equivalent to Oracle  
`SUM` | Returns the sum of a value of a column or expression | Yes | `SUM` | Equivalent to Oracle  
`LISTAGG` | Orders the data within each group specified in the `ORDER BY` clause and concatenates the values of the measure column:  
` SELECT LISTAGG( DEPARTMENT_NAME, ', ') WITHIN GROUP (ORDER BY DEPARTMENT_NAME) DEPT FROM DEPARTMENTS; -- Single line results = Accounting, Administration, Benefits, Construction ` | Requires a different function name and syntax | ` GROUP_ CONCAT ` | Use Cloud SQL for MySQL `GROUP_CONCAT` function to return equivalent results:  
` SELECT GROUP_CONCAT( DEPARTMENT_NAME ORDER BY DEPARTMENT_NAME SEPARATOR ', ') DEPT FROM DEPARTMENTS; -- Single line results = Accounting, Administration, Benefits, Construction `  
  
The following table describes where Oracle and Cloud SQL for MySQL `FETCH` function is equivalent by name and functionality.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function | Cloud SQL for MySQL implementation  
---|---|---|---|---  
`FETCH` | Retrieves a specified number of rows from the result set of a multi-row query:  
` SELECT * FROM EMPLOYEES FETCH FIRST 10 ROWS ONLY; ` | Yes | `LIMIT` | Use the MySQL [`LIMIT`](https://dev.mysql.com/doc/refman/5.7/en/select.html) clause to retrieve rows from a query:  
` SELECT * FROM EMPLOYEES LIMIT 10; `  
  
### Basic filtering, operators, and subqueries

Basic filtering, operator functions, and subqueries are relatively straightforward to convert, with nominal effort required. Most of the effort revolves around converting date formats because Oracle and Cloud SQL for MySQL use different default date formats:

  * The Oracle `SYSDATE` function returns this format by default: `01-AUG-19`.
  * The Cloud SQL for MySQL `SYSDATE()` function returns this format by default: `2019-08-01 12:04:05`.



To set date and time formats, use the MySQL [`DATE_FORMAT`](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_date-format) or the [`STR_TO_DATE`](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_str-to-date) functions.

The following table describes where Oracle and Cloud SQL for MySQL basic filtering, operators, and subquery functions are equivalent by name and functionality, and where a conversion is recommended.

Oracle function | Oracle implementation | Cloud SQL for MySQL equivalent | Cloud SQL for MySQL function  
---|---|---|---  
` EXISTS/ NOT EXISTS ` | Yes | ` EXISTS/ NOT EXISTS ` | ` SELECT * FROM DEPARTMENTS D WHERE EXISTS (SELECT 1 FROM EMPLOYEES E WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID); `  
`IN/NOT IN` | Yes | `IN/NOT IN` | ` SELECT * FROM DEPARTMENTS D WHERE DEPARTMENT_ID IN (SELECT DEPARTMENT_ID FROM EMPLOYEES E); -- OR SELECT * FROM EMPLOYEES WHERE (EMPLOYEE_ID, DEPARTMENT_ID) IN((100, 90)); `  
`LIKE/NOT LIKE` | Yes | `LIKE/NOT LIKE` | ` SELECT * FROM EMPLOYEES WHERE FIRST_NAME LIKE '_e_n%'; `  
` BETWEEN/ NOT BETWEEN ` | Yes | ` BETWEEN/ NOT BETWEEN ` | ` SELECT * FROM EMPLOYEES WHERE EXTRACT(YEAR FROM HIRE_DATE) NOT BETWEEN 2001 and 2004; `  
`AND/OR` | Yes | `AND/OR` | ` SELECT * FROM EMPLOYEES WHERE DEPARTMENT_ID IN(100, 101) AND (SALARY >= 1000 OR HIRE_DATE <= '2006-02-05'); `  
`SubQuery` | Yes | `SubQuery` | Cloud SQL for MySQL supports subqueries in the `SELECT` clause, in the `JOIN` clause, and for filtering in the `WHERE/AND` clauses:  
` -- SELECT Subquery SELECT D.DEPARTMENT_NAME, (SELECT AVG(SALARY) AS AVG_SAL FROM EMPLOYEES E WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID) AVG_SAL FROM DEPARTMENTS D; -- JOIN Subquery SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEES E JOIN (SELECT * FROM DEPARTMENTS WHERE LOCATION_ID = 2700) D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID; -- Filtering Subquery SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEES WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES); `  
Operators | Yes | Operators | Cloud SQL for MySQL supports all basic operators:  
`> | >= | < | <= | = | <> | !=`  
  
## Best practices for Cloud SQL for MySQL queries

To maintain comparable levels of performance between Cloud SQL for MySQL and Oracle, you might need to optimize your queries. These optimizations include changing the index structures and adjusting the database schema. This section provides a few guidelines to help you achieve comparable query performance on Cloud SQL for MySQL.

### Create a clustered index

When using the [InnoDB storage engine](https://wikipedia.org/wiki/InnoDB), a best practice is to define a table with a primary key, because this key creates a clustered index on that table. In addition to improving query performance, this approach also lets you create additional secondary indexes. You want to avoid creating too many indexes, though. Having redundant indexes does not improve performance and can slow down [DML](https://wikipedia.org/wiki/Data_manipulation_language) execution. This best practice leads to a second best practice: regularly monitor for redundant indexes, and if you have any redundant ones, drop them from the database.

Use the following query to identify tables with no primary keys so that you can create primary keys for them:
    
    
    mysql> SELECT t.table_schema, t.table_name
           FROM information_schema.tables t LEFT JOIN
           information_schema.statistics s
           ON t.table_schema=s.table_schema AND t.table_name=s.table_name
           AND s.non_unique=0
           WHERE s.table_name IS NULL
           AND t.table_schema NOT IN('sys', 'information_schema', 'mysql',
           'performance_schema')
           AND t.`TABLE_TYPE` <> 'VIEW';
    

Use the following query to find tables which have no indexes so you can create indexes for them:
    
    
    mysql> SELECT t.table_schema, t.table_name FROM INFORMATION_SCHEMA.tables t
           WHERE table_name NOT IN
                 (SELECT  table_name FROM (
                          SELECT  table_name, index_name
                          FROM information_schema.statistics
                      GROUP BY  table_name, index_name) tab_ind_cols
               GROUP BY table_name)
    AND table_schema NOT IN('sys', 'information_schema', 'mysql', 'performance_schema')
    AND TABLE_TYPE <> 'VIEW';
    

Use the following query to check for redundant indexes so that you can remove the redundancies:
    
    
    mysql> SELECT * FROM sys.schema_redundant_indexes;
    

### Adjust query parameters

To tune query performance, you might need to adjust session parameters. Cloud SQL for MySQL has a set of [flags](https://docs.cloud.google.com/sql/docs/mysql/flags) that you can alter for this purpose, including the following flags:

  * InnoDB-related parameters
  * `SORT` parameters
  * `JOIN` parameters
  * Cache-handling parameters



### Monitor queries

Slow-running queries can cause the system to stop responding or lead to other bottlenecks, so it's important to regularly monitor queries.

There are several ways to diagnose slow-running SQL statements:

  * Use the [Cloud SQL for MySQL dashboard](https://docs.cloud.google.com/sql/docs/mysql/instance-info) for real-time and historical insights on slow-running queries.
  * Use [Cloud Monitoring](https://docs.cloud.google.com/community/tutorials/stackdriver-monitor-slow-query-mysql) to monitor the Cloud SQL for MySQL slow query log.
  * Use the Cloud SQL for MySQL `statement_analysis` view to see the runtime statistics about a SQL statement:
        
        mysql> SELECT * FROM sys.statement_analysis;
        




## Analyze Cloud SQL for MySQL queries

The query optimizer in Cloud SQL for MySQL generates an execution plan for `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements. These plans are useful when you adjust a slow-running query. There are a few considerations to keep in mind:

  * Execution plans are not database objects that need to be migrated; rather, they are a tool for analyzing performance differences between Oracle and Cloud SQL for MySQL running the same statement on identical datasets.
  * Cloud SQL for MySQL does not support the same execution plan syntax, functionality, or output as Oracle.



Here is an example plan to illustrate the differences between an Oracle execution plan and a Cloud SQL for MySQL execution plan:
    
    
    SQL> EXPLAIN PLAN FOR
         SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = 105;
    
    SQL> SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY (FORMAT=>'ALL +OUTLINE'));
    
    Plan hash value: 1833546154
    
    ---------------------------------------------------------------------------------------------
    | Id  | Operation                   | Name          | Rows  | Bytes | Cost (%CPU)| Time     |
    ---------------------------------------------------------------------------------------------
    |   0 | SELECT STATEMENT            |               |     1 |    69 |     1   (0)| 00:00:01 |
    |   1 |  TABLE ACCESS BY INDEX ROWID| EMPLOYEES     |     1 |    69 |     1   (0)| 00:00:01 |
    |*  2 |   INDEX UNIQUE SCAN         | EMP_EMP_ID_PK |     1 |       |     0   (0)| 00:00:01 |
    ---------------------------------------------------------------------------------------------
    
    mysql> EXPLAIN SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = 105;
    
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
    | id | select_type | table     | partitions | type  | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
    |  1 | SIMPLE      | EMPLOYEES | NULL       | const | PRIMARY       | PRIMARY | 3       | const |    1 |   100.00 | NULL  |
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
    

### Optimize stored procedures and triggers

In contrast to Oracle, Cloud SQL for MySQL stored procedures and functions are parsed at each execution. A helpful tool for benchmarking stored procedure and function performance is the [MySQL `BENCHMARK()` utility](https://dev.mysql.com/doc/refman/8.0/en/select-benchmarking.html). This tool takes two parameters, an iteration count and an expression, and estimates the runtime of the given expression (for example, stored procedure, function, and `SELECT` statement). The output represents the approximate total runtime over all iterations.

The following is an example to illustrate the `BENCHMARK()` utility:
    
    
    -- SELECT Expression Example
    
    mysql> select benchmark(10000000, 'select sysdate()');
    +-----------------------------------------+
    | benchmark(10000000, 'select sysdate()') |
    +-----------------------------------------+
    |                                       0 |
    +-----------------------------------------+
    1 row in set (0.12 sec)
    
    -- Result: Run time of 0.12 sec for 1,0000,000 iterations
    
    -- FUNCTION Example
    mysql> select benchmark(1000000, func1());
    +-----------------------------+
    | benchmark(1000000, func1()) |
    +-----------------------------+
    |                           0 |
    +-----------------------------+
    1 row in set (2.54 sec)
    
    -- Result: Run time of 2.54 sec for 1,000,000 iterations
    

If you notice a performance regression during the conversion, use the MySQL `EXPLAIN` command to identify possible factors contributing to the regression. One common solution for slow performance is to alter a table index structure to accommodate the MySQL optimizer. Another common practice is to optimize a converted PL/SQL code by reducing unnecessary data retrieval or by using temporary tables within the procedural MySQL code.

## What's next

  * Explore more about [MySQL](https://docs.cloud.google.com/sql/docs/mysql/users) user accounts.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
