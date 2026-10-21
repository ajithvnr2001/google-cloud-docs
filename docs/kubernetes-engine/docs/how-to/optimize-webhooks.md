---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks/
title: Ensure control plane stability when using webhooks \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:33:11.442240+00:00
---

# Ensure control plane stability when using webhooks  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Ensure control plane stability when using webhooks Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Admission webhooks, or _webhooks_ in Kubernetes, are a type of [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/), which can be used in Kubernetes clusters to validate or mutate requests to the control plane prior to a request being persisted. It is common for third-party applications to use webhooks that operate on system-critical resources and namespaces. Incorrectly configured webhooks can impact control plane performance and reliability. For example, an incorrectly configured webhook created by a third-party application could prevent GKE from creating and modifying resources in the managed `kube-system` namespace, which could degrade the functionality of the cluster.

Google Kubernetes Engine (GKE) monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to deliver guidance for how you can optimize your usage of the platform. To help you ensure that your cluster remains stable and performant, see recommendations from GKE for the following scenarios:

  * Webhooks that operate but have no endpoints available.
  * Webhooks that are considered unsafe as they operate on system critical resources and namespaces.



With this guidance, you can see instructions for how to check your potentially misconfigured webhooks and update them, if necessary.

To learn more about how to manage insights and recommendations from Recommenders, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Identify misconfigured webhooks that could affect your cluster

To get insights identifying webhooks that could affect your cluster's performance and stability, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs). You can get insights in the following ways:

  * Use the Google Cloud console.
  * Use the Google Cloud CLI, or the Recommender API, filtering with the subtypes `K8S_ADMISSION_WEBHOOK_UNSAFE` and `K8S_ADMISSION_WEBHOOK_UNAVAILABLE`.



After you identify the webhooks via the insights, follow the instructions to troubleshoot the detected webhooks.

## When GKE detects misconfigured webhooks

