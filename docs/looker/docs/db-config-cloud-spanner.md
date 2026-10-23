---
url: https://docs.cloud.google.com/looker/docs/db-config-cloud-spanner/
title: Google Spanner \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:18.922797+00:00
---

# Google Spanner  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-cloud-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Google Spanner Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up a connection in Looker to Google Spanner.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Getting the connection credentials

  1. Log in to the [Google Cloud console](https://console.cloud.google.com/).

  2. Select the appropriate project.

  3. From the menu, select **IAM & Admin** and then **Service accounts**.

  4. Select **Create service account** and fill in the dialog box as follows:

     * **Service account name** : Enter `looker-spanner-service` or something similar.
     * **Role** : Select **Cloud Spanner** and then **Cloud Spanner Database Reader**.
     * **Furnish a new private key** : Select the **Furnish a new private key** checkbox, and select **JSON** under **Key type**.

![](https://docs.cloud.google.com/static/looker/docs/images/setup-google-spanner-create-service-account-524.png)

  5. Click **Create** and keep track of the following:

     * The email address associated with the service account
     * The name and location of the JSON credential file that was downloaded

![](https://docs.cloud.google.com/static/looker/docs/images/setup-google-spanner-account-created-524.png)




## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Dialect** : **Google Spanner**.
  * **Name** : The name of the connection.
  * **Project Name** : The project ID for the Google project that contains the Spanner database.
  * **Instance Name** : The name of the instance that contains the Spanner database.
  * **Database** : The name of the Spanner database.
  * **Schema** : Leave this blank.
  * **Max connections per node** : The maximum number of total connections to the Spanner database across all users. The default is 30. This setting can be left at the default value initially. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
  * **Connection Pool Timeout** : The number of seconds a query will wait before timing out because of a full connection pool.
  * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for a list of supported parameters.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Google Spanner {: #google}, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `autocommit`
  * `autoConfigEmulator`
  * `endpoint`
  * `maxSessions`
  * `minSessions`
  * `numChannels`
  * `oauthToken`
  * `optimizerVersion`
  * `readonly`
  * `retryAbortsInternally`
  * `rpcPriority`
  * `usePlainText`



## Feature support

For Looker to support some features, your database dialect must also support them.

Google Spanner supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
## References

  * [Documented Spanner limits](https://docs.cloud.google.com/spanner/docs/limits)

  * [Google Spanner IAM documentation](https://docs.cloud.google.com/spanner/docs/iam)




## Next steps

After you have connected your database to Looker, [configure sign-in options for your users](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
