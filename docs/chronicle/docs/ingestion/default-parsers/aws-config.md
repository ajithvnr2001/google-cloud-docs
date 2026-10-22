---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config/
title: Collect AWS Config logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:27.287954+00:00
---

# Collect AWS Config logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Config logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Config logs to Google Security Operations using Amazon S3.

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against selected configurations. Configuration history files are delivered every six hours and configuration snapshots can be delivered on demand to an Amazon S3 bucket.

For more information, see [Collect AWS Config logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-config).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **AWS** (S3, IAM, Config)



## Configure AWS Config to deliver logs to Amazon S3

To configure AWS Config to record resource configurations and deliver them to an S3 bucket:

  1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).
  2. Go to **AWS Config > Settings**.
  3. If this is the first time setting up AWS Config, click **Get started**. Otherwise, click **Edit**.
  4. In the **Recording strategy** section, configure the following: 
     * **All resource types with customizable overrides** : Records all current and future supported resource types. You can configure the default recording frequency: 
       * **Continuous recording** : Records configuration changes continuously whenever a change occurs
       * **Daily recording** : Records one configuration item representing the most recent state over the last 24-hour period
     * **Specific resource types** : Choose individual resource types to record and set their frequency
  5. In the **Data governance** section, configure the following: 
     * **Data retention period** : Set the retention period (default is 7 years, minimum is 30 days)
     * **IAM role for AWS Config** : Select **Service-linked role** (recommended) or choose an existing IAM role
  6. In the **Delivery method** section, configure the following: 
     * **S3 bucket** : Select **Create a bucket** to create a new bucket, or select **Choose a bucket from your account** to use an existing bucket
     * **S3 bucket name** : Enter a name for the bucket (for example, `aws-config-logs`)
     * **Amazon SNS topic** (optional): Select **Stream configuration changes and notifications to an Amazon SNS topic** if you want notifications
  7. Click **Next**.
  8. In the **Rules** section, optionally configure managed rules. Click **Next**.
  9. Review your settings and click **Confirm**.



For more information, see [Setting up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html).

**Note:** AWS Config delivers configuration history files and configuration snapshots to the S3 bucket in the following path format: `s3://<bucket-name>/[optional-prefix]/AWSLogs/<account-id>/Config/`.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. If AWS Config created a new bucket, note the bucket **Name** and **Region** from **S3 > Buckets**.
  2. If you selected an existing bucket during AWS Config setup, note the bucket **Name** and **Region**.
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
  10. Click **Create access key**.
  11. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3ReadOnlyAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.

**Note:** **AmazonS3ReadOnlyAccess** is sufficient since Google SecOps only needs to read the log files. If you plan to use the deletion option for transferred files, use **AmazonS3FullAccess** instead.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New**
  * **Content Hub > Content Packs > Get Started**



## Configure a feed in Google SecOps to ingest AWS Config logs

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Config** log type.
  3. Select **Amazon S3 V2** as the **Source type**.
  4. Specify values for the following fields:

     * **S3 URI** : Enter the S3 URI for the AWS Config logs:
           
           s3://aws-config-logs/AWSLogs/
           

