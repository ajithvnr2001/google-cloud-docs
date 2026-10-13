---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/replace_all_regex/
title: Function: text.replace_all_regex \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:28.482544+00:00
---

# Function: text.replace_all_regex  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/replace_all_regex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.replace_all_regex Stay organized with collections  Save and categorize content based on your preferences. 

Replaces all matches of a regular expression with a new string.

In the case of overlapping matches, the leftmost instance is replaced and if multiple matches start at the same index, then the longest one is replaced. If the expression is empty, it matches at the beginning of the string and after each code point, yielding up to `k+1` replacements for a string with `k` code points.

Note that regular expression backreferences are not supported and you can't refer to text previously matched by a capturing group.

## Arguments

Arguments  
---  
`source` |  `string` The subject of the function. A modified copy is returned.  
`regexp` |  `string` The regular expression used for matching substrings. Uses [RE2 syntax](https://github.com/google/re2/wiki/Syntax).  
`repl` |  `string` The string that will replace all matches of `regexp`. Backreferences are not supported. For example, you can't use the expression `\1` to refer to text previously matched by a capturing group.  
  
## Returns

A copy of `source` where all matches of `regexp` are replaced by `repl`.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `source`, `regexp`, or `repl` is not a string.  
`ValueError` | If either `regexp` or `repl` is not UTF-8 encoded or if `regexp` is an invalid regular expression.  
  
## Examples
    
    
    # Replace matches of regular expression; returns "three three"
    - returnStep:
        return: ${text.replace_all_regex("one two", "one|two", "three")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
