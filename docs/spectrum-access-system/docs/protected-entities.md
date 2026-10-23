---
url: https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities/
title: Simulated protected entities in the test SAS environment \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:13.773041+00:00
---

# Simulated protected entities in the test SAS environment  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/protected-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Simulated protected entities in the test SAS environment Stay organized with collections  Save and categorize content based on your preferences. 

You can test the interoperability of your Citizens Broadband Radio Service Device (CBSD) with Spectrum Access System (SAS) and simulate different types of [incumbents](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#incubment).

To do this, the test SAS environment offers the following:

  * [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) regulations
  * A suspension zone
  * [Priority Access License (PAL)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#pal) testing zones
  * A [termination zone](https://docs.cloud.google.com/spectrum-access-system/docs/termination-zone)
  * A Grandfathered Wireless Protection Zone (GWPZ)



## Suspension zone

The test SAS environment provides a suspension zone to help with testing scenarios related to grant requests, grant authorization, and grant suspension. This zone is defined as a rectangle with corners at the following [locations](https://storage.googleapis.com/support-kms-prod/7FEG4C0UNXaVWxdW9dm0kl2JvGE8QWE8cvKR):

  * 63° North, -156° East
  * 62° North, -156° East
  * 62° North, -155° East
  * [63° North, -155° East](https://storage.googleapis.com/support-kms-prod/hBKwPcVsRNwcAA0uQGDIA3uTMlfVrJO3joXJ)



The frequency range associated with the suspension zone is from 3550 MHz to 3620 MHz. All grants, whether partially or fully overlapping this frequency range, are affected by the suspension zone. The zone is active every hour between 5–10, 15–25, and 35–50 minutes past the hour—for example, from 12:05 PM to 12:10 PM, 12:15 PM to 12:25 PM, and 12:35 PM to 12:50 PM.

## PAL testing zones

The test SAS environment provides zones to support PAL testing. The equipment manufacturers receive information by email about the zone where the testing takes place. SAS customers can only perform PAL testing _after_ their official PAL assignments are made public.

Some tests require a [CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsdconfig) with the intermittent PAL [user ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid) called `test_pal_user_id`. This ID is a special user ID that results in intermittent, scheduled PAL behavior in specific geographic areas in the test environment. During certain times of the day, CBSDs registered with `test_pal_user_id` are PAL-qualified. At other times, these CBSDs act as [GAA-only](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#gaaonly).

The time schedule for the intermittent PAL user ID is as follows:

  * Between 14:30 to 22:30 UTC, no PALs are associated with `test_pal_user_id`.
  * At all other times of the day, the ID is linked with test PALs in specific South Dakota counties.



## Termination zone

The test SAS environment provides a periodic termination zone for testing purposes. This zone is defined as a rectangle with corners at the following [locations](https://storage.googleapis.com/support-kms-prod/S3Jl4c3vmgwPUPrMm2yhzPth7LIPHZjOyLon):

  * 67° North, -159° East
  * 66° North, -159° East
  * 66° North, -158° East
  * [67° North, -158° East](https://storage.googleapis.com/support-kms-prod/j73kOT0oaNlFBodFj6Z01NdxyHbOCyXZgTbX)



The frequency range associated with the termination zone is from 3550 MHz to 3620 MHz. All grants partially or fully overlapping this frequency range are affected by the zone. The termination zone is active every hour between 5–10, 15–25, and 35–50 minutes past the hour—for example, 12:05 PM to 12:10 PM, 12:15 PM to 12:25 PM, and 12:35 PM to 12:50 PM.

For CBSDs that have grants and are registered inside the termination zone, SAS terminates _all_ active grants that partially or fully overlap with the 3550 MHz to 3620 MHz frequency range at 5, 15, and 35 minutes after every hour. SAS also suggests a new frequency range from 3620 MHz to 3700 MHz in the heartbeat response, which notifies the CBSD of grant termination. For example, if the CBSD starts at minute 0 (zero), it receives a grant and a heartbeat. At 5 minutes past the hour, SAS terminates the grant. The next heartbeat response contains `responseCode 500` (`Terminated_grant`) and the suggested operation parameters.

The following example shows a response:
    
    
    "operationParam": {
       "operationFrequencyRange": {
         "lowFrequency": 3620000000,
         "highFrequency": 3700000000
        }
    }
    

While the termination zone is active, any requested grants that partially or fully overlap with the 3550 MHz–3620 MHz frequency range are automatically rejected. This facilitates verification of correct CBSD behavior through observation of the radio frequency output.

## GWPZ

An example of GWPZ defined in the test SAS environment is available as a circle centered at [70° North, -162° East](https://storage.googleapis.com/support-kms-prod/ntHGf4LYG3aDoDdu5VlFhMS1jVCRUa0t5jQd) with a radius of 18 km.

The frequency range associated with the GWPZ is from 3650 MHz to 3700 MHz. Unlike the other zones described in the test plan, the GWPZ is _always_ protected from interference.

## What's next

  * Learn about [PAL interoperability test suite](https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest).
  * Learn about [CBSD interoperability with SAS](https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
