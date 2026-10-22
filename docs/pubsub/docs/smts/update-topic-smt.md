---
url: https://docs.cloud.google.com/pubsub/docs/smts/update-topic-smt/
title: Update topic SMTs \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:06.398476+00:00
---

# Update topic SMTs  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/update-topic-smt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Update topic SMTs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to update a Single Message Transform (SMT) for a Pub/Sub topic. Changes to SMTs take effect within a few minutes. For topic SMTs, the changes apply to new messages published after the SMT is updated.

To update topic SMTs, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API.

## Required roles and permissions

To get the permission that you need to update topic SMTs, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `pubsub.topics.update` permission, which is required to update topic SMTs. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level.

## Update topic SMTs

To update topic SMTs, follow these steps:

### Console

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click the topic for which you want to edit SMTs.

  3. In the topic details page, click **Edit**.

The **Transforms** tab lists all the SMTs that are attached to the topic.

  4. In the Edit topic page, you can do the following tasks:

     1. Add a new SMT. Click **Add a transform**.

     2. Edit an existing SMT. Expand any SMT to edit the SMT.

     3. Rearrange the SMTs. Use the up and down arrows.

     4. Delete an SMT. Click the delete button.

  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [ `gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update)command:
         
         gcloud pubsub topics update TOPIC_ID \
             --message-transforms-file=TRANSFORMS_FILE

Replace the following:

     * TOPIC_ID: The ID or name of the topic you want to update.

     * TRANSFORMS_FILE: The path to the YAML or JSON file containing the updated SMTs.

The following is an example of a YAML transforms file:
           
           - javascriptUdf:
               code: >
                   function redactSSN(message, metadata) {
                     const data = JSON.parse(message.data);
                     delete data['ssn'];
                     message.data = JSON.stringify(data);
                     return message;
                   }
               functionName: redactSSN
           - javascriptUdf:
               code: >
                   function filterHighAmount(message, metadata) {
                     const data = JSON.parse(message.data);
                     if (data['amount'] > 100 ) { return null; }
                     return message;
                   }
               functionName: filterHighAmount

To clear all the SMTs from the topic, use the following command:
    
    gcloud pubsub topics update TOPIC_ID --clear-message-transforms

Replace TOPIC_ID with the ID or name of the topic you want to update.




## What's next

  * [Create a topic with SMTs](https://docs.cloud.google.com/pubsub/docs/smts/create-topic-smt)

  * [Delete topic SMTs](https://docs.cloud.google.com/pubsub/docs/smts/delete-topic-smt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
