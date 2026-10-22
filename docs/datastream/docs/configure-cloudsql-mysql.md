---
url: https://docs.cloud.google.com/datastream/docs/configure-cloudsql-mysql/
title: Configure a Cloud SQL for MySQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:16.942955+00:00
---

# Configure a Cloud SQL for MySQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-cloudsql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Cloud SQL for MySQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you stream change data capture (CDC) updates from a Cloud SQL for MySQL database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. To prepare your source instance, you enable binary logging, set database flags for GTID-based or binlog-based replication, and configure a Datastream user.

## Enable binary logging

  1. To enable binary logging for Cloud SQL for MySQL, see [Enabling point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#enablingpitr).



## Configure database flags

  1. In Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select the project that contains the Cloud SQL instance for which you want to set the database flags.

  3. Open the instance and click **Edit**.

  4. Go to the **Flags** section.

  5. Click **Add a database flag**.

  6. Choose the following flags from the drop-down menu, and set their values:

     * For **GTID-based** replication:

Parameter| Value  
---|---  
net_read_timeout| `3600`  
net_write_timeout| `3600`  
wait_timeout| `86400`  
binlog_row_image| `full`  
max_allowed_packet| `1073741824` (recommended value)  
     * For **binlog-based** replication:

Flag| Value  
---|---  
net_read_timeout| `3600`  
net_write_timeout| `3600`  
wait_timeout| `86400`  
  7. Click **Save** to save your changes.




## Create a Datastream user

  1. To create a Datastream user, enter the following MySQL commands:
         
         CREATE USER 'datastream'@'%' IDENTIFIED BY 'YOUR_PASSWORD';
         GRANT REPLICATION SLAVE, SELECT, REPLICATION CLIENT ON *.* TO 'datastream'@'%';
         FLUSH PRIVILEGES;




## What's next

  * Learn more about how Datastream works with [MySQL sources](https://docs.cloud.google.com/datastream/docs/sources-mysql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
