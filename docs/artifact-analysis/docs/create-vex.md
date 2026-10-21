---
url: https://docs.cloud.google.com/artifact-analysis/docs/create-vex/
title: Create VEX statements \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:43.110029+00:00
---

# Create VEX statements  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/create-vex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Create VEX statements Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create [Vulnerability Exploitability eXchange (VEX)](https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf) statements.

For every container image pushed to Artifact Registry, Artifact Analysis can store an associated VEX statement. VEX is a type of security advisory that indicates whether a product is affected by a known vulnerability.

Each statement provides:

  * The publisher of the VEX Statement
  * The artifact for which the statement is written
  * The vulnerability assessment (VEX status) for any known vulnerabilities



Software publishers can create VEX statements to describe the security posture of an application. VEX statements note any vulnerabilities discovered in specific artifacts and provide context about their impact to their customers or regulatory bodies.

Security and policy enforcers can use VEX status to triage risks in their software supply chains and use VEX statements to attest to the composition of their artifacts to help organizations meet regulatory requirements.

## VEX status

The VEX status indicates whether an artifact is affected by a known vulnerability.

The status can be one of:

  * **Not affected** : No remediation is required regarding this vulnerability.
  * **Affected** : Remediation actions are recommended.
  * **Fixed** : In this version of the product, a fix has been applied to address the vulnerability.
  * **Under Investigation** : The status of this product is yet to be determined. The publisher will provide an updated status in a later release.



## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Container Analysis, Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://containeranalysis.googleapis.com,https://artifactregistry.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
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

  10. Enable the Container Analysis, Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://containeranalysis.googleapis.com,https://artifactregistry.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Have container images stored in an Artifact Registry repository, or [create a repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) and [push your images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).



## Required roles

To get the permissions that you need to upload VEX assessments and check the VEX status of vulnerabilities, ask your administrator to grant you the following IAM roles on the project: 

  * To create and update notes: [Container Analysis Notes Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.editor) (`roles/containeranalysis.notes.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create VEX statements

Artifact Analysis supports the [Common Security Advisory Format (CSAF)](https://oasis-open.github.io/csaf-documentation/) 2.0 standard in JSON. To produce a new VEX statement, use the [CSAF schema](https://github.com/oasis-tcs/csaf/blob/master/csaf_2.0/json_schema/csaf_json_schema.json).

The following is an example of a VEX statement for an image in Artifact Registry with one `cve` branch for a known vulnerability.

You must define the value of the `product_status` for each CVE.
    
    
    {
      "document": {
        "csaf_version": "2.0",
        "lang": "en-US",
        "publisher": {
          "name": "Sample-Company",
          "namespace": "https://sample-company.com"
        },
        "title": "Vex document 1.1"
      },
      "product_tree": {
        "branches": [
          {
            "name": "https://LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME",
            "product": {
              "name": "PRODUCT_NAME",
              "product_id": "IMAGE_NAME"
            }
          }
        ]
      },
      "vulnerabilities": [
        {
          "cve": "CVE_ID",
          "product_status": {
            "PRODUCT_STATUS": [
              "IMAGE_NAME"
            ]
          }
        }
      ]
    }
    

Where

  * PRODUCT_NAME Human-readable product name for the image. Takes a string value. The value should be the product's full canonical name, including version number and other attributes.
  * LOCATION is the region or multi-regional location of your repository.
  * PROJECT_ID is the ID for the project that contains your repository.
  * REPO_NAME is the name of your Docker repository in Artifact Registry.
  * IMAGE_NAME is the name of the image.
  * CVE_ID is the identifier for the vulnerability, such as `CVE-2017-11164`.
  * PRODUCT_STATUS is the assessment of the security risk. Artifact Analysis supports four status types: `known_affected`, `known_not_affected`, `under_investigation`, and `fixed`.



For each vulnerability that you want to list in your VEX statement, you must create a `cve` branch and define the value of the `product_status`.

The value of the `name` field in `product_tree.branches.name` is the image URI. Including this value associates the VEX statement to a specific Docker image.

## What's next

  * [Upload VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/upload-vex) your existing VEX statements or VEX statements provided by other publishers.
  * Prioritize vulnerability issues using VEX. Learn how to [view VEX statements](https://docs.cloud.google.com/artifact-analysis/docs/view-vex) and filter vulnerabilities by VEX status.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
