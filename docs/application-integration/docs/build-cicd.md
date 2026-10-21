---
url: https://docs.cloud.google.com/application-integration/docs/build-cicd/
title: Build CICD for your integration \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:35.442411+00:00
---

# Build CICD for your integration  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/build-cicd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback 

#  Build CICD for your integration Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to automate promoting an integration between different environments in different Google Cloud projects using [config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var) ([preview](https://cloud.google.com/products#product-launch-stages)).

**Note:** You cannot use config variables to configure entity operations and actions for connectors.**Tip:** To learn how to store integration and connector assets to a source code repository, promote changes across environments, and how such deployments can be automated, see the [CICD for Application Integration](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/CI-CD-for-Application-Integration/ta-p/722811) blog. 

## Overview

In this tutorial, you'll automate Application Integration deployments using config variable for a sample integration. This sample integration flow calls an API and publishes the response from the API to a Pub/Sub topic. This sample is meant to illustrate the use of **Call REST Endpoint** and **Connectors** tasks. You can store the sample integration in GitHub repositories that correspond to the different environments and Google Cloud projects. 

## Objectives

This tutorial shows you how to complete the following tasks in your integration:

  * Create an integration.
  * Create config variables and use them in your integration.
  * Promote your integration to another environment.



## Costs

In this tutorial, you use the following billable components of Google Cloud:

  * [ Application Integration](https://docs.cloud.google.com/application-integration/docs/pricing)
  * [ Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/pricing)



The instructions in this tutorial are designed to keep your resource usage within the limits of Google Cloud [Free cloud features and trial offer](https://docs.cloud.google.com/free/docs/free-cloud-features). 

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

  4. Enable the Secret Manager API, Connectors API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,connectors.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Pub/Sub Publisher (`roles/pubsub.publisher`)** role to the service account. 

To grant the role, find the **Select a role** list, then select **Pub/Sub Publisher (`roles/pubsub.publisher`)**. 

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

  8. Enable the Secret Manager API, Connectors API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,connectors.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Pub/Sub Publisher (`roles/pubsub.publisher`)** role to the service account. 

To grant the role, find the **Select a role** list, then select **Pub/Sub Publisher (`roles/pubsub.publisher`)**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 




## Create a Pub/Sub topic

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click **Create topic**.

  3. In the **Topic ID** field, enter an ID for your topic. For more information about naming topics, see [Guidelines to name a topic, subscription, schema, or snapshot. ](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names)

  4. Retain the option **Add a default subscription**.

  5. Do not select the other options.

  6. Click **Create topic**.




## Configure a Pub/Sub connector

  1. In the [Google Cloud console](https://console.cloud.google.com/), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create New** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Pub/Sub** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter `pub-sub-connector`. 
     4. **Service Account** : Select a service account that has the required roles.
     5. **Project ID** : Google Cloud project ID where the Pub/Sub instance resides. 
     6. **Topic ID** : Enter the name of your Pub/Sub topic. 
     7. Click **Next**.
  5. In the **Authentication** section, click **NEXT**.
  6. **Review** : Review your connection and authentication details.
  7. Click **Create**.



## Create a new integration

After you Set up Application Integration, you can create a new integration: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Click add_box **Create integration** and provide the following details in the **Create Integration** page: 
     1. **Integration name:** Enter a name for your integration. For example, `build-cicd`.
     2. **Description:** Optionally, enter a description for your integration. For example, `Demo integration created for CICD tutorial`.
     3. **Region:** Select the region `us-central1` from the list of provisioned regions. If the region that you want to select is not provision, see [Provision a new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#provision-new-region). To see a list of supported regions, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).
     4. **Service account** : This field appears if you have enabled governance for your region. Select the service account for your integration. To learn how to enable governance for your region, see [Edit region](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region).
     5. Click **Create**. This opens the integration editor page in which you can add the [tasks](https://docs.cloud.google.com/application-integration/docs/tasks) and the [triggers](https://docs.cloud.google.com/application-integration/docs/triggers) to build your integration.



## Create an integration flow

### Add an API trigger and a Call REST Endpoint

To add an **API trigger** trigger, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**

The **Integrations List** page appears listing all the integrations available in the Google Cloud project. 

  3. Select the `build-cicd` integration. 

This opens the integration in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Triggers > API Trigger** to add the trigger. 
  5. In the _integration editor_ navigation bar, click **Tasks > Call REST Endpoint** to add the task. 
  6. Add an edge connection from the **API trigger** element to the **Call REST Endpoint** element by hovering over a control point on the **API trigger** element, then clicking and dragging a line to a control point on the **Call REST Endpoint** task element. 



### Create config variables

To create config variables, follow these steps: 

  1. In the integration editor navigation bar, click last_page (Toggle panel) to bring up the **Variables** pane.
  2. Click **+Create**.
  3. Do the following in the **Create Variable** pane: 
     1. For **Name** , enter `url`. 

Application Integration adds ``CONFIG_` prefix to the config variables. If you want to add the config variable to your integration using APIs, use the following format for config variables: ``CONFIG_CONFIG_VARIABLE_NAME``. For information about how to download and upload integrations, see [Upload and download integrations](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations).

     2. For **Variable type** , select **Config Variable**.
     3. For **Data type** , select **String**.
     4. Click **Create**. 

The config variable appears in the **Variables** pane.

  4. Repeat Step 2 and 3 to add the following config variable: 
     * **Name:** `connection_name`
     * **Variable type:** `Config Variable`
     * **Data type:** `String`



### Add and configure Call REST Endpoint

To create a config variable, follow these steps: 

  1. In the _integration editor_ , click the **Call REST Endpoint** task to open the task configuration pane. Then, do the following: 
     1. Expand the **Task input** section.
     2. In the **Endpoint base URL** click **Variable** and add `$`CONFIG_url`$`.



### Add and configure a Connectors task

  1. In the _integration editor_ navigation bar, click **Task > Connectors**. 
  2. Click **Configure Connectors**.
  3. From the **Region** list, select the region where you created your Pub/Sub connector.
  4. In the **Connection** field, select the Pub/Sub connector that you created in the preceding step.
  5. In the **Type** section, select **Actions**.
  6. In the **Set entities/actions** section, for **Actions** , select **publishMessage**.
  7. In the **Default value** , add the default value for the config variable. 
  8. Click **Create**.
  9. In the **Connectors** task configuration pane, expand the **Connection details** section to update the following field: 
     1. In the **Connection name** field, click **Variable** and select `$`CONFIG_connection_name`$`.



### Add a Data Mapping task

  1. In the _integration editor_ navigation bar, click **Task > Data mapping**. 
  2. Add an edge connection from the **Call REST Endpoint** element to the **Data Mapping** element by hovering over a control point on the **Call REST Endpoint** element, then clicking and dragging a line to a control point on the **Data Mapping** task element. 
  3. Add another edge connection from the **Data Mapping** element to the **Connectors** element by hovering over a control point on the **Data Mapping** element, then clicking and dragging a line to a control point on the **Connectors** task element. 
  4. In the Data Mapping task configuration pane, click **Open Data Mapping Editor**. 
  5. Map the output variable of the Call REST Endpoint task to the input variable of the Connectors task.



## Publish the integration

To publish the integration, follow these steps: 

  1. To publish the integration click **Publish** in the integration editor toolbar. 

The _Publish integration_ dialog appears.

  2. In the _Publish integration_ dialog, enter the value for the following config variables: 
     1. `url`: Enter the name of the endpoint URL.
     2. `connection_name`: Enter the name of the Pub/Sub connector that you created in the preceding step.
  3. Click **Publish**.
  4. Upon successfully publishing your integration, you can view and inspect the [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) of the published integration. To view logs, click **Logs** in the toolbar of the integration editor.



## Promote integration across environments

To promote your integration across environments, you can use the `integrationcli` tool, which is an open-source tool that lets you interact with [Application Integration APIs](https://docs.cloud.google.com/application-integration/docs/reference/rest) and [Integration Connectors APIs](https://docs.cloud.google.com/integration-connectors/docs/reference/rest). This tool lets you manage integration entities such as integrations, auth configs, and so on. For information about how to generate the scaffold for the integration and apply the changes generated by the scaffold, see [Introduction to `integrationcli`](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/CI-CD-for-Application-Integration/ta-p/722811#toc-hId--834912134) in the community blog.

You can also promote changes across environments by setting up DevOps pipelines for example, by using Jenkins, GitLab, Cloud Build, and so on. For more information, see [Integration with Cloud Build](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/CI-CD-for-Application-Integration/ta-p/722811#toc-hId--1425956340).

If you don't want to use `integrationcli`, you can manually [download and upload the integration](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations) to a new project. You'll have to create the connectors in the new project manually as they are currently not downloadable. When you publish the integration in the new environment, Application Integration enables you to enter values for the config variables.

## What's next

  * Explore [sample integrations](https://github.com/GoogleCloudPlatform/application-integration-samples) in GitHub.
  * Learn more about [config variables](https://docs.cloud.google.com/application-integration/docs/variables).
  * Learn more about the [`integrationcli`](https://github.com/GoogleCloudPlatform/application-integration-management-toolkit) tool.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
