---
url: https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync/
title: Spectrum Access System sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:44.837898+00:00
---

# Spectrum Access System sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Spectrum Access System sync Stay organized with collections  Save and categorize content based on your preferences. 

All Spectrum Access System (SAS) users are required to collaborate to determine power allocation for Citizens Broadband Radio Service Devices (CBSDs). To achieve synchronous power allocation among SASs, all SAS users perform a procedure called [Coordinated Periodic Activities among SASs (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas). WInnForum defines CPAS in the document [WINNF-SSC-0008](https://winnf.memberclicks.net/assets/CBRS/WINNF-SSC-0008.pdf).

During CPAS, all SAS users do the following:

  * Exchange information with one another.
  * Retrieve the latest information from the [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) and [WInnForum](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#winforum) databases.
  * Reallocate resources among CBSDs with the Iterative Allocation Process (IAP) algorithm defined in [R2-SGN-16 of the WInnForum requirements](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0112.pdf). In particular, grant powers are adjusted in an equitable way.
  * Recalculate the [Dynamic Protected Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) move lists by using the algorithm defined in [R2-SGN-24 of the WInnForum requirements](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0112.pdf).



SAS users synchronize these activities to make sure that all entities are protected.

## When CPAS runs

CPAS runs from 7 AM to 10 AM UTC each day. During CPAS, SAS can't issue new grants. When you perform CBSD maintenance that requires new grants, we recommend that you do the maintenance before CPAS begins. This maximizes the potential power that SAS can offer after CPAS completes.

**Note:** UTC to US time zone conversion differs by one hour between US Standard Time and US Daylight Savings Time.

## What CPAS means to a CBSD operator

During CPAS, as a CBSD operator you are responsible for limiting transmission power because grant power is not increased during CPAS. Also, SAS recalculates the DPA move lists during CPAS. Therefore, it's important to retain the grant suspension for the CBSDs.

### Transmission power limits

Resources are reallocated once per day during CPAS. During this reallocation, a small portion of the resources are reserved for new grants that are requested before the next CPAS. Any grants that are authorized the next day use that reservation.

If a requested grant exceeds the remaining reservation, the grant request can be approved, but the grant might not be authorized in the subsequent heartbeat. During the next CPAS, this grant is given an equitable portion of the resources and then authorized.

Alternatively, the CBSD might perform a spectrum inquiry before requesting the grant. The spectrum inquiry response indicates how much of the reservation is available for use by the CBSD. If the CBSD requests a grant with the indicated transmission power, it's likely to be authorized for immediate transmission with the possible exception of DPAs. The grant power is not increased during the subsequent CPAS; if a higher-power grant is desired, it should be requested directly.

### Grant suspension

Due to the nature of the DPA protection requirements, SAS is not allowed to reserve even a small portion of the resources when protecting DPAs. This means that any new grant inside a DPA neighborhood must automatically be placed on the DPA's move list, regardless of the amount of interference that the grant might cause to the DPA.

When CPAS runs, SAS recalculates the DPA move lists. If possible, SAS removes the grant from the DPA move list. Learn more about [DPA protections](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast).

New grants are sometimes at a disadvantage in terms of their transmission power and how likely they can be suspended. The CBSDs are encouraged to retain their grants for a long time to avoid these disadvantages.

## How the CBSD gets notified of CPAS results

At the end of the CPAS, SAS notifies the CBSD of any required changes through the heartbeat response. The following table contains potential outcomes.

Heartbeat response | Interpretation | Recommended behavior  
---|---|---  
`responseCode: SUCCESS` `operationParam: unset` | No changes are recommended at this time. | Continue heartbeating normally.  
`responseCode: TERMINATED_GRANT` `operationParam: set` | A power decrease is required for this grant. Alternative operating parameters are provided. | Request a new grant by using the suggested operating parameters.  
`responseCode: TERMINATED_GRANT` `operationParam: unset` | It's not possible to authorize even a very low-power grant on this channel. | Perform a spectrum inquiry request and request a new grant.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
