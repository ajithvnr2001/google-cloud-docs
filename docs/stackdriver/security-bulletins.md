---
url: https://docs.cloud.google.com/stackdriver/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:07.212007+00:00
---

# Security bulletins  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes all security bulletins related to Google Cloud Observability.

## GCP-2026-039

**Published** : 2026-06-22

Description | Severity | Notes  
---|---|---  
A vulnerability in Cloud Logging could have allowed attackers to hijack log sink destinations by recreating the target Cloud Storage bucket in a project controlled by the attacker. This issue could have resulted in the continuous routing of sensitive logs to an unauthorized third party. **What should I do?** No action is required. Cloud Logging has been updated to remediate this vulnerability. Consequently, log sinks will now return an error if the parent project of a destination Cloud Storage bucket has changed since the initial configuration. To restore log exports, users must delete and recreate the affected log sink. As a best practice, users should always delete associated log sinks before removing the destination resource to avoid dangling sinks. **What vulnerabilities are being addressed?** The vulnerability could allow an opportunistic attacker to compromise log exports configured for Cloud Storage. Cloud Logging sinks previously relied solely on the globally unique Cloud Storage bucket name to route logs. This could allow a malicious actor to recreate a deleted bucket of the same name in a project controlled by the attacker. An active log sink would then automatically resume exports, routing sensitive logs to the attacker's bucket and resulting in unauthorized continuous data exfiltration. To execute this attack the malicious actor needed to know the name of the destination Cloud Storage bucket in advance and the Cloud Storage bucket needed to be deleted. The implemented fix mitigates this vulnerability by ensuring the destination bucket resides within the same parent project that was configured when the sink was initially created. Cloud Logging now continually performs this check while it writes log data to the Cloud Storage bucket. | Medium |   
  
## GCP-2026-009

**Published** : 2026-02-13

Description | Severity | Notes  
---|---|---  
Observability Analytics user interface versions prior to January 2026 can be configured to automatically execute SQL queries. A vulnerability can allow an attacker to craft a query URL which, when opened by someone with credentials, could access table contents or incur query cost. **What should I do?** No user action is needed. The vulnerability was patched, and the affected user interfaces were updated in January 2026 to include intervention points to prevent malicious SQL from running without an opportunity for the user to inspect it. **What vulnerabilities are being addressed?** The vulnerability can allow an attacker to access limited contents of a target's Observability Analytics or BigQuery tables when the target executes an attacker-crafted SQL query. The vulnerability leverages BigQuery audit logs to convey information about the target's table contents to an attacker-controlled Google Cloud project. The vulnerability is exacerbated by the Observability Analytics interfaces behavior of automatically executing queries embedded in the URL, which prevents the target from inspecting the attacker-crafted query prior to executing it with their credentials. | High |   
  
## GCP-2026-005

**Published** : 2026-01-28

Description | Severity | Notes  
---|---|---  
This vulnerability affects Observability Analytics interface and Cloud Monitoring dashboarding interface versions prior to January 2026. **What should I do?** No user action is needed. The affected user interfaces were updated in January 2026 to include intervention points to prevent malicious SQL from running without an opportunity for the user to inspect it. **What vulnerabilities are being addressed?** The vulnerability allows an attacker to access limited contents of a target's Observability Analytics or BigQuery tables when the target views an attacker-crafted dashboard. The vulnerability leverages BigQuery metadata channels to convey information about the target's table contents to an attacker-controlled Google Cloud project. The vulnerability is exacerbated by the dashboard interfaces behavior of automatically executing queries to populate SQL-backed widgets, which prevents the target from inspecting the attacker-crafted query prior to executing it with their credentials. | High |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
