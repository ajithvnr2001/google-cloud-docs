---
url: https://docs.cloud.google.com/data-studio/parsedatetime/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:38.438123+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/parsedatetime/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PARSE_DATETIME

Converts text to a date with time.

## Sample usage

```PARSE_DATETIME("%Y-%m-%d %H:%M:%S", DateTimeText)```

## Syntax

```PARSE_DATETIME( format_string, text )```

### Parameters

```format_string``` \- See [Supported Format Elements For DATETIME](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time) for a list of format elements that this function supports.

```text``` \- a text representation of a date.

## Return data type

Date & Time

## Examples

In this example, **DateTimeText** is a field containing a text date and time. The result of applying ```PARSE_DATETIME``` with the correct _format_string_ is a Date & Time value.

Example formula | Input | Output  
---|---|---  
` PARSE_DATETIME("%d/%m/%y %H:%M:%S", DateTimeText) ` |  ` 25/12/08 12:12:12 ` |  2008-12-25 12:12:12   
  
The following example parses the _DateTimeText_ field containing a date in a natural language format as a Date & Time value.

Example formula | Input | Output  
---|---|---  
` PARSE_DATETIME('%A, %B %e, %Y', DateTimeText) ` |  Wednesday, December 19, 2018  |  2018-12-19 00:00:00   
  
## Notes

When using ```PARSE_DATETIME```, keep the following in mind:

  * **Unspecified fields**. Any unspecified field is initialized from 1970-01-01.
  * **Case insensitive names**. Names, such as Monday, February, and so on, are case insensitive.
  * **Whitespace**. One or more consecutive white spaces in the format string matches zero or more consecutive white spaces in the date string. In addition, leading and trailing white spaces in the date string are always allowed -- even if they are not in the format string.
  * **Format precedence**. When two (or more) format elements have overlapping information (for example both ```%F``` and ```%Y``` affect the year), the last one generally overrides any earlier ones.



> This function supports format elements, but does not have full support for ```%Q, %a, %A, %g, %G, %j, %u, %U, %V, %w, and %W.``` See [Supported Format Elements For DATETIME](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time) for a list of format elements that this function supports.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
