---
url: https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access/
title: Configure private network access \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:09.350510+00:00
---

# Configure private network access  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Configure private network access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up [private network access](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview) and route traffic within a Google Cloud network.

To set up private network access, you configure three projects:

  * A project that contains a Virtual Private Cloud (VPC) network to be used by the target virtual machine instance (VM) or target internal load balancer.
  * A project that acts as a Service Directory service project.
  * A project for a Google Cloud product with the configuration that invokes private network access. An example of a Google Cloud product that can call endpoints using private network access is Dialogflow CX.



The artifacts of the projects could be in the same project or in different projects.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _and_ IAM roles.

**Permissions**

  * `servicedirectory.services.resolve`
  * `servicedirectory.networks.access`
  * `servicedirectory.networks.attach`



**Roles**

  * `servicedirectory.editor`
  * `servicedirectory.viewer`
  * `servicedirectory.pscAuthorizedService`
  * `servicedirectory.networkAttacher`

**Note:** Grant the IAM roles to per-product per-project service accounts. If you aren't assigned the permissions or roles, contact the IAM Administrator who has the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`) to grant you the missing roles.

## Before you begin

Before you configure private network access, complete the following steps:

  * For each project, in the Google Cloud console, on the [**APIs & Services**](https://console.cloud.google.com/apis/dashboard) page, click add**Enable APIs and services** to enable APIs that you want to use that aren't already enabled, including the Service Directory API.

  * To link your VPC network to on-premises hosts, [create a Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create_vpn_tunnels) or a [Cloud Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

**Note:** To set up private network access to on-premises hosts we recommend using an internal load balancer. Create an [internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) with backend hybrid NEGs in the VPC network that's connected to your on-premises network. Then set up private network access to use the internal proxy Network Load Balancer. For details about connectivity requirements for hybrid NEGs, see [Network connectivity requirements](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#network_connectivity_requirements).
  * Ensure that the Google Cloud project is within the VPC Service Controls perimeter of both the network project and the Service Directory project for `servicedirectory.googleapis.com`.

Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).




## Configure the project for the VPC network

To configure the project for the VPC network, follow these steps:

  1. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) or select an existing VPC network that has either an IPv4-only or dual-stack subnet in the region you want to use. [Legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) are not supported.

  2. Create necessary ingress allow firewall rules.

     * If the target is a VM or an internal passthrough Network Load Balancer, firewall rules must permit TCP traffic from the `35.199.192.0/19` range to the ports used by the software running on the target VM instances.

     * If the target is an internal Application Load Balancer or an internal proxy Network Load Balancer, VPC firewall rules and hierarchical firewall policies [do _not_ control](https://docs.cloud.google.com/firewall/docs/firewalls#proxy-lb) which protocols and ports are accepted by the load balancer. For internal Application Load Balancer, a [Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) can be used to restrict access to your load balancer.

For more information about the `35.199.192.0/19` range, see [Paths for Cloud DNS and Service Directory](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns).

  3. Grant the Identity and Access Management (IAM) Private Service Connect Authorized Service role (`roles/servicedirectory.pscAuthorizedService`) to the service agent of the Google Cloud product that will call the endpoint.

For more information about roles and permissions, see [Service Directory permissions and roles](https://docs.cloud.google.com/service-directory/docs/access-control#permissions_and_roles).




## Configure the Service Directory project

To configure the Service Directory project, follow these steps:

  1. In the VPC network, [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) or an [internal load balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid).

  2. Grant the IAM Service Directory Viewer role (`roles/servicedirectory.viewer`) to the service agent of the Google Cloud product that will call the endpoint.

  3. [Create a Service Directory namespace and service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory). Then, create an endpoint for this service, following the steps in the next section.




### Create an endpoint with private network access

**Note:** If the principal performing this operation does not already have broad permissions in the network project, then grant it the Service Directory Network Attacher role (`roles/servicedirectory.networkAttacher`) there.

To create an endpoint with private network access configured, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Service Directory namespaces** page. [Go to Service Directory namespaces](https://console.cloud.google.com/net-services/service-directory/namespaces)
  2. Click a namespace.
  3. Click a service.
  4. Click **Add endpoint**.
  5. For **Endpoint name** , enter a name for the endpoint.
  6. For **IP address** , enter an IPv4 address, such as `192.0.2.0`.
  7. For **Port** , enter a port number, such as `443` or `80`.
  8. To enable private network access, in **Associated VPC network** , select the required option: 
     * To choose from a list of available networks, click **Choose from the list** , and then select the network.
     * To specify a project and a network, click **Specify by a project and network name** , and then enter the project number and the network name.
  9. Click **Create**.



###  gcloud 

Use the [`gcloud service-directory endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create) with the project ID and the network path specified.
    
    
    gcloud service-directory endpoints create ENDPOINT_NAME \
    --project=PROJECT_ID \
    --location=REGION \
    --namespace=NAMESPACE_NAME \
    --service=SERVICE_ID \
    --address=IP_ADDRESS \
    --port=PORT_NUMBER \
    --network=NETWORK_PATH
    

Replace the following:

  * `ENDPOINT_NAME`: a name for the endpoint that you're creating in your service, such as `my-endpoint`
  * `PROJECT_ID`: the ID of the project
  * `REGION`: the Google Cloud region that contains the namespace
  * `NAMESPACE_NAME`: the name that you gave the namespace, such as `my-namespace`
  * `SERVICE_ID`: the ID of the service
  * `IP_ADDRESS`: the IP address of the endpoint, such as `192.0.2.0`
  * `PORT_NUMBER`: the ports that the endpoints are running on, typically `443` or `80`
  * `NETWORK_PATH`: the URL to the network, such as `projects/PROJECT_NUMBER/locations/global/networks/NETWORK_NAME`



**Note:** If the target of your Service Directory endpoint is an on-premises IP address, associate the endpoint with the VPC network that is directly connected to the Cloud VPN tunnel or the Cloud Interconnect connection. For example, in a hub-and-spoke model, associate the endpoint with the hub VPC network and not to the spoke VPC network.

## Configure the Google Cloud product project

To configure the Google Cloud product project, follow these steps:

  1. [Enable the Google Cloud product API](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

  2. Configure your Google Cloud product to call the Service Directory service that you created. The required steps depend on the specific Google Cloud product.




## Use cases

This section provides example use cases for configuring private network access.

### Call an HTTP endpoint when a VPC network, a VM, and Service Directory are in the same project

In this use case, you set up Dialogflow CX, a Google Cloud product for natural language processing, to call an HTTP endpoint on your VM. While calling the endpoint, ensure that the traffic doesn't transition over the public internet.

In this use case, you create the following artifacts in the same project:

  * A VPC network
  * A VM
  * A Service Directory service
  * Dialogflow CX



Figure 1 shows how you can allow a Google service configuration of a project to egress to a VM. The VM resides in a VPC network of the project.

[ ![Allow a Google service configuration of a project to egress to a network project VM.](https://docs.cloud.google.com/static/service-directory/images/egress_to_vm_in_vpc_network.svg)](https://docs.cloud.google.com/static/service-directory/images/egress_to_vm_in_vpc_network.svg) **Figure 1.** Allow a Google service configuration of a project to egress to a VM (click to enlarge).

#### Set up your network and target network

  1. [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), such as `myproject`.
  2. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks), such as `vpc-1`.

While creating the VPC network, in **Subnet creation mode** , select **Automatic**.

  3. [Create a firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules), such as `firewall-1`.

While creating the firewall rule, enter or select the following values:

     * For **Network** , select `vpc-1`.
     * For **Source IPv4 ranges** , enter `35.199.192.0/19`.
     * For **Protocols and ports** , select **TCP** and enter `443` or `80`.
  4. In the `us-central1` region, [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), such as `vm-1`.

While creating the VM, enter or select the following values:

     * For **Networking > Network Interfaces**, select `vpc-1`.
     * For **Firewall** , select **Allow HTTP traffic**.

If you want to use HTTPS, select **Allow HTTPS traffic**. Also make sure that you install a Public Key Infrastructure (PKI) Transport Layer Security (TLS) certificate.

  5. In the `us-central1` region, create a namespace, such as `namespace-1`.

  6. In the namespace, register a Service Directory service, such as `sd-1`.

  7. Create an endpoint in `sd-1`. For the endpoint address, use the internal IP address of `vm-1` on port `443`. For more information, see Create an endpoint with private network access.

  8. Grant the following IAM roles to the service agent of the Google Cloud product that will call the endpoint:

     * Service Directory Viewer role (`roles/servicedirectory.viewer`)
     * Private Service Connect Authorized Service role (`roles/servicedirectory.pscAuthorizedService`)
  9. Optional: If you want to add more VMs, you can set up another VM, such as `vm-2`, and add its endpoint, such as `endpoint-2`.




#### Set up a Google Cloud product

  1. Configure a Google Cloud product configuration, such as " Cloud Scheduler, call me every minute".
  2. Set up an HTTP request.
  3. Specify that requests should go over private networking, such as through `sd-1`.
  4. Optional: [Configure Certificate Authority Service settings](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities).



The Google Cloud product can now invoke the HTTP request by using `sd-1`.

### Call an HTTP endpoint when a Shared VPC network, a VM, and Service Directory are in different projects

In this use case, you set up Dialogflow CX, a Google Cloud service for natural language processing, to call an HTTP endpoint on your VM. While calling the endpoint, ensure that the traffic doesn't transition over the public internet.

In this use case, you create the following artifacts in different projects:

  * A Shared VPC network
  * A VM
  * A Service Directory service
  * Dialogflow CX



Before you create the projects, note the following:

  * Ensure that the API invocation respects the VPC Service Controls perimeter.
  * Ensure that the configuration of the Google Cloud service project allows egress to a VM that resides in the VPC network project.
  * The producer project might not be the same as the Google Cloud service project.
  * Ensure that the VPC Service Controls perimeters of both projects are used.
  * The Service Directory project and the network project don't need to be connected, but they must both be part of the same VPC Service Controls.
  * In the network and the service, the firewall and IAM are disabled by default.



Figure 2 shows how you can send traffic by using private network access with VPC Service Controls perimeters enforced.

[ ![Send traffic by using private network access with VPC Service Controls
         perimeters enforced.](https://docs.cloud.google.com/static/service-directory/images/traffic_using_pna_with_perimeters_enforced.svg)](https://docs.cloud.google.com/static/service-directory/images/traffic_using_pna_with_perimeters_enforced.svg) **Figure 2.** Send traffic by using private network access with VPC Service Controls perimeters enforced (click to enlarge).

#### Configure the network project

  1. [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), such as `my-vpc-project`.
  2. [Create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks), such as `vpc-1`.

While creating the VPC network, for **Subnet creation mode** , select **Automatic**.

  3. [Create a firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules), such as `firewall-1`.

While creating the rule, enter or select the following values:

     * For **Network** , select `vpc-1`.
     * For **Source IPv4 ranges** , enter `35.199.192.0/19`.
     * For **Protocols and ports** , select **TCP** and enter `443` or `80`.
  4. In the `us-central1` region, [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), such as `vm-1`.

While creating the VM, enter or select the following values:

     * For **Networking > Network Interfaces**, select `vpc-1`.
     * For **Firewall** , select **Allow HTTP traffic**.

If you want to use HTTPS, select **Allow HTTPS traffic**. Also make sure that you install a Public Key Infrastructure (PKI) Transport Layer Security (TLS) certificate.




If you're using VPC Service Controls, the VPC Service Controls perimeter enables Service Directory to connect to both the Google Cloud service project and the Service Directory project.

**Notes:**

  * For `servicedirectory.googleapis.com`, the Google Cloud service project must be within the VPC Service Controls perimeter of the Google Cloud service project and the Service Directory project.
  * For `servicedirectory.googleapis.com`, the Google Cloud service project must be within the VPC Service Controls perimeter of the Google Cloud service project and the network project.
  * VPC Service Controls is enabled by default.



#### Configure the Service Directory project

  1. [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects), such as `my-sd-project`.

  2. You require an extra IAM permission because the VPC network project and the Service Directory project are different projects.

From the network project, grant the Service Directory Network Attacher role (`roles/servicedirectory.networkAttacher`) to the IAM principal that creates the Service Directory endpoint.

  3. Create a Service Directory endpoint that points to the VM in the VPC network:

     1. In the `us-central1` region, create a namespace, such as `namespace-1`.
     2. In the namespace, register a Service Directory service, such as `sd-1`.
     3. Create an endpoint in `sd-1`. For the endpoint address, use the internal IP address of `vm-1` on port `443`. For more information, see Create an endpoint with private network access.
  4. Grant the following IAM roles to the service agent of the Google Cloud product that will call the endpoint:

     * Service Directory Viewer role (`roles/servicedirectory.viewer`) in the Service Directory project
     * Private Service Connect Authorized Service role (`roles/servicedirectory.pscAuthorizedService`) in the network project



If you're using VPC Service Controls, the VPC Service Controls perimeter enables Service Directory to connect to both the Google Cloud service project and the Service Directory project.

#### Configure the Google Cloud service project

  1. [Enable the API](https://docs.cloud.google.com/apis/docs/getting-started#enabling-apis) for the Google Cloud service that you're using, if it's not already enabled.
  2. To configure the Google Cloud service `PUSH`, use the Service Directory service from the Service Directory project.



If you're using VPC Service Controls, the VPC Service Controls perimeter enables Service Directory to connect to both the network project and the Service Directory project.

## Use Service Directory private network access with Dialogflow

For instructions about how you can use Service Directory private network access with Dialogflow, see [Using Service Directory for private network access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd).

## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To learn more about Private Service Connect, see [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * To find solutions for common issues that you might experience when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
