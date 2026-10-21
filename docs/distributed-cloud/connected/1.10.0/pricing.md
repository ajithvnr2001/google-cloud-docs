---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/pricing/
title: Pricing \u00a0|\u00a0 Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:38.825006+00:00
---

# Pricing  |  Google Cloud

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/pricing/




Stay organized with collections  Save and categorize content based on your preferences. 

# Google Distributed Cloud connected pricing

Distributed Cloud connected pricing is based on the following factors:

  * Hardware configuration
  * Procurement model
  * Term commitment
  * Geographical location
  * Google Cloud region



## Hardware configuration

Distributed Cloud connected hardware is a 1U server machine that can be deployed either as a single node or in groups of three nodes for high availability. You must order all of the Distributed Cloud connected hardware for each zone together. You cannot add or remove machines after the hardware has been deployed. You also cannot mix three-machine and single-machine clusters in the same zone.

For more information, see [How Distributed Cloud works](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works) and [Installation requirements](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements).

## Procurement model

This section summarizes the procurement models for Distributed Cloud connected hardware. For more information, see [Distributed Cloud connected procurement models](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works#procurement).

  * **Google-sourced hardware**. In this model, Google provides both the hardware and the service, including the software solution, remote management, and hardware support.

  * **Customer-sourced hardware**. In this model, Google provides the service, while you work with a Google-certified systems integrator (SI) to procure Google-certified hardware for your Distributed Cloud connected deployment. The SI provides support for the hardware.




## Term commitment

You are billed for Distributed Cloud connected on a monthly basis. You must commit to a term of either 36 or 60 months.

## Pricing for Distributed Cloud connected hardware

Pricing for Distributed Cloud connected hardware is available on the corresponding [SKU page](https://cloud.google.com/skus?e=13802955&filter=8A2D-5CB1-345B&currency=USD).

## Included and add-on services

Distributed Cloud connected ships with the [Distributed Cloud connected services platform](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/services), which lets you integrate external services with your Distributed Cloud connected deployment.

The following table describes the cost of integrating each supported service with Distributed Cloud connected:

Service type | Included in GDC connected costs | Billed separately  
---|---|---  
**Compute** | [Software-only Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)  
[VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/overview) | Guest operating systems  
(you must obtain your own licenses)  
**Storage** | Raw (persistent volume) storage  
[Container Storage Interface (CSI)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-csi-driver)  
Hybrid storage | Software Defined Storage (SDS),  
such as [Symcloud Storage](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/storage)  
(you must obtain your own licenses)  
**Networking** | [Edge Network API](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/networking)  
VLAN support  
GKE Custom Network Interface (CNI) plugins  
GKE bundled L4 load balancer  
| Not applicable  
**AI/ML** | Deploying AutoML models in containers | Not applicable  
**Database** | None | [AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni) (preview)  
Third-party database solutions, such as MongoDB  
(you must obtain your own licenses)  
**Observability** | [Cloud Logging](https://docs.cloud.google.com/logging)  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring)  
[Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest) GDCc logs and metrics | [Prometheus](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/logs-metrics#collect_metrics_with_prometheus) for disconnected observability  
Application-level custom logs and metrics  
**Configuration Management** | [Config Sync](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/overview)  
[Fleet packages](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/fleet-packages) (preview) | Not applicable  
**Management** | Google Kubernetes Engine dashboard in the Google API Console  
[Connect Gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using)  
The `kubectl` local tool  
[Distributed Cloud connected software upgrades](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/availability#cluster-maintenance) | Not applicable  
**Security** | [Cloud Key Management Service integration](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/security#cmek)  
Self-Encrypting Disk (SED) drives  
[Fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure)  
[Audit logging](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/audit-logging) | Not applicable  
  
## Purchase the minimum required support

Distributed Cloud connected requires, at minimum, [Enhanced Support](https://docs.cloud.google.com/support/docs/enhanced). If you're not an Enhanced Support or a Premium Support customer, you must purchase at least Enhanced Support to use Distributed Cloud connected.

## Billing for other Google Cloud services

If you use any Google Cloud services, such as Cloud VPN or Google Cloud Observability on your Google Distributed Cloud connected deployment, you are billed separately for the usage of each of those services.

## Billing for logs and metrics

Distributed Cloud connected logs various types of information about its operation, such as Distributed Cloud connected system activities and the workloads that you run on your Distributed Cloud clusters.

The following table describes the pricing for collecting various logs and metrics on Distributed Cloud.

Log type | Billing | Description  
---|---|---  
**System metrics** | Free | Metrics for Distributed Cloud system activities.  
**System logs** | Free for specific namespaces | System logs collected from the following namespaces are free:

  * `anthos-identity-service`
  * `cert-manager`
  * `gke-system`
  * `kube-system`

System logs collected from the following namespaces are billable according to [Cloud Logging pricing](https://docs.cloud.google.com/stackdriver/pricing):

  * `gke-managed-metrics-server`
  * `metallb-system`
  * `nf-operator`
  * `sriov-fec-system`
  * `sriov-network-operator`
  * `vm-system`

  
**Application metrics** | Billable | Billable according to Cloud Logging pricing.  
**Application logs** | Billable | Billable according to Cloud Logging pricing.  
**Audit logs** | Free | [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) collected for Distributed Cloud operations.

#### Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.  [ Contact sales ](https://docs.cloud.google.com/contact?direct=true) [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
