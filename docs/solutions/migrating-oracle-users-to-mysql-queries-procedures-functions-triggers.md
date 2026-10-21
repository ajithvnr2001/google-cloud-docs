---
url: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-queries-procedures-functions-triggers/
title: Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:30.546360+00:00
---

# Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-queries-procedures-functions-triggers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to Cloud SQL for MySQL version 5.7, second-generation instances. The series includes the following parts:

  * [Migrating Oracle users to Cloud SQL for MySQL: Terminology and functionality](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-terminology)
  * [Migrating Oracle users to Cloud SQL for MySQL: Data types, users, and tables](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-data-users-tables)
  * Migrating Oracle users to Cloud SQL for MySQL: Queries, stored procedures, functions, and triggers (this document)
  * [Migrating Oracle users to Cloud SQL for MySQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-mysql-security-ops-monitoring-logging)



## Queries

Oracle and Cloud SQL for MySQL support the ANSI SQL standard. It's generally straightforward to migrate SQL statements by using only basic syntax elements (for example, not specifying any scalar functions or any other Oracle extended feature). The following section discusses common Oracle query elements and their corresponding Cloud SQL for MySQL equivalents.

### Basic SELECT and FROM syntax

Oracle feature name or syntax name | Oracle overview or implementation | MySQL support | MySQL corresponding or alternative solution  
---|---|---|---  
**SQL basic syntax for data retrieval** | 
    
    
    SELECT
    FROM
    WHERE
    GROUP BY
    HAVING
    ORDER BY
    

| Yes | 
    
    
    SELECT
    FROM
    WHERE
    GROUP BY
    HAVING
    ORDER BY
      
  
**`SELECT` for output print** | 
    
    
    SELECT 1 FROM DUAL
    

| Yes | 
    
    
    SELECT 1
    OR
    SELECT 1 FROM DUAL
      
  
**Column aliases** | 
    
    
    SELECT COL1 AS C1
    

| Yes | 
    
    
    SELECT COL1 AS C1
    OR
    SELECT COL1 C1
      
  
**Table name**  
**case sensitivity** | No case sensitivity  
(for example, table name can be `orders` and/or `ORDERS`). | No | Case sensitive according to the defined table name (for example, table name can be only `orders` or `ORDERS`).  
  
You can read more details on MySQL's [`SELECT` syntax](https://dev.mysql.com/doc/refman/5.7/en/select.html).

  * **In-line views**
    * In-line views (also known as _derived tables_) are `SELECT` statements, located in the `FROM` clause and used as a subquery.
    * Inline views can help make complex queries simpler by removing compound calculations or eliminating join operations, while condensing several separate queries into a single, simplified query.
    * **Conversion note** : Oracle in-line views do not require the use of aliases, while MySQL do require specific aliases for each in-line view.



The following table presents a conversion example from Oracle to MySQL, as an in-line view.

Oracle 11g/12c  
---  
      
    
    SQL> SELECT FIRST_NAME,
                DEPARTMENT_ID,
                SALARY,
                DATE_COL
         FROM EMPLOYEES,
              (SELECT SYSDATE AS DATE_COL FROM DUAL);
    

  
The output is similar to the following:  

    
    
    FIRST_NAME           DEPARTMENT_ID     SALARY DATE_COL
    -------------------- ------------- ---------- ---------
    Steven                          90      24000 30-JUL-19
    Neena                           90      17000 30-JUL-19
    Lex                             90      17000 30-JUL-19
      
  
**Cloud SQL for MySQL 5.7**  
**Without alias for the in-line view:**  

    
    
    mysql> SELECT FIRST_NAME,
                  DEPARTMENT_ID,
                  SALARY,
                  DATE_COL
           FROM EMPLOYEES, (SELECT SYSDATE() AS DATE_COL FROM DUAL);
      
    
    ERROR 1248 (42000): Every derived table must have its own alias
    

  
**Adding an alias to the in-line view:**  

    
    
    mysql> SELECT FIRST_NAME,
                  DEPARTMENT_ID,
                  SALARY,
                  DATE_COL
           FROM EMPLOYEES, (SELECT SYSDATE() AS DATE_COL FROM DUAL) AS A1;
    

  
The output is similar to the following:  

    
    
    +-------------+---------------+----------+---------------------+
    | FIRST_NAME  | DEPARTMENT_ID | SALARY   | DATE_COL            |
    +-------------+---------------+----------+---------------------+
    | Steven      |            90 | 23996.00 | 2019-07-30 09:28:00 |
    | Neena       |            90 | 22627.00 | 2019-07-30 09:28:00 |
    | Lex         |            90 | 22627.00 | 2019-07-30 09:28:00 |
      
  
### JOIN statements

