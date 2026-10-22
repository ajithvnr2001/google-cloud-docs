---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/feature-matrix/
title: GKE feature matrix for Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:20.852713+00:00
---

# GKE feature matrix for Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/feature-matrix/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  GKE feature matrix for Google Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the availability of various Kubernetes and GKE features on Distributed Cloud connected. Because Distributed Cloud connected is a managed platform, Google manages many of the underlying platform features.

The following tables summarize whether a feature is available, who manages it, and how its behavior might differ from standard Kubernetes or cloud-based GKE.

## Cluster management and lifecycle

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Control plane** | Available | Google | Google fully provisions and manages the Kubernetes control plane. You can't access or modify control plane components.  
**Worker node operating system (OS)** | Available | Google | Google provisions and manages the operating system on the worker nodes.  
**Cluster upgrades** | Available | Google (default) or You (optional) | Google automatically schedules and performs cluster upgrades by default. You can opt out of automatic upgrades by choosing the `NONE` release channel. You can manually trigger upgrades using the Google Cloud CLI or the API. For more information, see [Upgrade the software version of a cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters#software-upgrade).  
**Fleet registration** | Available | Google | Clusters are automatically registered to a Google Cloud Fleet upon creation.  
**SSH access to nodes** | Unavailable | Not applicable | Direct SSH access to worker nodes isn't available.  
**Cluster autoscaler** | Unavailable | Not applicable | Because the physical hardware capacity is fixed, cluster autoscaling isn't supported.  
**Node auto-provisioning** | Unavailable | Not applicable | Not supported because the physical hardware capacity is fixed.  
**Survivability mode** | Available | Google | If disconnected from Google Cloud, your clusters enter survivability mode, and workloads continue to run for up to 7 days. For more information, see [Survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/survivability).  
  
## Compute and workloads

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Linux containers** | Available | You | You deploy and manage standard Kubernetes container workloads. For more information, see [Deploy workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy).  
**Virtual machines (VM Runtime on GDC)** | Available | You | You deploy and manage virtual machine guest workloads alongside containers using the Google-managed VM runtime. For more information, see [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/virtual-machines).  
**GPU workloads** | Available | You | Supported on select hardware configurations. You manage the workload deployments. For more information, see [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/gpu).  
**Horizontal pod autoscaling (HPA)** | Available | You | You can use HPA to automatically scale your workloads based on resource utilization (CPU and memory) using standard Kubernetes manifests. Because the physical hardware capacity is fixed, you must manage your overall cluster capacity and configure resource quotas. GKE-specific HPA features, such as traffic-based autoscaling and HPA performance profiles, are not supported. For more information, see [Configure horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).  
**Custom resource definitions (CRDs)** | Available | You | You can deploy and manage CRDs to extend the Kubernetes API for your own workloads. Because Distributed Cloud connected is a managed environment, Google doesn't support or troubleshoot user-installed CRDs or operators. You must not modify or delete Google-managed system CRDs. For more information, see the [Kubernetes Custom Resources documentation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).  
**Preemptible or Spot VMs** | Unavailable | Not applicable | Not supported on dedicated hardware.  
**Windows Server nodes** | Unavailable | Not applicable | Windows nodes (Kubernetes worker nodes) aren't supported. However, you can run Windows Server guest workloads as virtual machines using [VM Runtime on GDC](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/overview).  
**Host namespaces** | Unavailable | Not applicable | User workloads can't run in the host's PID, IPC, or network namespaces.  
**Privileged containers** | Unavailable | Not applicable | User containers can't be run in privileged mode (`securityContext.privileged: true`).  
**Control plane node scheduling** | Unavailable | Not applicable | You can't schedule user workloads on control plane nodes. Under node toleration restrictions, scheduling Pods with control plane toleration keys is blocked.  
  
## Networking

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Network Function operator** | Available | Google | Google installs and manages the Network Function operator. You configure advanced networking scenarios, such as VLANs, using the custom resources provided by the operator. For more information, see [Network Function operator](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/network-function).  
**Ingress** | Available | You | You can configure an `Ingress` resource for your workloads using the provided network features. For more information, see [Networking features of Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking).  
**Service load balancing** | Available | You | You can expose your workloads to your local network using standard Kubernetes services of type `LoadBalancer`, which are backed by a bundled MetalLB Layer 2 load balancer. For more information, see [Load balancing](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking#load-balancing).  
**Network policies** | Available | You | Standard Kubernetes network policies are supported for workload traffic control. For more information, see [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).  
**Cluster DNS** | Available | Google | Google installs and manages the underlying cluster DNS components. You configure the upstream name servers and domain-specific routing rules using the `ClusterDNS` custom resource. For more information, see [Configure DNS for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/cluster-dns).  
**Multiple network interfaces (multi-NIC) for Pods** | Available | You | You can connect your Pods to multiple network interfaces to separate different types of traffic or to connect workloads to secondary networks. You configure the networks and subnetworks using Distributed Cloud connected custom resources. The MacVLAN driver isn't supported on Pods running virtual machines. For more information, see [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networks).  
  
## Storage

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Storage classes** | Available | You (configuration) and Google (updates) | You configure and manage Symcloud Storage classes, including setting the default storage class. Google manages software updates for the underlying bundled software-defined storage solution. For more information, see [Symcloud Storage classes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/storage#classes).  
**Persistent volume claims** | Available | You | You create persistent volume claims to request persistent storage for your workloads. Only the ReadWriteOnce (RWO) access mode is supported. ReadWriteMany (RWX) is not supported. For more information, see [Configure abstracted Symcloud Storage volumes for workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/storage#configure-abstracted-symcloud-storage-volumes-for-workloads).  
**External block storage** | Unavailable | Not applicable | Not supported on dedicated Distributed Cloud connected hardware. Workloads must use the configured local software-defined storage classes (Symcloud Storage).  
**hostPath volumes** | Available | Google (policies) and you (configuration) | Use `hostPath` volumes only as a highly restricted fallback, not as a recommended design pattern for general storage. For standard application volumes and VM disks, we recommend using network-based storage classes or `PersistentVolumeClaims`. To support low-level hardware pass-through and networking configuration, Google enforces policy controller webhooks that restrict read/write access to the following directories: `/dev/hugepages`, `/dev/infiniband`, `/dev/vfio`, `/dev/char`, and `/sys/devices`.  
**Volume types** | Available | You | User workloads support only a restricted set of volume types: `configMap`, `csi`, `downwardAPI`, `emptyDir`, `nfs`, `persistentVolumeClaim`, `projected`, and `secret`.  
  
## Security and identity

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Workload Identity** | Available | Google | Fleet Workload Identity Federation is the default and is configured automatically for your clusters. For more information, see [Workload Identity Cluster Authentication](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth).  
**Workload role-based access control (RBAC)** | Available | You | You configure RBAC for your users and workloads. For more information, see [Roles and permissions](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/permissions).  
**Platform RBAC** | Available | Google | Google manages RBAC for system components and the control plane. For more information, see [Roles and permissions](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/permissions).  
**External Secrets Operator** | Available | You | You install and manage the External Secrets Operator to securely retrieve secrets from Secret Manager for your workloads. For more information, see [Use External Secrets Operator](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/external-secrets).  
**User and group impersonation** | Unavailable | Not applicable | Kubernetes user and group impersonation isn't supported.  
**CertificateSigningRequest** | Unavailable | Not applicable | Workloads can't request X.509 certificate issuance through the standard Kubernetes `CertificateSigningRequest` resource type.  
  
## Observability and configuration

Feature | Availability | Managed by | Description and differences  
---|---|---|---  
**Audit logging** | Available | Google | Audit logs are automatically collected and routed to Cloud Logging. For more information, see [Google Distributed Cloud connected audit logging](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/audit-logging).  
**Platform metrics and logs** | Available | Google | Google monitors the health and performance of platform components. For more information, see [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics).  
**Application metrics and logs** | Available | You | You are responsible for monitoring your own application workloads. For more information, see [Logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/logs-metrics).  
**Fleet packages** | Available | You | You can use Config Sync fleet packages to automate the deployment of configurations across your clusters. For more information, see [Use fleet packages in Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/fleet-packages-guide).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
