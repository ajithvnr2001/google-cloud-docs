---
url: https://docs.cloud.google.com/kubernetes-engine/docs/terraform/
title: Provision GKE resources with Terraform \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:46.544425+00:00
---

# Provision GKE resources with Terraform  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provision GKE resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including GKE.

This page introduces you to using Terraform with GKE, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for GKE, code examples, and guides for using Terraform to provision GKE resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your GKE resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding GKE APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for GKE

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for GKE:

**GKE product or service** | **Terraform resource**  
---|---  
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) | `[google_container_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster)`  
`[google_container_node_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool)`  
`[google_gke_hub_feature](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature)`  
`[google_gke_hub_feature_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_iam)`  
`[google_gke_hub_feature_membership](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership)`  
`[google_gke_hub_fleet](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_fleet)`  
`[google_gke_hub_membership](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_membership)`  
`[google_gke_hub_membership_binding](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_membership)`  
`[google_gke_hub_membership_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_membership_iam)`  
`[google_gke_hub_membership_rbac_role_binding](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_membership_rbac_role_binding)`  
`[google_gke_hub_namespace](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_namespace)`  
`[google_gke_hub_namespace](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_namespace)`  
`[google_gke_hub_scope](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_scope)`  
`[google_gke_hub_scope_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_scope_iam)`  
`[google_gke_hub_scope_rbac_role_binding](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_scope_rbac_role_binding)`  
[Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) | `[google_gke_backup_backup_channel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_backup_channel)`  
`[google_gke_backup_backup_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_backup_plan)` | `[google_gke_backup_backup_plan_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_backup_plan_iam)`  
`[google_gke_backup_restore_channel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_restore_channel)` | `[google_gke_backup_restore_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_restore_plan)`  
`[google_gke_backup_restore_plan_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_restore_plan_iam)`  
  
## Terraform-based guides for GKE

The following table lists Terraform-based how-to guides and tutorials for GKE:

Select categoriesCluster and node pool creationNode managementUpgradesNetworkingStorageAI/MLObservabilityBackup and recoveryResource metadataFleet management

**Guide** | **Details**  
---|---  
[Create a GKE cluster and deploy a workload by using Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform) | Explains how to create a Google Kubernetes Engine (GKE) Autopilot cluster and deploy a workload by using Terraform.  
[Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) | Explains how to create a GKE cluster in Autopilot.  
[Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) | Explains shows you how to create a Standard zonal cluster with the default features enabled in GKE.  
[Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) | Explains how to create a Standard regional cluster in GKE.  
[Create a multi-tenant cluster by using Terraform](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quickstarts/create-multi-tenant-cluster) | Explains how to create a multi-tenant cluster and deploy a workload by using Terraform.  
[Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools) | Explains how to add and perform operations on node pools running your GKE Standard clusters.  
[Create clusters and node pools with Arm nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes) | Explains how to create a GKE Standard cluster or node pool with Arm nodes, so that you can run Arm workloads on GKE.   
[Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) | Explains how to consume reserved Compute Engine resources in GKE.  
[Specify a node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images) | Explains how to specify a node image for nodes in GKE Standard clusters.  
[Creating a cluster that uses Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) | Explains how to create a GKE cluster with node pools running Microsoft Windows Server.  
[Create and manage cluster and node pool labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels) | Explains how to create a cluster that has labels attached.  
[Manage GKE resources by using Tags](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags) | Explains how to use Tags to manage your GKE clusters.  
[Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config) | Explains how to customize your GKE node system configuration by using a node system configuration file.  
[Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) | Explains how to configure VPC-native clusters in GKE.  
[Create an internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing) | Explains how to create an internal passthrough Network Load Balancer or internal load balancer on GKE.  
[Configure networking for a basic production cluster](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configure-networking) | Describes how to deploy a web application to a GKE cluster and exposing it with an HTTPS load balancer.  
[Sequence the rollout of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/manage-upgrades-with-rollout-sequencing) | Explains how to manage GKE cluster upgrades by using rollout sequencing.  
[Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus) | Explains how to request and deploy large-scale artificial intelligence (AI) and machine learning (ML) model training, tuning, and inference workloads that use Cloud TPU accelerators (TPUs) in GKE Standard clusters.  
[Run GPUs in GKE Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus) | Explains how to run and optimize your compute-intensive workloads, such as artificial intelligence (AI) workloads, by attaching and using NVIDIA GPUs in your GKE Standard clusters' nodes.  
[Running multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi) | Explains how to increase utilization and reduce costs by running multi-instance GPUs.  
[Enable the Ray operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke) | Explains how to enable the Ray operator for GKE.  
[Enable ML Diagnostics on GKE](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke#terraform) | Explains how to configure a GKE cluster for ML Diagnostics by using Terraform.  
[Use secondary boot disks to preload data or container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading) | Explains how to improve workload startup latency by using secondary boot disks.  
[Collect and view control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics) | Describes how to configure a GKE cluster to send metrics emitted by the Kubernetes API server, Scheduler, and Controller Manager to Cloud Monitoring by using Google Cloud Managed Service for Prometheus.  
[Collect and view cAdvisor/Kubelet metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cadvisor-kubelet-metrics) | Describes how to configure a Google Kubernetes Engine (GKE) cluster to send a curated set of cAdvisor/Kubelet metrics to Cloud Monitoring by using Google Cloud Managed Service for Prometheus.  
[Adjust log throughput](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput) | Describes default log throughput and how to increase throughput.  
[Deploy Managed OpenTelemetry for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke) | Explains how to set up Managed OpenTelemetry for GKE to send OTLP traces, metrics, and logs to Google Cloud Observability.  
[Collect and view kube-state-metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics) | Describes how to configure a GKE cluster to send kube-state-metrics to Cloud Monitoring by using Google Cloud Managed Service for Prometheus.  
[Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) | Explains how to install Policy Controller by using Terraform.  
[Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster) | Describes how to enable Backup for GKE for a cluster.  
[Modify resources during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/transformation-rules) | Describes how to make modifications to Kubernetes resources during the restoration process by using transformation rules.  
[Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode) | Explains how to enable permissive mode on a backup plan.  
[Enable Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install) | Describes how to enable Backup for GKE.  
[Plan a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan) | Describes how to create a Backup for GKE backup plan, which is used for backing up your workloads in GKE.  
[Register a cluster on Google Cloud to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke) | Explains how to register a GKE cluster on Google Cloud to your fleet by using Terraform.  
[Install Config Sync as a fleet default](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-fleet) | Explains how to configure Config Sync as a fleet-level default for all new clusters.  
[Manage team resources across your fleet](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-tenancy) | Explains how to use Config Sync and Terraform to dynamically create team-scoped resources across a fleet of clusters.  
  
## Terraform modules and blueprints for GKE

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to GKE:

Module or blueprint | Details  
---|---  
[terraform-google-kubernetes-engine](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine) | Configures opinionated GKE clusters.  
[terraform-google-gke-gitlab](https://github.com/terraform-google-modules/terraform-google-gke-gitlab) | Installs GitLab on GKE.  
  
## What's next

  * [Terraform code samples for GKE](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
