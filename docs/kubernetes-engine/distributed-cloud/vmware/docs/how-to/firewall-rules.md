---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules/
title: Proxy and firewall rules \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:50.057541+00:00
---

# Proxy and firewall rules  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Proxy and firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to set up proxy and firewall rules for Google Distributed Cloud (software only) for VMware. This page is for Networking specialists who implement data security systems such as firewalls. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

**Note:** You cannot use [SSL MITM proxy](https://mitmproxy.org/) for your proxy, because this requires automatically deploying an extra CA certificate for the proxy, which is not supported. Note: In 1.10, konnectivity is enabled by default. You need to create a firewall rule so that user worker nodes can access ports 8132 on the user control plane VIP address and get return packets.

## Allowlisting addresses for your proxy

If your organization requires outbound traffic to pass through a proxy server, allowlist the following addresses in your proxy server. Note that `www.googleapis.com` is needed, instead of `googleapis.com`:

  * dl.google.com **1**
  * gcr.io
  * us.gcr.io
  * www.googleapis.com
  * accounts.google.com
  * anthos.googleapis.com
  * anthosgke.googleapis.com
  * cloudresourcemanager.googleapis.com
  * compute.googleapis.com
  * connectgateway.googleapis.com
  * container.googleapis.com
  * gkeconnect.googleapis.com **2**
  * gkehub.googleapis.com
  * gkeonprem.googleapis.com
  * gkeonprem.mtls.googleapis.com
  * iam.googleapis.com
  * iamcredentials.googleapis.com
  * kubernetesmetadata.googleapis.com
  * logging.googleapis.com
  * monitoring.googleapis.com
  * oauth2.googleapis.com
  * opsconfigmonitoring.googleapis.com
  * securetoken.googleapis.com
  * servicecontrol.googleapis.com
  * serviceusage.googleapis.com
  * storage.googleapis.com
  * sts.googleapis.com
  * releases.hashicorp.com (Optional) **3**



**Notes** :

**1**`dl.google.com` is required by the Google Cloud SDK installer.

**2** If your cluster was registered to the fleet using a Google Cloud region, you need to allowlist `REGION-gkeconnect.googleapis.com` (for example, `us-central1-gkeconnect.googleapis.com`). If you didn't specify a region, the cluster uses the global Connect service instance, and you allowlist `gkeconnect.googleapis.com`. If you need to find your cluster's fleet membership location, run `gcloud container fleet memberships list`. For more information, see [`gkeConnect.location`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeconnect-location-field).

**3** If you don't use the Terraform client on your admin workstation to run commands such as `terraform apply`, then you don't need to allowlist `releases.hashicorp.com`. If you do use the Terraform client on your admin workstation, you can optionally allowlist `releases.hashicorp.com` so that you can check if the Terraform client version that you are using is the latest by running the [`terraform version`](https://developer.hashicorp.com/terraform/cli/commands/version) command.

Also, if your vCenter Server has an external IP address, allowlist its address in your proxy server.

## Firewall rules for admin clusters

The admin cluster IP addresses depend on whether Controlplane V2 is enabled on the user cluster and the version in which the cluster was created.

  * When Controlplane V2 is enabled, the control plane for a user cluster runs on the user cluster itself. When Controlplane V2 isn't enabled, the control plane for a user cluster runs on one or more nodes in the admin cluster, which is referred to as kubeception.

  * In 1.28 and higher, new HA admin clusters don't have add-on nodes.




The IP addresses of admin cluster add-on nodes (if they exist) and kubeception user cluster control plane nodes are listed in the admin cluster [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file). The admin cluster control plane nodes are configured in the `network.controlPlaneIPBlock.ips` section in the admin cluster configuration file.

Because the IP addresses in the admin cluster IP block file are not assigned to specific nodes, you must make sure that all of the firewall rules listed in the following table apply to all of the IP addresses available for the admin cluster.

**Note:** In the following table, an admin cluster worker node refers to either an add-on node or a Kubeception user cluster control plane node.

Set up your firewall rules to allow the following traffic.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Admin cluster control-plane node | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  Cluster resizing.  
Admin cluster add-on nodes | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  User cluster lifecycle management.  
Admin cluster add-on nodes | 32768- 60999 |  VIP of the admin cluster's Kubernetes API server VIPs of user clusters' Kubernetes API servers |  443 |  TCP/https |  User cluster create. User cluster update. User cluster upgrade. User cluster delete.  
Admin cluster control-plane nodes | 32768- 60999 |  gcr.io  
cloudresourcemanager.googleapis.com  
compute.googleapis.com  
iam.googleapis.com  
oauth2.googleapis.com  
serviceusage.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin or user clusters  
VIPs of user clusters' Kubernetes API servers  
VIP of the admin cluster's Kubernetes API server  
vCenter Server API  
Admin cluster F5 BIG_IP API  
User cluster F5 BIG_IP API  
Admin cluster NTP servers  
User cluster NTP servers  
Admin cluster DNS servers  
User cluster DNS servers  
|  443 |  TCP/https |  Preflight checks (validation). When you create, update, or upgrade user clusters. When you create, update or upgrade the admin cluster.  
Admin cluster control plane nodes | 32768- 60999 |  User cluster On-premises local Docker registry  
  
|  Depends on your registry |  TCP/https |  Preflight checks (validation). Required if a user cluster is configured to use a local private Docker registry instead of gcr.io. When you create or upgrade user clusters. When you create or upgrade the admin cluster.  
Admin cluster control-plane nodes | 32768- 60999 |  Admin cluster nodes  
User cluster nodes  
Admin cluster Load Balancer VIPs  
User cluster Load Balancer VIPs  
|  |  icmp |  Preflight checks (validation). When you create, update or upgrade user clusters. When you create, update or upgrade the admin cluster.  
Admin cluster control-plane nodes | 32768- 60999 |  User cluster worker nodes  
|  22 |  ssh |  Preflight checks (validation). When you upgrade user clusters. When you upgrade the admin cluster.  
User cluster control-plane node (kubeception only) | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  Cluster resizing.  
User cluster control-plane node (kubeception only) | 1024 - 65535 |  cloudresourcemanager.googleapis.com  
gkeconnect.googleapis.com or REGION-gkeconnect.googleapis.com  
gkehub.googleapis.com  |  443 |  TCP/https |  Access is required for fleet registration. See  note 2 after the list of URLs to allowlist.  
User cluster control-plane node (kubeception only) | 1024 - 65535 |  F5 BIG-IP API |  443 |  TCP/https |   
User cluster control-plane node (kubeception only) | 1024 - 65535 |  On-premises local Docker registry |  Depends on your registry |  TCP/https |  Required if Google Distributed Cloud is configured to use a local private Docker registry instead of gcr.io.  
User cluster control-plane node (kubeception only) | 1024 - 65535 |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin cluster  |  443  |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
Cloud Logging Collector, which runs on an admin cluster add-on node | 1024 - 65535 |  oauth2.googleapis.com  
logging.googleapis.com  
servicecontrol.googleapis.com  
storage.googleapis.com  
www.googleapis.com  |  443 |  TCP/https |   
Cloud Metadata Collector, which runs on an admin cluster add-on node | 1024 - 65535 |  opsconfigmonitoring.googleapis.com  |  443 |  TCP/https |   
Cloud Monitoring Collector, which runs on an admin cluster add-on node | 1024 - 65535 |  oauth2.googleapis.com  
monitoring.googleapis.com  
|  443 |  TCP/https |   
Admin cluster control-plane node | 1024 - 65535 |  F5 BIG-IP API |  443 |  TCP/https |   
Admin cluster control-plane node | 1024 - 65535 |  On-premises local Docker registry |  Depends on your registry |  TCP/https |  Required if Google Distributed Cloud is configured to use a local private Docker registry instead of gcr.io.  
Admin cluster control-plane node | 1024 - 65535 |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin cluster  |  443 |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
Admin cluster worker nodes | 1024 - 65535 |  Admin cluster worker nodes |  All |  179 - bgp 443 - https 5473 - Calico/Typha 9443 - Envoy metrics 10250 - kubelet node port |  All worker nodes must be layer-2 adjacent and without any firewall.  
Admin cluster nodes | 1024 - 65535 |  Admin cluster pod CIDR |  all |  any |  External traffic gets SNAT'ed on the first node and sent to pod IP.  
Admin cluster worker nodes | all |  User cluster nodes |  22 |  ssh |  Required for kubeception. API server to kubelet communication over an SSH tunnel. This should be skipped for Controlplane V2.  
Admin cluster nodes | 1024 - 65535 |  IPs of Seesaw LB VMs of the admin cluster |  20255,20257 |  TCP/http |  LB config push and metrics monitoring. Only needed if you are using Bundled LB Seesaw.  
Admin cluster nodes | 1024 - 65535 |  Admin cluster nodes |  7946 |  TCP/UDP |  MetalLB health check. Only needed if you are using Bundled LB MetalLB.  
Admin cluster nodes | All |  User cluster control-plane VIP |  443 |  https |  Required for Controlplane V2. Allow nodes and Pods in the admin cluster to talk to the Kubernetes API server of the user cluster.  
Admin cluster nodes | All |  User cluster control-plane nodes |  443 |  https |  Required for Controlplane V2. Allow nodes and Pods in the admin cluster to talk to the Kubernetes API server of the user cluster by using the IP address of a user cluster control-plane node.  
  
## Firewall rules for user cluster nodes

In the user cluster nodes, their IP addresses are listed in the [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file).

As with the admin cluster nodes, you don't know which IP address will be used for which node. Thus, all of the rules in the user cluster nodes apply to each user cluster node.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  Cluster resizing.  
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 |  cloudresourcemanager.googleapis.com  
gkeconnect.googleapis.com or REGION-gkeconnect.googleapis.com  
gkehub.googleapis.com  |  443 |  TCP/https |  Access is required for fleet registration. See  note 2 after the list of URLs to allowlist.  
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 |  On-premises local Docker registry |  Depends on your registry |  TCP/https |  Required if Google Distributed Cloud is configured to use a local private Docker registry instead of gcr.io.  
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin cluster  |  443  |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 |  F5 BIG-IP API |  443 |  TCP/https |   
User cluster control-plane node (Controlplane V2 only) | 1024 - 65535 | User cluster nodes | 14443 | TCP | ANG Webhook Service. Required if `advancedNetworking` is enabled. `kube-apiserver` communicates with `ang-controller-manager` for admission checks.  
User cluster worker nodes | all |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for this cluster  |  443 |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
User cluster worker nodes | all |  F5 BIG-IP API |  443 |  TCP/https |   
User cluster worker nodes | all |  VIP of the pushprox server, which runs in the Admin cluster. |  8443 |  TCP/https |  Prometheus traffic.  
User cluster worker nodes | all |  User cluster worker nodes |  all |  22 - ssh 179 - bgp 443 - https 5473 - calico-typha 9443 - envoy metrics 10250 - kubelet node port" |  All worker nodes must be layer-2 adjacent and without any firewall.  
User cluster worker nodes | all |  User control plane VIP |  443 |  TCP/https |   
User cluster worker nodes | All |  User control plane VIP |  8132 |  GRPC |  Required for kubeception. Konnectivity connection. This should be skipped for Controlplane V2.  
Admin cluster nodes | All |  User cluster vCenter Server |  443 |  https |  Allow the admin cluster to manage the lifecycle of the user cluster. Required if the admin and user clusters have different vCenter Servers.  
Admin cluster nodes | 1024 - 65535 | User cluster nodes | 14443 | TCP | ANG Webhook Service. Required if `advancedNetworking` is enabled. `kube-apiserver` communicates with `ang-controller-manager` for admission checks.  
User cluster nodes | 1024 - 65535 |  User cluster pod CIDR |  all |  any |  External traffic gets SNAT'ed on the first node and sent to pod IP.  
Cloud Logging Collector, which runs on a random user cluster worker node | 1024 - 65535 |  oauth2.googleapis.com  
logging.googleapis.com  
servicecontrol.googleapis.com  
www.googleapis.com  |  443 |  TCP/https |   
Connect agent, which runs on a random user cluster worker node. | 1024 - 65535 |  cloudresourcemanager.googleapis.com  
gkeconnect.googleapis.com or REGION-gkeconnect.googleapis.com  
gkehub.googleapis.com  
www.googleapis.com  
iam.googleapis.com  
iamcredentials.googleapis.com  
oauth2.googleapis.com  
securetoken.googleapis.com  
sts.googleapis.com  
accounts.google.com  
|  443 |  TCP/https |  [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect) traffic. See  note 2 after the list of URLs to allowlist.  
Cloud Metadata Collector, which runs on a random user cluster worker node | 1024 - 65535 |  opsconfigmonitoring.googleapis.com kubernetesmetadata.googleapis.com  |  443 |  TCP/https |   
Cloud Monitoring Collector, which runs on a random user cluster worker node | 1024 - 65535 |  oauth2.googleapis.com  
monitoring.googleapis.com  
|  443 |  TCP/https |   
User cluster nodes | 1024 - 65535 |  IPs of Seesaw LB VMs of the user cluster |  20255,20257 |  TCP/http |  LB config push and metrics monitoring. Only needed if you are using Bundled LB Seesaw.  
Users cluster nodes with enableLoadBalancer=true | 1024 - 65535 |  Users cluster nodes with enableLoadBalancer=true |  7946 |  TCP/UDP |  MetalLB health check. Only needed if you are using Bundled LB MetalLB.  
User cluster network | all |  User cluster control plane VIP |  443 |  TCP/https |   
  
## Firewall rules for remaining components

These rules apply to all other components not listed in the tables for the admin cluster and user cluster nodes.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Admin cluster pod CIDR | 1024 - 65535 |  Admin cluster pod CIDR |  all |  any |  Inter-pod traffic does L2 forwarding directly using source and destination IP within Pod CIDR.  
Admin cluster pod CIDR | 1024 - 65535 |  Admin cluster nodes |  all |  any |  Return traffic of external traffic.  
User cluster pod CIDR | 1024 - 65535 |  User cluster pod CIDR |  all |  any |  Inter-pod traffic does L2 forwarding directly using source and destination IP within Pod CIDR.  
User cluster pod CIDR | 1024 - 65535 |  User cluster nodes |  all |  any |  Return traffic of external traffic.  
Clients and application end users |  all |  VIP of Istio ingress |  80, 443 |  TCP |  End user traffic to the ingress service of a user cluster.  
Jump server to deploy the admin workstation |  ephemeral port range |  vCenter Server API  
ESXi VMkernel (mgt) IPs of hosts in target cluster  
|  443 |  TCP/https |  Check ephemeral port range from `cat /proc/sys/net/ipv4/ip_local_port_range`.   
Admin workstation | 32768- 60999 |  gcr.io  
cloudresourcemanager.googleapis.com  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for this cluster  |  443 |  TCP/https |  Download Docker images from public Docker registries.  
Admin workstation | 32768- 60999 |  gcr.io  
cloudresourcemanager.googleapis.com  
compute.googleapis.com  
iam.googleapis.com  
oauth2.googleapis.com  
serviceusage.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin or user clusters  
VIPs of user clusters' Kubernetes API servers  
VIP of the admin cluster's Kubernetes API server  
vCenter Server API  
F5 BIG-IP API  |  443 |  TCP/https |  Preflight checks (validation). When you create, update, upgrade, or delete clusters using `gkectl`.  
Admin workstation | 32768- 60999 |  vCenter Server API F5 BIG-IP API |  443 |  TCP/https |  Admin cluster create. User cluster create.  
Admin workstation | 32768- 60999 |  ESXi VMkernel (mgt) IPs of hosts in target cluster |  443 |  TCP/https |  The admin workstation uploads the OVA to the datastore through the ESXi hosts.  
Admin workstation | 32768- 60999 |  VIP of the admin cluster's Kubernetes API server VIPs of user clusters' Kubernetes API servers |  443 |  TCP/https |  Admin cluster create. Admin cluster update. User cluster create. User cluster update. User cluster delete.  
Admin workstation | 32768- 60999 |  Admin cluster control-plane node and worker nodes |  443 |  TCP/https |  Admin cluster create. Control plane upgrades.  
Admin workstation | 32768- 60999 |  All admin cluster nodes and all user cluster nodes |  443 |  TCP/https |  Network validation as part of the `gkectl check-config` command.  
Admin workstation | 32768- 60999 |  VIP of the admin cluster's Istio ingress VIP of user clusters' Istio ingress |  443 |  TCP/https |  Network validation as part of the `gkectl check-config` command.  
Admin workstation | 32768- 60999 |  oauth2.googleapis.com  
logging.googleapis.com  
monitoring.googleapis.com  
servicecontrol.googleapis.com  
storage.googleapis.com  
www.googleapis.com  |  443 |  TCP/https |  Cloud logging and monitoring access.  
Admin workstation | 32768- 60999 |  IPs of Seesaw LB VMs in both admin and user clusters Seesaw LB VIPs of both admin and user clusters |  20256,20258 |  TCP/http/gRPC |  Health check of LBs. Only needed if you are using Bundled LB Seesaw.  
Admin workstation | 32768- 60999 |  Node IP of the cluster control plane |  22 |  TCP |  Required if you need SSH access from the admin workstation to the admin cluster control plane.  
Admin workstation | 32768- 60999 | releases.hashicorp.com | 443 | TCP/https |  Optional. See  note 3 after the list of URLs to allowlist.   
LB VM IPs | 32768- 60999 |  node IPs of the corresponding cluster |  10256: node health check  
30000 - 32767: healthCheckNodePort |  TCP/http |  Node health check. healthCheckNodePort is for services with externalTrafficPolicy set to Local. Only needed if you are using Bundled LB Seesaw.  
F5 Self-IP | 1024 - 65535 |  All admin and all user cluster nodes |  30000 - 32767 |  any |  For the data plane traffic that F5 BIG-IP load balances via a virtual server VIP to the node ports on the Kubernetes cluster nodes. Typically the F5 self-ip is on the same network/subnet as the Kubernetes cluster nodes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
