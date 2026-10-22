---
url: https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc/
title: Attach a Managed Service for Apache Spark cluster or a self-managed cluster \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:18.202202+00:00
---

# Attach a Managed Service for Apache Spark cluster or a self-managed cluster  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Attach a Managed Service for Apache Spark cluster or a self-managed cluster Stay organized with collections  Save and categorize content based on your preferences. 

After you create a Dataproc Metastore service, you can attach any of the following services:

  * A Managed Service for Apache Spark cluster.
  * A self-managed [Apache Hive](https://hive.apache.org/) instance, an [Apache Spark](https://spark.apache.org/) instance, or a [Presto](https://prestodb.io/) cluster.



After you connect one of these services, it uses your Dataproc Metastore service as its Hive metastore during query execution.

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.



### Required Roles

To get the permissions that you need to create a Dataproc Metastore and a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * To grant full control of Dataproc Metastore resources, either: 
    * [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the user account or service account
    * [Dataproc Metastore Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`) on the user account or service account
  * To create a Managed Service for Apache Spark cluster: (`roles/dataproc.worker`) on the [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity)
  * To grant read and write permissions to the Hive warehouse directory: (`roles/storage.objectAdmin`) on the [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a Dataproc Metastore and a Managed Service for Apache Spark cluster. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Dataproc Metastore and a Managed Service for Apache Spark cluster:

  * To create a Dataproc Metastore: metastore.services.create on the user account or service account 
  * To create a Managed Service for Apache Spark cluster: dataproc.clusters.create on the user account or service account 
  * To access the Hive warehouse directory: `orgpolicy.policy.get1`,`resourcemanager.projects.get`,`resourcemanager.projects.list`,`storage.objects.*`,`storage.multipartUploads.*` on the [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity)



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Managed Service for Apache Spark clusters

Managed Service for Apache Spark is a managed Apache Spark and Apache Hadoop service that lets you take advantage of open source data tools for batch processing, querying, streaming, and machine learning.

### Considerations

Before you create and attach a Managed Service for Apache Spark cluster, check what [endpoint protocol](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols) your Dataproc Metastore service is using. This protocol defines how your Hive Metastore clients access metadata stored in your Dataproc Metastore. This choice can also affect the features that you can integrate and use with your service.

### Apache Thrift

If you use the Apache Thrift endpoint protocol, consider the following network requirements:

  * By default, you should create your Managed Service for Apache Spark cluster and Dataproc Metastore service on the same network. Your Managed Service for Apache Spark cluster can also use a subnet of the Dataproc Metastore service's network.

  * If your Managed Service for Apache Spark cluster belongs to a different project than the network, you must [configure shared network permissions](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#create_a_cluster_that_uses_a_network_in_another_project).

  * If your Managed Service for Apache Spark cluster belongs to a different project than your Dataproc Metastore service, you must [set up additional permissions](https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment) before creating a Managed Service for Apache Spark cluster.




### gRPC

If you use the gRPC endpoint protocol, consider the following network requirements:

  * After you create a Dataproc Metastore using the gRPC endpoint protocol, you must grant [additional IAM roles](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints).

  * If you're using [Dataproc Personal Cluster Authentication](https://docs.cloud.google.com/dataproc/docs/concepts/iam/personal-auth), your Dataproc Metastore must use the gRPC endpoint protocol.

  * If your Managed Service for Apache Spark cluster belongs to a different project than your Dataproc Metastore service, you must [set up additional permissions](https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment) before creating a Managed Service for Apache Spark cluster.




### Create a cluster and attach a Dataproc Metastore

The following instructions show you how to create a Managed Service for Apache Spark cluster and connect to it from a Dataproc Metastore service. These instructions assume you have already [Created a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

  * Before creating your Managed Service for Apache Spark cluster, make sure the Managed Service for Apache Spark image you choose is compatible with the Hive metastore version you selected when you created your Dataproc Metastore. For more information, see [Managed Service for Apache Spark Image version list](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions).
  * To optimize network connectivity, create the Managed Service for Apache Spark cluster in the same region as your Dataproc Metastore service.




### Console

  1. In the Google Cloud console, open the Managed Service for Apache Spark **Create a cluster** page:

[Open **Create a cluster**](https://console.cloud.google.com/dataproc/clustersAdd)

  2. In the **Cluster Name** field, enter a name for your cluster.

  3. For the **Region** and **Zone** menus, select the same region that you created your Dataproc Metastore service in. You can choose any Zone.

  4. Click the **Customize cluster** tab.

  5. In the **Network configuration** section, select the same network that you created your Dataproc Metastore service in.

  6. In the **Dataproc Metastore** section, select the Dataproc Metastore service you want to attach. If you haven't created one yet, you can select **Create New Service**.

**Note:** if you don't see your Dataproc Metastore service in this list, double check which region you selected for your Managed Service for Apache Spark cluster. Both services must be configured to use the same region.
  7. Optional: If your Dataproc Metastore service uses the gRPC endpoint protocol:

     1. Click the **Manage Security** tab.
     2. In the **Project Access** section, select **Enable the cloud-platform scope for this cluster**.
  8. Configure the remaining service options as needed.

  9. To create the cluster, click **Create**.

Your new cluster appears in the Clusters list. The cluster status is listed as _Provisioning_ until the cluster is ready to use. When it's ready for use, the status changes to _Running_.




### gcloud CLI

To create a cluster and attach a Dataproc Metastore, run the following [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --dataproc-metastore=projects/PROJECT_ID/locations/LOCATION/services/SERVICE \
        --region=LOCATION \
        --scopes=SCOPES

Replace the following:

  * `CLUSTER_NAME`: the name of your new Managed Service for Apache Spark cluster.
  * `PROJECT_ID`: the project ID of the project you created your Dataproc Metastore service in.
  * `LOCATION`: the same region you created your Dataproc Metastore service in.
  * `SERVICE`: the name of the Dataproc Metastore service that you're attaching to the cluster.
  * `SCOPES`: (Optional) If your Dataproc Metastore service uses the gRPC endpoint protocol, use `cloud-platform`.



### REST

Follow the API instructions to [create a cluster](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters/create) by using the APIs Explorer.

### Attach a cluster using Managed Service for Apache Spark cluster properties

You can also attach a Managed Service for Apache Spark cluster to a Dataproc Metastore using [Managed Service for Apache Spark properties](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties). These properties include the Dataproc Metastore `ENDPOINT_URI` and `WAREHOUSE_DIR`.

Use these instructions if your Dataproc Metastore service uses [Private Service Connect](https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb) or if you want to attach a Managed Service for Apache Spark cluster to the [auxiliary version](https://docs.cloud.google.com/dataproc-metastore/docs/auxiliary-versions) of your Dataproc Metastore service.

There are two ways that you can attach a Managed Service for Apache Spark cluster using the `ENDPOINT_URI` and `WAREHOUSE_DIR` properties:

#### Option 1: While creating a Managed Service for Apache Spark cluster

When creating a Managed Service for Apache Spark cluster, use the properties flag with the following Hive configuration.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
         --properties="hive:hive.metastore.uris=ENDPOINT_URI,hive:hive.metastore.warehouse.dir=WAREHOUSE_DIR/hive-warehouse"

Replace the following:

  * `CLUSTER_NAME`: the name of your new Managed Service for Apache Spark cluster.
  * `ENDPOINT_URI`: The [endpoint URI](https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol#endpoint-value) of your Dataproc Metastore service.
  * `WAREHOUSE_DIR`: The location of your [Hive warehouse directory](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#hive-warehouse-dir).



#### Option 2: Update the `hive-site.xml` file

You can also attach a Managed Service for Apache Spark cluster by directly modifying the cluster's `hive-site.xml` file.

  1. Connect to the `.*-m` cluster [using SSH](https://docs.cloud.google.com/dataproc/docs/concepts/accessing/ssh).
  2. Open the `/etc/hive/conf/hive-site.xml` file and modify the following lines:
         
         <property>
            <name>hive.metastore.uris</name>
            <!-- Update this value. -->
            <value>ENDPOINT_URI</value>
         </property>
         <!-- Add this property entry. -->
         <property>
            <name>hive.metastore.warehouse.dir</name>
            <value>WAREHOUSE_DIR</value>
         </property>
         

Replace the following:

     * `ENDPOINT_URI`: The [endpoint URI](https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol#endpoint-value) of your Dataproc Metastore service.
     * `WAREHOUSE_DIR`: The location of your [Hive warehouse directory](https://docs.cloud.google.com/dataproc-metastore/docs/data-storage-internal-tables#hive-warehouse-dir).
  3. Restart HiveServer2:
         
         sudo systemctl restart hive-server2.service
         




## Self-managed clusters

A self-managed cluster can be an [Apache Hive](https://hive.apache.org/) instance, an [Apache Spark](https://spark.apache.org/) instance, or a [Presto](https://prestodb.io/) cluster.

### Attach a self-managed cluster

Set the following values in your client configuration file:
    
    
    hive.metastore.uris=ENDPOINT_URI
    hive.metastore.warehouse.dir=WAREHOUSE_DIR
    

Replace the following:

  * `ENDPOINT_URI`: The [endpoint URI](https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol#endpoint-value) of your Dataproc Metastore service.
  * `WAREHOUSE_DIR`: The location of your [Hive warehouse directory](https://docs.cloud.google.com/dataproc-metastore/docs/data-storage-internal-tables#hive-warehouse-dir).



## What's next

  * [Quickstart for deploying Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)
  * [Dataproc Metastore overview](https://docs.cloud.google.com/dataproc-metastore/docs/overview)
  * [Managed Service for Apache Spark overview](https://docs.cloud.google.com/dataproc/docs/concepts/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
