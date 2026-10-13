---
url: https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier/
title: Activate Security Command Center Standard tier for an organization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:45.757294+00:00
---

# Activate Security Command Center Standard tier for an organization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Activate Security Command Center Standard tier for an organization Stay organized with collections  Save and categorize content based on your preferences. 

Standard [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The Security Command Center Standard tier lets you gain centralized visibility into vulnerabilities and risks across your organization. Activating the tier at the organization level in the Google Cloud console grants access to baseline security posture and compliance features across your organization's assets. However, specific vulnerability assessment capabilities require configuration. For feature details, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) and [Differences between Standard and Standard-legacy tiers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy#feature-differences).

To activate other tiers or scopes, see [Activate Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier), [Activate Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier), or [Activate Security Command Center for a project](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project).

## Before you begin

Before you activate Security Command Center Standard for an organization, you need to do the following:

  * Obtain specific Identity and Access Management (IAM) roles and permissions.
  * Optional: Enable the Security Center Management API.
  * Review your organization policies, if applicable to your organization.
  * If you plan to enable data residency, review [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and determine which location to use.
  * If you plan to use a customer-managed encryption key (CMEK), complete the required tasks for [enabling CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek#before_you_begin).

You can configure data residency and data encryption when you activate Security Command Center. To change these settings after you activate Security Command Center Standard or Premium, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).




### Required roles

To get the permissions that you need to activate Security Command Center for an organization, ask your administrator to grant you the following IAM roles on your organization: 

  * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
  * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the Security Center Management API

If you plan to use the Security Center Management API, enable this API in the project where you plan to call it: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securitycentermanagement.googleapis.com)

### Review organization policies

If your organization policies are set to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), confirm the following:

  * You must be signed in to the Google Cloud console on an account that's in an allowed domain.
  * Your service accounts must be in an allowed domain, or members of a group within your domain. This requirement lets you allow services that use the `@*.gserviceaccount.com` service account to access resources when domain-restricted sharing is enabled.



If your organization policies are set to [restrict resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources), verify that the following APIs are [allowed by your policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy):

  * `securitycenter.googleapis.com`
  * `securitycentermanagement.googleapis.com`



## Activate Security Command Center Standard

You can activate Security Command Center Standard for an organization through the Google Cloud console.

  1. In the Google Cloud console, go to the Security Command Center welcome page.

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=organizationId)

  2. If you want to [enable data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#locations), open a [jurisdictional console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console) using the URL that matches the location you plan to configure.

You must use the jurisdictional Google Cloud console to activate Security Command Center with data residency controls and modify the data residency configuration after activation. For details, see [About the jurisdictional Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console).

**Caution:** Security Command Center doesn't validate your data residency location against any organization policies that enforce the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), `gcp.resourceLocations`. When you configure data residency, you must select a location that's consistent with your organization policies. 
  3. Select the organization that you want to enable Security Command Center Standard for, and then click **Get Standard**.

  4. On the welcome page, click **Select**.

  5. Optional: To confirm the data residency configuration or change the data encryption configuration, click **Show more**.

     * If you are using a jurisdictional console, the **Data residency** field displays **Enable** and the **Location** field displays the same location as the jurisdictional console. To change the location, open the console using a URL that matches the location you want to configure. 
     * The default data encryption configuration uses Google-owned and Google-managed encryption keys. To use a Cloud Key Management Service key, click **Edit data encryption** , and then do the following: 
       1. Select **Cloud KMS key**.
       2. Select a project.
       3. Select a key. You can select a key from any Google Cloud project, including projects in other organizations. Only keys in compatible locations are displayed in the list.

To learn which key locations are compatible with Security Command Center, see [Determine the key location](https://docs.cloud.google.com/security-command-center/docs/cmek#key-location). 

If your organization uses [CMEK organization policies](https://docs.cloud.google.com/security-command-center/docs/cmek#org-policies), you might only have the option to choose CMEK or specific keys. 

During the activation process, Security Command Center grants the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role to the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-security-command-center-service-agent) on the Cloud KMS key.

  6. Click **Activate**.




As results become available, they are displayed in the console. Then you can use the Google Cloud console to review and remediate Google Cloud security and data risks.

Security Command Center completes its first full scan within 24 hours. There might be a delay before scans are started for some services. For more information, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

If you [upgrade from Security Command Center Standard to Premium](https://docs.cloud.google.com/security-command-center/docs/modify-standard-tier#standard-to-premium), you gain access to charts that show the scan progress for features such as issues, threats, and frameworks. Existing charts are also updated with scan results from Premium detectors as results become available.

## Services for Security Command Center Standard

After you activate Security Command Center Standard, specific services are automatically enabled, and service agents are created so that these services can act on your behalf.

Security Command Center uses [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) to detect security issues. The following services are enabled when you activate Security Command Center Standard:

  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)

  * [Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security)

  * [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview)




See each service's documentation for usage and optimization instructions.

You can enable additional services by following the steps in [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

## Modify your Security Command Center service tier

For more information about tier management, see [Modify Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/modify-standard-tier).

## What's next

  * Learn how to [configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).
  * Learn how to [use Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).
  * Learn how to work with [Security Command Center findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * Learn about [Google Cloud security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).
  * Find out how [Model Armor](https://docs.cloud.google.com/model-armor/overview) can help protect your AI workloads.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
