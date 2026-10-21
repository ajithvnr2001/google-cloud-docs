---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements/
title: Installation requirements \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:23:57.394596+00:00
---

# Installation requirements  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/requirements/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Installation requirements Stay organized with collections  Save and categorize content based on your preferences. 

Before you procure the Google Distributed Cloud connected hardware, you must meet the Distributed Cloud connected installation requirements described on this page.

## Plan the hardware configuration

Before you can procure the Google-certified hardware, your system administrator must work with Google to plan the hardware configuration for your Distributed Cloud connected deployment. Distributed Cloud connected hardware has been certified on the following platforms:

  * **Distributed Cloud connected servers G1.** A group of three Dell XR11 1U rackmount machines.

  * **Distributed Cloud connected servers G2.** A Dell XR8000r chassis populated with three XR8610t machine sleds.




You procure all of the Distributed Cloud connected hardware before you can provision each of your Distributed Cloud connected zones. You cannot add or remove hardware from a zone after that hardware has been deployed.

### Distributed Cloud connected servers G1 hardware

Google has certified the following Distributed Cloud connected servers G1 platform configurations:

| GDC connected servers G1 (medium) | GDC connected servers G1 (large)  
---|---|---  
**Configuration** | 3 rackmount Dell XR11 1U machines with local SSD storage | 3 rackmount Dell XR11 1U machines with local SSD storage  
**Purpose** | Ideal for medium-scale general-purpose computing | Ideal for large-scale general-purpose computing  
**CPU** | 32 vCPUs per machine | 64 vCPUs per machine  
**GPU** | 1 NVIDIA L4 GPU (optional) per machine | 1 NVIDIA L4 GPU (optional) per machine  
**RAM** | 64 GB per machine | 128 GB per machine  
**Storage** | 1.6 TB SSD per 1U machine | 3.2 TB SSD per 1U machine  
**Power** | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only  
  
### Distributed Cloud connected servers G2 hardware

Google has certified the following Distributed Cloud connected servers G2 platform configurations:

| GDC connected servers G2 (small 64GB) | GDC connected servers G2 (small 128GB) | GDC connected servers G2 (medium) | GDC connected servers G2 (large)  
---|---|---|---|---  
**Configuration** | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage | 3 Dell XR8610t sled machines in a Dell XR8000r chassis with local SSD storage  
**Purpose** | Ideal for small-scale general-purpose computing | Ideal for small-scale general-purpose computing that require extra memory | Ideal for medium-scale general-purpose computing | Ideal for large-scale general-purpose computing  
**CPU** | 32 vCPUs per machine | 32 vCPUs per machine | 48 vCPUs per machine | 64 vCPUs per machine  
**GPU** | Not supported | Not supported | Not supported | Not supported  
**RAM** | 64 GB per machine | 128 GB per machine | 128 GB per machine | 128 GB per machine  
**Storage** | 3.84 TB SSD per sled machine | 3.84 TB SSD per sled machine | 3.84 TB SSD per sled machine | 3.84 TB SSD per sled machine  
**Power** | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only | Dual 1400W (1800W in EU Lot 9 countries), AC only  
  
## Procure Distributed Cloud connected hardware

You must procure the Distributed Cloud connected certified hardware through a Google-certified systems integrator in one of the certified configurations listed on this page. Your responsibilities include, but are not limited to:

  * Meeting the space, power, cooling, and other installation requirements of the certified hardware.
  * Complying with all tax and regulatory requirements of the target locality.
  * Deploying, repairing, and decommissioning the certified hardware.
  * Sanitizing the disk drives in each certified machine at the conclusion of your contract.



For more information on sourcing Distributed Cloud connected hardware, including availability in your country, contact your Google field sales representative.

## Purchase the minimum required support

