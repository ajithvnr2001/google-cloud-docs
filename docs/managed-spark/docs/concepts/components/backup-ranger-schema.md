---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/backup-ranger-schema/
title: Back up and restore a Ranger schema \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:42.114778+00:00
---

# Back up and restore a Ranger schema  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/backup-ranger-schema/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Back up and restore a Ranger schema Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to back up and restore a Ranger schema on [Managed Service for Apache Spark with Ranger clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger).

## Before you begin

  1. Create a bucket if needed. You must have access to a Cloud Storage bucket, which you will use to store and restore a Ranger schema.

To create a bucket:

     1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

     2. Click add_box **Create**. 
     3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
        1. In the **Get started** section, do the following: 
           * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
           * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
        2. In the **Choose where to store your data** section, do the following: 
           1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
           2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
              * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
           3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

              1. In the **Bucket** menu, select a bucket.
              2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

                 * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
                 * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
                 * Click **Done**.

        3. In the **Choose how to store your data** section, do the following: 
           1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
           2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
        4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
        5. In the **Choose how to protect object data** section, do the following: 
           * Select any of the options under **Data protection** that you want to set for your bucket. 
             * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
             * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
             * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
               * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
               * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
           * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
     4. Click **Create**. 



## Back up a Ranger schema

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the Managed Service for Apache Spark master node of the cluster with the Ranger schema. **Run the commands in this section in the SSH terminal session running on the master node.**

  2. Set environment variables.
         
         BUCKET_NAME=bucket name \
           MYSQL_PASSWORD=MySQL password
           SCHEMA_FILE=schema filename
         

Replace the following:

     * MySQL password: You can open `/etc/mysql/my.cnf` on the cluster master node to copy the MySQL password.

     * bucket name: The name of the Cloud Storage bucket to use to store the Ranger schema.

     * schema filename: Specify a filename, without the `.sql` filename extension. The Ranger schema is saved to this file on the master node, then saved in bucket name in Cloud Storage .

  3. Stop Hive services. 
         
         sudo systemctl stop hive-metastore.service
         sudo systemctl stop hive-server2.service
         

  4. Prevent changes to the Ranger schema tables.
         
         mysql -u root -p${MYSQL_PASSWORD}
         REVOKE ALL PRIVILEGES ON ranger.* from 'rangeradmin'@'localhost';
         GRANT SELECT ON ranger.* TO 'rangeradmin'@'localhost';
         FLUSH PRIVILEGES;
         SHOW GRANTS FOR 'rangeradmin'@'localhost';
         exit;
         

  5. Save the Ranger schema to an `.sql` file.
         
         mysqldump -u root -p${MYSQL_PASSWORD} ranger > ${SCHEMA_FILE}.sql
         

  6. Reset Ranger privileges.
         
         mysql -u root -p${MYSQL_PASSWORD}
         REVOKE SELECT ON ranger.* from 'rangeradmin'@'localhost';
         GRANT ALL PRIVILEGES ON ranger.* to 'rangeradmin'@'localhost';
         FLUSH PRIVILEGES;
         SHOW GRANTS FOR 'rangeradmin'@'localhost';
         exit;
         

  7. Restart Hive and Ranger services.
         
         sudo systemctl start hive-metastore.service
           sudo systemctl start hive-server2.service
           sudo systemctl restart ranger-admin.service
           sudo systemctl restart ranger-usersync.service
         

  8. Copy the Ranger schema to Cloud Storage.
         
         gcloud storage cp ${SCHEMA_FILE}.sql gs://${BUCKET_NAME}
         




## Restore a Ranger schema

**Note:** If you back up then restore the schema to same cluster, you may be able to use the SSH session and environment variables used in your Ranger schema backup session.

  1. Use [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the Managed Service for Apache Spark master node of the cluster where you will restore the cluster schema. **Run the commands in this section in the SSH terminal session running on the master node.**

  2. Set environment variables.
         
         BUCKET_NAME=bucket name \
           MYSQL_PASSWORD=MySQL password
           SCHEMA_FILE=schema filename
         

Replace the following:

     * MySQL password: You can open `/etc/mysql/my.cnf` on the cluster master node to copy the MySQL password.

     * bucket name: The name of the Cloud Storage bucket that contains the saved Ranger schema.

     * schema filename: The name of the Ranger schema filename, without the `.sql` filename extension, saved in bucket name in Cloud Storage.

  3. Stop Hive services. 
         
         sudo systemctl stop hive-metastore.service
         sudo systemctl stop hive-server2.service
         

  4. Prevent changes to the Ranger schema tables.
         
         mysql -u root -p${MYSQL_PASSWORD}
         REVOKE ALL PRIVILEGES ON ranger.* from 'rangeradmin'@'localhost';
         GRANT SELECT ON ranger.* TO 'rangeradmin'@'localhost';
         FLUSH PRIVILEGES;
         SHOW GRANTS FOR 'rangeradmin'@'localhost';
         exit;
         

  5. Copy the Ranger schema `.sql` file in Cloud Storage to the cluster master node.
         
         gcloud storage cp ${BUCKET_NAME}/${SCHEMA_FILE}.sql .
         

  6. Restore the Ranger schema. **This step overwrites the contents of the existing Ranger schema.**
         
         mysqldump -u root -p${MYSQL_PASSWORD} ranger < ${SCHEMA_FILE}.sql
         

  7. Reset Ranger privileges.
         
         mysql -u root -p${MYSQL_PASSWORD}
         REVOKE SELECT ON ranger.* from 'rangeradmin'@'localhost';
         GRANT ALL PRIVILEGES ON ranger.* to 'rangeradmin'@'localhost';
         FLUSH PRIVILEGES;
         SHOW GRANTS FOR 'rangeradmin'@'localhost';
         exit;
         

  8. Update Ranger configuration files. Change the Ranger DB host to a new database hostname in the following files with the following properties:

File | Property  
---|---  
`ranger-hdfs-security.xml` | `ranger.plugin.hdfs.policy.rest.url`  
`ranger-yarn-security.xml` | `ranger.plugin.yarn.policy.rest.url`  
  9. Restart Hive and Ranger services.
         
         sudo systemctl start hive-metastore.service
           sudo systemctl start hive-server2.service
           sudo systemctl restart ranger-admin.service
           sudo systemctl restart ranger-usersync.service
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
