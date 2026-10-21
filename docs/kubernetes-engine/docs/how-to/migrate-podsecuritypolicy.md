---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-podsecuritypolicy/
title: Migrate from PodSecurityPolicy to the PodSecurity admission controller \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:12:13.432778+00:00
---

# Migrate from PodSecurityPolicy to the PodSecurity admission controller  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-podsecuritypolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Migrate from PodSecurityPolicy to the PodSecurity admission controller Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to continue to enforce many Pod-level security controls in your Google Kubernetes Engine (GKE) clusters by migrating from PodSecurityPolicy to the [PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission).

## Overview

PodSecurityPolicy was a Kubernetes admission controller that let you enforce Pod-level security controls such as the [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/), providing granular control over the security configuration of your deployed workloads. The Kubernetes project deprecated PodSecurityPolicy and removed the feature entirely in Kubernetes v1.25.

If you currently use PodSecurityPolicy in your GKE clusters, disable the feature before you upgrade to GKE version 1.25 and later.

To learn more about the deprecation and removal of PodSecurityPolicy, refer to [PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy).

### PodSecurity and PodSecurityPolicy

The `PodSecurity` admission controller is available and enabled by default on clusters running the following GKE versions:

  * Version 1.25 or later: Stable
  * Version 1.23 and version 1.24: Beta



`PodSecurity` allows you to enforce the policies defined in the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) on your deployed workloads. `PodSecurity` lets you continue to implement recommended Pod-level security configurations in your clusters after you migrate from PodSecurityPolicy. Unlike PodSecurityPolicy, `PodSecurity` doesn't support custom configurations.

