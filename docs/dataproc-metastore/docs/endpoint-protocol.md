---
url: https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol/
title: Choose an endpoint protocol for Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:56.687637+00:00
---

# Choose an endpoint protocol for Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/endpoint-protocol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Choose an endpoint protocol for Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to choose an endpoint protocol for Dataproc Metastore.

You first choose your endpoint protocol when you create a Dataproc Metastore service. This choice affects the features that you can integrate and use with your service. It's important to note that once you choose an endpoint protocol, there are some restrictions if you want to change it. Make sure you choose the appropriate protocol for your needs.

To understand the differences between endpoint protocols, see [About endpoint protocols](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols).

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service) in your project.
  * [Understand networking requirements](https://docs.cloud.google.com/dataproc-metastore/docs/access-service) specific to your project.



### Required Roles

To get the permission that you need to create a Dataproc Metastore, ask your administrator to grant you the following IAM roles on your project, based on the principle of least privilege: 

  * [Grant full control of Dataproc Metastore resources ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.editor) (`roles/metastore.editor`)
  * [Grant full access to all Dataproc Metastore resources, including IAM policy administration ](https://docs.cloud.google.com/iam/docs/roles-permissions/metastore#metastore.admin) (`roles/metastore.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `metastore.services.create` permission, which is required to create a Dataproc Metastore. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about specific Dataproc Metastore roles and permissions, see [Manage Managed Service for Apache Spark access with IAM](https://docs.cloud.google.com/dataproc-metastore/docs/iam-and-access-control). 

## Choose an endpoint protocol

The following examples show an abbreviated version of the steps that you follow to choose an endpoint protocol. For complete step-by-step instructions on the entire process you must follow, see [Create a Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/create-service).

### For a new Dataproc Metastore service

To create a Dataproc Metastore service and choose the endpoint protocol for the first time, follow these instructions:

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. In the **Dataproc Metastore** Navigation menu, click **Create**.

The **Create service** page opens.

  3. In the **Endpoint protocol** section, select **Thrift** or **gRPC**.

Thrift is the default preselected endpoint protocol.

You can only update an existing endpoint protocol from Thrift to gRPC. If you want to move from gRPC to Thrift, create a new Dataproc Metastore service.

**Tip:** We recommend that you use the gRPC protocol. gRPC provides additional security through Identity and Access Management (IAM). It also supports federation integrations with other Google Cloud products. For more information about choosing an endpoint protocol, see [About endpoint protocols](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols).
  4. Choose the [remaining configurations](https://docs.cloud.google.com/dataproc-metastore/docs/create-service) for your service, as needed.

  5. To create and start the service, click **Submit**.

If you selected a gRPC endpoint, you must grant additional IAM permissions to your service. For more information, see [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints).




### gcloud CLI

  1. To choose an endpoint protocol, run the following [`gcloud metastore services create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create) command:
         
         gcloud metastore services create SERVICE \
            --endpoint-protocol=ENDPOINT_PROTOCOL ; default="thrift"
         

Replace the following:

     * `SERVICE_ID`: The name or ID for your Dataproc Metastore service.
     * `ENDPOINT_PROTOCOL`: The endpoint protocol that you want to use for your Dataproc Metastore. You can specify either `thrift` or `grpc`.

Thrift is the default preselected endpoint protocol.

You can only update an existing endpoint protocol from Thrift to gRPC. If you want to move from gRPC to Thrift, you must create a new service.

**Tip:** We recommend that you use the gRPC protocol. gRPC provides additional security through Identity and Access Management (IAM). It also supports federation integrations with other Google Cloud products. For more information about choosing an endpoint protocol, see [About endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/about-endpoint-protocols).
  2. Verify that your service was successfully created.

If you selected a gRPC endpoint protocol, you must add additional IAM permissions to your account. For more information, see [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints).




### For an existing Dataproc Metastore service

To update the endpoint protocol of an existing Dataproc Metastore service, follow these instructions:

**Note:** You can only update an existing endpoint protocol from Thrift to gRPC. If you want to move from gRPC to Thrift, you must create a new service.

### Console

  1. In the Google Cloud console, open the Dataproc Metastore page:

[Open Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the service to update.

The **Service detail** page opens.

  3. On the **Configuration** tab, click **Edit**.

The **Edit service** page opens.

  4. In the **Endpoint protocol** section, select **gRPC**.

  5. To update the service, click **Submit**.

After updating to the gRPC endpoint protocol, you must add additional IAM permissions to your account. For more information, see [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints).




### gcloud CLI

  1. To update an endpoint protocol, run the following [`gcloud metastore services update`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/update) command:
         
         gcloud metastore services update SERVICE \
            --endpoint-protocol=ENDPOINT_PROTOCOL
         

Replace the following:

     * `SERVICE`: The name of your Dataproc Metastore service.
     * `ENDPOINT_PROTOCOL`: The endpoint protocol that you want to update for your Dataproc Metastore service. You can only specify `grpc`.
  2. Verify that your update was successful.

After updating to a gRPC endpoint, you must grant additional IAM permissions to your service. For more information, see [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints).




## Find your endpoint URI value

### Console

You can view your endpoint URI on the **Dataproc Metastore** page.

  * For Thrift endpoints, the **URL** value starts with `thrift://`
  * For gRPC endpoints, the **URL** value starts with `https://`



The following image shows an example of a Dataproc Metastore service configured with a gRPC endpoint protocol.

![A service detail page showing the URL and hive.metastore.warehouse.dir values for a service configured with a gRPC endpoint protocol](https://docs.cloud.google.com/static/dataproc-metastore/images/dataproc-metastore-endpoint-uri.png)

### gcloud CLI

To view your endpoint URI, run the following [`gcloud metastore services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/describe) command:
    
    
    gcloud metastore services describe SERVICE --format="get(endpointUri)"
    

Replace the following:

  * `SERVICE`: The name of your Dataproc Metastore service.



## What's next

  * [Access gRPC endpoints](https://docs.cloud.google.com/dataproc-metastore/docs/grpc-endpoints)
  * [Attach a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
