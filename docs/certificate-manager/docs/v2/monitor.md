---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/monitor/
title: Monitor your certificates \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:01.008542+00:00
---

# Monitor your certificates  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Monitor your certificates Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Certificate Manager (2nd gen) overview dashboard helps you maintain a secure and healthy certificate environment. You can use the dashboard to identify expiring certificates, audit your security posture, and track issuance trends.

The overview dashboard includes the following monitoring charts:

  * **Number of certificates issued in the last 7 days** : Tracks the total number of certificates issued over the last 7 days.
  * **Certificates issued by authority type** : Groups certificates by authority type (public, private, or unknown).
  * **Certificates issued by location** : Sorts certificates geographically by deployment location.
  * **Expiring certificates** : Shows certificates expiring within both 7 and 30 days.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Certificate Authority Service, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com,certificatemanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Certificate Authority Service, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com,certificatemanager.googleapis.com)




### Required roles

To get the permissions that you need to monitor certificates, ask your administrator to grant you the following IAM roles on your project: 

  * [Certificate Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.viewer) (`roles/certificatemanager.viewer`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access the overview dashboard

To access the dashboard and view your certificate metrics, follow these steps:

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager overview dashboard](https://console.cloud.google.com/security/ccm/overview)

  2. Optional: To adjust the time span, use the time selector at the top right of the dashboard. By default, the dashboard displays metrics for the last 7 days.




The dashboard data updates every 24 hours.

## Monitor certificate health and expirations

The dashboard provides metrics specifically focused on **long-duration certificates** , which are certificates with a lifetime that's greater than 72 hours.

Certificate Manager (2nd gen) excludes short-duration certificates (with a lifetime of less than 72 hours) because they undergo frequent automated rotation and don't require the same manual monitoring as long-duration certificates.

To monitor expiring certificates that require manual intervention, follow these steps:

  1. Locate the **Expiring certificates** chart on the dashboard.
  2. Review the warnings for certificates nearing expiration.
  3. If you receive an expiration warning, search your inventory by using certificate identity to verify if a replacement is already in place. For more information, see [Filter the certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory#filter-inventory).

**Note:** An expiring certificate warning doesn't always mean that a replacement certificate hasn't been issued.

## Audit your certificate inventory

Use the **Inventory metrics** section of the dashboard to audit the active certificates in your environment during your selected time span.

To audit your inventory, review the certificates categorized by the following criteria:

  * **View active certificates by resource** : Track certificate volume based on the Google Cloud resource that issued them. Certificate Manager (2nd gen) identifies certificates issued by either managed workload identity or load balancing; other certificates issued through Certificate Authority Service are categorized as **Unspecified**. For more information, see [Supported services](https://docs.cloud.google.com/certificate-manager/docs/v2/overview#supported-gcp-services).
  * **View active certificates by key algorithm** : Audit your cryptographic standards by grouping certificates by their leaf key algorithm (for example, RSA or ECDSA). This ensures compliance with your organization's security policies.
  * **View active certificates by key usage profile** : Group certificates by their intended use. Certificate Manager labels certificates by the closest matching profile. If a profile can't be determined, it is labeled as **Other**.



To view the specific certificates in any of these categories, click **View certificates** to open the inventory page.

## Track certificate issuance trends

Use the **Issuance metrics** chart to monitor how your configured services generate certificates over time. This approach helps you track growth and identify potential issuance anomalies.

To track issuance trends, monitor the following metrics:

  1. **Certificates issued by location** : Observe the number of certificates issued in each location to see the geographic distribution of your certificate volume.
  2. **Certificates issued by authority type** : Observe the number of certificates issued by public CAs (such as Public Certificate Authority) versus private CAs (such as CA Service).
  3. **Total certificates issued** : Monitor the total volume of certificates issued in the selected time span to understand the scale of your environment.



## What's next

  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)
  * [Monitor resources using Cloud Monitoring](https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
