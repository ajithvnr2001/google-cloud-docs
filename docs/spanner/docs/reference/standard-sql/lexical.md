---
url: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/lexical/
title: Lexical structure and syntax in GoogleSQL \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:22.683210+00:00
---

# Lexical structure and syntax in GoogleSQL  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/standard-sql/lexical/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Lexical structure and syntax in GoogleSQL Stay organized with collections  Save and categorize content based on your preferences. 

A GoogleSQL statement comprises a series of tokens. Tokens include identifiers, quoted identifiers, literals, keywords, operators, and special characters. You can separate tokens with comments or whitespace such as spaces, backspaces, tabs, or newlines.

## Identifiers

Identifiers are names that are associated with columns, tables, fields, path expressions, and more. They can be unquoted or quoted and some are case-sensitive.

### Unquoted identifiers

  * Must begin with a letter or an underscore (_) character.
  * Subsequent characters can be letters, numbers, or underscores (_).



### Quoted identifiers

  * Must be enclosed by backtick (`) characters.
  * Can contain any characters, including spaces and symbols.
  * Can't be empty.
  * Have the same escape sequences as string literals.
  * If an identifier is the same as a reserved keyword, the identifier must be quoted. For example, the identifier `FROM` must be quoted. Additional rules apply for path expressions and field names.



### Identifier examples

Path expression examples:
    
    
    -- Valid. _5abc and dataField are valid identifiers.
    _5abc.dataField
    
    -- Valid. `5abc` and dataField are valid identifiers.
    `5abc`.dataField
    
    -- Invalid. 5abc is an invalid identifier because it's unquoted and starts
    -- with a number rather than a letter or underscore.
    5abc.dataField
    
    -- Valid. abc5 and dataField are valid identifiers.
    abc5.dataField
    
    -- Invalid. abc5! is an invalid identifier because it's unquoted and contains
    -- a character that isn't a letter, number, or underscore.
    abc5!.dataField
    
    -- Valid. `GROUP` and dataField are valid identifiers.
    `GROUP`.dataField
    
    -- Invalid. GROUP is an invalid identifier because it's unquoted and is a
    -- stand-alone reserved keyword.
    GROUP.dataField
    
    -- Valid. abc5 and GROUP are valid identifiers.
    abc5.GROUP
    

Function examples:
    
    
    -- Valid. dataField is a valid identifier in a function called foo().
    foo().dataField
    

Array access operation examples:
    
    
    -- Valid. dataField is a valid identifier in an array called items.
    items[OFFSET(3)].dataField
    

Named query parameter examples:
    
    
    -- Valid. param and dataField are valid identifiers.
    @param.dataField
    

Protocol buffer examples:
    
    
    -- Valid. dataField is a valid identifier in a protocol buffer called foo.
    (foo).dataField
    

## Path expressions

A path expression describes how to navigate to an object in a graph of objects and generally follows this structure:
    
    
    path:
      [path_expression][. ...]
    
    path_expression:
      [first_part]/subsequent_part[ { / | : | - } subsequent_part ][...]
    
    first_part:
      { unquoted_identifier | quoted_identifier }
    
    subsequent_part:
      { unquoted_identifier | quoted_identifier | number }
    

  * `path`: A graph of one or more objects.
  * `path_expression`: An object in a graph of objects.
  * `first_part`: A path expression can start with a quoted or unquoted identifier. If the path expressions starts with a reserved keyword, it must be a quoted identifier.
  * `subsequent_part`: Subsequent parts of a path expression can include non-identifiers, such as reserved keywords. If a subsequent part of a path expressions starts with a reserved keyword, it may be quoted or unquoted.



Examples:
    
    
    foo.bar
    foo.bar/25
    foo/bar:25
    foo/bar/25-31
    /foo/bar
    /25/foo/bar
    

## Field names

A field name represents the name of a field inside a complex data type such as a struct, protocol buffer message, or JSON object.

  * A field name can be a quoted identifier or an unquoted identifier.



## Literals

A literal represents a constant value of a built-in data type. Some, but not all, data types can be expressed as literals.

### String and bytes literals

A string literal represents a constant value of the [string data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#string_type). A bytes literal represents a constant value of the [bytes data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#bytes_type).

Both string and bytes literals must be _quoted_ , either with single (`'`) or double (`"`) quotation marks, or _triple-quoted_ with groups of three single (`'''`) or three double (`"""`) quotation marks.

#### Formats for quoted literals

The following table lists all of the ways you can format a quoted literal.

Literal | Examples | Description  
---|---|---  
Quoted string | 

  * `"abc"`
  * `"it's"`
  * `'it\'s'`
  * `'Title: "Boy"'`

| Quoted strings enclosed by single (`'`) quotes can contain unescaped double (`"`) quotes, as well as the inverse.   
Backslashes (`\`) introduce escape sequences. See the Escape Sequences table below.  
Quoted strings can't contain newlines, even when preceded by a backslash (`\`).  
Triple-quoted string | 

  * `"""abc"""`
  * `'''it's'''`
  * `'''Title:"Boy"'''`
  * `'''two  
lines'''`
  * `'''why\?'''`

| Embedded newlines and quotes are allowed without escaping - see fourth example.  
Backslashes (`\`) introduce escape sequences. See Escape Sequences table below.  
A trailing unescaped backslash (`\`) at the end of a line isn't allowed.  
End the string with three unescaped quotes in a row that match the starting quotes.  
Raw string | 

  * `r"abc+"`
  * `r'''abc+'''`
  * `r"""abc+"""`
  * `r'f\(abc,(.*),def\)'`

| Quoted or triple-quoted literals that have the raw string literal prefix (`r` or `R`) are interpreted as raw strings (sometimes described as regex strings).  
Backslash characters (`\`) don't act as escape characters. If a backslash followed by another character occurs inside the string literal, both characters are preserved.  
A raw string can't end with an odd number of backslashes.  
Raw strings are useful for constructing regular expressions. The prefix is case-insensitive.   
Bytes | 

  * `B"abc"`
  * `B'''abc'''`
  * `b"""abc"""`

| Quoted or triple-quoted literals that have the bytes literal prefix (`b` or `B`) are interpreted as bytes.  
Raw bytes | 

  * `br'abc+'`
  * `RB"abc+"`
  * `RB'''abc'''`

| A bytes literal can be interpreted as raw bytes if both the `r` and `b` prefixes are present. These prefixes can be combined in any order and are case-insensitive. For example, `rb'abc*'` and `rB'abc*'` and `br'abc*'` are all equivalent. See the description for raw string to learn more about what you can do with a raw literal.   
  
#### Escape sequences for string and bytes literals

The following table lists all valid escape sequences for representing non-alphanumeric characters in string and bytes literals. Any sequence not in this table produces an error.

Escape Sequence | Description  
---|---  
`\a` | Bell  
`\b` | Backspace  
`\f` | Formfeed  
`\n` | Newline  
`\r` | Carriage Return  
`\t` | Tab  
`\v` | Vertical Tab  
`\\` | Backslash (`\`)  
`\?` | Question Mark (`?`)  
`\"` | Double Quote (`"`)  
`\'` | Single Quote (`'`)  
`\`` | Backtick (```)  
`\ooo` | Octal escape, with exactly 3 digits (in the range 0–7). Decodes to a single Unicode character (in string literals) or byte (in bytes literals).  
`\xhh` or `\Xhh` | Hex escape, with exactly 2 hex digits (0–9 or A–F or a–f). Decodes to a single Unicode character (in string literals) or byte (in bytes literals). Examples:

  * `'\x41'` == `'A'`
  * `'\x41B'` is `'AB'`
  * `'\x4'` is an error

  
`\uhhhh` | Unicode escape, with lowercase 'u' and exactly 4 hex digits. Valid only in string literals or identifiers.  
Note that the range D800-DFFF isn't allowed, as these are surrogate unicode values.  
`\Uhhhhhhhh` | Unicode escape, with uppercase 'U' and exactly 8 hex digits. Valid only in string literals or identifiers.  
The range D800-DFFF isn't allowed, as these values are surrogate unicode values. Also, values greater than 10FFFF aren't allowed.  
  
### Integer literals

Integer literals are either a sequence of decimal digits (0–9) or a hexadecimal value that's prefixed with "`0x`" or "`0X`". Integers can be prefixed by "`+`" or "`-`" to represent positive and negative values, respectively. Examples:
    
    
    123
    0xABC
    -123
    

An integer literal is interpreted as an `INT64`.

A integer literal represents a constant value of the [integer data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#integer_types).

### `NUMERIC` literals

You can construct `NUMERIC` literals using the `NUMERIC` keyword followed by a floating point value in quotes.

Examples:
    
    
    SELECT NUMERIC '0';
    SELECT NUMERIC '123456';
    SELECT NUMERIC '-3.14';
    SELECT NUMERIC '-0.54321';
    SELECT NUMERIC '1.23456e05';
    SELECT NUMERIC '-9.876e-3';
    

A `NUMERIC` literal represents a constant value of the [`NUMERIC` data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#decimal_types).

### Floating point literals

Syntax options:
    
    
    [+-]DIGITS.[DIGITS][e[+-]DIGITS]
    [+-][DIGITS].DIGITS[e[+-]DIGITS]
    DIGITSe[+-]DIGITS
    

`DIGITS` represents one or more decimal numbers (0 through 9) and `e` represents the exponent marker (e or E).

Examples:
    
    
    123.456e-67
    .1E4
    58.
    4e2
    

Numeric literals that contain either a decimal point or an exponent marker are presumed to be type double.

Implicit coercion of floating point literals to float type is possible if the value is within the valid float range.

There is no literal representation of NaN or infinity, but the following case-insensitive strings can be explicitly cast to float:

  * "NaN"
  * "inf" or "+inf"
  * "-inf"



A floating-point literal represents a constant value of the [floating-point data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#floating_point_types).

### Array literals

Array literals are comma-separated lists of elements enclosed in square brackets. The `ARRAY` keyword is optional, and an explicit element type T is also optional.

Examples:
    
    
    [1, 2, 3]
    ['x', 'y', 'xy']
    ARRAY[1, 2, 3]
    ARRAY<STRING>['x', 'y', 'xy']
    ARRAY<INT64>[]
    
    

An array literal represents a constant value of the [array data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#array_type).

### Struct literals

A struct literal is a struct whose fields are all literals. Struct literals can be written using any of the syntaxes for [constructing a struct](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#constructing_a_struct) (tuple syntax, typeless struct syntax, or typed struct syntax).

Note that tuple syntax requires at least two fields, in order to distinguish it from an ordinary parenthesized expression. To write a struct literal with a single field, use typeless struct syntax or typed struct syntax.

Example | Output Type  
---|---  
`(1, 2, 3)` | `STRUCT<INT64, INT64, INT64>`  
`(1, 'abc')` | `STRUCT<INT64, STRING>`  
`STRUCT(1 AS foo, 'abc' AS bar)` | `STRUCT<foo INT64, bar STRING>`  
`STRUCT<INT64, STRING>(1, 'abc')` | `STRUCT<INT64, STRING>`  
`STRUCT(1)` | `STRUCT<INT64>`  
`STRUCT<INT64>(1)` | `STRUCT<INT64>`  
  
A struct literal represents a constant value of the [struct data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#struct_type).

### Date literals

Syntax:
    
    
    DATE 'date_canonical_format'
    

Date literals contain the `DATE` keyword followed by [`date_canonical_format`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#canonical_format_for_date_literals), a string literal that conforms to the canonical date format, enclosed in single quotation marks. Date literals support a range between the years 1 and 9999, inclusive. Dates outside of this range are invalid.

For example, the following date literal represents September 27, 2014:
    
    
    DATE '2014-09-27'
    

String literals in canonical date format also implicitly coerce to DATE type when used where a DATE-type expression is expected. For example, in the query
    
    
    SELECT * FROM foo WHERE date_col = "2014-09-27"
    

the string literal `"2014-09-27"` will be coerced to a date literal.

A date literal represents a constant value of the [date data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#date_type).

### Timestamp literals

Syntax:
    
    
    TIMESTAMP 'timestamp_canonical_format'
    

Timestamp literals contain the `TIMESTAMP` keyword and [`timestamp_canonical_format`](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#canonical_format_for_timestamp_literals), a string literal that conforms to the canonical timestamp format, enclosed in single quotation marks.

Timestamp literals support a range between the years 1 and 9999, inclusive. Timestamps outside of this range are invalid.

A timestamp literal can include a numerical suffix to indicate the time zone:
    
    
    TIMESTAMP '2014-09-27 12:30:00.45-08'
    

If this suffix is absent, the default time zone, America/Los_Angeles, is used.

For example, the following timestamp represents 12:30 p.m. on September 27, 2014 in the default time zone, America/Los_Angeles:
    
    
    TIMESTAMP '2014-09-27 12:30:00.45'
    

For more information about time zones, see Time zone.

String literals with the canonical timestamp format, including those with time zone names, implicitly coerce to a timestamp literal when used where a timestamp expression is expected. For example, in the following query, the string literal `"2014-09-27 12:30:00.45 America/Los_Angeles"` is coerced to a timestamp literal.
    
    
    SELECT * FROM foo
    WHERE timestamp_col = "2014-09-27 12:30:00.45 America/Los_Angeles"
    

A timestamp literal can include these optional characters:

  * `T` or `t`
  * `Z` or `z`



If you use one of these characters, a space can't be included before or after it. These are valid:
    
    
    TIMESTAMP '2017-01-18T12:34:56.123456Z'
    TIMESTAMP '2017-01-18t12:34:56.123456'
    TIMESTAMP '2017-01-18 12:34:56.123456z'
    TIMESTAMP '2017-01-18 12:34:56.123456Z'
    

A timestamp literal represents a constant value of the [timestamp data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#timestamp_type).

#### Time zone

Since timestamp literals must be mapped to a specific point in time, a time zone is necessary to correctly interpret a literal. If a time zone isn't specified as part of the literal itself, then GoogleSQL uses the default time zone value, which the GoogleSQL implementation sets.

GoogleSQL can represent a time zones using a string, which represents the [offset from Coordinated Universal Time (UTC)](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#utc_offset).

Examples:
    
    
    '-08:00'
    '-8:15'
    '+3:00'
    '+07:30'
    '-7'
    

Time zones can also be expressed using string [time zone names](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#time_zone_name).

Examples:
    
    
    TIMESTAMP '2014-09-27 12:30:00 America/Los_Angeles'
    TIMESTAMP '2014-09-27 12:30:00 America/Argentina/Buenos_Aires'
    

### Interval literals

An interval literal represents a constant value of the [interval data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#interval_type). There are two types of interval literals:

  * Interval literal with a single datetime part
  * Interval literal with a datetime part range



An interval literal can be used directly inside of the `SELECT` statement and as an argument in some functions that support the interval data type.

#### Interval literal with a single datetime part

Syntax:
    
    
    INTERVAL step_size step_unit
    

The single datetime part syntax includes an `INT64` expression and a single [interval-supported datetime part](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#interval_datetime_parts). For example:
    
    
    -- 0 years, 0 months, 5 days, 0 hours, 0 minutes, 0 seconds (0-0 5 0:0:0)
    INTERVAL 5 DAY
    
    -- 0 years, 0 months, -5 days, 0 hours, 0 minutes, 0 seconds (0-0 -5 0:0:0)
    INTERVAL -5 DAY
    
    -- 0 years, 0 months, 0 days, 0 hours, 0 minutes, 1 seconds (0-0 0 0:0:1)
    INTERVAL 1 SECOND
    

When a negative sign precedes the year or month part in an interval literal, the negative sign distributes over the years and months. Or, when a negative sign precedes the time part in an interval literal, the negative sign distributes over the hours, minutes, and seconds. For example:
    
    
    -- -2 years, -1 months, 0 days, 0 hours, 0 minutes, and 0 seconds (-2-1 0 0:0:0)
    INTERVAL -25 MONTH
    
    -- 0 years, 0 months, 0 days, -1 hours, -30 minutes, and 0 seconds (0-0 0 -1:30:0)
    INTERVAL -90 MINUTE
    

For more information on how to construct interval with a single datetime part, see [Construct an interval with a single datetime part](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#single_datetime_part_interval).

#### Interval literal with a datetime part range

Syntax:
    
    
    INTERVAL datetime_parts_string starting_datetime_part TO ending_datetime_part
    

The range datetime part syntax includes a [datetime parts string](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#range_datetime_part_interval), a [starting datetime part](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#interval_datetime_parts), and an [ending datetime part](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#interval_datetime_parts).

For example:
    
    
    -- 0 years, 0 months, 0 days, 10 hours, 20 minutes, 30 seconds (0-0 0 10:20:30.520)
    INTERVAL '10:20:30.52' HOUR TO SECOND
    
    -- 1 year, 2 months, 0 days, 0 hours, 0 minutes, 0 seconds (1-2 0 0:0:0)
    INTERVAL '1-2' YEAR TO MONTH
    
    -- 0 years, 1 month, -15 days, 0 hours, 0 minutes, 0 seconds (0-1 -15 0:0:0)
    INTERVAL '1 -15' MONTH TO DAY
    
    -- 0 years, 0 months, 1 day, 5 hours, 30 minutes, 0 seconds (0-0 1 5:30:0)
    INTERVAL '1 5:30' DAY TO MINUTE
    

When a negative sign precedes the year or month part in an interval literal, the negative sign distributes over the years and months. Or, when a negative sign precedes the time part in an interval literal, the negative sign distributes over the hours, minutes, and seconds. For example:
    
    
    -- -23 years, -2 months, 10 days, -12 hours, -30 minutes, and 0 seconds (-23-2 10 -12:30:0)
    INTERVAL '-23-2 10 -12:30' YEAR TO MINUTE
    
    -- -23 years, -2 months, 10 days, 0 hours, -30 minutes, and 0 seconds (-23-2 10 -0:30:0)
    SELECT INTERVAL '-23-2 10 -0:30' YEAR TO MINUTE
    
    -- Produces an error because the negative sign for minutes must come before the hour.
    SELECT INTERVAL '-23-2 10 0:-30' YEAR TO MINUTE
    
    -- Produces an error because the negative sign for months must come before the year.
    SELECT INTERVAL '23--2 10 0:30' YEAR TO MINUTE
    
    -- 0 years, -2 months, 10 days, 0 hours, 30 minutes, and 0 seconds (-0-2 10 0:30:0)
    SELECT INTERVAL '-2 10 0:30' MONTH TO MINUTE
    
    -- 0 years, 0 months, 0 days, 0 hours, -30 minutes, and -10 seconds (0-0 0 -0:30:10)
    SELECT INTERVAL '-30:10' MINUTE TO SECOND
    

For more information on how to construct interval with a datetime part range, see [Construct an interval with a datetime part range](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#single_datetime_part_interval).

### Enum literals

There is no syntax for enum literals. Integer or string literals are coerced to the enum type when necessary, or explicitly cast to a specific enum type name. For more information, see [Literal coercion](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/conversion_rules#coercion).

An enum literal represents a constant value of the [enum data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#enum_type).

### JSON literals

Syntax:
    
    
    JSON 'json_formatted_data'
    

A JSON literal represents [JSON](https://en.wikipedia.org/wiki/JSON)-formatted data.

Example:
    
    
    JSON '
    {
      "id": 10,
      "type": "fruit",
      "name": "apple",
      "on_menu": true,
      "recipes":
        {
          "salads":
          [
            { "id": 2001, "type": "Walnut Apple Salad" },
            { "id": 2002, "type": "Apple Spinach Salad" }
          ],
          "desserts":
          [
            { "id": 3001, "type": "Apple Pie" },
            { "id": 3002, "type": "Apple Scones" },
            { "id": 3003, "type": "Apple Crumble" }
          ]
        }
    }
    '
    

A JSON literal represents a constant value of the [JSON data type](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-types#json_type).

## Case sensitivity

GoogleSQL follows these rules for case sensitivity:

Category | Case-sensitive? | Notes  
---|---|---  
Keywords | No |   
Function names | No |   
Table names | See Notes |  Table names are usually case-insensitive, but they might be case-sensitive when querying a database that uses case-sensitive table names.   
Column names | No |   
Field names | No |   
Constant variables | No |   
All type names except for protocol buffer type names | No |   
Protocol buffer type names | Yes |   
Enum type names | Yes |   
String values | Yes |  Any value of type `STRING` preserves its case. For example, the result of an expression that produces a `STRING` value or a column value that's of type `STRING`.   
String comparisons | Yes |  However, string comparisons are case-insensitive in [collations](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/collation-concepts) that are case-insensitive. This behavior also applies to operations affected by collation, such as `GROUP BY` and `DISTINCT` clauses.   
Aliases within a query | No |   
Regular expression matching | See Notes |  Regular expression matching is case-sensitive by default, unless the expression itself specifies that it should be case-insensitive.   
`LIKE` matching | Yes |   
Property graph names | No |   
Property graph label names | No |   
Property graph property names | No |   
  
## Reserved keywords

Keywords are a group of tokens that have special meaning in the GoogleSQL language, and have the following characteristics:

  * Keywords can't be used as identifiers unless enclosed by backtick (`) characters.
  * Keywords are case-insensitive.



GoogleSQL has the following reserved keywords.

ALL  
AND  
ANY  
ARRAY  
AS  
ASC  
ASSERT_ROWS_MODIFIED  
AT  
BETWEEN  
BY  
CASE  
CAST  
COLLATE  
CONTAINS  
CREATE  
CROSS  
CUBE  
CURRENT  
DEFAULT  
DEFINE  
DESC  
DISTINCT  
ELSE  
END  
|  ENUM  
ESCAPE  
EXCEPT  
EXCLUDE  
EXISTS  
EXTRACT  
FALSE  
FETCH  
FOLLOWING  
FOR  
FROM  
FULL  
GRAPH_TABLE  
GROUP  
GROUPING  
GROUPS  
HASH  
HAVING  
IF  
IGNORE  
IN  
INNER  
INTERSECT  
INTERVAL  
INTO  
|  IS  
JOIN  
LATERAL  
LEFT  
LIKE  
LIMIT  
LOOKUP  
MERGE  
NATURAL  
NEW  
NO  
NOT  
NULL  
NULLS  
OF  
ON  
OR  
ORDER  
OUTER  
OVER  
PARTITION  
PRECEDING  
PROTO  
RANGE  
|  RECURSIVE  
RESPECT  
RIGHT  
ROLLUP  
ROWS  
SELECT  
SET  
SOME  
STRUCT  
TABLESAMPLE  
THEN  
TO  
TREAT  
TRUE  
UNBOUNDED  
UNION  
UNNEST  
USING  
WHEN  
WHERE  
WINDOW  
WITH  
WITHIN  
  
---|---|---|---  
  
## Terminating semicolons

You can optionally use a terminating semicolon (`;`) when you submit a query string statement through an Application Programming Interface (API).

In a request containing multiple statements, you must separate statements with semicolons, but the semicolon is generally optional after the final statement. Some interactive tools require statements to have a terminating semicolon.

## Trailing commas

You can optionally use a trailing comma (`,`) at the end of a column list in a `SELECT` statement. You might have a trailing comma as the result of programmatically creating a column list.

**Example**
    
    
    SELECT name, release_date, FROM Books
    

## Query parameters

You can use query parameters to substitute arbitrary expressions. However, query parameters can't be used to substitute identifiers, column names, table names, or other parts of the query itself. Query parameters are defined outside of the query statement.

Client APIs allow the binding of parameter names to values; the query engine substitutes a bound value for a parameter at execution time.

Parameterized queries have better [query cache](https://docs.cloud.google.com/spanner/docs/whitepapers/life-of-query#caching) hit rates resulting in lower query latency and lower overall CPU usage.

For example, instead of using a query like the following:
    
    
    SELECT AlbumId FROM Albums WHERE SEARCH(AlbumTitle_Tokens, 'cat')
    

use the following syntax:
    
    
    SELECT AlbumId FROM Albums WHERE SEARCH(AlbumTitle_Tokens, @p)
    

Spanner runs the query optimizer on distinct SQL. The fewer distinct SQL instances the application uses, the fewer times the query optimization is invoked.

### Named query parameters

Syntax:
    
    
    @parameter_name
    

A named query parameter is denoted using an identifier preceded by the `@` character.

A named query parameter can start with an identifier or a reserved keyword. An identifier can be unquoted or quoted.

**Example:**

This example returns all rows where `LastName` is equal to the value of the named query parameter `myparam`.
    
    
    SELECT * FROM Roster WHERE LastName = @myparam
    

## Hints
    
    
    @{ hint [, ...] }
    
    hint:
      [engine_name.]hint_name = value
    

The purpose of a hint is to modify the execution strategy for a query without changing the result of the query. Hints generally don't affect query semantics, but may have performance implications. These hint types are available:

  * [GROUP hints](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax#group_hints)
  * [JOIN hints](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax#join_hints)
  * [STATEMENT hints](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax#statement_hints)
  * [TABLE hints](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax#table_hints)



Hint syntax requires the `@` character followed by curly braces. You can create one hint or a group of hints. The optional `engine_name.` prefix allows for multiple engines to define hints with the same `hint_name`. This is important if you need to suggest different engine-specific execution strategies or different engines support different hints.

You can assign identifiers and literals to hints.

  * Identifiers are useful for hints that are meant to act like enums. You can use an identifier to avoid using a quoted string. In the resolved AST, identifier hints are represented as string literals, so `@{hint="abc"}` is the same as `@{hint=abc}`. Identifier hints can also be used for hints that take a table name or column name as a single identifier.
  * NULL literals are allowed and are inferred as integers.



Hints are meant to apply only to the node they are attached to, and not to a larger scope. For example, a hint on a `JOIN` in the middle of the `FROM` clause is meant to apply to that `JOIN` only, and not other `JOIN`s in the `FROM` clause. Statement-level hints can be used for hints that modify execution of an entire statement, for example an overall memory budget or deadline.

**Examples**

In this example, a literal is assigned to a hint. This hint is only used with two database engines called `database_engine_a` and `database_engine_b`. The value for the hint is different for each database engine.
    
    
    @{ database_engine_a.file_count=23, database_engine_b.file_count=10 }
    

In this example, an identifier is assigned to a hint. There are unique identifiers for each hint type. You can view a list of hint types at the beginning of this topic.
    
    
    @{ JOIN_METHOD=HASH_JOIN }
    

## Comments

Comments are sequences of characters that the parser ignores. GoogleSQL supports the following types of comments.

### Single-line comments

Use a single-line comment if you want the comment to appear on a line by itself.

**Examples**
    
    
    # this is a single-line comment
    SELECT book FROM library;
    
    
    
    -- this is a single-line comment
    SELECT book FROM library;
    
    
    
    /* this is a single-line comment */
    SELECT book FROM library;
    
    
    
    SELECT book FROM library
    /* this is a single-line comment */
    WHERE book = "Ulysses";
    

### Inline comments

Use an inline comment if you want the comment to appear on the same line as a statement. A comment that's prepended with `#` or `--` must appear to the right of a statement.

**Examples**
    
    
    SELECT book FROM library; # this is an inline comment
    
    
    
    SELECT book FROM library; -- this is an inline comment
    
    
    
    SELECT book FROM library; /* this is an inline comment */
    
    
    
    SELECT book FROM library /* this is an inline comment */ WHERE book = "Ulysses";
    

### Multiline comments

Use a multiline comment if you need the comment to span multiple lines. Nested multiline comments aren't supported.

**Examples**
    
    
    SELECT book FROM library
    /*
      This is a multiline comment
      on multiple lines
    */
    WHERE book = "Ulysses";
    
    
    
    SELECT book FROM library
    /* this is a multiline comment
    on two lines */
    WHERE book = "Ulysses";
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
