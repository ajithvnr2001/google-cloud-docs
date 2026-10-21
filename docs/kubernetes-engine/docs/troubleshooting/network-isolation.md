---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-isolation/
title: Troubleshoot network isolation in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:17.033162+00:00
---

# Troubleshoot network isolation in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/network-isolation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot network isolation in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Incorrect [network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) configurations in Google Kubernetes Engine (GKE) can cause problems such as cluster creation timeouts, nodes failing to register, control plane unreachability, or inability to pull images.

Use this document for guidance on troubleshooting problems such as control plane access, CIDR range overlaps, image pull errors from public repositories, and issues related to VPC Network Peering or Private Service Connect.

This information is important for Platform admins and operators and Network administrators who configure and manage network-isolated GKE clusters to meet security and compliance requirements. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## GKE cluster not running

Deleting the firewall rules that allow ingress traffic from the cluster control plane to nodes on port 10250, or deleting the default route to the default internet gateway, causes a cluster to stop functioning. If you delete the default route, you must ensure traffic to necessary Google Cloud services is routed. For more information, see [custom routing](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing-custom).

## Timeout when creating a cluster

Symptoms
    Clusters created in version 1.28 or earlier with private nodes require a peering route between VPCs. However, only one peering operation can happen at a time. If you attempt to create multiple clusters with the preceding characteristics at the same time, cluster creation may time out.
Resolution
    

Use one of the following solutions:

  * Create clusters in version 1.28 or earlier serially so that the VPC peering routes already exist for each subsequent cluster without an external endpoint. Attempting to create a single cluster may also time out if there are operations running on your VPC.

  * Create clusters in version 1.29 or later.




## VPC Network Peering connection is accidentally deleted

Symptoms
    

