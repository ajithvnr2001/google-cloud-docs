---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedDetails (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:40.326886+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedDetails (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedDetails (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::FeedDetails.

Additional details of the feed, these details are dynamic and will be different for each of the feeds.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #amazon_kinesis_firehose_settings
    
    
    def amazon_kinesis_firehose_settings() -> ::Google::Cloud::Chronicle::V1::AmazonKinesisFirehoseSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonKinesisFirehoseSettings)) — Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_kinesis_firehose_settings=
    
    
    def amazon_kinesis_firehose_settings=(value) -> ::Google::Cloud::Chronicle::V1::AmazonKinesisFirehoseSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonKinesisFirehoseSettings)) — Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonKinesisFirehoseSettings)) — Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_s3_settings
    
    
    def amazon_s3_settings() -> ::Google::Cloud::Chronicle::V1::AmazonS3Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonS3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3Settings)) — Amazon S3 settings.

Note: The following fields are mutually exclusive: `amazon_s3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_s3_settings=
    
    
    def amazon_s3_settings=(value) -> ::Google::Cloud::Chronicle::V1::AmazonS3Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AmazonS3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3Settings)) — Amazon S3 settings.

Note: The following fields are mutually exclusive: `amazon_s3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonS3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3Settings)) — Amazon S3 settings.

Note: The following fields are mutually exclusive: `amazon_s3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_s3_v2_settings
    
    
    def amazon_s3_v2_settings() -> ::Google::Cloud::Chronicle::V1::AmazonS3V2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonS3V2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3V2Settings)) — Settings for S3 Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_s3_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_s3_v2_settings=
    
    
    def amazon_s3_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::AmazonS3V2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AmazonS3V2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3V2Settings)) — Settings for S3 Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_s3_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonS3V2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonS3V2Settings)) — Settings for S3 Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_s3_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_sqs_settings
    
    
    def amazon_sqs_settings() -> ::Google::Cloud::Chronicle::V1::AmazonSQSSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonSQSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSSettings)) — Amazon SQS settings.

Note: The following fields are mutually exclusive: `amazon_sqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_sqs_settings=
    
    
    def amazon_sqs_settings=(value) -> ::Google::Cloud::Chronicle::V1::AmazonSQSSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AmazonSQSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSSettings)) — Amazon SQS settings.

Note: The following fields are mutually exclusive: `amazon_sqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonSQSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSSettings)) — Amazon SQS settings.

Note: The following fields are mutually exclusive: `amazon_sqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_sqs_v2_settings
    
    
    def amazon_sqs_v2_settings() -> ::Google::Cloud::Chronicle::V1::AmazonSQSV2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonSQSV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSV2Settings)) — Settings for SQS Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_sqs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #amazon_sqs_v2_settings=
    
    
    def amazon_sqs_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::AmazonSQSV2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AmazonSQSV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSV2Settings)) — Settings for SQS Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_sqs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AmazonSQSV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AmazonSQSV2Settings)) — Settings for SQS Omniflow feeds.

Note: The following fields are mutually exclusive: `amazon_sqs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #anomali_settings
    
    
    def anomali_settings() -> ::Google::Cloud::Chronicle::V1::AnomaliIocSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AnomaliIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AnomaliIocSettings)) — Anomali IOC settings.

Note: The following fields are mutually exclusive: `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #anomali_settings=
    
    
    def anomali_settings=(value) -> ::Google::Cloud::Chronicle::V1::AnomaliIocSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AnomaliIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AnomaliIocSettings)) — Anomali IOC settings.

Note: The following fields are mutually exclusive: `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AnomaliIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AnomaliIocSettings)) — Anomali IOC settings.

Note: The following fields are mutually exclusive: `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #asset_namespace
    
    
    def asset_namespace() -> ::String

**Returns**

  * (::String) — The asset namespace to apply to all logs ingested through this feed. 



### #asset_namespace=
    
    
    def asset_namespace=(value) -> ::String

**Parameter**

  * **value** (::String) — The asset namespace to apply to all logs ingested through this feed. 



**Returns**

  * (::String) — The asset namespace to apply to all logs ingested through this feed. 



### #aws_ec2_hosts_settings
    
    
    def aws_ec2_hosts_settings() -> ::Google::Cloud::Chronicle::V1::AWSEC2HostsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2HostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2HostsSettings)) — AWS EC2 Hosts settings.

Note: The following fields are mutually exclusive: `aws_ec2_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_ec2_hosts_settings=
    
    
    def aws_ec2_hosts_settings=(value) -> ::Google::Cloud::Chronicle::V1::AWSEC2HostsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AWSEC2HostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2HostsSettings)) — AWS EC2 Hosts settings.

Note: The following fields are mutually exclusive: `aws_ec2_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2HostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2HostsSettings)) — AWS EC2 Hosts settings.

Note: The following fields are mutually exclusive: `aws_ec2_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_ec2_instances_settings
    
    
    def aws_ec2_instances_settings() -> ::Google::Cloud::Chronicle::V1::AWSEC2InstancesSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2InstancesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2InstancesSettings)) — AWS EC2 Instances settings.

Note: The following fields are mutually exclusive: `aws_ec2_instances_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_ec2_instances_settings=
    
    
    def aws_ec2_instances_settings=(value) -> ::Google::Cloud::Chronicle::V1::AWSEC2InstancesSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AWSEC2InstancesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2InstancesSettings)) — AWS EC2 Instances settings.

Note: The following fields are mutually exclusive: `aws_ec2_instances_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2InstancesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2InstancesSettings)) — AWS EC2 Instances settings.

Note: The following fields are mutually exclusive: `aws_ec2_instances_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_ec2_vpcs_settings
    
    
    def aws_ec2_vpcs_settings() -> ::Google::Cloud::Chronicle::V1::AWSEC2VpcsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2VpcsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2VpcsSettings)) — AWS EC2 Vpcs settings.

Note: The following fields are mutually exclusive: `aws_ec2_vpcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_ec2_vpcs_settings=
    
    
    def aws_ec2_vpcs_settings=(value) -> ::Google::Cloud::Chronicle::V1::AWSEC2VpcsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AWSEC2VpcsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2VpcsSettings)) — AWS EC2 Vpcs settings.

Note: The following fields are mutually exclusive: `aws_ec2_vpcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSEC2VpcsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSEC2VpcsSettings)) — AWS EC2 Vpcs settings.

Note: The following fields are mutually exclusive: `aws_ec2_vpcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_iam_settings
    
    
    def aws_iam_settings() -> ::Google::Cloud::Chronicle::V1::AWSIAMSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSIAMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSIAMSettings)) — AWS IAM settings.

Note: The following fields are mutually exclusive: `aws_iam_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #aws_iam_settings=
    
    
    def aws_iam_settings=(value) -> ::Google::Cloud::Chronicle::V1::AWSIAMSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AWSIAMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSIAMSettings)) — AWS IAM settings.

Note: The following fields are mutually exclusive: `aws_iam_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AWSIAMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AWSIAMSettings)) — AWS IAM settings.

Note: The following fields are mutually exclusive: `aws_iam_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_audit_settings
    
    
    def azure_ad_audit_settings() -> ::Google::Cloud::Chronicle::V1::AzureADAuditSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADAuditSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADAuditSettings)) — Azure AD Audit settings.

