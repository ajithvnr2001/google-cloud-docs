---
url: https://docs.cloud.google.com/chronicle/docs/yara-l/meta-syntax/
title: Meta section syntax \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:06.006530+00:00
---

# Meta section syntax  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/yara-l/meta-syntax/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Meta section syntax

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

The `meta` section of a YARA-L rule is required and must appear at the start of the query.

**Note:** The `meta` section is not used in search or dashboard queries.

This section can include multiple lines, where each line defines a key-value pair. The `key` is a string value without quotes, and the `value` is a string with quotes, such as: `<key> = "<value>"`

For example:
    
    
    rule failed_logins_from_new_location {
      meta:
       author = "Security Team"
       description = "Detects multiple failed logins for a user from a new, never-before-seen IP address within 10 minutes."
       severity = "HIGH"
    
      ... rest of the rule ...
    }
    

## What's next

  * [Events section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/events-syntax)
  * [Match section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax)
  * [Outcome section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/outcome-syntax)
  * [Condition section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/condition-syntax)
  * [Options section syntax](https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax)



## Additional information

  * [Expressions, operators, and constructs used in YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/expressions)
  * [Functions in YARA-L 2.0](https://docs.cloud.google.com/chronicle/docs/yara-l/functions)
  * [Build composite detection rules](https://docs.cloud.google.com/chronicle/docs/yara-l/composite-detection-rules)
  * [Examples: YARA-L 2.0 queries](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
