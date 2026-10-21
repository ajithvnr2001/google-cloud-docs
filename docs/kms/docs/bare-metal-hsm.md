---
url: https://docs.cloud.google.com/kms/docs/bare-metal-hsm/
title: Bare Metal HSM \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:15:02.732640+00:00
---

# Bare Metal HSM  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/bare-metal-hsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)



Send feedback 

#  Bare Metal HSM Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Bare Metal HSM solution.

## Overview

Bare Metal HSM is an infrastructure-as-a-service offering that lets you deploy customer-owned hardware security modules (HSMs) next to your Google Cloud workloads. Your HSMs are deployed in PCI-compliant facilities to meet your security, compliance, and low-latency requirements.

To support moving your workloads to the cloud, Google hosts your HSMs, providing physical and network security, rack and shelf space, power, and network integration for a monthly fee.

Bare Metal HSM lets you contract directly with Google for placement of your HSMs. HSMs are placed within specified colocation facilities and connect to Google Cloud.

The Bare Metal HSM solution is supported in colocation facilities with active peering fabrics. These facilities meet and exceed Google's standards for data center security and provide low-latency, highly available service.

### Comparison with Bare Metal Rack HSM

Both Bare Metal Rack HSM and Bare Metal HSM let you host your own HSMs in Google Cloud facilities. The primary difference between the Bare Metal Rack HSM and Bare Metal HSM solutions is scale. The following table summarizes the key differences between these solutions:

Bare Metal HSM | Bare Metal Rack HSM  
---|---  
Google hosts your HSMs on a _per-device basis_. | Google hosts your HSMs on a _per-rack basis_.  
You have logical access to your HSMs but _no physical access_.  | You have logical access to your HSMs and can schedule _escorted physical access_.  
Intended for small deployments of _10-15 HSMs_ | Intended for large rack-level deployments of _100 or more HSMs_  
  
If you're not sure which of these solutions is right for your needs, reach out to your account representative.

## Operational model

  * Onboarding process 
    * Contract: Minimum of 12 months. Premium Support is required.
    * Procurement and configuration: Your organization acquires, configures, and ships HSMs to Google.
    * Rack and stack and connect: Google deploys your HSMs and configures the Partner Interconnect connection.
    * Validation and handoff: Confirm the engineering solution and accessibility to the HSMs, test the solution, and sign off.
  * Support model 
    * Google provides support for rack and stack, hosting, smart hands, compliance, and Partner Interconnect connection.
    * Work with your HSM vendor for support for HSM software, licensing, tools, and troubleshooting.
  * Decommission process 
    * You file a request for decommissioning.
    * You must erase all data and initialize all HSM to factory default.



## Compliance requirements

This offering is limited to HSMs that are FIPS 140-2 Level 3 certified or better, and is not a generalized hosting or colocation service. The Bare Metal HSM solution is hosted in facilities that are fully compliant with PCI-DSS, PCI-3DS, and SOC 1, 2, and 3. Google will support your AOC for PCI-PIN, PCI-P2PE, and SOC compliance in all regions.

## Separation of responsibilities

It's your responsibility to obtain and provision HSMs and ship them to the appropriate Google Cloud regions. The HSMs used are your choice, but they must comply with the HSM equipment requirements.

Google pre-configures the racks, top-of-rack switches, and connectivity. The switches are from different vendors for each pair of racks. For the Bare Metal HSM solution, you have your own dedicated racks and switches. Google provides a racking service for your HSMs and works with you to validate the Partner Interconnect connection. Each rack has redundant power supplies.

### Accessing Bare Metal HSM

You have logical management access to your HSMs and are responsible for their maintenance and management. You maintain full control of your HSMs.

Google doesn't have logical access to your HSMs, but provides and maintains the racks, switching, and connection. Google has no access to the data or keys on your HSM.

You must deploy HSMs with complete remote management capability. You can't physically access your HSMs while they are in the colocation facility.

Google provides a remote hands service. Customer visits to the facility are not permitted. You are responsible for your own compliance and audit requirements.

At the end of your contract or the HSM's end of life, you submit a request to decommission the HSMs and erase all data or restore the HSMs to factory settings. After the HSMs are erased or reset and legal clearance is obtained, the HSMs will be shipped back to you or destroyed if they can't be shipped back.

## HSM equipment requirements

This section details the physical requirements for HSMs and associated cables for hosting HSMs in a Google facility.

The number of HSMs that may fit in a rack depends on the number of ports available in the current model of the top-of-rack switch, the number of rack units taken up the HSM model, and the power draw of the HSMs.

