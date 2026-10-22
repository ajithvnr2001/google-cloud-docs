---
url: https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication/
title: Configure Google Cloud identity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:37.245442+00:00
---

# Configure Google Cloud identity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Google Cloud identity

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

You can use Cloud Identity, Google Workspace, or a third-party identity provider (such as Okta or Azure AD) to manage users, groups, and authentication.

This page describes how to use Cloud Identity or Google Workspace.

When using Cloud Identity or Google Workspace, you create managed user accounts to control access to Google Cloud resources and to Google SecOps.

You create IAM policies that define which users and groups have access to Google SecOps features. These IAM policies are defined using predefined roles and permissions provided by Google SecOps or custom roles that you create.

As part of linking a Google SecOps instance to Google Cloud services, configure a connection to a Google Cloud IdP. The Google SecOps instance integrates directly with Cloud Identity or Google Workspace to authenticate users and enforce access control based on your configured IAM policies.

See [Identities for users](https://docs.cloud.google.com/iam/docs/user-identities#google-accounts) for detailed information about creating Cloud Identity or Google Workspace accounts.

## Common use cases

Google SecOps requires using Cloud Identity or Google Workspace as the SSO broker for a varied set of use cases.

### Comply with strict security standards

  * **Objective** : Meet strict regulatory standards for system and cloud access.
  * **Value** : Helps conform to FedRAMP High (or higher) compliance requirements by securely brokering SSO.



### Manage enterprise access control

  * **Objective** : Control feature and data access centrally across the organization.
  * **Value** : Enables enterprise-level RBAC in Google SecOps by using IAM.



### Automate API programmatic access

  * **Objective** : Provide self-service methods to securely interact with the Chronicle APIs.
  * **Value** : Reduces manual administrative overhead by letting customers manage their credentials programmatically.



## Grant a role to enable sign-in to Google SecOps

The following steps describe how to grant a specific role using IAM so that a user can sign in to Google SecOps. Perform the configuration using the Google SecOps-bound Google Cloud project you created earlier.

  1. Grant the [Chronicle API Viewer (`roles/chronicle.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer) role to users or groups that should have access to the Google Security Operations application.

**Note:** The following examples use the `gcloud` command. To use the Google Cloud console, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).**Important:** The following examples don't configure authorization to Google SecOps features. This is done using IAM for feature access control.
     * The following example grants the Chronicle API Viewer role to to a specific group:
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/chronicle.viewer \
             --member "group:GROUP_EMAIL"
           

Replace the following:

       * `PROJECT_ID`: with the project ID of the Google Security Operations-bound project you configured in [Configure a Google Cloud project for Google Security Operations](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project). See [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for a description of fields that identify a project.
       * `GROUP_EMAIL`: the email alias for the group, such as `analyst-t1@example.com`.
     * To grant the Chronicle API Viewer role to a specific user, run the following command:
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/chronicle.viewer \
             --member "user:USER_EMAIL"
           

Replace `USER_EMAIL`: the user's user email address, such as `alice@example.com`.

     * For examples of how to grant roles to other members, such as a group or domain, see [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) and [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) reference documentation.

  2. Configure additional IAM policies to meet your organization's access and security requirements.


**Note:** Custom IAM role mappings aren't supported for the SOAR side of the Google SecOps platform.

## What's next

After completing the steps in this document, perform the following:

  * Perform steps to [Link a Google Security Operations instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

  * If you have not yet set up audit logging, continue with [enabling Google Security Operations audit logging](https://docs.cloud.google.com/chronicle/docs/preview/audit-logging/audit-logging).

  * If you are configuring for Google Security Operations, perform additional steps in [Provision, authenticate, and map users in Google Security Operations](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).

  * To configure access to features, perform additional steps in [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access) and [Google Security Operations permissions in IAM](https://docs.cloud.google.com/chronicle/docs/reference/feature-rbac-permissions-roles).




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
