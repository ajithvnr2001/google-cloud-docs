---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/list-storage-objects/
title: List storage objects \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:42.810332+00:00
---

# List storage objects  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/list-storage-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  List storage objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to list objects within Google Distributed Cloud (GDC) air-gapped appliance storage buckets.

## Before you begin

A project namespace manages bucket resources in the management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

You must also have the appropriate bucket permissions to perform the following operation. See [Grant bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access#grant_bucket_access).

To run commands against the management API server, [sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) the kubeconfig file for the management API server if you don't have one.

## List objects in storage buckets

List the objects in the top level directory of a bucket:
    
    
    gdcloud storage ls s3://FULLY_QUALIFIED_BUCKET_NAME
    

List all versions of objects in the top level directory of a bucket:
    
    
    gdcloud storage ls --all-versions s3://FULLY_QUALIFIED_BUCKET_NAME
    

List the objects in a bucket with a prefix:
    
    
    gdcloud storage ls s3://FULLY_QUALIFIED_BUCKET_NAME/<Prefix>/
    

List all versions of objects in a bucket with a prefix:
    
    
    gdcloud storage ls --all-versions s3://FULLY_QUALIFIED_BUCKET_NAME/<Prefix>/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
