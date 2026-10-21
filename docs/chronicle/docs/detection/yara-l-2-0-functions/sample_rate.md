---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/sample_rate/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:13:57.928370+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/sample_rate/




Stay organized with collections  Save and categorize content based on your preferences. 

### sample_rate

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    optimization.sample_rate(byteOrString, rateNumerator, rateDenominator)
    

#### Description

This function determines whether to include an event based on a deterministic sampling strategy. This function returns: 

  * `true` for a fraction of input values, equivalent to (`rateNumerator` / `rateDenominator`), indicating that the event should be included in the sample.
  * `false` indicating that the event shouldn't be included in the sample. 



This function is useful for optimization scenarios where you want to process only a subset of events. Equivalent to:
    
    
    hash.fingerprint2011(byteOrString) % rateDenominator < rateNumerator
    

#### Param data types

  * byteOrString: Expression that evaluates to either a `BYTE` or `STRING`.
  * rateNumerator: 'INT'
  * rateDenominator: 'INT' 



#### Return type

`BOOL`

#### Code sample
    
    
    events:
        $e.metadata.event_type = "NETWORK_CONNECTION"
        $asset_id = $e.principal.asset.asset_id
        optimization.sample_rate($e.metadata.id, 1, 5) // Only 1 out of every 5 events
    
      match:
        $asset_id over 1h
    
      outcome:
        $event_count = count_distinct($e.metadata.id)
      // estimate the usage by multiplying by the inverse of the sample rate
        $usage_past_hour = sum(5.0 * $e.network.sent_bytes)
    
     condition:
      // Requiring a certain number of events after sampling avoids bias (e.g. a
      // device with just 1 connection will still show up 20% of the time and
      // if we multiply that traffic by 5, we'll get an incorrect estimate)
      $e and ($usage_past_hour > 1000000000) and $event_count >= 100
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
