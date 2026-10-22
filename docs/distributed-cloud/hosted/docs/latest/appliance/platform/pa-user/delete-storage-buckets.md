---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/delete-storage-buckets/
title: Delete storage buckets \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:00.754083+00:00
---

# Delete storage buckets  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/delete-storage-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Delete storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to delete storage buckets within Google Distributed Cloud (GDC) air-gapped appliance environments. It covers prerequisites and methods for deleting buckets through the GDC console and command line interface (CLI). Learn how to delete buckets with retention policies by crypto shredding—a process where you delete the encryption key associated with the storage bucket. This information lets you securely and permanently manage the lifecycle of your object storage, providing data hygiene and compliance

This page is for audiences such as IT admins within the infrastructure operator group or developers within the application operator group who are responsible for managing object storage resources in GDC air-gapped environments.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

You can delete storage buckets by using the kubectl CLI. **Buckets must be empty before you can delete them.**

  1. Use the [`GET` or `DESCRIBE` command](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/list-view-storage-buckets#view_bucket_configuration) to get the fully qualified bucket name.

  2. If the bucket is not empty, empty the bucket:
         
         gdcloud storage rm --recursive s3://FULLY_QUALIFIED_BUCKET_NAME
         

  3. Delete the empty bucket:
         
         kubectl delete buckets/BUCKET_NAME --namespace NAMESPACE_NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
