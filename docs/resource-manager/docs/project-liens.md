---
url: https://docs.cloud.google.com/resource-manager/docs/project-liens/
title: Protect projects with liens \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:55:58.149379+00:00
---

# Protect projects with liens  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/project-liens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Protect projects with liens Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Google Cloud project liens to protect critical projects from being accidentally or maliciously deleted. A lien blocks anyone from deleting a project until an [Organization Administrator](https://docs.cloud.google.com/resource-manager/docs/access-control-org#permissions_and_roles) or [Project Owner](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#permissions_and_roles) removes the lien.

Google Cloud can also automatically apply liens to protect your resources. For example, if you [attach a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project) from one project to a resource in a different project, Google Cloud places a lien on the project that owns the Identity and Access Management (IAM) service account to prevent broken dependencies.

## Before you begin

The gcloud CLI is the easiest way to interact with project liens. If you don't have it installed, you can use [Google Cloud Shell](https://docs.cloud.google.com/shell/docs).

### Required roles

To get the permissions that you need to modify liens, ask your administrator to grant you the [Project lien modifier ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.lienModifier) (`roles/resourcemanager.lienModifier`) IAM role on projects. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to modify liens. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to modify liens:

  * `resourcemanager.projects.updateLiens`
  * List liens on a project: `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Place a lien on a project

To place a lien on a project, use the `alpha resource-manager liens create` command.
    
    
    gcloud alpha resource-manager liens create \
        --project=PROJECT_ID \
        --restrictions=resourcemanager.projects.delete \
        --reason=LIEN_REASON \
        --origin=LIEN_ORIGIN

Replace the following:

  * PROJECT_ID: ID of the project the lien applies to.
  * LIEN_REASON: human-readable description of why this lien exists. Put this description within double quotation marks. Example: `"This project is protected by a lien"`.
  * LIEN_ORIGIN: string denoting the user or system which originated the lien. It's a required field, but is automatically populated with the user's email address if omitted.



## List liens on a project

To list all liens applied to a project, use the `alpha resource-manager liens list` command.
    
    
    gcloud alpha resource-manager liens list
    

The output is similar to the following:
    
    
    NAME                                                  ORIGIN            REASON
    p1061081023732-l3d8032b3-ea2c-4683-ad48-5ca23ddd00e7  user@example.com  testing
    

## Remove liens from a project

To remove a lien from a project, use the `alpha resource-manager liens delete` command.
    
    
    gcloud alpha resource-manager liens delete LIEN_NAME

Replace LIEN_NAME with the name of the lien to be deleted, such as `p1061081023732-l3d8032b3-ea2c-4683-ad48-5ca23ddd00e7`.

## References

API Reference: [REST Resource: liens](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