Note: The following fields are mutually exclusive: `azure_ad_audit_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_audit_settings=
    
    
    def azure_ad_audit_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureADAuditSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureADAuditSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADAuditSettings)) — Azure AD Audit settings.

Note: The following fields are mutually exclusive: `azure_ad_audit_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADAuditSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADAuditSettings)) — Azure AD Audit settings.

Note: The following fields are mutually exclusive: `azure_ad_audit_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_context_settings
    
    
    def azure_ad_context_settings() -> ::Google::Cloud::Chronicle::V1::AzureADContextSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADContextSettings)) — Azure AD Context settings.

Note: The following fields are mutually exclusive: `azure_ad_context_settings`, `anomali_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_context_settings=
    
    
    def azure_ad_context_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureADContextSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureADContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADContextSettings)) — Azure AD Context settings.

Note: The following fields are mutually exclusive: `azure_ad_context_settings`, `anomali_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADContextSettings)) — Azure AD Context settings.

Note: The following fields are mutually exclusive: `azure_ad_context_settings`, `anomali_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_settings
    
    
    def azure_ad_settings() -> ::Google::Cloud::Chronicle::V1::AzureADSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADSettings)) — Azure AD settings.

Note: The following fields are mutually exclusive: `azure_ad_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_ad_settings=
    
    
    def azure_ad_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureADSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureADSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADSettings)) — Azure AD settings.

Note: The following fields are mutually exclusive: `azure_ad_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureADSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureADSettings)) — Azure AD settings.

Note: The following fields are mutually exclusive: `azure_ad_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_blob_store_settings
    
    
    def azure_blob_store_settings() -> ::Google::Cloud::Chronicle::V1::AzureBlobStoreSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureBlobStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreSettings)) — Azure Blob Storage settings.

Note: The following fields are mutually exclusive: `azure_blob_store_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_blob_store_settings=
    
    
    def azure_blob_store_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureBlobStoreSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureBlobStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreSettings)) — Azure Blob Storage settings.

Note: The following fields are mutually exclusive: `azure_blob_store_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureBlobStoreSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreSettings)) — Azure Blob Storage settings.

Note: The following fields are mutually exclusive: `azure_blob_store_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_blob_store_v2_settings
    
    
    def azure_blob_store_v2_settings() -> ::Google::Cloud::Chronicle::V1::AzureBlobStoreV2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureBlobStoreV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreV2Settings)) — Settings for Azure Blobstore Omniflow feeds.

Note: The following fields are mutually exclusive: `azure_blob_store_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_blob_store_v2_settings=
    
    
    def azure_blob_store_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureBlobStoreV2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureBlobStoreV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreV2Settings)) — Settings for Azure Blobstore Omniflow feeds.

Note: The following fields are mutually exclusive: `azure_blob_store_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureBlobStoreV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureBlobStoreV2Settings)) — Settings for Azure Blobstore Omniflow feeds.

Note: The following fields are mutually exclusive: `azure_blob_store_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_event_hub_settings
    
    
    def azure_event_hub_settings() -> ::Google::Cloud::Chronicle::V1::AzureEventHubSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureEventHubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureEventHubSettings)) — Settings for Omniflow based native ingestion from azure event hub.

Note: The following fields are mutually exclusive: `azure_event_hub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_event_hub_settings=
    
    
    def azure_event_hub_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureEventHubSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureEventHubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureEventHubSettings)) — Settings for Omniflow based native ingestion from azure event hub.

Note: The following fields are mutually exclusive: `azure_event_hub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureEventHubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureEventHubSettings)) — Settings for Omniflow based native ingestion from azure event hub.

Note: The following fields are mutually exclusive: `azure_event_hub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_mdm_intune_settings
    
    
    def azure_mdm_intune_settings() -> ::Google::Cloud::Chronicle::V1::AzureMDMIntuneSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureMDMIntuneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureMDMIntuneSettings)) — Azure MDM Intune settings.

Note: The following fields are mutually exclusive: `azure_mdm_intune_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_mdm_intune_settings=
    
    
    def azure_mdm_intune_settings=(value) -> ::Google::Cloud::Chronicle::V1::AzureMDMIntuneSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::AzureMDMIntuneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureMDMIntuneSettings)) — Azure MDM Intune settings.

Note: The following fields are mutually exclusive: `azure_mdm_intune_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::AzureMDMIntuneSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-AzureMDMIntuneSettings)) — Azure MDM Intune settings.

Note: The following fields are mutually exclusive: `azure_mdm_intune_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_passage_settings
    
    
    def cloud_passage_settings() -> ::Google::Cloud::Chronicle::V1::CloudPassageSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CloudPassageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CloudPassageSettings)) — Cloud Passage settings.

Note: The following fields are mutually exclusive: `cloud_passage_settings`, `anomali_settings`, `azure_ad_context_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_passage_settings=
    
    
    def cloud_passage_settings=(value) -> ::Google::Cloud::Chronicle::V1::CloudPassageSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CloudPassageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CloudPassageSettings)) — Cloud Passage settings.

Note: The following fields are mutually exclusive: `cloud_passage_settings`, `anomali_settings`, `azure_ad_context_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::CloudPassageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CloudPassageSettings)) — Cloud Passage settings.

Note: The following fields are mutually exclusive: `cloud_passage_settings`, `anomali_settings`, `azure_ad_context_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cortex_xdr_settings
    
    
    def cortex_xdr_settings() -> ::Google::Cloud::Chronicle::V1::CortexXDRSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CortexXDRSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CortexXDRSettings)) — Cortex XDR settings.

Note: The following fields are mutually exclusive: `cortex_xdr_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cortex_xdr_settings=
    
    
    def cortex_xdr_settings=(value) -> ::Google::Cloud::Chronicle::V1::CortexXDRSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CortexXDRSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CortexXDRSettings)) — Cortex XDR settings.

Note: The following fields are mutually exclusive: `cortex_xdr_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::CortexXDRSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CortexXDRSettings)) — Cortex XDR settings.

Note: The following fields are mutually exclusive: `cortex_xdr_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #crowdstrike_alerts_settings
    
    
    def crowdstrike_alerts_settings() -> ::Google::Cloud::Chronicle::V1::CrowdStrikeAlertsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CrowdStrikeAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeAlertsSettings)) — CrowdStrike Alerts API settings.

Note: The following fields are mutually exclusive: `crowdstrike_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #crowdstrike_alerts_settings=
    
    
    def crowdstrike_alerts_settings=(value) -> ::Google::Cloud::Chronicle::V1::CrowdStrikeAlertsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CrowdStrikeAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeAlertsSettings)) — CrowdStrike Alerts API settings.

Note: The following fields are mutually exclusive: `crowdstrike_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::CrowdStrikeAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeAlertsSettings)) — CrowdStrike Alerts API settings.

Note: The following fields are mutually exclusive: `crowdstrike_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #crowdstrike_detects_settings
    
    
    def crowdstrike_detects_settings() -> ::Google::Cloud::Chronicle::V1::CrowdStrikeDetectsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CrowdStrikeDetectsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeDetectsSettings)) — CrowdStrike Detects API settings.

