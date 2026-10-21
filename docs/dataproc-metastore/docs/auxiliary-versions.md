---
url: https://docs.cloud.google.com/dataproc-metastore/docs/auxiliary-versions/
title: Auxiliary versions \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:56.998012+00:00
---

# Auxiliary versions  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/auxiliary-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Auxiliary versions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the auxiliary versions feature with Dataproc Metastore.

Auxiliary versions let you connect two different versions of a Hive metastore to a single Dataproc Metastore service. This configuration lets you support multiple data processing engines that need to run on different Hive metastore versions.

For example, using auxiliary versions, you can connect multiple Managed Service for Apache Spark clusters to the same Dataproc Metastore service. In this configuration, one cluster can run Managed Service for Apache Spark version 2.0 while the other runs Managed Service for Apache Spark version 1.5. The Managed Service for Apache Spark 2.0 cluster can connect to an endpoint that exposes Hive version 3.1.2, while the Managed Service for Apache Spark 1.5 cluster connects to an endpoint that exposes Hive version 2.3.6.

## How auxiliary versions work

When you enable auxiliary versions, Dataproc Metastore exposes a separate endpoint for each Hive metastore version. However, both endpoints continue to share the same metadata database.

This feature doesn't let you use different sets of metadata with a single Dataproc Metastore service. Instead, it offers a way for you to extend and enhance compatibility between your services.

**Note:** When you enable this feature, the original Hive metastore in your configuration is called the _primary version_ and the other Hive metastore is called the _auxiliary version_.

### Considerations

