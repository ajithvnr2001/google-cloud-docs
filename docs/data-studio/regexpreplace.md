---
url: https://docs.cloud.google.com/data-studio/regexpreplace/
title: REGEXP_REPLACE \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:58.185944+00:00
---

# REGEXP_REPLACE  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regexpreplace/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  REGEXP_REPLACE Stay organized with collections  Save and categorize content based on your preferences. 

Replaces text within the target value.

## Sample usage

`REGEXP_REPLACE(Campaign, '(Sale):(Summer)', '\\2 \\1')`

## Syntax

`REGEXP_REPLACE(X, regular_expression, replacement)`

### Parameters

  * `X` \- a field or expression that includes a field.
  * `regular_expression` \- a regular expression that matches a portion of `X`.
  * `replacement` \- the text with which to replace the matched portion of `field_expression`.`



### Returns

The `REGEXP_REPLACE` function returns **Text** values.

### Notes

`REGEXP_REPLACE` returns text where all substrings of `X` that match `regular_expression` are replaced with _X_.

You can use backslashed-escaped digits (\1 to \9) within the `replacement` argument to insert text matching the corresponding parenthesized group in the `regular_expression` pattern. Use \0 to refer to the entire matching text.

To search for a literal backslash in your regular expression, you must escape the literal backslash with a second backslash. For example:

`REGEXP_REPLACE('abc', 'b(.)', 'X\\1');`

returns `aXc`.

You can also use [raw strings](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/lexical#string_and_bytes_literals) to remove one layer of escaping. For example:

`REGEXP_REPLACE('abc', 'b(.)', r'X\1');`

The `REGEXP_REPLACE` function only replaces non-overlapping matches. For example, replacing `ana` within `banana` results in only one replacement, not two.

## Examples

Example formula | Input | Output  
---|---|---  
` REGEXP_REPLACE(LOWER(Campaign), ".bc123", "Summer Sale") ` |  abc123  |  Summer Sale   
` REGEXP_REPLACE(LOWER(Campaign), ".bc123", "Summer Sale") ` |  BBC123  |  Summer Sale   
` REGEXP_REPLACE(Campaign, '(.*):(.*)', '\\2 \\1') ` |  Sale:Summer  |  Summer Sale   
` REGEXP_REPLACE(Campaign, '(.*):(.*)', '\\2 \\1') ` |  Sale:Winter  |  Winter Sale   
  
## Related resources

  * [Regular expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
