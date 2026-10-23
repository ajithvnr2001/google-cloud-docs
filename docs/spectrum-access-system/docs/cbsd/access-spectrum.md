---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum/
title: How a CBSD gets access to the spectrum \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:25.795649+00:00
---

# How a CBSD gets access to the spectrum  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/access-spectrum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  How a CBSD gets access to the spectrum Stay organized with collections  Save and categorize content based on your preferences. 

To get access to the spectrum, follow these steps:

  1. Request a grant to reserve a part of the spectrum. If the grant request is approved, the [reservation](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#reservation) is done but the Citizens Broadband Radio Service Device (CBSD) is not yet authorized to transmit by using the grant.
  2. Periodically send heartbeat requests for each of the approved grants to receive authorization to transmit.
  3. Relinquish the grant when the CBSD no longer uses a grant.



The following sections describe these steps.

## Request a grant

After a CBSD decides on which frequency range it will operate, it sends a grant request to Spectrum Access System (SAS). SAS approves or rejects the request as needed to protect incumbents and sends the result in a grant response. If the grant request is approved, SAS includes the grant ID and the suggested `heartbeatInterval` value in the grant response. However, the CBSD is not yet allowed to transmit.

If the grant request is rejected, the CBSD does not get the grant and the CBSD can try for another spectrum inquiry. A request is rejected because it had invalid parameters or the CBSD requested spectrum is unavailable.

### Request size and power for a grant

A CBSD can request any grant size from 5 MHz to 150 MHz. The grant size must always be a multiple of 5 MHz with start and end frequencies divisible by five. For example, a grant request for 3640 MHz to 3655 MHz is correct, but a grant request for 3642 MHz to 3647 MHz is incorrect.

**Important:** The spectrum inquiry response always shows the spectrum availability in channels of 10 MHz.

If you request a grant for more than 10 MHz, the maximum approved [Effective Isotropic Radiated Power (EIRP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp) is the lowest from all channels within that range.

For example, SAS indicates that the range from 3550 MHz to 3560 MHz can support an EIRP of 30 dBm/MHz, and the range from 3560 MHz to 3570 MHz can support an EIRP of 27 dBm/MHz. The device should conclude that 3550 MHz to 3570 MHz is available with a maximum EIRP of 27 dBm/MHz, which is the minimum value from the relevant channels.

## Send heartbeat requests for authorization to transmit

After the CBSD has a grant, it can send a heartbeat request for that grant. A CBSD can have multiple grants, but it must send a heartbeat request for each one. The heartbeat request is used to ask SAS if the CBSD can transmit with the parameters it sent in the grant request.

If SAS approves the heartbeat request, the CBSD is authorized to transmit until the `transmitExpireTime` value specified in the heartbeat response. To ensure that the CBSD can continue to transmit, the CBSD must send a heartbeat request to SAS at least once before the `transmitExpireTime`. To maximize uptime and reliability of CBSDs connected to SAS, the CBSD should heartbeat at the suggested `heartbeatInterval` value in seconds specified in the grant response.

The `transmitExpireTime``values from the heartbeat response and the`heartbeatInterval` values from the grant response depend on whether the CBSD is located in a [Dynamic Protection Area (DPA) neighborhood](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa). In such cases, the values depend on whether the grant is in the 3550 MHz to 3650 MHz range. The following table describes this relationship:

| `transmitExpireTime` value | `heartbeatInterval` value  
---|---|---  
**CBSD not in a DPA** | 6 hours after the most recent `Authorized` heartbeat response | 30 minutes  
**CBSD in a DPA with a 3550~3650MHz grant** | 4 minutes after the most recent `Authorized` heartbeat response | 60 seconds  
**CBSD in a DPA with only a 3650~3700MHz grant** | 6 hours after the most recent `Authorized` heartbeat response | 60 seconds  
  
In its heartbeat response, SAS can do one of the following:

  * **Authorize the grant:** the CBSD can start or continue to transmit.
  * **Terminate the grant:** SAS can't allow the grant to transmit while protecting incumbents.
  * **Suspend the grant:** the CBSD isn't allowed to transmit at the moment but might be able to transmit again.



To learn more about DPAs and reasons for grant suspension, see the following topics:

  * [Operate CBSDs near the coast](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast)
  * [SAS synchronization](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync)



If the CBSD does not receive a heartbeat response from SAS, it should send another heartbeat request after 30 seconds. This period is the `retryInterval` value. To maximize the uptime of your CBRS network with SAS, check with your CBSD manufacturer on how to set the `retryInterval` value to 30 seconds and the `heartbeatIntterval` value as suggested in the grant response.

## Relinquish a grant

If a CBSD no longer needs a grant, it sends a relinquishment request to SAS. SAS responds with a relinquishment response, which approves the request.

## What's next

  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