Note: The following fields are mutually exclusive: `crowdstrike_detects_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #crowdstrike_detects_settings=
    
    
    def crowdstrike_detects_settings=(value) -> ::Google::Cloud::Chronicle::V1::CrowdStrikeDetectsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CrowdStrikeDetectsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeDetectsSettings)) — CrowdStrike Detects API settings.

Note: The following fields are mutually exclusive: `crowdstrike_detects_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::CrowdStrikeDetectsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CrowdStrikeDetectsSettings)) — CrowdStrike Detects API settings.

Note: The following fields are mutually exclusive: `crowdstrike_detects_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_api_settings
    
    
    def custom_api_settings() -> ::Google::Cloud::Chronicle::V1::CustomAPISettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CustomAPISettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPISettings)) — Settings for Custom API (Codeless) Feeds.

Note: The following fields are mutually exclusive: `custom_api_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_api_settings=
    
    
    def custom_api_settings=(value) -> ::Google::Cloud::Chronicle::V1::CustomAPISettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CustomAPISettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPISettings)) — Settings for Custom API (Codeless) Feeds.

Note: The following fields are mutually exclusive: `custom_api_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::CustomAPISettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPISettings)) — Settings for Custom API (Codeless) Feeds.

Note: The following fields are mutually exclusive: `custom_api_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dummy_log_type_settings
    
    
    def dummy_log_type_settings() -> ::Google::Cloud::Chronicle::V1::DummyLogTypeSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DummyLogTypeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DummyLogTypeSettings)) — DummyLogType Settings.

Note: The following fields are mutually exclusive: `dummy_log_type_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dummy_log_type_settings=
    
    
    def dummy_log_type_settings=(value) -> ::Google::Cloud::Chronicle::V1::DummyLogTypeSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DummyLogTypeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DummyLogTypeSettings)) — DummyLogType Settings.

Note: The following fields are mutually exclusive: `dummy_log_type_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::DummyLogTypeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DummyLogTypeSettings)) — DummyLogType Settings.

Note: The following fields are mutually exclusive: `dummy_log_type_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duo_auth_settings
    
    
    def duo_auth_settings() -> ::Google::Cloud::Chronicle::V1::DuoAuthSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DuoAuthSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoAuthSettings)) — Duo Auth settings.

Note: The following fields are mutually exclusive: `duo_auth_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duo_auth_settings=
    
    
    def duo_auth_settings=(value) -> ::Google::Cloud::Chronicle::V1::DuoAuthSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DuoAuthSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoAuthSettings)) — Duo Auth settings.

Note: The following fields are mutually exclusive: `duo_auth_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::DuoAuthSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoAuthSettings)) — Duo Auth settings.

Note: The following fields are mutually exclusive: `duo_auth_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duo_user_context_settings
    
    
    def duo_user_context_settings() -> ::Google::Cloud::Chronicle::V1::DuoUserContextSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::DuoUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoUserContextSettings)) — Duo User Context settings.

Note: The following fields are mutually exclusive: `duo_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duo_user_context_settings=
    
    
    def duo_user_context_settings=(value) -> ::Google::Cloud::Chronicle::V1::DuoUserContextSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::DuoUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoUserContextSettings)) — Duo User Context settings.

Note: The following fields are mutually exclusive: `duo_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::DuoUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DuoUserContextSettings)) — Duo User Context settings.

Note: The following fields are mutually exclusive: `duo_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #feed_source_type
    
    
    def feed_source_type() -> ::Google::Cloud::Chronicle::V1::FeedDetails::FeedSourceType

**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedDetails::FeedSourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-FeedSourceType)) — Source Type of the feed. 



### #feed_source_type=
    
    
    def feed_source_type=(value) -> ::Google::Cloud::Chronicle::V1::FeedDetails::FeedSourceType

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::FeedDetails::FeedSourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-FeedSourceType)) — Source Type of the feed. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedDetails::FeedSourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-FeedSourceType)) — Source Type of the feed. 



### #fox_it_stix_settings
    
    
    def fox_it_stix_settings() -> ::Google::Cloud::Chronicle::V1::FoxITStixSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::FoxITStixSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FoxITStixSettings)) — Fox-IT STIX settings.

Note: The following fields are mutually exclusive: `fox_it_stix_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #fox_it_stix_settings=
    
    
    def fox_it_stix_settings=(value) -> ::Google::Cloud::Chronicle::V1::FoxITStixSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::FoxITStixSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FoxITStixSettings)) — Fox-IT STIX settings.

Note: The following fields are mutually exclusive: `fox_it_stix_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::FoxITStixSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FoxITStixSettings)) — Fox-IT STIX settings.

Note: The following fields are mutually exclusive: `fox_it_stix_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_settings
    
    
    def gcs_settings() -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageSettings)) — Google Cloud Storage settings.

Note: The following fields are mutually exclusive: `gcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_settings=
    
    
    def gcs_settings=(value) -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageSettings)) — Google Cloud Storage settings.

Note: The following fields are mutually exclusive: `gcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageSettings)) — Google Cloud Storage settings.

Note: The following fields are mutually exclusive: `gcs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_v2_settings
    
    
    def gcs_v2_settings() -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageV2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageV2Settings)) — Settings for Google Cloud Storage Omniflow feeds.

Note: The following fields are mutually exclusive: `gcs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_v2_settings=
    
    
    def gcs_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageV2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageV2Settings)) — Settings for Google Cloud Storage Omniflow feeds.

Note: The following fields are mutually exclusive: `gcs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageV2Settings)) — Settings for Google Cloud Storage Omniflow feeds.

Note: The following fields are mutually exclusive: `gcs_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_identity_device_users_settings
    
    
    def google_cloud_identity_device_users_settings() -> ::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDeviceUsersSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDeviceUsersSettings)) — Google Cloud Identity Device Users settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_device_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_identity_device_users_settings=
    
    
    def google_cloud_identity_device_users_settings=(value) -> ::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDeviceUsersSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDeviceUsersSettings)) — Google Cloud Identity Device Users settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_device_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDeviceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDeviceUsersSettings)) — Google Cloud Identity Device Users settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_device_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_identity_devices_settings
    
    
    def google_cloud_identity_devices_settings() -> ::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDevicesSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDevicesSettings)) — Google Cloud Identity Devices settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_devices_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_identity_devices_settings=
    
    
    def google_cloud_identity_devices_settings=(value) -> ::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDevicesSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDevicesSettings)) — Google Cloud Identity Devices settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_devices_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudIdentityDevicesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudIdentityDevicesSettings)) — Google Cloud Identity Devices settings.

Note: The following fields are mutually exclusive: `google_cloud_identity_devices_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_storage_event_driven_settings
    
    
    def google_cloud_storage_event_driven_settings() -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageEventDrivenSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageEventDrivenSettings)) — Settings for Omniflow based Google Cloud Storage event driven feeds.

Note: The following fields are mutually exclusive: `google_cloud_storage_event_driven_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #google_cloud_storage_event_driven_settings=
    
    
    def google_cloud_storage_event_driven_settings=(value) -> ::Google::Cloud::Chronicle::V1::GoogleCloudStorageEventDrivenSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageEventDrivenSettings)) — Settings for Omniflow based Google Cloud Storage event driven feeds.

