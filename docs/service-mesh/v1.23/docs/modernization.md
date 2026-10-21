---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/modernization/
title: Managed control plane modernization \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:08.575976+00:00
---

# Managed control plane modernization  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/modernization/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed control plane modernization

Starting on July 22, 2024, Google will gradually update existing clusters to use the managed control plane with TD implementation. You will be notified before we update your meshes.

You can review the capabilities of the Istiod and Traffic Director control planes on the page that describes [Supported features using Istio APIs (managed control plane)](https://docs.cloud.google.com/service-mesh/v1.23/docs/supported-features-managed).

## Scheduling and Notification

You should receive notification that a cluster is scheduled to be updated at least two weeks before the update. Notifications are available in your cluster-level feature state conditions.

Use the following Google Cloud CLI command to check the notification:
    
    
    gcloud container fleet mesh describe --project=PROJECT_ID
    

You see results similar to the following:
    
    
    membershipStates:
      projects/656460026795/locations/us-central1/memberships/cluster:
        servicemesh:
          conditions:
          - code: MODERNIZATION_SCHEDULED
            details: This cluster has been scheduled for modernization on or after (date ~ at least 2 weeks).
            documentationLink: 
            severity: INFO
    

Any legacy managed control plane clusters that were onboarded using the `meshconfig.googleapis.com` API will be automatically registered to the fleet in the cluster's project with the `gkehub.googleapis.com` Membership API. If you have any automation that deregisters a cluster, you must remove it before modernization or the modernization will have issues. For the managed product to work successfully, it must be registered to a fleet with the mesh feature enabled.

[Contact support](https://docs.cloud.google.com/service-mesh/v1.23/docs/getting-support) if you need to customize your modernization or if you have questions about whether you are using unsupported features.

## Active modernization

During the modernization, in a safe and controlled way, the following changes take place:

  * To enable health checking, the `snk` daemonset is created in the `kube-system` namespace of the cluster and a per-cluster a firewall rule is created.
  * To enable [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs) ingestion, the annotation `cloud.google.com/neg` is added to all Kubernetes services.
  * New Google Cloud resources such as [`Mesh`](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/service-routing-overview), [`Routes`](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/service-routing-overview), [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service), and [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) are created in the cluster.
  * Pods managed by Kubernetes deployments are restarted to reconnect to the Traffic Director control plane.



Some of the new resources are quota-limited. You can [view quotas and request more if necessary](https://docs.cloud.google.com/load-balancing/docs/quotas).

You can track the progress of a fleet's modernization with the following Google Cloud CLI command, and looking in each member's `conditions`:
    
    
    gcloud container fleet mesh describe --project=PROJECT_ID
    

When a cluster is being modernized you will see:
    
    
    conditions:
    - code: MODERNIZATION_IN_PROGRESS
      details: The modernization for this cluster is in progress.
      documentationLink: 
      severity: INFO
    

When the modernization is complete you will see: 
    
    
    conditions:
    - code: MODERNIZATION_COMPLETED
      details: The modernization for this cluster was completed.
      documentationLink: 
      severity: INFO
    

If the modernization is cancelled you will see: 
    
    
    conditions:
    - code: MODERNIZATION_ABORTED
      details: The modernization for this cluster was aborted.
      documentationLink: 
      severity: INFO
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
