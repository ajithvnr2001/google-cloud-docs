---
url: https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets/
title: Set up a regional external Application Load Balancer with Cloud Storage buckets \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:57.730130+00:00
---

# Set up a regional external Application Load Balancer with Cloud Storage buckets  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external Application Load Balancer with Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create a regional external Application Load Balancer to route requests for static content to [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).

## Before you begin

Make sure that your setup meets the following prerequisites.

### Install the Google Cloud CLI

Some of the instructions in this guide can only be carried out using the Google Cloud CLI. To install it, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

You can find commands related to load balancing in the [API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis) document.

### Required roles

If you are the project creator, you are granted the [Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, the Owner role (`roles/owner`) or the Editor role (`roles/editor`) includes the permissions necessary to follow this document.

If you aren't the project creator, required permissions must be granted on the project to the appropriate [_principal_](https://docs.cloud.google.com/iam/docs/overview#principals). For example, a principal can be a Google Account (for end users) or a service account. 

To get the permissions that you need to to create Cloud Storage buckets and network resources, ask your administrator to grant you the following IAM roles on your project: 

  * Create a VPC network and load balancing components: [Compute Network Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
  * Create Cloud Storage buckets: [Storage Object Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles and permissions for Cloud Load Balancing, see [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control). For more information about defining IAM policies with conditional grants for forwarding rules, see [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions).

### Set up an SSL certificate resource

For a regional external Application Load Balancer that uses HTTPS as the request-and-response protocol, you can create an SSL certificate resource using either a Compute Engine SSL certificate or a Certificate Manager certificate.

For this example, create an SSL certificate resource using Certificate Manager as described in one of the following documents:

  * [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional)
  * [Deploy a regional Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional)
  * [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)



After you create the certificate, you can attach the certificate to the HTTPS target proxy.

We recommend using a Google-managed certificate.

## Limitations

The following limitations apply to Cloud Storage buckets when serving as backends to a regional external Application Load Balancer:

  * Private bucket access isn't supported, so the backend bucket must be publicly accessible over the internet.

  * [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) aren't supported.

  * Cloud CDN integration isn't available when creating backend buckets for a regional external Application Load Balancer.

  * When using a regional external Application Load Balancer to access backend buckets, only the HTTP `GET` method is supported. You can download content from the bucket, but uploading content to the bucket through the regional external Application Load Balancer isn't available.

  * For a regional external Application Load Balancer, Cloud Storage buckets are supported only in the region where the load balancer is configured. [Dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) or [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) buckets aren't supported.




## Setup overview

The following diagram shows a regional external Application Load Balancer with backend buckets located in the same region as the load balancer.

The forwarding rule of the regional external Application Load Balancer has an external IP address.

[ ![A regional external Application Load Balancer sends traffic to a Cloud Storage backend.](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-backend-buckets.svg)](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-backend-buckets.svg) Distributing traffic to Cloud Storage (click to enlarge).

In the sections that follow, you configure the different resources as shown in the preceding diagram.

## Configure the network and the proxy-only subnet

**Note:** For this setup, you don't need a subnet for the forwarding rule or the Cloud Storage bucket. 

  * Regional external IPv4 addresses always exist outside of VPC networks. For more information, see [Forwarding rules and VPC networks](https://docs.cloud.google.com/load-balancing/docs/https#fw-rule-network).
  * A Cloud Storage bucket isn't associated with any VPC network.



This example uses the following VPC network, region, and proxy-only subnet:

  * **Network**. The network is a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnet for Envoy proxies**. A subnet named `proxy-only-subnet-us` in the `us-east1` region uses `10.129.0.0/23` for its primary IP range.




### Configure a custom mode VPC network

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. Click **Create**.




###  gcloud 

  1. Create a custom VPC network, named `lb-network`, with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create lb-network --subnet-mode=custom
         




### Configure the proxy-only subnet

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google Cloud uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all Envoy-based regional load balancers in the same region as the VPC network. There can only be one active proxy-only subnet for a given purpose, per region, per network.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that you created.

  3. On the **Subnet** tab, click **Add subnet**.

  4. Enter the following information:

     * **Name** : `proxy-only-subnet-us`
     * **Region** : `us-east1`
     * **Purpose** : **Regional Managed Proxy**
     * **IP address range** : `10.129.0.0/23`
  5. Click **Add**.




###  gcloud 

  1. Create a proxy-only subnet in the `us-east1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create proxy-only-subnet-us \
             --purpose=REGIONAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=us-east1 \
             --network=lb-network \
             --range=10.129.0.0/23
         




## Configure your Cloud Storage buckets

The process for configuring your Cloud Storage buckets is as follows:

  * Create the buckets.
  * Copy content to the buckets.



### Create Cloud Storage buckets

In this example, you create two Cloud Storage buckets in the `us-east1` region.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box**Create**.

  3. In the **Get started** section, enter a globally unique name that follows the [naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

  4. Click **Choose where to store your data**.

  5. Set **Location type** to **Region**.

  6. From the list of regions, select **us-east1**.

  7. Click **Create**.

  8. Click **Buckets** to return to the Cloud Storage Buckets page. Use these instructions to create a second bucket in the **us-east1** region.




###  gcloud 

  1. Create the first bucket in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET1_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access
         

  2. Create the second bucket also in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET2_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access
         




Replace the variables `BUCKET1_NAME` and `BUCKET2_NAME` with your Cloud Storage bucket names.

### Copy graphic files to your Cloud Storage buckets

To enable you to test the setup, copy a graphic file from a public Cloud Storage bucket to your own Cloud Storage buckets.

Run the following commands in Cloud Shell, replacing the bucket name variables with your unique Cloud Storage bucket names:
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET1_NAME/love-to-purr/
    
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/two-dogs.jpg gs://BUCKET2_NAME/love-to-fetch/
    

### Make your Cloud Storage buckets publicly readable

To make all objects in a bucket readable to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer role (`roles/storage.objectViewer`).

###  Console 

To grant all users access to view objects in your buckets, repeat the following procedure for each bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab.

  4. In the **Permissions** section, click the person_add**Grant access** button. The **Grant access** dialog appears.

  5. In the **New principals** field, enter `allUsers`.

  6. In the **Select a role** field, enter `Storage Object Viewer` in the filter box and select the **Storage Object Viewer** from the filtered results.

  7. Click **Save**.

  8. Click **Allow public access**.




###  gcloud 

To grant all users access to view objects in your buckets, run the [`buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding).
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET1_NAME \
        --member=allUsers \
        --role=roles/storage.objectViewer
    
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET2_NAME \
       --member=allUsers \
       --role=roles/storage.objectViewer
    

## Reserve the load balancer's IP address

Reserve a static external IP address for the forwarding rule of the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Reserve a static address** page.

[Go to Reserve a static address](https://console.cloud.google.com/networking/addresses/add)

  2. Choose a **Name** for the new address.

  3. For **IP version** , select **IPv4**.

  4. For **Type** , select **Regional**.

  5. For **Region** , select **us-east1**.

  6. Leave the **Attached to** option set to **None**. After you create the load balancer, this IP address is attached to the load balancer's forwarding rule.

  7. Click **Reserve** to reserve the IP address.




###  gcloud 

  1. To reserve a static external IP address, use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create ADDRESS_NAME \
            --region=us-east1
         

Replace the following:

     * `ADDRESS_NAME`: the name you want to call this address.
  2. Use the [`gcloud compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result:
         
         gcloud compute addresses describe ADDRESS_NAME
         




The IP address returned is referred to as `RESERVED_IP_ADDRESS` in the following section.

## Configure the load balancer with backend buckets

This section shows you how to create the following resources for a regional external Application Load Balancer:

  * Two backend buckets. The backend buckets serve as a wrapper to the Cloud Storage buckets that you created earlier.
  * URL map
  * Target proxy
  * A forwarding rule with a regional IP addresses. The forwarding rule has an external IP address.



In this example, you can use HTTP or HTTPS as the request-and-response protocol between the client and the load balancer. To create an HTTPS load balancer, you must add an SSL certificate resource to the load balancer's frontend.

**Note:** You can only use the gcloud CLI to configure a regional external Application Load Balancer with backend buckets.

To create the aforementioned load balancing components using the gcloud CLI, follow these steps:

  1. Create two backend buckets in the `us-east1` region with the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create). The backend buckets have a load balancing scheme of `EXTERNAL_MANAGED`.
         
         gcloud compute backend-buckets create backend-bucket-cats \
             --gcs-bucket-name=BUCKET1_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --region=us-east1
         
         
         gcloud compute backend-buckets create backend-bucket-dogs \
             --gcs-bucket-name=BUCKET2_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --region=us-east1
         

Replace the variables `BUCKET1_NAME` and `BUCKET2_NAME` with your Cloud Storage bucket names.

**Note:** When creating a backend bucket for a regional external Application Load Balancer, you cannot enable Cloud CDN.
  2. Create a URL map to route incoming requests to the backend bucket with the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-backend-bucket=backend-bucket-cats \
             --region=us-east1
         

Replace the variable `URL_MAP_NAME` with the name of the URL map.

  3. Configure the host and path rules of the URL map with the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher).

In this example, the default backend bucket is `backend-bucket-cats`, which handles all the paths that exist within it. However, any request targeting `http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg` uses the `backend-bucket-dogs` backend. For example, if the `/love-to-fetch/` folder also exists within your default backend (`backend-bucket-cats`), the load balancer prioritizes the `backend-bucket-dogs` backend because there is a specific path rule for `/love-to-fetch/*`.
         
         gcloud compute url-maps add-path-matcher URL_MAP_NAME \
             --path-matcher-name=path-matcher-pets \
             --new-hosts=* \
             --backend-bucket-path-rules="/love-to-fetch/*=backend-bucket-dogs" \
             --default-backend-bucket=backend-bucket-cats
         

Replace the variable `URL_MAP_NAME` with the name of the URL map.

  4. Create a target proxy with the [`gcloud compute target-http-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create).

_For HTTP traffic_ , create a target HTTP proxy to route requests to the URL map:
         
         gcloud compute target-http-proxies create http-proxy \
             --url-map=URL_MAP_NAME \
             --region=us-east1
         

Replace the variable `URL_MAP_NAME` with the name of the URL map.

_For HTTPS traffic_ , create a target HTTPS proxy to route requests to the URL map. The proxy is the part of the load balancer that holds the SSL certificate for an HTTPS load balancer. After you create the certificate, you can attach the certificate to the HTTPS target proxy.

To attach a Certificate Manager certificate, run the following command:
         
         gcloud compute target-https-proxies create https-proxy \
             --url-map=URL_MAP_NAME \
             --certificate-manager-certificates=CERTIFICATE_NAME \
             --region=us-east1
         

Replace the following:

     * `URL_MAP_NAME`: the name of the URL map

     * `CERTIFICATE_NAME`: the name of the SSL certificate you created using Certificate Manager.

  5. Create a forwarding rule with an IP address in the `us-east1` region by using the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

_For HTTP traffic_ , create a regional forwarding rule to route incoming requests to the HTTP target proxy:
         
         gcloud compute forwarding-rules create http-fw-rule \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network=lb-network \
             --address=RESERVED_IP_ADDRESS \
             --ports=80 \
             --region=us-east1 \
             --target-http-proxy=http-proxy \
             --target-http-proxy-region=us-east1
         

_For HTTPS traffic_ , create a regional forwarding rule to route incoming requests to the HTTPS target proxy:
         
         gcloud compute forwarding-rules create https-fw-rule \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network=lb-network \
             --address=RESERVED_IP_ADDRESS \
             --ports=443 \
             --region=us-east1 \
             --target-https-proxy=https-proxy \
             --target-https-proxy-region=us-east1
         




## Send an HTTP request to the load balancer

Now that the load balancing service is running, you can send a request to the forwarding rule of the load balancer.

  1. Get the IP address of the load balancer's forwarding rule (`http-fw-rule`), which is in the `us-east1` region.
         
         gcloud compute forwarding-rules describe http-fw-rule \
               --region=us-east1
         

Copy the returned IP address to use as `FORWARDING_RULE_IP_ADDRESS` in the next step.

  2. Make an HTTP request to the virtual IP address (VIP) of the forwarding rule using curl.
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-purr/three-cats.jpg --output three-cats.jpg
         
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg --output two-dogs.jpg
         




## What's next

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
