---
url: https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation/
title: Check control plane implementation \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:00.602102+00:00
---

# Check control plane implementation  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Check control plane implementation

The [`gcloud container fleet mesh describe`](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/mesh/describe) command lets you determine which control plane implementation manages your Cloud Service Mesh clusters. You can confirm whether a cluster uses Google Cloud managed infrastructure (`TRAFFIC_DIRECTOR`), managed `istiod`, or an in-cluster deployment to verify feature compatibility and monitor migrations.

To identify your cluster's control plane implementation, run the following command:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

The output is similar to the following:
    
    
      ...
      membershipSpecs:
        projects/746296320118/locations/us-central1/memberships/demo-cluster-1:
          mesh:
            management: MANAGEMENT_AUTOMATIC
      membershipStates:
        projects/746296320118/locations/us-central1/memberships/demo-cluster-1:
          servicemesh:
            controlPlaneManagement:
              details:
              - code: REVISION_READY
                details: 'Ready: asm-managed'
              state: ACTIVE
              implementation: TRAFFIC_DIRECTOR
      ...
    

The possible values of the `implementation` are:

  * `TRAFFIC_DIRECTOR`: The core infrastructure of Google Cloud serves as the Cloud Service Mesh control plane.
  * `ISTIOD` [Deprecated](https://docs.cloud.google.com/service-mesh/deprecations): managed instance of `istiod` serves as the Cloud Service Mesh control plane.
  * `UPDATING`: The cluster is being migrated between implementations. Soon you will have the `TRAFFIC_DIRECTOR` implementation.

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

If you don't see `controlPlaneManagement.state: ACTIVE` this means you don't have a managed control plane. To confirm that you have an in-cluster control plane, check for an `istiod` deployment in your `istio-system` namespace:
    
    
    kubectl -n istio-system get deploy istiod
    

The output is similar to the following:
    
    
    NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
    istiod                 1/1     1            1           20m
    

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
