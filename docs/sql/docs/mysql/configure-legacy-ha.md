---
url: https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha/
title: Legacy configuration for high availability \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:28.639721+00:00
---

# Legacy configuration for high availability  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Legacy configuration for high availability Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Important:** As of January 13, 2025, the legacy configuration for high availability (HA) is deprecated for all instances. You can't create instances with legacy high availability configuration, and you can't enable legacy high availability configuration on any existing instances. In addition, after January 13, 2025, legacy high availability instances are no longer covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
  
We recommend that you update your remaining legacy high availability instances to the current high availability configuration. You can do so by following the instructions in [Update an instance from legacy to current high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy). Starting on May 1, 2025, Cloud SQL will begin updating any instances that use the legacy high availability configuration to use the current regional persistent disk-based high availability configuration automatically. 

This page describes the legacy configuration for a MySQL instance for high availability (HA).

In a legacy HA configuration, a Cloud SQL for MySQL instance uses a failover replica to add high availability to the instance. This feature isn't available in Google Cloud console. The recommended configuration doesn't use failover replicas. Instead, the current high availability configuration uses Google [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks#repds), which synchronously replicate data at the block-level between two zones in a region.

For more information about the current high availability configuration, see [Overview of the High Availability Configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

## Update an instance from legacy to current high availability

To update your instance from the legacy to the current high availability configuration, do the following:

  1. Update your instance to the current high availability configuration.

     1. Delete the failover replica for the MySQL instance you want to update. For more information, see Disable high availability on an instance.
     2. Configure the primary instance to use the current version of high availability. For more information, see [Configure an existing instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing).

As another option, use Database Migration Service to [migrate to an instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job#dest) that uses the current high availability configuration.

  2. [Create a read replica instance](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#create-2nd-gen) to offload any read workloads that you don't want to perform on the primary instance.




## Initiate failover

Testing failover is optional, but is recommended so that you can see how your application responds in the event of a failover.

**Note:** This feature helps you test your application's response to an automatic failover. Make sure your instance has completed any previous failover (so it is responding to connection requests) before you trigger another failover.

To learn more about failovers, see the [Failover overview](https://docs.cloud.google.com/sql/docs/mysql/high-availability#failover-overview).

### gcloud

Initiate the failover:
    
    
    gcloud sql instances failover PRIMARY_INSTANCE_NAME

### curl

  1. Describe the primary instance to get the value of the `settingsVersion` field. 
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              -X GET \
              https://www.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/PRIMARY_INSTANCE_NAME

  2. Initiate the failover: 
         
         gcloud auth login
         ACCESS_TOKEN="$(gcloud auth print-access-token)"
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data '{"failoverContext":{"settingsVersion":"SETTINGS_VERSION"}}' \
              -X POST \
              https://www.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/PRIMARY_INSTANCE_NAME/failover




The instance fails over and is not available to serve data for a few minutes.

## Legacy configuration: Create an alert for replication lag

The time required for a failover operation depends on the amount of replication lag when the failover is initiated. You can use Cloud Monitoring in the Google Cloud console to alert you when replication lag exceeds a threshold.

**Note:** Failover downtime caused by replication lag greater than 1200 seconds is not counted against the SLA for the instance.

For more information about replication lag, search for "seconds_behind_master" on the [SHOW SLAVE STATUS Syntax](https://dev.mysql.com/doc/refman/8.4/en/show-slave-status.html) page in the MySQL documentation.

For more information about Cloud Monitoring, see [the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

**Note:** A newly created Cloud SQL instance can take time to appear in the Cloud Monitoring interface. If you don't see a new instance, then check again in an hour.

### Legacy configuration: Set an alert for a specific failover replica

  1. In the navigation panel of the Google Cloud console, select **Monitoring** , and then select **Alerting**.
  2. Click **Create Alerting Policy**.
  3. Enter a descriptive name for your alert.
  4. Select **Metric Threshold** and click **Next** to open the Target tab.
  5. For **Resource Type** , select **Cloud SQL**.
  6. For **Applies To** , select **Single** , then select your failover replica.
  7. Click **Next** to open the Configuration tab.
  8. Enter the following values:

Field | Value  
---|---  
If Metric | Seconds Behind Master  
Condition | above  
Thresholds | 120 (or whatever value is appropriate for your environment)  
For | 3 minutes  
  9. Select your **Notification** methods, and click **Save Condition**.




### Legacy configuration: Set an alert for a group of failover replicas

If you plan to create multiple failover replicas in the same project, it could be easier to set the alert for the entire group, rather than on each failover replica individually. To create a group for monitoring, use a suffix for the failover replicas' names, such as "-failover". Make sure you don't use this suffix for any other types of Cloud SQL instances.

**Create your failover replica group:**

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. From the upper menu bar, select **Groups** > **Create...**.
  3. Enter a descriptive name for your group.
  4. Leave **Name** and **Contains** selected, and enter your name substring.
  5. Click **Save Group**. The summary page for the new group opens.
  6. Confirm that the expected instances are included in the group.

**Note:** If you open the **Groups Overview** page, where all existing groups are listed, then your group shows 0 instances. This is because Cloud Monitoring uses the term "instances" to mean VMs and VM clusters. Cloud SQL instances are shown under _Resources_.

**Create the alert for the failover replica group:**

  1. In the navigation panel of the Google Cloud console, select **Monitoring** , and then select **Alerting**.
  2. Click **Create Alerting Policy**.
  3. Enter a descriptive name for your group alert.
  4. Select **Metric Threshold** and click **Next** to open the Target tab.
  5. For **Resource Type** , select **Cloud SQL**.
  6. For **Applies To** , select **Group** , then select your failover group.
  7. Leave **Any Member Violates** selected and click **Next** to open the Configuration tab.
  8. Enter the following values:

Field | Value  
---|---  
If Metric | Seconds Behind Master  
Condition | above  
Thresholds | 120 (or whatever value is appropriate for your environment)  
For | 3 minutes  
  9. Select your desired **Notification** methods, and click **Save Condition**.




### Legacy configuration: Disable high availability on an instance

You need to delete the failover replica instance to remove high availability from the primary instance.

Before you perform this procedure, make sure there are no operations currently running on the primary instance.

To disable high availability:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the failover instance associated with the instance you want to disable high availability on.
  3. On the **Instance details** page, click **Delete**.
  4. In the **Delete Replica** window, retype the name of failover instance.
  5. Click **Delete**. The configuration for the original instance changes to zonal.



### gcloud

For reference information, see `[gcloud sql instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete)`. 
    
    
    gcloud sql instances delete FAILOVER_REPLICA_NAME

### curl

The following request uses the `[instances:delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/delete)` method to delete the instance. 
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json'\
          -X DELETE\
    https://www.googleapis.com/sql/v1beta4/projects/PROJECT-ID/instances/INSTANCE_NAME

## What's next

  * Learn more about [how the high availability configuration works](https://docs.cloud.google.com/sql/docs/mysql/high-availability).
  * Test how your application responds to lost connections by [restarting your instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance).
  * Learn more about [managing your database connections](https://docs.cloud.google.com/sql/faq#connections).
  * Learn more about [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).
  * [Create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication) for your instance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
