---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements/
title: Installation requirements \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:58.599235+00:00
---

# Installation requirements  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements/

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
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Installation requirements Stay organized with collections  Save and categorize content based on your preferences. 

Before you order Google Distributed Cloud connected hardware, you must meet the Distributed Cloud connected installation requirements described on this page.

## Plan the hardware configuration

Before you can order hardware, your network administrator must work with Google to plan the hardware configuration for the Distributed Cloud connected installation. Distributed Cloud connected servers hardware is available in the following form factors:

  * **Distributed Cloud connected servers G1.** A group of three Dell XR11 1U rackmount machines.

  * **Distributed Cloud connected servers G2.** A Dell XR8000r chassis populated with three XR8610t machine sleds.




Based on your business requirements, your network administrator must determine and provide the following information:

  * Number of units of each form factor
  * Hardware configuration for each unit



You must select and order all of the Distributed Cloud connected hardware for each Distributed Cloud connected zone at the same time. You cannot add or remove hardware from a zone after that hardware has been deployed.

### Distributed Cloud connected servers G1 hardware

Distributed Cloud connected servers G1 ship in one of the following variants:

| GDC connected servers G1 (medium) | GDC connected servers G1 (large)  
---|---|---  
**Configuration** | 3 rackmount Dell XR11 1U machines with local SSD storage | 3 rackmount Dell XR11 1U machines with local SSD storage  
**Purpose** | Ideal for medium-scale general-purpose computing | Ideal for large-scale general-purpose computing  
**Estimated cost** | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing) | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing)  
**CPU** | 32 vCPUs per machine | 64 vCPUs per machine  
**GPU** | 1 NVIDIA L4 GPU (optional) per machine | 1 NVIDIA L4 GPU (optional) per machine  
**RAM** | 64 GB per machine | 128 GB per machine  
**Storage** | 1.6 TB SSD per 1U machine | 3.2 TB SSD per 1U machine  
**Power** | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only  
**Machine SKU** | `gdccs-g1-32vcpu-64gb-1tb` | `gdccs-g1-64vcpu-128gb-3tb`  
  
### Distributed Cloud connected servers G2 hardware

Distributed Cloud connected servers G2 ship in one of the following variants:

| GDC connected servers G2 (small) | GDC connected servers G2 (medium) | GDC connected servers G2 (large)  
---|---|---|---  
**Configuration** | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage  
**Purpose** | Ideal for small-scale general-purpose computing | Ideal for medium-scale general-purpose computing | Ideal for large-scale general-purpose computing  
**Estimated cost** | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing) | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing) | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing)  
**CPU** | 32 vCPUs per machine | 32 vCPUs per machine | 64 vCPUs per machine  
**GPU** | Not supported | Not supported | Not supported  
**RAM** | 64 GB per machine | 128 GB per machine | 128 GB per machine  
**Storage** | 3.84 TB SSD per sled machine | 3.84 TB SSD per sled machine | 3.84 TB SSD per sled machine  
**Power** | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only  
**Machine SKU** | `GDCc-Server-B2i-8` | `GDCc-Server-B2i-11` | `GDCc-Server-B2i-9`  
  
## Choose the procurement model

You can order the Distributed Cloud connected server hardware in one of the following ways, based on your business requirements:

  * **Google-sourced hardware.** You can order the Distributed Cloud connected hardware directly from Google. In this scenario:

    * Google owns the Distributed Cloud connected hardware and delivers it to your premises.
    * Google sources, maintains, repairs, and decommissions the Distributed Cloud connected hardware.
    * Google deploys, maintains, and troubleshoots the Distributed Cloud connected software.
    * When your contract concludes, Google collects the Distributed Cloud hardware and destroys all data stored on it.
  * **Customer-sourced hardware.** You can order Distributed Cloud connected hardware from a Google-certified Systems Integrator (SI) after consulting with Google on a deployment configuration that fits your business requirements. In this scenario:

    * You own the Distributed Cloud connected hardware and are responsible for meeting the tax and regulatory requirements of the locality in which you want to deploy it.
    * The SI works with you and Google to deploy, repair, and decommission the hardware.
    * Google works with you directly to deploy, maintain, and troubleshoot the Distributed Cloud connected software.
    * When your contract concludes, the SI wipes all Google software and your data from the Distributed Cloud connected hardware. You are then free to reuse or dispose of the hardware.
    * For more information on sourcing your own hardware, including availability in your country, contact your Google field sales representative.



## Purchase the minimum required support

