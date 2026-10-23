---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status/
title: Check VPN status \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:48.622015+00:00
---

# Check VPN status  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Check VPN status Stay organized with collections  Save and categorize content based on your preferences. 

After you configure your peer VPN gateways, check the following components to ensure that they are communicating correctly with Cloud VPN:

  * Check the status of the HA VPN or Classic VPN tunnels that you configured, including the operational state.
  * Check the high availability status of tunnels on an HA VPN gateway.
  * View the status of Cloud Router Border Gateway Protocol (BGP) sessions or the routes that Cloud Router is advertising.



For more information about Cloud VPN, see the following resources:

  * For best practices to consider before setting up Cloud VPN, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices).

  * For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).




## Check HA VPN tunnels

Use this procedure to check the status of tunnels on both interfaces of an HA VPN gateway.

**Caution:** When using HA VPN, you should also check the high-availability status of tunnels on your VPN gateway to ensure that you are receiving the 99.99% availability SLA.

###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=tunnels)

  2. View the **VPN tunnel status** and the [**BGP session status**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  3. To view tunnel details, click the **Name** of a tunnel.

  4. Under **Cloud VPN Gateway** , click **View** for viewing logs.

  5. You can also modify the BGP session associated with this tunnel.




###  gcloud 

There are two steps to viewing tunnel status. First, identify the tunnel name and region, and then use the `describe` command option to view tunnel details.

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `GW_NAME`: the name of the gateway
  * `REGION`: the region where the gateway or tunnel resides
  * `NAME`: the name of the tunnel



To view tunnel status, complete the following steps:

  1. Identify the name and region of the VPN tunnel whose status you need to check. You can identify the tunnel by using either of the following methods:

     1. **Option 1:** To list _all_ VPN tunnels in your project, run the following command:
            
            gcloud compute vpn-tunnels list
              --project=PROJECT_ID
            

The command output should look similar to the following example:
            
            NAME                REGION       GATEWAY      VPN_INTERFACE  PEER_ADDRESS
            tunnel-a-to-b-if-0  us-central1  ha-vpn-gw-a  0              10.242.123.165
            tunnel-a-to-b-if-1  us-central1  ha-vpn-gw-a  1              10.220.75.213
            tunnel-b-to-a-if-0  us-central1  ha-vpn-gw-b  0              10.242.127.148
            tunnel-b-to-a-if-1  us-central1  ha-vpn-gw-b  1              10.220.66.156
            

     2. **Option 2:** If you know the name of the VPN gateway that contains the tunnel, to retrieve the list of the gateway's associated tunnels, run the following command:
            
            gcloud compute vpn-gateways describe GW_NAME \
              --region=REGION \
              --project=PROJECT_ID \
              --format='flattened(tunnels)'
            

  2. After you know the name and region of the tunnel, use the `describe` option of the `vpn-tunnels` command to determine the tunnel's status:
         
         gcloud compute vpn-tunnels describe NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --format='flattened(status,detailedStatus)'
         

The basic status message and a more detailed message are returned. The command output should look similar to the following example. For a full listing, omit the `--format` option.
         
         detailedStatus: Tunnel is up and running.
         

The following four command output examples show a full listing for a pair of tunnels on each of two HA VPN gateways that are connected to each other. That is, on `ha-vpn-gw-a`, the tunnels on `interface 0` and `interface 1` are connected to tunnels on the corresponding interfaces of `ha-vpn-gw-b`.

Example 1: **`tunnel-a-to-b-if-0`**
         
         creationTimestamp: '2018-10-11T13:12:33.851-07:00'
          description: ''
          detailedStatus: Tunnel is up and running.
          id: '2919847494518181982'
          ikeVersion: 2
          kind: compute#vpnTunnel
          labelFingerprint: LABEL_FINGERPRINT
          localTrafficSelector:
          — 0.0.0.0/0
          name: tunnel-a-to-b-if-0
          peerIp: GW_A_IF_0_IP
          region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
          remoteTrafficSelector:
          — 0.0.0.0/0
          router: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
          selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
          sharedSecret: '*************'
          sharedSecretHash: SECRET_HASH
          vpnGateway: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a
          vpnGatewayInterface: 0
         

Example 2: **`tunnel-a-to-b-if-1`**
         
         creationTimestamp: '2018-10-11T13:14:21.630-07:00'
          description: ''
          detailedStatus: Tunnel is up and running.
          id: '178016642781024754'
          ikeVersion: 2
          kind: compute#vpnTunnel
          labelFingerprint: LABEL_FINGERPRINT
          localTrafficSelector:
          —0.0.0.0/0
          name: tunnel-a-to-b-if-1
          peerIp: GW_B_IF_1_IP
          region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
          remoteTrafficSelector:
          — 0.0.0.0/0
          router: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
          selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
          sharedSecret: '*************'
          sharedSecretHash: SECRET_HASH
          vpnGateway: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a
          vpnGatewayInterface: 1
         

Example 3: **`tunnel-b-to-a-if-0`**
         
         creationTimestamp: '2018-10-11T13:16:19.345-07:00'
          description: ''
          detailedStatus: Tunnel is up and running.
          id: '1183416925692236156'
          ikeVersion: 2
          kind: compute#vpnTunnel
          labelFingerprint: LABEL_FINGERPRINT
          localTrafficSelector:
          — 0.0.0.0/0
          name: tunnel-b-to-a-if-0
          peerIp: GW_A_IF_0_IP
          region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
          remoteTrafficSelector:
          — 0.0.0.0/0
          router: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b
          selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
          sharedSecret: '*************'
          sharedSecretHash: SECRET_HASH
          vpnGateway: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-b
          vpnGatewayInterface: 0
         

Example 4: **`tunnel-b-to-a-if-1`**
         
         creationTimestamp: '2018-10-11T13:19:01.562-07:00'
          description: ''
          detailedStatus: Tunnel is up and running.
          id: '8199247227773914842'
          ikeVersion: 2
          kind: compute#vpnTunnel
          labelFingerprint: LABEL_FINGERPRINT
          localTrafficSelector:
          — 0.0.0.0/0
          name: tunnel-b-to-a-if-1
          peerIp: GW_A_IF_1_IP
          region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
          remoteTrafficSelector:
          — 0.0.0.0/0
          router: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b
          selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
          sharedSecret: '*************'
          sharedSecretHash: SECRET_HASH
          vpnGateway: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-b
          vpnGatewayInterface: 1
         




###  API 

To view tunnel details, you can use either of the following API calls:

  * To list the attributes and status of all VPN tunnels in a specific project and region, make a GET request by using the [`vpnTunnels.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/list) method:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels
        

  * To list the attributes and status of a specific tunnel in a specific project and region, make a GET request by using the [`vpnTunnels.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/get) method:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
        




## Check Classic VPN tunnels

Use this procedure to check the status of tunnels on a Classic VPN gateway.

###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=tunnels)

  2. View the [**VPN tunnel status**](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#message_list) and the [**BGP session status**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  3. To view tunnel details, click the **Name** of a tunnel.

  4. Under **Cloud VPN Gateway** , click **View** for viewing logs.

  5. You can also modify the BGP session associated with this tunnel.




###  gcloud 

The procedure for checking Classic VPN tunnel status is similar to the one for HA VPN.

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `GW_NAME`: the name of the gateway
  * `REGION`: the region where the gateway or tunnel resides
  * `NAME`: the name of the tunnel



To view tunnel status, complete the following steps:

  1. Identify the name and region of the VPN tunnel whose status you need to check. You can identify the tunnel by using either of the following methods:

     1. **Option 1:** To list _all_ VPN tunnels in your project, run the following command:
            
            gcloud compute vpn-tunnels list
              --project=PROJECT_ID
            

     2. **Option 2:** If you know the name of the VPN gateway that contains the tunnel, to retrieve the list of the gateway's associated tunnels, run the following command:
            
            gcloud compute target-vpn-gateways describe GW_NAME \
              --region=REGION \
              --project=PROJECT_ID \
              --format='flattened(tunnels)'
            

  2. Describe the tunnel to determine its status by running the following command. The basic status message and a more detailed message are returned. For a full listing, omit the `--format` option.
         
         gcloud compute vpn-tunnels describe NAME \
             --region=REGION \
             --project=PROJECT_ID \
             --format='flattened(status,detailedStatus)'
         




###  API 

To view tunnel details, you can use either of the following API calls:

  * To list the attributes and status of all VPN tunnels in a specific project and region, make a GET request by using the [`vpnTunnels.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/list) method:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels
        

  * To list the attributes and status of a specific tunnel in a specific project and region, make a GET request by using the [`vpnTunnels.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/get) method:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
        




## Check Classic VPN forwarding rules

Use this procedure to check the forwarding rules that you created for your Classic VPN gateway.

###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=gateways)

  2. Click a **Gateway name**.

  3. On the **VPN details** page, view the forwarding rules that you created.




###  gcloud 

To view the forwarding rules for a Classic VPN gateway in a specific region, run the following command:
    
    
    gcloud compute target-vpn-gateways describe GW_NAME
        --region=REGION \
        --project=PROJECT_ID
    

###  API 

To view the forwarding rules for a Classic VPN gateway in a specific region, use the [`targetVpnGateways.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/get) method. Replace `RESOURCE_ID` with the name of the gateway.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetVpnGateways/RESOURCE_ID
    

## Interpret tunnel status messages

To interpret tunnel status messages from the Google Cloud console or the Google Cloud CLI, use the following table.

Status | Detailed status message | Notes | Allocating resources | Allocating resources. VPN tunnel will start soon. | The initial state for a newly created Cloud VPN tunnel.  
---|---|---  
Waiting for full config | Waiting for route configuration. | Routes or routing configuration is being prepared.  
First Handshake | Handshake with peer broken for unknown reason. Trying again soon. | Phase 1 (IKE SA) negotiation with the peer VPN is in progress. It might have failed at least once.  
Established | Tunnel is up and running. | The tunnel is up, and routes have been configured.  
No Incoming Packets | No incoming packets from peer. | No traffic is being received from the peer VPN gateway.  
  
## Check high availability status for HA VPN gateways

**Note:** For configurations that do or don't guarantee 99.99% availability, see [Cloud VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).

To check the high-availability configuration status for tunnels on an HA VPN gateway, use the Google Cloud console, the `compute vpn-gateways get-status` command, or the `vpnGateways.getStatus` method.

The output displays the high-availability redundancy requirement state for VPN tunnels associated with each peer gateway to which the HA VPN gateway is connected.

The peer gateway can be another HA VPN gateway or an external VPN gateway. If there are multiple peer gateways connected to the HA VPN gateway, multiple high-availability configuration statuses are displayed, one status per each peer gateway.

The command output indicates the correct tunnel amount and coverage in the following ways:

  * VPN gateways configured with adequate redundancy (coverage) show the following status:  
`HighAvailabilityRedundancyRequirementState: CONNECTION_REDUNDANCY_MET`.
  * VPN gateways that are not configured with adequate redundancy show the following status:  
`HighAvailabilityRedundancyRequirementState: CONNECTION_REDUNDANCY_NOT_MET`.
  * If there are not enough tunnels configured between your HA VPN gateway and another HA VPN gateway or a peer gateway, the command output shows the following status:  
`redundancyUnsatisfiedReason: INCOMPLETE_TUNNELS_COVERAGE`.



For additional information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#vpn-monitoring-metrics).

###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=gateways)

  2. To view gateway details for the gateway and its tunnels, click **Gateway name**. For HA VPN gateways, you can also view high-availability status for the gateway.




###  gcloud 

To display tunnel status for the HA VPN gateway, run the following command. Replace the following:

  * `GW_NAME`: the name of the HA VPN gateway
  * `REGION`: the region where the gateway resides


    
    
    gcloud compute vpn-gateways get-status GW_NAME \
        --region=REGION
    

The following command output example shows information for an HA VPN gateway connected to a peer gateway with two interfaces:
    
    
      peerGateways:
      — peerExternalGateway: peer-gw
      tunnels:
      — localGatewayInterface: 0
        peerGatewayInterface: 0
        tunnelUrl:
        https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
        regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0
      — localGatewayInterface: 1
        peerGatewayInterface:1
        tunnelUrl:
        https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
        regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1
        **HighAvailabilityRedundancyRequirementState:
          state: CONNECTION_REDUNDANCY_MET**
    

The following command output example is for two HA VPN gateways connected to each other. For this type of configuration, run the command for each HA VPN gateway name:

  * Getting status for `ha-vpn-gw-a` shows its connection to `ha-vpn-gw-b`:
        
        peerGateways:
        — peerGcpGateway: ha-vpn-gw-b
        tunnels:
        — localGatewayInterface: 0
          peerGatewayInterface: 0
          tunnelUrl:
          https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
          regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
        — localGatewayInterface: 1
          peerGatewayInterface: 1
          tunnelUrl:
          https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
          regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
          **HighAvailabilityRedundancyRequirementState:
            state: CONNECTION_REDUNDANCY_MET**
        

  * Getting status for `ha-vpn-gw-b` shows its connection to `ha-vpn-gw-a`:
        
        peerGateways:
        — peerGcpGateway: ha-vpn-gw-a
        tunnels:
        — localGatewayInterface: 0
          peerGatewayInterface: 0
          tunnelUrl:
          https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
          regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
        — localGatewayInterface: 1
          peerGatewayInterface: 1
          tunnelUrl:
          https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
          regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
          **HighAvailabilityRedundancyRequirementState:
            state: CONNECTION_REDUNDANCY_MET**
        




The following command output example is for one HA VPN gateway connected to an AWS virtual gateway with two connections and four IP addresses:
    
    
      peerGateways:
      - peerExternalGateway: peer-gw
      tunnels:
       - localGatewayInterface: 0
         peerGatewayInterface: 0
         tunnelUrl:
         https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
         regions/us-central1/vpnTunnels/tunnel-a-to-aws-connection-0-ip0
       - localGatewayInterface: 0
         peerGatewayInterface: 1
         tunnelUrl:
         https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
         regions/us-central1/vpnTunnels/tunnel-a-to-aws-connection-0-ip1
       - localGatewayInterface: 1
         peerGatewayInterface: 2
         tunnelUrl:
         https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
         regions/us-central1/vpnTunnels/tunnel-a-to-aws-connection-1-ip0
       - localGatewayInterface: 1
         peerGatewayInterface: 3
         tunnelUrl:
         https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
         regions/us-central1/vpnTunnels/tunnel-a-to-aws-connection-1-ip1
         **HighAvailabilityRedundancyRequirementState:
           state: CONNECTION_REDUNDANCY_MET**
    

The following command output example is for two HA VPN gateways connected to each other with a single tunnel. This configuration _does not_ meet the 99.99% availability SLA:
    
    
      peerGateways:
        - peerGcpGateway: ha-vpn-gw-a
        tunnels:
        - localGatewayInterface: 0
          peerGatewayInterface: 0
          tunnelUrl:
          https://www.googleapis.com/compute/v1/projects/PROJECT_ID/
          regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
          **HighAvailabilityRedundancyRequirementState:
            state: CONNECTION_REDUNDANCY_NOT_MET
          detailedStatus:
            redundancyUnsatisfiedReason: INCOMPLETE_TUNNELS_COVERAGE**
    

###  API 

To get the status of a specific HA VPN gateway in a specific project and region, make a GET request by using the [`vpnGateways.getStatus`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/getStatus) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/GATEWAY_NAME/getStatus
    

## Check BGP status

For tunnels that use dynamic routing with BGP, you can [check Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details) to view details such as the status of a router's BGP sessions or the routes that the Cloud Router is advertising.

## What's next

  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
