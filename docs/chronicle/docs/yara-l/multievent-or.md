---
url: https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-or/
title: Use or in the condition section \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:27.147456+00:00
---

# Use or in the condition section  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-or/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use or in the condition section

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to use the `or` operator to write flexible and concise detection logic within the `condition` section of your query.

Using `or` between event or placeholder variables lets you combine multiple conditions, reducing the overall complexity of your query syntax:

  * Checks for the presence of either of the specified variables. For example, `$e1 or $e2` requires at least one instance of `$e1` or one instance of `$e2`.



## `or` syntax in condition section

Use the `or` keyword directly between variables. The following example is equivalent of `COUNT($e1)>0 or COUNT($e2)>0`:
    
    
    condition:
      $e1 or $e2  // True if $e1 exists or $e2 exists
    

## Example rule: risky IP or bad hash execution

The following example rule detects a threat if a process launch from a risky IP address is detected or a known bad hash is executed:
    
    
    rule MultiEventOr {
      meta:
        author = "google-secops"
      events:
        $e1.principal.ip = "1.1.1.1"
        $e1.metadata.event_type = "PROCESS_LAUNCH"
        $e2.target.file.sha256 = "badhash..."
        $user = $e1.principal.user.userid
        $user = $e2.principal.user.userid
      match:
        $user over 5m
      condition:
        $e1 or $e2
    }
    

## Example search: risky IP or bad hash execution

The following example shows how you could reformat the example rule as a search query.

**Note:** You must specify `event` variables when using a multi-event `or` in the `condition` section.
    
    
    $e1.principal.ip = "1.1.1.1"
    $e1.metadata.event_type = "PROCESS_LAUNCH"
    $e2.target.file.sha256 = "badhash..."
    $user = $e1.principal.user.userid
    $user = $e2.principal.user.userid
    
    match:
      $user over 5m
    
    condition:
      $e1 or $e2
    

## Known limitations

  * **Resource consumption** : When you use `or` between event variables, it consumes more resources than using `and` and can result in longer query execution times.

  * **Event variable limit** : For Search and Dashboards, you can use maximum of 3 events in multi-event `or` syntax. For Rules, you can use maximum of 2 events in multi-event `or` syntax.

  * **Required event existence** : Expressions using `or` can't be unbounded. The existence of the event must be a requirement for the clause to be true (for example, `$e1` or `#e1 > 0`).

  * **Variable type mixing** : You can't combine non-UDM variables with UDM event variables within the same `or` list.

  * **Window restriction** : You can't use tumbling windows with `or` syntax.




## What's next?

  * [Condition section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/condition-syntax)
  * [Use N OF syntax with event variables](https://docs.cloud.google.com/chronicle/docs/yara-l/multievent-n-of)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
