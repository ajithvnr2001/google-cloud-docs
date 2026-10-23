---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-backend-multicluster-inference-gateway/
title: Customize backend configurations with GCPBackendPolicy scopes \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:44.312997+00:00
---

# Customize backend configurations with GCPBackendPolicy scopes  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-backend-multicluster-inference-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Customize backend configurations with GCPBackendPolicy scopes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In a [multi-cluster Google Kubernetes Engine (GKE) Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway) environment, you can apply different backend configurations to services deployed across multiple clusters. For example, you can set different maximum request rates or capacity scalers for backends in different regions or environments.

To understand this document, you should be familiar with the following:

  * [AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * [Generative AI terminology](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/glossary-genai).
  * [GKE networking concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview) including [Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), [GKE Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), and the [ GKE Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * [Load balancing in Google Cloud](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), especially how load balancers interact with GKE.



This document targets the following personas:

  * Machine learning (ML) engineers, Platform admins and operators, and Data and AI specialists interested in using Kubernetes container orchestration capabilities for serving AI/ML workloads.
  * Cloud architects or Networking specialists who interact with Kubernetes networking.



To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE Enterprise user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## How `GCPBackendPolicy` scopes work

The `scopes` field in `GCPBackendPolicy` lets you tailor backend configurations based on the specific clusters where your backends are running. You can apply different settings to backends in different environments or regions, which gives you fine-grained control over your distributed AI/ML workloads. The following sections explain how to target resources, define policy scopes, and handle conflict resolution.

### Target Inference Gateway resources

To use Inference Gateway policies in a multi-cluster GKE environment, the `GCPBackendPolicy`'s `targetRef` field must reference a `GCPInferencePoolImport` resource:
    
    
    targetRef:
      group: networking.gke.io
      kind: GCPInferencePoolImport
      name: example
    

### Policy scope definition

The `scopes` field in `GCPBackendPolicy` lets you apply different backend settings to specific groups of backends. By defining configuration objects within `default.scopes`, you can use cluster labels to precisely target backends and apply specific settings. For example, you can set unique capacity limits or request rates for backends in different regions or clusters.

You can't specify the same backend-level fields (like `maxRatePerEndpoint`) in both the main `default` section and within the `default.scopes` entries. Attempting to do so causes the policy to be rejected, which helps to ensure clear and consistent configurations.

### Conflict resolution

When a backend matches multiple scopes, the system applies the following rules to ensure predictable behavior:

  * **Prioritized matching:** if a backend matches multiple selectors in your `scopes` list, the system applies only the settings from the _first_ matching selector. Order your scopes from the most specific to the most general to help ensure your intended configuration takes effect.
  * **Precise targeting:** when a single selector contains multiple labels (for example, `gke.io/region: us-central1` and `env: prod`), the backend must satisfy _all_ those labels for the system to apply the scope's configuration. This approach lets you precisely target backends based on multiple criteria.



## Supported per-backend fields

The following table lists the backend-level fields that you can customize to control backend behavior in different environments or regions.

Field Name | Description | Example Configuration  
---|---|---  
`backendPreference` | Specifies whether the backend is preferred (`PREFERRED`) or default (`DEFAULT`) during capacity chasing for multi-region load balancing. | `backendPreference: PREFERRED`  
`balancingMode` | Specifies the balancing algorithm. Supported values are `RATE`, `UTILIZATION`, or `CUSTOM_METRICS`. | `balancingMode: CUSTOM_METRICS`  
`capacityScalerPercent` | Configures traffic distribution based on capacity. This value is a percentage from 0 to 100, acting as a multiplier on the backend's configured target capacity. The default value is 100%. | `capacityScalerPercent: 20`  
`customMetrics` | Specifies custom metrics used for load balancing when `balancingMode` is set to `CUSTOM_METRICS`. This field is a list of metric definitions. | `customMetrics: [{ name: "my-metric", value: 0.8 }]`  
`maxInFlightPerEndpoint` | Sets the maximum number of concurrent requests or connections per endpoint. | `maxInFlightPerEndpoint: 100`  
`maxRatePerEndpoint` | Sets the maximum rate of requests per endpoint, in requests per second (RPS). | `maxRatePerEndpoint: 50`  
  
## Specify scope selectors

The `selectors` field in each scope lets you control which backends receive specific policy settings. You can target backends based on their cluster labels—either built-in GKE labels or your own custom labels—to tailor configurations for different groups of backends.

**Warning:** The `IN_FLIGHT` and `CUSTOM_METRICS` load balancing modes must be wholly specified in the default configuration. These modes don't support granular scope selectors within the `scopes` field. For example, if `balancingMode` is `IN_FLIGHT` in the default configuration, you can't specify `maxInFlightPerEndpoint` within a scope. Similarly, if `balancingMode` is `CUSTOM_METRICS`, you can't specify `customMetrics` within a more specific scope. The following is an invalid configuration:
    
    
    kind: GCPBackendPolicy
    apiVersion: networking.gke.io/v1
    metadata:
      name: echoserver-v2
    spec:
      targetRef:
        group: "networking.gke.io"
        kind: GCPInferencePoolImport
        name: test-inference-pool
      default:
        balancingMode: IN_FLIGHT # IN_FLIGHT mode is set at the default level
        scopes:
        - selector:
            gke.io/zone: "us-central1-a"
          maxInFlightPerEndpoint: 100 # Invalid: maxInFlightPerEndpoint cannot be set within a scope when balancingMode is IN_FLIGHT at the default level
    

### Implicit GKE labels

The following implicit labels are available to use as selectors. GKE automatically applies these labels to your clusters:

Label | Description | Example Value  
---|---|---  
`gke.io/cluster-name` | The name of the GKE cluster. | `my-cluster`  
`gke.io/region` | The region where the cluster is located. | `us-central1`  
`gke.io/zone` | The zone where the cluster is located. | `us-central1-a`  
  
### Custom cluster labels

Custom cluster labels provide more flexibility for grouping and managing your backends. By defining your own labels on your GKE clusters, you can create highly specific selectors in your `GCPBackendPolicy` to apply unique configurations. For example, you can base these configurations on criteria such as different environments (`dev`, `staging`, or `prod`) or specific application versions.

To add a custom label, such as `environment=production`, to a GKE cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --region=REGION \
        --update-labels=LABEL_KEY=LABEL_VALUE
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `REGION`: the region of your cluster.
  * `LABEL_KEY`: the key for your custom label, for example, `environment`.
  * `LABEL_VALUE`: the value for your custom label, for example, `production`.



You can then select backends in this cluster by using the custom label selector in your policy.

## Example `GCPBackendPolicy` with scope selectors

The following example defines a `GCPBackendPolicy` that targets an `GCPInferencePoolImport` named `experimental`. The policy uses implicit and custom labels to set values for `backendPreference`, `maxRatePerEndpoint`, and `capacityScalerPercent`.
    
    
    apiVersion: networking.gke.io/v1
    kind: GCPBackendPolicy
    metadata:
      name: backend-policy
    spec:
      targetRef:
        kind: GCPInferencePoolImport
        name: experimental
      default:
        scopes:
          # Selector 1: Targets backends in us-west2, sets capacity to 50%
          - capacityScalarPercent: 50
            selector:
              gke.io/region: us-west2
    
          # Selector 2: Targets backends in clusters labeled 'env: prod'
          - maxRatePerEndpoint: 40
            selector:
              env: prod
    
          # Selector 3: Targets backends in a specific US-Central zone and marks them as PREFERRED
          - backendPreference: PREFERRED
            maxRatePerEndpoint: 50
            selector:
              gke.io/cluster-name: my-cluster
              gke.io/zone: us-central1-a
    

After applying this policy, you observe the following behaviors:

  * Backends in clusters within the `us-west2` region have their effective capacity scaled to 50%.
  * Backends in clusters labeled with `env: prod` are limited to a maximum of 40 requests per second per endpoint.
  * Backends in clusters specifically located in the `us-central1-a` zone are prioritized (`PREFERRED`) during load balancing and have a maximum rate of 50 requests per second per endpoint.



## What's next

  * Learn how to [Configure a `GCPBackendPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure-backend-selection).
  * Learn more about [multi-cluster GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multi-cluster-inference-gateway).
  * Learn more about [Set up the multi-cluster GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multicluster-inference-gateway).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
