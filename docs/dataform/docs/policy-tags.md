---
url: https://docs.cloud.google.com/dataform/docs/policy-tags/
title: Control column access \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:19.114869+00:00
---

# Control column access  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/policy-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Control column access Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We recommend using [BigQuery data governance tags (Preview)](https://docs.cloud.google.com/bigquery/docs/tags#data-governance-tags) instead of policy tags for column-level security. Dataform can [automatically preserve only data governance tags across workflow executions](https://docs.cloud.google.com/dataform/docs/create-tables#preserve-access-controls). Dataform can't preserve legacy policy tags.

This document shows you how to control column access by adding BigQuery policy tags to table columns with [Dataform core](https://docs.cloud.google.com/dataform/docs/overview#dataform-core).

You can set [BigQuery policy tags](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) on table columns in the `config` block in a table definition SQLX file.

## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. [Create a table](https://docs.cloud.google.com/dataform/docs/create-tables#create-table).




### Required roles

To get the permissions that you need to add a BigQuery policy tag to a table in Dataform, ask your administrator to grant you the [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) IAM role on workspaces. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Additionally, you must grant the [BigQuery roles for column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro#roles) to your [custom service account](https://docs.cloud.google.com/dataform/docs/access-control#about-service-accounts).

## Add a BigQuery policy tag

To add a BigQuery policy tag to a table column, follow these steps:

  1. Go to your development workspace.
  2. In the **Files** pane, expand `definitions/`.
  3. Select a table definition SQLX file.
  4. In the `config` block, add a full tag identifier to a selected column in the following format:
         
         columns: {
             column_name: {
               bigqueryPolicyTags: ["FULL_TAG_IDENTIFIER"]
             }
           }
         

Replace FULL_TAG_IDENTIFIER with the full identifier of the selected tag.

  5. Optional: Click **Format**.




The following code sample shows the `projects/example-project/locations/us/taxonomies/123456789/policyTags/123456789` sample BigQuery policy tag added to `column1`:
    
    
    config {
      type: "table",
      columns: {
        column1: {
          description: "Some description",
          bigqueryPolicyTags: ["projects/example-project/locations/us/taxonomies/123456789/policyTags/123456789"]
        }
      }
    }
    
    SELECT "test" AS column1
    
    

## What's next

  * To learn more about BigQuery policy tags, see [Introduction to column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro).
  * To learn how to add BigQuery labels in Dataform, see [Add BigQuery labels](https://docs.cloud.google.com/dataform/docs/labels).
  * To learn how to add Dataform tags to create collections of tables, see [Add execution tags](https://docs.cloud.google.com/dataform/docs/configure-additional-actions#add-execution-tags).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