**Note:** Replace `aws-config-logs` with your actual bucket name. You can narrow the path to a specific account or region if needed (for example, `s3://aws-config-logs/AWSLogs/123456789012/Config/us-east-1/`).
     * **Source deletion option** : Select the deletion option according to your preference

     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Access Key ID** : User access key with access to the S3 bucket

     * **Secret Access Key** : User secret key with access to the S3 bucket

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the IAM user.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  5. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AccountId_label` | `additional.fields` | Merged  
`AllSupported_label` | `additional.fields` | Merged  
`AuthenticationType_label` | `additional.fields` | Merged  
`DeploymentDurationInMinutes_label` | `additional.fields` | Merged  
`DomainName_label` | `additional.fields` | Merged  
`EnableTerminationProtection_label` | `additional.fields` | Merged  
`Enable_label` | `additional.fields` | Merged  
`EventBusName_label` | `additional.fields` | Merged  
`EventPattern_detail_eventSource_label` | `additional.fields` | Merged  
`EventPattern_detail_managementEvent_label` | `additional.fields` | Merged  
`EventPattern_detail_type_label` | `additional.fields` | Merged  
`EventPattern_source_label` | `additional.fields` | Merged  
`FinalBakeTimeInMinutes_label` | `additional.fields` | Merged  
`FindingPublishingFrequency_label` | `additional.fields` | Merged  
`GrowthFactor_label` | `additional.fields` | Merged  
`GrowthType_label` | `additional.fields` | Merged  
`Id_label` | `additional.fields` | Merged  
`IncludeGlobalResourceTypes_label` | `additional.fields` | Merged  
`Kubernetes_AuditLogs_Enable_label` | `additional.fields` | Merged  
`Name_label` | `additional.fields` | Merged  
`Reason_label` | `additional.fields` | Merged  
`RecordingStrategy_UseOnly_label` | `additional.fields` | Merged  
`ReplicateTo_label` | `additional.fields` | Merged  
`ResolverRuleAssociationId_label` | `additional.fields` | Merged  
`ResolverRuleId_label` | `additional.fields` | Merged  
`S3Logs_Enable_label` | `additional.fields` | Merged  
`ServiceType_label` | `additional.fields` | Merged  
`StandardsArn_label` | `additional.fields` | Merged  
`StandardsControlArn_label` | `additional.fields` | Merged  
`State_label` | `additional.fields` | Merged  
`TlsConfig_SecurityPolicy_label` | `additional.fields` | Merged  
`VPCId_label` | `additional.fields` | Merged  
`WorkGroupConfiguration_EnforceWorkGroupConfiguration_label` | `additional.fields` | Merged  
`WorkGroupConfiguration_EngineVersion_EffectiveEngineVersion_label` | `additional.fields` | Merged  
`WorkGroupConfiguration_EngineVersion_SelectedEngineVersion_label` | `additional.fields` | Merged  
`WorkGroupConfiguration_PublishCloudWatchMetricsEnabled_label` | `additional.fields` | Merged  
`WorkGroupConfiguration_RequesterPaysEnabled_label` | `additional.fields` | Merged  
`accountState_resourceState_codeRepository_status_label` | `additional.fields` | Merged  
`accountState_resourceState_ec2_status_label` | `additional.fields` | Merged  
`accountState_resourceState_ecr_status_label` | `additional.fields` | Merged  
`accountState_resourceState_lambdaCode_status_label` | `additional.fields` | Merged  
`accountState_resourceState_lambda_status_label` | `additional.fields` | Merged  
`accountState_state_status_label` | `additional.fields` | Merged  
`asso_cidr_label` | `additional.fields` | Merged  
`asso_id_label` | `additional.fields` | Merged  
`asso_state_label` | `additional.fields` | Merged  
`associationState_state_label` | `additional.fields` | Merged  
`canaryInterval_label` | `additional.fields` | Merged  
`canaryPercentage_label` | `additional.fields` | Merged  
`cidrBlock_label` | `additional.fields` | Merged  
`computePlatform_label` | `additional.fields` | Merged  
`config_description_label` | `additional.fields` | Merged  
`configurationItemVersion_label` | `additional.fields` | Merged  
`configurationStateId_label` | `additional.fields` | Merged  
`createdTime_label` | `additional.fields` | Merged  
`defaultCooldown_label` | `additional.fields` | Merged  
`deletionPolicy_label` | `additional.fields` | Merged  
`deploymentConfigId_label` | `additional.fields` | Merged  
`description_label` | `additional.fields` | Merged  
`desiredCapacity_label` | `additional.fields` | Merged  
`destinationCidrBlock_label` | `additional.fields` | Merged  
`digest_s3_bucket_label` | `additional.fields` | Merged  
`digest_s3_object_label` | `additional.fields` | Merged  
`digest_signature_algorithm_label` | `additional.fields` | Merged  
`disableRollback_label` | `additional.fields` | Merged  
`egress_label` | `additional.fields` | Merged  
`feature_label` | `additional.fields` | Merged  
`field_` | `additional.fields` | Merged  
`field_value` | `additional.fields` | Merged  
`fromPort_label` | `additional.fields` | Merged  
`gatewayId_label` | `additional.fields` | Merged  
`groupId_label` | `additional.fields` | Merged  
`instanceStatus_label` | `additional.fields` | Merged  
`ipProtocol_label` | `additional.fields` | Merged  
`ipProtocol_label_egress` | `additional.fields` | Merged  
`isDefault_label` | `additional.fields` | Merged  
`lastUpdatedTime_label` | `additional.fields` | Merged  
`lastUpdatedTimestamp_label` | `additional.fields` | Merged  
`logicalResourceId_label` | `additional.fields` | Merged  
`main_label` | `additional.fields` | Merged  
`managementEvent_label` | `additional.fields` | Merged  
`maxSize_label` | `additional.fields` | Merged  
`max_results_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (5 total, e.g. `Records` → `managementEvent_label`, `Records` → `readOnly_labe...  
`mfaAuthenticated_label` | `additional.fields` | Merged  
`minSize_label` | `additional.fields` | Merged  
`minimumHealthyHosts_type_label` | `additional.fields` | Merged  
`minimumHealthyHosts_value_label` | `additional.fields` | Merged  
`networkAclId_label` | `additional.fields` | Merged  
`newInstancesProtectedFromScaleIn_label` | `additional.fields` | Merged  
`origin_label` | `additional.fields` | Merged  
`output_desc_label` | `additional.fields` | Merged  
`output_label` | `additional.fields` | Merged  
`parameter_label` | `additional.fields` | Merged  
`physicalResourceId_label` | `additional.fields` | Merged  
`protocol_label` | `additional.fields` | Merged  
`readOnly_label` | `additional.fields` | Merged  
`relationship_resource_ids` | `additional.fields` | Merged  
`relationship_resource_names` | `additional.fields` | Merged  
`relationship_resource_types` | `additional.fields` | Merged  
`resourceStatus_label` | `additional.fields` | Merged  
`resourceType_label_` | `additional.fields` | Merged  
`routeTableAssociationId_label` | `additional.fields` | Merged  
`routeTableId_label` | `additional.fields` | Merged  
`ruleAction_label` | `additional.fields` | Merged  
`ruleNumber_label` | `additional.fields` | Merged  
`serviceLinkedRoleARN_label` | `additional.fields` | Merged  
`session_issuer_type_label` | `additional.fields` | Merged  
`stackDriftStatus_label` | `additional.fields` | Merged  
`stackId_label` | `additional.fields` | Merged  
`stackName_label` | `additional.fields` | Merged  
`stackResourceDriftStatus_label` | `additional.fields` | Merged  
`stackStatus_label` | `additional.fields` | Merged  
`state_label` | `additional.fields` | Merged  
`toPort_label` | `additional.fields` | Merged  
`trafficRoutingConfig_type_label` | `additional.fields` | Merged  
`unsupportedResources_resourceId_label` | `additional.fields` | Merged  
`unsupportedResources_resourceType_label` | `additional.fields` | Merged  
`updateReplacePolicy_label` | `additional.fields` | Merged  
`userId_label` | `additional.fields` | Merged  
`vpczoneIdentifier_label` | `additional.fields` | Merged  
`has_principal_user` | `extensions.auth.type` | Mapped: `true` → `MACHINE`  
`message` | `extensions.auth.type` | Mapped: `Records` → `MACHINE`  
`message` | `intermediary` | Mapped: `Records` → `intermediary`  
`record.userIdentity.sessionContext.sessionIssuer.accountId` | `intermediary.cloud.project.id` | Directly mapped  
`record.userIdentity.sessionContext.sessionIssuer.arn` | `intermediary.resource.name` | Directly mapped  
`record.userIdentity.sessionContext.sessionIssuer.principalId` | `intermediary.resource.product_object_id` | Directly mapped  
`messageType` | `metadata.description` | Directly mapped  
`record.eventCategory` | `metadata.description` | Directly mapped  
`configItem.resourceCreationTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`configurationItem.configurationItemCaptureTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`configuration_Item_CaptureTime` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`digestEndTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd'T'HH:mm:ssZ`  
`digestStartTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd'T'HH:mm:ssZ`  
`record.eventTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd'T'HH:mm:ss'Z'`  
`record.requestParameters.endTime` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`record.requestParameters.startTime` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`record.userIdentity.sessionContext.attributes.creationDate` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`resource_Creation_Time` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `USER_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped: `Records` → `USER_LOGIN`, `Records` → `USER_UNCATEGORIZED`, `Records` → `STATUS_UPDA...  
`config_snapshot_id_value` | `metadata.id` | Directly mapped  
`message` | `metadata.id` | Mapped: `Records` → `bytes`  
`record.eventID` | `metadata.id` | Directly mapped  
`record.eventName` | `metadata.product_event_type` | Directly mapped  
`record.requestID` | `metadata.product_log_id` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `Records` → `AWS Config`  
`configurationItem.configurationItemVersion` | `metadata.product_version` | Directly mapped  
`file_version_value` | `metadata.product_version` | Directly mapped  
`record.eventVersion` | `metadata.product_version` | Directly mapped  
`message` | `metadata.vendor_name` | Mapped: `Records` → `AMAZON`  
`message` | `network.http.parsed_user_agent` | Mapped: `Records` → `parseduseragent`  
`record.userAgent` | `network.http.parsed_user_agent` | Directly mapped  
`record.userAgent` | `network.http.user_agent` | Directly mapped  
`record.tlsDetails.cipherSuite` | `network.tls.cipher` | Directly mapped  
`record.tlsDetails.tlsVersion` | `network.tls.version` | Directly mapped  
`record.sourceIPAddress` | `principal.asset.hostname` | Directly mapped  
`ip_val` | `principal.asset.ip` | Merged  
`ip_val_1` | `principal.asset.ip` | Merged  
`message` | `principal.asset.ip` | Mapped: `Records` → `source_ip`  
`source_ip` | `principal.asset.ip` | Merged  
`record.userIdentity.type` | `principal.cloud.project.type` | Directly mapped  
`record.sourceIPAddress` | `principal.hostname` | Directly mapped  
`ip_val` | `principal.ip` | Merged  
`ip_val_1` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `Records` → `source_ip`  
`source_ip` | `principal.ip` | Merged  
`availabilityZone_1` | `principal.location.country_or_region` | Directly mapped  
`index` | `principal.location.country_or_region` | Directly mapped  
`record.awsRegion` | `principal.location.country_or_region` | Directly mapped  
`availabilityZone_1_label` | `principal.resource.attribute.labels` | Merged  
`name_label` | `principal.resource.attribute.labels` | Merged  
`resourceId_label` | `principal.resource.attribute.labels` | Merged  
`resourceType_label` | `principal.resource.attribute.labels` | Merged  
`record.userIdentity.arn` | `principal.resource.name` | Directly mapped  
`resource.ARN` | `principal.resource.name` | Directly mapped  
`resource.type` | `principal.resource.type` | Directly mapped  
`email` | `principal.user.email_addresses` | Merged  
`record.userIdentity.principalId` | `principal.user.product_object_id` | Directly mapped  
`configItem.tags.Contact` | `principal.user.user_display_name` | Directly mapped  
`record.userIdentity.sessionContext.sessionIssuer.userName` | `principal.user.user_display_name` | Directly mapped  
`user_name` | `principal.user.user_display_name` | Renamed/mapped  
`awsAccountId` | `principal.user.userid` | Directly mapped  
`configItem.awsAccountId` | `principal.user.userid` | Directly mapped  
`configurationItem.awsAccountId` | `principal.user.userid` | Directly mapped  
`record.userIdentity.accessKeyId` | `principal.user.userid` | Directly mapped  
`resource.accountId` | `principal.user.userid` | Directly mapped  
`message` | `security_result` | Mapped: `Records` → `security_result`  
`security_result_outer` | `security_result` | Merged  
`security_result_rule_list` | `security_result` | Merged  
`keySpec_label` | `security_result.about.labels` | Merged  
`message` | `security_result.about.labels` | Mapped: `Records` → `keySpec_label`  
`record.requestParameters.keyId` | `security_result.about.resource.id` | Directly mapped  
`record.eventSource` | `security_result.about.resource.name` | Directly mapped  
`attribute_key_value_label` | `security_result.detection_fields` | Merged  
`aws_cloudtrail_arn_label` | `security_result.detection_fields` | Merged  
`aws_s3_arn_label` | `security_result.detection_fields` | Merged  
`clientProvidedHostHeader_label` | `security_result.detection_fields` | Merged  
`digest_public_key_fingerprint_label` | `security_result.detection_fields` | Merged  
`eventType_label` | `security_result.detection_fields` | Merged  
`hashAlgorithm_label` | `security_result.detection_fields` | Merged  
`hashValue_label` | `security_result.detection_fields` | Merged  
`invokedBy_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (6 total, e.g. `Records` → `eventType_label`, `Records` → `attribute_key_value...  
`s3Bucket_label` | `security_result.detection_fields` | Merged  
`s3Object_label` | `security_result.detection_fields` | Merged  
`message` | `target.asset.attribute.cloud.environment` | Mapped: `Records` → `AMAZON_WEB_SERVICES`  
`relationship.resourceId` | `target.asset.attribute.cloud.vpc.id` | Directly mapped  
`attribute_label` | `target.asset.attribute.labels` | Merged  
`configItem.awsRegion` | `target.asset.location.country_or_region` | Directly mapped  
`configurationItem.awsRegion` | `target.asset.location.country_or_region` | Directly mapped  
`message` | `target.asset.platform_software.platform` | Mapped: `Windows` → `WINDOWS`, `(Linux/LINUX)` → `LINUX`  
`configItem.configuration.privateIpAddress` | `target.ip` | Merged  
`configItem.configuration.publicIpAddress` | `target.ip` | Merged  
`configItem.availabilityZone` | `target.location.name` | Directly mapped  
`ARN_label` | `target.resource.attribute.labels` | Merged  
`KeyspaceName_label` | `target.resource.attribute.labels` | Merged  
`autoScalingGroupARN_label` | `target.resource.attribute.labels` | Merged  
`autoScalingGroupName_label` | `target.resource.attribute.labels` | Merged  
`awsAccountId_label` | `target.resource.attribute.labels` | Merged  
`configurationStateId_label` | `target.resource.attribute.labels` | Merged  
`configurationStateMd5Hash_label` | `target.resource.attribute.labels` | Merged  
`granularity_label` | `target.resource.attribute.labels` | Merged  
`healthCheckGracePeriod_label` | `target.resource.attribute.labels` | Merged  
`healthCheckType_label` | `target.resource.attribute.labels` | Merged  
`launchTemplateId_label` | `target.resource.attribute.labels` | Merged  
`launchTemplateName_label` | `target.resource.attribute.labels` | Merged  
`metric_label` | `target.resource.attribute.labels` | Merged  
`terminationPolicies_label` | `target.resource.attribute.labels` | Merged  
`version_label` | `target.resource.attribute.labels` | Merged  
`configItem.ARN` | `target.resource.id` | Directly mapped  
`configItem.resourceId` | `target.resource.id` | Directly mapped  
`configurationItem.resourceId` | `target.resource.id` | Directly mapped  
`configItem.resourceName` | `target.resource.name` | Directly mapped  
`record.recipientAccountId` | `target.resource.product_object_id` | Directly mapped  
`configItem.resourceType` | `target.resource.resource_subtype` | Directly mapped  
`configurationItem.resourceType` | `target.resource.resource_subtype` | Directly mapped  
`message` | `target.resource.resource_type` | Mapped: `Records` → `VIRTUAL_MACHINE`  
`record.userIdentity.accountId` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.id` | Constant: `bytes`  
N/A | `metadata.product_name` | Constant: `AWS Config`  
N/A | `metadata.vendor_name` | Constant: `AMAZON`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
N/A | `target.asset.attribute.cloud.environment` | Constant: `AMAZON_WEB_SERVICES`  
N/A | `target.asset.attribute.cloud.vpc.resource_type` | Constant: `VPC_NETWORK`  
N/A | `target.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `target.resource.resource_type` | Constant: `VIRTUAL_MACHINE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-config-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
