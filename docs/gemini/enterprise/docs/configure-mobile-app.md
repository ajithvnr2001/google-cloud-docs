---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/
title: Configure the mobile app \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:36.922869+00:00
---

# Configure the mobile app  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure the mobile app Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure the Gemini Enterprise mobile app on user devices. Gemini Enterprise app administrator can choose to configure access for users using one of three available methods.

## Overview

As a Gemini Enterprise administrator, you can configure the mobile app for users with one of three methods:

  * You can use a Mobile Device Management (MDM) solution to remotely install and configure the app on user devices. MDM solutions allow admins to complete set up steps prior to delivering apps to users.

  * You can enable a QR code within the Gemini Enterprise web app. Users can then configure the mobile app by scanning this QR code. QR codes can simplify the distribution of access to users and can be used in addition to MDM solutions.

  * You can generate an access link and distribute it to users, which lets them configure the app by opening the link on their mobile devices.


**Note:** MDM configuration overrides all other configuration methods. If you have configured an MDM solution on a device, it takes priority and overrides any attempt by a user to _configure_ the app using a QR code or an access link. In this case, the app displays a message indicating that the configuration is managed. 

The following sections describe the steps required by each method.

## Before you begin

Before you configure the app for users, set up an identity provider for your Gemini Enterprise organization. The Gemini Enterprise mobile app supports the use of Google Identity and third-party identity providers. For more information, see [Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).

**Note:** Signing in with multiple identity providers on a single device can cause authentication conflicts, resulting in an "Incomplete sign-in details" error. If a user encounters this message, they can resolve it by signing out and signing in again. 

## Use a Mobile Device Management (MDM) solution

The Gemini Enterprise administrator panel provides an app URL that contains the parameters required to configure the mobile app in your MDM solution. These parameters map directly to `AppConfig` parameters in the **AppConfig standard** and can be used to configure the app, and enforce security policies.

The following steps use Google Endpoint Management (GEM) as an example of configuring an MDM, but the `AppConfig` parameters should be applicable to other MDM solutions. These steps require access to your MDM administrator console. If you don't have access, contact your organization administrator for next steps.

To configure the app for users in the GEM MDM management solution:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click your app. The **Overview** page displays.

  3. Click **Copy URL** to copy the mobile link. The format of the mobile link differs based on your identity provider.

###  Google Identity 

If your Gemini Enterprise app uses Google as an identity provider, the mobile app URL looks like this:
         
         https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global
         

###  Third-party identity provider 

If your Gemini Enterprise app uses a third-party identity provider, the mobile app URL looks like this:
         
         https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&idp=locations/global/workforcePools/my-pool/providers/my-provider
         

  4. Extract the parameters from the app URL, and use them to fill in the app configuration in your MDM administrator console:

###  Google Identity 

**Deeplink parameter** | **MDM configuration key** | **MDM configuration name** | **Example value**  
---|---|---|---  
`cid` | `config_id` | Configuration ID | `123`  
`cid_location` | `location` | Location | `global`  
  
Leave all other fields empty.

**Note:** When you configure the Android app in Google Endpoint Management (GEM), use the _MDM configuration name_ in the managed configuration form. However, for iOS, manually enter the _MDM configuration key_ with its corresponding value.

For example, the following XML configures an iOS application in GEM:
         
         <dict>
            <key>config_id</key>
            <string>123</string>
            <key>location</key>
            <string>global</string>
         </dict>
         

###  Third-party identity provider 

**Deeplink parameter** | **MDM configuration key** | **MDM configuration name** | **Example value**  
---|---|---|---  
`cid` | `config_id` | Configuration ID | `123`  
`cid_location` | `location` | Location | `global`  
`idp` | `identity_provider` | Identity Provider | `locations/global/workforcePools/my-pool/providers/my-provider`  
`tenant_id` | `tenant_id` | Tenant ID (Deprecated, leave empty) |   
`client_id` | `client_id` | Client ID (Deprecated, leave empty) |   
`project_id` | `project_id` | Project ID (Deprecated, leave empty) |   
  



### Configure citation browser preferences

Gemini Enterprise administrators can use MDM configuration keys to specify how citations and web pages open from Gemini Enterprise mobile sessions.

  * **Open citations in the default browser**

To open citations in the system's default browser using MDM, set the following MDM configuration key:
        
        url_launch_mode = external_browser
        

  * **Open citations in a specific browser**

To force citations to open in a specific browser using MDM, set an additional MDM configuration key:
        
        url_launch_mode = external_browser, preferred_browser = chrome (or edge, or firefox)
        


**Note:** If the specified browser is not installed on the user's device, the citation will automatically open in the system's default browser instead. 

## Enable a QR code on the web app homepage

As a Gemini Enterprise administrator, you can display a QR code on the web app homepage, which allows users to configure the mobile app on their devices by scanning the QR code using their device's camera. This serves as a simpler way to distribute the access link to users.

To manage the configuration QR code visibility:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** and then click the **Feature Management** tab.

  4. Turn on or turn off the **Enable mobile app access** toggle to display or hide the QR code on the web app user's home page.




After the QR code is enabled, users can scan the QR code displayed on their Gemini Enterprise web app using their mobile device to configure and connect the mobile app.

**Note:** If MDM is configured on the user's device, the MDM configuration overrides the QR code setup and displays a message indicating that the configuration is managed. 

To view the QR code on the web app to set up the mobile app:

  1. Open your Gemini Enterprise web app.
  2. Click **Settings & help**.
  3. Click **Mobile login**.
  4. Scan the QR code with your mobile device to sign in to the Gemini Enterprise mobile app.



## Generate an access link

To generate the access link for distribution to Gemini Enterprise mobile app users, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click your app. The **Overview** page displays.

  3. Click **Copy URL** to copy the mobile link. You can then distribute the link to users. The format of the mobile link differs based on your identity provider.

###  Google Identity 

If your Gemini Enterprise uses Google as an identity provider, the mobile app URL looks like this:
         
         https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global
         

###  Third-party identity provider 

If your Gemini Enterprise uses a third-party identity provider, the mobile app URL looks like this:
         
         https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&idp=locations/global/workforcePools/my-pool/providers/my-provider
         


**Note:** If MDM is configured on the user's device, the MDM configuration overrides the access link setup and displays a message indicating that the configuration is managed. 

### Configure citation browser preferences

Gemini Enterprise administrators can use access link parameters to specify how citations and web pages open from Gemini Enterprise mobile sessions.

  * **Open citations in the default browser**

To open citations in the system's default browser with an access link, pass the following parameter in the URL:
        
        url_launch_mode=external_browser
        

  * **Open citations in a specific browser**

To force citations to open in a specific browser with an access link, pass set an additional parameter in the URL:
        
        url_launch_mode=external_browser, preferred_browser=chrome (or edge, or firefox)
        

For example:
        
        https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&url_launch_mode=external_browser&preferred_browser=chrome
        


**Note:** If the specified browser is not installed on the user's device, the citation will automatically open in the system's default browser instead. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
