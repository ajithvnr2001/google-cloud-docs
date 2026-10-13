---
url: https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/database/
title: Query a database \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:59.406832+00:00
---

# Query a database  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/database/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Query a database Stay organized with collections  Save and categorize content based on your preferences. 

Your webhook currently uses hardcoded data in the `cruisePlanCoverage` function. In this step of the tutorial, you will create a [Spanner](https://docs.cloud.google.com/spanner/docs) database, populate it with covered destinations, and update your function to query the database.

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

  5. In **Choose your configuration** , retain the default option **Regional** and select the same region [location](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail) that you chose when creating the function.

  6. In **Allocate compute capacity** , enter 100 processing units. This provides a minimal capacity for the tutorial.

  7. Click **Create**. The Google Cloud console displays the **Overview** page for the instance you created.




## Create a Spanner database

Now that you have an instance, you need to create a database. To create a database:

  1. In the instance **Overview** page, click **Create database**.
  2. For the database name, enter **tutorial-database**.
  3. Select the **Google Standard SQL** database dialect.
  4. Click **Create**. The Google Cloud console displays the **Overview** page for the database you created.



## Create a table for your database

Now that you have a database, you need to create a table for the database. To create a table:

  1. In the Tables section of the database **Overview** page, click **Create table**.
  2. In the **Write DDL statements** page, enter:
         
         CREATE TABLE Destinations (
           Destination STRING(1024),
           Covered BOOL,
         ) PRIMARY KEY(Destination);
         

  3. Click **Submit**. The Google Cloud console returns to the database **Overview** page and shows that **Schema updates** are underway. Wait until the update is complete.




## Insert data into your table

Now that your database has a table, you need to add data to the table. To add data:

  1. In the list of tables on the database **Overview** page, click the Destinations table. The Google Cloud console displays the Destinations table's **Schema** page.
  2. In the left navigation menu, click **Data** to display the Destinations table's **Data** page.
  3. Click **Insert**. The Google Cloud console displays the Destinations table's **Query** page with a new query tab that contains `INSERT` and `SELECT` statements. Overwrite those statements with the following:
         
         INSERT INTO Destinations (Destination, Covered)
         VALUES('anguilla', TRUE),
               ('canada', TRUE),
               ('china', TRUE),
               ('italy', TRUE),
               ('mexico', TRUE),
               ('spain', FALSE);
         

  4. Click **Run**.

  5. In the left navigation menu, click **Data** again to display the Destination table's data. Confirm that the table contains the desired data.




## Update the Cloud Function to query the database

The `cruisePlanCoverage` function in the webhook code checks whether specific environment variables are set with information for connecting to the database. If these environment variables are not set, the function uses a hardcoded list of destinations.

Now that you have a database set up, update your Cloud Function to set required environment variables:

  1. Open the Cloud Functions overview page.

[Go to Cloud Functions overview](https://console.cloud.google.com/functions/list)

  2. Click the tutorial-telecommunications-webhook function to go to its details page.

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
1 | Hello | Hi! I'm the virtual telecommunications agent. I can help you resolve billing and plan questions, troubleshoot, and add travel and cruise plans. How can I assist you today?  
2 | I want to add a cruise plan | Let me take a look for you. What is your phone number with us?  
3 | 123-123-1234 | How many days is your cruise?  
4 | 7 | Option 1 includes talk and text. It costs $[XX]/day. More info here [URL]. Option 2 includes talk, text and data. It costs $[XX]/day. More info here [URL]. Which cruise plan would you like to add?  
5 | Option 1 | Got it. I've added that plan to your account. While on your cruise, you may also need coverage on land. What port will you be stopping at?  
6 | Italy | And, how many days are you spending there?  
7 | 3 | Great news! Italy has free coverage on land. You're all set. Is there anything else I can help you with today?  
  
If you examine the code, Italy is not in the hardcoded list of covered destinations. This means that your webhook has successfully connected to the database, which does include Italy.

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



[ Previous arrow_back  Create a webhook service  ](https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/webhook)

[ Next Host your agent  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy/host)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
