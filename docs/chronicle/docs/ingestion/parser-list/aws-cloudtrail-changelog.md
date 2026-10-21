---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudtrail-changelog/
title: Change log for AWS_CLOUDTRAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:14:29.193794+00:00
---

# Change log for AWS_CLOUDTRAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudtrail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_CLOUDTRAIL

Date | Changes  
---|---  
2026-09-21 |  \- Enhanced the parser logic to handle the edge case of `Records.requestParameters.policyArn` raw log field for `GetPolicy` event.   
2026-08-27 |  \- `network.http.user_agent` : Newly mapped `Records.insightDetails.insightContext.attributions.attribute` and `Records.insightDetails.insightContext.attributions.insight.value` raw log field with `network.http.user_agent` UDM field when `attribute` is `userAgent`.  
\- `principal.user.userid` : Newly mapped `Records.insightDetails.insightContext.attributions.attribute` raw log field with `principal.user.userid` UDM field when `attribute` is `userIdentityArn`.  
\- `metadata.event_type` : Newly mapped the value `RESOURCE_DELETION` with `metadata.event_type` UDM field when `Records.insightDetails.eventName` is `DeleteSubscriptionFilter`.   
2026-07-24 |  \- `target.resource.name` : Newly mapped `requestParameters.policyArn` raw log field with `target.resource.name` UDM field when `eventName` is `GetPolicy`.  
\- `principal.user.group_identifiers`: Modified the mapping for `principal.user.group_identifiers` from replace to merge to ensure values from `iter_Records.Actor.User.Account.Uid` are appended to the repeated field, rather than overwriting existing values.   
2026-07-09 |  \- `target.resource.name`: Newly mapped `Records.requestParameters.logGroupName` raw log field with `target.resource.name` UDM field for `DeleteLogGroup` event.   
2026-05-20 |  \- Modified the parser logic to first attempt parsing the message field as JSON. If JSON parsing fails, the parser now falls back to the existing GROK patterns to handle non-JSON formatted logs   
2026-03-24 |  \- `target.resource.attribute.labels[req_instance_ids]`: Newly mapped `Records.requestParameters.instanceIds` raw log field with `target.resource.attribute.labels[req_instance_ids]` UDM field.  
\- The validation condition has been enhanced to accurately parse the metadata.event_type UDM field.   
2026-02-25 |  \- `target.resource.name`: Newly mapped `Records.serviceEventDetails.closeAccountStatus.accountId` raw log field with `target.resource.name` UDM field.  
\- `target.resource.attribute.labels[service_event_details_close_account_status_completed_timestamp]`: Newly mapped `Records.serviceEventDetails.closeAccountStatus.completedTimestamp` raw log field with `target.resource.attribute.labels[service_event_details_close_account_status_completed_timestamp]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_close_account_status_requested_timestamp]`: Newly mapped `Records.serviceEventDetails.closeAccountStatus.requestedTimestamp` raw log field with `target.resource.attribute.labels[service_event_details_close_account_status_requested_timestamp]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_close_account_status_state]`: Newly mapped `Records.serviceEventDetails.closeAccountStatus.state` raw log field with `target.resource.attribute.labels[service_event_details_close_account_status_state]` UDM field.  
\- `target.resource.name`: Newly mapped `Records.serviceEventDetails.createAccountStatus.accountId` raw log field with `target.resource.name` UDM field.  
\- `target.user.user_display_name`: Newly mapped `Records.serviceEventDetails.createAccountStatus.accountName` raw log field with `target.user.user_display_name` UDM field.  
\- `target.resource.attribute.labels[service_event_details_create_account_status_completed_timestamp]`: Newly mapped `Records.serviceEventDetails.createAccountStatus.completedTimestamp` raw log field with `target.resource.attribute.labels[service_event_details_create_account_status_completed_timestamp]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_create_account_status_id]`: Newly mapped `Records.serviceEventDetails.createAccountStatus.id` raw log field with `target.resource.attribute.labels[service_event_details_create_account_status_id]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_create_account_status_requested_timestamp]`: Newly mapped `Records.serviceEventDetails.createAccountStatus.requestedTimestamp` raw log field with `target.resource.attribute.labels[service_event_details_create_account_status_requested_timestamp]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_create_account_status_state]`: Newly mapped `Records.serviceEventDetails.createAccountStatus.state` raw log field with `target.resource.attribute.labels[service_event_details_create_account_status_state]` UDM field.  
\- `target.resource.name`: Newly mapped `Records.serviceEventDetails.eventRequestDetails.analysisId` raw log field with `target.resource.name` UDM field.  
\- `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_analysis_id]`: Newly mapped `Records.serviceEventDetails.eventResponseDetails.analysisDetails.analysisId` raw log field with `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_analysis_id]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_analysis_name]`: Newly mapped `Records.serviceEventDetails.eventResponseDetails.analysisDetails.analysisName` raw log field with `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_analysis_name]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_%{index1}_data_set_id_list]`: Newly mapped `Records.serviceEventDetails.eventResponseDetails.analysisDetails.dataSetIdList` raw log field with `target.resource.attribute.labels[service_event_details_event_response_details_analysis_details_%{index1}_data_set_id_list]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_instance_id_set_%{index1}]`: Newly mapped `Records.serviceEventDetails.instanceIdSet` raw log field with `target.resource.attribute.labels[service_event_details_instance_id_set_%{index1}]` UDM field.  
\- `target.resource.product_object_id`: Newly mapped `Records.serviceEventDetails.keyId` raw log field with `target.resource.product_object_id` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_last_evaluated_at]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lastEvaluatedAt` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_last_evaluated_at]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_action]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.action` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_action]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_description]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.description` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_description]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_count_number]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.lifecycleEventSelection.countNumber` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_count_number]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_count_type]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.lifecycleEventSelection.countType` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_count_type]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_tag_status]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.lifecycleEventSelection.tagStatus` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_lifecycle_event_selection_tag_status]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_rulePriority]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.lifecycleEventRules.rulePriority` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_lifecycle_event_rules_%{index1}_rulePriority]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_policy_id]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.policyId` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_policy_id]` UDM field.  
\- `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_policy_version]`: Newly mapped `Records.serviceEventDetails.lifecycleEventPolicy.policyVersion` raw log field with `target.resource.attribute.labels[service_event_details_lifecycle_event_policy_policy_version]` UDM field.  
\- `target.resource.name`: Newly mapped `Records.serviceEventDetails.repositoryName` raw log field with `target.resource.name` UDM field.  
\- `target.resource.product_object_id`: Newly mapped `Records.serviceEventDetails.snapshotId` raw log field with `target.resource.product_object_id` UDM field.  
\- `target.resource.product_object_id`: Newly mapped `Records.serviceEventDetails.vpcId` raw log field with `target.resource.product_object_id` UDM field.  
\- `target.resource.attribute.labels[service_event_details_event_request_details_query_id]`: Newly mapped `Records.serviceEventDetails.eventRequestDetails.queryId` raw log field with `target.resource.attribute.labels[service_event_details_event_request_details_query_id]` UDM field.   
2026-01-30 |  \- `principal.user.attribute.roles.name`: Newly mapped role value extracted from `Records.userIdentity.arn` raw log field with `principal.user.attribute.roles.name` UDM field for all the event except `ConsoleLogin` and `UserAuthentication`.  
\- `target.user.attribute.roles.name`: Newly mapped role value extracted from `Records.userIdentity.arn` raw log field with `target.user.attribute.roles.name` UDM field for the event `ConsoleLogin` and `UserAuthentication`.   
2025-12-11 |  \- Enhanced the parser logic to handle the edge cases of `Records.userIdentity.principalId` and `Records.userIdentity.arn` raw log fields.   
2025-11-07 |  \- network.dns.additional.name: Newly mapped `Records.requestParameters.changeBatch.changes.resourceRecordSet.name` raw log field with `network.dns.additional.name` UDM field.  
\- network.dns.additional.ttl: Newly mapped `Records.requestParameters.changeBatch.changes.resourceRecordSet.tTL` raw log field with `network.dns.additional.ttl` UDM field.  
\- network.dns.additional.type: Newly mapped `Records.requestParameters.changeBatch.changes.resourceRecordSet.type` raw log field with `network.dns.additional.type` UDM field.  
\- network.dns.additional.data: Newly mapped `Records.requestParameters.changeBatch.changes.resourceRecordSet.resourceRecords.value` raw log field with `network.dns.additional.data` UDM field.   
2025-10-28 |  \- This is a new Premium version for the AWS_CLOUDTRAIL parser.  
\- For the configuration details along with the list mapping which were changed in comparison to the existing default parser, please check the parser documentation page https://docs.cloud.google.com/chronicle/docs/reference/aws-cloudtrail-field-map#mapping-delta   
2025-05-26 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `req.requestParameters.Actions.FindingFieldsUpdate.Workflow.Status` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `req.requestParameters.Actions.FindingFieldsUpdate.Note.Text` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `req.requestParameters.Actions.FindingFieldsUpdate.Note.UpdatedBy` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `req.userIdentity.sessionContext.sessionIssuer.principalId` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `req.userIdentity.sessionContext.sessionIssuer.userName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `req.additionalEventData.UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `req.additionalEventData.LoginTo` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Added null conditional check for `req.userIdentity.accessKeyId` raw log field before being mapped to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.event_type: if prinicipal data is not present and `event.idm.read_only_udm.metadata.event_type` is `STATUS_UNCATEGORIZED` then set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `req.insightDetails.insightContext.attributions.attribute`, `req.insightDetails.insightContext.attributions.attribute.baseline.value` and `req.insightDetails.insightContext.attributions.attribute.baseline.average` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `req.userIdentity.sessionContext.webIdFederationData.federatedProvider` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field   
2025-03-06 |  Enhancement:  
\- Added Grok patterns to support new format of syslog logs.   
2025-02-20 |  Enhancement:  
\- Mapped `req.detail.userIdentity.principalId` to `principal.user.product_object_id`.  
\- Mapped `req.detail.userIdentity.sessionContext.sessionIssuer.principalId` to `additional.fields`.  
\- Mapped `req.detail.userIdentity.sessionContext.sessionIssuer.arn` to `additional.fields`.  
\- Mapped `req.detail.userIdentity.sessionContext.sessionIssuer.userName` to `target.user.user_display_name`.  
\- Mapped `req.detail.userIdentity.sessionContext.sessionIssuer.type` to `target.user.attribute.labels`.  
\- Mapped `req.detail.additionalEventData.CipherSuite` to `network.tls.cipher`.  
\- Mapped `req.detail.additionalEventData.AuthenticationMethod` to `additional.fields`.  
\- Mapped `req.detail.additionalEventData.SignatureVersion` to `additional.fields`.  
\- Mapped `req.detail.additionalEventData.x-amz-id-2` to `additional.fields`.  
\- Mapped `req.detail.additionalEventData.bytesTransferredIn` to `network.received_bytes`.  
\- Mapped `req.detail.additionalEventData.SSEApplied` to `additional.fields`.  
\- Mapped `req.detail.vpcEndpointId` to `additional.fields`.  
\- Mapped `req.System` to `additional.fields`.  
\- Mapped `req.cloudwatch_logs.log_stream` to `additional.fields`.  
\- Mapped `req.cloudwatch_logs.log_group` to `additional.fields`.  
\- Mapped `req.cloudwatch_logs.event_id` to `additional.fields`.  
\- Mapped `req.detail.responseElements.x-amz-version-id` to `additional.fields`.  
\- Mapped `req.detail.responseElements.x-amz-server-side-encryption-aws-kms-key-id` to `additional.fields`.  
\- Mapped `req.detail.responseElements.x-amz-server-side-encryption` to `additional.fields`.  
\- Mapped `req.detail.responseElements.x-amz-expiration` to `additional.fields`.  
\- Mapped `req.detail.requestParameters.accessControlList.x-amz-grant-full-control` to `additional.fields`.  
\- Mapped `req.detail.requestParameters.bucketName` to `additional.fields`.  
\- Mapped `req.detail.requestParameters.key` to `additional.fields`.  
\- Mapped `req.detail.userIdentity.accessKeyId` to `target.user.userid`.  
\- Mapped `req.detail.userIdentity.arn` to `principal.resource.name`.   
2025-02-12 |  Enhancement:  
\- Changed `req.requestParameters.destinationParentId` mapping from `additional.fields` to `target.process.parent_process.pid`.   
2025-01-16 |  Enhancement:  
\- Changed mapping for `detail.eventID` from `principal.asset.asset_id` to `metadata.product_log_id`.  
\- Mapped `detail.eventName` to `metadata.product_event_type`.  
\- Mapped `eventType` to `additional.fields`.  
\- Mapped `requestParameters` to `security_result.detection_fields`.  
\- Mapped `detail.userIdentity.userName` to `principal.user.user_display_name`.  
\- Mapped `detail.userIdentity.arn` to `principal.user.userid`.   
2024-12-12 |  Enhancement:  
\- Parsed the unparsed fields for sample logs.   
2024-11-25 |  Enhancement:  
\- Mapped `Metadata.Product.Version` to `metadata.product_version`.  
\- Mapped `Event_code` to `security_result.detection_fields`.  
\- Mapped `Metadata.Uid` to `metadata.product_log_id`.  
\- Mapped `Cloud.Region` to `principal.location.country_or_region`.  
\- Mapped `target.resource.attribute.cloud.environment` to `AMAZON_WEB_SERVICES` when `Cloud.Provider` is `AWS`.  
\- Mapped `credentials.sessionToken` to `security_result.detection_fields`.  
\- Mapped `Api.Operation` to `additional.fields`.  
\- Mapped `Api.Service.Name` to `principal.resource.name`.  
\- Mapped `roleArn` to `target.url`.  
\- Mapped `roleSessionName` to `target.resource.name`.  
\- Mapped `Api.Request.Uid` to `additional.fields`.  
\- Mapped `Actor.User.Type` to `principal.resource.resource_subtype` and `principal.resource.type`.  
\- Mapped `Actor.User.Uid_alt` to `additional.fields`.  
\- Mapped `Actor.User.Uid` to `principal.user.userid`.  
\- Mapped `Actor.User.Account.Uid` to `additional.fields`.  
\- Mapped `Actor.User.Credential_uid` to `additional.fields`.  
\- Mapped `Actor.Session.Issuer` to `security_result.detection_fields`.  
\- Mapped `Session.Credential_uid` to `additional.fields`.  
\- Mapped `Actor.Invoked_by` to `principal.user.userid`.  
\- Mapped `Http_request.User_agent` to `network.http.user_agent`.  
\- Mapped `Src_endpoint.Ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Src_endpoint.Domain` to `principal.domain.name`.  
\- Mapped `Class_name` to `additional.fields`.  
\- Mapped `Class_uid` to `security_result.detection_fields`.  
\- Mapped `Category_name` to `security_result.detection_fields`.  
\- Mapped `security_result.severity` to `INFORMATIONAL` when `Severity` is `Informational`.  
\- Mapped `Activity_name` to `metadata.product_event_type`.  
\- Mapped `Activity_id` to `security_result.detection_fields`.  
\- Mapped `Type_uid` to `security_result.detection_fields`.  
\- Mapped `Type_name` to `security_result.detection_fields`.  
\- Mapped `Unmapped.managementEvent` to `additional.fields`.  
\- Mapped `Unmapped.readOnly` to `additional.fields`.  
\- Mapped `Unmapped.recipientAccountId` to `target.resource.id`.  
\- Mapped `Unmapped.resources[].ARN` to `additional.fields`.  
\- Mapped `Unmapped.resources[].type` to `target.resource.type`.  
\- Mapped `credentials.accessKeyId` to `target.resource.product_object_id`.  
\- Mapped `credentials.expiration` to `security_result.detection_fields`.  
\- Mapped `Unmapped.tlsDetails.cipherSuite` to `network.tls.cipher`.  
\- Mapped `Unmapped.tlsDetails.clientProvidedHostHeader` to `security_result.detection_fields`.  
\- Mapped `Unmapped.sharedEventID` to `target.resource.attribute.labels`.  
\- Mapped `Unmapped.tlsDetails.tlsVersion` to `network.tls.version`.  
\- Mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.principalId` to `target.user.userid`.  
\- Mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.type` to `target.user.attribute.labels`.  
\- Mapped `Unmapped.userIdentity.sessionContext.sessionIssuer.userName` to `target.user.user_display_name`.  
\- Depending on the `arr.Type_id` value, the value of each array element is assigned to different properties of the observer object: `observer.hostname` for 1, `observer.ip` for 2, `observer.user.user_display_name` for 4, and `observer.resource.product_object_id` for 10.   
2024-11-14 |  Enhancement:  
\- Added support to handle new JSON log format.   
2024-11-07 |  Enhancement:  
\- When `eventName` is `DeleteBackupSelection`, and then `metadata.event_type` is mapped to `RESOURCE_DELETION`.   
2024-10-14 |  Enhancement:  
\- Changed the naming for `ManagementEvent` to `managementEvent`.  
\- Changed the naming for `ReadOnly` to `readOnly`.  
\- Changed the naming for `SharedEventID` to `sharedEventID`.  
\- Changed the naming for `ApiVersion` to `apiVersion`.  
\- Changed the naming for `Type` to `type`.  
\- Changed the mapping for `recipientAccountId` to `additional.fields`.  
\- Changed the mapping for `accountId` from `additional.fields` to `principal.user.attribute.labels`.   
2024-10-03 |  Enhancement:  
\- Added validation check for `metadata.event_type` with value `USER_UNCATEGORIZED`.   
2024-09-18 |  Enhancement:  
\- Mapped `readOnly` to `additional.fields`.   
2024-07-30 |  Enhancement:  
\- Fixed the mapping of `src_ip` and `event_type` to parse the new logs.   
2024-07-29 |  Bug-Fix:  
\- When `eventName` is `GetLoginProfile`, `metadata.event_type` is mapped to `RESOURCE_READ`.   
2024-07-24 |  Enhancement:  
\- Changed the mapping from `recipientAccountId` to `userIdentity.accountId` and mapped it to `additional.fields`.   
2024-07-23 |  Enhancement:  
\- Mapped `alert_emails` and `owner_names` to `target.resource.attribute.labels`.   
2024-07-09 |  Enhancement:  
\- Mapped `eventVersion` to `metadata.product_version`.  
\- Mapped `userIdentity.principalId` to `principal.user.attribute.labels`.  
\- Mapped `userIdentity.sessionContext.attributes.creationDate` to `principal.user.attribute.creation_time`.  
\- Mapped `userIdentity.sessionContext.sessionIssuer.type` to `target.user.attribute.labels`.  
\- Mapped `additionalEventData.bytesTransferredIn` to `network.received_bytes`.  
\- Mapped `additionalEventData.bytesTransferredOut` to `network.sent_bytes`.  
\- Mapped `managementEvent`, `readOnly`, `sharedEventID`, `apiVersion`, `additionalEventData.x-amz-id-2`, `additionalEventData.SignatureVersion`, `additionalEventData.AuthenticationMethod`, `additionalEventData.CipherSuite`, and `additionalEventData.sub` to `additional.fields`.   
2024-06-24 |  Enhancement:  
\- Updated the mapping from `principal.resource.type` to `principal.resource.resource_subtype` since the field `principal.resource.type` is a deprecated field.   
2024-05-21 |  Enhancement:  
\- When `requestParameters.bucketPolicy.Statement.n.Resource` is an array, then mapped `requestParameters.bucketPolicy.Statement.n.Resource` to `additional.fields`.   
2024-05-09 |  Enhancement:  
\- Mapped the `groupid` part from `principal.user.userid` to `principal.user.groupid` and `principal.user.group_identifiers` when the `userid` matches the format `^arn:aws:sts::\d+:assumed-role\/\w+\/\w+$`.   
2024-04-30 |  Enhancement:  
\- Mapped `req.requestParameters.networkInterfaceSet.items.associatePublicIpAddress` to `target.resource.attribute.labels`.   
2024-03-22 |  Enhancement:  
\- Mapped `Noun.user.userid` to `Noun.user.product_object_id`.  
\- Mapped `RoleName` from `userIdentity.arn` to `principal.user.role_name` and `principal.user.attribute.roles.name`.  
\- Mapped `PoicyName` from `requestParameters.policyArn` to `security_result.rule_name`.   
2024-03-04 |  Enhancement:  
\- For logs having `eventName` as `TerminateInstances`:  
\- Mapped `responseElements` JSON Object to `target.resource.attribute.labels`.  
\- Mapped `sessionCredentialFromConsole` to `target.resource.attribute.labels`.  
\- For logs where `eventName` is `CreateDomain`,`DeleteDomain`,`CreateCollection`,  
`DeleteCollection`,`CreateDBCluster`,`DeleteDBCluster`,`StopDBCluster`,`StartDBCluster`,  
`CreateCluster`,`DeleteCluster`, `ListClusters`, `CreateNodegroup`, `DeleteNodegroup`,  
`RegisterCluster`, `DeregisterCluster`, `DescribeCluster`, `DescribeNodegroup`, `ListNodegroups`.  
\- Set `target.resource.resource_type` to `CLUSTER`.   
2023-11-21 |  Enhancement:  
\- Mapped `awsRegion` to `target.location.name`.  
\- For logs having `eventName` as `PutBucketAcl`, when `userIdentity.arn` is not present, then modify `metadata.event_type` to `STATUS_UPDATE`.  
\- For logs having `eventName` as prefix `Get`, `List`, `Describe`, `Detect`, `Query`, `Check`, `Decode`,  
`Decrypt`, `Download`, `Retrieve`, `Read`, `Discover`, `Lookup`, `Preview`, `Scan`, `Select`, `Classify`, `Show`, `View`:  
\- Set `metadata.event_type` to `RESOURCE_READ`.  
\- For logs having `eventName` as prefix `Delete`, `Terminate`:  
\- Set `metadata.event_type` to `RESOURCE_DELETION`.  
\- For logs having `eventName` as prefix `Create`, `Put`, `Import`, `Generate`, `Allocate`:  
\- Set `metadata.event_type` to `RESOURCE_CREATION`.  
\- For logs having `eventName` as prefix `Start`, `Activate`, `Reboot`, `Initialize`, `New`:  
\- Set `metadata.event_type` to `STATUS_STARTUP`.  
\- For logs having `eventName` as prefix `Stop`, `Cancel`, `Disconnect`:  
\- Set `metadata.event_type` to `STATUS_SHUTDOWN`.  
\- For logs having `eventName` as prefix `Test`, `Accept`, `Notify`, `Request`, `Validate`, `Confirm`, `Reject`, `Verify`, `Authorize`, `Complete`:  
\- Set `metadata.event_type` to `STATUS_UPDATE`.  
\- For logs having `eventName` as prefix `Assume`, `ConsoleLogin`:  
\- Set `metadata.event_type` to `USER_LOGIN`.  
\- For logs having `eventName` as `SendHeartbeat`:  
\- Set `metadata.event_type` to `STATUS_HEARTBEAT`.  
\- For logs haveing `eventName` as prefix `Initiate`, `Publish`, `Replace`, `Resume`, `Run`, `Submit`, `Suspend`,  
`Alter`, `Increase`, `Invite`, `Provision`, `Refresh`, `Report`, `Upgrade`, `Abort`, `Apply`, `Backup`, `Decrease`,  
`Merge`, `Retry`, `Rotate`, `Rotation`, `Transfer`, `Unassign`, `Analyze`, `Archive`, `Beta_`, `Clear`, `Configure`,  
`Confirm_`, `Do`, `Evaluate`, `Failover`, `Forgot`, `Lock`, `Migrate`, `O`, `Process`, `Promote`, `Release`, `Renew`,  
`Sign`, `Unarchive`, `Undeprecate`, `Unlock`, `Acknowledge`, `Approve`, `Connect`, `Continue`, `Decline`, `Deploy`,  
`Diagnostic`, `Drop`, `Exit`, `Finalize`, `Flush`, `Forget`, `Grant`, `Issue`, `Logout`, `Move`, `Opt`, `Pause`,  
`Rebuild`, `Redeem`, `Replicate`, `Restart`, `S`, `Save`, `Subscribe`, `Sync`, `Unlink`, `Unsubscribe`, `Unsuspend`,  
`Allow`, `Ato`, `Back`, `Backtrack`, `Bid`, `Bind`, `Build`, `Bundle`, `Clone`, `Close`, `Cognito`, `Console`, `Dispose`,  
`Dissociate`, `End`, `Enroll`, `Enter`, `Environment`, `Event_`, `Exclude`, `Global`, `Include`, `Index`, `Insert`, `Install`,  
`Invalidate`, `Join`, `Leave`, `Load`, `Managed`, `Mark`, `Monitor`, `Peer`, `Persist`, `Prepare`, `Pubkey`, `Purge`, `Push`,  
`Rebalance`, `Record`, `Recovery`, `Redact`, `Refuse`, `Reinvite`, `Reload`, `Rename`, `Respond`, `Resync`, `Retire`, `Reverse`,  
`Rollback`, `Schedule`, `Secret`, `Shutdown`, `Signal`, `Skip`, `Split`, `Stream`, `Swap`, `Switch`, `Toggle`, `Token_`,  
`Translate`, `Trim`, `Unauthorize`, `Undeploy`, `Unmonitor`, `Unpeer`, `Use`:  
\- Set `metadata.event_type` to `RESOURCE_WRITTEN`.  
\- For logs haveing `eventName` as prefix `Update`, `Associate`, `Disassociate`, `Modify`, `Set`, `Register`, `Deregister`,  
`Add`, `Remove`, `Enable`, `Disable`, `Send`, `Restore`, `Reset`, `Attach`, `Detach`, `Export`, `Copy`, `Tag`,  
`Untag`, `Execute`, `Purchase`, `Allocate`, `Deactivate`, `Post`, `Resend`, `Upload`, `Assign`, `Change`, `Define`,  
`Deprecate`, `Invoke`, "Revoke:  
\- Set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.   
2023-11-11 |  Enhancement:  
\- Initialize variables to null or empty, to avoid duplicate mappings.  
\- When `requestParameters.tagSpecificationSet.items.key` is `Hostname` , map to `target.hostname`.   
2023-10-27 |  Enhancement:  
For logs having `eventName` as `AssociateIamInstanceProfile`:  
\- Mapped `responseElements.AssociateIamInstanceProfileResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.name`.  
\- Mapped `responseElements.AssociateIamInstanceProfileResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.product_object_id`.  
\- Set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
\- Set `target.resource.resource_type` to `ACCESS_POLICY`.  
For logs having `eventName` as `DisassociateIamInstanceProfile`:  
\- Mapped `responseElements.DisassociateIamInstanceProfileResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.name`.  
\- Mapped `responseElements.DisassociateIamInstanceProfileResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.product_object_id`.  
\- Set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
\- Set `target.resource.resource_type` to `ACCESS_POLICY`.  
For logs having `eventName` as `ReplaceIamInstanceProfileAssociation`:  
\- Mapped `responseElements.ReplaceIamInstanceProfileAssociationResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.name`.  
\- Mapped `responseElements.ReplaceIamInstanceProfileAssociationResponse.iamInstanceProfileAssociation.instanceid` to `target.resource.product_object_id`.  
\- Set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
\- Set `target.resource.resource_type` to `ACCESS_POLICY`.  
Mapped `requestParameters` and `responseElements` JSON Object to `target.resource.attribute.labels`.  
Corrected typo error for `req.userIdentity.userName` from `req.userIdentity.username`.   
2023-10-13 |  Enhancement:  
\- For logs having `eventName` as `UpdateDetector`:  
\- Mapped `requestParameters.features.name` and `requestParameters.features.status` to `target.resource.attribute.labels`.  
\- For logs having `eventName` as `SendCommand`:  
\- Mapped `requestParameters.documentName` to `target.resource.product_object_id`.  
\- Mapped `responseElements.command.commandId` to `target.process.product_specific_object.id`.  
\- Mapped `metadata.event_type` to `PROCESS_LAUNCH`.  
\- Mapped `requestParameters.documentName` to `target.resource.name`.  
\- Mapped all the parameters in `requestParameters` and `responseElements` to `target.resource.attribute.labels`.  
\- For logs having `eventName` as `createAccountResult` map `event_type` as `USER_RESOURCE_ACCESS`.  
\- For logs having `eventName` as `createAccount` map `event_type` as `RESOURCE_CREATION`.   
2023-09-30 |  Enhancement: Add new mappings for the following fields:  
\- Mapped `req.requestParameters.durationSeconds` to `target.resource.attribute.labels`.  
\- Mapped `req.requestParameters.policyArns` to `target.resource.attribute.labels`.  
\- For logs having `eventName` as `GetParameter`, `GetParameters`, `GetParameterHistory`, `GetParametersByPath`, `DescribeParameters`:  
\- Mapped `metadata.event_type` to `RESOURCE_READ`.  
\- Mapped `req.requestParameters.withDecryption` to `security_result.detection_fields`.  
\- For logs having `eventName` as `DeleteParameters`,`DeleteParameter`, set `metadata.event_type` to `RESOURCE_DELETION`.  
\- For logs having `eventName` as `PutParameter`, set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
\- For logs having `eventName` as `EnableRegion` or `DisableRegion`, set `target.resource.name` from `req.requestParameters.map.RegionName`.  
\- For logs having `eventName` as `GetFederationToken`:  
\- Mapped `metadata.event_type` to `RESOURCE_READ`.  
\- Mapped `req.responseElements.federatedUser.arn` to `target.resource.name`.  
\- Mapped `req.responseElements.federatedUser.federatedUserId` to `target.user.userid`.  
\- Mapped `req.responseElements.packedPolicySize` to `security_result.detection_fields`.  
\- Mapped `req.responseElements.credentials.sessionToken` to `security_result.detection_fields`.   
2023-09-15 |  Enhancement: Add new mappings for the following fields:  
\- Mapped `requestParameters.userName` to `target.user.user_display_name`.  
\- Mapped `additionalEventData.SamlProviderArn` to `additional.fields`.  
\- Mapped `eventSource` to `metadata.ingestion_labels`.  
\- When value of `requestParameters.tagSpecificationSet.items.tags.key` is `Name`, then mapped `requestParameters.tagSpecificationSet.items.tags.value` to `target.resource.name`.   
2023-08-24 |  Enhancement:  
\- For logs having `eventName` as `CreateSubnet`, set `metadata.event_type` to `RESOURCE_CREATION`.  
\- Mapped `req.responseElements.subnet.subnetId` to `target.resource.attribute.labels`.  
\- Mapped `req.requestParameters.cidrBlock` to `target.resource.attribute.labels`.  
\- For logs having `eventName` as `DeleteSubnet`, set `metadata.event_type` to `RESOURCE_DELETION`.  
\- Mapped `req.requestParameters.subnetId` to `target.resource.attribute.labels`.   
2023-08-16 |  Enhancement:  
\- For logs having `eventName` as `DeleteSecret`, mapped `responseElements.arn` to `target.resource.name`.   
2023-08-02 |  Enhancement:  
\- For logs having `eventName` as `CreateTags`, mapped `metadata.event_type` to `RESOURCE_WRITTEN`.  
\- Mapped `responseElements.description` ,`requestParameters.name`,`requestParameters.tagSet.items`, `requestParameters.attributeType` to `target.resource.attribute.labels`.  
\- Set `metadata.event_type` to `RESOURCE_CREATION` for logs having the following `eventName`:  
`CreateNetworkAcl`,`CreateVolume`,`CreatePublishingDestination`,`CreateIPSet`,`CreateThreatIntelSet`,  
`CreateAddon`,`CreateRepository`,`CreateStack`,`CreateDomain`,`CreateCollection`,`CreateTable`,  
`CreateDBInstance`,`CreateDBCluster`,`CreateDBSnapshot`,`CreateDBClusterSnapshot`,`PutConfigRule`,  
`PutDeliveryChannel`,`CreateListener`,`CreateLoadBalancer`,`PutLoggingConfiguration`,`CreateTargetGroup`,  
`CreateWebACL`,`RequestCertificate`,`CreateCluster`  
\- Set `metadata.event_type` to `RESOURCE_WRITTEN for logs having the follow `eventName":  
`MoveAccount`,`PutEventSelectors`,`PutInsightSelectors`,`UpdateIPSet`,`UpdateThreatIntelSet`,`CreateTags`,  
`UpdateTable`,`ModifyDBInstance`,`StopDBInstance`,`StartDBInstance`,`RebootDBInstance`,  
`StartDBCluster`,`StopDBCluster`,`ModifyDBSnapshotAttribute`,`ModifyDBClusterSnapshotAttribute`,  
`AddListenerCertificates`,`ModifyLoadBalancerAttributes`,`SetSubnets`,`SetSecurityGroups`,  
`ModifyListener`,`UpdateWebACL`,`ResendValidationEmail`,`ModifyInstanceAttribute`,  
`StopInstances`,`StartInstances`,`RebootInstances`  
\- Set `metadata.event_type` to `RESOURCE_WRITTEN` for logs having the following `eventName`.  
`DeletePublishingDestination`,`DeleteIPSet`,`DeleteThreatIntelSet`,`DeleteRepository`,  
`DeleteStack`,`DeleteCollection`,`DeleteDomain`,`DeleteTable`,`DeleteDBInstance`,`DeleteDBCluster`,  
`DeleteDBSnapshot`,`DeleteDBClusterSnapshot`,`DeleteConfigRule`,`DeleteEvaluationResults`,  
`DeleteTargetGroup`,`DeleteLoadBalancer`,`DeleteListener`,`DeleteLoggingConfiguration`,  
`DeleteWebACL`,`DeleteCertificate`,`DeleteCluster`  
\- Set `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE` for logs having the following `eventName`:  
`AssociateWebACL`,`DisassociateWebACL`,`AttachGroupPolicy`,`PutBucketAcl`  
\- Set `metadata.event_type` to `RESOURCE_READ` for logs having the following `eventName`:  
`GetPasswordData`,`GetSessionToken`  
\- Mapped `target.resource.resource_type` and other unmapped fields for the above mentioned event names.   
2023-07-18 |  Enhancement:  
\- For logs with the following `eventName`, mapped `metadata.event_type` to `RESOURCE_CREATION`.  
`EnableMacie`,`ConnectDirectory`,`RunInstances`,`CreateImage`,`CreateOrganization`, `CreateNetworkInterface`,  
`StartSSO`,`CreateEmailIdentity`,`VerifyDomainIdentity`,`VerifyDomainDkim`,`VerifyEmailIdentity`,  
`CreateConfigurationSet`,`CreateSecret`,`ImportKeyPair`,`CreateAlias`,`CreateKey`,`CreateOrganizationalUnit`,  
`CreateNetworkAcl`,`CreateVolume`,`CreatePublishingDestination`,`CreateIPSet`,`CreateThreatIntelSet`  
\- For logs with the following `eventName`, mapped `metadata.event_type` to `RESOURCE_WRITTEN`.  
`UpdateMacieSession`,`PutAccountSendingAttributes`,`PutConfigurationSetSendingOptions`,`UpdateAccountSendingEnabled`,  
`UpdateConfigurationSetSendingEnabled`,`UpdateSecret`,`DisableKey`,`EnableKey`,`CancelKeyDeletion`,  
`MoveAccount`,`PutEventSelectors`,`PutInsightSelectors`,`UpdateIPSet`,`UpdateThreatIntelSet`  
\- For logs with the following `eventName`, mapped `metadata.event_type` to `RESOURCE_DELETION`.  
`DeleteSnapshot`,`DeleteDetector`,`DeleteFlowLogs`,`DeregisterImage`,`TerminateInstances`, `RESOURCE_DELETION`,  
`DeleteNetworkInterface`,`DeleteSSO`,`DeleteBucketPublicAccessBlock`,`DeleteAccountPublicAccessBlock`,  
`RemoveAccountFromOrganization`,`DeleteEmailIdentity`,`LeaveOrganization`,`DeleteConfigurationSet`,  
`DeleteSecret`,`DeleteKeyPair`,`DeleteAlias`,`ScheduleKeyDeletion`,`DeleteNetworkAcl`,  
`DeletePublishingDestination`,`DeleteIPSet`,`DeleteThreatIntelSet`  
\- For logs with the following `eventName`, mapped `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
`DetachRolePolicy`,`PutRolePolicy`,`PutResourcePolicy`,`PutCredentials`,`DeleteDirectory`,  
`AuthorizeSecurityGroupEgress`,`AuthorizeSecurityGroupIngress`,`RevokeSecurityGroupEgress`,`RevokeSecurityGroupIngress`,  
`ModifySnapshotAttribute`,`ModifyImageAttribute`,`CreateNetworkAclEntry`,`ReplaceNetworkAclAssociation`,`DeleteNetworkAclEntry`  
\- Mapped `target.resource.resource_type` and other unmapped fields for the above mentioned eventNames.  
\- Added a null check before mapping field `userIdentity.invokedBy`.   
2023-07-06 |  Enhancement:  
\- Added null check before mapping field `userIdentity.invokedBy`.  
\- Mapped `requestParameters.instanceType`,`requestParameters.instancesSet.items.0.minCount`,`requestParameters.instancesSet.items.0.maxCount` to `target.resource.attribute.labels`.   
2023-06-23 |  Enhancement: Mapped logs to more specific `metadata.event_type` based on the field `eventName`.  
\- Mapped `target.resource.resource_type` as `VIRTUAL_MACHINE`.  
\- Mapped `requestParameters.status`, `responseElements.certificate.status` to `target.resource.attribute.labels`.  
\- Mapped `requestParameters.instanceId` to `target.resource_ancestors.product_object_id`.  
\- Mapped `requestParameters.userName` to `target.user.userid`.  
\- Mapped `target.resource.name` and `target.resource.product_object_id` based upon keys present under each `eventName`.  
\- Mapped `userIdentity.arn` to `principal.resource.name`.  
\- Mapped `userIdentity.accountId` to `principal.resource.product_object_id`.  
\- For logs having `eventName` as following, mapped `metadata.event_type` to `RESOURCE_CREATION`.  
`CreateTrail`,`AllocateAddress`,`CreateVolume`,`CreateVirtualMFADevice`,`UploadSigningCertificate`,  
`CreateAccessKey`,`UploadSSHPublicKey`,`CreateServiceSpecificCredential`,`UploadCloudFrontPublicKey`,  
`CreateAnalyzer`,`CreateSAMLProvider`,`PutConfigurationRecorder`,`CreateRole`,`CreateInstanceProfile`,  
`CreateExportTask`,`CreateLogGroup`,`EnableSecurityHub`,`CreateEnvironment`,`CreateSession`,`CreateServiceLinkedRole`,  
`CreateSnapshot`,`CreateKeyPair`,`CreateSecurityGroup`,`CreateDetector`,`CreateFlowLogs`,  
`EnableMacie`,`ConnectDirectory`,`RunInstances`,`CreateImage`,`CreateOrganization`  
\- For logs having `eventName` as following, mapped `metadata.event_type` to `RESOURCE_WRITTEN`.  
`StartLogging`,`StopLogging`,`AssociateAddress`,`DisassociateAddress`,`DetachVolume`,  
`AttachVolume`,`ModifyVolume`,`EnableMFADevice`,`ResyncMFADevice`,`UpdateSigningCertificate`,  
`UpdateAccessKey`,`UpdateSSHPublicKey`,`ResetServiceSpecificCredential`,`UpdateServiceSpecificCredential`,  
`UpdateCloudFrontPublicKey`,`DisableRegion`,`EnableRegion`,`UpdateSAMLProvider`,`StartConfigurationRecorder`,  
`StopConfigurationRecorder`,`PutRetentionPolicy`,`PutDataProtectionPolicy`,`UpdateDetector`,`UpdateMacieSession`  
\- For logs having `eventName` as following, mapped `metadata.event_type` to `RESOURCE_DELETION`.  
`DeleteTrail`,`ReleaseAddress`,`DeleteVolume`,`DeactivateMFADevice`,`DeleteVirtualMFADevice`,  
`DeleteSigningCertificate`,`DeleteAccessKey`,`DeleteSSHPublicKey`,`DeleteServiceSpecificCredential`,  
`DeleteCloudFrontPublicKey`,`DeleteAnalyzer`,`DeleteSAMLProvider`,`DeleteConfigurationRecorder`,  
`DeletePolicy`,`DeleteRole`,`DeleteInstanceProfile`,`DeleteLogGroup`,`DisableSecurityHub`,`DisableMacie`,  
`DeleteSnapshot`,`DeleteDetector`,`DeleteFlowLogs`,`DeregisterImage`,`TerminateInstances`  
\- For logs having `eventName` as following, mapped `metadata.event_type` to `RESOURCE_PERMISSIONS_CHANGE`.  
`AttachUserPolicy`,`DetachUserPolicy`,`PutUserPolicy`,`DeleteUserPolicy`,  
`PutUserPermissionsBoundary`,`DeleteUserPermissionsBoundary`,`AttachRolePolicy`,  
`DetachRolePolicy`,`PutRolePolicy`,`PutResourcePolicy`,`PutCredentials`,`DeleteDirectory`  
2023-06-09 |  Enhancement:  
\- Modified the regex to identify the JSON Array logs.   
2023-06-07 |  Enhancement:  
\- Mapped all the `principal.user` fields to `target.user` for `eventName` as `ConsoleLogin`.   
2023-05-26 |  Enhancement:  
Parsed logs of different josn pattern.  
\- Mapped `cipherSuite` to `network.tls.cipher`.  
\- Mapped `requestID` to `target.resource.attribute.labels`.  
\- Mapped `assumedRoleId` to `security_result.about.resource.name`.  
\- Mapped `roleSessionName` to `target.resource.name`.  
\- Mapped `roleArn` to `target.resource.product_object_id`.  
\- Mapped `userAgent` to `network.http.user_agent`.  
\- Mapped `sourceIPAddress` to `principal.ip`.  
\- Mapped `sessionIssuer.userName` to `target.user.user_display_name`.  
\- Mapped `sessionIssuer.principalId` to `target.user.userid`.  
\- Mapped `userIdentity.accessKeyId` to `target.resource.product_object_id`.  
\- Mapped `userIdentity.arn` to `security_result.about.resource.id`.  
\- Mapped `req.detail.Longitude` to `_principal.location.region_longitude`.  
\- Mapped `req.detail.Latitude` to `_principal.location.region_latitude`.  
\- Mapped `detail.resourceType` to `target.resource.resource_subtype`.  
\- Set `security_result.alert_state` to `ALERTING`.  
\- Mapped `req.detail.recommendRemediation` to `security_result.action_details`.  
\- Mapped `eventLog.detail.eventName` to `metadata.product_event_type`.   
2023-02-23 |  Enhancement:  
\- Mapped `requestParameters.principalArn` to `principal.resource.name`.  
\- Mapped `resources.ARN` to `about.resource.name`.   
2022-11-24 |  Fix:  
\- Parsed new format logs that has configurationItem by mapping following fields.  
\- Mapped `configurationItem.awsAccountId` to `principal.user.userid`.  
\- Mapped `configurationItem.resourceId` to `target.resource.id`.  
\- Mapped `configurationItem.resourceType` to `target.resource.resource_subtype`  
\- Mapped `configurationItem.awsRegion` to `target.location.country_or_region`.  
\- Mapped `configurationItem.configurationItemCaptureTime` to `target.asset.attribute.creation_time`.  
\- Mapped `configurationItem.configurationItemStatus` to `target.asset.attribute.labels`.  
\- Mapped `configurationItems.ARN` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.availabilityZone` to `target.resource.attribute.cloud.availability_zone`.  
\- Mapped `configurationItems.awsRegion` to `target.location.country_or_region`.  
\- Mapped `configurationItems.awsAccountId` to `principal.user.userid`.  
\- Mapped `configurationItems.configuration.activityStreamStatus` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.configuration.allocatedStorage` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.configuration.autoMinorVersionUpgrade` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.configuration.backupRetentionPeriod` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.configuration.copyTagsToSnapshot` to `target.resource.attribute.labels`.  
\- Mapped `configurationItems.configuration.dbClusterResourceId` to `target.resource.product_object_id`.  
\- Mapped `configurationItems.configuration.masterUsername` to `principal.user.user_display_name`.  
\- Mapped `configurationItems.resourceName` to `target.resource.name`.   
2022-10-13 |  Enhancement:  
\- For `eventName`: `CreateAccessKey` mapped the field `responseElements.accessKey.accessKeyId` to `target.resource.product_object_id`.  
\- For `eventName`: `UpdateAccessKey` mapped the field `requestParameters.accessKeyId` to `target.resource.product_object_id`.  
\- For `eventName`: `DeleteAccessKey` mapped the field `requestParameters.accessKeyId` to `target.resource.product_object_id`.  
\- For `eventName`: `CreateUser` mapped the field `responseElements.user.userId` to `target.user.product_object_id`.  
\- Mapped the field `eventTime` to `metadata.collected_timestamp`.   
2022-07-27 |  Enhancement:  
\- Added eventType `QueryDatabase` and mapped it"s fields.  
\- Modified conditions for principal.ip or principal.host for handling new logs.  
\- Changed the mapping of `requestParameters.roleArn`, `requestParameters.registryId`, `resources.accountId` from `target.resource.id` to `target.resource.product_object_id`.  
\- Modified the parsing condition for `req_params` to extract the values.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `req.requestParameters.roleName` from `target.user.role_name` to `target.user.attribute.roles`.   
2022-07-06 |  \- Changed mapping of `req.awsRegion` from `_principal.location.country_or_region` to `_principal.location.name`.  
\- Modified event_type from `GENERIC_EVENT` to `USER_LOGIN` for eventName `AssumeRole`.  
\- Modified event_type from `GENERIC_EVENT` to `USER_RESOURCE_ACCESS` for eventNAme `PutImage` or `GetDownloadUrlForLayer` or `BatchGetImage`.  
\- Modified event_type from `GENERIC_EVENT` to `USER_RESOURCE_DELETION` for eventName `DeleteNetworkInterface`.   
2022-06-06 |  For eventName `CreateUser/DeleteUser`, modified condition for handling src mapping as existing one failed for new logs.  
Modified puserId field to handle new unparsed log.   
2022-05-27 |  Enhancement - Modified the value stored in metadata.product_name to `AWS CloudTrail`.   
2022-04-13 |  Enhancement to map following raw logs elements to UDM elements:  
Mapped field `requestParameters.PublicAccessBlockConfiguration.IgnorePublicAcls`, `requestParameters.CreateAccessPointRequest.PublicAccessBlockConfiguration.RestrictPublicBuckets`, `requestParameters.CreateAccessPointRequest.PublicAccessBlockConfiguration.BlockPublicPolicy`, `requestParameters.CreateAccessPointRequest.PublicAccessBlockConfiguration.BlockPublicAcls`, `requestParameters.CreateAccessPointRequest.PublicAccessBlockConfiguration.IgnorePublicAcls`, `additionalEventData.configRuleInputParameters.RestrictPublicBuckets`, `additionalEventData.configRuleInputParameters.BlockPublicPolicy`, `additionalEventData.configRuleInputParameters.BlockPublicAcls`, `additionalEventData.configRuleInputParameters.IgnorePublicAcls` to `target.resource.attribute.labels`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