GKE generates an insight and recommendation if either of the following criteria are true for a cluster:

  * `K8S_ADMISSION_WEBHOOK_UNAVAILABLE`: The GKE cluster has one or more webhooks reporting no available endpoints. Follow the instructions to check webhooks reporting no available endpoints.
  * `K8S_ADMISSION_WEBHOOK_UNSAFE`: The GKE cluster has one or more webhooks that are considered unsafe based on the resources they intercept. Follow the instructions to check the webhooks that are considered unsafe. The following webhooks are considered unsafe:

    * Webhooks intercepting resources, including Pods and [Leases](https://kubernetes.io/docs/concepts/architecture/leases/), in the `kube-system` namespace.
    * Webhooks intercepting Leases in the `kube-node-lease` namespace.
    * Webhooks intercepting cluster-scoped system resources, including [`Nodes`](https://kubernetes.io/docs/concepts/architecture/nodes/), [`TokenReviews`](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/), [`SubjectAccessReviews`](https://kubernetes.io/docs/reference/access-authn-authz/authorization/), and [`CertificateSigningRequests`](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/).



## Troubleshoot the detected webhooks

The following sections have instructions for you to troubleshoot the webhooks that GKE detected as potentially misconfigured.

After you implement the instructions and the webhooks are correctly configured, the recommendation is resolved within 24 hours and no longer appears in the console.

If you do not want to implement the recommendation, you can [dismiss it](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#dismiss-recommendation).

### Webhooks reporting no available endpoints

If a webhook is reporting that it has no available endpoints, the Service that is backing the webhook endpoint has one or more Pods which are not running. To make the webhook endpoints available, follow the instructions to find and troubleshoot the Pods of the Service that is backing this webhook endpoint:

  1. [View insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs), choosing one insight at a time to troubleshoot. GKE generates one insight per cluster, and this insight lists one or more webhooks with a broken endpoint that must be investigated. For each of these webhooks, the insight also states the Service name, what endpoint is broken, and the last time that the endpoint was called.

  2. Find the serving Pods for the Service associated with the webhook:

### Console

From the insight's sidebar panel, see the table of misconfigured webhooks. Click on the name of the Service.

### kubectl

Run the following command to describe the Service:
         
         kubectl describe svc SERVICE_NAME -n SERVICE_NAMESPACE
         

Replace SERVICE_NAME and SERVICE_NAMESPACE with the name and namespace of the service, respectively.

If you cannot find the Service name listed in the webhook, the unavailable endpoint might be caused by a mismatch between the name listed in the configuration and the actual name of the Service. To fix the endpoint availability, update the Service name in the webhook configuration to match the correct Service object.

  3. Inspect the serving Pods for this Service:

### Console

Under **Serving Pods** in the **Service details** , see the list of Pods backing this Service.

### kubectl

Identify which Pods are not running by listing the Deployment or Pods:
         
         kubectl get deployment -n SERVICE_NAMESPACE
         

Or, run this command:
         
         kubectl get pods -n SERVICE_NAMESPACE -o wide
         

For any Pods that are not running, inspect the Pod logs to see why the Pod is not running. For instructions on common issues with Pods, see [Troubleshoot issues with deployed workloads](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads).




### Webhooks that are considered unsafe

If a webhook is intercepting any resources in system-managed namespaces, or certain types of resources, GKE considers this unsafe and recommends that you update the webhooks to avoid intercepting these resources.

  1. Follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs), choosing one insight at a time to troubleshoot. GKE only generates one insight per cluster, and this insight lists one or more webhook configurations, each of which lists one or more webhooks. For each webhook configuration listed, the insight states the reason why the configuration was flagged.
  2. Inspect the webhook configuration:

### Console

From the insight's sidebar panel, see the table. In each row is the name of the webhook configuration, and the reason why this configuration was flagged.

To inspect each configuration, click the name to navigate to this configuration in the GKE [Object Browser](https://console.cloud.google.com/kubernetes/object/browser) dashboard.

### kubectl

Run the following `kubectl` command to get the webhook configuration, replacing CONFIGURATION_NAME with the name of the webhook configuration:
         
         kubectl get validatingwebhookconfigurations CONFIGURATION_NAME -o yaml
         

If this command doesn't return anything, run the command again, replacing `validatingwebhookconfigurations` with `mutatingwebhookconfigurations`.

In the `webhooks` section, there are one or more webhooks listed.

  3. Edit the configuration, depending on the reason the webhook was flagged:

#### Exclude kube-system and kube-node-lease namespaces

A webhook is flagged if `scope` is `*`. Or, a webhook is flagged if scope is `Namespaced` and either of the following conditions are true:

     * The `operator` condition is `NotIn` and `values` omits `kube-system` and `kube-node-lease`, as in the following example:
           
           webhooks:
           - admissionReviewVersions:
             ...
             namespaceSelector:
               matchExpressions:
               - key: kubernetes.io/metadata.name
                 operator: NotIn
                 values:
                 - blue-system
             objectSelector: {}
             rules:
             - apiGroups:
               ...
               scope: '*'
             sideEffects: None
             timeoutSeconds: 3
           

Ensure that you set `scope` to `Namespaced`, not `*`, so that the webhook only operates in specific namespaces. Also ensure that if the `operator` is `NotIn`, you include `kube-system` and `kube-node-lease` in `values` (in this example, with `blue-system`).

     * The `operator` condition is `In` and `values` includes `kube-system` and `kube-node-lease`, as in the following example:
           
           namespaceSelector:
               matchExpressions:
               - key: kubernetes.io/metadata.name
                 operator: In
                 values:
                 - blue-system
                 - kube-system
                 - kube-node-lease
           

Ensure that you set `scope` to `Namespaced`, not `*`, so that the webhook only operates in specific namespaces. Ensure that if `operator` is `In`, you don't include `kube-system` and `kube-node-lease` in `values`. In this example, only `blue-system` should be in `values` as the `operator` is `In`.

#### Exclude matched resources

A webhook is also flagged if `nodes`, `tokenreviews`, `subjectaccessreviews`, or `certificatesigningrequests` are listed under resources, as in the following example:
    
    - admissionReviewVersions:
    ...
      resources:
      - 'pods'
      - 'nodes'
      - 'tokenreviews'
      - 'subjectaccessreviews'
      - 'certificatesigningrequests'
      scope: '*'
    sideEffects: None
    timeoutSeconds: 3
    

Remove `nodes`, `tokenreviews`, `subjectaccessreviews`, and `certificatesigningrequests` from the resource section. You can keep `pods` in `resources`.




### Webhooks that block system-critical components

Webhooks that intercept requests to create or update `ClusterRoles` and `ClusterRoleBindings` can interfere with the control plane's ability to reconcile these critical system resources. For example, during a cluster upgrade, the `kube-apiserver` might need to update its system roles. If a webhook that is not available or is misconfigured blocks this update, the `kube-apiserver` will fail to become healthy, which will block the cluster upgrade.

GKE doesn't detect whether webhooks intercept `ClusterRoles` and `ClusterRoleBindings`, so no insight is generated for this scenario.

The following example shows a problematic webhook configuration that intercepts `ClusterRoles`:
    
    
    -   admissionReviewVersions:
      ...
      resources:
      -   'clusterroles'
      -   'clusterrolebindings'
      scope: '*'
    sideEffects: None
    timeoutSeconds: 3
    

To avoid this situation, ensure that your webhooks don't intercept requests for `ClusterRoles` and `ClusterRoleBindings` that have the `system: prefix` setting.

### Admission deadlock

When a webhook is configured to fail closed, it can create a situation where the cluster cannot recover automatically. For example, if all nodes in a cluster are deleted, the webhook will also be down. Because adding a new node requires admission validation, the webhook needs to be available to approve the request. This creates a circular dependency that can prevent the cluster's control plane from recovering.

GKE doesn't detect admission deadlock scenarios, so no insight is generated for this scenario. However, an admission deadlock might occur if webhook Pods are down, in which case GKE detects that the webhook has no available endpoints and generates a `K8S_ADMISSION_WEBHOOK_UNAVAILABLE` insight.

To mitigate this, you can delete the `ValidatingWebhookConfiguration` to break the circular dependency and allow the cluster to recover.

### Cluster control plane availability

When a webhook is configured to fail closed, the availability of the Kubernetes control plane becomes dependent on the availability of the webhook. To improve the availability of the control plane, consider the following:

GKE doesn't detect cluster control plane availability issues caused by webhooks, so no insight is generated for this scenario.

  * **Limit the webhook's scope:** You can exempt critical resources from being validated by the webhook to prevent the webhook from interfering with sensitive processes. You can exempt namespaces or specific kinds of resources. However, be aware of non-obvious dependencies. For example, a `ConfigMap` can be a critical resource for leader election in Kubernetes.

  * **Harden the webhook deployment:** Running the webhook in multiple Pods can increase its resilience and uptime. You can use node selectors to distribute the Pods across different failure domains.




## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders)
  * [Troubleshooting common issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting)
  * [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  * [Learn about feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
