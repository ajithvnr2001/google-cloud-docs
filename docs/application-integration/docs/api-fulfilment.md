---
url: https://docs.cloud.google.com/application-integration/docs/api-fulfilment/
title: API request fulfilment \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:50.082304+00:00
---

# API request fulfilment  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/api-fulfilment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback 

#  API request fulfilment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes a use case on how you can use Application Integration to route and fetch information for an ingress API request. 

## Overview

In this tutorial, you'll create an integration with an API trigger that receives API requests for retrieving customer information. Depending on the API request location, the integration retrieves the customer details from either a MySQL database or an Oracle database. 

![API Fulfilment diagram](https://docs.cloud.google.com/static/application-integration/images/api-fulfilment.png)![API Fulfilment diagram](https://docs.cloud.google.com/static/application-integration/images/api-fulfilment.png)

## Objectives

This tutorial shows you how to complete the following tasks in your integration:

  * Add an API trigger.
  * Add and configure Connectors tasks for MySQL and Oracle connections.
  * Add and configure data mapping tasks to extract and map API payload.



## Costs

In this tutorial, you use the following billable components of Google Cloud:

  * [ Application Integration](https://docs.cloud.google.com/application-integration/docs/pricing)
  * [ Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/pricing)
  * [ Secret Manager](https://docs.cloud.google.com/secret-manager/pricing)



The instructions in this tutorial are designed to keep your resource usage within the limits of Google Cloud's [ Always Free tier](https://docs.cloud.google.com/free/docs/frequently-asked-questions#always-free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Secret Manager Viewer (`roles/secretmanager.viewer`), Secret Manager Secret Accessor (`roles/secretmanager`)**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Secret Manager Viewer (`roles/secretmanager.viewer`), Secret Manager Secret Accessor (`roles/secretmanager`)**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 


**Note:** All the other required Google Cloud APIs such as, the _Application Integration API_ , the _Secret manager API_ , and the _Connectors API_ are enabled during the Application Integration setup. For more details, see [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration#enable-api). 

## Prepare your environment

### Set up a MySQL database

Connect to your MySQL server and create a database and a table to use in this tutorial. This tutorial uses a database that contains a table named `Customers` with the following rows:
    
    
      +-------------+---------------+--------------------+------------------+
      | customer_id | customer_name | customer_emailID   | customer_city    |
      +-------------+---------------+--------------------+------------------+
      |           1 | Alex          | test-01@test.com   | New York         |
      |           2 | Dana          | test-02@test.com   | Seattle          |
      +-------------+---------------+--------------------+------------------+
      

For information about creating and using a MySQL database, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/tutorial.html). 

### Set up an Oracle database

Connect to your Oracle database and create a table to use in this tutorial. This tutorial uses a database that contains a SQL table named `Customers` with the following rows:
    
    
      +-------------+---------------+--------------------+------------------+
      | customer_id | customer_name | customer_emailID   | customer_city    |
      +-------------+---------------+--------------------+------------------+
      |           1 | Amal          | test-01@test.com   | Delhi            |
      |           2 | Hao           | test-02@test.com   | Beijing          |
      +-------------+---------------+--------------------+------------------+
      

For information about creating and using a Oracle database, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/introduction-to-oracle-database.html). 

### Configure connections

For this tutorial, you must configure the following connections in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs):

**Tip:** We recommend that you create the following connections in the `us-central1(lowa)` region. 

MySQL connection
    Configure a MySQL connection in Integration Connectors to get the `Customer` tables entities. For information on configuring a MySQL connector, see [MySQL connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/mysql/configure).
Oracle DB connection
    Configure a Oracle DB connection in Integration Connectors to get the `Customer` tables entities. For information on configuring a MySQL connector, see [Oracle DB connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/oracledb/configure).

## Create integration

To create a new integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter `api_fulfilment`.
     2. **Description:** Enter `Demo integration created for tutorial`.
     3. **Region:** Select `us-central1` from the list of [supported regions](https://docs.cloud.google.com/application-integration/docs/locations).
     4. Click **Create** to open the integration editor.



## Set up integration trigger

Once you have successfully created your integration, you can add and configure an integration trigger that invokes the integration for an identified event.

For this tutorial, an API trigger is used to invoke the integration for every new API request. To add and configure an **API trigger** in your `api_fulfilment` integration, do the following: 

  1. In the integration editor, click **Triggers** to display a list of available triggers.
  2. Click and place the **API trigger** element in the integration editor. 

Application Integration automatically populates the trigger Label, trigger name, and trigger ID. **Trigger ID** is a machine-generated ID in the format `api_trigger/TRIGGER_NAME`, and is used in the API request.

No further configuration is required for this trigger.




## Create integration variables

Integration variables are similar to variables used in a programming language. Data in the variables can be read and written throughout the execution of the integration. To create the required variables for this tutorial, do the following:

  1. Click last_page (Toggle panel) in the designer navigation bar to bring up the **Variables** pane.
  2. Click **\+ Create** and create the following integration variables: Variable name | Data type | Variable type | `location` | `STRING` | Input to integration  
---|---|---  
`customer_id` | `STRING` | **Input to Integration**  
`customer_record` | `JSON` | **Output from Integration**  



## Retrieve customer data from MySQL database

If the ingress API request is from the `US` location, then do the following to retrieve customer data from the MySQL database.

### Connect to the MySQL database

Perform the following steps to add and configure a **Connectors** task to retrieve the customers details from the MySQL **Customers** table: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Select the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** label to `Fetch MySQL Data`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your Salesforce connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Customers** from the list of available entities and then select **Get** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Map customer ID to MySQL connector

A **Data Mapping** task is used to map the customer ID to the MySQL connector. To add and configure the data mapping in your integration, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Select the **Data Mapping** element on the designer to view the task configuration pane. 
  4. Click  edit  and rename the **Data Mapping** task to `Map to MySQL`.
  5. Click **Open Data Mapping Editor**. 

The **Data Mapping Editor** lets you map input variables to the desired output variables, using the available transformation functions. The output is then available as a variable to any other integration task or trigger. For more details on mapping variables, see [Add a mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task#add-map).

  6. Map the trigger —`customer_id`—integration variable to the auto-generated connector—`entityId(Fetch MySQL Data)`—input variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Map to MySQL** task to the **Fetch MySQL Data** connector.



### Retrieve MySQL customer details

To retrieve the customer details from the MySQL connector, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Get MySQL data`.
  5. Click **Open Data Mapping Editor**.
  6. Map the MySQL—`connectorOutputPayload (Fetch MySQL Data)`—output variable to the `customer_record` integration variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Fetch MySQL Data** connector to the **Get MySQL data** task.



## Retrieve customer data from Oracle database

If the ingress API request is from the `APAC` location, then do the following to retrieve customer data from the Oracle database.

### Connect to the Oracle database

Perform the following steps to add and configure a **Connectors** task to retrieve the customers details from the Oracle **Customers** table: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Select the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** label to `Fetch Oracle Data`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your Salesforce connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Customers** from the list of available entities and then select **Get** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Map customer ID to Oracle connector

To add and configure the data mapping in your integration, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Select the **Data Mapping** element on the designer to view the task configuration pane. 
  4. Click  edit  and rename the **Data Mapping** task to `Map to Oracle`.
  5. Click **Open Data Mapping Editor**. 
  6. Map the trigger —`customer_id`—integration variable to the auto-generated connector—`entityId(Fetch Oracle Data)`—input variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Map to Oracle** task to the **Fetch Oracle Data** connector.



### Retrieve Oracle customer details

To retrieve the customer details from the Oracle connector, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Get Oracle data`.
  5. Click **Open Data Mapping Editor**.
  6. Map the Oracle—`connectorOutputPayload (Fetch Oracle Data)`—output variable to the `customer_record` integration variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Fetch Oracle Data** connector to the **Get Oracle data** task.



##  Add edge condition 

An edge condition lets you specify the conditions that must be met for control of an integration to pass to the task connected by the edge. Now that you have added and configured and the required tasks, you can add an edge condition to define the flow of the integration. 

The following edge condition controls the flow of the integration based on the `location` integration variable:

  1. Add an edge connection from the **API** trigger to the **Map to MySQL** task with the following edge condition: 
         
         $location$ = "US"

  2. Add another edge connection from the **API** trigger to the **Map to Oracle** task with the following edge condition: 
         
         $location$ = "APAC"




## Sample integration flow

The following figure shows a sample layout of the integration created using this tutorial.

![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/api-fulfilment-flow.png)![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/api-fulfilment-flow.png)

## Publish integration

To publish the integration click **Publish** in the integration editor toolbar.

Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **![image showing the icon for execution logs](https://docs.cloud.google.com/static/application-integration/images/logs-icon.png)View execution logs for this integration**. The **Execution Logs** page appears.

## Test the integration

###  Test the integration from the integration editor 

To test the integration from the integration editor, perform the following steps: 

  1. Click  play_circle  **Test** in the integration editor toolbar.

The **Test Integration** pane appears. 

  2. You are prompted to enter the test values for the integration input variables. For the purpose of this test, do the following:. 
     * **customer_id:** Enter `1`.
     * **location:** Enter `APAC`.
  3. Click **Test Integration**.



The integration executes successfully and the following customer value is displayed:
    
    
    { 
      "CUSTOMER_ID": 1,
      "CUSTOMER_NAME": "Amal"
      "CUSTOMER_EMAILID": "test-01@test.com "
      "CUSTOMER_CITY": "Delhi"
    }
    

For more information about testing, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).

###  Test using a REST API call 

Now that the integration is published and running, you can invoke it using the following POST REST call: 

**URL:**
    
    
    https://integrations.googleapis.com/v1/projects/project-name/locations/-/integrations/api_fulfilment:execute 

**Request body:**
    
    
    {"trigger_id":"api_trigger/api_fulfilment_API_1"}

#### Example: Make an API request with custom inputs

**Note:** The following example uses `curl`, which typically comes pre-installed for Linux and macOS operating systems. If you don't have `curl`, you can download it from the `curl` [releases and downloads page](https://curl.haxx.se/download.html).
    
    
    curl -v -X POST -H "Content-Type: application/json" 'https://integrations.googleapis.com/v1/projects/connectors-ip-test/locations/us-central1/integrations/api-fulfillment-integration:execute' -H "Authorization: Bearer $(gcloud auth AUTH_PROFILE)" -d  '{ "triggerId": "api_trigger/api-fulfillment-integration_API_1", "inputParameters": { "customer_id": {"string_value": 1}, "location" : {"string_value" : "US"}} }'
    

The API returns the integration execution response containing all following JSON: 
    
    
      { 
        "CUSTOMER_ID": 2,
        "CUSTOMER_NAME": "Dana"
        "CUSTOMER_EMAILID": "test-02@test.com "
        "CUSTOMER_CITY": "Seattle"
      }
      

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, unpublish the integration and delete the connections created in Integration Connectors.

  * To unpublish this integration, click **Unpublish** in the integration editor toolbar. See [Delete integrations](https://docs.cloud.google.com/application-integration/docs/delete-integrations) for more information.
  * For information about how to delete a connection, see [Manage connectors](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
