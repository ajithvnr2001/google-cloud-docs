---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-lambda-function-changelog/
title: Change log for AWS_LAMBDA_FUNCTION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:42:43.590079+00:00
---

# Change log for AWS_LAMBDA_FUNCTION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-lambda-function-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_LAMBDA_FUNCTION

Date | Changes  
---|---  
2025-07-29 |  Enhancement:  
\- Added support for a new pattern of JSON logs.  
\- The raw field `target` is internally renamed to `targetVar` to prevent conflicts.  
\- If the raw `severity` field is empty, it will now be populated with the value from the `level` field.  
\- Added gsub to replace `event` with `Event` in `message`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `error` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `targetVar` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `filename` raw log field to `event.idm.read_only_udm.target.process.file.full_path`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `line_number` raw log field to a key named `line_number` within `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.target.application: Newly mapped `service` raw log field to `event.idm.read_only_udm.target.application`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `version` raw log field to a key named `version` within `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `env` raw log field to a key named `env` within `event.idm.read_only_udm.additional.fields`.   
2025-05-26 |  Enhancement  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Activity_id` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Activity_name` log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `Actor.Invoked_by` log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Actor.User.Type` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `Api.Operation` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `Api.Request.Uid` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `functionName` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `sourceArn` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logType` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `contentType` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sourceAccount` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `Api.Service.Name` log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `Category_name` log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Class_name` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Category_uid` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Class_uid` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Metadata.Event_code` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Metadata.Product.Feature.Name` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Metadata.Product.Name` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Metadata.Product.Vendor_name` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Metadata.Product.Version` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Metadata.Profiles.Array` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Observables.Array.Name` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Observables.Array.Type` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Observables.Array.Type_id` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Observables.Array.Value` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Resources.Array.Owner.Account.Uid` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Resources.Array.Type` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Resources.Uid` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Metadata.Uid` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Metadata.Version` log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.cloud.environment: Newly mapped `Cloud.Provider` log field with `event.idm.read_only_udm.principal.resource.attribute.cloud.environment` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.cloud.availability_zone: Newly mapped `Cloud.Region` log field with `event.idm.read_only_udm.principal.resource.attribute.cloud.availability_zone` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `Http_request.User_agent` log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `Severity` log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Severity_id` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Src_endpoint.Domain` log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `Status` log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Type_name` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Type_uid` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `Time` log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `Api.Service.Name` log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-02-19 |  Enhancement  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
