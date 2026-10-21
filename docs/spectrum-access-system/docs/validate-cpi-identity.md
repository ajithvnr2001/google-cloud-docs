---
url: https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-identity/
title: Validate CPI identity \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:28.941570+00:00
---

# Validate CPI identity  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Validate CPI identity Stay organized with collections  Save and categorize content based on your preferences. 

According to the WInnForum requirements, certain Citizens Broadband Radio Service Devices (CBSDs) require that a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) validate the installation parameters _before_ they are sent to Spectrum Access System (SAS).

[ ![CPI identity validation flow](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/user-with-role-cpi.svg)](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/user-with-role-cpi.svg) CPI identity validation flow (click to enlarge)

In the Google SAS Portal API, validate that a given user has a valid CPI certification before they call the [`SignDevice()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices/signDevice). You can validate a user's CPI certification by using the following validation method:

  1. Make sure that the user is signed in with their Google Account, and the traffic uses HTTPS.
  2. A [`role_cpi`](https://docs.cloud.google.com/spectrum-access-system/docs/roles-and-permissions#cpi) user calls the [`GenerateSecret()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/installer/generateSecret), which returns a [secret](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#secret) in the form of a token.
  3. The user then signs the secret with their private key and uses the [`ValidateInstaller()` method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/installer/validate) to send the encoded version back as a [JSON Web Token (JWT)](https://jwt.io/), along with their CPI ID and the original secret. For more details about token creation, see [JSON Web Token format](https://docs.cloud.google.com/spectrum-access-system/docs/json-web-token-format).



The CPI role permissions become effective only after a user with the `role_cpi` role successfully completes the CPI validation flow.

## What's next

  * To get an overview of the SAS Portal API, see [Google SAS Portal API overview](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).
  * For information about each API, see [Customers API](https://docs.cloud.google.com/spectrum-access-system/docs/customers-api) and [Device Manager API](https://docs.cloud.google.com/spectrum-access-system/docs/device-manager-api).
  * For examples of how to use the API, see [API code samples](https://docs.cloud.google.com/spectrum-access-system/docs/samples).
  * For reference documentation, see [APIs and reference](https://docs.cloud.google.com/spectrum-access-system/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
