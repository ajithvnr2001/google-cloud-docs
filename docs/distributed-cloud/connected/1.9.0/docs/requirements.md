---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/requirements/
title: Installation requirements \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:30:43.980812+00:00
---

# Installation requirements  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/requirements/

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
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/overview)



Send feedback 

#  Installation requirements Stay organized with collections  Save and categorize content based on your preferences. 

Before you order Google Distributed Cloud connected hardware, you must meet the Distributed Cloud connected installation requirements described on this page.

## Plan the hardware configuration

Before you can order hardware, your network administrator must work with Google to plan the hardware configuration for the Distributed Cloud connected installation.

Based on your business requirements, your network administrator must determine and provide the following information:

  * Number of units (racks or servers) of each form factor
  * Number and types of machines in each rack, if applicable
  * Power supply requirements



You must select and order all of the Distributed Cloud connected hardware for each Distributed Cloud connected zone at the same time. You cannot add or remove hardware from a zone after that hardware has been deployed.

Distributed Cloud connected ships in one of the following variants:

| GDC connected rack (base or expansion) | GDC connected server (medium) | GDC connected server (large)  
---|---|---|---  
**Configuration** | Three to twelve nodes with local SSD storage, two ToR switches, aggregator switch (base rack only) | One or three standalone servers with local SSD storage | One or three standalone servers with local SSD storage  
**Purpose** | Ideal for large-scale network-intensive computing | Ideal for medium-scale general-purpose computing | Ideal for large-scale general-purpose computing  
**Estimated cost** | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing) | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing) | [Pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing)  
**CPU** | 3 to 12 x 128 vCPUs (384 to 1546 vCPUs total) | 1 or 3 x 32 vCPUs (32 or 96 vCPUs total) | 1 or 3 x 64 vCPUs (32 or 192 vCPUs total)  
**GPU** | Not supported | 1 or 3 x NVIDIA L4 GPU (optional) | 1 or 3 x NVIDIA L4 GPU (optional)  
**RAM** | 3 to 12 x 512 GB (1536 GB to 6144 GB total) | 1 or 3 x 64 GB (64 GB or 192 GB total) | 1 or 3 x 128 GB (128 GB or 384 GB total)  
**Storage** | 3 to 12 x 3.2 TB SSD (9.6 TB to 38.4 TB total) | 1 or 3 x 1.6 TB SSD (1.6 TB or 4.8 TB total) | 1 or 3 x 3.2 TB SSD (3.2 TB or 9.6 TB total)  
**Power** | AC only | AC only | AC only  
  
### Configure a Distributed Cloud connected rack deployment

A Distributed Cloud connected rack deployment consists of a pair of base racks, which form the core of the deployment, and up to three optional expansion racks, for a total of five racks per Distributed Cloud connected zone. For each cluster, you can only assign nodes from that cluster's zone. You cannot assign nodes from multiple zones to the same cluster.

Distributed Cloud connected racks can hold up to twelve machines, installed in blocks of three. Each machine block populates one of the four available machine block slots in the rack. Each rack must have at least one machine block slot populated with a compute machine block to operate. The fifth machine slot is reserved for Google use. You cannot add or remove machine blocks or individual machines after a Distributed Cloud connected rack has been deployed on your premises.

As of this release of Distributed Cloud connected, the only machine type available is the network-optimized compute machine.

### Configure a Distributed Cloud connected server deployment

By default, you can only order Distributed Cloud connected servers in a three-machine configuration. If your business requirements call for single-machine deployments of Distributed Cloud connected servers, contact your Google field sales representative for more information.

## Choose the procurement model

You can order the Distributed Cloud connected server hardware in one of the following ways, based on your business requirements:

  * **Google-sourced hardware.** You can order the Distributed Cloud connected hardware directly from Google. This ownership model is available for server and rack hardware and is available in all countries where Distributed Cloud connected is sold. In this scenario:

    * You lease the Distributed Cloud connected hardware from Google.
    * Google sources, owns, maintains, repairs, and decommissions the Distributed Cloud connected hardware.
    * Google deploys, maintains, and troubleshoots the Distributed Cloud connected software.
    * When your contract concludes, Google collects the Distributed Cloud hardware and destroys all data stored on it.
  * **Customer-sourced hardware.** You can order Distributed Cloud connected hardware from a Google-certified Systems Integrator (SI) after consulting with Google on a deployment configuration that fits your business requirements. This ownership model is only available for Distributed Cloud connected server hardware and might not be available in every country in which Distributed Cloud connected is available. In this scenario:

    * You own the Distributed Cloud connected hardware and are responsible for meeting the tax and regulatory requirements of the locality in which you want to deploy it.
    * The SI works with you and Google to deploy, repair, and decommission the hardware.
    * Google works with you directly to deploy, maintain, and troubleshoot the Distributed Cloud connected software.
    * When your contract concludes, the SI wipes all Google software and your data from the Distributed Cloud connected hardware. You are then free to reuse or dispose of the hardware.
    * For more information on sourcing your own hardware, including availability in your country, contact your Google field sales representative.



