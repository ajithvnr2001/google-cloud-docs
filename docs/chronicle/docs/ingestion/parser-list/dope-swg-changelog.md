---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dope-swg-changelog/
title: Change log for DOPE_SWG \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:44.581852+00:00
---

# Change log for DOPE_SWG  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dope-swg-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DOPE_SWG

Date | Changes  
---|---  
2025-03-12 |  Enhancement:  
\- Added support for Json logs.  
\- Mapped `schemaVersion` to `metadata.product_version`.  
\- Mapped `destination.matchedDestination` to `target.ip` and `target.asset.ip` if it's an IP address.  
\- Mapped `destination.matchedDestination` to `target.hostname` and `target.asset.hostname` if it's not an IP address.  
\- Mapped `destination.url` to `target.url`.  
\- Mapped `destination.destinationIP` to `target.ip` and `target.asset.ip` if it's an IP address.  
\- Mapped `endpoint.tenantID` to `principal.asset.attribute.cloud.project.id`.  
\- Mapped `endpoint.agentID` to `principal.asset.asset_id` with a `DS:` prefix.  
\- Mapped `endpoint.user` to `principal.user.userid`.  
\- Mapped `endpoint.deviceName` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `endpoint.oidcUser` to `principal.user.email_addresses` if it's an email address.  
\- Mapped `endpoint.oidcUser` to `principal.user.user_display_name` if it's not an email address.  
\- Mapped `bandwidth.dataSentInBytes` to `network.sent_bytes`.  
\- Mapped `bandwidth.dataReceivedInBytes` to `network.received_bytes`.  
\- Mapped `policy.verdict` to `security_result.action` (mapping `1` to `BLOCK`, `0` to `ALLOW`, and `2` to `CHALLENGE`).  
\- Mapped `policy.policyType` to `security_result.rule_type`.  
\- Mapped `policy.policyName` to `security_result.rule_name`.  
\- Mapped `policy.categories` to `additional.fields` as a list with key `policy_categories_values`.  
\- Mapped `request.duration` to `network.session_duration.seconds`.  
\- Mapped `request.httpVersion` to `network.http.user_agent`.  
\- Mapped `request.processName` to `principal.process.command_line`.  
\- Mapped `request.processTree` to `additional.fields` as a list with key `request_processTree_values`.   
2023-05-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
