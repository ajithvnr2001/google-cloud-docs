---
url: https://docs.cloud.google.com/spectrum-access-system/docs/pals/
title: Priority Access Licenses \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:14.891479+00:00
---

# Priority Access Licenses  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/pals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Priority Access Licenses Stay organized with collections  Save and categorize content based on your preferences. 

The Citizens Broadband Radio Service (CBRS) band operates as a shared spectrum with three tiers of users. The [Priority Access License (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) resides in Tier 2. The following diagram shows the tiers in the CBRS band.

[ ![Tiers in the CBRS band \(click to enlarge\)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/about-pal.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/about-pal.svg) Tiers in the CBRS band (click to enlarge)

## Interference protection

To get protection from [General Authorized Access (GAA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gaa)—users in the third tier—interference, you can buy a PAL at an auction. Each PAL receives interference protection in [PAL Protection Areas (PPAs)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#ppa) on a 10-MHz channel from 3550 MHz to 3650 MHz. The interference protection tiers are explained as follows.

### Tier 1

Tier 1 [incumbents](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#incubment) get protection from both PAL and GAA users. Within a protection area, channel availability and power limitations apply to PAL and GAA users equally.

For example, in a [Dynamic Protection Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa), grants on PAL channels can be suspended due to DPA activations. The CBSDs can request grants on GAA channels, but aren't protected from GAA interference.

### Tier 2

Tier 2 PAL users get interference protection from GAA users. When a PPA goes into effect, GAA users with grants on PAL channels that are determined to cause interference to the PPA have their grants terminated with [error code 500](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/errors-grant-suspension#troubleshooting-matrix). Sometimes, the grant termination includes suggested operating parameters such as a lower [Effective Isotropic Radiated Power (EIRP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp).

Although PAL users have a right to protection in the entire county, they are protected only where they have deployed CBSDs and only on their PAL channels. The PPAs generally cover only part of a county's license area, leaving space where GAA users can operate freely on PAL channels. In every county, there are eight channels that are never allocated for PAL. That means that all 15 channels could be available to GAA users in any county.

### Tier 3

Tier 3 GAA users are unlicensed with no guaranteed interference protection. In this tier, CBSD operates as licensed-by-rule.

## PAL auction

The PAL auction was closed on August 25, 2020. A maximum of seven channels were auctioned in each US county where a single operator was limited to a maximum of four channels in any county. The [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) database publishes the list of PAL licensees. Licenses are valid for ten years. PAL licensees can use their PAL licenses with any SAS with a start date indicated in the [CBRS status summary](https://cbrs.wirelessinnovation.org/cbrs-status-summary).

## PAL channel allocation

SAS administrators coordinated to develop a methodology for PAL channel allocation in accordance with the CBRS functional and operational requirement developed in WInnforum. The methodology is developed by receiving the inputs from each operator on their channel preference for their auctioned logical PAL channels.

All PAL licensees received information on the PAL Channel Assignment Procedure in December 2020. If you didn't get the email about the PAL channel assignment procedure, or if you want to know more about the assignment procedure, write an email to SAS administrators at [cbrs_pal_channels@outlook.com](mailto:cbrs_pal_channels@outlook.com).

## Secondary market

The PAL licensees can sell or sub-license their PALs to other operators for all or part of the license area. Sub-license agreements can be recorded by Google SAS in the [FCC Universal Licensing System (ULS) database](https://www.fcc.gov/wireless/universal-licensing-system). To verify a licensee's claim of a PAL or sub-licensed PAL, SAS checks the FCC ULS database.

## What's next

  * Learn how to [use PALs in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/use-pals).
  * Learn about [SAS sync (or IAP)](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
