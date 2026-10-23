---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles/
title: Analyze data profiles stored in BigQuery \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:46.832676+00:00
---

# Analyze data profiles stored in BigQuery  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Analyze data profiles stored in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

If you [configured the sensitive data discovery service](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder) to send all successfully generated data profiles to BigQuery, you can query those data profiles to gain insights about your data. You can also use visualization tools like Data Studio to build custom reports tailored to your business needs. Alternatively, you can use a premade report that Sensitive Data Protection provides, tune it, and share it as needed.

This page provides example SQL queries that you can use to learn more about your data profiles. It also shows you how you can visualize data profiles in in Data Studio.

For more information on data profiles, see [Overview of sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## Before you begin

This page assumes that you have configured profiling at the organization, folder, or project level. In your discovery scan configuration, make sure that the **Save data profile copies to BigQuery** action is enabled. For more information about how to create a discovery scan configuration, see [Create a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create).

## The output table

In this document, the table that contains the exported data profiles is called the _output table_.

**Important:** The output table uses [`DataProfileBigQueryRowSchema`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

Make sure you have the project ID, dataset ID, and table ID of the output table readily available. You need them to perform the procedures on this page.

## The `latest` view

When Sensitive Data Protection exports data profiles to your output table, it also creates the `latest` [view](https://docs.cloud.google.com/bigquery/docs/views-intro). This view is a prefiltered virtual table that includes only the latest snapshots of your data profiles. The `latest` view has the same schema as the output table, so you can use the two interchangeably in your SQL queries and Data Studio reports. The results can differ because the output table contains older snapshots of the data profiles.

The `latest` view is stored in the same location as the output table. Its name has the following format:
    
    
    OUTPUT_TABLE_latest_VERSION
    

Replace the following:

  * OUTPUT_TABLE: the ID of the table that contains the exported data profiles.
  * VERSION: the version number of the view.



For example, if your output table's name is `table-profile`, then the `latest` view has a name like `table-profile_latest_v1`.

![Latest view](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/latest-view.png)

When using the `latest` view in SQL queries, use the view's full name, which includes the project ID, dataset ID, table ID, and suffix—for example, `myproject.mydataset.table-profile_latest_v1`.
    
    
    PROJECT_ID.DATASET_ID.OUTPUT_TABLE_latest_VERSION
    

**Note:** Sensitive Data Protection automatically creates the view. To avoid failures when loading data into the Data Studio, don't edit or delete the view.

## Choose between the output table and the `latest` view

The `latest` view includes only the latest data profile snapshots, while the output table has all data profile snapshots, including snapshots that are outdated. For example, a query on the output table can return multiple [column data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#column-data-profile) for the same column—one for each time that column was profiled.

When choosing between using the output table and the `latest` view in your SQL queries or Data Studio reports, consider the following:

  * The `latest` view is useful if you have data assets that have been reprofiled and you only want to see the latest profiles—not their earlier versions. That is, you want to see the current state of your profiled data.

  * The output table is useful if you want to get a historical view of your profiled data. For example, you're trying to determine whether your organization has ever stored a particular infoType, or you want to see the changes a particular data profile has undergone.




## Sample SQL queries

This section provides example queries that you can use when analyzing data profiles. To run these queries, see [Running interactive queries](https://docs.cloud.google.com/bigquery/docs/running-queries#queries).

In the following examples, replace TABLE_OR_VIEW with either of the following:

  * The name of the output table, which is the table that contains the exported data profiles—for example, `myproject.mydataset.table-profile`.
  * The name of the `latest` view of the output table—for example, `myproject.mydataset.table-profile_latest_v1`.



In either case, you must include the project ID and the dataset ID.

For more information, see Choose between the output table and the `latest` view on this page.

To troubleshoot any errors you encounter, see [Error messages](https://docs.cloud.google.com/bigquery/docs/error-messages).

### List all columns that have a high free-text score and evidence of other infoType matches
    
    
    SELECT
      column_profile.table_full_resource,
      column_profile.COLUMN,
      other_matches.info_type.name,
      column_profile.profile_last_generated
    FROM
       `TABLE_OR_VIEW`
      LEFT JOIN UNNEST(column_profile.other_matches) AS other_matches
    WHERE
      column_profile.free_text_score = 1
      AND ( column_profile.column_info_type.info_type.name>""
        OR ARRAY_LENGTH(column_profile.other_matches)>0 )
    

For information about how to remediate these findings, see [Recommended strategies for mitigating data risk](https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-for-mitigating-data-risk).

For more information about the **Free text score** and **Other infoTypes** metrics, see [Column data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#column-data-profile).

### List all tables that contain a column of credit card numbers
    
    
    SELECT
      column_profile.table_full_resource,
      column_profile.profile_last_generated
    FROM
      `TABLE_OR_VIEW`
    WHERE
      column_profile.column_info_type.info_type.name="CREDIT_CARD_NUMBER"
    

`CREDIT_CARD_NUMBER` is a [built-in infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) that represents a credit card number.

For information about how to remediate these findings, see [Recommended strategies for mitigating data risk](https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-for-mitigating-data-risk).

### List table profiles that contain columns of credit card numbers, US Social Security numbers, and person names
    
    
    SELECT
      table_full_resource,
      COUNT(*) AS count_findings
    FROM (
      SELECT
        DISTINCT column_profile.table_full_resource,
        column_profile.column_info_type.info_type.name
      FROM
        `TABLE_OR_VIEW`
      WHERE
        column_profile.column_info_type.info_type.name IN ('PERSON_NAME',
          'CREDIT_CARD_NUMBER',
          'US_SOCIAL_SECURITY_NUMBER')
      ORDER BY
        column_profile.table_full_resource ) ot1
    GROUP BY
      table_full_resource
      #increase this number to match the total distinct infoTypes that must be present
    HAVING
      count_findings>=3
    

This query uses the following [built-in infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference):

  * `CREDIT_CARD_NUMBER`: represents a credit card number
  * `PERSON_NAME`: represents the full name of a person
  * `US_SOCIAL_SECURITY_NUMBER` represents a US Social Security number



For information about how to remediate these findings, see [Recommended strategies for mitigating data risk](https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-for-mitigating-data-risk).

### List buckets where the sensitivity score is `SENSITIVITY_HIGH`
    
    
    SELECT file_store_profile.file_store_path, file_store_profile.resource_visibility, file_store_profile.sensitivity_score
    FROM `TABLE_OR_VIEW`
    WHERE file_store_profile.sensitivity_score.score ='SENSITIVITY_HIGH'
    ;
    

For more information, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

### List all bucket paths, clusters, and file extensions scanned where the sensitivity score is `SENSITIVITY_HIGH`
    
    
    SELECT file_store_profile.file_store_path, summaries.file_cluster_type.cluster, STRING_AGG(scanned_file_extensions.file_extension) AS scanned_extensions, file_store_profile.profile_last_generated.timestamp
    FROM `TABLE_OR_VIEW`
    LEFT JOIN UNNEST(file_store_profile.file_cluster_summaries) as summaries
    LEFT JOIN UNNEST(summaries.file_store_info_type_summaries) as info_types
    LEFT JOIN UNNEST(summaries.file_extensions_scanned) as scanned_file_extensions
    WHERE file_store_profile.data_source_type.data_source = 'google/storage/bucket'
    AND summaries.sensitivity_score.score ='SENSITIVITY_HIGH'
    GROUP BY 1, 2, 4
    ;
    

For more information, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

### List all bucket paths, clusters, and file extensions scanned where credit card numbers were detected
    
    
    SELECT file_store_profile.file_store_path, summaries.file_cluster_type.cluster, STRING_AGG(scanned_file_extensions.file_extension) AS scanned_extensions
    FROM `TABLE_OR_VIEW`
    LEFT JOIN UNNEST(file_store_profile.file_cluster_summaries) as summaries
    LEFT JOIN UNNEST(summaries.file_store_info_type_summaries) as info_types
    LEFT JOIN UNNEST(summaries.file_extensions_scanned) as scanned_file_extensions
    WHERE file_store_profile.data_source_type.data_source = 'google/storage/bucket'
    AND info_types.info_type.name='CREDIT_CARD_NUMBER'
    GROUP BY 1, 2
    ;
    

`CREDIT_CARD_NUMBER` is a [built-in infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) that represents a credit card number.

For more information, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

### List all bucket paths, clusters, and file extensions scanned where a credit card number, person name, or US Social Security number was detected
    
    
    SELECT file_store_profile.file_store_path, summaries.file_cluster_type.cluster, STRING_AGG(scanned_file_extensions.file_extension) AS scanned_extensions
    FROM `TABLE_OR_VIEW`
    LEFT JOIN UNNEST(file_store_profile.file_cluster_summaries) as summaries
    LEFT JOIN UNNEST(summaries.file_store_info_type_summaries) as info_types
    LEFT JOIN UNNEST(summaries.file_extensions_scanned) as scanned_file_extensions
    WHERE file_store_profile.data_source_type.data_source = 'google/storage/bucket'
    AND info_types.info_type.name IN ('CREDIT_CARD_NUMBER', 'PERSON_NAME', 'US_SOCIAL_SECURITY_NUMBER')
    GROUP BY 1, 2
    ;
    

This query uses the following [built-in infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference):

  * `CREDIT_CARD_NUMBER`: represents a credit card number
  * `PERSON_NAME`: represents the full name of a person
  * `US_SOCIAL_SECURITY_NUMBER` represents a US Social Security number



For more information, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

### Create a view that shows sample findings from only the latest data profiles

By default, the `latest` view of your sample findings table includes the most recent sample findings detected for each data asset. If a data asset is reprofiled and the new profile has no findings, the `latest` sample findings view still retains the findings from the earlier profile.

To see sample findings from only the latest profile of each data asset—so that assets with no findings in their recent profile show no findings—create a custom view that joins the sample findings table with the `latest` view of your data profiles table.

**Important:** The dataset containing your view and the dataset containing the tables referenced by the view must be in the same location.

#### Sample query for table data profiles
    
    
    CREATE OR REPLACE VIEW
      `PROJECT_ID.DATASET_ID.VIEW_ID` AS
    SELECT
      findings_table.*
    FROM
      `FINDINGS_TABLE_PROJECT_ID.FINDINGS_TABLE_DATASET_ID.FINDINGS_TABLE_ID` AS findings_table
    INNER JOIN
      `PROFILES_TABLE_PROJECT_ID.PROFILES_TABLE_DATASET_ID.PROFILES_TABLE_ID_latest_v1` AS profiles_table
    ON
      findings_table.data_profile_resource_name = profiles_table.table_profile.name
      AND findings_table.timestamp.timestamp = profiles_table.table_profile.profile_last_generated.timestamp
    ;
    

#### Sample query for file store data profiles
    
    
    CREATE OR REPLACE VIEW
      `PROJECT_ID.DATASET_ID.VIEW_ID` AS
    SELECT
      findings_table.*
    FROM
      `FINDINGS_TABLE_PROJECT_ID.FINDINGS_TABLE_DATASET_ID.FINDINGS_TABLE_ID` AS findings_table
    INNER JOIN
      `PROFILES_TABLE_PROJECT_ID.PROFILES_TABLE_DATASET_ID.PROFILES_TABLE_ID_latest_v1` AS profiles_table
    ON
      findings_table.data_profile_resource_name = profiles_table.file_store_profile.name
      AND findings_table.timestamp.timestamp = profiles_table.file_store_profile.profile_last_generated.timestamp
    ;
    

## Work with data profiles in Data Studio

To visualize your data profiles in Data Studio, you can use a premade report, or you can create your own.

### Use a premade report

Sensitive Data Protection provides a premade Data Studio report that highlights the rich insights of data profiles. The **Sensitive Data Protection Dashboard** is a multi-page report that gives you a quick high-level view of your data profiles, including breakdowns by risk, by infoType, and by location. Explore the other tabs to see views by geographic region and posture risk, or drill down to specific metrics. You can use this premade report as is, or you can customize it as needed. This is the recommended version of the premade report.

To view the premade report with your data, enter the required values in the following URL. Then, copy the resulting URL to your browser.
    
    
    https://lookerstudio.google.com/c/u/0/reporting/create?c.reportId=c9826374-e016-4c96-a495-7281328375c6&ds.connector=BIG_QUERY&ds.projectId=PROJECT_ID&ds.datasetId=DATASET_ID&ds.tableId=TABLE_OR_VIEW&ds.type=TABLE&ds.useFreshSchema=false
    

Replace the following:

  * PROJECT_ID: the project that contains the output table.
  * DATASET_ID: the dataset that contains the output table.
  * TABLE_OR_VIEW: either of the following:

    * The name of the output table, which is the table that contains the exported data profiles—for example,`myproject.mydataset.table-profile`.
    * The name of the `latest` view of the output table—for example, `myproject.mydataset.table-profile_latest_v1`.

For more information, see Choose between the output table and the `latest` view on this page.




It can take a few minutes for Data Studio to load the report with your data. If you encounter errors or if the report doesn't load, see Troubleshoot errors with the premade report on this page.

In the following example, the dashboard shows that low-sensitivity and high-sensitivity data are present in multiple countries around the world.

![Premade report](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/premade-report.png)

### Earlier version of the premade report

The first version of the premade report is still available at the following address:
    
    
    https://lookerstudio.google.com/c/u/0/reporting/create?c.reportId=907a2b73-ffe4-40b2-b9a1-c2aa0bbd69fd&ds.connector=BIG_QUERY&ds.projectId=PROJECT_ID&ds.datasetId=DATASET_ID&ds.tableId=TABLE_OR_VIEW&ds.type=TABLE&ds.useFreshSchema=false
    

### Create a report

[Data Studio](https://lookerstudio.google.com/overview) lets you create interactive reports. In this section, you create a simple table report in Data Studio that is based on the data profiles exported to your output table in BigQuery.

Make sure you have the project ID, dataset ID, and table ID of the output table or the `latest` view readily available. You need them to perform this procedure.

This example shows you how to create a report containing a table that shows each [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) reported in your data profiles and its corresponding frequency.

In general, you incur [BigQuery usage costs](https://cloud.google.com/bigquery/pricing) when accessing BigQuery through Data Studio. For more information, see [Visualizing BigQuery data using Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-data-studio).

To create a report, do the following:

  1. Open [Data Studio](https://lookerstudio.google.com/) and log in.
  2. Click **Blank Report**.
  3. On the **Connect to data** tab, click the **BigQuery** card.
  4. If prompted, authorize Data Studio to access your BigQuery projects.
  5. Connect to your BigQuery data:

     1. For **Project** , select the project that contains the output table. You can search for the project in the **Recent projects** , **My projects** , and **Shared projects** tabs.
     2. For **Dataset** , select the dataset that contains the output table.
     3. For **Table** , select either the output table or the `latest` view of the output table.

For more information, see Choose between the output table and the `latest` view on this page.

     4. Click **Add**.

     5. In the dialog that appears, click **Add to report**.

  6. To add a table that shows each infoType reported and its corresponding frequency (record count), follow these steps:

     1. Click **Add a chart**.
     2. Select a table style.
     3. Click the area where you want to position the chart.

The chart appears in table format.

     4. Resize the table as needed.

As long as the table is selected, its properties appear in the **Chart** pane.

     5. In the **Chart** pane, on the **Setup** tab, remove any preselected dimensions and metrics.

     6. For **Dimension** , add `column_profile.column_info_type.info_type.name` or `file_store_profile.file_cluster_summaries.file_store_info_type_summaries.info_type.name`.

These examples provide data at the column and file cluster levels. You can try other dimensions as well. For example, you can use table-level and bucket-level dimensions.

     7. For **Metric** , add **Record Count**.

The resulting table looks similar to the following:

![A table showing the infoTypes detected and their corresponding
record counts](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/infotype-frequency.png)




Learn more about [tables in Data Studio](https://support.google.com/looker-studio/answer/7189044#zippy=%2Cin-this-article).

## Troubleshoot errors with the premade report

If you see any errors, missing controls, or missing charts when loading the premade report, make sure that the premade report is using the latest fields:

  * If your premade report is connected to the output table, confirm that this table is attached to an active discovery scan configuration. To view the settings of your scan configurations, see [View a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-config).

  * If your premade report is connected to the `latest` view, confirm that this view is still present in BigQuery. If it is present, try making a change to the view. Alternatively, make a copy of the view and connect the premade report to that copy. For more information about the `latest` view, see [The `latest` view](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#latest-view) on this page.




If you continue to see errors after trying these steps, contact [Cloud Customer Care](https://docs.cloud.google.com/sensitive-data-protection/docs/getting-support).

## What's next

Learn about actions you can take to [remediate](https://docs.cloud.google.com/sensitive-data-protection/docs/best-practices-for-mitigating-data-risk) data profile findings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