Distributed Cloud connected requires, at minimum, [Enhanced Support](https://docs.cloud.google.com/support/docs/enhanced). If you're not an Enhanced Support or a Premium Support customer, you must purchase at least Enhanced Support to use Distributed Cloud connected.

## Provide Google Cloud information

When you order Distributed Cloud connected, you must provide the following information to Google, if applicable:

  * Your Google Cloud organization ID,
  * Whether you're provisioning your Distributed Cloud connected hardware as part of an existing Google Cloud project or if you want a new Google Cloud project,
  * The ID of the target Google Cloud project (if you're provisioning as part of an existing Google Cloud project),
  * The target number of Distributed Cloud connected zones.



## Backup power

We highly recommend that you use independent uninterruptible power supplies (UPS) capable of powering the Distributed Cloud hardware continuously for a minimum of 20 minutes for battery systems and 15 seconds for inertial systems.

## Networking

A Distributed Cloud connected server machine requires, at a minimum, two gigabit Ethernet connections to your Top-of-Rack (ToR) switch, one in-band, and one out-of-band. Google recommends two in-band connections per machine for redundancy. For a three-node deployment, that is six connections per Distributed Cloud connected server chassis.

You must specify your network requirements, such as IP address ranges and firewall configuration, when you order Distributed Cloud connected.

Before you order, your network administrator must work with Google to plan the network configuration for the Distributed Cloud connected installation.

For more information, see [Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/how-it-works#hardware).

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

When you order Distributed Cloud connected, your network administrator must provide the preceding CIDR block allocation information. These values cannot be changed after Distributed Cloud connected is deployed.

Node and machine management CIDR blocks must be routable subnetworks on your local network. They can be private RFC 1918-range subnetworks or public networks. You must configure the appropriate BGP sessions on your peering edge routers to accept routes for the Distributed Cloud connected nodes subnetwork, and the Distributed Cloud connected machine management subnetwork.

The CIDR blocks are allocated per Distributed Cloud connected zone. When you create a Distributed Cloud connected cluster, Distributed Cloud connected automatically assigns nodes within that cluster to IP addresses within the specified node CIDR block based on their capabilities and availability.

In a multi-zone Distributed Cloud connected deployment, you must specify unique CIDR blocks for each Distributed Cloud connected zone. Each zone is connected to your network separately.

When your Distributed Cloud connected installation is up and running, you also need to allocate network IP addresses for your Distributed Cloud connected Pods and Services as described in [Distributed Cloud connected Pod and Service network address allocation](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/address-allocation).

### Configure firewalls

If your local network uses a firewall, Distributed Cloud connected requires that you configure your firewall to allow the following types of network traffic:

  * Distributed Cloud connected management and monitoring traffic
  * Distributed Cloud connected workload traffic



#### Distributed Cloud connected management and monitoring traffic

Distributed Cloud connected requires that you open the following ports on your local network. Distributed Cloud connected requires these ports for outbound connections to Google over the internet for management and monitoring traffic. You must use a stateful firewall that tracks this outbound traffic and allows the corresponding returning inbound traffic through to Distributed Cloud connected.

This connectivity is critical for Google to remotely monitor your deployment and alert you to any infrastructure issues. For details about what Google monitors, see [Shared responsibility](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/shared-responsibility) and the [Alerting strategy](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/monitoring#alerting-strategy).

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

### Validate your connectivity before ordering Distributed Cloud connected

Google provides a network connectivity validation tool for Distributed Cloud connected. This tool lets you verify whether your local network is properly configured to support a Distributed Cloud connected deployment, including:

  * DNS configuration
  * NTP configuration
  * Switch management connectivity
  * Google API endpoint connectivity
  * VPN connectivity



To validate your connectivity, download and run the network connectivity validation tool as follows:

  1. Go to the tool's [Releases page](https://github.com/GDC-ConsumerEdge/site-discovery/releases) on GitHub and download the version for your target platform:

     * For Windows, download the `siteDiscovery.exe` file.
     * For Linux, download the `siteDiscovery` file.
  2. Download the [`playbook.yaml`](https://github.com/GDC-ConsumerEdge/site-discovery/raw/refs/heads/main/playbook.yaml) file and place it in the directory where you downloaded the validation tool.

  3. From the command line, change into the directory containing the tool and the `playbook.yaml` file and run the tool as follows:

     * On Windows:
           
           siteDiscovery.exe
           

     * On Linux:
           
           chmod +x siteDiscovery
           ./siteDiscovery
           

  4. When the tool completes, it writes a report file to the directory from which it was run, then outputs a confirmation message similar to the following:
         
         Write report to /usr/local/google/home/myuseraccount/site-discovery-report_20260526-190033.txt ... Done
         

  5. View the report file. For example:
         
         cat /usr/local/google/home/myuseraccount/site-discovery-report_20260526-190033.txt
         




See the tool's [README](https://github.com/GDC-ConsumerEdge/site-discovery/blob/main/README.md) file for more information, such as runtime flags, running the tool using Python, or troubleshooting. You can also send the generated report file to your Google field sales representative for assistance. The tool's [source code](https://github.com/GDC-ConsumerEdge/site-discovery) is freely available for viewing.

## On-site maintenance

Google remotely monitors the Distributed Cloud connected hardware. If you encounter an issue, contact [Support](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/getting-support) to file a ticket. If Google detects a hardware failure, we will notify you and your service partner. You must work with your service partner to coordinate a technician visit and make the required repairs.

For Google-operated Distributed Cloud connected hardware, we will schedule a technician to visit your deployment site. A Google-provided technician works with you to coordinate the visit andmake the required repairs.

## What's next

  * [Order Distributed Cloud connected hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/order)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
