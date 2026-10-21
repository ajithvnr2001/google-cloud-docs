---
url: https://docs.cloud.google.com/storage/docs/list-ip-filter/
title: List bucket IP filtering rules \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.414161+00:00
---

# List bucket IP filtering rules  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/list-ip-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  List bucket IP filtering rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to list the [bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) rules. With the list bucket IP filtering rules operation, you can check if IP filtering is enabled or disabled on a bucket. If you need to view information about the specific network sources that are allowed, use the [Get bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/get-ip-filter) operation.

## Required roles

To get the required permissions for listing the bucket IP filtering rules, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the `storage.buckets.list` permission required to list bucket IP filtering rules.

You can also get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). You might be able to get this permission with other predefined roles as well. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions on granting roles for projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## List bucket IP filtering rules

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Permissions** section, navigate to **IP filtering**. Then, click edit **Edit IP filtering configuration**.

The **IP filtering** page displays the following details:

     * IP filtering status of the bucket.
     * Whether service agents are configured to bypass the IP filter validation.
     * Whether access from cross-organization VPC networks is allowed.
     * All configured IP filtering rules.



### gcloud

  1. Verify that you have the Google Cloud CLI version 526.0.0 or later installed:
         
         gcloud version | head -n1
         

  2. If you have an earlier gcloud CLI version installed, update the version:
         
         gcloud components update --version=526.0.0
         

  3. To list the bucket IP filtering rules, run the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command in your development environment:
         
         gcloud storage buckets describe gs://BUCKET_NAME --format="default(ip_filter_config)"

Where:

`BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`List` bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b?project=PROJECT_ID"

Where:

`PROJECT_ID` is the ID of the project containing the buckets you want to list. For example, `my-project`.

The response looks like the following example:
         
         {
           "kind": "storage#buckets",
           "items":
                 {
                 "kind": "storage#bucket",
                 "selfLink": "https://www.googleapis.com/storage/v1/b/my-bucket1",
                 "id": "my-bucket1",
                 "name": "my-bucket1",
                 "projectNumber": "123456789012",
                 ...
                   },
                 "ipFilter": {
                   "mode": "Disabled"
                  }
                 {
                 "kind": "storage#bucket",
                 "selfLink": "https://www.googleapis.com/storage/v1/b/my-bucket2",
                 "id": "my-bucket2",
                 "name": "my-bucket2",
                 "projectNumber": "123456789013",
                 ...
                 },
                 "ipFilter": {
                   "mode": "Enabled"
                 }
         },




## What's next

  * [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter).
  * [Get bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/get-ip-filter).
  * [Disable bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
