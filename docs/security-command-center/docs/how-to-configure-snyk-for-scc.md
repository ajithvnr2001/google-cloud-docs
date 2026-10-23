---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-snyk-for-scc/
title: Send Snyk data to Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:25.439429+00:00
---

# Send Snyk data to Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-snyk-for-scc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Snyk data to Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The **Snyk for Google Security Command Center (SCC)** integration, available in Cloud Marketplace, lets you view and manage issues identified by Snyk as security findings in Google Cloud. Issues received from Snyk are represented in Security Command Center as code security findings. When Snyk issues are updated, the corresponding Security Command Center findings are automatically updated as well.

Complete the following sections in order:

  1. Before you begin

  2. Configure the integration in the Google Cloud console

  3. Configure the integration in Snyk

  4. View Snyk findings




## Before you begin

  * Create a Snyk user account with [permissions to edit and view group integrations](https://docs.snyk.io/admin/user-roles/user-role-management).

  * Prepare your Google Cloud environment.

    1. Create a Google Cloud organization with Security Command Center enabled at the organization level. For information about how to do this, see the following documentation specific to your Security Command Center service tier:

       * [Activate Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)
       * [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)
       * [Activate Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier)
    2. Identify or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) in the organization from the previous step. Record the project information. You need this when configuring the integration.

    3. Optional: Manually [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) in the project from the previous step, then do the following. If you don't create the service account manually, you must create it when configuring the integration. It is used to authenticate with Google Cloud.

       1. Grant the [Security Center Findings Editor (`roles/securitycenter.findingsEditor`)](https://docs.cloud.google.com/security-command-center/docs/access-control-org#securitycenter.findingsEditor) role to the service account.

       2. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) for the service account. Create the key in JSON format.

       3. Record the following information. You use this when configuring the integration.

          * Service account name
          * Service account ID
          * Service account key



### Configure the integration in the Google Cloud console

During this process, you configure the Snyk integration and create or configure a service account.

  1. If you manually created the service account, get the following information:

     * Service account name: display name for this service account.
     * Service account ID: alphanumeric ID used in the service account email address.
  2. In the Google Cloud console, go to the **Snyk for Google Security Command Center (SCC)** in **Marketplace**.

[Go to Snyk listing](https://console.cloud.google.com/marketplace/product/snyk-marketplace/snyk-google-scc)

As an alternative, you can search for **Snyk for Google Security Command Center (SCC)** in [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace).

  3. Select the organization where Security Command Center is enabled.

  4. Click **Sign up with partner** to configure the integration.

  5. Click **Change** to select a project in the organization. This is where the service account exists if you have already created it. If you have not created the service account, this is where it is created.

  6. Select one of the following options:

     * **Create a new service account**. Select this if you didn't create a service account manually. Enter the following information:

       * Service account name: display name for this service account.
       * Service account ID: alphanumeric ID used in the service account email address.
     * **Use an existing service account**. Select this if you created a service account manually. From the menu, select the service account.

  7. Click **Submit**.

  8. In Security Command Center, go to **Settings** > **Integrated services**.

  9. Find the listing for **Snyk for Google Security Command Center (SCC)**.

  10. Record the **Source ID** value for the integration. You need this information in the following section. This is also known as the relative resource name stored in the finding source [`name`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources) field.

  11. If you selected **Create a new service account** in the previous step, go to IAM in Google Cloud console and [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) for the service account that was created. Create the key in JSON format and save it. You use it in a later step.




### Configure the integration in Snyk

  1. Collect the following information:

     * Source ID: the relative resource name that you saved in the previous section. The Google Cloud organization ID is parsed automatically from this field.

     * Service account key: the JSON key that you created from the service account.

  2. Navigate to your Snyk group-level integrations page, called **Integrations Hub** , and then sign in using your Snyk credentials.

  3. Search for `Google SCC`, and then click **Use integration** in the **Google SCC** entry that is returned.

  4. Enter values for the following:

     * **Profile name** : a name that you define for this integration.
     * **Source ID** : you recorded this previously.
     * **Service account key** : you recorded this previously.
  5. Click **Done**.




After the connection is established, the **Google SCC** integration status changes to **Setup in progress**. The status automatically changes to **Connected** when the next Snyk scan occurs in your environment.

## View Snyk findings on the Findings page

To display only findings received from Snyk, add the following condition to the query: `parent_display_name="Snyk for Google Security Command Center (SCC)"`.

See [Review and manage findings in the console](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) for more information about using the Google Cloud console **Findings** page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
