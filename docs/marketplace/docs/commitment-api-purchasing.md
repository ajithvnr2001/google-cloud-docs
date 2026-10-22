---
url: https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing/
title: Use the API to purchase a spend-based commitment \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:50.764770+00:00
---

# Use the API to purchase a spend-based commitment  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/commitment-api-purchasing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Use the API to purchase a spend-based commitment Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to purchase a spend-based commitment by using the Cloud Commerce Consumer Procurement API for Cloud Marketplace purchases. 

This API only supports purchasing spend-based commitments, not resource-based commitments.

## Before you begin

  * Enable the [Cloud Commerce Consumer Procurement API](https://console.cloud.google.com/apis/api/cloudcommerceconsumerprocurement.googleapis.com) for your Google Cloud project.

  * Ensure that you have one of the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles for the Cloud Billing account you want to use to purchase the commitment:

    * [Billing Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) (`roles/billing.admin`) for the target Cloud Billing account _OR_ the Google Cloud organization where your billing account is located.

    * [Consumer Procurement Order Administrator](https://docs.cloud.google.com/marketplace/docs/access-control#roles-permissions) (`roles/consumerprocurement.orderAdmin`) for the target Cloud Billing account _OR_ the Google Cloud organization where your billing account is located.




## Identify the Offer you want to purchase

To purchase a spend-based commitment, use an Offer name which indicates the product you're purchasing and the discount term, you must use the Offer name that matches your Cloud Billing account's model.

**Note** : This document discusses some spend-based committed use discounts (CUDs) that automatically migrate to a new consumption model, which leverages discounts rather than credits. The migration date is indicated by a notification in the Google Cloud console Billing Overview page. For more information about the improvements, the affected CUDs, and any required actions on your part, see [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds-multiprice). 

The following Offers are available for purchase, and follow the [new consumption model (direct discount, no credits)](https://docs.cloud.google.com/docs/cuds-multiprice) :

Product | Term | Scope | Offer name | Required parameters  
---|---|---|---|---  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/cud) | 1 year | Global | services/alloydb.googleapis.com/standardOffers/ff04ec3e-278c-4ec8-8278-12f875a8cea2 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/cud) | 3 years | Global | services/alloydb.googleapis.com/standardOffers/9522b4d8-bff7-4141-81d6-b71d9113c69a | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Backup and DR (Oracle)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) | 1 year | Global | services/backupdr.googleapis.com/standardOffers/16e6132e-8a72-4a7f-8941-bf52246afc82 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Backup and DR (Oracle)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) | 3 years | Global | services/backupdr.googleapis.com/standardOffers/1e028b05-4344-4bca-87e7-235ee3536354 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[BigQuery](https://docs.cloud.google.com/bigquery/docs/bigquery-cud) | 1 year | Regional | services/bigqueryreservation.googleapis.com/standardOffers/d73ae4d8-d096-4c9b-9c20-cd92c3c53724 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[BigQuery](https://docs.cloud.google.com/bigquery/docs/bigquery-cud) | 3 years | Regional | services/bigqueryreservation.googleapis.com/standardOffers/f43d480d-3e77-4079-946c-e1b2ab640a8a | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Bigtable](https://docs.cloud.google.com/bigtable/docs/cuds) | 1 year | Global | services/bigtable.googleapis.com/standardOffers/c0bf8ba5-65ee-4f7d-9e1e-3953433cf193 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Bigtable](https://docs.cloud.google.com/bigtable/docs/cuds) | 3 years | Global | services/bigtable.googleapis.com/standardOffers/460fb2ef-456d-4263-a070-4f993fa37996 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Cloud Run](https://docs.cloud.google.com/run/cud) | 3 years | Regional | services/run.googleapis.com/standardOffers/88a5fc51-d63b-4865-bf3b-c49e05a8c5c0 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Cloud Run](https://docs.cloud.google.com/run/cud) | year | Regional | services/run.googleapis.com/standardOffers/392802d4-e57b-40d3-9684-a1e8cdca6fb5 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Cloud SQL](https://docs.cloud.google.com/sql/cud) | 1 year | Regional | services/cloudsql.googleapis.com/standardOffers/d31cf078-36a2-4a8a-a2e6-b23caec0e7a3 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Cloud SQL](https://docs.cloud.google.com/sql/cud) | 3 years | Regional | services/cloudsql.googleapis.com/standardOffers/48960309-1646-4fa2-9bf8-d7e72090d2b8 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Compute Engine flexible commitment](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#applicable_discounts) | 1 year | Global | services/compute.googleapis.com/standardOffers/1b2601a4-9d76-462d-bd5b-5b835d245f93 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Compute Engine flexible commitment](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#applicable_discounts) | 3 years | Global | services/compute.googleapis.com/standardOffers/61612674-a9a9-4687-8449-baca71fbd0d1 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/cuds) | 1 year | Global | services/dataflow.googleapis.com/standardOffers/127d79e4-1d52-48b0-9f31-8ba02586ff95 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/cuds) | 3 years | Global | services/dataflow.googleapis.com/standardOffers/03f4d3b1-44b8-4e88-9e75-b1d4e2d04573 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Firestore](https://docs.cloud.google.com/firestore/docs/cuds) | 1 year | Global | services/firestore.googleapis.com/standardOffers/de6aa077-3170-4250-89b6-0ccd470f9e21 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Firestore](https://docs.cloud.google.com/firestore/docs/cuds) | 3 years | Global | services/firestore.googleapis.com/standardOffers/e8f59240-c088-4a22-87c3-e58722cca300 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Gemini Enterprise Flexible Savings Plan](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans#genai_fsp) | 1 year | Global | services/aiplatform.googleapis.com/standardOffers/740fd2e8-ff1d-4304-9e85-61c0f8d75811 | `commitment_amount`  
[Gemini Enterprise Flexible Savings Plan](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans#genai_fsp) | 3 years | Global | services/aiplatform.googleapis.com/standardOffers/4733352d-24b5-4609-b3ff-d2a694f51654 | `commitment_amount`  
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/cud) | 1 year | Regional | services/container.googleapis.com/standardOffers/2f48e468-a86a-452d-88df-edacd94a3c44 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/cud) | 3 years | Regional | services/container.googleapis.com/standardOffers/89027902-6f83-40aa-8861-7c2446b11015 | `commitment_amount` (recommended)  
_or_ `hourly_commit, `  
  
