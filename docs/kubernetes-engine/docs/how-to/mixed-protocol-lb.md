---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/mixed-protocol-lb/
title: Create a mixed-protocol load balancer \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:09.703393+00:00
---

# Create a mixed-protocol load balancer  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/mixed-protocol-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Create a mixed-protocol load balancer Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to expose an application running in a Google Kubernetes Engine (GKE) cluster by using a mixed-protocol external or internal LoadBalancer Service for both TCP and UDP traffic.

To learn more about L4 load balancers, see [About LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).

## Overview

You can expose applications that use both TCP and UDP protocols by using two separate GKE LoadBalancer Services with a manually coordinated, shared IP address. However, this approach is inefficient because it requires managing multiple Services for a single application and might lead to issues such as configuration errors or exhausted IP address quotas.

Mixed-protocol LoadBalancer Services let you use a single Service to manage traffic for both TCP and UDP. Using a single Service simplifies your configuration by letting you use a single IP address and a consolidated set of forwarding rules for both protocols. This feature is supported for both regional external passthrough Network Load Balancers and internal passthrough Network Load Balancers.

GKE supports mixed-protocol Services with IPv4, IPv6, and dual-stack configurations. Mixed-protocol Services use Layer 3 (L3) forwarding rules. By design, these rules forward all traffic that arrive on the load balancer's virtual IP (VIP) address directly to the cluster nodes.

