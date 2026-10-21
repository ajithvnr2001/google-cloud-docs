---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-new-features/
title: GKE release notes (new features) \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:12.010624+00:00
---

# GKE release notes (new features)  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-new-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release notes (new features) Stay organized with collections  Save and categorize content based on your preferences. 

This page documents new features in Google Kubernetes Engine (GKE). You can periodically check this page for new feature announcements. The overall [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) also include the information in this page. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gke-new-features-release-notes.xml) directly. 

## October 19, 2026

Feature

You can now provision GKE nodes from storage-optimized [Z4M machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series):

  * Manually: starting from GKE version 1.36.3-gke.1767000 and later.
  * Using compute classes, cluster autoscaler, node pool auto-creation and in Autopilot clusters: starting from GKE version 1.37.0-gke.4713000 and later.



Z4M machine series are suited for large parallel file systems to support AI/ML workloads and for I/O intensive workloads such as databases. GKE does not support Z4M bare metal instances at this time. See [Machine support with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-support#machine-support).

## October 07, 2026

Feature

The microVM sandbox type is now Generally Available (GA) with GKE Sandbox in clusters that run version 1.37.0-gke.4713000 and later. MicroVM sandboxes provide hardware virtualization and isolation for untrusted workloads, AI agent runtimes, and multi-tenant environments. GKE microVM sandboxes use Kata Containers and Cloud Hypervisor to provide this isolation while maintaining a full Linux kernel that includes standard Linux features

For more information, see the [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) documentation.

## October 05, 2026

Feature

GKE support for using the `c4-standard-*` machine types (up to 192 vCPUs) as Confidential GKE Nodes with Intel TDX is generally available. For more information, see the following pages:

  * To use this feature with GKE , see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).
  * To learn more about the feature from Compute Engine, see [Confidential VM overview](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).
  * To see supported configurations, including machine support, see [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) and its "Machine types, CPUs, and zones" section.



## October 02, 2026

Feature

You can use Vertical Pod Autoscaler (VPA) with Horizontal Pod Autoscaler (HPA) to automatically optimize container CPU requests for workloads that scale replicas based on CPU utilization. This feature is available in Public Preview on clusters running GKE version 1.36.3-gke.1630000 or later. For more information, see [Rightsize HPA workloads with VPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rightsize-hpa-workloads-with-vpa).

## September 30, 2026

Feature

GKE now automatically applies protection tier labels to TPU node pools created from Compute Engine reservations. Depending on your configuration, GKE adds:

  * Node pool resource label: `goog-gke-node-pool-protection-tier` (`standard` or `capacity_optimized`)
  * Kubernetes node label: `cloud.google.com/protection-tier` (`STANDARD` or `CAPACITY_OPTIMIZED`)



