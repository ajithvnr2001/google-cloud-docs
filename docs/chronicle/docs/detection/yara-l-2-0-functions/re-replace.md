---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-replace/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:28.575154+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-replace/




Stay organized with collections  Save and categorize content based on your preferences. 

### re.replace

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    re.replace(stringText, replaceRegex, replacementText)
    

#### Description

Performs a regular expression replacement.

This function takes three arguments:

  * `stringText`: the original string.
  * `replaceRegex`: the regular expression indicating the pattern to search for.
  * `replacementText`: The text to insert into each match.



Returns a new string derived from the original `stringText`, where all substrings that match the pattern in `replaceRegex` are replaced with the value in `replacementText`. You can use backslash-escaped digits (`\1` to `\9`) within `replacementText` to insert text matching the corresponding parenthesized group in the `replaceRegex` pattern. Use `\0` to refer to the entire matching text.

The function replaces non-overlapping matches and will prioritize replacing the first occurrence found. For example, `re.replace("banana", "ana", "111")` returns the string "b111na".

#### Param data types

`STRING`, `STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example captures everything after the `@` symbol in an email, replaces `com` with `org`, and then returns the result. Notice the use of nested functions.
    
    
    "email@google.org" = re.replace($e.network.email.from, "com", "org")
    

##### Example 2

This example uses backslash-escaped digits in the `replacementText` argument to reference matches to the `replaceRegex` pattern.
    
    
    "test1.com.google" = re.replace(
                           $e.principal.hostname, // holds "test1.test2.google.com"
                           "test2\.([a-z]*)\.([a-z]*)",
                           "\\2.\\1"  // \\1 holds "google", \\2 holds "com"
                         )
    

##### Example 3

Note the following cases when dealing with empty strings and `re.replace()`:

Using empty string as `replaceRegex`:
    
    
    // In the function call below, if $e.principal.hostname contains "name",
    // the result is: 1n1a1m1e1, because an empty string is found next to
    // every character in `stringText`.
    re.replace($e.principal.hostname, "", "1")
    

To replace an empty string, you can use `"^$"` as `replaceRegex`:
    
    
    // In the function call below, if $e.principal.hostname contains the empty
    // string, "", the result is: "none".
    re.replace($e.principal.hostname, "^$", "none")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