Note: The following fields are mutually exclusive: `google_cloud_storage_event_driven_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::GoogleCloudStorageEventDrivenSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GoogleCloudStorageEventDrivenSettings)) — Settings for Omniflow based Google Cloud Storage event driven feeds.

Note: The following fields are mutually exclusive: `google_cloud_storage_event_driven_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #http_settings
    
    
    def http_settings() -> ::Google::Cloud::Chronicle::V1::HttpSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpSettings)) — HTTP settings.

Note: The following fields are mutually exclusive: `http_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #http_settings=
    
    
    def http_settings=(value) -> ::Google::Cloud::Chronicle::V1::HttpSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::HttpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpSettings)) — HTTP settings.

Note: The following fields are mutually exclusive: `http_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpSettings)) — HTTP settings.

Note: The following fields are mutually exclusive: `http_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_amazon_kinesis_firehose_settings
    
    
    def https_push_amazon_kinesis_firehose_settings() -> ::Google::Cloud::Chronicle::V1::HttpsPushAmazonKinesisFirehoseSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushAmazonKinesisFirehoseSettings)) — Https push Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `https_push_amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_amazon_kinesis_firehose_settings=
    
    
    def https_push_amazon_kinesis_firehose_settings=(value) -> ::Google::Cloud::Chronicle::V1::HttpsPushAmazonKinesisFirehoseSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushAmazonKinesisFirehoseSettings)) — Https push Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `https_push_amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushAmazonKinesisFirehoseSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushAmazonKinesisFirehoseSettings)) — Https push Amazon Kinesis Firehose settings.

Note: The following fields are mutually exclusive: `https_push_amazon_kinesis_firehose_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_google_cloud_pubsub_settings
    
    
    def https_push_google_cloud_pubsub_settings() -> ::Google::Cloud::Chronicle::V1::HttpsPushGoogleCloudPubSubSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushGoogleCloudPubSubSettings)) — Https push Google Pub/Sub settings.

Note: The following fields are mutually exclusive: `https_push_google_cloud_pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_google_cloud_pubsub_settings=
    
    
    def https_push_google_cloud_pubsub_settings=(value) -> ::Google::Cloud::Chronicle::V1::HttpsPushGoogleCloudPubSubSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushGoogleCloudPubSubSettings)) — Https push Google Pub/Sub settings.

Note: The following fields are mutually exclusive: `https_push_google_cloud_pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushGoogleCloudPubSubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushGoogleCloudPubSubSettings)) — Https push Google Pub/Sub settings.

Note: The following fields are mutually exclusive: `https_push_google_cloud_pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_webhook_settings
    
    
    def https_push_webhook_settings() -> ::Google::Cloud::Chronicle::V1::HttpsPushWebhookSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushWebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushWebhookSettings)) — Https push Webhook settings.

Note: The following fields are mutually exclusive: `https_push_webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #https_push_webhook_settings=
    
    
    def https_push_webhook_settings=(value) -> ::Google::Cloud::Chronicle::V1::HttpsPushWebhookSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::HttpsPushWebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushWebhookSettings)) — Https push Webhook settings.

Note: The following fields are mutually exclusive: `https_push_webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::HttpsPushWebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HttpsPushWebhookSettings)) — Https push Webhook settings.

Note: The following fields are mutually exclusive: `https_push_webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #imperva_waf_settings
    
    
    def imperva_waf_settings() -> ::Google::Cloud::Chronicle::V1::ImpervaWAFSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ImpervaWAFSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ImpervaWAFSettings)) — Imperva WAF settings.

Note: The following fields are mutually exclusive: `imperva_waf_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #imperva_waf_settings=
    
    
    def imperva_waf_settings=(value) -> ::Google::Cloud::Chronicle::V1::ImpervaWAFSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ImpervaWAFSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ImpervaWAFSettings)) — Imperva WAF settings.

Note: The following fields are mutually exclusive: `imperva_waf_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ImpervaWAFSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ImpervaWAFSettings)) — Imperva WAF settings.

Note: The following fields are mutually exclusive: `imperva_waf_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The ingestion metadata labels to apply to all logs ingested through this feed, and the resulting normalized data. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The ingestion metadata labels to apply to all logs ingested through this feed, and the resulting normalized data. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The ingestion metadata labels to apply to all logs ingested through this feed, and the resulting normalized data. 



### #last_v2_migration_attempt_time
    
    
    def last_v2_migration_attempt_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-Timestamp)) — Optional. The time of the last attempt to migrate the feed to STS V2. 



### #last_v2_migration_attempt_time=
    
    
    def last_v2_migration_attempt_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-Timestamp)) — Optional. The time of the last attempt to migrate the feed to STS V2. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-Timestamp)) — Optional. The time of the last attempt to migrate the feed to STS V2. 



### #log_type
    
    
    def log_type() -> ::String

**Returns**

  * (::String) — LogType. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type} 



### #log_type=
    
    
    def log_type=(value) -> ::String

**Parameter**

  * **value** (::String) — LogType. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type} 



**Returns**

  * (::String) — LogType. Format: projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type} 



### #mandiant_ioc_settings
    
    
    def mandiant_ioc_settings() -> ::Google::Cloud::Chronicle::V1::MandiantIoCSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::MandiantIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MandiantIoCSettings)) — Mandiant IOC settings.

Note: The following fields are mutually exclusive: `mandiant_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mandiant_ioc_settings=
    
    
    def mandiant_ioc_settings=(value) -> ::Google::Cloud::Chronicle::V1::MandiantIoCSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::MandiantIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MandiantIoCSettings)) — Mandiant IOC settings.

Note: The following fields are mutually exclusive: `mandiant_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::MandiantIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MandiantIoCSettings)) — Mandiant IOC settings.

Note: The following fields are mutually exclusive: `mandiant_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #microsoft_graph_alert_settings
    
    
    def microsoft_graph_alert_settings() -> ::Google::Cloud::Chronicle::V1::MicrosoftGraphAlertSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::MicrosoftGraphAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftGraphAlertSettings)) — Microsoft Graph Alert settings.

Note: The following fields are mutually exclusive: `microsoft_graph_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #microsoft_graph_alert_settings=
    
    
    def microsoft_graph_alert_settings=(value) -> ::Google::Cloud::Chronicle::V1::MicrosoftGraphAlertSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::MicrosoftGraphAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftGraphAlertSettings)) — Microsoft Graph Alert settings.

Note: The following fields are mutually exclusive: `microsoft_graph_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::MicrosoftGraphAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftGraphAlertSettings)) — Microsoft Graph Alert settings.

