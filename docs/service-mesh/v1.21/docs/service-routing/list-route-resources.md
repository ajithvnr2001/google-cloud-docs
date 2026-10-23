---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/list-route-resources/
title: List `Route` resources \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:29.134740+00:00
---

# List `Route` resources  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/list-route-resources/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List `Route` resources

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://docs.google.com/forms/d/119ST-Y-CsAg-HiW8TzIDKp7Qoz6aRP8-C6GtOK_FvDY/viewform?edit_requested=true). 

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document is for mesh administrators using the service routing APIs to configure service meshes.

In the service routing API model, `Route` resources are attached to `Mesh` or `Gateway` resources. In its configuration, the `Mesh` or `Gateway` resource references one or more `Route` resources.

If you are the owner of a `Mesh` or `Gateway` resource, you can list the `Route` resources attached to the `Mesh` or `Gateway`.

Each `Mesh` or `Gateway` resource has synthetic child collection of `RouteView` resources. Each `RouteView` corresponds to a single `Route`. `RouteView` objects are created alongside `Route` objects.

In the following diagram, the `RouteView` for `Gateway` A consists of the `TCPRoute` resources from Project A. The `RouteView` for `Gateway` B comprises the `HTTPRoute` resources from Project B and `GRPCRoute` resources from Project C.

[ ![The relationships among the `Route`, `Routeview`, and `Gateway` resources.](https://docs.cloud.google.com/static/service-mesh/v1.21/docs/images/routeview.svg)](https://docs.cloud.google.com/static/service-mesh/v1.21/docs/images/routeview.svg) The relationships among the `Route`, `Routeview`, and `Gateway` resources.(click to enlarge)

This feature is scoped to the `Mesh` or `Gateway` level. A `RouteView` for a `Gateway` or `Mesh` lists routes attached to that `Gateway` or `Mesh` and not all the routes attached to the associated scope.

To list the `RouteView` resources, issue the following command:
    
    
    gcloud alpha network-services route-views list \
        --location=global \
        --[mesh | gateway]=[ MESH_NAME | GATEWAY_NAME ]
    

To get more information on the Route itself, issue the following command: 
    
    
    gcloud alpha network-services route-views describe --route-view=ROUTEVIEW_FULLNAME
    

A common workflow would be be listing the `RouteViews` for a Mesh or Gateway then describing each for a full overview of the attached Routes.

**Note:** Google Cloud CLI wraps two endpoints for convenience. When you use the API directly, the specific `Mesh` or `Gateway` endpoint and associated requests must be used for the appropriate parent(`Mesh` or `Gateway`).

You cannot create, update, or delete `RouteView` resources. They are created, updated, and deleted when their corresponding `Route` resources are created, updated, and deleted.

## Troubleshooting

**Important:** RouteViews were backfilled for existing resources as 'best effort' and will continue to self-heal during the course of normal HttpRoute, GrpcRoute, TcpRoute, and TlsRoute update operations. Routes not updated on or before 2024-08-20 may not be reflected with RouteViews for projects with certain security configurations. 

If the route-views commands fail to list RouteViews for routes such as `Listed 0 items.` or not listing all known routes: 

  * Verify that the Mesh or Gateway used in the `route-views list` are referenced within the Route's `meshes` or `gateways` fields, respectively using:
    * gcloud network-services [http-routes|grpc-routes|tcp-routes|tls-routes] describe \
              --location global ROUTE_ID

  * For customers with many resources, create a support ticket for assistance.
  * Manually Trigger an update for your Route/s
    * Reimporting the route
      1. gcloud network-services http-routes export my-route --location=global \
                   --destination=export.yaml

      2. gcloud network-services http-routes import my-route --location=global \
                   --source=export.yaml

    * For customers using the generated NetworkServices client, call appropriate NetworkServices.Update*Route API.
    * Modify description to trigger Terraform automation.



## What's next

  * For information about how service routing works, read [Service routing overview](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/service-routing-overview)
  * For information about the service routing APIs, read the documentation for the [network services APIs](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-services/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
