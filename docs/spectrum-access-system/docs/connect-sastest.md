---
url: https://docs.cloud.google.com/spectrum-access-system/docs/connect-sastest/
title: Connect to the test SAS environment \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:22.541737+00:00
---

# Connect to the test SAS environment  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/connect-sastest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Connect to the test SAS environment Stay organized with collections  Save and categorize content based on your preferences. 

Spectrum Access System (SAS) is fully compatible with the [SAS to Citizens Broadband Radio Service Device (CBSD) communication standards](https://cbrs.wirelessinnovation.org/release-1%20standards-specifications) defined by [WInnForum](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#winforum).

The test SAS environment accepts official CPI certificates issued by a [WInnForum-approved CBRS CA operator](http://cbrs.wirelessinnovation.org/cbrs-root-ca-operators). To get CPI certificates for the test SAS environment, download the [test CPI certificate.zip](https://storage.googleapis.com/support-kms-prod/DCnjTIWKvjWj3f7mLG4SxfT6fOMAMLRPH6Kz) and follow the instructions in the `text_cpi_id_a README.txt` file.

To test the CBSD model with SAS, you need the following:

  * **[Federal Communications Commission (FCC) ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fccid)**
  * **[User IDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#userid)**
  * **CBSD or Domain Proxy (DP) certificates**

Use your production certificates. To obtain test certificates, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).

  * **Certified Professional Installer (CPI) certificate**

SAS provides test CPI certificates, but you can also use the CPI certificate provided by your [Training Program Administrator (TPA)](https://cbrs.wirelessinnovation.org/cpi-program-administrator).

  * **Google account**

The Google account credentials that you use to log in to the SAS Portal.

  * **Root of trust**

The list of Google's test instance root certificate authority (CA) certificates in the CBSD or DP.




To test CBSD in the test SAS environment, use any of the following connection points.

| Connection point  
---|---  
SAS Portal | A web-based application that you use for multistep registration, CPI validation, and for viewing the status of your CBSDs. Access the [test SAS Portal](https://wirelessconnectivity.google.com/test-sas/).  
SAS Portal API | A set of APIs that you can use to integrate your application with SAS. For more information, see the [SAS API documentation](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).  
SAS-CBSD API Base URL | A URL to connect your CBSDs to communicate with SAS. The entry points for each type of request are as follows: `https://test.sas.goog/v1.2/registration` `https://test.sas.goog/v1.2/spectrumInquiry` `https://test.sas.goog/v1.2/grant` `https://test.sas.goog/v1.2/heartbeat` `https://test.sas.goog/v1.2/relinquishment` `https://test.sas.goog/v1.2/deregistration`  
  
## What's next

  * Learn about [Google's PAL interoperability test suite](https://docs.cloud.google.com/spectrum-access-system/docs/pal-iottest).
  * Learn about [CBSD interoperability with Google SAS](https://docs.cloud.google.com/spectrum-access-system/docs/sas-iottest).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
