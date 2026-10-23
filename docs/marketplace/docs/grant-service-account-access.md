---
url: https://docs.cloud.google.com/marketplace/docs/grant-service-account-access/
title: Granting service accounts access to your projects \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:49.329174+00:00
---

# Granting service accounts access to your projects  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/grant-service-account-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Granting service accounts access to your projects Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Some service providers use a service account to provide additional functionality to their software. They can provide access to a page that explains the Identity and Access Management (IAM) roles the service account requires and that you use to grant the roles to the service accounts. You can revoke the access at any time.

If you cancel your purchase, you must manually revoke the access and remove any resources created for the service account.

## Before you begin

  * You must have the Owner (`roles/owner`) role, _OR_

You must have the `resourcemanager.projects.getIamPolicy` _AND_ `resourcemanager.projects.setIamPolicy` permissions.

  * Verify with your Organization Admin that you can grant IAM roles to service accounts across projects or organizations. For more information around restrictions that might be applied to your organization, see [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) or [Disable attachment of service accounts to resources in other projects](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts).




## Granting access to a service account

This grants the roles listed on the page to service account for all the projects listed on the page.

  1. Open the link provided by your service provider. It's usually on the app's management console.

  2. Review the roles your provider wants the service account to have.

  3. To choose a project, click **Select Project**. If the app is included in multiple projects that you have access to, you can select all those projects. If a project is greyed out, you don't have sufficient privileges to grant the service account access to it.

  4. If you don't want to grant the service account access, click **Remove** to delete it from the list.

  5. Click **Grant**.




The listed roles are granted to service account for all the projects listed on the **Project with granted access** section.

## Remove access to your app

You can revoke a service account's access to the app at any time.

  1. Open the link provided by your service providers. It's usually on the app's management console.

  2. Click **Select Project** , and then select the project you don't want the service account to access anymore. If a project is greyed out, you don't have sufficient privileges to grant the service account access to it.

  3. In the **Project with granted access** list, click **Remove Access** next to the service account that you no longer want to be able to access your project.




You can grant access to the service account after the access has been revoked.

If you are permanently removing access to your app, view your service provider's documentation to ensure you remove any resources created for the service account.

### Remove access to your app manually

If you want to revoke a service account's access manually, or have cancelled your purchase, use the **IAM** page in the console.

View the IAM documentation on [Granting, changing, and revoking access for users](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) for more information.

If you are permanently removing access to your app, view your service provider's documentation to ensure you remove any resources created for the service account.

## Verifying service account roles

To verify the access granted or removed from a service account, open the IAM page in the console and find the service account. Ensure that the listed roles match the roles granted to the service account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
