---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/cost-optimization/
title: Design and configure GKE clusters for cost optimization \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:33.938299+00:00
---

# Design and configure GKE clusters for cost optimization  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Design and configure GKE clusters for cost optimization Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document helps you navigate Google Kubernetes Engine (GKE) documentation to find guidelines and recommendations for cost optimization. GKE offers extensive autoscaling and scheduling capabilities that you can use to minimize cluster cost while maintaining application stability.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

You should already be familiar with the following:

  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)



## Overview

When you implement GKE, you must consider different technical aspects to align with application and business requirements. Beyond defining networking, security, storage, and other technical aspects, you must evaluate both cost and performance to meet business needs. Instead of treating cost and performance as distinct entities, you must integrate them from the initial stages of infrastructure planning to define a unified relationship that determines both reliability and cloud spending. Low cost and high reliability are expected, but as you scale, the complexity of managing this trade-off increases.

To achieve low cost and application stability, you can set or tune the following GKE features:

  * GKE configuration
  * Workload configuration
  * Cost baseline and visibility



You can also discover and implement cost optimization best practices by using Compute Advisor (Preview). For more information, see Use Compute Advisor.

## Use GKE Autopilot

For small sandbox or development environments, select Autopilot clusters. In Autopilot, GKE dynamically manages nodes and you are billed only for requested Pod capacity, which helps you avoid VM, node operating system, and system overhead charges.

For more information, see [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

## Understand how autoscaling works

GKE autoscaling controllers dynamically adjust resources as traffic requests change.

### Add and remove Pods based on utilization metrics

A HorizontalPodAutoscaler (HPA) adds and removes Pods based on CPU or custom metrics.

To understand and configure horizontal Pod autoscaling, see the following GKE documentation:

  * [Horizontal Pod autoscaling concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)
  * [Configure horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling)
  * [View Horizontal Pod Autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-horizontalpodautoscaling-events)
  * [Expose custom application metrics for autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics-autoscaling)



Configure a target utilization threshold (for example, 70% or 80%) to maintain a buffer that handles traffic surges while additional replica Pods start.

### Scale your Pods based on utilization metrics

Use VerticalPodAutoscaler (VPA) to dynamically size container CPU and memory requests for workloads that don't employ horizontal Pod autoscaling, or when peak workloads are unknown.

To understand and configure vertical Pod autoscaling, see the following GKE documentation:

  * [Vertical Pod autoscaling concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)
  * [Scale container resource requests and limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling)



Keep VPA in `Off` (recommendation-only) mode for at least 24 hours (ideally one week) in production-like environments to capture representative traffic patterns. To prevent erratic sizing adjustments, specify explicit minimum and maximum bounds in your VerticalPodAutoscaler object before enabling `Initial` or `Auto` modes.

### Automate infrastructure scaling using Cluster Autoscaler

To scale underlying compute nodes based on active scheduling simulation rather than metric loads, enable Cluster Autoscaler in GKE Standard node pools. Specify minimum node parameters to support baseline night capacity.

Always configure a PodDisruptionBudget (PDB) object for system and application Pods. This configuration helps ensure that Cluster Autoscaler doesn't inadvertently cause service disruption when consolidating or scaling down underutilized node pools.

To understand and configure Cluster Autoscaler, see the following GKE documentation:

  * [About GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)
  * [Autoscaling a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler)
  * [View cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility)



### Deploy dynamic node pools using node pool auto-creation

Enable node pool auto-creation to automatically generate custom GKE node pools whose shapes, CPU counts, or memory limits precisely fit the scheduling parameters of pending Pods. This feature minimizes resources left over on oversized nodes.

To understand and configure node pool auto-creation, see the following GKE documentation:

  * [Node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning)
  * [Configure node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)



### Autoscaling checklist

Add and remove Pods based on utilization metrics

Scale your Pods based on utilization metrics

Automate infrastructure scaling using Cluster Autoscaler

Deploy dynamic node pools using node pool auto-creation

## Infrastructure characteristics

Align cluster hardware, location, and node network rules with cost-optimization priorities.

### Select the appropriate machine types

Select the appropriate machine types for your cluster based on the location of your users and the location of the data that your cluster needs to access.

For more information, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).

### Deploy fault-tolerant workloads on Spot VMs

Use Spot VMs to run stateless, fault-tolerant, or batch workloads at a discount of up to 91% compared to on-demand VM instances.

**Note:** GKE Spot VM node pools can be preempted at any time. Set up node selectors and taints to route critical serving components to node pools.

