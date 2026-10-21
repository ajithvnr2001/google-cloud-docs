---
url: https://docs.cloud.google.com/spectrum-access-system/docs/locations/
title: Areas with limited CBRS spectrum \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:12.086341+00:00
---

# Areas with limited CBRS spectrum  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Resources ](https://docs.cloud.google.com/spectrum-access-system/docs/resources)



Send feedback 

#  Areas with limited CBRS spectrum Stay organized with collections  Save and categorize content based on your preferences. 

Spectrum Access System (SAS) controls access to the Citizens Broadband Radio Service (CBRS) band everywhere in the United States and protects higher-tier users from interference. In certain areas, interference protection requirements might limit the available spectrum. For more information about regions and zones, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## In quiet zones

SAS rejects registration requests from Citizens Broadband Radio Service Devices (CBSDs) located in areas near [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) field offices and federal government facilities because these locations are highly sensitive to interference. Find a full list of these locations in Section 8.14 of [WInnForum Document WINNF-TS-0061](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0061.pdf).

If a device is located within the [National Radio Quiet Zone (NRQZ)](https://greenbankobservatory.org/about/national-radio-quiet-zone/), [confirm the coordination with the NRQZ office](mailto:%20nrqz@gb.nrao.edu) before registration and operation. To confirm successful coordination, a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) must provide the [NRQZ Case ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#nrqz) furnished by the NRQZ office. Learn how to [operate CBSDs in the NRQZ](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-nrqz).

## Near the Canadian border

[Arrangement R between the US and Canada](http://transition.fcc.gov/ib/sand/agree/files/can-nb/Arrangement_R.pdf) restricts CBRS operations from 3650 MHz to 3700 MHz. Within 8 km of the border, CBSD power is limited. Between 8 km and 56 km of the Canadian border, restrictions vary based on the distance from the border, antenna orientation, and power. For more information, see paragraph R2-SGN-19 of WInnForum Document [WINNF-TS-0112](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0112.pdf) and Section 8.13.3.2 of WInnForum Document [WINNF-TS-0061](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0061.pdf).

## Outside the continental US

Due to their proximity to the ocean, many non-contiguous US locations in Hawaii, Alaska, and Guam **except** American Samoa are included in [Dynamic Protection Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) neighborhoods. There is no [Environmental Sensing Capability (ESC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#esc) network to protect these DPAs, so spectrum availability from 3550 MHz to 3650 MHz is restricted. American Samoa has access to the full CBRS spectrum

**Important:** Google does not have immediate plans to deploy ESC devices outside of the contiguous US. We constantly evaluate ESC deployments based on customer needs.

Spectrum is usually available from 3650 MHz to 3700 MHz in Puerto Rico, Hawaii, Alaska, and Guam.

**American Samoa, US Virgin Islands, and Northern Mariana Islands.** SAS is not authorized to provide CBRS service in American Samoa, the US Virgin Islands, and the Northern Mariana Islands per [PNDA-20-110A1](https://docs.fcc.gov/public/attachments/DA-20-110A1.pdf). As a result, registration requests from CBSDs are rejected. Operators with an experimental license (STA) in these areas can contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).

## Near the Mexican border

There are no additional restrictions on CBRS operations near the US border with Mexico.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
