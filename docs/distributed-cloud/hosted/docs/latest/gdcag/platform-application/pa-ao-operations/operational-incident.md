---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-incident/
title: Respond to storage operational incidents \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:18.979617+00:00
---

# Respond to storage operational incidents  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-incident/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Respond to storage operational incidents Stay organized with collections  Save and categorize content based on your preferences. 

## Tenant metrics

As a Platform Administrator (PA), view tenant metrics to help diagnose operational incidents.

### Tenant capacity usage

To view current capacity usage of an organization by storage class in the monitoring dashboard, go to the **Explore** option. You can execute the following query to view the capacity percentage used by that organization and storage class.
    
    
    sum by (TENANT_TYPE, SKU_NAME) (OBJECT_TENANT_USED_CAPACITY_BYTES_COUNT) / sum by (TENANT_TYPE, SKU_NAME) (OBJECT_TENANT_QUOTA_BYTES)
    

### Object Storage Platform dashboard

The **Object Storage Platform** dashboard shows a view of each object storage class in the organization with the respective usage, quota, and capacity remaining.

![High-level storage class usage breakdown](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/object_storage_tenant_usage.png)

You can also view more granular usage stats about each storage class down to the bucket level.

![Bucket usage in storage class](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform-application/images/object_storage_bucket_usage.png)

### Organization utilization alert

If you have received an alert with code `OBJ-A0011`, complete the following steps:

  1. View the **Object Storage Platform** dashboard and determine the storage tier that causes the alert.
  2. Depending on the value, choose the recommended course of action:

     * If the remaining capacity is near 25% but usage is stable and not increasing, choose to ignore the alert at the current time.
     * If usage is increasing and you are concerned about usage surpassing the set quota threshold, determine if there are any buckets or objects that are not vital and delete them.
     * If you do not want to delete any objects from object storage, or you are concerned with the available capacity, increase the allocated capacity for the specific storage class. To increase the quota, you must reach out to the Infrastructure Operator (IO) with a request to raise the specific storage class's quota.
**Note:** Failure to increase quota prior to available capacity running out results in failures to add or modify objects in object storage for the specific storage class. You cannot add or modify objects until capacity is available.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