To maintain security, GKE automatically creates and manages firewall rules on priority 999 that allow only the specific TCP and UDP traffic defined in your Service manifest. All other unauthorized traffic directed to the load balancer's VIP address is blocked by GKE managed firewall rules by using priority 1000\. If you create higher-priority firewall rules, ensure that the rules don't accidentally allow unauthorized traffic to reach your nodes. For more information, see [GKE Service firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Requirements

To create a LoadBalancer Service that uses mixed protocols, your cluster must meet the following requirements:

  * Mixed-protocol load balancing is generally available from GKE version 1.36.2-gke.1498000 and later. The generally available version supports both external and internal load balancers with IPv4, IPv6, and dual-stack configurations.
  * For versions 1.34.1-gke.2190000 through to 1.36.2-gke.1498000, mixed-protocol load balancing is supported only for external load balancers that use IPv4 addresses.
  * You must have the `HttpLoadBalancing` addon enabled on your cluster.
  * For internal load balancers, the cluster must have [GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable_ilb_subsetting_existing_cluster) enabled.
  * For new internal LoadBalancer Services, in the Service manifest, set the value of the `spec.loadBalancerClass` field to `networking.gke.io/l4-regional-internal`. For existing internal Services, your manifest already has the `networking.gke.io/load-balancer-type: "Internal"` annotation, and you can leave the annotation as is.
  * For new external LoadBalancer Services, ensure the load balancer is a backend service-based regional external passthrough Network Load Balancer. In GKE 1.37 and later, this configuration is the default. In earlier versions, set the `spec.loadBalancerClass` field to `networking.gke.io/l4-regional-external` in the Service manifest. For existing external Services, your manifest already has the `cloud.google.com/l4-rbs: "enabled"` annotation, and you can leave the annotation as is.



## Limitations

  * On versions 1.34.1-gke.2190000 through to 1.36.2-gke.1498000, mixed-protocol load balancers support only IPv4 addresses.
  * Existing Services that have the `gke.networking.io/l4-ilb-v1` or `gke.networking.io/l4-netlb-v1` finalizers cannot be used for mixed-protocol load balancing. If you want to use mixed protocols on these Services, you must delete and re-create the Service according to the preceding requirements.
  * Updating ports on the Service might cause a brief traffic disruption for all traffic routed through the load balancer.
  * You can't attach Private Service Connect to mixed-protocol Services.



## Pricing

Google Cloud bills you per forwarding rule, for any external IP addresses, and for data sent. The following table describes the number of forwarding rules and external IP addresses used for specified configurations. For more information, see [VPC network pricing](https://docs.cloud.google.com/vpc/network-pricing).

Type | Transport Layer | Internet Layer | Number of Forwarding Rules | Number of External IP Addresses  
---|---|---|---|---  
Internal | Single or mixed (TCP, UDP, or both) | IPv4 | 1 | 0  
IPv6 | 1 | 0  
IPv4 and IPv6 (DualStack) | 2 | 0  
External | Single or mixed (TCP, UDP, or both) | IPv4 | 1 | 1  
IPv6 | 1 | 1  
IPv4 and IPv6 (DualStack) | 2 | 2  
**Note:** In GKE versions earlier than 1.36.2-gke.1498000, mixed-protocol external load balancers use two forwarding rules (one for TCP and one for UDP) instead of a single L3 forwarding rule.

## Deploy a workload

This section shows how to deploy a sample workload that listens on both TCP and UDP ports. Note that the Deployment configuration is the same whether you are using a mixed-protocol LoadBalancer Service or two separate single-protocol LoadBalancer Services.

  1. The following manifest is for a sample application that listens on port 8080 for both TCP and UDP traffic. Save the following manifest as `mixed-app-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: mixed-app-deployment
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: mixed-app
           template:
             metadata:
               labels:
                 app: mixed-app
             spec:
               containers:
               - image: gcr.io/kubernetes-e2e-test-images/agnhost:2.6
                 name: agnhost
                 args: ["serve-hostname", "--port=8080", "--tcp=true", "--udp=true", "--http=false"]
                 ports:
                   - name: tcp8080
                     protocol: TCP
                     containerPort: 8080
                   - name: udp8080
                     protocol: UDP
                     containerPort: 8080
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f mixed-app-deployment.yaml
         




## Create a mixed-protocol load balancer

Create a Service of type `LoadBalancer` that exposes the deployment to both TCP and UDP traffic. You can create either an external or an internal load balancer.

  1. To create an external load balancer, save the following manifest as `mixed-protocol-lb.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: mixed-protocol-external-lb
         spec:
           loadBalancerClass: "networking.gke.io/l4-regional-external"
           type: LoadBalancer
           selector:
             app: mixed-app
           ports:
           - name: tcp-port
             protocol: TCP
             port: 8080
           - name: udp-port
             protocol: UDP
             port: 8080
         

To create an internal load balancer, set the value of the `spec.loadBalancerClass` field to `networking.gke.io/l4-regional-internal`.

The preceding Service has two ports, one for TCP and one for UDP, both on port 8080.

  2. Apply the manifest to your cluster:
         
         kubectl apply --server-side -f mixed-protocol-lb.yaml
         


**Note:** If you created the Service with the `cloud.google.com/l4-rbs: "enabled"` annotation instead, you might see a warning event from the legacy service controller: `mixed-protocol is not supported for LoadBalancer`. You can safely ignore this message because the new controller, which supports mixed-protocols, correctly provisions the load balancer.

## Verify the mixed-protocol load balancer

After you create the Service, verify that GKE created the load balancer successfully.

  1. Inspect the Service:
         
         kubectl describe service SERVICE_NAME
         

Replace `SERVICE_NAME` with the name of your Service (for example, `mixed-protocol-lb`).

The output shows the IP address of the load balancer and the forwarding rules. Verify the following details in the output:

     * The `status.loadBalancer.ingress.ip` field is populated.
     * For clusters on versions 1.34.1-gke.2190000 through to 1.36.2-gke.1498000, verify that the following annotations for your external load balancer are present: 
       * `service.kubernetes.io/tcp-forwarding-rule`
       * `service.kubernetes.io/udp-forwarding-rule`
     * For clusters that are created on versions after 1.36.2-gke.1498000, verify that the following annotations for your load balancer are present, depending on your configuration: 
       * **For IPv4** : `service.kubernetes.io/l3-forwarding-rule`
       * **For IPv6** : `service.kubernetes.io/l3-forwarding-rule-ipv6`
       * **For dual-stack** : both annotations.
     * The `Events` section contains no error messages.



## Update the mixed-protocol load balancer

You can update the ports on a mixed-protocol load balancer by editing the Service manifest. To edit the Service, run the following command:
    
    
    kubectl edit service SERVICE_NAME
    

Replace `SERVICE_NAME` with the name of your Service.

### Update ports

To update the ports on a mixed-protocol load balancer, modify the `ports` section of the Service manifest. You can add, remove, or modify ports.

The following example adds a UDP port for streaming and a TCP port for game-server metadata:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: mixed-protocol-lb
    spec:
      loadBalancerClass: "networking.gke.io/l4-regional-external"  # for internal LB, use: "networking.gke.io/l4-regional-internal"
      type: LoadBalancer
      selector:
        app: mixed-app
      ports:
      - name: tcp-port
        protocol: TCP
        port: 8080
      **- name: streaming
        protocol: UDP
        port: 10100
      - name: gameserver-metadata
        protocol: TCP
        port: 10400
      - name: https
        protocol: TCP
        port: 443**
    

### Update a single-protocol load balancer to mixed-protocol

To change a single-protocol load balancer to a mixed-protocol load balancer, edit the Service to include ports for both the TCP and UDP protocols.

The following example adds a UDP port for DNS to an existing TCP-only load balancer:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: already-existing-single-protocol-lb
    spec:
      loadBalancerClass: "networking.gke.io/l4-regional-external" # for internal LB, use: "networking.gke.io/l4-regional-internal"
      type: LoadBalancer
      selector:
        app: mixed-app
      ports:
      - name: http
        protocol: TCP
        port: 80
      - name: https
        protocol: TCP
        port: 443
      **- name: dns
        protocol: UDP
        port: 53**
    

### Update a mixed-protocol load balancer to single-protocol

To change a mixed-protocol load balancer to a single-protocol load balancer, remove all ports for one of the protocols.

The following example removes the UDP port for DNS, which converts the load balancer to TCP-only:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: already-existing-mixed-protocol-lb
    spec:
      loadBalancerClass: "networking.gke.io/l4-regional-external" # for internal LB, use: "networking.gke.io/l4-regional-internal"
      type: LoadBalancer
      selector:
        app: mixed-app
      ports:
      - name: http
        protocol: TCP
        port: 80
      - name: https
        protocol: TCP
        port: 443
    

## Delete the mixed-protocol LoadBalancer

To delete the mixed-protocol LoadBalancer Service, run the following command:
    
    
    kubectl delete service SERVICE_NAME
    

Replace `SERVICE_NAME` with the name of your Service (for example, `mixed-protocol-external-lb`).

GKE automatically removes all load balancer resources created for the Service.

## Troubleshooting

This section describes how to resolve common issues with mixed-protocol LoadBalancer Services.

### Check for error events

The first step in troubleshooting is to check the events associated with your Service.

  1. Get the details of your Service:
         
         kubectl describe service SERVICE_NAME
         

Replace `SERVICE_NAME` with the name of your Service.

  2. Review the `Events` section at the end of the output for any error messages.




### Error: Mixed Protocol is not supported for LoadBalancer

If you created the Service with the `cloud.google.com/l4-rbs: "enabled"` annotation, you might see a warning event from the original service controller after you create the mixed-protocol load balancer: `mixed-protocol is not supported for LoadBalancer`.

You can safely ignore this message because the new controller, which supports mixed-protocols, correctly provisions the load balancer.

### Port definition is missing after an update

**Symptom:**

When you update a Service that uses the same port for both TCP and UDP (for example, port 8080), one of the port definitions is missing from the updated Service.

**Cause:**

This is a known issue in Kubernetes. When you update a Service with multiple protocols on the same port, the client-side patch calculation can incorrectly merge the port list, which causes one of the port definitions to be removed. This issue affects clients that use client-side patching, such as `kubectl apply` and the Go client with merge patches.

**Solution:**

The workaround for this issue depends on your client.

  * **For kubectl** : Use the `--server-side` flag with `kubectl apply`:
        
        kubectl apply --server-side -f YOUR_SERVICE_MANIFEST.yaml
        

Replace `YOUR_SERVICE_MANIFEST` with the name of your Service manifest.

  * **For go-client** : Don't use merge patches. Instead, use an update call to replace the Service. This requires an HTTP `PUT` request with the entire Service object specification.




## What's next

  * Learn more about [exposing applications using Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).
  * Read about [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
