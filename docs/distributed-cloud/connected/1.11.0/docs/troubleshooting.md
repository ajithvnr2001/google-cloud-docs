---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/troubleshooting/
title: Troubleshoot Distributed Cloud connected \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:52.324515+00:00
---

# Troubleshoot Distributed Cloud connected  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/troubleshooting/

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
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Troubleshoot Distributed Cloud connected Stay organized with collections  Save and categorize content based on your preferences. 

Google remotely monitors and maintains the Google Distributed Cloud connected hardware. For this purpose, Google engineers have Secure Shell (SSH) access to the Distributed Cloud connected hardware. If Google detects an issue, a Google engineer contacts you to troubleshoot and resolve it. If you have identified an issue yourself, contact Google Support immediately to diagnose and resolve it.

## Distributed Cloud connected machine connectivity

This section describes how to check the internet and Google Cloud connectivity for your Distributed Cloud connected machines using the Metrics Explorer feature of Cloud Monitoring.

This procedure uses the following Monitoring metrics:

  * **Machine Connected** (`/machine/connected`): indicates whether the machine is connected to Google Cloud.

  * **Network Connectivity** (`/machine/network/connectivity`): indicates whether the machine's primary network interface has internet connectivity.




To complete the steps in this section, you must satisfy the following prerequisites:

  1. Access to the Google Cloud console and your Distributed Cloud connected Google Cloud project.
  2. The **Monitoring Viewer** IAM role, which lets you view Monitoring metrics.
  3. (Optional) the `machine_id` value of the target Distributed Cloud connected machine for filtering the returned results.



### Use Metrics Explorer to validate machine connectivity

  1. Navigate to Metrics Explorer:

     1. In the Google Cloud console, navigate to the **Monitoring** section.

     2. In the left-hand navigation tree, click **Metrics Explorer**.

  2. Select the target resource type:

     1. In the Metrics Explorer page, navigate to the **Queries** page.

     2. Use the search bar to search for the **Machine** resource type. You can also use the full resource identifier `edgecontainer.googleapis.com/Machine`.

     3. In the returned results, click the **Machine** resource type.

  3. Validate the machine's connection to Google Cloud:

     1. In the **Metric** section, search for the `connected` value.

     2. Select the **Machine Connected** metric. Its full path is `edgecontainer.googleapis.com/machine/connected`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the **Healthy** line remains at 100% contiguously. If at any point this value is 0% or **Unhealthy** , the machine had lost connectivity with Google Cloud at the indicated time.

  4. Validate the machine's internet connectivity:

     1. In the **Metric** section, search for the `connectivity` value.

     2. Select the **Network Connectivity** metric. Its full path is `edgecontainer.googleapis.com/machine/network/connectivity`.

     3. (Optional) Filter by the target `machine_id` value using the **Filter** section.

     4. In the time chart that appears, verify that the **Healthy** line remains at 100% contiguously. If at any point this value is 0% **Unhealthy** , the machine had lost internet connectivity at the indicated time.




### Understand validation results

The following table explains the results returned by Metrics Explorer.

Machine state | Diagnosis | Resolution  
---|---|---  
**Healthy**  
"Machine Connected" metric value is `1`  
"Network Connectivity" metric value is `1`  
| Normal operation. | None.  
**Disconnected**  
"Machine Connected" metric value is `0`  
"Network Connectivity" metric value is `1`  
| Machine has internet connectivity but can't connect to Google Cloud. | Check your [firewall rules](distributed-cloud/connected/1.11.0/docs/requirements#connected_management_and_monitoring_traffic) for Google services and API endpoints. Verify that Distributed Cloud connected agents are running on the machine.  
**Isolated**  
"Machine Connected" metric value is `0`  
"Network Connectivity" metric value is `0`  
| Machine has no internet connectivity. | Check power and network cabling, local network configuration, machine LED status. Verify your VLAN and routing configuration.  
**Intermittent**  
"Machine Connected" metric value alternates between `0` and `1`  
"Network Connectivity" metric value alternates between `0` and `1`  
| Unstable network connection, packet loss, or excessive latency. | Check your local network for congestion and faulty hardware.  
  
If you notice sustained values of `0` for either metric, follow the troubleshooting steps described in the table to resolve them. If the problem persists, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/docs/latest/getting-support) with the affected machine's `machine_id` value and the timestamp of the outage.

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

