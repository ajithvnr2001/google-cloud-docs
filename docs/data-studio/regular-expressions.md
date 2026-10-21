---
url: https://docs.cloud.google.com/data-studio/regular-expressions/
title: Regular expressions in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:30.111432+00:00
---

# Regular expressions in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regular-expressions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Regular expressions in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

A regular expression (regexp) is a specific sequence of characters that broadly or narrowly matches patterns in your data. You can use regular expressions to create more flexible filters in charts and controls. You can also use the following regular expression functions in calculated field formulas:

Function| Description  
---|---  
`REGEXP_CONTAINS` |  Returns true if the input value contains the regular expression pattern, otherwise returns false.  [ Learn more about `REGEXP_CONTAINS`.](https://docs.cloud.google.com/data-studio/regexpcontains)  
`REGEXP_EXTRACT` |  Returns the first matching substring in the input value that matches the regular expression pattern.  [ Learn more about `REGEXP_EXTRACT`.](https://docs.cloud.google.com/data-studio/regexpextract)  
`REGEXP_MATCH` |  Returns true if the input value matches the regular expression pattern, otherwise returns false.  [ Learn more about `REGEXP_MATCH`.](https://docs.cloud.google.com/data-studio/regexpmatch)  
`REGEXP_REPLACE` |  Replaces all occurrences of text that match the regular expression pattern in the input value with the _replacement_ string.  [ Learn more about `REGEXP_REPLACE`.](https://docs.cloud.google.com/data-studio/regexpreplace)  
  
## Alternatives to using regular expressions

Constructing regular expressions can be complex. Before using a regexp function, consider whether using a simpler text function will achieve your goal. The following functions provide regular expression-like functionality without requiring you to know regexp syntax.

Function  |  Description   
---|---  
[`CONTAINS_TEXT`](https://docs.cloud.google.com/data-studio/containstext) |  Returns true if the specified text is found in the field or expression, otherwise returns false.   
[`ENDS_WITH`](https://docs.cloud.google.com/data-studio/endswith) |  Returns true if the field or expression ends with the specified text, otherwise returns false.   
[`LEFT_TEXT`](https://docs.cloud.google.com/data-studio/lefttext) |  Returns a number of characters from the beginning of a specified string.   
[`REPLACE`](https://docs.cloud.google.com/data-studio/replace) |  Returns a copy of the original text with all occurrences of the search text substituted with the replacement text.   
[`RIGHT_TEXT`](https://docs.cloud.google.com/data-studio/righttext) |  Returns a number of characters from the end of a specified string.   
[`STARTS_WITH`](https://docs.cloud.google.com/data-studio/startswith) |  Returns true if the field or expression begins with the specified text, otherwise returns false.   
[`TRIM`](https://docs.cloud.google.com/data-studio/trim) |  Returns text with leading and trailing spaces removed.   
  
## Regular expression examples

**Matches if MyField contains space characters:**

`REGEXP_CONTAINS(MyField, "\\s+")`

**Extracts the top-level directory in a URL:**

`REGEXP_EXTRACT(URL, `^https://[^/]+/([^/]+)/`)`

For example, if the `URL` field contained this page's address, the previous function would return `looker-studio`.

Categorize ad campaigns by language:
    
    
    CASE
        WHEN REGEXP_MATCH(Campaign 2, R".*\|\s*en\s*\|.*") then "English"
        WHEN REGEXP_MATCH(Campaign 2, R".*\|\s*es\s*\|.*") then "Spanish"
        ELSE "Other language"
    END
    

For example, applying this regular expression to the _Campaign_ dimension in the Google Analytics Demo account gives these results:

Campaign  |  Language   
---|---  
Campaign #1  |  Other language   
1000549 | Google Analytics Demo | DR | apontes | NA | US | en | Hybrid | AW SEM | BKWS | ~ AW - Google Brand (US)  |  English   
1000549 | Google Analytics Demo | DR | apontes | NA | CA | es | Hybrid | AW SEM | BKWS | ~ AW - YouTube (CA)  |  Spanish   
  
**Swap the order of sections in a string:**

`REGEXP_REPLACE(Campaign, R'(.*):(.*)', R'\2 \1')`

In the previous example, the sections are separated by a colon (:).

## Metacharacters

Metacharacters are characters that have special meaning in a regular expression. Following are some of the more common metacharacters you can use. Note that these examples will open in the Google Analytics Help Center, but the information presented there applies equally to Data Studio.

**Note:** See [google/RE2 GitHub documentation](https://github.com/google/re2/wiki/Syntax) for complete regular expression syntax.

### Wildcards

Character| Description| Example  
---|---|---  
.  |  Matches any single character (letter, number, or symbol).  |  1\. matches 10, 1A 1.1 matches 111, 1A1 [Examples of matching a single character](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash)  
?  |  Matches the preceding character 0 or 1 times.  |  10? matches 1, 10  [Examples of matching a character 0 or 1 times](https://docs.cloud.google.com/data-studio/regex-example-question-plus-asterisk#question_mark)  
\+  |  Matches the preceding character 1 or more times.  |  10+ matches 10, 100  [Examples of matching character 1 or more times](https://docs.cloud.google.com/looker/doc<p></p>udio/regex-example-question-plus-asterisk#plus_sign)  
*  |  Matches the preceding character 0 or more times.  |  10* matches 1, 10, 100  [Examples of matching a character 0 or more times](https://docs.cloud.google.com/looker/doc<p></p>udio/regex-example-question-plus-asterisk#asterisk)  
|  |  Creates an OR match.  Don't use at the endan expression.  |  1|10 matches 1, 10  [Examples of creating an OR match](https://docs.cloud.google.com/looker/doc<p></p>udio/regex-example-parentheses-pipe#pipe)  
  
### Anchors

Character| Description| Example  
---|---|---  
^  |  Matches the adjacent characters at the beginning of a string.  |  ^10 matches **10** , **10** 0, **10** x  ^10 does not match 1 **10** , 1 **10** x  [Examples of matching characters after the beginning of a string](https://docs.cloud.google.com/data-studio/regex-example-caret)  
$  |  Matches the adjacent characters at the end of a string.  |  10$ matches 1 **10** , 10 **10** 10$ does not match **10** 0, **10** x  [Examples of matching characters before the end of a string](https://docs.cloud.google.com/data-studio/regex-dollar)  
  
### Groups

Character| Description| Example  
---|---|---  
( )  |  Matches the enclosed characters in exact order anywhere in a string.  Also used to group other expressions.  |  (10) matches **10** , **10** 1, **10** 11  ([0-9]|[a-z]) matches any number or lowercase letter  [Examples of grouping characters and expressions](https://docs.cloud.google.com/data-studio/regex-example-parentheses-pipe#parentheses)  
[ ]  |  Matches any one of the characters in brackets.  |  part[12] matches part1, part2  [Examples of creating a set of characters to match](https://docs.cloud.google.com/data-studio/regex-example-brackets#brackets)  
\-  |  Creates a range of characters within brackets to match anywhere in a string.  |  [0-9] matches any number 0 through 9  [Examples of matching a range of characters](https://docs.cloud.google.com/data-studio/regex-example-brackets#hyphen)  
  
### Escape

Character| Description| Example  
---|---|---  
\\\  |  Indicates that the adjacent character should be interpreted literally rather than as a regular expression metacharacter.  |  \\\ indicates that the adjacent dot should be interpreted as a period or decimal rather than as a wildcard  216\\\\.239\\\\.32\\\\.34 matches 216.239.32.34  [Examples of escaping characters](https://docs.cloud.google.com/data-studio/regex-example-dot-backslash)  
  
### Character classes

Class| Characters  
---|---  
\d  |  digits (≡ [0-9])   
\D  |  not digits (≡ [^0-9])   
\s  |  whitespace (≡ [\t\n\f\r ])   
\S  |  not whitespace (≡ [^\t\n\f\r ])   
\w  |  word characters (≡ [0-9A-Za-z_])   
\W  |  not word characters (≡ [^0-9A-Za-z_])   
  
## Tips

### Use simple expressions

Keep your regular expressions simple. Less complex expressions are easier for another user to interpret and modify.

### Case-sensitivity

Regular expressions are case-sensitive by default. You can make the match case-insensitive by using the `(?i)` flag. For example, this expression extracts both "abc123" and "ABC123":

`REGEXP_EXTRACT(MyField, '(?i)(a.*)')`

### Escaping a backslash character

If you want to write a filter condition that includes a backslash character, you need to escape the backslash character with a second backslash character.

For example, the following expression checks whether a field contains the string `green\yellow`:

`REGEXP_CONTAINS(field_name, "green\\yellow")`

You can also prepend an expression with the Raw string literal prefix, **R**. If you do this, then you don't need to escape special characters like the backslash character. The preceding example could be equivalently rewritten as follows:

`REGEXP_CONTAINS(field_name, R"green\yellow")`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
