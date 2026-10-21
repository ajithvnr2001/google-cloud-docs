---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-last_non_null/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:37:29.929763+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-last_non_null/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.last_non_null

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.last_non_null(order_by_expression, value_expression)
    

#### Description

Returns the last non-null value of `value_expression` within a window, ordered by the `order_by_expression` (which must be an integer, typically a timestamp). This function is used in aggregate queries, often within a `match` window. In YARA-L rules, it is used in the `outcome` section of multi-event rules and cannot be used in the `events` or `match` sections. It can also be used in Search and Dashboard queries for aggregations. **Use Case:**

This function is particularly useful when you need to find the most recent known value of a field that is not always populated across all events. For example, if you are grouping events by an asset ID, and only some events contain the asset's hostname, you can use `window.last_non_null` ordered by the event timestamp to find the most recently seen non-null hostname for that asset within the window.

#### Param data types

`INT`, `STRING`

#### Return type

`STRING`

#### Code samples

The following examples demonstrate how to use `window.last_non_null`.

##### Example 1

This example groups events by IP address over a 5-minute window and uses `window.last_non_null` to find the most recent non-null hostname, ordered by the event timestamp.
    
    
        $e.principal.ip = $ip
        $ip != ""
    
        // Conceptual events for a given $ip within a window:
        // { time: 10, host: "hostA" }
        // { time: 20, host: null    }
        // { time: 30, host: "hostB" } // last_non_null should pick this
        // { time: 40, host: null    }
    
      match:
        $ip over 5m
    
      outcome:
        // Orders by $e.metadata.event_timestamp.seconds, returns $e.principal.hostname
        // from the latest event where hostname is not null.
        $last_hostname = window.last_non_null($e.metadata.event_timestamp.seconds, $e.principal.hostname)
        $event_count = count($e.metadata.id)
    
      condition:
        $e
    

##### Example 2

This example skips over events with NULL values at the end of the time window to find the last actual non-null value. We'll group by principal.asset_id.
    
    
        $e.principal.asset_id = $asset_id
        $asset_id != ""
    
        // Conceptual events for a given $asset_id within a window:
        // { time: 10, user: "userA" }
        // { time: 20, user: "userB" } // This should be selected
        // { time: 30, user: null }
        // { time: 40, user: null }
    
      match:
        $asset_id over 5m
    
      outcome:
        // $last_user is expected to be "userB" based on the conceptual events.
        $last_user = window.last_non_null($e.metadata.event_timestamp.seconds, $e.principal.user.userid)
        $event_count = count($e.metadata.id)
    
      condition:
        $e
    

##### Example 3

This example will return the value from the event with the highest timestamp.
    
    
        $e.principal.asset_id = $asset_id
        $asset_id != ""
    
        // Conceptual events for a given $asset_id within a window:
        // { time: 10, user: "userA" }
        // { time: 20, user: "userB" }
        // { time: 30, user: "userC" } // This should be selected
    
      match:
        $asset_id over 5m
    
      outcome:
        // $last_user is expected to be "userC"
        $last_user = window.last_non_null($e.metadata.event_timestamp.seconds, $e.principal.user.userid)
        $event_count = count($e.metadata.id)
    
      condition:
        $e
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
