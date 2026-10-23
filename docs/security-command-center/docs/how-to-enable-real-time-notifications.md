---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications/
title: Enabling real-time chat notifications \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:44.244615+00:00
---

# Enabling real-time chat notifications  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enabling real-time chat notifications Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

## Overview

Security Command Center provides real-time notifications of findings in the Google Cloud console. This guide describes how to use Google Cloud services and third-party APIs to extend that functionality and receive near real-time notifications in Slack. When you complete the guide, you get alerts about new findings in configured third-party services without logging into the Google Cloud console, allowing for faster triaging of vulnerabilities and threats. Learn more about the different types of [vulnerabilities and threats](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) in Security Command Center.

### Topology

In this guide, you create the configuration that is illustrated in the following diagram.

[ ![Near real-time notifications workflow \(click to enlarge\)](https://docs.cloud.google.com/static/security-command-center/images/real-time-notifications.svg)](https://docs.cloud.google.com/static/security-command-center/images/real-time-notifications.svg) Near real-time notifications workflow for Security Command Center (click to enlarge)

## Objectives

In this guide, you do the following:

  1. Set up a Pub/Sub topic.
  2. Set up Slack.
  3. Write code in Cloud Run functions.
  4. Configure Pub/Sub and Cloud Run functions to send notifications to Slack whenever a new high or critical severity finding is written to Security Command Center.
  5. Troubleshoot notification problems.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Pub/Sub
  * Cloud Run functions
  * Cloud Build



Use the [pricing calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage.

## Before you begin

To complete this guide, you must have the following Identity and Access Management (IAM) roles:

  * Organization Admin (`roles/resourcemanager.organizationAdmin`)
  * Security Center Admin (`roles/securitycenter.admin`)
  * Security Admin (`roles/iam.securityAdmin`)
  * A role with the [`serviceusage.services.use` permission](https://docs.cloud.google.com/iam/docs/permissions-reference), such as Owner (`roles/owner`), Editor (`roles/editor`), or a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles)
  * Create Service Accounts (`roles/iam.serviceAccountCreator`)
  * Pub/Sub Editor (`roles/pubsub.editor`)
  * Billing Account Administrator (`roles/billing.admin`)



The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

### Setting up a project

Complete the following steps to create or select a project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




Estimated time: it takes approximately one hour to set up and test notifications for a single service.

## Setting up a Pub/Sub topic

**Important:** If you already configured Security Command Center to publish findings in Pub/Sub, you can skip to Setting up a messaging app. Otherwise, follow the instructions in this section to set up a Pub/Sub topic.

Pub/Sub is a real-time messaging service that enables messages to be sent and received between independent applications. Learn more about [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/admin).

In this section, you configure Security Command Center to publish findings to a Pub/Sub topic.

To set up and subscribe to a Pub/Sub topic:

  1. Specify your Google Cloud project in an environment variable.

**Note:** This project ID is used throughout this document.
         
         export PROJECT_ID=PROJECT_ID
         

Replace PROJECT_ID with your project ID.

  2. Specify your Google Cloud organization in an environment variable.
         
         export ORG_ID=ORG_ID
         

Replace ORG_ID with your organization ID.

  3. Set the project ID for `gcloud` commands.
         
         gcloud config set project PROJECT_ID
         

  4. Create the Pub/Sub topic where notifications are published.
         
         gcloud pubsub topics create scc-critical-and-high-severity-findings-topic
         

  5. Specify the topic in an environment variable.
         
         export TOPIC=projects/$PROJECT_ID/topics/scc-critical-and-high-severity-findings-topic
         

  6. Create the subscription that notifies Cloud Run functions to send a chat message when messages are published to the topic.
         
         gcloud pubsub subscriptions create scc-critical-and-high-severity-findings-sub \
           --topic scc-critical-and-high-severity-findings-topic
         

**Note:** By default, Pub/Sub subscriptions expire after 31 days of inactivity, defined as subscriptions without active connections, pull requests, or push successes. To keep subscriptions longer, set the `--expiration-period` flag to a higher value or the special value `never`, indicating the subscription never expires. See [Using subscription properties](https://docs.cloud.google.com/pubsub/docs/admin#using_subscription_properties) for more information.
  7. Configure Security Command Center to publish notifications to the topic. Any filter compatible with the ListFindings API can be used.

The following filter publishes notifications for active high and critical severity findings in the `global` location. Learn more about [filtering findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#filtering_findings).
         
         gcloud scc notifications create scc-critical-high-severity \
              --pubsub-topic=$TOPIC \
              --organization=$ORG_ID \
              --location=global \
              --filter '(severity="HIGH" OR severity="CRITICAL") AND state="ACTIVE"' \
              --deletion-notifications-enabled
         

Add the `--deletion-notifications-enabled` flag to receive notifications about finding deletion events due to retention policies. The notification contains the `deletedFinding: true` field set. Ensure your Cloud Run functions or application parses the `deletedFinding` attribute so alerts properly reflect the finding deletions. To disable deletion notifications, update the `NotificationConfig` and set the `--no-deletion-notifications-enabled` flag.

**Note:** If you use VPC Service Controls, you might need to grant access to protected project resources before creating a `NotificationConfig` and in order for notifications to work. For more information, see [Granting perimeter access in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access).



Next, you create or configure your chat app to receive notifications from Pub/Sub.

## Setting up a messaging app

This section describes how to use Pub/Sub and [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) or Cloud Run functions (1st gen) to enable near real-time notifications for Slack.

**Note:** The Slack example shows how to send notifications with basic information (the finding category). You can customize this example to include as much or as little information as you want.

To send notifications to a Slack channel, you do the following:

  * Create a new Slack app with sufficient privileges to post messages to a public Slack channel.
  * Create and deploy a Cloud Run function that posts chat messages to Slack when notifications are received from Pub/Sub.



### Create a new Slack app

In this section, you create a new Slack app to receive notifications.

  1. Navigate to [Slack API apps](https://api.slack.com/apps). The page opens in a new tab.
  2. Sign in or create an account.

  3. Select **Create an App**.

  4. Set **App Name** to "**SCC Finding Notifier**."

  5. Select the **Development Slack Workspace** where you'd like the Slack Bot to post messages, and then click **Create App**.

  6. In the navigation panel, select **OAuth & Permissions**.

  7. Navigate to the **Scopes** section. Scopes fall into two categories:

     * **Bot Token Scopes**
     * **User Token Scopes**
  8. For this exercise, you don't need to add a User Token Scope. Under Bot Token Scopes, click **Add an OAuth Scope** and enter:

     * `chat:write`
     * `chat:write.public`
  9. Go to the top of the **OAuth & Permissions** page and click **Install App to Workspace**.

  10. In the confirmation dialog, click **Allow**.

  11. Copy the **Bot User OAuth Access Token** for use in the Cloud Function.




Next, you deploy a Cloud Run function to send notifications to a Slack group.

### Create the Slack Cloud Run function

In this section, you deploy a function to send notifications to your Slack account. The code sample in this section is written in Python, but you can use any language that is supported by Cloud Run functions.

**Note** : This code sample requires you to hardcode user or application credentials. For added security, and to safeguard credentials, consider using Secret Manager with Cloud Run functions. For instructions, see [Using secrets](https://docs.cloud.google.com/functions/docs/configuring/secrets) in the Cloud Run functions documentation.

  1. In the Google Cloud console, go to Cloud Run functions **Services** page.

[Go to Services](https://console.cloud.google.com/projectselector2/run/services?supportedpurview=project)

  2. Select the ID of the project that contains the Pub/Sub topic.

  3. Click **Write a function** , and fill in the fields:

     1. For **Service name** , enter `slack-chat-high-and-critical-findings`.
     2. For **Region** , select the region where you want to store the service.
     3. For **Runtime** , select the Python version to use to run your function.
  4. Click **Add trigger** and select **Pub/Sub trigger**.

  5. Enter the details of the Pub/Sub topic that you created in Setting up a Pub/Sub topic, and click **Save trigger**.

  6. Click **Create**. The service details are displayed.

  7. In the **Source** pane of the **Source** tab, click **requirements.txt**.

  8. In the code editor, add `requests` and `functions-framework==3.*`:
         
         requests
         functions-framework==3.*
         

  9. In the **Source** pane, click **main.py**.

  10. In the code editor, replace the code with the following:
         
         import base64
         import json
         import requests
         import functions_framework
         
         TOKEN = "BOT_ACCESS_TOKEN"
         
         @functions_framework.cloud_event
         def send_slack_chat_notification(cloud_event):
         
             pubsub_message = base64.b64decode(cloud_event.data["message"]["data"]).decode('utf-8').strip()
             message_json = json.loads(pubsub_message)
         
             finding = message_json['finding']
         
             requests.post("https://slack.com/api/chat.postMessage", data={
                 "token": TOKEN,
                 "channel": "#SLACK_CHANNEL_NAME",
                 "text": f"A high severity finding {finding['category']} was detected."
             })
         

Replace the following:

     * `BOT_ACCESS_TOKEN`: the **Bot User OAuth Access Token** that you created with the Slack app.
     * `SLACK_CHANNEL_NAME`: the Slack channel where you want to send the notifications.
  11. In the **Function entry point** field, enter the name of the function in the code sample: `send_slack_chat_notification`.

  12. Click **Save and redeploy**. If a green check mark appears next to the function name, your function has been successfully deployed. This process can take a few minutes.




If the preceding steps completed without errors, the setup is complete and you start receiving notifications. Keep in mind:

  * You receive a separate chat message for each individual critical or high severity finding. The frequency or number of notifications depends on the resources within your organization.
  * Notifications are published and sent in near real time. However, the immediacy of messages is not guaranteed and multiple factors can cause delays, including issues with Slack.



To change the notifications workflow, you can do the following:

  * Change recipients by updating your Cloud Run function.
  * Change which findings trigger notifications by updating the filter for the Pub/Sub topic.



## Testing notifications

To test whether notifications are properly configured, follow these instructions to toggle high severity findings between active and inactive states.

  1. Go to the Security Command Center **Findings** page.  
[Go to the Findings page](https://console.cloud.google.com/security/command-center/findings)  

  2. Select your organization, if prompted.
  3. In the **Quick filters** panel, go to the **Severity** section and select either **High** or **Critical**. The **Findings query results** panel updates to show findings of only the selected severity.
  4. In the **Findings query results** panel, select a finding by checking the box next to its name.
  5. From the **Change active state** menu in the **Findings query results** action bar, select **Inactive**. If the current findings query shows only active findings, the finding is removed from the query results.
  6. In the **Quick filters** panel, go to the **State** section and change the selections so that only **Inactive** is selected. The **Findings query results** panel updates to show only inactive findings.
  7. In the **Findings query results** panel, select the finding that you marked inactive.
  8. From the **Change active state** menu in the **Findings query results** action bar, select **Active**.
  9. Check your Slack messages. A message similar to the following image is displayed:



![Slack notification](https://docs.cloud.google.com/static/security-command-center/images/slack_notification.png)

## Troubleshooting

If chat messages are not being sent or received, follow these steps to identify and resolve potential issues.

  1. Check [Stackdriver logs](https://console.cloud.google.com/projectselector2/logs/viewer) for your Cloud Run function to determine whether the function is being invoked. If it is not being invoked, ensure that notifications are set up correctly.

  2. If the Cloud Run function is being invoked, then it might be crashing. Check for errors in Cloud Run functions using [Google Cloud console Error Reporting](https://console.developers.google.com/errors).




## Cleaning up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Deleting the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Deleting individual resources

  1. Delete your notification configuration:
         
         gcloud scc notifications delete scc-critical-high-severity \
             --organization=ORG_ID \
             --location=global
         

Replace ORG_ID with your organization ID.

To maintain your configuration and temporarily pause notifications, comment out the `send` or `post` calls in your Cloud Run function.

  2. Delete your Cloud Run function:

     1. Go to Cloud Run functions.  
[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)  

     2. Click the checkbox next to the function you want to delete.
     3. Click **Delete** delete.
  3. Delete the service account:

     1. Go to the **Service accounts** page.  
[Go to the Service accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)
     2. Select a project.
     3. Select the service account you want to delete, and then click **Delete** delete.



## What's next

  * Read more about [notification errors](https://docs.cloud.google.com/security-command-center/docs/error-messages).
  * Learn about [filtering notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).
  * Learn how to remediate [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings) and [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings) findings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
