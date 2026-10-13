---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2
title: Package google.cloud.gkehub.policycontroller.v2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:44.928541+00:00
---

# Package google.cloud.gkehub.policycontroller.v2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Package google.cloud.gkehub.policycontroller.v2 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[BundleInstallSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.BundleInstallSpec)` (message)
  * `[HubConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.HubConfig)` (message)
  * `[HubConfig.InstallSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.HubConfig.InstallSpec)` (enum)
  * `[MonitoringConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.MonitoringConfig)` (message)
  * `[MonitoringConfig.MonitoringBackend](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.MonitoringConfig.MonitoringBackend)` (enum)
  * `[OnClusterState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.OnClusterState)` (message)
  * `[PolicyContentSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyContentSpec)` (message)
  * `[PolicyContentState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyContentState)` (message)
  * `[PolicyControllerDeploymentConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig)` (message)
  * `[PolicyControllerDeploymentConfig.Affinity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig.Affinity)` (enum)
  * `[PolicyControllerDeploymentConfig.Toleration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig.Toleration)` (message)
  * `[ResourceList](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.ResourceList)` (message)
  * `[ResourceRequirements](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.ResourceRequirements)` (message)
  * `[Spec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.Spec)` (message)
  * `[State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.State)` (message)
  * `[State.LifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.State.LifecycleState)` (enum)
  * `[TemplateLibraryConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.TemplateLibraryConfig)` (message)
  * `[TemplateLibraryConfig.Installation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.TemplateLibraryConfig.Installation)` (enum)



## BundleInstallSpec

BundleInstallSpec is the specification configuration for a single managed bundle.

Fields  
---  
`exempted_namespaces[]` |  `string` the set of namespaces to be exempted from the bundle  
  
## HubConfig

Configuration for Policy Controller

Fields  
---  
`install_spec` |  `[HubConfig.InstallSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.HubConfig.InstallSpec)` The install_spec represents the intended state specified by the latest request that mutated install_spec in the feature spec, not the lifecycle state of the feature observed by the Hub feature controller that is reported in the feature state.  
`exemptable_namespaces[]` |  `string` The set of namespaces that are excluded from Policy Controller checks. Namespaces do not need to currently exist on the cluster.  
`referential_rules_enabled` |  `bool` Enables the ability to use Constraint Templates that reference to objects other than the object currently being evaluated.  
`log_denies_enabled` |  `bool` Logs all denies and dry run failures.  
`mutation_enabled` |  `bool` Enables the ability to mutate resources using Policy Controller.  
`deployment_configs` |  `map<string, `[PolicyControllerDeploymentConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig)`>` Map of deployment configs to deployments (“admission”, “audit”, “mutation”).  
`audit_interval_seconds` |  `int64` Sets the interval for Policy Controller Audit Scans (in seconds). When set to 0, this disables audit functionality altogether.  
`monitoring` |  `[MonitoringConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.MonitoringConfig)` Monitoring specifies the configuration of monitoring.  
`policy_content` |  `[PolicyContentSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyContentSpec)` Specifies the desired policy content on the cluster  
`constraint_violation_limit` |  `int64` The maximum number of audit violations to be stored in a constraint. If not set, the internal default (currently 20) will be used.  
  
## InstallSpec

Enums  
---  
`INSTALL_SPEC_UNSPECIFIED` | Spec is unknown.  
`INSTALL_SPEC_NOT_INSTALLED` | Request to uninstall Policy Controller.  
`INSTALL_SPEC_ENABLED` | Request to install and enable Policy Controller.  
`INSTALL_SPEC_SUSPENDED` | Request to suspend Policy Controller i.e. its webhooks. If Policy Controller is not installed, it will be installed but suspended.  
`INSTALL_SPEC_DETACHED` | Request to stop all reconciliation actions by PoCo Hub controller. This is a breakglass mechanism to stop PoCo Hub from affecting cluster resources.  
  
## MonitoringConfig

MonitoringConfig specifies the backends Policy Controller should export metrics to. For example, to specify metrics should be exported to Cloud Monitoring and Prometheus, specify backends: ["cloudmonitoring", "prometheus"]

Fields  
---  
`backends[]` |  `[MonitoringConfig.MonitoringBackend](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.MonitoringConfig.MonitoringBackend)` Specifies the list of backends Policy Controller will export to. An empty list would effectively disable metrics export.  
  
## MonitoringBackend

Supported backend options for monitoring

Enums  
---  
`MONITORING_BACKEND_UNSPECIFIED` | Backend cannot be determined  
`PROMETHEUS` | Prometheus backend for monitoring  
`CLOUD_MONITORING` | Stackdriver/Cloud Monitoring backend for monitoring  
  
## OnClusterState

OnClusterState represents the state of a sub-component of Policy Controller.

Fields  
---  
`state` |  `[State.LifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.State.LifecycleState)` The lifecycle state of this component.  
`details` |  `string` Surface potential errors or information logs.  
  
## PolicyContentSpec

PolicyContentSpec defines the user's desired content configuration on the cluster.

Fields  
---  
`bundles` |  `map<string, `[BundleInstallSpec](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.BundleInstallSpec)`>` map of bundle name to BundleInstallSpec. The bundle name maps to the `bundleName` key in the `policycontroller.gke.io/constraintData` annotation on a constraint.  
`template_library` |  `[TemplateLibraryConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.TemplateLibraryConfig)` Configures the installation of the Template Library.  
  
## PolicyContentState

The state of the policy controller policy content

