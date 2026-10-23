---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-cross-project-mesh-route/
title: Set up cross-project references \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:39.327126+00:00
---

# Set up cross-project references  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-cross-project-mesh-route/

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

# Set up cross-project references

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

This document applies only to Cloud Service Mesh with the Google Cloud service routing APIs. Don't use this document if you are configuring Cloud Service Mesh with the Istio APIs.

In some scenarios, the service mesh configuration includes services that are in different projects. For example, in Shared VPC or peered VPC deployments it is possible for each project owner to define their own set of services to make these services available to all other projects.

[ ![Cross-project configuration with Mesh resources](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/cross-ref-setup.svg)](https://docs.cloud.google.com/static/service-mesh/v1.24/docs/images/cross-ref-setup.svg) Cross-project configuration with `Mesh` resources (click to enlarge)

This configuration is called a _cross-project_ configuration because multiple resources defined in different projects are combined to form a single configuration that can be served to an Envoy proxy or proxyless gRPC client.

The following instructions use the `Mesh` and `HTTPRoute` resources, but they can be applied to the `Gateway` resource and to the `GRPCRoute` and `TCPRoute` resources.

## Configure the `Mesh` resource

Designate a project as the host project where you administer the `Mesh` resource. Any service account with the permissions to create, update, or delete `Mesh` resources in this project can control the routing configurations attached to `Mesh` resources in this project.

  1. In the file `shared-mesh.yaml`, create a `Mesh` specification.
         
         name: shared-mesh
         interceptionPort: 15001
         

  2. Define a `Mesh` resource in this project.
         
         gcloud network-services meshes import shared-mesh \
           --source=shared-mesh.yaml \
           --location=global
         

  3. Write down the full URI of the `Mesh` resource, because service owners need the URI to attach their routes to this `Mesh`.
         
         /projects/HOST_PROJECT_NUMBER/locations/global/meshes/shared-mesh
         

  4. Grant the `networkservices.meshes.use` IAM permission for this `Mesh` to the cross-project service accounts that should be able to attach their services information to this `Mesh`.
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_NUMBER
           --member='HTTP_ROUTE_SERVICE_OWNER_ACCOUNT'
           --role='roles/compute.networkAdmin'
         




All service owners that have`networkservices.meshes.use` permission granted to them are able to add their routing rules to this `Mesh` resource.

## Set up routing in the service projects

Each service owner needs to create one or more backend service and `Route` resources in their project, similar to the example in the [sidecar proxy configuration guide](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-envoy-http-mesh). The only difference is that each `HTTPRoute`, `GRPCRoute`, or `TCPRoute` resource must have the URI of the host project's `Mesh` resource in the `meshes` field.

  1. Use the following to populate the `meshes` field. You can use either the project ID or the project number.
         
         echo "name: sharedvpc-http-route
         hostnames:
         - helloworld-gce
         meshes:
         - /projects/HOST_PROJECT_NUMBER/locations/global/meshes/shared-mesh
         rules:
         - action:
             destinations:
             - serviceName: \"url/of/the/service\"" | \
         gcloud network-services http-routes import sharedvpc-http-route \
             --source=- \
             --location=global
         




## Create the client services in the service projects

When you configure a Cloud Service Mesh client that is located in a service project, the bootstrap configuration must specify the project number where the `Mesh` resource is located and the `Mesh` name. This requirement applies to both [Envoy proxy](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-envoy-http-mesh#client) and [proxyless gRPC deployments](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/set-up-proxyless-mesh#set-up-bootstrap). With Envoy deployments, use the `--service-proxy:project-number` option.

## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/list-route-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
