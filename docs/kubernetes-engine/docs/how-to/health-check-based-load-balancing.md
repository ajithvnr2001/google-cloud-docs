---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/health-check-based-load-balancing/
title: Configure health-check-based load balancing \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:38.079934+00:00
---

# Configure health-check-based load balancing  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/health-check-based-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure health-check-based load balancing Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to implement high availability for persistent IP addresses on Google Kubernetes Engine (GKE) by using health-check-based load balancing. Although standard persistent IP configurations map a single persistent IP address to a single Pod, health-check-based load balancing lets you distribute traffic from one or more persistent IP addresses across a pool of healthy Pods.

To claim specific persistent IP addresses and identify which Pods receive traffic, you create a GKEIPRoute custom resource. By integrating the GKEIPRoute resource with regional health checks, GKE monitors your workloads at the networking layer and routes traffic only to Pods that are ready to receive it. You can also designate optional backup Pods by using the GKEIPRoute object. GKE routes traffic only to these standby Pods if every primary active Pod fails its health check.

## Requirements and limitations

  * To use health-check-based load balancing, your cluster must be on GKE version 1.32.3-gke.1440000 or later. GKE supports selecting backup Pods only on version 1.35.0-gke.1403000 or later.
  * Your cluster must have GKE Dataplane V2 and Gateway API enabled.
  * A single GKEIPRoute object supports only one matching Pod per node. If multiple Pods on a node match the GKEIPRoute's Pod selector, GKE chooses the most recently created Pod on that node. field to ensure proper distribution of Pods.
  * You can't modify a Gateway class after you create the GKEIPRoute object.
  * Health-check-based load balancing supports only traffic that is initiated from outside the workload. Traffic initiated from within the workload to the persistent IP address is not supported.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Read about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).



## Implement health-check-based load balancing

This section summarizes the workflow to implement health-check-based load balancing:

  1. **Create a regional health check** : define the parameters that GKE uses to monitor the status of your Pods. This object tells the networking layer which endpoints are healthy and eligible to receive traffic from the persistent IP address.
  2. **Create a cluster** : set up a GKE cluster with GKE Dataplane V2 and Gateway API enabled. These components provide the underlying infrastructure required to manage persistent IP routing and health-check-based load balancing.
  3. **Reserve an IP address** : select and reserve a static internal or external IP address in the same region as your cluster. This address serves as the persistent entry point that GKE will distribute across your pool of active or backup Pods.
  4. **Create a Gateway** : configure a Gateway object to manage your reserved persistent IP addresses. The GKEIPRoute object claims and uses specific IP addresses from the Gateway for your workloads.
  5. **Create a GKEIPRoute object** : define the routing rules that map your persistent IP address to a group of Pods by using label selectors. Within this object, you reference your regional health check and optionally designate backup Pods for failover scenarios.
  6. **View matching endpoints** : verify that GKE has correctly identified your active and backup Pods by inspecting the automatically-generated EndpointSlices. This step confirms that your labels match the expected Pods and that the networking layer is ready to route traffic.



## Step 1: Create a regional health check and firewall rules

