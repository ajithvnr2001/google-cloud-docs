---
url: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-spanner/
title: Connect to Google Cloud Spanner \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:24.553089+00:00
---

# Connect to Google Cloud Spanner  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-cloud-spanner/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Cloud Spanner Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Spanner connector lets you access data from Google Cloud Spanner within Data Studio. Cloud Spanner is an enterprise-grade, globally-distributed, and strongly consistent database service built for the cloud specifically to combine the benefits of relational database structure with non-relational horizontal scale.

Cloud Spanner is a paid service. [Learn more about pricing](https://cloud.google.com/spanner/pricing).

## How to connect to Google Cloud Spanner

A Data Studio data source can connect to Cloud Spanner databases using [Google Standard SQL query syntax](https://docs.cloud.google.com/spanner/docs/query-syntax).

### To connect

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Select the **Cloud Spanner** connector.
  4. If asked, authorize Data Studio to access your data.
  5. On the left, set up the connection to your database. You'll need to provide: 
     1. Project ID
     2. Instance ID (see the _Notes_ section to find out how to list your instance configurations).
     3. Database ID
  6. In the text field, enter your SQL query.
  7. In the upper right, click **CONNECT**.



In a moment, the data source fields list page appears. Click **CREATE REPORT** to start visualizing your data.

## Notes

### List instance configurations

The [Cloud SDK](https://cloud.google.com/sdk) command-line tool lets you interact with Cloud Spanner. For example, the following command lists the regional and multi-region instance configurations that are available for your project:
    
    
    gcloud spanner instance-configs list
    
    

Regional configurations distribute data in a single region, while multi-region configurations distribute data geographically across multiple regions. Learn more about [Instances](https://docs.cloud.google.com/spanner/docs/instances).

Data Studio maps your database's built-in data types to a unified set of [data types](https://docs.cloud.google.com/data-studio/data-types). If Data Studio encounters a column in your table or query of an unsupported type, it won't create a field for that column. 

## Limits of the Spanner connector

  * The response size from Spanner is limited to 10 MB. See the [Spanner Limits article](https://cloud.google.com/spanner/quotas) for other limits.
  * Column headers (field names) must use ASCII characters only. Non-ASCII characters aren't supported.



## Troubleshooting

See the [Data Studio troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) for a list of common error messages and steps to resolve them.

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Google Cloud Platform overview](https://cloud.google.com/docs/overview/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
