---
url: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets/
title: Set up a cross-region internal Application Load Balancer with Cloud Storage buckets \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:25.305178+00:00
---

# Set up a cross-region internal Application Load Balancer with Cloud Storage buckets  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a cross-region internal Application Load Balancer with Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create a cross-region internal Application Load Balancer to route requests for static content to [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).

## Before you begin

Make sure that your setup meets the following prerequisites.

### Install the Google Cloud CLI

Some of the instructions in this guide can only be carried out using the Google Cloud CLI. To install it, see the document [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

You can find commands related to load balancing in the [API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis) document.

### Permissions

To follow this guide, you need to create Cloud Storage buckets and network resources in your project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)   
Add and remove firewall rules | [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`)   
Create Cloud Storage buckets | [Storage Object Admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) (`roles/storage.objectAdmin`)   
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



### Set up an SSL certificate resource

For a cross-region internal Application Load Balancer that uses HTTPS as the request-and-response protocol, create an SSL certificate resource using Certificate Manager as described in one of the following documents:

  * [Deploy a cross-region Google-managed certificate issued by your CA Service instance](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-cross-reg)
  * [Deploy a cross-region Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth-cross-reg)
  * [Deploy a cross-region self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-cross-reg)



After you create the certificate, you can attach the certificate to the HTTPS target proxy.

We recommend using a Google-managed certificate.

## Limitations

The following limitations apply to Cloud Storage buckets when serving as backends to a cross-region internal Application Load Balancer:

  * Private bucket access isn't supported, so the backend bucket must be publicly accessible over the internet.

  * [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) aren't supported.

  * Cloud CDN integration is not available when creating backend buckets for a cross-region internal Application Load Balancer.

  * When using a cross-region internal Application Load Balancer to access backend buckets, only the HTTP `GET` method is supported. You can download content from the bucket, but uploading content to the bucket through the cross-region internal Application Load Balancer isn't available.




## Setup overview

You can configure a cross-region internal Application Load Balancer in multiple regions as shown in the following diagram:

[ ![A cross-region internal Application Load Balancer sends traffic to a Cloud Storage
    backend.](https://docs.cloud.google.com/static/load-balancing/images/cross-region-internal-l7-lb-buckets.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-region-internal-l7-lb-buckets.svg) Distributing traffic to Cloud Storage (click to enlarge).

As shown in the architecture diagram, this example creates a cross-region internal Application Load Balancer in a Virtual Private Cloud (VPC) network with two backend buckets, where each backend bucket references a Cloud Storage bucket. The Cloud Storage buckets are located in the `us-east1` and `asia-east1` region.

This deployment architecture offers [high availability](https://docs.cloud.google.com/load-balancing/docs/l7-internal#ha-cross-reg-int). If the cross-region internal Application Load Balancer in a region fails, the DNS routing policies route traffic to a cross-region internal Application Load Balancer in another region.

## Configure the network and subnets

Within the VPC network, configure a subnet in each region where the forwarding rule of your load balancers is to be configured. In addition, configure a `proxy-only-subnet` in each region in which you want to configure the load balancer.

This example uses the following VPC network, region, and subnets:

  * **Network**. The network is a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnets for load balancer**. A subnet named `subnet-us` in the `us-east1` region uses `10.1.2.0/24` for its primary IP range. A subnet named `subnet-asia` in the `asia-east1` region uses `10.1.3.0/24` for its primary IP range.

  * **Subnet for Envoy proxies**. A subnet named `proxy-only-subnet-us-east1` in the `us-east1` region uses `10.129.0.0/23` for its primary IP range. A subnet named `proxy-only-subnet-asia-east1` in the `asia-east1` region uses `10.130.0.0/23` for its primary IP range.




Cross-region internal Application Load Balancers can be accessed from any region within the VPC. So clients from any region can globally access your load balancer backends.

### Configure the subnets for the load balancer's forwarding rule

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section, set the **Subnet creation mode** to **Custom**.

  5. In the **New subnet** section, enter the following information:

     * **Name** : `subnet-us`
     * Select a **Region** : `us-east1`
     * **IP address range** : `10.1.2.0/24`
  6. Click **Done**.

  7. Click **Add subnet**.

  8. Create another subnet for the load balancer's forwarding rule in a different region. In the **New subnet** section, enter the following information:

     * **Name** : `subnet-asia`
     * **Region** : `asia-east1`
     * **IP address range** : `10.1.3.0/24`
  9. Click **Done**.

  10. Click **Create**.




###  gcloud 

  1. Create a custom VPC network, named `lb-network`, with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. Create a subnet in the `lb-network` VPC network in the `us-east1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create subnet-us \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-east1
         

  3. Create a subnet in the `lb-network` VPC network in the `asia-east1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create subnet-asia \
             --network=lb-network \
             --range=10.1.3.0/24 \
             --region=asia-east1
         




### Configure the proxy-only subnets

A [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google Cloud uses to run Envoy proxies on your behalf. The proxies terminate connections from the client and create new connections to the backends.

This proxy-only subnet is used by all Envoy-based regional load balancers in the same region as the VPC network. There can only be one active proxy-only subnet for a given purpose, per region, per network. In this example, we create two proxy-only subnets—one in the `us-east1` region, and the other in the `asia-east1` region.

**Important:** Don't try to assign addresses from the proxy-only subnet to your load balancer's forwarding rule or backends. You assign the forwarding rule's IP address and the backend instance IP addresses from a different subnet range (or ranges), not this one. Google Cloud reserves this subnet range for Google Cloud-managed proxies.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that you created.

  3. On the **Subnet** tab, click **Add subnet**.

  4. Enter the following information:

     * For **Name** , enter `proxy-only-subnet-us`.
     * For **Region** , enter `us-east1`.
     * For **Purpose** , select **Cross-region Managed Proxy**.
     * For **IP address range** , enter `10.129.0.0/23`.
  5. Click **Add**.

  6. Create another proxy-only subnet in the `asia-east1` region. On the **Subnet** tab, click **Add subnet**.

  7. Enter the following information:

     * For **Name** , enter `proxy-only-subnet-asia`.
     * For **Region** , enter `asia-east1`.
     * For **Purpose** , select **Cross-region Managed Proxy**.
     * For **IP address range** , enter `10.130.0.0/23`.
  8. Click **Add**.




###  gcloud 

  1. Create a proxy-only subnet in the `us-east1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create proxy-only-subnet-us \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=us-east1 \
             --network=lb-network \
             --range=10.129.0.0/23
         

  2. Create a proxy-only subnet in the `asia-east1` region with the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create proxy-only-subnet-asia \
             --purpose=GLOBAL_MANAGED_PROXY \
             --role=ACTIVE \
             --region=asia-east1 \
             --network=lb-network \
             --range=10.130.0.0/23
         




### Configure a firewall rule

This example uses the following firewall rule:

  * An ingress rule that allows SSH access on port `22` to the client VM. In this example, this firewall rule is named `fw-allow-ssh`.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** to create the rule to allow incoming SSH connections on the client VM:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : 
       * Choose **Specified protocols and ports**.
       * Select the **TCP** checkbox, and then enter `22` for the port number.
  3. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `--source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         




## Configure your Cloud Storage buckets

The process for configuring your Cloud Storage buckets is as follows:

  * Create the buckets.
  * Copy content to the buckets.



### Create Cloud Storage buckets

In this example, you create two Cloud Storage buckets, one the in the `us-east1` region and another in the `asia-east1` region. For production deployments, we recommend that you choose a [multi-region bucket](https://docs.cloud.google.com/storage/docs/locations#location-mr), which automatically replicates objects across multiple Google Cloud regions. This can improve the availability of your content and improve failure tolerance across your application.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box**Create**.

  3. In the **Name your bucket** box, enter a globally unique name that follows the [naming guidelines](https://docs.cloud.google.com/storage/docs/buckets#naming).

  4. Click **Choose where to store your data**.

  5. Set **Location type** to **Region**.

  6. From the list of regions, select **us-east1**.

  7. Click **Create**.

  8. Click **Buckets** to return to the Cloud Storage Buckets page. Use these instructions to create a second bucket, but set the **Location** to **asia-east1**.




###  gcloud 

  1. Create the first bucket in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET1_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access
         

  2. Create the second bucket in the `asia-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET2_NAME \
             --default-storage-class=standard \
             --location=asia-east1 \
             --uniform-bucket-level-access
         




Replace the variables BUCKET1_NAME and BUCKET2_NAME with your Cloud Storage bucket names.

### Copy graphic files to your Cloud Storage buckets

To enable you to test the setup, copy a graphic file from a public Cloud Storage bucket to your own Cloud Storage buckets.

Run the following commands in Cloud Shell, replacing the bucket name variables with your unique Cloud Storage bucket names:
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET1_NAME/never-fetch/
    
    
    
    gcloud storage cp gs://gcp-external-http-lb-with-bucket/two-dogs.jpg gs://BUCKET2_NAME/love-to-fetch/
    

### Make your Cloud Storage buckets publicly readable

To make all objects in a bucket readable to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer role (`roles/storage.objectViewer`).

###  Console 

To grant all users access to view objects in your buckets, repeat the following procedure for each bucket:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab near the top of the page.

  4. In the **Permissions** section, click the person_add**Grant access** button. The **Grant access** dialog appears.

  5. In the **New principals** field, enter `allUsers`.

  6. In the **Select a role** field, enter `Storage Object Viewer` in the filter box and select the **Storage Object Viewer** from the filtered results.

  7. Click **Save**.

  8. Click **Allow public access**.




###  gcloud 

To grant all users access to view objects in your buckets, run the [`buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding).
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET1_NAME --member=allUsers --role=roles/storage.objectViewer
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET2_NAME --member=allUsers --role=roles/storage.objectViewer

Replace the bucket name variables with your unique Cloud Storage bucket names.

## Configure the load balancer with backend buckets

This section shows you how to create the following resources for a cross-region internal Application Load Balancer:

  * Two backend buckets. The backend buckets serve as a wrapper to the Cloud Storage buckets that you created earlier.
  * URL map
  * Target proxy
  * Two global forwarding rules with regional IP addresses. The forwarding rules are assigned an IP addresses from the subnets created for the load balancer's forwarding rules. If you try to assign an IP address to the forwarding rule from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets), the forwarding rule creation fails.



In this example, you can use HTTP or HTTPS as the request-and-response protocol between the client and the load balancer. To create an HTTPS load balancer, you must add an SSL certificate resource to the load balancer's frontend.

**Note:** You can only use the gcloud CLI to configure a cross-region internal Application Load Balancer with backend buckets.

To create the aforementioned load balancing components using the gcloud CLI, follow these steps:

  1. Create two backend buckets, one for each Cloud Storage bucket, with the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create#--load-balancing-scheme). The backend buckets have a load balancing scheme of `INTERNAL_MANAGED`.
         
         gcloud compute backend-buckets create backend-bucket-cats \
             --gcs-bucket-name=BUCKET1_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED
         
         
         gcloud compute backend-buckets create backend-bucket-dogs \
             --gcs-bucket-name=BUCKET2_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED
         

**Note:** When creating a backend bucket for a cross-region internal Application Load Balancer, you cannot enable Cloud CDN. In other words, Cloud CDN integration is not available when `--load-balancing-scheme=INTERNAL_MANAGED`.
  2. Create a URL map to route incoming requests to the backend bucket with the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).
         
         gcloud compute url-maps create lb-map \
             --default-backend-bucket=backend-bucket-cats \
             --global
         

  3. Configure the host and path rules of the URL map with the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher).

In this example, the default backend bucket is `backend-bucket-cats`, which handles all the paths that exist within it. However, any request targeting `http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg` uses the `backend-bucket-dogs` backend. For example, if the `/love-to-fetch/` folder also exists within your default backend (`backend-bucket-cats`), the load balancer prioritizes the `backend-bucket-dogs` backend because there is a specific path rule for `/love-to-fetch/*`.
         
         gcloud compute url-maps add-path-matcher lb-map \
             --path-matcher-name=path-matcher-pets \
             --new-hosts=* \
             --backend-bucket-path-rules="/love-to-fetch/*=backend-bucket-dogs" \
             --default-backend-bucket=backend-bucket-cats
         

  4. Create a target proxy with the [`gcloud compute target-http-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create).

**For HTTP traffic** , create a target HTTP proxy to route requests to the URL map:
         
         gcloud compute target-http-proxies create http-proxy \
             --url-map=lb-map \
             --global
         

**For HTTPS traffic** , create a target HTTPS proxy to route requests to the URL map. The proxy is the part of the load balancer that holds the SSL certificate for an HTTPS load balancer. After you create the certificate, you can attach the certificate to the HTTPS target proxy.
         
         gcloud compute target-https-proxies create https-proxy \
             --url-map=lb-map \
             --certificate-manager-certificates=CERTIFICATE_NAME \
             --global
         

Replace `CERTIFICATE_NAME` with the name of the SSL certificate you created using Certificate Manager.

  5. Create two global forwarding rules, one with an IP address in the `us-east1` region and another with an IP address in the `asia-east1` region with the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

If you want to reserve a static internal IP address for your load balancer's forwarding rule, see [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address). Reserving an IP address is optional for an HTTP forwarding rule; however, you need to reserve an IP address for an HTTPS forwarding rule.

In this example, an ephemeral IP address is associated with your load balancer's HTTP forwarding rule. An ephemeral IP address remains constant while the forwarding rule exists. If you need to delete the forwarding rule and recreate it, the forwarding rule might receive a new IP address.

**For HTTP traffic** , create the global forwarding rules to route incoming requests to the HTTP target proxy:
         
         gcloud compute forwarding-rules create http-fw-rule-1 \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=subnet-us \
             --subnet-region=us-east1 \
             --ports=80 \
             --target-http-proxy=http-proxy \
             --global-target-http-proxy \
             --global
         
         
         gcloud compute forwarding-rules create http-fw-rule-2 \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=subnet-asia \
             --subnet-region=asia-east1 \
             --ports=80 \
             --target-http-proxy=http-proxy \
             --global-target-http-proxy \
             --global
         

**For HTTPS traffic** , create the global forwarding rules to route incoming requests to the HTTPS target proxy:
         
         gcloud compute forwarding-rules create https-fw-rule-1 \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=subnet-us \
             --subnet-region=us-east1 \
             --address=RESERVED_IP_ADDRESS \
             --ports=443 \
             --target-https-proxy=https-proxy \
             --global-target-https-proxy \
             --global
         
         
         gcloud compute forwarding-rules create https-fw-rule-2 \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=subnet-asia \
             --subnet-region=asia-east1 \
             --address=RESERVED_IP_ADDRESS \
             --ports=443 \
             --target-https-proxy=https-proxy \
             --global-target-https-proxy \
             --global
         




## Send an HTTP request to the load balancer

Send a request from an internal client VM to the forwarding rule of the load balancer.

### Get the IP address of the load balancer's forwarding rule

  1. Get the IP address of the load balancer's forwarding rule (`http-fw-rule-1`), which is in the `us-east1` region.
         
         gcloud compute forwarding-rules describe http-fw-rule-1 \
             --global
         

  2. Get the IP address of the load balancer's forwarding rule (`http-fw-rule-2`), which is in the `asia-east1` region.
         
         gcloud compute forwarding-rules describe http-fw-rule-2 \
             --global
         




### Create a client VM to test connectivity

  1. Create a client VM in the `us-east1` region.
         
         gcloud compute instances create client-a \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --network=lb-network \
             --subnet=subnet-us \
             --zone=us-east1-c \
             --tags=allow-ssh
         

  2. Establish an SSH connection to the client VM.
         
         gcloud compute ssh client-a --zone=us-east1-c
         

  3. In this example, the cross-region internal Application Load Balancer has frontend virtual IP addresses (VIP) in both the `us-east1` and `asia-east1` regions in the VPC network. Make an HTTP request to the VIP in either region by using curl.
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg --output two-dogs.jpg
         
         
         curl http://FORWARDING_RULE_IP_ADDRESS/never-fetch/three-cats.jpg --output three-cats.jpg
         




### Test high availability

  1. Delete the forwarding rule (`http-fw-rule-1`) in the `us-east1` region to simulate regional outage and check whether the client in the `us-east` region can still access data from the backend bucket.
         
         gcloud compute forwarding-rules delete http-fw-rule-1 \
             --global
         

  2. Make an HTTP request to the VIP of the forwarding rule in either region by using curl.
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg --output two-dogs.jpg
         
         
         curl http://FORWARDING_RULE_IP_ADDRESS/never-fetch/three-cats.jpg --output three-cats.jpg
         

If you make an HTTP request to the VIP in the `us-east1` region, the DNS routing policies detect that this VIP isn't responding, and return the next most optimal VIP to the client (in this example, `asia-east1`). This behavior helps ensure that your application stays up even during regional outages.




## What's next

  * [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
