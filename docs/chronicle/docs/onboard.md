---
url: https://docs.cloud.google.com/chronicle/docs/onboard/
title: Deploy an instance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:37.757829+00:00
---

# Deploy an instance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy an instance

Supported in:

Google SecOps 

This document describes how to onboard (deploy) a Google SecOps (SIEM and SOAR) instance, and enable Google SecOps features based on your Google SecOps package tier and entitlements. These onboarding steps apply to the following [Google SecOps packages](https://cloud.google.com/security/products/security-operations): _Standard_ , _Enterprise_ , and _Enterprise Plus_.

Your designated _onboarding SME_ , also referred to as the _Google SecOps SME_ or the _billing administrator_ , performs the onboarding process. This person serves as your organization's main point of contact for Google SecOps.

## Prerequisites

Before you can onboard a new Google SecOps instance, make sure your organization has met these prerequisites:

  * An active registration for one of the following [Google SecOps packages](https://cloud.google.com/security/products/security-operations): _Standard_ , _Enterprise_ , or _Enterprise Plus_.

  * A signed Google SecOps contract from your organization. This contract gives you permission to provision each new Google SecOps instance.

  * If your organization uses [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), you must configure the relevant ingress and egress rules, which are documented in [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) for Google SecOps.




## Deploy a new Google SecOps instance

Perform these steps to deploy a new Google SecOps instance:

  1. Sign the Google SecOps contract.

Provisioning a new Google SecOps instance starts when your organization signs a Google SecOps contract. This action triggers Google's internal onboarding workflow and registers the contract details in Google's system, including your billing account and your onboarding SME's email address.

  2. Prepare your environment for onboarding.

Your onboarding SME should prepare your environment before you onboard a new Google SecOps instance.

  3. Onboard a new Google SecOps instance.

  4. Contact your account team or partner team to deploy additional instances.




## Prepare your environment for onboarding

The onboarding SME should prepare your environment before onboarding a Google SecOps instance, as described in these sections:

  1. Grant permissions to perform onboarding.
  2. Set up an Assured Workloads folder (optional).
  3. Configure a Google Cloud project.
  4. Configure an identity provider.



### Grant permissions to perform onboarding

For each new Google SecOps instance, grant the required onboarding roles and permissions to the onboarding SME, as described in Required roles and permissions.

### Set up an Assured Workloads folder (optional)

To create an Assured Workloads folder, do the following:

  1. Go to [Supported products by control package](https://docs.cloud.google.com/assured-workloads/docs/supported-products).
  2. In the list, select the _control package_ type you want to apply to the Assured Workloads folder.
  3. Make sure you have the required permissions listed in the **Required IAM roles** section.
  4. Follow the steps in the **Create an Assured Workloads folder for...** section.

**Note:** If you manage multiple organizations, select the correct **organization** where the Assured Workloads folder should be created. For **region** , select **US** , which corresponds to the **US multi-region**.



As you set up your folder, consider these guidelines:

  * A _compliance controlled_ tenant (instance) is one that must conform to one or more of the following compliance control standards: **FedRAMP** , **FedRAMP_MODERATE** , **PCI_DSS** , **FedRAMP_HIGH** , **IL4** , **IL5** , **CMEK_V1** , or **DRZ_ADVANCED**.

  * All files associated with a compliance-controlled tenant must reside in an Assured Workloads folder that is configured for the appropriate compliance control standard.

  * An Assured Workloads folder is created at the organization level. 

  * An organization can create multiple Assured Workloads folders, each dedicated to a specific compliance control package based on its requirements. For example, one folder may support **FedRAMP_MODERATE** instances, while another **FedRAMP_HIGH** instances.




Consider these guidelines when you deploy a compliance controlled tenant (instance):

  * You must link the compliance controlled tenant (instance) to a Google Cloud project that is located within an Assured Workloads folder.

  * If you plan to create a new Google Cloud project for your Google SecOps instance, you must create the project within an Assured Workloads folder that is configured for the required compliance control package.

  * If your organization doesn't have an Assured Workloads folder, you must create one.




Each new Google SecOps instance must be linked to a Google Cloud project. You can use an existing Google Cloud project or create a new one.

To create a new Google Cloud project:

  1. For a FedRAMP-compliant tenant (instance), create the project within your organization's Assured Workloads folder. If your organization doesn't have an Assured Workloads folder for the required control package, create one.

  2. Follow the steps in [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

**Note:** Use the `<CUSTOMER-name>-chronicle` naming convention and confirm that the project's billing account matches your Google SecOps instance's billing account. **Note:** To allocate charges to a different billing account, you must enter a new order.



### Configure a Google Cloud project

A Google Cloud project acts as the control layer for the linked Google SecOps instance.

To set it up properly, follow the steps in [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

### Configure an identity provider

Configure an identity provider to manage users, groups, and authentication for your Google SecOps instance.

There are two supported options:

  * Option 1: **Google Cloud Identity** : 

Use this option if you have a Google Workspace account, or you sync identities from your IdP to Google Cloud.

    1. Create managed user accounts to control access to Google Cloud resources and your Google SecOps instance.

    2. Define IAM policies using predefined or custom roles to grant feature access to users and groups.

For detailed instructions, see [Configure a Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).

**Note:** This option is not supported for **FedRAMP** , **IL4** , or **IL5** compliance customers.
  * Option 2: **Workforce Identity Federation** : 

Use this option if you use a third-party IdP (such as Okta or Azure AD).

Configure Google's [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and create a workforce identity pool. Google's Workforce Identity Federation lets you grant on-premises or multi-cloud workloads access to Google Cloud resources, without using service account keys.

For detailed instructions, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).




## Onboard a new Google SecOps instance

The Google system sends a Google SecOps onboarding invitation email to your onboarding SME. This email includes an activation link to initiate the setup process.

**Important:** The Google Cloud project that hosts your Google SecOps instance must be linked to the exact same billing account ID that was used to book your Google SecOps subscription order. If these accounts do not match, the system can't apply your subscription credits to your usage, resulting in incorrect charges. To allocate charges to a different billing account, you must enter a new order. 

After preparing your environment for onboarding, the onboarding SME should do the following:

  * Click the activation link in the invitation email.
  * Perform the steps in the following sections to deploy the Google SecOps instance:

    1. [Configure a new Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#new-instance) and link it to a Google Cloud project.
    2. [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).
    3. [Configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).
    4. [Map IdP groups to access control parameters](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform#map-parameters) to complete the deployment.



## Required roles and permissions

This section lists the roles and permissions required to deploy a Google SecOps instance. Grant these permissions to the onboarding SME performing the deployment tasks:

  * **All roles and permissions must be granted at the project level**. These permissions apply only to the specified Google Cloud project and the associated Google SecOps instance. To deploy additional instances, contact your account team or partner team.
  * If you deploy another Google SecOps instance under a different contract, you must grant a new set of roles and permissions for that deployment.



Grant the onboarding SME the roles and permissions listed in these following sections:

  1. Permissions in the Google billing account
  2. Predefined IAM roles
  3. Permissions to create an Assured Workloads folder
  4. Permissions to add a Google Cloud project
  5. Permissions to configure an identity provider
     1. Permissions to configure Cloud Identity or Google Workspace
     2. Permissions to configure a third-party identity provider
  6. Permissions to link a Google SecOps instance to Google Cloud services
  7. Permissions to configure feature access control using IAM
  8. Permissions to configure data access control
  9. Google SecOps advanced capabilities requirements



### Permissions in the Google billing account

Grant the onboarding SME the `billing.resourceAssociations.list` permission for the Google billing account specified in the contract. For detailed steps, see [Update user permissions for a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing#update-cloud-billing-permissions).

### Predefined IAM roles

Grant the onboarding SME the following predefined IAM roles:

  * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
  * [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin)
  * [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin)

**Note:** The IAM role should be granted even when deploying a non-SOAR instance.



### Permissions to create an Assured Workloads folder

**Note:** These permissions are needed to perform the steps in [Create a new Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder#select-program).

Grant the onboarding SME the [Assured Workloads Administrator (`roles/assuredworkloads.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/assuredworkloads#assuredworkloads.admin) role, which contains the minimum IAM permissions to create and manage Assured Workloads folders.

### Permissions to add a Google Cloud project

**Note:** These IAM permissions are needed to perform the steps in [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

Grant the onboarding SME the project creator permissions required to create a Google Cloud project and enable the Chronicle API:

  * If the onboarding SME has [project creator (`resourcemanager.projects.create`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectCreator) permissions at the organization level, no additional permissions are required.

  * If the onboarding SME doesn't have project creator permissions at the organization level, grant the following project-level IAM roles:

    * [Chronicle Service Admin (`roles/chroniclesm.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (if this role was not granted earlier)
    * [Editor (`roles/editor`)](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
    * [Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
    * [Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)



### Permissions to configure an identity provider

You can use an IdP to manage users, groups, and authentication.

Grant the following permissions to the onboarding SME for configuring an IdP:

#### Permissions to configure Cloud Identity or Google Workspace

**Note:** These permissions are needed to perform the steps in [Configure a Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).

  * **For Cloud Identity:**

If you're using Cloud Identity, grant the onboarding SME the roles and permissions described in [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions).

  * **For Google Workspace:**

If you're using Google Workspace, the onboarding SME must have a [Cloud Identity administrator account](https://support.google.com/a/answer/182076) and be able to sign in to the [Admin console](https://support.google.com/a/answer/6270675).




For more information about using Cloud Identity or Google Workspace as the identity provider, see [Configure Google Cloud identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).

#### Permissions to configure a third-party IdP

If you use a third-party IdP (such as Okta or Azure AD), configure [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) along with a workforce identity pool to enable secure authentication. 

**Note:** These permissions are needed to perform the steps in [Configure a third-party IdP](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

Grant the onboarding SME the following IAM roles and permissions:

  * [Editor (`roles/editor`)](https://docs.cloud.google.com/iam/docs/roles-overview#basic): _Project Editor_ permissions to the Google SecOps-bound project.

  * [IAM Workforce Pool Admin (`roles/iam.workforcePoolAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) permission at the organization level.

Use the following example to set the `roles/iam.workforcePoolAdmin` role:
        
        gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
          --member "user:USER_EMAIL" \
          --role roles/iam.workforcePoolAdmin
        

Replace the following:

    * `ORGANIZATION_ID`: numeric organization ID.
    * `USER_EMAIL`: administrator's email address.
  * [Organization Viewer (`resourcemanager.organizations.get`)](https://docs.cloud.google.com/resource-manager/docs/access-control-org#resourcemanager.organizationViewer) permission at the organization level.




### Permissions to link a Google SecOps instance to Google Cloud services

**Note:** These permissions are needed to perform the steps in [Link Google SecOps to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).

Grant the onboarding SME the same permissions as the Permissions to add a Google Cloud project.

If you plan to [migrate an existing Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#migrate-existing), you need permissions to access Google SecOps. For a list of predefined roles, see [Google SecOps predefined roles in IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#predefined-roles).

### Permissions to configure feature access control using IAM

**Note:** These permissions are needed to perform the steps in [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

  * Grant the [Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) role at the project level to the onboarding SME. This permission is required to assign and modify IAM role bindings for the project.

  * Assign IAM roles to users based on their responsibilities. For examples, see [Assign roles to users and groups](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#assign-roles).

If you plan to migrate an existing Google SecOps instance to IAM, grant the onboarding SME the same permissions as the Permissions to configure an identity provider.




### Permissions to configure data access control

**Note:** These permissions are needed to [configure data RBAC for users](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users).

Grant the onboarding SME the following IAM roles:

  * Chronicle API Admin (`roles/chronicle.admin`) and Role Viewer (`roles/iam.roleViewer`) roles, for configuring data RBAC for users.
  * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, for assigning the scopes to users.



If you don't have the required roles, [assign the roles in IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#assign-roles).

### Google SecOps advanced capabilities requirements

The following table lists Google SecOps advanced capabilities and their dependencies on a customer-provided Google Cloud project and Google workforce identity federation. 

Capability | Google Cloud foundation | Requires Google Cloud project? | Requires IAM integration?  
---|---|---|---  
Cloud Audit Logs: administrative activities | Cloud Audit Logs | Yes | Yes  
Cloud Audit Logs: data access | Cloud Audit Logs | Yes | Yes  
Cloud Billing: online subscription or pay-as-you-go | Cloud Billing | Yes | No  
Chronicle APIs: general access, mint and manage credentials using third-party IdP | Google Cloud APIs | Yes | Yes  
Chronicle APIs: general access, mint and manage credentials using Cloud Identity | Google Cloud APIs, Cloud Identity | Yes | Yes  
Compliant controls: CMEK | Cloud Key Management Service or Cloud External Key Manager | Yes | No  
Compliant controls: FedRAMP High or above | Assured Workloads | Yes | Yes  
Compliant controls: Organization Policy Service | Organization Policy Service | Yes | No  
Contact management: legal disclosures | Essential Contacts | Yes | No  
Health monitoring: ingestion pipeline outages | Cloud Monitoring | Yes | No  
Ingestion: webhook, Pub/Sub, Azure Event Hub, Amazon Kinesis Data Firehose | Identity and Access Management | Yes | No  
Role-based access controls: data | Identity and Access Management | Yes | Yes  
Role-based access controls: features or resources | Identity and Access Management | Yes | Yes  
Support access: case submission, tracking | Cloud Customer Care | Yes | No  
Unified SecOps authentication | Google workforce identity federation | No | Yes  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
