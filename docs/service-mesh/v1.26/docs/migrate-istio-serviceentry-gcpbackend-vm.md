---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/migrate-istio-serviceentry-gcpbackend-vm/
title: Migrate Istio ServiceEntry to GCPBackend for Compute Engine VMs \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:09.766644+00:00
---

# Migrate Istio ServiceEntry to GCPBackend for Compute Engine VMs  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/migrate-istio-serviceentry-gcpbackend-vm/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate Istio ServiceEntry to GCPBackend for Compute Engine VMs

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

This page shows you how to migrate from ServiceEntry to GCPBackend, demonstrating how Istio's traffic management capabilities can ensure a smooth and safe transition.

Migrating to GCPBackend provides the following benefits:

  1. Endpoint Discovery - VM endpoints in the Backend Service are automatically updated when VM instances are added or removed.
  2. Centralized Health Checking - VM endpoints are health checked and traffic is automatically routed away from unhealthy to healthy backends.
  3. Global load balancing and advanced load balancing algorithms - VM endpoints can be deployed in multiple regions. Use our load balancing algorithms to configure load balancing behavior across these regions. See https://cloud.google.com/service-mesh/v1.26/docs/service-routing/advanced-load-balancing-overview and https://cloud.google.com/service-mesh/v1.26/docs/service-routing/advanced-load-balancing-overview for more details.
  4. Seamless migration: Utilize traffic splitting and mirroring to safely migrate traffic without disrupting the application.
  5. Enhanced manageability: Benefit from the streamlined configuration and management.



## Before you begin

The following sections assume that you have:

  1. [A GKE Cluster with Cloud Service Mesh enabled](https://docs.cloud.google.com/service-mesh/v1.26/docs/onboarding/provision-control-plane).
  2. An Istio Service Entry.
  3. Configured GCPBackend resource for [Compute Engine VM](https://docs.cloud.google.com/service-mesh/v1.26/docs/route-to-Compute%20Engine-vms#configure_a_service_as_a_gcpbackend).



## Create or modify the existing VirtualService to include both the ServiceEntry and GCPBackend as destinations

You can use traffic splitting to gradually shift traffic from the ServiceEntry to the GCPBackend. You should start with a small percentage of traffic directed to the GCPBackend and gradually increase it while monitoring for any issues.

The following example describes migrating 10% of the requests to the GCPBackend.
    
    
    cat <<EOF > virtual-service.yaml
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: gcpbackend-migration
      namespace: NAMESPACE
    spec:
      hosts:
      - service-entry.com
      http:
      - route:
        - destination:
            host: gcpbackend.com
          weight: 10 # 10% traffic to gcp backend.
        - destination:
            host: service-entry.com
          weight: 90 # 90% traffic to service entry
    EOF
    kubectl apply -f virtual-service.yaml
    

Where:

  * NAMESPACE is the namespace name.



In this example:

  * VIRTUAL_SERVICE is `gcpbackend-migration`.
  * SERVICE_ENTRY_HOSTNAME is `service-entry.com`.
  * GCP_BACKEND_HOSTNAME is `gcpbackend.com`.



### (Optional) Configure VirtualService for Traffic Mirroring

To further ensure a smooth transition, you can configure traffic mirroring to send a copy of the traffic to the GCPBackend while still primarily directing traffic to the ServiceEntry. This allows for testing and validation of the GCPBackend configuration without impacting the primary traffic flow. For more information, see the [Istio Virtual Service API](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPMirrorPolicy).

## Validate functionality

Refer to your application logs or Cloud Service Mesh metrics to check error rate of requests to $SERVICE_ENTRY_HOSTNAME. There shouldn't be any errors. 

To test outside of your application, you can deploy a curl client. If the request is routed to using the GCPBackend API then the request doesn't need an IAM token explicitly attached to the request because Cloud Service Mesh attaches it automatically.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: v1
    kind: Pod
    metadata:
      name: testcurl
      namespace: default
    spec:
      containers:
      - name: curl
        image: curlimages/curl
        command: ["sleep", "3000"]
    EOF
    
    kubectl exec testcurl -c curl -- curl "$SERVICE_ENTRY_HOSTNAME"
    

The output should be a valid HTTP 200 response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
