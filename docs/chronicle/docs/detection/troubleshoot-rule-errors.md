---
url: https://docs.cloud.google.com/chronicle/docs/detection/troubleshoot-rule-errors/
title: Troubleshoot detection rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:29:34.769457+00:00
---

# Troubleshoot detection rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/troubleshoot-rule-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot detection rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Runtime errors can occur during rule execution and prevent a rule from executing successfully. This document helps you troubleshoot some common runtime issues.

  * You can prevent runtime errors by testing your rules before deployment. Click **Run Test** in the rules editor—if an error is detected, follow the error link for details.

  * If an error occurs during rule execution, follow the error link on the **Detections** page for details.




## Query syntax and logic errors

These errors occur when the query structure is invalid, too complex, or uses incompatible data types.

Error message  | Underlying cause  | Resolution  | `Too many `OR` and `AND` operations` | The query contains deeply nested expressions or logic that exceeds stack space limits.  | Simplify the rule's conditions. Break down complex logic into smaller parts.  
---|---|---  
`Query is too long` | The query requires too much stack space to process.  | Split the logic into multiple rules.   
`Accessing a new field that did not exist for this time range` | The rule references a field recently added to the schema, but the rule is running over a time range where that field did not exist.  | Adjust the time range to start after the field was present. Modify the rule to handle cases where the field is null or missing.  
`Invalid subnet CIDR` | Some functions encountered an unparseable Classless Inter-Domain Routing (CIDR) range  | Check the format of CIDR ranges in the rule.   
`Invalid IP address` | Some functions encountered a malformed IP address.  | Ensure the field value contains a valid IP address format   
`Map access for reading label does not support duplicate map keys` | Some functions tried to access elements from a map-like structure (for example, additional fields) where duplicate keys exist (not allowed in the operation).  | Investigate the data source for duplicate keys. Adapt rule logic to handle this data characteristic.  
`Invalid regular expression` | The regular expression used in functions like `re.regex()` is malformed.  | Correct the regular expression syntax.  
`Invalid re.replace()` | Incorrect usage of `re.regex()`, often due to a mismatch between parenthesized subexpressions and references in the replacement string.  | Ensure the rewrite schema in `re.regex()` matches the parenthesized subexpressions in the regular expression.   
`Integer overflow in sum() aggregation` | The sum of values exceeds the maximum limit for standard integers.  | Cast the field to a floating-point type before summing (for example, use `sum(0.0 + $e.field)`).   
`Cannot complete [arithmetic/mod] operation between unsigned and signed integer` | Caused by attempting arithmetic operations (`+`, `-`, `*`, `/`, `MOD`) between different integer types.  | Use `cast.as_int()` or `cast.as_uint()` to convert one field to match the other.   
  
## Resource limits and performance errors

These errors indicate that the query is too heavy for the system to process.

Error message  | Underlying cause  | Resolution  | `Request was throttled, please try again later` | The rule requires more memory or processing power than allocated (often due to complex joins, large aggregations, or insufficient filtering).  | Add more specific filters to the events section.   
---|---|---  
`Not enough memory for aggregation` | The `aggregate_memory_limit` was exceeded.  | Optimize aggregations by reducing the number of keys in the `match` section.   
`Spilled bytes exceed limit` | The query is attempting to process too many events.  | Optimize the query by adding filters, such as by `metadata.log_type`.   
`Your query resource usage is exceeding its allocation` | The query was cancelled by the resource manager because it used too many resources.  | Optimize the query by adding filters, such as by `metadata.log_type`.   
  
## Data access and system errors

These errors are often transient or related to the backend data storage.

Error message  | Underlying Cause  | Resolution  | `Error reading files` | Temporary problems accessing underlying data.  | Retry after some time. If the error persists, contact support.   
---|---|---  
`Error reading database` | Temporary problems accessing underlying data.  | Retry after some time. If the error persists, contact support.   
`Internal error` | A transient issue within the system.  | Retry after some time. If the error persists, contact support.   
`Unknown error` | A default error message when a specific internal error code is not defined.  | Retry after some time. If the error persists, contact support.   
`Request was throttled, please try again later` | The system is under heavy load.  | Retry after some time.   
  
## Unknown runtime errors

You may encounter unknown runtime errors that lack a description. If this occurs, contact [Google SecOps Support](https://docs.cloud.google.com/chronicle/docs/getting-support).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
