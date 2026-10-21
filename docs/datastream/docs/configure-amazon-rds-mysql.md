---
url: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-mysql/
title: Configure an Amazon RDS MySQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:46.999949+00:00
---

# Configure an Amazon RDS MySQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure an Amazon RDS MySQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from an Amazon RDS for MySQL database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

## Create a parameter group

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Parameter Groups**.

  3. Click **Create Parameter Group**. The **Create Parameter Group** page appears.

  4. Select the database family that matches your database, provide a name and description for the parameter group.

  5. Click **Create**.

  6. Select the checkbox to the left of your newly created parameter group.

  7. Under **Parameter group actions** , click **Edit**.

  8. Use the following table to set the parameters for your group.

     * For **binlog-based** replication:

Parameter| Value  
---|---  
binlog_format| `ROW`  
log_bin_use_v1_row_events| `1`  
read_only| `0`  
net_read_timeout| `3600`  
net_write_timeout| `3600`  
wait_timeout| `86400`  
     * For **GTID-based** replication:

Parameter| Value  
---|---  
binlog_format| `ROW`  
log_bin_use_v1_row_events| `1`  
read_only| `0`  
net_read_timeout| `3600`  
net_write_timeout| `3600`  
wait_timeout| `86400`  
expire-logs-days| `7`  
binlog_row_image| `FULL`  
max_allowed_packet| `1G` (recommended value)  
log-replica-updates| `1`  
enforce-gtid-consistency| `ON`  
gtid_mode| `ON`You can only set this parameter to `ON` after you set `enforce-gtid-consistency` to `ON`. In general, `gtid_mode` can have the following values: 
       * `OFF`
       * `OFF_PERMISSIVE`
       * `ON_PERMISSIVE`
       * `ON`
You can only change the values of the `gtid_mode` parameter one step at a time. For example, if the current mode is set to `OFF`, do the following: 
       1. Change the setting to `OFF_PERMISSIVE`.
       2. Change the setting to `ON_PERMISSIVE`.
       3. Change the setting to `ON`.
For more information, see [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/replication-options-gtids.html#sysvar_gtid_mode).  
  9. Click **Save Changes**.




## Create a read replica

Although this is an optional step, we highly recommend using a read replica because it significantly decreases the load of replication on your MySQL database.

If you choose to replicate directly from the main server, then proceed to the instructions in Configure the source database and the read replica.

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Databases**.

  3. Select the main database instance to which you want Datastream to connect.

  4. Expand the **Actions** button, and then click **Create read replica**.

  5. Configure the read replica, as necessary.

  6. Click **Create read replica**.




## Configure the source database and the read replica

If you chose to replicate directly from the main server, configure the source database using the steps that follow.

If you chose to use a read replica, configure both the source database and the read replica using the steps that follow.

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Databases**.

  3. Select the instance that you want to configure and then click **Modify**.

  4. Go to the **Additional configuration** section.

  5. Select the parameter group that you created.

  6. Set the **Backup retention period** to **7 days**.

  7. Click **Continue**.

  8. Under **Scheduling of modifications** , select **Apply immediately**.

Wait until the changes to your parameter group are applied before proceeding.



## Verify that the parameter group is assigned to the database instance

  1. Launch your Amazon RDS Dashboard.

  2. In the **Navigation Drawer** , click **Databases** , and then select your database instance.

  3. Click the **Configurations** tab.

  4. Verify that you see the parameter group that you created, and that its status is **pending-reboot**.

  5. Reboot your database instance to complete the configuration. To reboot the instance:

     1. In the **Navigation Drawer** , click **Instances**.
     2. Select your database instance.
     3. From the **Instance Actions** menu, select **Reboot**.
After you reboot your database instance, its status changes to **in-sync**.



## Set the binary log retention period

  1. Enter the following MySQL command:
         
         call mysql.rds_set_configuration('binlog retention hours', 168);

You're entering this command because you want to ensure proper replication by configuring your system to retain binary logs for a minimum of 7 days (or 168 hours).
  2. Restart your MySQL server so that the changes you made can take effect.




## Create a Datastream user

  1. Create a Datastream user:
         
         CREATE USER 'datastream'@'%' IDENTIFIED BY 'YOUR_PASSWORD';

  2. Grant the following privileges to them:
         
         GRANT REPLICATION SLAVE, SELECT, REPLICATION CLIENT ON *.* TO 'datastream'@'%';
         GRANT EXECUTE ON PROCEDURE mysql.rds_show_configuration TO 'datastream'@'%';
         FLUSH PRIVILEGES;




## What's next

  * Learn more about how Datastream works with [MySQL sources](https://docs.cloud.google.com/datastream/docs/sources-mysql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
