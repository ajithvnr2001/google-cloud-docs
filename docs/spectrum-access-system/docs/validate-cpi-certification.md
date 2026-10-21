---
url: https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-certification/
title: Validate CPI certification \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:28.749756+00:00
---

# Validate CPI certification  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-certification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Validate CPI certification Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to validate [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) certification in the Google Spectrum Access System (SAS) Portal. If you are a CPI, you must verify your identity in the SAS Portal and sign off on [Citizens Broadband Radio Service Device (CBSD)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) configurations.

## Before you begin

Make sure that you have the following:

  * CPI ID
  * CPI certificate file
  * CPI certificate password



## Verify your identity as a CPI

Make sure that you verify your CPI identity periodically to show that your credentials are still valid. To verify your identity as a CPI, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. On the left, click **SAS Portal**.
  3. Select a network deployment, and then click **Open**.
  4. On the right, select your Google Account, and then click **Verify CPI identity**.
  5. Enter your **CPI ID** , **Certificate** , and **Certificate password**.
  6. Click **Verify**.

The SAS Portal validates that you are a CPI by encoding a random string that uses your certificate file and password. It also decodes the string with the corresponding public key in the [WInnForum CPI database](https://cbrs.wirelessinnovation.org/). The validation takes place locally in the browser, so your certificate file stays on your computer.

  7. After your CPI identity is verified, repeat step 4 and sign off on any additional CBSD configurations.




## What's next

  * [Register a CBSD that needs CPI validation](https://docs.cloud.google.com/spectrum-access-system/docs/portal#register-cbsd).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
