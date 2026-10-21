---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/firewall-rules/
title: Proxy and firewall rules \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:25.928796+00:00
---

# Proxy and firewall rules  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/firewall-rules/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Proxy and firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to set up proxy and firewall rules for Google Distributed Cloud.

**Note:** You cannot use [SSL MITM proxy](https://mitmproxy.org/) for your proxy, because this requires automatically deploying an extra CA certificate for the proxy, which is not supported.

## Allowlisting addresses for your proxy

If your organization requires outbound traffic to pass through a proxy server, allowlist the following addresses in your proxy server. Note that `www.googleapis.com` is needed, instead of `googleapis.com`:

  * dl.google.com (required by Google Cloud SDK installer)
  * gcr.io
  * www.googleapis.com
  * accounts.google.com
  * cloudresourcemanager.googleapis.com
  * container.googleapis.com
  * gkeconnect.googleapis.com
  * gkehub.googleapis.com
  * iam.googleapis.com
  * iamcredentials.googleapis.com
  * logging.googleapis.com
  * monitoring.googleapis.com
  * oauth2.googleapis.com
  * securetoken.googleapis.com
  * servicecontrol.googleapis.com
  * serviceusage.googleapis.com
  * storage.googleapis.com
  * sts.googleapis.com
  * checkpoint-api.hashicorp.com
  * releases.hashicorp.com (Optional. Required only if you use Terraform to create an admin workstation.)



If you use `gkeadm` to install Google Distributed Cloud, you don't need to allowlist the hashicorp URLs above.

Also, if your vCenter Server has an external IP address, allowlist its address in your proxy server.

## Firewall rules

Set up your firewall rules to allow the following traffic.

### Firewall rules for IP addresses available in the admin cluster

The IP addresses available in the admin cluster are listed in the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/ip-block-file). These IP addresses are used for the admin cluster control-plane node, admin cluster add-on nodes, and the user cluster control-plane node. Because the IP addresses for the admin cluster are not assigned to specific nodes, you must make sure that all of the firewall rules listed in the following table apply to all of the IP addresses available for the admin cluster.

**Note:** An admin cluster worker node can be either an admin cluster add-on node or a user cluster control-plane node.From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Admin cluster control-plane node | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  Cluster resizing.  
Admin cluster add-on nodes | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  User cluster lifecycle managemet.  
User cluster control-plane node | 1024 - 65535 |  vCenter Server API |  443 |  TCP/https |  Cluster resizing.  
Cloud Logging Collector, which runs on an admin cluster add-on node | 1024 - 65535 |  oauth2.googleapis.com  
logging.googleapis.com  
stackdriver.googleapis.com  
servicecontrol.googleapis.com  
storage.googleapis.com  
www.googleapis.com  |  443 |  TCP/https |   
Cloud Monitoring Collector, which runs on an admin cluster add-on node | 1024 - 65535 |  oauth2.googleapis.com  
monitoring.googleapis.com  
stackdriver.googleapis.com  
servicecontrol.googleapis.com  
|  443 |  TCP/https |   
Admin cluster control-plane node | 1024 - 65535 |  F5 BIG-IP API |  443 |  TCP/https |   
User cluster control-plane node | 1024 - 65535 |  F5 BIG-IP API |  443 |  TCP/https |   
Admin cluster control-plane node | 1024 - 65535 |  On-premises local Docker registry |  Depends on your registry |  TCP/https |  Required if Google Distributed Cloud is configured to use a local private Docker registry instead of gcr.io.  
User cluster control-plane node | 1024 - 65535 |  On-premises local Docker registry |  Depends on your registry |  TCP/https |  Required if Google Distributed Cloud is configured to use a local private Docker registry instead of gcr.io.  
Admin cluster control-plane node | 1024 - 65535 |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin cluster  |  443 |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
User cluster control-plane node | 1024 - 65535 |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin cluster  |  443  |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
Admin cluster worker nodes | 1024 - 65535 |  Admin cluster worker nodes |  All |  179 - bgp 443 - https 5473 - Calico/Typha 9443 - Envoy metrics 10250 - kubelet node port |  All worker nodes must be layer-2 adjacent and without any firewall.  
Admin cluster nodes | 1024 - 65535 |  Admin cluster pod CIDR |  all |  any |  External traffic get SNAT'ed on the first node and sent to pod IP.  
Admin cluster worker nodes | all |  User cluster nodes |  22 |  ssh |  API server to kubelet communication over an SSH tunnel.  
Admin cluster nodes | 1024 - 65535 |  IPs of Seesaw LB VMs of the admin cluster |  20255,20257 |  TCP/http |  LB config push and metrics monitoring. Only needed if you are using Bundled LB Seesaw.  
  
## Firewall rules for user cluster nodes

In the user cluster nodes, their IP addresses are listed in the [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/ip-block-file).

