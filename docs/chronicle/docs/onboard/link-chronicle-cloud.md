---
url: https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud/
title: Link an instance to Google Cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:23.167257+00:00
---

# Link an instance to Google Cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Link an instance to Google Cloud

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to link a Google SecOps instance to a new subscription.

## Subscription activation scenarios

This document applies to the following subscription activation scenarios:

**For new customers:**

  * To provision a new Google SecOps instance for the first time.
  * To retain your POC data from your recently completed proof of concept (POC).



**For existing customers:**

  * To activate subscription renewals and contractual amendments for existing Google SecOps instances.

**Note:** If you have questions or need help with provisioning, contact your Google account team, customer engineer (CE), or partner engineer (PE). If they're not available, reach out to [Google SecOps Support](https://console.cloud.google.com/support)).

### Subscription linking scenarios not covered in this document

The following instance-linking scenarios require different actions that this document doesn't describe:

  * **Link a Managed Security Service Provider (MSSP) instance** : 

To link a Google SecOps instance for a Managed Security Service Provider (MSSP), contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)), to assist with the setup.

  * **Compliance-controlled tenants (instances)** :

    * A compliance-controlled tenant (instance) conforms to one of the following compliance control standards: **FedRAMP** , **FedRAMP_MODERATE** , **HIPAA** , **PCI_DSS** , **FedRAMP_HIGH** , **IL4** , **IL5** , **CMEK_V1** , or **DRZ_ADVANCED**.

    * For a _compliance-controlled_ tenant (instance), contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)). They provide a separate invitation that follows a different workflow for compliance-controlled tenants.

In the compliance-controlled workflow, note the following:

      * You must locate a compliance-controlled tenant (instance) in a project within an Assured Workloads folder. See [Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication) for details.

      * When selecting a Google Cloud project to hold a compliance-controlled tenant:

        1. Select an Assured Workloads folder to open it. 
        2. Inside the Assured Workloads folder, click the name of a Google Cloud project.
        3. Complete the configuration as described in [Configure the IdP](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication#configure-idp).
  * **Migrate a non-POC Google SecOps instance from a Google Cloud project to a Bring Your Own Project (BYOP) Google Cloud project**

You can migrate your Google SecOps instance (and its data) from a Google Cloud project to a Bring Your Own Project (BYOP) Google Cloud project. For details, see [Migrate a non-POC project to a BYOP](https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another#migrate_a_non-poc_project_to_a_byop).

  * **Migrate an existing legacy Google SecOps instance** :

You can migrate an existing legacy Google SecOps instance to Google Cloud if it meets **any** of the following conditions:

    * Is not deployed in your Google Cloud project.
    * Does not use Google Cloud Authentication (Workforce Identity Federation / Cloud Identity).
    * Does not use Google Cloud Identity and Access Management (IAM) for Role-Based Access Control (RBAC).

To migrate such an existing Google SecOps instance, follow the steps in the [Migrate legacy SIEM Infra to Google Cloud](https://docs.cloud.google.com/chronicle/docs/administration/migrate-legacy-siem-infra) guide.




## Before you begin

Before you can use a Google SecOps instance with Google Cloud services, you must do the following:

  * **Verify permissions**. Ensure you have the necessary permissions to complete the steps in this document. For information about required permissions for each phase of the onboarding process, see [Required roles and permissions](https://docs.cloud.google.com/chronicle/docs/onboard#required-roles).



Before you can _create a new_ Google SecOps instance with Google Cloud services, you must do the following:

  * **Choose a Google Cloud project** : You can either create a new Google Cloud project for your Google SecOps instance or link it to an existing Google Cloud project. 

To create a new Google Cloud project and enable the Chronicle API, follow the steps in [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

**Note:** The Google Cloud project's billing account must always match the subscription's billing account.
  * **Plan your identity provider (IdP) set up for Google SecOps instance** :

Your Google SecOps instance uses single sign-on (SSO) and identity providers (IdP) for user authentication and to enforce secure access controls. Configure one of the following to manage users, groups, and authentication for your Google SecOps instance: Cloud Identity, Google Workspace, or a third-party identity provider (such as Okta or Azure AD):

    * To use a third-party IdP, see [Configure a third-party identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

    * To use Cloud Identity or Google Workspace, see [Configure a Google Cloud identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).

  * **Configure rules for VPC Service Controls** :

If your organization uses [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), you must configure the relevant ingress and egress rules, which are documented in [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) for Google SecOps.




## Link a Google SecOps instance to a new subscription

After your organization signs the new Google SecOps subscription contract, Google sends a subscription activation email to your organization's onboarding SME (your technical point of contact) on the subscription start date. This email contains subscription activation instructions and a one-time activation link, which is valid for 60 days.

To link your Google SecOps instance to a new subscription, complete the following steps:

  1. Activate the subscription
  2. Select the Google Cloud project
  3. Add essential contacts
  4. Verify the deployment details
  5. Start the instance setup



### Activate the subscription

Complete the Google SecOps subscription activation:

  1. Read the activation instructions in the activation email.
  2. Click the **Activate Your Subscription** link to open the **Google Security Operations activation** page. 

  3. The activation page displays your subscription **Entitlements**.

Read and check your subscription entitlement details and billing account ID.

     * If all the details are correct, select the **I have ... agreed to proceed with activation** checkbox. Make a note of the billing account ID for use in the upcoming steps.
     * To update any entitlement details, contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)).
  4. In the **Create or start with an existing SecOps instance** section, link your new subscription to an existing instance or create a new instance based on your activation requirements:

     * **To create a new Google SecOps instance for a new subscription:**

Select **Create New Instance** to open the **Link SecOps to a project** page.

     * **To link an existing POC Google SecOps instance to a new subscription:**

       1. Select **Existing Instance**.

       2. Enter your POC Google SecOps instance ID and click **Validate**.

**Note:** After you successfully activate the subscription, contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)), to migrate all the POC data.
     * **To renew an existing Google SecOps subscription or apply a subscription amendment:**

       1. Select **Existing Instance**.

The system displays a list of existing Google SecOps instances that are linked to the billing account. After activation, the system applies the new subscription entitlements to all of these linked instances.

       2. Check that the list of instances is correct.

If any instances are missing from the list, do one of the following:

          * Check that the billing accounts of the Google Cloud projects hosting the missing instances match the billing account of the new subscription. If they don't match, update the billing accounts of the Google Cloud projects to match the billing account of the new subscription.
          * Contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)).
       3. (Optional) If you want to create an additional new Google SecOps instance at the same time as activating the subscription, select the **I want to create a new instance...** checkbox.

       4. Click **Activate Subscription**.

