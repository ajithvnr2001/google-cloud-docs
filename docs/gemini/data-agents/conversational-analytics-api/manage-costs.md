---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs/
title: Manage BigQuery costs for Conversational Analytics API agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:54.934379+00:00
---

# Manage BigQuery costs for Conversational Analytics API agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Manage BigQuery costs for Conversational Analytics API agents Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor and manage BigQuery costs for your Conversational Analytics API agents, which incur costs by running queries against your BigQuery data. You can use the following methods to control spending and prevent unexpected expenses:

  * Set quotas for projects and users to apply broad spending limits for an entire project or for individual users.
  * Limit costs for individual queries by setting a `big_query_max_billed_bytes` value in the agent's configuration.



## Before you begin

Before you implement the cost controls that are described on this page, you must meet the following requirements:

  * You must have a Google Cloud project with billing enabled.
  * You must have the necessary Identity and Access Management (IAM) permissions to manage quotas and billing for your Google Cloud project.



## Set quotas for projects and users

You can set spending limits for a Google Cloud project or for individual users by applying standard [BigQuery quotas](https://docs.cloud.google.com/bigquery/quotas). These limits help you control overall costs and prevent individual users from overspending.

For agents that might incur high costs, such as an agent that is built on a very large or unpartitioned table, the recommended practice is to first isolate the agent in its own dedicated project. You can then apply a project-level quota to cap the project's maximum daily cost, a user-level quota to ensure fair use among users, or both project-level and user-level quotas.

### Set up a dedicated project for your agent

To set up a dedicated project for your Conversational Analytics API agent or agents, follow these steps:

  1. In the Google Cloud console, [create a new Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project). This project will be dedicated to your agent or agents.
  2. Make sure that billing is enabled for the new project.
  3. Confirm that the agent is configured to use this new project for billing. When you configure the agent, you'll need to specify the project ID of this new project.



### Set a quota for the project

After you have set up a dedicated Google Cloud project, you can apply a quota to control costs for the entire project. To set a project-level quota, follow these steps:

  1. In the Google Cloud project for your agent, navigate to **IAM & Admin > Quotas**.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. Filter for the BigQuery API service, and select the **Query usage per day** quota.

  3. Edit the quota to your chosen daily limit (for example, 10 TiB). This limit creates a hard stop that prevents the project from exceeding the specified daily cost.




### Set a quota for users

To prevent any individual user from generating a large bill, you can set a per-user quota by following these steps:

  1. In the Google Cloud project for your agent, navigate to **IAM & Admin > Quotas**.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. Filter for the **BigQuery API** service and select the **Query usage per day per user** quota.

  3. Edit the quota to your chosen daily limit (for example, 1 TiB per user per day). This limit ensures that no single user can consume an excessive amount of resources.




## Limit costs for individual queries

To prevent any individual user query from generating a large, unexpected bill, you can set a per-query cost limit by configuring the `big_query_max_billed_bytes` field in your agent's [data source options](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#DatasourceOptions).

Before the agent runs a query, it performs a trial run to estimate the cost. If the estimated bytes to be scanned exceed the `big_query_max_billed_bytes` value, the query fails without incurring a charge, and the agent returns an error message.

You can set the `big_query_max_billed_bytes` parameter within the `published_context` or `staging_context` fields when you create or configure an agent [with HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create_a_data_agent) or [with the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#create_a_data_agent). The following sample JSON code illustrates a request that configures a 100 MiB limit for an agent:
    
    
    {
      "data_analytics_agent": {
        "published_context": {
          "system_instruction": "This agent provides information about street trees in San Francisco, including their species, location, and planting date.",
          "options": {
            "datasource": {
              "big_query_max_billed_bytes": "104857600"
            }
          },
          "datasource_references": {
            "bq": {
              "tableReferences": [
                {
                  "projectId": "bigquery-public-data",
                  "datasetId": "san_francisco",
                  "tableId": "street_trees"
                }
              ]
            }
          }
        }
      }
    }
    

In this example, the `big_query_max_billed_bytes` parameter is set to `104857600` bytes (100 MiB). This value establishes a limit for any queries that are run by the `sample-agent-id` agent on the `bigquery-public-data.san_francisco.street_trees` BigQuery table.

## Limitations

Keep the following limitations in mind when you're managing costs for your Conversational Analytics API agents:

  * These cost management tools apply only to projects that use [on-demand billing](https://cloud.google.com/bigquery/pricing#on_demand_pricing) and not to projects that use [slot reservations](https://cloud.google.com/bigquery/pricing#reservations_pricing).
  * Setting quotas for individual agents isn't supported. As described in Set quotas for projects and users, the recommended practice is to isolate the agent in its own project, and then apply project-level or per-user quotas to that project.
  * Tracking costs for individual agents by using [BigQuery labels](https://docs.cloud.google.com/bigquery/docs/labels-intro) isn't supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
