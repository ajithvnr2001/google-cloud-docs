---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-hosts/
title: Collect AWS EC2 Hosts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:51.592902+00:00
---

# Collect AWS EC2 Hosts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-hosts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS EC2 Hosts logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to integrate AWS EC2 Hosts logs into Google Security Operations for monitoring and analysis. The integration involves parsing and mapping EC2 host logs to the Unified Data Model (UDM), performing data transformation, and creating relationships between EC2 hosts and instances. The logs provide valuable information about the instances, host properties, instance types, and performance metrics that can be used for security monitoring, audit, and compliance.

## Before you begin

  * Ensure that you have a Google SecOps instance.
  * Ensure that you have privileged access to AWS.



## Configure AWS IAM and S3

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for later use.
  3. Create a user following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as the **Use case**.
  8. Click **Next**.
  9. Optional: add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for later use. 
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in the **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Configure CloudTrail for AWS KMS

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type and select **CloudTrail** from the services list.
  3. Click **Create trail**.
  4. Provide a **Trail name** ; for example, `EC2-Activity-Trail`.
  5. Select the **Enable for all accounts in my organization** checkbox.
  6. Type the S3 bucket URI created earlier (the format should be: `s3://your-log-bucket-name/`), or create a new S3 bucket.
  7. If SSE-KMS is enabled, provide a name for **AWS KMS alias** , or choose an **existing AWS KMS Key**.
  8. You can leave the other settings as default.
  9. Click **Next**.
  10. Select **Management events** and **Data events** under **Event Types** to capture EC2 host activity. 
  11. Click **Next**.
  12. Review the settings in **Review and create**. 
  13. Click **Create trail**.
  14. Optional: if you created a new bucket, continue with the following process: 
     * Go to **S3**.
     * Identify and select the newly created log bucket. 
     * Select the folder **AWSLogs**.
     * Click **Copy S3 URI** and save it.



## Configure a feed in Google SecOps to ingest AWS EC2 Hosts

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add new**.
  3. In the **Feed name** field, enter a name for the feed; for example, **AWS EC2 Hosts Logs**.
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **AWS EC2 Hosts** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters:

     * **S3 URI** : the bucket URI. 
       * `s3://your-log-bucket-name/`
         * Replace `your-log-bucket-name` with the actual name of the bucket.
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Access Key ID** : the User access key with access to the s3 bucket.

     * **Secret Access Key** : the User secret key with access to the s3 bucket.

     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : the label to be applied to the events from this feed.

  8. Click **Next**.

  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Supported AWS EC2 Hosts log formats

The AWS EC2 Hosts parser supports logs in JSON format.