## Requirements and limitations

  * `PodSecurity` is available in beta in GKE versions 1.23 and 1.24, and in stable in GKE version 1.25 and later.
  * `PodSecurity` doesn't terminate Pods that are already running on your nodes, even if they violate the applied policy.
  * `PodSecurity` doesn't mutate fields. If you use any [mutating fields in your PodSecurityPolicy](https://kubernetes.io/docs/reference/access-authn-authz/psp-to-pod-security-standards/#podsecuritypolicy-spec), modify your Pod spec to ensure that those fields are present when you deploy the workloads.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE Autopilot or Standard cluster running version 1.23 or later. 
    * For Autopilot clusters, [enroll in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#enrolling_a_cluster_in_a_release_channel) in which the default version is 1.23 or later.
    * For Standard clusters, enroll in a release channel or [upgrade the cluster to a specific version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Check your `PodSecurityPolicy` resources for mutating field configurations. Add those fields to your Pod manifests so that any workloads already running on your nodes conform with a policy defined in the Pod Security Standards. For instructions, refer to [Simplify and standardize Pod Security Policies](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/#simplify-psps).



## Configure the PodSecurity admission controller in your cluster

The `PodSecurity` admission controller enforces the Pod Security Standards at the namespace level. You must configure the controller to enforce one of the policies defined by the Pod Security Standards in each namespace. The following policies are available:

  * **Restricted** : Most restrictive policy. Complies with Pod hardening best practices.
  * **Baseline** : Minimally restrictive policy that prevents known privilege escalations. Allows all default values for fields in Pod specifications.
  * **Privileged** : Unrestricted policy that allows anything, including known privilege escalations. Apply this policy with caution.



To migrate your PodSecurityPolicy configuration to the `PodSecurity` admission controller, do the following in **every namespace** in your cluster. These steps are described in detail in the sections that follow.

  1. Apply the **Restricted** policy in `dry-run` mode to the namespace and check for violations.
  2. If your Pods violate the **Restricted** policy, apply the less restrictive **Baseline** policy in `dry-run` mode to the namespace and check for violations.
  3. If your Pods violate the **Baseline** policy, modify your Pod specs to fix the violations.
  4. When the **Baseline** policy no longer returns violations, apply the policy in `enforce` mode to the namespace.



To avoid potential downtime if `PodSecurity` rejects new Pods, perform these steps in a staging environment. Alternatively, you can apply the identified policy in `audit` mode instead of `enforce` mode and review your audit logs to find potential rejected Pods.

`audit` mode doesn't enforce the policy. GKE deploys the Pods and adds entries to the [GKE audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).

### List all namespaces in your cluster

Get a list of all namespaces in your cluster. Repeat the steps in the following sections for every namespace in the list:
    
    
    kubectl get ns
    

In the following GKE versions, GKE ignores policies that you apply to the `kube-system` namespace:

  * 1.23.6-gke.1900 and later
  * 1.24.0-gke.1200 and later



In earlier GKE versions, avoid enforcing policies in `kube-system`.

### Apply each policy of the Pod Security Standards in dry-run mode

In the following steps, you'll apply each policy in [`dry-run` mode](https://kubernetes.io/docs/reference/using-api/api-concepts/#dry-run), starting with the most restrictive **Restricted** policy. If the output shows a warning, either modify the violating Pod spec to comply with the policy, or try the less restrictive **Baseline** policy. If the output doesn't show a warning, you can then apply the **Baseline** policy without `dry-run` mode.

  1. Apply the **Restricted** policy in `dry-run` mode:
         
         kubectl label --dry-run=server --overwrite ns NAMESPACE \
             pod-security.kubernetes.io/enforce=restricted
         

If a Pod in the namespace violates the Restricted policy, the output is similar to the following:
         
         Warning: existing pods in namespace "NAMESPACE" violate the new PodSecurity enforce level "restricted:latest"
         namespace/NAMESPACE labeled
         

If the **Restricted** policy displays a warning, modify your Pods to fix the violation and try the command again. Alternatively, try the less restrictive **Baseline** policy in the following step.

  2. Apply the **Baseline** policy in `dry-run` mode:
         
         kubectl label --dry-run=server --overwrite ns NAMESPACE \
             pod-security.kubernetes.io/enforce=baseline
         

If a Pod in the namespace violates the Baseline policy, the output is similar to the following:
         
         Warning: existing pods in namespace "NAMESPACE" violate the new PodSecurity enforce level "baseline:latest"
         namespace/NAMESPACE labeled
         




If your Pods violate the Baseline policy, modify your Pods to fix the violations and repeat this step until GKE no longer displays a warning.

**Caution:** You can optionally use the Privileged policy, which has no restrictions. Before using the Privileged policy, ensure that you trust all workloads and users that have access to the namespace. The Privileged policy allows known privilege escalations, but may be required for certain privileged system workloads.

### Enforce the policy on a namespace

When you identify the policy that works for a namespace, apply the policy to the namespace in `enforce` mode:
    
    
    kubectl label --overwrite ns NAMESPACE \
        pod-security.kubernetes.io/enforce=POLICY
    

Replace `POLICY` with the name of the policy, which can be one of `restricted`, `baseline`, or `privileged`.

Ensure that you repeat the preceding steps for every namespace in your cluster.

## Disable the PodSecurityPolicy feature on your cluster

After you configure the `PodSecurity` admission controller for **every namespace** in your cluster, disable the PodSecurityPolicy feature:
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --no-enable-pod-security-policy
    

Replace `CLUSTER_NAME` with the name of your GKE cluster.

**Note:** After you disable the feature, you don't need to manually remove any remaining `PodSecurityPolicy` objects. When you run `kubectl get psp`, GKE might display the remaining policies, but GKE doesn't enforce those policies.

When you upgrade your cluster to GKE version 1.25, GKE automatically removes all remaining `PodSecurityPolicy` objects, including those added by GKE, Policy Controller, and any `PodSecurityPolicy` objects that you previously defined.

## Recommendations

  * Try to conform to the Restricted policy where possible. Audit your applications to see if the configuration can be hardened further.
  * You can lock the Pod security mode to a specific Kubernetes minor version by adding the `pod-security.kubernetes.io/MODE-version: VERSION` label to the `kubectl label` commands in the previous steps. Replace `VERSION` with the Kubernetes version number, such as `v1.24`.
  * After you disable the PodSecurityPolicy feature, review your running applications to check for disruptions or gaps in the security configuration.
  * After you configure `PodSecurity`, update your namespace creation process to automatically apply a `PodSecurity` label to all new namespaces. For information, see [Review namespace creation process](https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/#review-namespace-creation-process)



## What's next

  * [Learn more about Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
  * [Learn more about the `PodSecurity` admission controller](https://kubernetes.io/docs/concepts/security/pod-security-admission/).
  * [Learn how to apply custom Pod-level security policies using Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper).
  * [Read about the PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
