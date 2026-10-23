---
url: https://docs.cloud.google.com/vpc/docs/configure-published-service-backends/
title: Access published services through published service backends and endpoints \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:15.725642+00:00
---

# Access published services through published service backends and endpoints  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-published-service-backends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access published services through published service backends and endpoints

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can configure supported load balancers or regional Cloud Service Mesh to route traffic to published services through Private Service Connect endpoints. To do this, you associate a regional backend service with a service attachment. This configuration is known as a published service backend.

This page describes how to configure published service backends for load balancers. For information about configuring published service backends for regional Cloud Service Mesh, see [Configure published service backends for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/regional-cloud-service-mesh#configuring-published-service-backends).

Published service backends are only supported if both the producer and consumer VPC networks belong to the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

## Before you begin

  * Read about [published service backends](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backends).
  * Make sure that the producer VPC network that hosts the service belongs to the same organization as the consumer network where you want to configure published service backends.
  * [Identify the service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) of the service that you want to access.
  * Identify or create a Private Service Connect endpoint that connects to the service you want to access. This endpoint must be in the same region as your consumer load balancer.
  * Identify or create a consumer load balancer that [supports published service backends](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backend-support): 
    * The load balancer's forwarding rule and backend service must be in the same region as the service attachment and the Private Service Connect endpoint that connects to the service.
    * If you create a new load balancer, don't add any backends to the load balancer's backend service. You will add them when you configure a published service backend.
  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.



### Required roles

To get the permissions that you need to configure load balancing for Private Service Connect endpoints, ask your administrator to grant you the [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add a published service backend to a consumer load balancer

To create a published service backend, you associate a load balancer's regional backend service with a service attachment. You don't explicitly associate the load balancer with an endpoint. Instead, when a client sends a request to the load balancer, the load balancer routes traffic through an `ACCEPTED` Private Service Connect endpoint that connects to the service attachment.

###  gcloud 

Use the [`gcloud beta compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/add-backend).
    
    
    gcloud beta compute backend-services add-backend BACKEND_SERVICE \
        --region=REGION \
        --service=//compute.googleapis.com/projects/PROJECT_ID/locations/REGION/serviceAttachments/SERVICE_ATTACHMENT
    

Replace the following:

  * `BACKEND_SERVICE`: the name of the backend service
  * `REGION`: the region of the backend service, which must match the region of the service attachment
  * `PROJECT_ID`: the project ID of the service attachment's project
  * `SERVICE_ATTACHMENT`: the name of the service attachment to associate with the backend service



###  API 

  1. You need to include the backend service's fingerprint when you update the backend service. To find the fingerprint, send a request to the [`regionBackendServices.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionBackendServices/get).

HTTP method and URL:
         
         GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
         

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `REGION`: the region of the backend service, which must match the region of the service attachment
     * `BACKEND_SERVICE`: the name of the backend service

Note the `fingerprint` value in the response, which you need for the next step.

  2. Send a request to the [`regionBackendServices.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionBackendServices/patch).

The following request replaces any existing backends.

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE
         

Request JSON body:
         
         {
           "backends": [
             {
               "group": "https://www.googleapis.com/compute/beta/projects/PROJECT_ID/locations/REGION/serviceAttachments/SERVICE_ATTACHMENT"
             }
           ],
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `SERVICE_ATTACHMENT`: the name of the service attachment to associate with the backend service
     * `FINGERPRINT`: the fingerprint value that you noted in the previous step



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
