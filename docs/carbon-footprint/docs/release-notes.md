---
url: https://docs.cloud.google.com/carbon-footprint/docs/release-notes/
title: Carbon Footprint release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:14.474493+00:00
---

# Carbon Footprint release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback 

#  Carbon Footprint release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Carbon Footprint. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/carbon-footprint-release-notes.xml) directly. 

## September 15, 2026

Change

For the July 2026 data release (published mid-September 2026), we have upgraded the carbon model to version 17 and implemented the following updates:

**Updating Scope 1 & 3 Emissions from Google's Corporate Footprint**

  * Allocation factor refresh: Updated Scope 1 and Scope 3 allocation factors using company-wide data from the [2026 Google Environmental Report](https://sustainability.google/google-2026-environmental-report/).
  * Methodology application: For details on how corporate Scope 1 and Scope 3 emissions are distributed across cloud products and services, refer to the [non-electricity emission sources section of the methodology documentation](https://docs.cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation).



**Updating Inputs for Scope 2 Market-Based Emissions Calculations**

  * Updated annual renewable electricity allocation percentages in accordance with the [2026 Google Environmental Report](https://sustainability.google/google-2026-environmental-report/).
  * Refreshed background annual emissions factors using updated government data sources across Scope 1, Scope 2, and Scope 3. Note that Scope 2 location-based emissions continue to be calculated using hourly greenhouse gas emission factors. Learn more in the[ Scope 2 market-based allocation documentation](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation).
  * Incorporated marketplace purchases of Granular Certificates covering a significant portion of electricity load across carbon-intensive regions.
  * Granular certificate purchases represent market-based accounting allocations. Customers seeking to minimize emissions are encouraged to prioritize [regions with high Carbon Free Energy](https://cloud.google.com/sustainability/region-carbon#data) (CFE) scores for new workloads.



**Regional Accounting & Boundary Updates**

  * Aligned European clean energy matching boundaries with updated [RE100](https://www.theclimategroup.org/hubfs/RE100/PDFs/RE100%20technical%20criteria%20+%20appendices%20\(15%20April%202025\).pdf#page=28) criteria.
  * Corrected country mapping configurations in annual emission factor scripts to resolve historical data discrepancies across select Asian market regions (e.g., asia-east2, asia-northeast3).



To correct your July emissions data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#bq_8) for the month.

## August 14, 2026

Announcement

As detailed in our [2026 Environmental Report (p. 22)](https://storage.googleapis.com/gweb-mobius-cdn/sustainability/uploads/21455428735c7305f2cb5c0038fc14bb0803abb8.pdf#page=22), Google is now using Granular Certificates purchased from the marketplace to strategically match more of our load on an hourly basis. To accurately incorporate these certificates into the Cloud customers' allocation of carbon intensity calculations, the July 2026 semi-annual [methodology refresh](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation) will be delayed by one month. We will provide further updates once the revised data is available.

## February 27, 2026

Feature

The improved data export experience in the Cloud Carbon console is now available in **Public Preview**.

This feature, previously in Experimental Preview, lets you view the Carbon Footprint exports for a given billing account directly in the Cloud Carbon console. Only exports that you have permission to view are shown. You can use this view to better manage your Carbon Footprint exports in BigQuery.

## February 15, 2026

Feature

**Methodology update** : Starting with January 2026 data, we have updated our calculation model to align with the comprehensive AI energy/emissions framework detailed in [Measuring the environmental impact of delivering AI at Google Scale](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference). This update allocates previously unallocated AI inference model emissions to the associated Google Cloud services, following the SKU-level allocation described in the [Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology). This change is part of our ongoing effort to provide more accurate and transparent emissions data for AI inference.

**Impact** : Customers will see an increase in reported emissions for services that utilize AI model inference across all SKUs. Such an increase is spread across all SKUs within those services, based on the SKU-level allocation [methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology#sku-allocation). The primary impact is on Vertex AI. Other impacted services include Video Stitcher API, Notebooks, Cloud Natural Language, Cloud Speech API, Cloud Document AI API, Cloud Dialogflow API, Cloud Machine Learning Engine, Cloud Text-to-Speech API and Cloud Vision API.

## January 30, 2026

Fixed

We have corrected the issue resulting in incomplete Cloud Run emissions data for November and December 2025. Customers who used Cloud Run during this period can now access the corrected data.

**Action Required** : To see the corrected Cloud Run emissions data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for November and December 2025. Note that there is a half-month lag of our data release. For example, to backfill November and December 2025 data, run the backfill for December 15, 2025 and January 15, 2026, which will update the data for November and December 2025 in your BigQuery table.

## January 01, 2026

Issue

We have identified an issue resulting in incomplete Cloud Run emissions data for November and December 2025. Customers may observe lower than actual emissions for Cloud Run during this period. We are actively working on a fix and will provide an update when the data correction is available.

## October 01, 2025

Feature

Cloud Carbon Footprint launched an improved data export experience in the Cloud Carbon console, now available in Experimental Preview. 

When you click **Data export** on the Cloud Carbon console Ul for a given billing account, you can now see Carbon Footprint exports that you have access to for that billing account, in addition to the ability to create a new data export. This feature helps you better manage your Carbon Footprint exports in BigQuery. [Read more](https://cloud.google.com/carbon-footprint/docs/export#manage) for details.

In some cases, the list of exports may not be complete for the following reasons:

  * **Permissions** : The export was configured in a project that you don't have permission to view.
  * **Performance Optimization** : To optimize performance and prevent latency when you have access to a very large number of projects, the search may not display exports in all projects.



## September 12, 2025

Fixed

We have corrected an issue affecting the market-based Scope 2 emissions for the europe-west2 (London) region in the July 2025 Carbon Footprint data.

In the [July 2025 methodology update](https://docs.cloud.google.com/carbon-footprint/docs/release-notes#August_14_2025), renewable energy coverage was misapplied to the Scope 2 market-based emissions in the europe-west2 (London) region. This resulted in non-zero Scope 2 market-based emissions for europe-west2. This inconsistency arose from evolving RE100 market-boundary guidance following Brexit. While RE100 guidance excludes the UK from the EU market-boundary post-Brexit, it allows for the use of previously purchased EU energy attribute certificates (EACs) with sufficiently close vintages to be applied against UK consumption in 2024. Google's application of these EACs to UK consumption results in zero Scope 2 market-based emissions in the europe-west2 (London). 

We have corrected our data to align with the RE100 market boundaries guidance and our corporate environmental reporting of matched renewable energy. Scope 2 market-based emissions for europe-west2 are now correctly reported as zero for July 2025, using 2024 renewable energy coverage consistent with Google's environmental report.

  * To correct your historical data, please [run a backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for July 2025 in your carbon footprint export. Due to a half-month lag in our data release, you will need to backfill the data for August 15, 2025, which will then update the July 2025 data in your BigQuery table.



Data for August 2025, available on September 15, 2025, will automatically reflect this correction. Data for all previous periods remains unaffected.

## September 03, 2025

Announcement

We recently released a new technical paper, ["Measuring the Environmental Impact of Delivering AI at Google Scale"](https://arxiv.org/abs/2508.15734) and [blogpost](https://docs.cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference). This research establishes a more comprehensive methodology for measuring the energy, emissions, and water consumption of AI inference in a live production environment. Our goal is to promote greater transparency and encourage the industry to align on more standardized, comprehensive measurement frameworks.

Currently, the data in Google Cloud Carbon Footprint for AI services does not fully reflect this comprehensive approach, which we believe is the most transparent environmental impact assessment from AI labs today. To better align with this new, more detailed methodology, we will be updating our carbon accounting pipeline for services that use AI, such as Vertex AI.

The new methodology provides a more accurate and complete picture of the environmental impact of AI services. We anticipate that this change, which will be implemented during our next semi-annual methodology refresh, may result in an increase in the emissions data for some of our Cloud AI services. However, we believe this move to more actionable data will enable us to more readily incentivize and track optimizations for these AI services. 

The updated data will be released with the January 2026 methodology refresh, which is expected to be available in mid-February 2026. We believe this is an important step toward providing you with the most accurate and actionable data possible to manage your cloud usage more sustainably.

## August 14, 2025

Change

For the July 2025 semi-annual methodology refresh (released in mid-August 2025), we implemented the following improvements and updated the carbon model to version 14:

**Updating Scope 1 & 3 emissions from Google's corporate footprint**:

  * Updated Scope 1 & 3 allocation factors using latest Google company-wide data from [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/). See the [non-electricity emission sources section of methodology documentation](https://docs.cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation) on how we apply these Scope 1 & 3 emissions across Google products and services. 



**Updating inputs for Scope 2 market-based emissions calculation from Google's corporate footprint** :

  * Updated **annual** renewable electricity percentage from Google's clean energy procurement, in accordance with [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/), as an input for Scope 2 market-based emissions. 
  * Updated annual emissions factors from latest government sources, in accordance with [2025 Google Environmental Report](https://www.sustainability.google/reports/google-2025-environmental-report/), as an input for Scope 2 market-based emissions. Note that Scope 2 location-based emissions are estimated using **hourly** greenhouse gas emissions factors. Read more about the difference in methodology between Scope 2 location-based and market-based emissions in the [methodology document](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation).



**Improving data accuracy** :

  * A data issue impacting Cloud Run emissions calculations for March 2025 has been resolved. Incorrect carbon footprint data were generated for some Cloud Run SKUs due to a bug in our data processing logic, resulting in inflated carbon emission figures for affected users. 
    * To correct your historical data, please [run a backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for March 2025 in your carbon footprint export. Due to a half-month lag in our data release, you will need to backfill the data for April 15, 2025, which will then update the March 2025 data in your BigQuery table. Data for all other periods remains unaffected.



**Updating service coverage** :

  * Integration Connectors and Application Integration were removed from [covered services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) of Carbon Footprint, due to potential mis-attribution of carbon to these services. We are actively investigating and working on the improvements. Once internal data mapping improves for a service, we plan to add it back.



**Deprecating carbon offsets fields from schema** :

  * The `carbon_offsets_kgCO2e` and `carbon_footprint_total_kgCO2e.after_offsets` fields have been deprecated in the Carbon Footprint [schema](https://docs.cloud.google.com/carbon-footprint/docs/data-schema) due to Google's strategic shift from traditional carbon offsets to a direct focus on carbon removal technologies and projects. If you have already set up an [export](https://docs.cloud.google.com/carbon-footprint/docs/export), these two fields have been set to NULL and will not be updated. 

  * This change is in line with Google's evolving strategy for achieving its net-zero climate goals with more robust and impactful climate solutions such as carbon removal technologies. Read more about [Google's progress to accelerate carbon removal solutions](https://blog.google/outreach-initiatives/sustainability/our-progress-to-accelerate-carbon-removal-solutions/).




## March 14, 2025

Fixed

An issue resulting in unusually high emissions data for the service Identity Platform has been resolved. This affected some customers in their January 2025 data and was caused by an incorrect internal resource mapping for Identity Platform.

To correct your January emissions data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for the month. Note that there is a half-month lag of our data release. For example, to backfill January 2025 data, run the backfill for February 15, 2025, which will update the data for January 2025 in your BigQuery table.

Change

Updated carbon model to version 13 to reflect the above-mentioned fixes.

## February 13, 2025

Change

For the January 2025 semi-annual methodology refresh (released in mid-February 2025), we implemented the following improvements and updated the carbon model to version 12:

Improved internal cost accounting for Vertex AI and Notebooks services. This resulted in an improved allocation of energy consumption and emissions to these services. For more information on how we use internal cost to reallocate shared infrastructure, see [Energy use and allocation to internal services](https://cloud.google.com/carbon-footprint/docs/methodology#energy-allocation).

## September 23, 2024

Announcement

**Scope 2 market-based emissions data is now Generally Available**. This metric represents purchased electricity, incorporating Google's annual renewable energy purchases. Scope 2 emissions on this page are estimated using annual emissions factors from government sources (IEA, EPA & AIB). You can [learn more here](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation) about the methodology and the difference between location-based and market-based emission metrics.

Scope 2 market-based emissions data is available only from January 2023 onwards and can be accessed in:

  * The [console Dashboard](https://console.cloud.google.com/carbon) on the **Market-based emissions** [tab](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data#market-based-location-based), and

  * The [BigQuery export](https://docs.cloud.google.com/carbon-footprint/docs/export) as field `carbon_footprint_kgCO2e.scope2.market_based` in the [export data schema](https://docs.cloud.google.com/carbon-footprint/docs/data-schema).




## August 14, 2024

Change

Beginning with the release of January 2024 data, Google Cloud Carbon Footprint has adopted a semi-annual methodology improvement schedule, with updates planned for January and July data releases each year.

For the July 2024 data release (in mid-August 2024), we have upgraded the carbon model to version 11 and implemented the following updates:

**Updating Scope 1 & 3 emissions from Google's corporate footprint**:

  * Updated Scope 1 & 3 allocation factors using latest Google company-wide data from [2024 Google Environmental Report](https://sustainability.google/reports/google-2024-environmental-report/). See the [non-electricity emission sources section of methodology documentation](https://docs.cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation) on how we apply these Scope 1 & 3 emissions across Google products and services. 

  * Notably, expanded the Scope 1 & 3 inventory boundary to include the following for a more comprehensive emissions inventory:

    * HVAC fugitive emissions
    * Additional emissions categories of transmission & distribution (T&D) loss 
    * Extraction and transportation of fuels used to generate grid electricity



**Updating renewable electricity percentage for Scope 2 market-based emissions from Google's corporate footprint** :

  * Updated **annual** renewable electricity percentage from Google's clean energy procurement, in accordance with [2024 Google Environmental Report](https://sustainability.google/reports/google-2024-environmental-report/), as an input for Scope 2 market-based emissions. Note that Scope 2 location-based emissions are estimated using **hourly** greenhouse gas emissions factors. Read more about the difference in methodology between Scope 2 location-based and market-based emissions in the [methodology document](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation).



**Improving allocation of shared internal AI/ML resources** :

  * Improved the treatment of central machine learning compute resources and workloads across Google products and services, including corrected central resource impact to the following Google Cloud services: 
    * Cloud Natural Language
    * Translate
    * Cloud Vision API
    * Cloud Speech API
    * Cloud Dialogflow API
    * Vertex AI
    * Cloud AutoML
    * Cloud Machine Learning Engine
    * Video Stitcher API
    * Cloud Video Intelligence API
    * Notebooks
    * Cloud Text-to-Speech API



**Improving data accuracy** :

  * Improved data center PUE mapping and energy allocation to internal services.



## April 01, 2024

Feature

Scope 2 market-based emissions data is now launched in Preview. This metric represents purchased electricity, incorporating Google's annual renewable energy purchases. Scope 2 emissions on this page are estimated using annual emissions factors from government sources (IEA, EPA & AIB). You can [learn more here](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation) about the methodology and the difference between location-based and market-based emission metrics.

Scope 2 market-based emissions data is available only from January 2023 onwards and can be accessed in:

  * The [console Dashboard](https://console.cloud.google.com/carbon) on the **Market-based emissions** [tab](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data#market-based-location-based), and

  * The [BigQuery export](https://docs.cloud.google.com/carbon-footprint/docs/export) as field `carbon_footprint_kgCO2e.scope2.market_based` in the [export data schema](https://docs.cloud.google.com/carbon-footprint/docs/data-schema). 




Please note that data already [exported to BigQuery](https://docs.cloud.google.com/carbon-footprint/docs/export) for previous months will still have Scope 2 market-based emissions data as NULL in your exported tables. To see the newly-released market-based data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for the desired time period. Note that there is a half-month lag of our data release. For example, to backfill January and February 2023 data, run the backfill for February 15, 2023 and March 15, 2023, which will update the data for January and February 2023 in your BigQuery table.

## March 15, 2024

Change

Emissions reported for Google Kubernetes Engine (GKE) declined starting in February 2024. This change is a result of an update to Google's internal cost allocation, which determines how shared infrastructure costs are attributed to individual services. According to our methodology ([Technical details - Electricity use](https://docs.cloud.google.com/carbon-footprint/docs/methodology#details-electricity)), these internal costs are used to apportion electricity consumption and carbon emissions to services, so changes in cost apportionment result in corresponding changes to carbon apportionment and reporting for that service.

## February 14, 2024

Change

Beginning with the release of January 2024 data, Google Cloud Carbon Footprint will adopt a biannual methodology refresh schedule, with updates planned for January and July data releases each year. 

For the January 2024 data release (in mid-February 2024), we have made the updates below and updated carbon model to version 10:

**Data accuracy** :

  * Improve internal machine-level power readings for storage machines. Update allocation of energy from some machines, improving Bigtable data accuracy.
  * Further improve mapping between Google Cloud services and internal resource use, particularly for a few Networking SKUs.
  * Improve Google Cloud region defaults and coverage. [`location.location`/`location.region`](https://docs.cloud.google.com/carbon-footprint/docs/data-schema) with former `NULL` values are defined as `global`, and we improved data for the `europe` multiregion. 



**Corporate data input refresh** :

  * Update Scope 1/3 apportionment factors using latest Google company-wide data from [2023 Google Environmental Report](https://www.gstatic.com/gumdrop/sustainability/google-2023-environmental-report.pdf). See the [Non-electricity emission sources section of methodology document](https://docs.cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation) on how we apply these apportionment factors.



**Service coverage** :

  * Reintroduce App Engine and GKE Enterprise/GDC services [(formerly Anthos/GDC-V)](https://docs.cloud.google.com/anthos/docs/concepts/overview), as internal data mappings have been improved. 
  * Remove Looker, Apigee, Chronicle, and AppSheet from [covered services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) of Carbon Footprint, due to potential mis-attribution of carbon to these services. We are actively investigating and working on the improvements. Once internal data mapping improves for a service, we plan to add it back.



## December 13, 2023

Fixed

Fixed bugs for Scope 1 and Scope 3 (non-electricity sources) emissions apportionment for September 2023 and October 2023 and Scope 2 location-based emissions for October 2023. Specifically:

  * In September and October 2023, incorrect apportionment factors were used to estimate emissions from non-electricity sources. Some customers might have seen an increase in Scope 1 emissions and a decrease in Scope 3 emissions in their reports. To address the issue, we have corrected the apportionment factors from September 2023 onwards.

    * For more information on how we allocate Scope 1 and 3 emissions, refer to the [Non-electricity emission sources](https://docs.cloud.google.com/carbon-footprint/docs/methodology#non-electricity-allocation) Section in our public methodology document.
  * Customers may have seen an increase across all services in Scope 2 location-based emissions in October 2023. This was due to an error in an upstream hourly carbon intensity data source. The error has now been corrected for Scope 2 location-based emissions for October 2023. 




Please note that data already [exported to BigQuery](https://docs.cloud.google.com/carbon-footprint/docs/export) for previous months is not automatically corrected in your exported tables. To see the corrected data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for the desired time period. Note that there is half a month lag of our data release. For example, to backfill September and October 2023 data, run the backfill for October 15, 2023 and November 15, 2023, which will update the data for September and October 2023 in your BigQuery table.

Fixed

Improved data consistency on BigQuery exports, particularly on the `project_id` field. In our BigQuery [data exports](https://docs.cloud.google.com/carbon-footprint/docs/export), there were instances where the `project_id` field contained a NULL value, and in some of these cases, carbon for a particular project was split between two rows where the project ID was listed as NULL and non-NULL. (Note that the `project_number` field is always populated, and the total carbon when summed across all rows is correct for a given project number.) We have updated our reports for all prior months in order to populate the `project_id` field consistently, with a non-NULL value wherever possible. We have ensured each project's carbon is reported as a single row within a given month, service, and location. 

To update previous months of data, [schedule a manual data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#manually_trigger_a_transfer_or_backfill) for the desired time period.

## August 14, 2023

Change

Updated carbon model to version 9. 

Customer carbon data for Cloud Functions will see a decrease starting from 2023-07-01 data onward. This decrease is a result of improvements in the apportionment of energy and carbon between Cloud Functions and App Engine. The impact is only seen in Cloud Functions, because App Engine is not yet supported in our [covered services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services). This improvement is part of our efforts to support App Engine in the near future.

## January 01, 2023

Change

Improvements to customer carbon data starting 2023-01-01 onward. The following services are seeing the largest data changes: Compute Engine, BigQuery, Kubernetes Engine, Cloud Storage, Networking, Cloud Filestore, Cloud SQL, Cloud Dataflow, Vertex AI, and Alloy DB. These changes are the results of ongoing improvement to the apportionment of machine idle power and shared infrastructure's energy consumption.

Change

Updated carbon model to version 8.

## December 23, 2022

Fixed

Fixed an issue that omitted Scope 1 and Scope 3 emissions for a given region in a given month that has zero Scope 2 emissions due to 100% carbon free energy.

Specifically, in July 2022, `northamerica-northeast1` had 100% of its electricity generated from hydro power for the month, resulting in no Scope 2 emissions for the month despite positive energy consumption to run the data center. However, there were Scope 1 and Scope 3 emissions apportioned to the usage of this data center, but our data erroneously omitted them. 

As a fix, we have added the Scope 1 and Scope 3 emissions back for any usage in `northamerica-northeast1` in July 2022, and will not omit such emissions going forward that have positive apportioned Scope 1 and Scope 3 emissions but zero Scope 2 emissions.

Change

Electricity Maps (EM), our carbon emissions factors data source, is making improvements to their methodology that will affect carbon emissions data released beginning on December 15th. For a detailed description of the improvement, please see Electricity Maps blog post [here](https://www.electricitymaps.com/blog/increasing-the-precision-of-our-data-using-regional-emission-factors). 

In sum, EM will now be incorporating the efficiency and technology of power plants into consideration when calculating emission factors, increasing the precision of how emission factors are measured. It represents a data quality improvement, which will impact data for cost centers located in the United States and European Union.

Change

Updated carbon model to version 7 to reflect the above-mentioned changes.

## October 13, 2022

Fixed

We fixed a bug that caused some customers to see duplicate rows in their BigQuery data exports. If you ran a manual data backfill between 2022-09-28 and 2022-10-13 (for any target date) and notice duplicate rows, you can correct the problem by re-running the backfill following [the instructions here](https://cloud.google.com/carbon-footprint/docs/export#bigquery).

## October 11, 2022

Announcement

[Google Cloud Carbon Footprint](https://docs.cloud.google.com/carbon-footprint) is now Generally Available.

## October 05, 2022

Change

We improved the data quality and updated coverage for the following services:

  * Improved mapping between Google Cloud services and internal resource use, particularly for a few Networking SKUs. 
  * Removed App Engine (including Firestore and Datastore), Support, and Anthos from [covered services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) of Carbon Footprint, due to potential mis-attribution of carbon to these services. We are actively investigating and working on the improvements. Once internal data consistency improves for a service, we plan to add it back.



Change

Updated carbon model to version 6

## August 23, 2022

Fixed

The `carbon_footprint_kgCO2e.scope2.market_based` and `carbon_offsets_kgCO2e` fields of the [exported carbon data](https://docs.cloud.google.com/carbon-footprint/docs/data-schema) are set to `NULL` instead of `0`, to better reflect that the fields are not yet populated.

## July 07, 2022

Change

We've made the following updates to data sources and methodology for Scope 2 location-based emissions:

  * Improved power data measurements.
  * Changed from LCA grid carbon intensity values to scope-2-compliant direct grid emissions.
  * Corrected data that led to changes in internal cost-based reallocation of shared infrastructure energy consumption.
  * Removed `VPC Network Logs` SKU that caused inaccurate results.



Feature

Carbon Footprint now reports carbon emissions broken down by scope 1, scope 2, and scope 3 categories, following the [Greenhouse Gas (GHG) Protocol carbon reporting standards](https://ghgprotocol.org/standards).

Breaking

We've renamed the Carbon Footprint export table from `carbon_footprint_export` to `carbon_footprint` within the target BigQuery dataset indicated by your data transfer configuration. The renamed table contains an [updated schema](https://cloud.google.com/carbon-footprint/docs/data-schema). Furthermore, the renamed table is now [ partitioned](https://cloud.google.com/bigquery/docs/partitioned-tables) by month. Each month's data is exported on the 15th day of the following month. **Data for previous months is not automatically exported** , but you can [schedule manual data backfills](https://cloud.google.com/bigquery/docs/working-with-transfers#schedule_a_backfill) to export data for previous months. Carbon Footprint will no longer update existing `carbon_footprint_export` tables.

Change

Updated carbon model to version 5

## April 26, 2022

Change

Viewing and exporting carbon footprint data now requires the `billing.accounts.getCarbonInformation` [IAM permission](https://docs.cloud.google.com/carbon-footprint/docs/iam). This permission is part of the _Carbon Footprint Viewer_ (`roles/billing.carbonViewer`) and _Billing Account Viewer_ (`roles/billing.viewer`) [IAM roles](https://docs.cloud.google.com/carbon-footprint/docs/iam).

## March 31, 2022

Fixed

Improved carbon accounting for Retail API

Fixed

Improved mapping between Google Cloud services and internal resource use. This changes the carbon footprint of some Google Cloud services and adds other Google Cloud Services, like Networking, to the list of covered services.

Change

Updated carbon model to version 4

Fixed

Improved carbon accounting for many AI services (these services aren't covered in 2021)

## January 20, 2022

Feature

A [Carbon Footprint Looker block](https://marketplace.looker.com/marketplace/detail/carbon) is available to create custom dashboards using [Looker](https://looker.com/).

## January 11, 2022

Feature

[Unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) now reports the reduction in gross carbon footprint associated with your workloads. If there is a recommendation, it is now displayed directly in the Carbon Footprint dashboard.

## October 12, 2021

Announcement

[Google Cloud Carbon Footprint](https://docs.cloud.google.com/carbon-footprint) is in Public Preview

## August 25, 2021

Announcement

Google Cloud Carbon Footprint is in Private Preview

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