**General**

  * You can only create one auxiliary version for each Dataproc Metastore service.

  * The auxiliary version must be configured to use a lower Hive metastore version than the primary version.

  * The auxiliary version maintains a separate log file than the primary version. To debug Hive metastore issues, you can use [Cloud Logging](https://docs.cloud.google.com/dataproc-metastore/docs/logging).




**Feature support**

  * The auxiliary version doesn't support the following features:

    * [Import metadata](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata), [Export metadata](https://docs.cloud.google.com/dataproc-metastore/docs/export-metadata)
    * [Back up from a metastore](https://docs.cloud.google.com/dataproc-metastore/docs/backup-metadata), [Restore a metastore from a backup](https://docs.cloud.google.com/dataproc-metastore/docs/restore-metadata)

The metadata-related features (import/export/backup/restore) can only be used with the primary version, since the backend metadata between both versions is shared.

  * Some Hive methods might not be compatible between the auxiliary and the primary version. This compatibility depends on what versions of Hive you're using for your primary and auxiliary versions and the methods that are compatible between the Hive versions.

  * Not all functions of a primary Dataproc Metastore instance are supported by the auxiliary version. For example, inserting records into a Hive transactional table is not supported with a Hive 2 client interfacing with an auxiliary version 2.3.6. However, this operation is supported with a Hive 3 client interfacing with primary version 3.1.2.

If a feature in a lower Hive version is deprecated in a higher Hive version, then the corresponding lower auxiliary version won't support the deprecated feature. For example, Hive 2 supports [indexes](https://cwiki.apache.org/confluence/display/hive/indexdev), but an auxiliary version running Hive 2.3.6 won't support the index if the primary version runs Hive 3.1.2.

  * Creating transactional tables using the auxiliary version or inserting any data in transactional tables in the auxiliary version is prevented.




### Shared properties between versions

When you create an auxiliary version, some properties are shared and remain common between the auxiliary version and the primary version. Other properties aren't shared and are separate between both versions.

The following table lists these differences.

Properties | Common | Separate  
---|---|---  
**Endpoint** |  | ✓  
**Hive config overrides** * |  | ✓  
**Kerberos config** | ✓ |   
**Endpoint protocol (Thrift/gRPC)** | ✓ |   
**Thrift port** | ✓ |   
**Artifacts Cloud Storage bucket** | ✓ |   
**Tier** | ✓ |   
**Maintenance window** | ✓ |   
**Release channel** | ✓ |   
**Encryption config** | ✓ |   
**Database type** | ✓ |   
**Data Catalog sync toggle** | ✓ |   
**Request count metric** |  | ✓  
**Network configurations** |  | ✓  
  
* The Hive configuration overrides remain separate between the auxiliary and the primary version. However, the auxiliary version references a merged list of the overrides (primary+auxiliary). In this case, the auxiliary configuration takes precedence over the primary configuration.

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service)



### Required Roles

To get the permission that you need to create a Dataproc Metastore that uses auxiliary versions, ask your administrator to grant you the following IAM roles on your project, based on the principle of least privilege: 

  * [Grant full control of Dataproc Metastore resources ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)
  * [Grant full access to all Dataproc Metastore resources, including IAM policy administration ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `metastore.services.create` permission, which is required to create a Dataproc Metastore that uses auxiliary versions. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage Managed Service for Apache Spark access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Create an auxiliary version for a new service

The following example shows an abbreviated version of the steps that you follow to enable auxiliary versions. For complete step-by-step instructions on the entire process you must follow, see [Create a Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. At the top of the **Dataproc Metastore** page, click the **Create** button.

The **Create service** page opens.

  3. Under **Auxiliary version config** , enable auxiliary versions.

  4. Click **Add Auxiliary Version**.

     1. Enter a name for your auxiliary version.

     2. Select a version for your auxiliary version.

     3. Optional: To apply a mapping to the auxiliary version, click **\+ Add Overrides**.

     4. Click **Done**.

  5. Choose the [remaining configurations](https://docs.cloud.google.com/dataproc-metastore/docs/create-service) for your service, as needed.

  6. Click **Submit**.




### gcloud CLI

  1. To create a Dataproc Metastore service with an auxiliary version, run one of the following [`gcloud metastore services create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create) commands:
         
         gcloud metastore services create SERVICE \
             --location=LOCATION \
             --auxiliary-versions=AUXILIARY_VERSIONS, ...
         

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the region you want to create your Dataproc Metastore service in.
     * `AUXILIARY_VERSIONS`: a comma-separated list of the Hive metastore versions to deploy for your auxiliary version. Only one auxiliary version is supported. Use the following format `"2.3.6"`.
     * `AUXILIARY_VERSIONS_FROM_FILE`: a path to a YAML file containing the auxiliary versions configuration. For more information and an example, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create#--auxiliary-versions).
  2. Verify that the creation was successful.




### curl

To create a Dataproc Metastore service with an auxiliary version, use the [`create`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/create) method.

**Note:** The following command assumes that you have logged in to the gcloud CLI with your user account by executing gcloud init or gcloud auth login, or by using Cloud Shell, which automatically logs you into the gcloud CLI. You can check the active account by running `gcloud auth list`.
    
    
    curl -X POST -s -i \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -d '{"network":"projects/PROJECT_ID/global/networks/default", "port": 9083, "hive_metastore_config": {"auxiliary_versions": {"aux-version1": {"version": "AUX_VERSION"} } } }' \
         -H "Content-Type:application/json" \
         https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services?service_id=SERVICE_ID
    

Replace the following:

  * `SERVICE_ID`: the name of your new Dataproc Metastore service.
  * `PROJECT_ID`: the Google Cloud project ID that you're creating the Dataproc Metastore service in.
  * `LOCATION`: the region where your Dataproc Metastore resides.
  * `AUX_VERSIONS`: a comma-separated list of Hive metastore versions to deploy. Only one auxiliary version is supported.



## Update an auxiliary version for an existing service

The following instructions show you how to update an existing Dataproc Metastore service that uses auxiliary versions.

When running an update operation, you can complete the following tasks:

  * Add a new auxiliary version.
  * Delete an existing auxiliary version.
  * Add or modify overrides of an existing auxiliary version.




### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service name of the service you want to update.

The **Service detail** page opens.

  3. On the **Configuration** tab, click **Edit**.

The **Edit service** page opens.

  4. In the **Auxiliary version config** section, click the toggle to enable or disable auxiliary versions.

You can complete the following tasks:

     1. To delete an existing auxiliary version, click **Delete**.

     2. To add a new auxiliary version, click **Add Auxiliary Version**.

     3. To apply an override mapping to an auxiliary version, click **\+ Add Overrides**.

  5. Click **Submit**.




### gcloud CLI

  1. To update a Dataproc Metastore service that uses an auxiliary version, run one of the following [`gcloud metastore services update`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/update) commands:
         
         gcloud metastore services update SERVICE \
            --location=LOCATION \
            --add-auxiliary-versions=AUXILIARY_VERSIONS, ...
         

or
         
         gcloud metastore services update SERVICE \
            --location=LOCATION \
            --update-auxiliary-versions-from-file=AUXILIARY_VERSIONS_FROM_FILE
         

Replace the following:

     * `SERVICE`: the name of your Dataproc Metastore service.
     * `LOCATION`: the region where your Dataproc Metastore resides.
     * `AUXILIARY_VERSIONS`: a comma-separated list of auxiliary Hive metastore versions to deploy.
     * `AUXILIARY_VERSIONS_FROM_FILE`: a path to a YAML file containing the auxiliary versions configuration; for more information and an example, see the [SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create).
  2. Verify that the update was successful.




### curl

To update a Dataproc Metastore service that uses an auxiliary version, use the [`patch`](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/patch) method.

**Note:** The following command assumes that you have logged in to the gcloud CLI with your user account by executing gcloud init or gcloud auth login, or by using Cloud Shell, which automatically logs you into the gcloud CLI. You can check the active account by running `gcloud auth list`.
    
    
    curl -X PATCH -s -i \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -d '{"hive_metastore_config": {"auxiliary_versions": {"aux-version1": {"version": "AUX_VERSION} } } }' \
       -H "Content-Type:application/json" \
       https://metastore.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/services/SERVICE_ID?update_mask=hive_metastore_config.auxiliary_versions
    

Replace the following:

  * `SERVICE_ID`: the name of your Dataproc Metastore service.
  * `PROJECT_ID`: the Google Cloud project ID that you're creating the Dataproc Metastore service cluster in.
  * `LOCATION`: the region in which your Dataproc Metastore resides.
  * `AUX_VERSIONS`: a comma-separated list of auxiliary Hive metastore versions to deploy.



## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
