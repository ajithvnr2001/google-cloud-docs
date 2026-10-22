---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-messagetrace-changelog/
title: Change log for OFFICE_365_MESSAGETRACE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:30.943879+00:00
---

# Change log for OFFICE_365_MESSAGETRACE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-messagetrace-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OFFICE_365_MESSAGETRACE

Date | Changes  
---|---  
2026-04-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `receivedDateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `fromIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `toIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `size` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `senderAddress` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `recipientAddress` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `messageId` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `Status` is `delivered`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `Status` is `resolved`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `Status` is `failed`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: If `Status` is `quarantined`, updated the value of `event.idm.read_only_udm.security_result.action` to `QUARANTINE`.   
2025-08-21 |  Enhancement:  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped Size raw log field to event.idm.read_only_udm.network.received_bytes UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Index`, `__metadata.type`, `__metadata.id` raw log fields to event.idm.read_only_udm.additional.fields UDM field.  
\- Enhanced timestamp parsing for the `Received` raw log field to handle UNIX millisecond format and mapped to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2024-06-07 |  Enhancement:  
\- When the timestamps are in dd/MMM/yyyy HH:mm:ss format, then added support to parse `Received` to `metadata.event_timestamp`.  
\- Mapped `ToIP` to `target.ip`.   
2024-05-28 |  Enhancement:  
\- Mapped `properties.SenderMailFromDomain`, `properties.UserLevelAction`, and `properties.UserLevelPolicy` to `principal.user.attribute.labels`.  
\- Mapped `properties.SenderFromDomain` to `principal.administrative_domain`.  
\- Mapped `properties.EmailDirection` to `network.direction`.  
\- Mapped `properties.DeliveryAction`, `properties.DeliveryLocation`, `properties.Connectors`, `properties.OrgLevelAction`, `properties.OrgLevelPolicy`, `properties.AdditionalFields`, and `properties.UrlLocation` to `additional.fields`.  
\- Mapped `properties.Subject` to `network.email.subject`.  
\- Mapped `properties.ConfidenceLevel` to `additional.fields`.  
\- Mapped `properties.Url` to `target.url`.  
\- Mapped `properties.UrlDomain` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `properties.AuthenticationDetails` to `extensions.auth.auth_details`.   
2024-04-18 |  Enhancement:  
\- Mapped `time` to `metadata.event_timestamp`.  
\- Mapped `tenantId` to `metadata.product_deployment_id`.  
\- Mapped `operationName`, `Tenant` to `additional.fields`.  
\- Mapped `category` to `metadata.product_event_type`.  
\- Mapped `properties.SenderFromAddress` to `principal.user.email_addresses` and `network.email.from`.  
\- Mapped `properties.RecipientEmailAddress` to `network.email.to` and `target.user.email_addresses`.  
\- Mapped `properties.FileName` to `principal.process.file.names`.  
\- Mapped `properties.SHA256` to `principal.process.file.sha256`.  
\- Mapped `properties.FileSize` to `principal.process.file.size`.  
\- Mapped `properties.RecipientObjectId` to `target.user.product_object_id`.  
\- Mapped `properties.SenderObjectId` to `principal.user.product_object_id`.  
\- Mapped `properties.SenderDisplayName` to `principal.user.user_display_name`.  
\- Mapped `properties.ThreatNames` to `security_result.threat_name`.  
\- Mapped `properties.DetectionMethods` to `security_result.detection_fields`.   
2023-05-10 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
