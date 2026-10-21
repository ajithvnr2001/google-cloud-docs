---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy/
title: Control communication between Pods and Services using network policies \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:11.952058+00:00
---

# Control communication between Pods and Services using network policies  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Control communication between Pods and Services using network policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to control communication between your cluster's Pods and Services using GKE's _network policy enforcement_.

You can also control Pods' egress traffic to any endpoint or Service outside of the cluster using fully qualified domain name (FQDN) network policies. For more information, see [Control communication between Pods and Services using FQDNs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies).

## About GKE network policy enforcement

Network policy enforcement lets you create Kubernetes [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) in your cluster. By default, all Pods within a cluster can communicate with each other freely. Network policies create Pod-level firewall rules that determine which Pods and Services can access one another inside your cluster.

Defining network policy helps you enable things like [defense in depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)) when your cluster is serving a multi-level application. For example, you can create a network policy to ensure that a compromised front-end service in your application cannot communicate directly with a billing or accounting service several levels down.

Network policy can also make it easier for your application to host data from multiple users simultaneously. For example, you can provide secure multi-tenancy by defining a tenant-per-namespace model. In such a model, network policy rules can help ensure that Pods and Services in a given namespace cannot access other Pods or Services in a different namespace.

**Note:** For network policy enforcement to function correctly, GKE deploys Pods to your nodes that have elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb), such as the ability to patch all deployments and update the status of nodes. These permissions are required for GKE to enforce your network policies based on your configuration.

### NetworkPolicy plugins in GKE

