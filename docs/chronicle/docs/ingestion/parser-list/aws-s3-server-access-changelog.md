---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-s3-server-access-changelog/
title: Change log for AWS_S3_SERVER_ACCESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:50:17.050901+00:00
---

# Change log for AWS_S3_SERVER_ACCESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-s3-server-access-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_S3_SERVER_ACCESS

Date | Changes  
---|---  
2025-06-11 |  Enhancement:  
\- Created separate mutate blocks for replace and merge which were in the same mutate block.  
\- Removed initial declaration for on_error values.  
\- Updated duplicating on_error values to unique values.  
\- Added on_errors wherever missing.   
2025-06-09 |  Enhancement:  
\- Removed initial declaration for on_error values.  
\- Updated duplicating on_error values to unique values.   
2025-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Metadata.Product.Version` raw log field with the `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `Metadata.Product.Name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Metadata.Product.Feature.Name` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Metadata.Event_code` raw log field with the `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `Metadata.Uid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Metadata.Profiles.Array` with `event.idm.read_only_udm.additional.fields`UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Metadata.Version` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.cloud.availability_zone`: Newly mapped `Cloud.Region` raw log field with `event.idm.read_only_udm.target.cloud.availability_zone` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `Api.Operation` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Api.Service.Name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Api.Request.Data` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `Api.Request.Uid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.role_name`: Newly mapped `Actor.User.Type` raw log field with `event.idm.read_only_udm.principal.user.role_name UDM` field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Actor.User.Uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Actor.User.Uid_alt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Actor.User.Account.Uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Actor.User.Credential_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.creation_time`: Newly mapped `Actor.Session.Created_time_dt` raw log field with `event.idm.read_only_udm.principal.user.attribute.creation_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Actor.Session.Is_mfa` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `Actor.Session.Issuer` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `Http_request.User_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Src_endpoint.Uid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Src_endpoint.Ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Resources.Array.Uid` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Resources.Array.Type` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Class_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Class_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Category_name` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Category_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Severity_id` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Activity_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Activity_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Type_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Type_uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Status` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.additionalEventData.AuthenticationMethod` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `Unmapped.additionalEventData.CipherSuite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.additionalEventData.SignatureVersion` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `Unmapped.additionalEventData.bytesTransferredIn` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `Unmapped.additionalEventData.bytesTransferredOut` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.additionalEventData.x-amz-id-2` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.managementEvent` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.readOnly` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.cloud.project.id`: Newly mapped `Unmapped.recipientAccountId` raw log field with `event.idm.read_only_udm.target.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.sharedEventID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `Unmapped.tlsDetails.clientProvidedHostHeader` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly `mapped `Unmapped.tlsDetails.tlsVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.accountId` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.principalId` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.type` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped Unmapped.userIdentity.sessionContext.sessionIssuer.userName raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.cloud.project.id`: Newly mapped `Unmapped.vpcEndpointAccountId` raw log field with `event.idm.read_only_udm.principal.cloud.project.id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Observables.Array.Name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Observables.Array.Value` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Observables.Array.Value` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Observables.Array.Type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `obs.Type_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-11-12 |  Enhancement:  
\- Added support for unparsed logs.  
\- Mapped `target.resource.resource_type` to `DATABASE`.   
2023-07-19 |  Bug-Fix -  
\- Modified Grok pattern to handle a hyphen (-) when data is not present.  
\- Mapped `aclRequired` to `target.resource.attribute.labels`.   
2023-05-04 |  Enhancement-  
\- Added support for JSON format logs.   
2022-07-21 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
