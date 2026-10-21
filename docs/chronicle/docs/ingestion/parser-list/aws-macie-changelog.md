---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-macie-changelog/
title: Change log for AWS_MACIE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:00:21.411953+00:00
---

# Change log for AWS_MACIE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-macie-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_MACIE

Date | Changes  
---|---  
2025-05-15 |  Enhancement:  
\- Initialized the `resourcesAffected.s3Bucket.owner.id`, `resourcesAffected.s3Bucket.name`, `resourcesAffected.s3Bucket.tags`, `resourcesAffected.s3Object.path`, `resourcesAffected.s3Object.key`, `resourcesAffected.s3Object.lastModified`, `resourcesAffected.s3Object.eTag`, `resourcesAffected.s3Object.storageClass`, `classificationDetails.result.mimeType`, `classificationDetails.jobArn`, `classificationDetails.jobId`, `classificationDetails.originType`, `severity.description` and `sr` fields with empty strings to ensure proper data mapping. These fields were previously uninitialized.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `account` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `detail.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `detail.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `detail.policyDetails.action.actionType` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `detail.policyDetails.action.apiCallDetails.apiServiceName` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipAddressV4` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.accessKeyId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.arn` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.principalId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.sessionContext.sessionIssuer.userName` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `detail.createdAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `detail.resourcesAffected.s3Bucket.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `detail.resourcesAffected.s3Bucket.owner.displayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `detail.resourcesAffected.s3Bucket.owner.id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `detail.title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `detail.severity.description` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `detail.severity.score` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Modified the parser logic to conditionally set the `event.idm.read_only_udm.metadata.event_type` UDM field based on the presence of `has_principal` and `has_target_file` fields. If `has_principal` and `has_target_file` are true, `event_type` is set to `SCAN_FILE`. If only `has_principal` is true, `event_type` is set to `STATUS_UPDATE`.Otherwise, `event_type` is set to `GENERIC_EVENT`.  
\- Modified the parser logic for the `event.idm.read_only_udm.target.file.mime_type` UDM field mapping. Added an `on_error` condition to the `mutate` block that populates the `mime_type`.Introduced a new variable `has_target_file` set to `true` if the `mime_type` is successfully extracted.  
\- Modified the parser logic for the `event.idm.read_only_udm.principal.hostname` UDM field mapping. Added an `on_error` condition to the `mutate` block that populates the `no_principal_hostname`.Introduced a new variable `has_principal` set to `true` if the `no_principal_hostname` is successfully extracted.  
\- Modified the parser logic for the `event.idm.read_only_udm.target.file.names` UDM field mapping. Added an `on_error` condition to the `mutate` block that populates the `no_resource_ancestors_to_merge`.Introduced a new variable `has_target` set to `true` if the `no_resource_ancestors_to_merge` is successfully extracted.  
\- Modified the parser logic for the `event.idm.read_only_udm.target.file.md5` UDM field mapping. Added an `on_error` condition to the `mutate` block that populates the `no_md5`.Introduced a new variable `has_target_file` set to `true` if the `no_md5` is successfully extracted.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `detail-type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.schemaVersion` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.accountId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.partition` raw log field with `event.idm.read_only_udm.additional.fields`` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.region` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `detail.type` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `detail.updatedAt` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.count` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `detail.resourcesAffected.s3Bucket.arn` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.creation_time: Newly mapped `detail.resourcesAffected.s3Bucket.createdAt` raw log field with `event.idm.read_only_udm.target.resource.attribute.creation_time` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `detail.resourcesAffected.s3Bucket.tags.key` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `detail.resourcesAffected.s3Bucket.tags.value` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `detail.resourcesAffected.s3Bucket.defaultServerSideEncryption.encryptionType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `detail.resourcesAffected.s3Bucket.defaultServerSideEncryption.kmsMasterKeyId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.rule_labels: Newly mapped `detail.resourcesAffected.s3Bucket.publicAccess.effectivePermission` raw log field with `event.idm.read_only_udm.security_result.rule_labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.resourcesAffected.s3Bucket.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicAcls` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.resourcesAffected.s3Bucket.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.blockPublicPolicy` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.resourcesAffected.s3Bucket.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.ignorePublicAcls` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.resourcesAffected.s3Bucket.publicAccess.permissionConfiguration.accountLevelPermissions.blockPublicAccess.restrictPublicBuckets` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.action.apiCallDetails.api` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `detail.policyDetails.action.apiCallDetails.firstSeen` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- event.idm.read_only_udm.security_result.last_updated_time: Newly mapped `detail.policyDetails.action.apiCallDetails.lastSeen` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.policyDetails.actor.UserIdentity.assumedRole.accountId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.sessionContext.sessionIssuer.accountId` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.sessionContext.attributes.mfaAuthenticated` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.sessionContext.sessionIssuer.arn` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `detail.policyDetails.actor.userIdentity.assumedRole.sessionContext.sessionIssuer.principalId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.network.asn: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipOwner.asn` raw log field with `event.idm.read_only_udm.principal.network.asn` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipCountry.code` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.network.organization_name: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipOwner.asnOrg` raw log field with `event.idm.read_only_udm.principal.network.organization_name` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipOwner.isp` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipOwner.org` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipCity.name` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipCountry.name` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.principal.location.latitude: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipGeoLocation.lat` raw log field with `event.idm.read_only_udm.principal.location.latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.longitude: Newly mapped `detail.policyDetails.actor.ipAddressDetails.ipGeoLocation.lon` raw log field with `event.idm.read_only_udm.principal.location.longitude` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.sample` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detail.archived` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-08 |  Enhancement:  
\- Initialized the `title`, `description`, and `category` fields with empty strings to ensure proper data mapping. These fields were previously uninitialized.  
\- Added a regex check to validate the field `resourcesAffected.s3Object.eTag` is a 32-character hexadecimal string.   
2022-08-08 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