## Purchase Premium Support

Distributed Cloud connected requires [Premium Support](https://docs.cloud.google.com/support/docs/premium). If you're not currently a Premium Support customer, you must purchase Premium Support to use Distributed Cloud connected.

## Provide Google Cloud information

When you order the hardware, you must provide the following information to Google, if applicable:

  * Your Google Cloud organization ID
  * Whether you want Google to provision your Distributed Cloud connected machines as part of an existing Google Cloud project or if you want a new Google Cloud project
  * The ID of the target Google Cloud project (if you're provisioning as part of an existing Google Cloud project)
  * The desired number of Distributed Cloud connected zones



## Delivery path and installation site

To verify that your delivery path and installation site can accommodate the Distributed Cloud rack hardware, Google or a Google-certified SI might ask you for photographs and drawings that accurately depict both, or they might perform a pre-delivery survey of your site.

The delivery path must be free from obstructions and have a grade below 3%. If the installation site is not on the same floor as your loading dock or building entrance, then you must provide access to an elevator.

All doorways, hallways, and elevators must support the gross weight and dimensions of the crated Distributed Cloud rack hardware.

You must provide Google service technicians access throughout the delivery path up to and including the installation site.

If your installation site is not a typical data center, you must provide dimensional drawings of the installation site before you order hardware to ensure that the rack can be safely installed and powered up.

Distributed Cloud servers are standard rack-mount form factor and do not require special delivery provisions.

## Space needed

The Distributed Cloud connected rack hardware comes in a crate with the following dimensions.

Dimension | Value (imperial) | Value (metric)  
---|---|---  
**Height** | 87 inches | 221 cm  
**Depth** | 60 inches | 152 cm  
**Width** | 40 inches | 102 cm  
  
The Distributed Cloud connected rack hardware has the following dimensions.

Dimension | Value (imperial) | Value (metric)  
---|---|---  
**Height** | 80 inches | 203 cm  
**Depth** | 48 inches | 122 cm  
**Width** | 24 inches | 61 cm  
  
If your local jurisdiction or facility requires that you brace the Distributed Cloud rack, you might need special seismic bracing hardware. The Distributed Cloud rack ships anchored to its crate with brackets that you can re-use to attach the rack to your floor. However, these brackets might not meet your local bracing requirements.

The Distributed Cloud connected server hardware has the following dimensions per machine:

Dimension | Value (imperial) | Value (metric)  
---|---|---  
**Height** | 1.7 inches | 4.3 cm  
**Depth** | 19 inches | 48 cm  
**Width** | 19 inches | 48 cm  
  
## Weight

The gross weight of the Distributed Cloud connected rack is as follows.

Rack fill | Gross weight  
---|---  
**Typical** | 900 lbs (408 kg)  
**Maximum** | 1300 lbs (590 kg)  
  
The delivery path, including any elevators, and the installation site must safely support this weight while in full compliance with local building codes.

The weight of each Distributed Cloud connected server machine is 20 lbs (9 kg).

## Power supply

The Distributed Cloud connected hardware requires single-phase or three-phase alternating current power at 50Hz or 60Hz. You must specify the required power supply type when you order the hardware.

You must supply power to the installation site in accordance with your local building codes, including the following work:

  * Installing cabling conduits
  * Running the required cabling
  * Connecting the cabling to your electrical panel
  * Turning on the power



All electrical work must be performed by a certified electrician.

### Line specifications

You must supply the following number of independent power lines to ensure high availability, based on the variant that you want to deploy.

Variant | Line requirement  
---|---  
**AC power (rack)** | Two (2) independent power lines with a dedicated ground connection  
**AC power (server)** | One (1) independent power supply line with a dedicated ground connection per machine.  
  
All power receptacles must be located at most 6 feet (1.8 meters) from the installation site.

### Power specifications for Distributed Cloud racks

For AC power supplied to Distributed Cloud connected racks, all power supply lines must meet _one_ of the following specifications.

Phase | Voltage | Amperage | Connector  
---|---|---|---  
**Single-phase** | 208V, 50/60Hz | 30A | NEMA L6-30P  
**Single-phase** | 230V, 50/60Hz | 32A | IEC 60309 2P+2E 6Hr  
**Three-phase Wye** | 120V/208V, 50/60Hz | 30A | NEMA L21-30P  
**Three-phase Delta** | 208V, 50/60Hz | 60A | IEC 60309 3P+G 9Hr  
**Three-phase Delta** | 208V, 50/60Hz | 50A | CS8365 50A 3P+G  
**Three-phase Wye** | 240V/410V, 50/60Hz | 16A | IEC 60309 3P+N+PE 6Hr  
**Three-phase Wye** | 230V/400V, 50/60Hz | 32A | IEC 60309 3P+N+PE 6Hr  
  
### Power specifications for Distributed Cloud connected servers

For AC power supplied to each Distributed Cloud connected server machine, all power supply lines must be capable of supplying between 100V and 240V at 50 or 60Hz of single-phase power per Distributed Cloud connected server machine. The Distributed Cloud connected server machine power supplies are auto-switching.

### Power draw

The power draw of a Distributed Cloud connected rack ranges between 6,000W and 20,000W based on the selected configuration, presence of GPUs, CPU load, and other factors.

The power draw of a Distributed Cloud connected server machine ranges between 200W and 800W based on the selected configuration, CPU load, and other factors.

### Backup power

For either variant, each of the independent power lines must have an independent uninterruptible power supply (UPS) capable of powering the Distributed Cloud hardware continuously for a minimum of 20 minutes for battery systems and 15 seconds for inertial systems.

In addition to UPS backup, you must also provide emergency electrical generator backup of sufficient capacity to both charge the UPS units and power the Distributed Cloud hardware for a minimum of four hours. The Distributed Cloud hardware must be connected to the UPS units. The UPS units must then connect to the generator backup by using an automatic transfer switch (ATS) or similar system that does not require human intervention to facilitate an emergency transfer.

Battery UPS systems without generator backup, such as older DC plants, must have sufficient capacity to power Distributed Cloud hardware for a minimum of four hours.

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

A Distributed Cloud connected rack produces up to 27,000 BTUs of heat per hour and uses forced air to remove the heat from the installed hardware. The front of the rack acts as a cold air intake, and the back of the rack acts as a hot air exhaust. You must provide 4 feet (1.2 meters) of open space at both the front and the back of the rack to allow for sufficient airflow. If possible, install the rack in front of a dedicated perforated tile or register.

A Distributed Cloud connected server typically produces about 3,000 BTUs of heat per hour and also uses forced air to remove heat from its chassis. Google strongly recommends that you follow best practices similar to those described above to ensure proper cooling of your Distributed Cloud connected server machines.

Distributed Cloud hardware requires that air at your deployment site be continuously circulated, conditioned, and filtered by using permanently installed commercial or industrial-grade HVAC equipment. Failure to maintain the required environmental conditions could result in long-term damage to Distributed Cloud hardware and a reduced reliability of your Distributed Cloud deployment.

Your cooling infrastructure must meet the following guidelines:

  * All HVAC equipment must have backup power and the capability to automatically restart after power loss.
  * Air handlers, conditioning equipment, condensers, pumps, cooling towers, chillers, and other HVAC components must have appropriate redundancy.
  * You must regularly inspect and maintain your HVAC equipment to keep its operating performance consistent and within the required ranges.
  * You must not expose the Distributed Cloud hardware to direct sunlight or any other type of infrared radiation because this alters the validated temperature profile of the hardware.
  * You must not expose the Distributed Cloud hardware to unconditioned, unfiltered air. Even brief exposure can cause dust buildup and restrict airflow to critical components.
  * A fresh-air cooling system is acceptable if it is professionally engineered and installed. However, it must meet the thermal requirements listed previously.



## Networking

A Distributed Cloud connected rack requires four LC single-mode fiber connections split between two redundant network devices on your local network. Supported connection types are 10GBASE-LR, 25GBASE-LR, 40GBASE-LR4, and 100GBASE-LR4.

A Distributed Cloud connected server machine requires, at a minimum, two gigabit Ethernet connections to your Top-of-Rack (ToR) switch, one in-band, and one out-of-band. Google recommends two in-band connections per machine for redundancy.

You must specify your network requirements, such as IP address ranges and firewall configuration, when you order Distributed Cloud connected hardware. For optical transport circuits, enable fault propagation for optimal routing protocol convergence.

Before you order, your network administrator must work with Google to plan the network configuration for the Distributed Cloud connected installation.

For more information, see [Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/how-it-works#hardware).

### Workload network traffic tagging

Distributed Cloud connected supports tagging workload traffic between your local network and workload Pods that use the `kube0` network interface:

  * **Distributed Cloud connected racks** tag workload traffic on the `kube0` interface with VLAN ID of `2`. This value cannot be changed.

  * **Distributed Cloud connected servers** do not tag workload traffic on the `kube0` interface by default. However, when ordering your Distributed Cloud connected servers hardware, you can request that the workload traffic on the `kube0` interface is tagged with a VLAN ID of your choice. You cannot enable this feature after your Distributed Cloud connected server deployment has been put into service.




### Internet connection bandwidth

Distributed Cloud connected requires the following minimum bandwidth for its connection to the internet:

  * **Downstream:** 100 megabits per second
  * **Upstream:** 30 megabits per second



### Allocate address blocks

Distributed Cloud connected requires that you allocate the following address blocks on your local network. If you are using private IP addresses for the Distributed Cloud connected management subnetworks listed in this section, you must configure Network Address Translation (NAT) for those addresses before advertising your deployment's public IP addresses to the internet. traffic

#### Address blocks for Distributed Cloud connected racks

The following table describes the required address blocks for Distributed Cloud connected racks:

Network component | Allocation requirement  
---|---  
Peering link to your local network | Four public or private /31 CIDR blocks. You can provide four /31 CIDR blocks, a VLAN ID, and two BGP ASNs that cover these four address blocks. One ASN is for your local routers that peer with Distributed Cloud connected ToR switches, and one ASN is for the Distributed Cloud switches.  
ToR switch management subnetwork | At least one /30 CIDR block, either public or RFC 1918.  
Distributed Cloud connected machine management subnetwork | At least one /27 CIDR block, either public or RFC 1918.  
Distributed Cloud connected nodes subnetwork | At least one /27 CIDR block, either public or RFC 1918.  
  
#### Address blocks for Distributed Cloud Servers

The following table describes the required address blocks for Distributed Cloud connected servers:

Network component | Allocation requirement  
---|---  
Distributed Cloud connected machine management subnetwork | One (1) IP address per machine in your local network VLAN, either public or RFC 1918.  
Distributed Cloud connected nodes subnetwork | One (1) IP address per machine in your local network VLAN, either public or RFC 1918.  
Distributed Cloud connected load balancer pool | Six (6) IP address per machine in your local network VLAN, either public or RFC 1918.  
  
The IP addresses for the machine management and node subnetworks must be contiguous. You must also provide the IP address of your default gateway, and the subnet mask of your local network.

#### How to allocate the required address blocks

When you order Distributed Cloud connected hardware, your network administrator must provide the preceding CIDR block allocation information. These values cannot be changed after Distributed Cloud connected is deployed.

Node, machine management, and ToR switch CIDR blocks must be routable subnetworks on your local network. They can be private RFC 1918-range subnetworks or public networks. You must configure the appropriate BGP sessions on your peering edge routers to accept routes for the Distributed Cloud connected nodes subnetwork, the Distributed Cloud connected machine management subnetwork, and the lower two /32 IP addresses of the ToR switch management subnetwork.

The CIDR blocks are allocated per Distributed Cloud connected rack. When you create a Distributed Cloud connected cluster, Distributed Cloud connected automatically assigns nodes within that cluster to IP addresses within the specified node CIDR block based on their capabilities and availability.

In a multi-rack Distributed Cloud connected installation, you must specify unique CIDR blocks for each Distributed Cloud connected rack. Each rack is connected to your network separately.

If you plan to expand your Distributed Cloud connected installation with additional machines, you must account for the additional IP addresses that this requires in your initial Distributed Cloud connected order. You must also account for overhead IP addresses, such as gateway addresses and floating addresses used by VPN connections between your workloads and Google Cloud. Work with your Google Cloud sales representative to determine the optimum node CIDR block allocations based on your business requirements.

When your Distributed Cloud connected installation is up and running, you also need to allocate network IP addresses for your Distributed Cloud connected Pods and Services as described in [Distributed Cloud connected Pod and Service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/address-allocation).

### Configure firewalls

If your local network uses a firewall, Distributed Cloud connected requires that you configure your firewall to allow the following types of network traffic:

  * Distributed Cloud connected management and monitoring traffic
  * Distributed Cloud connected workload traffic



#### Distributed Cloud connected management and monitoring traffic

Distributed Cloud connected requires that you open the following ports on your local network. Distributed Cloud connected requires these ports for outbound connections to Google over the internet for management and monitoring traffic. You must use a stateful firewall that tracks this outbound traffic and allows the corresponding returning inbound traffic through to Distributed Cloud connected.

Function | Originating subnetwork | Protocol | Ports  
---|---|---|---  
Domain Name System (DNS) | ToR switch management, Distributed Cloud connected machine management, Distributed Cloud connected nodes | TCP, UDP | 53  
Network Time Protocol (NTP) | ToR switch management, Distributed Cloud connected machine management, Distributed Cloud connected nodes | UDP | 123  
Terminal Access Controller Access Control System (TACACS) for switch authentication | ToR switch management | TCP | 3535  
Management VPN | ToR switch management, Distributed Cloud connected machine management | TCP, UDP | 443  
Bootstrap and Management API | ToR switch management, Distributed Cloud connected machine management | TCP, UDP | 443  
Monitoring service | Distributed Cloud connected machine management, Distributed Cloud connected nodes | TCP, UDP | 443  
Logging service | Distributed Cloud connected machine management, Distributed Cloud connected nodes | TCP, UDP | 443  
Cloud VPN and Virtual Private Cloud data plane | Distributed Cloud connected nodes | UDP (ESP, IKE) | 500, 4500  
  
#### Distributed Cloud connected workload traffic

Your network administrator must also configure additional firewall rules to allow traffic to and from the workloads deployed on your Distributed Cloud connected clusters.

If you deploy Distributed Cloud connected behind a NAT gateway, and you have additional firewall rules configured on your WAN gateways that filter or block inbound UDP traffic, the Cloud VPN connectivity required by Distributed Cloud connected might be affected. In such cases, you must allow inbound Cloud VPN UDP traffic from the Cloud VPN IP address ranges.

For example, you need to allow inbound UDP traffic from the source IP address ranges `35.242.0.0/17`, `35.220.0.0/17`, and `34.157.0.0/16` with the source port matching `500` or `4500` (IKE/ESP). If your firewall solution requires a more exact configuration, set the destination IP address range to match the IP address range of the Distributed Cloud connected nodes subnetwork. If your firewall is upstream of your NAT gateway, set the destination IP address range to the NAT gateway's public IP address.

### Validate your connectivity before ordering Distributed Cloud connected

Google provides a network connectivity validation tool for Distributed Cloud connected. This tool allows you to verify whether your local network is properly configured to support a Distributed Cloud connected deployment, including:

  * DNS configuration
  * NTP configuration
  * Switch management connectivity
  * Google API endpoint connectivity
  * VPN connectivity



You can download the tool from the following locations:

  * [Download for Windows](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/release/alpha/siteDiscovery.exe)
  * [Download for Linux](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/release/alpha/siteDiscovery)
  * [Download the playbook file (required)](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/playbook.yaml)



You can also view the tool's [source code](https://github.com/GDC-ConsumerEdge/site-discovery).

To run the tool, execute the respective binary. The tool generates a report file and a log file. Send these files with your Google field sales representative to complete the network validation.

## On-site maintenance

Google remotely monitors the Distributed Cloud connected hardware. If you encounter an issue, contact [Support](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/support) to file a ticket. If Google detects a hardware failure, we will do one of the following:

  * For Google-owned Distributed Cloud hardware, we will schedule a visit to your installation site. A Google-certified technician works with you to coordinate the visit and make the required repairs.
  * For customer-owned Distributed Cloud hardware, we will notify you and the Google-certified SI who delivered your Distributed Cloud connected hardware. You must work with the SI to coordinate a technician visit and make the required repairs.



## What's next

  * [Order Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/order)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
