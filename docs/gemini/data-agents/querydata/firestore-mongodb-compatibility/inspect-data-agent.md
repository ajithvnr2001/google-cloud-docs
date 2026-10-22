---
url: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/inspect-data-agent/
title: Test QueryData in Firestore Studio \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:49.788032+00:00
---

# Test QueryData in Firestore Studio  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/inspect-data-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)



Send feedback 

#  Test QueryData in Firestore Studio Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to test QueryData and update the context set file. You can test QueryData's ability to generate MongoDB-compatible Query Language (MQL) queries from natural language questions. If a generated query is not accurate, you can update the context set file.

To learn about context sets, see [Context sets overview](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview). 

## Before you begin

Make sure that a context set is already created and the context set file is uploaded to the QueryData agent. For more information, see [Manage context sets in Firestore Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/manage-data-agents).

To download, update, and upload context set files, make sure that the IAM user has the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role on the project. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).

## Test QueryData

To test a QueryData, perform the following steps:

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database to which you added a context set. Only Firestore with MongoDB compatibility is supported.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , click **View actions** next to the context set you're using.

  5. Click **Test context set**.

  6. In the query editor, click **Generate Query** to open the **Help me code** panel.

  7. Enter a natural language question in the editor to generate a MQL query, and click **Generate**.

  8. Review the MQL query for accuracy.




## Download and update a context set

If you are not satisfied with the generated MQL query for a natural language question, download the existing context set file. You can then review and update the query template, and reupload the updated context file to the agent.

To download and update a context set, perform the following steps:

  1. In the **Explorer pane** , click **View actions**.
  2. Click **Download context file**.
  3. Follow steps in [Build contexts sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets) to update context with additional query pairs.
  4. In the **Explorer pane** , click **View actions** next to the context set you're using.
  5. Click **Edit context set**.
  6. Click **Browse** in the **Upload context set file** section, and select the updated context set file.
  7. Click **Save** to update the context set.



After you are satisfied with the accuracy of your responses, you can use the `QueryData` endpoint to connect your application to the context set.

**Note:** After you upload the updated context set file, it overwrites the existing context set.

## Find the context set ID

To connect a data application to the QueryData agent, you need the context set's ID.

  1. In the Google Cloud console, go to the Firestore page.

[Go to Firestore](https://console.cloud.google.com/firestore)

  2. Select a database to which you added a context set.

  3. In the navigation menu, click **Firestore Studio**. 

  4. In the **Explorer pane** , click **View actions** next to the context set you're using.

  5. Click **Edit context set**.

  6. Note the context ID in **Context set ID**. The context set ID format is similar to `projects/data-agents-project/locations/us-central1/contextSets/bdf_pg_all_templates`.




## Connect QueryData to application

Set the context set ID in the `QueryData` method call to provide authored context for database data sources such as AlloyDB, Spanner, Cloud SQL, Cloud SQL for PostgreSQL, and Firestore. For more information, see [Define data agent context for database data sources](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/data-agent-authored-context-databases).

After testing the context set, you can reference the database data source in your `QueryData` call.

### Example `QueryData` request with authored context

The following example shows a `QueryData` request using the `firestore_reference` (Firestore with MongoDB compatibility) data source. The `agent_context_reference.context_set_id` field is used to link to pre-authored context stored in the database.
    
    
    {
      "parent": "projects/context-set-project/locations/us-central1",
      "prompt": "How many accounts in the Prague region are eligible for loans?",
      "context": {
        "datasource_references": [
          {
            "firestore_reference": {
              "database_reference": {
                "project_id": "context-set-project",
                "region": "us-central1",
                "database_id": "financial"
              },
              "agent_context_reference": {
                "context_set_id": "projects/context-set-project/locations/us-central1/contextSets/bdf_pg_all_templates"
              }
            }
          }
        ]
      },
      "generation_options": {
        "generate_query_result": true,
        "generate_natural_language_answer": true,
        "generate_disambiguation_question": true,
        "generate_explanation": true
      }
    }

The request body contains the following fields:

  * `prompt`: The natural language question from the end user.
  * `context`: Contains information about the data sources. 
    * `datasource_references`: Specifies the data source type. 
      * `firestore_reference`: Required when querying the database. This field changes based on the database you are querying. 
        * `database_reference`: Specifies information related to your database instance. 
          * `project_id`: The project ID of the database.
          * `region`: The region of the database.
          * `database_id`: The ID of the database.
        * `agent_context_reference`: Links to authored context in the database. 
          * `context_set_id`: The complete context set ID of the context stored in the database. For example, `projects/context-set-project/locations/us-central1/contextSets/bdf_gsql_gemini_all_templates`.
  * `generationOptions`: Configures the type of output to generate. 
    * `generate_query_result`: Set to true to generate and return the query results.
    * `generate_natural_language_answer`: Optional. If set to true, generates a natural language answer.
    * `generate_explanation`: Optional. If set to true, generates an explanation of the MQL query.
    * `generate_disambiguation_question`: Optional. If set to true, generates disambiguation questions if the query is ambiguous.



### Example `QueryData` response

Here is an example of a successful response from a `QueryData` call:
    
    
    {
      "generated_query": "// Count the number of accounts in Prague that are eligible for loans\ndb.loans.aggregate([\n  // 1. Filter loans in the Prague region\n  { \n    $match: { \"district.name\": \"Prague\" } \n  },\n  // 2. Group by account_id to get distinct values, and count them\n  { \n    $group: { \n      _id: null, \n      uniqueAccounts: { $addToSet: \"$account_id\" } \n    } \n  },\n  // 3. Project the size of the unique accounts array\n  { \n    $project: { \n      _id: 0,\n      distinct_account_count: { $size: \"$uniqueAccounts\" } \n    } \n  }\n]);",
      "intent_explanation": "The question asks for the number of accounts eligible for loans in the Prague region. I need to filter the documents in the loans collection to only give me those in the Prague region. Then I need to group the loans by account ID to get distinct values and count them. Finally, I need to project the size of the array of unique accounts.",
      "query_result": {
        "columns": [
          {
            "name": "distinct_account_count"
          }
        ],
        "rows": [
          {
            "values": [
              {
                "value": "2"
              }
            ]
          }
        ],
        "total_row_count": 1
      },
      "natural_language_answer": "There are 2 accounts in Prague that are eligible for loans."
    }
    

## What's next

  * Learn more about [context sets](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/context-sets-overview).
  * Learn how to [build contexts sets using the context engineering agent](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/build-context-sets).
  * Learn how to [Manage context sets in Firestore Studio](https://docs.cloud.google.com/gemini/data-agents/querydata/firestore-mongodb-compatibility/manage-data-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
