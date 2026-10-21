---
url: https://docs.cloud.google.com/datastream/docs/best-practices-stream-data/
title: Use Datastream and Dataflow to stream data into BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:44.325143+00:00
---

# Use Datastream and Dataflow to stream data into BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/best-practices-stream-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Use Datastream and Dataflow to stream data into BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you'll find best practices for using [Datastream and Dataflow to stream data into BigQuery](https://docs.cloud.google.com/datastream/docs/implementing-datastream-dataflow-analytics).

## Partition replica datasets on user defined keys

The staging dataset in BigQuery is partitioned automatically. However, by default, the replica dataset isn't partitioned because the partition keys on the replica tables must be defined based on specific business logic, instead of being enforced by Datastream and Dataflow.

For each table in the replica dataset that needs partitioning:

  1. [Stop and drain the Dataflow job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#stopping_a_job)

  2. Use the SQL editor in BigQuery to run the following SQL script for each table in the replica dataset. For this example, the `actor` table in the `datastream_cdc` dataset has a `last_update` column that we want to set as our partition key. By running the script, you recreate the table with the correct partition key.
         
         create table '[BigQuery_PROJECT_ID].datastream_cdc.actor_new' partition by date(last_update)
         as SELECT * FROM '[BigQuery_PROJECT_ID].datastream_cdc.actor'
         
         drop table '[BigQuery_PROJECT_ID].datastream_cdc.actor'
         
         alter table '[BigQuery_PROJECT_ID].datastream_cdc.actor_new' rename to 'actor'

  3. Use the [Datastream to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#datastream-to-bigquery) to recreate a Dataflow job.




## Run user-defined functions to manipulate event data

You can use the [Datastream to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#datastream-to-bigquery) to run a Javascript user-defined function. To do this, first, place a file containing the function in a specific location within Cloud Storage. Then, do the following:

  * Use the `javascriptTextTransformGcsPath` parameter in the template to specify the location of the file in Cloud Storage that contains your user-defined function.
  * Use the `javascriptTextTransformFunctionName` parameter to specify the name of the Javascript function that you want to call as your user-defined function.



For example, you can run a user-defined function to retain deleted records in the tables of the replica dataset within BigQuery. This process is known as a soft delete.

To achieve this, create a function that copies the value of the `_metadata_deleted` column into a new column named `is_deleted`, and then resets the `_metadata_deleted` column value to `false`. This causes the Dataflow job to ignore the delete events and retain the deleted records when updating the replica dataset in BigQuery.

Here's the sample code for this user-defined function:
    
    
    /**
    * This function changes the behavior of the Datastream to
    * BigQuery template to allow soft deletes.
    * @param {string} messageString from DatastreamIO data
    * @return {string} same as an input message with an added property
    */
    function transform(messageString) {
       // messageString is a JSON object as a string
       var messageJson = JSON.parse(messageString);
        // Moving the deleted flag to a new column will cause the pipeline to soft delete data.
       messageJson['is_deleted'] = messageJson['_metadata_deleted'];
       messageJson['_metadata_deleted'] = false;
        return JSON.stringify(messageJson);
     }

## Set the merge frequency

Use the `mergeFrequencyMinutes` parameter of the [Datastream to BigQuery template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#datastream-to-bigquery) to set the merge frequency. This is the number of minutes between merges for a given table in the replica dataset in BigQuery. While historical data is being backfilled, we recommend that you keep the merge frequency low (12 or 24 hours) to keep costs under control.

For example, if you set the value of this parameter to 10 minutes, then Dataflow will run the job that uses the template every 10 minutes. However, the first time that the job runs, there'll be a 5-minute delay. For this example, if the job runs at 9:14 AM, then the first merge will occur at 9:29 AM (10 minutes for the merge and 5 minutes for the delay). The second merge will occur at 9:39 AM, and all subsequent merges will occur in 10-minute intervals (9:49 AM, 9:59AM, 10:09 AM, and so on).

If you set the merge frequency to 60 minutes, then the job will run on the hour, after a 5-minute delay for the initial running of the job. If the job is scheduled to run at 10 AM, then it will actually run at 10:05 AM because of the 5-minute delay. All subsequent merges will occur in 60-minute intervals (11:05 AM, 12:05 PM, 1:05 PM, and so on).

Whether as a result of controlling costs or for other reasons, you may not be able to perform a merge at a frequency that meets your business needs. You may not have the freshest data. To access the freshest data, create a view on top of the tables of the staging and replica datasets in BigQuery, where the view mimics the merge. This view is created as one logical table (for both the staging and replica datasets). If the merge frequency is low, and you need faster access to the data, then use the view.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
