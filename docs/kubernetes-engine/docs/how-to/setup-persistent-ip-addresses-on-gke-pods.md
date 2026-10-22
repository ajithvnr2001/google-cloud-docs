---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods/
title: Control communication with persistent IP addresses \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:03.129778+00:00
---

# Control communication with persistent IP addresses  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Control communication with persistent IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to implement persistent IP addresses on Google Kubernetes Engine (GKE) Pods. You can take control of your GKE Pod networking with custom persistent IP address mapping. To learn more about persistent IP addresses, their use cases, and benefits, see [About persistent IP addresses for GKE Pod](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods).

## Requirements

  * GKE version 1.31 or later.
  * Choose between reserving Google-provided IP addresses or bringing your own IP addresses (BYOIP).
  * Configure your application running within the Pods to recognize and use assigned persistent IP addresses.
  * Persistent IP addresses for GKE Pods require [ GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) and Gateway API enabled clusters.



## Limitations

  * You must configure your applications to use assigned persistent IP addresses. GKE doesn't automatically add the IP address configuration to the Pod's network interfaces.
  * You can associate each persistent IP address with a single Pod at a time. When you have multiple Pods available, GKE typically sends traffic to the newest matching Pod. However, GKE only does this if the newest Pod is healthy, meaning the Pod has the `Ready` condition status as `True` by default. You can configure this behavior and change it using the `reactionMode` setting on `GKEIPRoute`.
  * GKE only supports IPv4 addresses as persistent IP addresses.
  * GKE only supports [Layer 3 or Device type multi-networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#prepare-an-additional-vpc). 
    * High availability (HA) support using persistent IP addresses is not supported for non-DPDK use cases.
  * You can specify up to 16 IP addresses on a single `GKEIPRoute`. In order to configure more addresses, you can create multiple `GKEIPRoute` objects.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Read about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).

  * Review the requirements and limitations.




## Implement persistent IP addresses for GKE Pods

Persistent IP addresses in GKE offer a way to give your Pods a stable network identity, even if the Pods themselves are updated or moved around.

This section summarizes the workflow to implement persistent IP addresses for GKE Pods:

  1. **Create a cluster** : Create a cluster that has Gateway API, GKE Dataplane V2.
  2. **Reserve an IP address** : Decide whether you need an external (publicly accessible) or internal (Google Cloud only) IP address and reserve it. Choose the same region as your GKE cluster.
  3. **Create a Gateway** : Configure the Kubernetes Gateway object that holds your reserved persistent IP addresses and lets you create rules (`GKEIPRoutes`) about which Pods in your cluster can use those persistent IP addresses.
  4. **Create or identify workloads for persistent IP addresses** : If you use persistent IP addresses on an additional network, prepare Pods to use persistent IP addresses by enabling multiple network interfaces and defining the network where the persistent IP addresses reside.
  5. **Create the`GKEIPRoute` object for selected workloads**: Configure `GKEIPRoute` to assign the persistent IP address to a specific Pod. You can use labels to target the right Pod(s) and can optionally configure how the routing reacts to Pod changes.
  6. **Configure your application awareness** : Configure your application within the Pod to actively use the persistent IP address.
  7. **Monitoring** : Keep track of the status of your Gateway and `GKEIPRoute` objects to ensure everything is working as expected.



To implement persistent IP address for GKE Pods, perform the following steps:

## Step 1: Create a Gateway API and GKE Dataplane V2 enabled GKE cluster

