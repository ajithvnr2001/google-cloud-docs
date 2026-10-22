---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/inventory/
title: View certificate directory \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:32.496134+00:00
---

# View certificate directory  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  View certificate directory Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to view and filter your certificate directory by using the Certificate Manager (2nd gen) page in the Google Cloud console. You can use the directory to monitor the expiration status of your certificate, identify associated resources, and find specific certificates.

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

To get the permissions that you need to view the certificate directory, ask your administrator to grant you the following IAM roles on your project: 

  * [Certificate Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.viewer) (`roles/certificatemanager.viewer`)
  * [Certificate Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.editor) (`roles/certificatemanager.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access the certificate directory

To access the directory and view your certificates, follow these steps:

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to certificate directory](https://console.cloud.google.com/security/ccm/certificateDirectory)

  2. Review the certificate directory table that's displayed.




By default, the table displays only **long-duration certificates** (lifetime greater than 72 hours). To display short-duration certificates, see Include short-duration certificates.

**Note:** Certificate Manager (2nd gen) doesn't present certificates from CA Service that are encrypted with customer-managed encryption keys (CMEK).**Note:** For large projects that contain more than one million certificates, cataloging into the directory can take up to a week. Certificate Manager gradually identifies and populates certificates to ensure reliable operation.

## Filter your certificate directory

Use filters to find specific certificates or narrow down your directory view based on your monitoring needs.

### Include short-duration certificates

By default, the system excludes short-duration certificates because their automated rotation can create noise. These workloads use short-duration certificates that rotate frequently for mutual TLS (mTLS). You can include them to audit or troubleshoot workloads that use managed workload identity or Agent Identity. Displaying them can help you verify successful certificate rotation and check workload identity state.

To view certificates with a lifetime under 72 hours, follow these steps:

  * Click the **Include short-duration certificates** toggle. The certificates are displayed in the directory.



### Use the filter panel

To filter the table using predefined values, follow these steps:

  1. Click **Filter panel**.
  2. Select the checkboxes next to the criteria that you want to apply, such as **Issuer type** or **Expiration status**.



### Use the filter bar

To enter custom filters for specific columns, follow these steps:

  1. Click the **Filter** field in the filter bar in the directory table.
  2. Select a column from the list, such as **Identity** , **Expiration date** , or **Resources**.
  3. Enter the value that you want to filter for (for example, a domain name or a specific resource name).



## Review and manage certificate details

To monitor key parameters and manage individual certificates in the directory table, use the following tasks.

### Monitor certificate status and view certificate details

To check the status of a specific certificate, follow these steps:

  1. Locate the certificate in the directory table.
  2. Review the **Expiration status** column to determine whether the certificate is valid or expired.
  3. Click the identity name (Common Name or SAN) in the **Identity** column to view its full details.



### Audit locations and resources

To verify the source and usage of your certificates, follow these steps:

  1. Look at the **Location** and **Issuer type** columns to verify where your certificates are staged and whether they were issued by a public CA (such as Public Certificate Authority) or a private CA (such as CA Service).
  2. In the **Resources** column, find the Google Cloud resource that issued the certificate, such as a `TargetHttpsProxy`.
  3. Click the resource name to view more information about that specific resource.



### Track lifecycle dates

To monitor issuance and expiration timelines, follow these steps:

  1. Locate the certificate in the directory table.
  2. Review the **Issuance date** and **Expiration date** columns to track when your managed certificates were generated and when they are scheduled to expire.



## What's next

  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)
  * [Configure lifecycle management for managed workloads](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
