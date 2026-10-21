---
url: https://docs.cloud.google.com/telecom-network-automation/docs/operate-edge/
title: Operate GDC network \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:44.495284+00:00
---

# Operate GDC network  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/operate-edge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Operate GDC network Stay organized with collections  Save and categorize content based on your preferences. 

In addition to Kubernetes cluster resources, APIs, and the default Kubernetes pod network, GDC lets you provision additional networks in a GDC zone and connect them with your networks. For example, if using a user plane function (UPF), you might create a radio access network (RAN) and a data plane network, each with different subnets that connect to the UPF pods.

For more information about Edge Network resources, see [Networking](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/how-it-works#networking).

## `EdgeNetwork` blueprints

This blueprint contains multiple custom resources with the intent to allow users to provision and configure additional networks in a GDC zone and connect them with your networks. For example, you might create an operations, administration, and maintenance (OAM) network and a Signal network, each with different multiple subnets that connect to the secondary interfaces of the Network Function pods. The following resources are used for the `EdgeNetwork` blueprint:

  * `EdgeNetwork`: a virtual private network in a GDC zone. Packets are routed independently within an `EdgeNetwork`.
  * `EdgeRouter`: a logical resource in the GDC zone that configures BGP related parameters for an `EdgeNetwork`.
  * `EdgeSubne`t: An L2 domain, L3 subnet in a GDC zone. `EdgeSubnet` is created as a VLAN with an associated VLAN ID in the network.
  * `EdgeInterconnectAttachment`: configures a new virtual link between a GDC zone router and one of your Provider Edge (PE) routers. You can use the attachment to connect an `EdgeNetwork` resource with a network, such as virtual routing and formatting (VRF), on your network.



When creating a deployment, you can customize a blueprint using the following parameters in the `setters.yaml` file:

Parameter | Description  
---|---  
`project-id` | The project ID of a project that manages `EdgeNetwork` related resources. You must link Edge to this specific project ID.  
`network-name` | The name of an `EdgeNetwork` resource.  
`location` | The Google Cloud region of the GDC zone. For example, `us-west-1`.  
`zone` | The GDC zone to create the `EdgeNetwork`.  
`mtu` | The IP maximum transmission unit (MTU) of the `EdgeNetwork`. Valid options are between `1500` and `9000`.  
`interconnect-attachment-name` | The name of the interconnect attachment.  
`interconnect-attachment-vlanid` | The package tagged VLAN ID assigned to an interconnect attachment.  
`interconnect-attachment-interface-ipv4cidr` | The IP address for the `EdgeRouter`interface that connects to the `EdgeInterconnectAttachment` resource.  
`interconnect-attachment-bgppeer-ipv4cidr` | The GDC zone peer side IPv4 address of the BGP session.  
`subnet-name` | The name of the `EdgeSubnet` resource.  
`subnet-vlan-id` | The VLAN ID assigned to an `EdgeSubnet` resource.  
`subnet-ipv4cidr` | The IPv4 subnet for an `EdgeSubnet`resource. The first IP address in the classless interdomain routing (CIDR) is reserved as the subnet gateway.  
`subnet-bgppeer-ipv4cidr` | The IP address of the BGP in the peer side. The IP address must be in the same subnet of the `EdgeSubnet` resource.  
  
## Configure the network with two subnets

This section covers operations to configure a network with two subnets. For example, the example network `ran-network` has two subnets, `ranaccess-1`and `ranaccess-2`. For northbound connections, `ran-network` configures two interconnect attachments for interconnects `cbae0a11-5d97-4bd6-8a09-e5133bb541ca` and `a52e2c74-84f2-4a6d-8cd2-7c5b0fc1c031`.

### Import an `EdgeNetwork` blueprint

  1. From the navigation menu, click **Blueprints**.
  2. From the dropdown menu, select your preferred Orchestration cluster.
  3. Click **Import from Library**.
  4. Select the blueprint, **GDCE EdgeNetwork setup**.
  5. Click **Add Blueprint**.
  6. On the next page, specify a name for the blueprint. For example, **GDCE EdgeNetwork setup**. 
     1. Optionally, add any labels.
  7. Click **Create**. The blueprint appears in the **Draft Blueprints** list.



### Edit a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint.**
  2. Select the blueprint you want to edit. A blueprint editor opens.
  3. Edit the resources to your specification.
  4. Afterwards, click **Save File**.

**Note:** You must save each file individually.



### Propose a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint.** A blueprint editor appears.
  2. Click **Propose**. The status of the blueprint updates to **Proposed**.



### Approve a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint**.
  2. Click on the **Action** icon by the blueprint name.
  3. Select **Approve**. The blueprint appears in **Approved Blueprints**.



## Retrieve the interconnect information

To retrieve the interconnect information, do the following:

  1. Set and export environment variables:
         
         export networkName=NETWORK_NAME
         export MACHINES_LOCATION=MACHINE_LOCATION # value where machines or rack is located. Can be different from cluster location.
         export MACHINES_PROJECT_ID=PROJECT_ID # project in which machines or rack is registered. Can be different from cluster project
         export EDGE_ZONE=ZONE # Edge zone in which machines or rack is located
         

Replace the following:

     * `NETWORK_NAME`: The name of the network.
     * `MACHINE_LOCATION`: The location of your machine or rack. This value can be different from the cluster location.
     * `PROJECT_ID`: The project where the machine or rack is registered. This value can be different from the cluster project.
     * `ZONE`: The Edge zone where the machines or rack is located.
  2. Retrieve the interconnect information:
         
         gcloud alpha edge-cloud networking interconnects list --zone=$EDGE_ZONE --location=$MACHINES_LOCATION --project=$MACHINES_PROJECT_ID
         

The output is similar to the following. Note the name and physical ports of the interconnect to apply on the interconnect attachment with the network.
         
         NAME UUID
         DEVICECLOUDRESOURCENAME
         PHYSICALPORTS
         cbae0a11-5d97-4bd6-8a09-e5133bb541ca cbae0a11-5d97-4bd6-8a09-e5133bb541ca projects/81907970660/locations/us-central1-edge-den8/switches/et19.den97
         
         HundredGigE0/0/0/0,HundredGigE0/0/0/23
         a52e2c74-84f2-4a6d-8cd2-7c5b0fc1c031 a52e2c74-84f2-4a6d-8cd2-7c5b0fc1c031 projects/81907970660/locations/us-central1-edge-den8/switches/et19.den97 HundredGigE0/0/0/1,HundredGigE0/0/0/22
         37e5da97-1a3f-4935-9d9b-0a8cea589644 37e5da97-1a3f-4935-9d9b-0a8cea589644 projects/81907970660/locations/us-central1-edge-den8/switches/et20.den97 HundredGigE0/0/0/0,HundredGigE0/0/0/23
         71b54ef5-6b12-4b03-b8ce-eb88196f8a93 71b54ef5-6b12-4b03-b8ce-eb88196f8a93 projects/81907970660/locations/us-central1-edge-den8/switches/et20.den97 HundredGigE0/0/0/1,HundredGigE0/0/0/22
         




## `EdgeNetwork` deployment

### Create an `EdgeNetwork` deployment

  1. From the navigation menu, click **Blueprints > Approved Blueprints**.
  2. Click on the `EdgeNetwork` blueprint you want to deploy.
  3. Click **Create Deployment**.
  4. Provide a name for the deployment.
  5. Click **Create Deployment**. The deployment appears in **Draft Deployment**.



### Edit an `EdgeNetwork` deployment

  1. From the navigation menu, click **Blueprints**.
  2. Click on the `EdgeNetwork` blueprint you want to edit. A deployment editor appears.
  3. Edit the `setters.yaml` file. For details on each field in the file, see `EdgeNetwork` blueprints. The following example `setters.yaml` file shows a complete configuration:
         
         apiVersion: v1
         kind: ConfigMap
         metadata: # kpt-merge: /setters
           name: setters
           annotations:
             config.kubernetes.io/local-config: "true"
             internal.kpt.dev/upstream-identifier:'|ConfigMap|default|setters'
         data:
           # The project managing the GDC Edge machines.
           project-id: tna-testing-01
           # Name of the network
           network-name: ranprod
           # Location in which to create the resources
           location: us-central1
           # Zone to create in the resources
           zone: us-central1-edge-den8
           # Details of subnets for southbound peering
           # Details of subnet 1
           # Name of the subnet
           subnet1-name: ranaccess-prod1
           # vlanId for the subnet
           subnet1-vlanid: 2142
           # ipv4cidr for the subnet
           subnet1-ipv4cidr: 10.142.0.0/24
           # ipv4cidr for the subnet bgppeer
           subnet1-bgppeer-ipv4cidr: 10.142.0.0/24
           # Details of subnets for southbound peering
           # Details of subnet 1
           # Name of the subnet
           subnet2-name: ranaccess-prod2
           # vlanId for the subnet
           subnet2-vlanid: 2132
           # ipv4cidr for the subnet
           subnet2-ipv4cidr: 10.132.0.0/24
           # ipv4cidr for the subnet bgppeer
           subnet2-bgppeer-ipv4cidr: 10.132.0.0/24
           # Interconnect attachments for northbound peering
           # Details of interconnect attachment 1
           # Name of the interconnect
           interconnect1-name: cbae0a11-5d97-4bd6-8a09-e5133bb541ca
           # Name of the interconnect attachment
           interconnect1-attachment-name: prod1-ran
           # valnId of the interconnect attachment
           interconnect1-attachment-vlanid: 2010
           # ip4vcidr for the interconnect attachment interface
           interconnect1-attachment-interface-ipv4cidr:10.65.128.17/31  # ipv4cidr for the interconnect attachment bgppeer
           interconnect1-attachment-bgppeer-ipv4cidr: 10.65.128.16/31
           # Interconnect attachments for northbound peering
           # Details of interconnect attachment 1
           # Name of the interconnect
           interconnect2-name: a52e2c74-84f2-4a6d-8cd2-7c5b0fc1c031
           # Name of the interconnect attachment
           interconnect2-attachment-name: prod2-ran
           # valnId of the interconnect attachment
           interconnect2-attachment-vlanid: 2020
           # ip4vcidr for the interconnect attachment interface
           Interconnect2-attachment-interface-ipv4cidr:10.65.128.13/31 # ipv4cidr for the interconnect attachment bgppeer
           interconnect2-attachment-bgppeer-ipv4cidr: 10.65.128.12/31
         

  4. Afterwards, click **Save File**.




### Apply an `EdgeNetwork` deployment

  1. From the navigation menu, click **Deployments**.
  2. Select the `EdgeNetwork` deployment you want to apply.
  3. Click **Deploy**.
  4. Confirm the deployment. The deployment appears in **Applied Deployment**.



### Verify an `EdgeNetwork` blueprint

To verify the creation status of `EdgeNetwork` resources, do the following:

###  kubectl 

  1. Generate `kube-credentials` for the Orchestration cluster to use the `kubectl`CLI:
         
         gcloud anthos config controller get-credentials ORCHESTRATION_CLUSTER_NAME
         

Replace ORCHESTRATION_CLUSTER_NAME with the name of the Orchestration cluster.

  2. Wait 30 to 40 minutes for the resources to process.

  3. View the status of the resources:
         
         kubectl describe EdgeNetwork ${networkName} --namespace=tna-config-control
         

The output is similar to the following. Note the `message` and `reason` in `status.conditions`.
         
         Name: ranprod
         Namespace: tna-config-control
         ....
         API Version: config.cloud.google.com/v1alpha1
         Kind: EdgeNetwork
         ....
         Spec:
           Mtu: 9000
           Network Location: us-central1
           Network Zone: us-central1-edge-den8
         Status:
           Conditions:
             Last Transition Time: 2023-03-23T10:08:40Z
             Message: The resource is up to date
             Reason: UpToDate
             Status: True
             Type: Ready
           Create Time: 2023-03-23T10:08:36.582479587Z
           Self Link:
           //gkehub.googleapis.com/v1/projects/tna-testing-01/locations/us-central1/zone s/us-central1-edge-den8/networks/ranprod
           Update Time: 2023-03-23T10:08:40.010036655Z
         Events: <none>
         

  4. Get information of the created Edge router:
         
         kubectl describe EdgeRouter router-${networkName} --namespace=tna-config-control
         

The output is similar to the following:
         
         Name: router-ranprod
         Namespace: tna-config-control
         ...
         API Version: config.cloud.google.com/v1alpha1
         Kind: EdgeRouter
         ....
         Spec:
         .....
           Network:
             External: projects/tna-testing-01/locations/us-central1/zones/us-central1-edge-den8/net works/ranprod
             Object Ref:
               API Group:
               Kind:
               Name:
               Namespace:
           Router Location: us-central1
           Router Zone: us-central1-edge-den8
         Status:
           Bgp Peer:
             Interface: inf-ranaccess-prod1
             Name: 2142-bgp0
             Peer Asn: 3300
             peerIpv4Cidr: 10.142.0.0/24
             Interface: inf-ranaccess-prod2
             Name: 2132-bgp0
             Peer Asn: 3300
             peerIpv4Cidr: 10.132.0.0/24
             Interface: vlan-2010-prod1-ran
             interfaceIpv4Cidr: 10.65.128.17/31
             Name: vlan-2010-bgp0
             Peer Asn: 577
             peerIpv4Cidr: 10.65.128.16/31
             Interface: vlan-2020-prod2-ran
             interfaceIpv4Cidr: 10.65.128.13/31
             Name: vlan-2020-bgp1
             Peer Asn: 577
             peerIpv4Cidr: 10.65.128.12/31
           Conditions:
             Last Transition Time: 2023-03-23T10:47:12Z
             Message: The resource is up to date
             Reason: UpToDate
             Status: True
             Type: Ready
           Create Time: 2023-03-23T10:08:38.995964419Z
           Interface:
             Name: inf-ranaccess-prod1
             Subnetwork:
               API Group: config.cloud.google.com
               Kind: EdgeSubnet
               Name: ranaccess-prod1
               Namespace: tna-config-control
             Name: inf-ranaccess-prod2
             Subnetwork:
               API Group: config.cloud.google.com
               Kind: EdgeSubnet
               Name: ranaccess-prod2
               Namespace: tna-config-control
             ipv4Cidr: 10.65.128.17/31
             Linked Interconnect Attachment:
               API Group: config.cloud.google.com
               Kind: EdgeInterconnectAttachment
               Name: prod1-ran
               Namespace: tna-config-control
             Name: vlan-2010-prod1-ran
             ipv4Cidr: 10.65.128.13/31
             Linked Interconnect Attachment:
               API Group: config.cloud.google.com
               Kind: EdgeInterconnectAttachment
               Name: prod2-ran
               Namespace: tna-config-control
             Name: vlan-2020-prod2-ran
           Self Link: //gkehub.googleapis.com/v1/projects/tna-testing-01/locations/us-central1/zone s/us-central1-edge-den8/routers/router-ranprod
           State: STATE_RUNNING
           Update Time: 2023-03-23T10:36:58.126306756Z
         Events: <none>
         




###  gcloud 

  * Get information of the created Edge router:
        
        gcloud edge-cloud networking routers describe router-${networkName} \ --zone=$EDGE_ZONE \
        --location=$LOCATION \
        --project=GDCE_MACHINES_PROJECT
        

Replace `GDCE_MACHINES_PROJECT` with the project ID of where the GDC machines are registered.

To configure networks for User Plane Function (UPF), repeat this step for each network.




### Delete an `EdgeNetwork` deployment

  1. From the navigation menu, click **Deployments > Applied Deployments**.
  2. Select the `EdgeNetwork` blueprint you want to delete.
  3. Click **Delete**.
  4. Confirm the deletion.
  5. Wait 30 to 45 minutes for the deletion to process.
  6. To ensure you've deleted the resources, repeat the steps in Edit an `EdgeNetwork` deployment . 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
