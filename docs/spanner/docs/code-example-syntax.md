---
url: https://docs.cloud.google.com/spanner/docs/code-example-syntax/
title: SQL syntax quick reference \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:26.928403+00:00
---

# SQL syntax quick reference  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/code-example-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  SQL syntax quick reference Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a quick reference (also known as a _cheat sheet_) for SQL syntax used in Spanner documentation code examples. 

For a more comprehensive reference of SQL query syntax in Spanner, see [Query syntax in GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax).

## SQL syntax notation rules

The following table lists and describes the syntax notation rules that Spanner documentation commonly uses.

Notation | Example | Description  
---|---|---  
Square brackets | `[ ]` | Indicates that the enclosed clause or argument is optional. Don't include these brackets in your SQL query.   
Parentheses | `( )` | Literal parentheses. Include the parentheses in your SQL query.  
Vertical bar | `|` | Indicates that you must choose only one option from the alternatives separated by vertical bars. Don't include bars in your SQL query.   
Curly braces | `{ }` | Indicates that the enclosed items represent a set of choices. You must choose exactly one of the options, which are separated by vertical bars (for example, in `{ a | b | c }`, you must choose a, b, or c). Don't include the curly braces in your SQL query.   
Ellipsis | `...` | Indicates that a list or a portion of the syntax has been truncated for brevity. This is distinct from a comma followed by an ellipsis, which indicates a repeating list. Don't include the ellipsis in your query.   
Comma | `,` | Indicates a literal comma, typically used to separate items in a list. Include commas in your query.   
Comma followed by an ellipsis | `, ...` | Indicates that the preceding element can be repeated multiple times, with each instance separated by a comma. Don't include the ellipsis in your query. Include the commas to separate the repeated elements.   
Item list | `item [, ...]` | Indicates that you must include at least one item. You can optionally include more items, separated by commas. Don't include the brackets or the ellipsis in your query. Include the commas to separate the additional item.   
`[item, ...]` | Indicates that you can optionally include at least one item. You can also optionally include more items, separated by commas. Don't include the brackets or the ellipsis in your query. Include the commas to separate the additional items.   
Single quotes | `''` | Indicates a literal single quote mark. Used to define [string literals](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/lexical#string_and_bytes_literals) in your query. Include the single quote marks in your query.   
Double quotes or Backticks | `""` or ```` | Indicates literal double quote marks or backticks. Used to enclose [quoted identifiers](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/lexical#quoted_identifiers) in your query. Include the double quote marks or backticks in your query.   
Angle brackets | `< >` | Literal angle brackets. Include the angle brackets in your SQL query.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
