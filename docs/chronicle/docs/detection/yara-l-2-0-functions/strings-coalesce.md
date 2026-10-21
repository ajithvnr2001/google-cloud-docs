---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-coalesce/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:34:10.931349+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-coalesce/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.coalesce

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.coalesce(a, b, c, ...)
    

#### Description

This function takes an unlimited number of arguments and returns the value of the first expression that does not evaluate to an empty string (for example, "non-zero value"). If all arguments evaluate to an empty string, the function call returns an empty string.

The arguments can be literals, event fields, or function calls. All arguments must be of `STRING` type. If any arguments are event fields, the attributes must be from the same event.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

The following example includes string variables as arguments. The condition evaluates to true when (1) `$e.network.email.from` is `suspicious@gmail.com` or (2) `$e.network.email.from` is empty and `$e.network.email.to` is `suspicious@gmail.com`.
    
    
    "suspicious@gmail.com" = strings.coalesce($e.network.email.from, $e.network.email.to)
    

##### Example 2

The following example calls the `coalesce` function with more than two arguments. This condition compares the first non-null IP address from event `$e` against values in the reference list `ip_watchlist`. The order that the arguments are coalesced in this call is the same as the order they are enumerated in the rule condition:

  1. `$e.principal.ip` is evaluated first.
  2. `$e.src.ip` is evaluated next.
  3. `$e.target.ip` is evaluated next.
  4. Finally, the string "No IP" is returned as a default value if the previous `ip` fields are unset.


    
    
    strings.coalesce($e.principal.ip, $e.src.ip, $e.target.ip, "No IP") in %ip_watchlist
    

##### Example 3

The following example attempts to coalesce `principal.hostname` from event `$e1` and event `$e2`. It will return a compiler error because the arguments are different event variables.
    
    
    // returns a compiler error
    "test" = strings.coalesce($e1.principal.hostname, $e2.principal.hostname)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
