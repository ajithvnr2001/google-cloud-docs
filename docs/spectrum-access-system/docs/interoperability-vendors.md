---
url: https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors/
title: CBSD interoperability testing overview \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:34.070017+00:00
---

# CBSD interoperability testing overview  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/interoperability-vendors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  CBSD interoperability testing overview Stay organized with collections  Save and categorize content based on your preferences. 

Interoperability testing helps you ensure that a Citizens Broadband Radio Service Device (CBSD) model and its software version work well with Spectrum Access System (SAS). We recommend that you, as a CBSD vendor, complete interoperability testing on the test SAS environment before proceeding with the production SAS environment.

## Test and production SAS environments

The test environment is free to use. You can use the test environment for the following types of testing:

  * CBSD interoperability
  * API integration
  * Simulated or pre-production deployments by customers, vendors, and integrators



To access the test environment, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).

**Important:** This test environment is not [Part 96](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-96) compliant and cannot be used for commercial purposes.

The test environment does not moderate live traffic in the Citizens Broadband Radio Service (CBRS) spectrum, but the production environment does. However, the production environment is only available to SAS customers.

The following table highlights the _differences_ between the test and production SAS environments.

| Test SAS environment | Production SAS environment  
---|---|---  
SAS Portal URL | <https://wirelessconnectivity.google.com/test-sas> | <https://wirelessconnectivity.google.com/sas> <https://g.co/sasportal>  
SAS URL for CBSD communications | `https://test.sas.goog/v1.2/` | `https://sas.goog/v1.2/`  
SAS Portal API base URL | `https://test-sasportal.googleapis.com/` | `https://sasportal.googleapis.com/v1alpha1/`  
Federal Communications Commission (FCC) IDs | Lets you use certified and non-certified CBSDs. To allowlist the [FCC IDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc-id) of non-certified equipment, contact [Google SAS Support](mailto:sas-support@google.com). | Accepts only FCC-certified CBSDs.  
SAS certificates | In CBSD or Domain Proxy (DP), the root CA certificate of the Google test instance _must_ be listed as a root of trust. | All [WInnForum root CA certificates](https://cbrs.wirelessinnovation.org/cbrs-root-ca-operator/) _must_ be listed as roots of trust in the CBSD or [DP](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dp).  
CBSD certificates | SAS accepts the following certificates: 

  * Official certificates issued by [WInnForum-approved CBRS CA operators](https://cbrs.wirelessinnovation.org/cbrs-root-ca-operators).
  * Google test CBSD certificates issued by [Google SAS Support](mailto:sas-support@google.com).

| SAS accepts _only_ the official certificates issued by [WInnForum-approved CBRS CA operators](https://cbrs.wirelessinnovation.org/cbrs-root-ca-operators).  
Certified Professional Installer (CPI) | SAS accepts requests from the following CPIs: 

  * CPIs accredited by [approved CPI Training Program Administrators (TPAs)](https://cbrs.wirelessinnovation.org/cpi-program-administrator).
  * Google test [CPI](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) credentials issued by [Google SAS Support](mailto:sas-support@google.com).

| SAS only accepts requests from CPIs accredited by [approved CPI TPAs](https://cbrs.wirelessinnovation.org/cpi-program-administrator). If SAS rejects your CPI credentials, then contact your TPA to confirm that your credentials are valid and have been uploaded to the WInnForum CPI database.  
Grant authorization | Grants are authorized for test purposes only. Protected entities are enforced based on the specifications for termination and suspension zones in the test plan. | Grants are authorized to transmit according to the FCC regulations. Grant authorization protects higher-tier usage in the band in accordance with the [specifications of termination and suspension zones in the test plan](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#validateinterop).  
Protected entities | Entities such as simulated termination and suspension zones are protected according to FCC regulations. | All entities are protected according to FCC regulations. However, grant requests are rejected inside exclusion zones and might require grant adjustments or suspensions.  
[Coordinated Periodic Activities among SASs (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas) | Runs once a day from 7:00 AM to 8:30 AM UTC. | Runs once a day from 7:00 AM to 10:00 AM UTC.  
Dynamic Protected Areas (DPAs) | [DPAs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) are inactive _except_ for Guam, Hawaii, and Puerto Rico. They might be activated periodically and without notice to facilitate device testing. | DPAs are activated based on incumbent activity detected by [Environmental Sensing Capability (ESC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#esc) sensors. In areas where ESC sensors are not deployed, DPAs remain active.  
  
## What's next

  * Learn about the [PAL interoperability test suite](https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest).
  * Learn about [CBSD interoperability with Google SAS](https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
