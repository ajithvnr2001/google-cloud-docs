---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways/
title: VPN gateways \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:40.506555+00:00
---

# VPN gateways  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VPN gateways

VPN gateways provide secure connectivity between multiple sites, such as on-premises data centers, Google Cloud Virtual Private Cloud (VPC) networks, and Google Cloud VMware Engine private clouds. Traffic is encrypted because the VPN connections traverse the internet. Each VPN gateway can support multiple connections. When you create multiple connections to the same VPN gateway, all VPN tunnels share the available gateway bandwidth.

VMware Engine supports VPN connectivity by using the following types of gateways:

  * **Point-to-site VPN gateways:** for point-to-site connections, like connecting from your computer to your private cloud
  * **[Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect):** for site-to-site connections, like establishing a connection between your on-premises network and your private cloud



For more details about Cloud VPN and Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

## Point-to-site VPN gateways

A point-to-site VPN gateway sends encrypted traffic between a VMware Engine network and a client computer. You can use a VPN gateway to access your private cloud network, including your private cloud vCenter and workload VMs. To connect to your private cloud after you set up your VPN gateway, see [Connecting using VPN](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpn-connect).

To set up a point-to-site VPN gateway, first choose a marketplace vendor solution. You can deploy marketplace VPN gateway solutions as VMs on a VPC network connected to your private cloud. Alternatively, you can deploy VPN gateway VMs in VMware Engine, then expose and secure them using the VMware Engine public IP service and external firewall rules.

After you set up the VPN gateway, extend the encryption domain to include both the management and NSX subnets in your private cloud. If preferred, you can summarize or group subnets when setting up your encryption domain.

To get a list of the subnets to add to your encryption domain, do the following:

  1. [Access the Google Cloud console](https://console.cloud.google.com/vmwareengine).
  2. From the main menu, go to **Subnets**.
  3. From the **Subnet** column, copy the IP address ranges that you want to get access to remotely.



### Example: OpenVPN Access Server

For example, [OpenVPN Access Server](https://openvpn.net/vpn-server-resources/google-cloud-platform-byol-instance-quick-launch-guide/) is a marketplace solution for a VPN gateway. After you activate the appliance, you deploy a host VM for the gateway that allows transit to VMware Engine networks.

To access the encryption domain settings in the OpenVPN Access Server administrator panel, go to **Configuration > VPN Settings > Routing**. Then, enter a list of your subnet IP address ranges in the field labeled "Specify the private subnets to which all clients should be given access".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
