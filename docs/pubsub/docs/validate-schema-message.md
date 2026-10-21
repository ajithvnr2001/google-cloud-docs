---
url: https://docs.cloud.google.com/pubsub/docs/validate-schema-message/
title: Validate a message for a schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:58.443313+00:00
---

# Validate a message for a schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/validate-schema-message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Validate a message for a schema Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to validate schemas for Pub/Sub topics.

You can validate that messages adhere to a certain schema, before or after you create a schema resource. This step ensures that the messages you intend to send through a topic associated with a schema actually match before applying the schema.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to validate schema messages and manage them, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to validate schema messages and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to validate schema messages and manage them:

  * Create schema: `pubsub.schemas.create`
  * Attach schema to topic: `pubsub.schemas.attach`
  * Commit a schema revision: `pubsub.schemas.commit`
  * Delete a schema or a schema revision: `pubsub.schemas.delete`
  * Get a schema or schema revisions: `pubsub.schemas.get`
  * List schemas: `pubsub.schemas.list`
  * List schema revisions: `pubsub.schemas.listRevisions`
  * Rollback a schema: `pubsub.schemas.rollback`
  * Validate a message: `pubsub.schemas.validate`
  * Get the IAM policy for a schema: `pubsub.schemas.getIamPolicy`
  * Configure the [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy) for a schema: `pubsub.schemas.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can grant roles and permissions to principals such as users, groups, domains, or service accounts. You can create a schema in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Validate a message for a schema

### Console

  1. In the Google Cloud console, go to the **Pub/Sub schemas** page.

[Go to Schemas](https://console.cloud.google.com/cloudpubsub/schema)

The list of schemas is displayed.

  2. Click the **Schema ID** of an existing schema.

The **Schema details** page for the schema opens.

  3. In the **Revisions** section, click the revision for which you want to validate a message.

  4. In the **Details** section, click **Test message**.

  5. In the **Test message** window, select a type of **Message encoding**.

  6. In the **Message** body, enter a test message.

  7. Click **Test**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To validate a message against a schema use the [gcloud pubsub schemas validate-message](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-message) command. 
         
         gcloud pubsub schemas validate-message --message=MESSAGE \
             --message-encoding=MESSAGE_ENCODING \
             (--schema-name=SCHEMA_NAME | \
             --type=TYPE \
             (--definition=DEFINITION | \
             --definition-file=DEFINITION_FILE))
         

Replace the following:

     * MESSAGE: message to validate against the schema

     * MESSAGE_ENCODING: encoding of the message. Specify one of the following values: `binary` or `json`.

     * SCHEMA_NAME: name or full path of an existing schema.

     * TYPE: type of inline schema. Specify one of the following values: `avro` or `protocol-buffer`.

     * DEFINITION: inline schema definition.

     * DEFINITION_FILE: file containing the schema definition. 




## What's next

  * [Validate a schema definition when you create a topic](https://docs.cloud.google.com/pubsub/docs/create-schemas#create-schema)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