**Note:** You are provided with a rack that has 36 rack units available.

  * Power 
    * Dual AC power supplies (16A max per power supply).
  * Power distribution 
    * 208V line to line (for United States based locations).
    * Rack PDU providing C13 or C19 receptacles and outlets.
  * Power cables (to be provided by you) 
    * Rack PDU cable end should be C14 or C20 connector types.
    * 2 x 6 feet or 2 meter (preferred length) power cables.
  * Network 
    * Network interface controller: Dual 1g copper NICs (if applicable).
  * Network Cables (to be provided by you) 
    * 2 x 6 feet or 2 meter (preferred length) CAT-5e or better patch cables.
  * Physical dimensions 
    * Rack depth: 42 inches deep.
    * Rack unit spacing: Standard EIA-310 19" rack mount with square hole mounts. You can occupy up to 4 rack units per HSM.
  * Security 
    * The HSMs cannot be equipped with cameras or wireless networks such as Bluetooth.
    * The HSM must be FIPS 140-2 Level 3 certified or better.
  * The HSM must be fully remotely manageable.



There are no requirements for weight or cooling.

## Deployment overview

To qualify for a 99.99% uptime SLA, you must meet the following requirements:

  * Deploy HSMs in a minimum of two zones—either two different [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions) or, where available, two zones in the same region.
  * Deploy a minimum of two HSMs per zone (at least one HSM per rack in at least two racks).



You provide Google with the MAC address for each HSM network interface and its assigned IP address. This information helps Google verify server-to-top-of-rack cabling and aids troubleshooting during the deployment process.

**Note:** The HSM internal IP address allocations shouldn't overlap with IP addresses used in your on-premise network or in your Google Cloud project.

Network requirements will be discussed in more detail with your account representative during the onboarding process.

### Network topology

A pair of racks in a single zone is covered by a 99.9% SLA.

A full deployment across two zones provides a 99.99% SLA. This can be achieved using two regions or, where available, two zones in the same region.

Applications should be designed to take advantage of this redundancy model. An application should be able to fail over from zone 1 to zone 2 within a single location, from HSM to HSM.

Enabling the Global Routing feature lets HSMs at either location reach Google Cloud resources in any region.

A single Partner Interconnect connection failure isn't an SLA violation.

The following high-level diagram shows the required connectivity to achieve a 99.99% SLA on the service.

![Network topology for Bare Metal HSM](https://docs.cloud.google.com/static/kms/images/private_hsm_network.png)

  * Each zone deployment contains a minimum of two racks for your use, and one switch per rack.
  * The top-of-rack switches are provided by Google and are from different vendors.
  * Each top-of-rack switch has a 10G [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) with redundant VLAN attachments for Partner Interconnect to redundant Cloud Routers.
  * Each HSM should have a minimum of 2 1GE copper network interfaces with redundant connections to both top-of-rack switches. Both the management and data interfaces should have their own redundant connections to both top-of-rack switches.
  * You provide the IP address allocations for the HSM networks.
  * Top-of-rack switches advertise their locally attached subnets to the pair of Cloud Routers.
  * You enable global dynamic routing in your virtual private cloud (VPC) to allow access to the HSMs from any Google Cloud region where you've deployed resources. Global dynamic routing is also required to qualify for 99.99% availability.
  * BGP between the top-of-rack switches and the Cloud Routers in your project exchange reachability information to route between Google Cloud project resources and the HSMs.



### Networking requirements

You must complete the following steps for each set of racks in a zone to enable your HSMs to be hosted with Google:

  1. Create a redundant pair of Cloud Routers per zone using ASN16550. For detailed instructions, see [Creating Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-on-premises-network).

  2. Create two redundant pairs of [VLAN attachments with Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments) per zone using the Cloud Routers from the previous step. Create the attachments with the pre-activate option enabled. There should be a total of four attachments per zone. If the attachments were created without the pre-activation option enabled, you can [activate the connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) manually.

For more information about Partner Interconnect and pre-activation options, see [Partner Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

  3. Enable global dynamic routing in the VPC network.

     * To achieve 99.99% availability, use the steps in [Establishing 99.99% Availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability).
     * Deployments in a single zone have 99.9% availability until the second zone is available. For this case, see [Establishing 99.9% Availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability)
  4. Configure firewall rules as needed to allow traffic between your premises and project resources.




## Location compatibility

Bare Metal HSM is available in the following Cloud KMS locations:

Geographical area | Location name | Location description | Zones per region  
---|---|---|---  
Americas | `us-central1` | Iowa | 1  
Americas | `us-south1` | Dallas | 1  
Americas | `us-east4` | Northern Virginia | 1  
Americas | `us-west1` | Oregon | 1  
Europe | `europe-west4` | Netherlands | 1  
Europe | `europe-west3` | Frankfurt | 1  
Americas | `southamerica-west1` | Santiago | 1  
Americas | `southamerica-east1` | São Paulo | 1  
Asia-Pacific | `australia-southeast1` | Sydney | 2  
Asia-Pacific | `australia-southeast2` | Melbourne | 2  
Middle East | `me-west1` | Tel Aviv | 2  
  
**Note:** You can achieve a 99.99% SLA at a single region if the region contains two zones. 

## Contact Google

This product is only available for customers with specific business and technical requirements.

If you're interested in Bare Metal HSM with Google, reach out to your account representative for additional assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
