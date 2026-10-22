---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices/
title: Apply YARA-L 2.0 rule best practices \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:35.813110+00:00
---

# Apply YARA-L 2.0 rule best practices  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply YARA-L 2.0 rule best practices

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes Google Security Operations's recommended best practices for writing rules in YARA-L 2.0.

## Filter out zero values

Fields might be automatically omitted in the events you run your rules against. When fields are omitted, they default to their zero values.

For example, an omitted string value defaults to `""`.

If you equate two fields that are both omitted, they might both default to their zero values. This might lead to unintended matches where two fields match because they both have zero values. You can avoid this behavior by explicitly specifying the zero value.

For example, if you have a rule that equates two events based on two fields, there is a chance that both of those fields are empty, causing a match:
    
    
    $e1.field1 = $e2.field2
    

If both `e1.field1` and `e2.field2` are omitted in the data, `"" = ""` is true, causing a match.

The following comparison expressions ensure that you don't get a match because `e1.field1` and `e2.field2` don't include any data:
    
    
     $e1.field1 = $e2.field2
     $e1.field != ""
    

### Zero values and enrichment-dependent rules

If a rule depends on enriched data it hasn't been updated yet, the value might be null or zero. Therefore, it is good practice to filter out zero values (null checks) on enrichment-dependent rules. Learn [how Google SecOps enriches event and entity data](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment) and [how to use context-enriched data in rules](https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules).

**Note:** Zero values are filtered out from match variables by default. For more information, see [zero value handling in the match section](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax#zero-values-in-match-section).

## Add an event type filter

In the following example, the IP addresses for each UDM event are checked against the reference list, consuming a lot of resources:
    
    
    events:
    // For every UDM event, check if the target.ip is listed in
    // the suspicious_ip_addresses reference list.
    $e.target.ip in %suspicious_ip_addresses
    

If your YARA-L rule only detects on UDM events of a certain event type, adding an event type filter can help to optimize your rule by reducing the number of events the rule needs to evaluate.
    
    
    events:
    // For every UDM event of type NETWORK_DNS, check if the target.ip is
    // listed in the suspicious_ip_addresses reference list.
    $e.metadata.event_type = "NETWORK_DNS"
    $e.target.ip in %suspicious_ip_addresses
    

Add these filters to the beginning of the events section. You should also put equality filters before regular expression or other comparisons. Filters are applied in the order they appear in the rule.

For Community blogs on working with YARA-L, see:

  * [YARA-L basics](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-basics/ta-p/635468)
  * [YARA-L rule variables](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-rule-variables/ta-p/635481)
  * [YARA-L operators and modifiers](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-know-Google-SecOps-SIEM-YARA-L-operators-and/ta-p/635489)
  * [Building a single event rule using a regular expression](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Building-a-single-event-rule/ta-p/635498)
  * [Aggregating events in rules](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Aggregating-events-in-rules/ta-p/635507)
  * [Setting a threshold in conditions](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Setting-a-threshold-in/ta-p/635521)
  * [Rules editor navigation](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-SIEM-Rules-Editor-Navigation/ta-p/659309)
  * [YARA-L Rule Options](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-YARA-L-Rule-Options/ta-p/659313)
  * [Building a Single Event Rule - String Match](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-SIEM-Building-a-Single-Event-Rule/ta-p/659317)
  * [Building a Multi Event Rule - Joining Events](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-Building-a-Multi-Event-Rule-Joining/ta-p/665140)
  * [Building a Multi Event Rule - Ordering Events](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Building-a-Multi-Event-Rule/ta-p/677993)
  * [Building a Multi Event Rule - Multiple Joins and Counts in Conditions](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-Building-a-Multi-Event-Rule-Multiple/ta-p/683984)
  * [Building a Multi Event Rule - Sliding Windows](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Building-a-Multi-Event-Rule/ta-p/693405)
  * [Introducing Outcomes in a Single Event Rule](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-Introducing-Outcomes-in-a-Single-Event/ta-p/699600)
  * [Outcomes in a Multi Event Rule - Counts](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Outcomes-in-a-Multi-Event-Rule/ta-p/703096)
  * [Outcomes in Multi Event Rules - Arrays](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-SIEM-Outcomes-in-Multi-Event-Rules/ta-p/705657)
  * [Outcomes in a Multi Event Rule - Max, Min, Sum](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Outcomes-in-a-Multi-Event-Rule-Max/ta-p/709795)
  * [Outcomes - Risk Score, Conditional Logic and Mathematical Operators](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Chronicle-Outcomes-Risk-Score-Conditional-Logic/ta-p/714517)
  * [Functions - strings.concat](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Functions-strings-concat/ta-p/719344)
  * [Functions - strings.coalesce](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Functions-strings-coalesce/ta-p/726303)
  * [Functions - Network](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Functions-Network/ta-p/732001)
  * [Reference List](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Reference-List/ta-p/738238)
  * [CIDR Reference Lists](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-CIDR-Reference-Lists/ta-p/745365)
  * [Regex Reference Lists](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Regex-Reference-Lists/ta-p/750396)
  * [Strings Function - Upper or Lower Case](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Strings-Function-Upper-Lower-Case/ta-p/750408)
  * [Regular Expression Function - re.regex](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Regular-Expression-Function-re/ta-p/768660)
  * [Regular Expression Function - re.capture](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Regular-Expression-Function-re/ta-p/775278)
  * [String Function - strings.base64_decode](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-String-Function-strings-base64/ta-p/783968)
  * [Regular Expression Function - re.replace](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Regular-Expression-Function-re/ta-p/791965)
  * [Getting started with Statistical Search](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Getting-Started-with-Statistical/ta-p/799951)
  * [Statistical Search - More Than a Count](https://www.googlecloudcommunity.com/gc/Google-Security-Operations-Best/Getting-to-Know-Google-SecOps-Statistical-Search-More-Than-a/ta-p/803150)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
