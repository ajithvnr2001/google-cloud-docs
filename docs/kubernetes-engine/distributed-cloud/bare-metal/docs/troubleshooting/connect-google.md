---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/connect-google/
title: Troubleshoot your connection to Google \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:54.218117+00:00
---

# Troubleshoot your connection to Google  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/connect-google/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot your connection to Google Stay organized with collections  Save and categorize content based on your preferences. 

This document gives troubleshooting guidance for issues related to your connection to Google.

## Network Connectivity Gateway

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section gives troubleshooting tips related to [Network Connectivity Gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/network-connectivity-gateway).

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



### Verify that the controller and gateway Pods are running

  * List the Network Connectivity Gateway Pods:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get pods \
            --namespace kube-system | grep ncg
        

Replace `CLUSTER_KUBECONFIG` with the path of your cluster kubeconfig file.

In the output, verify that you see a controller Pod and a gateway Pod. The name of the controller Pod begins with `ncg-controller`, and the name of the gateway Pod begins with `ncgd`. For example:
        
        ncg-controller-5f5d489b68-r87pp     1/1     Running
        ncgd-gvl76                          1/1     Running
        

Make a note of the name of the gateway Pod. You will need it for various troubleshooting commands.




### Check the gateway Pod logs

  * Check to see if there are any errors in the logs from the gateway Pod:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG logs GATEWAY_POD \
            --namespace kube-system
        

Replace `GATEWAY_POD` with the name of your gateway Pod.




### Running `ncgcli` inside the gateway Pod

The gateway Pod has a command-line tool named `ncgcli` that you can use to get information about the gateway and traffic in the tunnels.

  * Use the following command to run `ncgcli` inside the gateway Pod:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG exec -it GATEWAY_POD \
            --namespace kube-system -- ncgCLI_COMMAND
        

Replace `ncgCLI_COMMAND` with a `ncgcli` command.

For example:
        
        kubectl --kubeconfig my-kubeconfig exec ncgd-6hkk2 --namespace kube-system \
            -- ncgcli --help
        




The following sections give more examples of `ncgcli` commands.

### IPsec tunnel failed to come up

  * Check the status of the `NetworkConnectivityGateway` custom resource:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get NetworkConnectivityGateway \
            --namespace kube-system --output yaml
        

In the output, verify that you see `Status: Healthy`. For example:
        
        apiVersion: networking.gke.io/v1alpha1
        kind: NetworkConnectivityGateway
        metadata:
          namespace: kube-system
          name: default
        spec:
        status:
          CurrNode: worker1-node
          CreatedTime: 2021-09-07T03:18:15Z
          LastReportTime: 2021-09-21T23:57:54Z
          Status:  Healthy
        

  * Check the status of your `OverlayVPNTunnel` custom resources:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get OverlayVPNTunnel \
            --namespace kube-system --output yaml
        

  * Check the status of your tunnels from inside the gateway Pod:
        
        ncgcli overlay peers show
        




For more information, see [Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

### Failed to establish BGP session

Verify that you have used link-local IP addresses, such as `169.254.1.2` and `169.254.2.2`, for the BGP sessions between the Cloud Router and the gateway Pod in your cluster.

  * Check the status of your BGP sessions:
        
        kubectl --kubeconfig CLUSTER_KUBECONFIG get OverlayBGPPeer \
            --namespace kube-system --output yaml
        

  * Check the status of your BGP sessions from inside the gateway Pod:
        
        ncgcli overlay routes show
        




For more information about troubleshooting your BGP sessions, see the following:

  * [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states)
  * [Troubleshoot BGP peering](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering)
  * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)



### Traffic forwarding issues even if the tunnel is up

If the traffic forwarding fails, run `ncgcli` inside the gateway Pod to check the status of tunnels, routing, and data plane programming.

  * Ensure that IPsec tunnel to the peer is established:
        
        ncgcli overlay peers show
        

  * Confirm that the overlay routes have been exchanged over BGP and resolved to the appropriate IPsec tunnel:
        
        ncgcli overlay routes show
        

  * Display routes programmed in the data plane and the output should include overlay routes:
        
        ncgcli fast-path routes show
        




### Adjust maximum transmission unit

The [maximum transmission unit (MTU)](https://wikipedia.org/wiki/Maximum_transmission_unit) is the size, in bytes, of the largest packet supported by a network layer protocol, including both headers and data. If there are traffic issues caused by underlay network MTU limitations, you can configure the MTU on the `OverlayVPNTunnel` custom resource. The default MTU for the tunnels is 1380 bytes.

To adjust MTU for your tunnels:

  1. Check the status of the tunnels:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get OverlayVPNTunnel \
             --namespace kube-system --output yaml
         

The `status` section should look like the following example:
         
         status:
           IfName: ipsec2
           LastTransition: "2022-06-16T07:13:28Z"
           SLA:**    DiscoveredMTU: 1300**
             Jitter(ms): 1
             Latency(ms): 26
             Loss(%): "0.00"
         

If the `status.SLA.DiscoveredMTU` value is less than the default of `1380`, use the following steps to change the `Spec.mtu` value in your `OverlayVPNTunel` custom resources to match.

  2. Open your `OverlayVPNTunnel` custom resources for editing with the `kubectl edit` command:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG edit OVERLAY_VPN_TUNNEL_NAME
             --namespace kube-system --output yaml
         

To avoid packet loss, configure the same MTU for the two `OverlayVPNTunnel` custom resources used by Network Connectivity Gateway.

  3. Set the `mtu` value to match the `DiscoveredMTU` value from the first step:
         
         apiVersion: networking.gke.io/v1alpha1
           kind: OverlayVPNTunnel
           metadata:
             name: vpc2
             namespace: kube-system
           Spec:**    mtu: 1300**
             ikeKey:
               name: ike-key
               namespace: kube-system
             localTunnelIP: 169.254.0.2
             peer:
               publicIP: 34.100.10.10
             self:
               publicIP: 70.32.151.5
         

  4. To apply your changes, save and close your editor.




For more information about MTU and how it affects traffic performance, see [MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

### See traffic flow and application-level statistics

To see traffic flow and statistics, run `ncgcli` inside the gateway Pod.

  * For an instantaneous view of the flows and traffic applications:
        
        ncgcli forwarding flows top
        

  * For aggregate statistics at the flow level:
        
        ncgcli forwarding flows aggregates show
        

  * For aggregate statistics at the interface level:
        
        ncgcli interfaces statistics show
        




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