Note: The following fields are mutually exclusive: `microsoft_graph_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #microsoft_security_center_alert_settings
    
    
    def microsoft_security_center_alert_settings() -> ::Google::Cloud::Chronicle::V1::MicrosoftSecurityCenterAlertSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftSecurityCenterAlertSettings)) — Microsoft Security center alert settings.

Note: The following fields are mutually exclusive: `microsoft_security_center_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #microsoft_security_center_alert_settings=
    
    
    def microsoft_security_center_alert_settings=(value) -> ::Google::Cloud::Chronicle::V1::MicrosoftSecurityCenterAlertSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftSecurityCenterAlertSettings)) — Microsoft Security center alert settings.

Note: The following fields are mutually exclusive: `microsoft_security_center_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::MicrosoftSecurityCenterAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MicrosoftSecurityCenterAlertSettings)) — Microsoft Security center alert settings.

Note: The following fields are mutually exclusive: `microsoft_security_center_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mimecast_mail_settings
    
    
    def mimecast_mail_settings() -> ::Google::Cloud::Chronicle::V1::MimecastMailSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::MimecastMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailSettings)) — Mimecast mail settings.

Note: The following fields are mutually exclusive: `mimecast_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mimecast_mail_settings=
    
    
    def mimecast_mail_settings=(value) -> ::Google::Cloud::Chronicle::V1::MimecastMailSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::MimecastMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailSettings)) — Mimecast mail settings.

Note: The following fields are mutually exclusive: `mimecast_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::MimecastMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailSettings)) — Mimecast mail settings.

Note: The following fields are mutually exclusive: `mimecast_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mimecast_mail_v2_settings
    
    
    def mimecast_mail_v2_settings() -> ::Google::Cloud::Chronicle::V1::MimecastMailV2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::MimecastMailV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailV2Settings)) — Required. Mimecast mail v2 settings.

Note: The following fields are mutually exclusive: `mimecast_mail_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mimecast_mail_v2_settings=
    
    
    def mimecast_mail_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::MimecastMailV2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::MimecastMailV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailV2Settings)) — Required. Mimecast mail v2 settings.

Note: The following fields are mutually exclusive: `mimecast_mail_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::MimecastMailV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-MimecastMailV2Settings)) — Required. Mimecast mail v2 settings.

Note: The following fields are mutually exclusive: `mimecast_mail_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netskope_alert_settings
    
    
    def netskope_alert_settings() -> ::Google::Cloud::Chronicle::V1::NetskopeAlertSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::NetskopeAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertSettings)) — Netskope alert settings.

Note: The following fields are mutually exclusive: `netskope_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netskope_alert_settings=
    
    
    def netskope_alert_settings=(value) -> ::Google::Cloud::Chronicle::V1::NetskopeAlertSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::NetskopeAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertSettings)) — Netskope alert settings.

Note: The following fields are mutually exclusive: `netskope_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::NetskopeAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertSettings)) — Netskope alert settings.

Note: The following fields are mutually exclusive: `netskope_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netskope_alert_v2_settings
    
    
    def netskope_alert_v2_settings() -> ::Google::Cloud::Chronicle::V1::NetskopeAlertV2Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::NetskopeAlertV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertV2Settings)) — Netskope alert V2 settings.

Note: The following fields are mutually exclusive: `netskope_alert_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netskope_alert_v2_settings=
    
    
    def netskope_alert_v2_settings=(value) -> ::Google::Cloud::Chronicle::V1::NetskopeAlertV2Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::NetskopeAlertV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertV2Settings)) — Netskope alert V2 settings.

Note: The following fields are mutually exclusive: `netskope_alert_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::NetskopeAlertV2Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NetskopeAlertV2Settings)) — Netskope alert V2 settings.

Note: The following fields are mutually exclusive: `netskope_alert_v2_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #office365_settings
    
    
    def office365_settings() -> ::Google::Cloud::Chronicle::V1::Office365Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::Office365Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Office365Settings)) — Office 365 settings.

Note: The following fields are mutually exclusive: `office365_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #office365_settings=
    
    
    def office365_settings=(value) -> ::Google::Cloud::Chronicle::V1::Office365Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::Office365Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Office365Settings)) — Office 365 settings.

Note: The following fields are mutually exclusive: `office365_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::Office365Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Office365Settings)) — Office 365 settings.

Note: The following fields are mutually exclusive: `office365_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #okta_settings
    
    
    def okta_settings() -> ::Google::Cloud::Chronicle::V1::OktaSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::OktaSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaSettings)) — Okta settings.

Note: The following fields are mutually exclusive: `okta_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #okta_settings=
    
    
    def okta_settings=(value) -> ::Google::Cloud::Chronicle::V1::OktaSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::OktaSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaSettings)) — Okta settings.

Note: The following fields are mutually exclusive: `okta_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::OktaSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaSettings)) — Okta settings.

Note: The following fields are mutually exclusive: `okta_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #okta_user_context_settings
    
    
    def okta_user_context_settings() -> ::Google::Cloud::Chronicle::V1::OktaUserContextSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::OktaUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaUserContextSettings)) — Okta user context settings.

Note: The following fields are mutually exclusive: `okta_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #okta_user_context_settings=
    
    
    def okta_user_context_settings=(value) -> ::Google::Cloud::Chronicle::V1::OktaUserContextSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::OktaUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaUserContextSettings)) — Okta user context settings.

Note: The following fields are mutually exclusive: `okta_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::OktaUserContextSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-OktaUserContextSettings)) — Okta user context settings.

Note: The following fields are mutually exclusive: `okta_user_context_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pan_ioc_settings
    
    
    def pan_ioc_settings() -> ::Google::Cloud::Chronicle::V1::PanIocSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::PanIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanIocSettings)) — PAN IOC settings.

Note: The following fields are mutually exclusive: `pan_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pan_ioc_settings=
    
    
    def pan_ioc_settings=(value) -> ::Google::Cloud::Chronicle::V1::PanIocSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::PanIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanIocSettings)) — PAN IOC settings.

Note: The following fields are mutually exclusive: `pan_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::PanIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanIocSettings)) — PAN IOC settings.

Note: The following fields are mutually exclusive: `pan_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pan_prisma_cloud_settings
    
    
    def pan_prisma_cloud_settings() -> ::Google::Cloud::Chronicle::V1::PanPrismaCloudSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::PanPrismaCloudSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanPrismaCloudSettings)) — PAN Prisma Cloud settings.

Note: The following fields are mutually exclusive: `pan_prisma_cloud_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pan_prisma_cloud_settings=
    
    
    def pan_prisma_cloud_settings=(value) -> ::Google::Cloud::Chronicle::V1::PanPrismaCloudSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::PanPrismaCloudSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanPrismaCloudSettings)) — PAN Prisma Cloud settings.

Note: The following fields are mutually exclusive: `pan_prisma_cloud_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::PanPrismaCloudSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PanPrismaCloudSettings)) — PAN Prisma Cloud settings.

Note: The following fields are mutually exclusive: `pan_prisma_cloud_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #proofpoint_mail_settings
    
    
    def proofpoint_mail_settings() -> ::Google::Cloud::Chronicle::V1::ProofpointMailSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ProofpointMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointMailSettings)) — Proofpoint mail settings.

Note: The following fields are mutually exclusive: `proofpoint_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #proofpoint_mail_settings=
    
    
    def proofpoint_mail_settings=(value) -> ::Google::Cloud::Chronicle::V1::ProofpointMailSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ProofpointMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointMailSettings)) — Proofpoint mail settings.