For more information, see the following GKE documentation:

  * [Spot VMs concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)
  * [Run fault-tolerant workloads at lower costs with Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms)
  * [Run fault-tolerant workloads at lower costs in Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods)



### Map efficient machine families and OS system settings

Customize node pool machine settings with cost-efficient instance profiles (for example, E2 VM architectures).

For more information about sizing nodes, configuring Spot VM preemption timings, and configuring kernel configurations, see [About node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).

### Select the appropriate region

When latency doesn't affect your users, run cluster workloads in Compute Engine regions with lower operating costs.

For more information, see [Best practices for Compute Engine region selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).

### Sign up for CUD

Purchase committed-use discounts (CUDs) to secure deeply discounted pricing (up to 70%) for baseline compute resources over a one-year or three-year term.

For more information, see [Resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

### Consider networking costs

Regional and multi-zonal GKE clusters improve application reliability but can generate internal cross-zone network egress costs.

To minimize and control networking costs, consider the following:

  * **Cross-zone data transfers:** although regional clusters increase availability by spreading workloads across zones, there are associated costs for data transferred between these zones.



For more information, see [All networking pricing](https://docs.cloud.google.com/vpc/network-pricing).

### Deploy single-zone clusters for non-production environments

In non-production environments, to avoid cross-zone network charges and reduce VM overhead, deploy single-zone clusters instead of regional or multi-zonal clusters.

For more information, see [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview).

### Optimize cluster DNS resolution paths and ingress traffic

To optimize cluster DNS resolution and ingress traffic, you can deploy NodeLocal DNSCache and network endpoint groups (NEGs).

When you run DNS-heavy workloads, NodeLocal DNSCache runs a local DNS daemon on each node. This configuration prevents high query loads from exhausting CoreDNS, avoiding the need to scale CoreDNS and reducing overall GKE costs.

For ingress traffic, container-native load balancing through NEGs routes traffic directly to Pod IP addresses instead of instance groups. This direct routing facilitates graceful traffic redirection during Pod scaling actions.

For more information, see:

  * [Set up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
  * [Container-native load balancing overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native-load-balancing)
  * [Configure Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)



### Apply resource quotas per namespace

Deploy standard Kubernetes ResourceQuota objects per namespace in multi-tenant clusters to lock down CPU and memory shape thresholds and prevent individual teams from scheduling noncompliant workloads that trigger unexpected compute charges.

For more information, see [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes documentation.

### Implement Policy Controller audits

Deploy Policy Controller to dynamically audit and enforce cluster compliance with corporate standards. Policy Controller uses admission control to reject misconfigured resources.

For more information, see the following:

  * [Policy Controller overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)
  * [Install Policy Controller on GKE](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller)



### Gate noncompliant manifests in CI/CD pipelines

Validate cost policy compliance earlier in your development lifecycle. Integrate validation scripts (such as `kpt` parsing) into pre-commit or pull-request checks to audit and block noncompliant manifests before they reach the cluster.

For more information, see [Validate apps against company policies in a CI pipeline](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline).

### Infrastructure checklist

Select the appropriate machine types

Deploy fault-tolerant workloads on Spot VMs

Map efficient machine families and OS system settings

Select the appropriate region

Sign up for CUDs

Consider networking costs

Deploy single-zone clusters for non-production environments

Optimize cluster DNS resolution paths and ingress traffic using NEGs

Apply resource quotas per namespace

Implement Policy Controller audits

Gate noncompliant manifests in CI/CD pipelines

## Application and workload optimization

Configure your workloads to use resources efficiently and reduce operational overhead.

### Specify matching memory requests and limits

Specify precise container CPU and memory requests before deployment. For CPU, configure requests to meet your service-level objectives (SLOs) but leave limits unrestricted. For memory, ensure that the requested allocation matches the memory limit.

For more information, see [Resize CPU and Memory Resources assigned to Containers](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) in the Kubernetes documentation.

### Accelerate container start times

Make container images as small as possible to minimize image download times.

### Configure PDBs

Specify a PodDisruptionBudget (PDB) object for application replicas to limit voluntary disruptions and ensure stability when GKE scales down or when node upgrades occur.

For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

### Set meaningful readiness and liveness probes

Configure readiness and liveness probes for all containers to help ensure that GKE both routes traffic only to ready Pods and restarts failed instances, preventing traffic loss during autoscaling.

For more information, see [Configure Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

### Configure graceful application shutdown

Prepare containers for graceful termination by listening for the `SIGTERM` signal, finalizing in-flight requests before exiting, or by configuring `preStop` hooks.

For more information, see [Termination and graceful shutdown of preemptible VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms#graceful-shutdown).

### Implement retries with exponential backoff

Implement exponential backoff retries at the application or service mesh level to handle transient failures or potential Spot VM preemptions.

For more information, see [Retries](https://istio.io/latest/docs/concepts/traffic-management/#retries) in Istio documentation.

### Application and workload optimization checklist

Specify matching memory requests and limits

Accelerate container start times

Configure PDBs

Set meaningful readiness and liveness probes

Configure graceful application shutdown

Implement retries with exponential backoff

## Cost baseline and visibility

To optimize costs, you first need visibility into your GKE spending and how it's allocated. This visibility helps you attribute costs to the teams and business units that incur them.

The following GKE documentation describes how to establish deep visibility into GKE billing, resource consumption, and baseline metrics.

### Enable GKE cost allocation

Enable GKE cost allocation to get visibility into workload resource requests and associated costs. Cost allocation attributes cluster costs to namespaces and Kubernetes labels of your workloads.

Export these details to BigQuery to analyze the data in Cloud Billing. Use this analysis to identify which workloads cause billing peaks, perform chargebacks, and optimize resource requests.

For more information, see [Get key spending insights for your GKE resource allocation and cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

### Review log and metric ingestion volumes

Enabling Cloud Logging and Cloud Monitoring for your clusters incurs costs. High volumes of log and custom metric ingestion can result in unexpected charges. Centrally audit which log levels and custom metrics are ingested.

For more information about troubleshooting high logging API usage or log write limit timeouts, see:

  * [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs)
  * [Troubleshoot missing logs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging)



### Monitor the health of Metrics Server

Monitor the health of the Metrics Server Deployment, because GKE's built-in autoscaling controllers rely on it to retrieve CPU and memory metrics.

For more information, see [Troubleshoot horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling).

### Foster a cost-saving culture

Provide developers with access to cloud spending dashboards and establish FinOps training to align architectural decisions with business cost budgets.

For more information about organizational cost-efficiency culture, see [Spread the cost saving culture](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#spread_the_cost-saving_culture).

### Cost baseline and visibility checklist

Enable GKE cost allocation

Review log and metric ingestion volumes

Monitor the health of Metrics Server

Foster a cost-saving culture

## Use Compute Advisor

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Compute Advisor is an AI-powered interface in the Google Cloud console, powered by Gemini, that helps you design resilient and cost-effective architectures for GKE.

Compute Advisor provides near-real-time availability guidance for Flex-start VMs and Spot VMs, while verifying your organization's policies and resource quotas before deployment. Compute Advisor doesn't provide availability guidance for workloads that require on-demand resources.

To access Gemini in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Overview** page.

[Go to Overview](https://console.cloud.google.com/kubernetes/overview)

  2. In the **Design your infrastructure with Compute Advisor** section, submit a prompt. Gemini starts to generate a response.

**Caution:** Generative AI can make mistakes. Validate all recommendations and configurations before you take any actions on a resource that Gemini recommends you to create, modify, or delete.
  3. To generate architectural recommendations, run one of the following example prompts in Compute Advisor. When you click the **Run prompt in Compute Advisor** buttons, the Google Cloud console might take longer than 15 seconds to load:



  * **Autoscaling and bin packing** :

_Use case:_ to maximize bin packing and minimize idle CPU overhead, use this prompt to configure a strategy for GKE cluster autoscaling and node pools.
        
        Configure a GKE cluster to use autoscaler and node pool strategy
          to maximize bin packing and minimize idle CPU overhead.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_finops_autoscaling_bin_packing)

  * **Multi-tenancy governance** :

_Use case:_ to keep development namespaces within budget bounds, use this prompt to draft a ResourceQuota policy for a multi-tenant GKE cluster.
        
        Draft a ResourceQuota policy for a multi-tenant GKE
          cluster to keep development namespaces within budget bounds.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_finops_multi_tenancy_governance)

  * **Workload optimization** :

_Use case:_ to help you decide whether to use GKE Autopilot or Standard mode for a batch workload with variable resource demands, use this prompt to get a recommendation:
        
        Recommend whether to use GKE Autopilot or Standard mode for a batch processing workload with highly variable resource demands.
        

[Run prompt in Compute Advisor](https://console.cloud.google.com/compute/advisor/?advisor_ref=gke_finops_workload_optimization)




## What's next

For more information about the architectural principles and organizational culture required for cost-efficiency, see [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
