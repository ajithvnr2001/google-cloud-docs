---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-egress-dscp-tagging/
title: Configure DSCP tags for egress traffic \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:37.818095+00:00
---

# Configure DSCP tags for egress traffic  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-egress-dscp-tagging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure DSCP tags for egress traffic Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to configure Differentiated Services Code Point (DSCP) tagging for egress traffic for Distributed Cloud software only for bare metal.

You can prioritize outbound network traffic from your clusters by marking your IP headers with a DSCP value. Your upstream physical network infrastructure uses the DSCP tags to apply Quality of Service (QoS) policies, such as priority queuing or bandwidth shaping.

## Before you begin

Before you configure egress DSCP tags, read the [DSCP tagging overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/egress-dscp-tagging) to learn how the system resolves conflicts. Ensure your environment meets the following requirements.

**Important:** Distributed Cloud software only for bare metal adds a tag to your outgoing IP packets. Distributed Cloud software only for bare metal does not shape or queue traffic. You must configure your upstream physical network infrastructure to read the DSCP tags and enforce QoS policies.

### Requirements

To use DSCP tagging, you must meet the following requirements:

  * You must use Distributed Cloud software only for bare metal version 1.35 or higher.
  * You can only tag outbound (north-south) traffic leaving the cluster. You cannot tag internal traffic between pods.
  * You can only tag IPv4 traffic.



## Enable the DSCP tagging feature

To use egress DSCP tagging, you must enable the feature on your cluster. To enable this feature, do the following:

  1. Open the cluster configuration file that you used to create the cluster (typically located at `bmctl-workspace/<var>CLUSTER_NAME</var>/<var>CLUSTER_NAME</var>.yaml`) in a text editor.
  2. Add the `preview.baremetal.cluster.gke.io/traffic-selector: "enable"` annotation to the `metadata` section. The following is an example of how your cluster configuration file looks when you turn on DSCP tagging:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: my-cluster
           namespace: cluster-my-cluster
           annotations:
             preview.baremetal.cluster.gke.io/traffic-selector: "enable"
         spec:
           # Remaining cluster specifications...
         

  3. Apply the configuration to your cluster using `bmctl`:
         
         bmctl update cluster -c <var>CLUSTER_NAME</var> --kubeconfig=<var>ADMIN_KUBECONFIG</var>

Replace the following:

     * CLUSTER_NAME: The name of your cluster.
     * ADMIN_KUBECONFIG: The path to your admin cluster kubeconfig file.



## Define global DSCP values

Create an `EgressDSCP` custom resource. To create this custom resource, do the following:

  1. Create an `EgressDSCP` custom resource and provide a numeric DSCP value between 0 and 63.

The following example shows an `EgressDSCP` custom resource named `dscp-high-priority` that applies a DSCP value of `40`:
         
         apiVersion: networking.gke.io/v1
         kind: EgressDSCP
         metadata:
           name: dscp-high-priority
         spec:
           dscp: 40
         

  2. Apply the resource to your cluster:
         
         kubectl apply -f my-egress-dscp.yaml

  3. Verify the resource is active and available across the cluster:
         
         kubectl get egressdscps




## Prioritize outbound traffic from workloads

Create a `TrafficSelector` custom resource to target specific pods and apply your DSCP tag to outgoing pod traffic.

  1. Create the custom resource. The following example displays an example of how to create a custom resource. This example matches outbound TCP traffic from pods labeled `app: critical-upload` to the IP address `8.8.8.8/32`. The rule references the `dscp-high-priority` custom resource to apply its DSCP value to all matching packets:
         
         apiVersion: networking.gke.io/v2
         kind: TrafficSelector
         metadata:
           name: ts-pod-upload
           namespace: default
         spec:
           priority: 10
           subject:
             pods:
               namespaceSelector:
                 matchLabels:
                   kubernetes.io/metadata.name: default
               podSelector:
                 matchLabels:
                   app: critical-upload
           egress:
             to:
               ipBlock:
                 cidrs:
                   - "8.8.8.8/32"
             ports:
               - allPorts:
                   protocol: TCP
           action:
             apiVersion: networking.gke.io/v1
             kind: EgressDSCP
             name: dscp-high-priority
         

  2. Apply the traffic selector:
         
         kubectl apply -f ts-pod-upload.yaml




**Important:** Because this feature is in preview, the `EgressDSCP` and `TrafficSelector` custom resource schemas might change in a future release.

## Prioritize return traffic from external services

Create a `TrafficSelector` custom resource to tag return traffic going back to external clients.

