---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-trust/
title: Cluster trust \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:07.843216+00:00
---

# Cluster trust  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-trust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Cluster trust Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document is about the trust model in Google Kubernetes Engine (GKE) clusters, including communication within clusters and how requests are authenticated for components like control planes. This document assumes that you know about the following:

  * [Overview of GKE security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)
  * [Overview of GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)



This document is for Security specialists who want to understand GKE's cluster trust model. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Intracluster communication

GKE applies various security mechanisms to traffic between cluster components, as follows:

  * **Traffic between the control plane and nodes** : the control plane communicates with a node for managing containers. When the control plane sends a request, (for example, `kubectl logs`) to nodes, the request is sent over a Konnectivity proxy tunnel. Requests that the control plane sends are authenticated and protected by TLS. When a node sends a request to the control plane, for example, from the kubelet to the API server, that request is authenticated and encrypted using mutual TLS (mTLS).

All newly created and updated clusters use TLS 1.3 for control plane to node communication. TLS 1.2 is the minimum supported version for control plane to node communication.

  * **Traffic between nodes** : nodes are Compute Engine VMs. Connections between nodes inside the Google Cloud production network are authenticated and encrypted. For details, refer to the VM-to-VM section of the [Encryption in Transit whitepaper](https://docs.cloud.google.com/docs/security/encryption-in-transit#virtual_machine_to_virtual_machine).

  * **Traffic between Pods** : when a Pod sends a request to another Pod, that traffic isn't authenticated by default. GKE encrypts traffic between Pods on different nodes at the network layer. Traffic between Pods on the _same node_ isn't encrypted by default. For details about the network-layer encryption, see [Google Cloud virtual network encryption and authentication](https://docs.cloud.google.com/docs/security/encryption-in-transit#virtual-network).

You can restrict Pod-to-Pod traffic with a [NetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy), and you can encrypt all Pod-to-Pod traffic, including traffic on the same node, by using a service mesh like [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) or a different method of application-layer encryption.

  * **Traffic between control plane components** : traffic between various components that run on the control plane is authenticated and encrypted using TLS. The traffic never leaves a Google-owned network that's protected by firewalls.




## Root of trust

GKE has the following configuration:

  * The [cluster root Certificate Authority (CA)](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/) is used to validate the API server and kubelets' client certificates. That is, control planes and nodes have the same root of trust. Any kubelet within the cluster node pool can request a certificate from this CA using the `certificates.k8s.io` API, by submitting a [certificate signing request](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/#create-a-certificate-signing-request). The root CA has a limited lifetime as described in the Cluster root CA lifetime section.
  * In clusters that run etcd database instances on the control plane VMs, a separate per-cluster etcd peer CA is used to establish trust between etcd instances.
  * In all GKE clusters, a separate etcd API CA is used to establish trust between the Kubernetes API server and the etcd API.



### API server and kubelets

The API server and the kubelets rely on the cluster root CA for trust. In GKE, the control plane API certificate is signed by the cluster root CA. Each cluster runs its own CA, so that if one cluster's CA is compromised, no other cluster CA is affected.

An internal service manages root keys for this CA, which are non-exportable. This service accepts certificate signing requests, including those from the kubelets in each GKE cluster. Even if the API server in a cluster were compromised, the CA would not be compromised, so no other clusters would be affected.

Each node in the cluster is injected with a shared secret at creation, which it can use to submit certificate signing requests to the cluster root CA and obtain kubelet client certificates. These certificates are then used by the kubelet to authenticate its requests to the API server. This shared secret is reachable by Pods on the node, unless you enable [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) or [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

#### Cluster root CA lifetime

The cluster root CA has a limited lifetime, after which any certificates signed by the expired CA are invalid. Check the approximate expiry date of your cluster's CA by following the instructions in [Check credential lifetime](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#check_credential_lifetime).

You should manually rotate your credentials before your existing root CA expires. If the CA expires and you don't rotate your credentials, your cluster might enter an unrecoverable state. GKE has the following mechanisms to try and prevent unrecoverable clusters:

  * Your cluster enters a `DEGRADED` state seven days before CA expiry
  * GKE attempts an automatic credential rotation 30 days before CA expiry. This automatic rotation ignores maintenance windows and might cause disruptions as GKE recreates nodes to use new credentials. External clients, like kubectl in local environments, won't work until you update them to use the new credentials.

**Note:** This is a last resort to prevent an unrecoverable cluster. Don't rely on automatic rotation—instead, plan to rotate your credentials manually during maintenance periods well in advance of CA expiry.



To learn how to perform a rotation, see [Rotate your cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation).

### Cluster state storage

GKE clusters store the state of Kubernetes API objects as key-value pairs in a database. The Kubernetes API server in your control plane interacts with this database by using the [etcd API](https://etcd.io/docs/latest/learning/api/). GKE uses one of the following technologies to run the cluster state database:

  * **etcd** : the cluster uses etcd instances that run on the control plane VMs.
  * **Spanner** : the cluster uses a [Spanner](https://docs.cloud.google.com/spanner) database that runs outside of the control plane VMs.



Regardless of the database technology that a cluster uses, every GKE cluster serves the etcd API in the control plane. To encrypt traffic that involves the cluster state database, GKE uses one or both of the following per-cluster CAs:

  * **etcd API CA** : used to sign certificates for traffic to and from etcd API endpoints. An etcd API CA runs in every GKE cluster.
  * **etcd peer CA** : used to sign certificates for traffic between etcd database instances on the control plane. An etcd peer CA runs in any cluster that uses etcd databases. Clusters that use Spanner databases don't use the etcd peer CA.



Root keys for the etcd API CA are distributed to the metadata of each Compute Engine instance that the control plane runs on. The etcd API CA isn't shared between clusters.

The validity of the etcd CA certificate depends on the cluster creation date, as follows:

  * For clusters that were created before October 2021, the certificate is valid for 5 years.
  * For clusters that were created after October 2021, the certificate is valid for 30 years. Regardless of the cluster creation date, the new etcd CA certificate that's created during a certificate rotation is valid for 30 years. The certificate will be rotated automatically 6 months before it expires.



## Certificate rotation

To rotate all your cluster's API server and kubelet certificates, perform a [credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation). There is no way for you to trigger a rotation of the etcd certificates; this is managed for you in GKE.

**Note:** Performing a credential rotation causes GKE to upgrade all node pools to the closest supported node version, and causes brief downtime for the cluster API.

## What's next

  * [Read more about Managing TLS certificates in the Kubernetes documentation](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
