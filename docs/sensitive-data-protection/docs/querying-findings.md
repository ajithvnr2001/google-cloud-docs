---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings/
title: Query Sensitive Data Protection findings in BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:53.301221+00:00
---

# Query Sensitive Data Protection findings in BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/querying-findings/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Query Sensitive Data Protection findings in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This page provides example queries that you can use to analyze Sensitive Data Protection findings that were exported to BigQuery.

You can [configure an inspection job or job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers) to save the findings to BigQuery. Doing so lets you query the findings for further analysis. When your findings are exported to BigQuery, the data is written to either a new or existing table.

For more information about all the actions that Sensitive Data Protection can perform after inspection, see the [Actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) conceptual topic.

For more information about running queries, see the following:

  * [Run interactive and batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries)
  * [Using the `bq` command-line tool](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool)



## Columns of the BigQuery table

The columns of the table of exported findings are based on the attributes of the [`Finding`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2#finding) object.

## Link results back to the rows containing the findings

If you are [configuring inspection of a BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspect_a_table), you can set up the job or job trigger such that the exported findings will contain the row's identifiers. Doing so lets you link the inspection findings back to the rows that contain them.

In the inspection job or job trigger, set the following fields to the names of the columns that uniquely identify each row in the table—that is, the columns that serve the purpose of a primary key:

  * If you're using the Google Cloud console, set the **Identifying fields (comma separated)** field.
  * If you're using the DLP API, set the [`identifyingFields`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.identifying_fields) property.



When the inspection is done and the findings are exported to BigQuery, each finding will contain the corresponding values of the columns that you specified. Those values will be in the `location.content_locations.record_location.record_key.id_values` field. You can then use those values to link the finding back to the specific row in the inspected BigQuery table.

**Note:** The [`rowIndex`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#tablelocation) property is not intended for use in BigQuery inspection jobs.

## Sample queries

You can use the following sample queries to analyze your findings. You can also use the queries in a visualization tool such as [Data Studio](https://www.google.com/analytics/data-studio/). These queries are provided to help you get started querying your findings data.

In each of the following queries, replace the following:

  * `PROJECT_ID`: the project identifier
  * `DATASET`: the BigQuery dataset name
  * `TABLE_ID`: the table ID



### Select the count of each infoType

###  Google Cloud console 
    
    
    SELECT info_type.name,
    COUNT(info_type.name) AS count
    FROM `PROJECT_ID.DATASET.TABLE_ID`
    GROUP BY info_type.name
    ORDER BY count DESC;

###  Command-line 
    
    
    bq query --use_legacy_sql=false ' SELECT info_type.name,
    COUNT(info_type.name) AS count
    FROM `PROJECT_ID.DATASET.TABLE_ID`
    GROUP BY info_type.name ORDER BY count DESC;'

### Select the count of each infoType by day

###  Google Cloud console 
    
    
    SELECT info_type.name, cast(TIMESTAMP_SECONDS(create_time.seconds) as date) as day,
    COUNT(locations.container_name) AS count
    FROM `PROJECT_ID.DATASET.TABLE_ID`,
    UNNEST(location.content_locations) AS locations
    GROUP BY info_type.name, day
    ORDER BY count DESC;

###  Command-line 
    
    
    bq query --use_legacy_sql=false ' SELECT info_type.name,
    cast(TIMESTAMP_SECONDS(create_time.seconds) as date) as day,
    COUNT(locations.container_name) AS count FROM `PROJECT_ID.DATASET.TABLE_ID`,
    UNNEST(location.content_locations) AS locations
    GROUP BY info_type.name, day ORDER BY count DESC;'

### Selects the count of each infoType in each container

###  Google Cloud console 
    
    
    SELECT info_type.name, locations.container_name,
    COUNT(locations.container_name) AS count
    FROM `PROJECT_ID.DATASET.TABLE_ID`,
    UNNEST(location.content_locations) AS locations
    GROUP BY locations.container_name, info_type.name
    ORDER BY count DESC;

###  Command-line 
    
    
    bq query --use_legacy_sql=false ' SELECT info_type.name, locations.container_name,
    COUNT(locations.container_name) AS count FROM `PROJECT_ID.DATASET.TABLE_ID`,
    UNNEST(location.content_locations) AS locations
    GROUP BY locations.container_name,info_type.name ORDER BY count DESC;'

### Selects the finding types found for each column of a table

This query will group all the findings by column name and is intended to work on findings from a BigQuery inspection job. This query is useful if you are trying to identify the likely types for a given column. You can adjust settings by modifying the WHERE and HAVING clauses. For example, if multiple table results are included in your findings table, you can limit these to just one job run or one table name.

###  Google Cloud console 
    
    
    SELECT
      table_counts.field_name,
      STRING_AGG( CONCAT(" ",table_counts.name," [count: ",CAST(table_counts.count_total AS String),"]")
      ORDER BY
        table_counts.count_total DESC) AS infoTypes
    FROM (
      SELECT
        locations.record_location.field_id.name AS field_name,
        info_type.name,
        COUNT(*) AS count_total
      FROM
        `PROJECT_ID.DATASET.TABLE_ID`,
        UNNEST(location.content_locations) AS locations
      WHERE
        (likelihood = 'LIKELY'
          OR likelihood = 'VERY_LIKELY'
          OR likelihood = 'POSSIBLE')
      GROUP BY
        locations.record_location.field_id.name,
        info_type.name
      HAVING
        count_total>200 ) AS table_counts
    GROUP BY
      table_counts.field_name
    ORDER BY
      table_counts.field_name

The above query might produce a result like this for a sample table, where the infoTypes column tells us how many instances of each infoType was found for that given column.

field_name | infoTypes  
---|---  
`field1` | `CUSTOM_USER_US [count: 7004]`, `CUSTOM_USER_EU [count: 2996]`  
`field2` | `US_VEHICLE_IDENTIFICATION_NUMBER [count: 9597]`  
`field3` | `EMAIL_ADDRESS [count: 10000]`  
`field4` | `IP_ADDRESS [count: 10000]`  
`field5` | `PHONE_NUMBER [count: 7815]`  
`field6` | `US_SOCIAL_SECURITY_NUMBER [count: 10000]`  
`field7` | `CREDIT_CARD_NUMBER [count: 10000]`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