Network policy requires a [network plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) to implement enforcement. GKE has the following mutually exclusive network plugins:

  * [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2), which is based on [Cilium](https://cilium.io/use-cases/network-policy/). GKE Dataplane V2 is the recommended network plugin for all clusters and is default for Autopilot clusters.
  * The [Calico](https://docs.tigera.io/calico/latest/network-policy/get-started/calico-policy/calico-network-policy) network policy plugin, which is available only in Standard clusters.



If a cluster isn't configured with a managed network plugin, a self-managed plugin is required to enforce network policy. If no network plugin is configured, network policies aren't enforced.

If you don't use a network plugin to enforce network policies, we recommend removing all network policies from the cluster. These network policies might cause unexpected traffic restrictions if you subsequently install a network plugin that enforces network policy.

If a GKE managed network plugin is not configured, and you have a network policy object in your cluster, GKE provides a [Recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) informing you that the policy might not be enforced.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.

* Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). 

### Requirements and limitations

The following requirements and limitations apply to both Autopilot and Standard clusters:

  * You must allow egress to the metadata server.
  * For more information about limitations for GKE Dataplane V2 clusters, see the [GKE Dataplane V2 known issues page](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#known_issues)



The following requirements and limitations only apply to Standard clusters:

  * You must allow egress to the metadata server if you use network policy with [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).
  * Enabling network policy enforcement increases the memory footprint of the `kube-system` process by approximately 128 MB, and requires approximately 300 millicores of CPU. This means that if you enable network policies for an existing cluster, you might need to [increase the cluster's size](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster#resize) to continue running your scheduled workloads.
  * Enabling network policy enforcement requires that your nodes be re-created. If your cluster has an active [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-window), your nodes are not automatically re-created until the next maintenance window. If you prefer, you can [manually upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) at any time.
  * The _required_ minimum cluster size to run network policy enforcement is three `e2-medium` instances or one machine type instance with more than 1 _allocatable_ vCPU. See [GKE known issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues) for more details.
  * Network policy isn't supported for clusters whose nodes are `f1-micro` or `g1-small` instances, as the resource requirements are too high.



For more information about node machine types and allocatable resources, see [Standard cluster architecture - Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes).

The following limitations are relevant to Pods that use the `hostNetwork: true` setting:

  * An empty `podSelector` field in a NetworkPolicy selects all Pods in that namespace except for Pods that have the `hostNetwork: true` setting.
  * In clusters that use GKE Dataplane V2, you can't use any of the following fields to identify traffic to or from Pods that use the `hostNetwork: true` setting:

    * `ingress[].from[].podSelector`
    * `ingress[].from[].namespaceSelector`
    * `egress[].to[].namespaceSelector`
    * `egress[].to[].podSelector`
    * `ingress[].from[].ipBlock`
    * `egress[].to[].ipBlock`
  * In clusters that use the legacy dataplane, you can use only the `ingress[].from[].ipBlock` and the `egress[].to[].ipBlock` fields to identify traffic to or from Pods that use the `hostNetwork: true` setting. You can't use any of the following fields to identify that traffic:

    * `ingress[].from[].podSelector`
    * `ingress[].from[].namespaceSelector`
    * `egress[].to[].namespaceSelector`
    * `egress[].to[].podSelector`



## Enable network policy enforcement

If you use GKE Dataplane V2 in your cluster, skip to Create a network policy.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

Before you proceed: network policies will be enforced when nodes are re-created.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To enable network policy enforcement on your cluster, perform the following tasks:

**Caution:** By default, enabling network policy enforcement for your cluster also enables enforcement for the cluster's nodes and might cause a disruption for manually deployed Pods. For more information, see Manually deployed Pods unscheduled.
     1. Run the following command to enable the add-on:
            
            gcloud container clusters update CLUSTER_NAME --update-addons=NetworkPolicy=ENABLED
            

Replace `CLUSTER_NAME` with the name of the cluster.

     2. Run the following command to enable network policy enforcement on your cluster, which in turn re-creates your cluster's node pools with network policy enforcement enabled:
            
            gcloud container clusters update CLUSTER_NAME --enable-network-policy
            

**Note:** Both enabling the `NetworkPolicy` add-on and enabling network policy enforcement on the nodes are required for network policies to function. Enabling only the add-on without enabling enforcement on the nodes will not enforce any policies. Typically, you should run both commands in sequence.



### Console

To enable network policy enforcement on your cluster:

**Caution:** By default, enabling network policy enforcement for your cluster also enables enforcement for the cluster's nodes and might cause a disruption for manually deployed Pods. For more information, see Manually deployed Pods unscheduled.

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Cluster Networking** , in the **Calico Kubernetes Network Policy** field, click _edit_ **Edit network policy**.

  4. In the **Edit network policy** dialog, select the **Enable Calico Kubernetes network policy for control plane** checkbox and click **Save changes**.

  5. Wait for your changes to apply. To monitor the progress, click _notifications_ **Notifications** in the top-right corner of the console.

  6. In the **Calico Kubernetes Network Policy** field, click _edit_ **Edit network policy** again.

  7. In the **Edit network policy** dialog, select the **Enable Calico Kubernetes network policy for nodes** checkbox.

  8. Click **Save changes**.




### API

To enable network policy enforcement, perform the following:

**Caution:** By default, enabling network policy enforcement for your cluster also enables enforcement for the cluster's nodes and might cause a disruption for manually deployed Pods. For more information, see Manually deployed Pods unscheduled.

  1. Specify the `networkPolicy` object inside the `cluster` object that you provide to [projects.zones.clusters.create](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create) or [projects.zones.clusters.update](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/update).

  2. The `networkPolicy` object requires an enum that specifies which network policy provider to use, and a boolean value that specifies whether to enable network policy. If you enable network policy but do not set the provider, the `create` and `update` commands return an error.




## Disable network policy enforcement in a Standard cluster

You can disable network policy enforcement by using the gcloud CLI, the Google Cloud console, or the GKE API. You cannot disable network policy enforcement in Autopilot clusters or clusters that use GKE Dataplane V2.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.**Caution:** When you disable network policy enforcement on the nodes (`--no-enable-network-policy`), GKE also removes the managed `ip-masquerade-agent` Pods from your cluster. If your cluster's network behavior relies on the IP masquerading provided by this agent, this removal might lead to unexpected changes in network traffic, particularly for Pod-to-external communication. Evaluate your network setup before you disable network policy enforcement.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To disable network policy enforcement, perform the following tasks:

     1. Disable network policy enforcement on your cluster:
    
    gcloud container clusters update CLUSTER_NAME --no-enable-network-policy
    

Replace `CLUSTER_NAME` with the name of the cluster.

After you run this command, GKE re-creates your cluster node pools with network policy enforcement disabled.

  3. Verify that all your nodes were re-created:
         
         kubectl get nodes -l projectcalico.org/ds-ready=true
         

If the operation is successful, the output is similar to the following:
         
         No resources found
         

If the output is similar to the following, then you must wait for GKE to finish updating the node pools:
         
         NAME                                             STATUS                     ROLES    AGE     VERSION
         gke-calico-cluster2-default-pool-bd997d68-pgqn   Ready,SchedulingDisabled   <none>   15m     v1.22.10-gke.600
         gke-calico-cluster2-np2-c4331149-2mmz            Ready                      <none>   6m58s   v1.22.10-gke.600
         

When you disable network policy enforcement, GKE might not update the nodes immediately if your cluster has a configured maintenance window or exclusion. For more information, see Cluster slow to update.

  4. After all of the nodes are re-created, disable the add-on:
         
         gcloud container clusters update CLUSTER_NAME --update-addons=NetworkPolicy=DISABLED
         




### Console

To disable network policy enforcement for an existing cluster, perform the following:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Networking** , in the **Network policy** field, click _edit_ **Edit network policy**.

  4. Clear the **Enable network policy for nodes** checkbox and click **Save Changes**.

  5. Wait for your changes to apply, and then click _edit_ **Edit network policy** again.

  6. Clear the **Enable network policy for master** checkbox.

  7. Click **Save Changes**.




### API

To disable network policy enforcement for an existing cluster, do the following:

  1. Update your cluster to use `networkPolicy.enabled: false` using the [`setNetworkPolicy` API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/setNetworkPolicy).

  2. Verify that all your nodes were re-created using the gcloud CLI:
         
         kubectl get nodes -l projectcalico.org/ds-ready=true
         

If the operation is successful, the output is similar to the following:
         
         No resources found
         

If the output is similar to the following, then you must wait for GKE to finish updating the node pools:
         
         NAME                                             STATUS                     ROLES    AGE     VERSION
         gke-calico-cluster2-default-pool-bd997d68-pgqn   Ready,SchedulingDisabled   <none>   15m     v1.22.10-gke.600
         gke-calico-cluster2-np2-c4331149-2mmz            Ready                      <none>   6m58s   v1.22.10-gke.600
         

When you disable network policy enforcement, GKE might not update the nodes immediately if your cluster has a configured maintenance window or exclusion. For more information, see Cluster slow to update.

  3. Update your cluster to use `update.desiredAddonsConfig.NetworkPolicyConfig.disabled: true` using the [`updateCluster` API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/update).




## Create a network policy

You can create a network policy using the Kubernetes Network Policy API.

For further details on creating a network policy, see the following topics in the [Kubernetes documentation](https://kubernetes.io/docs):

  * [Network Policy Overview](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
  * [Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)



## Network policy and Workload Identity Federation for GKE

If you use network policy with Workload Identity Federation for GKE, you must allow egress to the following IP addresses so your Pods can communicate with the [GKE metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#metadata_server).

  * For clusters running GKE version 1.21.0-gke.1000 and later, allow egress to `169.254.169.252/32` on ports `988` and `987`.
  * For clusters running GKE versions earlier than 1.21.0-gke.1000, allow egress to `127.0.0.1/32` on ports `988` and `987`.
  * For clusters running GKE Dataplane V2, allow egress to `169.254.169.254/32` on ports `80` and `8080`.



If you don't allow egress to these IP addresses and ports, you might experience disruptions during auto-upgrades.

## Migrating from Calico to GKE Dataplane V2

If you migrate your network policies from [Calico](https://github.com/projectcalico/calico) to GKE Dataplane V2, consider the following limitations:

  * You cannot use a Pod or Service IP address in the `ipBlock.cidr` field of a `NetworkPolicy` manifest. You must reference workloads using labels. For example, the following configuration is invalid:
        
        - ipBlock:
            cidr: 10.8.0.6/32
        

  * You cannot specify an empty `ports.port` field in a `NetworkPolicy` manifest. If you specify a protocol, you must also specify a port. For example, the following configuration is invalid:
        
        ingress:
        - ports:
          - protocol: TCP
        




## Working with Application Load Balancers

When an Ingress is applied to a Service to build an HTTP(S) load balancer, you must ensure your network policy allows traffic from the HTTP(S) [ Application Load Balancer health check IP address ranges](https://docs.cloud.google.com/load-balancing/docs/health-checks).

**Note:** In GKE Dataplane V2 environments, you can't use `ipBlock.cidr` to specify Pod or Service IP addresses within your network policy. However, you can use `ipBlock.cidr` to define other CIDR blocks, such as those required for load balancer health checks.

If you are not using container-native load balancing with network endpoint groups, node ports for a Service might forward connections to Pods on other nodes unless they are prevented from doing so by setting [`externalTrafficPolicy` to `Local`](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) in the Service definition. If `externalTrafficPolicy` is not set to `Local`, the network policy must also allow connections from other node IP addresses in the cluster.

Container-native load balancing, which is enabled by default with all GKE clusters, routes traffic directly to Pod endpoints. To achieve this, GKE Services are automatically annotated with `cloud.google.com/neg: '{"ingress": true}'`. However, enabling GKE network policy is one of the specific conditions that prevents container-native load balancing from being enabled by default. To maintain the benefits of container-native load balancing while using network policies, you must manually apply the following annotation to your Service manifests:
    
    
    kind: Service
    ...
      annotations:
        cloud.google.com/neg: '{"ingress": true}'
    ...
    

For the full list of default enablement conditions, see [Container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native_load_balancing).

**Note:** If network policy addon and enforcement are enabled on an existing cluster (rather than during cluster creation), GKE may continue to automatically apply the `cloud.google.com/neg: '{"ingress": true}'` annotation to new Services.

## Inclusion of Pod IP ranges in ipBlock rules

To control traffic for specific Pods, always select Pods by their namespace or Pod labels by using `namespaceSelector` and `podSelector` fields in your NetworkPolicy ingress or egress rules. Don't use the `ipBlock.cidr` field to intentionally select Pod IP address ranges, which are ephemeral in nature. The Kubernetes project doesn't explicitly define the behavior of the `ipBlock.cidr` field when it includes Pod IP address ranges. Specifying broad CIDR ranges in this field, like `0.0.0.0/0` (which include the Pod IP address ranges) might have unexpected results in different implementations of NetworkPolicy.

The following sections describe how the different implementations of NetworkPolicy in GKE evaluate the IP address ranges that you specify in the ipBlock.cidr field, and how that might impact Pod IP address ranges that are inherently included in broad CIDR ranges. Understanding the different behavior between implementations will help you to prepare for the results when you migrate to another implementation.

### ipBlock behavior in GKE Dataplane V2

With the GKE Dataplane V2 implementation of NetworkPolicy, Pod traffic is never covered by an `ipBlock` rule. Therefore, even if you define a broad rule such as `cidr: '0.0.0.0/0'`, it will not include Pod traffic. This is useful as it lets you to, for example, allow Pods in a namespace to receive traffic from the internet, without also allowing traffic from Pods. To also include Pod traffic, select Pods explicitly using an additional Pod or namespace selector in the ingress or egress rule definitions of the NetworkPolicy.

### ipBlock behavior in Calico

For the Calico implementation of NetworkPolicy, the `ipBlock` rules **do** cover Pod traffic. With this implementation, to configure a broad CIDR range without allowing Pod traffic, explicitly exclude the cluster's Pod CIDR range, like in the following example:
    
    
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: allow-non-pod-traffic
    spec:
      ingress:
      - from:
        - ipBlock:
          cidr: '0.0.0.0/0'
          except: ['POD_IP_RANGE']
    

In this example, `POD_IP_RANGE` is your cluster's Pod IPv4 address range, for example `10.95.0.0/17`. If you have multiple IP ranges, these can be included individually in the array, for example `['10.95.0.0/17', '10.108.128.0/17']`.

## Control network policy behavior with `externalTrafficPolicy`

The `externalTrafficPolicy` setting for your Service influences how Kubernetes applies network policies. This setting determines the source IP address that your Pods see for incoming traffic, and this can affect how Kubernetes evaluates NetworkPolicy rules.

**Note:** The `externalTrafficPolicy` field is valid only for externally-accessible services. You can set this field if your Service type is set to `LoadBalancer` or `NodePort`. Applying this field to a default `ClusterIP` Service results in an invalid configuration error.

`externalTrafficPolicy` has two possible values:

  * **`Cluster`:** When `externalTrafficPolicy` is set to `Cluster`, the destination Pod sees the source IP address as the IP address of the node where the traffic is initially received. If you have a NetworkPolicy that denies traffic based on client IP addresses but does not include the remote node IP addresses, it might unintentionally block external traffic from the external clients specified in the policy rules. To avoid this, create a policy that allows traffic from all nodes in the cluster. However, this policy will allow traffic from any external client.

  * **`Local`:** When `externalTrafficPolicy` is set to `Local`, the Pod sees the source IP address as the original client IP address. This allows for more granular control with network policies, as you can define rules based on the actual client IP addresses.




## Troubleshooting

### Pods can't communicate with control plane on clusters that use Private Service Connect

Pods on GKE clusters that use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) might experience a communication issue with the control plane if the Pod's egress to the control plane's internal IP address is restricted in egress network policies.

To mitigate this issue:

  1. Confirm that your cluster uses [Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect). On clusters that use Private Service Connect, if you use the `master-ipv4-cidr` flag when creating the subnet, GKE assigns each control plane an internal IP address from the values you defined in `master-ipv4-cidr`. Otherwise, GKE uses the cluster node subnet to assign each control plane an internal IP address.

  2. Configure your cluster's egress policy to allow traffic to the control plane's internal IP address.

To find the control plane's internal IP address:

### gcloud

To look for `privateEndpoint`, run the following command:
         
         gcloud container clusters describe CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of the cluster.

This command retrieves the `privateEndpoint` of the specified cluster.

### Console

     1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

     2. From the navigation pane, under **Clusters** , click the cluster whose internal IP address you want to find.

     3. Under **Cluster basics** , navigate to `Internal endpoint`, where the internal IP address is listed.

Once you are able to locate the `privateEndpoint` or `Internal endpoint`, configure your cluster's egress policy to allow traffic to the control plane's internal IP address. For more information, see [Create a network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#creating_a_network_policy).




### Cluster slow to update

When you enable or disable network policy enforcement on an existing cluster, GKE might not update the nodes immediately if the cluster has a configured [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

You can manually upgrade a node pool by setting the `--cluster-version` flag to the same GKE version that the control plane is running. You must use the Google Cloud CLI to perform this operation. For more information, see [caveats for maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats).

### Manually deployed Pods unscheduled

When you enable network policy enforcement on the control plane of existing cluster, GKE unschedules any ip-masquerade-agent or calico node Pods that you manually deployed.

GKE does not reschedule these Pods until network policy enforcement is enabled on the cluster nodes and the nodes are recreated.

If you have configured a [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), this might cause an extended disruption.

To minimize the duration of this disruption, you can manually assign the following labels to the cluster nodes:

  * `node.kubernetes.io/masq-agent-ds-ready=true`
  * `projectcalico.org/ds-ready=true`



### Network policy not taking effect

If a NetworkPolicy is not taking effect, you can troubleshoot using the following steps:

  1. Confirm that network policy enforcement is enabled. The command that you use depends on if your cluster has GKE Dataplane V2 enabled.

If your cluster has GKE Dataplane V2 enabled, run the following command:
         
         kubectl -n kube-system get pods -l k8s-app=cilium
         

If the output is empty, network policy enforcement is not enabled.

If your cluster does not have GKE Dataplane V2 enabled, run the following command:
         
         kubectl get nodes -l projectcalico.org/ds-ready=true
         

If the output is empty, network policy enforcement is not enabled.

  2. Check the Pod labels:
         
         kubectl describe pod POD_NAME
         

Replace `POD_NAME` with the name of the Pod.

The output is similar to the following:
         
         Labels:        app=store
                        pod-template-hash=64d9d4f554
                        version=v1
         

  3. Confirm that the labels on the policy match the labels on the Pod:
         
         kubectl describe networkpolicy
         

The output is similar to the following:
         
         PodSelector: app=store
         

In this output, the `app=store` labels match the `app=store` labels from the previous step.

  4. Check if there are any network policies selecting your workloads:
         
         kubectl get networkpolicy
         

If the output is empty, no NetworkPolicy was created in the namespace and nothing is selecting your workloads. If the output is not empty, check if the policy selects your workloads:
         
         kubectl describe networkpolicy
         

The output is similar to the following:
         
         ...
         PodSelector:     app=nginx
         Allowing ingress traffic:
            To Port: <any> (traffic allowed to all ports)
            From:
               PodSelector: app=store
         Not affecting egress traffic
         Policy Types: Ingress
         




## Known issues

### Pod stuck in `containerCreating` state

There can be scenario where GKE clusters with [Calico](https://github.com/projectcalico/calico) network policy enabled might experience an issue where Pods get stuck in `containerCreating` state.

Under the Pod **Events** tab, you see a message similar to the following:
    
    
    plugin type="calico" failed (add): ipAddrs is not compatible with
    configured IPAM: host-local
    

To mitigate this issue, use host-local ipam for Calico instead of calico-ipam in GKE clusters.

### 503 Calico readiness probe failures in large clusters

In large clusters that do a lot of autoscaling, Calico might restart frequently enough to cause disruption. In some situations, you might want to desensitize its vertical autoscaler with higher values for the `step` field.

To change the values, edit the `calico-node-vertical-autoscaler` ConfigMap to use the same parameter values for the `base` and `max` field. This approach disables dynamic CPU resource requests, stopping fluctuating CPU requests with node churn:
    
    
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: calico-node-vertical-autoscaler
      namespace: kube-system
      labels:
        kubernetes.io/cluster-service: "true"
        addonmanager.kubernetes.io/mode: EnsureExists
    data:
      node-autoscaler: |-
        {
          "calico-node": {
            "requests": {
              "cpu": {
                "base": "200m",
                "step": "100m",
                "nodesPerStep": 50,
                "max": "200m"
              }
            }
          }
        }
    

Setting the value of the `base` field (`200m`) higher than the value of the `step` field (`100m`) helps ensure that `calico-node` Pods have enough CPU resources for clusters of up to 60 nodes, according to the [autoscaler formula](https://github.com/kubernetes-sigs/cluster-proportional-vertical-autoscaler?tab=readme-ov-file#calculation-of-resource-requests-and-limits), because the requested CPU will no longer scale with the number of nodes.

**Note:** Changes in the ConfigMap within the `kube-system` namespace won't be reconciled by GKE.

## What's next

  * [Follow the Network Policies tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy).

  * [Read the Kubernetes documentation about network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

  * [Implement common approaches to restrict traffic using network policies](https://github.com/GoogleCloudPlatform/anthos-security-blueprints/tree/master/restricting-traffic).

  * [Using network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).

  * [Use security insights to explore other ways to harden your infrastructure](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