To create a regional health check, follow the steps in [Create health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#create-hc). The name that you provide here will be used in your GKEIPRoute configuration. For example:
    
    
    gcloud compute health-checks create http reg-lb-hc \
        --region=us-central1 \
        --check-interval=5s \
        --timeout=5s \
        --healthy-threshold=2 \
        --unhealthy-threshold=2
    

To let health check probes from Google Cloud reach your nodes, you must also [create firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

## Step 2: Create a GKE cluster

Create a cluster with Gateway API and GKE Dataplane V2 enabled. For example:
    
    
    gcloud container clusters create cluster-1 \
        --enable-dataplane-v2 \
        --gateway-api=standard \
        --region=us-central1
    

If you configure the GKEIPRoute object on a VPC network that is different from the default VPC network of the cluster, then you must create a GKE cluster with multi-network capabilities. For more information, see [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).

## Step 3: Reserve IP addresses

Reserve the IP addresses that you want to use for your workloads. You can choose between reserving Google-provided IP addresses or using your own (BYOIP).

### Step 3a: Reserve Google-provided IP addresses

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

  * `ADDRESS_NAME`: the names of one or more addresses that you want to reserve. In case of multiple addresses, specify all the addresses as a list, separated by spaces. For example, example-address-1 example-address-2 example-address-3.
  * `REGION`: the region for this request.
  * `SUBNETWORK`: the subnet for this internal IPv4 address.
  * `IP_ADDRESS`: an unused internal IP address from the selected subnet's primary IP address range.



To ensure traffic is routed correctly within your private network, internal IP addresses must belong to the cluster's default subnet or additional network subnet.

For more information about external and internal IP addresses or to see how to reserve addresses using the Google Cloud console, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) and [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

### Step 3b: Bring your own IP addresses (BYOIP)

You can bring your own IP addresses (BYOIP), instead of relying on Google-provided IP addresses. BYOIP is helpful if you need specific IP addresses for your applications or are moving existing systems into Google Cloud. To use BYOIP, Google validates that you own the IP address range, and after the IP addresses are imported to Google Cloud, you can assign them as the IP addresses for GKE Pods. For more information, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Step 4: Create Gateway objects

You create a Gateway by using one of the following Gateway classes which support only the L3 network type:

  * gke-passthrough-lb-external-managed or
  * gke-passthrough-lb-internal-managed.



The following example defines a Gateway that manages a pool of external IP addresses:
    
    
    kind: Gateway
    apiVersion: gateway.networking.k8s.io/v1beta1
    metadata:
      name: lb-gateway
    spec:
      gatewayClassName: gke-passthrough-lb-external-managed
    
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
    

In the preceding example, note the following fields:

  * **addresses** : lists all the IP address ranges for which the specific Gateway manages permissions.
  * **listeners** : identifies the namespaces from which GKEIPRoute objects can reference this Gateway.



For details about Listener usage, see [Create Gateway objects](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods#create-gateway-objects).

## Step 5: Create a GKEIPRoute object with load balancing and health check configuration

Create a GKEIPRoute object where you define your primary and backup Pod selectors, and associate the health check that you created in step 1.
    
    
    kind: GKEIPRoute
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: default
      name: my-ip-route
    spec:
      parentRefs:
      - name: lb-gateway
      addresses:
      - value: "34.123.10.1/32"
        type: "gke.networking.io/cidr"
      - value: "34.123.10.2/32"
        type: "gke.networking.io/cidr"
      network: default
      podSelector:
        matchLabels:
          component: activePodSelector
    
      loadBalancing:
        healthCheckName: "reg-lb-hc"
        backupPodSelector:
          namespaceSelector:
            matchLabels:
              environment: test
              dc: us-central
          podSelector:
            matchLabels:
              component: backupPodSelector
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
    

Note the following:

  * `podSelector`: identifies the primary active Pods that receive traffic from the defined persistent IP addresses. This field uses labels to match Pods within the same namespace as the GKEIPRoute resource. GKE distributes traffic across all healthy Pods that match this selector. If multiple matching Pods reside on the same node, GKE selects only the most recently created Pod to receive traffic. The labels defined here must not overlap with those in the `backupPodSelector` field. This field is mutable.
  * `backupPodSelector`: defines the standby Pods that receive traffic only if all primary Pods that match the podSelector object fail their health checks. This selector includes the following: 
    * `namespaceSelector`: determines which namespaces GKE searches to find these backup Pods. You can limit the search to specific namespaces by using label selectors. If this field is omitted or empty, GKE looks for backup Pods across all namespaces in the cluster.
    * `podSelector`: matches backup Pods based on their labels. These labels must be distinct from those used in the primary podSelector object.



For more details about the other fields in this manifest, see [Create the GKEIPRoute object](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-persistent-ip-addresses-on-gke-pods#create-gkeiproute).

**Important:** Backup Pods must reside on different nodes than the primary active Pods

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

## Step 8: View matching Endpoints

To manage traffic distribution, GKE creates EndpointSlices for each GKEIPRoute object. These slices act as a registry of all Pods designated as routing destinations for that specific route.

GKE generates separate EndpointSlices for active and backup endpoints. The system automatically scales the number of EndpointSlices based on your workload. Although a single `EndpointSlice` supports up to 1,000 endpoints, GKE creates additional slices if your matching Pod count exceeds this limit.

To view all EndpointSlices for a specific GKEIPRoute object, run the following command:
    
    
    kubectl get endpointslices --all-namespaces -l \
      networking.gke.io/gkeiproute-name=GKEIPROUTE_NAME,\
      networking.gke.io/gkeiproute-namespace=GKEIPROUTE_NAMESPACE
    

Replace the following:

  * `GKEIPROUTE_NAME`: the name of the GKEIPRoute manifest.
  * `GKEIPROUTE_NAMESPACE`: the namespace of the GKEIPRoute manifest.



The following output shows an example of an `EndpointSlice`:
    
    
    apiVersion: discovery.k8s.io/v1
    kind: EndpointSlice
    metadata:
     name: {gkeiproute_name-truncated}-{gkeiproute_namespace-truncated}-backup-{unique_hash}
     namespace: {gkeiproute_namespace}
     labels:
      endpointslice.kubernetes.io/managed-by: gkeiproute-controller
      networking.gke.io/gkeiproute-name: {gkeiproute_name}
      networking.gke.io/gkeiproute-namespace: {gkeiproute_namespace}
      networking.gke.io/pip-es-role: backup
     ownerReferences:
      - kind: GKEIPRoute
        name: {gkeiproute_name}
        apiVersion: networking.gke.io/v1
        uid: {uid}
        controller: true
    addressType: IPv4
    endpoints:
     - addresses:
         - "{pod_ip_address}"
       targetRef:
         Name: {pod_name}
       nodeName: {node_name}
    

To view EndpointSlices specifically for either active or backup endpoints, filter the results by using the `pip-eps-role` label. For example:
    
    
    kubectl get endpointslices --all-namespaces -l \
       networking.gke.io/pip-eps-role=ROLE \
      networking.gke.io/gkeiproute-name=GKEIPROUTE_NAME,
    

Replace the following:

  * `ROLE`: the type of endpoint you want to view, either `active` or `backup`.
  * `GKEIPROUTE_NAME`: the name of your specific GKEIPRoute object.



## Troubleshoot health-check-based load balancing

This section shows you how to resolve issues related to health-check-based load balancing.

### Some active Pods are unhealthy but backup Pods don't receive traffic

**Symptom**

The GKEIPRoute status shows `Ready`, which indicates that the IP address configuration for matching Pods is complete. Health checks or other diagnostics show that some active Pods are unhealthy. However, backup pods don't receive traffic.

**Cause**

Backup Pods don't receive traffic until _all_ active Pods are unhealthy. Until then, all traffic is distributed across the remaining healthy, active Pods.

**Resolution**

If necessary, update the `podSelector` field labels so that they no longer match any active Pods. GKE automatically routes traffic to the backend group.

### GKEIPRoute is configured but not all Pods receive traffic

**Symptom**

The GKEIPRoute status shows `Ready`, which indicates that the IP address configuration for matching Pods is complete, but some of the matching Pods don't receive traffic.

**Cause**

The Pods that don't receive traffic might not be healthy, or might not be responding to health checks correctly. Note that if all matching Pods are not healthy, GKE distributes traffic across all Pods, regardless of their health status.

**Resolution**

  * **Verify that the Pod is healthy** : use the Google Cloud CLI or the Google Cloud console to verify that the Pod responds correctly to health checks.
  * **Investigate further if necessary** : if the Pod is unhealthy, verify that you have correctly set up [firewalls for the health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule), and that your Pod is responding.



### Invalid load balancer configuration Errors

This section helps you troubleshoot GKEIPRoute status errors.

#### `Backup pod and active pod are on the same node`

**Symptom**

The GKEIPRoute status reports the following error:
    
    
    invalid LB configuration: Backup pod %s and active pod %s are on the same node %s. Active and backup pods must reside on different nodes.
    

**Cause**

An active Pod and a backup Pod matching the same GKEIPRoute object are scheduled onto the same node. In other words, there are Pods that match both the active and backup podSelector objects on the same node.

**Resolution**

Ensure that the active and backup Pods are on different nodes. Update your GKEIPRoute configuration and adjust your `podSelector` or `backupPodSelector` labels so that no two Pods on the same node match the same GKEIPRoute object.

#### `Pod cannot be selected as both an active and a backup pod`

**Symptom**

The GKEIPRoute status reports the following error:
    
    
    invalid LB configuration: pod %s cannot be selected as both an active and a backup pod. Active and backup pod sets must be mutually exclusive
    

**Cause**

One or more Pods match the label selectors for both the `podSelector` (active) field and the `backupPodSelector` (standby) field. GKE requires that these two groups are mutually exclusive. A single Pod can't serve as its own backup.

**Resolution**

Ensure that your active and backup Pods are unique. Modify the `podSelector` field or the `backupPodSelector` field in your GKEIPRoute manifest to use more specific or distinct label keys and values.

#### `NoPodsFound` status

**Symptom**

The GKEIPRoute manifest shows a status of `NoPodsFound` which indicates that there are no Pods within the namespaces that have matching labels.

**Potential causes**

  * **Incorrect labels** : the Pod with which you intend to use the configured IP address might have the wrong labels, or no labels at all.
  * **No Pods exist** : if the `reactionMode == Exists`, check if the Pod is assigned to a node by checking the `pod.Spec.nodeName` field. There might not be any Pods running in the GKEIPRoute's namespace that match the selector.
  * **Pods not Ready** : if `reactionMode == ReadyCondition`, check if the Pod status is `READY`. If a matching Pod exists but it isn't in a `READY` state, the Pod can't serve traffic and isn't selected.



**Resolution**

  * **Check the labels** : confirm that the labels in your GKEIPRoute object's `podSelector` field match the labels that you've applied to the intended Pod.
  * **Verify Pod existence** : make sure a Pod with the correct labels actually exists in the GKEIPRoute object's namespaces specified by your Gateway's Listeners. If the `reactionMode == Exists`, check if the Pod is assigned to a node by checking the `pod.Spec.nodeName` field.
  * **Confirm Pod readiness** : if `reactionMode == ReadyCondition`, check if the Pod status is `READY`. Ensure that the Pod is in the `Ready` state by using the following command:
        
        kubectl get pods -n NAMESPACE
        

Pods in other states (for example, `Pending`, `Error`) aren't selected.




#### `Mutated` status when a matching Pod was found and GKEIPRoute IP address programming is in progress

**Symptom**

The GKEIPRoute status shows `Mutated`, which indicates that the IP address configuration for a matching Pod is in progress.

**Potential cause**

You can expect the `Mutated` status during configuration while the system is setting up the GKE datapath and Google Cloud resources for the configured IP address.

**Resolution**

  1. **Wait and retry** : in most cases, the configuration process completes automatically within a short time. Check the status after waiting. It will change to `Ready` when successful.
  2. **Investigate further (if necessary)** : if the `Mutated` status persists for an extended period, this might indicate a configuration error. Examine the other status conditions on your GKEIPRoute object:

     * **Accepted** : indicates if your GKEIPRoute setup is valid.
     * **GCPReady** : indicates if the Google Cloud resources are set up as expected.



Look for error messages within these conditions to help troubleshoot the issue.

## What's next

  * Learn more about [Persistent IP addresses for GKE Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-persistent-ip-addresses-for-gke-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
