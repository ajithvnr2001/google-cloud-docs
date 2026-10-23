---
url: https://docs.cloud.google.com/pubsub/docs/smts/delete-subscription-smt/
title: Delete subscription SMTs \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:27.530135+00:00
---

# Delete subscription SMTs  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/delete-subscription-smt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Delete subscription SMTs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete Single Message Transforms (SMTs) from an existing Pub/Sub subscription.

To delete subscription SMTs, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API.

## Required roles and permissions

To get the permissions that you need to delete subscription SMTs, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete subscription SMTs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete subscription SMTs:

  * Grant the delete a subscription permission on the subscription: `pubsub.subscriptions.delete`
  * Grant the view a subscription permission on the project. This permission is only required if you are using the Google Cloud console: `pubsub.subscriptions.view`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level.

## Delete subscription SMTs

To delete subscription SMTs, follow these steps:

### Console

  1. In the Google Cloud console, go to the Pub/Sub **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscriptions)

  2. Click the subscription for which you want to delete an SMT.

  3. In the subscription details page, click **Edit**.

The **Transforms** tab lists all the SMTs that are attached to the subscription.

  4. Click the delete button for the SMT you would like to delete.

  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. This command deletes all SMTs associated with the specified subscription.

Run the [`gcloud pubsub subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update) command with the `--clear-message-transforms` flag:
         
         gcloud pubsub subscriptions update SUBSCRIPTION_ID \
             --clear-message-transforms

Replace the following:

     * SUBSCRIPTION_ID: The ID or name of the subscription you want to update.

To instead remove a single SMT, refer to [Update subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/update-subscription-smt) and create a new `message-transforms-file` that excludes the SMT you wish to delete.




## What's next

  * [Create a subscription with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt)

  * [Update subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/update-subscription-smt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
