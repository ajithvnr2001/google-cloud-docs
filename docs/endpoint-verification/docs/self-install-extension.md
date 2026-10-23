---
url: https://docs.cloud.google.com/endpoint-verification/docs/self-install-extension/
title: Install the Endpoint Verification extension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:08.013535+00:00
---

# Install the Endpoint Verification extension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/self-install-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Install the Endpoint Verification extension Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how employees of an organization can install the Endpoint Verification extension on their devices.

As an employee of an organization, you can access your corporate account on a company-owned device or a personal device. To ensure that you can securely access your organization's data from any of your devices, the administrator of your organization might either install Endpoint Verification on your devices or require you to install the Endpoint Verification Chrome extension on your devices.

## Before you begin

Ensure that your device is running one of the following operating systems:

  * ChromeOS
  * Apple® Mac® OS X® El Capitan (10.11) or later
  * Microsoft® Windows® 10 and 11
  * Linux® Debian® and Ubuntu®



## Install the Endpoint Verification extension

  1. Open the Chrome browser and install the [Endpoint Verification extension](https://chrome.google.com/webstore/detail/endpoint-verification/callobklhcbilhphinckomhgkigmfocg).
  2. On the browser toolbar, if you see Exception ![exception bubble](https://docs.cloud.google.com/endpoint-verification/images/exception.png) on the extension, click the extension to open it.
  3. If prompted, click **Add account** and enter your corporate email address and password.

**Note:** For the devices running ChromeOS, only the account that is used to sign in to the device is supported.

Information about your computer automatically synchronizes to your administrator.

  4. If you want to manually sync information, on the toolbar, click **Endpoint Verification > Sync now**.




## Install the Endpoint Verification helper app

After installing the Endpoint Verification extension, if you see a message that the helper app is required on your device, do the following:

###  Mac or Windows 

  1. Click **Install it**.

  2. Follow the steps to install the helper app.

  3. Click the extension again and then click **Sync now**.




###  Linux 

  1. To open a terminal, click **Activities** and enter `terminal`, and select the terminal icon from the results.

  2. Add the package source and import the key:

     1. Create the `keyrings` directory:
            
            sudo mkdir -m 0755 -p /etc/apt/keyrings/
            

     2. Import Google's public GPG key and convert it to a binary that is required for package verification:
            
            curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/endpoint-verification.gpg
            

     3. Register Endpoint Verification to use the GPG key to verify the authenticity of the software:
            
            echo "deb [signed-by=/etc/apt/keyrings/endpoint-verification.gpg] https://packages.cloud.google.com/apt endpoint-verification main" | sudo tee /etc/apt/sources.list.d/endpoint-verification.list > /dev/null
            

  3. Update and install Endpoint Verification:

     1. Update the package index files to get the latest list of available packages:
            
            sudo apt-get update
            

     2. Install Endpoint Verification:
            
            sudo apt-get install endpoint-verification
            

  4. Open the Chrome browser and on the toolbar, click **Endpoint Verification > Sync now**.




## What's next

  * [Troubleshoot issues with Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/troubleshoot-issues-user)
  * [Uninstall the Endpoint Verification extension](https://docs.cloud.google.com/endpoint-verification/docs/uninstall-ev)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
