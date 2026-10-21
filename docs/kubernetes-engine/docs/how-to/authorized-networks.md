---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks/
title: About network isolation in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:24:53.087236+00:00
---

# About network isolation in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About network isolation in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can customize network access for the control plane and nodes of your Google Kubernetes Engine (GKE) cluster to improve network security for the cluster and its workloads. This document explains the various types of isolation that you can configure for your cluster, the benefits of isolating your network, and any limitations that you must consider before you isolate your cluster.

To configure specific isolation levels for your cluster, see the following documents:

  * [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [Restrict egress traffic from the API server](https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane)

**Best practice** : 

Plan and design your network isolation configuration with your organization's Network architects, Network engineers, Network administrators, or another team who is responsible for the definition, implementation, and maintenance of the network architecture.

## Types of network access

Components in your cluster—like the control plane, API server, and nodes—send and receive network traffic for different purposes. You can customize your cluster's isolation by controlling one or more of the following types of network access:

  * **Access to the control plane from external sources** : customize who can access your control plane to perform tasks like running `kubectl` commands in the cluster.
  * **Access to external webhooks from the API server** : customize whether the Kubernetes API server can send traffic directly to [external webhook servers](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#contacting-the-webhook) through the control plane.
  * **Access to the nodes from external sources:** customize whether external clients on the public internet can access your nodes.



## Access to the control plane from external sources

In this section, you'll consider who can access your control plane.

Every GKE cluster has a [control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) that handles Kubernetes API requests. The control plane runs on a virtual machine (VM) that is in a VPC network in a Google-managed project. A regional cluster has multiple replicas of the control plane, each of which runs on its own VM. Principals like cluster administrators use a control plane endpoint to access the cluster for tasks like running `kubectl` commands or deploying workloads. The control plane endpoint is used by external clients to access the cluster, and isn't used for direct communication with the Compute Engine VM instances that host the control plane replicas. The control plane has the following kinds of endpoints for access to the cluster:

The control plane has two kinds of endpoints for cluster access:

  * DNS-based endpoint
  * IP-based endpoints

**Best practice** : 

Use only the DNS-based endpoint to access your control plane for simplified configuration and a flexible and policy-based layer of security.

### DNS-based endpoint

The DNS-based endpoint gives a unique and immutable DNS or fully qualified domain name (FQDN) for each cluster control plane. This DNS name can be used to access your control plane for its entire lifecycle. The DNS name resolves to an endpoint that is accessible from any network reachable by Google Cloud APIs, including on-premises or other cloud networks. Enabling the DNS-based endpoint eliminates the need for a bastion host or proxy nodes to access the control plane from other VPC networks or external locations.

To access the control plane endpoint, you need to configure IAM roles and policies, and authentication tokens. For more details on the exact permissions required, see [Customize your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).

In addition to IAM policies and tokens, you can also configure the following access attributes:

  * **IP address or network-based controls with[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)**: to enhance security for your GKE cluster control plane, VPC Service Controls adds another layer of access security. It uses context-aware access based on attributes like network origin.

VPC Service Controls doesn't directly support clusters with public IP addresses for their control plane. However, GKE clusters, including both private and public clusters, gain protection from VPC Service Controls when you access them using the DNS-based endpoint.

You configure VPC Service Controls to protect your GKE cluster's DNS-based endpoint by including `container.googleapis.com` and `kubernetesmetadata.googleapis.com` in your service perimeter's restricted services list. Adding these APIs to your service perimeter will enable VPC-SC for _all_ GKE API operations. This configuration helps ensure that your defined security perimeters govern access to the control plane.

By using both IAM policies and VPC Service Controls to secure access to the DNS-based endpoint, you create a multi-layer security model for your cluster control plane. VPC Service Controls integrates with supported Google Cloud services. It aligns your cluster's security configuration with the data you host in other Google Cloud services.

  * **Private Service Connect or Cloud NAT** : to access the DNS-based endpoint from clients that don't have public internet access. By default, the DNS-based endpoint is accessible through Google Cloud APIs that are available on the public internet. To learn more, see [DNS-based endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#dns-based-endpoint) in the Customize your network isolation page.

  * **Kubernetes authentication credentials** : to authenticate to the DNS-based endpoint by using [Kubernetes ServiceAccount bearer tokens](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens) or [X.509 client certificates](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#x509-client-certificates). These authentication methods are disabled by default in GKE clusters. You can enable these methods when you configure the DNS-based endpoint for a cluster.

**Best practice** : 

ServiceAccount tokens and client certificates can add complexity and management overhead to your security configuration. Unless your use case requires one of these authentication methods, [use IAM credentials to authenticate to your control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).




### IP-based endpoints

Optionally, you can also configure access to the control plane using IP-based endpoints.

#### Terminology related to clusters and IP addresses

  * **Google Cloud external IP addresses** :

    * External IP addresses assigned to any VM used by any customer hosted on Google Cloud. Google Cloud owns these IP addresses. To learn more, see [Where can I find Compute Engine IP ranges?](https://docs.cloud.google.com/compute/docs/faq#find_ip_range)

    * External IP addresses used by Google Cloud products such as Cloud Run or Cloud Run functions. Any client hosted on Google Cloud can instantiate these IP addresses. Google Cloud owns these IP addresses.

  * **Google-reserved IP addresses** : External IP addresses for GKE cluster management purposes. These IP addresses include GKE managed processes and other production Google services. Google owns these IP addresses.

  * **GKE cluster IP address ranges** : Internal IP addresses assigned to the cluster that GKE uses for the cluster's nodes, Pods, and Services.

  * **Internal IP addresses** : IP addresses from your cluster's VPC network. These IP addresses can include your cluster IP address, on-premises networks, the [RFC 1918 ranges](https://datatracker.ietf.org/doc/html/rfc1918), or the privately used public IP (PUPI) addresses that include non-RFC 1918 ranges.

  * **External IP-based cluster endpoint** : The IP address of the external endpoint, which GKE assigns to the control plane.

  * **External control plane VM IP address** : The external IP address that's assigned to every VM instance that runs the control plane and is used only for egress traffic from the API server.

  * **Internal endpoint** : The internal IP address that GKE assigns to the control plane.

  * **VPC network** : A virtual network in which you create subnets with IP address ranges specifically for the cluster's nodes and Pods.




When using IP-based endpoints, you have two options:

  * **Expose the control plane on both the external and internal endpoints**. This means that the control plane's external endpoint is accessible from an external IP address, and the internal endpoint is accessible from your cluster's VPC network. Nodes will communicate with the control plane on the internal endpoint only.

  * **Expose the control plane on the internal endpoint only.** This means that clients on the internet cannot connect to the cluster and the control plane is accessible from any IP address from your cluster's VPC network. Nodes will communicate with the control plane on the internal endpoint only.

This is the most secure option when using IP-based endpoints as it prevents all internet access to the control plane. This is a good choice if you have workloads that—for example—require controlled access due to data privacy and security regulations.




In both of the preceding options, you can restrict which IP addresses reach the endpoints by configuring _authorized networks_. If you use IP-based endpoints, then we strongly recommend that you add at least one authorized network. Authorized networks grant control plane access to a specific set of trusted IPv4 addresses, and provide protection and additional security benefits for your GKE cluster.

**Best practice** : 

Enable authorized networks when using IP-based endpoints to secure your GKE cluster.

#### How authorized networks work

Authorized networks provide an IP-based firewall that controls access to the GKE control plane. Access to the control plane depends on the source IP addresses. When you enable authorized networks, you configure the IP addresses for which you want to allow access to the GKE cluster control plane endpoint as a CIDR block list.

The following table shows:

  * The preset IP addresses that can always access the GKE control plane regardless of whether you enable authorized networks.
  * The configurable IP addresses that can access the control plane when you allowlist them by enabling authorized networks.

Control plane endpoints | Preset IP addresses that can _always_ access the endpoints | Configurable IP address that can access the endpoints after enabling authorized networks  
---|---|---  
External and internal endpoints enabled | 

  * Google-reserved IP addresses
  * GKE cluster IP address ranges

| 

  * Allowlisted external IP addresses
  * Allowlisted internal IP addresses
  * Google Cloud external IP addresses

  
Only internal endpoint enabled | 

  * Google-reserved IP addresses
  * GKE cluster IP address ranges

| 

  * Allowlisted internal IP addresses.

  
**Note:** If you only want internal IP addresses to access the control plane, ensure that you enable authorized networks _after_ disabling the control plane's external endpoint. If you enable authorized networks with allowlisted external IP addresses before disabling the control plane external endpoint, the allowlisted addresses can still access the control plane internal endpoint.

With an authorized network, you can also configure the region from which an internal IP address can reach your control plane's internal endpoint. You can choose to allow access only from the cluster's VPC network, or from any Google Cloud region in a VPC or on-premises environment.

### Limitations of using IP-based endpoints

  * If you [expand a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet) that is used by a cluster with authorized networks, you must update the authorized network configuration to include the expanded IP address range.
  * If you have clients connecting from networks with dynamic IP addresses, such as employees on home networks, you must update the list of authorized networks frequently to maintain access to the cluster.
  * Disabling access to the control plane's external endpoint prevents you from interacting with your cluster remotely. If you need to remotely access the cluster, you must use a [bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host#create-bastion) which forwards client traffic to the cluster. In contrast, using a DNS-based endpoint only requires setting up IAM permissions.
  * IP-based endpoints don't directly integrate with VPC Service Controls. VPC Service Controls operate at the service perimeter level to control data access and movement within Google Cloud. We recommend using both a DNS-based endpoint with VPC Service Controls for robust security defense.
  * You can specify up to 100 authorized IP address ranges (external and internal IP addresses inclusive).



### Transport security for control plane connections

When you send requests to the Kubernetes API server in a cluster by using methods like client libraries or the `kubectl` CLI, the connection between the client and the server is [protected by TLS](https://kubernetes.io/docs/concepts/security/controlling-access/#transport-security).

To establish a TLS connection, the server presents a certificate to the client. The specific server that presents the certificate and the certificate authority (CA) that signs the certificate depend on the endpoint that you use to access the control plane, as follows:

  * **DNS-based endpoint** : the Google Front End (GFE) service that hosts the DNS-based endpoint presents the certificate. The certificate is signed by a public, generally recognized Google CA. The client can use the public CA information to validate the certificate.
  * **IP-based endpoints** : the Kubernetes API server presents the certificate. The certificate is signed by the cluster root CA. To validate the API server certificate, the client must use the public certificate of the cluster root CA. When you set up a client in an environment that doesn't have access to the gcloud CLI, you must add the root CA certificate for the cluster to your `~/.kube/config` file. For more information, see [Authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#environments-without-gcloud).



## Access to external sources from the API server

The GKE cluster control plane runs Kubernetes [control plane components](https://kubernetes.io/docs/concepts/architecture/#control-plane-components) like the API server, scheduler, and controllers. The control plane runs on a Compute Engine VM instance that's owned by GKE in a managed project. Regional clusters and Autopilot clusters have multiple replicas of the control plane, each of which runs on its own VM instance.

By default, each of these Compute Engine VM instances has an external IP address that's assigned directly to the VM. This IP address is used only to send admission requests from the Kubernetes API server on an instance to [admission webhook servers](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#contacting-the-webhook) that run outside of the cluster, for example in a different cloud service or on-premises. This IP address is used only if the admission webhooks directly contact the webhook server by using the server URL or the server IP address.

To improve the security posture of your control plane, you can disable the external IP address on your control plane VM instances. In the event of a compromise, potential attackers can't use these external IP addresses to communicate. You can customize egress traffic from the API server in the following ways:

  * **No egress traffic (`NONE`)**: disable the external IP address of each control plane instance and route API server egress traffic to a [black hole](https://en.wikipedia.org/wiki/Black_hole_\(networking\)#Black_hole_filtering). All non-critical egress traffic from the API server to external destinations is blocked, including traffic to Google Cloud services outside of the cluster. This option doesn't affect critical system traffic or traffic from your nodes.
  * **All egress traffic (`VIA_CONTROL_PLANE`)**: retain the external IP address of each control plane instance and let the API server use the IP address for egress traffic. This option is the default in GKE.



To learn how to customize your cluster for one of these options, see [Restrict egress traffic from the API server](https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane).

### External webhook configuration

When you set control plane egress restrictions to `NONE`, the API server can't make any direct calls to external IP addresses or fully qualified domain names (FQDNs). The `NONE` setting has the following effects on external webhooks:

  * In version 1.35.1-gke.1396000 and later, GKE prevents the creation of, or updates to, ValidatingWebhookConfigurations or MutatingWebhookConfigurations that use the `clientConfig.url` field.
  * Existing webhook configurations that use the `clientConfig.url` field to contact an external server stop working.



To create and use external webhook servers, you must do the following:

  1. Update your ValidatingWebhookConfigurations or MutatingWebhookConfigurations to use the `clientConfig.service` field. This field lets the API server send requests to a Service endpoint, such as `my-webhook.default.svc`, in your cluster. These requests aren't blocked, because the traffic is inside the cluster. For more information, see [Service reference](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#service-reference).
  2. Configure the Service to route traffic to your external webhook server. You can use one of the following traffic routing designs, depending on your security and operational requirements:

     * **Proxy Pods** : use a Deployment or StatefulSet as the backend for your Service. Configure the Pods to function as proxies that redirect incoming admission requests to your external webhook server. This design lets you perform extra tasks, like inspecting and modifying the admission requests.
     * **EndpointSlices** : create the Service without a selector, and then manually add an [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) that maps the Service to the IP address of the external webhook server. This design routes traffic without modifying the requests.



When you design your webhook configuration, consider the following factors:

  * **Authentication and credentials** : consider how to authenticate with the external webhook server. Your traffic routing workflow must also manage how credentials (such as API keys, mTLS certificates, and OAuth tokens) are applied to connections.
  * **Security and network control** : consider the attack surface of your routing design and your options for security and auditing. The design that you implement affects what constraints you can apply to the traffic. For example, you can use [NetworkPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) with proxy Pods.
  * **Observability and reliability** : consider how to monitor connections. For example, you can configure proxy Pods to emit metrics, or you can implement network observability for EndpointSlices.



## Access to the nodes from external sources

This section discusses isolating _nodes_ within a Kubernetes cluster.

### Enable private nodes

Prevent external clients from accessing nodes by provisioning those nodes only with internal IP addresses, making the nodes private. Workloads running on nodes without an external IP address cannot reach the internet unless NAT is enabled on the cluster's network. You can change these settings at any time.

You can enable private nodes at an individual cluster level or at the node pool (for Standard) or workload (for Autopilot) level. Enabling private nodes at the node pool or workload level overrides any node configuration at the cluster level.

If you update a public node pool to private mode, workloads that require access outside the cluster network might fail in the following scenarios:

  * Clusters in a Shared VPC network where Private Google Access is not enabled. Manually [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) to ensure GKE downloads the assigned node image. For clusters that aren't in a Shared VPC network, GKE automatically enables Private Google Access.

  * Workloads that require access to the internet where Cloud NAT is not enabled or a custom NAT solution is not defined. To allow egress traffic to the internet, [enable Cloud NAT](https://docs.cloud.google.com/nat/docs/gke-example) or a custom NAT solution.




Whether or not you enable private nodes, the control plane still communicates with all nodes through internal IP addresses only.

## Benefits of network isolation

The following are the benefits of network isolation:

  * **Flexibility** :

    * Clusters have unified and flexible configuration. Clusters with or without external endpoints all share the same architecture and support the same functionality. You can secure access based on controls and best practices that meet your needs. All communication between the nodes in your cluster and the control plane use an internal IP address.
    * You can change the control plane access and cluster node configuration settings at any time without having to re-create the cluster.
    * You can choose to enable the external endpoint of the control plane if you need to manage your cluster from any location with internet access, or from networks or devices that aren't directly connected with your VPC. Or you can disable the external endpoint for enhanced security if you need to maintain network isolation for sensitive workloads. In either case, you can use authorized networks to limit access to trusted IP ranges.
  * **Security** :

    * DNS-based endpoints with VPC Service Controls provide a multi-layer security model that protects your cluster against unauthorized networks as well as unauthorized identities accessing the control plane. VPC Service Controls integrate with Cloud Audit Logs to monitor access to the control plane.
    * Private nodes, and the workloads running on these nodes, are not directly accessible from the public internet, significantly reducing the potential for external attacks on your cluster.
    * You can block control plane access from Google Cloud external IP addresses or from external IP addresses to fully isolate the cluster control plane and reduce exposure to potential security threats.
    * You can disable the external IP addresses of your control plane VM instances to prevent attackers from using the IP addresses.
  * **Compliance** : If you work in an industry with strict regulations for data access and storage, private nodes help with compliance by ensuring that sensitive data remains within your private network.

  * **Control** : Private nodes give you granular control over how traffic flows in and out of your cluster. You can configure firewall rules and network policies to allow only authorized communication. If you operate across multi-cloud environments, private nodes can help you establish secure and controlled communication between different environments.

  * **Cost** : By enabling private nodes, you can reduce costs for nodes that don't require an external IP address to access public services on the internet.




## What's next

  * Follow the instructions in [Configuring network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation) to experiment with network isolation.
  * Learn how to [restrict egress traffic from the API server](https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane).
  * Learn more about [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect).
  * Read an overview of [cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).
  * Learn about [networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
