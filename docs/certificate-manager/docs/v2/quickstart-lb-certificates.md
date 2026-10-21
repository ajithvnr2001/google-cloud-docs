---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-lb-certificates/
title: Automate certificate lifecycle for load balancers \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:04:08.368704+00:00
---

# Automate certificate lifecycle for load balancers  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-lb-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Automate certificate lifecycle for load balancers

Learn how to use Certificate Manager (2nd gen) to automate the lifecycle of a Google-managed certificate for a global Application Load Balancer.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, Certificate Manager, Certificate Authority Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com,privateca.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, Certificate Manager, Certificate Authority Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com,privateca.googleapis.com)

  8. You need an existing Application Load Balancer with at least one target HTTPS proxy. For more information, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer). 



### Required roles

To get the permissions that you need to configure lifecycle management, ask your administrator to grant you the following IAM roles on your project: 

  * [Certificate Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.editor) (`roles/certificatemanager.editor`)
  * [Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure lifecycle management. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure lifecycle management:

  * `compute.targetHttpsProxies.update`
  * `compute.targetSslProxies.update`
  * `compute.targetHttpsProxies.setCertificateMap`
  * `compute.targetSslProxies.setCertificateMap`
  * `compute.sslCertificates.*`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure certificate lifecycle management

To configure lifecycle management for your load balancer certificate:

  1. In the Google Cloud console, go to **Certificate Manager (2nd gen)**. 

[Go to Certificate Manager (2nd gen)](https://console.cloud.google.com/security/ccm/overview)

  2. In the navigation menu, click **Manage Lifecycle**.

  3. Click the **Load balancing** tab. A list of your load balancers appears.

  4. Expand the load balancer row to see the attached certificates.

  5. Click the name of the **target proxy**.

  6. Click **Configure lifecycle management**. The page displays a list of associated certificates that you can add to and remove from.

  7. Click **Certificate** and then click **Add certificate**.

  8. Select an existing certificate or create a new certificate.

  9. Enter the following details for the new certificate:

     * **Name:** Enter a unique name (for example, `my-lb-cert`).
     * **Scope:** Select the appropriate key distribution scope (for example, `Default`).
     * **Certificate type:** Select Self-managed or Google-managed certificates. For more information, see [certificate types](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types).
     * **Domain Name:** Enter the domain name that this certificate covers (for example, `app.example.com`). This domain must be one that you control.
     * **Issuance Configuration:** Select your existing issuance configuration from the list. This configuration dictates the certificate authority, lifetime, and key type.
  10. Click **Create**. The console adds the new certificate to the list for the target proxy.

  11. Review the list of certificates, and then click **Update** to apply the changes to the target proxy.




### Verify the configuration

To verify the certificate configuration:

  1. Check the certificate status. Issuance and provisioning can take from several minutes to a few hours. The certificate starts with a **Pending** status.

  2. Monitor the certificate status on the **Certificates** tab within Certificate Manager (2nd gen). When the status is **Active** , the certificate is ready.

  3. Ensure your domain's DNS records point to the load balancer IP address.

  4. Test the setup by accessing your service using HTTPS (for example, `https://app.example.com`).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. **Remove the certificate from the target proxy:**

     1. Go to the **Manage Lifecycle > Load balancing** tab for your target proxy.
     2. Find the certificate that you created (`my-lb-cert`).
     3. Remove the certificate from the list.
     4. Click **Update**.
  2. **Delete the certificate resource:**

     1. Go to the **Certificates** tab in Certificate Manager (2nd gen).
     2. Select the certificate (`my-lb-cert`).
     3. Click **Delete**.



You don't need to delete the load balancer, target proxy, or certificate issuance configuration that you created or used in this quickstart.

## What's next

  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Issue a certificate using CA Service and verify in Certificate Manager (2nd gen)](https://docs.cloud.google.com/certificate-manager/docs/v2/quickstart-ca-service)
  * [View certificate inventory](https://docs.cloud.google.com/certificate-manager/docs/v2/inventory)
  * [Create issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/v2/issuance-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
