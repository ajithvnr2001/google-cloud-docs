---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-read-pool/
title: Create an asynchronous read pool instance in Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:10:13.201689+00:00
---

# Create an asynchronous read pool instance in Kubernetes  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-read-pool/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Create an asynchronous read pool instance in Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-read-pool)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-read-pool)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/kubernetes-read-pool)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/kubernetes-read-pool)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/kubernetes-read-pool)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/kubernetes-read-pool)

To increase read throughput and availability of your database cluster, you can create an asynchronous read pool instance of your database instance. A read pool instance provides a read-only clone of your database instance ensuring data access even if your database instance becomes unavailable. 

You can define the read pool instance configuration in the database instance's manifest file. Each read pool instance requires creating a unique manifest file. You can create up to 20 read pool instances.

Each read pool instance occupies the same amount of storage as the instance it replicates.

**Note:** You can configure your instance's standby replica to be used as a synchronous read-only instance. For more information, see [Use the standby as a read-only instance](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/kubernetes-ha#create-read-only-instance).

## Create an asynchronous read pool instance

You can create any number of read pool instances in your database cluster. To create an AlloyDB Omni asynchronous read pool instance, complete the following steps:

  1. Create the database instance manifest to define the read pool instance type:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBInstance
         metadata:
           name: READ_POOL_INSTANCE_NAME
           namespace: NAMESPACE
         spec:
           instanceType: ReadPool
           nodeCount: READ_POOL_INSTANCE_SIZE
           dbcParent:
             name: DB_CLUSTER_NAME
         

Replace the following:

     * `READ_POOL_INSTANCE_NAME`: a name for this resource—for example, `read-pool-instance-1`.

     * `NAMESPACE`: the namespace of the database cluster.

     * `DB_CLUSTER_NAME`: the name of the database cluster to which the instance belongs.

     * `READ_POOL_INSTANCE_SIZE`: the number of nodes in a read pool instance. This determines the instance's overall computing capacity. You can have a maximum of 20 nodes per read pool instance. 

**Caution:** Creating too many read pool instances in your database cluster might reduce the primary instance's performance.
  2. Apply the manifest.




## Verify instance status

To verify the availability of the read pool instance, run the following command:
    
    
      kubectl get dbinstance -n NAMESPACE READ_POOL_INSTANCE_NAME -o jsonpath='{.status.conditions[?(@.type=="Available")].status}'

The response `true` indicates that the read pool instance can serve queries, but might not be replicating data from your database instance.

To verify the streaming status of the read pool instance, run the following command:
    
    
      kubectl get dbinstance -n NAMESPACE READ_POOL_INSTANCE_NAME -o jsonpath='{.status.conditions[?(@.type=="Streaming")].status}'

The response `true` indicates that the read pool instance is connected to your database instance and actively streaming changes.

When your database instance is unreachable, the read pool instance continues to serve the queries. In this case, the availability status will be `true` while the streaming status will be `false`.

After you set up the read pool instance, all inserts, updates, and deletions to rows in your instance become readable on your read pool instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
