---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/database/
title: Query a database \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:04.637985+00:00
---

# Query a database  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Query a database Stay organized with collections  Save and categorize content based on your preferences. 

Your webhook currently uses hardcoded data in the `accountBalanceCheck` function. In this step of the tutorial, you will create a [Spanner](https://docs.cloud.google.com/spanner/docs) database, populate it with balance data, and update your function to query the database.

## Project configuration

It is important that your Dialogflow agent and the database are both in the same project. This is the easiest way for your function to have secure access to your database. Also, you must enable the Spanner API.

  1. Before creating the database, select your project from the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Spanner API for the project.

[Enable the Spanner API](https://console.cloud.google.com/apis/enableflow?apiid=spanner.googleapis.com)




## Create a Spanner instance

When you first use Spanner, you must create an instance, which is an allocation of resources that are used by Spanner databases in that instance.

  1. In the Google Cloud console, go to the **Spanner Instances** page.

[Go to Spanner instances](https://console.cloud.google.com/spanner/instances)

  2. Click **Create instance**.

  3. For the instance name, enter **Tutorial Instance**.

  4. The instance ID is automatically entered based on the instance name.

  5. In **Choose your configuration** , retain the default option **Regional** and select the same region [location](https://docs.cloud.google.com/dialogflow/es/docs/how/region) that you chose when creating the function.

  6. In **Allocate compute capacity** , enter 100 processing units. This provides a minimal capacity for the tutorial.

  7. Click **Create**. The Google Cloud console displays the **Overview** page for the instance you created.




## Create a Spanner database

Now that you have an instance, you need to create a database. To create a database:

  1. In the instance **Overview** page, click **Create database**.
  2. For the database name, enter **tutorial-database**.
  3. Select the **Google Standard SQL** database dialect.
  4. Click **Create**. The Google Cloud console displays the **Overview** page for the database you created.



## Create tables for your database

Now that you have a database, you need to create tables for the database. To create tables:

  1. In the Tables section of the database **Overview** page, click **Create table**.
  2. In the **Write DDL statements** page, enter:
         
         CREATE TABLE Checking (
           AccountId INT64,
           Balance INT64,
         ) PRIMARY KEY(AccountId);
         

  3. Click **Submit**. The Google Cloud console returns to the database **Overview** page and shows that **Schema updates** are underway. Wait until the update is complete.

  4. In the Tables section of the database **Overview** page, click **Create table**.

  5. In the **Write DDL statements** page, enter:
         
         CREATE TABLE Savings (
           AccountId INT64,
           Balance INT64,
         ) PRIMARY KEY(AccountId);
         

  6. Click **Submit**. The Google Cloud console returns to the database **Overview** page and shows that **Schema updates** are underway. Wait until the update is complete.




## Insert data into your tables

Now that your database has tables, you need to add data to the tables. To add data:

  1. In the list of tables on the database **Overview** page, click the Checking table. The Google Cloud console displays the table's **Schema** page.
  2. In the left navigation menu, click **Data** to display the table's **Data** page.
  3. Click **Insert**. The Google Cloud console displays the table's **Query** page with a new query tab that contains `INSERT` and `SELECT` statements. Overwrite those statements with the following:
         
         INSERT INTO Checking (AccountId, Balance)
         VALUES(1, 1000),
               (2, 2000);
         

  4. Click **Run**.

  5. In the left navigation menu, click **Data** again to display the table's data. Confirm that the table contains the desired data.

  6. Click the **tutorial-database: Overview** link to return to the database overview page.

  7. In the list of tables on the database **Overview** page, click the Savings table. The Google Cloud console displays the table's **Schema** page.

  8. In the left navigation menu, click **Data** to display the table's **Data** page.

  9. Click **Insert**. The Google Cloud console displays the table's **Query** page with a new query tab that contains `INSERT` and `SELECT` statements. Overwrite those statements with the following:
         
         INSERT INTO Savings (AccountId, Balance)
         VALUES(1, 10000),
               (2, 20000);
         

  10. Click **Run**.

  11. In the left navigation menu, click **Data** again to display the table's data. Confirm that the table contains the desired data.




## Update the Cloud Function to query the database

The `accountBalanceCheck` function in the webhook code checks whether specific environment variables are set with information for connecting to the database. If these environment variables are not set, the function uses a hardcoded account balance.

Now that you have a database set up, update your Cloud Function to set required environment variables:

  1. Open the Cloud Functions overview page.

[Go to Cloud Functions overview](https://console.cloud.google.com/functions/list)

  2. Click the tutorial-banking-webhook function to go to its details page.

  3. Click **Edit**.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Runtime** tab.

  6. Add the following variables in the Runtime environment variables section:

     * `PROJECT_ID`: your project ID
     * `SPANNER_INSTANCE_ID`: your Spanner instance ID (probably `tutorial-instance`)
     * `SPANNER_DATABASE_ID`: your spanner database ID (probably `tutorial-database`)
  7. Click **Next**.

  8. Click **Deploy**.

  9. Wait until the status indicator shows that the function has successfully deployed.




## Test your agent

Your agent is now ready to try. Click the **Test Agent** button from the Dialogflow console to open the simulator. Attempt to have the following conversation with the agent:

Conversational turn | You | Agent  
---|---|---  
1 | Hello | Hello, thanks for choosing ACME Bank.  
2 | I want to know my account balance | What account do you want the balance for: savings or checking?  
3 | Checking | Here's your latest balance: $10.00  
  
If you examine the code, $10 is not the hardcoded value. This means that your webhook has successfully connected to the database, which does have a balance of $10.

## Troubleshooting

The webhook code includes logging statements. If you are having issues, try viewing the logs for your Cloud Function.

If your function is not connecting to the database, and you see a permission error in the logs, you may need to fix the role for the default service account used by your function. This service account is of the form `PROJECT_ID@appspot.gserviceaccount.com`. You can fix this in one of the following ways:

  * If the default service account is shown on the IAM main page, [change permissions for the service account](https://docs.cloud.google.com/functions/docs/securing/function-identity#default). The _Editor_ role will work, but you may want a more granular role in a production scenario.

[Go to the IAM main page](https://console.cloud.google.com/iam-admin/iam)

  * If the a default service account is not shown on the IAM main page, [grant the required role](https://docs.cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role) by adding the service account as a new principal.

  * Alternatively, you can [use a service account that you create](https://docs.cloud.google.com/functions/docs/securing/function-identity#individual).




## More information

For more information about the steps above, see:

  * [Using Cloud Spanner with Cloud Functions](https://docs.cloud.google.com/functions/docs/tutorials/use-cloud-spanner)
  * [Create and query a database by using the Google Cloud console](https://docs.cloud.google.com/spanner/docs/create-query-database-console)
  * [Google Standard SQL data definition language](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/data-definition-language)
  * [Google Standard SQL data manipulation language](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/dml-syntax)



[ Previous arrow_back  Create a webhook service  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/webhook)

[ Next Host your agent  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy/host)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