As with the admin cluster nodes, you don't know which IP address will be used for which node. Thus, all of the rules in the user cluster nodes apply to each user cluster node.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
User cluster worker nodes | all |  gcr.io  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for this cluster  |  443 |  TCP/https |  Download images from public Docker registries. Not required if using a private Docker registry.  
User cluster worker nodes | all |  F5 BIG-IP API |  443 |  TCP/https |   
User cluster worker nodes | all |  VIP of the pushprox server, which runs in the Admin cluster. |  8443 |  TCP/https |  Prometheus traffic.  
User cluster worker nodes | all |  User cluster worker nodes |  all |  22 - ssh 179 - bgp 443 - https 5473 - calico-typha 9443 - envoy metrics 10250 - kubelet node port" |  All worker nodes must be layer-2 adjacent and without any firewall.  
User cluster nodes | 1024 - 65535 |  User cluster pod CIDR |  all |  any |  External traffic get SNAT'ed on the first node and sent to pod IP.  
Cloud Logging Collector, which runs on a random user cluster worker node | 1024 - 65535 |  oauth2.googleapis.com  
logging.googleapis.com  
stackdriver.googleapis.com  
servicecontrol.googleapis.com  
www.googleapis.com  |  443 |  TCP/https |   
Connect agent, which runs on a random user cluster worker node. | 1024 - 65535 |  cloudresourcemanager.googleapis.com  
gkeconnect.googleapis.com  
gkehub.googleapis.com  
www.googleapis.com  
iam.googleapis.com  
iamcredentials.googleapis.com  
oauth2.googleapis.com  
securetoken.googleapis.com  
sts.googleapis.com  
accounts.google.com  
|  443 |  TCP/https |  [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect) traffic.  
Cloud Monitoring Collector, which runs on a random user cluster worker node | 1024 - 65535 |  oauth2.googleapis.com  
Monitoring.googleapis.com  
stackdriver.googleapis.com  
servicecontrol.googleapis.com  
|  443 |  TCP/https |   
User cluster nodes | 1024 - 65535 |  IPs of Seesaw LB VMs of the user cluster |  20255,20257 |  TCP/http |  LB config push and metrics monitoring. Only needed if you are using Bundled LB Seesaw.  
  
## Firewall rules for remaining components

These rules apply to all other components not listed in the tables for the admin cluster and user cluster nodes.

From | Source port | To | Port | Protocol | Description  
---|---|---|---|---|---  
Admin cluster pod CIDR | 1024 - 65535 |  Admin cluster pod CIDR |  all |  any |  Inter-pod traffic does L2 forwarding directly using source and destination IP within Pod CIDR.  
Admin cluster pod CIDR | 1024 - 65535 |  Admin cluster nodes |  all |  any |  Return traffic of external traffic.  
User cluster pod CIDR | 1024 - 65535 |  User cluster pod CIDR |  all |  any |  Inter-pod traffic does L2 forwarding directly using source and destination IP within Pod CIDR.  
User cluster pod CIDR | 1024 - 65535 |  User cluster nodes |  all |  any |  Return traffic of external traffic.  
Clients and application end users |  all |  VIP of Istio ingress |  80, 443 |  TCP |  End user traffic to the ingress service of a user cluster.  
Jump server to deploy the admin workstation |  ephemeral port range |  checkpoint-api.hashicorp.com  
releases.hashicorp.com  
vCenter Server API  
ESXi VMkernel (mgt) IPs of hosts in target cluster  
|  443 |  TCP/https |  Terraform deployment of the admin workstation. (Optional. Required only if you use Terraform to create an admin workstation.)  
Check ephemeral port range from `cat /proc/sys/net/ipv4/ip_local_port_range`.   
Admin workstation | 32768- 60999 |  gcr.io  
cloudresourcemanager.googleapis.com  
oauth2.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for this cluster  |  443 |  TCP/https |  Download Docker images from public Docker registries.  
Admin workstation | 32768- 60999 |  gcr.io  
cloudresourcemanager.googleapis.com  
iam.googleapis.com  
oauth2.googleapis.com  
serviceusage.googleapis.com  
storage.googleapis.com  
Any *.googleapis.com URL required for the services enabled for the admin or user clusters  |  443 |  TCP/https |  Preflight checks (validation).  
Admin workstation | 32768- 60999 |  vCenter Server API F5 BIG-IP API |  443 |  TCP/https |  Cluster bootstrapping.  
Admin workstation | 32768- 60999 |  ESXi VMkernel (mgt) IPs of hosts in target cluster |  443 |  TCP/https |  The admin workstation uploads the OVA to the datastore through the ESXi hosts.  
Admin workstation | 32768- 60999 |  Node IP of Admin Cluster control-plane VM |  443 |  TCP/https |  Cluster bootstrapping.  
Admin workstation | 32768- 60999 |  VIP of the admin cluster's Kubernetes API server VIPs of user clusters' Kubernetes API servers |  443 |  TCP/https |  Cluster bootstrapping. User cluster deletion.  
Admin workstation | 32768- 60999 |  Admin cluster control-plane node and worker nodes |  443 |  TCP/https |  Cluster bootstrapping. Control plane upgrades.  
Admin workstation | 32768- 60999 |  All admin cluster nodes and all user cluster nodes |  443 |  TCP/https |  Network validation as part of the `gkectl check-config` command.  
Admin workstation | 32768- 60999 |  VIP of the admin cluster's Istio ingress VIP of user clusters' Istio ingress |  443 |  TCP/https |  Network validation as part of the `gkectl check-config` command.  
Admin workstation | 32768- 60999 |  IPs of Seesaw LB VMs in both admin and user clusters Seesaw LB VIPs of both admin and user clusters |  20256,20258 |  TCP/http/gRPC |  Health check of LBs. Only needed if you are using Bundled LB Seesaw.  
Admin workstation | 32768- 60999 |  Node IP of the cluster control plane |  22 |  TCP |  Required if you need SSH access from the admin workstation to the admin cluster control plane.  
LB VM IPs | 32768- 60999 |  node IPs of the corresponding cluster |  10256: node health check  
30000 - 32767: healthCheckNodePort |  TCP/http |  Node health check. healthCheckNodePort is for services with externalTrafficPolicy set to Local. Only needed if you are using Bundled LB Seesaw.  
F5 Self-IP | 1024 - 65535 |  All admin and all user cluster nodes |  30000 - 32767 |  any |  For the data plane traffic that F5 BIG-IP load balances via a virtual server VIP to the node ports on the Kubernetes cluster nodes. Typically the F5 self-ip is on the same network/subnet as the Kubernetes cluster nodes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
