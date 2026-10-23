---
url: https://docs.cloud.google.com/sql/docs/postgres/recommender-high-transactionid-utilization/
title: Prevent transaction ID wraparound \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:25.377100+00:00
---

# Prevent transaction ID wraparound  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/recommender-high-transactionid-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Prevent transaction ID wraparound Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

The Cloud SQL high-transaction-ID-utilization [recommender](https://docs.cloud.google.com/recommender/docs/overview) proactively generates recommendations that help you avoid potential transaction ID wraparound for Cloud SQL for PostgreSQL instances. The Cloud SQL high-transaction-ID-utilization recommender is supported only for Cloud SQL Enterprise Plus edition instances.

You can apply this recommendation when a Cloud SQL instance is trending toward a transaction ID wraparound problem. This page describes how the Cloud SQL high-transaction-ID-utilization recommender works and how you can use it.

## How it works

A transaction ID is assigned when the transaction starts, and it's frozen until the transaction is vacuumed. Transaction ID utilization is the number of unvacuumed transactions (assigned minus frozen) expressed as a fraction of the maximum value of 2 billion. Under the default PostgreSQL settings, with vacuum processes performing optimally and without interruption, most databases experience transaction ID utilization in the region of approximately 10%. Higher transaction ID utilization levels can be observed in busy databases where regular workloads frequently take precedence over vacuum. If the transaction ID utilization trends towards very high values (80% or more), the database might be at risk of transaction ID exhaustion. Transaction ID utilization reaching 100% is termed as transaction ID wraparound. Once the transaction ID utilization percentage reaches 100%, PostgreSQL stops accepting write queries.

The Cloud SQL high-transaction-ID-utilization recommender analyzes transaction ID utilization on a Cloud SQL for PostgreSQL instance.

If the transaction ID utilization percentage is more than or equal to 80%, it's recommended to take actions to avoid transaction ID wraparound.

**Note:** Recommendations are generated daily.

## Pricing

The Cloud SQL high-transaction-ID-utilization recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/postgres/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List Improve Instance Performance recommendations

You can list the Improve Instance Performance recommendations by using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

The improve instance performance recommendations are shown only if you have instances that are nearing a transaction ID wraparound.

###  Console 

To list recommendations about instance performance using the Google Cloud console, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click **View all** on the Prevent transaction ID wraparound recommendations banner.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **Improve Cloud SQL Instance Performance** card, click **View all**.

  3. Select the instances with **Prevent transaction ID wraparound** recommendation.




###  gcloud CLI 

To list Improve Instance Performance recommendations by using `gcloud CLI`, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE
    

Replace the following:

  * `PROJECT_ID`: Your project ID
  * `LOCATION`: A region, such as `us-central1`



###  API 

To list Improve Instance Performance recommendations by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender.PostgresHighTransactionIdUtilizationBestPractice/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



If the recommender detects instances with high transaction ID utilization, it lists them in a table with other performance recommendations. Each row shows the instance ID, a brief recommendation, database engine, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that are trending toward a transaction ID wraparound using the Google Cloud console, `gcloud CLI`, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that are close to the performance threshold by using the Google Cloud console, click the recommendation link in the list of instances.

###  gcloud CLI 

To view insights and detailed recommendations about instances that are close to the performance threshold by using `gcloud CLI`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that are close to the performance threshold by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceRecommender.PostgresHighTransactionIdUtilization/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



The following table lists the insight and recommendation that the Cloud SQL high-transaction-ID-utilization recommender generates. The subtypes are visible in the `gcloud CLI` and API results.

Insight | Recommendation  
---|---  
Transaction ID utilization percentage on this instance is high and close to 100%.   
Subtype: `POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION` |  Avoid potential transaction ID wraparound for Cloud SQL instances.  
Subtype: `POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE`  
  
## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

  * To examine the recommendation, click **View instance**. See Optimize the performance of your instance or Prevent transaction ID wraparound and follow the recommendations.

  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




### Optimize the performance of your instance

To address the transaction ID wraparound problem with the instance, do the following:

  1. [Find the database and table causing the wraparound.](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#find_the_database_and_table_causing_the_wraparound)

  2. [Explore and interpret transaction ID utilization metrics on your database instances.](https://cloud.google.com/blog/products/databases/monitor-transaction-id-utilization-in-cloud-sql-postgresql)

  3. [Check for a stuck transaction ID.](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#check_for_a_stuck_transaction_id)

  4. [Remove VACUUM blockers.](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#how-to-remove)

  5. [Check and accelerate VACUUM speed.](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#tuning-vacuum-detailed)




For additional information, also see the blog post [Using VACUUM to accelerate transaction ID freezing in Cloud SQL for PostgreSQL](https://cloud.google.com/blog/products/databases/how-to-accelerate-transaction-id-freezing-in-cloud-sql-for-postgresql).

### Prevent transaction ID wraparound

To prevent transaction ID wraparound for an instance, run the following command:
    
    
    SELECT * FROM google_vacuum_mgmt.pg_fix_wraparound();

Example output:
    
    
    postgres=> select * from google_vacuum_mgmt.pg_fix_wraparound();
    -[ RECORD 1 ]-----+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    issue_description | Cloud SQL for PostgreSQL has detected an open prepared transaction on your instance which is blocking VACUUM. Monitor the transaction ID utilization and commit or rollback the transaction, as needed.
    query             | ROLLBACK PREPARED 'trx_id_pin'; or COMMIT PREPARED 'trx_id_pin';
    recommendation    | To commit a prepared transaction, you must be connected as the same user that originally executed the transaction: postgres
    insights          | Transaction ID Utilization: 88.49%
    

## What's next

  * [Monitor disk availability](https://docs.cloud.google.com/sql/docs/postgres/using-ood-recommender)
  * [Identify idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-idle)
  * [Reduce overprovisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-overprovisioned)
  * Explore [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
