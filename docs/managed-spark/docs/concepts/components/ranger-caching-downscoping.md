---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger-caching-downscoping/
title: Use Ranger with caching and downscoping \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:24.361086+00:00
---

# Use Ranger with caching and downscoping  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/ranger-caching-downscoping/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use Ranger with caching and downscoping Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:** Learn how to use Ranger properties to enable caching and downscoping on a Managed Service for Apache Spark cluster.

## Enable caching

This section lists the steps to enable caching with Ranger in order to reduce Ranger Key Management System (KMS) round trips to encrypt and decrypt tokens.

**Note:** Ranger caching is available with Managed Service for Apache Spark image versions starting with image version `2.0.92`.

  1. Install [`memcached`](https://memcached.org/) on Managed Service for Apache Spark cluster VMs. By default, the memcached server starts on VM port 11211 (`localhost:11211`). 
         
         sudo apt-get install -y memcached
         

  2. Set the following properties in the `/etc/dataproc-ranger-gcs-plugin/conf/ranger-gcs-site.xml` Ranger config file on Managed Service for Apache Spark cluster VMs. 
         
         <property>
         <name>authorization.service.remoteCaching.address</name>
         <value>localhost:11211</value>
         </property>  
         
         <property>
         <name>authorization.service.remoteCaching.class</name>
         <value>com.google.cloud.hadoop.ranger.gcs.authorization.caching.MemcachedCache</value>
         </property>  
         
         <property>
         <name>authorization.service.remoteCaching.encryption.key.uri</name>
         <value>gcp-kms://projects/PROJECT_ID_OF_KMS_KEY/locations/REGION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME</value>
         </property>
         

  3. Restart the authorization service. 
         
         sudo systemctl restart ranger-gcs-plugin-authorization-server
         




### View cache status

You can use [`telnet`](https://en.wikipedia.org/wiki/Telnet) to view Ranger cache status.

  1. Install `telnet`. 
         
         sudo apt-get install -y telnet
         

  2. Use telnet to connect to `memcache` on VM port `11211`. 
         
         sudo telnet 127.0.0.1 11211
         

  3. Use `telnet` commands to view cache status, including the following commands:

     * `stats items`: List the status of cache items. Sample output: 
           
           STAT items:17:number 2
           STAT items:17:number_hot 0
           STAT items:17:number_warm 0
           STAT items:17:number_cold 2
           

     * `stats cachedump`: List keys stored in the cache. Sample output: 
           
           stats cachedump 17 2
           ITEM 0616eeeeb54e23a09505da5bf75cd7fafe733eacf0d07bd7b1ac9cf46d17c188 [3051 b; 1707948281 s]
           ITEM d23645df9c79290d59ddb1b9710ff04fee37aa0b5de866b9b6d56b54641d68b4 [3078 b; 1707948281 s]
           

     * `flush_all`: Invalidate cache items.



## Downscope Cloud Storage access tokens

You might need to downscope Ranger access tokens to move up (upscope) the Cloud Storage paths that an external Hive table points to.

To move all partitions and subpartitions up to the table level, set the `downscope.table.partition-name.pruning.enabled` property to `true` in the `ranger-gcs-site.xml` config file on Managed Service for Apache Spark cluster VMs.
    
    
    <property>
      <name>downscope.table.partition-name.pruning.enabled</name>
      <value>true</value>
    </property>
    

Example:

  * Cloud Storage bucket name: `gs://warehouse`
  * Original access token path: `warehouse/hive/table/type=debit/year=2017/month=Aug/day=01/`
  * After setting `downscope.table.partition-name.pruning.enabled` to `true`, upscoped access token path: `warehouse/hive/table/`

**Note:** You can verify access token paths in the `/var/log/ranger-gcs-plugin-authorization-server.log` when `log4j.properties` is set to `debug`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