To enable the advanced network routing and IP address management capabilities necessary for implementing persistent IP addresses on GKE Pods, you must [create](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-a-gke-cluster) a GKE Dataplane V2 cluster as follows:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --cluster-version=CLUSTER_VERSION \
        --enable-dataplane-v2 \
        --enable-ip-alias \
        --gateway-api=standard
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CLUSTER_VERSION`: the version of the cluster.

**Note:** If required, you can enable multi-networking.

## Step 2: Set up persistent IP addresses

To establish reliable network identities for your Pods and set up persistent IP addresses, you must first acquire persistent IP addresses. You can choose between reserving Google-provided IP addresses or using your own (BYOIP).

### Step 2a: Reserve Google-provided IP addresses

To reserve external IP addresses, run the following command:
    
    
    gcloud compute addresses create ADDRESS_NAME \
       --region=REGION
    

Replace the following:

  * `ADDRESS_NAME`: the name that you want to associate with this address.
  * `REGION`: the region where you want to reserve this address. This region should be the same region as the Pod that you want to attach the IP address to.

**Note** : You must specify a region when reserving an IP address because forwarding rules, which handle traffic routing for persistent IP addresses, are regional. Your IP address and GKE cluster must be in the same region for routing to work correctly.




To reserve internal IP addresses, run the following command:
    
    
    gcloud compute addresses create ADDRESS_NAME \
        --region REGION
        --subnet SUBNETWORK \
        --addresses IP_ADDRESS
    

Replace the following:

  * `ADDRESS_NAME`: the names of one or more addresses that you want to reserve. In case of multiple addresses, specify all the addresses as a list, separated by spaces. For example, example-address-1 example-address-2 example-address-3
  * `REGION`: the region for this request.
  * `SUBNETWORK`: the subnet for this internal IPv4 address.



To ensure traffic is routed correctly within your private network, internal IP addresses must belong to the cluster's default subnet or additional network subnet.

For more information on external and internal IP addresses or to see how to reserve addresses using the console, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) and [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

### Step 2b: Bring your own IP addresses (BYOIP)

You can bring your own IP addresses (BYOIP), instead of relying on Google-provided IP addresses. BYOIP is helpful if you need specific IP addresses for your applications or are moving existing systems into Google Cloud. To use BYOIP, Google validates that you own the IP address range, and after the IP addresses are imported to Google Cloud, you can assign them as the persistent IP addresses for GKE Pods. For more information, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Step 3: Create Gateway objects

Gateway objects hold the IP addresses and define which Pods are eligible to use them. To control how persistent IP addresses are assigned to your GKE Pods, you'll use Gateway objects.

  1. Create a Kubernetes Gateway object of the appropriate class: 
     * `gke-persistent-regional-external-managed` for external (public) IP addresses.
     * `gke-persistent-regional-internal-managed` for internal ( Google Cloud-only) IP addresses.
     * `gke-persistent-fast-regional-external-managed` for external IP addresses with fast failover.
     * `gke-persistent-fast-regional-internal-managed` for internal (Google Cloud-only) IP addresses with fast failover.
  2. Within the Gateway's addresses section, list the persistent IP addresses (Google-provided or BYOIP) that this Gateway manages.
  3. Use the `Listeners` section to determine which Pods (and their associated `GKEIPRoute` objects) can potentially use the Gateway's IP addresses. `Listeners` act as a filter based on the `GKEIPRoute`'s namespace where a `GKEIPRoute` object exists.

You can choose from the following Kubernetes namespace selection options:

     * **All Namespaces** : Any `GKEIPRoute` in the cluster.
     * **Selector** : `GKEIPRoute` in `GKEIPRoute`'s namespaces matching a specific label.
     * **Same Namespace** : Only `GKEIPRoutes` within the same `GKEIPRoute`'s namespace as the Gateway.



The following example provides cluster-wide access to external persistent IP addresses, allowing any Pod to potentially use them.

Save the following sample manifest as `allowed-pod-ips.yaml`:
    
    
    kind: Gateway
    apiVersion: gateway.networking.k8s.io/v1
    metadata:
      namespace: default
      name: allowed-pod-ips
    spec:
      gatewayClassName: gke-persistent-regional-external-managed
    
      listeners:
        - name: default
          port: 443
          protocol: none
          allowedRoutes:
            namespaces:
              from: All
    
      addresses:
        - value: "34.123.10.1/32"
          type: "gke.networking.io/cidr"
        - value: "34.123.10.2/32"
          type: "gke.networking.io/cidr"
    

where:

  * **addresses** : lists all the IP addresses whose permissions are managed by the specific Gateway.
  * **listeners** : used to identify the namespaces from which `GKEIPRoute` objects can reference this Gateway.

**Note:** A persistent IP address doesn't use the "port" and "protocol" fields in the listener configuration. This is because the forwarding rule associated with a persistent IP addresses uses L3_DEFAULT setting, which allows traffic on all TCP/UDP ports. For more details on forwarding rule protocols, see [Forwarding rule protocols](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule-protocols).

Apply the manifest to the cluster:
    
    
    kubectl apply -f allowed-pod-ips.yaml
    

**Note:** Changing the gateway class associated with a `GKEIPRoute` is not supported. You can't point a `GKEIPRoute` to a new gateway with a different class, or change the class on the current gateway.

## Step 4: (Optional) Create or identify workloads with additional networks for persistent IP addresses

If you plan to use your persistent IP addresses with Pods that require connectivity to multiple networks, you can [Set up multi-network Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods) and [create network objects](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods#create-pod-network) denoting the networks that the persistent IP address belongs to.

## Step 5: Create the `GKEIPRoute` object for selected workloads

To assign a persistent IP address to a selected Pod, create a `GKEIPRoute` object.

Save the following sample manifest as `my-ip-route.yaml`:
    
    
    kind: GKEIPRoute
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: default
      name: my-ip-route
    spec:
      parentRefs:
      - name: allowed-pod-ips
        namespace: default
      addresses:
      - value: "34.123.10.1/32"
        type: "gke.networking.io/cidr"
      network: default
      reactionMode: ReadyCondition
      podSelector:
        matchLabels:
          component: proxy
      nodeSelector: # Can only be specified when using fast failover Gateway Classes.
        matchLabels:
          component: proxy
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      namespace: default
      name: proxy-deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          component: proxy
      template:
        metadata:
          # annotations:  <- Include these lines if the pods are multi-nic pods
          #   networking.gke.io/default-interface: 'eth0'
          #   networking.gke.io/interfaces: '[{"interfaceName":"eth0","network":"default"}, {"interfaceName":"eth1","network":"blue-network"}]'
          labels:
            component: proxy
        spec:
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

where:

  * **parentRefs** : points to the Gateway from which persistent IP addresses are used. This field is immutable.
  * **addresses** : lists all the persistent IP addresses that are routed to the Pod identified with `podSelector`. This field is mutable. For IPv4, only /32 addresses are supported.
  * **podSelector** : specifies labels that identify the Pod where the persistent IP addresses are routed to. This field is mutable and applies to the same namespace in which `GKEIPRoute` is placed. If you select multiple Pods, two additional factors are taken under consideration: the Pod creation time (GKE picks the newest) and setting of `reactionMode` field.
  * **reactionMode** : specifies how this feature behaves when a specific Pod (selected by the `podSelector`) gets created or deleted. This field is optional and defaults to `ReadyCondition`. The `ReadyCondition` field is immutable. You can set the `reactionMode` to control how the feature acts when Pods are created, deleted, or updated.
  * **network** : points to the network interface on a Pod to which persistent IP addresses are routed. This field is optional and defaults to `default`. Note that if you use the default network, `network` must be set to `default`. If you use additional networks, set network to the name of the network object that you created previously. This field is immutable.
  * **nodeSelector** : specifies the labels of the nodes to preconfigure for fast failover. This field must be set when using fast failover Gateway Classes, and you can select a maximum of 64 nodes. You must ensure that Pods with persistent IP addresses are scheduled on these nodes, typically by using the Pod's `nodeSelector`.



Apply the manifest to the cluster:
    
    
    kubectl apply -f my-ip-route.yaml
    

### Assign persistent IP addresses to StatefulSet Pods

To assign a persistent IP address to a specific multinetwork Pod within a StatefulSet, use the Pod's predictable hostname and Kubernetes' automatic labeling, as shown in the following example:

Save the following sample manifest as `my-pod-ips.yaml`:
    
    
    kind: GKEIPRoute
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: proxy-ss-ns
      name: my-pod-ips
    spec:
      parentRefs:
      - name: allowed-pod-ips
        namespace: default
      addresses:
      - value: "34.123.10.1/32"
        type: "gke.networking.io/cidr"
      - value: "34.123.10.2/32"
        type: "gke.networking.io/cidr"
      network: blue-network
      reactionMode: ReadyCondition
      podSelector:
        matchLabels:
          statefulset.kubernetes.io/pod-name: proxy-ss-1
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      namespace: proxy-ss-ns
      name: proxy-ss
    spec:
      selector:
        matchLabels:
          component: proxy
      serviceName: "proxy"
      replicas: 3
      template:
        metadata:
          # annotations:  <- Include these lines if the pods are multi-nic pods
          #   networking.gke.io/default-interface: 'eth0'
          #   networking.gke.io/interfaces: '[{"interfaceName":"eth0","network":"default"}, {"interfaceName":"eth1","network":"blue-network"}]'
          labels:
            component: proxy
        spec:
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

Apply the manifest to the cluster (ensure you have a Network named "blue-network"):
    
    
    kubectl apply -f my-pod-ips.yaml
    

### Assign persistent IP addresses to Deployment Pods

To assign a persistent IP address to the newest Pod in a Deployment, apply a `GKEIPRoute` with the following configuration:

Save the following sample manifest as `my-pod-ips.yaml`:
    
    
    kind: GKEIPRoute
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: proxy-deploy-ns
      name: my-pod-ips
    spec:
      parentRefs:
      - name: allowed-pod-ips
        namespace: default
      addresses:
      - value: "34.123.10.1/32"
        type: "gke.networking.io/cidr"
      - value: "34.123.10.2/32"
        type: "gke.networking.io/cidr"
      network: blue-network # point to the right network if you intend to use persistent-ip on additional networks
      reactionMode: ReadyCondition
      podSelector:
        matchLabels:
          component: proxy
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      namespace: proxy-deploy-ns
      name: proxy-deploy
    spec:
      selector:
        matchLabels:
          component: proxy
      replicas: 4 # Latest Pod is used
      template:
        metadata:
          # annotations:  <- Include these lines if the pods are multi-nic pods
          #   networking.gke.io/default-interface: 'eth0'
          #   networking.gke.io/interfaces: '[{"interfaceName":"eth0","network":"default"}, {"interfaceName":"eth1","network":"blue-network"}]'
          labels:
            component: proxy
        spec:
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
    

Apply the manifest to the cluster:
    
    
    kubectl apply -f my-ip-route.yaml
    

Ensure you have a Network named "blue-network", if you are using additional networks.

## Step 6: Use the assigned IP addresses inside the Pod

Assigning an IP address to a GKE Pod by using a GKEIPRoute object doesn't automatically make the IP addresses usable by your application. The IP addresses are handled at a network routing level, but your Pod's default configuration won't be aware of them. You must configure your Pod specification to recognize and use the address within the Pod. To achieve this, your Pod requires privilege permissions.

You can configure your Pod specification by using one of the following options:

  * **Modify`net.ipv4.ip_nonlocal_bind` sysctl**

You can modify system settings to allow your application to use IP addresses not directly assigned to its interface by setting `net.ipv4.ip_nonlocal_bind` sysctl in your Pod `securityContext`. This option is useful if your application can bind to an IP address that is not on an interface.

Add the following to your Deployment or StatefulSet YAML specification under `spec.template.spec`:
        
        securityContext:
          sysctls:
          - name: net.ipv4.ip_nonlocal_bind
            value: "1"
        

  * **Add the assigned IP address to the Pod interface**

You can manually add the IP address that is claimed by the GKEIPRoute object to one of the Pod's interfaces using an init container. This makes the IP address visible to the Pod as if it were directly assigned. This requires the `NET_ADMIN` capability.

Add the following to your Deployment or StatefulSet YAML specification under `spec.template.spec`:
        
        initContainers:
        - name: configure-ips
          image: gcr.io/google.com/cloudsdktool/cloud-sdk:slim
          command: ['sh', '-c', 'ip address add ASSIGNED_IP/32 dev eth0']
          securityContext:
            capabilities:
              add:
              - NET_ADMIN
        

Replace `ASSIGNED_IP` with one of the IP addresses assigned to the GKEIPRoute object.

  * **Raw sockets:** for even more control, your application could directly interact with the network stack (advanced).

  * **Userspace IP address stack:** in specialized cases, a separate application might run within the Pod to manage the IP address (very advanced).




## Step 7: Enable ARP for the assigned IP addresses (default network only)

To generate valid Address Resolution Protocol (ARP) requests and responses, and to establish a new connection to a Pod by using the IP address assigned by the GKEIPRoute object on the default network, you must configure the `arp_announce` variable.

To set the `arp_announce` variable, run the following command on your Pod:
    
    
    echo "2" > /proc/sys/net/ipv4/conf/eth0/arp_announce
    

where `arp_announce` variable controls how ARP announcements are handled. Setting it to '2' helps ensure that ARP announcements are made for the persistent IP address, allowing other devices on the network to learn about the new association.

## Step 8: Use fast failover

If you use persistent IP addresses with fast failover, you can temporarily direct traffic to a Pod by issuing a Gratuitous ARP (GARP) from that Pod. Google Cloud respects that GARP for approximately 20 minutes. During this period, you must update the cluster configuration. To do this, in the `GKEIPRoute`'s `spec.podSelector` field, replace the old Pod's labels with the labels from the new Pod.

## Customize persistent IP address behavior during Pod changes

This section describes how the persistent IP address for GKE Pod behaves when the targeted Pod is created or deleted. The GKE controller monitors your Pods and the `GKEIPRoute` configuration. When it detects an update is happening, it automatically reassigns the persistent IP address to a suitable Pod according to your chosen `reactionMode`.

Understand how the persistent IP address feature automatically handles Pod changes and the configuration options available to you:

  * Decide between [ReadyCondition](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods#ready-condition) or [Exists](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods#exists) within the [reactionMode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods#reaction-mode) field of your `GKEIPRoute` configuration. Consider your application's needs regarding how quickly the IP address is assigned versus strict readiness requirements.
  * If you are using `ReadyCondition` to ensure readiness, make sure that your Pods have correctly implemented [Kubernetes readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes). Otherwise, the persistent IP address might not function as intended.
  * We recommend that you monitor the status of your Pods and the `Conditions` field of the `GKEIPRoute` object to ensure the system is working correctly. The `true` status of the `Ready` condition indicates that the system is working correctly.



## Troubleshoot communication with persistent IP addresses for Pods

This section shows you how to resolve issues related to persistent IP addresses for Pods.

### `NoPodsFound` when there are no matching Pods found

**Symptom**

The `GKEIPRoute` object specifies a `podSelector` (a set of labels) to identify which Pods are associated with the persistent IP address. The `NoPodsFound` status indicates that there are no Pods within the targeted `GKEIPRoute's` namespaces that have the matching labels.

