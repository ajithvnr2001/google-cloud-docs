---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/configure-load-balancers/
title: Configure lifecycle management for load balancers \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:09.016205+00:00
---

# Configure lifecycle management for load balancers  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/configure-load-balancers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Configure lifecycle management for load balancers Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows how to configure certificate lifecycle management for Application Load Balancers using Certificate Manager (2nd gen). 

There are different ways to configure a load balancer's certificates depending on the properties of the load balancer and previously configured certificate configuration parameters. The Certificate Manager (2nd gen) interface detects and displays the appropriate configuration method based on what is available for a particular load balancer.

The following options are available:

  1. Configure a global load balancer with an SSL certificate.
  2. Configure a regional load balancer with a networking certificate or Compute SSL certificate.
  3. Configure a global load balancer with a certificate map.
  4. Configure a global load balancer with a networking certificate.



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

  10. Make sure that you have an existing Application Load Balancer with at least one target HTTPS proxy. For more information, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer). 



### Required roles

To get the permissions that you need to configure lifecycle management, ask your administrator to grant you the following IAM roles on your project: 

  * [Certificate Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.editor) (`roles/certificatemanager.editor`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure lifecycle for load balancers

To configure lifecycle management for your load balancer certificate, follow the steps for your specific load balancer configuration:

### Global load balancer with Compute SSL certificates

  1. In the Google Cloud console, go to **Certificate Manager (2nd gen)**. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/landing)

  2. In the navigation menu, click **Manage Lifecycle**.

  3. Click the **Load balancing** tab. A list of your load balancers appears.

  4. Locate the load balancer and click the toggle node to expand the row to see the associated target proxies.

  5. Click the name of the target proxy.

  6. Click **Configure lifecycle management**. The page displays certificates associated with this target proxy.

  7. Select a certificate from the available list. You can use your own certificate or a Google-managed certificate.

  8. Click **Additional certificates** and then **Add a certificate**.

  9. Select a certificate from the available list. Each forwarding rule of the load balancer can have 1-14 additional certificates.

  10. Click **Update** to apply the changes to the target proxy. This action updates the underlying certificate map entry or creates a new one.




### Regional load balancer with networking or SSL certificates

  1. In the Google Cloud console, go to **Certificate Manager (2nd gen)**. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/landing)

  2. In the navigation menu, click **Manage Lifecycle**.

  3. Click the **Load balancing** tab. A list of your load balancers appears.

  4. Locate the load balancer and click the toggle node to expand the row to see the associated target proxies.

  5. Click the name of the target proxy.

  6. Click **Configure lifecycle management**. The page displays certificates associated with this target proxy's effective certificate map.

  7. Select a repository type: **Certificates** or **Classic certificates**.

  8. Click **Add a certificate**.

  9. Select an existing certificate or create a new certificate.

  10. Enter the following details for the new certificate:

     * **Name:** A unique name for this certificate resource (for example, `my-lb-cert`).
     * **Scope:** Select the appropriate key distribution scope (for example, `Default`).
     * **Certificate type:** Self-managed or Google-managed [types of certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types).
     * **Domain Name:** The domain name this certificate will cover (for example, `app.example.com`). This domain must be one that you control.
     * **Issuance Configuration:** Select your existing issuance configuration from the list. This configuration dictates the CA, lifetime, and key type.
  11. Click **Create**. The console adds the new certificate to the list for the target proxy.

  12. Review the list of certificates, and then click **Update** to apply the changes to the target proxy. This action updates the underlying certificate map entry or creates a new one.




### Global load balancer with a certificate map

  1. In the Google Cloud console, go to **Certificate Manager (2nd gen)**. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/landing)

  2. In the navigation menu, click **Manage Lifecycle**.

  3. Click the **Load balancing** tab. A list of your load balancers appears.

  4. Locate the load balancer and click the toggle node to expand the row to see the associated target proxies.

  5. Click the name of the target proxy.

  6. Click **Update certificate map**. The page displays certificate map details and certificate map entries.

  7. Click **Edit** and then click **Add map entry**.

  8. Enter the following details for the new map entry:

     * **Name:** A unique name for this certificate resource (for example, `my-lb-cert`).
     * **Hostname:** Select the appropriate hostname. Certificate searches match the exact hostname provided. For single-level subdomains, the search also includes certificates issued for the parent domain wildcard. For example, entering `app.example.com` returns certificates for both `app.example.com` and `*.example.com`.
  9. Select an existing certificate or create a new certificate.

  10. Click **Add**. The console adds the new certificate to the list for the target proxy.

  11. Review the list of certificates, and then click **Save** to apply the changes to the target proxy. This action updates the underlying certificate map entry or creates a new one.




### Global load balancer with a networking certificate

  1. In the Google Cloud console, go to **Certificate Manager (2nd gen)**. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/landing)

  2. In the navigation menu, click **Manage Lifecycle**.

  3. Click the **Load balancing** tab. A list of your load balancers appears.

  4. Locate the load balancer and click the toggle node to expand the row to see the associated target proxies.

  5. Click the name of the target proxy.

  6. Click **Configure lifecycle management**. The page displays certificates associated with this target proxy's effective certificate map.

  7. Click **Add a certificate**.

  8. Select an existing certificate or create a new certificate.

  9. Enter the following details for the new certificate:

     * **Name:** A unique name for this certificate resource (for example, `my-lb-cert`).
     * **Scope:** Select the appropriate key distribution scope (for example, `Default`).
     * **Certificate type:** Self-managed or Google-managed [types of certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types).
     * **Domain Name:** The domain name this certificate will cover (for example, `app.example.com`). This domain must be one that you control.
     * **Issuance Configuration:** Select your existing issuance configuration from the list. This configuration dictates the CA, lifetime, and key type.
  10. Click **Create**. The console adds the new certificate to the list for the target proxy.

  11. Review the list of certificates, and then click **Update** to apply the changes to the target proxy. This action updates the underlying certificate map entry or creates a new one.




## What's next

  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Configure lifecycle management for managed workloads](https://docs.cloud.google.com/certificate-manager/docs/v2/configure-managed-workloads)
  * [Create trust configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/trust-configuration)
  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Monitor your certificates](https://docs.cloud.google.com/certificate-manager/docs/v2/monitor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
