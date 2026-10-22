---
url: https://docs.cloud.google.com/config-connector/docs/concepts/controller-types/
title: Config Connector controller types \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:45.064751+00:00
---

# Config Connector controller types  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/controller-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Config Connector controller types

Config Connector uses a layered architecture to reconcile resources in your Google Cloud environment with your Kubernetes specifications. A top-level parent controller routes the reconciliation of each resource to one of four underlying controller implementations.

Understanding each controller type, how they differ technically, and how you can control namespace-wide routing can help you optimize performance and troubleshoot configuration issues.

## Underlying controller types

Config Connector uses the following controller types:

  * **Direct controllers:** This controller uses the standard Kubernetes `controller-runtime` library and communicates with Google Cloud APIs directly using the official Google Cloud Go SDKs. We recommend you use direct controllers when possible. Not all resources support the direct controller. New resources use the direct controller by default. Existing resources are migrated regularly. For more information, see the [release notes](https://docs.cloud.google.com/config-connector/docs/release-notes).
  * **Terraform-based controllers (TF):** This controller acts as a "wrapper" for the Terraform Google Provider. The controller translates Kubernetes Resource Model (KRM) specifications into Terraform-compatible states and implements `plan` and `apply` Terraform operations.
  * **DCL-based controllers:** This controller type acts as a "wrapper" for the Google Cloud Declarative Client Library (DCL).
  * **IAM-specific controllers:** These are specialized controllers designed specifically to manage Identity and Access Management (IAM) resources, including IAMPolicy, IAMPartialPolicy, IAMPolicyMember, and IAMAuditConfig. Some IAM resources optionally support the direct controller.



## Benefits of direct controllers

Some resource types support multiple controller types. If a resource supports the direct controller, we recommend using direct instead of another controller type for the following reasons:

  * **Reduced resource consumption:** Direct controllers don't have the CPU and memory overhead associated with running and translation of Terraform-based or DCL-based states.
  * **Improved reconciliation latency:** Direct controllers can make direct operations against Google Cloud endpoints, reducing the average time required to reach consistency of the resource state.
  * **Granular status and structured diffs:** The direct controller provides structured diff reporting in `cnrm-controller-manager` logs. These logs contain the precise field changes that initiated errors like reconciliation loops, which can help make troubleshooting easier.
  * **Native observed state:** Direct controllers populate `status.observedState` in the resource status, providing a transparent, server-side view of the resource fields returned directly by the Google Cloud APIs.
  * **Improved lifecycle handling:** Direct controllers include additional features such as graceful orphan deletion.



## Parent routing controller

Regardless of the resource type, Config Connector intercepts all reconciliation requests within a central parent controller. The parent controller acts as a router, evaluating which child logic handles the active sync using the following precedence rules:

  1. **Namespace overrides:** The parent controller first checks the ConfigConnectorContext resource configuration in the target resource's namespace for any explicit controller overrides.
  2. **Static defaults:** If no local overrides are specified, the parent controller defaults to the build-time reconciler defined in the Config Connector static mapping config.



## Identify the controller for a resource

You can determine which controller type is configured or active for a specific Google Cloud resource by using the active code mapping or examining CustomResourceDefinition (CRD) structures in Google Kubernetes Engine (GKE).

To look up the static configuration for a resource, inspect the resource in GitHub at [pkg/controller/resourceconfig/static_config.go](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/pkg/controller/resourceconfig/static_config.go), and look for the configuration block for the resource, such as the following example:
    
    
    {Group: "alloydb.cnrm.cloud.google.com", Kind: "AlloyDBCluster"}: {
        DefaultController:    k8s.ReconcilerTypeTerraform,
        SupportedControllers: []k8s.ReconcilerType{k8s.ReconcilerTypeDirect, k8s.ReconcilerTypeTerraform},
    }
    

  * **`DefaultController`:** Indicates the default reconciler used if no namespace-level context override rules are specified.
  * **`SupportedControllers`:** Lists all reconcilers implemented and available for this resource. Overrides switch to reconcilers listed here.



To inspect CRD labels, use the `kubectl get crd` command:
    
    
    kubectl get crd RESOURCE_NAME -o jsonpath='{.metadata.labels}'
    

Replace `RESOURCE_NAME` with the exact name of the Config Connector CRD, for example, `bigquerydatasets.bigquery.cnrm.cloud.google.com`.

Check the results for the following information:

  * **`cnrm.cloud.google.com/tf2crd: "true"`:** The Terraform-based (TF) controller manages the resource.
  * **`cnrm.cloud.google.com/dcl2crd: "true"`:** The DCL-based controller manages the resource.
  * **Absence of these labels:** The direct controller manages the resource.



## Override the default controller

There are two primary methods for overriding the controller type in Config Connector. The distinction between them primarily involves their operational scope, maintenance overhead, and the precedence they take during reconciliation.

The following table summarizes the differences between the two approaches:

Feature | Resource annotation | ConfigConnectorContext override  
---|---|---  
Scope | Single resource instance | All resources of a kind in a namespace  
Precedence | Highest (overrides ConfigConnectorContext) | Medium (overrides static default)  
Recommended? | No | Yes  
Best for | One-off testing | Team or project-wide rollout  
  
### Override the controller for a specific resource

You can force a specific resource instance to run with a specific reconciler by adding the `alpha.cnrm.cloud.google.com/reconciler` annotation to the resource metadata. Although this approach is not recommended for the reasons specified in the previous section, you might need it to test configurations for a single resource instance or for maintain legacy configurations.
    
    
    apiVersion: bigquery.cnrm.cloud.google.com/v1beta1
    kind: BigQueryDataset
    metadata:
      name: my-bq-ds
      namespace: NAMESPACE_NAME
      annotations:
        alpha.cnrm.cloud.google.com/reconciler: direct
    spec:
      ...
    

Supported values for the annotation are `direct`, `tf`, or `dcl`.

### Override the controller for a namespace

To configure a namespace-wide override using the ConfigConnectorContext custom resource, complete the following steps:

  1. Retrieve the name and group from the resource definitions. For example, for the `BigQueryDataset` resource, the resource kind is `BigQueryDataset` and the group is `bigquery.cnrm.cloud.google.com`.

  2. Edit the ConfigConnectorContext object inside the namespace containing your managed resources:
         
         kubectl edit configconnectorcontext configconnectorcontext.core.cnrm.cloud.google.com -n NAMESPACE_NAME
         

Replace `NAMESPACE_NAME` with your target namespace.

  3. Add your target overrides. For example, to override all `BigQueryDataset` instances in this namespace to run with the direct controller, define the configuration as follows:
         
         apiVersion: core.cnrm.cloud.google.com/v1beta1
         kind: ConfigConnectorContext
         metadata:
           name: configconnectorcontext.core.cnrm.cloud.google.com
           namespace: NAMESPACE_NAME
         spec:
           googleServiceAccount: "kcc-sa@my-project.iam.gserviceaccount.com"
           experiments:
             controllerOverrides:
               BigQueryDataset.bigquery.cnrm.cloud.google.com: direct
         

  4. Save and apply the resource. The parent controller automatically applies the new direct reconciler routing rules dynamically to all matching resources in this namespace.




### Namespace override constraints and use cases

  * **Explicit support requirement:** For an override to succeed, the targeted controller type must be implemented for the resource kind. To check if a controller type is supported, see Identify the controller for a resource. If the controller type you specify in the override is not supported, the parent controller ignores the override and the default reconciler continues handling the resource.
  * **Namespace limit:** Overrides under a ConfigConnectorContext apply collectively to all instances of that resource type that reside inside that specific namespace. You cannot target individual resource instances with namespace-scoped overrides.
  * **Access control:** Updating a ConfigConnectorContext object typically requires higher-level platform team privileges compared to standard resource edits.
  * **Override status reporting:** If an invalid or unsupported controller type is specified in the `ConfigConnectorContext` overrides, the parent controller marks the context as unhealthy. You can verify this by running `kubectl get configconnectorcontext configconnectorcontext.core.cnrm.cloud.google.com -n NAMESPACE_NAME -o yaml` and checking the `.status.healthy` and `.status.errors` fields.
  * **When to use:** This is the recommended approach for overriding controllers. Use it to opt-in entire namespaces to modern controllers (such as direct) or to enforce architectural consistency across a project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
