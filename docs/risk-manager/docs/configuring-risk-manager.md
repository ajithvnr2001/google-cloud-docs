---
url: https://docs.cloud.google.com/risk-manager/docs/configuring-risk-manager/
title: Configuring Cyber Insurance Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:23.830903+00:00
---

# Configuring Cyber Insurance Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/risk-manager/docs/configuring-risk-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cyber Insurance Hub ](https://docs.cloud.google.com/risk-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/risk-manager/docs/quickstarts)



Send feedback 

#  Configuring Cyber Insurance Hub Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure your Google Cloud organization to use Cyber Insurance Hub for the first time. These steps are prerequisites for most tasks in Cyber Insurance Hub.

### Required setup permissions

To get the permissions that you need to configure Cyber Insurance Hub, ask your administrator to grant you the following IAM roles on your organization: 

  * [Risk Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.admin) (`roles/riskmanager.admin`)
  * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure Cyber Insurance Hub. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure Cyber Insurance Hub:

  * `riskmanager.serviceAccount.create`
  * `resourcemanager.organizations.getIamPolicy`
  * `resourcemanager.organizations.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant the Risk Manager Service Agent access to your organization

When you begin to set up Cyber Insurance Hub in the Google Cloud console, a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) is created. Upon creation, this service agent has no permissions and cannot perform any actions.

To read security findings and build reports, the Risk Manager Service Agent must be granted the [Risk Manager Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.serviceAgent) (`roles/riskmanager.serviceAgent`).

To grant the role to the service agent, follow these steps:

  1. Go to the Cyber Insurance Hub setup page:

[Cyber Insurance Hub setup](https://console.cloud.google.com/projectselector2/security/riskmanager/setup/steps?supportedpurview=organizationId)

  2. Select your organization.

  3. Click **Grant Roles**.

  4. Verify that **Grant Roles** is updated to **Roles Granted**.




### Enroll in Cyber Insurance Hub

Enrolling in Cyber Insurance Hub enables any backend services that are needed for Cyber Insurance Hub to work.

For enrollment to succeed, the organization must have Security Command Center enabled, with the Security Health Analytics service enabled within Security Command Center. The Security Command Center and Security Health Analytics enablement process is detailed in [the Cyber Insurance Hub onboarding page](https://docs.cloud.google.com/risk-manager/docs/onboard).

To enroll in Cyber Insurance Hub, follow these steps:

  1. Go to the Cyber Insurance Hub setup page:

[Cyber Insurance Hub setup](https://console.cloud.google.com/projectselector2/security/riskmanager/setup/steps?supportedpurview=organizationId)

  2. Select your organization.

  3. Click **Enroll**.

  4. Verify that **Enroll** is updated to **Enrolled**.




After you enroll in Cyber Insurance Hub, Cyber Insurance Hub enables regular scans of your organization's Google Cloud resources to generate the data contained in Cyber Insurance Hub reports. Initial scans can take up to 24 hours to complete.

### Grant access to Cyber Insurance Hub

Before a user can create, review, share, or send a report, that user must have the appropriate IAM permissions. You can grant one or more predefined roles or create and grant custom roles. For more information, including a list of predefined roles for Cyber Insurance Hub, see [Access control with IAM](https://docs.cloud.google.com/risk-manager/docs/access-control).

**Note:** Always grant the minimum set of permissions required to perform a given task.

To grant a role, follow these steps:

### Console

**Note:** If the Cyber Insurance Hub roles aren't visible in the Google Cloud console, you need to use the Google Cloud CLI.

  1. In the Google Cloud console, go to the [IAM](https://console.cloud.google.com/iam-admin/iam) page.

[Go to IAM](https://console.cloud.google.com/projectselector2/iam-admin/iam?supportedpurview=organizationId)

  2. Select the organization that you enrolled in Cyber Insurance Hub.

  3. On the **IAM** page, find the username of the user to whom you want to grant a role and then click edit **Edit principal**.

  4. On the **Edit permissions** pane that appears, add the necessary roles.

     1. Click **Add another role**. Select a role to add, such as **Risk Manager Report Reviewer**.

     2. To add more roles, repeat the previous step. Click **Save**.




### gcloud

  1. [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

**Note:** The Google Cloud CLI is available automatically in [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-the-cloud-shell-terminal). If you are using the Cloud Shell, you don't need to install the gcloud CLI manually in order to use it.
  2. Run the following command:
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
           --member=user:USERNAME --role=roles/ROLE
         

Replace the following:

     * `ORGANIZATION_ID`: the numeric ID of your organization for which you enrolled Cyber Insurance Hub.

     * `USERNAME`: the principal that you want to grant this role to. This must be a member of your organization; for example, `test-user@example.com`.

     * `ROLE`: the name of the [Cyber Insurance Hub role](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager) that you want to grant; for example, `riskmanager.reviewer`.




## What's next?

  * Learn how to [create a report](https://docs.cloud.google.com/risk-manager/docs/managing-reports#create).
  * Learn how to [remediate findings](https://docs.cloud.google.com/risk-manager/docs/remediate-findings).
  * Learn how to [automatically generate reports](https://docs.cloud.google.com/risk-manager/docs/automated-reports).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