To learn more, see [Automatically applied labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#automatically-applied-labels).

## September 28, 2026

Feature

The storage-optimized [Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) is available with GKE clusters running 1.36.3-gke.1244000 or later. You can use Z4D machine types in Standard or Autopilot mode. For more information about limitations for this machine series in GKE, see [About machine support with GKE clusters](https://docs.cloud.google.com//kubernetes-engine/docs/concepts/machine-support#machine-support).

## September 25, 2026

Feature

GKE Standard clusters now support up to 512 maximum Pods per node, an increase from the previous limit of 256. Nodes configured for 257 to 512 Pods will now be allocated a /22 Pod CIDR block (1,024 IP addresses).

## September 24, 2026

Feature

GKE ambient networking is now available in [Preview](https://cloud.google.com/products#product-launch-stages) through an allowlist.

GKE ambient networking provides a simplified, sidecarless deployment model for a service mesh with Layer 4 capabilities. By moving proxy functionality to node-level components integrated into [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2), ambient networking reduces resource overhead, eliminates workload restarts for proxy updates, and simplifies mesh lifecycle management.

The Preview release supports single-cluster Layer 4 mesh capabilities using the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api), which includes mutual TLS (mTLS), service discovery, Layer 4 traffic management, and Layer 4 telemetry.

For more information, see [Ambient networking overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ambient-overview) and [Prepare GKE ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking).

## September 11, 2026

Feature

Agent Substrate on GKE is now available for evaluation and non-production use. Production support is offered on an allowlist basis under a limited GA program.

Agent Substrate runs agentic workloads at scale on GKE clusters. To reduce resource usage, Agent Substrate suspends idle agents and takes a snapshot of the agent's active memory (RAM) and local files. When a suspended agent is triggered, the system restores the agent's state onto an available sandbox with sub-second latency.

Agent Substrate improves on the capabilities of Agent Sandbox by bypassing the bottlenecks of the standard Kubernetes control plane to run significantly more concurrent agents per machine.

For more information, see [About GKE Substrate](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-substrate/about-agent-substrate).

## September 04, 2026

Feature

#### New features in 1.37

  * The [PodCertificateRequest](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#pod-certificate-requests) and [ClusterTrustBundle](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#cluster-trust-bundles) APIs are generally available and promoted to certificates.k8s.io/v1.
  * [DRA device metadata publishing](https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/) is enabled with beta support (for use with DRA drivers which include this feature).
  * HorizontalPodAutoscaler enables beta support for [scaling to zero](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#scaling-to-and-from-zero).
  * [StatefulSet maxUnavailable support](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#maximum-unavailable-pods) is now enabled.



## September 03, 2026

Feature

GKE support for using the `c3-standard-*-lssd` machine types as Confidential GKE Nodes with Intel TDX is generally available. For more information, see the following:

  * To use this feature with GKE, see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).
  * To learn more about the feature from Compute Engine, see [Confidential VM overview](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).
  * To see supported configurations, including machine support, see [Supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) and its "Machine types, CPUs, and zones" section.



## September 01, 2026

Feature

The bare metal machine types from the [C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) are now generally available with GKE clusters. You can now provision machine types such as `c3-standard-192-metal` in Standard mode with any available GKE version.

To use these machine types with Autopilot mode, ComputeClasses, and node pool auto-creation, you must specify the exact machine type using a custom ComputeClass and use GKE version 1.35.3-gke.1389000 or later.

## August 31, 2026

Feature

Session affinity support using GCPTrafficDistributionPolicy for GKE Gateway is generally available. This release currently supports single-cluster GKE Gateway load balancers using the following GatewayClasses:

  * `gke-l7-rilb`
  * `gke-l7-regional-external-managed`
  * `gke-l7-global-external-managed`



In addition to the session affinity types available in Preview, you can now use the `STRONG_COOKIE_AFFINITY` type, which provides the most persistent session stickiness among the session affinity types available in Google Cloud Application Load Balancers.

The session affinity types require the following minimum GKE versions:

  * `CLIENT_IP`, `HEADER_FIELD`, `GENERATED_COOKIE`, and `HTTP_COOKIE`: version 1.35.2-gke.1269001 or later
  * `STRONG_COOKIE_AFFINITY`: version 1.36.3-gke.1767000 or later



For more information, see [Configure session affinity using GCPTrafficDistributionPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#expanded-session-affinity).

## August 27, 2026

Feature

Network Endpoint Group (NEG) pre-provisioning is now available in Preview. With this feature, you can force the creation of empty zonal `GCE_VM_IP_PORT` NEGs in specified zones (or all zones within a region) during Service creation, regardless of whether the cluster has nodes in those zones. By extending the `cloud.google.com/neg` Service annotation with a custom zones parameter, you can seamlessly automate infrastructure deployments (such as attaching NEGs to backend services) without waiting for workloads to deploy. For more information, see [Pre-provisioning empty NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg#pre-provisioning).

## August 26, 2026

Feature

In GKE version 1.36 and later, GCPAuthzPolicy and GCPAuthzExtension resources for GKE Gateway are now available in Preview. You can use these resources to enforce identity-based access control and zero-trust authorization on incoming traffic at the Gateway layer. These capabilities are supported on the following GatewayClasses:

  * gke-l7-global-external-managed
  * gke-l7-regional-external-managed
  * gke-l7-rilb



For more information, see [Configure the GCPAuthzExtension resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcp-authz-ext).

## August 05, 2026

Feature

You can generate optimized GKE configurations that can improve performance for specific workloads, such as Redis and MySQL, by using the gcloud CLI. The configurations are ConfigMaps and ComputeClasses that apply performance recommendations to the workloads and the nodes. These optimizations are available in Preview for GKE version 1.31.1-gke.12000 or later. You can measure the performance improvements by using open source benchmarks. For more information, see [Optimize for workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-optimization).

Feature

In GKE version 1.36.0-gke.3302001 and later, you can run Arm workloads on the Autopilot container-optimized compute platform by using the general-purpose `autopilot-arm` and `autopilot-arm-spot` ComputeClasses. You can select these ComputeClasses in Autopilot or Standard clusters. GKE runs the workloads that select these ComputeClasses in Autopilot mode. This compute platform improves Pod scheduling latency, especially during autoscaling operations. For more information, see the following documents:

  * [Deploy workloads in Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#deploy-workloads)
  * [Autopilot Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads)



## August 03, 2026

Feature

TPU Subslicing (also known as Dynamic Subslicing) is now generally available for Ironwood (TPU7x). This feature enables you to incrementally provision node pools for a cube or litepod, breaking them into smaller slices (subslices) to run workloads requiring smaller topologies. Updates in this GA release include:

  * **Dynamic sub-slicing** (topologies smaller than `4x4x4`, such as `2x2x1`, `2x2x2`, `2x2x4`, and `2x4x4`): Supported in GKE version `1.36.0-gke.3712000` or later.
  * **Dynamic super-slicing** (topologies `4x4x4` or larger): Supported in GKE version `1.35.2-gke.1842000` or later.
  * **Partition Health Labels** : The partition state label is updated to `cloud.google.com/gke-tpu-partition-[shape]-state` to specify smaller subslice shapes. It also introduces `UNSET` and `INCOMPLETE` states. Support for the `DEGRADED` state only applies to the top-level `4x4x4` topology, and not for smaller sub-slicing topologies.



For more information, see [About GKE dynamic slicing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing).

## July 28, 2026

Feature

GKE now supports opting out of the default `kubernetes.io/arch=arm64:NoSchedule` taint on Arm nodes in Standard node pools and in custom ComputeClasses. To opt out of the default taint, set the `--node-architecture-taint-behavior` gcloud CLI flag to `NONE` for a node pool or set the `taintConfig.architectureTaintBehavior` field to `NONE` for a ComputeClass. By configuring this behavior, you allow workloads that lack explicit Arm tolerations to be scheduled on Arm-based machine families (such as N4A and C4A). This is useful for running multi-architecture workloads or simplifying scheduling in mixed-mode clusters. For more information, see [Configure the default Arm architecture taint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint).

Feature

GKE Gateway and Inference Gateway now support Cross-Origin Resource Sharing (CORS). You can configure a CORS filter directly on an `HTTPRoute` resource by using the portable syntax standardized by [Gateway API](https://gateway-api.sigs.k8s.io/guides/user-guides/http-cors/). This feature is available in Preview in GKE version 1.35 and later for the following GatewayClasses:

  * `gke-l7-rilb`
  * `gke-l7-regional-external-managed`
  * `gke-l7-global-external-managed`



For more information, see [Configure Cross-Origin Resource Sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors).

## July 27, 2026

Feature

In GKE version 1.36 and later, GKE Dataplane V2 with NetworkPolicies supports up to 15,000 nodes per cluster, increased from the previous limit of 7,500 nodes. For clusters exceeding 5,000 nodes, contact Cloud Customer Care to request a quota increase. For more information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).

Feature

In version 1.36.2-gke.1498000 and later, GKE supports mixed-protocol Services of type LoadBalancer in general availability (GA). Mixed-protocol Services let both external (NetLB) and internal (ILB) passthrough Network Load Balancers handle simultaneous TCP and UDP traffic on a single IP address across IPv4, IPv6, and dual-stack environments.

## July 16, 2026

Feature

In GKE version 1.36.0-gke.3204000 and later, when you manually or automatically create a GKE node pool that consumes capacity reservations, you can stop GKE from falling back to on-demand capacity if reserved capacity isn't available. To consume any matching reservation without fallback, specify the `any-reservation-then-fail` reservation affinity in your node pool creation request, Pod specification, or ComputeClass specification. In ComputeClasses, this reservation affinity lets GKE move on to the next priority rule instead of creating on-demand compute resources. For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

Feature

GKE version 1.33 now supports the N4D machine series for node pool auto-creation and Autopilot clusters in the following patch versions and later:

  * **Node pool auto-creation** : 1.33.12-gke.1208000 and later
  * **Autopilot** : 1.33.13-gke.1079000 and later



Feature

In GKE version 1.36.0-gke.4447000 and later, the VerticalPodAutoscaler supports [CPU startup boost](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#cpu-startup-boost), which temporarily increases CPU requests during application startup to improve startup latency and cost efficiency. This feature is available in Preview.

## July 14, 2026

Feature

Rollout sequencing with custom stages is now generally available. This version of rollout sequencing, which is recommended if you're configuring an environment for the first time, offers a robust set of features including the following:

  * **Define custom stages** : Sequence the rollout of a new GKE version across environments. With custom stages, you can, for example, deploy a new version on a small subset of production clusters before a wider rollout.
  * **Choose the scope of rollouts** : Decide what types of versions that GKE rolls out in the sequence. For example, you can have GKE roll out patch versions, but not minor versions, across a sequence.
  * **Initiate a rollout** : Create a rollout of a specific version, if you want GKE to roll out that version across your sequence.
  * **Manage a rollout** : Pause, resume, cancel rollouts, or complete rollout stages as needed.



For more information, see [About rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).

## July 08, 2026

Feature

The network-optimized [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) is available with GKE clusters running 1.36.0-gke.3009002 or later. You can use C4N machine types in Standard or Autopilot mode.

## July 07, 2026

Feature

In GKE version 1.34 and later, you can configure Google Cloud Managed Service for Prometheus to collect Pressure Stall Information (PSI) metrics from cAdvisor. You can use PSI metrics to monitor CPU, memory, and I/O congestion and stall times for your containers, Pods, and nodes. For more information, see [Collect specific Prometheus metrics from Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics).

Feature

In GKE version 1.35.3-gke.1389000 and later, you can run GPU workloads on Confidential GKE Nodes with certain G4 machine types and NVIDIA RTX PRO 6000 GPUs. This feature is available in Preview. For more information, see [Encrypt GPU workload data in use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes).

Feature

In GKE version 1.36.0-gke.1601000 and later, you can enable the logging of VerticalPodAutoscaler decisions in Cloud Logging. You can use these logs to understand why specific vertical Pod autoscaling decisions were made. This feature is available in Preview. For more information, see [Collect vertical Pod autoscaler event logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events).

Feature

GKE Gateway now supports backend mutual TLS (mTLS). In addition to backend authenticated TLS, backend mTLS allows the GKE Gateway load balancer to authenticate its identity to backend Pods by presenting a client certificate. GKE Gateway configures backend mTLS using the standard Gateway API `spec.tls.backend.clientCertificateRef` field.

This feature is supported for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-regional-external-managed`
  * `gke-l7-rilb`



For more information, see [Configure backend mutual TLS (mTLS) for a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-mtls).

## June 04, 2026

Feature

GKE Gateway now supports frontend mTLS (client certificate validation). Frontend mTLS allows the Gateway to authenticate client-presented certificates. This feature is available for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-regional-external-managed`
  * `gke-l7-rilb`



For more information, see [Configure frontend mTLS for a Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-frontend-mtls).

## June 02, 2026

Feature

GKE is introducing the following changes to expand the capabilities of maintenance exclusions:

  * **Per-node pool maintenance exclusions** : Available in release channels, these replicate the functionality of disabling node pool auto-upgrades when your cluster isn't enrolled in a release channel.
  * **Extended "No upgrades" exclusion** : The "No upgrades" default maintenance exclusion can now be up to 90 days long.



For more information, see [Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).

## May 29, 2026

Feature

GKE Gateway now supports backend authenticated TLS for Gateway-originated connections to Pods or InferencePools for the following GatewayClasses:

  * `gke-l7-global-external-managed`
  * `gke-l7-regional-external-managed`
  * `gke-l7-rilb`



## May 28, 2026

Feature

C4A bare metal instances are generally available with GKE clusters. For more information, see the [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke) document, including the "Requirements and limitations" section for specific version requirements.

Feature

[Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#confidential-gke-nodes) now support cluster level enablement of [AMD SEV-SNP](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#amd_sev-snp) and [Intel TDX](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#intel_tdx) on GKE Autopilot.

Feature

In GKE versions 1.36.0-gke.2459000 and later, you can directly configure Cloud Logging for L4 load balancer backend services by using the L4LBConfig CustomResourceDefinition (CRD).

This feature is available for the following load balancer types:

  * [Internal L4 load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable-logging) with subsetting enabled.
  * [External L4 load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer#enable-logging) with regional backend services (RBS) enabled.



## May 25, 2026

Feature

To monitor the efficiency of the GKE training JobSet, the following two GKE system metrics are available in Preview:

  * `kubernetes.io/jobset/scheduling_goodput`: the fraction of time that all the resources required to run the training JobSet are available.
  * `kubernetes.io/jobset/proxy_runtime_goodput`: the fraction of time that all required accelerators are productive. This metric provides an estimate of the real runtime goodput.



For details about GKE metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes). For details about goodput metrics that are used to measure efficiency, see [Monitor goodput with the ML Goodput Measurement library](https://docs.cloud.google.com/tpu/docs/goodput#jobset-dashboard).

You can also view these new GKE metrics in the [JobSet monitoring dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue#monitor_the_workloads).

## May 14, 2026

Feature

GKE now supports concurrent node pool upgrades for clusters (Preview). By default, GKE automatically upgrades one node pool at a time. To decrease the total time required to upgrade your cluster, you can now configure the maximum number of node pools that GKE auto-upgrades simultaneously. This feature is supported for both Standard and Autopilot clusters. For more information, see [Configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades).

Feature

Managed OpenTelemetry on GKE now supports the collection of multimodal prompts and responses (Preview) for LangGraph and Agent Development Kit (ADK) agents. You can view and analyze the data in the Trace Explorer and BigQuery platforms. For more details, see [Collect multimodal prompts and responses data](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#multimodal-prompts-responses).

## May 06, 2026

Feature

GKE Pod Snapshots is generally available on clusters that run version 1.35.3-gke.1234000 or later. For more information, see [About GKE Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots).

Feature

In GKE Standard clusters, [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) is now supported on Confidential GKE Nodes that use [C3D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machines) with [AMD SEV](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#amd_sev) enabled.

## May 01, 2026

Feature

#### New features in 1.36

  * [L4 Internal Load Balancer services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing) now use GKE subsetting by default. This change transitions the default implementation from Instance Groups to Network Endpoint Groups (NEGs). This NEG-based approach provides improved scalability and enhanced performance through faster synchronization. This change applies only to newly created Internal Load Balancer services, while existing services remain unaffected and continue using Instance Groups.
  * [Mutating Admission Policies](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/) are now Generally Available. Mutating admission policies allow for resource mutations using Common Expression Language (CEL) expressions as a more efficient alternative to mutating admission webhooks. For more information, see the [kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/).
  * The kube-dns image switches from an implementation based on [kubernetes/dns](https://github.com/kubernetes/dns) to one based on [CoreDNS](https://coredns.io/). This implementation is more efficient, and it supports bigger headless services, more upstream DNS services, and more concurrent connections.



## April 27, 2026

Feature

Google Kubernetes Engine now offers support for AI zones. To learn more, see [AI zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#ai-zones).

## April 21, 2026

Feature

For clusters running GKE version 1.35.3-gke.1389000 or later, you can now use the `c4a-highmem-96-metal` ([Preview](https://cloud.google.com/products#product-launch-stages)) machine type from the C4A machine series with the following features:

  * [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode
  * [Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#cluster-level-enablement)
  * [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) that auto-create node pools
  * [Cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)



Feature

Starting in GKE version 1.35.2-gke.1842000, you can install the Slurm Operator add-on for GKE ([Preview](https://cloud.google.com/products#product-launch-stages)). This managed installation of the Slurm Operator allows you to enable Slurm scheduling capabilities on any GKE cluster. The add-on provides the foundation to build customized AI and HPC platforms, including CPU, GPU, and TPU machines (covering specific scenarios). For more information, see [About Slurm on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/concepts/overview).

## April 20, 2026

Feature

Accelerator network profile is Generally Available (GA), simplifying your AI/ML node pool setup. Accelerator network profile automates networking configuration, including the creation of necessary VPCs and subnets, removing the need for complex, manual steps previously required for configuring GPU and TPU workloads. For details, see [Configure automated networking for accelerator VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/config-auto-net-for-accelerators).

## April 08, 2026

Feature

[Gateway API v1.5](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.5.0) is supported in GKE version 1.35.2-gke.1842000 and later. The GKE Gateway controller passes core conformance tests for this version of the Gateway API.

Feature

GKE managed DRANET is now Generally Available (GA) for GKE version 1.35.2-gke.1842000 or later.

GKE DRANET is a managed feature that implements the Kubernetes Dynamic Resource Allocation (DRA) API for high-performance networking. The GA release expands support beyond the preview phase to include the following hardware:

  * NVIDIA GPU Instances: Support for instances starting from A3 Ultra, including A4, A4X, and A4X Max.
  * Cloud TPU Instances: Support for TPU v6e and TPU v7x.



For more information, see [Allocate network resources by using GKE managed DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra).

## March 25, 2026

Feature

To provide more controls over the control plane version upgrade, you can now do the following:

  * Configure a frequency of disruption from auto-upgrades by using the cluster disruption budget. For more information, see [Control the frequency of disruption from auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget).
  * Continue using an existing control plane patch for a longer period, which facilitates large-scale upgrade and downgrade operations. For more information, see [Patch version support](https://docs.cloud.google.com/kubernetes-engine/versioning#patch-version-support).



## March 13, 2026

Feature

In GKE version 1.35 and later, all organization and cluster administrators can granularly control which privileged Autopilot partner workloads can run in GKE clusters. Additionally, approved customers can authorize and run their own privileged workloads in Autopilot mode by using custom allowlists.

For more information, see [About Autopilot privileged workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads).

## March 10, 2026

Feature

Managed OpenTelemetry for GKE is available in Preview for clusters running version 1.34.1-gke.2178000 or later. Managed OpenTelemetry for GKE provides a fully managed and simplified experience for collecting OpenTelemetry Protocol (OTLP) traces, metrics, and logs on GKE. This feature includes the following characteristics:

  * **Managed collection:** an in-cluster OTLP endpoint that automatically routes telemetry to the Cloud Telemetry API.
  * **Automatic configuration:** a new Instrumentation custom resource that automatically injects environment variables into your workloads to simplify OTLP ingestion.



For more information, see [Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-otel-gke).

## March 05, 2026

Feature

GKE Inference Quickstart (GIQ) now offers recommendations for distributed AI inference. This enables you to deploy optimized, full configurations for advanced models, such as the Qwen and gpt-oss model families, on NVIDIA GPUs and Cloud TPUs.

This release introduces GKE Inference Gateway by integrating llm-d inference scheduling. You can select optimized configurations for workloads like Advanced Customer Support, Code Completion, and Deep Research. This tunes your infrastructure to meet the specific latency and throughput requirements of these applications.

For more information, see [Analyze model serving performance and costs with Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).

Feature

You can use automated disk type selection for Hyperdisk volumes on GKE. This feature allows GKE to automatically select the most appropriate disk type based on the machine type of the node where your workload is scheduled.

With this feature, you can create a single StorageClass that supports clusters with mixed VM generations. For example, GKE can provision Hyperdisk on compatible instances (such as C3 or C4) while automatically falling back to Persistent Disk on other generations.

For more information, see [Automated disk type selection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection).

Feature

The [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series), designed for high performance computing (HPC) workloads, is generally available for GKE clusters. Based on 5th generation AMD EPYC Turin with Cloud RDMA 200 Gbps networking, H4D VMs offer 192 cores (SMT disabled), up to 1,488 GB of memory, and 3,750 GiB of Local SSD. H4D is optimized for tightly-coupled applications that scale across multiple nodes and offers RDMA-enabled 200 Gbps networking.

You can use H4D with GKE clusters in Standard, or with the Performance compute class in Autopilot. For more information, see [Run high performance computing (HPC) workloads with H4D](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads).

## February 24, 2026

Feature

The release note for [November 11, 2025](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#November_11_2025) has been updated to correct the version requirements for using N4D machine types. Cluster autoscaler was incorrectly included in the list of features requiring GKE version 1.34.1-gke.2037000 or later. You can use any available GKE version to use N4D and Cluster autoscaler.

Feature

You can create a bare metal instance from the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) with the `c4a-highmem-96-metal` machine type. This machine type is available in Public Preview for Standard clusters running GKE version 1.35.0-gke.2232000 or later. You can select this machine type by using the `--machine-type` flag when creating a cluster or node pool. For more information about the requirements and limitations of this machine type, see the [Requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations) section of the "Arm workloads on GKE" document.

## February 13, 2026

Feature

You can now determine the status and health of a TPU slice and partition by monitoring these new beta system metrics:

  * `kubernetes.io/accelerator/slice/state`: Indicates the current status of the slice.
  * `kubernetes.io/accelerator/partition/state`: Indicates the health of the partition.



For more information, see the [GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) documentation.

## February 05, 2026

Feature

Image streaming is now available in the `asia-southeast3` region. For more information, see the [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) documentation.

## February 03, 2026

Feature

Image streaming and secondary boot disks are now generally available (GA) for nodes using the Ubuntu with containerd (`UBUNTU_CONTAINERD`) image type. These features improve workload startup performance on GKE Standard and Autopilot clusters through image data streaming and preloaded disk data. To use these features on Ubuntu nodes, your cluster must be running GKE version 1.35.0-gke.1403000 or later.

For more information, see the documentation for [Image Streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) and [Using Secondary Boot Disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading).

## January 27, 2026

Feature

Stream Control Transmission Protocol (SCTP) support on GKE Dataplane V2 is now generally available (GA). You can now deploy workloads that use SCTP on GKE Standard clusters. This feature enables direct SCTP communication for Pod-to-Pod and Pod-to-Service traffic.

SCTP support requires clusters to use GKE Dataplane V2 and Ubuntu node images. This feature is available in GKE version 1.32.2-gke.1297000 or later.

For more information, see [Deploy workloads with SCTP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-workloads-with-sctp).

## January 26, 2026

Feature

The [N4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series) is generally available for GKE clusters in Autopilot and Standard modes. For more information, see [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

## January 21, 2026

Feature

You can now determine which Kubernetes JobSets are scheduled on which GKE node pools and nodes by monitoring the new generally available system metrics:

  * `kubernetes.io/jobset/assigned_node_pools`: GKE node pools where a Kubernetes JobSet has scheduled Pods.
  * `kubernetes.io/jobset/assigned_nodes`: GKE nodes where a Kubernetes JobSet has scheduled Pods.
  * `kubernetes.io/node_pool/assigned_jobsets`: Kubernetes JobSets that have scheduled Pods on a GKE node pool.
  * `kubernetes.io/node/assigned_jobsets`: Kubernetes JobSets that have scheduled Pods on a GKE node.



## January 20, 2026

Feature

The `asia-southeast3` region in Bangkok, Thailand is available. For more information, see the [Global Locations](https://cloud.google.com/about/locations/).

## January 07, 2026

Feature

NodeLocal DNSCache is enabled by default on new Standard GKE clusters which are created running version 1.34.1-gke.3720000 or later. NodeLocal DNSCache is a GKE add-on that improves DNS performance by running a DNS cache directly on each cluster node as a DaemonSet. To learn more, see [Set up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).

## December 29, 2025

Feature

#### New features in 1.35

  * **In-place Pod Resize:** [In-place Pod Resize](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) is now GA. This feature allows Pod CPU and memory requests and limits to be modified in-place without Pod or container restart.
  * **Writable cgroups:** GKE [Writable cgroups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/writable-cgroups) for containers is now GA. This feature allows workloads to manage resources for child processes using the Linux cgroups API, improving reliability for applications like [Ray](https://www.ray.io/).



## December 19, 2025

Feature

Rollout sequencing with custom stages is now available in Preview. This feature offers granular control over upgrading groups of clusters within a fleet, allowing you to progressively roll out GKE versions across environments. For more information see [About rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).

## December 15, 2025

Feature

GKE Autopilot now supports N4A machine types in Public Preview, available on clusters running version 1.34.1-gke.3403001 or later.

## December 10, 2025

Feature

In GKE version 1.34.1-gke.2541000 and later, you can specify secure tags for firewalls in the [`spec.nodePoolConfig.resourceManagerTags` field](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#resourceManagerTags) in ComputeClasses. GKE adds those secure tags to the nodes that GKE creates for that ComputeClass, so that you can target nodes by using these tags in firewall policies. For more information, see [Selectively enforce firewall policies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies).

## November 27, 2025

Feature

TPU7x (Ironwood), Google's seventh-generation TPU for large-scale AI workloads, is available in [Preview](https://cloud.google.com/products#product-launch-stages) in GKE Standard clusters that run version 1.34.0-gke.2201000 and later, and in Autopilot clusters that run version 1.34.1-gke.3084001 and later. TPU7x offers a significant performance increase compared to previous generations, with 2307 TFLOPs of BF16 performance and 192 GB of high-bandwidth memory (HBM) per chip. For more information, see [Get started with Ironwood (TPU7x)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#ironwood-benefits).

## November 24, 2025

Feature

Fast-starting nodes are now generally available. GKE provisions fast-starting nodes on a best-effort basis in Autopilot when workloads use compatible configurations. For more information, see [About quicker workload startup with fast-starting nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes).

## November 17, 2025

Feature

NVIDIA recommends that Kubernetes clusters enable Coherent Driver-Based Memory Management (CDMM) to resolve memory over-reporting. CDMM is enabled by default on A4X nodes running the R580 GPU driver in GKE clusters with the following versions:

  * **1.33 or later** : 1.33.4-gke.1036000 or later
  * **1.32** : 1.32.8-gke.1108000 or later



CDMM allows GPU memory to be managed through the driver instead of the operating system (OS), avoiding OS onlining of GPU memory, and exposing the GPU memory as a Non-Uniform Memory Access (NUMA) node to the OS.

For more information about CDMM, see [Hardware and Software Support](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-65-06/index.html#hardware-software-support). To create GKE clusters with A4X, see the following documents:

  * [Create an AI-optimized GKE cluster with default configuration](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
  * [Create a custom AI-optimized GKE cluster which uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom-a4x)



## November 11, 2025

Feature

This note was updated on February 24, 2026. Cluster autoscaler was incorrectly included in the list of features which required 1.34 support with N4D. The correct features are now listed as follows.

The N4D machine family is now Generally Available (GA) for Standard and Autopilot mode. N4D instances are powered by the fifth generation AMD EPYC SP5 processors (Turin). The N4D machine series is available as follows:

  * **Compute classes, node pool auto-creation, and Autopilot mode** : GKE version 1.34.1-gke.2037000 and later.
  * **Manually created node pools in Standard mode** : all available GKE versions.



For more information, see [N4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series).

## November 07, 2025

Feature

**Important:** This note is incorrect. For the correct note, see the entry for [April 8, 2026](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#April_08_2026).

In GKE version 1.34.1-gke.2037001 and later, the GKE logging agent in your clusters can process logs up to two times faster per node than in version 1.33 and earlier. The logging agent also uses less node resources, which improves efficiency especially if you use [high-throughput logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput#enable). These improvements to the logging agent are automatically enabled in version 1.34.1-gke.2037001 and later.

Feature

In version 1.34.1-gke.1829001 and later, GKE can [auto-create](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) multiple node pools concurrently to improve the speed with which multiple new node pools become ready.

Feature

In GKE version 1.35 and later, GKE rejects anonymous requests to cluster endpoints (except for the `livez`, `/healthz`, and `/readyz` health check endpoints) by default for all new Autopilot or Standard clusters. Existing clusters aren't affected by this change. To allow anonymous requests to cluster endpoints, explicitly specify a value of `ENABLED` in the `--anonymous-authentication-config` flag or the `AnonymousAuthenticationConfig.mode` API field. For more information, see [Restrict anonymous access to cluster endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict-anon-access).

## October 31, 2025

Feature

The Multi-Cluster Services (MCS) feature has been updated with a finalizer to more effectively prevent potential resource leaks and ensure a full cleanup during the feature's disablement process. As a result of this improvement, the disablement procedure has been updated. For more details on how to disable MCS, see [Disabling MCS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#disabling_mcs).

## October 28, 2025

Feature

Autoscaled blue-green upgrades are a type of node upgrade strategy that maximizes the amount of time before disruption-intolerant workloads are evicted, while minimizing cost. This feature is available in Preview for GKE Standard node pools. For more information, see [Autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy).

Feature

You can use the G4 VM, powered by NVIDIA's RTX PRO 6000 GPUs, with GKE Autopilot in version 1.34.1-gke.1829001 or later. To get started, see [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

## October 21, 2025

Feature

The G4 VM, powered by NVIDIA's RTX PRO 6000 Blackwell Server Edition GPUs with the AMD EPYC Turin CPU platform, is generally available on GKE. G4 instances have up to 384 vCPUs, 1,440 GB of memory, 12 TiB of Titanium SSD disks attached, and up to 400 Gbps of standard network performance. The G4 VM offers a leap in performance with up to 9 times the throughput of G2 instances for workloads such as AI development, and graphics rendering. G4 VMs are currently available with 1, 2, 4, or 8 GPUs.

  * For GKE Standard, use GKE version 1.34.0-gke.1662000 or later. To get started, see [Run GPUs in GKE Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).



## October 09, 2025

Feature

The following networking features are available:

  * In GKE version 1.33.4-gke.1055000 or later, you can control how external traffic reaches your Services on GKE clusters by using Network Service Tiers. You can configure the network tier to use either Standard Tier or Premium Tier when you create or update clusters or when you update LoadBalancer Services. For more information, see [Configure external traffic with Network Service Tiers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-tiers).

  * Starting with GKE versions 1.33 and later, you can enable automatic IP address management (auto IPAM) on GKE clusters. Auto IPAM dynamically adds or removes additional IP address ranges for nodes and Pods as the cluster scales up or down. This feature eliminates the need for large, potentially wasteful, upfront IP reservations and manual intervention during cluster scaling. For more information, see [Use auto IP address management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-auto-ipam).

  * In GKE version 1.30.3-gke.1211000 and later, you can assign additional subnets to a VPC-native cluster. Additional subnets assigned to a cluster let you create new node pools where IPv4 addresses for both nodes and Pods come from the additional subnet ranges. This enhancement removes single-subnet limitations, increases scalability, and enhances the flexibility of your GKE clusters. For more information, see [Add subnets to clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster).




Feature

For AI models deployed on a GKE cluster, you can view details about these deployments in the Google Cloud console. The pages include deployment details, logs, and [observability dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring#aiml-dashboard).

## October 07, 2025

Feature

Starting with GKE version 1.33.2-gke.1240000 and later, you can specify the network tier (Standard or Premium) for ephemeral IP addresses used by the `gke-l7-regional-external-managed-mc` GatewayClass. For more information, see [Configure Network Tier](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-network-tier).

## October 01, 2025

Feature

The GKE cluster autoscaler now allows for a significantly longer node drain time. From GKE version 1.32.7-gke.1079000 and later, the graceful node drain timeout has been increased from 10 minutes to 1 hour. For more information, see [How cluster autoscaler works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#how_cluster_autoscaler_works).

Feature

The [`InPlaceOrRecreate`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler#inplaceorrecreate_mode) mode for Vertical Pod Autoscaler (VPA) is now available for Public Preview in GKE.

This mode uses [In-Place Pod Resize (IPPR/IPPU)](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/enhancements/4016-in-place-updates-support), which allows VPA to automatically adjust workload resources, without requiring Pod recreation. This seamless rightsizing capability helps ensure better service continuity and helps minimize costs by optimizing resource allocation, particularly during idle periods.

VPA is enabled by default in Autopilot clusters. For Standard clusters, you must first enable VPA. For more information on configuring a VPA object, see [Set Pod resource requests automatically](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#gcloud).

## September 29, 2025

Feature

To improve security and workload isolation, GKE has introduced a new, dedicated service agent for logging and monitoring of GKE nodes on clusters running version 1.33 and later. For more information, see [GKE service agents](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#gke-service-agents).

#### What's changing?

GKE will now use the following service agent for logging and monitoring on your nodes:

`service-{PROJECT_NUMBER}@gcp-sa-gkenode.iam.gserviceaccount.com`

This service agent has the minimal permissions GKE needs to operate nodes, which are included in the [`role/container.defaultNodeServiceAgent` IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent).

Using a dedicated service agent helps to isolate the requirements of GKE-managed workloads from your own workloads.

#### What's the impact?

  * This change affects only _GKE system workloads_ , which will now use the new service agent for their logging and monitoring capabilities. Your own workloads are not impacted.
  * You might notice missing logs or metrics for your nodes if the new service agent doesn't have the necessary permissions.



#### What do I need to do?

In the vast majority of cases, no action is needed, as the role `role/container.defaultNodeServiceAgent` has been automatically granted to the new GKE Node Service Agent on your cluster project.

However, you will need to re-apply the role `role/container.defaultNodeServiceAgent` to the new service agent in the following scenarios:

  * You have automation that might have removed this role.
  * You notice missing logs or metrics for your nodes.



You can find the full list of permissions for this role in the [IAM documentation](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent).

## September 25, 2025

Feature

You can now let GKE auto-create node pools with ComputeClasses without having to enable node auto-provisioning for the entire cluster. This provides more granular control over auto-created node pools, enabling you to target specific workloads and optimize resource usage. For more information, see [Node auto-provisioning and ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#autoprovisioning-and-compute-classes).

To use this feature, your cluster must meet both of the following requirements:

  * Enrolled in the Rapid release channel.
  * Running GKE version 1.33.3-gke.1136000 or later.



Feature

GKE Standard clusters now support Autopilot features, including the container-optimized compute platform and fully managed nodes, letting you use Autopilot's advantages without migrating to a dedicated Autopilot cluster. For more information, see [Run Autopilot workloads in GKE Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters).

To use these features, your cluster must meet the following requirements:

  * Enrolled in the Rapid release channel.
  * Running GKE version 1.33.1-gke.1107000 or later.



## September 11, 2025

Feature

The accelerator-optimized A4X VM, an exascale platform based on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/), is now Generally Available on GKE. A4X is the first GPU VM to run on Arm with the NVIDIA GB200 Grace Blackwell Superchips. You can use A4X to run your large artificial intelligence (AI) models, machine learning (ML), and high performance computing (HPC) workloads.

**Important:** Updated on September 25, 2025. The GKE version support for the A4X machine series in this feature note was listed incorrectly. For more information, see the **Issue** published on [September 25, 2025](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#September_25_2025). The correct versions are now listed as follows.

The A4X machine type is available as `a4x-highgpu-4g` in the us-central1-a zone with the following GKE versions:

  * For GKE Standard 1.32, use 1.32.8-gke.1108000 or later.
  * For GKE Autopilot 1.33, use 1.33.4-gke.1036000 or later.



To create GKE clusters with A4X, see the following instructions:

  * To quickly deploy production-ready clusters, see [Create an AI-optimized GKE cluster with default configuration](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).
  * For precise customization or expansion of existing production GKE environments, see [Create a custom AI-optimized GKE cluster which uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute-custom-a4x).



Feature

GKE now provisions fast-starting nodes, which have significantly lower startup time, in Autopilot mode for G2 nodes with NVIDIA L4 GPUs. Fast-starting nodes are in Public Preview for clusters in the Rapid channel, and are available on a best-effort basis when workloads use compatible configurations. For more information, see [About quicker workload startup with fast-starting nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes).

## September 08, 2025

Feature

Starting with GKE version 1.33.4-gke.1036000, `ComputeClass` supports the following new `sysctls` configurations:

  * kernel.shmmni
  * kernel.shmmax
  * kernel.shmall
  * net.core.rmem_default
  * net.netfilter.nf_conntrack_max
  * net.netfilter.nf_conntrack_buckets
  * net.netfilter.nf_conntrack_tcp_timeout_close_wait
  * net.netfilter.nf_conntrack_tcp_timeout_time_wait
  * net.netfilter.nf_conntrack_tcp_timeout_time_wait
  * net.netfilter.nf_conntrack_acct
  * vm.dirty_background_ratio
  * vm.dirty_writeback_centisecs
  * vm.overcommit_memory
  * vm.overcommit_ratio
  * vm.vfs_cache_pressure
  * fs.aio-max-nr
  * fs.file-max
  * fs.inotify.max_user_instances
  * fs.inotify.max_user_watches
  * fs.nr_open



For more information, see the [ComputeClass CRD reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#sysctls).

## September 04, 2025

Feature

**New features in Kubernetes 1.34**

  * The [Kubernetes Dynamic Resource Allocation (DRA) APIs ](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#api)are now generally available. For more information about using DRA in GKE, see [About dynamic resource allocation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation). The Prioritized list and Admin access features have been promoted to beta and will be enabled by default. The kubelet API has been updated to report status on resources allocated through DRA.
  * [The Sleep Action for Pod prestop lifecycle hook](https://github.com/kubernetes/enhancements/issues/3960) is now GA. This can be used to delay Pod termination for graceful shutdown.
  * [Streaming List Response Encoding](https://github.com/kubernetes/enhancements/issues/5116) is now GA. It enables efficient handling of requests for large object collections, improving API server reliability and performance.
  * [In-Place Pod Resize](https://github.com/kubernetes/enhancements/issues/1287), which was in beta, is now improved by adding support for decreasing memory limits with best-effort OOM protection. Improved deferred resize retries are also added, which are now prioritized and more responsive to resources becoming available. A new `ResizeCompleted` event records when a resize is completed.



Feature

On clusters with GKE Dataplane V2 that are on GKE version 1.34 and later, the [ptp plugin](https://www.cni.dev/plugins/current/main/ptp) is removed from the Container Network Interface (CNI) path. Pods that are created on new nodes have interfaces named `lxc[INTERFACE_HASH]` instead of `gke[INTERFACE_HASH]`. Additionally, the CNI configuration is moving from the `netd` DaemonSet to the `cni-writer` container in the `anetd` DaemonSet. For more information, see [Overview of GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#introduction).

Feature

GKE alpha clusters enable all alpha and the default beta feature gates, which help you to test and validate upcoming Kubernetes capabilities. You can now modify the feature gates to enable or disable differently from the default values, which provides more granular control when leveraging these experimental features. Note that alpha clusters shouldn't be used for production workloads to ensure that your workloads remain stable and performant. For more information, see [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

## September 03, 2025

Feature

In GKE version 1.33.3-gke.1392000 or later, you can use ComputeClasses to provision Confidential GKE Nodes with any supported Confidential Computing type. This feature is now generally available. For more information, see [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

## August 28, 2025

Feature

You can now run GPU workloads on Confidential GKE Nodes with the A3 High machine type and NVIDIA H100 GPUs. This feature is available in GKE version 1.32.2-gke.1297000 and later for manual GPU driver installation, and in version 1.33.3-gke.1392000 and later for automatic driver installation. This enables stronger data protection and integrity for GPU-accelerated computations running within GKE clusters and nodes. This feature is in General Availability.

For more information, see [Encrypt GPU workload data in use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes).

## August 25, 2025

Feature

In GKE version 1.33 and later, the Horizontal Pod Autoscaler has been re-architected for improved performance and scalability. This update enables a consistent 15-second recalculation period and supports up to 5,000 HPA objects per cluster.

For more information see, [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler#scalability).

## August 21, 2025

Feature

The [M4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) is generally available in GKE Autopilot clusters with version 1.33.4-gke.1013000 or later. For more information, see M4 in [Resource requests in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).

Feature

Starting with GKE version 1.33.2-gke.1240000 and later, you can now specify the network service tier (Standard or Premium) for ephemeral IP addresses used by the `gke-l7-regional-external-managed` GatewayClass. This GatewayClass configures Regional External Application Load Balancers for single clusters.

For more information, see [Configure network tier for Gateway IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-network-tier).

## August 15, 2025

Feature

For clusters enrolled in the Extended channel, you can now use [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) with GKE version 1.30 or later, or [customized sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).

Feature

You can now receive a patch version in a release channel as soon as the version is available and before GKE sets the version as an auto-upgrade target in the channel by using _accelerated patch auto-upgrades_. Receiving patch versions earlier can help accelerate auto-upgrade timelines for patches, especially for use cases such as accelerating your compliance with security requirements.

For more information, see [Accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch).

## August 14, 2025

Feature

You can now configure GKE clusters to have a default compute class in GKE versions 1.33.1-gke.1744000 or later. For more details, see the [default custom compute class documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

## August 12, 2025

Feature

Starting with GKE version 1.33.1-gke.1231000, you can view KubeRay Operator addon logs. These logs are available by default in Cloud Logging when the Ray operator addon is enabled in GKE. This integration helps you to monitor and debug the Ray Operator. Previously, accessing these logs required more complex steps. To view the logs, navigate to Cloud Logging Logs Explorer in the Google Cloud console and run a query to filter for the Ray Operator logs for your specific cluster.

For more information, see [View Ray Operator logs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/view-ray-operator-logs).

Feature

Starting on August 1, 2025, the Performance HorizontalPodAutoscaler profile is enabled by default for GKE Standard clusters that run GKE version 1.33.2-gke.4605000 and later and meet all of the [Performance profile requirements](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#requirements_2). The Performance profile improves the reaction time, speed, and scalability of the Horizontal Pod Autoscaler. You can optionally [disable the Performance profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#disable_the_performance_hpa_profile).

## August 08, 2025

Feature

You can now [customize a node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#kubelet-options) with the following new Kubelet, Sysctl, and Linux config options:

  * kubeletConfig flags:

    * topologyManager (on GKE versions 1.32.3-gke.1785000 and later)
    * memoryManager (on GKE versions 1.32.3-gke.1785000 and later)
    * maxParallelImagePulls (on GKE versions 1.33.1-gke.1918000 and later)
    * singleProcessOomKill (on GKE versions 1.32.4-gke.1132000, 1.33.0-gke.1748000 and later)
    * evictionSoft
    * evictionSoftGracePeriod
    * evictionMinimumReclaim
    * evictionMaxPodGracePeriodSeconds
  * sysctl flags:

    * vm.overcommit_memory
    * vm.overcommit_ratio
    * vm.vfs_cache_pressure
    * vm.dirty_ratio
    * vm.dirty_background_ratio
    * vm.dirty_expire_centisecs
    * vm.dirty_writeback_centisecs
    * vm.watermark_scale_factor
    * vm.min_free_kbytes
    * vm.swappiness
    * fs.nr_open
    * fs.file-max
    * fs.inotify.max_user_watches
    * fs.inotify.max_user_instances
    * fs.aio-max-nr
    * net.ipv4.tcp_max_orphans
  * linuxConfig flags:

    * transparentHugepageEnabled (on GKE versions 1.33.2-gke.4655000 and later)
    * transparentHugepageDefrag (on GKE versions 1.33.2-gke.4655000 and later)



Feature

The C4 machine series now has General Availability machine types that support Local SSD storage options. These machine types are available in all GKE versions for Standard mode, and in GKE version 1.33.1-gke.1545000 and later for Autopilot mode. For more information about these machine types, see the "C4 standard with Local SSD" and "C4 highmem with Local SSD" tabs in [C4 machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types).

## August 05, 2025

Feature

The [M4 machine series](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_series) is generally available in GKE Standard clusters.

## July 28, 2025

Feature

In GKE version 1.33.1-gke.1788000 and later, you can target specific reservation sub-blocks in a reservation block by using the [`reservationSubBlock` field in compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#reservationSubBlock).

Feature

In GKE version 1.32.2-gke.1359000 and later, you can now configure [collection scheduling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling) for single-host and multi-host TPU node pools by using [compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). Collection scheduling lets you set a Service Level Objective (SLO) for your TPU workloads.

Feature

In GKE version 1.33.2-gke.1335000 and later, the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) supports [Gateway API v1.3 CRDs](https://gateway-api.sigs.k8s.io/implementations/v1.3/).

## July 21, 2025

Feature

In GKE version 1.33.2-gke.1111000 and later, you can use compute classes to set [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) on all nodes that are created for that compute class. These labels are applied to the corresponding `Node` objects in the Kubernetes API. For more information about setting node labels in compute classes, see the [ComputeClass custom resource definition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig).

## June 25, 2025

Feature

The C4D machine series is generally available in GKE. The following version requirements apply:

  * Standard clusters: 
    * Manual node creation: GKE version 1.30 and later.
    * Node auto-provisioning and cluster autoscaler with Confidential GKE Nodes and compact placement: GKE version 1.32.3-gke.1717000 and later.
  * Autopilot clusters, including compact placement: 
    * C4D machine types without Titanium SSD: GKE version 1.33.0-gke.1439000 and later.
    * C4D machine types with Titanium SSD: GKE version 1.33.1-gke.1171000 and later.



You can use the C4D machine series with Confidential GKE Nodes and in compact placement policies in Autopilot and Standard clusters.

For more information, see [C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series).

## June 16, 2025

Feature

For clusters running GKE version 1.32.4-gke.1236000 or later, the cluster autoscaler can scale down nodes by evicting Pods in the kube-system namespace that have no Pod Disruption Budget (PDB) set and have been running for at least one hour.

## June 10, 2025

Feature

GKE now reports CPU and memory requests and limits [metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) for Kubernetes-native [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) starting from GKE version 1.32.4-gke.1106006.

Feature

Flex-start provisioning mode on GKE now supports TPUs in single-host node pools. Flex-start makes accessing highly-demanded accelerators, like TPU v5e, v5p, and Trillium easier while optimizing their utilization. To learn more, see [About GPU and TPU provisioning with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).

## May 30, 2025

Feature

GKE now provides insights and recommendations that help you to [identify and remediate](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability#identify-fix-etcd-usage) clusters where the etcd cluster state database size is approaching the limit. Implementing the recommendation helps you to keep your clusters stable and performant.

## May 27, 2025

Feature

In GKE version 1.32.2-gke.1297000 and later, you can use the Intel TDX and AMD SEV-SNP [Confidential Computing technologies](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with Confidential GKE Nodes. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages). Use Confidential GKE Nodes to encrypt your workload data in-use through Compute Engine Confidential VMs for data and code confidentiality and integrity. For more information, see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

Feature

In GKE version 1.32.2-gke.1297000 and later, you can run GPU workloads on Confidential GKE Nodes with the [A3 High machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) and NVIDIA H100 GPUs. This enables stronger data protection and integrity for GPU-accelerated computations running within GKE clusters and nodes. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Encrypt GPU workload data in use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes).

## May 23, 2025

Feature

In the Google Cloud console, the GKE security posture dashboard now uses Security Command Center to show the [top threats](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#scc-integration) that affect your GKE workloads. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## May 20, 2025

Feature

In GKE version 1.32.3-gke.1927002 and later, GKE uses a container-optimized compute platform for the general-purpose Autopilot compute class. This platform improves Pod scheduling latency, especially during autoscaling operations. The container-optimized compute platform provides benefits like faster scaling reaction times and more precise capacity right-sizing. For more information about the general-purpose compute class, see [About built-in compute classes in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/balanced-scale-out-autopilot).

## May 13, 2025

Feature

GKE now provides insights and recommendations that help you to [identify and troubleshoot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/crd-with-invalid-caBundle) clusters with Custom Resource Definitions that contain an invalid or malformed Certificate Authority bundle, which might disrupt cluster operations. Implementing the recommendation helps you to keep your clusters stable and performant.

## May 12, 2025

Feature

In GKE version 1.33 and later, the Compute Engine persistent disk CSI Driver supports provisioning Hyperdisk Balanced High Availability volumes in the `ReadWriteOnce`, `ReadWriteOncePod`, and `ReadWriteMany` access modes. For more information, see [Provisioning Hyperdisk Balanced High Availability volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd#balanced_high_availability).

## May 08, 2025

Feature

In GKE version 1.32 and later, GKE Sandbox (gVisor) can now be configured with SYS_ADMIN privileges in GKE Autopilot. This lets you use [Docker-in-Docker with gVisor](https://gvisor.dev/docs/tutorials/docker-in-gke-sandbox/) in GKE Autopilot.

Feature

ClusterProfile sync is now available to generate a cluster inventory for an existing fleet. A cluster inventory lets you work with open source and third party integrations that use the [ClusterProfile](https://multicluster.sigs.k8s.io/concepts/cluster-profile-api/) specification.

## April 17, 2025

Feature

GKE Inference Gateway is now available to significantly improve the performance, efficiency, and observability of generative AI workloads on GKE.

GKE Inference Gateway provides:

  * **Improved performance** : AI serving tail latency is reduced, and AI serving throughput is increased through inference-optimized load balancing.
  * **Efficient resource utilization** : Enables dense multi-workload serving of multiple LoRA fine-tuned models on a shared accelerator, leading to higher GPU/TPU utilization.
  * **Simplified operations** : Features include model-aware routing, model-specific serving priority, and integrated AI Safety.
  * **Enhanced observability** : Golden signals of observability are provided for inference requests.



## April 03, 2025

Feature

GKE now provides insights and recommendations that help you [identify workloads without resource requests or limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling#identify-workloads) so that you can specify the resource needs for these workloads. Configuring CPU and memory requests and limits for containers is the [best practice](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#set_appropriate_resource_requests_and_limits) for improving reliability and performance, and is a necessary prerequisite for understanding and optimizing resource utilization by your workloads and their cost.

## April 02, 2025

Feature

Automatic application monitoring is now generally available in GKE versions 1.28 and later. When configured on GKE clusters, this feature automatically collects key metrics with Google Cloud Managed Service for Prometheus and provides out-of-the-box dashboards for monitoring the supported workloads. Automatic application monitoring supports six new AI model servers (NVIDIA Triton, vLLM, TGI, JetStream, TorchServe and TensorFlow Serving). For more information, see [Configure automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring).

## March 28, 2025

Feature

In version 1.32.1-gke.1729000 and later, you can customize specific kubelet and Linux kernel parameters like sysctls and huge pages by using the [`nodeSystemConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#customize-node-system-config) field in your GKE compute classes. Additionally, you can now specify default values for fields that are omitted in individual rules in a compute class by using the [`priorityDefaults`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#priorityDefaults) field. For details, see [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#autoprovisioning-and-compute-classes).

## March 21, 2025

Feature

In GKE version 1.32.2-gke.1652000 and later, new external LoadBalancer Services use zonal Network Endpoint Group (NEG) backends by default. This applies only to new backend service-based external LoadBalancer Services. Existing LoadBalancer Services are not affected. To learn more, see [Create a backend service-based external load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).

Feature

Starting in GKE version 1.32.1-gke.1729000, Autopilot clusters will automatically use the new [Performance HPA Profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile). This new profile enables faster autoscaling on CPU and Memory metrics for up to 1,000 `HorizontalPodAutoscaler` objects by routing autoscaling metrics through the `gke-metrics-agent` Daemonset. If desired, users can revert to the old autoscaling profile by [disabling the Peformance HPA Profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#disable_performance_hpa_profile).

Feature

All GKE clusters now export four new rollup metrics by default at no additional charge. These new metrics are for monitoring GKE TPU NodePools and JobSets:

  * `kubernetes.io/node_pool/accelerator/times_to_recover`: Distribution of recovery period durations. Each sample indicates a single recovery operation for the NodePool to recover from a downtime period. The data is sampled within 60s after the completion of NodePool recovery, and emitted within 24h. This metric does not include a sample for downtime period longer than 7 days. This metric is only applicable for GKE multi-host TPU node pools.

  * `kubernetes.io/jobset/times_between_interruptions`: Distribution of times between the end of last interruption and beginning of current interruption for a JobSet. Each sample indicates a single duration between last and current interruption. The data is sampled within 60s after the current interruption starts, and emitted within 24h. The metric does not include a sample for duration between interruptions longer than 7 days. This metric is only applicable for JobSets running on nodes with GPU/TPU and having a single replicated job.

  * `kubernetes.io/jobset/times_to_recover`: Distribution of recovery period durations. Each sample indicates a single recovery operation for the JobSet to recover from a downtime period. The data is sampled within 60s after the completion of JobSet recovery, and emitted within 24h. This metric does not include samples for downtime periods longer than 7 days. This metric is only applicable for JobSets running on nodes with GPU/TPU and having a single replicated job.

  * `kubernetes.io/jobset/uptime`: Total time the JobSet has been available. The data is sampled every 60s and emitted within 24h after sampling. This metric is only applicable for JobSets running on nodes with GPU/TPU and having a single replicated job.




## March 14, 2025

Feature

JobSet metrics are automatically available on new GKE Standard and Autopilot clusters starting from version 1.32.1-gke.1357001 or later. For existing clusters, you can upgrade your clusters and manually enable the JobSet metrics package. For more details on the list of JobSet metrics, see [JobSet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics).

## March 07, 2025

Feature

You can now [monitor startup latency](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/monitor-startup-latency-metrics) of Kubernetes workloads and nodes using the new **Startup Latency** dashboard available in the Observability tab on the Deployment details and Cluster details pages in the GKE Console. The dashboard is useful for tracking, troubleshooting and optimizing startup latency of your GKE workloads.

Feature

GKE now allows you to enable logging of Horizontal Pod Autoscaler decisions starting from GKE version 1.31.5-gke.1090000 or later, or version 1.32.1-gke.1260000 or later. These logs include [atomic recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events#atomic_recommendation) (based on individual metrics) and [final recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events#final_recommendation) (consolidated HPA decisions). The logs are stored in Cloud Logging and offer insights into the decision-making process of the Horizontal Pod Autoscaler.

## March 04, 2025

Feature

The [`europe-north2`](https://docs.cloud.google.com/compute/docs/regions-zones) region in Stockholm, Sweden is now available. For more information, see the [Global Locations](https://cloud.google.com/about/locations).

## February 28, 2025

Feature

New recommendations of `NODE_SA_MISSING_PERMISSIONS` subtype are added to the portfolio of [GKE Recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders). Use the new recommendations to [identify clusters](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging#identify-fix-permissions-logs-in-all-clusters) with node service accounts missing IAM permissions that are critical for normal cluster operations.

If your organization has a policy to [disable automatic role grants to default service accounts](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable_service_account_default_grants), the created [default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent) will not get the necessary permissions. Missing critical permissions can degrade your essential cluster operations, such as logging and monitoring.

## February 27, 2025

Feature

The GKE Autopilot partner program now lets partners create and manage allowlists that correspond to specific partner workloads. In GKE version 1.32.1-gke.1729000 and later, you can explicitly install allowlists in your clusters to run only the partner solutions that you need. 

To learn more, see [Run privileged workloads from GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).

## February 25, 2025

Feature

Three new metrics are added for checking node and node pool status:

  * `kubernetes.io/node/status_condition`: The condition of a node from the node status condition field. The `Ready` field has `Unknown` status if the node controller has not heard from the node in the last `node-monitor-grace-period` period. This metric is available for clusters with GKE version 1.32.1-gke.1260000 and later.

  * `kubernetes.io/node_pool/multi_host/available`: The multi-host NodePool availability. When _all_ the nodes in the node pool are available, the value is `True`. If any of the nodes in the node pool are unavailable, the value is `False`. This metric is available for Multi-host TPU node pools only.

  * `kubernetes.io/node_pool/status`: The current status of the node pool from the `NodePool` instance. Status updates happen after GKE API operations complete. This metric is available for Multi-host TPU node pools only.




## February 20, 2025

Feature

GKE Managed NVIDIA Data Center GPU Manager (DCGM) Metrics Package is now generally available for both GKE Standard and Autopilot clusters running version 1.32.0-gke.1764000 and later. You can enable the feature via the Console, gcloud, or Terraform. Starting with cluster version 1.32.1-gke.1357000, GKE Managed NVIDIA DCGM will be default-on for new clusters. 

GKE Managed DCGM provides a curated set of metrics for monitoring the utilization, performance, and health of NVIDIA GPUs. These metrics are collected by Google Cloud Managed Service for Prometheus and you can view the metric charts in the Observability Tab on the Kubernetes Clusters page or in Cloud Monitoring. For more information, see Collect and view DCGM metrics.

To learn more, see [Collect and view DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics).

Feature

GKE automatically adds the following resource labels to node pools:

  * `goog-gke-accelerator-type`: The accelerator type used in the node pool.
  * `goog-gke-tpu-node-pool-type`: The TPU node pool type, which can be single-host or multi-host.
  * `goog-gke-node-pool-provisioning-model`: The provisioning model of the node pool. The nodes can be on demand, by reservation, or Spot VMs. 



To learn more, see [Automatically applied labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#automatically-applied-labels).

## February 06, 2025

Feature

Weighted load balancing for GKE External LoadBalancer Services is now generally available on GKE clusters running version 1.31.0-gke.1506000 or later. Weighted load balancing is a more efficient way to distribute traffic to nodes based on the number of serving Pods they have backing the Service. 

To learn more, see [Weighted load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#weighted-lb).

## February 04, 2025

Feature

GKE cluster notifications have the following new capabilities:

  * You can now receive cluster notifications through Cloud Logging. To learn more, see [Viewing cluster notifications in Cloud Logging (Preview)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).
  * GKE now sends a cluster notification to notify you when your cluster is running a minor version that is at or near the end of support. To learn more, see [Minor version at or near the end of support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#end-of-standard-support-notification).
  * GKE now sends a cluster notification to notify you when your cluster has completed an upgrade operation. To learn more, see [Upgrade operation is complete](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#upgrade-operation-complete-notification).



For more details about the different types of cluster notifications GKE sends and how you can receive them, see [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).

## January 23, 2025

Feature

You can now [customize a node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#kubelet-options) with the following new kubelet and sysctl configuration options:

  * Kubelet

    * containerLogMaxSize
    * containerLogMaxFiles
    * imageGcLowThresholdPercent
    * imageGcHighThresholdPercent
    * imageMinimumGcAge
    * imageMaximumGcAge (1.30.7-gke.1076000 and later, 1.31.3-gke.1023000 and later)
    * allowedUnsafeSysctls (1.32.0-gke.1448000 and later)
  * Sysctl

    * kernel.shmmni
    * kernel.shmmax
    * kernel.shmall
    * net.netfilter.nf_conntrack_acct (1.32.0-gke.1448000 and later)
    * net.netfilter.nf_conntrack_max (1.32.0-gke.1448000 and later)
    * net.netfilter.nf_conntrack_buckets (1.32.0-gke.1448000 and later)
    * net.netfilter.nf_conntrack_tcp_timeout_close_wait (1.32.0-gke.1448000 and later)
    * net.netfilter.nf_conntrack_tcp_timeout_established (1.32.0-gke.1448000 and later)
    * net.netfilter.nf_conntrack_tcp_timeout_time_wait (1.32.0-gke.1448000 and later)



To learn more, see [Kubelet configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#kubelet-options) and [Sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).

Feature

User-managed firewall rules for GKE LoadBalancer Services is now generally available on GKE clusters running version 1.31.3-gke.1056000 or later. By allowing user-managed firewall rules for GKE LoadBalancer Services, advanced firewall policies can now be configured to control ingress traffic to your GKE Services exposed with passthrough network load balancers. To learn more, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

## January 21, 2025

Feature

You can now use A3 Ultra VM powered by NVIDIA H200 Tensor Core GPUs with our new Titanium ML network adapter, which delivers non-blocking 3.2 Tbps of GPU-to-GPU traffic with RDMA over Converged Ethernet (RoCE). 

A3 Ultra VMs are generally available in the `a3-ultragpu-8g` machine type and can be used through both the modes of operation in Google Kubernetes Engine (GKE):

  * GKE Standard supports A3 Ultra with GPUDirect RDMA on GKE version 1.31.4-gke.1183000 or higher. To get started, see [Create a Hypercompute Cluster with GKE with default configuration](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).
  * GKE Autopilot supports A3 Ultra without GPUDirect RDMA on GKE version 1.31.4-gke.1183000 or higher. To get started, see [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus). A3 Ultra with GPUDirect RDMA is not yet supported on GKE Autopilot.



## December 16, 2024

Feature

Trillium, our sixth-generation TPU, is now generally available. Support is available for GKE Standard clusters in version `1.31.1-gke.1846000` or later, and Autopilot clusters in version `1.31.2-gke.1384000` or later. You can use TPU Trillium in the `us-east5-b`, `europe-west4-a`, `us-east1-d`, `asia-northeast1-b`, and `us-south1-a` zones. 

To learn more, see [Benefits of using TPU Trillium](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#trillium-benefits).

Feature

Cloud DNS additive VPC scope is now generally available on GKE clusters running version `1.28.3-gke.1430000` or later. You can now configure your GKE clusters to add GKE headless service entries to your Cloud DNS private zone visible from your VPC networks, on top of using Cloud DNS (cluster scope) as your GKE DNS provider.

To learn more, read [Cloud DNS scopes for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#dns-scopes).

## December 13, 2024

Feature

The C4A machine family is generally available in the following versions:

  * Standard clusters in version `1.28.13-gke.1024000`, `1.29.8-gke.1057000`, `1.30.4-gke.1213000` or later. To use this family in GKE Standard, you can use the `--machine-type` flag when creating a cluster or node pool.

  * Autopilot clusters in `1.28.15-gke.1344000`, `1.29.11-gke.1012000`, `1.30.7-gke.1136000`, `1.31.3-gke.1056000` or later. To use this family in GKE Autopilot, schedule your workloads along with the `kubernetes.io/machine-family: c4a` node selector. In versions `1.31` or above, the `kubernetes.io/arch: arm64` node selector would default to C4A machine family.




Cluster autoscaler and node auto-provisioning are supported in `1.28.15-gke.1344000`, `1.29.11-gke.1012000`, `1.30.7-gke.1136000`, `1.31.3-gke.1056000` or later.

Local SSD support is available for Public [Preview](https://cloud.google.com/products#product-launch-stages) from `1.31.1-gke.2008000`. Contact your Account Team to participate in the preview.

Feature

GKE now provides insights and recommendations that help you identify and amend clusters running a minor version that reached [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#recommender-end-of-support), clusters with nodes in [violation of version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#recommender-version-skew), and clusters [without a maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#recommender-maintenance-window) to achieve reliable operations, up-to-date security posture and supportability.

## December 02, 2024

Feature

In GKE version 1.31.1-gke.2105000 or later, you can now configure custom compute classes to consume Compute Engine reservations. Workloads that use those custom compute classes automatically trigger reservation consumption during node creation. This lets you manage reservation consumption more centrally. To learn more, see [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#reservations).

## November 27, 2024

Feature

Cloud TPU Trillium (v6e) machine types are now in public preview for Autopilot clusters running version 1.31.2-gke.1384000 or later. These TPUs are available in the following zones: `us-east5-b`, `europe-west4-a`, `us-east1-d`, `asia-northeast1-b`, and `us-south1-a`. To learn more, see [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).

## November 26, 2024

Feature

Cluster autoscaler and node auto-provisioning support the C4 machine family in GKE version 1.28.15-gke.1159000, 1.29.10-gke.1227000 or later.

## November 20, 2024

Feature

You can now specify a custom resource policy as a compact placement policy with node auto-provisioning in clusters running GKE version 1.31.1-gke.2010000 or later. To learn more, see [Use compact placement for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement#compact-placement-node-autoprovision).

## November 19, 2024

Feature

GKE version 1.31 introduces increased scalability, allowing users to create clusters with up to 65,000 nodes. For clusters exceeding 5,000 nodes, a quota increase is required. Contact Google Cloud support to request this increase.

## November 18, 2024

Feature

Performance horizontal Pod autoscaling (HPA) profile is now available in Preview for new and existing GKE clusters running version 1.31.2-gke.1138000 or later. This feature speeds up HPA reaction time and enables quick recalculation of up to 1,000 HPA objects. To learn more, see [Configuring Performance HPA profile](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).

## November 11, 2024

Feature

DNS-based access for GKE clusters control plane is now generally available. This capability provides each cluster with a unique domain name system (DNS) name or fully-qualified domain name (FQDN). Access to clusters is controlled through IAM policies, eliminating the need for bastion hosts or proxy nodes. Authorized users can connect to the control plane from different cloud networks, on-prem deployments, or from remote locations, without relying on proxies.

To learn more, see [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).

## November 07, 2024

Feature

GKE clusters running version 1.28 or later now support automatic application monitoring in public preview. Enabling this feature automatically deploys `PodMonitoring` configurations to capture key metrics for supported workloads like Apache Airflow, Istio, and RabbitMQ. These metrics are integrated with Cloud Monitoring dashboards for observability. To learn more, see [Configure automatic application monitoring for workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring).

## November 06, 2024

Feature

The GKE Volume Populator is generally available on GKE clusters running version 1.31.1-gke.1729000 or later. This feature provides a way to automate data transfer from a Google Cloud Storage bucket source storage to a destination PersistentVolumeClaim backed by a Parallelstore instance. To learn more, see [Transfer data from Cloud Storage during dynamic provisioning using GKE Volume Populator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-volume-populator).

## November 05, 2024

Feature

Cloud TPU v6e machine types are now in public preview for GKE clusters running version 1.30.4-gke.1167000 or later. These TPU VMs (`ct6e-standard`) are available in the following zones: `us-east5-b`, `europe-west4-a`, `us-east1-d`, `asia-northeast1-b`, and `us-south1-a`. To learn more, see [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).

Feature

**Generally available** : In GKE version 1.26 and later, Hyperdisk Balanced volumes can be created in Confidential mode for [custom boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#confidential-mode-for-hyperdisk-balanced) and [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#creating_chd_pv) and attached to [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).

## October 31, 2024

Feature

GKE control plane authority is now generally available with version 1.31.1-gke.1846000 or later. GKE control plane authority provides enhanced visibility, security controls, and customization of the GKE control plane. For more information, see the [About GKE control plane authority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).

Feature

For GKE clusters running version 1.31.1-gke.1146000 or later, Cloud Tensor Processing Unit (TPU) v3 machine types are generally available. These TPU VMs (`ct3-hightpu-4t` and `ct3p-hightpu-4t`) are currently available in us-east1-d, europe-west4-a, us-central1-a, us-central1-b, and us-central1-f. To learn more, see [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

## October 30, 2024

Feature

Weighted load balancing for GKE External LoadBalancer Services is now available in Preview. Weighted load balancing is a more efficient way to distribute traffic to nodes based on the number of serving Pods they have backing the Service. To learn more, see [About LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

## October 29, 2024

Feature

Three new metrics are added for measuring node and workload startup latency:

  * `kubernetes.io/node/latencies/startup`: The total startup latency of a node, from the GCE instance's `CreationTimestamp` to `Kubernetes Node Ready` for the first time.

  * `kubernetes.io/pod/latencies/pod_first_ready`: The Pod end-to-end startup latency (from Pod `Created` to `Ready`), including image pulls. This metric is available for clusters with GKE version 1.31.1-gke.1678000 or later.

  * `kubernetes.io/autoscaler/latencies/per_hpa_recommendation_scale_latency_seconds`: Horizontal Pod Autoscaling (HPA) scaling recommendation latency (the time between metrics being created and the corresponding scaling recommendation being applied to the API server) for the HPA target. This metric is available for clusters running the following versions or later:

    * 1.30.4-gke.1348001
    * 1.31.0-gke.1324000



## October 28, 2024

Feature

The A3 Edge (`a3-edgegpu-8g`) machine type with H100 80GB GPUs attached is now available on GKE Standard clusters. To learn more, see [About GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).

## October 17, 2024

Feature

You can now use NVIDIA H100 80GB GPUs on GKE in the following smaller machine types: 

  * `a3-highgpu-1g` (1 GPU)
  * `a3-highgpu-2g` (2 GPUs)
  * `a3-highgpu-4g` (4 GPUs)



These machine types are available through [Dynamic Workload Scheduler Flex Start mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest), [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms) in GKE Standard mode clusters, or [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods) in GKE Autopilot mode clusters. You can only provision these machine types if there's available capacity in your region.

GKE continues to support the 8 GPU H100 80GB machine types: `a3-highgpu-8g` and `a3-megagpu-8g`.

Feature

In GKE clusters with the control plane running version 1.29.1-gke.1425000 or later, TPU slice nodes support `SIGTERM` signals that alert the node of an imminent shutdown. The imminent shutdown notification is configurable up to five minutes in TPU nodes. To configure GKE to terminate your workloads gracefully within this notification timeframe, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

Feature

The new release of the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) (2024-R2) is now generally available. With this release, the GKE Gateway controller provides the following new capabilities:

  * [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/) support
  * [Cloud Armor backend security policy support for internal Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor)
  * [Regional selection for regional multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure-region)
  * [Traffic-based autoscaling for single cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_service_capacity)



**Conformance:**

  * [GKE Gateway is now conformant to Gateway APIs v1.1.0](https://gateway-api.sigs.k8s.io/implementations/#google-kubernetes-engine)



To learn more about our GKE Gateway controller capabilities, see the [supported capabilities per GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

## October 15, 2024

Feature

You can now create workloads with multiple network interfaces in GKE Autopilot clusters running version 1.29.5-gke.1091000 and later or version 1.30.1-gke.1280000 and later. For more information, see [Setup multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).

## October 04, 2024

Feature

Ray Operator on GKE is now generally available on 1.29 and later. Ray Operator is a GKE add-on that lets you manage and scale [Ray](https://docs.ray.io/) applications. To learn more, see the [Ray Operator documentation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).

Feature

The following beta APIs were added in Kubernetes 1.31 and are available in GKE version 1.31.1-gke.1361000 and later:

  * networking.k8s.io/v1beta1/ipaddresses
  * networking.k8s.io/v1beta1/servicecidrs



Enabling both APIs at the same time enables the Multiple Service CIDRs Kubernetes feature in a GKE cluster. For more information, see the following resources:

  * [KEP-1880 - Multiple Service CIDRs](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/1880-multiple-service-cidrs/README.md)
  * [Extended Service IP ranges](https://kubernetes.io/docs/tasks/network/extend-service-ip-ranges/)



During the beta phase, you can only create Service CIDRs in the `34.118.224.0/20` reserved IP address range to avoid possible issues with overlapping IP address ranges.

## October 01, 2024

Feature

In GKE version 1.30.3-gke.1639000 and later and 1.31.0-gke.1058000 and later, GKE can handle GPU and TPU node disruptions by notifying you in advance of a shutdown and by gracefully terminating your workloads. This feature is generally available. For details, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

Feature

GKE now supports the Parallelstore CSI driver in allowlisted general availability (GA), which means that you can reach out to your Google support team to use the service under [GA terms](https://cloud.google.com/products#product-launch-stages).

Parallelstore accelerates AI/ML training and excels at saturating individual compute clients, ensuring that expensive compute resources are efficiently used. The product demonstrated a 3.9x training time improvement and 3.7x better throughput improvement compared to native ML framework data loaders and saturates single clients NIC bandwidth at 90%+.

For details, see [About the GKE Parallelstore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre).

## September 11, 2024

Feature

For GPU node pools created in GKE Standard clusters running version 1.30.1-gke.115600 or later, GKE automatically installs the `default` NVIDIA GPU driver version corresponding to the GKE version if you don't specify the `gpu-driver-version` flag.

## August 27, 2024

Feature

Starting from version 1.30.3-gke.1451000, new and upgraded GKE clusters support the GKE Metrics Server updates where the addon-resizer runs in the cluster's control plane instead of worker nodes.

## August 21, 2024

Feature

GKE support for [Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-ml) as an attached persistent disk option is now generally available. Support is available for both Autopilot and Standard clusters running GKE versions 1.30.2-gke.1394000 and later.

## August 20, 2024

Feature

The C4 machine family is generally available in the following versions:

  * Standard clusters in version 1.29.2-gke.1521000 and later. To use this family in GKE Standard, you can use the `--machine-type` flag when creating a cluster or node pool.
  * Autopilot clusters in 1.30.3-gke.1225000 and later. To use this family in GKE Autopilot, you can use the Performance compute class when scheduling your workloads.
  * Cluster autoscaler and node auto-provisioning are supported in 1.30.3-gke.1225000 and later.



## August 13, 2024

Feature

Custom compute classes are a new set of capabilities in GKE that provide an API for fine-grained control over fallback compute priorities, autoscaling configuration, obtainability and node consolidation. Custom compute classes offer enhanced flexibility and control over your GKE compute infrastructure so that you can ensure optimal resource allocation for your workloads. You can use custom compute classes in GKE version 1.30.3-gke.1451000 and later. To learn more, see [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## August 06, 2024

Feature

You can now keep a GKE Standard cluster on a minor version for longer with the Extended release channel. Clusters running 1.27 or later can be enrolled in the Extended channel, and automatically receive security patches during the extended support period after the end of standard support. To learn more, see [Get long-term support with the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended).

## August 02, 2024

Feature

The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html) can now be [used as an alternative](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator) to fully managed GKE for both Container-Optimized OS and Ubuntu node images. Choose this [option to manage your GPU stack](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#manage-gpu-stack) if you're looking for a consistent multi-cloud experience, already using the NVIDIA GPU Operator, or have software reliant on it.

## August 01, 2024

Feature

You can now enable NCCL Fast Socket on your multi-GPU Autopilot workloads. [NCCL Fast Socket](https://github.com/google/nccl-fastsocket) is a transport layer plugin designed to improve NVIDIA Collective Communication Library (NCCL) performance on Google Cloud. To enable NCCL Fast Socket on GKE Autopilot, you must use a GKE Autopilot cluster with control plane version 1.30.2-gke.1023000 or later. For more information, see [Improve workload efficiency using NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket#nccl-fastsocket-autopilot).

## July 31, 2024

Feature

You can now keep a GKE Standard cluster on a minor version for longer with the Extended release channel. Clusters running 1.27 or later can be enrolled in the Extended channel, and automatically receive security patches during the extended support period after the end of standard support. To learn more, see [Get long-term support with the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended).

## July 16, 2024

Feature

[Compute flexible committed use discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) (CUDs), previously known as Compute Engine Flexible CUDs, have been [expanded](https://cloud.google.com/blog/products/containers-kubernetes/compute-flexible-cud-expands-to-gke-autopilot-and-cloud-run) to include several GKE Autopilot and Cloud Run SKUs (see the [GKE CUD documentation](https://cloud.google.com/kubernetes-engine/cud) for details). The legacy GKE Autopilot CUD will be removed from sale on October 15, 2024. GKE Autopilot CUDs purchased before this date will continue to apply through their term.

## July 08, 2024

Feature

Ray Operator on GKE is now generally available in the Rapid channel. Ray Operator is a GKE add-on that allows you to manage and scale [Ray](https://docs.ray.io/) applications. To learn more, see the [Ray Operator documentation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview).

## July 03, 2024

Feature

You can now preload data or container images in new nodes on GKE, enabling faster workload deployment and autoscaling. This feature is Generally Available and production-ready, with support for Autopilot and Terraform. To learn more, see [Use secondary boot disks to preload data or container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading).

Feature

GKE Managed DCGM Metrics Package is now available in Preview for both GKE Standard and Autopilot clusters running version 1.30.1-gke.1204000 and later. 

You can now configure Autopilot and Standard clusters to export a predefined list of DCGM metrics emitted by GKE Managed DCGM exporter including metrics for GPU performance, utilization, and I/Os in the GPU node pools with GKE-managed NVIDIA drivers. These metrics are collected by Google Cloud Managed Service for Prometheus. You can view the curated DCGM metrics in the Observability Tab on the Kubernetes Clusters page or in Cloud Monitoring. 

For more information, see [Collect and view DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics).

## June 07, 2024

Feature

[Fully managed cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics) are now available on GKE clusters running version 1.29.3-gke.1093000 or later.

## May 24, 2024

Feature

GKE now provides insights and recommendations to create a backup plan for unprotected clusters that have existed for more than 7 days. These insights and recommendations are currently available in `us-central1-a`. See [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) and [protect clusters with Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/data-protection-recommendations) documents for details.

## May 22, 2024

Feature

The C4 machine family is available in Public Preview for Standard clusters running GKE version 1.29.2-gke.1521000 and later. You can select this family by using the `--machine-type` flag when creating a cluster or node pool. The following limitations apply:

  * GKE versions prior to 1.29.2-gke.1521000 might encounter a volume device path mounting error which can cause Pods to be stuck in a Pending state. If you encounter this issue, try deleting and re-creating the Pod, to trigger re-processing of the volume mount.
  * [Confidential GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes) are not supported in Public Preview.
  * [Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) is not supported.
  * [Nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) is not supported in Public Preview.



## May 10, 2024

Feature

In new Standard clusters running GKE version 1.29 and later, GKE assigns IP addresses for GKE Services from a Google-managed range: `34.118.224.0/20` by default. With this feature, you don't need to specify your own IP address range for Services. For more information, see [Subnet secondary IP address range for Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_svcs).

## May 02, 2024

Feature

The new release of the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) (2024-R1) is now **generally available**. With this release, the GKE Gateway controller will provide the following new capabilities and fixes:

**New capabilities:**

  * Gateway API CRDs v1.0.0
  * Cloud Armor backend security policy support for Regional external Gateways
  * Self-managed certificates with Certificate Manager on Regional internal & external Gateways
  * Google-managed certificates with Certificate Manager on Regional internal & external Gateways [**Preview**]



**Bug fixes:**

  * Fixed missing permissions to MCI service agent role for regional SSL policy



To learn more about our GKE Gateway controller capabilities, see the [supported capabilities per GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

Feature

Starting in GKE 1.30, the metric `scheduler_pod_scheduling_duration_seconds` in [control plane metrics package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#scheduler) will no longer be available, as a result of [deprecation in the upstream OSS](https://github.com/kubernetes/kubernetes/pull/119049). The replacement metric `scheduler_pod_scheduling_sli_duration_seconds` will be exported as part of the the control plane metrics package instead.

## April 30, 2024

Feature

In GKE 1.29.2-gke.1355000 and later, GPU workloads using the Accelerator compute class in GKE Autopilot support scheduling multiple GPU pods on a single node. To schedule multiple GPU Pods on the same node, specify the `gke-accelerator-count` node selector with a value that's higher than the Pod GPU request. For details, see [Deploy GPU workloads in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#request-gpus).

Feature

You can now configure access to private image registries that use private certificates using a containerd configuration file. For details, see [Customize containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).

Feature

A [Quick Start Solution](https://console.cloud.google.com/marketplace/product/google/rag-on-gke) and [Reference Architecture](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/applications/rag#rag-on-gke-application) are now available for developing and deploying Retrieval Augmented Generation (RAG) applications on GKE. RAG improves the quality of Large Language Model (LLM) responses for a specific application. For example, RAG can enable a customer service chatbot to access help center articles, a shopping assistant to tap into product catalogs and customer reviews, or a travel booking agent to access up-to-date flight and hotel information.

## April 29, 2024

Feature

Dual-stack LoadBalancer Services are now generally available with GKE. You can now create a dual-stack GKE cluster and expose GKE Services using either IPv4, IPv6 ,or a combination of both, depending on your `ipFamilyPolicy` and `ipFamilies` specs.

To learn more, see [GKE LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#ipv4ipv6_dual-stack_loadbalancer_service).

Feature

Cloud DNS additive VPC scope is now available in Preview. You can now configure your GKE clusters to add GKE headless Service entries to your Cloud DNS private zone visible from your VPC networks, on top of using Cloud DNS (cluster scope) as your GKE DNS provider.

To learn more, see [Cloud DNS scopes for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns#dns_scopes).

## April 26, 2024

Feature

You can now use the node system configuration file in GKE to enable and use Linux huge pages in your Pods. For instructions, see [Linux huge page configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#huge-page-options).

Feature

GKE Sandbox supports the use of NVIDIA GPUs (H100, A100, L4, and T4) in Public Preview in GKE version 1.29.2-gke.1108000 and later on both Standard and Autopilot clusters. GKE Sandbox provides an extra layer of security to prevent untrusted code from affecting the host kernel on your cluster nodes. For GPUs, while GKE Sandbox doesn't mitigate all NVIDIA driver vulnerabilities, it helps protect against Linux kernel vulnerabilities. For details, see [GPUs in GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus).

Feature

GKE Standard clusters now support nested virtualization. For details, including requirements and limitations, see [Use nested VMs with GKE Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization).

## April 16, 2024

Feature

The Z3 machine family is generally available in Standard clusters running for GKE 1.25 and later. You can select this family by using the `--machine-type` flag when creating a cluster or node pool. The following limitations apply:

  * Node auto-provisioning for Z3 is supported in 1.29 and later.
  * GKE Autopilot is supported in 1.29 and later.
  * Z3 machines are gracefully terminated during host maintenance.



## April 12, 2024

Feature

GPUDirect-TCPX is now supported on GKE version 1.27 and later and requires the following patch versions:

  * For GKE version 1.27, use GKE patch version 1.27.7-gke.1121000 or later.
  * For GKE version 1.28, use GKE patch version 1.28.8-gke.1095000 or later.
  * For GKE version 1.29, use GKE patch version 1.29.3-gke.1093000 or later.



To use GPUDirect-TCPX, see [Maximize GPU network bandwidth with GPUDirect-TCPX and multi-networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).

## April 10, 2024

Feature

The N4 machine family is generally available in GKE Standard clusters running on GKE 1.29.3-gke.1121000 and later. You can select this family by using the `--machine-type` flag when creating a cluster or node pool. The following limitations apply:

  * Confidential GKE nodes is not supported.
  * Local SSD is not supported.
  * `hyperdisk-balanced` is the only supported boot disk type.



Change

This note was updated on June 3, 2024. The GKE version required for N4 machine type support has been updated.

## April 09, 2024

Feature

Cloud Tensor Processing Units (TPUs) are now available in GKE Autopilot clusters running version 1.29.2-gke.1521000 or later. To learn more, visit [Deploy TPU workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot).

## April 05, 2024

Feature

GPU NVIDIA Multi-Process Service (MPS) is available in version 1.27.7-gke.1088000 and later, which allows multiple workloads to [share a single NVIDIA GPU hardware accelerator with NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus).

## April 03, 2024

Feature

The GKE compliance dashboard now offers compliance evaluation for CIS Kubernetes Benchmark 1.5, Pod Security Standards (PSS) Baseline, and PSS Restricted standards in Preview. To learn more, see [About the compliance dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation#compliance-dashboard).

Feature

GKE threat detection is now available in Preview. Threats against the Kubernetes control plane impacting your GKE Enterprise clusters are now visible in the GKE security posture dashboard. To learn more, see [About GKE threat detection](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation#ksp-advanced-tier).

## April 02, 2024

Feature

Observability for Google Kubernetes Engine: Added a dashboard for Tensor Processing Unit (TPU) metrics on the Observability tab of both the cluster listing and cluster details pages for GKE clusters. The charts on this dashboard are populated with data only if the cluster [has TPU nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus) and [GKE system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) is enabled. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## March 19, 2024

Feature

Cilium cluster-wide network policies are now generally available with the following GKE versions:

  * 1.28.6-gke.1095000 or later
  * 1.29.1-gke.1016000 or later



You can now control your GKE workloads' ingress and egress traffic cluster-wide, without being bound to a namespace for your network policies. This new capability is intended to streamline network policies for GKE platform administrators looking for a uniform way to apply policies across namespaces or application teams.

Cilium cluster-wide network policy is available in all [GKE editions](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/release-notes#edition_features).

To learn more, read [Control cluster-wide communication using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy).

## March 11, 2024

Feature

Opportunistic bursting and lower Pod minimums are now available on newly created GKE Autopilot clusters at version 1.29.2-gke.1060000 or later, and on existing clusters created at 1.26 or later that have been fully upgraded (including all nodes) to 1.29.2-gke.1060000 or later. To learn more, see [Configure Pod bursting on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).

Feature

Private clusters created on GKE versions 1.29.0-gke.1384000 and later use [Private Service Connect (PSC)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases#public-cluster-psc) for nodes to privately communicate with the control plane. There is no price increase for using GKE private clusters running on PSC.

For private clusters created with a different GKE version, the clusters continue to use [VPC Peering](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#the_control_plane_in_private_clusters) for node-to-control plane communication.

Feature

Secret Manager add-on for GKE is now available. With the add-on, you can access the secrets stored in Secret Manager as volumes mounted in Kubernetes Pods. The add-on is supported on Standard and Autopilot clusters versioned 1.29 and later. For more info, see [Use Secret Manager add-on with GKE](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component).

## March 07, 2024

Feature

You can now [preload data or container images in new nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading) to get fast workload deployment and auto scaling. This feature is available in Preview starting from GKE version 1.28.3-gke.1067000.

## March 04, 2024

Feature

NVIDIA H100 (80 GB) GPUs are [now available](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) in GKE Autopilot mode in versions 1.28.6-gke.1369000 or later, and 1.29.1-gke.1575000 or later.

Feature

GPU workloads running in Autopilot mode can now be configured using the [Accelerator Compute Class](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus). This configuration supports resource reservations, Compute Engine committed use discounts, and a new pricing model in GKE versions 1.28.6-gke.1095000 and later, and 1.29.1-gke.1143000 and later.

## February 28, 2024

Feature

The [Performance Compute Class](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods), designed for running whole-machine CPU workloads, is available in Autopilot mode from versions 1.28.6-gke.1369000 and 1.29.1-gke.1575000 and later.

## February 26, 2024

Feature

GKE now supports Gemma (2B, 7B), Google's new state-of-the-art open models. To learn more, refer to the following guides:

  * [Serve Gemma on GKE with GPUs using Hugging Face TGI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tgi)
  * [Serve Gemma on GKE with GPUs using vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm)
  * [Serve Gemma on GKE with GPUs using TensorRT-LLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tensortllm)
  * [Serve Gemma on GKE with TPUs using SaxML](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/serve-gemma-tpu-saxml)



Deployment to GKE is also supported via Vertex AI Model Garden as part of our Hugging Face, Vertex AI, and GKE integration.

## February 21, 2024

Feature

The [GKE Stateful HA Operator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-ha) is now available in GA starting in GKE versions 1.28.5-gke.1113000 and later, or 1.29.0-gke.1272000 and later. The GKE Stateful HA Operator is enabled in new Autopilot clusters and opt-in for new Standard clusters.

## February 20, 2024

Feature

You can now use the GKE API to apply Resource Manager tags to your GKE nodes. GKE attaches these tags to the underlying Compute Engine VMs. You can use these tags to [selectively enforce Cloud Firewall network firewall policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies). This feature is generally available in GKE version 1.28 and later.

Feature

Kubernetes Engine best practice observability packages, including [control plane logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#control-plane-logs), [control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics), and [kube state metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) are now enabled by default for new [managed GKE Enterprise clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options#enabling_gke_enterprise) to ensure availability of necessary data when it's needed for troubleshooting or optimization. Control plane metrics and kube state metrics are [included](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/release-notes#edition_features) in GKE [Enterprise Edition](https://cloud.google.com/kubernetes-engine/pricing#enterprise_edition) at [no additional charge](https://cloud.google.com/products/observability/pricing#anthos-costs).

Feature

GKE now delivers insights and recommendations if your cluster's [Certificate Authority (CA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation) is expired or will expire in the next 180 days. To learn more, see [Find clusters with expiring or expired credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#gke-notification-for-expiring).

## February 02, 2024

Feature

FQDN network policies are now generally available with the following GKE versions:

  * 1.26.4-gke.500 and later.
  * 1.27.1-gke.400 and later.
  * 1.28 and later.



You can further control your GKE workloads' egress traffic to a public or private service or endpoint by using a network policy matching a fully-qualified domain name or a regular expression.

FQDN Network Policy is only available and supported with [GKE Enterprise](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/release-notes).

To learn more, read [Control Pod egress traffic using FQDN network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies).

## February 01, 2024

Feature

You can now encrypt Pod-to-Pod traffic between nodes in the same cluster or in a multi-cluster environment natively with GKE. Inter-node transparent encryption is now generally available, only with GKE Enterprise, for GKE clusters in the following versions:

  * 1.26.9-gke.1024000 and later.
  * 1.27.6-gke.1506000 and later.
  * 1.28.2-gke.1098000 and later.
  * 1.29 and later.



To learn more, see [Encrypt your data in-transit in GKE with user-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption).

## January 31, 2024

Feature

The [`africa-south1`](https://docs.cloud.google.com/compute/docs/regions-zones) region in Johannesburg, South Africa is now available.

## December 19, 2023

Feature

You can now modify the `vm.max_map_count` Linux kernel attribute for nodes in a GKE Standard cluster node pool using the node system configuration. To learn more, see [Sysctl configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#sysctl-options).

## December 18, 2023

Feature

All newly created Google Kubernetes Engine (GKE) Autopilot clusters starting with 1.27.4-gke.900 will automatically collect and send metrics from the [kube-state-metrics package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) to [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).

Feature

The GKE NEG controller now supports IPv6 endpoints with GKE version 1.28.4-gke.1083000 and later.

With this new capability, when you create a dual stack Service in a dual stack GKE cluster, any NEGs associated with the Service will now contain both IPv4 and IPv6 endpoints. Existing dual stack Services utilizing NEGs (i.e. Ingress, Services using Standalone NEGs) will be migrated from "IPv4 only" endpoints to "IPv4 + IPv6" endpoints.

The migration will be completed in approximately one hour. In the event that a NEG contains a single endpoint, you might experience brief downtime of approximately 1-2 minutes during the migration of that endpoint.

Note that Having IPv6 endpoints in NEGs doesn't necessarily mean that the load balancer uses IPv6 for communication. How the load balancer communicates with your Pod depends on how the BackendService is configured, such as fields like `IpAddressSelectionPolicy`.

## December 15, 2023

Feature

The **Observability** tab in the cluster details page for each cluster and in the GKE cluster list page now shows GPU metrics if the cluster has GPU nodes. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

## November 29, 2023

Feature

Starting in GKE version 1.27.6-gke.1248000, clusters in Autopilot mode detect nodes that can't fit all DaemonSets and, over time, migrate workloads to larger nodes that can fit all DaemonSets. For more information, see [Best practices for DaemonSets on Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/deploy-workloads#autopilot-ds-best-practices).

Feature

Starting in GKE 1.27.7, you can configure your workloads to use TPU reservations with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#tpu).

## November 17, 2023

Feature

You can now run workloads on L4 GPUs in Autopilot clusters that use GKE version 1.28.3-gke.1203000 and later. For instructions, see [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

## November 15, 2023

Feature

Dynamic Workload Scheduler support on GKE through the Provisioning Request API launched in Preview in version 1.28. Use the Dynamic Workload Scheduler to get large atomic sets of available GPU models in GKE Standard clusters. For more information, see [Deploy GPUs for batch workloads with ProvisioningRequest](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).

## November 10, 2023

Feature

The **Observability** tab for a GKE deployment now shows application performance metrics if the metrics are available. The supported metric sources include Istio, GKE Ingress, NGINX Ingress and gRPC, and HTTP metrics collected by using Google Managed Service for Prometheus. For more information, see [Use application performance metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/app-performance-metrics).

## November 09, 2023

Feature

[GKE Infrastructure Dashboards and Metrics Packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) are now generally available for both GKE Autopilot and Standard clusters with control plane version 1.27.2-gke.1200 and later.

You can now configure your Autopilot or Standard clusters to export a predefined list of metrics emitted by GKE managed kube-state-metrics (KSM) for workloads state and persistent storage. The component will run in the GKE system namespace "gke-managed-cim" to collect the metrics using Google Cloud Managed Service for Prometheus and send them to Cloud Monitoring. You can [view the metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics) in the new **Persistent** and **Workloads State** dashboards in the Observability tab.

## November 08, 2023

Feature

Cloud Tensor Processing Unit (TPU) v5e is [generally available](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus) in clusters running GKE version 1.27.2-gke.2100 and later.

TPU v5e is purpose-built to bring the cost-efficiency and performance required for medium- and large-scale training and inference. TPU v5e delivers up to 2x higher training performance per dollar and up to 2.5x inference performance per dollar for LLMs and gen AI models compared to Cloud TPU v4. At less than half the cost of TPU v4, TPU v5e makes it possible for more organizations to train and deploy larger, more complex AI models.

Feature

New inference-focused Cloud Tensor Processing Unit (TPU) v5e machine types are available in GKE. These single-host TPU VMs are designed for inference workloads and contain one, four, or eight TPU v5e chips. These [three new TPU v5e machine types](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#configuration) (`ct5l-hightpu-1t`, `ct5l-hightpu-4t`, and `ct5l-hightpu-8t`) are currently available in the `us-central1-a` and `europe-west4-b` zones.

## October 31, 2023

Feature

GKE multi-cluster Gateway is now generally available in GKE versions 1.24 and later for GKE Standard clusters, and versions 1.26 and later for GKE Autopilot clusters. Use the [Gateway API](https://gateway-api.sigs.k8s.io/) to express the intent of your inbound HTTP(S) traffic into your fleet of GKE clusters. The [multi-cluster Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) deploys and manages the [Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) that forward traffic to your applications. To learn more, see [Enable multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-environment-multi-cluster-gateways). For the list of supported Cloud Load Balancers and their features, refer to [GatewayClass capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

## October 20, 2023

Feature

You can now use the GKE API to apply Resource Manager tags to your GKE resources. GKE attaches these tags to the underlying Compute Engine VMs. You can use these tags to [selectively enforce Cloud Firewall network firewall policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies). This feature is available in Public Preview in GKE version 1.28 and later.

## October 19, 2023

Feature

Compute resources can now be reserved in advance for use with GKE. Create a [future reservation](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) to request assurance of important or difficult-to-obtain capacity in advance. There are no additional costs for creating future reservation requests. You only start to pay when Compute Engine provisions the reserved resources, and you're charged at the same cost as on-demand reservations.

## October 16, 2023

Feature

Filestore Enterprise now supports backups on GKE, allowing you to make reliable copies of your data to be stored for later use. To trigger backups on Filestore Enterprise, use [Kubernetes volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/backup-filestore-volume-snapshots). Backups are currently not supported for Filestore Enterprise instances with [multishares enabled](https://docs.cloud.google.com/filestore/docs/multishares).

## October 13, 2023

Feature

Starting in GKE 1.28.1-gke.1066000, [two new TPU usage metrics are available](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#host_metrics): TensorCore utilization and Memory Bandwidth utilization.

## October 09, 2023

Feature

If you are using a [third generation machine series](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen) (for example, C3), GKE configures Local SSD volumes as the local ephemeral storage by default. You no longer need to specify the `--ephemeral-storage-local-ssd` flag when provisioning clusters or node pools. When you configure Local SSD volumes as raw block storage with the `--local-nvme-ssd-block` flag, specifying the `count` value is now optional.

## October 02, 2023

Feature

GKE now delivers insights and recommendations if users have installed webhooks that intercept system resources or webhooks that have no available endpoints. To learn more, see [Ensure control plane stability when using webhooks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks).

## September 21, 2023

Feature

The Observability dashboards on the GKE Clusters List, Cluster Details, and Workload List pages are now customizable. Additionally, the Cluster Details dashboards can be customized across the entire project, or per-cluster for specific use cases.

## September 19, 2023

Feature

The [`me-central2`](https://docs.cloud.google.com/compute/docs/regions-zones) region in Dammam, Saudi Arabia is now available.

## September 12, 2023

Feature

You can now use node auto-provisioning for TPU slices. With this feature, Standard clusters with GKE version 1.28 and later provision TPU node pools and multi-host TPU accelerators automatically to ensure the capacity required to schedule AI/ML workloads. To learn more, see [Configuring TPU node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#tpu).

## August 30, 2023

Feature

GKE now supports the ability to create nodes and workloads with multiple network interfaces. You can create new clusters with version 1.27 and later with multi networking enabled. The additional network interfaces on the Pods can be regular interfaces or high performance interfaces where the network interface is directly attached to the Pod. For more information, see [Setup multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).

Feature

Your clusters can now perform operations, such as node auto-provisioning or version upgrades, on multiple node pools in parallel. You no longer have to wait for an operation to complete before you initiate another operation. This feature is enabled for all GKE versions. This change provides you with benefits like the following:

  * More efficient scaling, which results in improved savings and faster workload deployment
  * Faster, less disruptive node pool upgrades
  * Fewer "operation already in progress" messages that could delay subsequent planned operations
  * More reliable rollback behavior to fix upgrade-related disruptions in production
  * Automatic control plane resize operations won't block other operations on the cluster



The [Google Cloud Platform Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) has also been updated to take advantage of this change.

## August 29, 2023

Feature

You can now sequence the rollout of cluster upgrades across fleets or across scopes. To learn more, see [About cluster upgrades with rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing).

Feature

You can now create Cloud Tensor Processing Unit (TPU) nodes in GKE to run AI workloads, from training to inference models. GKE manages your cluster by automating TPU resource provisioning, scaling, scheduling, repairing, and upgrading. GKE provides TPU infrastructure metrics in Cloud Monitoring, TPU logs, and error reports for better visibility and monitoring of TPU node pools in GKE clusters. TPUs are available with GKE Standard clusters. GKE supports TPU v4 in version 1.26.1.gke-1500 and later, and supports TPU v5e in version 1.27.2-gke.1500 and later. To learn more, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

## August 25, 2023

Feature

GKE now delivers insights and recommendations to ensure your workloads are ready for disruption using features such as Pod Disruption Budgets. To learn more, see [Ensure stateful workloads are disruption-ready](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness).

## August 22, 2023

Feature

The [`europe-west10`](https://docs.cloud.google.com/compute/docs/regions-zones) region in Berlin, Germany is now available.

## August 17, 2023

Feature

You can now easily identify clusters that use deprecated Kubernetes APIs removed in versions [1.25](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25), [1.26](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26), and [1.27](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-27). Kubernetes deprecation insights are now [available](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#use-of-features) for these versions.

## August 16, 2023

Feature

[GKE Infrastructure Dashboards and Metrics Packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#ksm-package) are now available for both GKE Autopilot and Standard clusters with control plane version 1.27.2-gke.1200 and later. You can now configure Autopilot or Standard clusters to export a predefined list of metrics emitted by GKE managed KSM (kube-state-metrics) for workloads state and Persistent Storage. These metrics are collected by Google Cloud Managed Service for Prometheus and are sent to Cloud Monitoring. You can also view new dashboards (Persistent and Workloads state) rendering those metrics in the Observability tab. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

Feature

You can now troubleshoot issues with [CPU limit utilization](https://console.cloud.google.com/monitoring/dashboards/gke-troubleshooting/cpu) and [Memory limit utilization](https://console.cloud.google.com/monitoring/dashboards/gke-troubleshooting/memory) of containers running in GKE by using the new "interactive playbook" dashboards in Cloud Monitoring.

## August 09, 2023

Feature

The Filestore CSI driver now supports smaller share sizes (10Gi) for Filestore multishares for GKE for enterprise instances starting in version 1.27.

## August 02, 2023

Feature

You can now run workloads on A100 80GB GPUs in [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) that use GKE version 1.27 and later.

## July 25, 2023

Feature

[Kubernetes control plane logs](http://cloud/stackdriver/docs/solutions/gke/managing-logs#control-plane-logs) and [Kubernetes control plane metrics](http://cloud/stackdriver/docs/solutions/gke/managing-metrics#control-plane-metrics) are now available for GKE Autopilot clusters with control plane version 1.22.0 and later and 1.22.13 and later, respectively. You can now configure Autopilot cluster to export logs and certain metrics emitted by the Kubernetes API server, scheduler, and controller manager to Cloud Logging and Cloud Monitoring.

## July 24, 2023

Feature

GKE Autopilot supports extended duration Pods from 1.27 or later with the `cluster-autoscaler.kubernetes.io/safe-to-evict=false` annotation. To learn more, see [how to extend the run time of Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods).

## July 13, 2023

Feature

The managed [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) for GKE is now GA in versions 1.26.5 and later. You can use this driver to consume Cloud Storage buckets for GKE workloads.

## July 12, 2023

Feature

In GKE version 1.24 and later, new beta APIs are, by default, disabled in new clusters. Starting in version 1.27, which is the first new minor version since 1.24 where new beta APIs are introduced, you can enable new APIs on cluster creation or for an existing cluster. 

For more information, see how to [Use Kubernetes beta APIs with GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis).

Feature

GKE Dataplane V2 observability is now available in Public Preview starting in GKE versions 1.26.4-gke.500 or later, or 1.27.1-gke.400 or later. You can now enable Dataplane V2 metrics and observability tools on your cluster. Dataplane V2 metrics are included in new Autopilot clusters and opt-in for new Standard clusters. You can opt-in to enable Dataplane V2 observability tools for Autopilot and Standard clusters. Existing clusters can also be updated to enable metrics and observability tooling.

For more information, check out [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).

## July 11, 2023

Feature

You can now troubleshoot common GKE issues by using the new "interactive playbook" dashboards in Cloud Monitoring: [unschedulable pods](https://console.cloud.google.com/monitoring/dashboards/gke-troubleshooting/unschedulable) and [crashlooping containers](https://console.cloud.google.com/monitoring/dashboards/gke-troubleshooting/crashloop). You can also access the interactive playbooks from GKE UI insights and set alerts that will allow you to know once those issues occurs.

For information about using these dashboards, see the GKE troubleshooting documentation for [unschedulable pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable) and [crashlooping](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#CrashLoopBackOff).

Feature

Starting in GKE version 1.27, cluster autoscaler always considers Compute Engine Reservations when making the scale-up decisions. The node pools with matching unused reservations are prioritized when choosing the node pool to scale up, even when the node pool is not the most efficient one. Additionally, unused reservations are always prioritized when balancing multi-zonal scale-ups. 

For more information, see how to [use cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

## July 10, 2023

Feature

The new release of the GKE Gateway controller (2023-R2) is now generally available. With this release, the GKE Gateway controller will provide the following new capabilities:

  * New GatewayClasses supporting the regional external Application Load Balancer
  * Identity-aware Proxy (IAP) Integration
  * Custom request and response headers
  * URL Rewrites and Path Redirects



To learn more, see the [supported capabilities per GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities).

## June 26, 2023

Feature

Managed Service for Prometheus is enabled by default in new GKE Standard clusters running version 1.27 and later. Existing clusters that upgrade to 1.27 will not automatically enable this feature. For more information, see [Enable managed collection: GKE](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke).

## June 23, 2023

Feature

Automatic GPU driver installation is available in version 1.27.2-gke.1200 and later, which enables you to install NVIDIA GPU drivers on nodes without manually applying a DaemonSet.

For instructions, see [Running GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create).

## June 22, 2023

Feature

GKE Autopilot now supports the ability to deploy your own service mesh. Many service meshes, such as Istio or LinkerD, require CAP_NET_ADMIN Linux capability to function, which is disabled on Autopilot clusters by default to reduce the size of the security attack surface. You can now optionally enable NET_ADMIN on your Autopilot clusters if you need this capability for your service meshes or other opt-in use cases. See [Autopilot Security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#linux_workload_limitations) for more information for how to enable NET_ADMIN.

## June 21, 2023

Feature

GKE support for [Hyperdisk Throughput and Hyperdisk Extreme](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) as an attached persistent disk option is now generally available. Support is available for both Autopilot and Standard clusters running GKE versions 1.26 and later.

## June 14, 2023

Feature

Clusters with low or no utilization can be identified by [Idle Cluster insights](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/idle-clusters).

## June 12, 2023

Feature

You can now use [deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations) to identify clusters on versions 1.21 to 1.24 that use Pod Security Policy, which is unsupported on GKE version 1.25 and later.

Feature

Dual-stack LoadBalancer Services are now available in Preview. Dual-stack LoadBalancer Services are supported on both GKE Standard and Autopilot dual-stack clusters. To learn more, see [Single-stack and dual-stack Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#single-stack_and_dual-stack_services).

## June 09, 2023

Feature

In addition to the existing egress network policy GKE already supports, you can now control the egress traffic of your Pods by using a network policy that matches a fully-qualified domain name or a regular expression. FQDN Network Policy is now available in Preview for clusters in version 1.26.4-gke.500 and later, and 1.27.1-gke.400 and later. For more information, see [Control Pod egress traffic using FQDN network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies).

## June 01, 2023

Feature

Agones on GKE users will get [recommendations and insights](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-agones-controller-gke) if they did not install the Agones controller on dedicated nodes.

## May 26, 2023

Feature

The **Observability** tab for each of your GKE clusters now includes metrics for ephemeral storage. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics#metrics_for_clusters_and_workloads).

## May 22, 2023

Feature

The C3 machine family is generally available for GKE Standard clusters running on version 1.22 and later. You can select this family by using the `--machine-type` flag when creating a cluster or node pool. 

The following features are not supported for this machine family: 

  * Node auto-provisioning.
  * Confidential GKE nodes.
  * Local SSD.
  * Standard persistent disks (pd-standard).



For more information, refer to the [C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_machine_types) documentation.

## May 12, 2023

Feature

The g2-standard machine family with NVIDIA L4 is generally available for node pools in clusters running GKE version 1.22 and later. To select the machine family, use the `--machine-type` flag in your create command.

## May 09, 2023

Feature

Now in GA for both GKE Standard and Autopilot clusters with GKE version 1.26 and later, you can add more IPv4 secondary Pod ranges to a new or existing cluster with the `--additional-pod-ipv4-ranges` flag. To learn more, see [Adding Pod IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).

## May 02, 2023

Feature

The managed [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) for GKE is now available in Preview in GKE versions 1.26.3 and later. You can use this driver to consume Cloud Storage buckets for GKE workloads.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
