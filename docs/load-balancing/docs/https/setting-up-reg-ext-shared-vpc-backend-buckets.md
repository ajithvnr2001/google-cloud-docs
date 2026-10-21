---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets/
title: Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:23.957222+00:00
---

# Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you two sample configurations for setting up a regional external Application Load Balancer in a Shared VPC environment with Cloud Storage buckets:

  * The first example creates all of the load balancer components and backends in one service project.
  * The second example creates the load balancer's frontend components and URL map in one service project, while the load balancer's backend bucket and Cloud Storage buckets are created in a different service project.



Both examples require the same initial configuration to grant required roles and set up a Shared VPC before you can start creating load balancers.

Apart from the aforementioned example configurations in this document, you can also set up a Shared VPC deployment where the load balancer's frontend and URL map are created in the host project and the backend buckets, along with the Cloud Storage buckets, are created in a service project. For more information on other valid Shared VPC architectures, see [Shared VPC architectures](https://docs.cloud.google.com/load-balancing/docs/https#shared-vpc).

If you don't want to use a Shared VPC network, see [Set up a regional external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets).

## Before you begin

Make sure that your setup meets the following prerequisites.

### Create Google Cloud projects

Create [Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) for one host and two service projects.

### Required roles

To get the permissions that you need to set up a regional external Application Load Balancer in a Shared VPC environment with Cloud Storage buckets, ask your administrator to grant you the following IAM roles: 

  * To set up Shared VPC: [Compute Shared VPC Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.xpnAdmin) (`roles/compute.xpnAdmin`) on the host project 
  * To provide access to a service project administrator to use the Shared VPC network: [Compute Network User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) on the host project 
  * To create Cloud Storage buckets: [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the service project 
  * To create the load balancing resources: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on the service project 
  * To create Compute Engine instances: [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the service project 
  * To create and modify Compute Engine SSL certificates: [Compute Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`) on the service project 
  * To create and modify Certificate Manager SSL certificates: [Certificate Manager Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.owner) (`roles/certificatemanager.owner`) on the service project 
  * To reference backend buckets in other service projects: [Compute Load Balancer Services User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerServiceUser) (`roles/compute.loadBalancerServiceUser`) on the service project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up a Shared VPC environment

Complete the following steps in the _host project_ to set up a Shared VPC environment:

  1. Configure a custom mode VPC network.
  2. Configure a proxy-only subnet.
  3. Set up a Shared VPC in the host project.



The steps in this section don't need to be performed every time you want to create a new load balancer. However, you must ensure that you have access to the resources described here before you proceed to creating the load balancer.

**Note:** For this setup, you don't need a subnet for the forwarding rule or the Cloud Storage bucket. 

  * Regional external IPv4 addresses always exist outside of VPC networks. For more information, see [Forwarding rules and VPC networks](https://docs.cloud.google.com/load-balancing/docs/https#fw-rule-network)
  * A Cloud Storage bucket isn't associated with any VPC network.



This example uses the following VPC network, region, and proxy-only subnet:

  * **Network**. The network is a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

  * **Subnet for Envoy proxies**. A subnet named `proxy-only-subnet-us` in the `us-east1` region uses `10.129.0.0/23` for its primary IP range.




#### Configure a custom mode VPC network

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. Click **Create**.




###  gcloud 

  1. Create a custom VPC network, named `lb-network`, with the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create lb-network \
               --subnet-mode=custom \
               --project=HOST_PROJECT_ID
         

Replace `HOST_PROJECT_ID` with the Google Cloud project ID assigned to the project that is enabled as a host project in a Shared VPC environment.




#### Configure a proxy-only subnet

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
             --range=10.129.0.0/23 \
             --project=HOST_PROJECT_ID
         

Replace `HOST_PROJECT_ID` with the Google Cloud project ID assigned to the host project.




#### Set up a Shared VPC in the host project

You can enable a Shared VPC host project and attach service projects to the host project so that the service projects can use the Shared VPC network. To set up a Shared VPC in the host project, see the following pages:

  * [Enable a host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host).
  * [Attach a service project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).



After completing the preceding steps, you can pursue either of the following setups:

  * Configure a load balancer in the service project
  * Configure a load balancer with a cross-project configuration



## Configure a load balancer in the service project

This example creates a regional external Application Load Balancer where all the load balancing components (forwarding rule, target proxy, URL map, and backend bucket) and Cloud Storage buckets are created in the service project.

The regional external Application Load Balancer's networking resources such as the proxy-only subnet is created in the host project.

[ ![Figure 1. Regional external HTTP\(S\) load balancer in a
    Shared VPC environment with Cloud Storage buckets](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-https-lb-shared-vpc-example.svg)](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-https-lb-shared-vpc-example.svg) **Figure 1.** Regional external Application Load Balancer in a Shared VPC environment with Cloud Storage buckets

This section shows you how to set up the load balancer and backends.

The example setups on this page explicitly configure a reserved IP address for the regional external Application Load Balancer's forwarding rule, rather than allowing an ephemeral IP address to be allocated. As a best practice, we recommend reserving IP addresses for forwarding rules.

### Configure your Cloud Storage buckets

The process for configuring your Cloud Storage buckets is as follows:

  1. Create the Cloud Storage buckets.
  2. Copy content to the Cloud Storage buckets.
  3. Make the Cloud Storage buckets publicly accessible.



#### Create the Cloud Storage buckets

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
             --uniform-bucket-level-access \
             --project=SERVICE_PROJECT_ID
         

  2. Create the second bucket also in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET2_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access \
             --project=SERVICE_PROJECT_ID
         




Replace the following:

  * `BUCKET1_NAME` and `BUCKET2_NAME`: the name of your Cloud Storage buckets
  * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project



#### Copy content to the Cloud Storage buckets

To populate the Cloud Storage buckets, copy a graphic file from a public Cloud Storage bucket to your own Cloud Storage buckets.
    
    
      gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET1_NAME/love-to-purr/
      
    
    
      gcloud storage cp gs://gcp-external-http-lb-with-bucket/two-dogs.jpg gs://BUCKET2_NAME/love-to-fetch/
      

Replace `BUCKET1_NAME` and `BUCKET2_NAME` with the name of your Cloud Storage buckets.

#### Make the Cloud Storage buckets publicly accessible

To make all objects in a bucket accessible to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer role (`roles/storage.objectViewer`).

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
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET1_NAME --member=allUsers --role=roles/storage.objectViewer
    
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET2_NAME --member=allUsers --role=roles/storage.objectViewer
    

Replace `BUCKET1_NAME` and `BUCKET2_NAME` with the name of your Cloud Storage buckets.

### Reserve the load balancer's IP address

Reserve a static external IP address for the forwarding rule of the load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Reserve a static address** page.

[Go to Reserve a static address](https://console.cloud.google.com/networking/addresses/add)

  2. For **Name** , enter a name for the new address.

  3. For **IP version** , select **IPv4**.

  4. For **Type** , select **Regional**.

  5. For **Region** , select **us-east1**.

  6. Leave the **Attached to** option set to **None**. After you create the load balancer, this IP address will be attached to the load balancer's forwarding rule.

  7. Click **Reserve** to reserve the IP address.




###  gcloud 

  1. To reserve a static external IP address using `gcloud compute`, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create ADDRESS_NAME  \
              --region=us-east1 \
              --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `ADDRESS_NAME`: the name that you want to assign to this IP address.
     * `REGION`: the region where you want to reserve this address. This region should be the same region as the load balancer.
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project.
  2. Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result:
         
         gcloud compute addresses describe ADDRESS_NAME
         

Replace `ADDRESS_NAME` with the name that you have assigned to the IP address.

The IP address returned is referred to as `RESERVED_IP_ADDRESS` in the subsequent sections.




### Set up an SSL certificate resource

For a regional external Application Load Balancer that uses HTTPS as the request-and-response protocol, you can create an SSL certificate resource using either a Compute Engine SSL certificate or Certificate Manager certificate.

For this example, create an SSL certificate resource using Certificate Manager as described in one of the following documents:

  * [Deploy a regional Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-regional)
  * [Deploy a regional Google-managed certificate with CA Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas-regional)
  * [Deploy a regional self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed-regional)



After you create the certificate, you can attach the certificate to the HTTPS target proxy.

We recommend using a Google-managed certificate.

### Configure the load balancer with backend buckets

This section shows you how to create the following resources for a regional external Application Load Balancer:

  * Two backend buckets. The backend buckets serve as a wrapper to the Cloud Storage buckets that you created earlier.
  * URL map
  * Target proxy
  * A forwarding rule with a regional IP addresses. The forwarding rule has an external IP address.



In this example, you can use HTTP or HTTPS as the request-and-response protocol between the client and the load balancer. To create an HTTPS load balancer, you must add an SSL certificate resource to the load balancer's frontend.

**Note:** You can only use the gcloud CLI to configure a regional external Application Load Balancer with backend buckets.

To create the aforementioned load balancing components using the gcloud CLI, follow these steps:

  1. Create two backend buckets with the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create#--load-balancing-scheme). The backend buckets have a load balancing scheme of `EXTERNAL_MANAGED`.
         
         gcloud compute backend-buckets create backend-bucket-cats \
               --gcs-bucket-name=BUCKET1_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --region=us-east1 \
               --project=SERVICE_PROJECT_ID
         
         
         gcloud compute backend-buckets create backend-bucket-dogs \
               --gcs-bucket-name=BUCKET2_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --region=us-east1 \
               --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `BUCKET1_NAME` and `BUCKET2_NAME`: the name of the Cloud Storage buckets
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project
  2. Create a URL map to route incoming requests to the backend bucket with the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).
         
         gcloud compute url-maps create URL_MAP_NAME \
               --default-backend-bucket=backend-bucket-cats \
               --region=us-east1 \
               --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project
  3. Configure the host and path rules of the URL map with the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher).

In this example, the default backend bucket is `backend-bucket-cats`, which handles all the paths that exist within it. However, any request targeting `http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg` uses the `backend-bucket-dogs` backend. For example, if the `/love-to-fetch/` folder also exists within your default backend (`backend-bucket-cats`), the load balancer prioritizes the `backend-bucket-dogs` backend because there is a specific path rule for `/love-to-fetch/*`.
         
         gcloud compute url-maps add-path-matcher URL_MAP_NAME \
               --path-matcher-name=path-matcher-pets \
               --new-hosts=* \
               --backend-bucket-path-rules="/love-to-fetch/*=backend-bucket-dogs" \
               --default-backend-bucket=backend-bucket-cats \
               --region=us-east1 \
               --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project
  4. Create a target proxy with the [`gcloud compute target-http-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create).

_For HTTP traffic_ , create a target HTTP proxy to route requests to the URL map:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
               --url-map=URL_MAP_NAME \
               --region=us-east1 \
               --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy
     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project

_For HTTPS traffic_ , create a target HTTPS proxy to route requests to the URL map. The proxy is the part of the load balancer that holds the SSL certificate for an HTTPS load balancer. After you create the certificate, you can attach the certificate to the HTTPS target proxy.

To attach a Certificate Manager certificate, run the following command:
    
    gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
          --url-map=URL_MAP_NAME \
          --certificate-manager-certificates=CERTIFICATE_NAME \
          --region=us-east1 \
          --project=SERVICE_PROJECT_ID
    

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy
     * `URL_MAP_NAME`: the name of the URL map
     * `CERTIFICATE_NAME`: the name of the Certificate Manager SSL certificate
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project
  5. Create a forwarding rule with an IP address in the `us-east1` region with the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

_For HTTP traffic_ , create a regional forwarding rule to route incoming requests to the HTTP target proxy:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --network=projects/HOST_PROJECT_ID/global/networks/lb-network \
               --address=RESERVED_IP_ADDRESS \
               --ports=80 \
               --region=us-east1 \
               --target-http-proxy=TARGET_HTTP_PROXY_NAME \
               --target-http-proxy-region=us-east1 \
               --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `HOST_PROJECT_ID`: the Google Cloud project ID assigned to the host project
     * `RESERVED_IP_ADDRESS`: the reserved IP address
     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project

_For HTTPS traffic_ , create a regional forwarding rule to route incoming requests to the HTTPS target proxy:
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
          --load-balancing-scheme=EXTERNAL_MANAGED \
          --network=projects/HOST_PROJECT_ID/global/networks/lb-network \
          --address=RESERVED_IP_ADDRESS \
          --ports=443 \
          --region=us-east1 \
          --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
          --target-https-proxy-region=us-east1 \
          --project=SERVICE_PROJECT_ID
    

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `HOST_PROJECT_ID`: the Google Cloud project ID assigned to the host project
     * `RESERVED_IP_ADDRESS`: the reserved IP address
     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project



### Send an HTTP request to the load balancer

Now that the load balancing service is running, you can send traffic to the forwarding rule of the load balancer.

  1. Get the IP address of the load balancer's forwarding rule, which is in the `us-east1` region.
         
         gcloud compute forwarding-rules describe FORWARDING_RULE_NAME \
              --region=us-east1 \
              --project=SERVICE_PROJECT_ID
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project

Copy the returned IP address to use as `FORWARDING_RULE_IP_ADDRESS` in the next step.

  2. Make an HTTP request to the virtual IP address (VIP) of the forwarding rule using curl.
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-purr/three-cats.jpg --output three-cats.jpg
         
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg --output two-dogs.jpg
         

Replace `FORWARDING_RULE_IP_ADDRESS` with the IP address of the load balancer's forwarding rule.




## Configure a load balancer with a cross-project configuration

The previous example on this page shows you how to set up a Shared VPC deployment where all the load balancer components and its backends are created in the service project.

Regional external Application Load Balancers also let you configure Shared VPC deployments where a URL map in one host or service project can reference backend buckets located across multiple service projects in Shared VPC environments.

You can use the steps in this section as a reference to configure any of the supported combinations listed here:

  * Forwarding rule, target proxy, and URL map in the host project, and backend bucket in a service project
  * Forwarding rule, target proxy, and URL map in a service project, and backend bucket in another service project



In this section, the latter configuration is outlined as an example.

### Setup overview

This example configures a load balancer with its frontend and backend in two different service projects.

If you haven't already done so, you must configure the required roles and set up a Shared VPC environment. For instructions, see the following sections at the start of this page:

  * Configure the required roles
  * Set up a Shared VPC environment

[ ![Figure 2. Load balancer frontend and backend in different service projects](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-https-lb-shared-vpc-example-cross-project.svg)](https://docs.cloud.google.com/static/load-balancing/images/regional-ext-https-lb-shared-vpc-example-cross-project.svg) **Figure 2.** Load balancer frontend and backend in different service projects

### Configure the Cloud Storage buckets and backend buckets in service project B

_All the steps in this section must be performed in service project B_.

The process for configuring Cloud Storage buckets and backend buckets is as follows:

  1. Create the Cloud Storage buckets.
  2. Copy content to the Cloud Storage buckets.
  3. Make the Cloud Storage buckets publicly accessible.
  4. Create backend buckets and point it to the Cloud Storage buckets.



#### Create the Cloud Storage buckets

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
             --uniform-bucket-level-access \
             --project=SERVICE_PROJECT_B_ID
         

  2. Create the second bucket also in the `us-east1` region with the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create).
         
         gcloud storage buckets create gs://BUCKET2_NAME \
             --default-storage-class=standard \
             --location=us-east1 \
             --uniform-bucket-level-access \
             --project=SERVICE_PROJECT_B_ID
         




Replace the following:

  * `BUCKET1_NAME` and `BUCKET2_NAME`: the name of your Cloud Storage bucket
  * `SERVICE_PROJECT_B_ID`: the Google Cloud project ID assigned to the service project B



#### Copy content to the Cloud Storage buckets

To populate the Cloud Storage buckets, copy a graphic file from a public Cloud Storage bucket to your own Cloud Storage buckets.
    
    
        gcloud storage cp gs://gcp-external-http-lb-with-bucket/three-cats.jpg gs://BUCKET1_NAME/love-to-purr/
      
    
    
        gcloud storage cp gs://gcp-external-http-lb-with-bucket/two-dogs.jpg gs://BUCKET2_NAME/love-to-fetch/
      

Replace `BUCKET1_NAME` and `BUCKET2_NAME` with the name of your Cloud Storage buckets.

#### Make the Cloud Storage buckets publicly accessible

To make all objects in a bucket accessible to everyone on the public internet, grant the principal `allUsers` the Storage Object Viewer role (`roles/storage.objectViewer`).

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
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET1_NAME --member=allUsers --role=roles/storage.objectViewer
    
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET2_NAME --member=allUsers --role=roles/storage.objectViewer
    

Replace `BUCKET1_NAME` and `BUCKET2_NAME` with the name of your Cloud Storage buckets.

#### Create backend buckets and point it to the Cloud Storage buckets

To create the backend buckets, follow these steps:

  1. Create two backend buckets with the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create#--load-balancing-scheme). The backend buckets have a load balancing scheme of `EXTERNAL_MANAGED`.
         
         gcloud compute backend-buckets create backend-bucket-cats \
               --gcs-bucket-name=BUCKET1_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --region=us-east1 \
               --project=SERVICE_PROJECT_B_ID
         
         
         gcloud compute backend-buckets create backend-bucket-dogs \
               --gcs-bucket-name=BUCKET2_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --region=us-east1 \
               --project=SERVICE_PROJECT_B_ID
         

Replace the following:

     * `BUCKET1_NAME` and `BUCKET2_NAME`: the name of the Cloud Storage buckets
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project



### Configure the load balancer frontend components in service project A

_All the steps in this section must be performed in service project A_.

In service project A, you need to create the following frontend load balancing components:

  1. An SSL certificate resource that is attached to the target proxy. You can follow the steps outlined in the earlier section to create the SSL certificate.
  2. An IP address for the forwarding rule of the load balancer. You can follow the steps outlined in the earlier section to create an IP address.
  3. A URL map that references the backend buckets in service project B
  4. A target proxy
  5. A forwarding rule with a regional IP addresses. The forwarding rule has an external IP address.



To create the URL map, target proxy, and forwarding rule do the following:

  1. Create a URL map to route incoming requests to the backend bucket with the [`gcloud compute url-maps create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).
         
         gcloud compute url-maps create URL_MAP_NAME \
               --default-backend-bucket=backend-bucket-cats \
               --region=us-east1 \
               --project=SERVICE_PROJECT_A_ID
         

Replace the following:

     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A
  2. Configure the host and path rules of the URL map with the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher).

In this example, the default backend bucket is `backend-bucket-cats`, which handles all the paths that exist within it. However, any request targeting `http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg` uses the `backend-bucket-dogs` backend. For example, if the `/love-to-fetch/` folder also exists within your default backend (`backend-bucket-cats`), the load balancer prioritizes the `backend-bucket-dogs` backend because there is a specific path rule for `/love-to-fetch/*`.
         
         gcloud compute url-maps add-path-matcher URL_MAP_NAME \
               --path-matcher-name=path-matcher-pets \
               --new-hosts=* \
               --backend-bucket-path-rules="/love-to-fetch/*=projects/SERVICE_PROJECT_B_ID/regional/backendBuckets/backend-bucket-dogs" \
               --default-backend-bucket=projects/SERVICE_PROJECT_B_ID/regional/backendBuckets/backend-bucket-cats \
               --region=us-east1 \
               --project=SERVICE_PROJECT_A_ID
         

Replace the following:

     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A
  3. Create a target proxy with the [`gcloud compute target-http-proxies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create).

_For HTTP traffic_ , create a target HTTP proxy to route requests to the URL map:
         
         gcloud compute target-http-proxies create TARGET_HTTP_PROXY_NAME \
               --url-map=URL_MAP_NAME \
               --region=us-east1 \
               --project=SERVICE_PROJECT_A_ID
         

Replace the following:

     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy
     * `URL_MAP_NAME`: the name of the URL map
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A

_For HTTPS traffic_ , create a target HTTPS proxy to route requests to the URL map. The proxy is the part of the load balancer that holds the SSL certificate for an HTTPS load balancer. After you create the certificate, you can attach the certificate to the HTTPS target proxy.

To attach a Certificate Manager certificate, run the following command:
    
    gcloud compute target-https-proxies create TARGET_HTTPS_PROXY_NAME \
          --url-map=lb-map \
          --certificate-manager-certificates=CERTIFICATE_NAME \
          --region=us-east1 \
          --project=SERVICE_PROJECT_A_ID
    

Replace the following:

     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy
     * `URL_MAP_NAME`: the name of the URL map
     * `CERTIFICATE_NAME`: the name of the Certificate Manager SSL certificate
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A
  4. Create a forwarding rule with an IP address in the `asia-east1` region with the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).

_For HTTP traffic_ , create a regional forwarding rule to route incoming requests to the HTTP target proxy:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --network=projects/HOST_PROJECT_ID/global/networks/lb-network \
               --address=RESERVED_IP_ADDRESS \
               --ports=80 \
               --region=us-east1 \
               --target-http-proxy=TARGET_HTTP_PROXY_NAME \
               --target-http-proxy-region=us-east1 \
               --project=SERVICE_PROJECT_A_ID
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `HOST_PROJECT_ID`: the Google Cloud project ID assigned to the host project
     * `RESERVED_IP_ADDRESS`: the reserved IP address
     * `TARGET_HTTP_PROXY_NAME`: the name of the target HTTP proxy
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A

_For HTTPS traffic_ , create a regional forwarding rule to route incoming requests to the HTTPS target proxy:
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
          --load-balancing-scheme=EXTERNAL_MANAGED \
          --network=projects/HOST_PROJECT_ID/global/networks/lb-network \
          --address=RESERVED_IP_ADDRESS \
          --ports=443 \
          --region=us-east1 \
          --target-https-proxy=TARGET_HTTPS_PROXY_NAME \
          --target-https-proxy-region=us-east1 \
          --project=SERVICE_PROJECT_A_ID
    

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `HOST_PROJECT_ID`: the Google Cloud project ID assigned to the host project
     * `RESERVED_IP_ADDRESS`: the reserved IP address
     * `TARGET_HTTPS_PROXY_NAME`: the name of the target HTTPS proxy
     * `SERVICE_PROJECT_A_ID`: the Google Cloud project ID assigned to the service project A



### Grant permission to the Compute Load Balancer Admin to use the backend bucket in the service project

If you want load balancers to reference backend buckets in other service projects, the load balancer administrator must have the `compute.backendBuckets.use` permission. To grant this permission, you can use the predefined IAM role called Compute Load Balancer Services User (`roles/compute.loadBalancerServiceUser`). This role must be granted by the Service Project Admin and can be applied at the service project level or at the individual backend bucket level.

In this example, a Service Project Admin from service project B must run _one_ of the following commands to grant the `compute.backendBuckets.use` permission to a Load Balancer Admin from service project A. This can be done either at the project level (for all backend buckets in the project) or per backend bucket.

###  Console 

#### Project-level permissions

Use the following steps to grant permissions to all backend buckets in your project.

You require the `compute.regionBackendBuckets.setIamPolicy` and the `resourcemanager.projects.setIamPolicy` permissions to complete this step. 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview)

  2. Select your project.

  3. Click person_add**Grant access**.

  4. In the **New principals** field, enter the principal's email address or other identifier.

  5. In the **Assign roles** section, click **Add roles**.

  6. In the **Select roles** dialog, in the **Search for roles** field, enter `Compute Load Balancer Services User`.

  7. Select the **Compute Load Balancer Services User** checkbox.

  8. Click **Apply**.

  9. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  10. Click **Save**.




#### Resource-level permissions for individual backend buckets

Use the following steps to grant permissions to individual backend buckets in your project.

You require the `compute.regionBackendBuckets.setIamPolicy` permission to complete this step. 

  1. In the Google Cloud console, go to the **Backends** page.

[Go to Backends](https://console.cloud.google.com/loadbalancing/list/backends)

  2. From the backends list, select the backend bucket that you want to grant access to and click person_add**Permissions**.

  3. Click person_add**Add principal**.

  4. In the **New principals** field, enter the principal's email address or other identifier.

  5. In the **Select a role** list, select **Compute Load Balancer Services User**.

  6. Click **Save**.




###  gcloud 

#### Project-level permissions

Use the following steps to grant permissions to all backend buckets in your project.

You require the `compute.regionBackendBuckets.setIamPolicy` and the `resourcemanager.projects.setIamPolicy` permissions to complete this step. 
    
    
      gcloud projects add-iam-policy-binding SERVICE_PROJECT_B_ID \
          --member="user:LOAD_BALANCER_ADMIN" \
          --role="roles/compute.loadBalancerServiceUser"
    

Replace the following:

  * `SERVICE_PROJECT_B_ID`: the Google Cloud project ID assigned to the service project B
  * `LOAD_BALANCER_ADMIN`: the [principal](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding#--member) to add the binding for



#### Resource-level permissions for individual backend buckets

At the backend bucket level, Service Project Admins can use _either of the following commands_ to grant the Compute Load Balancer Services User role (`roles/compute.loadBalancerServiceUser`):

  * [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)
  * [`gcloud compute backend-buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/add-iam-policy-binding)



Use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to grant the Compute Load Balancer Services User role.

You require the `compute.regionBackendBuckets.setIamPolicy` permission to complete this step.
    
    
      gcloud projects add-iam-policy-binding SERVICE_PROJECT_B_ID \
          --member="user:LOAD_BALANCER_ADMIN" \
          --role="roles/compute.loadBalancerServiceUser" \
          --condition='expression=resource.name=="projects/SERVICE_PROJECT_B_ID/regions/REGION/backendBuckets/BACKEND_BUCKET_NAME",title=Shared VPC condition'
    

Replace the following: 

  * `SERVICE_PROJECT_B_ID`: the Google Cloud project ID assigned to the service project B
  * `LOAD_BALANCER_ADMIN`: the [principal](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding#--member) to add the binding for
  * `REGION`: the Google Cloud region where the backend bucket is located
  * `BACKEND_BUCKET_NAME`: the name of the backend bucket

Alternatively, use the [ `gcloud compute backend-buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/add-iam-policy-binding) to grant the Compute Load Balancer Services User role. 
    
    
      gcloud compute backend-buckets add-iam-policy-binding BACKEND_BUCKET_NAME \
          --member="user:LOAD_BALANCER_ADMIN" \
          --role="roles/compute.loadBalancerServiceUser" \
          --project=SERVICE_PROJECT_B_ID \
          --region=REGION
    

### Send an HTTP request to the load balancer

Now that the load balancing service is running, you can send traffic to the forwarding rule of the load balancer.

  1. Get the IP address of the load balancer's forwarding rule, which is in the `us-east1` region.
         
         gcloud compute forwarding-rules describe FORWARDING_RULE_NAME \
              --region=us-east1 \
              --project=SERVICE_PROJECT_A_ID
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule
     * `SERVICE_PROJECT_ID`: the Google Cloud project ID assigned to the service project

Copy the returned IP address to use as `FORWARDING_RULE_IP_ADDRESS` in the next step.

  2. Make an HTTP request to the VIP of the forwarding rule using curl.
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-purr/three-cats.jpg --output three-cats.jpg
         
         
         curl http://FORWARDING_RULE_IP_ADDRESS/love-to-fetch/two-dogs.jpg --output two-dogs.jpg
         

Replace `FORWARDING_RULE_IP_ADDRESS` with the IP address of the load balancer's forwarding rule.




## What's next

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets)
  * [Manage certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
