---
url: https://docs.cloud.google.com/compute/docs/samples/compute-add-iam-binding-for-oslogin/
title: Add OS login admin permissions for Compute Engine Service Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:39.014300+00:00
---

# Add OS login admin permissions for Compute Engine Service Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-add-iam-binding-for-oslogin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Add OS login admin permissions for Compute Engine Service Agent Stay organized with collections  Save and categorize content based on your preferences. 

Use this example to add OS Login admin role to the Compute Engine service account.

## Code sample

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_project" "project" {
    }
    resource "google_project_iam_member" "os_login_admin_users" {
      project = data.google_project.project.project_id
      role    = "roles/compute.osAdminLogin"
      member  = "serviceAccount:service-${data.google_project.project.number}@compute-system.iam.gserviceaccount.com"
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
