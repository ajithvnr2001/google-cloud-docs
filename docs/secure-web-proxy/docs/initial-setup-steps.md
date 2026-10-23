---
url: https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps/
title: Initial setup steps \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:35.648548+00:00
---

# Initial setup steps  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Initial setup steps Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the initial setup steps that are required to use Secure Web Proxy.

**Note:** These setup steps are required only before the first time you use Secure Web Proxy.

## Get IAM roles and permissions

To get the permissions that you need to provision a Secure Web Proxy instance, request your administrator to grant you the following IAM roles on your project:

  * To configure policies and provision a Secure Web Proxy instance: [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * To upload explicit Secure Web Proxy TLS certificates: [Certificate Manager Editor role](https://docs.cloud.google.com/certificate-manager/docs/permissions#certificatemanager.editor) (`roles/certificatemanager.editor`)
  * To configure distributed tracing and telemetry policies: [Network Services Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.admin) (`roles/networkservices.admin`) or [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * To view trace spans in Cloud Trace: [Cloud Trace User role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)
  * To export trace spans to Trace: grant the [Cloud Trace Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`) to the following service accounts: 
    * Compute Engine service agent: `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`
    * Network Security service agent: `service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com`
    * Client virtual machine (VM) service accounts, if client applications generate or propagate spans



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through custom roles or other predefined roles.

Optional: If you have a set of users who are responsible for managing your Compute Engine organization security policies, then grant them the [Compute Organization Security Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityPolicyAdmin) (`roles/compute.orgSecurityPolicyAdmin`).

For more information about project roles and permissions, see the following:

  * [Identity and Access Management documentation](https://docs.cloud.google.com/iam/docs)
  * [Compute Engine API documentation](https://docs.cloud.google.com/compute/docs/apis)
  * [Cloud Monitoring API documentation](https://docs.cloud.google.com/monitoring/docs/apis)



## Create a Google Cloud project

To create or select a Google Cloud project, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Either [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or select an existing project.




###  gcloud 

You can follow one of these steps:

  * To create a Google Cloud project, use the [`gcloud projects create` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create).
        
        gcloud projects create PROJECT_ID
        

Replace `PROJECT_ID` with a unique project ID.

  * To select an existing Google Cloud project, use the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
        
        gcloud config set project PROJECT_ID
        




## Enable billing

Make sure that billing is enabled for your Google Cloud project. For more information, see [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project) and [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

## Enable the required APIs

###  Console 

  1. In the Google Cloud console, go to the **Enable access to APIs** page.

[Go to Enable access to APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute,certificatemanager,networkservices,networksecurity,cloudtrace)

Follow the instructions to enable these required APIs: Compute Engine API, Certificate Manager API, Network Services API, Network Security API, and Cloud Trace API.

  2. Optional: If you plan to [configure TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection) for your proxy, then you must enable the Certificate Authority Service API.

[Go to Enable access to API](https://console.cloud.google.com/apis/enableflow?apiid=privateca)




###  gcloud 

To enable the required Google Cloud APIs, use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
    
    
    gcloud services enable \
        compute.googleapis.com \
        certificatemanager.googleapis.com \
        networkservices.googleapis.com \
        networksecurity.googleapis.com \
        privateca.googleapis.com \
        cloudtrace.googleapis.com
    

**Optional** : Enable the following APIs if required:

  * To configure TLS inspection for your proxy, enable the Certificate Authority Service API (`privateca.googleapis.com`).

  * To [trace outbound traffic with Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces), enable the Trace API (`cloudtrace.googleapis.com`).




## Create a VPC subnet

Create a subnet in the VPC network for each region where you want to deploy your Secure Web Proxy instance. If you've previously created a subnet, then you can reuse it as a VPC subnet by setting the `purpose` parameter to `PRIVATE`.

**Important:** VPC subnets are referenced when [creating a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-a-gateway).

###  gcloud 

To create a subnet, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create VPC_SUBNET_NAME \
        --purpose=PRIVATE \
        --region=REGION \
        --network=NETWORK_NAME \
        --range=IP_RANGE
    

Replace the following:

  * `VPC_SUBNET_NAME`: name of your VPC subnet
  * `REGION`: region where you want to deploy your VPC subnet
  * `NETWORK_NAME`: name of your VPC network
  * `IP_RANGE`: subnet range, such as `10.10.10.0/24`



## Create a proxy subnet

Create a proxy subnet for each region where you want to deploy your Secure Web Proxy instance.

We recommend that you create a subnet size of `/23`, which can store up to 512 proxy-only addresses. Secure Web Proxy uses this range to allocate a dedicated pool of unique IP addresses. This reserved pool helps ensure that the proxy has sufficient capacity to handle scaling and securely interact with Cloud NAT and destinations in your VPC network.

**Important:** Proxy-only subnets aren't referenced when [creating a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-a-gateway). For more information, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

###  gcloud 

To create a proxy subnet, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create PROXY_SUBNET_NAME \
        --purpose=REGIONAL_MANAGED_PROXY \
        --role=ACTIVE \
        --region=REGION \
        --network=NETWORK_NAME \
        --range=IP_RANGE
    

Replace the following:

  * `PROXY_SUBNET_NAME`: name of your proxy subnet
  * `REGION`: region where you want to deploy the proxy subnet
  * `NETWORK_NAME`: name of your VPC network
  * `IP_RANGE`: subnet range, such as `192.168.0.0/23`



## Deploy a TLS certificate

Because the default and most basic function of Secure Web Proxy—policy enforcement without deep inspection—doesn't require Transport Layer Security (TLS) certificates, TLS (formerly [SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0)) certificates are optional for Secure Web Proxy.

TLS certificates are required for Secure Web Proxy only when clients—the workloads, applications, or devices within your network—connect to the proxy by using HTTPS. For more information, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

To deploy TLS certificates by using Certificate Manager, follow any one of these methods:

  * [Deploy a regional Google-managed certificate with per-project DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional)

  * [Deploy a regional Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional)

  * [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)




The following example shows how to deploy a regional self-managed certificate by using Certificate Manager:

  1. Create a TLS certificate.
         
         openssl req -x509 -newkey rsa:2048 \
             -keyout KEY_PATH \
             -out CERTIFICATE_PATH -days 365 \
             -subj '/CN=SWP_HOST_NAME' -nodes -addext \
             "subjectAltName=DNS:SWP_HOST_NAME"
         

Replace the following:

     * `KEY_PATH`: path at which to save the private key, such as `~/key.pem`
     * `CERTIFICATE_PATH`: path at which to save the certificate, such as `~/cert.pem`
     * `SWP_HOST_NAME`: hostname of your Secure Web Proxy instance, such as `myswp.example.com`
  2. [Upload the TLS certificate to Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional#upload-self-managed-certificate-to-certificate-manager)

  3. [Deploy the TLS certificate to a load balancer](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional#deploy_the_self-managed_certificate_to_a_load_balancer)




## What's next

  * [Create and deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)
  * [Enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection)
  * [Create a policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy)
  * [Configure rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