## Supported AWS EC2 Hosts Sample Logs

  * JSON
        
        {
            "AllocationTime": "2018-01-23T12:33:31.692Z",
            "AllowsMultipleInstanceTypes": "",
            "AssetID": "",
            "AutoPlacement": "off",
            "AvailabilityZone": "us-east-1a",
            "AvailabilityZoneID": "",
            "AvailableCapacity": {
              "VCPUs": 96,
              "Instance": {
                "Available": 48,
                "Total": 48,
                "Type": "m5.large"
              }
            },
            "ClientToken": "",
            "ID": "h-05abcdd12ee9ca123",
            "Maintenance": "",
            "Properties": {
              "Cores": 48,
              "InstanceFamily": "",
              "InstanceType": "m5.large",
              "Sockets": 2,
              "TotalVCPUs": 96
            },
            "Recovery": "off",
            "ReservationID": "",
            "Instances": null,
            "MemberOfServiceLinkedResourceGroup": false,
            "OutpostARN": "",
            "OwnerID": "",
            "ReleaseTime": "",
            "State": "available",
            "TagSet": null
          }
        




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`AllocationTime` | `entity.metadata.creation_timestamp` | The `AllocationTime` field is parsed as a timestamp and mapped to the `creation_timestamp` field. The parser attempts various formats (yyyy-MM-dd HH:mm:ss, RFC 3339, UNIX, ISO8601).  
`AllowsMultipleInstanceTypes` | `entity.entity.asset.attribute.labels.value` | The value of `AllowsMultipleInstanceTypes` from the raw log is used as the value of a label. The key for this label is set to `allows_multiple_instance_types`.  
`AutoPlacement` | `entity.entity.asset.attribute.labels.value` | The value of `AutoPlacement` from the raw log is used as the value of a label. The key for this label is set to `auto_placement`.  
`AvailabilityZone` | `entity.entity.asset.attribute.cloud.availability_zone` | The `AvailabilityZone` field is directly mapped to the `availability_zone` field.  
`AvailabilityZoneID` | `entity.entity.asset.attribute.labels.value` | The value of `AvailabilityZoneID` from the raw log is used as the value of a label. The key for this label is set to `availability_zone_id`.  
`AvailableCapacity.AvailableInstanceCapacity.AvailableCapacity` | `entity.entity.asset.attribute.labels.value` | The value of `AvailableCapacity.AvailableInstanceCapacity.AvailableCapacity` (or `AvailableCapacity.Instance.Available` after renaming) is converted to a string and used as the value of a label. The key is set to `available_instance_capacity_available_capacity`.  
`AvailableCapacity.AvailableInstanceCapacity.InstanceType` | `entity.entity.asset.attribute.labels.value` | The value of `AvailableCapacity.AvailableInstanceCapacity.InstanceType` (or `AvailableCapacity.Instance.Type` after renaming) is used as the value of a label. The key is set to `available_instance_capacity_instance_type`.  
`AvailableCapacity.AvailableInstanceCapacity.TotalCapacity` | `entity.entity.asset.attribute.labels.value` | The value of `AvailableCapacity.AvailableInstanceCapacity.TotalCapacity` (or `AvailableCapacity.Instance.Total` after renaming) is converted to a string and used as the value of a label. The key is set to `total_capacity`.  
`AvailableCapacity.AvailableVCpus` | `entity.entity.asset.attribute.labels.value` | The value of `AvailableCapacity.AvailableVCpus` (or `AvailableCapacity.VCPUs` after renaming) is converted to a string and used as the value of a label. The key is set to `available_v_cpus`.  
`ClientToken` | `entity.entity.asset.attribute.labels.value` | The value of `ClientToken` from the raw log is used as the value of a label. The key for this label is set to `client_token`.  
`HostID` | `entity.metadata.product_entity_id` | The `HostID` (or `ID` after renaming) field is directly mapped to the `product_entity_id` field.  
`HostID` | `entity.entity.asset.asset_id` | The `HostID` (or `ID` after renaming) field is directly mapped to the `asset_id` field.  
`HostMaintenance` | `entity.entity.asset.attribute.labels.value` | The value of `HostMaintenance` (or `Maintenance` after renaming) from the raw log is used as the value of a label. The key for this label is set to `host_maintenance`.  
`HostProperties.Cores` | `entity.entity.asset.hardware.cpu_number_cores` | The value of `HostProperties.Cores` is converted to an unsigned integer and mapped to `cpu_number_cores`.  
`HostProperties.InstanceFamily` | `entity.entity.asset.attribute.labels.value` | The value of `HostProperties.InstanceFamily` from the raw log is used as the value of a label. The key for this label is set to `host_properties_instance_family`.  
`HostProperties.InstanceType` | `entity.entity.asset.attribute.labels.value` | The value of `HostProperties.InstanceType` from the raw log is used as the value of a label. The key for this label is set to `host_properties_instance_type`.  
`HostProperties.Sockets` | `entity.entity.asset.attribute.labels.value` | The value of `HostProperties.Sockets` is converted to a string and used as the value of a label. The key is set to `host_properties_sockets`.  
`HostProperties.TotalVCpus` | `entity.entity.asset.attribute.labels.value` | The value of `HostProperties.TotalVCpus` (or `HostProperties.TotalVCPUs` after renaming) is converted to a string and used as the value of a label. The key is set to `host_properties_total_v_cpus`.  
`HostRecovery` | `entity.entity.asset.attribute.labels.value` | The value of `HostRecovery` (or `Recovery` after renaming) from the raw log is used as the value of a label. The key for this label is set to `host_recovery`.  
`HostReservationID` | `entity.entity.asset.attribute.labels.value` | The value of `HostReservationID` (or `ReservationID` after renaming) from the raw log is used as the value of a label. The key for this label is set to `host_reservation_id`.  
`MemberOfServiceLinkedResourceGroup` | `entity.entity.asset.attribute.labels.value` | The value of `MemberOfServiceLinkedResourceGroup` is converted to a string and used as the value of a label. The key is set to `member_of_service_linked_resource_group`.  
`OwnerID` | `entity.entity.asset.attribute.labels.value` | The value of `OwnerID` from the raw log is used as the value of a label. The key for this label is set to `owner_id`.  
`ReleaseTime` | `entity.entity.asset.attribute.labels.value` | The value of `ReleaseTime` from the raw log is used as the value of a label. The key for this label is set to `release_time`.  
`State` | `entity.entity.asset.attribute.labels.value` | The value of `State` from the raw log is used as the value of a label. The key for this label is set to `state`.  
`TagSet` | `entity.entity.asset.attribute.labels` | The `TagSet` array is iterated over, and each tag's `Key` and `Value` are used as the key and value of a label, respectively. The value `AMAZON_WEB_SERVICES` is assigned to this field by the parser. The `collection_time` from the raw log is mapped to the `collected_timestamp` field. The value `ASSET` is assigned to this field by the parser. The value `AWS EC2 HOSTS` is assigned to this field by the parser. The value `AWS` is assigned to this field by the parser. Relations are derived from `Instances` and `OutpostArn` fields, but these fields themselves are not directly mapped to the IDM object. The parser logic creates relation objects based on these fields and merges them into the `relations` array.  
`collection_time` | `entity.metadata.collected_timestamp` | The log's `collection_time` is used as the event's `collected_timestamp`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ec2-hosts-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
