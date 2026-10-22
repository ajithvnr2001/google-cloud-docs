---
url: https://docs.cloud.google.com/bigquery/docs/repository-intro/
title: Introduction to repositories \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:10.738139+00:00
---

# Introduction to repositories  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/repository-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to repositories

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To provide feedback or ask questions that are related to this Preview feature, contact [bigquery-repositories-feedback@google.com](mailto:bigquery-repositories-feedback@google.com).

This document describes BigQuery repositories, which provide version control for the files you use within BigQuery. These repositories help you track changes to BigQuery assets like queries and notebooks, collaborate with your team, and revert to previous versions.

BigQuery repositories function as Git repositories. You can use the built-in Git capabilities of BigQuery or connect to an existing third-party Git repository. Within each repository, you create [workspaces](https://docs.cloud.google.com/bigquery/docs/workspaces-intro) to edit the code stored there.

To view repositories, on the BigQuery page, in the left pane, click explore **Explorer** , and then click **Repositories**. Your repositories are displayed in alphabetical order in a new tab in the details pane.

**Important:** If you create an asset in a BigQuery repository—for example, a query, notebook (including a notebook with an Apache Spark job), BigQuery pipeline, or Dataform workflow—you cannot schedule it for execution in a BigQuery repository. For scheduling and executing Dataform workflows, you need to use Dataform repositories. For scheduling queries and notebooks, use BigQuery Studio. For more information, see [Scheduling queries](https://docs.cloud.google.com/bigquery/docs/scheduling-queries), [Schedule notebooks](https://docs.cloud.google.com/bigquery/docs/orchestrate-notebooks), and [Schedule pipelines](https://docs.cloud.google.com/bigquery/docs/schedule-pipelines).

## Third-party repositories

You can connect a BigQuery repository to a third-party Git repository if you choose. In this case, the third-party repository stores the repository code instead of BigQuery. BigQuery interacts with the third-party repository to allow you to edit and execute its contents in a BigQuery workspace. Depending on the type of repository you choose, you can connect to a third-party repository by using SSH or HTTPS.

The following table lists supported Git providers and the connection methods that are available for their repositories:

Git provider | Connection method  
---|---  
Microsoft Azure DevOps Services | SSH  
Bitbucket | SSH  
GitHub | SSH or HTTPS  
GitLab | SSH or HTTPS  
  
For more information, see [Connect to a third-party repository](https://docs.cloud.google.com/bigquery/docs/repositories#connect-third-party) and [Manage code with BigQuery Studio Git repositories](https://docs.cloud.google.com/bigquery/docs/git-repositories).

## Service account

All BigQuery repositories are connected to the default Dataform service agent. This service account is derived from your project number in the following format:
    
    
    service-YOUR_PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
    

[Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) is enforced and requires all repositories to use a custom service account or user credentials for a Google Account to schedule pipelines and notebooks.

## Locations

You can create repositories in all [BigQuery Studio locations](https://docs.cloud.google.com/bigquery/docs/locations#bqstudio-loc).

## Quotas

[Dataform quotas](https://docs.cloud.google.com/dataform/docs/quotas#quotas) apply to use of BigQuery repositories.

## Pricing

You are not charged for creating, updating, or deleting a repository.

For more information on BigQuery pricing, see [Pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * Learn how to [create repositories](https://docs.cloud.google.com/bigquery/docs/repositories).
  * Learn how to [create workspaces](https://docs.cloud.google.com/bigquery/docs/workspaces).
  * Learn how to [manage code with BigQuery Studio Git repositories](https://docs.cloud.google.com/bigquery/docs/git-repositories).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
