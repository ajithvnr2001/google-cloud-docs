---
url: https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-data-profile/
title: Profile and validate data quality \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:51.652956+00:00
---

# Profile and validate data quality  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/quickstart-data-profile/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profile and validate data quality

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you profile BigQuery tables to calculate column-level statistics, such as null percentages, unique value counts, and value distributions. You can then use these insights to define data quality rules and validate your records for anomalies.

In this quickstart, you populate a sample BigQuery table with intentional anomalies, run a data profile scan, and evaluate the results with a data quality scan. For more information, see [About data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview) and [About auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).

## Before you begin

Set up your project: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Knowledge Catalog and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Knowledge Catalog and BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to create and run data profile and data quality scans, and manage BigQuery resources, ask your administrator to grant you the following IAM roles on the project: 

  * Create, run, and delete data scans: [Dataplex DataScan Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanEditor) (`roles/dataplex.dataScanEditor`) 
  * Create, populate, and delete sample tables: [BigQuery Data Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataOwner) (`roles/bigquery.dataOwner`) 
  * Run SQL queries in BigQuery: [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you have the necessary permissions to manage IAM access in your project, you can grant these roles to your own user account by running the following `gcloud` commands:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_EMAIL" \
        --role="roles/dataplex.dataScanEditor"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_EMAIL" \
        --role="roles/bigquery.dataOwner"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_EMAIL" \
        --role="roles/bigquery.jobUser"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `USER_EMAIL`: your user account email address (for example, `name@example.com`).



### Grant permissions to the Knowledge Catalog service agent

A [service agent](https://docs.cloud.google.com/iam/docs/service-agents) is a Google-managed service account that Knowledge Catalog uses to run scan queries in BigQuery on your behalf.

  1. In the Google Cloud console, click **Activate Cloud Shell** in the toolbar. The environment takes a few moments to provision and connect.

  2. Create the Knowledge Catalog service agent:
         
         gcloud beta services identity create --service=dataplex.googleapis.com
         

This command creates the service agent if it hasn't been provisioned yet and outputs its email. If your project already has a Knowledge Catalog service agent, the command returns the existing identity without making any changes.

The output is similar to the following:
         
         serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com
         

Note the `PROJECT_NUMBER` in the output for the next steps.

  3. Grant the **BigQuery Job User** (`roles/bigquery.jobUser`) role so Knowledge Catalog can run query jobs in your project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
            --role="roles/bigquery.jobUser"
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `PROJECT_NUMBER`: your Google Cloud project number.
  4. Grant the **BigQuery Data Viewer** (`roles/bigquery.dataViewer`) role so the service agent can read your table data and schema:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
            --role="roles/bigquery.dataViewer"
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `PROJECT_NUMBER`: your Google Cloud project number.



## Create a sample dataset and table

To try out profiling and data quality scans safely without touching production data, set up a dedicated BigQuery dataset and create a table containing sample bikeshare data with intentional anomalies, such as duplicates and null values.

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, click more_vert **View actions** next to your project ID, and then click **Create dataset**.

  3. In the **Dataset ID** field, enter `quickstart_data_profile`.

  4. In the **Data location** list, select **us-central1 (Iowa)**.

  5. Click **Create dataset**.

  6. In the query editor, enter the following SQL query to generate sample bikeshare data in your `bikeshare_trips` table:
         
         CREATE OR REPLACE TABLE `PROJECT_ID.quickstart_data_profile.bikeshare_trips` AS
         SELECT
         -- Duplicate and null IDs
         IF(MOD(x, 100) = 0, NULL, IF(x > 9900, 1000 + (x - 9900), 1000 + x)) AS trip_id,
         -- Nulls and unrecognized category values
         CASE
           WHEN MOD(x, 50) = 0 THEN 'INVALID_TIER'
           WHEN MOD(x, 25) = 0 THEN NULL
           WHEN MOD(x, 4) = 0 THEN 'Local Rider'
           WHEN MOD(x, 4) = 1 THEN 'Walk Up'
           WHEN MOD(x, 4) = 2 THEN 'Student Membership'
           ELSE 'Weekender'
         END AS subscriber_type,
         -- Nulls and malformed bike IDs
         CASE
           WHEN MOD(x, 60) = 0 THEN 'UNKNOWN'
           WHEN MOD(x, 30) = 0 THEN NULL
           ELSE CAST(2000 + x AS STRING)
         END AS bike_id,
         -- Null dates and future timestamps
         CASE
           WHEN MOD(x, 70) = 0 THEN NULL
           WHEN MOD(x, 40) = 0 THEN TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL x MINUTE)
           ELSE TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL x MINUTE)
         END AS start_time,
         -- Nulls and placeholder station values
         CASE
           WHEN MOD(x, 20) = 0 THEN 'STATION_UNKNOWN'
           WHEN MOD(x, 10) = 0 THEN NULL
           ELSE CAST(100 + MOD(x, 50) AS STRING)
         END AS start_station_id,
         -- Negative durations, zeros, and extreme outliers
         CASE
           WHEN MOD(x, 15) = 0 THEN -10.0
           WHEN MOD(x, 35) = 0 THEN 0.0
           WHEN MOD(x, 200) = 0 THEN 99999.0
           ELSE CAST(MOD(x, 120) + 1.5 AS FLOAT64)
         END AS duration_minutes
         FROM UNNEST(GENERATE_ARRAY(1, 10000)) AS x;

