---
url: https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed/
title: Deploy a global self-managed certificate \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:40.541740+00:00
---

# Deploy a global self-managed certificate  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Deploy a global self-managed certificate Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Certificate Manager to deploy a global self-managed certificate.

The following load balancers support global self-managed certificates:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Global external proxy Network Load Balancer
  * Classic proxy Network Load Balancer



If you want to deploy to regional or cross-region load balancers, see the following:

  * [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)
  * [Deploy a cross-region self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-cross-reg)



## Objectives

This tutorial shows you how to complete the following tasks:

  * Upload a self-managed certificate to Certificate Manager.


  * Deploy the certificate to a supported load balancer by using a target HTTPS proxy.



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

This tutorial assumes that you've already created and configured the load balancer's backends, health checks, backend services, and URL maps. If you've created an external Application Load Balancer, note the name of the URL map because you need it later in this tutorial.

If you haven't created the load balancer, see the following pages to create one:

  * To create a global external Application Load Balancer, see [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

  * To create a classic Application Load Balancer, see [Set up a classic Application Load Balancer with a managed instance group backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple).

  * To create a Global external proxy Network Load Balancer (SSL proxy), see [Set up a global external proxy Network Load Balancer (SSL proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl).

  * To create a Classic proxy Network Load Balancer (SSL proxy), see [Set up a classic proxy Network Load Balancer (SSL proxy) with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl).




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

  5. For **Location** , select **Global**.

  6. For **Scope** , select **Default**. 

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

To create a global self-managed certificate, use the [`certificate-manager certificates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create):
    
    
    gcloud certificate-manager certificates create CERTIFICATE_NAME \
        --certificate-file="CERTIFICATE_FILE" \
        --private-key-file="PRIVATE_KEY_FILE"
    

Replace the following:

  * `CERTIFICATE_NAME`: the name of the certificate.
  * `CERTIFICATE_FILE`: the path and filename of the CRT certificate file.
  * `PRIVATE_KEY_FILE`: the path and filename of the KEY private key file.



###  Terraform 

To upload a self-managed certificate, you can use a [`google_certificate_manager_certificate` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate) with the `self_managed` block.

###  API 

Upload the certificate by making a `POST` request to the `certificates.create` method as follows:
    
    
    POST /v1/projects/PROJECT_ID/locations/global/certificates?certificate_id=CERTIFICATE_NAME
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



## Deploy the self-managed certificate to a load balancer

To deploy the global self-managed certificate, use a certificate map.

### Create a certificate map

Create a certificate map that references the certificate map entry associated with your certificate:

###  gcloud 

To create a certificate map, use the [`gcloud certificate-manager maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/create):
    
    
    gcloud certificate-manager maps create CERTIFICATE_MAP_NAME
    

Replace `CERTIFICATE_MAP_NAME` with the name of the target certificate map.

###  Terraform 

To create a certificate map, you can use a [`google_certificate_manager_certificate_map` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map).
    
    
    resource "google_certificate_manager_certificate_map" "certificate_map" {
      name        = "${local.name}-certmap-${random_id.tf_prefix.hex}"
      description = "${local.domain} certificate map"
      labels = {
        "terraform" : true
      }
    }

### Create a certificate map entry

Create a certificate map entry and associate it with your certificate and certificate map:

###  gcloud 

To create a certificate map entry, use the [`gcloud certificate-manager maps entries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create):
    
    
    gcloud certificate-manager maps entries create CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME" \
        --certificates="CERTIFICATE_NAME" \
        --hostname="HOSTNAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
  * `CERTIFICATE_MAP_NAME`: name of the certificate map with which the certificate map entry is associated.
  * `CERTIFICATE_NAME`: the name of the certificate you want to associate with the certificate map entry.
  * `HOSTNAME`: hostname that you want to associate with the certificate map entry.

If you want to create a certificate that covers both a wildcard domain and a root domain, then specify the hostname with a root and a wildcard, such as `example.com` and `*.example.com`. In addition, you must specify two certificate map entries - one for `example.com` and the other for `*.example.com`.




###  Terraform 

To create a certificate map entry with a root domain, use a [`google_certificate_manager_certificate_map_entry` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map_entry).
    
    
    resource "google_certificate_manager_certificate_map_entry" "first_entry" {
      name        = "${local.name}-first-entry-${random_id.tf_prefix.hex}"
      description = "example certificate map entry"
      map         = google_certificate_manager_certificate_map.certificate_map.name
      labels = {
        "terraform" : true
      }
      certificates = [google_certificate_manager_certificate.root_cert.id]
      hostname     = local.domain
    }

To create a certificate map entry with a wildcard domain, use a [`google_certificate_manager_certificate_map_entry` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/certificate_manager_certificate_map_entry).
    
    
    resource "google_certificate_manager_certificate_map_entry" "second_entry" {
      name        = "${local.name}-second-entity-${random_id.tf_prefix.hex}"
      description = "example certificate map entry"
      map         = google_certificate_manager_certificate_map.certificate_map.name
      labels = {
        "terraform" : true
      }
      certificates = [google_certificate_manager_certificate.root_cert.id]
      hostname     = "*.${local.domain}"
    }

### Verify that the certificate map entry is active

Verify that the certificate map entry is active before attaching its corresponding certificate map to the target proxy.

To verify the certificate map entry, use the [`gcloud certificate-manager maps entries describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/describe):
    
    
    gcloud certificate-manager maps entries describe CERTIFICATE_MAP_ENTRY_NAME \
        --map="CERTIFICATE_MAP_NAME"
    

Replace the following:

  * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
  * `CERTIFICATE_NAME`: the name of the certificate you want to associate with the certificate map entry.



The output is similar to the following:
    
    
    certificates:
    createTime: '2021-09-06T10:01:56.229472109Z'
    hostname: example.com
    name: projects/my-project/locations/global/certificateMaps/myCertMap/certificateMapEntries/myCertMapEntry
    state: ACTIVE
    updateTime: '2021-09-06T10:01:58.277031787Z'
    

### Attach the certificate map to the target proxy

You can attach the certificate map to a new target proxy or an existing target proxy.

###  gcloud 

To attach the certificate map to a new target proxy, use the [`gcloud compute target-https-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/create):
    
    
    gcloud compute target-https-proxies create PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME" \
        --url-map="URL_MAP" \
        --global
    

Replace the following:

  * `PROXY_NAME`: name of the target proxy.
  * `CERTIFICATE_MAP_NAME`: name of the certificate map referencing the certificate map entry and the associated certificate.
  * `URL_MAP`: the name of the URL map



To attach the certificate map to an existing target HTTPS proxy, use the [`gcloud compute target-https-proxies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update). If you don't know the name of the existing target proxy, go to the [**Target proxies**](https://console.cloud.google.com/net-services/loadbalancing/advanced/targetProxies/list) page and note the name of the target proxy.
    
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --certificate-map="CERTIFICATE_MAP_NAME" \
        --global
    

After creating or updating the target proxy, run the following command to verify it:
    
    
    gcloud compute target-https-proxies list
    

###  Terraform 

To attach the certificate map to the target proxy, you can use a [`google_compute_target_https_proxy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy).

When configuring a target proxy, if you attach TLS (SSL) certificates directly and also through a certificate map, the proxy uses the certificates referenced by the certificate map and ignores the directly attached TLS (SSL) certificates.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete them.

  1. Delete the load balancer and its resources.

See [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).

  2. Delete or detach the certificate map from the proxy.

To delete the certificate map, run the following command:
         
         gcloud compute target-https-proxies delete PROXY_NAME
         

If you want to keep the target HTTPS proxy, then detach the certificate map from the proxy. 

**Caution:** Before you detach the certificate map, note the following considerations.
     * If there are any TLS (SSL) certificates attached directly to the proxy, then detaching the certificate map causes the proxy to resume using those directly attached TLS (SSL) certificates.
     * If there are no TLS (SSL) certificates attached directly to the proxy, then the certificate map can't be detached from the proxy. You must first attach at least one TLS (SSL) certificate directly to the proxy before you can detach the certificate map.

To detach the certificate map, run the following command:
    
    gcloud compute target-https-proxies update PROXY_NAME \
        --clear-certificate-map
    

Replace `PROXY_NAME` with the name of the target proxy.

  3. Delete the certificate map entry from the certificate map:
         
         gcloud certificate-manager maps entries delete CERTIFICATE_MAP_ENTRY_NAME \
             --map="CERTIFICATE_MAP_NAME"
         

Replace the following:

     * `CERTIFICATE_MAP_ENTRY_NAME`: name of the certificate map entry.
     * `CERTIFICATE_MAP_NAME`: name of the certificate map.
  4. Delete the certificate map:
         
         gcloud certificate-manager maps delete CERTIFICATE_MAP_NAME
         

Replace `CERTIFICATE_MAP_NAME` with the name of the certificate map.

  5. Delete the uploaded certificate:
         
         gcloud certificate-manager certificates delete CERTIFICATE_NAME
         

Replace `CERTIFICATE_NAME` with the name of the certificate.




## What's next

  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Manage certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps)
  * [Manage certificate map entries](https://docs.cloud.google.com/certificate-manager/docs/map-entries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
