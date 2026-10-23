---
url: https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends/
title: Create a Private Service Connect backend \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:36.319080+00:00
---

# Create a Private Service Connect backend  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Private Service Connect backend

You can use Private Service Connect backends to connect to supported services by using a load balancer for policy enforcement. You connect to the service through a forwarding rule that is mapped to a backend that contains a Private Service Connect network endpoint group (NEG).

For more information about supported services and configurations, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

This guide shows you how to add a Private Service Connect NEG to a load balancer to access either Google APIs or a published service. This guide does not include the full load balancer configuration.

For instructions that include creating a load balancer with a Private Service Connect backend, see the following:

  * [Create an internal Application Load Balancer to access Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls)
  * [Create a global external Application Load Balancer to access a published service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls)



## Roles

The [Compute Load Balancer Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) contains the permission required to perform the tasks described in this guide.

## Before you begin

  1. Determine which service you want to connect to:

     * For published services:

       * If you want to publish your own service, see [Publish managed services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

       * If you are connecting to a Google Cloud or third-party published service, ask the producer for the following information:

         * The URI of the service attachment for the service that you want to connect to.

         * Optionally, which port the service uses. If you know which port is used, you can specify it as part of the Private Service Connect NEG configuration.

         * Any requirements for what DNS names you use to send requests to. You might need to use specific DNS names in your URL map configuration.

     * For Google APIs, do one of the following:

       * Choose a [regional service endpoint](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).
       * Choose a [multi-regional service endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#multiregional-google-apis).
       * Choose a [global service endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis).
  2. Determine which load balancer type supports the service that you want to connect to and make sure that you are familiar with the load balancer that you are updating. This guide describes how to add a Private Service Connect NEG to a load balancer, but you might want to perform additional configuration steps.

For more information, see [Supported load balancers and targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#supported-lb-targets).




## Create a Private Service Connect NEG

When you create a NEG, you choose which type of target it connects to:

  * A published service
  * A regional endpoint for a Google API
  * A multi-regional endpoint for a Google API
  * A global Google API



### Create a NEG to connect to a published service

When you create a Private Service Connect NEG that points to a published service, you need the service attachment URI for the service. The service attachment has this format: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

The service producer might also provide a port to use for this service. If they do, make sure that you include the producer port in the NEG configuration.

For information about supported load balancers for this configuration, see [Published service targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#published-services).

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/add)  


  2. Click **Create network endpoint group**.

  3. Enter a name for the network endpoint group.

  4. For the **Network endpoint group type** , select **Private Service Connect NEG (Regional)**.

  5. Configure the target:

     1. For **Target** , select **Published service**.
     2. For **Target service** , enter the URI of the service attachment.
     3. Optional: For **Producer port** , enter the port that the producer has provided to you. If omitted, the port is automatically assigned.
     4. Select the **Network** and **Subnetwork** to create the network endpoint group in.

The subnet must be in the same region as the published service.

  6. Click **Create**.




###  gcloud 

Use the `gcloud compute network-endpoint-groups create` command:
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION \
        --network=NETWORK \
        --subnet=SUBNET
    

If you know [which port is being used by the producer](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#producer-ports), you can specify the port with `--producer-port=PORT`.

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the URI of the service attachment.

  * `REGION`: the region to create the network endpoint group in. The region must be the same region as the target service.

  * `NETWORK`: the network to create the network endpoint group in. If omitted, the default network is used.

  * `SUBNET`: the subnet to create the network endpoint group in. The subnet must be in the same region as the target service. A subnet must be provided if you provide the network. If both network and subnet are omitted, the default network is used, and the default subnet in the specified `REGION` is used.

  * `PORT`: the port that the producer is using for the service.




### Create a NEG to connect to a regional Google API

You can create a NEG to connect to a regional Google API.

For information about supported load balancers for this configuration, see [Regional Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#google-apis).

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/add)  


  2. Click **Create network endpoint group**.

  3. Enter a name for the network endpoint group.

  4. For the **Network endpoint group type** , select **Private Service Connect NEG (Regional)**.

  5. Configure the target:

     1. For **Target** , select **Google APIs**.
     2. Select a **Region** and the **Target service**.
  6. Click **Create**.




###  gcloud 

Use the `gcloud compute network-endpoint-groups create` command:
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the [regional service endpoint](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) that you want to connect to.

  * `REGION`: the region to create the network endpoint group in. The region must be the same region as the target service.




### Create a NEG to connect to a multi-regional Google API

You can create a Private Service Connect NEG to connect to a multi-regional Google API.

For information about supported load balancers for this configuration, see [Multi-regional API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#multiregional-google-apis).

###  gcloud 

Use the `gcloud compute network-endpoint-groups create` command:
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the [multi-regional Google API](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints) that you want to connect to.

  * `REGION`: the region to create the network endpoint group in.




### Create a NEG to connect to a global Google API

You can create a Private Service Connect NEG to connect to a global Google API. NEGs are regional, even when they are connecting to global APIs. In this configuration, the region is ignored.

For information about supported load balancers for this configuration, see [Global Google API targets](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis).

For complete instructions about creating a cross-region internal Application Load Balancer and a Private Service Connect NEG to access global Google APIs, see [Access global Google APIs](https://docs.cloud.google.com/vpc/docs/access-global-google-apis-backends).

###  Console 

  1. In the Google Cloud console, go to the **Network endpoint groups** page.

[Go to Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/add)  


  2. Click **Create network endpoint group**.

  3. Enter a name for the network endpoint group.

  4. For the **Network endpoint group type** , select **Private Service Connect NEG (Regional)**.

  5. Configure the target:

     1. For **Target** , select **Global Google APIs**.
     2. Select a **Region** and a **Target service**.
  6. Click **Create**.




###  gcloud 

Use the `gcloud compute network-endpoint-groups create` command:
    
    
    gcloud compute network-endpoint-groups create NEG_NAME \
        --network-endpoint-type=private-service-connect \
        --psc-target-service=TARGET_SERVICE \
        --region=REGION
    

Replace the following:

  * `NEG_NAME`: a name for the network endpoint group.

  * `TARGET_SERVICE`: the [global Google API](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#global-google-apis) that you want to connect to.

  * `REGION`: the region to create the network endpoint group in.




## Add a Private Service Connect backend to a load balancer

You can configure a [supported load balancer](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#supported-lb-targets) to direct traffic to a Private Service Connect NEG backend.

For more information about supported configurations, see [Specifications](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#specifications).

### Add a backend to an Application Load Balancer

Add a NEG to an Application Load Balancer.

###  Console 

### Edit the load balancer

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Click the load balancer that you want to modify.

  3. Click **Edit**.




### Update the backend configuration

  1. Click **Backend configuration**.
  2. Expand the list of backend services, and select **Create a backend service**.
  3. Enter a name for the backend service.
  4. Set the **Backend type** to **Private Service Connect network endpoint group**.
  5. In the **Backends** section, click the **Private Service Connect network endpoint group** list, and select the Private Service Connect NEG that you created. Click **Done**.
  6. If you are configuring a global external Application Load Balancer to connect to a published service in multiple regions, and you have created more than one Private Service Connect NEG, click **Add backend** to select another NEG.

Repeat this step until all NEGs for this managed service are added to the backend service.

  7. Click **Create**.




### Update the routing rules

  1. Click **Routing rules**.
  2. Enter a **Host** and **Path** for each backend service that you have added.
  3. To review the configuration, click **Review and finalize**.
  4. Click **Create**.



###  gcloud 

### Update the backend configuration

  1. Create a backend service for the target service.

     * If you are adding the backend service to a regional load balancer, use the `--region` flag to specify the same region as the load balancer.
           
           gcloud compute backend-services create BACKEND_SERVICE_NAME \
               --load-balancing-scheme=SCHEME \
               --protocol=HTTPS \
               --region=REGION
           

Replace the following:

       * `BACKEND_SERVICE_NAME`: the name of the backend service.
       * `SCHEME`: the load balancing scheme for the load balancer that you are modifying: 
         * For a regional external Application Load Balancer, use `EXTERNAL_MANAGED`.
         * For an internal Application Load Balancer, use `INTERNAL_MANAGED`.
       * `REGION`: the region of the backend service. Use the same region as the NEG.
     * If you are adding the backend service to a global external Application Load Balancer, use the `--global` flag.
           
           gcloud compute backend-services create BACKEND_SERVICE_NAME \
               --load-balancing-scheme=EXTERNAL_MANAGED \
               --protocol=HTTPS \
               --global
           

Replace `BACKEND_SERVICE_NAME` with the name of the backend service.

  2. Add the Private Service Connect NEG that points to the target service.

     * If you are adding a backend service to a regional load balancer, use the `--region` flag to specify the same region as the load balancer.
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
               --network-endpoint-group=NEG_NAME \
               --network-endpoint-group-region=NEG_REGION \
               --region=REGION
           

Replace the following:

       * `BACKEND_SERVICE_NAME`: the name of the backend service.
       * `NEG_NAME`: the name of the network endpoint group.
       * `NEG_REGION`: the region of the network endpoint group.
       * `REGION`: the region of the backend service.
     * If you are adding a backend service to a global external Application Load Balancer, use the `--global` flag.

If you have created multiple NEGs in different regions for the same service, repeat this step to add all of the NEGs to the backend service.
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
               --network-endpoint-group=NEG_NAME \
               --network-endpoint-group-region=NEG_REGION \
               --global
           

Replace the following:

       * `BACKEND_SERVICE_NAME`: the name of the backend service.
       * `NEG_NAME`: the name of the network endpoint group.
       * `NEG_REGION`: the region of the network endpoint group.



### Update the routing rules

  1. For each backend service that you created, add a path matcher to the load balancer's URL map.

     * If the URL map is regional, specify the region by using the `--region` flag.
           
           gcloud compute url-maps add-path-matcher URL_MAP_NAME \
               --path-matcher-name=PATH_MATCHER \
               --default-service=BACKEND_SERVICE_NAME \
               --region=REGION
           

Replace the following:

       * `URL_MAP_NAME`: the name of the URL map.
       * `PATH_MATCHER`: a name for the path matcher.
       * `BACKEND_SERVICE_NAME`: the name of the backend service.
       * `REGION`: the region of the URL map.
     * If the URL map is global, specify the `--global` flag.
           
           gcloud compute url-maps add-path-matcher URL_MAP_NAME \
               --path-matcher-name=PATH_MATCHER \
               --default-service=BACKEND_SERVICE_NAME \
               --global
           

Replace the following:

       * `URL_MAP_NAME`: the name of the URL map.
       * `PATH_MATCHER`: a name for the path matcher.
       * `BACKEND_SERVICE_NAME`: the name of the backend service.
  2. For each hostname, add a host rule.

Each host rule can reference only one path matcher, but two or more host rules can reference the same path matcher.

     * If the URL map is regional, specify the region by using the `--region` flag.
           
           gcloud compute url-maps add-host-rule URL_MAP_NAME \
               --hosts=HOST \
               --path-matcher-name=PATH_MATCHER \
               --region=REGION
           

Replace the following:

       * `URL_MAP_NAME`: the name of the URL map.
       * `HOST`: the hostname to send requests to for this service.
       * `PATH_MATCHER`: the name of the path matcher.
       * `REGION`: the region of the URL map.
     * If the URL map is global, specify the `--global` flag.
           
           gcloud compute url-maps add-host-rule URL_MAP_NAME \
               --hosts=HOST \
               --path-matcher-name=PATH_MATCHER \
               --global
           

Replace the following:

       * `URL_MAP_NAME`: the name of the URL map.
       * `HOST`: the hostname to send requests to for this service.
       * `PATH_MATCHER`: the name of the path matcher.



### Add a backend to a regional internal proxy Network Load Balancer

You can add a Private Service Connect NEG backend to a regional internal proxy Network Load Balancer if the NEG is pointing to a published service. Regional internal proxy Network Load Balancers support only one backend service.

To configure the regional internal proxy Network Load Balancer, follow the instructions to [set up a regional internal proxy Network Load Balancer with zonal backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal), but don't complete the "Create the zonal NEGs" steps or configure health checks. Instead of configuring a zonal NEG, use the following instructions to add the Private Service Connect NEG that you created to a Private Service Connect backend.

###  Console 

  1. In the regional internal proxy Network Load Balancer that you are creating, click **Backend configuration**.
  2. For **Backend type** , select **Private Service Connect network endpoint group**.
  3. For **New backend** , select the NEG that you created.
  4. Retain the remaining default values, and then click **Done**.
  5. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



###  gcloud 

  1. Create a backend service for the target service.
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --protocol=TCP \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `REGION`: the region of the backend service. Use the same region as the NEG.
  2. Add the Private Service Connect NEG that points to the target service.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-region=NEG_REGION \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `NEG_NAME`: the name of the network endpoint group.
     * `NEG_REGION`: the region of the network endpoint group.
     * `REGION`: the region of the backend service.



### Add a backend to a regional external proxy Network Load Balancer

You can add a Private Service Connect NEG backend to a regional external proxy Network Load Balancer if the NEG is pointing to a published service. This load balancer supports only one backend service.

To configure the load balancer, follow the instructions to [set up a regional external proxy Network Load Balancer with zonal backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-zonal), but don't complete the "Create the zonal NEGs" steps or configure health checks. Instead of configuring a zonal NEG, use the following instructions to add the Private Service Connect NEG that you created to a Private Service Connect backend.

###  Console 

  1. In the regional external proxy Network Load Balancer that you are creating, click **Backend configuration**.
  2. For **Backend type** , select **Private Service Connect network endpoint group**.
  3. For **New backend** , select the NEG that you created.
  4. Retain the remaining default values, and then click **Done**.
  5. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



###  gcloud 

  1. Create a backend service for the target service.
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --protocol=TCP \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `REGION`: the region of the backend service. Use the same region as the NEG.
  2. Add the Private Service Connect NEG that points to the target service.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-region=NEG_REGION \
             --region=REGION
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service.
     * `NEG_NAME`: the name of the network endpoint group.
     * `NEG_REGION`: the region of the network endpoint group.
     * `REGION`: the region of the backend service.



## List backends

You can list all configured Private Service Connect backends.

###  Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

The Private Service Connect backends are displayed in the **Load balancer endpoints** section.




## Describe a backend

You can describe a Private Service Connect backend to view its details, including its connection status.

###  Console

  1. List the available backends.
  2. Click the backend that you want to describe.



## Troubleshooting

### Error accessing load balancer's forwarding rule

If you see a `404` error when you try to access your load balancer's forwarding rule, the error might have one of the following causes:

  * **The URL map hasn't propagated yet.**

If you just created the load balancer, try waiting a few minutes.

  * **The URL that you are using in your request does not match a URL defined in the URL map.**

Verify that the URL you are trying matches the URL map configuration in your load balancer.

  * **The service producer backend does not support the URL that you are trying to access**

Ask the service producer to verify which URL you should use to access their service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
