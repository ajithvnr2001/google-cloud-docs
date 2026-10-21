---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-get_timestamp/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:03.566876+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-get_timestamp/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.get_timestamp

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.get_timestamp(unix_seconds, optional timestamp_format/time_granularity, optional timezone)
    

#### Description

This function returns a string in the format `YYYY-MM-DD`, representing the day a timestamp is in.

  * `unix_seconds` is an integer representing the number of seconds past Unix epoch, such as `$e.metadata.event_timestamp.seconds`, or a placeholder containing that value.
  * `timestamp_format` is optional and is a string representing the format for the timestamp. If omitted, the default is `%F %T`. You can specify the format using a date time format string or one of the following time granularity: `SECOND`, `MINUTE`, `HOUR`, `DATE`, `WEEK`, `MONTH`, or `YEAR`. For more formatting options, see [Format elements for date and time parts](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time)
  * `time_zone` is optional and is a string representing a time zone. If omitted, the default is `GMT`. You can specify time zones using string literals. The options are as follows: 
    * The IANA Time Zone (TZ) database name, for example, `America/Los_Angeles`. For more information, see the [list of tz database time zones on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    * The time zone offset from UTC, in the format `(+|-)H[H][:M[M]]`, for example: "-08:00".

**Note:** To maintain consistency with standard Gregorian calendar years, always use the 4-digit %Y format. Avoid using %y (2-digit) to prevent sorting errors, and avoid %G (ISO year), which can shift dates near the New Year depending on the week cycle.

Here are examples of valid `time_zone` specifiers, which you can pass as the second argument to time extraction functions:
    
    
    "America/Los_Angeles", or "-08:00". ("PST" is not supported)
    "America/New_York", or "-05:00". ("EST" is not supported)
    "Europe/London"
    "UTC"
    "GMT"
    

#### Param data types

`INT`, `STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

In this example, the `time_zone` argument is omitted, so it defaults to `GMT`.
    
    
    $ts = $e.metadata.collected_timestamp.seconds
    
    timestamp.get_timestamp($ts) = "2024-02-22 10:43:51"
    

##### Example 2

This example uses a string literal to define the `time_zone`.
    
    
    $ts = $e.metadata.collected_timestamp.seconds
    
    timestamp.get_timestamp($ts, "%F %T", "America/Los_Angeles") = "2024-02-22 10:43:51"
    

##### Example 3

This example uses a string literal to define the `timestamp_format`.
    
    
    $ts = $e.metadata.collected_timestamp.seconds
    
    timestamp.get_timestamp($ts, "%Y-%m", "GMT") = "2024-02"
    

##### Example 4

This example formats a unix timestamp as a string at second granularity.
    
    
    timestamp.get_timestamp(1708598631, "SECOND", "GMT") = "2024-02-22 10:43:51"
    

##### Example 5

This example formats a unix timestamp as a string at minute granularity.
    
    
    timestamp.get_timestamp(1708598631, "MINUTE", "GMT") = "2024-02-22 10:43"
    

##### Example 6

This example formats a unix timestamp as a string at hour granularity.
    
    
    timestamp.get_timestamp(1708598631, "HOUR", "GMT") = "2024-02-22 10"
    

##### Example 7

This example formats a unix timestamp as a string at day granularity.
    
    
    timestamp.get_timestamp(1708598631, "DATE", "GMT") = "2024-02-22"
    

##### Example 8

This example formats a unix timestamp as a string at week granularity.
    
    
    timestamp.get_timestamp(1708598631, "WEEK", "GMT") = "2024-02-18"
    

##### Example 9

This example formats a unix timestamp as a string at month granularity.
    
    
    timestamp.get_timestamp(1708598631, "MONTH", "GMT") = "2024-02"
    

##### Example 10

This example formats a unix timestamp as a string at year granularity.
    
    
    timestamp.get_timestamp(1708598631, "YEAR", "GMT") = "2024"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
