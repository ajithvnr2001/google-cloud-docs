---
url: https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools/
title: Deploying the Endpoint Verification native helper with third-party tools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:58.335663+00:00
---

# Deploying the Endpoint Verification native helper with third-party tools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-third-party-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)



Send feedback 

#  Deploying the Endpoint Verification native helper with third-party tools Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deploy the Endpoint Verification native helper to Apple Mac and Microsoft Windows devices within your organization with Jamf and Active Directory.

## Deploying to Apple Mac with Jamf

Note that this method requires your macOS devices to be managed with [Jamf](https://www.jamf.com/products/jamf-now/).

  1. Download the native helper `.dmg` package [here](https://dl.google.com/dl/secureconnect/install/mac/EndpointVerification.dmg).
  2. Mount the `.dmg` and extract `EndpointVerification.pkg`.
  3. Log in to [Jamf Now](https://www.jamf.com/products/jamf-now/).
  4. Click the **Apps** tab.
  5. Click **Add an App**.
  6. Click **Upload Your App**.
  7. Drag your custom `.pkg` file onto the upload page or click **Browse** to search for it on your computer.



The file now appears in the Apps page and is ready for deployment with Blueprint.

See the [Jamf MacOS deployment guide](https://support.jamfnow.com/s/article/360015973211-Tutorial-Deploying-macOS-packages) for more information.

## Deploying Microsoft Windows with Active Directory

By creating a Group Policy Object (GPO) with Microsoft Windows Active Directory, you enable additional controls over management and operating system configuration for user devices'. A GPO is a collection of settings you can create.

  1. Create a distribution point.

     1. Create a shared network folder.
     2. Download the [Endpoint Verification MSI](https://dl.google.com/secureconnect/install/win/EndpointVerification_admin.msi).
     3. Add the MSI to your shared folder.
  2. Create a GPO for your package.

     1. Click **Start > Go to Start > Group Policy Management**.
     2. From the left-hand panel select `Forest: [Your forest] > Domains > [Your domain]`.
     3. Right-click on **Group Policy Objects** and select **New**.
     4. Enter a name for your policy.
  3. Assign the Endpoint Verification package. A package can be assigned per-user or per-machine.

     1. Click your new policy.
     2. Click the **Settings** tab.
     3. In the panel that appears, right-click anywhere and select **Edit**.
     4. Select **User Configuration > Policies > Software Settings**.
     5. Right-click **Software Installation** and select **New > Package**.
     6. Select the Endpoint Verification package from your shared network folder.
     7. In the **Deploy Software** dialog that appears select **Assigned**
     8. Click **OK**.

Your package now appears in the **Software Installation** panel.

  4. Deploy the Endpoint Verification package.

     1. Double-click your Endpoint Verification package to open properties and select the **Deployment** tab.
     2. Select **Install this application at logon** and **Basic**.
     3. Click **OK**.
     4. Close the **Group Policy Management Editor** window and return to the **Group Policy Management** window.
     5. Right-click your domain name in the tree and select **Link an Existing GPO?**.
     6. Select your policy with the package and click **OK**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
