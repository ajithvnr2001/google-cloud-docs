---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-api-gateway-changelog/
title: Change log for AWS_API_GATEWAY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:35.774262+00:00
---

# Change log for AWS_API_GATEWAY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-api-gateway-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_API_GATEWAY

Date | Changes  
---|---  
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Metadata.Product.Feature.Name`, `Metadata.Profiles`, `Metadata.Product.Name`, `Metadata.Product.Vendor_name`, `Unmapped.Integration_latency`, `Http_request.Request_id`, `Unmapped.Response_latency`, `Connection_info.Protocol_num`, `Connection_info.Direction_id`, `Category_uid`, `Class_uid`, `Activity_id`, `Type_uid` and `Dst_endpoint.Type_id` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Api.Stage`, `Unmapped.Owner_account_id`, `Api.Resource_id`, `Api.Resource_path` and `Dst_endpoint.Type` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `App_Name` raw log field to `event.idm.read_only_udm.target.application` UDM field  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Src_endpoint.Ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`UDM fields.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Metadata.Version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Class_name` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `Metadata.Product.Uid` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Api.Api_id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Http_request.Url.Hostname` raw log fields to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `Dst_endpoint.Hostname` raw log fields to `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`,`event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `Http_request.User_agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Http_request.Url.Path` raw log fields to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Api.Name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.category`: Newly mapped `Category_name` raw log field to `event.idm.read_only_udm.security_result.category` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `Severity_id` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `Http_request.Http_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `Http_request.Extended_request_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `Http_response.Code` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `Http_request.Url.Scheme` and `Http_request.Protocol` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Connection_info.Protocol_name` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `Traffic.Bytes_out` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Activity_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal user data is present then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` UDM field.   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `accountId` from `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `accountId` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `wafStatusCode` from `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `wafStatusCode` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `wafResponseCode` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `wafAclArn` from `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `wafAclArn` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `UniqueRequestId` from `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.network.session_id`: Mapped `UniqueRequestId` raw log field to `event.idm.read_only_udm.network.session_id`.   
2025-12-26 |  Enhancement:  
\- Added support for the new pattern of logs.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `identity_sourceIp` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `identity_sourceIp` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `identity_user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `identity_userAgent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `identity_userAgent` raw log field to `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_caller` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `integrationStatus` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `responseLatency` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `authorizer_property` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `authorizer_claims_property` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `extendedRequestId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `authorizer_principalId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `awsEndpointRequestId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `authorizer_error_message` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `domainPrefix` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_cognitoIdentityPoolId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_cognitoIdentityId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_cognitoAuthenticationType` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_cognitoAuthenticationProvider` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `identity_accountId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `identity_userArn` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `error_message` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `error_responseType` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `wafStatusCode` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `wafAclArn` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `UniqueRequestId` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `wafResponseCode` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `domainName` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `domainName` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping `accountId` from `event.idm.read_only_udm.additional.fields` and mapped `event.idm.read_only_udm.principal.resource.attribute.labels` instead in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `authorizer_integrationlatency` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-03 |  Enhancement:  
event.idm.read_only_udm.principal.ip: Newly mapped `s3_remoteip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
event.idm.read_only_udm.principal.asset.ip: Newly mapped `s3_remoteip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
event.idm.read_only_udm.principal.user.userid: Newly mapped `s3_requester_user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
event.idm.read_only_udm.network.http.response_code: Newly mapped `s3_httpstatus` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
event.idm.read_only_udm.metadata.product_log_id: Newly mapped `s3_requestid` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
event.idm.read_only_udm.target.resource.name: Newly mapped `s3_bucket` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
event.idm.read_only_udm.target.file.full_path: Newly mapped `s3_uri` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.  
event.idm.read_only_udm.network.http.user_agent: Newly mapped `s3_useragent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
event.idm.read_only_udm.network.http.method: Newly mapped `s3_http_capture` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
event.idm.read_only_udm.target.url: Newly mapped `s3_hostheader` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
event.idm.read_only_udm.network.sent_bytes: Newly mapped `s3_bytes_sent` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
event.idm.read_only_udm.target.file.size: Newly mapped `s3_objectsize` raw log field to `event.idm.read_only_udm.target.file.size` UDM field.  
event.idm.read_only_udm.additional.fields: Newly mapped `apiKeyId` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
event.idm.read_only_udm.additional.fields: Newly mapped `apiKey` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
event.idm.read_only_udm.additional.fields: Newly mapped `latency` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-05 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `requestTime` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped `requestTime` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-08-26 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `apiId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user, authorizerPrincipalId` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `authorizerPrincipalId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `integrationLatency`, `xrayTraceId`, `accountId` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `requestTime` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Added grok pattern to extract `app_protocol_src` and `http_version` from `protocol` raw log field else mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- Newly mapped `app_protocol_src` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- Newly mapped `http_version` field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `requestId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `responseLength` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `sourceIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `sourceIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `statusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `resourcePath` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2025-02-13 |  Enhancement:  
\- Added `gsub` to parse new type of logs.  
\- Mapped `account_id`, `api_id`, `aws_endpoint_request_id`, `caller`, `domain_prefix`, `extended_request_id`, `identity_user_arn`, `resource_path`, `stage`, `waf_response_code`, and `web_acl_arn` to `additional.fields`.  
\- Mapped `domain_name` to `principal.administrative_domain`.  
\- Mapped `request_time` to `security_result.detection_fields`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `identity_principal_org_id` to `principal.resource.attribute.labels`.  
\- Mapped `identity_source_ip_address` to `principal.ip`.  
\- Mapped `identity_user` to `principal.user.userid`.   
2024-07-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
