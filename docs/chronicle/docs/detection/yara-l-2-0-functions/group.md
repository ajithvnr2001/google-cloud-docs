---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/group/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:43:08.806264+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/group/




Stay organized with collections  Save and categorize content based on your preferences. 

### group

Supported in:

[ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    group(field1, field2, field3, ...)
    

#### Description

Group fields of a similar type into a placeholder variable.

In UDM search, [grouped fields](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#search_grouped_fields) are used to search across multiple fields of a similar type. The group function is similar to grouped fields except that it lets you select which fields you want grouped together to trigger a detection. You can use the group function for gathering information about a specific entity (for example, a hostname, IP address, or userid) across different [Noun types](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#noun).

**Note:** For search, you can use grouped fields in the `events` section, but not in the `match` and `outcome` sections. For more details, [`events` section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/events-syntax), [`match` section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax), and [`outcome` section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax).

  * Parameter type: `Event type`

  * Return type: `Grouped event fields`




#### Code samples

**Example: Aggregate and count IP addresses**

Group all IP addresses together and provide a descending count of the most prevalent IP addresses in the time range scanned.
    
    
    $ip = group(principal.ip, about.ip, target.ip)
    $ip != ""
    match:
      $ip
    
    outcome:
      $count = count_distinct(metadata.id)
    
    order:
      $count desc
    

**Example: Count distinct events for each IP address**

In the following example, the `group()` function gathers all the IP addresses found in the `principal.ip`, `target.ip`, and `src.ip` fields across all events that triggered the detection. The IP addresses are then added to the placeholder variable `$ip`. The rule then matches the IP address and returns a count of distinct events for each unique IP address.
    
    
    $ip = group(detection.collection_elements.references.event.principal.ip, detection.collection_elements.references.event.target.ip, detection.collection_elements.references.event.src.ip)
    $ip != ""
    
    match:
      $ip
    
    outcome:
      $count = count_distinct(detection.id)
    
    order:
      $count desc
    
    // Detection1: principal.ip = 1.1.1.1
    // Detection2: src.ip = 1.1.1.1, target.ip = 2.2.2.2
    // Detection3: target.ip = 1.1.1.1
    // Detection4: principal.ip = 2.2.2.2
    

Result:

`$ip` | `$count`  
---|---  
1.1.1.1 | 3  
2.2.2.2 | 2  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
