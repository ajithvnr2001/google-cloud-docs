---
url: https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax/
title: Options section syntax \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:26.220791+00:00
---

# Options section syntax  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Options section syntax

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The `options` section of a YARA-L query is only available for Rules.

You can specify options using the syntax `key = value`, where `key` must be a predefined option name and `value` must be a valid value for the option:
    
    
    rule RuleOptionsExample {
      // Other rule sections
    
      options:
        allow_zero_values = true
    }
    

## Options values

The following values for options are available:

  * allow_zero_values

  * suppression_window




### allow_zero_values option

The valid values for `allow_zero_values` option are `true` and `false` (default), which determine if the option is enabled or not. The `allow_zero_values` option is disabled if it's not specified in the query.

To enable the `allow_zero_values` setting, add the following to the `options` section of your query: `allow_zero_values = true`

This action prevents the query from implicitly filtering out the zero values of placeholders that are used in the `match` section, as described in [Zero values in match section](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax#zero-values-in-match-section).

### suppression_window option

The `suppression_window` option provides a scalable mechanism to control alert volume and deduplicate findings, particularly for users who move from Splunk (and other platforms) that utilize similar alert-throttling capabilities.

The `suppression_window` uses a tumbling window approach—a fixed-size, non-overlapping window that suppresses duplicate detections. You can optionally provide a `suppression_key` to further refine which query instances are suppressed within the `suppression window`. The deduplication key (`suppression_key`), the specific data point the system looks at to decide if an event is a duplicate, varies by rule type:

  * [Single-event queries](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#single-event-rule) use an `outcome` variable named `suppression_key` to define the deduplication scope. If you don't specify a `suppression_key`, all query instances are suppressed globally during the window. 

**Note:** The `suppression_window` option doesn't work when testing a rule using [**Run test**](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules#test_your_rule). Suppression is a post-processing step that takes place only after detections have been written.

#### Example: suppression window option for single-event queries

In the following example, `suppression_window` is set to `5m` and `suppression_key` is set to the `$hostname` variable. After the query triggers a detection for `$hostname`, any further detections for `$hostname` are suppressed for the next five minutes. However, if the query triggers on an event with a different hostname, a detection is created.
    
    
    rule SingleEventSuppressionWindowExample {
      // Other rule sections
    
      outcome:
        $suppression_key = $hostname
    
      options:
        suppression_window = 5m
    }

  * [Multiple event queries](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#multiple-event-rule) use the variables defined in the `match` section to determine what should be suppressed. The `suppression_window` value must also be greater than the `match` window.



#### Example: suppression window option for multiple-event queries

In the following example, `suppression_window` is set to `1h`. After the query triggers a detection for (`$hostname`, `$ip`) over a `10m` window, any further detections for (`$hostname`, `$ip`) are suppressed for the next hour. However, if the query triggers on events with a different combination, a detection is created.
    
    
    rule MultipleEventSuppressionWindowExample {
      // Other rule sections
    
      match:
        $hostname, $ip over 10m
    
      options:
        suppression_window = 1h
    }

**Note:** The default value of `suppression_window` is `0`; that is, the `suppression window` is disabled by default.

## Additional information

  * [Expressions, operators, and constructs used in YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/expressions)
  * [Functions in YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/functions)
  * [Build composite detection rules](https://docs.cloud.google.com/chronicle/docs/yara-l/composite-detection-rules)
  * [Examples: YARA-L 2.0 queries](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
