---
url: https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes/
title: Data types, functions, operators \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:20:47.421480+00:00
---

# Data types, functions, operators  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/syntax/datatypes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Data types, functions, operators Stay organized with collections  Save and categorize content based on your preferences. 

The Workflows syntax supports the following data types:

  * Integer (64 bit, signed)
  * Double (64 bit, signed floating point number)
  * String (UTF‑8 encoding, [maximum length](https://docs.cloud.google.com/workflows/quotas#resource_limits))
  * Boolean (`true`/`false`, `True`/`False`, `TRUE`/`FALSE`)
  * Bytes (see Returning bytes)
  * Null



## Data type functions

The Workflows standard library includes functions to convert, format, and operate on data types. For details, see [Standard library overview](https://docs.cloud.google.com/workflows/docs/reference/stdlib/overview).

## Returning bytes

Bytes can't be returned by a workflow as they can't be JSON-encoded. You can [encode bytes to Base64 text](https://docs.cloud.google.com/workflows/docs/reference/stdlib/base64/encode). You can also [decode JSON bytes into an object](https://docs.cloud.google.com/workflows/docs/reference/stdlib/json/decode). Bytes _can_ be used as the body of HTTP requests. For more information, see [Make an HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

## Logical operators

Logical operators can be used only on boolean values, or on expressions that evaluate to boolean values. For examples, see the [Syntax cheat sheet](https://docs.cloud.google.com/workflows/docs/reference/syntax/syntax-cheat-sheet).

The following logical operators can be lower-case or upper-case (but not mixed-case):

  * `and`: logical AND
  * `or`: logical OR
  * `not`: logical NOT



## Order of operations

The following table is arranged in descending order of precedence of operators. Parentheses `()` have the highest precedence (most binding) while the `or` operator has the lowest precedence (least binding).

**Operator**| **Description**  
---|---  
`()` | Parentheses  
`.` | Access object property  
`[]` | Access list element  
`not` | Boolean NOT  
`-` | Unary minus  
`*`, `/`, `//`, `%` | Multiplication, division, floor division, remainder  
`+`, `-` | Addition, subtraction  
``, `<=`, `>=`, `>`, `==`, `!=`, `in` | Comparison, equality, membership  
`and` | Boolean AND  
`or` | Boolean OR  
  
## Implicit data type conversions

These tables show the outcome of expressions using the given operator and the following data types as inputs. For example, using the `+` operator on two strings results in a string.

**`+` operator**  
---  
| INTEGER | DOUBLE | STRING | BOOL  
INTEGER | INTEGER | DOUBLE | STRING | **ERROR**  
DOUBLE | DOUBLE | DOUBLE | STRING | **ERROR**  
STRING | STRING | STRING | STRING | STRING  
BOOL | **ERROR** | **ERROR** | STRING | **ERROR**  
  
In the case of integer or double addition, overflow can occur if the resulting value exceeds the available precision. During string concatenation, if the resulting string exceeds the allowed length of the string data type, the operation throws an error.

**`-` operator**  
---  
| INTEGER | DOUBLE | STRING | BOOL  
INTEGER | INTEGER | DOUBLE | **ERROR** | **ERROR**  
DOUBLE | DOUBLE | DOUBLE | **ERROR** | **ERROR**  
STRING | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
BOOL | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
**`*` operator**  
---  
| INTEGER | DOUBLE | STRING | BOOL  
INTEGER | INTEGER | DOUBLE | **ERROR** | **ERROR**  
DOUBLE | DOUBLE | DOUBLE | **ERROR** | **ERROR**  
STRING | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
BOOL | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
**`/` operator**  
---  
| INTEGER | DOUBLE | STRING | BOOL  
INTEGER | DOUBLE | DOUBLE | **ERROR** | **ERROR**  
DOUBLE | DOUBLE | DOUBLE | **ERROR** | **ERROR**  
STRING | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
BOOL | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
**`<`, `>`, `<=`, `>=` comparison operators**  
---  
| INTEGER | DOUBLE | STRING | BOOL  
INTEGER | BOOL | BOOL | **ERROR** | **ERROR**  
DOUBLE | BOOL | BOOL | **ERROR** | **ERROR**  
STRING | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
BOOL | **ERROR** | **ERROR** | **ERROR** | **ERROR**  
**`==`, `!=` comparison operators**  
---  
| INTEGER | DOUBLE | STRING | BOOL | NULL  
INTEGER | BOOL | BOOL | **ERROR** | **ERROR** | BOOL  
DOUBLE | BOOL | BOOL | **ERROR** | **ERROR** | BOOL  
STRING | **ERROR** | **ERROR** | BOOL | **ERROR** | BOOL  
BOOL | **ERROR** | **ERROR** | **ERROR** | BOOL | BOOL  
NULL | BOOL | BOOL | BOOL | BOOL | BOOL  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
