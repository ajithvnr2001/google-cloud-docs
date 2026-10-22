---
url: https://docs.cloud.google.com/dataproc-metastore/docs/manage-service/
title: Update a Dataproc Metastore service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:40.422948+00:00
---

# Update a Dataproc Metastore service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/manage-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Update a Dataproc Metastore service Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to update a Dataproc Metastore service.

You can update your Dataproc Metastore service to change configuration settings, or to enable or disable optional features.

## Before you begin

  * [Enable Dataproc Metastore in your project](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service).
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).



### Required roles

To get the permission that you need to update a Dataproc Metastore service, ask your administrator to grant you the following IAM roles on your project, based on the principle of least privilege: 

  * [Grant full control of Dataproc Metastore resources ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)
  * [Grant full access to all Dataproc Metastore resources, including IAM policy administration ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `metastore.services.update` permission, which is required to update a Dataproc Metastore service. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Dataproc Metastore IAM overview](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## About updating a service

You can update the following Dataproc Metastore parameters.

  * **Port number**. Update the TCP port number of the Apache Thrift interface.
  * **Service tier**. Switch between the **Developer** service tier or **Enterprise** service tier. These tiers influence the capacity of the service.
  * **Data Catalog sync**. Toggle the Data Catalog sync feature on or off.
  * **Maintenance window**. Change the frequency of your maintenance window, including **Day of week** and **Hour of day**.
  * **Kerberos**. Enable or disable Kerberos authentication. If previously enabled, you can update your Kerberos configuration files.
  * **Hive metastore configurations**. Update the location of your Hive warehouse directory.
  * **Auxiliary version config** ([Preview](https://cloud.google.com/products/#product-launch-stages)). Enable, disable, or add additional auxiliary versions.
  * **Labels**. Add or remove optional labels that describe your metadata.
  * **Scaling factor**. Change the scaling factor. You can enable or disable autoscaling and update the minimum or maximum scaling factors.

**Note:** To update other Dataproc Metastore parameters that aren't included in the previous list, you must [delete your service](https://docs.cloud.google.com/dataproc-metastore/docs/delete-service) and create a new one.

## Update a service

Before running an update, note the following considerations:

  * You can only run a single update job at a time (for each Dataproc Metastore service).
  * You can update multiple parameters in a single update job.
  * You can still use your Dataproc Metastore while it's being updated.



When the update succeeds, Dataproc Metastore automatically enters an [active](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#state) state. If the update fails, then the Dataproc Metastore service rolls back to its previous healthy state.

The following instructions show you how to update a Dataproc Metastore service.

### Console

  1. In the Google Cloud console, open the **Dataproc Metastore** page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service name of the service that you want to update.

The **Service detail** page opens.

![Service detail page](https://docs.cloud.google.com/static/dataproc-metastore/images/service-detail-page.png) The Dataproc Metastore Service detail page 
  3. On the **Configuration** tab, click **Edit**.

The **Edit service** page opens.

  4. Choose the values that you want to update for your service.

  5. Click **Submit**.

Return to the **Dataproc Metastore** page, and verify that your service was successfully updated.




### gcloud CLI

  1. To update a service, run the following [`gcloud metastore services update`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/update) command:
         
         gcloud metastore services update SERVICE \
             --location=LOCATION \
             --port=PORT \
             --tier=TIER \
             --kerberos_principal=KERBEROS_PRINCIPAL \
             --keytab=KEYTAB \
             --krb5-config=KRB5_CONFIG \
             --update-hive-metastore-configs-from-file=[KEY=VALUE, ...] \
             --clear-hive-metastore-configs \
             --remove-hive-metastore-configs=[KEY, ...] \
             --update-labels=[KEY=VALUE, ...] \
             --clear-labels \
             --remove-labels=[KEY, ...]
         

Replace the following:

     * `SERVICE`: The name of your Dataproc Metastore service.
     * `LOCATION`: The Google Cloud region that your Dataproc Metastore service resides in.
     * `PORT`: Optional: The TCP port of the Thrift interface you're using with your Dataproc Metastore service.
     * `TIER`: Optional: The tier capacity of your Dataproc Metastore service.
     * `MAINTENANCE_WINDOW_DAY`: Optional: The day of week when the service window starts.
     * `MAINTENANCE_WINDOW_HOUR`: Optional: The hour of day when the service window starts.
     * `KERBEROS_PRINCIPAL`: Optional: A Kerberos principal that exists in both the keytab and the KDC. A typical principal is of the form "primary/instance@REALM", but there's no exact format.
     * `KEYTAB`: Optional: A Kerberos keytab file that is used to authenticate a service principal with a Kerberos Key Distribution Center.
     * `KRB5_CONFIG`: Optional: The krb5.config file specifies the KDC and the Kerberos realm information, which includes locations of KDCs and defaults for the realm and Kerberos applications.
     * `[KEY, ...]`: Optional: The Hive metastore configs you want to update. If a variable exists in this field, its value is updated. Otherwise, a new variable is created. If this flag is set, then `-clear-hive-metastore-configs` is automatically set as well.
     * `[KEY, ...]`: Optional: The Hive metastore configs you want to remove.
     * `[KEY=VALUE, ...]`: Optional: The labels or Hive metastore key-value pair configs you want to update.
     * `[KEY, ...]`: Optional: The labels or Hive metastore key-value pair configs you want to remove.
  2. Verify that the update was successful.




### REST

Follow the API instructions to [update a service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/patch) by using the APIs Explorer.

## Update the Hive Metastore warehouse config

If your Hive warehouse directory is on Cloud Storage, you should set a Metastore config override. This override sets your specific data warehouse as the default warehouse directory for Dataproc Metastore

Before you set this override, make sure that your Dataproc Metastore service has object read and write permissions to access the warehouse directory. For more information, see [Hive warehouse directory](https://docs.cloud.google.com/dataproc-metastore/docs/hive-metastore#hive-warehouse-dir).

The following instructions show you how to update a Hive Metastore config override.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service name of the service you want to update.

The **Service detail** page opens.

  3. On the **Configuration** tab, click **Edit**.

The **Edit service** page opens.

  4. In the **Metastore config overrides** , enter the following:

     * **Key** : Enter the following value: `hive.metastore.warehouse.dir`.
     * **Value** : The Cloud Storage location of your warehouse directory. For example: `gs://my-bucket/path/to/location`.
  5. Click **Submit**.

Return to the **Dataproc Metastore** page, and verify that your service was successfully updated.




### gcloud

  1. To update a service, run the following `gcloud metastore services update` command:
         
         gcloud metastore services update SERVICE \
             --location=LOCATION \
             --update-hive-metastore-configs="hive.metastore.warehouse.dir=CUSTOMER_DIR"
         

Replace the following:

     * `SERVICE`: The name of your Dataproc Metastore service.
     * `LOCATION`: The Google Cloud region that your Dataproc Metastore service resides in.
     * `CUSTOMER_DIR`: The Cloud Storage location of your warehouse directory. For example: `gs://my-bucket/path/to/location`
  2. Verify that the update was successful.




## What's next

  * [Cloud audit logging](https://docs.cloud.google.com/dataproc-metastore/docs/audit-logging)
  * [Dataproc Metastore IAM and access control](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control)
  * [Service access](https://docs.cloud.google.com/dataproc-metastore/docs/access-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
