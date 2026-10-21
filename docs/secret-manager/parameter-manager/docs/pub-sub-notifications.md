---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/pub-sub-notifications/
title: Set up Pub/Sub notifications \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:08:27.706784+00:00
---

# Set up Pub/Sub notifications  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/pub-sub-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Set up Pub/Sub notifications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up notifications for updates to [parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter) and [parameter versions](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version).

Parameter Manager integrates with Pub/Sub to provide event notifications for changes to both parameters and parameter versions. You can use these notifications to initiate workflows, such as restarting an application when a new parameter version is added, or notifying security engineers when a parameter is deleted. For more information on how to use these notifications to start workflows, see the [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) documentation.

## Before you begin

  1. To set up Parameter Manager, complete the following:

     * Create or use an existing project to hold your Parameter Manager resources.

     * If necessary, complete the steps mentioned in the [Prepare your environment](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment) page.

  2. To set up Pub/Sub, complete the following:

     * Create or use an existing project to hold your Pub/Sub resources.

     * If necessary, [enable the Pub/Sub API](https://docs.cloud.google.com/pubsub/docs/create-topic-console#before-you-begin).

  3. Authenticate to Google Cloud using the following command:
         
         $ gcloud auth login --update-adc
             




## Create Pub/Sub topics

Follow the [Pub/Sub quickstart](https://docs.cloud.google.com/pubsub/docs/create-topic-console) to create topics in your Pub/Sub project in the Google Cloud console. Alternatively, create topics in the Google Cloud CLI using the following command:

### gcloud

Before using any of the command data below, make the following replacements: 

  * PUBSUB_PROJECT_ID: the ID of the project in which to create subscriptions
  * PUBSUB_TOPIC_NAME: the name of the topic



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud pubsub topics create "projects/PUBSUB_PROJECT_ID/topics/PUBSUB_TOPIC_NAME"

Retain the option to add a default subscription. Don't select any other option.

## Create a sink to route log entries

Configure Cloud Logging to route log entries to your Pub/Sub topic in the project where the log entries originate. To do this, follow these steps:

  1. In the Google Cloud console, go to the [Log Router](https://console.cloud.google.com/logs/router) page.
  2. If you use the search bar, select the result with the subheading **Logging**.
  3. Click **Create Sink** , enter a name and description, and then click **Next**.
  4. In the **Sink Service** menu, select **Cloud Pub/Sub topic**. Select your Pub/Sub topic, and then click **Next**.
  5. Select the log entries to include in the sink, and click **Next**.
  6. Optional: Select log entries to exclude.
  7. Click **Create Sink**. A dialog appears with the message `Sink created` confirming the successful creation and permissions for routing matching log entries.
  8. Grant the Pub/Sub Publisher role (`roles/pubsub.publisher`) to the sink's writer identity. Refer to [Set destination permissions](https://docs.cloud.google.com/logging/docs/routing/permissions#grant_roles) for details on obtaining the writer identity and granting roles.



Cloud Logging now sends log entries to your Pub/Sub topic.

## Check logs published to Pub/Sub topic

Log entries are generated whenever you perform the following operations:

  * Create a new parameter or parameter version within Parameter Manager.
  * Retrieve the details of a specific parameter or parameter version using its identifier.
  * List all parameters or parameter versions within a specified project.
  * Modify an existing parameter or parameter version.
  * Remove a parameter or parameter version.



To view log entries published to your Pub/Sub topic:

  1. Open the subscriber for your topic.
  2. Click **Pull messages**. The resulting list shows the log entries that match the filter criteria defined in your log sink.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
