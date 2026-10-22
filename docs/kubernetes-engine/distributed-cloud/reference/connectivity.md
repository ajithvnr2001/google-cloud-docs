---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/connectivity/
title: Impact of temporary disconnection from Google Cloud \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:46.430659+00:00
---

# Impact of temporary disconnection from Google Cloud  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Impact of temporary disconnection from Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud software only is based on Kubernetes, and you can deploy it on-premises on either VMware or bare metal servers. Although Distributed Cloud runs on-premises, we design it to have a permanent connection to Google Cloud for a number of reasons, including monitoring and management. However, you might need to know what happens if, for any reason, you lose the connection to Google Cloud (for example, because of a technical problem). This document outlines the impact of a loss of connectivity for clusters in a Distributed Cloud software only deployment (on bare metal or on VMware), and which workarounds you can use in this event.

This information is useful for architects who need to prepare for an unplanned or forced disconnection from Google Cloud and understand its consequences. However, you shouldn't plan to use a software-only Distributed Cloud deployment that's disconnected from Google Cloud as a nominal working mode. Remember that we design Distributed Cloud to take advantage of the scalability and availability of Google Cloud services. This document draws on the design and architecture of the various Google Cloud components that work compatibly with Distributed Cloud during a temporary interruption. We can't guarantee that this document is exhaustive.

This document assumes that you are familiar with GKE. If that isn't the case, we recommend that you first read the [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

## License validation and metering

