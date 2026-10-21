---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-control-tower-changelog/
title: Change log for AWS_CONTROL_TOWER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:04:10.814484+00:00
---

# Change log for AWS_CONTROL_TOWER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-control-tower-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_CONTROL_TOWER

Date | Changes  
---|---  
2026-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `req.sharedEventID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `req.eventVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `req.additionalEventData.bytesTransferredIn` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `req.additionalEventData.bytesTransferredOut` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `req.tlsDetails.clientProvidedHostHeader` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `req.userIdentity.sessionContext.sessionIssuer.arn` and `req.userIdentity.invokedBy` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `req.requestParameters.Host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `req.resources.ARN` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `req.resources.type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `req.resources.accountId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when principal machine data and principal user ID details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when principal machine data and target machine data are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when `eventName` consists of keywords `DescribeInstances`, `DescribeInstanceStatus`, `DescribeRouteTables`, or `ListDomainNames`, and principal or target user details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when the above conditions are not met.   
2024-03-17 |  Enhancement:  
\- Mapped `req.userIdentity.arn` and `req.userIdentity.userName` to `target.user.userid`.   
2023-01-04 |  Enhancement:  
\- Initialized variables to avoid replication of data in the For loop.   
2022-12-15 |  Enhancement:  
\- Mapped `metadata.vendor_name` to `AWS`.  
\- Mapped `metadata.product_name` to `AWS Control Tower`.  
\- Mapped `metadata.event_type` to `USER_LOGIN` when `eventName` is `ConsoleLogin`.  
\- Mapped `security_result.severity` to `INFORMATIONAL` when `eventName` is `ConsoleLogin`.   
2022-11-17 |  Enhancement:  
\- Mapped `req.userIdentity.userName` and `req.userIdentity.sessionContext.sessionIssuer.userName` to `target.user.id`.  
\- Mapped `ConsoleLogin:Success` to `security_result.action`.  
\- Mapped port information from `sourceIPAddress` to `principal.port`.   
2022-10-31 |  Enhancement: New Parser created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
