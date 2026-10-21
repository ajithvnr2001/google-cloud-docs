---
url: https://docs.cloud.google.com/application-integration/docs/automate-salesforce-case-routing/
title: Automate Salesforce case routing assignments \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:47.298135+00:00
---

# Automate Salesforce case routing assignments  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/automate-salesforce-case-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback 

#  Automate Salesforce case routing assignments Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes a use case on how you can use Application Integration to automate the business process flow of routing and assigning a Salesforce customer case. 

## Overview

In this tutorial, you'll create an integration that uses a Salesforce trigger to subscribe to a case channel in Salesforce. A new case in Salesforce invokes the integration, which extracts the case ID and case type. Depending on the case type, a new issue or incident is created in Jira Cloud or ServiceNow, respectively. 

![Salesforce Case flow diagram](https://docs.cloud.google.com/static/application-integration/images/case-to-incident.png)![Salesforce Case flow diagram](https://docs.cloud.google.com/static/application-integration/images/case-to-incident.png)

## Objectives

This tutorial shows you how to complete the following tasks in your integration:

  * Set up Salesforce Trigger to invoke your integration.
  * Add and configure Connectors tasks for Salesforce, Jira Cloud, and ServiceNow connections.
  * Add and configure data mapping tasks to extract and map case details.



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

### Verify Salesforce user setup

This tutorial assumes that you have an existing Salesforce developer account with the required user setup and permission set. Verify that your account has _Change Data Capture (CDC)_ enabled. For information about creating a new account, see [Set up an integration user](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger#set-up-an-integration-user). 

### Verify Jira Cloud account

This tutorial uses Jira Cloud. You can either use your existing Jira Cloud account or create a new one. Verify that your Jira Cloud project and boards are set up. For more information about Jira Cloud, see [Jira software documentation](https://www.atlassian.com/software/jira/guides/getting-started/introduction#what-is-jira-software). 

### Verify ServiceNow instance

This tutorial uses a ServiceNow free Personal Developer Instance (PDI). You can either use your existing ServiceNow instance or create a new one. Verify that your instance is active and note down its instance URL. For more information about PDI, see [ServiceNow PDI documentation](https://developer.servicenow.com/dev.do#!/guides/rome/developer-program/pdi-guide/personal-developer-instance-guide-introduction). 

### Configure connections

For this tutorial, you must configure the following connections in [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs):

**Tip:** We recommend that you create the following connections in the `us-central1(lowa)` region. 

Salesforce connection
    Configure a Salesforce connection in Integration Connectors. For information on configuring a Salesforce connector, see [Salesforce connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/salesforce/configure).
Jira Cloud connection
    Configure a Jira Cloud connection in Integration Connectors using your project URL tp create Jira issues in your project. Make sure to note down the project ID and issue ID. For information on configuring a Jira Cloud connector, see [Jira Cloud connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/jiracloud/configure).
ServiceNow connection
    Configure a ServiceNow connection in Integration Connectors using your instance URL to create incidents in ServiceNow. For information on configuring a ServiceNow connector, see [ServiceNow connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure).

## Create integration

To create a new integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter `salesforce-case-integration`.
     2. **Description:** Enter `Demo integration created for tutorial`.
     3. **Region:** Select `us-central1` from the list of [supported regions](https://docs.cloud.google.com/application-integration/docs/locations).
     4. Click **Create** to open the integration editor.



## Set up integration trigger

Once you have successfully created your integration, you can add and configure an integration trigger that invokes the integration for an identified event.

For this tutorial, a Salesforce trigger is used to invoke the integration for every new case that is created in Salesforce. To add and configure a **Salesforce trigger** in your `salesforce-case-integration` integration, do the following: 

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

        * **Salesforce object name** : Enter `Case`.
        * Click **Add**.
     4. **Operation** : Select **Create** from the drop-down list

Changes to the properties are saved automatically.




## Map trigger payload to Salesforce connector

When the integration is invoked using the Salesforce trigger, you extract the case ID and map it to a Salesforce connector to retrieve additional details of the case. 

### Connect to the Salesforce account

Perform the following steps to add and configure a **Connectors** task to retrieve the case details using the **Salesforce** connection: 

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
     5. Under **Set entities/actions** , select **Case** from the list of available entities and then select **Get** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Extract and map case ID

A **Data Mapping** task is used to map and extract the case details between that Salesforce trigger and the Salesforce connector.

To add and configure the data mapping in your integration, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Select the **Data Mapping** element on the designer to view the task configuration pane. 
  4. Click  edit  and rename the **Data Mapping** task to `Get Case ID`.
  5. Click **Open Data Mapping Editor**. 

The **Data Mapping Editor** lets you map input variables to the desired output variables, using the available transformation functions. The output is then available as a variable to any other integration task or trigger. For more details on mapping variables, see [Add a mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task#add-map).

  6. Map the trigger —`SalesforceTriggerCdcRecordID`—output variable to the auto-generated connector—`entityId(Fetch Salesforce Data)`—input variable. 

Once your mapping is complete, close the pane. Any changes will be autosaved. 

  7. Add an edge connection from the **Salesforce** trigger to the **Get Case ID** task.
  8. Add an edge connection from the **Get Case ID** task to the **Fetch Salesforce Data** connector.



## Extract case type

Once you retrieve all the case details from the Salesforce connector, you extract the case type and route it to Jira Cloud or ServiceNow application.

To extract the Salesforce case type, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Get case type`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following output variable: Output variable name | Data type | `sf_case_type` | `STRING`  
---|---  
  7. Create the following mapping between the Salesforce connector payload variable and the local variable: Input | Output | 
         
         connectorOutputPayload (Fetch Salesforce Data)
         .GET_PROPERTY("Type")
                     

| `sf_case_type`  
---|---  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Fetch Salesforce Data** connector to the **Get case type** task.



## Create new Jira issue

Once you have extracted the Salesforce case type, and if the case is of type: `Engineering`, then route it to Jira Cloud as a new issue.

###  Connect to Jira project 

Perform the following steps to configure a **Connectors** task that creates a new issue in your Jira project: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Create issue in Jira`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your Jira Cloud connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **Issues** from the list of available entities and then select **Create** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Transform and map issue details

To transform the case details and map it to a Jira issue, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Mapping for issue creation`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following variables: Variable name | Data type | Default value | `jira_project-id` | `STRING` | 
         
         JIRA_PROJECT_ID

Replace JIRA_PROJECT_ID with your Jira project ID.  
---|---|---  
`jira_issue_type_id` | `STRING` | 
         
         JIRA_ISSUE_TYPE_ID

Replace JIRA_ISSUE_TYPE_ID with any of the following issue type ID: 
     * `1000` \- for _Epic_
     * `1001` \- for _Story_
     * `1002` \- for _Task_
     * `1003` \- for _Sub-task_
     * `1004` \- for _Bug_  
  7. Create the following mapping: Input | Output | 
         
         "{ "IssueTypeId": jira_issue_type_id, "ProjectId": jira_project_id }"
         .TO_JSON()
         .SET_PROPERTY(
         connectorOutputPayload.Description (Fetch Salesforce Data),  
         "Description"
         )
         .SET_PROPERTY(
         connectorOutputPayload.Subject (Fetch Salesforce Data),  
         "Summary"
         )
                      

| `connectorInputPayload (Create issue in Jira)`  
---|---  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Mapping for issue creation** task to the **Create issue in Jira** connector.



## Create new ServiceNow incident

If the extracted case from Salesforce is of type: `Sales`, then route it to ServiceNow as a new incident.

###  Connect to ServiceNow 

Perform the following steps to configure a **Connectors** task that create a new incident to your ServiceNow instance: 

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Connectors** element in the integration editor.
  3. Click the **Connectors** task element on the designer to view the **Connectors task configuration pane**.
  4. Click  edit  and rename the **Connectors** to `Create incident in ServiceNow`.
  5. Click **Configure connector**.
  6. Do the following in the **Connectors Task Editor** page: 
     1. Under **Select connection** , choose the `us-central1` region.
     2. Select your ServiceNow connection from the list of available connections.
     3. Click **Next**.
     4. Under **Type** , choose **Entities**.
     5. Under **Set entities/actions** , select **incident** from the list of available entities and then select **Create** as the **Operation**.
     6. Click **Done** to complete the connection configuration and close the pane.



### Transform and map incident details

To transform the case details and map it to a ServiceNow incident, do the following:

  1. In the integration editor, click **Tasks** to display a list of available tasks.
  2. Click and place the **Data Mapping** element in the integration editor.
  3. Click the **Data Mapping** element on the designer to view the task configuration pane.
  4. Click  edit  and rename the **Data Mapping** task to `Mapping for incident creation`.
  5. Click **Open Data Mapping Editor**.
  6. Click **\+ Add new variable** and create the following input variables: 
  7. Create the following mapping: Input | Output | 
         
         "{}"
         .TO_JSON()
         .SET_PROPERTY(
         connectorOutputPayload.Description (Fetch Salesforce Data),  
         "description"
         )
         .SET_PROPERTY(
         connectorOutputPayload.Subject (Fetch Salesforce Data),  
         "short_description"
         )
                      

| `connectorInputPayload (Create incident in ServiceNow)`  
---|---  
  
Once your mapping is complete, close the pane. Any changes will be autosaved. 

  8. Add an edge connection from the **Mapping for incident creation** task to the **Create incident in ServiceNow** connector.



##  Add edge condition 

An edge condition lets you specify the conditions that must be met for control of an integration to pass to the task connected by the edge. Now that you have added and configured and the required tasks, you can add an edge condition to define the flow of the integration. 

The following edge condition controls the flow of the integration based on the type of the Salesforce case:

  1. Add an edge connection from the **Get case type** task to the **Mapping for issue creation** task with the following edge condition: 
         
         $sf_case_type$ = "Engineering"

  2. Add another edge connection from the **Get case type** task to the **Mapping for incident creation** task with the following edge condition: 
         
         $sf_case_type$ = "Sales"




## Sample integration flow

The following figure shows a sample layout of the integration created using this tutorial.

![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/case-to-incident-flow.png)![Sample image showing the integration flow](https://docs.cloud.google.com/static/application-integration/images/case-to-incident-flow.png)

## Publish and test the integration

To publish the integration click **Publish** in the integration editor toolbar.

Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **![image showing the icon for execution logs](https://docs.cloud.google.com/static/images/logs-icon.png)View execution logs for this integration**. The **Execution Logs** page appears.

### Test case 1: To check if a Jira issue is created for an enginnering case

Test the integration by logging in to the Salesforce instance and creating a new case. You must enter `Engineering` in the **Type** field while creating the case.

To verify the success of your integration:

Go to your Jira Cloud account. 

  * Check to confirm if a new issue is created in your project containing the Salesforce case description and summary.



### Test case 2: To check if a ServiceNow incident is created for a sales case

Test the integration by logging in to the Salesforce instance and creating a new case. You must enter `Sales` in the **Type** field while creating the case.

To verify the success of your integration:

Go to your ServiceNow instance. 

  * Check to confirm if a new incident is created in your instance containing the Salesforce case description and summary.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, unpublish the integration and delete the connections created in Integration Connectors.

  * To unpublish this integration, click **Unpublish** in the integration editor toolbar. See [Delete integrations](https://docs.cloud.google.com/application-integration/docs/delete-integrations) for more information.
  * For information about how to delete a connection, see [Manage connectors](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
