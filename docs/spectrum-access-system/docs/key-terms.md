---
url: https://docs.cloud.google.com/spectrum-access-system/docs/key-terms/
title: Key terms \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:27.223409+00:00
---

# Key terms  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Key terms Stay organized with collections  Save and categorize content based on your preferences. 

This page provides key terminology that applies to Spectrum Access System (SAS). Review these terms to better understand how SAS works and the concepts on which it is built.

Certified Professional Installer (CPI)
    The person who verifies the installation parameters of a CBSD and provides them to a SAS.
Citizens Broadband Radio Service (CBRS)
    A spectrum band from 3550 MHz to 3700 MHz that is available for shared use.
Citizens Broadband Radio Service Device (CBSD)
    A device that operates in the CBRS band after receiving authorization from a SAS, such as an eNodeB.
CBSD configuration
    A set of CBSD installation parameters. The SAS can have up to two configurations for the same CBSD, one set that is active and one set that is in draft, ready for CPI, or pending for registration. [Learn more about CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/portal#cbsd-config).
CBSD ID
    A unique identifier used by the SAS to identify a CBSD. It is composed of the CBSD's Federal Communications Commission (FCC) ID and a unique string derived from the device's serial number.
cohort
    A set of CBSDs in a network whose channel assignments are considered together to avoid interference issues.
Coordinated Periodic Activities among SASs (CPAS)
    The daily process where SASs exchange CBSD installation parameters to synchronize among themselves, recalibrate existing grants, and calculate new grants. This is to ensure that incumbents are protected and to recalculate the move list for Dynamic Protection Area (DPA) activity. CPAS is also called Iterative Allocation Process (IAP). [Learn more about CPAS](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).
customer account
    The highest organizational unit in the deployments list. Nodes and deployments exist within a customer account.
Customer Premises Equipment (CPE)
    Equipment that connects to a base station in a fixed wireless network configuration.
Distributed Antenna System (DAS)
    A network of spatially separated antenna nodes connected to a common source through a transport medium (cables) that provides wireless service within a geographic area or structure.
deployment
    A deployment contains every CBSD with the same user ID.
deployments list
    The list of all deployments where you can assign user permissions. Use the deployments list to navigate customer accounts, nodes, and deployments.
Domain Proxy (DP)
    A device that aggregates communications from multiple CBSDs to a single SAS. The DP also provides a translational capability for legacy radio equipment in the 3650 MHz to 3700 MHz band with a SAS to ensure compliance with [Part 96 regulations](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96).
Dynamic Protection Area (DPA)
    A geographic region where incumbents ([Tier 1 user](https://docs.cloud.google.com/spectrum-access-system/docs/pals)) get protection from PAL and GAA interference. The DPAs are dynamically activated and deactivated based on incumbent activity. The SAS suspends a set of grants so that the aggregate (PAL and GAA) is below the [NTIA-defined interference margins](https://www.ntia.doc.gov/fcc-filing/2015/ntia-letter-fcc-commercial-operations-3550-3650-mhz-band).
E-DPA
    

Short for ESC-controlled DPA, these DPAs are located along the coasts of all US states and territories and are protected in the 3550 MHz to 3650 MHz range.

  * **Where ESCs are deployed:** When incumbent activity is detected, grants that cause excess interference to the DPA are suspended, while those that cause minimal interference remain in their current state. When there is no incumbent activity, grants aren't affected.

  * **Where ESCs aren't deployed:** Grants that exceed the interference margin to E-DPAs are always suspended. [Learn about areas with limited CBRS spectrum](https://docs.cloud.google.com/spectrum-access-system/docs/locations#limited-spec).



Effective Isotropic Radiated Power (EIRP)
    

The hypothetical power that would have to be radiated by an isotropic antenna to give the same or equivalent signal strength as the actual source antenna in the direction of the antenna's highest gain.

Environmental Sensing Capability (ESC)
    

A device that monitors incumbent ([Tier 1 user](https://docs.cloud.google.com/spectrum-access-system/docs/pals)) activity along the coasts of US states and territories in the 3550 MHz to 3650 MHz range. When an ESC detects incumbent activity on a given channel, it informs the SAS to suspend PAL and GAA grants that collectively exceed the corresponding E-DPA interference margin on the impacted channels.

Federal Communications Commission (FCC)
    

The United States regulatory agency that defines national telecommunications rules. For more information, see [Part 96](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96).

FCC ID
    

The FCC ID is a unique string comprised of a grantee code followed by a product code. For [testing purposes](https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest), you can create your own FCC ID.

Frequency Reuse Group (FRG)
    

A group of CBSDs that can manage interference among each other if they use grants with the same frequency range. They don't have to use grants with the same frequency range. Also known as a Spectrum Reuse Group (SRG) in the Wireless Innovation Forum (WInnForum) and as an Interference Coordination Group (ICG) in CBRS Alliance.

General Authorized Access (GAA)
    

GAA is the tier where CBSD operates as licensed-by-rule. It's the third tier in a [3-tier](https://docs.cloud.google.com/spectrum-access-system/docs/pals) spectrum sharing framework.

GAA-only CBSD
    

A CBSD whose operator doesn't have a PAL in the area where it operates.

grant
    

The authorization provided by SAS to a CBSD (after a successful heartbeat exchange) to transmit by using specified operating parameters. The operating parameters are maximum EIRP and Channel. Grants are identified by a unique grant identifier. After the grant identifier is issued, the operating parameters are never changed. If new or modified operating parameters are required, then a new grant must be obtained.

grantee code
    

A three- or five-character alphanumeric string that represents the grantee or applicant. The three-character grantee codes always begin with a letter of the alphabet and do not contain the numbers one or zero. The five-character grantee codes always begin with a number and do not contain the numbers one or zero.

ground-based (GB)-DPA
    

The ground-based radar DPA protects ground-based radar sites from CBSD interference. These protection areas are always active, which means that CBSDs can only transmit nearby if the SAS determines that they won't exceed the DPA's interference margin.

**Note:** Use the heatmaps in the SAS Portal to verify how many channels are affected.
incumbent user
    

A federal entity authorized to operate on a primary basis in accordance with one of the following:

  * The table of frequency allocations ([section 96.11 FCC rules](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96/subpart-A/section-96.11))
  * A fixed satellite service operator


Manufacturer's Serial Number (MSN)
    

A unique number or code assigned to a device. The numbers are arranged in sequence and can be a combination of letters and numbers.

multistep registration
    

A process in which a CPI provides a set of parameters for CBSD installation to the SAS without sending that information through the CBSD itself. For example, the CPI might enter the information in the SAS's web UI (such as Google's SAS Portal) and then instruct the CBSD to send a registration request to the SAS.

National Radio Quiet Zone (NRQZ) Case ID
    

NRQZ was established by the FCC to minimize possible harmful interference to the National Radio Astronomy Observatory (NRAO). If a device is located within the [National Radio Quiet Zone (NRQZ)](https://greenbankobservatory.org/about/national-radio-quiet-zone/), coordination with the [NRQZ office](mailto:%20nrqz@gb.nrao.edu) must be confirmed before registration and operation. To confirm successful coordination, a CPI must provide the NRQZ Case ID obtained from the NRQZ office. Learn [how to operate CBSDs in the NRQZ](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-nrqz).

node
    

A node organizes deployments in a hierarchical structure under customer accounts in the SAS Portal, like folders that organize files. You can only create nodes in the [SAS Portal API](https://docs.cloud.google.com/spectrum-access-system/docs/apis).

Priority Access License (PAL)
    

A license to operate within the CBRS band on a priority access basis.

PAL Protection Area (PPA)
    

The geographic area within a PAL where only the entity that owns or leases the PAL-protected or PAL-qualified CBSDs can use a particular set of channels. A PPA is defined by a set of CBSDs and a boundary.

PAL-protected CBSD
    

A CBSD with only PAL grants, whose operator holds a PAL and is inside an active PPA.

PAL-qualified CBSD
    

A CBSD whose operator holds a PAL but doesn't have any PAL grants.

Partially PAL-protected
    

A CBSD with both PAL and GAA grants, whose operator holds a PAL and is inside an active PPA.

Passive DAS
    

A Distributed Antenna System of spatially separated TPs powered by an RU, in which there are only passive elements (such as feeders, splitters, or diplexers) between the RU and each of the TPs.

portal-controlled DPA (P-DPA)
    

A DPA that is only activated when an incumbent (Tier 1 user) manually submits a request for interference protection. The activation of a P-DPA can cause suspensions in the 3550 MHz to 3650 MHz range.

product code
    

The product code is the non-grantee code portion of the FCC ID. The product code can include hyphens or dashes.

Radio Unit (RU)
    

Also known as a Remote Radio Unit (RRU). A radio transceiver in wireless networks that connects to the Baseband Unit (BBU) of a base station.

    

The RU contains the base station's RF circuitry plus analog-to-digital or digital-to-analog converters and up or down converters. RUs also have operation and management processing capabilities and a standardized optical interface to connect to the rest of the base station.

    

When deployed as part of a DAS infrastructure, RUs are usually connected with a DAS Head-End that uses a fiber optic cable.

reservation
    

The information stored in the SAS about a relinquished grant. The stored relinquished grant information can be used for a new grant prior to the next CPAS by the same CBSD. The unused reservations are deleted as part of the CPAS process.

Same Frequency Group (SFG)
    

A group of CBSDs that must use grants with the same frequency range. Also known as a Single Frequency Group (SFG) in WInnForum or a Common Channel Group (CCG) in CBRS Alliance. An SFG can be viewed as a subset of a Frequency Reuse Group (FRG).

Spectrum Access System (SAS)
    

A cloud service that ensures the protection of higher-priority users by controlling the operating parameters (such as channels or transmission power) of lower-priority devices. SAS is an entity that's authorized and certified by the FCC to coordinate and control the operation of CBSD devices under [Part 96](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96).

SAS Portal
    

A web interface that manages CBSDs connected to the SAS. You can use the SAS Portal to get information about spectrum availability, channel quality, DPA neighborhoods, and channel guidance.

SAS Portal API
    

Exposes administrative actions to SAS customers and helps manage CBRS resources. It allows customers to integrate with existing tools and easily scale across large numbers of networks and devices.

Secondary PAL
    

The leasing terms by which PAL rights are conveyed from a PAL licensee to an eligible lessee. Also known as Secondary Market Leasing Agreement (SMLA).

Signal to Interference plus Noise Ratio (SINR)
    

Used to measure the signal quality. It is obtained when a strength of the wanted signal is compared to the unwanted interference and noise.

spectrum inquiry
    

To learn which operational frequencies and power levels are available at a CBSD location, the CBSD sends spectrum inquiry requests to SAS. SAS responds with the frequencies sorted from best channel quality to worst. For more information, see [How the CBSD knows what spectrum is available](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-spectrum-availability).

Spectrum Reuse Group (SRG)
    

The SRG identifies a group of CBSDs operated by a CBSD user or a group of CBSD users where the CBSDs can use the same spectrum. SAS is not involved in the interference management among the members of this group.

serial number
    

A unique identifier assigned to a particular CBSD by the manufacturer.

secret
    

The secret is a token that the server decodes and then determines if it has expired. It is used with the [`ValidateInstaller()`](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/validate) method, where the user sends the token back in two forms: **Unmodified** , and **Signed by the CPI's private key**. This allows the server to verify that the _Unmodified_ secret is not expired, and _private key_ was signed by the correct key.

Test SAS Portal
    

A web interface that manages CBSDs connected to the SAS test environment at [test.sas.goog](https://test.sas.goog).

transmission point (TP)
    

An antenna deployed at a fixed location. An RU can be connected to a single TP or multiple TPs. CBSD requirements apply to each TP even if the network management and communication with the SAS is accomplished by using a single network interface.

user ID
    

Identifies the owner or operator of CBSDs that connect to the SAS. Each deployment has a unique user ID that all devices within that deployment share. For testing purposes, you can make up your own user ID.

Wireless Innovation Forum (WInnForum)
    

An international group dedicated to advancing technologies that support the innovative utilization of spectrum and the development of wireless communications systems (essential or critical). WInnForum defines the baseline [requirements and protocols](https://cbrs.wirelessinnovation.org/) for CBRS.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