Replace `PROJECT_ID` with your Google Cloud project ID.

  7. Click play_circle **Run**.




### gcloud

  1. In Cloud Shell, create the `quickstart_data_profile` dataset in the `us-central1` region:
         
         bq --location=us-central1 mk --dataset PROJECT_ID:quickstart_data_profile
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Create and populate the `bikeshare_trips` sample table:
         
         bq query \
         --use_legacy_sql=false \
         "CREATE OR REPLACE TABLE \`PROJECT_ID.quickstart_data_profile.bikeshare_trips\` AS
         SELECT
           IF(MOD(x, 100) = 0, NULL, IF(x > 9900, 1000 + (x - 9900), 1000 + x)) AS trip_id,
           CASE
             WHEN MOD(x, 50) = 0 THEN 'INVALID_TIER'
             WHEN MOD(x, 25) = 0 THEN NULL
             WHEN MOD(x, 4) = 0 THEN 'Local Rider'
             WHEN MOD(x, 4) = 1 THEN 'Walk Up'
             WHEN MOD(x, 4) = 2 THEN 'Student Membership'
             ELSE 'Weekender'
           END AS subscriber_type,
           CASE
             WHEN MOD(x, 60) = 0 THEN 'UNKNOWN'
             WHEN MOD(x, 30) = 0 THEN NULL
             ELSE CAST(2000 + x AS STRING)
           END AS bike_id,
           CASE
             WHEN MOD(x, 70) = 0 THEN NULL
             WHEN MOD(x, 40) = 0 THEN TIMESTAMP_ADD(CURRENT_TIMESTAMP(), INTERVAL x MINUTE)
             ELSE TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL x MINUTE)
           END AS start_time,
           CASE
             WHEN MOD(x, 20) = 0 THEN 'STATION_UNKNOWN'
             WHEN MOD(x, 10) = 0 THEN NULL
             ELSE CAST(100 + MOD(x, 50) AS STRING)
           END AS start_station_id,
           CASE
             WHEN MOD(x, 15) = 0 THEN -10.0
             WHEN MOD(x, 35) = 0 THEN 0.0
             WHEN MOD(x, 200) = 0 THEN 99999.0
             ELSE CAST(MOD(x, 120) + 1.5 AS FLOAT64)
           END AS duration_minutes
         FROM UNNEST(GENERATE_ARRAY(1, 10000)) AS x;"
         




## Create and run a data profile scan

A data profile scan looks across your table rows to calculate statistical insights, including unique value counts, null ratios, and data distribution ranges.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click **Create data profile scan**.

  3. Under **Choose type** , leave **Data profile scan** selected.

  4. Under **General** , in the **Display name** field, enter `bikeshare-trips-profile`.

  5. Under **Table to scan** , in the **Table** field, click **Browse** , select the `quickstart_data_profile.bikeshare_trips` table in your project, and then click **Select**.

  6. For **Mode** , select **Standard**.

  7. For **Scope** , select **Entire data**.

  8. For **Schedule** , select **On-demand**.

  9. Leave the other settings as their defaults.

  10. Click **Run scan**.

The scan job starts. It typically takes 3 to 5 minutes for Knowledge Catalog to run the scan and calculate statistics for your table.




