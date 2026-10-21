---
url: https://docs.cloud.google.com/workstations/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:03.720546+00:00
---

# Access control with IAM  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to manage access to workstations and workstation configurations. To grant access, assign one or more [Identity and Access Management roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to a principal (user, group, or [service account](https://docs.cloud.google.com/iam/docs/service-account-overview)). The policy defines which roles are assigned to which principals.

## Enable required Identity and Access Management roles

If the Identity and Access Management permissions you need haven't yet been set up, follow these instructions to set up one or more of the following roles:

  * Cloud Workstations User
  * Cloud Workstations Creator
  * Cloud Workstations Admin
  * Cloud Workstations Network Admin
  * Cloud Workstations Limit Exempted Creator
  * Cloud Workstations Policy Admin



### **Cloud Workstations User** : for developers using a workstation

To get the permissions that you need to access a workstation, ask your administrator to grant you the following IAM roles: 

  * [Cloud Workstations User ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`) on the workstation
  * [Cloud Workstations Operation Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.operationViewer) (`roles/workstations.operationViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### **Cloud Workstations Creator** : for developers creating and connecting to workstations

To get the permissions that you need to view workstation configurations, create workstations, and access workstations, ask your administrator to grant you the following IAM roles: 

  * [Cloud Workstations Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`) on the project or individual workstation configuration
  * [Cloud Workstations Operation Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.operationViewer) (`roles/workstations.operationViewer`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Cloud Workstations automatically grants the Cloud Workstations User role (`roles/workstations.user`) on any workstation that you create as Cloud Workstations Creator.

### **Cloud Workstations Admin** : for administrators creating and updating workstation configurations and workstation clusters

To get the permissions that you need to create the Cloud Workstations resources in your project, ask your administrator to grant you the [Cloud Workstations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about using the Google Cloud console to change permissions, see Add users and edit permissions using the Google Cloud console.

### **Cloud Workstations Network Admin** : for network administrators creating and updating Shared VPC permissions

To get the permissions that you need to create the Cloud Workstations resources in your Shared VPC, ask your administrator to grant you the [Cloud Workstations Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.networkAdmin) (`roles/workstations.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about using the Google Cloud console to change permissions, see Add users and edit permissions using the Google Cloud console.

### **Cloud Workstations Limit Exempted Creator** : for developers creating and connecting to workstations

To get the permissions that you need to view workstation configurations, create workstations exempted from `maxUsableWorkstations` limit, and access workstations, ask your administrator to grant you the following IAM roles on the project: 

  * Cloud Workstations Limit Exempted Creator (`roles/workstations.workstationLimitExemptedCreator`) - the project or individual workstation configuration 
  * Cloud Workstations Operation Viewer (`roles/workstations.operationViewer`) - the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### **Cloud Workstations Policy Admin** : for developers updating IAM policy of their workstations

To get the permissions that you need to update IAM policy of the workstation which allows granting access to the entire workstation or its individual ports, ask your administrator to grant you the [Cloud Workstations Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.policyAdmin) (`roles/workstations.policyAdmin`) IAM role on the workstation. 

Cloud Workstations automatically grants the Cloud Workstations Policy Admin role (`roles/workstations.policyAdmin`) on any workstation that you create as Cloud Workstations Creator, if the **Grant Policy Admin role to workstation creators** option is enabled on the Cloud Workstations configuration. For more information about this option, see the [Add users](https://docs.cloud.google.com/workstations/docs/create-configuration#add_users) section of the [Create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration) guide.

## Add users and edit permissions using the Google Cloud console

If you're an administrator for Cloud Workstations, you must have the Cloud Workstations Admin role (or basic Editor or Owner role) assigned to your account.

To add users or edit permissions, follow these steps:

  1. Navigate to the Cloud Workstations **Workstation configurations** page.
  2. To add new users, click **Add users** next to the name of the configuration, and enter new user information in the **New principals** field.
  3. To change existing permissions on a configuration, click the arrow_drop_downexpander arrow on the row with the configuration name, select **Edit permissions** , and then select **Add principal**. 

![Add users and edit permissions from the **Workstation configurations** page](https://docs.cloud.google.com/static/workstations/images/console-configurations-edit-permissions.png)Add users and edit permissions from the Cloud Workstations **Workstation configurations** page.




## What's next

  * [Limit workstations per developer](https://docs.cloud.google.com/workstations/docs/limit-workstations-per-developer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
