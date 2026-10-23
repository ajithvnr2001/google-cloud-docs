---
url: https://docs.cloud.google.com/spectrum-access-system/docs/channel-masks/
title: Use channel masks \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:22.815927+00:00
---

# Use channel masks  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/channel-masks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Use channel masks Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to use and set channel masks for your Citizens Broadband Radio Service Device (CBSD).

When you request a channel mask, channel restrictions take effect immediately for spectrum inquiry requests and new grants. Any existing grants that overlap with newly restricted channels are terminated at the time specified in the **Pending changes** section of the **Coex** tab for that CBSD. Depending on your CBSD vendor, you might need to request grants for the available channels manually.

By default, Spectrum Access System (SAS) shows all channels as available to all CBSDs. Only users can set a channel mask. SAS doesn't automatically assign channel masks for any CBSDs.

After you set a channel mask for a CBSD, SAS rejects all new grant requests from that CBSD for the channels that you have restricted.

Use channel masks for the following:

  * To make sure that your CBSD uses the highest quality channel.
  * When you select new channels for a single CBSD with [channel guidance](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels) or for multiple CBSDs with a channel plan.
  * Occasionally, a CBSD automatically requests a grant for channels that you don't want to use. In this case, use channel masks to hide channels so that the CBSD doesn't request grants for them.



## Requirements to use a channel mask

  * To use channel masks, register through the [early access sign-up](https://docs.google.com/forms/d/e/1FAIpQLSfrjhKpdzOosLnsHI-kKY6wUVrKf_LpAHT0Zle-5nK2ZOwqpQ/viewform) form.
  * You can only use channel masks for a CBSD that has channel quality scores. Channel quality scores appear up to four hours after a CBSD configuration reaches the **Ready for CPI** status. [Learn how to choose a channel](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).
  * Channel masks must be set on one CBSD at a time. Currently, channel masks can't be set in bulk for an entire deployment or a subset of one.



## Set a channel mask

**Important:** Channel masks don't terminate active grants until [Coordinated Periodic Activities among SASes (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas).

To set a channel mask, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. Select the CBSD. On the right, the CBSD page opens.
  5. On the **Coex** tab, for **Channel mask** , click _expand_more_**Expand**.
  6. Click _lock_open_ **Lock node**.
  7. Click **Select channels** , and then select all the channels that you want the CBSD to use.

**Tip:** You can sort channels by frequency or by channel quality.
  8. Click **Schedule request**. The **Channel mask** section updates with your scheduled channel mask.

**Tip:** When you re-enable previously restricted channels, those channels become available to the CBSD immediately.



## What's next

  * [Choose the best channels for a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).
  * [Choose the best channels for your network](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/network-channel).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
