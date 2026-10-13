---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-cleanup/
title: Resolving cleanup issues \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:15.339424+00:00
---

# Resolving cleanup issues  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-cleanup/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving cleanup issues

This page explains how to resolve issues with Cloud Service Mesh managed control plane when using the `TRAFFIC_DIRECTOR` implementation.

## Clean up synthetic services

When using the `TRAFFIC_DIRECTOR` control plane implementation, Cloud Service Mesh creates synthetic Kubernetes services to support subset. These services are labeled with `istio.io/owned-by:gsmconfig.gke.io`.

When you unregister a cluster from a Google Cloud fleet, Cloud Service Mesh might not be able to remove these synthetic Kubernetes services.

To mitigate this issue, you can manually remove synthetic Kubernetes services in all namespaces by running the following command:
    
    
    kubectl delete service -l istio.io/owned-by=gsmconfig.gke.io -A
    

## Clean up network endpoint groups annotations

When using the `TRAFFIC_DIRECTOR` control plane implementation, Cloud Service Mesh creates network endpoint groups by adding `cloud.google.com/neg` annotations to services for load balancing.

When you unregister a cluster from a Google Cloud fleet, Cloud Service Mesh might not be able to remove these annotations to clean up the network endpoint groups.

To mitigate this issue, you can manually remove the `cloud.google.com/neg` annotations from services in all namespaces.
    
    
    service_names=($(kubectl get service -A -o jsonpath='{.items[*].metadata.name}'))
    for service in "${service_names[@]}"; do
      kubectl annotate service $service -A cloud.google.com/neg-
    done
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