Note: The following fields are mutually exclusive: `proofpoint_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ProofpointMailSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointMailSettings)) — Proofpoint mail settings.

Note: The following fields are mutually exclusive: `proofpoint_mail_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #proofpoint_on_demand_settings
    
    
    def proofpoint_on_demand_settings() -> ::Google::Cloud::Chronicle::V1::ProofpointOnDemandSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ProofpointOnDemandSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointOnDemandSettings)) — Proofpoint On-Demand settings.

Note: The following fields are mutually exclusive: `proofpoint_on_demand_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #proofpoint_on_demand_settings=
    
    
    def proofpoint_on_demand_settings=(value) -> ::Google::Cloud::Chronicle::V1::ProofpointOnDemandSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ProofpointOnDemandSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointOnDemandSettings)) — Proofpoint On-Demand settings.

Note: The following fields are mutually exclusive: `proofpoint_on_demand_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ProofpointOnDemandSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ProofpointOnDemandSettings)) — Proofpoint On-Demand settings.

Note: The following fields are mutually exclusive: `proofpoint_on_demand_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pubsub_settings
    
    
    def pubsub_settings() -> ::Google::Cloud::Chronicle::V1::PubsubSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::PubsubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PubsubSettings)) — Pub/Sub settings.

Note: The following fields are mutually exclusive: `pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pubsub_settings=
    
    
    def pubsub_settings=(value) -> ::Google::Cloud::Chronicle::V1::PubsubSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::PubsubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PubsubSettings)) — Pub/Sub settings.

Note: The following fields are mutually exclusive: `pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::PubsubSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-PubsubSettings)) — Pub/Sub settings.

Note: The following fields are mutually exclusive: `pubsub_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #qualys_scan_settings
    
    
    def qualys_scan_settings() -> ::Google::Cloud::Chronicle::V1::QualysScanSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::QualysScanSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysScanSettings)) — Qualys Scan Settings

Note: The following fields are mutually exclusive: `qualys_scan_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #qualys_scan_settings=
    
    
    def qualys_scan_settings=(value) -> ::Google::Cloud::Chronicle::V1::QualysScanSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::QualysScanSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysScanSettings)) — Qualys Scan Settings

Note: The following fields are mutually exclusive: `qualys_scan_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::QualysScanSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysScanSettings)) — Qualys Scan Settings

Note: The following fields are mutually exclusive: `qualys_scan_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #qualys_vm_settings
    
    
    def qualys_vm_settings() -> ::Google::Cloud::Chronicle::V1::QualysVMSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::QualysVMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysVMSettings)) — Qualys VM settings

Note: The following fields are mutually exclusive: `qualys_vm_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #qualys_vm_settings=
    
    
    def qualys_vm_settings=(value) -> ::Google::Cloud::Chronicle::V1::QualysVMSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::QualysVMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysVMSettings)) — Qualys VM settings

Note: The following fields are mutually exclusive: `qualys_vm_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::QualysVMSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-QualysVMSettings)) — Qualys VM settings

Note: The following fields are mutually exclusive: `qualys_vm_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rapid7_insight_settings
    
    
    def rapid7_insight_settings() -> ::Google::Cloud::Chronicle::V1::Rapid7InsightSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::Rapid7InsightSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Rapid7InsightSettings)) — Rapid7 Insight settings.

Note: The following fields are mutually exclusive: `rapid7_insight_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rapid7_insight_settings=
    
    
    def rapid7_insight_settings=(value) -> ::Google::Cloud::Chronicle::V1::Rapid7InsightSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::Rapid7InsightSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Rapid7InsightSettings)) — Rapid7 Insight settings.

Note: The following fields are mutually exclusive: `rapid7_insight_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::Rapid7InsightSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Rapid7InsightSettings)) — Rapid7 Insight settings.

Note: The following fields are mutually exclusive: `rapid7_insight_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #recorded_future_ioc_settings
    
    
    def recorded_future_ioc_settings() -> ::Google::Cloud::Chronicle::V1::RecordedFutureIocSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::RecordedFutureIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RecordedFutureIocSettings)) — Recorded Future IOC settings.

Note: The following fields are mutually exclusive: `recorded_future_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #recorded_future_ioc_settings=
    
    
    def recorded_future_ioc_settings=(value) -> ::Google::Cloud::Chronicle::V1::RecordedFutureIocSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::RecordedFutureIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RecordedFutureIocSettings)) — Recorded Future IOC settings.

Note: The following fields are mutually exclusive: `recorded_future_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::RecordedFutureIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RecordedFutureIocSettings)) — Recorded Future IOC settings.

Note: The following fields are mutually exclusive: `recorded_future_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rh_isac_ioc_settings
    
    
    def rh_isac_ioc_settings() -> ::Google::Cloud::Chronicle::V1::RHIsacIocSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::RHIsacIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RHIsacIocSettings)) — RH-ISAC IOC settings.

Note: The following fields are mutually exclusive: `rh_isac_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rh_isac_ioc_settings=
    
    
    def rh_isac_ioc_settings=(value) -> ::Google::Cloud::Chronicle::V1::RHIsacIocSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::RHIsacIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RHIsacIocSettings)) — RH-ISAC IOC settings.

Note: The following fields are mutually exclusive: `rh_isac_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::RHIsacIocSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-RHIsacIocSettings)) — RH-ISAC IOC settings.

Note: The following fields are mutually exclusive: `rh_isac_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #salesforce_settings
    
    
    def salesforce_settings() -> ::Google::Cloud::Chronicle::V1::SalesforceSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::SalesforceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SalesforceSettings)) — Salesforce settings.

Note: The following fields are mutually exclusive: `salesforce_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #salesforce_settings=
    
    
    def salesforce_settings=(value) -> ::Google::Cloud::Chronicle::V1::SalesforceSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::SalesforceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SalesforceSettings)) — Salesforce settings.

Note: The following fields are mutually exclusive: `salesforce_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::SalesforceSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SalesforceSettings)) — Salesforce settings.

Note: The following fields are mutually exclusive: `salesforce_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sentinelone_alert_settings
    
    
    def sentinelone_alert_settings() -> ::Google::Cloud::Chronicle::V1::SentineloneAlertSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::SentineloneAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SentineloneAlertSettings)) — SentinelOne Alert settings.

Note: The following fields are mutually exclusive: `sentinelone_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sentinelone_alert_settings=
    
    
    def sentinelone_alert_settings=(value) -> ::Google::Cloud::Chronicle::V1::SentineloneAlertSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::SentineloneAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SentineloneAlertSettings)) — SentinelOne Alert settings.

Note: The following fields are mutually exclusive: `sentinelone_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::SentineloneAlertSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SentineloneAlertSettings)) — SentinelOne Alert settings.

Note: The following fields are mutually exclusive: `sentinelone_alert_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #service_now_cmdb_settings
    
    
    def service_now_cmdb_settings() -> ::Google::Cloud::Chronicle::V1::ServiceNowCMDBSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ServiceNowCMDBSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ServiceNowCMDBSettings)) — ServiceNow CMDB settings.

Note: The following fields are mutually exclusive: `service_now_cmdb_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #service_now_cmdb_settings=
    
    
    def service_now_cmdb_settings=(value) -> ::Google::Cloud::Chronicle::V1::ServiceNowCMDBSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ServiceNowCMDBSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ServiceNowCMDBSettings)) — ServiceNow CMDB settings.

