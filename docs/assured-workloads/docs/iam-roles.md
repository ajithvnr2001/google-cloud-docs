---
url: https://docs.cloud.google.com/assured-workloads/docs/iam-roles/
title: IAM roles \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:27.066893+00:00
---

# IAM roles  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/iam-roles/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IAM roles

This page describes the Identity and Access Management (IAM) roles you can use to configure Assured Workloads. Roles limit a principal's ability to access resources. Only grant a principal the permissions it needs in order to interact with applicable Google Cloud APIs, features, or resources.

To be able to create an Assured Workloads folder, you must be assigned one of the roles listed below with that ability, as well as a Cloud Billing access control role. You must also have an active, valid billing account. For more information, see [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

## Required roles

Following are the minimum required Assured Workloads-related roles. To learn how to grant, change, or revoke access to resources using IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * **Assured Workloads Administrator (`roles/assuredworkloads.admin`):** For creating and deleting Assured Workloads folders.
  * **Resource Manager Organization Viewer (`roles/resourcemanager.organizationViewer`):** Access to view all resources belonging to an organization.

**Note:** To be able to assign roles, you must have the `resourcemanager.organizations.setIamPolicy` permission. This permission is included in the Organization Administrator role (`resourcemanager.organizationAdmin`). To learn more, see [Using predefined roles](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles).

## Assured Workloads roles

Following are the IAM roles that are associated with Assured Workloads, and how to grant these roles using the Google Cloud CLI. To learn how to grant these roles in the Google Cloud console or programmatically, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

Replace the ORGANIZATION_ID placeholder with the actual organization identifier and `example@customer.org` with the user email address. To retrieve your organization ID, see [Retrieving your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

### `roles/assuredworkloads.admin`

For creating and deleting Assured Workloads folders. Allows read-write access.
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member="user:example@customer.org" \
      --role="roles/assuredworkloads.admin"

### `roles/assuredworkloads.editor`

Allows read-write access.
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member="user:example@customer.org" \
      --role="roles/assuredworkloads.editor"

### `roles/assuredworkloads.reader`

For getting and listing Assured Workloads folders. Allows read-only access.
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
      --member="user:example@customer.org" \
      --role="roles/assuredworkloads.reader"

## Custom roles

If you want to define your own roles to contain bundles of permissions that you specify, use [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Assured Workloads IAM best practices

Properly securing IAM roles to follow [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely) is a Google Cloud security best practice. This principle follows the rule that users should only have access to the products, services, and applications required by their role. Users are not currently restricted from using out-of-scope services with Assured Workloads projects when deploying products and services outside of an Assured Workloads folder.

The [list of in-scope products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products) helps to guide security admins when creating [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that limit user access to only in-scope products within the Assured Workloads folder. Custom roles are able to help support obtaining and maintaining compliance within an Assured Workloads folder.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
