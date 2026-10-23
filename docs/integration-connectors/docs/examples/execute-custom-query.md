---
url: https://docs.cloud.google.com/integration-connectors/docs/examples/execute-custom-query/
title: Execute custom query \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:20.807851+00:00
---

# Execute custom query  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/examples/execute-custom-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Execute custom query

This page shows you how to execute a custom SQL query. To execute a custom query, you must be familiar with the following concepts:

  * [Creating integrations using Application Integration](https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce)
  * [Connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task)
  * [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview)
  * SQL queries



The **Execute custom query** is exposed to you as an action in the [Connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task). An action is a first class function that is made available to the integration through the connector interface. Actions let you make changes to an entity or entities, and vary from connector to connector. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty.

The following connectors support custom query:

  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Cloud SQL - MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL - PostgreSQL ](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL - SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [Couchbase](https://docs.cloud.google.com/integration-connectors/docs/connectors/couchbase/configure)
  * [Elasticsearch](https://docs.cloud.google.com/integration-connectors/docs/connectors/elasticsearch/configure)
  * [MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure)
  * [Oracle DB](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [Redshift](https://docs.cloud.google.com/integration-connectors/docs/connectors/redshift/configure)
  * [Salesforce](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure)
  * [SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)
  * [Snowflake](https://docs.cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)
  * [Spanner](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudspanner/configure)
  * [Terdata](https://docs.cloud.google.com/integration-connectors/docs/connectors/teradata/configure)



### Create a custom query

To create a custom query, follow these steps: 

  1. Follow the detailed instructions to [ add a connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).
  2. When you [configure the connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-the-connectors-task), in the type of action you want to perform, select **Actions**.
  3. In the **Action** list, select **Execute custom query** , and then click **Done**. 

![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)

  4. Expand the **Task input** section, and then do the following: 
     1. In the **Timeout after** field, enter the number of seconds to wait till the query executes. 

Default value: `180` seconds.

     2. In the **Maximum number of rows** field, enter the maximum number of rows to be returned from the database.

Default value: `25`.

     3. To update the custom query, click **Edit Custom Script**. The **Script editor** dialog opens. 

![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)

     4. In the **Script editor** dialog, enter the SQL query and click **Save**. 

You can use a question mark (?) in a SQL statement to represent a single parameter that must be specified in the query parameters list. For example, the following SQL query selects all rows from the `Employees` table that matches the values specified for the `LastName` column: 
            
            SELECT * FROM Employees where LastName=?

**Note:** Data manipulation language (DML) and data definition language (DDL) statements are supported.
     5. If you've used question marks in your SQL query, you must add the parameter by clicking **\+ Add Parameter Name** for each question mark. While executing the integration, these parameters replace the question marks (?) in the SQL query sequentially. For example, if you have added three question marks (?), then you must add three parameters in order of sequence. 

![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)

To add query parameters, do the following:

        1. From the **Type** list, select the data type of the parameter.
        2. In the **Value** field, enter the value of the parameter.
        3. To add multiple parameters, click **\+ Add Query Parameter**.

The **Execute custom query** action does not support array variables.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
