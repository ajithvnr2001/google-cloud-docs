---
url: https://docs.cloud.google.com/resource-manager/docs/delete-org/
title: Delete an organization \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:05.979059+00:00
---

# Delete an organization  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/delete-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Delete an organization Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to delete an organization and describes the consequences of this action.

The organization is bound to your Google Workspace (formerly G Suite) account.

If you prefer not to use the organization, consider restoring the organization's Identity and Access Management (IAM) allow policy to its original state by completing the following steps:

  1. Add your domain to the `Project Creator` and `Billing Account Creator` roles.
  2. Remove all other entries in the organization's allow policy.



This lets your users continue to create projects and billing accounts while letting the Google Workspace Super Admin recover central administration if needed.

## Before you delete an organization

Before you can delete your organization, you must delete all resources within the organization, as well as any organization-level resources. If you don't remove these resources, the deletion process will be blocked.

Ensure you have completed the following cleanup steps:

  1. **Delete all projects:** You must shut down all projects in the organization. For instructions, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).
  2. **Delete all folders:** You must delete all folders in the organization. For instructions, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#deleting_a_folder).
  3. **Delete organization-level resources:** You must delete any resources defined at the organization level that could block deletion. These include: 
     * **Organization-level firewall policies:** Delete any firewall policies associated with the organization.
     * **Access Context Manager policies:** Delete any Access Policies.
     * **Tags:** Delete all tag keys and values associated with the organization.



### Find blocking resources

You can use the Google Cloud CLI and Cloud Asset Inventory to search for resources that might block organization deletion.

To search for organization-level firewall policies and Access Context Manager policies, run the following command:
    
    
    gcloud asset search-all-resources \
        --scope='organizations/ORGANIZATION_ID' \
        --asset-types='identity.accesscontextmanager.googleapis.com/AccessPolicy,compute.googleapis.com/FirewallPolicy' \
        --order-by='createTime'
    

Replace `ORGANIZATION_ID` with your unique organization resource ID. See [gcloud asset search-all-resources](https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-resources) for more information.

## How to delete an organization

To delete your organization and _all the resources associated with it_ , [delete your Google Workspace account](https://support.google.com/). For [Cloud Identity](https://support.google.com/cloudidentity/answer/7384508) users, cancel all other Google services, and then delete your user account. This action is potentially very damaging and might be impossible to reverse completely, so you should only take this action if you are certain no resources are in active use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
