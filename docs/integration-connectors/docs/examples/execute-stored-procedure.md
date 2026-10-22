---
url: https://docs.cloud.google.com/integration-connectors/docs/examples/execute-stored-procedure/
title: Execute a stored procedure \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:53.479922+00:00
---

# Execute a stored procedure  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/examples/execute-stored-procedure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Execute a stored procedure

This example shows how to run a stored procedure when you are using a database connection. The example assumes that you are familiar with the following concepts:

  * [Creating integrations using Application Integration](https://docs.cloud.google.com/application-integration/docs/try-sample-integration-ecommerce)
  * [Connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task)
  * [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview)
  * Database stored procedures



All stored procedures in a database connection are exposed to you as actions in the [Connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task). An action is a first class function that is made available to the integration through the connector interface. Actions let you make changes to an entity or entities, and vary from connector to connector. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty.

The following connectors support stored procedures:

  * [BigQuery](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure)
  * [Cloud SQL - MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlformysql/configure)
  * [Cloud SQL - PostgreSQL ](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforpostgresql/configure)
  * [Cloud SQL - SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/cloudsqlforsqlserver/configure)
  * [MySQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure)
  * [Oracle DB](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure)
  * [PostgreSQL](https://docs.cloud.google.com/integration-connectors/docs/connectors/postgresql/configure)
  * [SQL Server](https://docs.cloud.google.com/integration-connectors/docs/connectors/sqlserver/configure)
  * [MariaDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/mariadb/configure)
  * [AlloyDB](https://docs.cloud.google.com/integration-connectors/docs/connectors/alloydb/configure)
  * [Snowflake](https://docs.cloud.google.com/integration-connectors/docs/connectors/snowflake/configure)
  * [Redshift](https://docs.cloud.google.com/integration-connectors/docs/connectors/redshift/configure)



### Example

Consider you have a MySQL database which has the following stored procedure that gets a customer's information from the `customers` table:
    
    
    CREATE PROCEDURE get_customer_info
    (IN p_customer_id INT, OUT p_name VARCHAR(50), OUT p_email VARCHAR(255))
    BEGIN
        SELECT name, email INTO p_name, p_email
        FROM customers
        WHERE id = p_customer_id;
    END
    

This stored procedure returns the name and email for the specified customer. It takes in the customer ID through the `p_customer_id` input variable and returns the name and email in the `p_name` and `p_email` output variables, respectively. 

Now suppose you want to get the name and email id of the customer with `customer_id=1001`, you must do the following tasks:

  1. Create a [connection to your MySQL database](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure).
  2. Open or create a new [integration](https://docs.cloud.google.com/application-integration/docs/quickstarts).
  3. Add the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) to your integration.
  4. In the **Configuration** section, click **Configure task** to open the **Configure connector task** pane.
  5. Configure the Connectors task to use the connection you created in step 1. 
     1. In the **Connection** column, select the required connection from the list of available connections. 

After you select a connection, the **Type** column appears with the values `Entities` and `Actions`. All the stored procedures will be listed in **Actions**.

     2. Select **Actions > get_customer_info**.
     3. Click **Done** to complete the connection configuration and close the pane.
  6. Click the `Connectors` task element, and then click `connectorInputPayload` in the `Task Input` section.
  7. Specify the following JSON payload in the `Default Value` field: 
         
         {
         "customer_id": 1001
         }

  8. Click the **Test** button in the integration editor toolbar to run the integration. 

If the integration runs successfully, the `connectorOutputPayload` vairable will have a JSON payload similar to the following:
         
         {
         "name": "John",
         "email": "john@test.com"
         }




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
