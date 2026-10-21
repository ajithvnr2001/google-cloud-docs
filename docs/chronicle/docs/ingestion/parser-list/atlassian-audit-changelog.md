---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-audit-changelog/
title: Change log for ATLASSIAN_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:15:24.916430+00:00
---

# Change log for ATLASSIAN_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ATLASSIAN_AUDIT

Date | Changes  
---|---  
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Removed mapping of `record.attributes.actor.auth.authType`, `record.attributes.actor.auth.tokenId`, and `record.attributes.actor.auth.tokenName` from `event.idm.read_only_udm.principal.user.attribute.labels` UDM field as they contain principal authentication resource subtype, token identifier, and token resource name data.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Mapped `record.attributes.actor.auth.authType` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `record.attributes.actor.auth.tokenId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Mapped `record.attributes.actor.auth.tokenName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Removed mapping of `data.record.attributes.container.attributes.siteName` and `attributes.container.attributes.siteName` from `event.idm.read_only_udm.target.resource.name` UDM field as it contains target hostname data.  
\- `event.idm.read_only_udm.principal.resource.name`: Removed mapping of `container.attributes.siteName` from `event.idm.read_only_udm.principal.resource.name` UDM field as it contains target hostname data.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `data.record.attributes.container.attributes.siteName`, `attributes.container.attributes.siteName` and `container.attributes.siteName` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Removed mapping of `data.record.attributes.container.attributes.fullPath`, `attributes.container.attributes.fullPath` from `event.idm.read_only_udm.target.process.file.full_path` UDM field as it contains the target API resource path name.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `data.record.attributes.container.attributes.fullPath`, `attributes.container.attributes.fullPath` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `data.record.attributes.container.links.alt`, `attributes.container.links.alt` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field as it contains the target URL data.  
\- `event.idm.read_only_udm.target.url`: Mapped `data.record.attributes.container.links.alt`, `attributes.container.links.alt` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `NETWORK_CONNECTION` to `event.idm.read_only_udm.metadata.event_type` UDM field when the log contains principal machine data and target machine data.   
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `record.attributes.actor.auth.authType`, `record.attributes.actor.auth.tokenId`, `record.attributes.actor.auth.tokenName`, and `container.type` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `container.attributes.query_fields`, `container.attributes.path_sprintId`, `container.attributes.query_maxResults`, `container.attributes.traceId` and `container.links.alt` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record.links.self`, `record.msg.format` and `data.type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `record.attributes.location.regionName` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `container.attributes.siteName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `container.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `container.attributes.httpMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `container.attributes.statusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `container.attributes.traceId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `container.attributes.siteHostName` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `container.attributes.fullPath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.   
2026-07-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `container.attributes.siteHostName` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when it contains the URL.  
\- `event.idm.read_only_udm.principal.url`: Mapped `container.attributes.siteHostName` with `event.idm.read_only_udm.principal.url` UDM field when it contains the URL.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `container.attributes.name` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as it is an email address not an valid hostname.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Mapped `container.attributes.name` with `event.idm.read_only_udm.principal.user.email_addresses` UDM field as it contains the email address.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `contextData.attributes.groupName` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `contextData.attributes.applicationCore` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `contextData.attributes.orgId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `contextData.attributes.siteName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `contextData.type`, `contextData.attributes.ownerType`, `contextData.attributes.managedStatus` `contextData.attributes.verificationType` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `contextData.attributes.status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `contextData.attributes.authFactors` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `type`, `msg.format`, `links.self`, `container.attributes.tenantID`, `contextData.attributes.shouldCreateHomePage`, `contextData.attributes.siteHostName`, `contextData.attributes.systemSpaceHomepageTemplate`, `id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `email_details`, `container.type`, `container.attributes.picture`, `container.attributes.email`, `container.attributes.accountType`, `container.links.alt`, `container.links.self` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `attributes.location.country_name` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `container.attributes.siteName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped to `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when user information is present alongside with either principal or target data present.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present or when `product_event_type` contains `jira`.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `event.idm.read_only_udm.metadata.vendor_name` to `Atlassian`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `event.idm.read_only_udm.metadata.product_name` to `Atlassian Cloud Admin Audit`.   
2025-01-09 |  Added support for unparsed logs.   
2024-12-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