The system applies the new subscription entitlements to all the instances linked to this billing account.




### Select the project to link your instance to

  1. On the **Link SecOps to a project** page, click **Select a project** to open the **Select a resource** page.

  2. On the **Select a resource** page, select your **Organization** from the list.

  3. Optional: We recommend that you create a new dedicated Google Cloud project for each Google SecOps instance.

Click **New Project** to create a new Google Cloud project for your instance, and follow the steps in [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).

  4. Select a Google Cloud project from the **Projects and folders** list as follows:

     * **Project selection criteria:**

       * You _cannot_ select a project or folder that has a  warning  **Warning** icon next to it. To see the reason, hold the pointer over the icon—for example, missing permissions or billing account mismatch.

         * The project must use the same billing account as the Google SecOps instance.

**Note:** Ensure the Google Cloud project's billing account matches both the subscription's billing account and the Google SecOps instance billing account.
         * You can link the Google Cloud project to only one Google SecOps instance.

         * You must have the required IAM permissions to access and work with the project, see [Permissions to add a Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard#roles-add-project).

     * **Select a Google Cloud project** :

       * Click the name of the Google Cloud project.

       * After selecting a project, if you want to select a different project, do the following: On the **Link SecOps to a project** page, click the project to open the **Select a resource** page, and select a different project.




### Add essential contacts

Add contacts to receive critical notifications about technical, security, legal, and billing issues.

After you select a project, the **Essential contacts** table appears. This table shows notification **Categories** and the **Email** addresses you assigned as contacts. You must assign a contact to at least these four mandatory categories: **technical** , **security** , **legal** , and **billing**.

Assign a contact to a notification category as follows:

  1. To open the **Edit contact** window, click **Add contact** or click  edit  **Edit** in a notification category that has an existing contact.

  2. Enter the contact person's **Email** address, and select one or more notification **Categories**.

  3. Click **Save**.

Repeat the steps for the next notification category.

  4. After assigning the contacts, click **Next** to link your Google SecOps instance to the selected project, and open the **Deployment** page.




### Verify the deployment details

The **Deployment** page shows the final details for you to review before you deploy.

Validate the details in each prefilled section:

  1. **Deployment details**

This section displays instance details your contract sets, for example company, region, package tier, and data retention duration.

     * To view instance information, go to https://console.cloud.google.com/security/chronicle/settings.

     * To update any information, contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)).

Click **Next** to move to the next section.

  2. **Review service account**

Review the details of the service account the system creates. Click **Next** to move to the next section.

  3. **Configure single sign-on (SSO)**

Choose one of the following SSO provider options based on the identity provider you use to manage user and group access to Google SecOps: 

     * **Google Cloud Identity** : To use Cloud Identity or Google Workspace.

     * **Workforce Identity Federation** : Your third-party identity provider.

If your identity provider isn't listed, configure it, and then select it from the list. For details, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

Click **Next** to move to the next section.

  4. **Terms of service**

Select the **I agree to...** checkbox to agree to the terms.




### Start the instance setup

Click **Start setup** to set up your Google SecOps instance according to the displayed details.

The system checks whether the Chronicle API is enabled. If the API is enabled, it runs the deployment process, which can take up to 30 minutes to complete.

  * When the deployment completes successfully, the system sends you a notification.
  * If the deployment fails, contact your Google representative (or, if they're not available reach out to [Google SecOps Support](https://console.cloud.google.com/support)).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
