---
url: https://docs.cloud.google.com/kubernetes-engine/security/autopilot-cluster-policies-standard/
title: Enforce Autopilot security policies in Standard clusters \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:52.330381+00:00
---

# Enforce Autopilot security policies in Standard clusters  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/autopilot-cluster-policies-standard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Enforce Autopilot security policies in Standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) Autopilot clusters enforce various [security policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) that are designed to prevent many common attack pathways. This document shows platform administrators how to enforce some or all of these Autopilot policies in Standard clusters. You can't disable cluster policy enforcement in Autopilot clusters, because Autopilot clusters are designed for a higher baseline GKE security posture.

In Standard clusters, you can enable and disable specific policies at any time. Organization administrators can control whether specific Autopilot policies can be disabled by enforcing a custom constraint in the organization, folder, or project. You can use these predefined policies to enforce security best practices without needing to write complex RBAC roles and bindings. Many of the cluster-level policies can help you to improve your cluster security even if you aren't interested in using Autopilot mode for the cluster or workloads. For more information about the available Autopilot cluster policies, see the Supported policies section.

## Considerations for enforcing Autopilot cluster policies

While Autopilot clusters always enforce these policies, Standard clusters often have existing workloads and node pools that might violate policies that you enforce. Before you enforce or disable a policy in your cluster, read the following considerations:

  * **Changes apply only to new workloads** : when you enable a policy that applies to workloads, the changes apply only to Pods that are created or modified after you enable that policy. Existing Pods that violate the policy can continue to run. Before you enable a policy, review the existing workloads in the cluster to verify that they comply with the policy's constraint.
  * **Node pool policies apply to all nodes** : when you enable a policy that applies to the node pools in your Standard cluster, the constraints apply to both new and existing node pools. If an existing node pool violates the policy, the cluster update operation fails. For example, if you try to enable the `no-standard-node-pools` policy in a cluster that has an existing user-managed node pool, your operation fails. Before you enable a node pool policy, review the existing node pools in the cluster.
  * **Enabling all policies enables Autopilot mode** : if you enable all of the available Autopilot policies (including the policy that prevents user-managed node pools), then all of the workloads in your cluster can run only in Autopilot mode. This means that all of your workloads must comply with the [Autopilot security constraints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#built-in-security) and with all of the cluster policies. This approach lets you run the entire Standard cluster in Autopilot mode, with the option to disable specific policies when required.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable specific Autopilot policies in your cluster

Use the gcloud CLI or the GKE API to enable specific policies when you create or update a Standard cluster. To add specific Autopilot cluster policies to the list of policies that GKE enforces in the cluster, use the `--autopilot-cluster-policies` flag with the `gcloud container clusters create` command or the `gcloud container clusters update` command.

The following example shows you how to enable policies in an existing cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --autopilot-cluster-policies=AUTOPILOT_POLICIES
    

Replace the following:

  * `CLUSTER_NAME`: the name of your Standard cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane, like `us-central1` or `us-central1-a`.
  * `AUTOPILOT_POLICIES`: a comma-separated list of Autopilot cluster policies to start enforcing in the cluster, such as `no-system-mutation,no-system-impersonation`. You must specify one or more supported policies. The policies that you specify are appended to the list of policies that GKE already enforces in the cluster. To disable the enforcement of a policy, see the Disable specific Autopilot policies in your cluster section.



If the command fails with an error message that starts with `Bad value [invalid policy]:`, verify that all of the policy names that you specified are in the list of supported policies.

## Verify policy enforcement

After you enable a specific policy, you can verify that the enforcement works by trying to create a resource that violates that policy. For example, if you enable the `no-system-mutation` policy, you can try to create a Pod in the `kube-system` namespace. GKE blocks the Pod creation operation and displays an error message that's similar to the following:
    
    
    Error from server (Forbidden): pods is forbidden: User cannot create resource "pods" in API group "" in the namespace "kube-system": GKE Warden authz [denied by managed-namespaces-limitation]: the namespace "kube-system" is managed and the request's verb "create" is denied
    

## Disable specific Autopilot policies in your cluster

You can disable any of the Autopilot cluster policies at any time. Disabling a policy is useful in situations where your security requirements have changed, or when an existing workflow was disrupted when you enabled that policy. To remove a policy from the list of policies that GKE enforces in the cluster, use the `--remove-autopilot-cluster-policies` flag with the `gcloud container clusters update` command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --remove-autopilot-cluster-policies=AUTOPILOT_POLICIES
    

You must specify at least one value for the `--remove-autopilot-cluster-policies` flag. If you specify this flag without a value, the operation fails.

If the command fails with an error message that starts with `Bad value [invalid policy]:`, verify that all of the policy names that you specified are in the list of supported policies.

## Enforce Autopilot cluster policies in organizations

Organization administrators can enforce the use of these cluster policies across an organization, project, or folder by using [custom organization policy constraints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies). This additional measure can help you to prevent unauthorized or unintended removal of required cluster policies from a cluster. Use the `ClusterPolicyConfig` field in your custom constraint, like in the following example:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.autopilotClusterPolicies
    resourceTypes:
    -   container.googleapis.com/Cluster
    methodTypes:
    -   CREATE
    -   UPDATE
    condition: "resource.ClusterPolicyConfig.no_system_mutation == true && resource.ClusterPolicyConfig.no_system_impersonation == true"
    actionType: ALLOW
    displayName: Autopilot policies in Standard clusters.
    description: For all new and existing Standard clusters, enable the no_system_mutation and no_system_impersonation Autopilot cluster policies. For more information, see https://docs.cloud.google.com/kubernetes-engine/security/autopilot-cluster-policies-standard.
    

## Supported policies

Each of the Autopilot policies that's available in Standard clusters implements one or more security best practices at the cluster level. Policies like `no-system-mutation`, `no-system-impersonation`, and `no-unsafe-webhooks` help to improve the security of any GKE cluster, even if you aren't interested in using Autopilot mode.

The following table describes the Autopilot policies that you can enable in Standard clusters and helps you to prepare for policy enforcement:

Policy name | Description | What to do before enablement  
---|---|---  
`no-system-mutation` | Prevent the creation or modification of resources in GKE system namespaces (such as `kube-system`). | Move your Pods from system namespaces into your own namespaces.  
`no-system-impersonation` | Blocks attempts to impersonate system users and prevents the creation of CertificateSigningRequests using system principals. | Look for any unauthorized CertificateSigningRequests that were generated for system identities. If you find any approved unauthorized CertificateSigningRequests, [rotate your cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation) to invalidate the certificates.  
`no-unsafe-webhooks` | Prevents admission webhooks and policies from intercepting critical system resources such as `Node` objects, PersistentVolumes, or CertificateSigningRequests. | Use the Recommender service to identify webhooks that intercept system resources. If you find any webhooks, modify the webhook configuration. For more information, see [Ensure control plane stability when using webhooks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks).  
`no-standard-node-pools` | Prevent any user-managed node pools, including manually created and auto-created node pools, from existing in the cluster. Only Autopilot node pools can exist in the cluster. | Delete all existing non-Autopilot node pools, including the default node pool that was created with the cluster.  
  
## What's next

  * Learn more about how to [harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * Learn about the other [Autopilot security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
