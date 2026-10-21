---
url: https://docs.cloud.google.com/data-studio/function-list/
title: Function list \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:18.409789+00:00
---

# Function list  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/function-list/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Function list Stay organized with collections  Save and categorize content based on your preferences. 

Data Studio provides a number of powerful functions that can be used inside of calculated field formulas.

**Note:** For a list of the functions that the Looker connector supports for calculated fields, see the [Overview of Looker connector requirements, limits, and feature support](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector) documentation page.**Tip:** More information on each function, including examples, is available in the formula editor. This help will appear as you begin to type your formula.

Narrow by type ...AggregationArithmeticConditionalDateGeoMiscellaneousText

Name | Type | Description | Syntax  
---|---|---|---  
`ABS` | Arithmetic | Returns the absolute value of number. [Learn more.](https://docs.cloud.google.com/data-studio/abs) | `ABS(X)`  
`ACOS` | Arithmetic | Returns the inverse of the cosine of X. [Learn more.](https://docs.cloud.google.com/data-studio/acos) | `ACOS(X)`  
`APPROX_COUNT_DISTINCT` | Aggregation | Returns the approximate number of unique values of X. [Learn more](https://docs.cloud.google.com/data-studio/approxcountdistinct) | `APPROX_COUNT_DISTINCT(X)`  
`ASIN` | Arithmetic | Returns the inverse of the sine of X. [Learn more.](https://docs.cloud.google.com/data-studio/asin) | `ASIN(X)`  
`ATAN` | Arithmetic | Returns the inverse of the tangent of X. [Learn more.](https://docs.cloud.google.com/data-studio/atan) | `ATAN(X)`  
`AVG` | Aggregation | Returns the average of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/avg) | `AVG(X)`  
`CASE (Simple)` | Conditional | Compares `input_expression` to `expression_to_match` of each successive WHEN clause and returns the first `result` where this comparison returns true. [Learn more](https://docs.cloud.google.com/data-studio/case-simple) | 
    
    
    
    CASE input_expression
        WHEN expression_to_match THEN result
        [WHEN expression_to_match THEN result]
        [...]
        [ELSE result]
    END  
  
`CASE` | Conditional | Evaluates the `condition` of each successive WHEN clause and returns the first `result` where the `condition` is true; any remaining WHEN and ELSE clauses are not evaluated. If all conditions are false or NULL, returns `else_result` if present; if not present, returns NULL. [Learn more](https://docs.cloud.google.com/data-studio/case-searched) | 
    
    
    
    CASE
        WHEN condition THEN result
        [WHEN condition THEN result]
        [...]
        [ELSE else_result]
    END  
  
`CAST` | Miscellaneous | Cast field or expression into TYPE. Aggregated fields are not allowed inside CAST.`TYPE` can be `NUMBER`, `TEXT`, or `DATETIME`. [Learn more.](https://docs.cloud.google.com/data-studio/cast) | `CAST(_field_expression_ AS _TYPE_)`  
`CEIL` | Arithmetic | Returns the nearest integer greater than X. For example, if the value of X is v, CEIL(X) is greater than or equal to v. [Learn more.](https://docs.cloud.google.com/data-studio/ceil) | `CEIL(X)`  
`COALESCE` | Conditional | Returns the first non-missing value found in a list of fields. [Learn more.](https://docs.cloud.google.com/data-studio/coalesce) | `COALESCE(field_expression[,field_expression, ...])`  
`CONCAT` | Text | Returns a text that is the concatenation of _X_ and _Y_. [Learn more.](https://docs.cloud.google.com/data-studio/concat) | `CONCAT(X, Y)`  
`CONTAINS_TEXT` | Text | Returns true if _X_ contains text, otherwise returns false. Case-sensitive. [Learn more.](https://docs.cloud.google.com/data-studio/containstext) | `CONTAINS_TEXT(X, text)`  
`COS` | Arithmetic | Returns the cosine of X. [Learn more.](https://docs.cloud.google.com/data-studio/cos) | `COS(X)`  
`COUNT` | Aggregation | Returns the number of values of X. [Learn more.](https://docs.cloud.google.com/data-studio/count) | `COUNT(X)`  
`COUNT_DISTINCT` | Aggregation | Returns the number of unique values of X. [Learn more.](https://docs.cloud.google.com/data-studio/countdistinct) | `COUNT_DISTINCT(X)`  
`CURRENT_DATE` | Date | Returns the current date as of the specified or default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/currentdate) | `CURRENT_DATE([time_zone])`  
`CURRENT_DATETIME` | Date | Returns the current date and time as of the specified or default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/currentdatetime) | `CURRENT_DATETIME([time_zone])`  
`DATE` | Date | Constructs a Date field or value from numbers or from a Date & Time field or expression. [Learn more.](https://docs.cloud.google.com/data-studio/date) | `DATE(year, month, day)`  
`DATE_DIFF` | Date | Returns the difference in days between X and Y (X - Y). [Learn more.](https://docs.cloud.google.com/data-studio/datediff) | `DATE_DIFF(X, Y)`  
`DATE_FROM_UNIX_DATE` | Date | Interprets an integer as the number of days since 1970-01-01. [Learn more.](https://docs.cloud.google.com/data-studio/datefromunixdate) | `DATE_FROM_UNIX_DATE(integer)`  
`DATETIME` | Date | Constructs a Date & Time field or value from numbers. [Learn more.](https://docs.cloud.google.com/data-studio/datetime) | `DATETIME(year, month, day, hour, minute, second)`  
`DATETIME_ADD` | Date | Adds a specified time interval to a date. [Learn more.](https://docs.cloud.google.com/data-studio/datetimeadd) | `DATETIME_ADD(datetime_expression, INTERVAL integer part)`  
`DATETIME_DIFF` | Date | Returns the number of part boundaries between two dates. [Learn more.](https://docs.cloud.google.com/data-studio/datetimediff) | `DATETIME_DIFF(date_expression, date_expression, part)`  
`DATETIME_SUB` | Date | Subtracts a specified time interval from a date. [Learn more.](https://docs.cloud.google.com/data-studio/datetimesub) | `DATETIME_SUB(datetime_expression, INTERVAL integer part) `  
`DATETIME_TRUNC` | Date | Truncates a date to the specified granularity. [Learn more.](https://docs.cloud.google.com/data-studio/datetimetrunc) | `DATETIME_TRUNC(date_expression, part)`  
`DAY` | Date | Returns the day of a Date or Date & Time. [Learn more.](https://docs.cloud.google.com/data-studio/day) | `Day(date_expression)`  
`ENDS_WITH ` | Text | Returns true if _X_ ends with text, otherwise returns false. Case-sensitive. [Learn more.](https://docs.cloud.google.com/data-studio/endswith) | `ENDS_WITH(X, text)`  
`EXTRACT` | Date | Returns part of a Date or Date & Time. [Learn more.](https://docs.cloud.google.com/data-studio/extract) | `EXTRACT(part FROM date_expression)`  
`FLOOR` | Arithmetic | Returns the nearest integer less than X. For example, if the value X is v, FLOOR(X) is equal to or less than v. [Learn more.](https://docs.cloud.google.com/data-studio/floor) | `FLOOR(X)`  
`FORMAT_DATETIME` | Date | Returns a formatted date string. [Learn more.](https://docs.cloud.google.com/data-studio/formatdatetime) | `FORMAT_DATETIME(format_string, datetime_expression)`  
`HOUR` | Date | Returns the hour of a date and time. [Learn more.](https://docs.cloud.google.com/data-studio/hour) | `HOUR(datetime_expression)`  
`HYPERLINK` | Miscellaneous | Returns a hyperlink to the URL, labeled with the link label. [Learn more](https://docs.cloud.google.com/data-studio/hyperlink). | `HYPERLINK(URL, link label)`  
`IF` | Conditional | If `condition` is true, returns `true_result`, else returns `false_result`. `false_result` is not evaluated if `condition` is true. `true_result` is not evaluated if `condition` is false or NULL. [Learn more](https://docs.cloud.google.com/data-studio/if) | `IF(condition, true_result, false_result)`  
`IFNULL` | Conditional | Returns a result if the input is null, otherwise, returns the input. [Learn more.](https://docs.cloud.google.com/data-studio/ifnull) | `IFNULL(input_expression, null_result)`  
`IMAGE` | Miscellaneous | Creates Image fields in your data source [Learn more](https://docs.cloud.google.com/data-studio/image). | `IMAGE(Image URL, [Alternative Text])`  
`LEFT_TEXT ` | Text | Returns a number of characters from the beginning of _X_. The number of characters is specified by _length_. [Learn more.](https://docs.cloud.google.com/data-studio/lefttext) | `LEFT_TEXT(X, length)`  
`LENGTH` | Text | Returns the number of characters in _X_. [Learn more.](https://docs.cloud.google.com/data-studio/length) | `LENGTH(X)`  
`LOG` | Arithmetic | Returns the logarithm to base 2 of X. [Learn more.](https://docs.cloud.google.com/data-studio/log) | `LOG(X)`  
`LOG10` | Arithmetic | Returns the logarithm to base 10 of X. [Learn more.](https://docs.cloud.google.com/data-studio/log10) | `LOG10(X)`  
`LOWER` | Text | Converts _X_ to lowercase. [Learn more.](https://docs.cloud.google.com/data-studio/lower) | `LOWER(X)`  
`MAX` | Aggregation | Returns the maximum value of X. [Learn more.](https://docs.cloud.google.com/data-studio/max) | `MAX(X)`  
`MEDIAN` | Aggregation | Returns the median of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/median) | `MEDIAN(X)`  
`MIN` | Aggregation | Returns the minimum value of X. [Learn more.](https://docs.cloud.google.com/data-studio/min) | `MIN(X)`  
`MINUTE` | Date | Returns the minutes component of a given date and time. [Learn more.](https://docs.cloud.google.com/data-studio/minute) | `MINUTE(datetime_expression)`  
`MONTH` | Date | Returns the month from a Date & Time value. [Learn more.](https://docs.cloud.google.com/data-studio/month) | `MONTH(date_expression)`  
`NARY_MAX` | Arithmetic | Returns the maximum value of X, Y, [,Z]*. All input arguments must be of the same type: all numbers. At least one input argument must be a field or an expression containing a field. [Learn more.](https://docs.cloud.google.com/data-studio/narymax) | `NARY_MAX(X, Y [,Z]*)`  
`NARY_MIN` | Arithmetic | Returns the minimum value of X, Y, [,Z]*. All input arguments must be of the same type, all numbers. At least one input argument must be a field or an expression containing a field. [Learn more.](https://docs.cloud.google.com/data-studio/narymin) | `NARY_MIN(X, Y [,Z]*)`  
`NATIVE_DIMENSION` | Miscellaneous | Returns the result of a SQL expression as evaluated by the underlying dataset. The expression cannot include any aggregations. [Learn more.](https://docs.cloud.google.com/data-studio/nativedimension) | `NATIVE_DIMENSION("JSON_VALUE('{"name": "Dana"}', '$.name')","STRING")`  
`NULLIF` | Conditional | Returns null if the input matches an expression, otherwise returns the input. [Learn more.](https://docs.cloud.google.com/data-studio/nullif) | `NULLIF(input_expression, expression_to_match)`  
`PARSE_DATE` | Date | Converts text to a date. [Learn more.](https://docs.cloud.google.com/data-studio/parsedate) | `PARSE_DATE(format_string, text)`  
`PARSE_DATETIME` | Date | Converts text to a date with time. [Learn more.](https://docs.cloud.google.com/data-studio/parsedatetime) | `PARSE_DATETIME(format_string, text)`  
`PERCENTILE` | Aggregation | Returns the percentile rank N of field X. [Learn more.](https://docs.cloud.google.com/data-studio/percentile) | `PERCENTILE(X,N)`  
`POWER` | Arithmetic | Returns result of raising X to the power Y. [Learn more.](https://docs.cloud.google.com/data-studio/power) | `POWER(X, Y)`  
`QUARTER` | Date | Returns the quarter of the year for a given date. [Learn more.](https://docs.cloud.google.com/data-studio/quarter) | `QUARTER(date_expression)`  
`REGEXP_CONTAINS` | Text | Returns true if _X_ contains the regular expression pattern, otherwise returns false. [Learn more.](https://docs.cloud.google.com/data-studio/regexpcontains) | `REGEXP_CONTAINS(X, regular_expression)`  
`REGEXP_EXTRACT` | Text | Returns first matching substring in _X_ which matches the regular expression pattern. [Learn more.](https://docs.cloud.google.com/data-studio/regexpextract) | `REGEXP_EXTRACT(X, regular_expression)`  
`REGEXP_MATCH` | Text | Returns true if _X_ matches the regular expression pattern, otherwise returns false. [Learn more.](https://docs.cloud.google.com/data-studio/regexpmatch) | `REGEXP_MATCH(X, regular_expression)`  
`REGEXP_REPLACE` | Text | Replaces all occurrences of text which matches the regular expression pattern in _X_ with the _replacement_ string. [Learn more.](https://docs.cloud.google.com/data-studio/regexpreplace) | `REGEXP_REPLACE(X, regular_expression, replacement)`  
`REPLACE` | Text | Returns a copy of _X_ with all occurrences of _Y_ in _X_ replaced by _Z_. [Learn more.](https://docs.cloud.google.com/data-studio/replace) | `REPLACE(X, Y, Z)`  
`RIGHT_TEXT ` | Text | Returns a number of characters from the end of _X_. The number of characters is specified by _length_. [Learn more.](https://docs.cloud.google.com/data-studio/righttext) | `RIGHT_TEXT(X, length)`  
`ROUND` | Arithmetic | Returns X rounded to Y precision digits. [Learn more.](https://docs.cloud.google.com/data-studio/round) | `ROUND(X, Y)`  
`SECOND` | Date | Returns the seconds component of a given date and time. [Learn more.](https://docs.cloud.google.com/data-studio/second) | `SECOND(datetime_expression)`  
`SIN` | Arithmetic | Returns the sine of X. [Learn more.](https://docs.cloud.google.com/data-studio/sin) | `SIN(X)`  
`SQRT` | Arithmetic | Returns the square root of X. Note that X must be non-negative. [Learn more.](https://docs.cloud.google.com/data-studio/sqrt) | `SQRT(X)`  
`STARTS_WITH ` | Text | Returns true if _X_ starts with text. Otherwise, returns false. Case-sensitive. [Learn more.](https://docs.cloud.google.com/data-studio/startswith) | `STARTS_WITH(X, text)`  
`STDDEV` | Aggregation | Returns the standard deviation of X. [Learn more.](https://docs.cloud.google.com/data-studio/stddev) | `STDDEV(X)`  
`SUBSTR` | Text | Returns a text that is a substring of _X_. The substring begins at _start index_ and is _length_ characters long. [Learn more.](https://docs.cloud.google.com/data-studio/substr) | `SUBSTR(X, start index, length)`  
`SUM` | Aggregation | Returns the sum of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/sum) | `SUM(X)`  
`TAN` | Arithmetic | Returns the tangent of X. [Learn more.](https://docs.cloud.google.com/data-studio/tan) | `TAN(X)`  
`TOCITY` | Geo | Returns the city name for X. | `TOCITY(X [,Input Format])`  
`TOCONTINENT` | Geo | Returns the continent name for X. [Learn more.](https://docs.cloud.google.com/data-studio/tocontinent) | `TOCONTINENT(X [,Input Format])`  
`TOCOUNTRY` | Geo | Returns the country name for X. [Learn more.](https://docs.cloud.google.com/data-studio/tocountry) | `TOCOUNTRY(X [,Input Format])`  
`TODATE` | Date | Returns a formatted compatibility mode Date. [Learn more](https://docs.cloud.google.com/data-studio/todate). | `TODATE(X, Input Format, Output Format)`  
`TODAY` | Date | Returns the current date as of the specified or default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/today) | `TODAY([time_zone])`  
`TOREGION` | Geo | Returns the region name for X. [Learn more.](https://docs.cloud.google.com/data-studio/toregion) | `TOREGION(X [,Input Format])`  
`TOSUBCONTINENT` | Geo | Returns the sub-continent name for X. [Learn more.](https://docs.cloud.google.com/data-studio/tosubcontinent) | `TOSUBCONTINENT(X [,Input Format])`  
`TRIM` | Text | Returns _X_ with leading and trailing spaces removed. [Learn more.](https://docs.cloud.google.com/data-studio/trim) | `TRIM(X)`  
`UNIX_DATE` | Date | Returns the number of days since 1970-01-01. [Learn more.](https://docs.cloud.google.com/data-studio/unixdate) | `UNIX_DATE(date_expression)`  
`UPPER` | Text | Converts _X_ to uppercase. [Learn more.](https://docs.cloud.google.com/data-studio/upper) | `UPPER(X)`  
`VARIANCE` | Aggregation | Returns the variance of X. [Learn more.](https://docs.cloud.google.com/data-studio/variance) | `VARIANCE(X)`  
`WEEK` | Date | Returns the week number for a given date. [Learn more.](https://docs.cloud.google.com/data-studio/week) | `WEEK(Date)`  
`WEEKDAY` | Date | Returns a number representing the day of the week for a given date. [Learn more.](https://docs.cloud.google.com/data-studio/weekday) | `WEEKDAY(Date)`  
`YEAR` | Date | Returns the year of a given date. [Learn more.](https://docs.cloud.google.com/data-studio/year) | `YEAR(Date)`  
`YEARWEEK` | Date | Returns the year and week number of a given date. [Learn more.](https://docs.cloud.google.com/data-studio/yearweek) | `YEARWEEK(Date)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
