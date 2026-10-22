---
url: https://docs.cloud.google.com/deployment-manager/quotas/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:03.144821+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/quotas/




Stay organized with collections  Save and categorize content based on your preferences. 

Quotas and Limits

Cloud Deployment Manager does not charge for use, but any resources you deploy using Deployment Manager may incur charges. For example, Compute Engine charges for resources per the [Compute Engine price sheet](https://cloud.google.com/compute/pricing). For more information, see the price sheets for the respective products.

## Quotas

### Deployment Manager

Deployment Manager enforces the following API limits and quotas:

  * **Unlimited read requests** , which include any requests made through `gcloud` or [Google Cloud console](https://console.cloud.google.com/). Requests such as `get` and `list` would be considered read requests.
  * **Unlimited delete requests** to delete deployments.
  * **1,000 API write requests per day** , including requests made through `gcloud`. This includes requests to change or create deployments and resources, such as `insert` and `update`.
  * **20 API requests per second**.
  * **1,000 active deployments per project**. If you want to create additional deployments, you must first [delete some deployments](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments).
  * **1 MB limit on user-provided configurations** , including the YAML configuration and any imports.
  * **1 MB limit on expanded configurations**. When fully-expanded, your configuration cannot exceed this size.
  * **10000 total resources per operation**. When you make a change to a deployment, the total number of resources in the new configuration plus the number of resources from the previous configuration that you are deleting can't exceed this limit.
  * **256 type providers per project**.
  * **256 composite types per project**.



In addition, you are subject to quotas enforced by any other Google Cloud services you use. For example, Deployment Manager can't deploy more Compute Engine virtual machines than the available quota for your project. For more information, refer to the quota information for the specific Google Cloud Platform services.

### Cloud Runtime Configuration API

Cloud Runtime Configuration API enforces the following API limits and quotas:

  * **1200 Queries Per Minute (QPM)** for `delete`, `create`, and `update` requests.
  * **600 QPM** for `watch` requests.
  * **6000 QPM** for `get` and `list` requests.
  * **4MB of data per project** , which consists of all data written to the Cloud Runtime Configuration API service and accompanying metadata.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
