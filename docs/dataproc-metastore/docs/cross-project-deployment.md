---
url: https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment/
title: Set up a cross-project deployment \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:42.396095+00:00
---

# Set up a cross-project deployment  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/cross-project-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Set up a cross-project deployment Stay organized with collections  Save and categorize content based on your preferences. 

You can set up a cross-project deployment for Dataproc Metastore to separate the following resources:

  * The Dataproc Metastore service.
  * The Managed Service for Apache Spark cluster attached to the Dataproc Metastore service.
  * The network used by the Managed Service for Apache Spark cluster.



## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.



### Required Roles

To get the permissions that you need to create a Dataproc Metastore and a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * To grant full control of Dataproc Metastore resources: [Dataproc Metastore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`) on the metastore project. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## About cross-project deployments

A cross-project deployment for Dataproc Metastore can consist of the following configurations:

  * Two projects:

    * Project one contains the Managed Service for Apache Spark cluster (cluster project).
    * Project two contains the Dataproc Metastore service and the network (metastore project and network project).
  * Two projects:

    * Project one contains the Managed Service for Apache Spark cluster.
    * Project two contains the Dataproc Metastore service and the network (metastore project and network project).
  * Two projects:

    * Project one contains the Managed Service for Apache Spark cluster and the Dataproc Metastore service (cluster project and metastore project).
    * Project two contains the network (network project).
  * Three projects:

    * Project one contains the Managed Service for Apache Spark cluster (cluster project).
    * Project two contains the Dataproc Metastore service (metastore project).
    * Project three contains the network (network project).



The following diagram provides an overview of the possible project configurations you can use.

![Overview of the possible project configurations when deploying a
Dataproc Metastore and Managed Service for Apache Spark cluster](https://docs.cloud.google.com/static/dataproc-metastore/images/cross-project-deployment-diagram.svg)

## Cross-project permissions

Before you set up cross-project permissions, determine if it's necessary for your configuration:

**You must set up additional cross-project permissions**

  * If your Managed Service for Apache Spark cluster and Dataproc Metastore service are in separate projects.

  * If your Dataproc Metastore service and network are in separate projects.




## Set up cross-project permissions

If the cluster project and metastore project are in separate projects, grant the following roles:

  * `roles/metastore.user` to the cluster project's Managed Service for Apache Spark Service Agent account (contained in the metastore project's IAM policy). This configuration applies to both the Thrift and gRPC endpoint protocols.



If the network project and metastore project are in separate projects, grant the following roles:

  * `roles/metastore.serviceAgent` to the [metastore project Service Agent](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control#service-accounts) (contained in the network project's IAM policy). This configuration only applies to the Thrift endpoint protocol.




### Console

To find your project number:

  1. Navigate to the IAM & Admin [**Settings**](https://console.cloud.google.com/iam-admin/settings/project) tab.

  2. From the project list at the top of the page, select the project you want to use to create the Managed Service for Apache Spark cluster.

  3. Note the project number.




Configure the permissions:

  1. Navigate to the [**IAM**](https://console.cloud.google.com/iam-admin/iam/project) tab.

  2. From the project list at the top of the page, select the metastore project.

  3. Click **Add**.

  4. Enter the service account in the **New Principals** field.

  5. From the Roles menu, select **Dataproc Metastore > Dataproc Metastore Viewer**.

  6. Click **Add**.




After you have completed the previous steps, you can create a Managed Service for Apache Spark cluster that's attached to a Dataproc Metastore service. Note that to do this, the Managed Service for Apache Spark cluster's network or subnetwork configuration must match the Dataproc Metastore network or subnetwork.

**Note:** If you're using a VPC network belonging to a different project than the service, you must provide the entire relative resource name in `gcloud metastore services create SERVICE`.

For example:
    
    
    gcloud metastore services create SERVICE \
         --network=projects/HOST_PROJECT/global/networks/NETWORK_ID

## What's next

  * [Quickstart for deploying Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)
  * [Dataproc Metastore overview](https://docs.cloud.google.com/dataproc-metastore/docs/overview)
  * [Managed Service for Apache Spark overview](https://docs.cloud.google.com/dataproc/docs/concepts/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