### gcloud

  1. In Cloud Shell, create the data profile scan:
         
         gcloud dataplex datascans create data-profile bikeshare-trips-profile \
          --location=us-central1 \
          --data-source-resource="//bigquery.googleapis.com/projects/PROJECT_ID/datasets/quickstart_data_profile/tables/bikeshare_trips" \
          --description="Data profile scan for sample bikeshare dataset"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Run the data profile scan:
         
         gcloud dataplex datascans run bikeshare-trips-profile \
          --location=us-central1
         

The scan job starts in the background. The scan typically takes 3 to 5 minutes to finish.




## Review data profile scan results

After the scan finishes, review the column statistics to understand your data characteristics.

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. In the list of scans, click **bikeshare-trips-profile**.

  3. If the scan has not run yet, click **Run now**.

  4. In the **Overview** section, wait for the latest scan job to show **Succeeded**.

The following image shows the scan job in the **Overview** section with the **Succeeded** status:

![Overview section of the bikeshare trips profile scan showing the job status as succeeded and the View results link.](https://docs.cloud.google.com/static/knowledge-catalog/images/data-profile-scan-overview.png)

  5. Inspect the scan results to understand your table's data distribution and identify potential data quality validation targets. In the **Latest job results** tab, Knowledge Catalog displays column-level metrics including **Null %** , **Unique count and %** , **Top values** , and **Summary statistics**.

The following table shows which profile metric to check for each table column, how to interpret the results, and which data quality rule to target:

Table column | Profile result metric | What to look for and how to interpret | Data quality validation target  
---|---|---|---  
`duration_minutes` | **Summary statistics** | **Negative values detected** : The **Min** value is `-10.0` minutes. Elapsed trip duration cannot be negative, indicating invalid sensor or ride recordings. | Target with a **Validity (Range)** rule (such as `duration_minutes ≥ 1.0`) to require positive elapsed ride times.  
`start_station_id` | **Null %** | **About 5% null values** : The null percentage is greater than 0%, showing that some records lack station checkout identifiers (such as dockless or kioskless trips). | Target with a **Completeness (Non-null)** rule to catch and flag records with missing station IDs.  
`subscriber_type` | **Top values** | **Unexpected categories** : Frequent values list non-standard categories (such as `INVALID_TIER`) alongside valid membership tiers, indicating unvalidated user input or ingestion issues. | Target with a **Validity (Set)** rule to enforce that all incoming values belong to your allowed list of membership types.  
`trip_id` | **Unique count and %** | **Duplicate IDs detected** : Uniqueness is lower than 100% (about 98%), indicating repeated identifier records. Primary keys and trip identifiers should be 100% unique. | Target with a **Uniqueness** rule to flag and prevent duplicate trip records.  



These profile findings give you an evidence-based baseline to create targeted data quality rules.

## Create and run a data quality scan

Now that you've discovered what the data looks like, set up automated data quality rules to catch anomalies. In this step, you configure four common rule types based on your profile findings.

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. Click **Create data quality scan**.

  3. Under **General** , in the **Display name** field, enter `bikeshare-trips-quality`.

  4. Under **Table to scan** , in the **Table** field, click **Browse** , select the `quickstart_data_profile.bikeshare_trips` table, and then click **Select**.

  5. For **Scope** , select **Entire data**.

  6. For **Schedule** , select **On-demand**.

  7. Leave the other settings as their defaults and click **Continue**.

  8. In the **Data quality rules** section, click **Add Rules** and select **Built-in rule types**.

**Note:** Although Knowledge Catalog can automatically generate baseline rules using **Profile based recommendations** , those recommendations reflect your existing data distribution (including any anomalies). To enforce business expectations and catch data defects, use **Built-in rule types**.
  9. In the **Add rules** panel, select the columns and rule types:

     * In the **Choose columns** field, click **Browse** , and select `duration_minutes`, `start_station_id`, `subscriber_type`, and `trip_id`.
     * Click **Select**.
     * In the **Choose rule types** list, select **Range check** , **NULL check** , **Value-set check** , and **Uniqueness check** , and then click **OK**.
     * In the generated rules list, select the checkbox for each of the following rules:

       * `duration_minutes`: **Range check**
       * `start_station_id`: **NULL check**
       * `subscriber_type`: **Value-set check**
       * `trip_id`: **Uniqueness check**
     * Click **Select**.

  10. In the **Data quality rules** table, configure parameters for the rules that require values:

     * For `duration_minutes` (**Range check**), click edit **Edit** , enter `1.0` in the **Min value** field, and click **Save**.
     * For `subscriber_type` (**Value-set check**), click edit **Edit** , click **Add Value** to add each of the allowed values (`Local Rider`, `Walk Up`, `Student Membership`, and `Weekender`), and click **Save**.
  11. Click **Continue** , and then click **Run scan**.




### gcloud

  1. In Cloud Shell, create a file named `dq_bikeshare.yaml` with rule specifications that target the anomalies found in your profile:
         
         cat << 'EOF' > dq_bikeshare.yaml
         rules:
           - column: trip_id
             dimension: UNIQUENESS
             uniquenessExpectation: {}
           - column: start_station_id
             dimension: COMPLETENESS
             nonNullExpectation: {}
           - column: duration_minutes
             dimension: VALIDITY
             rangeExpectation:
               minValue: "1.0"
           - column: subscriber_type
             dimension: VALIDITY
             setExpectation:
               values:
                 - "Local Rider"
                 - "Walk Up"
                 - "Student Membership"
                 - "Weekender"
         EOF
         

  2. Create the data quality scan:
         
         gcloud dataplex datascans create data-quality bikeshare-trips-quality \
          --location=us-central1 \
          --data-source-resource="//bigquery.googleapis.com/projects/PROJECT_ID/datasets/quickstart_data_profile/tables/bikeshare_trips" \
          --data-quality-spec-file="dq_bikeshare.yaml" \
          --description="Data quality scan for sample bikeshare dataset"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  3. Run the data quality scan:
         
         gcloud dataplex datascans run bikeshare-trips-quality \
          --location=us-central1
         




## Review data quality rule evaluations

Check your data quality results to see how your rules evaluated the sample data and identified anomalies.

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. In the **Scans** table, click the **bikeshare-trips-quality** scan.

  3. In the **Overview** section, click **View results** to open the job details.

  4. In the **Job details** panel, review the evaluation results:

     * **Data quality status** : As expected, all 3 evaluated dimensions show a status of **Failed**.

       * **Validity** : **Failed**. The `duration_minutes` column contains negative values and `subscriber_type` contains invalid membership values (`INVALID_TIER`).
       * **Completeness** : **Failed**. The `start_station_id` column contains null values.
       * **Uniqueness** : **Failed**. The `trip_id` column contains duplicate records.
     * **Rules** : In the **Rules** table, all 4 evaluated rules show a status of **Failed**.

       * `duration_minutes`: Range check (**Failed**)
       * `start_station_id`: NULL check (**Failed**)
       * `subscriber_type`: Value-set check (**Failed**)
       * `trip_id`: Uniqueness check (**Failed**)

For any failed rule, you can copy the SQL query in the **Query to get failed records** column and run it in BigQuery to isolate and inspect the invalid rows.




You've now profiled a BigQuery table to discover column statistics and used those insights to define and validate automated data quality rules.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Console

  1. In the Google Cloud console, go to the **Data profiling & quality** page.

[Go to Data profiling & quality](https://console.cloud.google.com/dataplex/govern/data-profiling-and-quality)

  2. In the **Scans** table, select **bikeshare-trips-quality** and **bikeshare-trips-profile**.

  3. Click **Delete** and confirm.

  4. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  5. In the **Explorer** pane, click **Datasets**.

  6. Select the `quickstart_data_profile` dataset, and then click **Delete**.




### gcloud

In Cloud Shell, delete the data quality scan, data profile scan, and sample dataset:
    
    
    gcloud dataplex datascans delete bikeshare-trips-quality --location=us-central1 --quiet
    gcloud dataplex datascans delete bikeshare-trips-profile --location=us-central1 --quiet
    bq rm -r -f -d PROJECT_ID:quickstart_data_profile
    

Replace `PROJECT_ID` with your Google Cloud project ID.

## What's next

  * [View and troubleshoot data quality scan results](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality#results)
  * [Monitor data scans and set up alerts](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-data-scans)
  * [Build a policy-as-code data quality workflow using the Antigravity CLI](https://docs.cloud.google.com/knowledge-catalog/docs/build-policy-as-code-data-quality-workflow)
  * [Manage data quality rules as code with Terraform](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code)
  * [Reuse data quality rules across tables](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules)
  * [Explore additional Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
