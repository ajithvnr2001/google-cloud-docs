---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/visualizing_re-id_risk/
title: Visualizing re-identification risk using Data Studio \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:04.358381+00:00
---

# Visualizing re-identification risk using Data Studio  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/visualizing_re-id_risk/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Visualizing re-identification risk using Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows how to measure [_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity) of a dataset using Sensitive Data Protection and visualize it in Data Studio. By doing so, you'll also be able to better understand risk and help evaluate the trade-offs in utility you might be making if you redact or de-identify data.

**Important:** You can also visualize your re-identification risk analysis results using Sensitive Data Protection in the Google Cloud console, without needing to use Data Studio. This built-in feature produces a similar visual representation to the procedure described in this topic, without having to configure another product. For more information, see [View _k_ -anonymity job results](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity#viewing-results) or [View _l_ -diversity job results](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity#viewing-results).

Though the focus of this topic is on visualizing the _k_ -anonymity re-identification risk analysis metric, you can also visualize the [_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-l-diversity) metric using the same methods.

This topic assumes you're already familiar with the [concept of _k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity) and its utility for assessing the re-identifiability of records within a dataset. It will also be helpful to be at least somewhat familiar with how to [compute _k_ -anonymity using Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity), and with using [Data Studio](https://lookerstudio.google.com/).

## Introduction

De-identification techniques can be helpful in protecting your subjects' privacy while you process or use data. But how do you know if a dataset has been sufficiently de-identified? And how will you know whether your de-identification has resulted in too much data loss for your use case? That is, how can you compare re-identification risk with the utility of the data to help make data-driven decisions?

Calculating the _k_ -anonymity value of a dataset helps answer these questions by assessing the re-identifiability of the dataset's records. Sensitive Data Protection contains built-in functionality to calculate a _k_ -anonymity value on a dataset based on quasi-identifiers that you specify. This helps enable you to quickly evaluate whether de-identifying a certain column or combination of columns will result in a dataset that is more or less likely to be re-identified.

**Note:** _Quasi-identifiers_ are database columns that could potentially be used in concert with other data to re-identify an individual. For more information, see [Risk analysis terms and techniques](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#risk_analysis_terms_and_techniques) in the [Risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) conceptual topic.

## Example dataset

Following are the first few rows of a large example dataset.

`user_id` | `age` | `title` | `score`  
---|---|---|---  
`602-61-8588` | `24` | `Biostatistician III` | `733`  
`771-07-8231` | `46` | `Executive Secretary` | `672`  
`618-96-2322` | `69` | `Programmer I` | `514`  
`...` | `...` | `...` | `...`  
  
For the purposes of this tutorial, `user_id` will not be addressed, as the focus is on quasi-identifiers. In a real-world scenario, you would want to ensure that `user_id` is redacted or [_tokenized_](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization) appropriately. The `score` column is proprietary to this dataset, and it's unlikely an attacker would be able to learn it by other means, so you will not include it in the analysis. Your focus will be on the remaining `age` and `title` columns, with which an attacker could potentially learn about an individual through other sources of data. The questions you're trying to answer for the dataset are:

  * What effect will the two quasi-identifiers—`age` and `title`—have on the overall re-identification risk of the de-identified data?
  * How will applying a de-identification transformation affect this risk?



You want to be sure that the combination of `age` and `title` won't map to a small number of users. For example, suppose there is only one user in the dataset whose title is Programmer I and who is age 69. An attacker might be able to cross-reference that information with demographics or other available information, figure out who the person is, and learn the value of their score. For more information about this phenomenon, see the "[Entity IDs and computing _k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity)" section in the [Risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) conceptual topic.

## Step 1: Calculate k-anonymity on the dataset

First, use Sensitive Data Protection to calculate _k_ -anonymity on the dataset by sending the following JSON to the [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. Within this JSON, you set the [entity ID](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#entity-ids) to the `user_id` column, and identify the two quasi-identifiers as both the `age` and `title` columns. You're also instructing Sensitive Data Protection to save the results to a new BigQuery table.

**Note:** You can also calculate _k_ -anonymity on the dataset using [Sensitive Data Protection in the Google Cloud console](https://console.cloud.google.com/security/sensitive-data-protection) or programmatically by using a [client library](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries).

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/dlp-demo-2/dlpJobs
    
    {
      "riskJob": {
        "sourceTable": {
          "projectId": "dlp-demo-2",
          "datasetId": "dlp_testing",
          "tableId": "dlp_test_data_kanon"
        },
        "privacyMetric": {
          "kAnonymityConfig": {
            "entityId": {
              "field": {
                "name": "id"
              }
            },
            "quasiIds": [
              {
                "name": "age"
              },
              {
                "name": "job_title"
              }
            ]
          }
        },
        "actions": [
          {
            "saveFindings": {
              "outputConfig": {
                "table": {
                  "projectId": "dlp-demo-2",
                  "datasetId": "dlp_testing",
                  "tableId": "test_results"
                }
              }
            }
          }
        ]
      }
    }

Once the _k_ -anonymity job has completed, Sensitive Data Protection sends the job results to a BigQuery table named `dlp-demo-2.dlp_testing.test_results`.

## Step 2: Connect results to Data Studio

Next, you'll connect the BigQuery table you produced in Step 1 to a new report in Data Studio.

  1. Open [Data Studio](https://lookerstudio.google.com/).

[Open Data Studio](https://lookerstudio.google.com/)

  2. Click **Create** > **Report**.

  3. In the **Add data to report** pane under **Connect to data** , click **BigQuery**. You may need to authorize Data Studio to access your BigQuery tables.

  4. In the column picker, select **My projects**. Then choose the project, dataset, and table. When you're done, click **Add**. If you see a notice that you're about to add data to this report, click **Add to report**.




The _k_ -anonymity scan results have now been added to the new Data Studio report. In the next step, you'll create the chart.

## Step 3: Create the chart

Do the following to insert and configure the chart:

  1. In Data Studio, if a table of values appears, select it and press Delete to remove it.
  2. On the **Insert** menu, click **Combo chart**.
  3. Click and draw a rectangle on the canvas where you want the chart to appear.



Next, configure the chart data under the **Data** tab so that the chart shows the effect of varying the size and value ranges of buckets:

  1. Clear the fields under the following headings by pointing to each field and clicking the cancel X, as shown here:  
![Detail of timestamp field with delete button
   enabled.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/visualizing_re-id_risk2.png)
     * **Date Range Dimension**
     * **Dimension**
     * **Metric**
     * **Sort**
  2. With all fields cleared, drag the **upper_endpoint** field from the **Available fields** column to the **Dimension** heading.
  3. Drag the **upper_endpoint** field to the **Sort** heading, and then select **Ascending**.
  4. Drag both the **bucket_size** and **bucket_value_count** fields to the **Metric** heading.
  5. Point to the icon to the left of the **bucket_size** metric and an editEdit icon appears. Click the editEdit icon, and then do the following: 
     1. In the **Name** field, type `Unique row loss`.
     2. Under **Type** , choose **Percent**.
     3. Under **Comparison calculation** , choose **Percent of total**.
     4. Under **Running calculation** , choose **Running sum**.
  6. Repeat the previous step for the **bucket_value_count** metric, but in the **Name** field, type `Unique quasi-identifier combination loss`.



Once you're done, the column should appear as shown here:

![Screen shot of fields list.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/visualizing_re-id_risk3.png)

Finally, configure the chart to display a line chart for both metrics:

  1. Click the **Style** tab in the pane on the right of the window.
  2. For both Series #1 and Series #2, choose **Line**.
  3. To view the final chart on its own, click the visibility**View** button in the upper-right corner of the window.



Following is an example chart after completing the preceding steps.

![Final chart](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/visualizing_re-id_risk4.png)

## Interpreting the chart

The generated chart plots, on the _y_ -axis, the potential percentage of data loss for both unique rows and unique quasi-identifier combinations to achieve, on the _x_ -axis, a _k_ -anonymity value.

Higher _k_ -anonymity values indicate less risk of re-identification. To achieve higher _k_ -anonymity values, however, you would need to remove higher percentages of the total rows and higher unique quasi-identifier combinations, which might decrease the utility of the data.

Thankfully, dropping data is not your only option to reduce re-identification risk. Other de-identification techniques can strike a better balance between loss and utility. For example, to address the kind of data loss associated with higher _k_ -anonymity values and this dataset, you could try bucketing ages or job titles to reduce the uniqueness of age/job title combinations. For example, you could try bucketing ages in ranges of 20-25, 25-30, 30-35, and so on. For more information about how to do this, see [Generalization and bucketing](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing) and [De-identifying sensitive data in text content](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
