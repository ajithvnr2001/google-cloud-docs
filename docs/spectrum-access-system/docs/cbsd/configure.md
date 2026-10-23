---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure/
title: Configure a CBSD \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:59.746312+00:00
---

# Configure a CBSD  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Configure a CBSD Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up a Citizens Broadband Radio Service Device (CBSD) configuration.

Before a new CBSD starts transmitting, it needs to register with Spectrum Access System (SAS) and send information about its physical installation such as the radio model, location, and antenna parameters.

## Registration prerequisites

Some CBSDs only support multistep registration and therefore must be pre-configured in the Google SAS Portal or by using the Google SAS Portal API.

Single-step registration is when a [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) provides device registration information to SAS in the registration request from the CBSD. For registration instructions that are specific to your CBSD, see your CBSD vendor documentation.

Only [Federal Communications Commission (FCC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc)-approved CBSDs in compliance with FCC Part 96 can be registered with SAS. Most Category A and all Category B CBSDs require a CPI to verify the device's installation.

Category A CBSDs that meet at least one of the following conditions require a CPI validation:

  * The CBSD does not automatically determine its location.
  * The CBSD operates outdoors with an antenna height above average terrain (HAAT) of more than six meters. This type of CBSD must be registered as a Category B device.



## Use multistep registration

The following sections describe how to use multistep registration to register a CBSD.

### Configure installation parameters

To configure the installation parameters, follow these steps:

  1. Create a [CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/portal#cbsd-config) by using the SAS Portal or the SAS Portal API.
  2. Import a CBSD by using the SAS Portal to create, sign, and update multiple CBSD configurations. For more information, see [Import the CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations).
  3. Configure the installation parameters: 
     * **Editors or admins only** : On the right, enter the installation parameters.
     * **CPIs** : Click **Sign device directly** or, to save as a draft, click **Save**.

**Note:** To configure parameters, you can use either the **Map view** or **Table view**. For more information, see [Register a CBSD that needs CPI validation](https://docs.cloud.google.com/spectrum-access-system/docs/portal#register-cbsd).

### Sign the installation parameters

To sign off on the installation parameters, you must be a CPI and have [verified your CPI identity in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/validate-cpi-certification). To get CPI privileges, contact your administrator.

### Register the CBSD to SAS

The steps to connect a CBSD with SAS might be different for each CBSD model. Check with your device vendor for documentation or instructions. Google SAS combines the information from the Google SAS Portal to process the registration request from the CBSD. If the registration request is successful, SAS responds with a CBSD ID. The CBSD is registered and can now request a grant.

If SAS rejects the registration request, it responds with an error message. The CBSD needs to correct the error and send another registration request.

**Tip:** For additional help, watch our [Getting Started videos on YouTube](https://www.youtube.com/watch?v=ly3H9_28COU).

The SAS portal rejects registration requests for any CBSD configurations that are already signed. You must enter CBSD parameters into the SAS Portal including the user ID, FCC ID, and the serial number.

## Register your CBSD

You can register your CBSD by using the Google SAS Portal or, if you are using Baicells equipment, by using Baicells.

### Use the SAS Portal

If you are using the SAS Portal to configure installation parameters, follow these steps:

  1. Enter the installation parameters for a CBSD configuration.
  2. Optional: If you aren't a CPI, click **Save** to save the draft of the CBSD configuration.
  3. Click **Ready for CPI** to indicate that you're finished with the configuration.
  4. After the CBSD configuration is signed by the CPI, a registration request can be sent from the device to Google SAS.
  5. If the registration request is successful, the CBSD is registered.



### Use Baicells

If you are using Baicells equipment to configure installation parameters, follow these steps:

  1. Configure the CBSD in Baicells.
  2. Export the CBSD configuration from Baicells as a CSV file.
  3. To complete Step 1, configure the installation parameters and import this CSV file into the Google SAS Portal.
  4. To complete Step 2 of the multistep registration, go back to Baicells, select the CBSD, and then send the registration request.



## What's next

  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
