---
url: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-sql-overprovisioned/
title: Reduce overprovisioned Cloud SQL instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:17.603634+00:00
---

# Reduce overprovisioned Cloud SQL instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-sql-overprovisioned/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Reduce overprovisioned Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-overprovisioned "View this page for the PostgreSQL database engine") | SQL Server

The Cloud SQL overprovisioned instance [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances that are unnecessarily large for a given workload. It then provides recommendations on how to resize such instances and reduce cost. This page describes how this recommender works and how to use it.

## How it works

The Cloud SQL overprovisioned recommender analyzes the usage metrics of primary instances that are older than 30 days. For each instance, the recommender considers the CPU and memory utilization based on the values of certain [metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql) within the last 30 days. The recommender does not analyze read replicas or instances configured for high availability (HA).

If the peak utilization of either or both the CPU and the memory within the observation period is low, the instance is estimated to be overprovisioned. Recommendations are generated every 24 hours for rightsizing such instances when the estimated monthly cost savings are greater than or equal to $10.

The recommender uses conservative thresholds to ensure that it flags only instances that are significantly overprovisioned, which is usually a good indicator of waste. The recommender suggests a machine type that has at least 8 vCPUs and 32 GB.

**Warning:** It's highly recommended that you evaluate the insights and in-context charts. Consult with the appropriate team to determine whether the flagged instance is inadvertently overprovisioned and a smaller instance might meet the needs of your application.

## Pricing

The Cloud SQL overprovisioned instance recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/sqlserver/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List overprovisioned Cloud SQL instance recommendations

You can list overprovisioned instance recommendations by using the Google Cloud console, `gcloud`, or the Recommender API.

###  Console 

To list recommendations about overprovisioned instances by using the Google Cloud console, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click **View all** on the overprovisioned instance recommendations banner.




Alternatively, follow these steps:

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Reduce Cloud SQL instance cost** card, click **View all**.

  3. Click the **Reduce instance** tab.




###  gcloud 

To list recommendations about overprovisioned instances by using `gcloud`, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.RECOMMENDER
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `RECOMMENDER`: The ID of the recommender as `OverprovisionedRecommender`.



###  API 

To list recommendations about overprovisioned instances by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.RECOMMENDER/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `RECOMMENDER`: The ID of the recommender as `OverprovisionedRecommender`.



If the recommender detects overprovisioned instances, it lists them in a table. Each row shows the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about overprovisioned instances by using the Google Cloud console, `gcloud`, or the Recommender API.

###  Console 

To view insights and detailed recommendations about an overprovisioned instance by using the Google Cloud console, click the recommendation button in the list of instances.

###  gcloud 

To view insights and detailed recommendations about overprovisioned instances by using `gcloud`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.INSIGHT_TYPE
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `CpuUsageInsight` or `MemoryUsageInsight`, which provide insights about CPU usage and memory, respectively.



###  API 

To view insights and detailed recommendations about overprovisioned instances by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.INSIGHT_TYPE/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `CpuUsageInsight`. or `MemoryUsageInsight`, which provide insights about CPU usage and memory, respectively.



A panel appears showing insights about the current memory and CPU utilization of the instance. The following categories of information are provided along with some supporting charts.

Fields | Descriptions and related metrics  
---|---  
**Max CPU utilization** | The maximum CPU utilization as a percentage.   
Pertains to `database/cpu/utilization`.  
**Max memory utilization** | The maximum memory utilization as a percentage.   
Pertains to `database/memory/utilization`.  
  
The following table lists the insights and recommendations that the Cloud SQL overprovisioned instance recommender might generate to help you reduce costs. The subtypes are visible in the `gcloud` and API results.

Insights | Recommendations  
---|---  
Based on the current CPU utilization trends, the instance is flagged as overprovisioned.   
Subtype: `LOW_CPU_UTILIZATION` | Reduce the number of vCPUs or switch to a machine with fewer vCPUs.  
Subtype: `CHANGE_INSTANCE_SIZE`  
Based on the current memory utilization trends, the instance is flagged as overprovisioned.  
Subtype: `LOW_MEMORY_UTILIZATION`. | Reduce the memory requirement or switch to a machine with less memory.  
Subtype: `CHANGE_INSTANCE_SIZE`  
  
## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

  * To examine the recommendation, click **View instance**.

A banner appears at the top of the page providing a recommendation.

[Edit](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance) the instance, if required, to reduce the vCPUs or memory. Alternatively, switch to a machine type with fewer vCPUs and less memory. You don't need to rightsize the instance exactly as recommended. Use your judgement about instance size based on how you intend to provision the instance. Keep in mind that the bigger the size, the greater the operational latency.

  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




You can also [export these recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq) and then examine them using [Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio) or [Looker](https://docs.cloud.google.com/bigquery/docs/looker).

## What's next

  * [Monitor disk availability](https://docs.cloud.google.com/sql/docs/sqlserver/using-ood-recommender)
  * [Reduce idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-sql-idle)
  * [Blog: Maximize your Cloud ROI](https://cloud.google.com/blog/products/management-tools/active-assist-comes-to-google-cloud)
  * [Blog: Do more with less](https://cloud.google.com/blog/products/databases/reduce-cloud-sql-costs-with-optimizations-by-active-assist)
  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
