---
url: https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles/
title: Create and configure app profiles \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:54.028134+00:00
---

# Create and configure app profiles  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and configure app profiles

**Note:** This document includes features that are available only in the Enterprise Plus edition. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

Bigtable application profiles (_app profiles_) let you specify routing policies, compute options, and workload isolation settings for incoming client requests. You can direct traffic across provisioned cluster nodes, run isolated high-throughput reads using Data Boost serverless compute, or route point reads to an in-memory tier ([Preview](https://cloud.google.com/products#product-launch-stages)) on Enterprise Plus instances.

## Before you begin

Before you create or configure an app profile, read the following documentation:

  * Read [App profiles overview](https://docs.cloud.google.com/bigtable/docs/app-profiles) to learn how app profiles work and the difference between a _standard app profile_ for standard compute and a _Data Boost app profile_ for serverless high-throughput read jobs. For more information about how Data Boost differs from compute using provisioned cluster nodes, see [Bigtable Data Boost overview](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).
  * If you're using standard app profiles to configure replication, read [Replication overview](https://docs.cloud.google.com/bigtable/docs/replication-overview) and [Examples of replication configurations](https://docs.cloud.google.com/bigtable/docs/replication-settings) to decide what settings are best for your use case.
  * If you're using an in-memory tier app profile, read [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).



## Required roles

To get the permissions that you need to create, configure, or delete an app profile, ask your administrator to grant you the [Bigtable administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.admin) (`roles/bigtable.admin`) IAM role on the instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an app profile

You can create many different custom app profiles for each instance. Use custom app profiles to control how each application, or each distinct function within an application, interacts with an instance. For example, you might use one app profile for a batch application to isolate its traffic to a single cluster, and you might use a different app profile to provide high availability for another application. 

### Create a standard app profile

To create a standard app profile, follow these steps:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance where you want to create the app profile.

  3. In the left pane, click **Application profiles**.

  4. Click **Create application profile**.

  5. Select **Standard**.

  6. Click **Next**.

  7. Enter the application profile ID.

The application profile ID is a permanent identifier for the app profile. Your application provides this ID when it connects to Bigtable.

  8. Enter a description of the app profile.

  9. Under **Cluster routing** , select either single-cluster routing or multi-cluster routing. [Learn more](https://docs.cloud.google.com/bigtable/docs/routing).

  10. If you choose **Single-cluster** :

     1. In the **Cluster** list, select the cluster to route requests to.

     2. If you need to enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions), select the **Allow single-row transactions** checkbox.

  11. If you choose **Multi-cluster** :

     1. In the **Cluster group** list, to route requests to any cluster in the instance, select **Any cluster**.
     2. To limit request routing to only some clusters in the instance (cluster group routing), select each cluster that you want to include in the routing group, and then click **OK**.
     3. To route single-row read and write requests to a specific cluster based on the row key of the request, select **Enable row affinity**.
  12. Under **Select a routing priority** , assign a routing priority to your requests by selecting one of the following:

     * **High** : use for latency-sensitive requests
     * **Medium** : use for general-purpose requests
     * **Low** : use for background tasks or less time-critical operations
  13. To create the app profile, click **Create**.

  14. Update your application's code for connecting to Bigtable so that it uses the new app profile. 




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. Use the [`bigtable app-profiles create` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/create) to create an app profile:
         
         gcloud bigtable app-profiles create APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             [--description=DESCRIPTION] \
             [--force] \
             [--route-any] \
             [--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...] \
             [--route-to=CLUSTER_ID] \
             [--transactional-writes] \
             [--priority=PRIORITY] \
             [--row-affinity]
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts the following optional flags: 

     * `--description=DESCRIPTION`: A detailed description of the app profile. 
     * `--force`: Ignore warnings about potential issues and conflicts with other app profiles. 
     * `--route-any`: Enable [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#multi-cluster) to route requests to any available cluster. 

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

     * `--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...`: A list of clusters that requests should be routed to. Use this option if you want to route requests to only some of the clusters in the instance.

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

     * `--route-to=CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 

You cannot combine this flag with the `--route-any` flag. 

     * `--transactional-writes`: Enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) in the app profile. 

You cannot combine this flag with the `--route-any` or `--restrict-to` flags.

     * `--priority=PRIORITY`: The priority level that the app profile should use. Accepted values are `PRIORITY_HIGH`, `PRIORITY_MEDIUM`, or `PRIORITY_LOW`.

     * `--row-affinity`: Enable [row-affinity routing](https://docs.cloud.google.com/bigtable/docs/routing#row-affinity) in the app profile. 

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

  3. Update your application's code for connecting to Bigtable so that it uses the new app profile. 




### Create an in-memory tier app profile

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create an app profile on a cluster with the in-memory tier enabled, follow these steps:

**Note:** You can't enable row-affinity routing for an app profile with in-memory tier.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance where you want to create the app profile.

  3. In the left pane, click **Application profiles**.

  4. Click **Create application profile**.

  5. Select **In-memory tier**.

  6. Click **Next**.

  7. Enter the application profile ID.

The application profile ID is a permanent identifier for the app profile. Your application provides this ID when it connects to Bigtable.

  8. Enter a description of the app profile.

  9. Under **Cluster routing** , select a cluster with the in-memory tier enabled.

In-memory tier clusters must use single-cluster routing.

  10. If you need to enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions), select **Allow single-row transactions**.

  11. Under **Select a routing priority** , assign a routing priority to your requests by selecting one of the following:

     * **High** : use for latency-sensitive requests
     * **Medium** : use for general-purpose requests
     * **Low** : use for background tasks or less time-critical operations
  12. Click **Create** to create the app profile.

  13. Update your application's code for connecting to Bigtable so that it uses the new app profile. 




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. Use the [`gcloud beta bigtable app-profiles create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/create) to create an app profile:
         
         gcloud beta bigtable app-profiles create APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --route-to=CLUSTER_ID \
             --use-memory-layer \
             [--description=DESCRIPTION] \
             [--transactional-writes] \
             [--priority=PRIORITY]
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts the following optional flags: 

     * `--route-to=CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 
     * `--use-memory-layer`: Route requests with this app profile to the in-memory tier. This flag is limited to the Enterprise Plus edition and single-cluster routing.
     * `--description=DESCRIPTION`: A detailed description of the app profile. 
     * `--transactional-writes`: Enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) in the app profile. 
     * `--priority=PRIORITY`: The priority level of requests sent using the app profile. Accepted values are `PRIORITY_HIGH`, `PRIORITY_MEDIUM`, or `PRIORITY_LOW`. Request priorities don't impact requests that are eligible for the in-memory tier.
  3. Update your application's code for connecting to Bigtable so that it uses the new app profile. 




### Create a Data Boost app profile

To create a Data Boost app profile — an app profile that uses Data Boost serverless compute — follow these steps. To make sure your workload is compatible with Data Boost, review the [limitations](https://docs.cloud.google.com/bigtable/docs/data-boost-overview#limitations).

**Note:** To use advanced Data Boost capabilities, your instance must use the Enterprise Plus edition.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance where you want to create the app profile.

  3. In the left pane, click **Application profiles**.

  4. Click **Create application profile**.

  5. Select **Data Boost**.

  6. Click **Next**.

  7. Enter the application profile ID.

The application profile ID is a permanent identifier for the app profile. Your application provides this ID when it connects to Bigtable.

  8. Enter a description of the app profile.

  9. Under **Cluster routing** , select the cluster to route requests to.

  10. Click **Create app profile** to create the app profile.

  11. Update your application's code for connecting to Bigtable so that it uses the new app profile. 




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. Use the [`gcloud beta bigtable app-profiles create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/create) to create an app profile:
         
         gcloud bigtable app-profiles create APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --data-boost \
             --data-boost-compute-billing-owner=HOST_PAYS \
             --route-to=CLUSTER_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 



## Connect with a custom app profile

After you create a custom app profile, you can update your code so that your application uses the app profile when it connects to Bigtable.

The following examples show how to specify an app profile when your app creates a Bigtable client and connects to an instance. Replace `[APP_PROFILE_ID]` with the appropriate value.

### C#
    
    
    var client = BigtableClient.Create(appProfileId: "[APP_PROFILE_ID]");

### Go
    
    
    clientConf := bigtable.ClientConfig{AppProfile:"[APP_PROFILE_ID]"}
    client, err = bigtable.NewClientWithConfig(ctx, project, instance, clientConf)

### HBase Java
    
    
    // If using BigtableOptions directly:
    optionsBuilder.setAppProfileId("[APP_PROFILE_ID]");
    
    // If using BigtableOptionsFactory:
    configuration.set(BigtableOptionsFactory.APP_PROFILE_ID_KEY, "[APP_PROFILE_ID]");
    
    // If using system properties, set "google.bigtable.app_profile.id" to
    // "[APP_PROFILE_ID]"
    
    // If using CloudBigtableIO for Cloud Dataflow:
    config.withConfiguration(BigtableOptionsFactory.APP_PROFILE_ID_KEY,
                             "[APP_PROFILE_ID]");

### Node.js
    
    
    const bigtable = new Bigtable({appProfileId: '[APP_PROFILE_ID]'});

### Python
    
    
    from google.cloud import bigtable
    
    client = bigtable.Client(project=project_id)
    instance = client.instance(instance_id)
    table = bigtable.table.Table(table_id, instance, '[APP_PROFILE_ID]')

## Update an app profile

You can view an instance's app profiles and update their settings at any time. Bigtable warns you about any updates that might cause unexpected changes in behavior.

**Important:** Changes to an app profile take effect immediately, and they apply to any application that uses the app profile. If you need to make changes that shouldn't take effect immediately, create a new app profile instead, and update your application to use the new app profile to connect to Bigtable.

To see how to update an app profile from standard to Data Boost or Data Boost to standard, see Convert an app profile.

### Update a standard app profile

To update a standard app profile, follow these steps:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance with the app profile that you want to update.

  3. In the left pane, click **Application profiles**.

  4. Click edit **Edit application profile** for the app profile that you want to update.

  5. Update the settings as needed.

  6. Click **Save** or, to exit without saving, click **Cancel**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Optional: Use the [`bigtable app-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/describe) to view the app profile's settings:
         
         gcloud bigtable app-profiles describe APP_PROFILE_ID \
             --instance=INSTANCE_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
  4. Use the [`bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/update) to update the app profile's settings:
         
         gcloud bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             [--description=DESCRIPTION] \
             [--force] \
             [--route-any] \
             [--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...]
             [--route-to=CLUSTER_ID] \
             [--transactional-writes] \
             [--row-affinity]
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts the following optional flags: 

     * `--description=DESCRIPTION`: A detailed description of the app profile. 
     * `--force`: Ignore warnings about potential issues and conflicts with other app profiles. 
     * `--route-any`: Enable [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#multi-cluster) to route requests to any available cluster. 

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

     * `--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...`: A list of clusters that requests should be routed to. Use this option if you want to route requests to only some of the clusters in the instance.

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

     * `--route-to=CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 

You cannot combine this flag with the `--route-any` flag. 

     * `--transactional-writes`: Enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) in the app profile. 

You cannot combine this flag with the `--route-any` flag. 

     * `--priority=PRIORITY`: The priority level that the app profile uses. Accepted values are `PRIORITY_HIGH`, `PRIORITY_MEDIUM`, or `PRIORITY_LOW`.




### Update an in-memory tier app profile

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To update an app profile on a cluster with the in-memory tier enabled, follow these steps:

###  Console 

**Note:** You can't enable row-affinity routing for an app profile with in-memory tier in the Google Cloud console.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance with the app profile that you want to update.

  3. In the left pane, click **Application profiles**.

  4. Click edit **Edit application profile** for the app profile that you want to update.

  5. Update the settings as needed.

  6. Click **Save** or, to exit without saving, click **Cancel**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Optional: Use the [`gcloud bigtable app-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/describe) to view the app profile's settings:
         
         gcloud bigtable app-profiles describe APP_PROFILE_ID \
             --instance=INSTANCE_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
  4. Use the [`gcloud beta bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/update) to update the app profile's settings:
         
         gcloud beta bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --route-to=CLUSTER_ID \
             [--description=DESCRIPTION] \
             [--transactional-writes] \
             [--priority=PRIORITY] \
             [--use-memory-layer] \
             [--no-use-memory-layer]
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts the following optional flags: 

     * `--description=DESCRIPTION`: A detailed description of the app profile. 
     * `--route-to=CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 
     * `--transactional-writes`: Enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) in the app profile. 
     * `--priority=PRIORITY`: The priority level that the app profile uses. Accepted values are `PRIORITY_HIGH`, `PRIORITY_MEDIUM`, or `PRIORITY_LOW`.
     * `--use-memory-layer`: Route requests with this app profile to the in-memory tier. Use `--no-use-memory-layer` to disable in-memory tier routing for this app profile. This flag is limited to the Enterprise Plus edition and single-cluster routing.



### Update a Data Boost app profile

To update the cluster that a Data Boost app profile reads from, follow these steps:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. In the **Application profiles** column, click the app profile you want to view or update.

If you don't see the app profile you want to edit, you can view a complete list by clicking the name of the instance and then clicking **Application profiles** in the left pane.

  3. Select the new cluster that traffic should be routed to, and then click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Optional: Use the [`gcloud bigtable app-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/describe) to view the app profile's settings:
         
         gcloud bigtable app-profiles describe APP_PROFILE_ID \
             --instance=INSTANCE_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
  4. Use the [`gcloud beta bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/update) to update the app profile's settings:
         
         gcloud beta bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --route-to=CLUSTER_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: the ID of the new cluster to read from



## Convert an app profile

You can convert a standard app profile to a Data Boost app profile, or convert a Data Boost app profile to a standard app profile. Before you convert an app profile, review the guidance at [App profile changes](https://docs.cloud.google.com/bigtable/docs/app-profiles#changes).

### Convert from standard to Data Boost

Before you update an app profile from standard (provisioned nodes for compute) to Data Boost serverless compute, check the Data Boost [eligibility metrics](https://docs.cloud.google.com/bigtable/docs/data-boost-overview). You should also be aware of [Data Boost limitations](https://docs.cloud.google.com/bigtable/docs/data-boost-overview#limitations).

**Note:** To use advanced Data Boost capabilities, your instance must use the Enterprise Plus edition.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. In the **Application profiles** column, click the app profile you want to update.

If you don't see the app profile you want to edit, you can view a complete list by clicking the name of the instance, then clicking **Application profiles** in the left pane.

  3. Select **Data Boost**.

  4. Select the cluster that requests should be routed to.

  5. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Optional: Use the [`bigtable app-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/describe) to view the app profile's settings:
         
         gcloud bigtable app-profiles describe APP_PROFILE_ID \
             --instance=INSTANCE_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
  4. Use the [`gcloud beta bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/update) to convert an app profile from standard to Data Boost:
         
         gcloud bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --data-boost \
             --data-boost-compute-billing-owner=HOST_PAYS \
             --route-to=CLUSTER_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 



### Convert from Data Boost to standard

To change an app profile from using Data Boost (serverless compute) to standard (provisioned nodes for compute) follow these steps:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. In the **Application profiles** column, click the app profile you want to update.

If you don't see the app profile you want to edit, you can view a complete list by clicking the name of the instance, then clicking **Application profiles** in the left pane.

  3. Select **Standard**.

  4. Click **Next**.

  5. Optional: Edit the app profile description.

  6. Under **Cluster routing** , select either single-cluster routing or multi-cluster routing. [Learn more](https://docs.cloud.google.com/bigtable/docs/routing).

  7. If you choose **Single-cluster** :

     1. In the **Cluster** list, select the cluster to route requests to.

     2. If you need to enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions), select the **Allow single-row transactions** checkbox.

  8. If you choose **Multi-cluster** :

     1. In the **Cluster group** list, to route requests to any cluster in the instance, select **Any cluster**.
     2. To limit request routing to only some clusters in the instance (cluster group routing), select each cluster that you want to include in the routing group, and then click **OK**.
     3. To route single-row read and write requests to a specific cluster based on the row key of the request, select **Enable row affinity**.
  9. Under **Select a routing priority** , assign a routing priority to your requests by selecting one of the following:

     * **High** : use for latency-sensitive requests
     * **Medium** : use for general-purpose requests
     * **Low** : use for background tasks or less time-critical operations
  10. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Optional: Use the [`bigtable app-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/describe) to view the app profile's settings:
         
         gcloud bigtable app-profiles describe APP_PROFILE_ID \
             --instance=INSTANCE_ID
         

  4. Use the [`gcloud beta bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/app-profiles/create) to convert the app profile:
         
         gcloud bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --standard \
             [--route-any] \
             [--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...]
             [--route-to=CLUSTER_ID] \
             [--transactional-writes]
         




Provide the following: 

  * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
  * `INSTANCE_ID`: The permanent identifier for the instance. 



The command accepts the following optional flags: 

  * `--route-any`: Enable [multi-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#multi-cluster) to route requests to any available cluster. 

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

  * `--restrict-to=CLUSTER_ID_1, CLUSTER_ID_2...`: A list of clusters that requests should be routed to. Use this option if you want to route requests to only some of the clusters in the instance.

You cannot combine this flag with the `--route-to` or `--transactional-writes` flags. 

  * `--route-to=CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 

You cannot combine this flag with the `--route-any` flag. 

  * `--transactional-writes`: Enable [single-row transactions](https://docs.cloud.google.com/bigtable/docs/routing#single-row-transactions) in the app profile. 

You can't combine this flag with the `--route-any` or `--restrict-to` flags.




## Delete an app profile

You can delete an instance's custom app profiles, but not the default app profile.

**Warning:** Don't delete a custom app profile that an application is still using. After you delete a custom app profile, any requests that use that app profile will fail.

To delete a custom app profile:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the app profile you want to delete.

  3. In the left pane, click **Application profiles**.

  4. Open the **more actions** menu more_vert, then click **Delete application profile**. A confirmation dialog appears.

  5. Follow the instructions in the confirmation dialog, then click **Delete**. 




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable app-profiles delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/delete) to delete the app profile:
         
         gcloud bigtable app-profiles delete APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             [--force]
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts the following optional flag: 

`--force`: Ignore warnings about potential issues and conflicts with other app profiles. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
