---
url: https://docs.cloud.google.com/pubsub/docs/validate-schema-definition/
title: Validate schema definitions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:58.860609+00:00
---

# Validate schema definitions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/validate-schema-definition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Validate schema definitions Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to validate schemas for Pub/Sub topics. The validation check does not check the compatibility of the new revision with the older revisions.

## Before you begin

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).



### Required roles and permissions

To get the permissions that you need to validate schemas definitions and manage them, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to validate schemas definitions and manage them. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to validate schemas definitions and manage them:

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

## Validate a schema definition

You can validate a schema by using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

Follow the steps discussed in [Create a schema](https://docs.cloud.google.com/pubsub/docs/create-schemas).

The validation check does not check the compatibility of the new revision with the older revisions.

## What's next

  * [Validate a message for a schema](https://docs.cloud.google.com/pubsub/docs/validate-schema-message)

  * [Publish messages to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/publish-topics-schema)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