Distributed Cloud connected requires, at minimum, [Enhanced Support](https://docs.cloud.google.com/support/docs/enhanced). If you're not an Enhanced Support or a Premium Support customer, you must purchase at least Enhanced Support to use Distributed Cloud connected.

## Provide Google Cloud information

When you order the hardware, you must provide the following information to Google, if applicable:

  * Your Google Cloud organization ID,
  * Whether you want Google to provision your Distributed Cloud connected machines as part of an existing Google Cloud project or if you want a new Google Cloud project,
  * The ID of the target Google Cloud project (if you're provisioning as part of an existing Google Cloud project),
  * The target number of Distributed Cloud connected zones.



## Space needed

The Distributed Cloud connected servers G1 hardware has the following dimensions per machine:

Dimension | Value (imperial) | Value (metric)  
---|---|---  
**Height** | 1.7 inches | 43 mm  
**Depth** | 19 inches | 483 mm  
**Width** | 19 inches | 483 mm  
  
The Distributed Cloud connected servers G2 hardware has the following dimensions per chassis:

Dimension | Value (imperial) | Value (metric)  
---|---|---  
**Height** | 3.4 inches | 87 mm  
**Depth** | 17 inches | 430 mm  
**Width** | 19 inches | 483 mm  
  
## Weight

The weight of each Distributed Cloud connected servers G1 machine is 20 lbs (9 kg). The weight of a fully populated Distributed Cloud connected servers G2 chassis is 71 lbs (32 kg).

## Power supply

The Distributed Cloud connected hardware requires single-phase alternating current power at 50Hz or 60Hz. You must supply power to the installation site in accordance with your local building codes, including the following work:

  * Installing cabling conduits
  * Running the required cabling
  * Connecting the cabling to your electrical panel
  * Turning on the power



All electrical work must be performed by a certified electrician.

### Line specifications

You must supply two (2) independent power supply lines with dedicated ground connections per Distributed Cloud connected servers G1 machine or Distributed Cloud connected servers G2 chassis.

For AC power supplied to each Distributed Cloud connected servers G1 machine or G2 chassis, all power supply lines must be capable of supplying between 100V and 240V at 50 or 60Hz of single-phase power per Distributed Cloud connected server machine. The Distributed Cloud connected servers machine power supplies are auto-switching.

### Power draw

The power draw of a Distributed Cloud connected servers G1 machine ranges between 200W and 800W based on the selected configuration, CPU load, and other factors.

The power draw of a Distributed Cloud connected servers G2 chassis populated with three sled machines ranges between 450W and 900W based on the selected configuration, CPU load, and other factors.

### Backup power

Each of the independent power lines must have an independent uninterruptible power supply (UPS) capable of powering the Distributed Cloud hardware continuously for a minimum of 20 minutes for battery systems and 15 seconds for inertial systems.

In addition to UPS backup, you must also provide emergency electrical generator backup of sufficient capacity to both charge the UPS units and power the Distributed Cloud hardware for a minimum of four hours. The Distributed Cloud hardware must be connected to the UPS units. The UPS units must then connect to the generator backup by using an automatic transfer switch (ATS) or similar system that does not require human intervention to facilitate an emergency transfer. Battery UPS systems without generator backup must have sufficient capacity to power Distributed Cloud hardware for a minimum of four hours.

## Cooling

The Distributed Cloud connected hardware is air-cooled and requires a climate-controlled environment to operate. Your installation site must provide adequate cooling to keep the Distributed Cloud connected hardware operational.

Your installation site must provide the following ambient environment.

Environmental factor | Required range  
---|---  
**Temperature** | Between 59°F (15°C) and 89°F (31°C)  
**Relative humidity** | Between 30% and 70%, non-condensing  
  
The ambient temperature and relative humidity fluctuations must not be greater than the following:

  * Ambient temperature: +/- 9°F (5°C) per hour
  * Relative humidity: +/- 5% per hour



These guidelines apply to installations at altitudes below 10,000' MSL (3050m). For higher altitudes, consult an HVAC professional and your Google or Google-certified SI representative. Extreme swings outside of these recommended ranges can result in a protective shutdown and/or permanent damage to Distributed Cloud hardware.

Both Distributed Cloud connected servers G1 and G2 variants typically produce up to 3,000 BTUs of heat per hour and use forced air to expunge it. Google strongly recommends that you follow best practices similar to those described above to ensure proper cooling of your Distributed Cloud connected server machines.

Distributed Cloud hardware requires that air at your deployment site be continuously circulated, conditioned, and filtered by using permanently installed commercial or industrial-grade HVAC equipment. Failure to maintain the required environmental conditions could result in long-term damage to Distributed Cloud hardware and a reduced reliability of your Distributed Cloud connected deployment.

Your cooling infrastructure must meet the following guidelines:

  * All HVAC equipment must have backup power and the capability to automatically restart after power loss.
  * Air handlers, conditioning equipment, condensers, pumps, cooling towers, chillers, and other HVAC components must have appropriate redundancy.
  * You must regularly inspect and maintain your HVAC equipment to keep its operating performance consistent and within the required ranges.
  * You must not expose the Distributed Cloud hardware to direct sunlight or any other type of infrared radiation because this alters the validated temperature profile of the hardware.
  * You must not expose the Distributed Cloud hardware to unconditioned, unfiltered air. Even brief exposure can cause dust buildup and restrict airflow to critical components.
  * A fresh-air cooling system is acceptable if it is professionally engineered and installed. However, it must meet the thermal requirements listed previously.



## Networking

A Distributed Cloud connected server machine requires, at a minimum, two gigabit Ethernet connections to your Top-of-Rack (ToR) switch, one in-band, and one out-of-band. Google recommends two in-band connections per machine for redundancy. For a three-node deployment, that is six connections per Distributed Cloud connected server chassis.

You must specify your network requirements, such as IP address ranges and firewall configuration, when you order Distributed Cloud connected hardware. For optical transport circuits, enable fault propagation for optimal routing protocol convergence.

Before you order, your network administrator must work with Google to plan the network configuration for the Distributed Cloud connected installation.

For more information, see [Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/how-it-works#hardware).

### Workload network traffic tagging

Distributed Cloud connected supports tagging workload traffic between your local network and workload Pods that use the `kube0` network interface. However, this feature is not enabled by default unless specifically requested when ordering.

When ordering Distributed Cloud connected, you can request that the workload traffic on the `kube0` interface is tagged with a VLAN ID of your choice. You cannot enable this feature after your Distributed Cloud connected servers deployment has been put into service.

### Internet connection bandwidth

Distributed Cloud connected requires the following minimum bandwidth for its connection to the internet:

  * **Downstream:** 20 megabits per second (Mbps)
  * **Upstream:** 5 megabits per second (Mbps)



### Allocate address blocks

Distributed Cloud connected requires that you allocate the following address blocks on your local network. If you are using private IP addresses for the Distributed Cloud connected management subnetworks listed in this section, you must configure Network Address Translation (NAT) for those addresses before advertising your deployment's public IP addresses to the internet.

The following table describes the required address blocks for Distributed Cloud connected servers:

Network component | Allocation requirement  
---|---  
Distributed Cloud connected machine management subnetwork | One (1) IP address per machine in your local network VLAN, either public or RFC 1918.  
Distributed Cloud connected nodes subnetwork | One (1) IP address per machine in your local network VLAN, either public or RFC 1918.  
Distributed Cloud connected load balancer pool | Six (6) IP address per machine in your local network VLAN, either public or RFC 1918.  
  
The IP addresses for the machine management and node subnetworks must be contiguous. You must also provide the IP address of your default gateway, and the subnet mask of your local network.

#### How to allocate the required address blocks

When you order Distributed Cloud connected hardware, your network administrator must provide the preceding CIDR block allocation information. These values cannot be changed after Distributed Cloud connected is deployed.

Node and machine management CIDR blocks must be routable subnetworks on your local network. They can be private RFC 1918-range subnetworks or public networks. You must configure the appropriate BGP sessions on your peering edge routers to accept routes for the Distributed Cloud connected nodes subnetwork, and the Distributed Cloud connected machine management subnetwork.

The CIDR blocks are allocated per Distributed Cloud connected zone. When you create a Distributed Cloud connected cluster, Distributed Cloud connected automatically assigns nodes within that cluster to IP addresses within the specified node CIDR block based on their capabilities and availability.

In a multi-zone Distributed Cloud connected deployment, you must specify unique CIDR blocks for each Distributed Cloud connected zone. Each zone is connected to your network separately.

If you plan to expand your Distributed Cloud connected installation with additional machines, you must account for the additional IP addresses that this requires in your initial Distributed Cloud connected order. You must also account for overhead IP addresses, such as gateway addresses and floating addresses used by VPN connections between your workloads and Google Cloud. Work with your Google Cloud sales representative to determine the optimum node CIDR block allocations based on your business requirements.

When your Distributed Cloud connected installation is up and running, you also need to allocate network IP addresses for your Distributed Cloud connected Pods and Services as described in [Distributed Cloud connected Pod and Service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/address-allocation).

### Configure firewalls

If your local network uses a firewall, Distributed Cloud connected requires that you configure your firewall to allow the following types of network traffic:

  * Distributed Cloud connected management and monitoring traffic
  * Distributed Cloud connected workload traffic



#### Distributed Cloud connected management and monitoring traffic

Distributed Cloud connected requires that you open the following ports on your local network. Distributed Cloud connected requires these ports for outbound connections to Google over the internet for management and monitoring traffic. You must use a stateful firewall that tracks this outbound traffic and allows the corresponding returning inbound traffic through to Distributed Cloud connected.

Function | Originating subnetwork | Destination | Protocol | Ports  
---|---|---|---|---  
Domain Name System (DNS) | Distributed Cloud connected machine management, Distributed Cloud connected nodes | `8.8.8.8` (default) | TCP, UDP | 53  
Network Time Protocol (NTP) | Distributed Cloud connected machine management, Distributed Cloud connected nodes | `time.google.com`  
`time1.google.com`  
`time2.google.com`  
`time3.google.com`  
`time4.google.com` | UDP | 123  
Management VPN | Distributed Cloud connected machine management | `192.178.18.0/23` | TCP, UDP | 443  
Management software downloads | Distributed Cloud connected machine management | `storage.googleapis.com` | TCP, UDP | 443  
Bootstrap and Management API | Distributed Cloud connected machine management | `*.gdce.google.com  
*.gdce.googleapis.com  
cache-management-prod.google.com  
offnetmanagement-pa.googleapis.com  
accounts.google.com  
cloud.google.com` | TCP, UDP | 443  
Monitoring service | Distributed Cloud connected machine management, Distributed Cloud connected nodes | `*.gdce.googleapis.com` | TCP, UDP | 443  
Container downloads | Distributed Cloud connected nodes | `*.k8s.io  
*.gcr.io` | TCP, UDP | 443  
Logging service | Distributed Cloud connected machine management, Distributed Cloud connected nodes | `*.gdce.googleapis.com` | TCP, UDP | 443  
  
#### Distributed Cloud connected workload traffic

Your network administrator must also configure additional firewall rules to allow traffic to and from the workloads deployed on your Distributed Cloud connected clusters.

If you deploy Distributed Cloud connected behind a NAT gateway, and you have additional firewall rules configured on your WAN gateways that filter or block inbound UDP traffic, the Cloud VPN connectivity required by Distributed Cloud connected might be affected. In such cases, you must allow inbound Cloud VPN UDP traffic from the Cloud VPN IP address ranges.

For example, you need to allow inbound UDP traffic from the source IP address ranges `35.242.0.0/17`, `35.220.0.0/17`, and `34.157.0.0/16` with the source port matching `500` or `4500` (IKE/ESP). If your firewall solution requires a more exact configuration, set the destination IP address range to match the IP address range of the Distributed Cloud connected nodes subnetwork. If your firewall is upstream of your NAT gateway, set the destination IP address range to the NAT gateway's public IP address.

### Validate your connectivity before ordering Distributed Cloud connected

Google provides a network connectivity validation tool for Distributed Cloud connected. This tool lets you verify whether your local network is properly configured to support a Distributed Cloud connected deployment, including:

  * DNS configuration
  * NTP configuration
  * Switch management connectivity
  * Google API endpoint connectivity
  * VPN connectivity



You can download the tool from the following locations:

  * [Download for Windows](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/release/alpha/siteDiscovery.exe)
  * [Download for Linux](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/release/alpha/siteDiscovery)
  * [Download the playbook file (required)](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/playbook.yaml)



For information on how to run the tool and interpret its results, see its [README](https://github.com/GDC-ConsumerEdge/site-discovery/blob/main/README.md) file. The tool generates a report file and a log file. Send these files with your Google field sales representative to complete the validation.

You can also view the tool's [source code](https://github.com/GDC-ConsumerEdge/site-discovery).

## On-site maintenance

Google remotely monitors the Distributed Cloud connected hardware. If you encounter an issue, contact [Support](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/getting-support) to file a ticket. If Google detects a hardware failure, we will do one of the following:

  * For Google-owned Distributed Cloud hardware, we will schedule a visit to your installation site. A Google-certified technician works with you to coordinate the visit and make the required repairs.
  * For customer-owned Distributed Cloud hardware, we will notify you and the Google-certified SI who delivered your Distributed Cloud connected hardware. You must work with the SI to coordinate a technician visit and make the required repairs.



## What's next

  * [Order Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/order)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
