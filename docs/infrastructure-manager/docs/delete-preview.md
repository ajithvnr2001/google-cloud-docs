---
url: https://docs.cloud.google.com/infrastructure-manager/docs/delete-preview/
title: Delete previews \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:58.769264+00:00
---

# Delete previews  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/delete-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Delete previews Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete existing previews. When you delete a preview, you delete the [preview's metadata](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#preview_metadata).

Previews are automatically deleted if they target a deployment and that deployment is updated or deleted.

If you have not created a preview, see [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).

If you want to delete a deployment, see [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).

## Before you begin

Ensure that you have the IAM permissions needed to delete previews: `roles/config.admin`.

## Delete a preview

To delete a preview:
    
    
    gcloud infra-manager previews delete projects/PROJECT_ID/locations/LOCATION/previews/PREVIEW_ID
    

Replace:

  * PROJECT_ID is the project ID where Infrastructure Manager runs.
  * LOCATION is the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of valid locations.
  * PREVIEW_ID is the preview identifier of the preview.



## What's next

  * [Create a new preview](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment).
  * [View and list previews](https://docs.cloud.google.com/infrastructure-manager/docs/list-preview).
  * Use Infra Manager to [deploy resources](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * Learn more about [Terraform with Infra Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
