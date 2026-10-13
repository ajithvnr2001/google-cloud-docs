---
url: https://docs.cloud.google.com/spectrum-access-system/docs/manage-ppa/
title: Manage PAL Protection Areas \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:53.003182+00:00
---

# Manage PAL Protection Areas  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/manage-ppa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Manage PAL Protection Areas Stay organized with collections  Save and categorize content based on your preferences. 

A [PAL Protection Area (PPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#ppa) is a geographic area protected from [General Authorized Access (GAA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gaa) interference when a [Priority Access License (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) operator uses a PAL channel. In this document, you learn how to manage and set up a PPA for your CBSDs.

PPAs in Spectrum Access System (SAS) are generated automatically for each PAL-qualified Citizens Broadband Radio Service Device (CBSD) that requests a grant on an operator's PAL channels. The size and shape of a PPA are determined by the following:

  * The location of the CBSD.
  * The CBSD's Effective Isotropic Radiated Power (EIRP) capability as specified by the registration request, up to the FCC-certified limit.
  * The CBSD's antenna height, gain, azimuth, and beamwidth.
  * A standard [WInnForum](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#winforum)-defined propagation model used by all SASs.



To minimize interference to the PPA, CBSDs located outside but near the PPA might have to reduce power on the PAL channel. Any new CBSDs deployed by another operator within the PPA cannot request grants for the PAL channel. [Learn how to find a PPA in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/use-pals#showpal).

SAS might create one or multiple PPAs within a county for the same PAL channel based on the service areas of one or more PAL-protected CBSDs. PPAs are dynamic because they can grow, merge, split, and shrink based on the size of the service areas. The SAS merges PPAs that overlap into a single PPA when those PPAs are on the same channel and in the same county. PPAs are updated daily during [Coordinated Periodic Activities among SASs (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas).

## Set up a PPA for your CBSD

You can set up a PPA for your CBSD before, during, and after CPAS.

**Before CPAS**

  * Request a grant on your PAL channels two hours before CPAS. This is to ensure that SAS creates a PPA during CPAS. Protection from CBSDs that have GAA grants begins afterwards.
  * If your PAL channel [doesn't have a high quality score](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels#channel-quality), and your equipment supports multiple grants, use a different grant to transmit until your PAL grant successfully finishes CPAS. This minimizes the risk and impact of interference before PAL protection begins.



**During CPAS**

We recommend that your CBSD keeps heartbeating on your PAL grant. New PPAs take time to get protected. Other operators' CBSDs within the PPA might use the PAL channel until CPAS has completed, so your PAL channel might experience interference.

**After CPAS**

  * The PPA protection begins after CPAS is completed. SAS terminates all grants on the PAL channel for other operators' CBSDs located within the PPA.

  * The CBSD sends heartbeats to receive authorization to transmit. Your CBSD is protected from interference from other CBSDs on the PAL channel.

  * If you experience interference on your PAL channel after the PPA is created, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).




## Maintain a PPA for a PAL-protected CBSD

To maintain a PPA for a PAL-protected CBSD, follow these steps:

  1. Continue heartbeating on the PAL grant. If the CBSD does not receive a heartbeat on a PAL grant for seven days, the CBSD's PPA is removed.

**Note:** If you use multiple PAL grants and miss heartbeats on one PAL grant, only the PPA associated with that grant is removed. If the CBSD continues to heartbeat on the remaining PAL grants, then the PPAs for the remaining grants are still enforced.
  2. If a PPA is removed from a PAL-protected CBSD, re-establish a PPA.


**Tip:** If you relinquish a PAL grant and request a new one within the same day, it does not affect the PPA.

## Re-establish a dropped PPA

To re-establish a PPA, do not re-register the CBSD. We strongly discourage re-registration because all of the CBSD's other grants are relinquished and might not be available immediately after re-registration.

To re-establish a dropped PPA, do the following:

  1. [Request a new PAL grant](https://docs.cloud.google.com/spectrum-access-system/docs/use-pals) for the same channel.
  2. Wait for the next CPAS cycle.
  3. After the next CPAS cycle, the PPA is established.



## What's next

  * Learn how to [use PALs in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/use-pals).
  * Learn about [SAS sync (or IAP)](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
