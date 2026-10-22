---
url: https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector/
title: Overview of Looker connector requirements, limits, and feature support \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:07.546225+00:00
---

# Overview of Looker connector requirements, limits, and feature support  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Overview of Looker connector requirements, limits, and feature support Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the following topics about the Looker connector in Data Studio:

  * Required configurations for each type of Looker instance
  * Limits of the Looker connector
  * Unsupported or partially supported Data Studio features



## Looker instance requirements

To set up a Looker data source by using the Looker connector in Data Studio, first verify that your Looker instance meets the following requirements:

  * The instance must be [Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted). **The Data Studio connector isn't available for customer-hosted Looker instances.**
  * The [**Data Studio** BI connector](https://docs.cloud.google.com/looker/docs/bi-connectors#looker_studio) must be enabled in the **Platform** section of the Looker instance's **Admin** panel.
  * Looker (original) instances that have the [**Enable IP Allowlist**](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) setting enabled may require additional configuration. [Contact Support](https://cloud.google.com/contact) for assistance.
  * Looker (original) instances must meet the following version requirements:

Hosting provider |  Minimum Looker version   
---|---  
AWS, Azure | 23.4  
Google Cloud | 22.16  
  * The Looker connector can connect to a Looker (Google Cloud core) [private connections (private services access)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) instance that is on the same network as Data Studio from [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro) or [Looker reports](https://docs.cloud.google.com/looker/docs/create-view-edit-reports) using the Looker instance ID. For more information, see the [Connecting to a private connections instance from Data Studio Pro or Looker reports](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil) documentation page.

  * If you're using a Looker (Google Cloud core) instance that has an [IP allowlist](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist) configured, the [**Link Google services with this instance** checkbox](https://docs.cloud.google.com/looker/docs/looker-core-ip-allowlist#allowlist-services) must be selected on the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the instance's **Instance** page in the Google Cloud console.

  * The Looker connector, when used with Data Studio Pro or Looker reports, can't connect to a Looker (Google Cloud core) instance that is inside of a [VPC Service Controls](https://docs.cloud.google.com/looker/docs/looker-core-vpcsc) perimeter.

  * Some tasks that are performed on reports that are built with the Looker connector require additional permissions, which are granted within Looker. For more information, see [Overview of Looker connector permissions](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions).




## Limits of the Looker connector

The Looker connector exhibits the following limitations, which may restrict the types of Looker instances and models that you can connect to:

  * The Looker connector cannot connect to [customer-hosted](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) Looker instances.
  * Exceptionally large Looker models (generally those that have more than 100 Explores) may cause long delays or timeouts during the data source creation process.
  * There is a 5-minute query timeout.
  * Charts are limited to 5,000 rows. While Looker has increased row limits for some chart types (such as maps and tables), Data Studio doesn't inherit those increases.
  * Data downloads and exports are limited to 75,000 rows, depending on [user permissions](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions).
  * Limit the [canvas size](https://docs.cloud.google.com/data-studio/report-and-page-layout) of reports that use table charts to no more than 500 px by 500 px.



## Support of Data Studio features

Looker data sources may not support or may only partially support the following Data Studio features:

  * Number of fields: You can include up to 100 [dimensions](https://docs.cloud.google.com/data-studio/dimension) and up to 100 [metrics](https://docs.cloud.google.com/data-studio/metric) in a [table](https://docs.cloud.google.com/data-studio/table-reference) visualization.
  * Data downloads, schedules, alerts, and exports: 
    * Downloads, schedules, alerts, and data exports aren't supported for reports that are built using Looker data from a Looker (Google Cloud core) instance that uses private connections or that is configured to use a Virtual Private Cloud (VPC) IP address. To learn more about Looker (Google Cloud core) instance networking, see the [Looker (Google Cloud core) networking options](https://docs.cloud.google.com/looker/docs/looker-core-networking-options) documentation.
    * Downloads, schedules, alerts, and data exports aren't supported for reports that are built using Looker data from a Looker (original) instance that is configured to use an [IP allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist).
    * Data export row limits are determined by [user permissions](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions).
  * Calculated fields: Data sources that are created with the Looker connector support some [Data Studio functions](https://docs.cloud.google.com/data-studio/function-list) for [calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields). These functions can be applied on dimensions only. 

#### Supported functions for calculated fields

Name | Type | Description | Syntax  
---|---|---|---  
`ABS` | Arithmetic | Returns the absolute value of number. [Learn more.](https://docs.cloud.google.com/data-studio/abs) | `ABS(X)`  
`ACOS` | Arithmetic | Returns the inverse of the cosine of X. [Learn more.](https://docs.cloud.google.com/data-studio/acos) | `ACOS(X)`  
`ASIN` | Arithmetic | Returns the inverse of the sine of X. [Learn more.](https://docs.cloud.google.com/data-studio/asin) | `ASIN(X)`  
`ATAN` | Arithmetic | Returns the inverse of the tangent of X. [Learn more.](https://docs.cloud.google.com/data-studio/atan) | `ATAN(X)`  
`AVG` | Aggregation | Returns the average of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/avg) | `AVG(X)`  
`CASE (Simple)` | Conditional | Compares `input_expression` to `expression_to_match` of each successive WHEN clause and returns the first `result` where this comparison returns `true`. [Learn more.](https://docs.cloud.google.com/data-studio/case-simple) | 
        
        CASE input_expression
            WHEN expression_to_match THEN result
            [WHEN expression_to_match THEN result]
            [...]
            [ELSE result]
            END  
  
`CASE` | Conditional | Evaluates the `condition` of each successive WHEN clause and returns the first `result` where the `condition` is true; any remaining WHEN and ELSE clauses aren't evaluated. If all conditions are false or NULL, returns `else_result` if present; if not present, returns `NULL`. [Learn more.](https://docs.cloud.google.com/data-studio/case-searched) | 
        
        CASE
            WHEN condition THEN result
            [WHEN condition THEN result]
            [...]
            [ELSE else_result]
            END  
  
`CAST` | Miscellaneous | Cast field or expression into TYPE. Aggregated fields aren't allowed inside CAST.`TYPE` can be `NUMBER`, `TEXT`, or `DATETIME`. [Learn more.](https://docs.cloud.google.com/data-studio/cast) | `CAST(_field_expression_ AS _TYPE_)`  
`CEIL` | Arithmetic | Returns the nearest integer greater than X. For example, if the value of X is v, `CEIL(X)` is greater than or equal to v. [Learn more.](https://docs.cloud.google.com/data-studio/ceil) | `CEIL(X)`  
`COALESCE` | Conditional | Returns the first non-missing value found in a list of fields. [Learn more.](https://docs.cloud.google.com/data-studio/coalesce) | `COALESCE(field_expression[,field_expression, ...])`  
`CONCAT` | Text | Returns a text that is the concatenation of X and Y. [Learn more.](https://docs.cloud.google.com/data-studio/concat) | `CONCAT(X, Y)`  
`CONTAINS_TEXT` | Text | Returns true if _X_ contains text, otherwise returns false. Case-sensitive. [Learn more.](https://docs.cloud.google.com/data-studio/containstext) | `CONTAINS_TEXT(X, text)`  
`COS` | Arithmetic | Returns the cosine of X. [Learn more.](https://docs.cloud.google.com/data-studio/cos) | `COS(X)`  
`COUNT_DISTINCT` | Aggregation | Returns the number of unique values of X. [Learn more.](https://docs.cloud.google.com/data-studio/countdistinct) | `COUNT_DISTINCT(X)`  
`CURRENT_DATE` | Date | Returns the current date as of the default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/currentdate) | `CURRENT_DATE()`  
`CURRENT_DATETIME` | Date | Returns the current date and time as of the default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/currentdatetime) | `CURRENT_DATETIME()`  
`DATE` | Date | Constructs a `Date` field or value from numbers or from a `Date & Time` field or expression. [Learn more.](https://docs.cloud.google.com/data-studio/date) | `DATE(year, month, day)`  
`DATE_DIFF` | Date | Returns the difference in days between X and Y (X - Y). [Learn more.](https://docs.cloud.google.com/data-studio/datediff) | `DATE_DIFF(X, Y)`  
`DATE_FROM_UNIX_DATE` | Date | Interprets an integer as the number of days since 1970-01-01. [Learn more.](https://docs.cloud.google.com/data-studio/datefromunixdate) | `DATE_FROM_UNIX_DATE(integer)`  
`DATETIME` | Date | Constructs a Date & Time field or value from numbers. [Learn more.](https://docs.cloud.google.com/data-studio/datetime) | `DATETIME(year, month, day, hour, minute, second)`  
`DATETIME_ADD` | Date | Adds a specified time interval to a date. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. [Learn more.](https://docs.cloud.google.com/data-studio/datetimeadd) | `DATETIME_ADD(datetime_expression, INTERVAL integer part)`  
`DATETIME_DIFF` | Date | Returns the number of part boundaries between two dates. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. [Learn more.](https://docs.cloud.google.com/data-studio/datetimediff) | `DATETIME_DIFF(date_expression, date_expression, part)`  
`DATETIME_SUB` | Date | Subtracts a specified time interval from a date. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. [Learn more.](https://docs.cloud.google.com/data-studio/datetimesub) | `DATETIME_SUB(datetime_expression, INTERVAL integer part)`  
`DATETIME_TRUNC` | Date | Truncates a date to the specified granularity. Accepted `part` values include `SECOND`, `MINUTE`, `HOUR`, `DAY`, `MONTH`, `YEAR`. [Learn more.](https://docs.cloud.google.com/data-studio/datetimetrunc) | `DATETIME_TRUNC(date_expression, part)`  
`DAY` | Date | Returns the day of a Date or Date & Time. [Learn more.](https://docs.cloud.google.com/data-studio/day) | `Day(date_expression)`  
`EXTRACT` | Date | Returns part of a date or date & time. Accepted `part` values include `DAY`, `MONTH`, `YEAR`. [Learn more.](https://docs.cloud.google.com/data-studio/extract) | `EXTRACT(part FROM date_expression)`  
`FLOOR` | Arithmetic | Returns the nearest integer less than X. For example, if the value X is v, `FLOOR(X)` is equal to or less than v. [Learn more.](https://docs.cloud.google.com/data-studio/floor) | `FLOOR(X)`  
`HOUR` | Date | Returns the hour of a date and time. [Learn more.](https://docs.cloud.google.com/data-studio/hour) | `HOUR(datetime_expression)`  
`IF` | Conditional | If `condition` is true, returns `true_result`, else returns `false_result`. `false_result` isn't evaluated if `condition` is true. `true_result` isn't evaluated if `condition` is false or NULL. [Learn more.](https://docs.cloud.google.com/data-studio/if) | `IF(condition, true_result, false_result)`  
`IFNULL` | Conditional | Returns a result if the input is null, otherwise, returns the input. [Learn more.](https://docs.cloud.google.com/data-studio/ifnull) | `IFNULL(input_expression, null_result)`  
`LEFT_TEXT ` | Text | Returns a number of characters from the beginning of _X_. The number of characters is specified by _length_. [Learn more.](https://docs.cloud.google.com/data-studio/lefttext) | `LEFT_TEXT(X, length)`  
`LENGTH` | Text | Returns the number of characters in _X_. [Learn more.](https://docs.cloud.google.com/data-studio/length) | `LENGTH(X)`  
`LOG` | Arithmetic | Returns the logarithm to base 2 of X. [Learn more.](https://docs.cloud.google.com/data-studio/log) | `LOG(X)`  
`LOG10` | Arithmetic | Returns the logarithm to base 10 of X. [Learn more.](https://docs.cloud.google.com/data-studio/log10) | `LOG10(X)`  
`LOWER` | Text | Converts X to lowercase. [Learn more.](https://docs.cloud.google.com/data-studio/lower) | `LOWER(X)`  
`MAX` | Aggregation | Returns the maximum value of X. [Learn more.](https://docs.cloud.google.com/data-studio/max) | `MAX(X)`  
`MEDIAN` | Aggregation | Returns the median of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/median) | `MEDIAN(X)`  
`MIN` | Aggregation | Returns the minimum value of X. [Learn more.](https://docs.cloud.google.com/data-studio/min) | `MIN(X)`  
`MINUTE` | Date | Returns the minutes component of a given date and time. [Learn more.](https://docs.cloud.google.com/data-studio/minute) | `MINUTE(datetime_expression)`  
`MONTH` | Date | Returns the month from a `Date & Time` value. [Learn more.](https://docs.cloud.google.com/data-studio/month) | `MONTH(date_expression)`  
`NULLIF` | Conditional | Returns `NULL` if the input matches an expression, otherwise returns the input. [Learn more.](https://docs.cloud.google.com/data-studio/nullif) | `NULLIF(input_expression, expression_to_match)`  
`POWER` | Arithmetic | Returns result of raising X to the power Y. [Learn more.](https://docs.cloud.google.com/data-studio/power) | `POWER(X, Y)`  
`REPLACE` | Text | Returns a copy of _X_ with all occurrences of _Y_ in _X_ replaced by _Z_. [Learn more.](https://docs.cloud.google.com/data-studio/replace) | `REPLACE(X, Y, Z)`  
`RIGHT_TEXT ` | Text | Returns a number of characters from the end of _X_. The number of characters is specified by _length_. [Learn more.](https://docs.cloud.google.com/data-studio/righttext) | `RIGHT_TEXT(X, length)`  
`ROUND` | Arithmetic | Returns `X` rounded to `Y` precision digits. [Learn more.](https://docs.cloud.google.com/data-studio/round) | `ROUND(X, Y)`  
`SECOND` | Date | Returns the seconds component of a given date and time. [Learn more.](https://docs.cloud.google.com/data-studio/second) | `SECOND(datetime_expression)`  
`SIN` | Arithmetic | Returns the sine of X. [Learn more.](https://docs.cloud.google.com/data-studio/sin) | `SIN(X)`  
`SQRT` | Arithmetic | Returns the square root of X. Note that X must be non-negative. [Learn more.](https://docs.cloud.google.com/data-studio/sqrt) | `SQRT(X)`  
`SUBSTR` | Text | Returns a text that is a substring of _X_. The substring begins at _start index_ and is _length_ characters long. [Learn more.](https://docs.cloud.google.com/data-studio/substr) | `SUBSTR(X, start index, length)`  
`SUM` | Aggregation | Returns the sum of all values of X. [Learn more.](https://docs.cloud.google.com/data-studio/sum) | `SUM(X)`  
`TAN` | Arithmetic | Returns the tangent of X. [Learn more.](https://docs.cloud.google.com/data-studio/tan) | `TAN(X)`  
`TODAY` | Date | Returns the current date as of the default timezone. [Learn more.](https://docs.cloud.google.com/data-studio/today) | `TODAY()`  
`UNIX_DATE` | Date | Returns the number of days since 1970-01-01. [Learn more.](https://docs.cloud.google.com/data-studio/unixdate) | `UNIX_DATE(date_expression)`  
`UPPER` | Text | Converts _X_ to uppercase. [Learn more.](https://docs.cloud.google.com/data-studio/upper) | `UPPER(X)`  
`YEAR` | Date | Returns the year of a given date. [Learn more.](https://docs.cloud.google.com/data-studio/year) | `YEAR(Date)`  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