**Potential causes**

  * **Incorrect labels:** The Pod you intend to use the persistent IP address with might have the wrong labels, or no labels at all.
  * **No Pods exist:** If the `reactionMode == Exists`, check if the Pod is assigned to a node by checking the `pod.Spec.nodeName` field. There might not be any Pods running in the `GKEIPRoute's` namespace that match the selector.
  * **Pod not Ready:** If `reactionMode == ReadyCondition`, check if the Pod status is `READY`. Even if a matching Pod exists, if it's not in a `Ready` state, it can't serve traffic and so it isn't selected.



**Resolution**

  1. **Check Your Labels** : double-check that the labels in your `GKEIPRoute`'s `podSelector` match the labels you've applied to the intended Pod.
  2. **Verify Pod Existence** : make sure a Pod with the correct labels actually exists in the `GKEIPRoute`'s namespaces specified by your Gateway's `Listeners`. If the `reactionMode == Exists`, check if the Pod is assigned to a node by checking the `pod.Spec.nodeName` field
  3. **Confirm Pod Readiness** : if `reactionMode == ReadyCondition`, check if the Pod status is `READY`. Ensure the Pod is in the `Ready` state using the following command:
         
         kubectl get pods -n <namespace>
         

Pods in other states (for example, "Pending", "Error") aren't selected.

  4. [Configure your Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods#user-persistent-ip) to respond on the assigned persistent IP address.




### `Mutated` when a matching Pod was found and persistent IP address programming is in progress

**Symptom**

The `GKEIPRoute` status shows "Mutated", indicating that the persistent IP address configuration for a matching Pod is in progress.

**Potential Cause:**

You can expect the "Mutated" status during configuration as the system is setting up the GKE datapath and Google Cloud resources for the persistent IP address.

**Resolution:**

  1. **Wait and retry:** in most cases, the configuration process completes automatically within a short time. Check the status after waiting. It will change to `Ready` when successful.
  2. **Investigate further (if necessary):** if the "Mutated" status persists for an extended period, this might indicate a configuration error. Examine the other status conditions on your `GKEIPRoute`: 
     * **Accepted** : indicates if your `GKEIPRoute` setup is valid.
     * **DPV2Ready** : indicates if the datapath on the node is programmed correctly.
     * **GCPReady** : indicates if the Google Cloud resources are set up as expected.



Look for error messages within these conditions to help troubleshoot the issue.

### GARP sent but the Pod is not receiving traffic

**Symptom**

You've sent a GARP from a new Pod, but the traffic flow remains unchanged. The `GKEIPRoute` status remains Ready and doesn't indicate an error.

**Potential causes**

The Pod isn't on a node that matches the `nodeSelector` in the `GKEIPRoute`. The GARP uses an IP address that isn't associated with the `GKEIPRoute`.

**Resolution**

  * **Verify the Pod's node** : ensure that the Pod runs on a node that matches the `nodeSelector` in your `GKEIPRoute` configuration. If the Pod isn't on a matching node, the node might not be programmed for the `GKEIPRoute`.
  * **Verify the GARP's IP address** : make sure that the IP address in the GARP is one of the IP addresses specified in the `GKEIPRoute`'s address field. If the IP address isn't associated with the `GKEIPRoute`, the fast failover mechanism doesn't trigger.



## What's next

  * Read [About persistent IP addresses for GKE Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods)
  * Read [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
