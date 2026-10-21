---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/troubleshooting/
title: Troubleshoot Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:38.124006+00:00
---

# Troubleshoot Distributed Cloud connected  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/troubleshooting/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/overview)



Send feedback 

#  Troubleshoot Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

Google remotely monitors and maintains the Google Distributed Cloud connected hardware. For this purpose, Google engineers have Secure Shell (SSH) access to the Distributed Cloud connected hardware. If Google detects an issue, a Google engineer contacts you to troubleshoot and resolve it. If you have identified an issue yourself, contact Google Support immediately to diagnose and resolve it.

## Corrupt BGP sessions in Cloud Router resources used by VPN connections

Distributed Cloud VPN connections rely on BGP sessions established and managed by their corresponding Cloud Router resources to advertise routes between the Distributed Cloud connected cluster and Google Cloud. If you modify the configuration of a Cloud Router resource associated with a Distributed Cloud VPN connection, that connection can stop functioning.

To recover the corrupt BGP session configuration in the affected Cloud Router, complete the following steps:

  1. In the Google Cloud console, get the name of the corrupt BGP session. For example:
         
         INTERFACE=anthos-mcc-34987234
         

  2. Get the peer BGP and the Cloud Router BGP IP addresses for the corrupted BGP session, as well as the peer ASN used by the affected Distributed Cloud VPN connection. For example:
         
         GDCE_BGP_IP=168.254.208.74
         CLOUD_ROUTER_BGP_IP=168.254.208.73
         PEER_ASN=65506
         

If you deleted the BGP session, get this information from the Distributed Cloud connected cluster instead:

     1. Get the cluster credentials:
            
            gcloud edge-cloud container clusters get-credentials CLUSTER_ID \
              --location REGION \
              --project PROJECT_ID
            

Replace the following:

        * `CLUSTER_ID`: the name of the target cluster.
        * `REGION`: the Google Cloud region in which the target cluster is created.
        * `PROJECT_ID`: the ID of the target Google Cloud project.
     2. Get the configuration of the `MultiClusterConnectivityConfig` resource:
            
            kubectl get multiclusterconnectivityconfig -A
            

The command returns output similar to the following:
            
            NAMESPACE     NAME                   LOCAL ASN              PEER ASN
             kube-system   MultiClusterConfig1    65505                   65506
             ```
            

     3. Get the peer BGP IP address, the Cloud Router IP address, and the BGP session ASN:
            
            kubectl describe multiclusterconnectivityconfig -n kube-system MCC_CONFIG_NAME   
            

Replace `MCC_CONFIG_NAME` with the name of the `MultiClusterConfigResource` that you obtained in the previous step.

The command returns output similar to the following:
            
            ​​Spec:
             Asns:
               Peer:  65505
               Self:  65506 # GDCE ASN
             Tunnels:
               Ike Key:
                 Name:       MCC_CONFIG_NAME-0
                 Namespace:  kube-system
               Peer:
                 Bgp IP:      169.254.208.73 # Cloud Router BGP IP
                 Private IP:  34.157.98.148
                 Public IP:   34.157.98.148
               Self:
                 Bgp IP:      169.254.208.74 # GDCE BGP IP
                 Private IP:  10.100.29.49
                 Public IP:   208.117.254.68
             ```
            

  3. In the Google Cloud console, get the name, region, and Google Cloud project name for the corrupted VPN tunnel. For example:
         
         VPN_TUNNEL=VPNTunnel1
         REGION=US-East1
         VPC_PROJECT_ID=VPC-Project-1
         

  4. Delete the corrupted BGP session from the Cloud Router configuration.

  5. Create a new Cloud Router interface:
         
         gcloud compute routers add-interface --interface-name=INTERFACE_NAME \
            --vpn-tunnel=TUNNEL_NAME \ 
            --ip-address=ROUTER_BGP_IP \
            --project=VPC_PROJECT_ID \
            --region=REGION \      
            --mask-length=30
         

Replace the following:

     * `INTERFACE_NAME`: a descriptive name that uniquely identifies this interface.
     * `TUNNEL_NAME`: the name of the VPN tunnel that you obtained in the previous step.
     * `ROUTER_BGP_IP`: the BGP IP address of the Cloud Router that you obtained earlier in this procedure.
     * `VPC_PROJECT_ID`: the ID of the target VPC Google Cloud project.
     * `REGION`: the Google Cloud region in which the target VPC Google Cloud project has been created. 
  6. Create the BGP peer:
         
         gcloud compute routers add-bgp-peer --interface=INTERFACE_NAME \
            --peer-name=TUNNEL_NAME \
            --region REGION \
            --project=VPC_PROJECT_ID \
            --peer-ip-address=GDCE_BGP_IP \
            --peer-asn=GDCE_BGP_ASN \
            --advertised-route-priority=100 \
            --advertisement-mode=DEFAULT
         

Replace the following:

     * `INTERFACE_NAME`: the name of the interface that you created in the previous step.
     * `TUNNEL_NAME`: the name of the VPN tunnel that you used to create the interface in the previous step.
     * `REGION`: the Google Cloud region in which the target VPC Google Cloud project is created.
     * `VPC_PROJECT_ID`: the ID of the target VPC Google Cloud project.
     * `GDCE_BGP_IP`: the Distributed Cloud peer BGP IP address that you obtained earlier in this procedure.
     * `GDCE_BGP_ASN`: the Distributed Cloud peer BGP ASN that you obtained earlier in this procedure.



At this point, the BGP session is back up and operational.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
