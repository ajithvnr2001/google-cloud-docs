---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channel-guide/
title: Optimize channel guidance \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:13.928031+00:00
---

# Optimize channel guidance  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channel-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Optimize channel guidance Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand the channel guidance for a Citizens Broadband Radio Service Device (CBSD) in your network.

Channel quality and ranking vary based on a CBSD's frequency management group. Spectrum Access System (SAS) automatically assigns frequency management groups to all CBSDs unless the CBSD provides this information in the registration request. To optimize channel guidance information, you can use the Google SAS Portal to adjust frequency management groups.

SAS pre-populates values for your CBSDs every day:

  * The [Same Frequency Group (SFG)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sfg) is based on the best server available, azimuth, and on the channels that the CBSD uses.
  * The [Frequency Reuse Group (FRG)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#frg) is based on the channels that the CBSD uses and on [user IDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid).



To make sure that the pre-populated values match your network configuration, review the SFG and the FRG on the CBSD's **Config** tab.

To optimize channel guidance, assign frequency management groups as follows:

  * Assign an SFG to each CBSD that must use the same channel.
  * Assign an FRG to CBSDs that don't cause interference issues with each other when they share a channel.



After you confirm your frequency management groups, review the recommended channels on the CBSD's **Config** tab. You might have to wait up to four hours to view the updated results.

## Update frequency management groups

To update frequency management groups, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. To change group information, do the following: 
     * For an existing CBSD, [find your CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/review-configuration).
     * For a new CBSD, [create a new CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure) and save it as **Ready for CPI**.
  5. Select the CBSD. On the right, the CBSD page opens.
  6. On the **Config** tab, click the **Frequency management** _expand_more_ drop-down.
  7. For the **Same freq** and **Freq. reuse** fields, enter the group. You can assign a maximum of one SFG to a CBSD at a time and multiple FRGs to the same CBSD.

**Tip:** You can import CBSDs to specify SFG and FRG names. In the CSV template, use the CCG column for the SFG and the ICG column for the FRG.

## Overrides

Some CBSDs are configured to send SFG and FRG information to SAS. When the CBSD provides grouping parameters information like this, it overrides information saved in the SAS Portal.

You can change the frequency management group settings in the SAS Portal, but the CBSD might reset those values if it's programmed to do so. For more details, check with your CBSD vendor.

## What's next

  * [Choose the best channels for a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
