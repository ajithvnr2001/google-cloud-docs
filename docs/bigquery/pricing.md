---
url: https://docs.cloud.google.com/bigquery/pricing/
title: BigQuery | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:01.144571+00:00
---

# BigQuery | Google Cloud

> Source: https://docs.cloud.google.com/bigquery/pricing/

Page Contents




## 

BigQuery pricing

BigQuery is a serverless data analytics platform. You don't need to provision individual instances or virtual machines to use BigQuery. Instead, BigQuery automatically allocates computing resources as you need them. You can also reserve compute capacity ahead of time in the form of slots, which represent virtual CPUs. The pricing structure of BigQuery reflects this design.

### 

Overview of BigQuery pricing

BigQuery pricing has two main components:

  * [Compute pricing](https://docs.cloud.google.com/bigquery/pricing#compute-pricing-models) is the cost to process queries, including SQL queries, user-defined functions, scripts, and certain data manipulation language (DML) and data definition language (DDL) statements.
  * [Storage pricing](https://docs.cloud.google.com/bigquery/pricing#storage-pricing) is the cost to store data that you load into BigQuery.



BigQuery charges for other operations, including using [BigQuery Omni](https://docs.cloud.google.com/bigquery/pricing#bigquery-omni-pricing), [BigQuery ML](https://docs.cloud.google.com/bigquery/pricing#bigquery-ml-pricing), [BI Engine](https://docs.cloud.google.com/bigquery/pricing#bi-engine-pricing), and streaming [reads](https://docs.cloud.google.com/bigquery/pricing#data-extraction-pricing) and [writes](https://docs.cloud.google.com/bigquery/pricing#data-ingestion-pricing).

In addition, BigQuery has [free operations](https://docs.cloud.google.com/bigquery/pricing#free-operations) and a [free usage tier](https://docs.cloud.google.com/bigquery/pricing#free-usage-tier).

Every project that you create has a billing account attached to it. Any charges incurred by BigQuery jobs run in the project are billed to the attached billing account. BigQuery storage charges are also billed to the attached billing account. You can view BigQuery costs and trends by using the Cloud Billing reports page in the Google Cloud console.

**Key Point:** Pricing models apply to accounts, not individual projects, unless otherwise specified.

### 

Compute pricing models

BigQuery offers a choice of two compute pricing models for running queries:

  * [On-demand pricing](https://docs.cloud.google.com/bigquery/pricing#on-demand-compute-pricing) (per TiB). With this pricing model, you are charged for the number of bytes processed by each query. The first 1 TiB of query data processed per month is free.
  * [Capacity pricing ](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing)(per slot-hour). With this pricing model, you are charged for compute capacity used to run queries, measured in slots (virtual CPUs) over time. This model takes advantage of [BigQuery editions](https://cloud.google.com/bigquery/docs/editions-intro). You can use the BigQuery autoscaler or purchase slot commitments, which are dedicated capacity that is always available for your workloads, at a lower price.



For more information about which pricing to choose for your workloads, see [Workload management using Reservations](https://cloud.google.com/bigquery/docs/reservations-workload-management).

### 

Gemini in BigQuery pricing

See [Gemini in BigQuery Pricing Overview](https://cloud.google.com/products/gemini/pricing#gemini-in-bigquery-pricing) for information about pricing for Gemini in BigQuery.

## 

On-demand compute pricing

By default, queries are billed using the on-demand (per TiB) pricing model, where you pay for the data scanned by your queries.

With on-demand pricing, you will generally have access to up to 2,000 concurrent slots, shared among all queries in a single project. Periodically, BigQuery will temporarily burst beyond this limit to accelerate smaller queries. In addition, you might have fewer slots available if there is a high amount of contention for capacity in a specific location.

On-demand (per TiB) query pricing is as follows:

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Operation| Price (USD)| Details  
---|---|---  
Queries (on-demand)| 0 tebibyte to 1 tebibyteFree per 1 month / account1 tebibyte and above$6.25 / 1 tebibyte, per 1 month / account| The first 1 TiB per month is free.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Pricing details

Note the following regarding on-demand (per TiB) query charges:

  * BigQuery uses a [columnar data structure](https://en.wikipedia.org/wiki/Column-oriented_DBMS). You're charged according to the total data processed in the columns you select, and the total data per column is calculated based on the types of data in the column. For more information about how your data size is calculated, see [Estimate query costs](https://cloud.google.com/bigquery/docs/best-practices-costs#estimate-query-costs).
  * You are charged for queries run against shared data. The data owner is not charged when their data is accessed.
  * You aren't charged for queries that return an error or for queries that retrieve [results from the cache](https://cloud.google.com/bigquery/docs/cached-results). For [procedural language jobs](https://cloud.google.com/bigquery/docs/reference/standard-sql/procedural-language) this consideration is provided at a per-statement level.
  * Charges are rounded up to the nearest MB, with a minimum 10 MB data processed per table referenced by the query, and with a minimum 10 MB data processed per query.
  * Canceling a running query job might incur charges up to the full cost for the query if you let the query run to completion.
  * When you run a query, you're charged according to the data processed in the columns you select, even if you set an explicit LIMIT on the results.
  * [Partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables) and [clustering](https://cloud.google.com/bigquery/docs/clustered-tables) your tables can help reduce the amount of data processed by queries. As a best practice, use partitioning and clustering whenever possible.
  * On-demand (per TiB) pricing is referred to as analysis pricing on the [Google Cloud SKUs](https://cloud.google.com/skus/?filter=bigquery) page.
  * When you run a query against a clustered table, and the query includes a filter on the clustered columns, BigQuery uses the filter expression to prune the blocks scanned by the query. This can reduce the number of scanned bytes.



BigQuery provides cost control mechanisms that enable you to cap your query costs. You can set:

  * User-level and project-level [custom cost controls](https://cloud.google.com/bigquery/docs/custom-quotas)
  * The [maximum bytes billed](https://cloud.google.com/bigquery/docs/best-practices-costs#limit_query_costs_by_restricting_the_number_of_bytes_billed) by a query



For detailed examples of how to calculate the number of bytes processed, see [Query size calculation](https://cloud.google.com/bigquery/docs/estimate-costs#query_size_calculation).

## 

Capacity compute pricing

BigQuery offers a capacity-based compute pricing model for customers who need additional capacity or prefer a predictable cost for query workloads rather than the on-demand price (per TiB of data processed). The capacity compute model offers pay-as-you-go pricing (with autoscaling) and optional one year and three year commitments that provide discounted prices. You pay for query processing capacity, measured in [slots (virtual CPUs)](https://cloud.google.com/bigquery/docs/slots) over time.

To enable capacity pricing, use [BigQuery reservations](https://cloud.google.com/bigquery/docs/reservations-intro).

BigQuery slot capacity:

  * is available in 3 editions: Standard, Enterprise, and Enterprise Plus.
  * applies to query costs, including BigQuery ML, DML, and DDL statements.
  * does not apply to [storage costs](https://docs.cloud.google.com/bigquery/pricing#storage-pricing) or BI Engine costs.
  * does not apply to streaming inserts and using the [BigQuery Storage API](https://cloud.google.com/bigquery/docs/reference/storage).
  * can leverage the BigQuery autoscaler.
  * is billed per second with a one-minute minimum duration by default. You can opt in to BigQuery fluid scaling at the reservation level for per-second billing with no minimum duration.



Optional BigQuery [slot commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments):

  * are available for one or three year periods.
  * are available in Enterprise and Enterprise Plus editions.
  * are regional capacity. Commitments in one region (either customer selected single region or BigQuery selected single region on the customer’s behalf when the customer chooses multi-region) cannot be used in another region.
  * can be shared across your entire organization. There is no need to buy slot [commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments) for every project.
  * are offered with a 50-slot minimum and increments of 50 slots.
  * are automatically renewed unless set to cancel at the end of the period.



### 

Standard Edition

The following table shows the cost of slots in Standard edition.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Default* (USD)_info_

## Consumption model ID:

7754-699E-0EBF| BigQuery CUD - 1 Year* (USD)_info_

## Consumption model ID:

DD83-D9A3-79AF| BigQuery CUD - 3 Year* (USD)_info_

## Consumption model ID:

4D8D-49A7-C5B1| Details  
---|---|---|---  
$0.04 / 1 hour| $0.036 / 1 hour| $0.032 / 1 hour| No commitment. Billed per second with a 1-minute minimum. Opt-in to Fluid scaling for no-minimum, per-second billing  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

*Prices reflect Pay as you go

### 

Enterprise Edition

The following table shows the cost of slots in Enterprise edition.

Iowa (us-central1)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Sydney (AWS) (aws-ap-southeast-2)
  * Frankfurt (AWS) (aws-eu-central-1)
  * Ireland (AWS) (aws-eu-west-1)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Oregon (AWS) (aws-us-west-2)
  * Virginia (Azure) (azure-us-east2)
  * Washington (Azure) (azure-westus2)
  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Default* (USD)_info_

## Consumption model ID:

7754-699E-0EBF| BigQuery CUD - 1 Year* (USD)_info_

## Consumption model ID:

DD83-D9A3-79AF| BigQuery CUD - 3 Year* (USD)_info_

## Consumption model ID:

4D8D-49A7-C5B1| Resource CUDs - 1 Year (USD)| Resource CUDs - 3 Year (USD)  
---|---|---|---|---  
$0.06 / 1 hour| $0.054 / 1 hour| $0.048 / 1 hour| $0.048 / 1 hour| $0.036 / 1 hour  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

*Prices reflect Pay as you go

1Billed per second with a 1 minute minimum

### 

Enterprise Plus Edition

The following table shows the cost of slots in Enterprise plus edition.

Iowa (us-central1)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Sydney (AWS) (aws-ap-southeast-2)
  * Frankfurt (AWS) (aws-eu-central-1)
  * Ireland (AWS) (aws-eu-west-1)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Oregon (AWS) (aws-us-west-2)
  * Virginia (Azure) (azure-us-east2)
  * Washington (Azure) (azure-westus2)
  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Default* (USD)_info_

## Consumption model ID:

7754-699E-0EBF| BigQuery CUD - 1 Year* (USD)_info_

## Consumption model ID:

DD83-D9A3-79AF| BigQuery CUD - 3 Year* (USD)_info_

## Consumption model ID:

4D8D-49A7-C5B1| Resource CUDs - 1 Year (USD)| Resource CUDs - 3 Year (USD)  
---|---|---|---|---  
$0.10 / 1 hour| $0.09 / 1 hour| $0.08 / 1 hour| $0.08 / 1 hour| $0.06 / 1 hour  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

*Prices reflect Pay as you go

1Billed per second with a 1 minute minimum

## 

BigQuery services pricing

Additional services that are used as part of BigQuery will be billed using the BigQuery services SKU. These services include data transfer service.

The following table shows the various services that are billed using [BigQuery services SKU](https://cloud.google.com/skus?filter=BigQuery%20services).

Service| How to Use| Notes  
---|---|---  
Earth Engine in BigQuery| ST_RegionStats() calls in BigQuery scripts| This function sends tasks to Earth Engine; Earth Engine Compute Units are translated to BigQuery services slot hours.  
Python UDF| Refer to [this link](https://cloud.google.com/bigquery/docs/user-defined-functions-python)| BigQuery customers are charged for building and executing Python UDFs. Build charges are proportional to the build-time and the execution charges are proportional to compute and memory usage of the UDF.  
  
To see pricing, select a region from the drop-down list above the following table:

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Metric| Price (USD)*_info_

## Consumption model ID:

7754-699E-0EBF| BigQuery CUD - 1 Year* (USD)_info_

## Consumption model ID:

DD83-D9A3-79AF| BigQuery CUD - 3 Year* (USD)_info_

## Consumption model ID:

4D8D-49A7-C5B1  
---|---|---|---  
Compute (per slot-hour)| $0.06 / 1 hour| $0.054 / 1 hour| $0.048 / 1 hour  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

## 

Storage pricing

Storage pricing is the cost to store data that you load into BigQuery. You pay for  _active storage_ and  _long-term_ storage.

  * **Active storage** includes any table or table partition that has been modified in the last 90 days.
  * **Long-term storage** includes any table or table partition that has not been modified for 90 consecutive days. The price of storage for that table automatically drops by approximately 50%. There is no difference in performance, durability, or availability between active and long-term storage.



Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Operation| Price (USD)| Details  
---|---|---  
Active logical storage| $0.000031507 / 1 gibibyte hour, per 1 month / account| The first 10 GiB is free each month.  
Long-term logical storage| $0.000021918 / 1 gibibyte hour, per 1 month / account| The first 10 GiB is free each month.  
Active physical storage| $0.000054795 / 1 gibibyte hour, per 1 month / account| The first 10 GiB is free each month.  
Long-term physical storage| $0.000027397 / 1 gibibyte hour, per 1 month / account| The first 10 GiB is free each month.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

See the [physical storage documentation](https://cloud.google.com/bigquery/docs/datasets-intro#dataset_storage_billing_models) for eligibility criteria.

### 

Pricing details﻿

Storage pricing is based on the amount of data stored in your [tables](https://cloud.google.com/bigquery/docs/tables-intro#table_pricing). [Temporary session tables](https://cloud.google.com/bigquery/docs/sessions-intro) and [temporary multi-statement tables](https://cloud.google.com/bigquery/docs/multi-statement-queries#storage-pricing) are charged for active storage only. There are no storage charges for [temporary cached query result tables](https://cloud.google.com/bigquery/docs/cached-results). There are no charges for time travel and failsafe storage for logical storage. Time travel and failsafe storage charges apply for [physical storage](https://cloud.google.com/bigquery/docs/time-travel#billing).

The size of the data is calculated based on the data types of the individual columns. For a detailed explanation of how data size is calculated, see Data size calculation.

Storage pricing is prorated per MiB, per second. For example, if you are using active logical storage in us-central1:

  * For 512 MiB for half a month, you pay $0.00575 USD
  * For 100 GiB for half a month, you pay $1.15 USD
  * For 1 TiB for a full month, you pay $23.552 USD



Storage usage is calculated in [gibibytes months (GiB months)](https://en.wikipedia.org/wiki/Gibibyte), where 1 GiB is 230 bytes (1,024 MiB). Similarly, 1 tebibyte (TiB) is 240 bytes (1,024 GiB). The final usage value is the product of data size in gibibytes and storage use time in months.

If the data in a table is not modified or deleted within 90 consecutive days, it is billed at the **long-term storage** rate. There is no degradation of performance, durability, availability, or any other functionality when a table is considered long-term storage.

Each partition of a partitioned table is considered separately for long-term storage pricing. If a partition hasn't been modified in the last 90 days, the data in that partition is considered long term storage and is charged at the discounted price.

If the table is edited, the price reverts back to the regular storage pricing, and the 90-day timer starts counting from zero. Anything that modifies the data in a table resets the timer, including:

Action| Details  
---|---  
Loading data into a table| Any load or query job that appends data to a destination table or overwrites a destination table.  
Copying data into a table| Any copy job appends data to a destination table or overwrites a destination table.  
Writing query results to a table| Any query job that appends data to a destination table or overwrites a destination table.  
Using data manipulation language (DML)| Using a [DML statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language) to modify table data.  
Using data definition language (DDL)| Using a [CREATE OR REPLACE TABLE](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_statement) statement to replace a table.  
Streaming data into the table| Ingesting data using the [Storage Write API (REST)](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery) call.  
  
All other actions do not reset the timer, including the following:

  * Querying a table
  * Creating a view that queries a table
  * Exporting data from a table
  * Copying a table (to another destination table)
  * Patching or updating a [table resource](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables)



For tables that reach the 90-day threshold during a billing cycle, the price is prorated accordingly.

Long-term storage pricing applies only to BigQuery storage, not to data stored in [external data sources](https://docs.cloud.google.com/bigquery/external-data-sources) such as Bigtable, Cloud Storage, and Google Drive.

### 

Data size calculation

When you load data into BigQuery or query the data, you're charged according to the data size. Data size is calculated based on the size of each column's [data type](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types).

The size of your stored data and the size of the data processed by your queries is calculated in [gibibytes (GiB)](https://en.wikipedia.org/wiki/Gibibyte), where 1 GiB is 230 bytes (1,024 MiB). Similarly, 1 tebibyte (TiB) is 240 bytes (1,024 GiB).

For more information, see [Data type sizes](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#data_type_sizes).

## 

Data Transfer Service pricing

You are charged for the compute resources consumed by your data transfers, which is measured in slot-hours.

The total cost for a transfer consists of two components:

  1. [Transfer Orchestration](https://docs.cloud.google.com/bigquery/pricing#transfer-orchestration): The resources used to manage the connector execution.
  2. [Data Loading & Processing](https://docs.cloud.google.com/bigquery/pricing#data-loading-processing): The resources used to load and merge data into the destination table.



### 

Transfer Orchestration﻿

You are charged as follows:

Type| Billing Model| Connectors  
---|---|---  
**Free connectors**

  * Alphabet sources (excl. Google Play)
  * Object storage sources
  * Migration connectors

| No charge.| [**Campaign Manager**](https://cloud.google.com/bigquery/docs/doubleclick-campaign-transfer)**,**[**Cloud Storage**](https://cloud.google.com/bigquery/docs/cloud-storage-transfer)**,**[**Amazon S3**](https://cloud.google.com/bigquery/docs/s3-transfer)**1****,**[**Google Ads**](https://cloud.google.com/bigquery/docs/adwords-transfer)**,**[**Google Ad Manager**](https://cloud.google.com/bigquery/docs/doubleclick-publisher-transfer)**,**[**Google Merchant Center**](https://cloud.google.com/bigquery/docs/merchant-center-transfer)**,**[**Search Ads 360**](https://cloud.google.com/bigquery/docs/sa360-transfer)**,**[**YouTube Channel**](https://cloud.google.com/bigquery/docs/youtube-channel-transfer)**,**[**YouTube Content Owner**](https://cloud.google.com/bigquery/docs/youtube-content-owner-transfer)**,**[**Amazon Redshift**](https://cloud.google.com/bigquery/docs/migration/redshift-overview)**1****,**[**Teradata**](https://cloud.google.com/bigquery/docs/migration/teradata-overview)**12****,**[**Azure Blob Storage**](https://cloud.google.com/bigquery/docs/blob-storage-transfer), [**Display & Video 360**](https://cloud.google.com/bigquery/docs/display-video-transfer), [**Google Analytics 4**](https://cloud.google.com/bigquery/docs/google-analytics-4-transfer), [**Comparison Shopping Service (CSS) Center****PREVIEW**](https://docs.cloud.google.com/bigquery/docs/css-center-transfer-schedule-transfers)**,**[**Google Merchant Center****PREVIEW**](https://cloud.google.com/bigquery/docs/merchant-center-transfer), [**Hive Managed Tables****PREVIEW**](https://cloud.google.com/bigquery/docs/migration/hive-overview)**and**[**Snowflake Migration****PREVIEW******](https://cloud.google.com/bigquery/docs/migration/snowflake-transfer)**.**  
  
**﻿Paid connectors**

  * All other sources

| Consumption-based, measured in slot-hours. [See details.](https://docs.cloud.google.com/bigquery/pricing#consumption-based-pricing)  
Note: Connectors in “Preview” will not be charged. Billing will start once connector are GA.| **GA Connectors:**[**Salesforce**](https://cloud.google.com/bigquery/docs/salesforce-transfer)**,**[**ServiceNow**](https://cloud.google.com/bigquery/docs/servicenow-transfer)**,**[**Salesforce Marketing Cloud (SFMC)**](https://cloud.google.com/bigquery/docs/sfmc-transfer), [**Facebook Ads**](https://cloud.google.com/bigquery/docs/facebook-ads-transfer), [**MySQL**](https://cloud.google.com/bigquery/docs/mysql-transfer), [**PostgreSQL**](https://cloud.google.com/bigquery/docs/postgresql-transfer) **and** [**Oracle**](https://cloud.google.com/bigquery/docs/oracle-transfer)**.**  
**Preview Connectors:**[**Stripe**](https://docs.cloud.google.com/bigquery/docs/stripe-transfer)**,**[**Paypal**](https://docs.cloud.google.com/bigquery/docs/paypal-transfer),****[**HubSpot**](https://cloud.google.com/bigquery/docs/hubspot-transfer)**,**[**Klaviyo**](https://cloud.google.com/bigquery/docs/klaviyo-transfer)**and**[**SQL Server**](https://cloud.google.com/bigquery/docs/sqlserver-transfer)**.**  
$25 per unique [Package Name](https://docs.cloud.google.com/bigquery/pricing#google-play-package-name) in the Installs_country table. [See details.](https://docs.cloud.google.com/bigquery/pricing#google-play-package-name)| [**Google Play**](https://cloud.google.com/bigquery/docs/play-transfer)  
**Connectors offered by partners**|  Costs apply. [See details.](https://docs.cloud.google.com/bigquery/pricing#third-party-connectors)| For more information refer to individual connectors in the [Marketplace](https://cloud.google.com/marketplace).  
  
### **Notes on transfer pricing**

1\. Costs can be incurred outside of Google Cloud by using the BigQuery Data Transfer Service, such as AWS or Azure data transfer charges.

2\. Data is _not_ automatically deleted from your Cloud Storage bucket after it is uploaded to BigQuery. Consider deleting the data from your Cloud Storage bucket to avoid additional storage costs. See [Cloud Storage pricing](https://cloud.google.com/storage/pricing)

### 

Consumption-based pricing

You are charged for the compute resources consumed by your data transfers, which is measured in slot-hours.

The following table shows the cost of slots.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Show discount options

HourlyHourly

MonthlyMonthly

Default* (USD)_info_

## Consumption model ID:

7754-699E-0EBF| BigQuery CUD - 1 Year* (USD)_info_

## Consumption model ID:

DD83-D9A3-79AF| BigQuery CUD - 3 Year* (USD)_info_

## Consumption model ID:

4D8D-49A7-C5B1  
---|---|---  
$0.06 / 1 hour| $0.054 / 1 hour| $0.048 / 1 hour  
  
* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click [here](https://cloud.google.com/docs/cuds-multiprice#how-to-opt-in) to learn more.

### 

Cost Estimation

To estimate costs, you can use a conservative guideline of up to 20 slot-hours for each hour of a transfer’s run time. In the us-central1 region, this is equivalent to an estimated upper bound of $1.20 per hour of transfer run time. This is for planning purposes, and actual slot-hour consumption may differ.

### 

Google Play Package Name

Every Android app has a unique application ID that looks like a Java package name, such as com.example.myapp. The [Installs](https://support.google.com/googleplay/android-developer/answer/6135870#statistics&zippy=%2Cinstalls) report contains a column of "Package Name". The number of unique package names is used for calculating usage of transfers.

Each transfer you create generates one or more runs per day. Package names are only counted on the day a transfer run completes. For example, if a transfer run begins on July 14th but completes on July 15th, the package names are counted on July 15th.

If a unique package name is encountered in more than one transfer run on a particular day, it is counted only once. Package names are counted separately for different transfer configurations. If a unique package name is encountered in runs for two separate transfer configurations, the package name is counted twice.

If a package name appeared every day for an entire month, you would be charged the full $25 for that month. Otherwise, if it appeared for a part of the month, the charge would be prorated.

Example#1: If we sync for 1 application - com.smule.singandroid, will it cost us $25 per month + storage price for BigQuery?

The answer is $25 per month (prorated) + storage/querying costs from BigQuery.

Example#2: If we sync all historic data (for 10 years), will we be charged for 120 months or for 1 month, because we transferred them at once?

The answer is still $25 per month (prorated) + storage/querying costs from BigQuery, since we charge $25 per unique [Package Name](https://cloud.google.com/bigquery/pricing#google-play-package-name) in the Installs_country table, regardless of how many years the historic data goes back to that unique Package Name.

### 

Third-party Connectors

Costs apply for connectors provided by third-party partners. The pricing model differs for different partners and connectors. For more pricing details, refer to individual connectors when enrolling in [Marketplace](https://cloud.google.com/marketplace).

### 

Data Loading & Processing

You are charged as follows:

Destination Type| Operation Type| Data Loading & Processing Billing Model| Details  
---|---|---|---  
BigQuery Native Tables| Load| Free| Standard load jobs into BigQuery native tables.  
Merge| Standard BigQuery Rates| Standard merge jobs into BigQuery native tables.  
Lakehouse for Apache Iceberg tables| Load & Merge| Standard Lakehouse for Apache Iceberg Rates| Standard load and merge jobs into Lakehouse for Apache Iceberg tables.  
  
### 

How to Track Costs

To view the total cost of your transfers—aggregating both Transfer Orchestration and Data Loading & Processing—filter your billing reports by the following label:

Key: goog-bq-feature-type

Value: DATA_TRANSFER_SERVICE

**Note** : Starting August 11, 2026, all Data Transfer Service SKUs will be unified under the label value: data_transfer_service

## 

BigQuery Omni pricing

BigQuery Omni offers the following pricing models depending on your workloads and needs.

### 

On-Demand compute pricing

Similar to BigQuery on-demand analysis model, BigQuery Omni queries, by default are billed using the on-demand (per TiB) pricing model, where you pay for the data scanned by your queries.

With on-demand pricing, you will generally have access to a large pool of concurrent slots, shared among all queries in a single project. Periodically, BigQuery Omni will temporarily burst beyond this limit to accelerate smaller queries. In addition, you might have fewer slots available if there is a high amount of contention for capacity in a specific location.

BigQuery Omni on-demand (per TiB) query pricing is as follows:

Seoul (AWS) (aws-ap-northeast-2)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Sydney (AWS) (aws-ap-southeast-2)
  * Frankfurt (AWS) (aws-eu-central-1)
  * Ireland (AWS) (aws-eu-west-1)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Oregon (AWS) (aws-us-west-2)
  * Virginia (Azure) (azure-us-east2)
  * Washington (Azure) (azure-westus2)



Item| Price (USD)  
---|---  
BigQuery Omni on-demand| $9.125 / 1 tebibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Pricing details

The details and limitations are similar to BigQuery analysis pricing. Note the following regarding on-demand (per TiB) query charges:

  * BigQuery uses a [columnar data structure.](https://en.wikipedia.org/wiki/Column-oriented_DBMS) You're charged according to the total data processed in the columns you select, and the total data per column is calculated based on the types of data in the column. For more information about how your data size is calculated, see [Data size calculation.](https://docs.cloud.google.com/bigquery/pricing#data-size-calculation)
  * You aren't charged for queries that return an error or for queries that retrieve [results from the cache.](https://cloud.google.com/bigquery/docs/cached-results) For [procedural language jobs](https://cloud.google.com/bigquery/docs/reference/standard-sql/procedural-language) this consideration is provided at a per-statement level.
  * Charges are rounded up to the nearest MB, with a minimum 10 MB data processed per table referenced by the query, and with a minimum 10 MB data processed per query.
  * Canceling a running query job might incur charges up to the full cost for the query if you let the query run to completion.
  * When you run a query, you're charged according to the data processed in the columns you select, even if you set an explicit LIMIT on the results.
  * [Partitioning](https://cloud.google.com/bigquery/docs/partitioned-tables) and [clustering](https://cloud.google.com/bigquery/docs/clustered-tables) your tables can help reduce the amount of data processed by queries. As a best practice, use partitioning and clustering whenever possible.
  * On-demand (per TiB) pricing is referred to as analysis pricing on the [Google Cloud SKUs](https://cloud.google.com/skus/?filter=bigquery) page.
  * When you run a query against a clustered table, and the query includes a filter on the clustered columns, BigQuery uses the filter expression to prune the blocks scanned by the query. This can reduce the number of scanned bytes.



BigQuery provides cost control mechanisms that enable you to cap your query costs. You can set:

  * User-level and project-level [custom cost controls.](https://cloud.google.com/bigquery/docs/custom-quotas)
  * The [maximum bytes billed](https://cloud.google.com/bigquery/docs/best-practices-costs#limit_query_costs_by_restricting_the_number_of_bytes_billed) by a query



### 

BigQuery Omni with editions

BigQuery Omni regions support [BigQuery editions](https://docs.cloud.google.com/bigquery/pricing#editions-commitment-bundle). At present only Enterprise Edition is supported in Omni regions

The following table shows the cost of slots in Omni regions

Seoul (AWS) (aws-ap-northeast-2)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Sydney (AWS) (aws-ap-southeast-2)
  * Frankfurt (AWS) (aws-eu-central-1)
  * Ireland (AWS) (aws-eu-west-1)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Oregon (AWS) (aws-us-west-2)
  * Virginia (Azure) (azure-us-east2)
  * Washington (Azure) (azure-westus2)



Show discount options

HourlyHourly

MonthlyMonthly

Number of slots| PAYG (No commitment) (USD)| Resource CUDs - 1 Year (USD)| Resource CUDs - 3 Year (USD)  
---|---|---|---  
100| $7.50 / 1 hour| $6.00 / 1 hour| $4.50 / 1 hour  
  
### 

Omni Cross Cloud Data Transfer

When using Omni’s Cross Cloud capabilities (Cross Cloud Transfer, Create Table as Select, Insert Into Select, Cross Cloud Joins, and Cross Cloud Materialized Views) that involve data moving from AWS or Azure to Google Cloud, there will be additional charges for data transfer.

Specifically for Cross-Cloud Materialized Views, Create Table as Select, Insert Into Select, and Cross Cloud Joins there are no charges during Preview. Starting 29 February 2024, these services will be generally available and you will be charged for data transfer. You will be charged for data transfer only when using any of the above listed services from an AWS or Azure region to a Google Cloud BigQuery region. You will be charged on a per GiB rate based on the amount of data transferred from AWS or Azure to Google Cloud.

SKU| Billing model| Price (USD)  
---|---|---  
Cross-cloud data transfer from AWS North Virginia (aws-us-east-1) to Google Cloud North America| usage-based| $0.09 / 1 gibibyte  
Cross-cloud data transfer from Azure North Virginia (azure-eastus2) to Google Cloud North America| usage-based| $0.0875 / 1 gibibyte  
Cross-cloud data transfer from AWS Seoul (aws-ap-northeast-2) to Google Cloud Asia| usage-based| $0.126 / 1 gibibyte  
Cross-cloud data transfer from AWS Oregon (aws-us-west-2) to Google Cloud North America| usage-based| $0.09 / 1 gibibyte  
Cross-cloud data transfer from AWS Ireland (aws-eu-west-1) to Google Cloud Europe| usage-based| $0.09 / 1 gibibyte  
Cross-cloud data transfer from AWS Sydney (aws-ap-southeast-2) to Google Cloud Oceania| usage-based| $0.114 / 1 gibibyte  
Cross-cloud data transfer from AWS Frankfurt (aws-eu-central-1) to Google Cloud Europe| usage-based| $0.09 / 1 gibibyte  
  
### 

Omni Managed Storage

When using Omni’s Cross Cloud Materialized Views capability, you will also be charged for creation of local materialized views which is on BigQuery Managed Storage on AWS. You will be charged a per GiB for the amount of physical storage that is used for the local materialized view.

Seoul (AWS) (aws-ap-northeast-2)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Sydney (AWS) (aws-ap-southeast-2)
  * Frankfurt (AWS) (aws-eu-central-1)
  * Ireland (AWS) (aws-eu-west-1)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Oregon (AWS) (aws-us-west-2)



HourlyHourly

MonthlyMonthly

Operation| Price (USD)  
---|---  
Active physical storage| $0.000071233 / 1 gibibyte hour  
Long-term physical storage| $0.000035616 / 1 gibibyte hour  
  
## 

Data ingestion pricing

BigQuery offers two modes of data ingestion:

  * **Batch loading**. [Load source files](https://cloud.google.com/bigquery/docs/batch-loading-data) into one or more BigQuery tables in a single batch operation.
  * **Streaming**. Stream data one record at a time or in small batches using the [BigQuery Storage Write API](https://cloud.google.com/bigquery/docs/write-api) (gRPC) or [Storage Write API (REST)](https://docs.cloud.google.com/bigquery/docs/write-api-rest).



For more information about which mode to choose, see [Introduction to loading data](https://cloud.google.com/bigquery/docs/loading-data).

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Operation| Pricing| Details  
---|---|---  
Batch Loading| Free using the shared slot pool named default-pipeline.| Customers can choose [editions pricing ](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing)for guaranteed capacity. Once the data is loaded into BigQuery, you are charged for storage.  
Streaming inserts (Storage Write API (REST))| $0.01 / 200 mebibyte| You are charged for rows that are successfully inserted. Individual rows are calculated using a 1 KB minimum size.  
BigQuery Storage Write API (gRPC)| $0.025 / 1 gibibyte, per 1 month / account| The first 2 TiB per month are free.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Pricing details

By default, you are not charged for batch loading data from Cloud Storage or from local files into BigQuery. Cross-region load jobs are billed for network usage under [Network Data Transfer SKUs](https://cloud.google.com/skus?filter=Network%20Data%20Transfer%20GCP%20Inter%20Region%20storage&currency=USD).

Load jobs by default use a shared pool of slots. BigQuery does not make guarantees about the available capacity of this shared pool or the throughput you will see. Alternatively, you can purchase dedicated slots to run load jobs. You are charged [capacity-based pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing) for dedicated slots. When load jobs are assigned to a reservation, they lose access to the free pool. For more information, see [Assignments](https://cloud.google.com/bigquery/docs/reservations-intro#assignments).

Once your data is loaded into BigQuery, it is subject to BigQuery [storage pricing](https://docs.cloud.google.com/bigquery/pricing#storage-pricing). If you load data from Cloud Storage, you are charged for storing the data in Cloud Storage. For details, see [Data storage](https://cloud.google.com/storage/pricing#storage-pricing) on the Cloud Storage pricing page.

## 

Data extraction pricing

BigQuery offers the following modes of data extraction:

  * **Batch export**. Use an an [extract job](https://cloud.google.com/bigquery/docs/managing-jobs) to export table data to [Cloud Storage](https://cloud.google.com/bigquery/docs/exporting-data). There is no processing charge for exporting data from a BigQuery table using an extract job. Cross-region extract jobs are billed under [General Data Transfer Networking Traffic for Google Cloud Cross Region SKUs](https://cloud.google.com/skus?currency=USD&filter=General%20Data%20Transfer%20Networking%20Traffic%20for%20Google%20Cloud%20Cross%20Region).
  * **Export query results**. Use the [EXPORT DATA](https://cloud.google.com/bigquery/docs/reference/standard-sql/export-statements) statement to export query results to [Cloud Storage](https://cloud.google.com/bigquery/docs/exporting-data), [Bigtable](https://cloud.google.com/bigquery/docs/export-to-bigtable), or [Spanner](https://cloud.google.com/bigquery/docs/export-to-spanner). You are billed for the compute cost to process the query statement.
  * **Streaming reads**. Use the [Storage Read API](https://cloud.google.com/bigquery/docs/reference/storage) to perform high-throughput reads of table data. You are billed for the amount of data read.



**Note:** You are not charged for data extraction or data transfer when accessing [query results](https://cloud.google.com/bigquery/docs/writing-results) in the Google Cloud console, BigQuery API, or any other clients, such as Looker.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Operation| Pricing| Details  
---|---|---  
Batch exports| Free using the shared slot pool.| You can export up to [50 tebibytes per day ](https://cloud.google.com/bigquery/quotas#export_jobs)for free using the shared slot pool. You are charged for the data stored in Cloud Storage.  
Streaming reads (BigQuery Storage Read API)| $1.10 / 1 tebibyte, per 1 month / account| Customers can read up to 300 TiB of data per month at no charge.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Batch export data transfer pricing

You are charged for data transfer when you export data in batch from BigQuery to a Cloud Storage bucket or Spanner table in another region, as follows:

Case| Example| Rate  
---|---|---  
Export within the same location| From us-east1 to us-east1| Free  
Export from BigQuery US multi-region| From US multi-region to us-central1 (Iowa)| Free  
Export from BigQuery US multi-region| From US multi-region to any region (except us-central1 (Iowa))| See following table  
Export from BigQuery EU multi-region| From EU multi-region to europe-west4 (Netherlands)| Free  
Export from BigQuery EU multi-region| From EU multi-region to any region (except europe-west4 (Netherlands))| See following table  
Export across locations| From us-east1 to us-central1| See following table  
  
**Note:** All prices are in $/GiB and all GiB are in physical bytes.

| North America| Europe| Asia| Indonesia| Oceania| Middle East| Latin America| Africa  
---|---|---|---|---|---|---|---|---  
**North America**|  $0.02| $0.05| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Europe**|  $0.05| $0.02| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Asia**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Indonesia**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Oceania**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Middle East**|  $0.11| $0.11| $0.11| $0.11| $0.11| $0.08| $0.14| $0.11  
**Latin America**|  $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.20| $0.14  
**Africa**|  $0.11| $0.11| $0.11| $0.14| $0.14| $0.11| $0.14| $0.11  
  
### 

Storage Read API data transfer within Google Cloud

Case| Examples| Rate  
---|---|---  
Accessing cached query results from [temporary tables](https://cloud.google.com/bigquery/docs/cached-results#how_cached_results_are_stored)| 

  * Temporary tables "anonymous dataset"

| Free  
Data reads within the same location| 

  * From us-east1 to us-east1

| Free  
Data read from a [BigQuery multi-region](https://cloud.google.com/bigquery/docs/locations#multi-regional-locations) to a different BigQuery location, and both locations are on the same continent.| 

  * From us to us-east1
  * From eu to europe-west1

| Free  
Data read between different locations on the same continent (assuming none of the above free cases apply)| 

  * From us-east1 to northamerica-northeast1
  * From europe-west1 to europe-north1

| $0.01 / 1 gibibyte  
Data moves between different continents within Google cloud and neither is Australia.| 

  * From us to asia
  * From europe-west1 to southamerica-east1

| $0.08 / 1 gibibyte  
Data moves between different continents within Google cloud and one is Australia.| 

  * From us to australia-southeast1
  * From australia-southeast1 to europe-west1

| $0.15 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Storage Read API general network usage

| Price (USD)  
---|---  
Data Transfer to Worldwide Destinations (excluding Asia & Australia)| 0 tebibyte to 1 tebibyte$0.12 / 1 gibibyte, per 1 month / account1 tebibyte to 10 tebibyte$0.11 / 1 gibibyte, per 1 month / account10 tebibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data Transfer to Asia Destinations (excluding China, but including Hong Kong)| 0 tebibyte to 1 tebibyte$0.12 / 1 gibibyte, per 1 month / account1 tebibyte to 10 tebibyte$0.11 / 1 gibibyte, per 1 month / account10 tebibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data Transfer to China Destinations (excluding Hong Kong)| 0 tebibyte to 1 tebibyte$0.19 / 1 gibibyte, per 1 month / account1 tebibyte to 10 tebibyte$0.18 / 1 gibibyte, per 1 month / account10 tebibyte and above$0.15 / 1 gibibyte, per 1 month / account  
Data Transfer to Australia Destinations| 0 tebibyte to 1 tebibyte$0.19 / 1 gibibyte, per 1 month / account1 tebibyte to 10 tebibyte$0.18 / 1 gibibyte, per 1 month / account10 tebibyte and above$0.15 / 1 gibibyte, per 1 month / account  
Data transfer in| Free  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Storage Read API pricing details

The Storage Read API has an on-demand price model. With on-demand pricing, BigQuery charges for the number of bytes processed (also referred to as bytes read). On-demand pricing is solely based on usage, with a bytes read free tier of 300 TiB per month for each billing account. Bytes scanned as part of reads from [temporary tables](https://cloud.google.com/bigquery/docs/cached-results#how_cached_results_are_stored) are free and do not count against the 300TiB free tier. This free bytes read 300 TiB is on the bytes-read component, and does not apply to associated outbound data transfer.

Note the following regarding Storage Read API charges:

  * You are charged according to the total amount of data read. The total data read per column is calculated based on the type of data in the column, and the size of the data is calculated based on the column's data type. For a detailed explanation of how data size is calculated, see [Data size calculation](https://docs.cloud.google.com/bigquery/pricing#data-size-calculation).
  * You are charged for any data read in a read session even if a **ReadRows** call fails.
  * If you cancel a ReadRows call before the end of the stream is reached, you are charged for any data read before the cancellation. Your charges can include data that was read but not returned to you before the cancellation of the **ReadRows** call.
  * As a best practice, use partitioned and clustered tables whenever possible. You can reduce the amount of data read by using a **WHERE** clause to prune partitions. For more information, see [Querying partitioned tables](https://cloud.google.com/bigquery/docs/querying-partitioned-tables#querying_partitioned_tables_2).
  * When using Interconnect, Cloud [Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing#egress-traffic-from-a-vpc-network-through-an-interconnect-connection_1) applies instead of BigQuery Storage Read API General Network Usage prices.



## 

Data replication pricing

Besides copy operations within the same region, BigQuery offers two modes of replicating (copying) data between regions. You can perform a one-time copy operation, or use incremental, ongoing replication. Your options for copying data across regions include the following:

  * **Cross-region copy**. One time or scheduled copy of table data to between regions or multi-regions, see [copy datasets](https://cloud.google.com/bigquery/docs/managing-datasets#copy-datasets) or [copy tables](https://cloud.google.com/bigquery/docs/managing-tables#copy_tables_across_regions). Cross-region copy is billed under [General Data Transfer Networking Traffic for Google Cloud Cross Region SKUs](https://cloud.google.com/skus?currency=USD&filter=General%20Data%20Transfer%20Networking%20Traffic%20for%20Google%20Cloud%20Cross%20Region).
  * **Cross-region replication**. Ongoing, incremental replication of a dataset between two or more different regions or multi-regions, see [cross-region dataset replication](https://cloud.google.com/bigquery/docs/data-replication).
  * **Cross-region Turbo replication**. High performance, ongoing, incremental replication of a dataset between two or more different regions or multi-regions. Available only with [managed disaster recovery](https://cloud.google.com/bigquery/docs/managed-disaster-recovery).



Both cross-region replication and cross-region Turbo replication are billed under the [BigQuery Network Egress Replication SKUs](https://cloud.google.com/skus/sku-groups/bigquery-network-egress-replication).

### 

Storage for replicated data

Replicated data stored in the destination region or multi-region is charged according to [BigQuery storage pricing](https://docs.cloud.google.com/bigquery/pricing#storage-pricing).

### 

Data transfer pricing for replicated data

You are charged for data transfer for the volume of data replicated. The use cases and breakdown of data transfer charges are provided as follows:

Case| Example| Rate  
---|---|---  
Replicate within the same location| From us-east1 to us-east1, From US multi-region to US multi-region, From EU multi-region to EU multi-region| Free  
Replicate from BigQuery US multi-region to us-central1 or vice-versa| US multi-region to us-central1 (Iowa), us-central1 (Iowa) to US multi-region| Free  
Replicate from BigQuery US multi-region to any other region not in US multi-region| From US multi-region to any region (except us-central1 (Iowa))| See following table  
Replicate from BigQuery EU multi-region or vice-versa| From EU multi-region to europe-west4 (Netherlands), europe-west4 (Netherlands) to EU multi-region| Free  
Replicate from BigQuery EU multi-region to any other region not in EU multi-region| From EU multi-region to any region (except europe-west4 (Netherlands))| See following table  
Replicate across locations| From us-east1 to us-central1| See following table  
  
**Note:** All prices are in $/GiB and all GiB are in physical bytes.

| North America| Europe| Asia| Indonesia| Oceania| Middle East| Latin America| Africa  
---|---|---|---|---|---|---|---|---  
**North America**|  $0.02| $0.05| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Europe**|  $0.05| $0.02| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Asia**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Indonesia**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Oceania ﻿**| $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Middle East**|  $0.11| $0.11| $0.11| $0.11| $0.11| $0.08| $0.14| $0.11  
**Latin America**|  $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.20| $0.14  
**Africa**|  $0.11| $0.11| $0.11| $0.14| $0.14| $0.11| $0.14| $0.11  
  
## 

Notebook runtime pricing

BigQuery Studio Notebooks rely on a default notebook runtime that uses a [Colab Enterprise runtime](https://cloud.google.com/colab/docs/runtimes) to enable notebook code execution. The default Colab Enterprise runtime consumes compute and disk (both SSD and PD) resources.

Billing for these resources is metered as pay-as-you go slots as outlined below. These slots are billed under the [BigQuery Standard Edition SKU](https://cloud.google.com/skus/sku-groups/bigquery-standard-edition-payg).

Notebooks that use a non-default runtime are billed under Gemini platform SKUs.

The default notebook runtime is a Google-provisioned virtual machine (VM) that can run the code in your notebook (IPYNB file). This allows BigQuery customers to execute python script and is not charged after idle time.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Sao Paulo (southamerica-east1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Las Vegas (us-west4)



Show discount options

HourlyHourly

MonthlyMonthly

Resource| Pricing (USD)  
---|---  
Default notebook runtime compute| $0.160827408 / 1 hour| $0.14474466 / 1 hour| $0.128661928 / 1 hour  
  
*The Pay as you go slots, will be metered in the edition that is being used at the project level.

The default notebook allocates PD and SSD in the background to help users install new data science packages and maintain their work beyond the Python code they execute. Once the PD and SSD is released, you will not see charges.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Sao Paulo (southamerica-east1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Las Vegas (us-west4)



HourlyHourly

MonthlyMonthly

Resource| Pricing (USD)  
---|---  
Default notebook SSD| $0.000279452 / 1 gibibyte hour  
Default notebook PD| $0.000065753 / 1 gibibyte hour  
  
BigQuery Studio notebook pricing details:

  * Default runtime configuration may change to improve usability. Details can be found [here](https://cloud.google.com/colab/docs/runtimes#default-runtime).
  * Colab Enterprise runtimes shut down after 180 minutes of inactivity by default. [This page](https://cloud.google.com/colab/docs/idle-shutdown) describes the idle shutdown feature and how to change the default idle shutdown settings or turn the feature off when you create a runtime template.



## 

BigQuery ML pricing

BigQuery ML [models](https://cloud.google.com/bigquery/docs/bigqueryml-intro#overview) can be classified into two different categories: built-in models and external models. BigQuery ML built-in models are trained within BigQuery, such as linear regression, logistic regression, k-means, matrix factorization, PCA, and ARIMA models. The pre trained TimesFM model is also considered a built-in model. BigQuery ML external models are trained utilizing other Google Cloud services, DNN, boosted tree and random forest (which are trained on [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)) and AutoML models (which are trained on the [Gemini platform tables backend](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/overview)). BigQuery ML model training pricing is based on the model type and your usage pattern, as well as your pricing model: editions or on-demand. BigQuery ML prediction and evaluation functions are executed within BigQuery ML for all model types, priced as explained below.

### 

BigQuery ML editions pricing

BigQuery ML is available in Enterprise and Enterprise Plus Editions for customers who prefer a compute capacity (number of slots) based pricing model over the on-demand (number of bytes processed) model. Customers can use Enterprise or Enterprise Plus reservations to use all features of BigQuery ML. BigQuery ML usage will be included in the BigQuery Editions usage.

  


Reservations to create built-in models

BigQuery has three job types for reservation assignment: QUERY, PIPELINE, and ML_EXTERNAL. QUERY assignments, which are used for analytical queries, are also used to run CREATE MODEL queries for BigQuery ML built-in models. Built-in model training and analytical queries share the same pool of resources in their assigned reservations, and have the same behavior regarding being preemptible, and using idle slots from other reservations.

  


Reservations to create external models

Because external models are trained outside of BigQuery, these workloads are not preemptible. As a result, to ensure other workloads are not impacted, only reservations with ML_EXTERNAL job type assignment can be used for these external jobs. [Reservations workload management](https://cloud.google.com/bigquery/docs/reservations-workload-management) describes how to create reservations for external model training jobs. The slots usage per job is calculated to maintain the price parity between BigQuery slots and external Google Cloud service costs.

**Note:** You can add a **ML_EXTERNAL** job type assignment to reservations that you want to use for building BigQuery ML external models. When slots in the reservation are shared by both **QUERY** /**PIPELINE** and **ML_EXTERNAL** jobs, **QUERY** /**PIPELINE** jobs can use the slots only when they are available. Thus, it is important to ensure all critical **QUERY** and **PIPELINE** jobs run in their own reservations, as **ML_EXTERNAL** jobs are not preemptible. **ML_EXTERNAL** jobs cannot use idle slots from other reservations. On the other hand, if slots in this reservation (with **ML_EXTERNAL** assignment) are available, jobs from other reservations (with ignore_idle_slots=false) can use them.

**Note:** To create an AutoML Tables model, you need approximately 1000 **ML_EXTERNAL** slots. The number of slots is subject to change based on [Gemini platform tables backend](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/classification-regression/overview) pricing. Meanwhile, the number of external slots used to train other BigQuery ML external models (such as DNN, Boosted Tree, Random Forest etc.) is dynamically determined in order to scale the training job horizontally. More specifically, the Gemini platform training scale tier (Virtual Machine configurations for chief worker, parameter servers and workers) is determined at runtime based on the training data size and model type. The BigQuery ML service then reserves a number of slots equivalent to the total VM price from your **ML_EXTERNAL** reservations.

### 

BigQuery ML on-demand pricing﻿

BigQuery ML pricing for on-demand queries depends on the type of operation: model type, model creation, model evaluation, model inspection, or model prediction. For the models that support it, hyperparameter tuning is billed at the same rate as model creation. The cost of the model training associated with hyperparameter tuning is the sum of the cost of all executed trials.

**Note:** Matrix factorization models are only available to editions customers or customers with [reservations](https://cloud.google.com/bigquery/docs/reservations-intro).

BigQuery ML on-demand pricing is as follows:

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Operation| Pricing| Details  
---|---|---  
Logistic regression model creation1Linear regression model creation1K-means clustering model creation1PCA model creationTime series model creation1,2﻿Contribution analysis model creation| $312.50 / 1 tebibyte, per 1 month / account| An additional label is added to the billing record to distinguish between BigQuery ML model creation and regular BigQuery costs.The key is bigquery.googleapis.com/bqml, and the value can be one of the following:

  * bqml_linear_reg_training
  * bqml_logistic_reg_training
  * bqml_kmeans_training
  * bqml_pca_training
  * bqml_matrix_factorization_training
  * bqml_arima_plus_training
  * bqml_arima_plus_xreg_training
  * bqml_contribution_analysis_training

  
AutoML Tables model creation1DNN model creation1Wide-and-Deep model creation1Boosted tree model creationRandom forest model creationAutoencoder model creation1| $6.25 / 1 tebibyte, per 1 month / account| The total cost of a job is the sum of the following two costs:

  * BigQuery data processing cost (for preprocessing)
  * Passthrough Gemini platform cost (for training)

The cost is converted to BigQuery ML bytes processed, and two billing records with different labels are reported for the job:For BigQuery cost, the key is bigquery.googleapis.com/bqml and the value is bqml_analytic. For external Gemini platform service costs, the key is bigquery.googleapis.com/bqml, and the value can be one of the following: 1) CAIP; 2) AUTOML_TABLES.  
Matrix factorization model creation| Not supported| Matrix factorization is only available to editions customers or customers with [reservations ](https://cloud.google.com/bigquery/docs/reservations-intro)(Enterprise or Enterprise+).  
Evaluation, inspection, and prediction (all model types except remote model3)| $6.25 / 1 tebibyte, per 1 month / account| Charges from evaluation, inspection, and prediction queries are included in the 1 TiB of data per month under the BigQuery analysis free tier.  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

1The **CREATE MODEL** statement stops at 50 iterations for iterative models. This applies to both on-demand and editions pricing.

2For time series models, when auto-arima is enabled for automatic hyper-parameter tuning, multiple candidate models are fitted and evaluated during the training phase. In this case, the number of bytes processed by the input **SELECT** statement is multiplied by the number of candidate models, which can be controlled by the [AUTO_ARIMA_MAX_ORDER ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-time-series#auto_arima_max_order)training option for **ARIMA_PLUS** or the [AUTO_ARIMA_MAX_ORDER ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series#auto_arima_max_order)training option for **ARIMA_PLUS_XREG**. This applies to both on-demand and editions pricing. The following notes apply to time series model creation:

  * For single time series forecasting with auto-arima enabled, when **AUTO_ARIMA_MAX_ORDER** is (1, 2, 3, 4, 5), the number of candidate models is (6, 12, 20, 30, 42) respectively if non-seasonal  _d_ equals one; otherwise, the number of candidate models is (3, 6, 10, 15, 21).
  * For multiple time series forecasting using **TIME_SERIES_ID_COL** , the charge is for (6, 12, 20, 30, 42) candidate models when **AUTO_ARIMA_MAX_ORDER** is (1, 2, 3, 4, 5) respectively.
  * Note that this model selection only applies to model creation. For model evaluation, inspection, and prediction, only the selected model is used, with regular query pricing.



3See BigQuery ML Remote Model Inference for details.

### 

TabFM on BigQuery

TabFM on BigQuery will be moving to a token based pricing from 10/30/2026 onwards, whereby you will be charged for TabFM tokens consumed in your query and for BigQuery slot used/bytes processed for non model inference parts of the query.

TabFM on BigQuery token computation and pricing is as follows:

**Input tokens =** (train rows * columns + predict rows * (columns - 1)) * n_ensembles

**Output tokens =** prediction rows * n_ensembles

Where:

  * train_row is the number of input training rows
  * prediction_row is the number of rows to predict label
  * columns is the number of feature columns and target label column referenced
  * n_ensemble is the number of differently shuffled versions of data the model predicts on and averages to get a more accurate prediction



Item| Price (USD)  
---|---  
Input tokens| $0.05 / mtok  
Output tokens| $0.20 / mtok  
  
### 

TimesFM 3.0 on BigQuery

TimesFM 3.0 on BigQuery will be moving to a token-based pricing from [Target Enforcement Date, 12/01/2026] onwards, whereby you will be charged for TimesFM 3.0 tokens consumed in your query and for BigQuery slots used/bytes processed for non-model inference parts of the query. (During Preview prior to token billing enforcement, usage is billed in standard BigQuery slots for Enterprise/Enterprise Plus editions or bytes processed for on-demand mode.)

TimesFM 3.0 on BigQuery token computation and pricing is as follows (each data point equals 1 token):

**Input tokens =** S * (L * (N_target + N_past_cov) + (L + H) * N_fut_cov)

**Output tokens =** S * H * (N_target + N_past_cov)

Where:

  * **S** is the number of time series (entities / batches)
  * **L** is the history context length (number of past time steps)
  * **H** is the forecast horizon length (number of future time steps)
  * **N_target** is the number of target columns
  * **N_past_cov** is the number of past-only covariate columns
  * **N_fut_cov** is the number of past and future covariate columns



Item| Price (USD)  
---|---  
Input tokens| $0.05 / mtok  
Output tokens| $0.20 / mtok  
  
### 

BigQuery ML remote model training, inference, and tuning

BigQuery ML lets customers create a remote model that targets a [Gemini platform foundation model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models#foundation_model_apis), a Gemini platform online prediction endpoint, or a Cloud AI API, for example Cloud AI Vision API.

The pricing for BigQuery ML remote model inference has the following parts:

  1. The bytes processed by BigQuery are billed according to standard pricing such as on-demand or editions pricing.
  2. In addition, costs are incurred for the remote endpoint as follows:



Remote Model types| Inference functions| Pricing  
---|---|---  
Google models hosted on Gemini platform| **ML.GENERATE_TEXT****ML.GENERATE_EMBEDDING**| [Generative AI in Gemini platform batch pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).  
Anthropic's Claude models on Google Cloud| **ML.GENERATE_TEXT**| [Generative AI in Gemini platform pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#claude-models)  
Open models deployed to Gemini platform| **ML.GENERATE_TEXT**| [Gemini platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)  
Gemini platform endpoints| **ML.PREDICT**| [Gemini platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)  
Cloud Natural Language API| **ML.UNDERSTAND_TEXT**| [Cloud Natural Language API pricing](https://cloud.google.com/natural-language/pricing)  
Cloud Translation API| **ML.TRANSLATE ﻿**| [Cloud Translation API pricing](https://cloud.google.com/translate/pricing)  
Cloud Vision API| **ML.ANNOTATE_IMAGE**| [Cloud Vision API pricing](https://cloud.google.com/vision/pricing)  
Document AI API| **ML.PROCESS_DOCUMENT**| [Document AI API pricing](https://cloud.google.com/vision/pricing)  
Speech-to-Text API| **ML.TRANSCRIBE**| [Speech-to-Text API pricing](https://cloud.google.com/speech-to-text/pricing)  
  
For remote endpoint model pricing, you are billed directly by the above services. You may use the billing label billing_service = 'bigquery_ml' and the billing label bigquery_job_id_prefix to filter the exact charges.

### 

LLM supervised tuning costs﻿

When using supervised tuning with remote models over Gemini platform LLMs, costs are calculated based on the following:

  * The bytes processed from the training data table specified in the [AS SELECT clause](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model#as_select). These charges are billed from BigQuery to your project.
  * The GPU or TPU usage to tune the LLM. These charges are billed from Gemini platform to your project. For more information, see [Gemini platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#custom-trained_models).



### 

BigQuery ML dry run﻿

Due to the nature of the underlying algorithms of some model types and differences in billing, the bytes processed will not be calculated for some model types until after training is completed due to the complexity of calculating the initial estimate.

### 

BigQuery ML pricing example﻿

BigQuery ML charges are not itemized separately on your billing statement. For current models, if you have BigQuery Editions, BigQuery ML charges are included.

If you are using [on-demand](https://docs.cloud.google.com/bigquery/pricing#bigquery-ml-pricing) pricing, BigQuery ML charges are included in the BigQuery analysis (query) charges.

BigQuery ML jobs that perform inspection, evaluation, and prediction operations incur the same charges as on-demand query jobs. Because CREATE MODEL queries incur different charges, you must calculate CREATE MODEL job costs independently by using the Cloud logging audit logs. Using the audit logs, you can determine the bytes billed by the BigQuery ML service for each BigQuery ML CREATE MODEL job. Then, multiply the bytes billed by the appropriate cost for CREATE MODEL queries in your regional or multi-regional location.

For example, to determine the cost of a query job in the US that includes a BigQuery ML CREATE MODEL statement:

  * Open the [Cloud Logging](https://console.cloud.google.com/logs/query) page in the Google Cloud console.
  * Verify that the product is set to BigQuery.
  * Click the drop-down arrow in the "Filter by label or text search" box and choose **Convert to advanced filter**. This adds the following text to the filter:



  * 


Loading...

resource.type = "bigquery_resource"

_content_copy_

  * Add the following text on line two below the resource.type line:



  * 


Loading...

protoPayload.serviceData.jobCompletedEvent.job.jobConfiguration.query.statementType="CREATE_MODEL"

_content_copy_

  * To the right of the **Submit Filter** button, choose the appropriate time frame from the drop-down list. For example, choosing **Last 24 hours** would display BigQuery ML CREATE MODEL jobs completed in the past 24 hours.
  * Click **Submit Filter** to display the jobs completed in the given time window.
  * After the data is populated, click **View Options** and choose **Modify custom fields**.
  * In the **Add custom fields** dialog, enter:



  * 


Loading...

protoPayload.serviceData.jobCompletedEvent.job.jobStatistics.totalBilledBytes

 _content_copy_

  * Click **Save** to update the results.
  * To calculate the charges for the BigQuery ML CREATE MODEL job, multiply the bytes billed by the [BigQuery ML on-demand price](https://docs.cloud.google.com/bigquery/pricing#bigquery-ml-pricing). In this example, the CREATE MODEL job processed 100873011200 bytes. To calculate the cost of this job in the US multi-regional location, divide the billed bytes by the number of bytes per TiB, and multiply it by the model creation cost:



100873011200 / 1099511627776 x $312.5 = $28.669

**Note:** Currently, Cloud logging metrics are not available for BigQuery ML. When available, Cloud logging metrics will allow you to view BigQuery ML bytes billed in graphs with custom aggregations.

## 

BI Engine pricing

[BI Engine](https://cloud.google.com/bigquery/docs/bi-engine-intro) accelerates SQL queries by caching BigQuery data in memory. The amount of data stored is constrained by the amount of capacity you purchase. To purchase BI Engine capacity, create a BI Engine reservation in the project where queries will be run.

When BI Engine accelerates a query, the query stage that reads table data is free. Subsequent stages depend on the type of BigQuery pricing you're using:

  * For [on-demand pricing](https://docs.cloud.google.com/bigquery/pricing#bigquery-ml-pricing), stages that use BI Engine are charged for 0 scanned bytes. Subsequent stages will not incur additional on-demand charges.
  * For [editions pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing), the first stage consumes no BigQuery reservation slots. Subsequent stages use slots from the BigQuery reservation.



BI Engine pricing is as follows:

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Resource| Pricing| Details  
---|---|---  
Memory capacity| $0.0416 / 1 gibibyte hour| You are charged per GiB/hour for each project in which you have [reserved capacity](https://cloud.google.com/bigquery/docs/bi-engine-reserve-capacity).  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Editions commitment bundle

When you are using BigQuery [capacity compute pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing) with BigQuery editions commitments, you are eligible to receive a limited amount of BI Engine capacity as part of your editions price, at no extra cost, as shown in the following chart. To receive BI Engine capacity at no additional cost, follow the instructions to [reserve capacity](https://cloud.google.com/bigquery/docs/bi-engine-reserve-capacity) in a project within the same organization as your editions reservation. To ensure a particular project’s BI Engine reservation is discounted toward this bundled capacity, there should be some slots assigned to the project. BI Engine reservation in an 'on-demand analysis' project will not be counted towards the free capacity. Free capacity is shown in your Billing Reports as a normal cost, but it is discounted as a "Spending-Based Discount".

Number of slots purchased| No-cost, additional BI Engine capacity (GiB)  
---|---  
100| 5  
500| 25  
1000| 50  
1500| 75  
2000| 100 (maximum per organization)  
  
## 

Free operations

The following BigQuery operations are free of charge in every location. [Quotas and limits](https://cloud.google.com/bigquery/quotas) apply to these operations.

If you are copying tables across regions, you are charged for [data replication](https://docs.cloud.google.com/bigquery/pricing#data-replication-pricing).

Operation| Details  
---|---  
Batch load data| You are not charged for batch loading data using the shared slot pool. You can also create a reservation using [editions pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing) for guaranteed capacity. Once the data is loaded into BigQuery, you are charged for storage. For details, see [Batch loading data](https://cloud.google.com/bigquery/docs/batch-loading-data).  
Copy data| You are not charged for copying a table, but you do incur charges for storing the new table. For more information, see [Copying an existing table](https://cloud.google.com/bigquery/docs/managing-tables#copy-table).  
Export data| You are not charged for exporting data using the shared slot pool, but you do incur charges for storing the data in Cloud Storage. You can also create a reservation using [editions pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing) for guaranteed capacity. When you use the [EXPORT DATA SQL statement](https://cloud.google.com/bigquery/docs/reference/standard-sql/export-statements#export_data_statement), you are charged for query processing. For details, see [Exporting data](https://docs.cloud.google.com/bigquery/pricing#exporting_data).  
Delete operations| You are not charged for deleting datasets or tables, deleting individual table partitions, deleting views, or deleting user-defined functions.  
  
## 

Free usage tier

As part of the [Google Cloud Free Tier](https://cloud.google.com/free), BigQuery offers some resources free of charge up to a specific limit. These free usage limits are available during and after the free trial period. If you go over these usage limits and are no longer in the free trial period, you will be charged according to the pricing on this page. You can try BigQuery's free tier in the [BigQuery sandbox](https://cloud.google.com/bigquery/docs/sandbox) without a credit card.

Resource| Monthly free usage limits| Details  
---|---|---  
Storage| The first 10 GiB per month is free.| BigQuery ML models and training data stored in BigQuery are included in the BigQuery storage free tier.  
Queries (analysis)| The first 1 TiB of query data processed per month is free.| BigQuery [Editions pricing](https://docs.cloud.google.com/bigquery/pricing#capacity-compute-pricing) is also available for high-volume customers that prefer a stable, monthly cost.  
  
## 

Flat-rate pricing

**Note:** The BigQuery flat-rate pricing model is no longer offered as of July 5, 2023. It is described here for customers who have existing flat-rate commitments

### 

Flat-rate compute pricing

When you use the flat-rate compute pricing model, you purchase dedicated query processing capacity, measured in BigQuery [slots](https://cloud.google.com/bigquery/docs/slots). Your queries consume this capacity, and you are not billed for bytes processed. If your capacity demands exceed your committed capacity, BigQuery will queue up queries, and you will not be charged additional fees.

Flat-rate compute pricing:

  * Applies to query costs, including BigQuery ML, DML, and DDL statements.
  * Does not apply to [storage costs](https://docs.cloud.google.com/bigquery/pricing#storage-pricing) or BI Engine costs.
  * Does not apply to streaming inserts and using the BigQuery Storage API.
  * Is purchased as a regional resource. Slot [commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments) purchased in one region or multi-region cannot be used in another region or multi-region and cannot be moved.
  * Is available in per-second (flex), monthly, and annual commitments.
  * Can be shared across your entire organization. There is no need to buy slot [commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments) for every project.
  * Has a 100-slot minimum and is purchased in increments of 100 slots.
  * Is billed per second until you cancel the commitment, which can be done at any time after the commitment end date.



### 

Monthly flat-rate commitments

The following table shows the cost of your monthly flat-rate slot commitment. For more information, see [Monthly commitments](https://cloud.google.com/bigquery/docs/reservations-details#monthly_commitments).

Iowa (us-central1)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)
  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $2.739726027 / 1 hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Annual flat-rate commitments

The following table shows the cost of your annual flate-rate slot commitment. For more information, see [Annual commitments](https://cloud.google.com/bigquery/docs/reservations-details#annual_commitments).

Iowa (us-central1)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)
  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $2.328767123 / 1 hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Flex slots: short-term flat-rate commitments

Flex slots are a special commitment type:

  * Commitment duration is only 60 seconds.
  * You can cancel flex slots any time thereafter.
  * You are charged only for the seconds your commitment was deployed.



Flex slots are subject to capacity availability. When you attempt to purchase flex slots, success of this purchase is not guaranteed. However, once your commitment purchase is successful, your capacity is guaranteed until you cancel it. For more information, see [flex slots](https://cloud.google.com/bigquery/docs/reservations-details#flex_slots).

The following table shows the cost of your Flex slot commitment.

Iowa (us-central1)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)
  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Europe (eu)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * US (us)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $4.00 / 1 hour  
  
### 

BigQuery Omni flat-rate pricing

BigQuery Omni offers flat-rate pricing which provides a predictable cost for queries. To enable flat-rate pricing, use BigQuery Reservations.

When you enroll in flat-rate pricing for BigQuery Omni, you purchase dedicated query processing capacity, measured in slots, on Amazon Web Services or Microsoft Azure. Your queries consume this capacity, and you are not billed for bytes processed.

BigQuery Omni flat-rate pricing:

  * Applies to query costs. Does not apply to [storage costs](https://docs.cloud.google.com/bigquery/pricing#storage-pricing).
  * Slot [commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments) are purchased for a single multi-cloud region. Slots purchased in one region cannot be used in another region.
  * Is available in monthly, and annual commitments. Is billed per second until you cancel the commitment, which can be done at any time after the commitment end date.
  * Can be shared across your entire organization. There is no need to buy slot [commitments](https://cloud.google.com/bigquery/docs/reservations-intro#commitments) for every project.
  * Has a 100-slot minimum and is purchased in increments of 100 slots.



### 

Monthly flat-rate commitments

The following table shows the cost of your monthly slot commitment. For more information, see [Monthly commitments](https://cloud.google.com/bigquery/docs/reservations-details#monthly_commitments).

Seoul (AWS) (aws-ap-northeast-2)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $3.424657534 / 1 hour  
  
### 

Annual flat-rate commitments

The following table shows the cost of your annual slot commitment. For more information, see [Annual commitments](https://cloud.google.com/bigquery/docs/reservations-details#annual_commitments).

Seoul (AWS) (aws-ap-northeast-2)

  * Seoul (AWS) (aws-ap-northeast-2)
  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $2.910958904 / 1 hour  
  
### 

Flex slots: short-term commitments

Flex slots are a special commitment type:

  * Commitment duration is only 60 seconds.
  * You can cancel flex slots any time thereafter.
  * You are charged only for the seconds your commitment was deployed.



Flex slots on BigQuery Omni are subject to capacity availability on AWS or Azure. When you attempt to purchase flex slots, success of this purchase is not guaranteed. However, once your commitment purchase is successful, your capacity is guaranteed until you cancel it. For more information, see [flex slots](https://cloud.google.com/bigquery/docs/reservations-details#flex_slots).

The following table shows the cost of your Flex slot commitment.

Northern Virginia (AWS) (aws-us-east-1)

  * Northern Virginia (AWS) (aws-us-east-1)
  * Virginia (Azure) (azure-us-east2)



HourlyHourly

MonthlyMonthly

Number of slots| Cost  
---|---  
100| $5.00 / 1 hour  
  
### 

BI Engine flat-rate commitment bundle

When you are using BigQuery flat-rate slot commitments, you are eligible to receive a limited amount of BI Engine capacity as part of your flat-rate price, at no extra cost, as shown in the following chart. To receive BI Engine capacity at no additional cost, follow the instructions to [reserve capacity](https://cloud.google.com/bigquery/docs/bi-engine-reserve-capacity) in a project within the same organization as your flat-rate reservation. To ensure a particular project's BI Engine reservation is discounted toward this bundled capacity, there should be some slots assigned to the project. A BI Engine reservation in an on-demand compute project don't counted towards free capacity. Free capacity is shown in your [billing reports](https://cloud.google.com/billing/docs/reports) as a normal cost, but it is discounted as a "Spending-Based Discount".

Number of slots purchased| No-cost, additional BI Engine capacity (GiB)  
---|---  
100| 5  
500| 25  
1000| 50  
1500| 75  
2000| 100 (maximum per organization)  
  
## What's next

  * For information on analyzing billing data using reports, see [View your billing reports and cost trends](https://cloud.google.com/billing/docs/how-to/reports).
  * For information on analyzing your billing data in BigQuery, see [Export Cloud Billing data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * For information about estimating costs, see [Estimating storage and query costs](https://cloud.google.com/bigquery/docs/estimate-costs).
  * Read the [BigQuery documentation](https://cloud.google.com/bigquery/docs).
  * Get started with [BigQuery](https://cloud.google.com/bigquery/docs/quickstarts).
  * Try the [Pricing calculator](https://cloud.google.com/products/calculator).
  * Learn about [BigQuery solutions and use cases](https://cloud.google.com/architecture?text=BigQuery).



## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

Contact sales[](https://cloud.google.com/contact?direct=true)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact)



 _search_ _send_




[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/bigquery/pricing&hl=en-US&prompt=select_account&service=cloudconsole)

Start free[](https://console.cloud.google.com/freetrial)

Start free[](https://console.cloud.google.com/freetrial)

Contact us[](https://cloud.google.com/contact)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)




  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)




  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)




  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)




close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure Modernization
  * Productivity and Collaboration
  * Security
  * Startups and SMB



See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)


  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)


  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)


  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)


  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)


  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)


  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)


  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)


  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)


  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)


  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)


  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)


  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationModernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Application Modernization with AIAI-assisted code refactoring, assessment, and transformation for legacy applications.](https://cloud.google.com/solutions/application-modernization-with-ai)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Mainframe ModernizationAutomated tools and AI-driven guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)


  * [Database ModernizationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Data Lake ModernizationUnify and govern multimodal data on an open, high-performance cloud data lake.](https://cloud.google.com/solutions/data-lakehouse)


  * [Data Warehouse ModernizationMigrate and modernize your enterprise data warehouse for serverless analytics and AI.](https://cloud.google.com/solutions/data-migration)


  * [APIsUnlock legacy applications and build new digital channels using APIs and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [Platform EngManaged services and golden paths to build, manage, and scale internal developer platforms.](https://cloud.google.com/solutions/platform-engineering)


  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)


  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Gemini for enterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)


  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)


  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)


  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)


  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)


  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)


  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)


  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)


  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)


  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)


  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)


  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)


  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)


  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)


  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)


  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)


  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)


  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)


  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)


  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Rapid Migration and Modernization Program (RaMP)End-to-end migration program to simplify and accelerate your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Data Center ExitsMigration solutions for moving VMs, apps, databases, and workloads out of data centers.](https://cloud.google.com/solutions/data-center-migration)


  * [Application Modernization & MigrationDiscovery, assessment, and migration tools for moving and modernizing applications.](https://cloud.google.com/solutions/application-migration)


  * [Database Modernization & MigrationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Cross-Cloud NetworkingSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)


  * [High Performance Computing (HPC)Compute, storage, and networking options to support any high-performance workload.](https://cloud.google.com/solutions/hpc)


  * [VMwareFully managed, native VMware Cloud Foundation software stack on Google Cloud.](https://cloud.google.com/vmware-engine)


  * [SAPCertified infrastructure and AI solutions for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)


  * [WindowsTools, licenses, and partner solutions for running enterprise Windows workloads.](https://cloud.google.com/windows)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)


  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)


  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)


  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)


  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)


  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)


  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)


  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)


  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)


  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)


  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)


  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)



close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3



See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)


  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)


  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)


  * [Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)


  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)


  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)


  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)


  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)


  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)


  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)


  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)



  * Business Intelligence


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)


  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)


  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)


  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)


  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)


  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)


  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)


  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)


  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)


  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)


  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)


  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)


  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)


  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)


  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)


  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)


  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)


  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)


  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)


  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)


  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)


  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)


  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)


  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)


  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)


  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)


  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)



  * Hybrid and Multicloud


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)


  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)


  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)



  * Industry Specific


  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)


  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)


  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)


  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)


  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)


  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)


  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)


  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)


  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)


  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)


  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)


  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)


  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)


  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)


  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)


  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)


  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)


  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)



  * Media Services


  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)


  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)


  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)


  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)


  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)


  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)


  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)


  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)


  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)


  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)


  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)


  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)


  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)


  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)


  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)


  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)


  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)


  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)


  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)


  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)


  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)


  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)


  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)


  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)


  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)


  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)



  * Productivity and Collaboration


  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)


  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)


  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)


  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)


  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)


  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)


  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)


  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)


  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)


  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)


  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)


  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)


  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)


  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)


  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)


  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)


  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)


  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)


  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)


  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)


  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)



close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)




  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)




  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)




  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)




close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)




  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)




  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)




  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)




close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
    * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
    * arrow_forward
  * [Products](https://cloud.google.com/products)
    * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
    * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
    * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)



  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)


  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Application Modernization with AI](https://cloud.google.com/solutions/application-modernization-with-ai)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Mainframe Modernization](https://cloud.google.com/solutions/mainframe-modernization)
  * [Database Modernization](https://cloud.google.com/products/databases)
  * [Data Lake Modernization](https://cloud.google.com/solutions/data-lakehouse)
  * [Data Warehouse Modernization](https://cloud.google.com/solutions/data-migration)
  * [APIs](https://cloud.google.com/solutions/apis-and-applications)
  * [Platform Eng](https://cloud.google.com/solutions/platform-engineering)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini for enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Rapid Migration and Modernization Program (RaMP)](https://cloud.google.com/solutions/cloud-migration-program)
  * [Data Center Exits](https://cloud.google.com/solutions/data-center-migration)
  * [Application Modernization & Migration](https://cloud.google.com/solutions/application-migration)
  * [Database Modernization & Migration](https://cloud.google.com/products/databases)
  * [Cross-Cloud Networking](https://cloud.google.com/solutions/cross-cloud-network)
  * [High Performance Computing (HPC)](https://cloud.google.com/solutions/hpc)
  * [VMware](https://cloud.google.com/vmware-engine)
  * [SAP](https://cloud.google.com/solutions/sap)
  * [Windows](https://cloud.google.com/windows)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)


  * Featured Products
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)


  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)


  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)


