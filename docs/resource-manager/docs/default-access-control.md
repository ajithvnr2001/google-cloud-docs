---
url: https://docs.cloud.google.com/resource-manager/docs/default-access-control/
title: Managing default organization roles \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:39:35.908193+00:00
---

# Managing default organization roles  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/default-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)



Send feedback 

#  Managing default organization roles Stay organized with collections  Save and categorize content based on your preferences. 

When an organization resource is created, all users in your domain are granted the **Billing Account Creator** and **Project Creator** roles by default. These default roles allow your users to start using Google Cloud immediately, but are not intended for use in regular operation of your organization resource. 

This page describes how to designate a **Billing Account Creator** and **Project Creator** for regular operations, and how to remove roles that were assigned by default to the organization resource.

## Adding a Billing Account Creator and Project Creator

To migrate existing billing accounts into an organization resource, a user must have the Billing Account Creator IAM role. Users with the Project Creator role are able to create and manage Project resources. To add additional Billing Account Creators and Project Creators, follow these steps:

###  Console 

To grant the Billing Account Creator or Project Creator role using Google Cloud console:

  1. Go to the **Manage resources** page in the Google Cloud console: 

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. On the **Organization** drop-down list, select your organization resource.

  3. Select the check box for the organization resource. If you do not have a Folder resource, the organization resource will not be visible. To continue, see the instructions for granting roles through the [IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) page.

  4. On the right side **Info Panel** , under **Permissions** , enter the email address of the principal you want to add.

  5. In the **Select a role** drop-down, select **Billing > Billing Account Creator** or **Resource Manager > Project Creator**.

  6. Click **Add**. A dialog will appear to confirm the addition or update of the principal's new role.




## Removing default roles from the organization resource

After you designate your own Billing Account Creator and Project Creator roles, you can remove these roles from the organization resource to restrict those permissions to specifically designated users. To remove roles from the organization resource, follow these steps:

###  Console 

To remove the roles assigned to users by default using the Google Cloud console:

  1. Go to the **Manage resources** page in the Google Cloud console: 

[Open the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. Click the **Organization** drop-down list at the top of the page and then select your organization resource.

  3. Select the check box for the organization resource for which you want to change permissions. If you do not have a Folder resource, the organization resource will not be visible. To continue, see the instructions for revoking roles through the [IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) page.

  4. On the right side **Info Panel** , under **Permissions** , click to expand the role from which you want to remove users.

  5. Under the expanded role list, next to the principal you want to remove from the role, click remove. ![Screenshot of UI](https://docs.cloud.google.com/resource-manager/img/role.png)

  6. On the **Remove principal?** dialog that appears, click **Remove** to confirm removing the role from the specified principal.

  7. Repeat the above two steps for each role you want to remove.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
