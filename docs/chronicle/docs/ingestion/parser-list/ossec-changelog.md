---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ossec-changelog/
title: Change log for OSSEC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:11:01.031358+00:00
---

# Change log for OSSEC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ossec-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OSSEC

Date | Changes  
---|---  
2024-04-24 |  Added support of `ossec-testrule` and `ossec-analysisd` application logs not having `event_source` path.   
2024-02-14 |  Updated UDM mapping of the `logName` and `protoPayload.response.selfLinkWithId` raw log fields.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2022-09-28 |  Migrated parser to default parser.  
Below are the field mapping differences:  
1\. For event source /var/log/syslog:  
\- updated mappings for commad_line from src.process.command_line to principal.process.command_line.  
\- updated mappings for pid from src.process.pid to principal.process.pid.  
2\. For event source /var/log/apache2/error.log:  
\- updated mappings for pid from target.process.pid to target.process.parent_process.pid.  
\- updated mappings for tid from target.resource.product_object_id to target.process.pid.  
3\. For event source /var/log/nginx/access.log:  
-updated mappings for path from target.url to principal.resource.name.  
4\. For event source /var/log/nginx/error.log:  
\- updated mappings for resource_name from target.url to principal.resource.name.  
5\. For event source /var/ossec/logs/ossec.log:  
\- updated mappings for hostname from principal.hostname to target.hostname.  
6\. For event source /var/log/auth.log:  
\- updated mappings for description from metadata.description to security_result.description.  
7\. For event source /var/log/audit.log:  
\- Removed conditional stanza to map metadata.event_type with USER_UNCATEGORIZED, if principal.ip is not present for type USER_ACCT.  
8\. For event source /var/log/audit.log:  
\- Removed conditional stanza to map metadata.event_type with USER_RESOURCE_ACCESS, if principal.ip is not present for type SERVICE_START,SERVICE_STOP.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
