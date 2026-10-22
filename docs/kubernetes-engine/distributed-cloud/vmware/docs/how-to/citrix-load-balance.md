---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/citrix-load-balance/
title: Load balancing with Citrix \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:28.128566+00:00
---

# Load balancing with Citrix  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/citrix-load-balance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Load balancing with Citrix Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to configure the [Citrix load balancer](https://www.citrix.com/products/citrix-adc/?utm_campaign=WWWB0511NSTRDIYDR&utm_medium=Paid+Search+\(SEM\)&utm_source=sem-net-adc-us-en-sea-go&ctm_programid=WWWB0511NSTRDIYDR) for a cluster created with Google Distributed Cloud (software only) for VMware.

Clusters can run with one of three load balancing modes: integrated, bundled, or manual. To use the Citrix load balancer, you use [manual load balancing mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance).

## Citrix Netscaler version

The instructions in this topic are written for version 12.0 of the Citrix NetScaler VPX 1000 model.

If you are using a different version or model of the Citrix load balancer, the user interface might be different.

## Steps common to all manual load balancing

Before you configure your Citrix load balancer, perform the following steps, which are common to all manual load balancing configurations:

  * [Reserve IP addresses for nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#setting_aside_node_ip_addresses).

  * [Reserve VIPs for load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#set_aside_vips).

  * [Reserve node ports](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#setting_aside_node_ip_addresses).

  * [Modify the cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configuration-file-overview).




## Creating a Citrix ADC instance

To create a Citrix Application Delivery Controller (ADC), perform these steps:

  * In your vSphere environment, create a VM that runs the [Citrix ADC](https://www.citrix.com/products/citrix-adc/), formerly called NetScaler ADC.

For instructions, see [Install a Netscaler instance](https://docs.citrix.com/en-us/netscaler/12/deploying-vpx/install-vpx-on-esx.html).

  * See the information about [licensing](https://docs.citrix.com/en-us/netscaler/12/licensing.html) your Citrix ADC.

  * Configure a management IP address for your Citrix ADC. For instructions, see [Configuring the NetScaler IP Address (NSIP)](https://docs.citrix.com/en-us/netscaler/12/networking/ip-addressing/configuring-netscaler-owned-ip-addresses/configuring-netscaler-ip-address.html).




## Adding network adapters

Your Citrix ADC VM has one network adapter, and the adapter is associated with the management IP address for the VM. Now you need to add one or two additional network adapters to your Citrix ADC VM.

One possibility is to create a one-armed configuration. In this kind of configuration, your Citrix ADC VM has one network adapter in addition to the management network adapter. The one additional network adapter is connected to a subnet that has your cluster nodes. You can reach IP addresses on this subnet from the internet.

Another possibility is to create a two-armed configuration. In this kind of configuration, your Citrix ADC VM has two network adapters in addition to the management network adapter. One of the additional network adapters is connected to a private subnet that has your cluster nodes. The other additional network adapter is connected to a subnet that allows external requests to reach the Citrix load balancer. This could be a subnet that is directly accessible from the internet, or it could be a subnet that is protected from the internet by a jumpbox.

The following diagram shows an example of a two-armed configuration:

[ ![Diagram of two-armed configuration](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/two-armed-citrix.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/two-armed-citrix.svg) Two-armed configuration (click to enlarge)

To add one or two network adapters to your Citrix ADC VM, use the vSphere interface.

  1. In the left pane, locate your Citrix ADC VM.

  2. Right click your Citrix ADC VM, and select **Edit Settings**.


[ ![Screenshot of editing the Citrix ADC VM](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-adapter.png)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-adapter.png) Editing properties of the Citrix ADC (click to enlarge)

  1. For **New device** , open the **Select** menu, and select **Network**. Click **Add**.

  2. In the left pane, expand **New Network**. For **VM Network** , select the subnet where you want to connect your new network adapter.

  3. Make other settings as desired, and click **OK**.




## Using Terraform to configure Citrix ADC

Citrix has provided a [Terraform script](https://github.com/citrix/citrix-k8s-ingress-controller/tree/master/deployment/anthos/citrix-adc-for-control-plane) to automatically configure the Citrix ADC with servers, service groups, and virtual servers for the initial cluster set up.

You can choose to follow the manual steps below if preferred.

## Configuring servers

Recall that you already have a list of IP addresses that you intend to use for your cluster nodes. In this section, you associate each of those IP addresses with a name.

In a browser, enter the management IP address of your Citrix VM. This opens a web interface to your Citrix load balancer. In the Citrix interface, the term for a cluster node is _server_.

Open the **Configuration** tab.

In the left pane, go to **Traffic Management > Load Balancing > Servers**.

[ ![Screenshot of adding a server in the Citrix user interface](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-server.png)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-server.png) Adding a server in the Citrix user interface (click to enlarge)

For each admin cluster node and each user cluster node that you intend to create, perform the following steps:

  1. In the main pane, click **Add**.

  2. Enter a name and IP address for the node.

  3. Click **Create**.




## Configuring service groups

In the Citrix interface, a _service group_ is a set of servers along with a protocol and a port number. Here's an example:
    
    
    ({admin_node_1, admin_node_2, admin_node_3}, TCP, 30001)

In this section, you create a service group for each of the following:

  * Admin cluster control plane
  * Admin cluster addon manager
  * User cluster control plane
  * User cluster konnectivity server
  * User cluster HTTP ingress controller
  * User cluster HTTPS ingress controller



In each service group, the protocol is TCP. The VIP is an address that you previously set aside. The port is a `nodePort` value that you previously set aside.

For example, suppose these are the names of your user cluster nodes:

  * user_node_1
  * user_node_2
  * user_node_3



Also suppose you have chosen to use 203.0.113.1 as the VIP for the HTTP user cluster ingress controller. And you have chosen to use 32001 as the `nodePort` value for the HTTP user cluster ingress controller. Then you would create the following service group:
    
    
    ({user_node_1, user_node_2, user_node_3}, TCP, 32001)

To create a service group in the Citrix web interface, follow these steps:

  1. In the left pane, go to **Traffic Management > Load Balancing > Service Groups**.

[ ![Screenshot of adding a service group in the Citrix user interface \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-service-group.png)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-service-group.png) Adding a service group in the Citrix user interface (click to enlarge)

  1. In the main pane, click **Add**.

  2. Enter a name for the service group.

  3. For **Protocol** , select **TCP**.

  4. Click **OK**.

  5. Under **Service Group Members** , click the bar that says **No Service Group Member**.

  6. At the top of the page, select **Server Based**.

  7. Under **Select Server** , click the box.

  8. In the list of server names, select the servers that you want to be in your service group. Then click **Select**.

  9. For **Port** , enter the `nodePort` value for your service group.

  10. For **Hash Id** , enter a number of your choice.




Repeat these steps for each service group you want to create. You should create a service group for each of these components: admin cluster control plane, admin cluster addon manager, user cluster control plane, user cluster konnectivity server, user cluster HTTP ingress controller, and the user cluster HTTPS ingress controller. Each user cluster requires its own service groups for the user cluster HTTP ingress controller and the user cluster HTTPS ingress controller.

## Configuring virtual servers

At this point, you have 6 service groups. In this section, you associate each service group with a VIP, a protocol, and a port.

For example, suppose the following:

  * The service group for your user cluster HTTP ingress controller is named `user_http_ingress`.

  * You have chosen to use 203.0.113.1 as the VIP for your user cluster HTTP ingress controller. And you want the load balancer to listen for requests sent to this VIP on TCP port 80.

  * You have chosen to use 32001 as the `nodePort` value for the user cluster HTTP ingress controller.




Then you would create the following association:
    
    
    user_http_ingress --> (203.0.113.1, TCP, 80)

In the Citrix interface, an association of this type is called a _virtual server_.

To create a virtual server in the Citrix web interface, follow these steps:

  1. In the left pane, go to **Traffic Management > Load Balancing > Virtual Servers**.

[ ![Screenshot of adding a virtual server in the Citrix user interface \(click to enlarge\)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-virtual-server.png)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/add-service-group.png) Adding a virtual server in the Citrix user interface (click to enlarge)

  1. In the main pane, click **Add**.

  2. Enter a name for the virtual server.

  3. For **Protocol** , select **TCP**.

  4. For **IP Address** , enter the VIP for your virtual server.

  5. For **Port** , enter the TCP port for the virtual server. The load balancer will listen for requests sent to the VIP on this TCP port.

  6. On the **Load Balancing Virtual Server** page, under **Services and Service Groups** , click **No Load Balancing Virtual Server Service Group Binding**.

  7. Under **Select Service Group Name** , click the box.

  8. Select the service group that you want for the virtual server.

  9. At the top of the page, click **Select**.

  10. Click **Bind**.




Go through the preceding steps 6 times, so that you have a virtual server for each of your 6 service groups. Check [this page](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance#config_lb) for the complete port mapping.

## Verifying the configuration

To verify that your VIPs have been configured on your Citrix ADC, ping each of your VIPs.

## Modifying your configuration file

Before you install Google Distributed Cloud, [modify your configuration files](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configuration-file-overview) to include your static IP addresses, VIPs, and node port values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