`region`  
[Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds) | 1 year | Global | services/managedkafka.googleapis.com/standardOffers/647db981-009c-4e95-b62e-6aff19384956 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/cuds) | 3 years | Global | services/managedkafka.googleapis.com/standardOffers/9a7ed994-d3df-4680-b4e6-7c3d932add66 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/cuds) | 1 year | Global | services/redis.googleapis.com/standardOffers/8e0da7cb-196b-4351-bc32-6a6ba94f1456 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/cuds) | 3 years | Global | services/redis.googleapis.com/standardOffers/2a3729ac-1e38-4a34-bc96-bd988028351f | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Spanner](https://docs.cloud.google.com/spanner/docs/cuds) | 1 year | Global | services/spanner.googleapis.com/standardOffers/359db5c2-8c2c-49e3-a21d-26176c4cd403 | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
[Spanner](https://docs.cloud.google.com/spanner/docs/cuds) | 3 years | Global | services/spanner.googleapis.com/standardOffers/a6a32e10-1d76-4df8-8485-eee10d08a1cf | `commitment_amount` (recommended)  
_or_ `hourly_commit`  
  
The following Offers are available for purchase, and follow the [legacy credit model (list price charge + credit offset)](https://docs.cloud.google.com/docs/cuds-multiprice) :

Product | Term | Scope | Offer name | Required parameters  
---|---|---|---|---  
[Backup and DR (VMWare)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) | 1 year | Regional | services/backupdr.googleapis.com/standardOffers/30c7e770-724f-4a7d-8369-b726a397b53a | `hourly_commit, `  
  
`region`  
[Backup and DR (VMWare)](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/cud) | 3 years | Regional | services/backupdr.googleapis.com/standardOffers/6748e93c-4114-4fa2-bf3e-cb4d3534bb48 | `hourly_commit, `  
  
`region`  
[NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/cuds) | 1 year | Global | services/netapp.googleapis.com/standardOffers/90520cfa-14b6-42ae-92b9-129671bf2aca | `hourly_commit`  
[NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/cuds) | 3 years | Global | services/netapp.googleapis.com/standardOffers/c852fef8-e699-4524-90f4-e7b89edeb33c | `hourly_commit`  
  
## Identify the Offer parameters

Here are the parameters you should set to purchase the offer:

  * **Commitment_amount (recommended) or Hourly_commit** :

    * **For commitments on the new spend-based CUD model** : `commitment_amount` (recommended) or `hourly_commit`. The `hourly_commit` parameter will be deprecated eventually and replaced by the generic `commitment_amount` parameter in the future for commitments on the new model. Some CUDs support a different recurrence (hourly, monthly, etc.), and will only support the `commitment_amount` parameter, check the "Required parameters" column in the Offer tables for specific requirements.

    * **For offers that are unaffected by the new CUD model** : Specify `hourly_commit`. This represents the credit applied to your Cloud Billing account each hour. Legacy CUDs don't support `commitment_amount`.

  * **Region** (`region`): The region for which this commitment's benefits apply.

    * **For regional commitments** : Specify the target region (for example, `us-central1`). To find folders and supported regions for each product, refer to that product's documentation or the [Committed use discounts overview](https://docs.cloud.google.com/docs/cuds).
    * **For global commitments** : Omit this parameter, as global commitments apply across all regions.



## Purchase the Offer

To purchase an Offer, call [`billingAccounts.orders.place`](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/place), and supply the following parameters in the request body:

  * The commitment value parameter matching your CUD type:

    * For commitments on the new spend-based CUD model: Supply `commitment_amount` (recommended) or `hourly_commit` (deprecated, to be removed in the future). For new CUD offers (such as AI Platform), you must specify `commitment_amount`.
    * For legacy CUDs: Supply `hourly_commit`.
  * The `region` (only for regional commitments). If you are purchasing a global commitment, omit the `region` parameter.




To place an order, run the following command:
    
    
    curl 'https://cloudcommerceconsumerprocurement.googleapis.com/v1alpha1/billingAccounts/BILLING_ACCOUNT_ID/orders:place' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer ACCESS_TOKEN' \
        --header 'X-Goog-User-Project: CONSUMER_PROJECT_ID' \
        -d '@-' <<EOF
        {
        "displayName": "DISPLAY_NAME",
        "lineItemInfo": [{
            "parameters": [{
            "name": "commitment_amount",
            "value": {
                "doubleValue": COMMITMENT_AMOUNT
            }
            }, {
            "name": "region",
            "value": {
                "stringValue": "REGION"
            }
            }],
            "offer": "OFFER_NAME"
        }]
        }
    EOF

This returns the name of a long-running operation:
    
    
    {
        "name": "OPERATION_NAME"
    }
    

To verify that the returned long-running operation completed successfully, run the following command:
    
    
    curl 'https://cloudcommerceconsumerprocurement.googleapis.com/v1alpha1/OPERATION_NAME' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer ACCESS_TOKEN' \
        --header 'X-Goog-User-Project: CONSUMER_PROJECT_ID'

The long-running operation should complete in less than one second.

## View your Order

You can view the current state of a commitment directly in Google Cloud console, or by calling [`billingAccounts.orders.get`](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1alpha1/billingAccounts.orders/get). The `name` field of the created Order specifies the Order name.

### cURL

To view an order, run the following command:
    
    
    curl 'https://cloudcommerceconsumerprocurement.googleapis.com/v1alpha1/ORDER_NAME' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer ACCESS_TOKEN' \
        --header 'X-Goog-User-Project: CONSUMER_PROJECT_ID'

### Console

  1. In the Google Cloud console, go to your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing)

  2. Select **Committed use discounts (CUDs)** from the sidebar.

  3. Your purchased commitments are displayed.




## Related topics

  * [Spend-based CUD program improvements](https://docs.cloud.google.com/docs/cuds-multiprice)
  * [Spend-based CUD data model changes](https://docs.cloud.google.com/docs/cuds-multiprice-datamodel)
  * [Timelines for new CUD model migration](https://docs.cloud.google.com/docs/cuds-new-model-timeline)
  * [Verify your discounts after migration](https://docs.cloud.google.com/docs/cuds-verify-discounts)
  * [Choose the correct amount of CUD to buy](https://docs.cloud.google.com/docs/cuds-choose-correctly)
  * [Sample queries for the new CUDs data model](https://docs.cloud.google.com/docs/cuds-example-queries)
  * [Migrated CUD SKUs, offers, and consumption model IDs](https://docs.cloud.google.com/docs/cuds-migration)
  * [Billing user interface improvements](https://docs.cloud.google.com/docs/cuds-billing-ui-improvements)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
