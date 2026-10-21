---
url: https://docs.cloud.google.com/data-studio/literals/
title: Literals \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:30.027396+00:00
---

# Literals  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/literals/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Literals Stay organized with collections  Save and categorize content based on your preferences. 

A literal represents a constant value of a built-in data type. Some, but not all, data types can be expressed as literals.

## String literals

String literals must be _quoted_ , either with single ( `'` ) or double ( `"` ) quotation marks.

**Quoted literals:**

Literal  |  Sample usage  |  Notes   
---|---|---  
Quoted string  | 

  * ` "abc" `
  * ` "it's" `
  * ` 'it\'s' `
  * ` 'Title: "Boy"' `

| 

  * Quoted strings enclosed by single ( ` ' ` ) quotes can contain unescaped double ( ` " ` ) quotes, as well as the inverse. 
  * Backslashes ( ` \ ` ) introduce escape sequences. See the Escape sequences for string literals section. 
  * Quoted strings cannot contain newlines, even when preceded by a backslash ( ` \ ` ). 

  
Raw string  | 

  * ` R"abc+" `
  * ` r'f\(abc,(.\*),def\)' `

| 

  * Quoted literals that have the raw string literal prefix ( ` r ` or ` R ` ) are interpreted as raw/regex strings. 
  * Backslash characters ( ` \ ` ) do not act as escape characters. If a backslash followed by another character occurs inside the string literal, both characters are preserved. 
  * A raw string cannot end with an odd number of backslashes. 
  * Raw strings are useful for constructing regular expressions. 

  
  
### Escape sequences for string literals

The following table lists all valid escape sequences for representing non-alphanumeric characters in string literals. Any sequence not in this table produces an error.

Escape Sequence  |  Description   
---|---  
` \a ` |  Bell   
` \b ` |  Backspace   
` \f ` |  Formfeed   
` \n ` |  Newline   
` \r ` |  Carriage Return   
` \t ` |  Tab   
` \v ` |  Vertical Tab   
` \\ ` |  Backslash ( ` \ ` )   
` \? ` |  Question Mark ( ` ? ` )   
` \" ` |  Double Quote ( ` " ` )   
` \' ` |  Single Quote ( ` ' ` )   
` \\` ` |  Backtick ( ` \` ` )   
` \ooo ` |  Octal escape, with exactly 3 digits (in the range 0–7). Decodes to a single Unicode character (in string literals) or byte (in bytes literals).   
` \xhh ` or ` \Xhh ` |  Hex escape, with exactly 2 hex digits (0–9 or A–F or a–f). Decodes to a single Unicode character (in string literals) or byte (in bytes literals). Examples: 

  * ` '\x41' ` == ` 'A' `
  * ` '\x41B' ` is ` 'AB' `
  * ` '\x4' ` is an error 

  
` \uhhhh ` |  Unicode escape, with lowercase 'u' and exactly 4 hex digits. Valid only in string literals or identifiers.  Note that the range D800-DFFF is not allowed, as these are surrogate unicode values.   
` \Uhhhhhhhh ` |  Unicode escape, with uppercase 'U' and exactly 8 hex digits. Valid only in string literals or identifiers.  The range D800-DFFF is not allowed, as these values are surrogate unicode values. Also, values greater than 10FFFF are not allowed.   
  
### Date literals

To use literal date and time values in a calculated field, you can precede the value with the appropriate marker:

Literal  |  Canonical date format  |  Sample usage   
---|---|---  
Date  |  YYYY-[M]M-[D]D  |  ` DATE '2021-4-1' `  
Date and time  |  YYYY-[M]M-[D]D [[H]H:[M]M:[S]S]  |  ` DATETIME '2021-5-29 23:59:59' `  
  
## Numeric literals

Enter numeric literals using unquoted integer or floating point values. For example:

Literal  |  Examples  |  Sample usage   
---|---|---  
Integer  |  1, -1, 0  | 

  * ` 2 + 2 `
  * ` CASE WHEN Cost > 100 THEN... `

  
Floating point  |  1.23, -1.2345  | 

  * ` SQRT(3.14) `
  * ` FLOOR(-42.123) `

  
  
## Boolean literals

Use the literal values `true` and `false` when evaluating Boolean expressions. For example:
    
    
    IF( Boolean field = true, "yes","no")
    
    IF( Boolean field = false, "no","yes")
    

**Note:** while the previous is syntactically correct, you can simplify this by referencing the boolean field's value directly:
    
    
    IF( Boolean field, "yes","no")
    
    IF(not Boolean field, "yes","no")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