Fields  
---  
`template_library_state` |  `[OnClusterState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.OnClusterState)` The state of the template library  
`bundle_states` |  `map<string, `[OnClusterState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.OnClusterState)`>` The state of the any bundles included in the chosen version of the manifest  
`referential_sync_config_state` |  `[OnClusterState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.OnClusterState)` The state of the referential data sync configuration. This could represent the state of either the syncSet object(s) or the config object, depending on the version of PoCo configured by the user.  
  
## PolicyControllerDeploymentConfig

Deployment-specific configuration.

Fields  
---  
`pod_tolerations[]` |  `[PolicyControllerDeploymentConfig.Toleration](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig.Toleration)` Pod tolerations of node taints.  
`pod_affinity` |  `[PolicyControllerDeploymentConfig.Affinity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyControllerDeploymentConfig.Affinity)` Pod affinity configuration.  
`replica_count` |  `int64` Pod replica count.  
`container_resources` |  `[ResourceRequirements](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.ResourceRequirements)` Container resource requirements.  
`pod_anti_affinity  
**(deprecated)**` |  `bool` This item is deprecated!Pod anti-affinity enablement. Deprecated: use `pod_affinity` instead.  
  
## Affinity

The pod affinity configuration used by a deployment.

Enums  
---  
`AFFINITY_UNSPECIFIED` | No affinity configuration has been specified.  
`NO_AFFINITY` | Affinity configurations will be removed from the deployment.  
`ANTI_AFFINITY` | Anti-affinity configuration will be applied to this deployment. Default for admissions deployment.  
  
## Toleration

Toleration of a node taint.

Fields  
---  
`key` |  `string` Matches a taint key (not necessarily unique).  
`operator` |  `string` Matches a taint operator.  
`value` |  `string` Matches a taint value.  
`effect` |  `string` Matches a taint effect.  
  
## ResourceList

ResourceList contains container resource requirements.

Fields  
---  
`memory` |  `string` Memory requirement expressed in Kubernetes resource units.  
`cpu` |  `string` CPU requirement expressed in Kubernetes resource units.  
  
## ResourceRequirements

ResourceRequirements describes the compute resource requirements.

Fields  
---  
`limits` |  `[ResourceList](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.ResourceList)` Limits describes the maximum amount of compute resources allowed for use by the running container.  
`requests` |  `[ResourceList](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.ResourceList)` Requests describes the amount of compute resources reserved for the container by the kube-scheduler.  
  
## Spec

**Policy Controller** : Configuration for a single cluster. Intended to parallel the PolicyController CR.

Fields  
---  
`policy_controller_hub_config` |  `[HubConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.HubConfig)` Policy Controller configuration for the cluster.  
`version` |  `string` Version of Policy Controller installed.  
  
## State

**Policy Controller** : State for a single cluster.

Fields  
---  
`component_states` |  `map<string, `[OnClusterState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.OnClusterState)`>` Currently these include (also serving as map keys): 1. "admission" 2. "audit" 3. "mutation"  
`state` |  `[State.LifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.State.LifecycleState)` The overall Policy Controller lifecycle state observed by the Hub Feature controller.  
`policy_content_state` |  `[PolicyContentState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.PolicyContentState)` The overall content state observed by the Hub Feature controller.  
  
## LifecycleState

The set of states Policy Controller can exist in.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | The lifecycle state is unspecified.  
`NOT_INSTALLED` | The PC does not exist on the given cluster, and no k8s resources of any type that are associated with the PC should exist there. The cluster does not possess a membership with the PCH.  
`INSTALLING` | The PCH possesses a Membership, however the PC is not fully installed on the cluster. In this state the hub can be expected to be taking actions to install the PC on the cluster.  
`ACTIVE` | The PC is fully installed on the cluster and in an operational mode. In this state PCH will be reconciling state with the PC, and the PC will be performing it's operational tasks per that software. Entering a READY state requires that the hub has confirmed the PC is installed and its pods are operational with the version of the PC the PCH expects.  
`UPDATING` | The PC is fully installed, but in the process of changing the configuration (including changing the version of PC either up and down, or modifying the manifests of PC) of the resources running on the cluster. The PCH has a Membership, is aware of the version the cluster should be running in, but has not confirmed for itself that the PC is running with that version.  
`DECOMMISSIONING` | The PC may have resources on the cluster, but the PCH wishes to remove the Membership. The Membership still exists.  
`CLUSTER_ERROR` | The PC is not operational, and the PCH is unable to act to make it operational. Entering a CLUSTER_ERROR state happens automatically when the PCH determines that a PC installed on the cluster is non-operative or that the cluster does not meet requirements set for the PCH to administer the cluster but has nevertheless been given an instruction to do so (such as ‘install').  
`HUB_ERROR` | In this state, the PC may still be operational, and only the PCH is unable to act. The hub should not issue instructions to change the PC state, or otherwise interfere with the on-cluster resources. Entering a HUB_ERROR state happens automatically when the PCH determines the hub is in an unhealthy state and it wishes to ‘take hands off' to avoid corrupting the PC or other data.  
`SUSPENDED` | Policy Controller (PC) is installed but suspended. This means that the policies are not enforced, but violations are still recorded (through audit).  
`DETACHED` | PoCo Hub is not taking any action to reconcile cluster objects. Changes to those objects will not be overwritten by PoCo Hub.  
  
## TemplateLibraryConfig

The config specifying which default library templates to install.

Fields  
---  
`installation` |  `[TemplateLibraryConfig.Installation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rpc/google.cloud.gkehub.policycontroller.v2#google.cloud.gkehub.policycontroller.v2.TemplateLibraryConfig.Installation)` Configures the manner in which the template library is installed on the cluster.  
  
## Installation

How the template library should be installed

Enums  
---  
`INSTALLATION_UNSPECIFIED` | No installation strategy has been specified.  
`NOT_INSTALLED` | Do not install the template library.  
`ALL` | Install the entire template library.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
