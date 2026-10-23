---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability/
title: CBRS spectrum availability \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:13.186604+00:00
---

# CBRS spectrum availability  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  CBRS spectrum availability Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Maps interface in the Google Spectrum Access System (SAS) Portal to understand spectrum availability in the United States. This functionality includes [Dynamic Protection Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) neighborhood borders and Citizens Broadband Radio Service (CBRS) spectrum availability heatmaps.

## DPA neighborhood borders

DPA neighborhood borders show if your CBSD is in a DPA neighborhood. The CBSD in a DPA neighborhood might experience periodic grant suspensions due to incumbent activity on one or several channels in the lower 100 MHz of CBRS. [Learn how to operate CBSDs near the coast](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast).

To check if a CBSD is inside a DPA neighborhood, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Select the deployment, and then click **Open**.
  3. Click _map_ **Map view** , and then click _layers_ **Overlays**.
  4. Select a **DPA Neighborhood** overlay to display the corresponding DPA neighborhood border on the map.
  5. On the map, check if your CBSD falls within the DPA neighborhood border.



## CBRS heatmaps

CBRS heatmaps help you to determine how many channels are available in an area before you deploy a CBSD. Heatmaps assess general spectrum availability before the deployment, while the spectrum inquiry response from SAS to a CBSD shows which channels are available for that CBSD based on its current registration parameters.

CBRS heatmaps provide a granular and visual overview of spectrum availability from the 3550 MHz to 3700 MHz band in the United States.

CBRS heatmaps account for all types of Tier 1 ([incumbent user](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#incubment)) activity, which includes the following:

  * Specialized sensors such as [Environmental Sensing Capability (ESC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#esc) devices
  * In-band DPAs with pending ESCs deployment
  * Out-of-band DPA protection
  * [GB-DPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gbdpa) protection
  * Fixed satellite service (FSS)
  * US borders
  * Quiet zones, such as the [National Radio Quiet Zone (NRQZ)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#nrqz) and the [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc)
  * Exclusion zones
  * Table mountain



CBRS heatmaps _don't_ account for the following activity:

  * Temporary channel suspensions due to incumbent activity within in-band DPAs that include [E-DPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#edpa).
  * Interference caused by existing CBSDs.



CBRS heatmaps show the spectrum availability for a CBSD with the following configuration:

  * Category A CBSD: uses a zero-gain omnidirectional antenna, which is mounted outdoors and five meters above ground.
  * Category B CBSD: has the same characteristics as a Category A CBSD but is mounted 25 meters above ground.

**Note:** In both the categories, the CBSD is supposed to be the first CBSD deployed in the area.
  * Heatmaps are intended as a guide to channel availability. The CBSDs that are deployed are not considered in this calculation. The spectrum availability might be lower in congested areas where SAS protects incumbents.

  * Heatmaps show how many full-power 10-MHz channels are available for the first CBSD in the area within 48 hours of deployment.




To find how many channels are available, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Select the deployment, and then click **Open**.
  3. Click _map_ **Map view** , and then click _layers_ **Overlays**.
  4. Select **Spectrum availability (Cat. A)** or **Spectrum availability (Cat. B)**.
  5. On the map, search for a location.
  6. In the **Spectrum availability** section, select the channels that are available within 48 hours.



When you click anywhere on the map, it provides the location details such as elevation, clutter, height, and spectrum availability for Category A and Category B CBSD.

Spectrum availability information is also provided for every CBSD registered with the SAS Portal. This information represents the result of a real-time spectrum inquiry request for each CBSD. You can view this information on the **Config** tab of the SAS Portal.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
