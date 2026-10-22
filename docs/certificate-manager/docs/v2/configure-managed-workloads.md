---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads/
title: Configure lifecycle management for managed workloads \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:44.607642+00:00
---

# Configure lifecycle management for managed workloads  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Configure lifecycle management for managed workloads Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure certificate lifecycle management for managed workloads such as Compute Engine and Google Kubernetes Engine (GKE), using Certificate Manager (2nd gen). You can automate certificate issuance and renewal by linking a managed workload identity pool to a Certificate Authority Service pool using a certificate issuance configuration. This helps prevent service outages caused by expired certificates. 

## How managed workload identity works

[Managed workload identity](https://docs.cloud.google.com/iam/docs/managed-workload-identity) gives your Compute Engine and GKE workloads an attested identity, along with a certificate and the trust anchors that the workloads use to authenticate to each other over mutual TLS (mTLS). Managed workload identities are grouped into a workload identity pool, which acts as the trust boundary for the identities in it.

When you link a workload identity pool to a CA Service pool, Google Cloud automatically issues and renews certificates for your workloads. This automation eliminates manual credential management and prevents service outages.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Compute Engine, Certificate Manager, Certificate Authority Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com,privateca.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Compute Engine, Certificate Manager, Certificate Authority Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com,privateca.googleapis.com)

  10. Make sure that you have an existing workload identity pool with managed workload identities. For more information, see [Configure managed workload identity authentication for Compute Engine](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities) or [Configure managed workload identity authentication for GKE](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke). 
  11. Make sure that you have an existing CA Service pool that can issue certificates to your workloads. For more information, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool). 



### Required roles

To get the permissions that you need to configure lifecycle management, ask your administrator to grant you the following IAM roles on your project: 

  * [Certificate Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.editor) (`roles/certificatemanager.editor`)
  * [CA Service Certificate Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.certificateManager) (`roles/privateca.certificateManager`)
  * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure lifecycle for managed workloads

Configure a managed workload identity pool to specify how associated workloads receive and renew certificates from your existing CA Service pool.

  1. In the Google Cloud console, go to the **Certificate Manager (2nd gen)** page. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/landing)

  2. In the navigation pane, click **Manage Lifecycle**.
  3. Select the **Managed Workload Identity** tab.
  4. Locate the workload identity pool that you want to configure, and then click **Configure lifecycle management**.
  5. Select the **Region** and the **CA pool** for the region.
  6. In the **Certificate lifetime** field, specify the validity of the issued certificate. The value must be between 21 and 30 days.
  7. Set the **Rotation window** to a value between 50 and 80. This is the percentage of the certificate's lifetime that triggers a renewal.
  8. In the **Key algorithm** field, select the encryption algorithm to use to generate the private key.
  9. Click **Update**.



## What's next

  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)
  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)
  * [Configure lifecycle management for load balancers](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-load-balancers)
  * [Create trust configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/trust-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