Oracle `JOIN` statements are supported by MySQL [`JOIN`](https://dev.mysql.com/doc/refman/5.7/en/join.html) statements, except for the `FULL JOIN` clause. Additionally, MySQL `JOIN` statements support the use of alternate syntax, such as the `USING` clause, the `WHERE` clause instead of `ON` clause, and using `SUBQUERY` in the `JOIN` statement.

The following table presents a JOIN conversion example.

Oracle JOIN type | Supported by MySQL | MySQL JOIN syntax  
---|---|---  
      
    
    INNER JOIN
    

| Yes | 
    
    
    SELECT E.FIRST_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E JOIN DEPARTMENTS D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
      
      
    
    CROSS JOIN
    

| Yes | 
    
    
    SELECT E.FIRST_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E CROSS JOIN DEPARTMENTS D
      
      
    
    FULL JOIN
    

| No | For a workaround, consider using `UNION` with `LEFT` and` RIGHT JOIN` statements.  
      
    
    LEFT JOIN
    [ OUTER ]
    

| Yes | 
    
    
    SELECT E.FIRST_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
      
      
    
    RIGHT JOIN
    [ OUTER ]
    

| Yes | 
    
    
    SELECT E.FIRST_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E RIGHT JOIN DEPARTMENTS D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
      
      
    
    SUBQUERY
    

| Yes | 
    
    
    SELECT E.FIRST_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E JOIN (SELECT * FROM DEPARTMENTS)D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
      
  
#### UNION, UNION ALL, INTERSECT, and MINUS

MySQL does not support Oracle `INTERSECT` and `MINUS` functions except for the `UNION` and `UNION ALL` functions:

  * `UNION`: Attaches the result sets of two or more `SELECT` statements and eliminate duplicate records.
  * `UNION ALL`: Attaches the result sets of two or more `SELECT` statements without eliminating duplicate records.
  * `INTERSECT`: Returns the intersection of two or more `SELECT` statements only if a record exists in both data sets.
  * `MINUS`: Compares two or more `SELECT` statements, returning only distinct rows from the first query that are not returned by the other statements.



**Conversion notes**

When converting from Oracle `INTERSECT` and `MINUS` functions into MySQL, use `JOIN` statements and `IN` and `EXISTS` as an alternative solution.

**Examples**

Oracle function | Oracle implementation | MySQL support | MySQL corresponding or alternative solution  
---|---|---|---  
      
    
    UNION
    

| 
    
    
    SELECT COL1 FROM TBL1
    UNION
    SELECT COL1 FROM TBL2
    

| Yes | 
    
    
    SELECT COL1 FROM TBL1
    UNION
    SELECT COL1 FROM TBL2
      
      
    
    UNION ALL
    

| 
    
    
    SELECT COL1 FROM TBL1
    UNION ALL
    SELECT COL1 FROM TBL2
    

| Yes | 
    
    
    SELECT COL1 FROM TBL1
    UNION ALL
    SELECT COL1 FROM TBL2
      
      
    
    INTERSECT
    

| 
    
    
    SELECT COL1 FROM TBL1
    INTERSECT
    SELECT COL1 FROM TBL2
    

| No | 
    
    
    SELECT COL1 FROM TBL1
    WHERE COL1 IN
    (SELECT COL1 FROM TBL2)
      
      
    
    MINUS
    

| 
    
    
    SELECT COL1 FROM TBL1
    MINUS
    SELECT COL1 FROM TBL2
    

| No | 
    
    
    SELECT A.COL1
    FROM TBL1 A LEFT JOIN TBL2 B
    ON USING(COL1)
    WHERE B.COL1 IS NULL
      
  
#### Scalar (single-row) and group functions

MySQL provides an extensive list of scalar (single-row) and aggregation functions. Some of MySQL functions are similar to their Oracle counterparts (by name and functionality, or under a different name but with similar functionality). Although MySQL functions can have identical names to their Oracle counterparts, they can exhibit different functionality.

The following tables describe where Oracle and MySQL are equivalent by name and functionality (specified by "Yes") and where a conversion is recommended (all cases other than "Yes").

##### Character functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    CONCAT(_str1_ ,_str2_)
    

| Returns _str1_ concatenated with _str2_ :  

    
    
    CONCAT('A', 1) = A1
    

| Yes | 
    
    
    CONCAT
    

| Equivalent to Oracle:  

    
    
    CONCAT('A', 1) = A1
      
      
    
    LOWER/UPPER
    

| Returns char, with all letters lowercase or uppercase:  

    
    
    LOWER('SQL') = sql
    

| Yes | 
    
    
    LOWER/UPPER
    

| Equivalent to Oracle:  

    
    
    LOWER('SQL') = sql
      
      
    
    LPAD/RPAD(_expr1_ ,_n_ ,_expr2_)
    

| Returns _expr1_ , left or right padded to length _n_ characters with the sequence of characters in _expr2_ :  

    
    
    LPAD('A',3,'*') = **A
    

| Yes | 
    
    
    LPAD/RPAD
    

| Equivalent to Oracle:  

    
    
    LPAD('A',3,'*') = **A
      
      
    
    SUBSTR(_char_ ,_p_ ,_n_)
    

| Return a portion of _char_ , beginning at character position _p_ , substring length _n_ characters long:  

    
    
    SUBSTR('MySQL', 3, 3)
    = SQL
    

| Yes | 
    
    
    SUBSTR(_char_ ,_p_ ,_n_)
    

| Equivalent to Oracle:  

    
    
    SUBSTR('MySQL', 3, 3)
    = SQL
      
      
    
    INSTR(_index_ ,_str_)
    

| Returns the position (_index_) of the string _str_ :  

    
    
    INSTR('MySQL', 'y')
    = 2
    

| Yes | 
    
    
    INSTR
    

| Equivalent to Oracle:  

    
    
    INSTR('MySQL', 'y')
    = 2
      
      
    
    REPLACE(_char_ ,_str1_ ,_str2_)
    

| Returns char with every occurrence of a search string replaced with a replacement string:   

    
    
    REPLACE('ORADB', 'ORA', 'MySQL')
      
    
    = MySQLDB
    

| Yes | 
    
    
    REPLACE(_char_ ,_str1_ ,_str2_)
    

| Equivalent to Oracle:  

    
    
    REPLACE('ORADB', 'ORA', 'MySQL')
      
    
    = MySQLDB
      
      
    
    TRIM(_str_)
    

| Trim leading or trailing characters (or both) from a string:  

    
    
    TRIM(both '-' FROM '-MySQL-')
    = MySQL
      
    
    TRIM('  MySQL ')
    = MySQL
    

| Yes | 
    
    
    TRIM(_str_)
    

| Equivalent to Oracle:  

    
    
    TRIM(both '-' FROM '-MySQL-')
    = MySQL
      
    
    TRIM('  MySQL ')
    = MySQL
      
      
    
    LTRIM/RTRIM(_str_)
    

| Removes from the string's left or right end all of the characters that appear in the search:  

    
    
    LTRIM('   MySQL', ' ')
    = MySQL
    

| Partially | 
    
    
    LTRIM/RTRIM(_str_)
    

| Oracle `R/LTRIM` function except a replacement to parameter (whitespace or string). MySQL `R/LTRIM` only eliminates white spaces, accepting just the input string:  

    
    
    LTRIM('   MySQL')
    = MySQL
      
      
    
    ASCII(_char_)
    

| Returns the decimal representation in the database character set of the first character of _char_ :   

    
    
    ASCII('A') = 65
    

| Yes | 
    
    
    ASCII(_char_)
    

| Equivalent to Oracle:  

    
    
    ASCII('A') = 65
      
      
    
    CHR(_char_)
    

| Returns the ASCII code value, which is a numeric value between 0 and 225, to a character:  

    
    
    CHR(65) = A
    

| Partially with different function name | 
    
    
    CHAR(_char_)
    

| MySQL uses the `CHAR` function for the same functionality; thus, you must modify a function name:  

    
    
    CHAR(65) = A
      
      
    
    LENGTH(_str_)
    

| Return the length of a given string:  
  

    
    
    LENGTH ('MySQL') = 5
    

| Yes | 
    
    
    LENGTH(_str_)
    

| Equivalent to Oracle:  

    
    
    LENGTH('MySQL') = 5
      
      
    
    REGEXP_REPLACE(_str1_ ,_expr_ ,_str2_)
    

| Search a string for a regular expression pattern:  

    
    
    REGEXP_REPLACE('John', '[hn].', '1') = Jo1
    

| No | N/A | Supported only from MySQL version 8, as a workaround use the `REPLACE` function if possible or convert to the application layer  
      
    
    REGEXP_SUBSTR(_str_ ,_expr_)
    

| Extends the functionality of the `SUBSTR` function by searching a string for a regular expression pattern:  

    
    
    REGEXP_SUBSTR('https://console.cloud.google.com/sql/instances','https://([[:alnum:]]+\.?){3,4}/?')
    = https://console.cloud.google.com/
    

| No | N/A | Supported only from MySQL version 8. For a workaround, use the `SUBSTR` function if possible, or convert the functionality to the application layer.  
      
    
    REGEXP_COUNT(_str_ ,_expr_)
    

| Returns the number of times a pattern occurs in a source string. | No | N/A | For an alternative solution, convert the functionality to the application layer.  
      
    
    REGEXP_INSTR(_index_ ,_expr_)
    

| Search a string position (index) for a regular expression pattern. | No | N/A | Supported only from MySQL version 8.  
      
    
    REVERSE(_str_)
    

| Return a reversed string  

    
    
    REVERSE('MySQL')
    = LQSyM
    

| Yes | 
    
    
    REVERSE
    

| Equivalent to Oracle:  

    
    
    REVERSE('MySQL')
    = LQSyM
      
  
##### Numeric functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    ABS(_n_)
    

| Absolute value of _n_ :   

    
    
    ABS(-4.6) = 4.6
    

| Yes | 
    
    
    ABS
    

| Equivalent to Oracle:  

    
    
    ABS(-4.6) = 4.6
      
      
    
    CEIL(_n_)
    

| Returns the smallest integer that is greater than or equal to _n_ :  

    
    
    CEIL(21.4) = 22
    

| Yes | 
    
    
    CEIL
    

| Equivalent to Oracle:  

    
    
    CEIL(21.4) = 22
      
      
    
    FLOOR(_n_)
    

| Returns the largest integer equal to or less than _n_ :   

    
    
    FLOOR(-23.7) = -24
    

| Yes | 
    
    
    FLOOR
    

| Equivalent to Oracle:  

    
    
    FLOOR(-23.7) = -24
      
      
    
    MOD(_m_ ,_n_)
    

| Returns the remainder of _m_ divided by _n_ :  

    
    
    MOD(10, 3) = 1
    

| Yes | 
    
    
    MOD(_m_ ,_n_)
    

| Equivalent to Oracle:  

    
    
    MOD(10,3) = 1
      
      
    
    ROUND(_m_ ,_n_)
    

| Returns _m_ rounded to _n_ integer places to the right of the decimal point:  

    
    
    ROUND(1.39,1) = 1.4
    

| Yes | 
    
    
    ROUND
    

| Equivalent to Oracle:  

    
    
    ROUND(1.39,1) = 1.4
      
      
    
    TRUNC(_n1_ , _n2_)

| Returns _n1_ truncated to _n2_ decimal places:  

    
    
    TRUNC(99.999) = 99
    TRUNC(99.999,0) = 99
    

| Partially with different function name | 
    
    
    TRUNCATE(_n1_ , _n2_)

| The MySQL `TRUNCATE` function must accept an input number and an integer number to specify the accuracy amount to the right of the decimal point:  

    
    
    TRUNCATE(99.999,0) = 99
      
  
##### Date and time functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    SYSDATE
    

| Returns the current date and time set for the operating system on which the database server resides:  

    
    
    SELECT SYSDATE
    FROM DUAL
    = 31-JUL-2019
    

| Partially | 
    
    
    SYSDATE()
    

| The MySQL `SYSDATE()` must include parentheses and returns a different date/time format than the Oracle `SYSDATE` function:  

    
    
    SELECT SYSDATE()
    FROM DUAL;
    = 2019-01-31 10:01:01.0
    

  
Note that the date/time formatting can be changed at a session level  
      
    
    SYSTIMESTAMP
    

| Returns the system date, including fractional seconds and time zone:  

    
    
    SELECT SYSTIMESTAMP FROM DUAL
    = 01-JAN-19 07.37.11.622187000 AM +00:00
    

| Partially with different function name | 
    
    
    CURRENT_TIMESTAMP
    

| MySQL returns a different date/time formatting than Oracle. A date formatting is required (or a different date function) to match the original date/time formatting:  

    
    
    SELECT CURRENT_TIMESTAMP
    FROM DUAL
    = 2019-01-31 06:55:07
      
      
    
    LOCAL_TIMESTAMP
    

| Returns the current date and time in the session time zone in a value of data type `TIMESTAMP`:  

    
    
    SELECT LOCAL_TIMESTAMP
    FROM DUAL
    = 01-JAN-19 10.01.10.123456 PM
    

| Partially with different date/time formatting. | 
    
    
    LOCAL_TIMESTAMP
    

| MySQL returns different date/time formatting than Oracle. Date/time formatting is required (or a different date function) to match the original date/time formatting:  

    
    
    SELECT LOCAL_TIMESTAMP
    FROM DUAL
    = 2019-01-01 10:01:01.0
      
      
    
    CURRENT_DATE
    

| Returns the current date in the session time zone:  

    
    
    SELECT CURRENT_DATE
    FROM DUAL
    = 31-JAN-19
    

| Partially with different date/time formatting | 
    
    
    CURRENT_DATE
    

| MySQL returns a different date/time formatting than Oracle. Date/time formatting is required (or a different date function) to match the original date/time formatting:  

    
    
    SELECT CURRENT_DATE
    FROM DUAL
    = 2019-01-31
      
      
    
    CURRENT_TIMESTAMP
    

| Returns the current date and time in the session time zone:  

    
    
    SELECT CURRENT_TIMESTAMP
    FROM DUAL
    = 31-JAN-19 06.54.35.543146 AM +00:00
    

| Partially with different date/time formatting | 
    
    
    CURRENT_TIMESTAMP
    

| MySQL returns different date/time formatting than Oracle. Date/time formatting is required (or using a different date function) to match the original date/time formatting:  

    
    
    SELECT CURRENT_TIMESTAMP
    FROM DUAL
    = 2019-01-31 06:55:07
      
      
    
    ADD_MONTHS
    

| Returns the date plus integer months:  

    
    
    ADD_MONTHS(SYSDATE, 1)
    = 31-JAN-19
    

| Partially with different function name | 
    
    
    ADDDATE
    

| To achieve the same functionality MySQL uses the `ADDDATE` function:  

    
    
    ADDDATE(SYSDATE(), 1)
    = 2019-08-01 06:42:49.0
    

  
By default, MySQL returns different date/time and range/format than Oracle. Date/time formatting is required (or a different date function) to match the original date/time formatting.  
`EXTRACT`(_date part_) | Returns the value of a specified date/time field from a date/time or interval expression:  

    
    
    EXTRACT(YEAR FROM DATE '2019-01-31')
    = 2019
    

| Yes | `EXTRACT` (_date part_) | Equivalent to Oracle:  

    
    
    EXTRACT(YEAR FROM DATE '2019-01-31')
    = 2019
      
      
    
    LAST_DAY
    

| Returns the date of the last day of the month:  

    
    
    LAST_DAY('01-JAN-2019')
    = 31-JAN-19
    

| Partially with different date/time formatting | 
    
    
    LAST_DAY
    

| MySQL returns different date/time formatting than Oracle. Date/time formatting is required (or a different date function) to match the original date/time formatting:  

    
    
    LAST_DAY('2019-01-01')
    = 2019-01-31
      
      
    
    MONTH_BETWEEN
    

| Returns the number of months between dates date1 and date2:  

    
    
    MONTHS_BETWEEN(
    SYSDATE, SYSDATE-60)
    = 1.96
    

| Partially with different function name | 
    
    
    PERIOD_DIFF(_date1_ ,_date2_)
    

| The MySQL `PERIOD_DIFF` function returns the difference in months as an integer number between two periods (formatted as `YYMM` or `YYYYMM`):  

    
    
    PERIOD_DIFF(
    '201903', '201901')
    = 2
    

  
To achieve the same values as Oracle `MONTH_BETWEEN` function, a more specific conversion will be required  
`TO_CHAR` (date/time) | Converts a date/time or timestamp data type to a value of `VARCHAR2` data type in the format specified by the date format:  

    
    
    TO_CHAR(
    SYSDATE,'DD-MM-YYYY HH24:MI:SS')
    = 01-01-2019 10:01:01
    

| Partially with different function name | 
    
    
    DATE_FORMAT
    

| The MySQL `DATE_FORMAT` function formats a date as specified by a date format definition:  

    
    
    DATE_FORMAT(
    SYSDATE(),'%d-%m-%Y %H:%i:%s')
    = 01-01-2019 10:01:01
      
  
##### Encoding and decoding functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    DECODE
    

| Compares expression to each search value one by one using the functionality of an `IF-THEN-ELSE` statement | No | 
    
    
    CASE
    

| Use MySQL `CASE` statement to achieve similar functionality.  
      
    
    DUMP
    

| Returns a `VARCHAR2` value containing the data type code, length in bytes, and internal representation for a given expression. | No | N/A | Not supported.  
      
    
    ORA_HASH
    

| Computes a hash value for a given expression. | No | 
    
    
    MD5/SHA
    

| Use MySQL `MD5` for 128-bit checksum or the `SHA` function for 160-bit checksum in order to generate hash values  
  
##### Conversion functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    CAST
    

| Converts one built-in data type or collection-typed value into another built-in data type or collection-typed value:   

    
    
    CAST('1' as int) + 1
    = 2
    

| Partially | 
    
    
    CAST
    

| MySQL `CAST` function is similar to Oracle functionality, but in certain cases it must be adjusted depending on whether an explicit or implicit conversion is required:  

    
    
    CAST('1' AS SIGNED) + 1
    = 2
      
      
    
    CONVERT
    

| Converts a character string from one character set to another:   

    
    
    CONVERT('Ä Ê Í Õ Ø A B C D E ', 'US7ASCII', 'WE8ISO8859P1')
    = ?? ?? ?? A B C
    

| Partially | 
    
    
    CONVERT
    

| The MySQL `CONVERT` function requires some adjustments to the syntax and parameters in order to return the exact results as Oracle:  

    
    
    CONVERT('Ä Ê Í A B C ' USING utf8)
    = Ä Ê Í A B C
      
  
`TO_CHAR`   
(string/numeric) | The function converts a number or date to a string:   

    
    
    TO_CHAR(22.73,'$99.9')
    = $22.7
    

| No | 
    
    
    FORMAT
    

| The MySQL `FORMAT` function performs a formats of '#,###.##' from a number, rounding it to a certain number of decimal places and then it returns the result as a string, it has different functionality than Oracle:  

    
    
    CONCAT('$',
    FORMAT(22.73, 1))
    = $22.7
      
      
    
    TO_DATE
    

| The Oracle `TO_DATE` function converts a string to a date by the source specific date/time format:  

    
    
    TO_DATE(
    '2019/01/01', 'yyyy-mm-dd')
    = 01-JAN-2019
    

| Partially with different function name and date/time formatting | 
    
    
    STR_TO_DATE
    

| The MySQL `STR_TO_DATE` function takes a string and returns a date specified by date/time formatting:  

    
    
    STR_TO_DATE(
    '2019/01/01', '%Y/%m/%d')
    = 2019-01-01
      
      
    
    TO_NUMBER
    

| Converts expression to a value of a `NUMBER` data type:  

    
    
    TO_NUMBER('01234')
    = 1234
    

| No | 
    
    
    CAST
    

| For an alternative, use the MySQL `CAST` function to return the same result as Oracle `TO_NUMBER`:  

    
    
    CAST('01234' as SIGNED)
    = 1234
      
  
##### Conditional SELECT functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    CASE
    

| The `CASE` statement chooses from a sequence of conditions and runs a corresponding statement with the following syntax:  

    
    
    CASE WHEN condition THEN result
    [WHEN ...] [ELSE result]
    END
    

| Yes | 
    
    
    CASE
    

| In addition to the `CASE` function, MySQL is also supports the use of `[IF/ELSE](https://dev.mysql.com/doc/refman/8.0/en/flow-control-functions.html)` conditional handling inside the `SELECT` statement:  

    
    
    CASE WHEN condition THEN result
    [WHEN ...] [ELSE result]
    END
      
  
##### Null functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    COALESCE
    

| Returns the first non-null expression in the expression list:   

    
    
    COALESCE(
    null, '1', 'a')
    = a
    

| Yes | 
    
    
    COALESCE
    

| Equivalent to Oracle:  

    
    
    COALESCE(
    null, '1', 'a')
    = 1
      
      
    
    NULLIF
    

| Compare expr1 and expr2m. If they are equal, the function returns null. If they are not equal, the function returns expr1:   

    
    
    NULLIF('1', '2')
    = a
    

| Yes | 
    
    
    NULLIF
    

| Equivalent to Oracle:  

    
    
    NULLIF('1', '2')
    = a
      
      
    
    NVL
    

| Replace null (returned as a blank) with a string in the results of a query:   

    
    
    NVL(null, 'a')
    = a
    

| No | 
    
    
    IFNULL
    

| MySQL equivalent function would be the `IFNULL `function, which replaces null values with a given string:  

    
    
    IFNULL(null, 'a')
    = a
      
      
    
    NVL2
    

| Determine the value returned by a query based on whether a specified  
expression is null or not null. | No | 
    
    
    CASE
    

| The CASE statement  
chooses from a sequence of conditions and runs a corresponding statement:  

    
    
    CASE WHEN condition THEN result
    [WHEN ...] [ELSE result]
    END
      
  
##### Environment and identifier functions

Oracle function | Oracle function specification or implementation | MySQL equivalent | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    SYS_GUID
    

| Generates and returns a globally unique identifier (RAW value) made up of 16 bytes:  

    
    
    SELECT SYS_GUID()
    FROM DUAL
    = 8EFA4A31468B4C6DE05011AC0200009E
    

| No | `REPLACE` and `UUID` | For a workaround, use the MySQL `REPLACE` and `UUID` functions to simulate the Oracle `SYS_GUID` function:  

    
    
    REPLACE(
    UUID(), '-', '')
      
      
    
    UID
    

| Returns an integer that uniquely identifies the session user (the user  
who logged on):   

    
    
    SELECT UID FROM DUAL
    = 43
    

| No | N/A | N/A  
      
    
    USER
    

| Returns the name of the current session user name:  

    
    
    SELECT USER FROM DUAL
    = UserName
    

| Partially | 
    
    
    USER + INSTR + SUBSTR
    

| The MySQL USER function returns the user name along with the connect server (`root@_IP_`). To retrieve only the user name, use additional supporting functions:  

    
    
    SELECT
    SUBSTR(USER(), 1, INSTR(USER(), '@') -1) FROM DUAL
    = root
      
      
    
    USERENV
    

| Returns information about the current user session with the current parameter configuration:  

    
    
    SELECT USERENV('LANGUAGE')
    FROM DUAL
    = ENGLISH_AMERICA.AL32UTF8
    

| No | 
    
    
    SHOW SESSION
    VARIABLES
    

| Use the MySQL `SHOW SESSION`  
`VARIABLES` statement to view the settings for the current session:  

    
    
    SHOW SESSION VARIABLES LIKE '%collation%';
    = utf8_general_ci
      
      
    
    ROWID
    

| The Oracle server assigns each row in each table a unique `ROWID` to identify the row in the table. The `ROWID` is the address of the row that contains the data object number, the data block of the row, the row position, and data file. | No | N/A | If possible, try to emulate the same functionality with other MySQL functions.  
      
    
    ROWNUM
    

| Returns a number that represents the order that a row is selected by Oracle from a table or joined tables. | No | N/A | If possible, try to emulate the same functionality with other MySQL functions or session variables.  
  
##### Aggregate (group) functions

Oracle function | Oracle function specification or  
implementation | MySQL  
equivalent  | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    AVG
    

| Returns average value of column or expression. | Yes | 
    
    
    AVG
    

| Equivalent to Oracle  
      
    
    COUNT
    

| Returns the number of rows returned by a query. | Yes | 
    
    
    COUNT
    

| Equivalent to Oracle  
      
    
    COUNT
    (DISTINCT)
    

| Returns the number of unique values in the column or expression. | Yes | 
    
    
    COUNT
    (DISTINCT)
    

| Equivalent to Oracle  
      
    
    MAX
    

| Returns the maximum value of column or expression. | Yes | 
    
    
    MAX
    

| Equivalent to Oracle  
      
    
    MIN
    

| Returns the minimum value of column or expression. | Yes | 
    
    
    MIN
    

| Equivalent to Oracle  
      
    
    SUM
    

| Returns the sum of value of column or expression. | Yes | 
    
    
    SUM
    

| Equivalent to Oracle  
      
    
    LISTAGG
    

| Displays the data within each group by a single row specified in the `ORDER BY` clause by concatenating the values of the measure column:  

    
    
    SELECT LISTAGG(
    DEPARTMENT_NAME, ', ')
    WITHIN GROUP
    (ORDER BY DEPARTMENT_NAME) DEPT
    FROM DEPARTMENTS;
      
    
    -- Single line results
      
    
    = Accounting, Administration, Benefits, Construction
    

| No | 
    
    
    GROUP_CONCAT
    

| Use the MySQL GROUP_CONCAT function to return similar results as Oracle, expect syntax differences with certain cases:  

    
    
    SELECT GROUP_CONCAT(
    DEPARTMENT_NAME ORDER BY DEPARTMENT_NAME SEPARATOR ', ') DEPT
    FROM DEPARTMENTS;
      
    
    -- Single line results
      
    
    = Accounting, Administration, Benefits, Construction
      
  
##### Oracle 12c Fetch

Oracle function | Oracle function specification or  
implementation | MySQL  
equivalent  | MySQL corresponding function | MySQL function specification or implementation  
---|---|---|---|---  
      
    
    FETCH
    

| Retrieves rows of data from the result set of a multi-row query:   

    
    
    SELECT * FROM
    EMPLOYEES
    FETCH FIRST 10 ROWS ONLY;
    

| No | LIMIT | Use the MySQL [`LIMIT`](https://dev.mysql.com/doc/refman/5.7/en/select.html) clause to retrieve only a specific set of records:  

    
    
    SELECT * FROM
    EMPLOYEES
    LIMIT 10;
      
  
#### Basic filtering, operators, and subqueries

During conversion, basic filtering, operator functions, and subqueries are relatively straightforward, requiring minimal to no added effort.

**Conversion notes**

Examine and address date formats because Oracle and MySQL formats return different default results:

  * Oracle `SYSDATE` function by default returns `01-AUG-19`.
  * MySQL `SYSDATE()` function by default returns `2019-08-01 12:04:05`.
  * Date and time formats can be set using the MySQL `[DATE_FORMAT](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_date-format)` or the `[STR_TO_DATE](https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_str-to-date)` functions.

Oracle function or subquery | MySQL equivalent  | MySQL corresponding function or subquery | MySQL function specification or implementation  
---|---|---|---  
      
    
    EXISTS/NOT EXISTS
    

| Yes | 
    
    
    EXISTS/NOT EXISTS
    

| 
    
    
    SELECT * FROM DEPARTMENTS D
    WHERE EXISTS (SELECT 1
                  FROM EMPLOYEES E
                  WHERE
                  E.DEPARTMENT_ID =
                  D.DEPARTMENT_ID);
      
      
    
    IN/NOT IN
    

| Yes | 
    
    
    IN/NOT IN
    

| 
    
    
    SELECT * FROM DEPARTMENTS D
    WHERE DEPARTMENT_ID IN
                (SELECT DEPARTMENT_ID
                 FROM EMPLOYEES E);
      
    
    -- OR
      
    
    SELECT * FROM EMPLOYEES
    WHERE (EMPLOYEE_ID, DEPARTMENT_ID)
    IN((100, 90));
      
      
    
    LIKE/NOT LIKE
    

| Yes | 
    
    
    LIKE/NOT LIKE
    

| 
    
    
    SELECT * FROM EMPLOYEES
    WHERE FIRST_NAME LIKE '_e_n%';
      
      
    
    BETWEEN/NOT BETWEEN
    

| Yes | 
    
    
    BETWEEN/NOT BETWEEN
    

| 
    
    
    SELECT * FROM EMPLOYEES
    WHERE EXTRACT(YEAR FROM HIRE_DATE)
    NOT BETWEEN 2001 and 2004;
      
      
    
    AND/OR
    

| Yes | 
    
    
    AND/OR
    

| 
    
    
    SELECT * FROM EMPLOYEES
    WHERE DEPARTMENT_ID IN(100, 101)
    AND (SALARY >= 1000 OR HIRE_DATE <= '2006-02-05');
      
      
    
    SubQuery
    

| Yes | 
    
    
    SubQuery
    

| MySQL supports subqueries in the `SELECT` level, for `JOIN` statements and for filtering in the `WHERE/AND` clauses:  

    
    
    -- SELECT SubQuery
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
          WHERE  LOCATION_ID = 2700) D
    ON E.DEPARTMENT_ID = D.DEPARTMENT_ID;
      
    
    -- Filtering Subquery
    SELECT FIRST_NAME,
           LAST_NAME,
           SALARY
    FROM EMPLOYEES
    WHERE SALARY < (SELECT AVG(SALARY)
                    FROM EMPLOYEES);
      
  
Operators | Yes | Operators | MySQL supports all the basic operators:  

    
    
    > | >= | < | <= | = | <> | !=
      
  
#### Analytical functions (or window and ranking functions)

Oracle analytical functions extend the functionality of standard SQL analytic functions by providing capabilities to compute aggregate values based on a group of rows. These functions can be applied to logically partitioned sets of results within the scope of a single query expression. They are usually used in combination with business intelligence reports and analytics, with the potential to boost query performance as an alternative to achieving the same result using more complex, non-analytical SQL code.

**Conversion notes**

  * MySQL version 5.7 does not provide analytical functions to support a straightforward SQL statements conversion. However, this functionality was added partially in [MySQL version 8](https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html), making converting analytical functions a point to consider, likely requiring manual effort in the migration process.
  * An optional solution is to rewrite code to remove the use of analytical functions, reverting to more traditional SQL code solutions, or moving this logic to an application layer.



The following table lists the Oracle common analytical functions.

Function family | Related functions | Supported by MySQL 5.7  
---|---|---  
Analytical and ranking | 
    
    
    RANK
    AVERAGE_RANK
    DENSE_RANK
    RANK ROW_NUMBER
    PERCENT_RANK
    CUME_DIST
    NTILE
    FIRST_VALUE
    LAST_VALUE
    OVER (PARTITION BY...)
    

| No  
Hierarchical | 
    
    
    CONNECT BY
    HIER_ANCESTOR
    HIER_CHILD_COUNT
    HIER_DEPTH
    HIER_LEVEL
    HIER_ORDER
    HIER_PARENT
    HIER_TOP
    

| No  
Lag | 
    
    
    LAG
    LAG_VARIANCE LAG_VARIANCE_PERCENT LEAD
    LEAD_VARIANCE LEAD_VARIANCE_PERCENT
    

| No  
  
#### Common table expression (CTE)

CTEs provide a way to implement the logic of sequential code to reuse SQL code that might be too complex or not efficient for multiple use. CTEs can be named and then used multiple times in different parts of a SQL statement using the `WITH` clause.

**Conversion notes**

  * MySQL version 5.7 does not support CTEs, but [MySQL version 8](https://dev.mysql.com/doc/refman/8.0/en/with.html) does.
  * For an alternative solution, use derived tables or SubQueries or rewrite the SQL statement to eliminate the CTE functionality.



**Examples**

Oracle  
---  
      
    
    WITH DEPT_COUNT
    (DEPARTMENT_ID, DEPT_COUNT) AS
    (SELECT DEPARTMENT_ID,
            COUNT(*)
     FROM EMPLOYEES
     GROUP BY DEPARTMENT_ID)
      
    
    SELECT E.FIRST_NAME ||' '|| E.LAST_NAME AS EMP_NAME,
           D.DEPT_COUNT AS EMP_DEPT_COUNT
    FROM EMPLOYEES E JOIN DEPT_COUNT D
    USING (DEPARTMENT_ID)
    ORDER BY 2 DESC;
      
  
MySQL  
      
    
    SELECT * FROM (
    SELECT CONCAT(E.FIRST_NAME, ' ', E.LAST_NAME) AS EMP_NAME,
           (SELECT COUNT(*)
            FROM EMPLOYEES D
            WHERE E.DEPARTMENT_ID = D.DEPARTMENT_ID
            GROUP BY DEPARTMENT_ID) AS EMP_DEPT_COUNT
    FROM EMPLOYEES E
    ORDER BY 2 DESC) TBL
    WHERE EMP_DEPT_COUNT IS NOT NULL;
      
  
#### MERGE statement

The `MERGE` (or `UPSERT`) statement provides a means to specify single SQL statements that conditionally perform DML operations in one `MERGE` operation, as opposed to a single DML operation, running separately. It selects records from the source table and then, by specifying a logical structure, automatically performs multiple DML operations on the target table. This feature helps you avoid using multiple inserts, updates, or deletes. Note that `MERGE` is a deterministic statement, meaning that once a row has been processed by the `MERGE` statement, it cannot be processed again using the same `MERGE` statement.

**Conversion notes**

MySQL version 5.7 does not support the `MERGE` functionality, unlike Oracle. To partially simulate the `MERGE` functionality, MySQL provides the [`REPLACE`](https://dev.mysql.com/doc/refman/5.7/en/replace.html) and the [`INSERT… ON DUPLICATE KEY UPDATE`](https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html) statements:

  * `REPLACE`: Works in the same manner as an `INSERT` statement, except that if an old row in the table has the same value as a new row for a `PRIMARY KEY` or a `UNIQUE` index, the old row is deleted before the new row is inserted.

  * `INSERT… ON DUPLICATE KEY UPDATE`: If an inserted row would cause a duplicate value in a `PRIMARY KEY` or `UNIQUE` index, an `UPDATE` of the old row occurs in order to eliminate duplicate key exception, for example:
        
        INSERT INTO tbl (a,b,c) VALUES (1,2,3)
          ON DUPLICATE KEY UPDATE c=c+1;
        
        UPDATE tbl SET c=c+1 WHERE a=1;
        




Another solution would be to convert the `MERGE` functionality into a stored procedure to manage DML operations, using `INSERT`, `UPDATE`, and `DELETE` commands with exceptions and duplications handling.

#### SQL statement hints

Oracle provides a large collection of SQL query hints that let users influence Optimizer behavior and its decision making, aiming to produce more efficient query execution plans. Oracle supports over 60 different database hints. MySQL provides a limited set of query hints.

In general, MySQL version 5.7 supports two types of query hints: `OPTIMIZER HINTS` and `INDEX HINTS`. [MySQL Optimizer Hints](https://dev.mysql.com/doc/refman/5.7/en/optimizer-hints.html) provide the ability to control Optimizer behavior within individual SQL statements—for example:
    
    
    SELECT /*+ NO_RANGE_OPTIMIZATION(tbl PRIMARY, col1_idx) */ col1 FROM tbl;
    

**MySQL** **version 5.7 Available Optimizer Hints**

Hint name  | Hint overview | Applicable scopes  
---|---|---  
      
    
    BKA, NO_BKA
    

| Affects batched key access join processing | Query block, table  
      
    
    BNL, NO_BNL
    

| Affects block nested-loop join processing | Query block, table  
      
    
    MAX_EXECUTION_TIME
    

| Limits statement execution time | Global  
      
    
    MRR, NO_MRR
    

| Affects multi-range read optimization | Table, index  
      
    
    NO_ICP
    

| Affects index condition pushdown optimization | Table, index  
      
    
    NO_RANGE_OPTIMIZATION
    

| Affects range optimization | Table, index  
      
    
    QB_NAME
    

| Assigns name to query block | Query block  
      
    
    SEMIJOIN, NO_SEMIJOIN
    

| Affects semi-join strategies | Query block  
      
    
    SUBQUERY
    

| Affects materialization, `IN`-to-`EXISTS` SubQuery strategies. | Query block  
  
[MySQL Index Hints](https://dev.mysql.com/doc/refman/5.7/en/index-hints.html) provide the Optimizer with information about how to choose indexes during query processing. The `USE`, `FORCE`, or `IGNORE` keywords are used to control the Optimizer index usage process—for example:
    
    
    SELECT * FROM tbl USE INDEX (col1_index, col2_index);
    -- OR
    SELECT * FROM tbl IGNORE INDEX (col1_index, col2_index);
    

**Conversion notes**

Because there are fundamental differences between Oracle and MySQL Optimizer, and because there is limited if any overlap between Oracle and MySQL query hints, we recommend that you convert any Oracle SQL statement holding unspecified query hints over the target MySQL database.

Do MySQL performance tuning through MySQL tools (for example, MySQL [Workbench](https://dev.mysql.com/doc/workbench/en/wb-performance-dashboard.html) for real-time performance dashboards) and features such as examining queries using execution plans and adjusting the instance or session parameters according to the use case.

#### Execution plans

The main purpose of execution plans is to provide an inside look at the choices made by the query optimizer for accessing database data. The query optimizer generates execution plans for `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements for database users, also letting administrators have a better view on specific queries and DML operations. They are especially useful when you need to do performance tuning of queries—for example, to determine index performance or to determine if there are missing indexes that need to be created.

Execution plans can be affected by data volumes, data statistics, and instance parameters (global or session parameters).

**Conversion considerations**

Execution plans are not database objects that need to be migrated; instead, they are a tool to analyze performance differences between Oracle and MySQL running the same statement on identical data sets.

MySQL does not support the same execution plan syntax, functionality, or output as Oracle.

**Examples**

Oracle execution plan  
---  
      
    
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
      
  
MySQL execution plan  
      
    
    mysql> EXPLAIN SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = 105;
      
    
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
    | id | select_type | table     | partitions | type  | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
    |  1 | SIMPLE      | EMPLOYEES | NULL       | const | PRIMARY       | PRIMARY | 3       | const |    1 |   100.00 | NULL  |
    +----+-------------+-----------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
      
  
## Stored procedures, functions, and triggers

PL/SQL is the Oracle extended procedural language used to create, store, and apply code-based solutions within the database. In general, database stored procedures and functions are code elements consisting of ANSI SQL and SQL extended procedural language—for example, PL/SQL for Oracle, PL/pgSQL for PostgreSQL, and MySQL procedural language for MySQL. MySQL uses the same name as the database for its own extended procedural language.

The purpose of these stored procedures and functions is to provide solutions for requirements that are more suitable to run from within the database and not from the application (for example, performance, compatibility, and security). Although both stored procedures and functions use PL/SQL, stored procedures are used primarily to perform DDL/DML operations, and functions are primarily used to perform calculations to return specific results.

### PL/SQL to MySQL procedural language

From the Oracle PL/SQL to MySQL code migration perspective, MySQL procedural implementation is different from Oracle's. Therefore, code migration is required to convert PL/SQL functionality from Oracle into MySQL stored procedures and functions. In addition, Oracle Package and Package Body are not supported by MySQL, so when you are doing code conversion, convert these elements (or parse them) into single units of MySQL code. Note that MySQL stored procedures and functions are also referred to as _routines_.

### Code object owner

In Oracle, the owner of a stored procedure or function is a specific user. In MySQL, the owner is a specific schema (created in a database by a database user).

### Code object privileges and security

In Oracle, in order to create a stored procedure or function, the user must have the `CREATE PROCEDURE` system privilege (to create procedures or functions under other different users, the database users must have the `CREATE ANY PROCEDURE` privilege). To execute a stored procedure or a function, the database users must have the `EXECUTE` privilege.

In MySQL, in order to create a code element, the user must have the `CREATE ROUTINE` privilege and the `EXECUTE` privilege to run. The MySQL `DEFINER` clause defines the user creator for the code object, and the user must have the appropriate privileges such as `CREATE ROUTINE`.

### MySQL stored procedure and function syntax

The following example shows the MySQL stored procedure and function [syntax](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html):
    
    
    CREATE
        [DEFINER = user]
        PROCEDURE sp_name ([proc_parameter[,...]])
        [characteristic ...] routine_body
    
    CREATE
        [DEFINER = user]
        FUNCTION sp_name ([func_parameter[,...]])
        RETURNS type
        [characteristic ...] routine_body
    
    proc_parameter:
        [ IN | OUT | INOUT ] param_name type
    
    func_parameter:
        param_name type
    
    type:
        Any valid MySQL data type
    
    characteristic:
        COMMENT 'string'
      | LANGUAGE SQL
      | [NOT] DETERMINISTIC
      | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
      | SQL SECURITY { DEFINER | INVOKER }
    
    routine_body:
        Valid SQL routine statement
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
