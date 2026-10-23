---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels/
title: Choose CBSD channels \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:42.405027+00:00
---

# Choose CBSD channels  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Choose CBSD channels Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to choose the best channels for a Citizens Broadband Radio Service Device (CBSD). The Google Spectrum Access System (SAS) Portal offers channel guidance to help you maximize the Citizens Broadband Radio Service (CBRS) spectrum and manage interference.

In the SAS Portal, the **Coex** tab shows a ranked recommendation of channels for a CBSD. These recommendations are based on channel availability and the SAS assessment of _channel quality_. Channel quality is a combination of the level of interference and the [Effective Isotropic Radiated Power (EIRP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp) available.

The **Coex** tab is available for all registered CBSDs. It is also available for unregistered CBSDs in a **Ready for CPI** or **Pending Registration** configuration state.

**Important:** Channel guidance is only available for CBSDs located in the continental US.

## Channel quality

The channel quality score is a number between 0 (zero) and 100. The channel quality varies based on a CBSD's configuration and its surrounding environment.

**Important:** If a Customer Premises Equipment (CPE)-CBSD is part of a [Same Frequency Group (SFG)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sfg), the SAS ranks the channel as highest, even if the channel is not of the highest quality.

For all CBSDs, channel quality is affected by the following:

  * **The maximum EIRP available 24 hours after you request the spectrum grant.**

To protect incumbents, SAS does not offer full power in certain areas.

  * **Google's estimate of the interference caused by other CBSDs inside and outside your network.**

Based on configuration and active grants of surrounding CBSDs along with terrain and clutter data, the interference estimate takes into account all Category A CBSDs within one kilometer and Category B CBSDs within 10 kilometers.

  * **Interference and SINR estimation by using a generic antenna pattern based on the beamwidth information.**

For CBSDs in a frequency management group, SAS assumes that CBSDs in the same [Frequency Reuse Group (FRG)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#frg) don't interfere with each other when they use the same channel.




For fixed wireless networks, SAS assumes the following channel quality:

  * The CPE-CBSDs and Base Station-CBSDs in the same sector don't interfere with each other.

  * The CPE-CBSDs and Base Station-CBSDs in one sector interfere with CPE-CBSDs and Base Station-CBSDs in other sectors, unless they're in the same FRG.




## Channel ranking

_Channel ranking_ is the list of all available channels for the CBSD sorted from the highest quality to the lowest.

For fixed wireless networks, SAS assumes the following channel ranking:

  * For a CPE-CBSD that has been specified as an SFG, SAS recommends the channels that are used by the Base Station-CBSD in the SFG. SAS shows these channels at the top of the list regardless of quality scores.

  * For a Base Station-CBSD, SAS recommends the channels with the highest scores. It might recommend the same channels for all the CBSDs in the same FRG.




For mobile networks, SAS recommends the channels with the highest scores. It might recommend the same channels for all the CBSDs in the same FRG.

## Check recommended channels for a CBSD

**Important:** Channel guidance is based on the [state](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#state) of nearby CBSDs. The CBSD state is based on the configuration and active grants of the surrounding CBSDs.

To view the channel recommendation for a CBSD, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. In the **Channel recommendations** list, do one of the following: 
     * For an existing CBSD, [find your CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/review-configuration).
     * For a new CBSD, [create a new CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure) and save it as **Ready for CPI**.
  5. Select the CBSD. On the right, the CBSD page opens.
  6. Click the **Coex** tab. For a new CBSD, wait for four hours to see the **Coex** tab.
  7. To review the channels with the highest quality scores, use the channel ranking.

**Tip:** The channel ranking lists channels from the highest quality to the lowest.
  8. Request a new grant from your CBSD or Domain Proxy (DP) and specify the channels that you identified in the previous step. You might have to relinquish the previous grant.

**Important:** SAS does not automatically change your CBSD grants to use the recommended channels. You must request the grant from your CBSD or DP.



## What's next

  * Understand [CBRS spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability).
  * Learn [how the CBSD knows what spectrum is available](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsdspectrum-avail).
  * Understand [channel guidance for CBSDs in your network](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channel-guide).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
