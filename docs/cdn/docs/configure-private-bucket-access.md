---
url: https://docs.cloud.google.com/cdn/docs/configure-private-bucket-access/
title: Configure private bucket access \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:28.590883+00:00
---

# Configure private bucket access  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/configure-private-bucket-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Configure private bucket access Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of private bucket access and instructions for using it for Cloud Storage buckets with Cloud CDN.

## For Cloud Storage buckets

Implementing private bucket access for your Cloud CDN backend bucket lets content in your storage buckets be accessed _only_ through Cloud CDN and not directly by using the Cloud Storage XML API path-style endpoint or bucket-bound hostname.

To prevent direct access to your private Cloud Storage buckets, Cloud Storage uses [Identity and Access Management permissions](https://docs.cloud.google.com/iam/docs), which helps limit the access to Cloud CDN or Cloud Load Balancing traffic _only_ without having to enable [signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) or [signed cookies](https://docs.cloud.google.com/cdn/docs/using-signed-cookies) for this route.

To configure private bucket access for Cloud Storage, use the following instructions:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#create_a_bucket)

  2. [Move content into the bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#copy_file)

  3. [Create an external Application Load Balancer that connects your private Cloud Storage bucket to the backend bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#create-the).

  4. [Enable access for your service account](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#enable_private_bucket_access)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
