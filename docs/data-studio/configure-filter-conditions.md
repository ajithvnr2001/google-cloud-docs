---
url: https://docs.cloud.google.com/data-studio/configure-filter-conditions/
title: Configure filter conditions \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:28.452710+00:00
---

# Configure filter conditions  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/configure-filter-conditions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Configure filter conditions Stay organized with collections  Save and categorize content based on your preferences. 

You can configure filter conditions in Data Studio to refine the exact records displayed in your reports. By including or excluding data based on your specific criteria, you remove noise and highlight relevant information. You can combine multiple conditions to build targeted views for your audience.

## Include versus exclude filters

_Include_ filters retrieve only the records that _match_ the conditions, while _exclude_ filters retrieve only the records that _don't match_ the conditions.

## Filter clauses

A condition consists of one or more clauses.

A simple filter has just one clause that consists of a dimension or measure, a condition, and a value. For example, in the filter clause **Country Equal to (=) France** , **Country** is the dimension, **Equal to (=)** is the condition, and **France** is the value.

Multiple clauses can be joined with an OR operator (true if _any_ conditions are met), an AND operator (true if _all_ conditions are met), or both. For example, you can combine multiple clauses to create a filter with more complex logic, such as a filter that includes the following conditions:

  * The value of **Country** is either **France** or **Germany**
  * The value of **User Type** is **New user**
  * The value of **Sessions** is greater than 100



This filter clause would be defined as follows:

> ** Country Equal to (=) France OR Country Equal to (=) Germany AND User Type Equal to (=) New user AND Sessions Greater Than 100 **

A filter clause that uses an OR operator can contain dimensions or metrics, but not both.

## Conditions

Conditions compare the fields in the filter against values that you provide. The available conditions depend on whether you are filtering a text, number, date, or logical field.

### Text conditions

Conditions  |  Description   
---|---  
Equal to (=)  |  The comparison value exactly matches the dimension value.  **Example:** The comparison value "chrome" exactly matches "chrome" but not "Chrome" or "chromebook".   
Contains  |  The comparison value is contained within the dimension value.  **Example:** The comparison value "chrome" is contained within "chrome" and "chromebook" but not "Chrome".   
Starts with  |  The dimension value starts with the comparison value.  **Example:** The comparison value "Chrome" starts with "Chrome" and "Chromebook" but not "Google Chrome".   
Regexp Contains  |  The dimension value contains the regular expression.  **Example:** **(?i)C[a-z]*** matches "chrome", "Chrome", "Chromebook", and "Google Chrome".  **Regexp Contains** searches for the regular expression anywhere in the data.  The **(?i)** flag makes the regular expression case-insensitive.   
Regexp Match  |  The dimension value matches the regular expression.  **Example:** **C[a-z]*** matches "Chromebook" and "Chrome" but not "Google Chrome".  **Regexp Match** is an exact match expression: the data must begin with "C".   
In  |  One or more of the comparison values exactly matches the dimension value. Works just like **Equal to (=)** but for a comma-separated list of values.  **Example:** **In Chrome,Windows,MacOS** matches if any of those are in the dimension.  If your values contain commas or backslashes as part of the data to match, use a backslash to escape them.  **Example:** If you want to match "ab,cd" and "50\50", precede the comma and backslash with \:  **In "ab\,cd, 50\\\50"**  
Is Null  |  Matches if the dimension value is null.   
  
**Note:** Text comparisons are case-sensitive. For case-insensitive matching, use regular expressions.

Regular expressions in Data Studio use [Google RE2](https://github.com/google/re2/wiki/Syntax) regular expression syntax. 

### Numeric conditions

Condition  |  Description   
---|---  
Equal to (=)  |  The dimension or metric value is equal to the comparison value.   
Between (>=&&<=)  |  The dimension or metric value is within the specified range. The range includes the numbers that are specified.   
Greater than or equal to (>=)  |  The dimension or metric value is greater than or equal to the comparison value.   
Greater than (<)  |  The dimension or metric value is greater than the comparison value.   
Less than or equal to (<=)  |  The dimension or metric value is less than or equal to the comparison value.   
Less than (<)  |  The dimension or metric value is less than the comparison value.   
Is Null  |  The dimension or metric value is null.   
  
### Date and time conditions

Condition  |  Description   
---|---  
Equal to (=)  |  The dimension value is equal to the comparison value.   
Between (>=&&<=)  |  The dimension value is within the specified range, inclusive of both the start and end dates.   
Greater than or equal to (>=)  |  The dimension value is later than or the same date as the comparison value.   
Greater than (>)  |  The dimension value is later than the comparison value.   
Less than or equal to (<=)  |  The dimension value is earlier than or the same date as the comparison value.   
Less than (<)  |  The dimension value is earlier than the comparison value.   
Is Null  |  The dimension value is null.   
Is in the Last  |  The dimension value is within the specified duration relative to the current date.  **Example:** "Is in the Last 7 Days" returns the current day and the previous 6 days.  **Example:** "Is in the Last 1 Day" returns the current day.   
Is Before  |  The dimension value is earlier than the comparison value relative to the current date, not inclusive of the comparison value.   
Is On or After  |  The dimension value is within the specified duration relative to the current date, inclusive of the earliest date in the specified range.  **Example:** "Is On or After 1 day ago" returns yesterday's date and all dates thereafter.   
Is This  |  The dimension value is within a specified duration interval, relative to and inclusive of the current date.  **Example:** "Is This Week" returns the current day and the proceeding 6 days.   
Is Next  |  The dimension value is within a specified duration interval, relative to the current date.  **Example:** "Is Next Week" returns all values that occur in the following week, starting on Monday and ending on Sunday.   
Is in the Month  |  The dimension value is within the specified calendar month and year.   
Is in the Year  |  The dimension value is within the specified year.   
  
### Boolean conditions

Condition  |  Description   
---|---  
True  |  The dimension value evaluates to "true".   
False  |  The dimension value evaluates to "false".   
Is Null  |  The dimension or metric value is null.   
  
## Values

When defining filters on charts, pages, or reports that use **Equal to (=)** or **In** conditions, report editors can select from a list of possible filter values that are provided from the underlying data. To see filter value suggestions, enable **Show suggested values while typing** in the filter editor. Filter suggestions are supported for all data connectors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
