---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/operator-tips/
title: CBSD operator best practices \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:43.728554+00:00
---

# CBSD operator best practices  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/operator-tips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  CBSD operator best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page documents best practices for common tasks that a Citizens Broadband Radio Service Device (CBSD) operator might perform.

## Spectrum inquiry results

The following sections describe the spectrum inquiry responses that Spectrum Access System (SAS) reports.

### maxEirp parameter

The `maxEirp` parameter in the spectrum inquiry response is a best estimate of the [Effective Isotropic Radiated Power (EIRP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp) that could be authorized for immediate transmission. If a grant with the specified EIRP is not authorized by SAS, it's because of the [Dynamic Protection Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) activation.

### Channelization

SAS automatically splits spectrum inquiry requests into 10-MHz channels. This allows it to provide the maximum information to the CBSD because conditions can vary significantly between channels.

SAS supports grant requests larger than 10 MHz. To maximize transmission authorization, we recommend requesting the minimum EIRP reported by SAS across all selected channels.

### Channel unavailability

A 10-MHz channel is marked as unavailable by SAS if there is no power that can be supported in the foreseeable future. SAS marks channels as unavailable in the following circumstances:

  * **The CBSD is inside an exclusion zone:** the frequency range affected by the exclusion zone is marked as unavailable.
  * **The CBSD is inside a PAL Protection Area (PPA):** when a Priority Access License (PAL) licensee has an active PAL grant, the frequency range of the PAL grant is marked as unavailable for all General Authorized Access (GAA) users in areas which would interfere with the PAL grant.



## Impact of DPA activation

Each grant that SAS grants is considered in the aggregated interference calculations to protect DPA. To avoid grants unnecessarily being placed on a DPA move list, a CBSD requests only the grant power that it expects to utilize. To minimize the impact of DPA activation and reduce disruption, we recommend that you split up large grants.

If a device operates at multiple bandwidths, then request several 10-MHz grants rather than a single larger bandwidth grant.

DPA move lists are calculated independently for each 10-MHz channel. DPA activations also occur separately for each channel. If a CBSD holds a single 20-MHz grant, the grant must be suspended if a DPA activation affects either channel. If it holds two 10-MHz grants instead, the impact of a DPA activation can be minimized.

To fulfill operational security requirements from the Department of Defense (DoD), SAS does not indicate which channels are affected by DPA activations. Learn how to [operate CBSDs near the coast](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast).

## CBSD EIRP

The following sections describe when to increase CBSD EIRP, its capabilities, availabilities, specifications, and the FCC certified maximum EIRP.

### When to increase EIRP

If the CBSD needs to increase its EIRP while it minimizes downtime, follow these steps:

  1. Continue to heartbeat and transmit on the original low-power grant.
  2. Request a new higher-power grant on a channel that doesn't overlap with the original grant.
  3. If the new grant is authorized, relinquish the original grant and begin transmission on the new grant.
  4. If the new grant is suspended: 
     1. Continue to heartbeat on both grants until the next CPAS is complete. At that time, the new grant is adjusted to a power that can be authorized.
     2. After the new grant is authorized, relinquish the original grant and begin transmission on the new grant.



### Automated EIRP increase

To boost coverage and capacity, SAS strives to maximize the EIRP for grants near protected entities. SAS automatically evaluates and offers an EIRP increase to each grant that was authorized with an EIRP 6 dB or lower than their maximum EIRP capability before the first CPAS.

### EIRP capability

The CBSD reports its EIRP capability in the registration request to SAS. The EIRP capability must be specified in dBm/10 MHz. SAS rejects the registration request if the EIRP capability specified exceeds the maximum EIRP specified in the [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) database (`FCCMaxEirp`). If no EIRP capability value is specified in the registration request by the CBSD, SAS uses the `FCCMaxEirp` value as the device's EIRP capability.

### EIRP availability

For a spectrum inquiry request, SAS provides the maximum EIRP available, in dBm/MHz on each 10-MHz channel in the response. This number is based on the EIRP capability of the CBSD established during the registration.

### EIRP specifications

For a grant request, the CBSD must specify the EIRP in dBm/MHz. This value must be equal to or lower than the EIRP capability value of the CBSD established during the registration. To convert dBm/MHz to dBm/10 MHz, use the following formula:

$ =>37\hspace{1mm}dBm/MHz=37 + 10^* log(10)\hspace{1mm}dBm/10\hspace{1mm}MHz = 47\hspace{1mm}dBm/10\hspace{1mm}MHz $ 

### FCC certified maximum EIRP

All SAS users compute the certified maximum EIRP from the FCC EAS database based on the following rules:

  1. Only one `FCCMaxEirp` value is computed for each FCC ID.
  2. To calculate the power spectral density (PSD) for each row corresponding to a single FCC ID, the EIRP reported in the FCC EAS database is divided by the value obtained from rounding up the emission designator bandwidth to a channel bandwidth of 5, 10, 15, 20, 30, or 40 MHz as follows: 
     * 4.5-5 MHz to 5 MHz
     * 8-10 MHz to 10 MHz
     * 13-15 MHz to 15 MHz
     * 7.5-20 MHz to 20 MHz
     * 27-30 MHz to 30 MHz
     * 36-40 MHz to 40 MHz
  3. All power levels in the FCC EAS database are considered EIRP despite the **EP** grant note in the [KDB 953436 Aug 13, 2018 from FCC](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?switch=P&id=50070).
  4. If there are multiple maximum EIRPs for a single FCC in the FCC EAS database, the value reported for the 10-MHz channel bandwidth is used to derive the certified maximum EIRP density.
  5. Power output in the FCC EAS database is normalized with the channel bandwidth to obtain power per 10 MHz.
  6. If there are multiple entries corresponding to 10 MHz for a CBSD, the smallest power per 10 MHz is used as the certified maximum EIRP.
  7. For CBSDs that have only one row in the FCC EAS database, the maximum EIRP density is calculated with the reported EIRP and the channel bandwidth regardless of the value of the channel bandwidth.



## Recommended timeouts

SAS recommends the timeout and retry periods for heartbeat and other CBSD API requests.

SAS recommends 30 seconds for the heartbeat timeout and retry periods for heartbeat requests. This 30-second timeout and retry period gives the CBSD more time to recover from a suspended grant or connectivity issue before it needs to stop transmission.

The following example uses the minimum possible recommended heartbeat interval of 60 seconds and the minimum possible transmit expiration time of 4 minutes.

For example, for a connectivity issue with the recommended heartbeat interval, timeout, and retry, the CBSD has up to six opportunities to receive a heartbeat response for each transmit expiry period.

[ ![Heartbeat response \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/heartbeat-response.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/heartbeat-response.svg) Heartbeat response (click to enlarge)

Your CBSD can heartbeat, timeout, and retry at a different interval than the recommendation. However, if you use a heartbeat interval longer than the interval recommended in the grant response, it decreases the resiliency of the CBSD. If your CBSD heartbeats at the suggested interval, and sets timeout and retries at 30 second intervals, it maximizes its chances to recover from a failure to receive a heartbeat response.

To learn more about recommended heartbeat intervals and transmit expiration times, see the following:

  * [Request a grant](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#request-grant)
  * [Send heartbeat requests for authorization to transmit](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum#heartbeat)



For all SAS and CBSD API requests other than the heartbeat request, SAS recommends 120 seconds for the timeout and retry period.

## What's next

  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