**Important:** You can only tag return traffic for `LoadBalancer` and `NodePort` services. You cannot tag return traffic for `ClusterIP` services.

  1. Create the custom resource. The following example matches TCP return traffic from any service backend labeled `app: video-stream`. The rule references the `dscp-high-priority` custom resource to apply its DSCP value to the response stream sent back to external clients. By omitting the `spec.egress.to` field, this selector applies the DSCP tag to return traffic going to any external client IP address:
         
         apiVersion: networking.gke.io/v2
         kind: TrafficSelector
         metadata:
           name: ts-service-video
           namespace: media
         spec:
           priority: 20
           subject:
             services:
               namespaceSelector:
                 matchLabels:
                   kubernetes.io/metadata.name: media
               serviceSelector:
                 matchLabels:
                   app: video-stream
           egress:
             ports:
               - allPorts:
                   protocol: TCP
           action:
             apiVersion: networking.gke.io/v1
             kind: EgressDSCP
             name: dscp-high-priority
         

  2. Apply the traffic selector:
         
         kubectl apply -f ts-service-video.yaml




## Additional configuration examples

You can design your `TrafficSelector` resources to apply DSCP tags at different levels of granularity depending on your network architecture:

  * Tag by specific Pod labels to mark outgoing traffic for specific application workloads within a namespace.
  * Tag by service to mark the response loop traffic returning to external clients.
  * Tag by destination port or IP address to prioritize specific communication paths or network control services.
  * Tag by namespace as a catch-all policy to apply a single priority tier to an entire application sandbox or business unit.



### Example: Tag traffic by destination port

In edge environments with limited WAN bandwidth, you must prioritize   
network control services (like NTP and DNS) to maintain cluster stability. Delayed or dropped traffic can cause clock drift, control plane breakdowns, and secure connection failures. Tagging by destination port ensures this traffic receives priority over standard bulk data transfers.

The following example tags outbound traffic sent to specific external ports, such as TCP port `443` (HTTPS) and UDP port `123` (NTP) to ensure this traffic receives priority over standard bulk data transfers:
    
    
    apiVersion: networking.gke.io/v2
    kind: TrafficSelector
    metadata:
      name: ts-ports
      namespace: default
    spec:
      priority: 30
      subject:
        pods:
          podSelector:
            matchLabels:
              app: critical-sync
      egress:
        to:
          ipBlock:
            cidrs:
              - "0.0.0.0/0"
        ports:
          - portNumber:
              protocol: TCP
              port: 443
          - portNumber:
              protocol: UDP
              port: 123
      action:
        apiVersion: networking.gke.io/v1
        kind: EgressDSCP
        name: dscp-high-priority
    

### Example: Tag all traffic from a namespace

In multi-tenant clusters, tagging an entire namespace helps you enforce Service Level Agreements (SLAs) and streamline network management. For example, you can do the following:

  * Apply the tag directly to the namespace as an automatic catch-all policy. Every workload in the space inherits the tag without individual developers needing to configure pod labels.
  * If WAN bandwidth becomes congested, you can assign a high priority tier (like Gold or Silver) to critical business unit namespaces so that the upstream network prioritizes their traffic first.



**Note:** Because any workload deployed in the namespace automatically inherits the tag, make sure to restrict deployment permissions to prevent non-critical workloads from overloading your priority queue.

The following example tags all outbound traffic from every workload in the `frontend-ns` namespace:
    
    
    apiVersion: networking.gke.io/v2
    kind: TrafficSelector
    metadata:
      name: ts-namespace-full
      namespace: frontend-ns
    spec:
      priority: 40
      subject:
        pods:
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: frontend-ns
      egress:
        to:
          ipBlock:
            cidrs:
              - "0.0.0.0/0"
        ports:
          - allPorts:
              protocol: TCP
          - allPorts:
              protocol: UDP
      action:
        apiVersion: networking.gke.io/v1
        kind: EgressDSCP
        name: dscp-high-priority
    

## Verify and troubleshoot

To confirm your DSCP tag configuration, perform the following checks:

  1. Verify the tags on the wire. Run `tcpdump` to check if your outgoing network packets carry the correct header value.
  2. Troubleshoot missing tags. If the tags are not present, check your resource status to verify if the control plane accepted the rule.



### Verify applied DSCP tags

Inspect the live network traffic to verify the output headers.

**Important:** You must have root SSH access to the cluster node that hosts your source workload to run `tcpdump`.

  1. Connect to the host node where your pod is running using SSH.
  2. Run `tcpdump` to capture outgoing packets from the pod's IP address:
         
         sudo tcpdump -v host POD_IP_ADDRESS

  3. Verify that the `tos` header field matches your configured DSCP hex value. You can calculate your expected hex value by multiplying your decimal DSCP value by `4` and converting the result to a hexadecimal number. For example, a DSCP value of `42` multiplied by `4` equals `168`, which is `0xa8` in hex.




### Troubleshoot missing tags

If `tcpdump` shows that your packets are not getting marked, do the following:

  1. Inspect your `TrafficSelector` custom resource to see if a rule with higher priority is overriding it:
         
         kubectl get trafficselector TRAFFIC_SELECTOR_NAME -o yaml

  2. Check the `status.conditions` section. If the `Programmed` condition is `False`, the rule contains invalid references or a dominant rule shadowed it.




## What's next

  * Learn more about [Egress DSCP tagging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/egress-dscp-tagging).
  * Consult your network team to verify your upstream router configurations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
