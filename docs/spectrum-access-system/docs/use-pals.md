---
url: https://docs.cloud.google.com/spectrum-access-system/docs/use-pals/
title: Use Priority Access Licenses \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:15.679801+00:00
---

# Use Priority Access Licenses  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/use-pals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Use Priority Access Licenses Stay organized with collections  Save and categorize content based on your preferences. 

If you are a [Priority Access License (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) licensee, you can use the [Google Spectrum Access System (SAS) Portal](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas-portal) to do the following:

  * Confirm if your PAL is properly registered with [Spectrum Access System (SAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas).
  * Check the geographic areas that are protected from [General Authorized Access (GAA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gaa) interference for your PAL-protected SASs.

**Note:** Tier 1 incumbents can temporarily suspend PAL operators as needed. [Learn more about PALs](https://docs.cloud.google.com/spectrum-access-system/docs/pals).

## Before you begin

Only winners from the [Federal Communications Commission (FCC) auction 105](https://www.fcc.gov/auction/105), or a verified sub-licensee can get protection on their PAL channels. Contact your CBSD or Domain Proxy (DP) vendor support team to confirm the following:

  * Your vendor supports PALs and passed PAL interoperability testing with SAS.
  * If there are firmware upgrades required for PAL support.
  * If you need to configure any SAS or DP settings specific to PALs.



## Verify your FCC registration number

Your FRN must be saved to the SAS Portal to request PAL grants. If the FRN is not correct, SAS cannot provide PAL protection on your PAL channels in your licensed counties.

To verify the FRN, do the following:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. On the left, click _settings_ **Settings**.
  4. On the right, select the **FRN** field.
  5. Confirm that the FRN listed is correct. If the **FRN** field is missing or incorrect, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) and provide the correct FRN.



## Prepare your CBSD for a PAL grant

You must request the PAL grant from your CBSD or DP. You cannot request a grant from the SAS Portal.

To prepare your CBSD for a PAL grant, follow these steps:

  1. Confirm that your CBSD's GPS coordinates are located within your PAL county. 
     1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
     2. Click **View deployments**.
     3. On the left, click _map_ **Map view**.
     4. On the left, click _layers_ **Overlays** , and then click **PAL**.
     5. Expand the county folder and find the item labeled with the county name followed by county.
     6. To show it on the map, select the county boundary.
  2. Confirm your PAL channels. 
     1. [Find and select your CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/\(/spectrum-access-system/docs/cbsd/review-configuration\)).
     2. On the right, click the **Status** tab.
     3. Confirm that your PAL channels are marked with a **P**.
  3. Request a grant on one or multiple PAL channels. Check with your CBSD or DP vendor for instructions about how to request a grant on your PAL channel.
  4. After you request a valid PAL grant from your CBSD, SAS automatically generates a PPA at the next Coordinated Periodic Activities among SASs (CPAS). Any existing grants for other operators' CBSDs on your PAL channel within the PPA are terminated after CPAS. [Learn more about PPAs](https://docs.cloud.google.com/spectrum-access-system/docs/manage-ppa).



A single grant cannot contain both PAL and GAA frequencies. If you need more bandwidth than you have PAL channels, check with your CBSD vendor for instructions about how to request separate grants for the PAL and GAA frequency ranges. Other operators do not protect GAA grants next to a CBSD's PAL grant from interference.

## View the PPA for a PAL-protected CBSD

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. If you have access to multiple organizations, select the organization with the CBSD that you want to review.
  3. [Find your CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/review-configuration).
  4. Click the CBSD.
  5. On the right, click the **Coex** tab.
  6. In the **PAL Protection Areas** section, click the PPAs to view their boundaries.

**Important:** If a PPA is unavailable and you cannot click it, then the PPA doesn't have interference protection from GAA operators. Protection begins after the PAL grant has gone through CPAS. [Learn more about PPAs](https://docs.cloud.google.com/spectrum-access-system/docs/manage-ppa).



## View PALs and PPAs for your PAL counties

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. If you have access to multiple organizations, select the organization with the CBSD that you want to review.
  3. On the left, click _layers_ **Overlays**.
  4. Click the **PAL** tab.
  5. To find all PALs assigned to the county, expand the county folder.
  6. Select a PAL to load and show all PPAs associated with that PAL on the map.



## What's next

  * Learn about [PALs](https://docs.cloud.google.com/spectrum-access-system/docs/pals).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
