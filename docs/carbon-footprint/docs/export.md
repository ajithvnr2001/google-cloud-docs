---
url: https://docs.cloud.google.com/carbon-footprint/docs/export/
title: Export your carbon footprint \u00a0|\u00a0 Carbon Footprint \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:58.435057+00:00
---

# Export your carbon footprint  |  Carbon Footprint  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Export your carbon footprint

You can export your Carbon Footprint data to BigQuery in order to perform data analysis, or to create custom dashboards and reports.

The Carbon Footprint export captures estimated greenhouse gas emissions associated with the usage of [covered Google Cloud services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) for the selected billing account.

After configuring an export, you are charged for the [BigQuery](https://cloud.google.com/bigquery/pricing) resources used to store and query the exported data.

## Before you begin

To create a Carbon Footprint export, we recommend having the following IAM roles:

  * [_Project Owner_ or _Project Editor_](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on the Google Cloud project to export to.
  * [_Carbon Footprint Viewer_](https://docs.cloud.google.com/carbon-footprint/docs/iam) or [_Billing Account Viewer_](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on the billing account whose carbon data will be exported.



More precisely, you must have the following IAM permissions on the Google Cloud project:

  * `resourcemanager.projects.update`
  * `serviceusage.services.enable`
  * `bigquery.transfers.update`



And the following IAM permission on the billing account:

  * `billing.accounts.getCarbonInformation`



### If using VPC Service Controls

If your organization is using VPC Service Controls, an ingress rule needs to be defined for the BigQuery API and BigQuery Data Transfer Service API.

For your Ingress policy rule:

  * Set the source in the 'From' section to 'All sources allow'.
  * Grant permission to the identity, `els-da-carbon@gcp-carbon-footprint-exports.iam.gserviceaccount.com`.



## Configuring a Carbon Footprint export to BigQuery

Carbon Footprint data is exported via the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction). The data transfer creates a [monthly partitioned table](https://docs.cloud.google.com/bigquery/docs/partitioned-tables) called `carbon_footprint` in the BigQuery dataset of your choice.

Carbon Footprint exports each month's data on the 15th day of the following month. For example, carbon data for September 2022 will be exported on October 15, 2022.

Once a Carbon Footprint transfer config has been created, it will automatically export future carbon reports on the 15th of every month. You will also be able to run a backfill to request historical data back to January 2021.

###  Console 

Take the following steps to initiate the export:

  1. [Go to Carbon Footprint](https://console.cloud.google.com/carbon)
  2. Select the Cloud Billing account you want to export from the **Billing account** menu.
  3. Click **Data export** to open the side-panel for configuring the export.
  4. Select a project for your carbon footprint data export, and then click **Create export**.
  5. On the BigQuery Data Transfer Service page: 
     1. Ensure that **Source** is set to "Google Cloud Carbon Footprint Exports".
     2. In **Transfer config name** , enter a display name.
     3. In **Destination settings** , click the **Dataset ID** field and then select **Create new dataset** if you want to create a new BigQuery dataset to host the exported table; alternatively select an existing BigQuery dataset.
     4. In **Data source details** , confirm the Cloud Billing account ID to export. Optionally, add additional account IDs as a comma separated list. All billing account IDs should be in the format `XXXXXX-XXXXXX-XXXXXX`.
  6. Click **Save**.
  7. In the access request window, click **Allow**.



###  bq 

Use the [`bq mk --transfer_config` command](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) to initiate the export:
    
    
    bq mk \
    --transfer_config \
    --target_dataset=DATASET \
    --display_name=NAME \
    --params='{"billing_accounts":"BILLING_ACCOUNT_IDS"}' \
    --data_source='61cede5a-0000-2440-ad42-883d24f8f7b8'

Where:

  * DATASET is the target dataset for the transfer configuration.
  * NAME is the display name for the transfer configuration. For example: "Company Carbon Report".
  * BILLING_ACCOUNT_IDS is your billing account ID or a comma-separated list of billing account IDs. For example: `XXXXXX-XXXXXX-XXXXXX,XXXXXX-XXXXXX-XXXXXX`



###  Terraform 

Use the [`bigquery_data_transfer_config` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_data_transfer_config) to create an export:
    
    
    resource "google_bigquery_data_transfer_config" "RESOURCE_NAME" {
      display_name           = "NAME"
      data_source_id         = "61cede5a-0000-2440-ad42-883d24f8f7b8"
      destination_dataset_id = google_bigquery_dataset.DATASET.dataset_id
      params = {
        billing_accounts     = "BILLING_ACCOUNT_IDS"
      }
    }

Where:

  * RESOURCE_NAME is the name of the Terraform resource. For example: `carbon_export`.
  * NAME is the display name for the transfer configuration. For example: "Company Carbon Report".
  * DATASET is the name of the `google_bigquery_dataset` Terraform resource to use as the target dataset for the export.

  * BILLING_ACCOUNT_IDS is your billing account ID or a comma-separated list of billing account IDs. For example: `XXXXXX-XXXXXX-XXXXXX,XXXXXX-XXXXXX-XXXXXX`




The transfer config has now been created and will export data on the 15th of every future month.

**Note:** If you are using a method other than the console for exporting the data, the data source will not be automatically enrolled in your project. So, please use the [ Enroll Data Sources API](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects/enrollDataSources) to enroll the data source in your project before running the export operation. 

The transfer config does **not** automatically export historical data. To request historical data back to January 2021, schedule a [data backfill](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#set_up_backfills_and_refresh_runs) using the following steps.

###  Console 

Take the following steps to schedule the data backfill:

  1. Go to the details of the transfer you just created.
  2. Click **Schedule Backfill**.
  3. Select **Run for a date range**.
  4. Select February 15, 2021 as the **start date** and today's date as the **end date**. Note that the export for February 15, 2021 contains the January 2021 data and is therefore the earliest month available to request.
  5. Click **OK** to request the data backfill.



Data backfills will be created for the selected range, exporting historical monthly data to the destination dataset.

###  bq 

Use the [`bq mk --transfer_run` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-transfer-run) to create a backfill:
    
    
    bq mk \
    --transfer_run \
    --start_time=START_TIME \
    --end_time=END_TIME \
    CONFIG

Where:

  * START_TIME is a [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) that specifies the start time of the range to backfill. For example: `2021-02-15T00:00:00Z`. Note that February 15, 2021 is the earliest date you can specify here, as it contains the January 2021 data.
  * END_TIME is a [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) that specifies the end time of the range to backfill. For example: `2022-09-15T00:00:00Z`. You can use the current date.
  * TRANSFER_CONFIG is the identifier of the transfer created in the previous step. For example: `projects/0000000000000/locations/us/transferConfigs/00000000-0000-0000-0000-000000000000`.



Once the data is exported, you can use BigQuery to [view and query the data](https://docs.cloud.google.com/bigquery/docs). Read more about the [data schema](https://docs.cloud.google.com/carbon-footprint/docs/data-schema).

You can share the exported data to others in your organization by granting them the [BigQuery User IAM role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user) on the project selected earlier. Alternatively, you can grant fine-grained access at the dataset or table level using the [BigQuery Data Viewer IAM role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer).

## Managing Carbon Footprint exports

You can see all existing Carbon Footprint exports by clicking on **Data export** and opening the side-panel.

You can then manage each Carbon Footprint export by clicking on the transfer name to visit the [BigQuery Data Transfer Service](https://console.cloud.google.com/bigquery/transfers) or dataset name to see the destination dataset. Learn more about [Working with transfers](https://docs.cloud.google.com/bigquery/docs/working-with-transfers).

**Note:** In some cases, the list of exports may not be complete for the following reasons:

  * **Permissions** : The export was configured in a project that you don't have permission to view.
  * **Performance Optimization** : To optimize performance and prevent latency when you have access to a very large number of projects, the search may not display exports in all projects.



## Exporting to Google Sheets or CSV

After you've configured your carbon footprint export to BigQuery and the scheduled export has completed, you can export that data from BigQuery to Google Sheets or CSV.

  1. [Go to BigQuery](https://console.cloud.google.com/bigquery)
  2. In the **Explorer** panel, expand your project and dataset, then select the table that contains the exported carbon footprint data.
  3. Click **Query**.
  4. Enter a query to return the data you want to export. See below for an example.
  5. After the query has run, under **Query results** , click **Save results**.
  6. Select the desired format and click **Save**.



The following query lets you save the entire contents of the exported table:
    
    
    SELECT
      usage_month,
      billing_account_id,
      project.number AS project_number,
      project.id AS project_id,
      service.id AS service_id,
      service.description AS service_description,
      location.location AS location,
      location.region AS region,
      carbon_model_version,
      carbon_footprint_kgCO2e.scope1 AS carbon_footprint_scope1,
      carbon_footprint_kgCO2e.scope2.location_based AS carbon_footprint_scope2_location_based,
      carbon_footprint_kgCO2e.scope3 AS carbon_footprint_scope3,
      carbon_footprint_total_kgCO2e.location_based AS carbon_footprint_total_location_based
    FROM
      `PROJECT.DATASET.carbon_footprint`
    ORDER BY
      usage_month DESC,
      carbon_footprint_total_location_based DESC
    

## What's next?

  * [Read about the data schema used in the export](https://docs.cloud.google.com/carbon-footprint/docs/data-schema).
  * [Explore your gross carbon footprint in the Google Cloud console](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data).
  * [Create custom dashboards with the exported data](https://docs.cloud.google.com/carbon-footprint/docs/custom-dashboard).
  * [Understand the methodology behind Carbon Footprint](https://docs.cloud.google.com/carbon-footprint/docs/methodology).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
