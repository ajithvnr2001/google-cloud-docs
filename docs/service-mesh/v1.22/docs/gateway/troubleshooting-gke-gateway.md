---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/troubleshooting-gke-gateway/
title: Troubleshoot Cloud Service Mesh GKE service mesh deployments \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:24.656096+00:00
---

# Troubleshoot Cloud Service Mesh GKE service mesh deployments  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/gateway/troubleshooting-gke-gateway/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Cloud Service Mesh GKE service mesh deployments

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide contains information for resolving issues with Gateway API service mesh deployments.

## Information in the `status` field

All Gateway API resources have a `status` field that reflects the status of resources from the controller perspective. In addition to the `status` field, the controller appends events to Gateway API resources to provide information about its operations on those resources.

For example, use the following commands to inspect the status and events of a `TDMesh`:
    
    
    kubectl describe tdmesh td-mesh
    

The output is similar to the following:
    
    
    ...
    Status:
      Conditions:
        Last Transition Time:  1970-01-01T00:00:00Z
        Message:               Waiting for controller
        Reason:                NotReconciled
        Status:                False
        Type:                  Scheduled
    Events:
    ...
    

The previous status indicates that the controller has not started to reconcile this particular mesh. If this status lasts for more than 5 minutes with no events appended, read the following section, [Controller does not seem to reconcile a `TDMesh` resource](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/gke-gateway-overview#controller-issue) to further troubleshoot the issue.

You can use a similar method to debug issues related to other resources, such as `HTTPRoute`, `TCPRoute`, and other routing resources.

Usually, the statuses and events indicate the underlying issue.

### Controller does not seem to reconcile a `TDMesh` resource

To diagnose the issue, confirm that a `gke-td` `GatewayClass` exists:
    
    
    kubectl get gatewayclasses
    

The output should include a `GatewayClass` named `gke-td`.
    
    
    NAME             CONTROLLER
    gke-td           networking.gke.io/gateway
    

If a `GatewayClass` with that name is not returned, follow [Install the required custom resource definitions](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/prepare-gateway#install-crds) to confirm all required CRDs are installed in the config cluster, then reenable the hub feature for the Cloud Service Mesh Google Kubernetes Engine service mesh with the following commands:

  1. Disable the feature:
         
         gcloud container hub ingress disable
         

  2. Re-enable the feature:
         
         gcloud container hub ingress enable \
           --config-membership=/projects/PROJECT_ID/locations/global/memberships/gke-1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
