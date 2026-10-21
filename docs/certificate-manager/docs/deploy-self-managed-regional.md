---
url: https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional/
title: Deploy a regional self-managed certificate \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:30.132058+00:00
---

# Deploy a regional self-managed certificate  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Deploy a regional self-managed certificate Stay organized with collections  Save and categorize content based on your preferences. 

To secure communication for your regional external Application Load Balancers or regional internal Application Load Balancers, use Certificate Manager to deploy a self-managed certificate. This approach helps you use your own trusted certificates for your applications. This tutorial shows you how to deploy self-managed certificates specifically for regional load balancers.

Before you begin, make sure that you have created a regional external Application Load Balancer or a regional internal Application Load Balancer.

For global external or cross-region deployments, see the following:

  * [Deploy a global external self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)
  * [Deploy a cross-region self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-cross-reg)



## Objectives

This tutorial shows you how to complete the following tasks:

  * Upload a self-managed certificate to Certificate Manager.


  * Deploy the certificate to a regional external Application Load Balancer or to a regional internal Application Load Balancer by using a target HTTPS proxy.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Compute Engine, Certificate Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,certificatemanager.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

Make sure that you have the following roles to complete the tasks in this tutorial:

  * Certificate Manager Owner (`roles/certificatemanager.owner`)

Required to create and manage Certificate Manager resources.

  * Compute Load Balancer Admin (`roles/compute.loadBalancerAdmin`) or Compute Network Admin (`roles/compute.networkAdmin`)

Required to create and manage HTTPS target proxy.




For more information, see the following:

  * [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/permissions) for Certificate Manager.
  * [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam) for Compute Engine.

**Note:** If you aren't assigned the permissions or roles, request the missing roles from the Identity and Access Management (IAM) administrator who has the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`).

### Create the load balancer

This tutorial assumes that you've already created and configured the load balancer's backends, health checks, backend services, and URL maps. Make a note of the URL map's name because you need it later in this tutorial.

  * To create a regional external Application Load Balancer, see [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb).

  * To create a regional internal Application Load Balancer, see [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).




### Create a private key and certificate

To create a private key and a certificate, do the following:

  1. Use a trusted third-party certificate authority (CA) to issue the certificate along with its associated key.

  2. Verify that the certificate is properly chained and root-trusted.

  3. Prepare the following PEM-encoded files:

     * The certificate file (CRT)
     * The corresponding private key file (KEY)



For information about how to request and validate a certificate, see [Create a private key and certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs#create-key-and-cert).

## Upload a self-managed certificate to Certificate Manager

To upload the certificate to Certificate Manager, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Certificate Manager** page.

[Go to Certificate Manager](https://console.cloud.google.com/security/ccm/list)

  2. On the **Certificates** tab, click **Add Certificate**.

  3. In the **Certificate name** field, enter a unique name for the certificate.

  4. Optional: In the **Description** field, enter a description for the certificate. The description lets you identify the certificate. 

  5. For **Location** , select **Regional**.

  6. From the **Region** list, select your region. 

  7. For **Certificate type** , select **Create self-managed certificate**.

  8. For the **Certificate** field, do _either_ of the following:

     * Click the **Upload** button and select your PEM-formatted certificate file.
     * Copy and paste the contents of a PEM-formatted certificate. The contents must start with `-----BEGIN CERTIFICATE-----` and end with `-----END CERTIFICATE-----`.
  9. For the **Private key certificate** field, do _either_ of the following:

     * Click the **Upload** button and select your private key. Your private key must be PEM-formatted and not protected with a passphrase.
     * Copy and paste the contents of a PEM-formatted private key. The private keys must start with `-----BEGIN PRIVATE KEY-----` and end with `-----END PRIVATE KEY-----`.
  10. In the **Labels** field, specify labels to associate with the certificate. To add a label, click add_box**Add label** , and specify a key and a value for your label.

  11. Click **Create**.

The new certificate appears in the list of certificates.




###  gcloud 

To create a regional self-managed certificate, run the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --certificate-file="CERTIFICATE_FILE" \
        --private-key-file="PRIVATE_KEY_FILE" \
        --location="LOCATION"
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `CERTIFICATE_FILE`: the path and filename of the CRT certificate file.
  * `PRIVATE_KEY_FILE`: the path and filename of the KEY private key file.
  * `LOCATION`: the target Google Cloud location.



###  Terraform 

To upload a self-managed certificate, you can use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate#example-usage---certificate-manager-self-managed-certificate-regional) with the `self_managed` block.

###  API 

Upload the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/LOCATION/certificates?certificate_id=CERTIFICATE_NAME
    {
      self_managed: {
        pem_certificate: "PEM_CERTIFICATE",
        pem_private_key: "PEM_KEY",
      }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of your Google Cloud project.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `PEM_CERTIFICATE`: the certificate PEM.
  * `PEM_KEY`: the key PEM.
  * `LOCATION`: the target Google Cloud location.



## Deploy the self-managed certificate to a load balancer

To deploy the self-managed certificate, attach it directly to the target proxy.

### Attach the certificate directly to the target proxy

You can attach the certificate to a new target proxy or an existing target proxy.

To attach the certificate to a new target proxy, use the [`gcloud compute target-https-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create):
    
    
    gcloud compute target-https-proxies create PROXY_NAME \
        --certificate-manager-certificates=CERTIFICATE_NAME \
        --url-map=URL_MAP \
        --region=LOCATION
    

Replace the following:

  * `PROXY_NAME`: name of the target proxy.
  * `CERTIFICATE_NAME`: the name of the certificate.
  * `URL_MAP`: the name of the URL map. You created the URL map when you created the load balancer.
  * `LOCATION`: the target Google Cloud location where you want to create the HTTPS target proxy.



To attach certificate to an existing target HTTPS proxy, use the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update). If you don't know the name of the existing target proxy, go to the [**Target proxies**](https://console.cloud.google.com/net-services/loadbalancing/advanced/targetProxies/list) page and note the name of the target proxy.
    
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --region=LOCATION \
        --certificate-manager-certificates=CERTIFICATE_NAME
    

After creating or updating the target proxy, run the following command to verify it:
    
    
    gcloud compute target-https-proxies list
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the uploaded certificate:
    
    
    gcloud certificate-manager certificates delete CERTIFICATE_NAME
    

Replace `CERTIFICATE_NAME` with the name of the target certificate.

If you don't plan to use the load balancer, delete the load balancer and its resources. See [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).

## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
