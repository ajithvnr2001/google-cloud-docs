---
url: https://docs.cloud.google.com/dataproc-metastore/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:57:25.304529+00:00
---

# Quotas and limits  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Resources ](https://docs.cloud.google.com/dataproc-metastore/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

The following sections explain quotas and limits for Dataproc Metastore. To change a quota, request additional quota by using the Google Cloud console. Limits generally cannot be increased unless specifically noted.

## Quotas and limits

### Dataproc Metastore services

Item | Quotas and limits | Notes  
---|---|---  
Services per region | 20 [services](https://docs.cloud.google.com/dataproc-metastore/docs/core-concepts) | When a project violates Google Cloud service policy, its per-region service quota is significantly lowered.  
  
### Metadata storage for Dataproc Metastore services

Item | Quotas and limits | Notes  
---|---|---  
Metadata storage per `Developer` tier service | 10 GB |   
Metadata storage per `Enterprise` tier service | 1 TB |   
  
### Queries per second for Dataproc Metastore projects

Item | Quotas and limits | Notes  
---|---|---  
Queries per second (QPS) per project | 20 QPS  
Queries per second (QPS) per project per user | 5 QPS  
Maintenance queries per second (QPS) per project | 20 QPS | The following Hive Metastore requests consume this quota: 
* `createTable`
* `createDatabase`
* `deleteTable`
* `deleteDatabase`  
  
### Job timeout limit for Dataproc Metastore

Item | Quotas and limits | Notes  
---|---|---  
Job timeout limit for export/backup/restore | 1 hour |   
Job timeout limit for import | 3 hours |   
  
## Quotas management

Dataproc Metastore enforces quotas on resource usage for a variety of reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial.

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas may increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles.

Task | Required role  
---|---  
Check quotas for a project | Project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) _or_ [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement)  
Modify quotas, request additional quota | Project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement), or custom role with the `serviceusage.quotas.update` permission   
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.




### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `HTTP 413 Request Entity Too Large`.

### Request additional quota

Request additional quota from the **Quotas** page in the Google Cloud console. Quota requests take 24 to 48 hours to process.

### Console

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. On the **Quotas** page, select the quotas that you want to change.

  3. At the top of the page, click edit**Edit quotas**.

  4. Fill out your name, email, and phone number, and then click **Next**.

  5. Fill in your quota request, and then click **Done**.

  6. Submit your request.




### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, provided that resource is available. It's important to note that quotas _do not_ guarantee resource availability. Even if you have available quota, you won't be able to create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in the `us-central1` region, but that would not be possible if there were no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare; however, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

## What's next

  * Learn more about [Dataproc Metastore resources](https://docs.cloud.google.com/dataproc-metastore/docs/resources).
  * Learn about [Dataproc Metastore pricing](https://cloud.google.com/dataproc-metastore/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
