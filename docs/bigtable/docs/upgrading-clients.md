---
url: https://docs.cloud.google.com/bigtable/docs/upgrading-clients/
title: Upgrading client libraries \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:56.200936+00:00
---

# Upgrading client libraries  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/upgrading-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrading client libraries

Upgrading your Cloud Bigtable client libraries for Java, HBase for Java, and Go lets you migrate away from obsolete methods and adopt current connection and protocol buffer patterns. If you need to install a client library for the first time, follow the instructions for your preferred programming language at [Bigtable Client Libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

## Bigtable client for Java

The convenience methods in `BigtableTableAdminClient` and `BigtableInstanceAdminClient` are obsolete.

To upgrade your code, follow these steps:

  1. Instantiate the V2 clients, `BigtableTableAdminClientV2` and `BigtableInstanceAdminClientV2`, by using the static `create()` factory method.
  2. Replace the custom wrapper request objects, such as `com.google.cloud.bigtable.admin.v2.models.CreateTableRequest`, with standard protocol buffer request objects, such as `com.google.bigtable.admin.v2.CreateTableRequest`.
  3. Ensure that the new standard protocol buffer request objects use fully qualified resource names.
  4. Call the standard protocol buffer methods directly on your new V2 clients.
  5. Replace the placeholder variables in your code with identifiers, as shown in the following example:
         
         // Existing code
         [BigtableTableAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient.html) adminClient = [BigtableTableAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient.html).create(PROJECT_ID, INSTANCE_ID);
         adminClient.[createTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient.html#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClient_createTable_com_google_cloud_bigtable_admin_v2_models_CreateTableRequest_)(
             CreateTableRequest.of(TABLE_ID)
                 .addFamily("cf1"));
         
         // New code
         import com.google.bigtable.admin.v2.[ColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.ColumnFamily.html);
         import com.google.bigtable.admin.v2.[CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html);
         import com.google.bigtable.admin.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.html);
         import com.google.cloud.bigtable.admin.v2.[BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html);
         
         // ...
         
         try ([BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html) adminClient = [BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html).create()) {
           String parent = "projects/" + PROJECT_ID + "/instances/" + INSTANCE_ID;
           [CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html) request =
               [CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html).newBuilder()
                   .setParent(parent)
                   .[setTableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.RestoreTableRequest.html#com_google_cloud_bigtable_admin_v2_models_RestoreTableRequest_setTableId_java_lang_String_)(TABLE_ID)
                   .setTable([Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.html).newBuilder()
                       .putColumnFamilies("cf1", [ColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.ColumnFamily.html).getDefaultInstance())
                       .build())
                   .build();
           adminClient.[createTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient.html#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClient_createTable_com_google_cloud_bigtable_admin_v2_models_CreateTableRequest_)(request);
         }
         

Replace the following:

     * `PROJECT_ID`: the identifier of your Bigtable project
     * `INSTANCE_ID`: the identifier of your Bigtable instance
     * `TABLE_ID`: the identifier for your new table



## HBase client for Java

If you're upgrading from version **1.0 or later** of the [HBase client for Java](https://github.com/googleapis/java-bigtable-hbase), the only change you need to make is to update the version number in the configuration. You don't need to update your code.

If you're upgrading from **pre-1.0** HBase clients, complete the following steps:

  1. **Update your dependencies** to use the newest client library and remove artifacts that you no longer need:

     * Remove the `bigtable-hbase-1.0`, `bigtable-hbase-1.1`, and `bigtable-hbase-1.2` artifacts from your dependencies if they are present.

     * Remove `netty-tcnative-boringssl-static` from your dependencies unless another part of your application requires it.

     * Add one of the following artifacts to your dependencies, depending on your use case. The `2.x` versions include an HBase async client that the `1.x` versions don't have.

       * `bigtable-hbase-1.x` or `bigtable-hbase-2.x`: Use for standalone applications where you are in control of your dependencies.
       * `bigtable-hbase-1.x-hadoop` or `bigtable-hbase-2.x-hadoop`: Use in Hadoop environments.
       * `bigtable-hbase-1.x-shaded` or `bigtable-hbase-2.x-shaded`: Use in environments other than Hadoop that require earlier versions of components such as [protobuf](https://github.com/google/protobuf) or [Guava](https://github.com/google/guava).
  2. **Update your configuration settings** for connecting to Bigtable.

     * If the configuration settings in your code or in an `hbase-site.xml` file include a value for `hbase.client.connection.impl`, change the value to `com.google.cloud.bigtable.hbase1_x.BigtableConnection`.

     * If you use the `BigtableConnection` class directly, update your code to use `com.google.cloud.bigtable.hbase1_x.BigtableConnection` instead.

     * If you use an `hbase-site.xml` file to connect to Bigtable:

       * Add the property `google.bigtable.instance.id` if it is not present. Set the property value to your instance ID.
       * Remove the property `google.bigtable.cluster.name` if it is present.
       * Remove the property `google.bigtable.zone.name` if it is present.
     * If you connect to Bigtable by calling `BigtableConfiguration.connect()`, update your code as shown in the following example:
    
    // Existing code
    BigtableConfiguration.connect(PROJECT_ID, ZONE_ID, CLUSTER_ID);
    
    // New code
    BigtableConfiguration.connect(PROJECT_ID, INSTANCE_ID);
    

Replace the following:

     * `PROJECT_ID`: the identifier of your project.
     * `ZONE_ID`: the zone where your cluster resides.
     * `CLUSTER_ID`: the identifier of your cluster.
     * `INSTANCE_ID`: the identifier of your instance.
  3. **Redeploy your application** in all of your environments, including local development, testing, staging, and production.




For a list of releases for the HBase client for Java, see the [release history on GitHub](https://github.com/googleapis/java-bigtable-hbase/releases).

## Go

In June 2016, the Go client changed the way to connect to Bigtable. Instead of specifying a cluster ID and zone, specify an instance ID. You can find the instance ID by [visiting the Google Cloud console](https://console.cloud.google.com/bigtable/instances).

To download the client library, visit the [code repository on GitHub](https://github.com/GoogleCloudPlatform/google-cloud-go).

Update your code as shown in the following example:
    
    
      // Existing code
      adminClient, err := bigtable.NewAdminClient(ctx, PROJECT_ID, ZONE, CLUSTER_ID)
      client, err := bigtable.NewClient(ctx, PROJECT_ID, ZONE, CLUSTER_ID)
    
      // New code
      adminClient, err := bigtable.NewAdminClient(ctx, PROJECT_ID, INSTANCE_ID)
      client, err := bigtable.NewClient(ctx, PROJECT_ID, INSTANCE_ID)
    

Replace the following:

  * `PROJECT_ID`: the identifier of your project.
  * `ZONE`: the zone where your cluster resides.
  * `CLUSTER_ID`: the identifier of the cluster to which you want to connect.
  * `INSTANCE_ID`: the identifier of the instance to which you want to connect.



For a list of releases for the Go client library, see the [release history on GitHub](https://github.com/GoogleCloudPlatform/google-cloud-go/releases).

## What's next

  * Read more about [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).
  * Learn more about how Bigtable [integrates with other tools and Google Cloud services](https://docs.cloud.google.com/bigtable/docs/integrations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
