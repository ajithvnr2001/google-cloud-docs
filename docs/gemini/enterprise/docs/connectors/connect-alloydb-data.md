---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data/
title: Connect to data from AlloyDB for PostgreSQL (Preview) \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:11.570803+00:00
---

# Connect to data from AlloyDB for PostgreSQL (Preview)  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb-data/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to data from AlloyDB for PostgreSQL (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** You need to be on the allowlist to use this connector. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

You can connect your AlloyDB instance to Gemini Enterprise, enabling live access to your data.

Compared to importing from AlloyDB, connecting has the following advantages:

  * Avoids the need for importing, indexing, and duplicating data.
  * Maximal data freshness.
  * No additional indexing and storage costs.
  * No need to flatten structured data into uniform records.



Consider the following disadvantages of connecting compared to importing:

  * This approach supports only structured queries, not semantic or semi-semantic queries.
  * The setup is slightly more involved compared to importing the data.



## Limitations

Connecting to AlloyDB has the following limitations:

  * Gemini Enterprise supports access control on the level of database objects, such as tables and columns, but not on a per-user level. All users with access to your Gemini Enterprise app can see the same data.
  * Creating an AlloyDB data store is supported through the API, not through the Google Cloud console.



## Set up AlloyDB AI natural language

This connector relies on AlloyDB AI natural language in AlloyDB, which translates natural language queries into SQL queries.

Before connecting, set up AlloyDB AI natural language in your database using the steps in [Generate SQL queries that answer natural language questions](https://docs.cloud.google.com/alloydb/docs/ai/generate-sql-queries-natural-language) in the AlloyDB documentation.

Note that adding templates in AlloyDB AI natural language (a curated set of natural language questions with corresponding SQL queries) is particularly useful for quality. When adding templates, Google recommends the following:

  * Use `ORDER BY` to avoid non-determinism. For example: `SELECT customers.id FROM customers ORDER BY customers.id;`.

**Note:** You can add templates and other context later. For example, when you notice low answer quality in Gemini Enterprise for a specific question.



## Set up authentication between Gemini Enterprise and AlloyDB

Gemini Enterprise accesses AlloyDB using a dedicated service account and a database user in your AlloyDB instance. With this approach, every Gemini Enterprise user can see the same data, without user-specific access control.

A service account is used to connect and interact with your AlloyDB instance. To enable this, you need to configure the Identity and Access Management (IAM) settings in the Google Cloud project where your database instance resides.

To set up authentication, do the following:

  1. Navigate to the IAM configuration page of the project that hosts your AlloyDB instance.
  2. Grant the **Cloud AlloyDB Database User** role to the following principal: `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with the Google Cloud project number where you use Gemini Enterprise.

  3. In your AlloyDB instance, create a DB user to be used by Gemini Enterprise to execute SQL queries.

It is very important that you grant this user read-only access and only for tables, views and columns that should be accessible from Gemini Enterprise. This ensures that:

     * Queries from Gemini Enterprise cannot change or delete your data. Gemini Enterprise is designed to only read data from your database and not change anything, but Google can't fully exclude the possibility that the AI might generate unintended write-queries.

     * Users in Gemini Enterprise can only see data they are supposed to see.

For example:
           
           CREATE ROLE USER_NAME WITH LOGIN PASSWORD 'PASSWORD';
           GRANT SELECT ON TABLE "public"."TABLE_NAME_1" TO USER_NAME;
           GRANT SELECT ON TABLE "public"."TABLE_NAME_2" TO USER_NAME;
           

When linking Gemini Enterprise with AlloyDB, provide the username and password in the **User** and **Password** fields of `alloydbConnectionConfig`.




### Link Gemini Enterprise with AlloyDB

To connect your AlloyDB instance, follow these steps:

  1. Create a data store in Gemini Enterprise with your AlloyDB connection details using the API, including `federatedSearchConfig.alloyDbConfig`.

The following example:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -H "X-Goog-User-Project: PROJECT_ID" \
           "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" -d '{
           "displayName": "DATA_STORE_NAME",
           "federatedSearchConfig": {
             "alloyDbConfig": {
               "alloydbConnectionConfig": {
                 "instance": "INSTANCE_PATH",
                 "database": "DATABASE_NAME",
                 "user": "DATABASE_USER_NAME",
                 "password": "DATABASE_USER_PASSWORD",
                 "authMode": "AUTH_MODE_SERVICE_ACCOUNT"
               },
               "alloydb_ai_nl_config": { "nlConfigId": "NL_CONFIG_ID" }
             }
           },
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_SEARCH"]
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project where you use Gemini Enterprise.
     * `LOCATION`: The location of your data store. This should be the same location as your Gemini Enterprise instance.

**Important:** For locations other than `global`, replace `discoveryengine` with the location-specific path. For more information, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
     * `DATA_STORE_ID`: the ID of the data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.

     * `DATA_STORE_NAME`: the display name of the data store that you want to create.

     * `INSTANCE_PATH`: The path of your AlloyDB instance, in the format `projects/.../locations/.../clusters/.../instances/...`.

     * `DATABASE_NAME`: the ID of the AlloyDB database.

     * `DATABASE_USER_NAME`: the ID of the AlloyDB database user.

     * `DATABASE_USER_PASSWORD`: the password of the AlloyDB database user.

     * `NL_CONFIG_ID`: the ID of the AlloyDB AI natural language configuration.

  2. Attach your data store to an existing Gemini Enterprise app, or create a new app and select your connector, following the steps in [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  3. To preview how your search results appear after your app is set up, see [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
