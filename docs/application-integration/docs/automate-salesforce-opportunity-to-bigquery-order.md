---
url: https://docs.cloud.google.com/application-integration/docs/automate-salesforce-opportunity-to-bigquery-order/
title: Automate Salesforce opportunity to BigQuery order \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:41.148772+00:00
---

# Automate Salesforce opportunity to BigQuery order  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/automate-salesforce-opportunity-to-bigquery-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback 

#  Automate Salesforce opportunity to BigQuery order Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes a use case on how you can use Application Integration to automate an order management flow between a customer relationship management (CRM) application and an enterprise resource planning (ERP) application. 

## Overview

Business enterprises use various CRM and ERP applications to create, process, manage, and maintain sales orders. Each of these applications is handled by different teams or organizations, and ensuring that the order is constantly tracked while providing timely customer updates is a challenge. 

In this tutorial, you'll create an integration that uses a Salesforce trigger to subscribe to a new opportunity event in Salesforce. When a new opportunity is created, the integration will retrieve additional opportunity details, such as the account ID and name. These details are checked in a BigQuery table to create and update the opportunity with a tracking order number. During validation, if the account information doesn't exist in BigQuery, the integration will automatically create a new entry in both the BigQuery table and the attached ServiceNow instance using Integration Connectors. 

![Salesforce opportunity to BigQuery order diagram](https://docs.cloud.google.com/static/application-integration/images/opportunity-to-order.png)![Salesforce opportunity to BigQuery order diagram](https://docs.cloud.google.com/static/application-integration/images/opportunity-to-order.png)

## Objectives

This tutorial shows you how to complete the following tasks in your integration:

  * Set up Salesforce Trigger to invoke your integration.
  * Add and configure Connectors tasks for Salesforce, BigQuery, and ServiceNow connections.
  * Add and configure data mapping tasks to extract and map opportunity details.



## Costs

In this tutorial, you use the following billable components of Google Cloud:

  * [ Application Integration](https://docs.cloud.google.com/application-integration/docs/pricing)
  * [ Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/pricing)
  * [ BigQuery](https://cloud.google.com/bigquery/pricing)
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

  4. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **BigQuery Data Editor (`roles/bigquery.dataEditor`), BigQuery Read Session User (`roles/bigquery.readSessionUser`), Secret Manager Viewer (`roles/secretmanager.viewer`), Secret Manager Secret Accessor (`roles/secretmanager`)**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **BigQuery Data Editor (`roles/bigquery.dataEditor`), BigQuery Read Session User (`roles/bigquery.readSessionUser`), Secret Manager Viewer (`roles/secretmanager.viewer`), Secret Manager Secret Accessor (`roles/secretmanager`)**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 


**Note:** All the other required Google Cloud APIs such as, the _Application Integration API_ , the _Secret manager API_ , and the _Connectors API_ are enabled during the Application Integration setup. For more details, see [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration#enable-api). 

## Prepare your environment

### Verify Salesforce user setup

This tutorial assumes that you have an existing Salesforce developer account with the required user setup and permission set. Verify that your account has _Change Data Capture (CDC)_ enabled. For information about creating a new account, see [Set up an integration user](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger#set-up-an-integration-user). 

### Set up BigQuery dataset and table

For this tutorial, you must set up a BigQuery [dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) and create two [tables](https://docs.cloud.google.com/bigquery/docs/tables-intro) to store the Salesforce opportunity details and the ServiceNow account information.

### Set up BigQuery dataset

To set up the BigQuery dataset, do the following:

  1. Go to the **BigQuery** page in the Google Cloud console. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Click the **Explorer** panel and select the project that you're using for this tutorial.
  3. Expand more_vert (Actions) and select **Create dataset**.
  4. Configure the following details in the **Create dataset** page: 
     1. **Dataset ID:** Enter `Demo_order_dataset`.
     2. **Location type > Region:** Choose the `us-central1 (lowa)` region.
  5. Click **Create dataset**.

The new `Demo_order_dataset` dataset should now appear in your project in the **Explorer** panel. 




### Set up BigQuery tables

To create the BigQuery tables, do the following:

  1. In the **Explorer** panel, click and open the created `Demo_order_dataset` dataset.
  2. Perform the following steps to create an empty _Orders_ table to store the Salesforce opportunity details: 
     1. Click add_box **Create table**.
     2. In the **Destination** section, enter `Orders` as the table name.
     3. In the **Schema** section, click **Edit as text** and paste the following JSON schema definition: 
            
            [
              {
                "name": "order_number",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Salesforce order number"
              },
              {
                "name": "order_status",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Sale order status"
              },
              {
                "name": "tracking_number",
                "type": "INTEGER",
                "mode": "NULLABLE",
                "description": "Salesforce tracking number"
              }
            ]

     4. Click **Create table**.
  3. Perform the following steps to create an empty _Accounts_ table to store the Salesforce account details: 
     1. Click add_box **Create table**.
     2. In the **Destination** section, enter `Accounts` as the table name.
     3. In the **Schema** section, click **Edit as text** and paste the following JSON schema definition: 
            
            [
              {
                "name": "account_id",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Account ID for the opportunity"
              },
              {
                "name": "name",
                "type": "STRING",
                "mode": "NULLABLE",
                "description": "Account name for the opportunity"
              }
            ]

     4. Click **Create table**.

The new `Orders` and `Accounts` tables should now appear in your **Demo_order_dataset** dataset in the **Explorer** panel.




### Verify ServiceNow instance

This tutorial uses a ServiceNow free Personal Developer Instance (PDI). You can either use your existing ServiceNow instance or create a new one. Verify that your instance is active and note down its instance URL. For more information about PDI, see [ServiceNow PDI documentation](https://developer.servicenow.com/dev.do#!/guides/rome/developer-program/pdi-guide/personal-developer-instance-guide-introduction). 

### Configure connections

For this tutorial, you must configure the following connections in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs):

**Tip:** We recommend that you create the following connections in the `us-central1(lowa)` region. 

Salesforce connection
    Configure a Salesforce connection in Integration Connectors. For information on configuring a Salesforce connector, see [Salesforce connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure).
BigQuery connection
    Configure a BigQuery connection in Integration Connectors to get, update, and validate order and account details in the **Demo_order_dataset** dataset. For information on configuring a BigQuery connector, see [BigQuery connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure).
ServiceNow connection
    Configure a ServiceNow connection in Integration Connectors using your instance URL to create and retrieve account details in ServiceNow. For information on configuring a ServiceNow connector, see [ServiceNow connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure).

## Create integration

To create a new integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter `opportunity-to-order-integration`.
     2. **Description:** Enter `Demo integration created for tutorial`.
     3. **Region:** Select `us-central1` from the list of [supported regions](https://docs.cloud.google.com/application-integration/docs/locations).
     4. Click **Create** to open the integration editor.



## Set up integration trigger

Once you have successfully created your integration, you can add and configure an integration trigger that invokes the integration for an identified event.

For this tutorial, a Salesforce trigger is used to invoke the integration for every new opportunity that is created in the Salesforce instance. To add and configure a **Salesforce trigger** in your `opportunity-to-order-integration` integration, do the following: 

  1. In the integration editor, click **Triggers** to display a list of available triggers.
  2. Click and place the **Salesforce trigger** element in the integration editor.
  3. Select the **Salesforce trigger** element on the designer canvas to open the Salesforce trigger configuration pane.
  4. Configure the following fields under **Trigger Input** : 
     1. **Event type** : Select **Change Data Capture (CDC)** from the drop-down list.
     2. **Salesforce instance configuration** : Click the **\+ Add new Salesforce instance configuration** option from the drop-down list. 

In the **Add Salesforce instance configuration** dialog, do the following: 

        * **Salesforce instance connection name** : Enter a connection name for the Salesforce instance. For example, `test`. 
        * **Salesforce domain** : Enter your Salesforce domain name. You can find this information from your **Salesforce account > View profile** page. 
        * **Authentication profile** : Select an authentication profile. If you don't have an authentication profile, create a new profile. For information, see [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#create-a-new-authentication-profile).
        * Click **Add**.
     3. **Salesforce channel configuration** : Click the **\+ Add new Salesforce channel configuration** option from the drop-down list. 

In the **Add Salesforce channel** dialog, do the following: 

        * **Salesforce object name** : Enter `Opportunity`.
        * Click **Add**.
     4. **Operation** : Select **Create** from the drop-down list

Changes to the properties are saved automatically.




## Map trigger payload to Salesforce connector

When the integration is invoked using the Salesforce trigger, you extract the opportunity ID and map it to a Salesforce connector to retrieve additional details of the opportunity. 

### Connect to the Salesforce account

Perform the following steps to add and configure a **Connectors** task to retrieve the opportunity details using the **Salesforce** connection: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Select the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** label to `Fetch Salesforce Data`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your Salesforce connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Opportunity** from the list of available entities and then select **Get** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Extract and map opportunity ID

A **Data Mapping** task is used to map and extract the opportunity details between that Salesforce trigger and the Salesforce connector.

To add and configure the data mapping in your integration, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Select the **Data Mapping** element on the designer to view the task configuration pane. 
  4. Click  edit  and rename the **Data Mapping** task to `Map to opportunity ID`.
  5. Click **Open Data Mapping Editor**. 

The **Data Mapping Editor** lets you map input variables to the desired output variables, using the available transformation functions. The output is then available as a variable to any other integration task or trigger. For more details on mapping variables, see [Add a mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task#add-map).

  6. Map the trigger —`SalesforceTriggerCdcRecordID`—output variable to the auto-generated connector—`entityId(Fetch Salesforce Data)`—input variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Salesforce** trigger to the **Map to opportunity ID** task.
  8. Add an edge connection from the **Map to opportunity ID** task to the **Fetch Salesforce Data** connector.



## Validate Salesforce account in BigQuery table

Once you retrieve all the opportunity details from the Salesforce connector, you extract and map the account ID associated with the opportunity, and validate its existence in your BigQuery table. 

###  Connect to the BigQuery table 

Perform the following steps to configure a **Connectors** task that reads the BigQuery **Accounts** tables using the **BigQuery** connection: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Check account in BigQuery`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your BigQuery connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **accounts** from the list of available entities and then select **List** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.
  7. Add an edge connection from the **Fetch Salesforce Data** connector to the **Check account in BigQuery** connector.



### Extract and validate Salesforce account ID

To extract, map, and validate the account ID of the opportunity, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Check account`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following output variables: Output variable name | Data type | `sf_account_id` | `STRING`  
---|---  
`sf_account_name` | `STRING`  
`account_exists` | `BOOLEAN`  
  7. Create the following mapping between the Salesforce connector payload variable and the local variable: Input | Output | 
         
         connectorOutputPayload ( Fetch Salesforce Data)
         .GET_PROPERTY("AccountId")
                     

| `sf_account_id`  
---|---  
           
         connectorOutputPayload ( Fetch Salesforce Data)
         .GET_PROPERTY("Name")
                     

| `sf_account_name`  
           
         connectorOutputPayload (Check account in BigQuery)
         .FILTER(~obj1 ->
         ~obj1
         .GET_PROPERTY("account_id")
         .TO_STRING()
         .EQUALS(sf_account_id)
         )
         .SIZE()
         .EQUALS("1")
                     

| `account_exists`  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Check account in BigQuery** connector to the **Check account** task.



## Create new BigQuery account

Once you have validated the Salesforce account in BigQuery, and if the account doesn't exist, do the following to create a new account in BigQuery. You also use the same information to create an account in ServiceNow.

###  Add account to BigQuery 

Perform the following steps to configure a **Connectors** task that creates a new entity in the BigQuery **Accounts** table: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Create account in BigQuery`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your BigQuery connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **accounts** from the list of available entities and then select **Create** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



###  Create a new ServiceNow account 

Perform the following steps to configure a **Connectors** task that adds a new account to your ServiceNow instance: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Create account in ServiceNow`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your BigQuery connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **system_user** from the list of available entities and then select **Create** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Transform and map account details

To transform the account details and map it to the BigQuery and ServiceNow connectors, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Mapping for Account Creation`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following input variables: Input variable name | Data type | `new_BQaccount` | `JSON`  
---|---  
`new_SNaccount` | `JSON`  
  7. Create the following mapping to map the Salesforce account ID and name to the BigQuery table: Input | Output | 
         
         new_BQaccount
         .SET_PROPERTY(
         sf_account_id,
         "account_id"
         )
         .SET_PROPERTY(
           sf_account_name,
           "name"
           )
                      

| `connectorInputPayload (Create account in BigQuery)`  
---|---  
           
         new_SNaccount
         .SET_PROPERTY(
         sf_account_id,
         "sys_id"
         )
         .SET_PROPERTY(
          sf_account_name,
          "first_name"
          )
                     

| `connectorInputPayload (Create account in ServiceNow)`  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Mapping for Account Creation** task to the **Create account in BigQuery** connector.
  9. Add an edge connection from the **Mapping for Account Creation** task to the **Create account in ServiceNow** connector.



## Create new order in BigQuery

Do the following to generate an order number and add it in BigQuery. 

###  Add order to BigQuery 

Perform the following steps to configure a **Connectors** task that creates a new entity in the BigQuery **Orders** table: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Create order in BigQuery`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your BigQuery connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Orders** from the list of available entities and then select **Create** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Generate order and map to BigQuery

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Mapping for Order Creation`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following variable: Variable name | Data type | `order_number` | `STRING`  
---|---  
  7. Create the following mapping to generate a new order number and map the order details to the BigQuery connector: Input | Output | 
         
         GENERATE_UUID()
         .SPLIT("-")
         .GET("0")
                      

| `new_order_number`  
---|---  
           
         "{}"
         .TO_JSON()
         .SET_PROPERTY(
         connectorOutputPayload ( Fetch Salesforce Data)
         .GET_PROPERTY("DeliveryInstallationStatus__c")
         ,  
         "order_status"
         )
         .SET_PROPERTY(
         connectorOutputPayload ( Fetch Salesforce Data)
         .GET_PROPERTY("TrackingNumber__c")
         ,  
         "tracking_number"
         )
         .SET_PROPERTY(
         new_order_number
         ,
         "order_number"
         )
                     

| `connectorInputPayload (Create Order in BigQuery)`  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Create account in BigQuery** connector to the **Mapping for Order Creation** task.
  9. Add an edge connection from the **Create account in ServiceNow** connector to the **Mapping for Order Creation** task.
  10. Add an edge connection from the **Mapping for Order Creation** task to the **Create Order in BigQuery** connector.



## Update Salesforce opportunity

Once you have generated the new order number, you update the source Salesforce opportunity

###  Configure the Salesforce connector 

Perform the following steps to configure a **Connectors** task that updates the existing Salesforce opportunity: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Update Salesforce`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your Salesforce connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Opportunity** from the list of available entities and then select **Update** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Map order number to Salesforce

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Mapping to update opportunity`.
  5. Click **Open Data Mapping Editor**.
  6. Create the following mapping to update the Salesforce opportunity: Input | Output | 
         
         "{}"
         .TO_JSON()
         .SET_PROPERTY(
         new_order_number
         ,  
         "OrderNumber__c"
         )
                         

| `connectorInputPayload (Update Salesforce)`  
---|---  
           
         entityId ( Fetch Salesforce Data)
                        

| `entityId (Update Salesforce )`  
           
         "'"
         .CONCAT(entityId ( Fetch Salesforce Data))
         .CONCAT("'")
                       

| `filterClause (Update Salesforce )`  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Create Order in BigQuery** connector to the **Mapping to update opportunity** task.
  8. Add an edge connection from the **Mapping to update opportunity** task to the **Update Salesforce** connector.



##  Add edge condition 

An edge condition lets you specify the conditions that must be met for control of an integration to pass to the task connected by the edge. Now that you have added and configured and the required tasks, you can add an edge condition to define the flow of the integration. 

The following edge condition controls the flow of the integration based on the validation of the account information:

  1. Add an edge connection from the **Check account** task to the **Mapping for Account Creation** task with the following edge condition: 
         
         $account_exists$ = False

  2. Add another edge connection from the **Check account** task to the **Mapping for Order Creation** task with the following edge condition: 
         
         $account_exists$ = True




## Sample integration flow

The following figure shows a sample layout of the integration created using this tutorial.

![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/opportunity-to-order-flow.png)![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/opportunity-to-order-flow.png)

## Publish and test the integration

To publish the integration click **Publish** in the integration editor toolbar.

Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **![image showing the icon for execution logs](https://docs.cloud.google.com/static/images/logs-icon.png)View execution logs for this integration**. The **Execution Logs** page appears.

### Test case 1: To check if an order number is created for a new account ID

Test the integration by logging in to the Salesforce instance and creating a new opportunity. You must create the opportunity in a new account or an account that doesn't exist in your BigQuery table.

To verify the success of your integration:

  1. Go to the **BigQuery** page. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

     * Open the **Accounts** table and check to confirm the insertion of the new opportunity account ID.
     * Open the **Orders** table and check to confirm the insertion of the new order details.
  2. Go to your ServiceNow instance. 
     * Check to confirm if a new account is added to your instance containing the same Salesforce opportunity account ID.
  3. Open Salesforce. 
     * Check to confirm if the opportunity is updated with the new order number.



### Test case 2: To check if an order number is created for an existing account ID in BigQuery

Test the integration by logging in to the Salesforce instance and creating a new opportunity. You must create the opportunity in an existing account that also exists in your BigQuery table.

To verify the success of your integration:

  1. Go to the **BigQuery** page. 

[Go to BigQuery](https://console.cloud.google.com/bigquery)

     * Open the **Accounts** table and check to confirm that NO new account ID is inserted.
     * Open the **Orders** table and check to confirm the insertion of the new order details.
  2. Open Salesforce. 
     * Check to confirm if the opportunity is updated with the new order number.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, unpublish the integration and delete the connections created in Integration Connectors.

  * To unpublish this integration, click **Unpublish** in the integration editor toolbar. See [Delete integrations](https://docs.cloud.google.com/application-integration/docs/delete-integrations) for more information.
  * For information about how to delete a connection, see [Manage connectors](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
