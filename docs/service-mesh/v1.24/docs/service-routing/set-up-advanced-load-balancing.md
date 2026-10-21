---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-advanced-load-balancing/
title: Set up advanced load balancing \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:46.255238+00:00
---

# Set up advanced load balancing  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-advanced-load-balancing/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up advanced load balancing

This document contains directions for setting up the advanced load balancing options that are described in the [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/advanced-load-balancing-overview). This document is intended for users who have at least an intermediate understanding of Cloud Service Mesh and load balancing concepts.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

## Before you begin

Update Google Cloud CLI to make sure that you have the most recent version:
    
    
    gcloud components update
    

Create a new backend service or decide which existing backend service to use for advanced load balancing.

To create a new backend service called `hello-world-backend-service`, use the following command:
    
    
    gcloud compute backend-services create hello-world-backend-service \
        --global \
        --protocol=HTTP \
        --health-checks hello-world-health-check \
        --load-balancing-scheme=INTERNAL_SELF_MANAGED
    
    

## Create a service load balancing policy with YAML

You can define service load balancing policies in a YAML file. For example, set up a policy to enable the auto-capacity-drain feature as follows, in a file called `hello-world-lb-policy`:
    
    
    name: projects/${project-id}/locations/global/serviceLbPolicies/hello-world-lb-policy
    autoCapacityDrain:
      enable: True
    

After you create the YAML file, import it:
    
    
    gcloud network-services service-lb-policies import hello-world-lb-policy \
       --source=hello-world-lb-policy.yaml \
       --location=global
    

Lastly, associate the service load balancing policy with the backend service:
    
    
    gcloud compute backend-services update hello-world-backend-service \
      --service-lb-policy hello-world-lb-policy \
      --global
    

Alternatively, you can associate an existing service load balancing policy with a backend service when you create the backend service:
    
    
    gcloud compute backend-services create hello-world-backend-service \
        --global \
        --protocol=HTTP \
        --health-checks hello-world-health-check \
        --load-balancing-scheme=INTERNAL_SELF_MANAGED \
        --service-lb-policy hello-world-lb-policy
    

These instructions cover only changes to the backend service resource. Your Cloud Service Mesh deployment must also include a health check and firewall rules, and you must add backends as needed.

## Configure the spray-to-region algorithm

To configure the spray-to-region algorithm, which spreads traffic to all zones in a region, create a service load balancing policy in a file called `hello-world-lb-policy.yaml`:
    
    
    name: projects/${project-id}/locations/global/serviceLbPolicies/hello-world-lb-policy
    loadBalancingAlgorithm: SPRAY_TO_REGION
    

Import the yaml file:
    
    
    gcloud network-services service-lb-policies import hello-world-lb-policy \
       --source=hello-world-lb-policy.yaml \
       --location=global
    

You can also configure this algorithm with the gcloud CLI:
    
    
    gcloud network-services service-lb-policies create hello-world-lb-policy \
        --load-balancing-algorithm=SPRAY_TO_REGION \
        --location=global
    

## Configure the waterfall-by-zone algorithm

To configure the waterfall-by-zone algorithm, which sends traffic to the local zone before spilling traffic to other zones, create a service load balancing policy in a file called `hello-world-lb-policy.yaml`:
    
    
    name: projects/${project-id}/locations/global/serviceLbPolicies/hello-world-lb-policy
    loadBalancingAlgorithm: WATERFALL_BY_ZONE
    

Import the yaml file:
    
    
    gcloud network-services service-lb-policies import hello-world-lb-policy \
       --source=hello-world-lb-policy.yaml \
       --location=global
    

You can also configure this algorithm with the gcloud CLI:
    
    
    gcloud network-services service-lb-policies create hello-world-lb-policy \
        --load-balancing-algorithm=WATERFALL_BY_ZONE \
        --location=global
    

## Configure preferred backends

To configure preferred backends, configure the backend service as follows:
    
    
    name: projects/${project-id}/locations/global/backendServices/hello-world-service
    ...
    backends:
    ...
      preference: PREFERRED
    

The following example shows three backends, `MIG1`, `MIG2`, and `MIG3`:
    
    
    name: ..
    ...
    - backends
    name: MIG1
    preference: PREFERRED
    - backends
    name: MIG2
    preference: DEFAULT
    - backends
    name: MIG3
    ...
    

You can also configure this feature with the gcloud CLI:
    
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
          [...]
          --preference=PREFERRED \
          --global
    

To update the preferred backends:
    
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
          [...]
          --preference=PREFERRED
    

## Configure auto capacity drain

To configure Cloud Service Mesh to drain a backend automatically based on its health, create a service load balancing policy as follows:
    
    
    name: projects/${project-id}/locations/global/serviceLbPolicies/hello-world-lb-policy
    autoCapacityDrain:
      enable: True
    

You can also configure this feature with the gcloud CLI:
    
    
    gcloud network-services service-lb-policies create capacity-drain-policy \
        --auto-capacity-drain \
        --location=global
    

## Customize failover behavior

To configure Cloud Service Mesh for a specific value for the failover health threshold, include the following in a service load balancing policy, replacing `VALUE` with a value between 1 and 99. The default values are 50 for Cloud Service Mesh with proxyless gRPC and 70 for Cloud Service Mesh with Envoy.
    
    
    projects/${project-id}/locations/global/serviceLbPolicies/hello-world-lb-policy
    failoverConfig:
      failoverHealthThreshold: VALUE
    

To customize failover behavior with the gcloud CLI:
    
    
    gcloud network-services service-lb-policies create failover-health-threshold--policy \
       --failover-health-threshold=VALUE \
       --location=global
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