Note: The following fields are mutually exclusive: `service_now_cmdb_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ServiceNowCMDBSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ServiceNowCMDBSettings)) — ServiceNow CMDB settings.

Note: The following fields are mutually exclusive: `service_now_cmdb_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sftp_settings
    
    
    def sftp_settings() -> ::Google::Cloud::Chronicle::V1::SftpSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::SftpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SftpSettings)) — SFTP settings.

Note: The following fields are mutually exclusive: `sftp_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sftp_settings=
    
    
    def sftp_settings=(value) -> ::Google::Cloud::Chronicle::V1::SftpSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::SftpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SftpSettings)) — SFTP settings.

Note: The following fields are mutually exclusive: `sftp_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::SftpSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SftpSettings)) — SFTP settings.

Note: The following fields are mutually exclusive: `sftp_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sts_migration_readiness
    
    
    def sts_migration_readiness() -> ::Google::Cloud::Chronicle::V1::FeedDetails::STSMigrationReadiness

**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedDetails::STSMigrationReadiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-STSMigrationReadiness)) — Optional. The status of the feed's migration to STS. 



### #sts_migration_readiness=
    
    
    def sts_migration_readiness=(value) -> ::Google::Cloud::Chronicle::V1::FeedDetails::STSMigrationReadiness

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::FeedDetails::STSMigrationReadiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-STSMigrationReadiness)) — Optional. The status of the feed's migration to STS. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedDetails::STSMigrationReadiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedDetails-STSMigrationReadiness)) — Optional. The status of the feed's migration to STS. 



### #symantec_event_export_settings
    
    
    def symantec_event_export_settings() -> ::Google::Cloud::Chronicle::V1::SymantecEventExportSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::SymantecEventExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SymantecEventExportSettings)) — Symantec Event Export settings.

Note: The following fields are mutually exclusive: `symantec_event_export_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #symantec_event_export_settings=
    
    
    def symantec_event_export_settings=(value) -> ::Google::Cloud::Chronicle::V1::SymantecEventExportSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::SymantecEventExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SymantecEventExportSettings)) — Symantec Event Export settings.

Note: The following fields are mutually exclusive: `symantec_event_export_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::SymantecEventExportSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-SymantecEventExportSettings)) — Symantec Event Export settings.

Note: The following fields are mutually exclusive: `symantec_event_export_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #thinkst_canary_settings
    
    
    def thinkst_canary_settings() -> ::Google::Cloud::Chronicle::V1::ThinkstCanarySettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThinkstCanarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThinkstCanarySettings)) — Thinkst Canary settings.

Note: The following fields are mutually exclusive: `thinkst_canary_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #thinkst_canary_settings=
    
    
    def thinkst_canary_settings=(value) -> ::Google::Cloud::Chronicle::V1::ThinkstCanarySettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ThinkstCanarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThinkstCanarySettings)) — Thinkst Canary settings.

Note: The following fields are mutually exclusive: `thinkst_canary_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThinkstCanarySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThinkstCanarySettings)) — Thinkst Canary settings.

Note: The following fields are mutually exclusive: `thinkst_canary_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #threat_connect_ioc_settings
    
    
    def threat_connect_ioc_settings() -> ::Google::Cloud::Chronicle::V1::ThreatConnectIoCSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCSettings)) — ThreatConnect IOC settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #threat_connect_ioc_settings=
    
    
    def threat_connect_ioc_settings=(value) -> ::Google::Cloud::Chronicle::V1::ThreatConnectIoCSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCSettings)) — ThreatConnect IOC settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCSettings)) — ThreatConnect IOC settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #threat_connect_ioc_v3_settings
    
    
    def threat_connect_ioc_v3_settings() -> ::Google::Cloud::Chronicle::V1::ThreatConnectIoCV3Settings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCV3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCV3Settings)) — Threat Connect IOC V3 settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_v3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #threat_connect_ioc_v3_settings=
    
    
    def threat_connect_ioc_v3_settings=(value) -> ::Google::Cloud::Chronicle::V1::ThreatConnectIoCV3Settings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCV3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCV3Settings)) — Threat Connect IOC V3 settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_v3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::ThreatConnectIoCV3Settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ThreatConnectIoCV3Settings)) — Threat Connect IOC V3 settings.

Note: The following fields are mutually exclusive: `threat_connect_ioc_v3_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_alerts_settings
    
    
    def trellix_hx_alerts_settings() -> ::Google::Cloud::Chronicle::V1::TrellixHxAlertsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxAlertsSettings)) — Settings for Trellix HX Alerts Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_alerts_settings=
    
    
    def trellix_hx_alerts_settings=(value) -> ::Google::Cloud::Chronicle::V1::TrellixHxAlertsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::TrellixHxAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxAlertsSettings)) — Settings for Trellix HX Alerts Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxAlertsSettings)) — Settings for Trellix HX Alerts Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_bulk_acqs_settings
    
    
    def trellix_hx_bulk_acqs_settings() -> ::Google::Cloud::Chronicle::V1::TrellixHxBulkAcqsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxBulkAcqsSettings)) — Settings for Trellix HX Bulk Acquisitions Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_bulk_acqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_bulk_acqs_settings=
    
    
    def trellix_hx_bulk_acqs_settings=(value) -> ::Google::Cloud::Chronicle::V1::TrellixHxBulkAcqsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxBulkAcqsSettings)) — Settings for Trellix HX Bulk Acquisitions Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_bulk_acqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxBulkAcqsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxBulkAcqsSettings)) — Settings for Trellix HX Bulk Acquisitions Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_bulk_acqs_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_hosts_settings
    
    
    def trellix_hx_hosts_settings() -> ::Google::Cloud::Chronicle::V1::TrellixHxHostsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxHostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxHostsSettings)) — Settings for Trellix HX Host Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trellix_hx_hosts_settings=
    
    
    def trellix_hx_hosts_settings=(value) -> ::Google::Cloud::Chronicle::V1::TrellixHxHostsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::TrellixHxHostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxHostsSettings)) — Settings for Trellix HX Host Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::TrellixHxHostsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-TrellixHxHostsSettings)) — Settings for Trellix HX Host Metadata.

Note: The following fields are mutually exclusive: `trellix_hx_hosts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #webhook_settings
    
    
    def webhook_settings() -> ::Google::Cloud::Chronicle::V1::WebhookSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WebhookSettings)) — Webhook settings.

Note: The following fields are mutually exclusive: `webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #webhook_settings=
    
    
    def webhook_settings=(value) -> ::Google::Cloud::Chronicle::V1::WebhookSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WebhookSettings)) — Webhook settings.

Note: The following fields are mutually exclusive: `webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WebhookSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WebhookSettings)) — Webhook settings.

Note: The following fields are mutually exclusive: `webhook_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workday_settings
    
    
    def workday_settings() -> ::Google::Cloud::Chronicle::V1::WorkdaySettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkdaySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkdaySettings)) — Workday settings.

