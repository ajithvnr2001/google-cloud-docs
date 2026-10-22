---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/webhooks/
title: Troubleshoot Google Distributed Cloud webhook issues \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:18.298085+00:00
---

# Troubleshoot Google Distributed Cloud webhook issues  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/webhooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot Google Distributed Cloud webhook issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with problematic or unsafe webhooks in Google Distributed Cloud.

## Types of problematic webhooks

Admission webhooks, or _webhooks_ in Kubernetes, are a type of [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) that can be used in Kubernetes clusters to validate or mutate requests to the control plane prior to a request being persisted. It is common for third-party applications to use webhooks that operate on system-critical resources and namespaces. Incorrectly configured webhooks can impact control plane performance and reliability. For example, an incorrectly configured webhook created by a third-party application could prevent Google Distributed Cloud from creating and modifying resources in the managed `kube-system` namespace, which could degrade the functionality of the cluster.

Problematic webhooks include the following types:

  * **Webhooks that operate, but have no endpoints available.** Follow the instructions to check webhooks with no available endpoints.
  * **Webhooks that are considered unsafe as they operate on system critical resources and namespaces.**

The following webhooks are considered unsafe:

    * Webhooks that intercept Pods and leases in the `kube-system` namespace.
    * Webhooks that intercept leases in the `kube-node-lease` namespace.
    * Webhooks that intercept [`Nodes`](https://kubernetes.io/docs/concepts/architecture/nodes/), [`TokenReviews`](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/), [`SubjectAccessReviews`](https://kubernetes.io/docs/reference/access-authn-authz/authorization/), and [`CertificateSigningRequests`](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) resources.

Follow the instructions to check webhooks that are considered unsafe.




## Webhooks that have no available endpoints

If a webhook has no available endpoints, the Service that backs the webhook endpoint has one or more Pods which aren't running. To make the webhook endpoints available, follow the instructions to find and troubleshoot the Pods of the Service that is backing this webhook endpoint:

  1. Find the serving Pods for the Service associated with the webhook. Run the following command to describe the Service:
         
         kubectl describe svc SERVICE_NAME -n SERVICE_NAMESPACE
         

Replace the following:

     * SERVICE_NAME with the name of the Service.
     * SERVICE_NAMESPACE with the name of the namespace.

If you can't find the Service name listed in the webhook, the unavailable endpoint might be caused by a mismatch between the name listed in the configuration and the actual name of the Service. To fix the endpoint availability, update the Service name in the webhook configuration to match the correct Service object.

  2. Inspect the serving Pods for this Service. Identify which Pods aren't running by listing the Deployment:
         
         kubectl get deployment -n SERVICE_NAMESPACE
         

Or, run the following command to list the Pods:
         
         kubectl get pods -n SERVICE_NAMESPACE -o wide
         

For any Pods that aren't running, inspect the Pod logs to see why the Pod isn't running.




## Webhooks that are considered unsafe

If a webhook intercepts any resources in system-managed namespaces, we recommend that you update the webhooks to avoid intercepting these resources.

  1. Inspect the webhook configuration. Run the following `kubectl` command to get the webhook configuration:
         
         kubectl get validatingwebhookconfigurations CONFIGURATION_NAME -o yaml
         

Replace CONFIGURATION_NAME with the name of the webhook configuration.

If this command doesn't return anything, run the command again, replacing `validatingwebhookconfigurations` with `mutatingwebhookconfigurations`.

In the `webhooks` section of the output, one or more webhooks are listed.

  2. Edit the configuration, depending on the reason the webhook is considered unsafe:

#### Exclude kube-system and kube-node-lease namespaces

A webhook is considered unsafe if `scope` is `*`, or if scope is `Namespaced` and either of the following conditions are true:

     * The `operator` condition is `NotIn` and `values` omits `kube-system` and `kube-node-lease`, as in the following example:
           
           webhooks:
           - admissionReviewVersions:
             ...
             namespaceSelector:
               matchExpressions:
               - key: kubernetes.io/metadata.name
                 operator: NotIn
                 values:
                 - blue-system # add 'kube-system' and 'kube-node-lease' if `NotIn`
             objectSelector: {}
             rules:
             - apiGroups:
               ...
               scope: '*' # 'Namespaced'
             sideEffects: None
             timeoutSeconds: 3
           

Ensure that `scope` is set to `Namespaced`, not `*`, so that the webhook only operates in specific namespaces. Ensure that if `operator` is `NotIn`, `kube-system` and `kube-node-lease` are included in `values`.

     * The `operator` condition is `In` and `values` includes `kube-system` and `kube-node-lease`, as in the following example:
           
           namespaceSelector:
               matchExpressions:
               - key: kubernetes.io/metadata.name
                 operator: In
                 values:
                 - blue-system
                 - kube-system # remove as operator is `In`
                 - kube-node-lease # remove as operator is `In`
           

Ensure that `scope` is set to `Namespaced`, not `*`, so that the webhook only operates in specific namespaces. Ensure that if `operator` is `In`, `kube-system` and `kube-node-lease` are not included in `values`.

#### Exclude matched resources

A webhook is also considered unsafe if `nodes`, `tokenreviews`, `subjectaccessreviews`, or `certificatesigningrequests` are listed under resources, as in the following example:
    
    - admissionReviewVersions:
    ...
        resources:
        - 'pods' # keep, remove everything else
        - 'nodes'
        - 'tokenreviews'
        - 'subjectacessreviews'
        - 'certificatesigningrequests'
        scope: '*'
      sideEffects: None
      timeoutSeconds: 3
    

Remove `nodes`, `tokenreviews`, `subjectaccessreviews`, and `certificatesigningrequests` from the resource section.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
