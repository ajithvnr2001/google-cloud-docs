---
url: https://docs.cloud.google.com/storage/docs/get-ip-filter/
title: Get IP filtering rules \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:42.629747+00:00
---

# Get IP filtering rules  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/get-ip-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Get IP filtering rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get the IP filtering rules on a bucket. For information about bucket IP filtering, see [Bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

## Required roles

To get the required permissions for getting the IP filtering rules on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the permissions required to get bucket IP filtering rules.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.getIpFilter`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). You might be able to get these permissions with other predefined roles as well. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions on granting roles for projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Get bucket IP filtering rules

### Console

To view IP filtering rules in the Google Cloud console, follow the instructions in [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter#console). The Google Cloud console displays all configured IP ranges and settings on a single page.

### gcloud

  1. To get the IP filtering rules on a bucket, run the command [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) in your development environment:
         
         gcloud storage buckets describe gs://BUCKET_NAME --format="default(ip_filter_config)"

Where:

`BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Where:

`BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.




## What's next

  * [Create or update IP filtering rules on an existing bucket](https://docs.cloud.google.com/storage/docs/update-ip-filter).
  * [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter).
  * [Disable bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