Note: The following fields are mutually exclusive: `workday_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workday_settings=
    
    
    def workday_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkdaySettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkdaySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkdaySettings)) — Workday settings.

Note: The following fields are mutually exclusive: `workday_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkdaySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkdaySettings)) — Workday settings.

Note: The following fields are mutually exclusive: `workday_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_activity_settings
    
    
    def workspace_activity_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceActivitySettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceActivitySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceActivitySettings)) — Workspace activity settings.

Note: The following fields are mutually exclusive: `workspace_activity_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_activity_settings=
    
    
    def workspace_activity_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceActivitySettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceActivitySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceActivitySettings)) — Workspace activity settings.

Note: The following fields are mutually exclusive: `workspace_activity_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceActivitySettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceActivitySettings)) — Workspace activity settings.

Note: The following fields are mutually exclusive: `workspace_activity_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_alerts_settings
    
    
    def workspace_alerts_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceAlertsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceAlertsSettings)) — Workspace alerts settings.

Note: The following fields are mutually exclusive: `workspace_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_alerts_settings=
    
    
    def workspace_alerts_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceAlertsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceAlertsSettings)) — Workspace alerts settings.

Note: The following fields are mutually exclusive: `workspace_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceAlertsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceAlertsSettings)) — Workspace alerts settings.

Note: The following fields are mutually exclusive: `workspace_alerts_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_chrome_os_settings
    
    
    def workspace_chrome_os_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceChromeOSSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceChromeOSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceChromeOSSettings)) — Workspace ChromeOS settings.

Note: The following fields are mutually exclusive: `workspace_chrome_os_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_chrome_os_settings=
    
    
    def workspace_chrome_os_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceChromeOSSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceChromeOSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceChromeOSSettings)) — Workspace ChromeOS settings.

Note: The following fields are mutually exclusive: `workspace_chrome_os_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceChromeOSSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceChromeOSSettings)) — Workspace ChromeOS settings.

Note: The following fields are mutually exclusive: `workspace_chrome_os_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_groups_settings
    
    
    def workspace_groups_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceGroupsSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceGroupsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceGroupsSettings)) — Workspace Groups settings.

Note: The following fields are mutually exclusive: `workspace_groups_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_groups_settings=
    
    
    def workspace_groups_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceGroupsSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceGroupsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceGroupsSettings)) — Workspace Groups settings.

Note: The following fields are mutually exclusive: `workspace_groups_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceGroupsSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceGroupsSettings)) — Workspace Groups settings.

Note: The following fields are mutually exclusive: `workspace_groups_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_mobile_settings
    
    
    def workspace_mobile_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceMobileSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceMobileSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceMobileSettings)) — Workspace mobile settings.

Note: The following fields are mutually exclusive: `workspace_mobile_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_mobile_settings=
    
    
    def workspace_mobile_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceMobileSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceMobileSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceMobileSettings)) — Workspace mobile settings.

Note: The following fields are mutually exclusive: `workspace_mobile_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceMobileSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceMobileSettings)) — Workspace mobile settings.

Note: The following fields are mutually exclusive: `workspace_mobile_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_privileges_settings
    
    
    def workspace_privileges_settings() -> ::Google::Cloud::Chronicle::V1::WorkspacePrivilegesSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspacePrivilegesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspacePrivilegesSettings)) — Workspace privileges settings.

Note: The following fields are mutually exclusive: `workspace_privileges_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_privileges_settings=
    
    
    def workspace_privileges_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspacePrivilegesSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspacePrivilegesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspacePrivilegesSettings)) — Workspace privileges settings.

Note: The following fields are mutually exclusive: `workspace_privileges_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspacePrivilegesSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspacePrivilegesSettings)) — Workspace privileges settings.

Note: The following fields are mutually exclusive: `workspace_privileges_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_users_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_users_settings
    
    
    def workspace_users_settings() -> ::Google::Cloud::Chronicle::V1::WorkspaceUsersSettings

**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceUsersSettings)) — Workspace users settings.

Note: The following fields are mutually exclusive: `workspace_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #workspace_users_settings=
    
    
    def workspace_users_settings=(value) -> ::Google::Cloud::Chronicle::V1::WorkspaceUsersSettings

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::WorkspaceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceUsersSettings)) — Workspace users settings.

Note: The following fields are mutually exclusive: `workspace_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Chronicle::V1::WorkspaceUsersSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-WorkspaceUsersSettings)) — Workspace users settings.

Note: The following fields are mutually exclusive: `workspace_users_settings`, `anomali_settings`, `azure_ad_context_settings`, `cloud_passage_settings`, `cortex_xdr_settings`, `duo_auth_settings`, `duo_user_context_settings`, `microsoft_graph_alert_settings`, `microsoft_security_center_alert_settings`, `mimecast_mail_settings`, `office365_settings`, `proofpoint_mail_settings`, `recorded_future_ioc_settings`, `workday_settings`, `pan_ioc_settings`, `okta_settings`, `okta_user_context_settings`, `fox_it_stix_settings`, `threat_connect_ioc_settings`, `service_now_cmdb_settings`, `imperva_waf_settings`, `thinkst_canary_settings`, `rh_isac_ioc_settings`, `rapid7_insight_settings`, `salesforce_settings`, `netskope_alert_settings`, `azure_mdm_intune_settings`, `azure_ad_settings`, `proofpoint_on_demand_settings`, `workspace_activity_settings`, `workspace_alerts_settings`, `workspace_privileges_settings`, `workspace_mobile_settings`, `workspace_chrome_os_settings`, `workspace_groups_settings`, `azure_ad_audit_settings`, `symantec_event_export_settings`, `qualys_vm_settings`, `pan_prisma_cloud_settings`, `gcs_settings`, `http_settings`, `sftp_settings`, `amazon_s3_settings`, `azure_blob_store_settings`, `amazon_sqs_settings`, `google_cloud_identity_devices_settings`, `google_cloud_identity_device_users_settings`, `crowdstrike_detects_settings`, `mandiant_ioc_settings`, `sentinelone_alert_settings`, `qualys_scan_settings`, `pubsub_settings`, `amazon_kinesis_firehose_settings`, `webhook_settings`, `dummy_log_type_settings`, `https_push_google_cloud_pubsub_settings`, `https_push_amazon_kinesis_firehose_settings`, `https_push_webhook_settings`, `aws_ec2_hosts_settings`, `aws_ec2_instances_settings`, `aws_ec2_vpcs_settings`, `aws_iam_settings`, `netskope_alert_v2_settings`, `gcs_v2_settings`, `amazon_s3_v2_settings`, `amazon_sqs_v2_settings`, `azure_event_hub_settings`, `trellix_hx_hosts_settings`, `azure_blob_store_v2_settings`, `trellix_hx_alerts_settings`, `google_cloud_storage_event_driven_settings`, `crowdstrike_alerts_settings`, `trellix_hx_bulk_acqs_settings`, `mimecast_mail_v2_settings`, `threat_connect_ioc_v3_settings`, `custom_api_settings`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
