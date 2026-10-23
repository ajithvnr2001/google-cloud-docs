---
url: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/select-a-release-channel/
title: Managed Cloud Service Mesh release channels \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:58.487043+00:00
---

# Managed Cloud Service Mesh release channels  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/select-a-release-channel/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed Cloud Service Mesh release channels

**Deprecated:** Provisioning managed Cloud Service Mesh with asmcli will be deprecated on **Aug 22, 2024** and support will end in **February 2025**. This change only affects Google Cloud clusters. Off-Google Cloud clusters will continue to use asmcli as normal.

Cloud Service Mesh releases updates often, to deliver security updates, fix known issues, and introduce new features. Release channels balance between stability and the feature set of the Cloud Service Mesh version. Cloud Service Mesh release channels are tied to [Google Kubernetes Engine (GKE) release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). Google automatically manages the version and upgrade cadence for each release channel.

**Note:** Managed Cloud Service Mesh consists of the managed control plane and managed data plane. Both components use the same release channel.

This document covers comparisons of release channels, and how to update unmanaged proxies.

### Available release channels

The following release channels are available. Each channel offers a trade-off between feature availability and update churn. Features in each channel have a different maturity level. Critical security patches are delivered to all release channels in order to protect your clusters and Google's infrastructure.

**Channel** | **New managed Cloud Service Mesh availability** | **Properties**  
---|---|---  
Rapid | After each Cloud Service Mesh release | Get the latest Cloud Service Mesh release as early as possible, and be able to use new features the moment they are included in a release. Your control plane is frequently updated to stay on the latest available patch version, and deliver newer capabilities. The Rapid channel is best used to test newer Cloud Service Mesh versions and APIs on pre-production environments.  
Regular | Rapid is promoted to Regular* | Access Cloud Service Mesh and Istio features reasonably soon after they debut, but on a version that has been qualified over a longer period of time. Offers a balance of feature availability and release stability, and is what we recommend for most users.  
Stable | Regular is promoted to Stable* | Prioritize stability over new functionality. Changes and new versions in this channel are rolled out last, after being validated on the Rapid and Regular channels which allows even more time for validation.  
*The promotion schedule to the next channel depends on multiple factors, including the open source Istio release, Anthos release, and patching schedule, and therefore is subject to change. To stay informed with the latest information, add the URL of the [Cloud Service Mesh release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes) to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the feed URL directly: `https://cloud.google.com/feeds/servicemesh-release-notes.xml`  
  
When a minor version of managed Cloud Service Mesh has sufficient usage and demonstrated stability in the Rapid channel, it is promoted to the Regular channel. Eventually, the minor version is promoted to the Stable channel, which only receives high-priority updates and security patches. Each promotion signals a graduating level of stability and production-readiness, based on observed performance of the control plane running that version.

All channels are based on a generally available (GA) release (although individual features may not always be GA, as marked). New Cloud Service Mesh versions are first released to the Rapid channel, and over time are promoted to the Regular, and Stable channel. This allows you to select a channel that meets your business, stability, and functionality needs.

Your cluster's Cloud Service Mesh channel is determined by its GKE cluster channel.

GKE Channel | Cloud Service Mesh Channel  
---|---  
Rapid | Rapid  
Regular | Regular  
Stable | Stable  
(no channel) | Regular  
  
#### Cloud Service Mesh versions per channel

Your Cloud Service Mesh channel is determined by your GKE cluster channel at time of provisioning managed Cloud Service Mesh. If you change the GKE cluster channel later, then you keep the original Cloud Service Mesh channel.

The following table shows the current channel to Cloud Service Mesh version mapping:

Channel | Cloud Service Mesh Version  
---|---  
Rapid | 1.21  
Regular | 1.20  
Stable | 1.19  
  
#### Default channel

In a newly installed Cloud Service Mesh where there is a single managed channel installed in a cluster, that channel will be the default channel for that cluster.

If clusters with an existing Istio or Cloud Service Mesh installation have the default tag configured, then it must be pointed to the managed revision. Otherwise, no action is required.

You can use the `istio-injection=enabled` label as an alias that points injection to the other labels you use for the channel, such as the default revision. Wherever our documentation shows to use the `istio.io/rev` namespace label for injection, it's possible to use the `istio-injection=enabled` label instead.

#### Injection labels

To allow Cloud Service Mesh to manage the workloads in a given namespace, the namespace must be labeled with a label corresponding to the installed channel. Managed Cloud Service Mesh supports two types of labels:

  * standard [revision labels](https://docs.cloud.google.com/service-mesh/docs/revisions-overview#what_is_a_revision), namely `asm-managed-stable`, `asm-managed`, `asm-managed-rapid`, corresponding to the channels `stable`, `regular`, and `rapid`.
  * [default injection label](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) (for example, `istio-injection=enabled`), corresponding to the default channel for that cluster. Using the default injection label simplifies migration between revisions. For example, when [migrating from Istio OSS](https://docs.cloud.google.com/service-mesh/legacy/migrate-istio-operator) or from unmanaged Cloud Service Mesh to managed Cloud Service Mesh, since there is no need to re-label each namespace individually. Wherever Cloud Service Mesh documentation shows to use the `istio.io/rev` namespace label for injection, it's possible to use the `istio-injection=enabled` label instead.



Other examples of injection labels include labelling workloads with `sidecar.istio.io/inject` (commonly used for gateways) and `istio.io/rev`, which works for both namespaces and workloads.

### Default injection labels

To apply the default injection label to a namespace:

**Note:** Although you can also use `istio.io/rev=default` instead of `istio-injection=enabled` as a default injection label, we recommend to standardize around `istio-injection=enabled`.
    
    
    kubectl label namespace NAMESPACE istio-injection=enabled istio.io/rev- --overwrite
    

**Note:** You can ignore the message `"istio-injection not found"` in the output. That means that the namespace didn't previously have the `istio-injection` label, which you should expect in new installations of Cloud Service Mesh or new deployments.

### Revision labels

Like other Kubernetes labels, a revision label is a key-value pair. The key in a revision label is always `istio.io/rev`, but the value varies. To select a release channel, you apply one of the follow revision names to your namespaces:

Revision name | Channel  
---|---  
`asm-managed` | Regular  
`asm-managed-rapid` | Rapid  
`asm-managed-stable` | Stable  
  
For example, to apply the Regular release channel to a namespace:
    
    
    kubectl label namespace NAMESPACE istio.io/rev=asm-managed --overwrite
    

We recommend that you use the same release channel that the cluster uses.

To see what release channel a namespace is using:
    
    
    kubectl get namespace NAMESPACE -o jsonpath='{.metadata.labels.istio\.io/rev}{"\n"}'
    

### Update unmanaged proxies

After each Cloud Service Mesh release, restart the unmanaged proxies for your services and gateways. Although the service mesh is fine when the control plane and proxies are at different versions, we recommend that you update the proxies so that they are configured with the new Cloud Service Mesh version.

  1. Check the [control plane and proxy version](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#verify_control_plane_metrics).

  2. If the control plane version is newer than the proxy version, restart the unmanaged proxies for your services and gateways.
         
         kubectl rollout restart deployment -n NAMESPACE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