## Virtual machines stuck in `Pending` state

A virtual machine workload can get stuck in the `Pending` state and fail to schedule on a node if one of the following happens:

  * Distributed Cloud connected cannot allocate the requested resources, such as CPU time, memory, or disk space, to the virtual machine.
  * There is a fault in the virtual machine's configuration.
  * There is a fault with the virtual machine's storage.
  * The target node is tainted.



To resolve this issue, do the following:

  1. Obtain cluster credentials as described in [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters#credentials).

  2. Get information about the affected virtual machine:
         
         kubectl describe virtualmachine VM_NAME -n NAMESPACE
         

Replace the following:

     * `VM_NAME`: The name of the target virtual machine.
     * `NAMESPACE`: The namespace of the target virtual machine.

The command returns output similar to the following:
    
    Status:
    ...
    State:                    Pending
    ...
    Events:
    Type     Reason                  Age   From                       Message
    ----     ------                  ----  ----                       -------
    Normal   SuccessfulCreate        15m   virtualmachine-controller  Created virtual machine my-stuck-vm
    Warning  DiskProvisioningFailed  14m   virtualmachine-controller  Failed to provision disk: DataVolume my-stuck-vm-data-disk not ready
    Warning  PVCNotBound             14m   virtualmachine-controller  PersistentVolumeClaim my-stuck-vm-data-disk is in phase Pending
    Warning  VMINotCreated           10m   virtualmachine-controller  VirtualMachineInstance cannot be created: dependencies not ready
    

The output of the command contains messages that might indicate resource constraints, scheduling failures, storage faults, and other problems.

  3. Examine the output to determine the causes of the scheduling failure as explained in the next sections.




### Insufficient resources

You might see a message indicating insufficient resources, such as CPU, memory, or disk space. For example:
    
    
    5/8 nodes are available: 3 Insufficient memory, 3 Insufficient CPU.
    

To remedy this problem, check the resources allocated to the affected virtual machines and other workloads scheduled on the node, then do the following depending on your business needs:

  * Scale down other workloads scheduled on the node,
  * Reduce the amount of resources allocated to the affected virtual machine,
  * Add more machines to the affected cluster.



### Tainted nodes

You might see a message indicating the target node is tainted. For example:
    
    
    5/8 nodes are available: 3 node(s) had taint {<taint-key>:<taint-value>}, that the pod didn't tolerate.
    

To remedy this problem, do the following:

  1. Use the following command to check for taints on the node:
         
         kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
         

The command returns output similar to the following:
         
         NAME                           TAINTS
         node-name-1   [map[effect:PreferNoSchedule key:node-role.kubernetes.io/master] map[effect:PreferNoSchedule key:node-role.kubernetes.io/control-plane]]
         node-name-2   <none>
         

  2. Do one of the following:

     * For unexpected taints, remove them as described in [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).
     * For expected taints, add corresponding tolerations to the virtual machine's configuration, as described in [Taints and Tolerations](https://kubevirt.io/user-guide/compute/node_assignment/#taints-and-tolerations).



### Storage faults

You might see a message indicating a fault with the virtual machine's storage. For example:
    
    
    5/8 nodes are available: 3 node(s) had volume node affinity conflict, 3 node(s) had unbound immediate PersistentVolumeClaims.
    

This message might indicate that the corresponding persistent volume fails to mount on the target node.

To remedy this problem, do the following:

  1. Use the following command to obtain the status of the persistent volume claims (PVCs) in the affected virtual machine's namespace:
         
         kubectl get pvc -n NAMESPACE
         

Replace `NAMESPACE` with the name of the target namespace.

The command returns output similar to the following:
         
         NAME                                               STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS            AGE
         windows-robin-disk-0                               Bound     pvc-b1a1d264-84bf-4e58-857d-f37f629d5082   25Gi       RWX            robin-block-immediate   30h
         windows-robin-disk-1                               Bound     pvc-0130b9a8-7fed-4df0-8226-d79273792a16   25Gi       RWX            robin-block-immediate   30h
         windows-robin-vm-0-restored-windows-robin-disk-0   Pending                                                                        gce-pd-gkebackup-in     26m
         

  2. Verify that the corresponding PVC has a `Bound` status; if the status is `Pending`, the storage subsystem has failed to provision the volume. In such cases, you must troubleshoot the storage subsystem configuration and ensure that the appropriate `StorageClass` is available.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
