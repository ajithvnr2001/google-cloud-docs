---
url: https://docs.cloud.google.com/compute/docs/images/premium/access-rhel-knowledgebase/
title: Access Red Hat Knowledgebase \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:51.930188+00:00
---

# Access Red Hat Knowledgebase  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/access-rhel-knowledgebase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Access Red Hat Knowledgebase Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

The Red Hat Knowledgebase provides you with access to articles, solutions, product documentation, and community discussions.

The Red Hat Knowledgebase is normally available only if you have a subscription purchased directly from Red Hat. However, Google Cloud has partnered with Red Hat to provide access to the Red Hat Knowledgebase for all Red Hat Enterprise Linux (RHEL) users on Google Cloud. This is available as a single-sign-on (SSO) option through the Google Cloud console.

This SSO option to the Red Hat Knowledgebase is available whether your virtual machine (VM) instances use pay-as-you-go (PAYG) or bring-your-own-subscription (BYOS) RHEL OS images.

When you access the Red Hat Knowledgebase by using the Google Cloud console, you are granted access to the portal without the need for authentication for 24 hours. After 24 hours, the token expires and you need to authenticate again using the SSO from the Google Cloud console.

## Requirements

To access the Red Hat Knowledgebase you must have a VM instance that uses a [RHEL OS image](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel). The VM instance must also meet the following requirements:

  * The VM must have an attached BYOS or PAYG RHEL license. For more information, see [View the licenses associated with a VM](https://docs.cloud.google.com/compute/docs/licenses/view-append#view_the_licenses_associated_with_a_vm).
  * The VM must be in the `RUNNING` state. To view the state of a VM, [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).



### Required roles

To get the permissions that you need to view the Red Hat Knowledgebase, ask your administrator to grant you the [Compute Viewer role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view the Red Hat Knowledgebase. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the Red Hat Knowledgebase:

  * `compute.projects.get`
  * `compute.instances.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access Red Hat Knowledgebase

You can use the Google Cloud console to access the Red Hat Knowledgebase.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click any RHEL VM that you have running. The VM must be in a `RUNNING` state to access the Red Hat Knowledgebase link.

  3. Click **Red Hat Knowledgebase**.

![Red Hat Knowledgebase](https://docs.cloud.google.com/static/compute/images/os/rhel-knowledgebase-sso.png)

When you are redirected to the Red Hat Knowledgebase, the page might still show a **Login** button. However, you can view articles in the Knowledgebase. To verify your access, search for and open an article.




## What's next

  * Learn more about the [RHEL operating system images](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel) on Compute Engine.
  * Review the [RHEL FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
