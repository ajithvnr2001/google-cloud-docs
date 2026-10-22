---
url: https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql/
title: Configure a self-managed MySQL database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:15.337276+00:00
---

# Configure a self-managed MySQL database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a self-managed MySQL database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you stream change data capture (CDC) updates from a self-managed MySQL database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. To prepare your source, you configure full row-based binary logging with a 7-day retention period and create a Datastream user with replication privileges. You can also use this configuration for compatible databases such as MariaDB, Percona Server for MySQL, and Alibaba Cloud PolarDB.

## Verify the configuration and retention period of the binary log

  1. Confirm that the binary log is configured correctly by entering the following MySQL command:
         
         SHOW GLOBAL VARIABLES LIKE '%binlog_format%';
         

  2. Verify that the value for the `binlog_format` variable is set to `ROW`. Datastream doesn't support `MIXED` or `STATEMENT` binary log formats.

  3. Confirm that the row format for the binary log is set to `FULL` by entering the following MySQL command:
         
         SHOW GLOBAL VARIABLES LIKE 'binlog_row_image';
         

  4. For MySQL versions 8.0 and later, confirm that the `binlog_row_value_options` variable is set to an empty value by entering the following MySQL command:
         
         SHOW GLOBAL VARIABLES LIKE 'binlog_row_value_options';
         

  5. Verify that the replica updates option for the binary log is set to `ON` by entering the following MySQL command:
         
         SHOW GLOBAL VARIABLES LIKE 'log_replica_updates';
         

For MySQL versions earlier than 8.0.26, enter the following command instead:
         
         SHOW GLOBAL VARIABLES LIKE 'log_slave_updates';
         

  6. Verify that the retention period of the binary log is set to `604800` seconds (`7` days) by entering the following MySQL command:
         
         SHOW GLOBAL VARIABLES LIKE 'binlog_expire_logs_seconds';
         

For MySQL versions earlier than 8.0.3, enter the following command instead:
         
         SHOW GLOBAL VARIABLES LIKE 'expire_logs_days';
         

If your MySQL database isn't set to full row-based replication and a 7-day retention period, then you'll need to change the configuration of the binary log, as follows:

     1. Navigate to the `/etc/mysql/` directory.
     2. Using an editor, open the `my.cnf` file.
     3. Add the following lines to the file: 
            
            [mysqld]
              log-bin=mysql-bin
              server-id=1
              binlog_format=ROW
              binlog_row_value_options=''
              # For MySQL versions 8.0 and later.
              log-replica-updates=1
              # For MySQL versions earlier than 8.0.26, use log-slave-updates=true
              # instead.
              binlog_expire_logs_seconds=604800
              # For MySQL versions earlier than 8.0.3, use expire_logs_days=7 instead.
              max_allowed_packet=1G
              # '1G' is the recommended value.
              

     4. For GTID-based replication, also add the following lines: 
            
            [mysqld]
              gtid_mode=ON
              enforce-gtid-consistency=ON
              

     5. Save your changes to the `my.cnf` file, and then close the file.
     6. Restart your MySQL server so that the changes you made can take effect.



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
