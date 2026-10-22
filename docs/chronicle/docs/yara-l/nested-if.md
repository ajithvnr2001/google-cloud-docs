---
url: https://docs.cloud.google.com/chronicle/docs/yara-l/nested-if/
title: Use nested if statements for more complex logic \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:29.184397+00:00
---

# Use nested if statements for more complex logic  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/yara-l/nested-if/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use nested if statements for more complex logic

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can use `if` statements in both the `outcome` and `events` sections. You can also use `if` statements within the `then` `else` clauses of another `if` statement. This capability lets you introduce more complicated logic to your query.

This syntax is supported in Rules, Search, and Dashboards.

## Syntax
    
    
    if(BOOL_CLAUSE, THEN_CLAUSE, ELSE_CLAUSE)
    

## Nested `if` examples

### Search example: outcome section

This example assigns an outcome score based on `principal.hostname`.
    
    
    $nested_if.principal.hostname != ""
    outcome:
        $score = max(
            if($nested_if.principal.hostname = /win-adfs/,
               5,
              if($nested_if.principal.hostname = /server/,
                 3,
                if($nested_if.principal.hostname = /win-atomic/,
                   1,
                   0))))
    

### Search example: events section

This example assigns the placeholder IP to `target.ip` or `principal.ip` so long as they're non-empty. If the IP values are missing, it assigns `no_valid_ip`.
    
    
    events:
        $e.metadata.event_type = "NETWORK_CONNECTION"
        $ip = if($e.target.ip != "",
                $e.target.ip,
                if($e.principal.ip != "",
                  $e.principal.ip,
                  "no_valid_ip"))
    match:
       $ip
    

### Rule example: nested `if` in `outcome` section
    
    
    rule nested_if_outcome_example {
    meta:
    
    events:
        $e.metadata.event_type = "NETWORK_CONNECTION"
        $e.principal.ip = $ip
    match:
       $ip over 5m
    outcome:
        $score = max(
            if($e.principal.hostname = /win-adfs/,
               5,
              if($e.principal.hostname = /server/,
                 3,
                if($e.principal.hostname = /win-atomic/,
                   1,
                   0))))
      condition:
        $e
    }
    

### Rule example: nested `if` in `events` section
    
    
    rule nested_if_events_example {
    
    meta:
    
    events:
        $e.metadata.event_type = "NETWORK_CONNECTION"
        $ip = if($e.target.ip != "",
                $e.target.ip,
                if($e.principal.ip != "",
                  $e.principal.ip,
                  "no_valid_ip"))
    match:
       $ip over 5m
    
      condition:
        $e
    }
    

## Known limitation

The `if()` statement is a function in YARA-L 2.0 and subject to the function depth limit of 20.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
