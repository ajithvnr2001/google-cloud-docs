---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty_changelog/
title: Change log for GUARDDUTY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:46.214412+00:00
---

# Change log for GUARDDUTY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GUARDDUTY 

Date | Changes | 2022-03-31 | Enhancement   
If service.action.networkConnectionAction.localPortDetails.portName is not "Unknown" value mapped to principal.application.   
Entire list within "tags" field mapped to key-value fields.   
"service.action.networkConnectionAction.protocol" mapped to network.ip_protocol   
"service.action.networkConnectionAction.blocked" mapped to security_result.action   
"severity" mapped to security_result.severity_details   
If service.action.actionType is AWS_API_CALL, "accessKeyId" mapped to target.resource.id.   
In s3BucketDetails:   
\- "arn" mapped to target.asset.attribute.cloud.project.product_object_id.   
\- "name" mapped to target.resource.name.   
\- "encryptionType" mapped to network.tls.supported_ciphers.   
\- "owner.id mapped to target.resource.attribute.labels.   
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.accessControlList:   
\- mapped "allowsPublicReadAccess" to additional.fields attribute.   
\- mapped "allowsPublicWriteAccess" to additional.fields attribute.   
\---   
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.bucketPolicy:   
\- mapped "allowsPublicReadAccess" to additional.fields attribute.   
\- mapped "allowsPublicWriteAccess" to additional.fields attribute.   
\---   
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.bucketLevelPermissions.blockPublicAccess:   
\- mapped "ignorePublicAcls" to additional.fields attribute.   
\- mapped "restrictPublicBuckets" to additional.fields attribute.   
\- mapped "blockPublicAcls" to additional.fields attribute.   
\- mapped "blockPublicPolicy" to additional.fields attribute.   
\---   
Under resource.s3BucketDetails.0.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess   
mapped ignorePublicAcls to additional.fields attribute.   
"restrictPublicBuckets" to additional.fields attribute.   
"blockPublicAcls" to additional.fields attribute.   
"blockPublicPolicy" to additional.fields attribute.   
Under service.action.awsApiCallAction.remoteIpDetails.organization:   
\- "asn" mapped to additional.fields attribute.   
\- "asnOrg" mapped to additional.fields attribute.   
\- "isp" mapped to additional.fields attribute.   
\- "org" mapped to additional.fields attribute.   
Under service.action.awsApiCallAction.affectedResources, mapped "AWS::S3::Bucket" additional.fields attribute.   
If service.action.actionType is DNS_REQUEST, "accessKeyId" mapped to target.resource.id.   
\- resource.instanceDetails.instanceId mapped to target.resource.id   
\- resource.instanceDetails.instanceType mapped to target.resource.name   
\- resource.instanceDetails.networkInterfaces.0.vpcId mapped to target.asset.attribute.cloud.vpc.id   
Values under resource.instanceDetails.tags mapped the following fields:   
\- target.user.userid if the key is "ApplicationOwner".   
\- target.application if the key is "Application".   
\- user.email_addresses if the key is "Contact".   
\- additional.fields if the key is "Name", "DAM_Project", "Project", or "ehc:C3Schedule".   
service.action.dnsRequestAction.protocol mapped network.ip_protocol if value is not 0.   
service.action.networkConnectionAction.blocked mapped to security_result.action.   
"severity" mapped to security_result.severity_details.   
  
---|---  
2022-03-25 | Enhancement - Port udm is not a repeated field. This makes it unsuitable to capture a lot of ports from a log. This change uses about.port instead.   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
