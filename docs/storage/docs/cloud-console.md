---
url: https://docs.cloud.google.com/storage/docs/cloud-console/
title: Google Cloud console \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:42.327180+00:00
---

# Google Cloud console  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

The browser-based Google Cloud console tool lets you manage your Cloud Storage resources through a graphical interface. Use the Google Cloud console to manage your data if you prefer using a user interface through the browser.

This page describes how to access the Google Cloud console and lists tasks in Cloud Storage that can be performed using the Google Cloud console. As an alternative to the Google Cloud console, you can also use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), [REST API](https://docs.cloud.google.com/storage/docs/json_api), or [Cloud Storage client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).

## Console features

The Google Cloud console provides the following features:

  * Access to all your Google Cloud projects
  * Access to the [Cloud Shell](https://docs.cloud.google.com/shell/docs)
  * A customizable project dashboard, with an overview of Google Cloud resources, billing, and a filterable activity listing
  * Access to all Google Cloud APIs, with a dashboard specific to each API, and access to manage your resources
  * Links to Google Cloud starting points, news, and documentation



The Google Cloud console is used to perform a variety of tasks in Cloud Storage, such as the following:

  * [Creating buckets](https://docs.cloud.google.com/storage/docs/creating-buckets)
  * [Uploading objects to buckets](https://docs.cloud.google.com/storage/docs/uploading-objects) and [downloading objects from buckets](https://docs.cloud.google.com/storage/docs/downloading-objects)
  * Filtering and sorting lists of buckets and objects
  * [Deleting objects](https://docs.cloud.google.com/storage/docs/deleting-objects)
  * Creating and managing [folders](https://docs.cloud.google.com/storage/docs/folder-types)
  * [Controlling access to your data and resources](https://docs.cloud.google.com/storage/docs/access-control) by using Identity and Access Management (IAM) and ACLs
  * [Monitoring buckets and bandwidth usage](https://docs.cloud.google.com/storage/docs/monitoring)
  * Using Cloud Storage features like [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache), [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), and [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

## Access to the Google Cloud console

The Google Cloud console requires no setup or installation, and you can access it directly in a browser. Depending on your use case, you access the Google Cloud console using different URLs. If you are:

A user granted access to a project
    

Use: `https://console.cloud.google.com/`

    

[Go to the Google Cloud console](https://console.cloud.google.com/)

    

A current project owner can [give you access to the entire project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role), which applies equally to all buckets and objects defined in the project.

A user granted access to a bucket
    

Use: `https://console.cloud.google.com/storage/browser/BUCKET_NAME`

    

In this use case, a project owner gives you access to an individual bucket within a larger project. The owner then sends you the bucket name which you substitute into the URL. You are able to only work with objects in the specified bucket. This is useful for users who don't have access to the full project, but who need to access a bucket. When you access the URL, you authenticate if you are not already signed in.

    

A variation of this use case is when a project owner grants **All Users** permission to read objects in a bucket. This creates a bucket whose contents are publicly readable. For more information, see [Make data public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).

A user granted access to an object
    

Use: `https://console.cloud.google.com/storage/browser/_details/BUCKET_NAME/OBJECT_NAME`

    

In this use case, a project owner gives you access to single objects within a bucket and sends you the URL to access the objects. When you access the URLs, you are prompted to authenticate with a user account if you are not already signed in.

    

Note that the form of this URL is different from the URL for objects that are [shared publicly](https://docs.cloud.google.com/storage/docs/access-control/making-data-public). When you share a link publicly, the URL is of the form: `https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME`. This public URL does not require a recipient to authenticate with a valid account and can be used for non-authenticated access to an object.

## Filtering and sorting lists of buckets and objects

In the Google Cloud console list of buckets for a project, you can filter and sort the buckets you see.

  * To filter buckets, click **Filter buckets**. Then, specify the columns and values you want to filter by.

  * To sort buckets, click arrow_upward **Sort** next to the name of the column you want to sort by.

  * To improve filtering performance in projects with more than 1,000 buckets, you can limit filtering options and disable sorting. To do this, click **View options**. Select **Filter by name prefix only** , and then click **Save**. Then, specify the bucket name prefix you want to filter by.

**Note:** Projects with more than 1,000 buckets might experience degraded filtering and sorting performance.
  * To switch the list view between live buckets and soft-deleted buckets, click **View options**. Then, select **Live buckets only** or **Soft deleted buckets only**.




In the Google Cloud console list of objects for a bucket, you can filter the objects you see by using the **Filter** field.

  * To filter objects, select the **Sort and filter** option and then specify the column and value you want to filter by.

  * To filter objects by object name prefix, select the **Filter by name prefix only** option and then specify the object name prefix you want to filter by.

  * To sort objects, click arrow_upward **Sort** next to the name of the column you want to sort by.




Filtering and sorting only applies to objects and folders in the current path being displayed. For example, if you're viewing the top-level of a bucket, filtering and sorting don't return objects contained in folders.

**Note:** Buckets with large numbers of objects and folders in the current path might experience degraded performance when sorted or filtered with criteria other than the object name prefix.

## Showing and hiding columns

To show or hide columns for a list of buckets or objects, click **View column** (view_column), then select the columns you want to see or hide.

## Cross-product integrations

The following integrations with other Google Cloud products are available in the **Objects** tab of a bucket:

  * **Large scale data transfers to and from the bucket using Storage Transfer Service**

[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer-service) is a service that lets you transfer large volumes of data between your bucket and other storage options, such as your on-premises file system, other buckets, or other cloud providers.

You can initiate a transfer by clicking the **Transfer data** drop-down in the **Objects** tab, selecting either **Transfer data in** or **Transfer data out** , and following the instructions.

  * **Scanning the bucket for sensitive data using Sensitive Data Protection**

[Sensitive Data Protection](https://docs.cloud.google.com/security/products/sensitive-data-protection) is a service that lets you identify and protect sensitive data in your buckets, such as credit card numbers, IP IP addresses, and other forms of personally identifiable information (PII).

For a list of the types of data Sensitive Data Protection detects, see the [Infotype detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

You can initiate a Sensitive Data Protection scan for a bucket by clicking the **Other services** drop-down in the **Objects** tab, selecting **Inspect for sensitive data** , and following the instructions. For a guide to performing a Sensitive Data Protection scan on a bucket, see [Inspecting a Cloud Storage location](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspecting-gcs).

  * **Exporting data from the bucket to Pub/Sub**

[Pub/Sub](https://docs.cloud.google.com/pubsub) is a messaging service that lets you notify subscribers about events that occur for your Google Cloud resources. Pub/Sub supports receiving event records that are stored as text files in your bucket and publishing them to a Pub/Sub topic.

You can create an export job for a bucket by clicking the **Other services** drop-down in the **Objects** tab, selecting **Export data to Pub/Sub** , and following the instructions. For more information, see [Cloud Storage text to Pub/Sub (Batch) template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-pubsub).

  * **Processing data in the bucket using Cloud Run functions**

[Cloud Run functions](https://docs.cloud.google.com/functions) is a service that lets you specify code that should run when certain events occur within the bucket. For example, you could create a Java function that runs every time an object in the bucket is deleted.

You can define a function for a bucket by clicking the **Other services** drop-down in the **Objects** tab, selecting **Process data** , and following the instructions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