When you accidentally [delete a VPC Network Peering connection](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#deleting-peer), the cluster goes in a repair state and all nodes show an `UNKNOWN` status. You won't be able to perform any operation on the cluster since reachability to the control plane is disconnected. When you inspect the control plane, logs will display an error similar to the following:
    
    
    error checking if node NODE_NAME is shutdown: unimplemented
    

Potential causes
    

You accidentally deleted the VPC Network Peering connection.

**Resolution**

  1. Create a new GKE cluster with a version that predates the PSC switch and its specific configurations. This action is necessary to force the re-creation of the VPC peering connection, which will restore the old cluster to its normal operation. 
     * Use the following specific configurations for the new cluster: 
       * **Release channel:** extended
       * **Cluster version:** a version that's earlier than 1.29, such as 1.28.15-gke.2403000
       * **Master IPv4 CIDR:** a specific IP address range, such as `--master-ipv4-cidr=172.16.0.192/28`
  2. Monitor the original cluster status. 
     * After the new cluster is created (and thus the VPC peering is re-established), the original cluster should recover from its repair state, and its nodes should return to a `Ready` status.
  3. Delete the temporarily created GKE cluster. 
     * After the original cluster is fully restored and operates normally, you can delete the temporarily created GKE cluster.



## Private Service Connect endpoint and forwarding rule are accidentally deleted

Symptoms
    

When you accidentally delete a Private Service Connect endpoint or forwarding rule, the cluster goes into a repair state and all nodes show an `UNKNOWN` status. You won't be able to perform any operation on the cluster since access to the control plane is disconnected. When you inspect the control plane, logs will display an error similar to the following:
    
    
    error checking if node NODE_NAME is shutdown: unimplemented
    

Potential causes
    

You accidentally deleted the Private Service Connect endpoint or forwarding rule. Both resources are named `gke-[cluster-name]-[cluster-hash:8]-[uuid:8]-pe` and permit the control plane and nodes to privately connect.

Resolution
    

[Rotate your control plane IP address](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation).

## Cluster overlaps with active peer

Symptoms
    

Attempting to create a cluster without an external endpoint returns an error similar to the following:
    
    
    Google Compute Engine: An IP range in the peer network overlaps with an IP
    range in an active peer of the local network.
    

Potential causes
    

You chose an overlapping control plane CIDR.

Resolution
    

Use one of the following solutions:

  * Delete and recreate the cluster using a different control plane CIDR.
  * Recreate the cluster in version 1.29 and include the `--enable-private-nodes` flag.



## Can't reach control plane of a cluster with no external endpoint

Increase the likelihood that your cluster control plane is reachable by implementing any of the cluster endpoint access configuration. For more information, see [access to cluster endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#control-plane-access).

Symptoms
    

After creating a cluster with no external endpoint, attempting to run `kubectl` commands against the cluster returns an error similar to one of the following:
    
    
    Unable to connect to the server: dial tcp [IP_ADDRESS]: connect: connection
    timed out.
    
    
    
    Unable to connect to the server: dial tcp [IP_ADDRESS]: i/o timeout.
    

Potential causes
    

`kubectl` is unable to talk to the cluster control plane.

Resolution
    

Use one of the following solutions:

  * Enable DNS access for a simplified way of securely accessing your cluster. For more information, see [DNS-based endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#dns-based-endpoint).

  * Verify credentials for the cluster has been generated for kubeconfig or the correct context is activated. For more information on setting the cluster credentials see [generate kubeconfig entry](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

  * Verify that accessing the control plane using the IP-based external endpoint is permitted. Disabling external access to the cluster control plane isolates the cluster from the internet. With this configuration, only authorized internal network CIDR ranges or reserved network have access to the control plane.

    1. Verify the origin IP address is authorized to reach the control plane:
           
           gcloud container clusters describe CLUSTER_NAME \
                 --format="value(controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig)"\
                 --location=COMPUTE_LOCATION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.

If your origin IP address is not authorized, the output may return an empty result (only curly braces) or CIDR ranges which does not include your origin IP address
    
    cidrBlocks:
      cidrBlock: 10.XXX.X.XX/32
      displayName: jumphost
      cidrBlock: 35.XXX.XXX.XX/32
      displayName: cloud shell
    enabled: true
    

    2. [Add authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#define-ip-access) to access control plane.

  * If you run the `kubectl` command from an on-premises environment or a region different from the cluster's location, ensure that control plane private endpoint global access is enabled. For more information, see [Access using the control plane's internal IP address from any region](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#control-plane-access).

    1. Describe the cluster to see control access config response:
           
           gcloud container clusters describe CLUSTER_NAME \
               --location=COMPUTE_LOCATION \
               --flatten "controlPlaneEndpointsConfig.ipEndpointsConfig.globalAccess"
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster.
       * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) for the cluster.

A successful output is similar to the following:
    
    enabled: true
    

    2. If `null` is returned, [enable access using the control plane's internal IP address from any region](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#control-plane-access).




## Can't create cluster due to overlapping IPv4 CIDR block

Symptoms
    

`gcloud container clusters create` returns an error similar to the following:
    
    
    The given master_ipv4_cidr 10.128.0.0/28 overlaps with an existing network
    10.128.0.0/20.
    

Potential causes
    

You specified a control plane CIDR block that overlaps with an existing subnet in your VPC.

Resolution
    

Specify a CIDR block for `--master-ipv4-cidr` that does not overlap with an existing subnet.

## Can't create cluster due to services range already in use by another cluster

Symptoms
    

Attempting to create a cluster returns an error similar to the following:
    
    
    Services range [ALIAS_IP_RANGE] in network [VPC_NETWORK], subnetwork
    [SUBNET_NAME] is already used by another cluster.
    

Potential causes
    

The following configurations might cause this error:

  * You chose a service range which is still in use by another cluster, or the cluster was not deleted.
  * There was a cluster using that services range which was deleted but the secondary ranges metadata was not properly cleaned up. Secondary ranges for a GKE cluster are saved in the Compute Engine metadata and should be removed once the cluster is deleted. Even when a clusters is successfully deleted, the metadata might not be removed.


Resolution
    

Follow these steps:

  1. Check if the services range is in use by an existing cluster. You can use the [`gcloud container clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list) command with the `filter` flag to search for the cluster. If there is an existing cluster using the services ranges, you must delete that cluster or create a new services range.
  2. If the services range is not in use by an existing cluster, then manually [remove the metadata entry](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-metadata) that matches the services range you want to use.



## Can't create a subnet

Symptoms
    

When you attempt to create a cluster with an automatic subnet, or to create a custom subnet, you might encounter the any of the following errors:
    
    
    An IP range in the peer network overlaps
    with an IP range in one of the active peers of the local network.
    
    
    
    Error: Error waiting for creating GKE cluster: Invalid value for field
    PrivateClusterConfig.MasterIpv4CidrBlock: x.x.x.x/28 conflicts with an
    existing subnet in one of the peered VPCs.
    

Potential causes
    

The control plane CIDR range you specified overlaps with another IP range in the cluster. This subnet creation error can also occur if you're attempting to reuse the `master-ipv4-cidr` CIDRs used in a recently deleted cluster.

Resolution
    

Try using a different CIDR range.

## Can't pull image from public Docker Hub

Symptoms
    

A Pod running in your cluster displays a warning in `kubectl describe`:
    
    
    Failed to pull image: rpc error: code = Unknown desc = Error response
    from daemon: Get https://registry-1.docker.io/v2/: net/http: request canceled
    while waiting for connection (Client.Timeout exceeded while awaiting
    headers)
    

Potential causes
    

Nodes with private IP addresses only need additional configuration to meet the [internet access requirements](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs). However, the nodes can access Google Cloud APIs and services, including Artifact Registry, if you have [enabled Private Google Access and met its network requirements](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config).

Resolution
    

Use one of the following solutions:

  * Copy the images in your cluster from Docker Hub to Artifact Registry. See [Migrating containers from a third-party registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers) for more information.

  * GKE automatically checks `mirror.gcr.io` for cached copies of frequently-accessed Docker Hub images.

  * If you must pull images from Docker Hub or another public repository, use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) or an instance-based proxy that is the target for a static `0.0.0.0/0` route.




## Failure to create new external webhooks

The following error occurs when you attempt to create ValidatingWebhookConfigurations or MutatingWebhookConfigurations that use the `clientConfig.url` field to contact a webhook server that's outside the cluster:
    
    
    ValidatingAdmissionPolicy 'gke-restrict-webhook-url' denied request: Egress
    traffic from the API server through the control plane is disabled. As a result,
    direct API server calls to external webhook servers are blocked. To connect to
    external webhooks, update any webhook configurations that use clientConfig.url
    to use clientConfig.service instead.
    

This error occurs if your cluster configuration prevents direct egress traffic from the Kubernetes API server by disabling the external IP addresses of the control plane VM instances. GKE uses a ValidatingAdmissionPolicy to prevent the creation of, or updates to, webhook configurations that use `clientConfig.url` field.

To verify the cause of this error, describe your cluster configuration:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --format='value(controlPlaneEgress)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster, such as `us-central1` or `us-central1-a`.



If egress traffic from the API server is disabled, the output is `NONE`.

To resolve this error, update your webhook configurations to use the `clientConfig.service` field. This field lets the API server send admission requests to a Service in your cluster instead of sending traffic to an IP address or URL. For more information about how to configure the webhooks and Service, see [External webhook configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#external-webhook-configuration).

If you delete the ValidatingAdmissionPolicy, your webhook creation or update request will succeed, but admission requests to the webhook server will fail.

## Failures in external admission webhook requests

The following error occurs when you attempt to deploy Kubernetes resources that trigger admission webhook servers outside of your cluster VPC network:
    
    
    Error from server (InternalError): error when creating "STDIN": Internal error occurred: failed calling webhook WEBHOOK_NAME": failed to call webhook: Post "WEBHOOK_URL": proxyconnect tcp: dial tcp: lookup master-internet-access-unavailable.localhost on 169.254.169.254:53: no such host
    

This error occurs if all of the following conditions are met:

  * The webhook configuration uses an IP address or URL to contact the external webhook server.
  * The cluster configuration prevents direct egress traffic from the Kubernetes API server by disabling the external IP addresses of the control plane VM instances.



To verify the cause of this error, describe your cluster configuration:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --format='value(controlPlaneEgress)'
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster, such as `us-central1` or `us-central1-a`.



If egress traffic from the API server is disabled, the output is `NONE`.

To resolve this error, follow these steps:

  1. Identify any ValidatingWebhookConfigurations or MutatingWebhookConfigurations in the cluster that use the `clientConfig.url` field.
  2. Update your webhook configurations to use the `clientConfig.service` field. This field lets the API server send admission requests to a Service in your cluster instead of sending traffic to an IP address or URL. For more information about how to configure the webhooks and Service, see [External webhook configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#external-webhook-configuration).



## API request that triggers admission webhook timing out

Symptoms
    

An API request that triggers an admission webhook configured to use a service with a `targetPort` other than 443 times out, causing the request to fail:
    
    
    Error from server (Timeout): request did not complete within requested timeout 30s
    

Potential causes
    

By default, the [firewall](https://docs.cloud.google.com/vpc/docs/firewalls) does not allow TCP connections to nodes except on ports 443 (HTTPS) and 10250 (kubelet). An admission webhook attempting to communicate with a Pod on a port other than 443 will fail if there is not a custom firewall rule that permits the traffic.

Resolution
    

[Add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#add_firewall_rules) for your specific use case.

## Can't create cluster due to health check failing

Symptoms
    

After creating a Standard cluster with private node pools, it gets stuck at the health check step and reports an error similar to one of the following:
    
    
    All cluster resources were brought up, but only 0 of 2 have registered.
    
    
    
    All cluster resources were brought up, but: 3 nodes out of 4 are unhealthy
    

Potential causes
    

The following configurations might cause this error:

  * Cluster nodes can't download required binaries from the Cloud Storage API (`storage.googleapis.com`).
  * Firewall rules restricting egress traffic.
  * Shared VPC IAM permissions are incorrect.
  * Private Google Access requires you to configure DNS for `*.gcr.io`.


Resolution
    

Use one of the following solutions:

  * Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) on the subnet for node network access to `storage.googleapis.com`, or enable Cloud NAT to allow nodes to communicate with `storage.googleapis.com` endpoints.

  * For node read access to `storage.googleapis.com`, confirm that the service account assigned to the cluster node has [storage read access](https://docs.cloud.google.com/storage/docs/authentication#oauth-scopes).

  * Ensure that you have either a Google Cloud firewall rule to allow all egress traffic or [configure a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#add_firewall_rules) to allow egress traffic for nodes to the cluster control plane and `*.googleapis.com`.

  * Create the [DNS configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) for `*.gcr.io`.

  * If you have a non-default firewall or route setup, configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  * If you use VPC Service Controls, set up [Container Registry or Artifact Registry for GKE clusters](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke).

  * Ensure you have not deleted or modified the [automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws) for Ingress.

  * If using Shared VPC, ensure you have configured the required [IAM permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#enabling_and_granting_roles).




## kubelet Failed to create pod sandbox

Symptoms
    

After creating a cluster with private nodes, it reports an error similar to one of the following:
    
    
    Warning  FailedCreatePodSandBox  12s (x9 over 4m)      kubelet  Failed to create pod sandbox: rpc error: code = Unknown desc = Error response from daemon: Get https://registry.k8s.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
    
    
    
    NetworkReady=false reason:NetworkPluginNotReady message:docker: network plugin is not ready: cni config uninitialized
    

Potential causes
    

The `calico-node` or `netd` Pod can't reach `*.gcr.io`.

Resolution
    

Ensure you have completed the required [setup for Container Registry or Artifact Registry](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-gke).

## Private nodes created but not joining the cluster

For clusters using nodes with private IP addresses only, often when using custom routing and third-party network appliances on the VPC, the default route (`0.0.0.0/0`) is redirected to the appliance instead of the default internet gateway. In addition to the control plane connectivity, you need to ensure that the following destinations are reachable:

  * *.googleapis.com
  * *.gcr.io
  * gcr.io



Configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) for all three domains. This best practice allows the new nodes to startup and join the cluster while keeping the internet bound traffic restricted.

## Workloads on GKE clusters unable to access internet

Pods running in nodes with private IP addresses can't access the internet. For example, after running the `apt update` command from the Pod `exec shell`, it reports an error similar to the following:
    
    
    0% [Connecting to deb.debian.org (199.232.98.132)] [Connecting to security.debian.org (151.101.130.132)]
    

If subnet secondary IP address range used for Pods in the cluster is not configured on Cloud NAT gateway, the Pods can't connect to the internet as they don't have an external IP address configured for Cloud NAT gateway.

Ensure you configure the Cloud NAT gateway to apply at least the following subnet IP address ranges for the subnet that your cluster uses:

  * Subnet primary IP address range (used by nodes)
  * Subnet secondary IP address range used for Pods in the cluster
  * Subnet secondary IP address range used for Services in the cluster



To learn more, see [how to add secondary subnet IP range used for Pods](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#specify_subnet_ranges_for_nat).

## Direct IP access can't be disabled for public clusters

Symptoms
    

After disabling the IP address endpoint, you see an error message similar to the following:
    
    
    Direct IP access can't be disabled for public clusters
    

Potential causes
    

Your cluster uses [legacy network](https://docs.cloud.google.com/vpc/docs/legacy).

Resolution
    

Migrate your clusters to Private Service Connect. For more information about the status of the migration, [contact support](https://cloud.google.com/support-hub/) .

## Direct IP access can't be disabled for clusters in the middle of PSC migration

Symptoms
    

After disabling the IP address endpoint, you see an error message similar to the following:
    
    
    Direct IP access can't be disabled for public clusters
    

Potential causes
    

Your cluster uses [legacy network](https://docs.cloud.google.com/vpc/docs/legacy).

Resolution
    

Use one of the following solutions:

  * Manually recreate all node pools in a different version.
  * Wait until GKE automatically upgrades the node pools during a maintenance event.



## Control plane internal endpoint can't be enabled

Symptoms
    

When attempting to enable the internal endpoint of your cluster's control plane, you see error messages similar to the following:
    
    
    private_endpoint_enforcement_enabled can't be enabled when envoy is disabled
    
    
    
    private_endpoint_enforcement_enabled is unsupported. Please upgrade to the minimum support version
    

Potential causes
    

Your cluster needs to do IP address rotation or a version update.

Resolution
    

Use one of the following solutions:

  * [Rotate your control plane IP address](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation) to enable Envoy.
  * Upgrade your cluster to 1.28.10-gke.1058000 version or later.



## Cluster creation fails when organization policies are defined

Symptoms
    

When attempting to create a cluster, you see an error message similar to the following:
    
    
    compute.disablePrivateServiceConnectCreationForConsumers violated for projects
    

Potential causes
    

The cluster endpoint or backend is blocked by a consumer organization policy.

Resolution
    

Allow instances to create endpoints with the `compute.restrictPrivateServiceConnectProducer` constraint by completing the steps in [Consumer-side organization policies](https://docs.cloud.google.com/vpc/docs/private-service-connect-security#consumer-side-org-policies).

## The Private Service Connect endpoint might leak during cluster deletion

Symptoms
    

After creating a cluster, you might see one of the following symptoms:

  * You can't see a connected endpoint under Private Service Connect in your [Private Service Connect-based cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect).

  * You can't delete the subnet or VPC network allocated for the internal endpoint in a cluster that uses Private Service Connect. An error message similar to the following appears:
        
        projects/<PROJECT_ID>/regions/<REGION>/subnetworks/<SUBNET_NAME> is already being used by projects/<PROJECT_ID>/regions/<REGION>/addresses/gk3-<ID>
        



Potential causes
    

On GKE clusters that use Private Service Connect, GKE deploys a Private Service Connect endpoint by using a forwarding rule that allocates an internal IP address to access the cluster's control plane in a control plane's network. To protect the communication between the control plane and the nodes by using Private Service Connect, GKE keeps the endpoint invisible, and you can't see it on Google Cloud console or gcloud CLI.

Resolution
    

To prevent leaking the Private Service Connect endpoint before cluster deletion, complete the following steps:

  1. Assign the [`Kubernetes Engine Service Agent role`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#predefined) to the GKE service account.
  2. Ensure that the `compute.forwardingRules.*` and `compute.addresses.*` permissions are not explicitly denied from GKE service account.



If you see the Private Service Connect endpoint leaked, [contact support](https://cloud.google.com/support-hub/) .

## Unable to parse the cluster's authorized network

Symptoms
    

You can't create a cluster in version 1.29 or later. An error message similar to the following appears:
    
    
    Unable to parse cluster.master_ipv4_cidr "" into a valid IP address and mask
    

Potential causes
    

Your Google Cloud project uses private IP-based webhooks. Therefore, you are unable to create a cluster with Private Service Connect. Instead, your cluster uses VPC Network Peering which parses the `master-ipv4-cidr` flag.

Resolution
    

Use one of the following solutions:

  * Continue to create your VPC Network Peering cluster and include the `master-ipv4-cidr` to define valid CIDRs. This solution has the following limitations:

    * The `master-ipv4-cidr` flag has been deprecated on the Google Cloud console. To update this flag you can only use Google Cloud CLI or Terraform.
    * VPC Network Peering is deprecated in GKE version 1.29 or later.
  * Migrate your private IP-based webhooks by completing the steps in [Private Service Connect Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#limitations). Then, [contact support](https://cloud.google.com/support-hub/) to opt in to use clusters with Private Service Connect.




## Unable to define internal IP address range in clusters with public nodes

Symptoms
    

You can't define an internal IP address range by using the `--master-ipv4-cidr` flag. An error message similar to the following appears:
    
    
    ERROR: (gcloud.container.clusters.create) Cannot specify --master-ipv4-cidr
      without --enable-private-nodes
    

Potential causes
    

You are defining an internal IP address range for the control plane with the `master-ipv4-cidr` flag in a cluster without the `enable-private-nodes` flag enabled. To create a cluster with `master-ipv4-cidr` defined, you must configure your cluster to provision nodes with internal IP addresses (private nodes) by using the `enable-private-nodes` flag.

Resolution
    

Use one of the following solutions:

  * Create a cluster with the following command:
        
        gcloud container clusters create-auto CLUSTER_NAME \
            --enable-private-nodes \
            --master-ipv4-cidr CP_IP_RANGE
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `CLUSTER_NAME`: the internal IP address range for the control plane.
  * Update your cluster to provision nodes with only IP addresses. To learn more, see [Configure your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#enable-private-nodes-cluster).




## Unable to schedule public workloads on Autopilot clusters

Symptoms
    On Autopilot clusters, if your cluster uses private nodes only, you can't schedule workloads in public Pods using the `cloud.google.com/private-node=false` nodeSelector.
Potential causes
    The configuration of the `private-node` flag set as `false` in the Pod's nodeSelector is only available in clusters in version 1.30.3 or later.
Resolution
    Upgrade your cluster to 1.30 version or later.

## Access to the DNS-based endpoint is disabled

Symptoms
    

Attempting to run kubectl commands against the cluster returns an error similar to the following:
    
    
    couldn't get current server API group list:
    control_plane_endpoints_config.dns_endpoint_config.allow_external_traffic is
    disabled
    

Potential causes
    

DNS-based access has been disabled on your cluster.

Resolution
    

Enable access to the control plane by using the DNS-based endpoint of the control plane. To learn more, see [Modify the control plane access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#modify_the_control_plane_access).

## Nodes fail to allocate IP address during scaling

Symptoms
    

Attempting to expand subnet's primary IP address range to the list of authorized networks returns an error similar to the following:
    
    
     authorized networks fields cannot be mutated if direct IP access is disabled
    

Potential causes
    

You have disabled the cluster [IP-based endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).

Resolution
    

Disable and enable the cluster [IP-based endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation) by using the `enable-ip-access` flag.

## Too many CIDR blocks

`gcloud` returns the following error when attempting to create or update a cluster with more than 50 CIDR blocks:
    
    
    ERROR: (gcloud.container.clusters.update) argument --master-authorized-networks: too many args
    

To resolve this issue, try the following:

  * If your cluster doesn't use [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect) or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering), ensure that you specify no more than 50 CIDR blocks.
  * If your cluster uses [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect) or [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering), specify no more than 100 CIDR blocks.



## Unable to connect to the server

`kubectl` commands time out due to incorrectly configured CIDR blocks:
    
    
    Unable to connect to the server: dial tcp MASTER_IP: getsockopt: connection timed out
    

When you create or update a cluster, [ensure that you specify the correct CIDR blocks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#define-ip-access).

## Nodes can access public container images despite network isolation

Symptoms
    

You might observe that in a GKE cluster configured for network isolation, pulling a common public image like `redis` works, but pulling a less common or private image fails.

This behavior is expected due to GKE's default configuration and doesn't indicate that GKE has bypassed your network isolation.

Potential causes
    

This behavior occurs because of two features working together:

  * **Private Google Access** : this feature lets nodes with internal IP addresses connect to Google Cloud APIs and services without needing public IP addresses. Private Google Access is activated on the cluster's subnet within the VPC that's used by the nodes in the cluster. When a cluster or node pool is created or updated with the `--enable-private-nodes` flag, GKE automatically enables Private Google Access on this subnet. The only exception is if you use a Shared VPC, where you must manually enable Private Google Access.
  * **Google's image mirror (`mirror.gcr.io`)**: by default, GKE configures its nodes to first try pulling images from `mirror.gcr.io`, a Google-managed Artifact Registry that caches frequently requested public container images.



When you try to pull an image like `redis`, your node uses the private path from Private Google Access to connect to `mirror.gcr.io`. Because `redis` is a very common image, it exists in the cache, and the pull succeeds. However, if you request an image that isn't in this public cache, the pull fails because your isolated node has no other way to reach its original source.

Resolution
    

If an image that you need isn't available in the `mirror.gcr.io` cache, host it in your own private Artifact Registry repository. Your network-isolated nodes can access this repository using Private Google Access.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
