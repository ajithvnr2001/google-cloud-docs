---
url: https://docs.cloud.google.com/spectrum-access-system/docs/overview/
title: Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:45.175206+00:00
---

# Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Spectrum Access System Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a detailed overview of [Spectrum Access System (SAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas), including its features and architecture, and how it works with other network components.

Wireless technology has grown considerably over the past few decades. With billions of devices connected to mobile networks worldwide, the demand for faster and improved internet access is ever increasing. To keep up with this growing demand, service providers are investing considerably to enhance their wireless infrastructure and are pushing for access to more wireless spectrum.

Because most of the licensed wireless spectrum is already allocated, the National Telecommunications and Information Administration (NTIA) and the Federal Communications Commission (FCC) together have identified the _[Citizens Broadband Radio Service (CBRS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs)_ spectrum band of **3550 MHz to 3700 MHz** that can be reused for commercial wireless broadband internet service.

For the commercial use of CBRS, the [FCC](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) has defined [part 96 regulations](https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=&SID=2dd346ae3b51f2866ab6fb907e755526&mc=true&r=PART&n=pt47.5.96) that have been developed into standards by the [Wireless Innovation Forum](https://www.wirelessinnovation.org/) (WInnForum). These standards, processes, and procedures ensure that the CBRS spectrum can be shared between federal and non-federal users without disrupting the other's services. For example, when a government radar system is not using channels at specific times, that spectrum can be freed up for commercial use.

Mobile network operators and fixed-wireless network companies use the CBRS spectrum to build their own private networks. To build this network, they require services that can help them to do the following:

  * Plan, deploy, and manage cost-effective networks
  * Deploy low-cost networks to sell access on a wholesale basis
  * Manage costs by offloading data traffic from host networks to the CBRS spectrum
  * Find algorithmic solutions to problems such as network coexistence
  * Share networks by using user priority rules
  * Increase capacity to an existing mobility network



Google is an FCC-certified SAS administrator and is also one of the main contributors to CBRS WInnForum specifications and the OnGo Alliance. Google has developed a suite of cloud-based products and services that help these network operators to create a CBRS ecosystem that provides better wireless internet. For more information about various Google products and services in the shared spectrum space, see [Spectrum sharing](https://www.google.com/get/spectrumdatabase/).

The CBRS band is a shared wireless spectrum with a frequency band from 3550 MHz to 3700 MHz. The FCC has defined three tiers of CBRS users based on priority:

  * **Tier 1[Incumbent users](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#incubment)**.

High-priority users such as naval aircraft carriers and fixed satellite stations.

  * **Tier 2[Priority Access Licensee (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) users**.

Licensed users that do not interfere with the incumbent users, and tolerate any possible interference from them.

  * **Tier 3[General Authorized Access (GAA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gaa) users**.

General users that are authorized to use the CBRS band as long as they do not interfere with the Tier-1 and Tier-2 users.




A _[Citizens Broadband Radio Service Device (CBSD)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd)_ is a transmitter device that operates in the [Citizens Broadband Radio Service (CBRS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs) spectrum, such as an Evolved NodeB (eNodeB).

The primary function of Spectrum Access System (SAS) is to control spectrum access for a CBSD. A CBSD transmits only _after_ it has received authorization from SAS. This control ensures the protection of higher-priority CBRS users by controlling the operating parameters such as channels or transmission power of lower-priority CBRS devices.

A CBSD initiates all the required communications with SAS by using standard protocols defined by WInnForum. SAS then issues short-term spectrum leases to these CBSDs, abstracting the complexity of facilitating coexistence among many disparate systems that compete for shared spectrum resources.

## Google SAS features

Google SAS is a cloud service that helps network operators manage wireless communication in the CBRS band. As a network operator, you can use Google SAS to do the following:

  * Register CBRS devices.
  * Monitor device status with integrated map views.
  * Delegate administration and control access to your network across users.
  * Choose the best channels for a CBSD.
  * View dynamic protection areas as overlay.
  * Update and sign multiple CBSD configurations with the import templates.
  * Visualize Customer Premises Equipment (CPE) and base station connectivity in the map.
  * Resolve interference between CBSDs.
  * Decommission or move CBSDs.
  * View the last 30 days of CBSD device history.
  * Check your billing settings in the SAS Portal for greater transparency.
  * Organize CBSDs by network deployment in SAS Portal.



The following features and capabilities are provided by Google SAS.

  * **Create optimized CBSD deployment in your network**.

A deployment is a way of organizing the CBSDs in the SAS Portal. It has a unique user ID and is associated with your SAS account. You can also monitor deployment status, create users to manage access to your network, and access support resources. For more information, see [Get started with SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/portal).

  * **Identify spectrum availability using heatmaps**.

SAS Portal provides _Dynamic Protection Area (DPA)_ neighborhood borders and CBRS spectrum availability heatmaps across the United States by using the Google Maps interface. Heatmaps help you determine how many channels are available in an area before you deploy CBSDs. For more information about spectrum heatmaps, see [Understand CBRS spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability).

  * **Select the channel plan based on channel guidance**.

SAS Portal offers channel guidance to help you maximize the CBRS spectrum and manage interference. You can review and implement the most suitable channel plan for your CBRS network from SAS Portal. The channel plan is optimized to minimize interference with other CBSDs. For more information about channels, channel masks, and channel plans, see [Manage network interference](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).

  * **Manage the end-to-end CBSD workflow**.

SAS supports the entire lifecycle of CBSD, starting with registration, spectrum inquiry, grant requests, heartbeat requests, and deregistration. For more information, see [About CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview).

  * **Minimize DPA activations and whisper zones impact**.

For more information, see [CBSD operator best practices](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/operator-tips).

  * **Analyze network status by using real-time monitoring dashboards**.

SAS Portal provides real-time status of current grants, last heartbeat, and grant history for each CBSD. It also provides real-time data about the DPA movelist to track which grants were suspended during incumbent activity.

  * **Protect PAL operators from GAA user interference**.

For more information about PAL channel allocation and interference protection, see [Manage Priority Access Licenses](https://docs.cloud.google.com/spectrum-access-system/docs/manage-ppa).

  * **Choose a billing plan based on the requirements of your organization**.

For more information about various billing options available in SAS, see [SAS billing](https://docs.cloud.google.com/spectrum-access-system/docs/billing-questions).




## Advantages of using a SAS

  * **Channelization**.

SAS automatically splits spectrum inquiry requests into 10 MHz channels. Because conditions can vary significantly between channels, the splitting of requests provides the maximum information to the CBSDs.

  * **Cost savings**.

SAS allocates network capacity or coverage on an as-needed basis. This helps to significantly reduce operational costs.

  * **The`maxEirp` parameter determines the maximum approved EIRP**.

The `maxEirp` parameter in the spectrum inquiry response is a best estimate of the Effective Isotropic Radiated Power (EIRP) that could be authorized for immediate transmission. If a CBSD requests a grant for more than 10 MHz, the maximum approved EIRP is the lowest from all the channels within that range. If a grant with the specified EIRP is not authorized by SAS, it might be due to [DPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) activation.




## Google SAS service architecture

The shared spectrum network consists of various network elements that interact by using specific interfaces. SAS is the core service in the network and is responsible for dynamic frequency allocation in the shared spectrum range.

### SAS core service

[ ![SAS overview \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/sas-architecture.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/sas-architecture.svg) SAS overview (click to enlarge)

As shown in the preceding diagram, the SAS consists of three main components:

  * **Google SAS Portal**.

Includes the **Portal UI** and **Portal API** that manages the CBSDs connected to SAS.

  * **SAS Backend (SAS BE)**.

Includes all the services that SAS offers.

  * **SAS Database (DB)**.

Includes the **DB** that stores all CBSDs registered with SAS along with the information required to manage CBSDs. This information includes details about the grants that are currently active and aggregate interference for any protected points or areas. It also stores information collected from other SASs about where they have CBSDs and what protected points or areas exist.




These three SAS modules interact with each other and the other network elements to provide network operators with all the necessary tools and processes to manage their CBRS network.

### CBSD transmitter

A CBSD transmitter sends a registration request to SAS with information such as owner, location, and transmission characteristics.

After SAS approves the registration request, CBSD is ready to perform multiple operations such as the following:

  * Request spectrum grant
  * Make spectrum inquiries
  * Provide health checks
  * Relinquish a grant
  * Deregister



CBSD can register with multiple SASs, but cannot have an active grant from multiple SASs simultaneously. To make sure that there are no overlapping active grants, a daily _SAS- SAS_ sync is required. In this type of sync, SAS communicates with other SASs in the network to ensure consistency of bandwidth allocation among SASs. When a SAS- SAS sync occurs, all CBSDs and protected point areas known to SAS are shared with other SASs in the network. Learn more about how CBSDs communicate with SAS later on this page.

### Environmental Sensing Capability devices

The FCC has provided strict guidelines and regulations for spectrum sharing based on user priority. These guidelines ensure that higher-priority user transmissions do not get interference from lower-priority users. _Environmental Sensing Capability (ESC)_ devices enforce the FCC rules and enable SAS to manage spectrum allocation without interference to incumbent and other priority users.

ESCs are positioned along the US coast to detect when a DPA is active. A [DPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) is an exclusion zone that generally becomes active when incumbent users transmit in the CBRS spectrum. SAS maintains a list of CBSDs for each DPA neighborhood. When ESCs detect the activation of DPAs on a given channel, they send this information to SAS. SAS then suspends grants to the CBSDs in the DPA neighborhood on that channel to ensure that there's no interference.

## How SAS works

The primary function of any SAS is to authorize and manage wireless communication of CBSDs transmitting in the CBRS band. Therefore, CBSDs must be able to communicate with SAS to initiate transmission. [WInnForum](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#winforum) has defined standards and protocols to enable this communication. SAS implements the [SAS-CBSD API technical](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf) specification for the CBSD-SAS interface. This interface is based on the HTTP over Transport Layer Security (HTTPS) protocol.

### CBSD-SAS interface

CBSD is responsible for initiating communication with SAS in the following way:

  1. CBSD sends a registration request to SAS to indicate its intention to operate. Successful registration implies a validation by SAS that the CBSD has been FCC-certified and is authorized to receive a spectrum grant for transmission.
  2. After the registration is successful, CBSD can request a spectrum grant.
  3. SAS allocates a channel and power level to the CBSD. This channel is identified by a unique grant identifier. CBSD can start transmission in the allocated grant only after it has sent a heartbeat request.
  4. On receiving a positive response for the heartbeat request, CBSD can start the transmission.
  5. CBSD can ask for multiple grants in different spectrum channels and relinquish grants that it no longer requires.



The following diagram shows the end-to-end CBSD workflow:

[ ![CBSD workflow \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/cbsd-workflow.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/cbsd-workflow.svg) CBSD workflow (click to enlarge)

SAS has implemented six methods defined in the [SAS-CBSD API](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf) for the CBSD-SAS interface:

  * Registration
  * Spectrum inquiry
  * Grant requests
  * Heartbeat requests
  * Relinquish a grant
  * Deregistration



The following subsections describe these methods.

#### Registration

[ ![SAS registration \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/registration.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/registration.svg) SAS registration (click to enlarge)

A CBSD must register with SAS. During the registration process, each CBSD sends installation information such as fixed location, unique identifiers, group membership, and radio-related capabilities to SAS Portal.

If the registration is successful, SAS sends back a unique identifier for that CBSD. If SAS rejects the registration request, it responds with an error message. The CBSD must then correct the error and send another registration request. For more information about registration, see [CBSD registration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister).

#### Spectrum inquiry

[ ![Spectrum inquiry \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/spectrum-inquiry.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/spectrum-inquiry.svg) Spectrum inquiry (click to enlarge)

Spectrum inquiry is an optional procedure that a registered CBSD can initiate with SAS to inquire about available spectrum at its location and installation characteristics. SAS responds with detailed information about the frequencies available for the use of the CBSD and any additional information that can help the CBSD to choose a frequency range. For more information about spectrum inquiry, see [CBSD spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsdspectrum-avail).

**Important:** SAS _does not_ reserve any channel allocations as a part of spectrum inquiry. It also does not guarantee that the information shared in the spectrum inquiry response is still valid when the CBSD initiates a grant request.

#### Grant requests

[ ![Grant request \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/grant-request.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/grant-request.svg) Grant request (click to enlarge)

CBSDs request a grant to reserve a portion of the spectrum for their use. The grant request consists of several operational parameters that depend upon the CBSD capabilities, current operation, and configuration.

If approved, SAS responds with the grant ID and other parameters such as grant expiry interval, heartbeat interval, and channel type. When a grant is approved, SAS makes a [reservation](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#reservation) for the requesting CBSD. However, CBSD is not yet authorized to transmit by using the grant. For more information, see [Learn more about how to request a grant](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#request-grant).

#### Heartbeat requests

[ ![Heartbeat requests \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/heartbeat-request.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/heartbeat-request.svg) Heartbeat requests (click to enlarge)

CBSDs periodically send heartbeat requests for each of their approved grants to receive authorization to transmit. For more information, see [Learn more about heartbeat requests](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#heartbeat).

#### Relinquish a grant

[ ![Relinquish request \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/relinquish-request.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/relinquish-request.svg) Relinquish request (click to enlarge)

When the CBSD no longer wants to use a grant, it relinquishes the grant. For more information, see [Learn more about how to relinquish a grant](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#relinquish).

#### Deregistration

[ ![Deregistration \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/deregistration.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/deregistration.svg) Deregistration (click to enlarge)

If the CBSD is decommissioned or moved, it deregisters from the SAS. For more information, see [Learn more about deregistration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister).

### SAS-SAS interface

The SAS-SAS interface synchronizes Google SAS with other SAS Operators. Using this interface, SAS shares all relevant persistent store changes to other SAS Administrators. It also receives and processes changes from other SAS Administrators.

The SAS-SAS interface enables exchange of the following data:

  * Exchange of registration data
  * Exchange of all grants issued by the SAS
  * Exchange of all changes in registration and grant status
  * Exchange of regulatory inputs received by the FCC and WInnForum databases



SAS uses Coordinated Periodic Activities among SASs (CPAS) to facilitate communication with peer SASs. CPAS is a daily process executed by all SASs in the networks to exchange information. Google implements CPAS, as defined by WInnForum in [WINNF-SSC-0008](https://winnf.memberclicks.net/assets/CBRS/WINNF-SSC-0008.pdf). For more information about CPAS and SAS peer exchange, see [Learn more about CPAS and what it means to CBSD Operators](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).

### How SAS protects higher-priority users

SAS continuously communicates with CBSDs to make sure that the incumbent users, such as naval radars, are protected from PAL and GAA users. To ensure that there is no interference to these higher-priority users, SAS does the following:

  * SAS uses a network of ESCs to detect when the incumbent users are using the spectrum. Whenever any activity is detected, the spectrum on which they are transmitting is not available to other users. For more information, see [Learn how to operate CBSDs near the coast](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast).
  * Every night, all SASs execute [CPAS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas) to make sure that they are all operating with the latest information.



## What's next

  * Learn about the [Spectrum Access System Portal](https://docs.cloud.google.com/spectrum-access-system/docs/portal).
  * Learn about the [Citizens Broadband Radio Service Device](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview).
  * [Troubleshoot SAS](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
