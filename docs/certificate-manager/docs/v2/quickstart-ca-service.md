---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-ca-service/
title: Issue a certificate using CA Service and verify in Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:50.055220+00:00
---

# Issue a certificate using CA Service and verify in Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-ca-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issue a certificate using CA Service and verify in Certificate Manager (2nd gen)

Learn how to issue a private certificate with Certificate Authority Service and use Certificate Manager (2nd gen) to view and verify the certificate details in its directory.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the CA Service, Certificate Manager APIs, if any are not already enabled. 

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

  7. Enable the CA Service, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com,certificatemanager.googleapis.com)

  8. You need an existing CA pool with an enabled CA in CA Service. For more information, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool) and [Create a CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authority). 
  9. Ensure you have the required IAM roles. For more information, see Required roles. 



### Required roles

To get the permissions that you need to issue a certificate and view resources, ask your administrator to grant you the following IAM roles on the project: 

  * [CA Service Certificate Requester ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.certificateRequester) (`roles/privateca.certificateRequester`)
  * [CA Service Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.viewer) (`roles/privateca.viewer`)
  * [Certificate Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.viewer) (`roles/certificatemanager.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Issue a certificate using CA Service

To issue a certificate, complete the following steps:

  1. In the Google Cloud console, go to **CA Service**.

[Go to CA Service](https://console.cloud.google.com/security/cas/request)

  2. Follow the instructions in the CA Service documentation to [Request a certificate](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate#request-certificate).

  3. Note the _domain name_ or _identity_ that you specify. You use this value to find the certificate in the directory.




## View and verify the certificate details in Certificate Manager (2nd gen)

After CA Service issues the certificate, Certificate Manager (2nd gen) detects and adds it to the certificate directory as an observed certificate.

To view the certificate, complete the following steps:

  1. In the Google Cloud console, go to **Certificates**.

[Go to Certificates](https://console.cloud.google.com/security/ccm/certificateDirectory)

  2. Wait a few minutes for the certificate to appear in the directory. If it doesn't appear, refresh the directory.

  3. To find the certificate you issued, use the **Filter bar** to search using a relevant filter.

  4. To open the details pane, click the certificate's _domain name_ in the directory list.

  5. Inspect the certificate properties:

     * **Validity** : Check both the **Not valid before** and **Not valid after** dates.
     * **Subject** : Confirm the subject matches the details that you provided during issuance.
     * **Issuance details** : Note the issuing CA and organization.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid incurring unintended costs, revoke and delete the CA service resource.

For more information about managing certificates in CA Service, see [Manage certificates](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state).

**Note:** No Certificate Manager (2nd gen) resources require cleanup. Certificate Manager (2nd gen) only observes the certificate and automatically removes expired records from the directory.

## What's next

  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Automate certificate lifecycle for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-lb-certificates)
  * [View certificate directory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