If you have enabled the [Anthos API (`anthos.googleapis.com`)](https://console.cloud.google.com/apis/library/anthos.googleapis.com) in your Google Cloud project, the metering controller running in the cluster generates and refreshes the license entitlement periodically. The tolerance for disconnection is 12 hours. Additionally, the system requires the connection for managing metering and billing.

This table lists the behavior of features related to licensing and metering in case of temporary disconnection from Google Cloud:

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
License validation | The metering controller generates and refreshes the license entitlement custom resource periodically, as long as `anthos.googleapis.com` is enabled in the Google Cloud project. | The components that consume the entitlement custom resource support a grace period: they continue to function as long as the entitlement custom resource is refreshed within the grace period. | Unlimited. After the grace period expires, components start to log errors. You can't upgrade your cluster anymore. | None  
Metering and billing | The metering controller reports the vCPU capacity of the cluster to the Google Cloud Service Control API for billing purposes. | An in-cluster agent persists billing records in the cluster during disconnection and retrieves the records once the cluster re-connects to Google Cloud. | Unlimited. However, metering information is required for compliance as stated in the [Service Specific Terms](https://cloud.google.com/terms/service-terms) for "Premium Software". | None  
  
## Cluster lifecycle

This section covers scenarios such as creating, updating, deleting, and resizing clusters, as well as monitoring the status of these activities.

For most scenarios, you can use CLI tools such as `bmctl`, `gkectl`, and `kubectl` to perform operations during a temporary disconnection. You can also monitor the status of these operations with these tools. Upon reconnection, the Google Cloud console updates to display the results of operations performed during the disconnected period.

Action | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Cluster creation | You use the `bmctl` or `gkectl` CLI tools to create clusters. This operation requires a connection to Google Cloud. | You can't create clusters. | Zero | None  
Cluster upgrade | You use the `bmctl` or `gkectl` CLI tools to upgrade clusters. This operation requires a connection to Google Cloud. | You can't upgrade clusters. | Zero | None  
Cluster deletion | You use the `bmctl` or `gkectl` CLI tools to delete clusters. This operation doesn't require a connection to Google Cloud. | You can delete clusters. | Unlimited | -  
Viewing cluster status | You can see information about your clusters in the console, in the list of Google Kubernetes Engine clusters. | Cluster information isn't shown in the console. | Unlimited | Use `kubectl` to directly query your clusters and get the information you need.  
Removing nodes from a cluster | You don't need a connection to Google Cloud to remove nodes from a cluster. | You can remove nodes from a cluster. | Unlimited | -  
Adding nodes to a cluster | The new node pulls container images from Container Registry to properly work. A preflight check runs to validate that there is connectivity to Google Cloud.  | The preflight checks that run when adding a new node validate that there is connectivity to Google Cloud. Therefore, you can't add a new node to a cluster when disconnected. | Zero | None  
  
## Application lifecycle

A temporary disconnection from Google Cloud mostly doesn't affect managing your applications running in an on-premises cluster. Only the [ connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using) is affected. If you use [Container Registry](https://docs.cloud.google.com/container-registry), [ Artifact Registry](https://docs.cloud.google.com/artifact-registry), [Cloud Build](https://docs.cloud.google.com/build), or [ Cloud Deploy](https://docs.cloud.google.com/deploy) to manage your container images or CI/CD pipelines in Google Cloud, they become unavailable in case of disconnection. Strategies to deal with disconnection for those products are outside of the scope of this document.

Action | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Application deployment | You deploy applications locally using `kubectl`, through CI/CD tooling, or using the connect gateway. | The connect gateway isn't available. All other methods of deployments still work as long as they connect directly to the Kubernetes API. | Unlimited | If you use the connect gateway, switch to using `kubectl` locally.  
Application removal | You remove applications locally using `kubectl`, through CI/CD tooling, or using the connect gateway. | The connect gateway isn't available. All other methods of deployments still work as long as they connect directly to the Kubernetes API. | Unlimited | If you use the connect gateway, switch to using `kubectl` locally.  
Application scale-out | You scale out applications locally using `kubectl`, through CI/CD tooling, or using the connect gateway. | The connect gateway isn't available. All other methods of deployments still work as long as they connect directly to the Kubernetes API. | Unlimited | If you use the connect gateway, switch to using `kubectl` locally.  
  
## Logging and monitoring

Auditability helps your organization meet its regulatory requirements and compliance policies. Distributed Cloud helps with auditability by offering application logging, Kubernetes logging, and audit logging. Many customers choose to use Google's [Cloud Logging](https://docs.cloud.google.com/logging) and [ Cloud Monitoring](https://docs.cloud.google.com/monitoring) to avoid managing a logging and monitoring infrastructure on-premises. Other customers prefer to centralize their logs into an on-premises system for aggregation. To support these customers, Distributed Cloud supports direct integration to services such as [Prometheus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#prometheus_and_grafana). In this mode, during temporary disconnection from Google Cloud, there is no impact on logging or monitoring functionality.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Application logging using Cloud Logging | The system writes logs to Cloud Logging. | The system buffers logs to the local disk. | 4.5h or 4GiB local buffer per node. When the buffer fills or the disconnection lasts 4.5 hours, then the system drops the oldest entries. | Use a local logging solution.  
System/Kubernetes logging using Cloud Logging | The system writes logs to Cloud Logging. | The system buffers logs to the local disk. | 4.5h or 4GiB local buffer per node. When the buffer fills or the disconnection lasts 4.5 hours, then the system drops the oldest entries. | Use a local logging solution.  
Audit logging using Cloud Audit Logs | The system writes logs to Cloud Logging. | The system buffers logs to the local disk. | 10GiB local buffer per control plane node. When the buffer fills, then the system drops the oldest entries. | Set up log forwarding to a local logging solution.  
Application logging using other provider | You can use different third-party providers like Elastic, Splunk, Datadog, or Loki. | No impact | Unlimited | -  
System/Kubernetes logging using other provider | You can use different third-party providers like Elastic, Splunk, or Datadog. | No impact | Unlimited | -  
Application and Kubernetes metrics written to Cloud Monitoring | The system writes metrics to Cloud Monitoring. | The system buffers metrics to the local disk. | 24h or 6GiB local buffer per node for system metrics and 1GiB local buffer per node for application metrics. When the buffer fills or the disconnection lasts 24 hours, then the system drops the oldest entries | Use a local monitoring solution.  
Accessing and reading monitoring data from Kubernetes and application workloads | All metrics are available in the console and through the Cloud Monitoring API. | The system doesn't update metrics in Cloud Monitoring during the disconnection. | 24h or 6GiB local buffer per node for system metrics and 1GiB local buffer per node for application metrics. When the buffer fills or the disconnection lasts 24 hours, then the system drops the oldest entries | Use a local monitoring solution.  
Alerting rules and paging for metrics | Cloud Monitoring supports alerting. You can create alerts for any metric. The system can send alerts through different channels. | The system doesn't trigger alerts while disconnected. The system only triggers alerts from metrics data already sent into Cloud Monitoring. |  | Use a local monitoring and alerting solution.  
  
## Config and policy management

[Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) and [ Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) lets you manage configuration and policies at scale, across all of your clusters. You store configurations and policies in a Git repository, and the system automatically synchronizes them to your clusters.

### Config Sync

Config Sync uses in-cluster agents to connect directly to a Git repository. You can manage changes to the repository URL or the synchronization parameters with the Google Cloud CLI or `kubectl` tools.

During temporary disconnection, synchronization remains unaffected if the in-cluster agents can still reach the Git repository. However, if you change the synchronization parameters with the gcloud CLI or the console, the cluster doesn't apply them during the disconnection. You can temporarily overwrite them locally using `kubectl`. Reconnection overwrites any local changes.

### Policy Controller

Policy Controller enables the enforcement of fully programmable policies for your clusters. These policies act as "guardrails" and prevent any changes that violate security, operational, or compliance controls that you have defined.

Action | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Syncing configuration from a Git repository | In-cluster agents connect directly to the Git repository. You can change the repository URL or synchronization parameters with a Google Cloud API. | Configuration syncing remains unaffected. If you change the synchronization parameters with the gcloud CLI or in the console, the cluster doesn't apply them during the disconnection. You can temporarily overwrite them locally using `kubectl`. Reconnection overwrites any local changes. | Unlimited | Never use the [Fleet API](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleets#fleet-enabled-components) for Config Sync, and only configure it [by using the Kubernetes API.](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl)  
Enforcing policies on requests to the Kubernetes API | The in-cluster agent enforces constraints thanks to its integration with the Kubernetes API. You manage policies using the local Kubernetes API. You manage the system configuration of Policy Controller with a Google Cloud API. | Policy enforcement remains unaffected. You still manage policies using the local Kubernetes API. The system doesn't propagate changes to the Policy Controller system configuration using the Google Cloud API to the cluster, but you can temporarily overwrite them locally. Reconnection overwrites any local changes. | Unlimited | Never use the [Fleet API](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleets#fleet-enabled-components) for Policy Controller, and only configure it [by using the Kubernetes API.](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl)  
Installing, configuring, or upgrading Config Sync using the Google Cloud API | You use the Google Cloud API to manage the installation and upgrade of in-cluster agents. You also use this API (or the gcloud CLI, or the console) to manage the configuration of these agents. | In-cluster agents continue to operate normally. You can't install, upgrade, or configure in-cluster agents using the Google Cloud API. Any pending installations, upgrades, or configurations done using the API proceed upon reconnection. | Zero | Never use the [Fleet API](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleets#fleet-enabled-components) for Policy Controller, and only configure it [by using the Kubernetes API.](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl)  
Viewing system or sync status in the console | You can view the health of the in-cluster agents and the synchronization status using a Google Cloud API or the console. | Status information in the Google Cloud API or console becomes stale. The API shows a connection error. All the information remains available on a per-cluster basis using the local Kubernetes API. | Zero | Use the nomos CLI or the local Kubernetes API.  
  
## Security

This section outlines how security features, including identity, authentication, authorization, and secret management, are affected by a temporary disconnection from Google Cloud.

### Identity, authentication, and authorization

Distributed Cloud can connect directly to Cloud Identity for application and user roles, to manage workloads using Connect, or for endpoint authentication using [OIDC](https://openid.net/connect/). A disconnection from Google Cloud severs the connection to Cloud Identity, making those features unavailable. For workloads that require additional resiliency through a temporary disconnection, you can use [ GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity) to integrate with an LDAP or OIDC provider (including [ADFS](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services)) to configure end-user authentication.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Cloud Identity as identity provider, using the connect gateway | You can access Distributed Cloud resources using Cloud Identity as the identity provider, and connecting through the connect gateway. | The connect gateway requires a connection to Google Cloud. You aren't able to connect to your clusters during the disconnection. | Zero | Use GKE Identity Service to federate with another identity provider.  
Identity and authentication using a third-party identity provider | Supports OIDC and LDAP. You use the gcloud CLI to first log in. For OIDC providers, you can use the console to log in. You can then authenticate normally against the cluster API (for example, using `kubectl`). | As long as the identity provider remains accessible to both you and the cluster, then you can still authenticate against the cluster API. You can't log in through the console. You can only update the OIDC or LDAP configuration of your clusters locally, you can't use the console.  | Unlimited | -  
Authorization | Distributed Cloud supports role-based access control (RBAC). Roles can be attributed to users, groups, or service accounts. The system retrieves user identities and groups from the identity provider. | The RBAC system is local to the Kubernetes cluster, and disconnection from Google Cloud doesn't affect it. However, if it relies on identities coming from Cloud Identity then, they aren't available in case of disconnection. | Unlimited | -  
  
### Secret and key management

Secret and key management is an important part of your security posture. The behavior of Distributed Cloud in case of disconnection from Google Cloud depends on which service you are using for those features.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Secret and key management using Cloud Key Management Service and Secret Manager | You directly use Cloud Key Management Service for your cryptographic keys, and Secret Manager for your secrets. | Both Cloud Key Management Service and Secret Manager aren't available. | Zero | Use local systems instead.  
Secret and key management using Hashicorp Vault and Google Cloud services | You configure Hashicorp Vault to use Cloud Storage or Spanner to store secrets, and Cloud Key Management Service to manage keys. | If Hashicorp Vault runs on your on-premises cluster and the disconnection also impacts it, then secret storage and key management aren't available during the disconnection. | Zero | Use local systems instead.  
Secret and key management using Hashicorp Vault and on-premises services | You configure Hashicorp Vault to use an on-premises storage backend for secrets, and an on-premises key management system (such as a hardware security module). | Disconnection from Google Cloud has no impact. | Unlimited | -  
  
## Networking and network services

This section covers the networking and network services for on-premises clusters, including how they are impacted by a temporary disconnection from Google Cloud. It provides information on load balancing, Cloud Service Mesh, and other network services.

### Load Balancing

To expose Kubernetes Services hosted in an on-premises cluster to users, you have the following options:

  * Bare metal:

    * Use a provided bundled load balancer, [MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb) or [Bundled with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp).

    * [Manually configure your clusters to use your own load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/manual-lb), external to Distributed Cloud.

  * VMware:

    * Use the provided bundled load balancer, [MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb).

    * [Manually configure your clusters to use your own load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance), external to Distributed Cloud.




These load balancing options remain operational even if disconnected from Google Cloud.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
L4 bundled load-balancer | Provides L4 load balancing entirely locally with no dependency on Google Cloud APIs or network. | No change | Unlimited | -  
Manual or integrated load balancer | Supports F5 BIG-IP and others that are also hosted on-premises. | No change | Unlimited | -  
  
### Cloud Service Mesh

You can use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) to manage, observe, and secure communications across your services running in an on-premises cluster. Distributed Cloud doesn't support all Cloud Service Mesh features: see the [list of supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features) for more information.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Deploying or updating policies (routing, authorization, security, audit, etc.) | You can use the console, `kubectl`, `asmcli`, or `istioctl` to manage Cloud Service Mesh policies. | You can only use `kubectl` or `istioctl` to manage Cloud Service Mesh policies. | Unlimited | Use `kubectl` or `istioctl`  
Certificate authority (CA) | You can use either the in-cluster CA or the Cloud Service Mesh certificate authority to manage the certificates used by Cloud Service Mesh. | There is no impact if you are using the in-cluster CA.  
If you are using the Cloud Service Mesh certificate authority, then certificates expire after 24 hours. New service instances can't retrieve certificates. | Unlimited for in-cluster CA.  
Degraded service during 24h, and no service after 24h for Cloud Service Mesh certificate authority. | Use the in-cluster CA.  
Cloud Monitoring for Cloud Service Mesh | You can use Cloud Monitoring to store, explore and exploit HTTP-related metrics coming from Cloud Service Mesh. | Metrics aren't stored. | Zero | Use a compatible local monitoring solution such as Prometheus.  
Cloud Service Mesh audit logging | Cloud Service Mesh relies on the local Kubernetes logging facilities. The behavior depends on how you configured logging for your on-premises cluster. | Depends on how you configured logging for your on-premises cluster. | - | -  
Ingress gateway | You can define external IPs with the Istio Ingress Gateway. | No impact | Unlimited | -  
Istio Container Network Interface (CNI) | You can configure Cloud Service Mesh to use the Istio CNI instead of iptables to manage the traffic. | No impact | Unlimited | -  
Cloud Service Mesh end-user authentication for web applications | You can use the Cloud Service Mesh ingress gateway to integrate with your own identity provider (through OIDC) to authenticate and authorize end-users on web applications that are part of the mesh. | No impact | Unlimited | -  
  
### Other network services

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
DNS | The Kubernetes DNS server runs inside the cluster. | The Kubernetes DNS service works normally as it runs inside the cluster itself. | Unlimited | -  
Egress proxy | You can configure your on-premises clusters to use a proxy for egress connections.  | If your proxy runs on-premises, the cluster is still able to use it during a temporary disconnection. However, if the proxy loses the connection to Google Cloud, then all the scenarios from this document still apply. | Unlimited | -  
  
## Google Cloud Marketplace

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Deploying and managing applications and services from the Cloud Marketplace | The Cloud Marketplace is available in the console, and you can use it to discover, acquire, and deploy solutions. | You can't use the Cloud Marketplace. Some solutions from the Cloud Marketplace might have their own connectivity requirements which aren't documented here. | Zero | None  
  
## Support

This section covers the scenarios that you might have to go through while interacting with [Google Cloud support](https://docs.cloud.google.com/support) or your operating partner for a case related to your GKE on GDC clusters.

Feature | Connected behavior | Temporary disconnection behavior | Maximum disconnection tolerance | Loss of connectivity workaround  
---|---|---|---|---  
Sharing a cluster snapshot with the support team | You can create a cluster snapshot locally using the `bmctl check cluster` or `gkectl diagnose snapshot` commands. You share this snapshot through the normal support process. | You can still generate the snapshot as it is a local operation. If you lost access to Google Cloud and its support web interfaces, you can phone the support team provided you have subscribed to the Enhanced or Premium support plans. | Unlimited | -  
Sharing relevant log data with the support team | You can collect logs locally from your cluster and share them through the normal support process. | You can still collect logs from your cluster. If you lost access to Google Cloud and its support web interfaces, you can phone the support team provided you have subscribed to the Enhanced or Premium support plans. | Unlimited | -  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
