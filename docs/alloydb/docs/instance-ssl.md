---
url: https://docs.cloud.google.com/alloydb/docs/instance-ssl/
title: Configure SSL enforcement mode on AlloyDB instances \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:21.875020+00:00
---

# Configure SSL enforcement mode on AlloyDB instances  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure SSL enforcement mode on AlloyDB instances Stay organized with collections  Save and categorize content based on your preferences. 

To secure client connections and control whether unencrypted traffic or client certificates are permitted, you can configure the SSL enforcement mode on your AlloyDB for PostgreSQL instances.

By default, an AlloyDB instance accepts only connections using SSL.

AlloyDB uses SSL to establish secure, authenticated, and encrypted connections to AlloyDB instances. In addition, a configurable SSL enforcement mode ensures that all database connections to an instance use SSL encryption.

This document covers how to configure the SSL enforcement mode on an existing instance. For information about how to configure the SSL enforcement mode when you create an instance, see [create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create).

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Configure the SSL enforcement mode on an instance

### Console

  1. Go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource name** column.
  3. In the **Overview** page, go to the **Instances in your cluster** section, and click **Edit primary**.
  4. In the **Edit primary instance** pane, expand **Advanced configuration options**.
  5. Enable **Only allow SSL connections**. By default, this option is enabled.
  6. Click **Update instance**.



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--ssl-mode=ENCRYPTED_ONLY` argument to allow only encrypted database connections to an AlloyDB instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --ssl-mode=ENCRYPTED_ONLY

Replace the following:

  * `INSTANCE_ID`: The ID of the instance that you are updating.
  * `REGION_ID`: The region where the instance is placed.
  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



To allow unencrypted database connections to an instance, use the `gcloud alloydb instances update` command with the `--ssl-mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` argument.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --ssl-mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED

If the command returns an error message that includes the phrase `invalid cluster state MAINTENANCE`, then the cluster is undergoing routine maintenance. This temporarily disallows instance reconfiguration. Run the command again after the cluster returns to a `READY` state. To check the cluster's status, see [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
