---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started/
title: Getting started \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:09.129180+00:00
---

# Getting started  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Getting started Stay organized with collections  Save and categorize content based on your preferences. 

Integrate Contact Center AI Platform (CCAI Platform) capabilities into your web application using the web SDK. The web SDK builds on the [headless web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide), making all headless client methods available in the web SDK widget. This page shows you how to mount, initialize, and authenticate the web SDK. It also explains how to hide buttons and commands to start new conversations and download transcripts.

For help installing the web SDK, see the [implementation examples](https://github.com/GoogleCloudPlatform/ccaas-web-sdk-v3-examples) in GitHub.

## Basic example

The basic example requires only 3 options:

  1. `companyId`
  2. `host`
  3. `Authenticate`



Follow widget documentation to get your company ID and host.

### Full HTML
    
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Basic demo</title>
    </head>
    <body>
      <!-- An empty element to mount the CCAI Platform web SDK widget. -->
      <div id="ccaas-widget"></div>
    
      <!-- Include the CCAI Platform web SDK widget -->
      <script src="https://{your_ccaas_host}web-sdk/v3/widget.js"></script>
      <script>
        var ccaas = new UJET({
          companyId: "$COMPANY_ID",
          host: "$HOST",
          authenticate: getAuthToken
        });
        ccaas.mount("#ccaas-widget");
    
        function getAuthToken() {
          // YOU SHOULD HAVE THIS KIND OF API ON YOUR SERVER
          return fetch('/auth/token').then(function(resp) {
            // { token: 'a JWT contains user identifier, name, and email' }
            return resp.json();
          });
        }
      </script>
    </body>
    </html>
    

## Custom data example

The custom data example is similar to the basic example. You need to configure the custom data with `.config({ customData })`.

### Full HTML
    
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Custom Data demo</title>
    </head>
    <body>
      <!-- An empty element to mount the CCAI Platform web SDK widget. -->
      <div id="ccaas-widget"></div>
    
      <!-- Include the CCAI Platform web SDK widget -->
      <script src="https://{your_ccaas_host}web-sdk/v3/widget.js"></script>
      <script>
        var ccaas = new UJET({
          companyId: "$COMPANY_ID",
          host: "$HOST",
          authenticate: getAuthToken
        });
    
        // use `.config` to configure custom data.
        ccaas.config({
          customData: {
            version: {
              label: 'Version',
              value: '1.0.0'
            }
          }
        });
        ccaas.mount("#ccaas-widget");
    
        function getAuthToken() {
          // YOU SHOULD HAVE THIS KIND OF API ON YOUR SERVER
          return fetch('/auth/token').then(function(resp) {
            // { token: 'a JWT contains user identifier, name, and email' }
            return resp.json();
          });
        }
      </script>
    </body>
    </html>
    

## Preparation

To get the Contact Center AI Platform Web SDK up and running, do the following:

  1. Include the web SDK widget script.

  2. Prepare a mount element.

  3. Initialize the web SDK with your `COMPANY_KEY`

  4. Initialize authentication with your `COMPANY_SECRET` using your backend code
         
         <!-- an empty element to mount the web SDK -->
         <div id="ccaas-widget"></div>
         
         <script src="https://{your_ccaas_host}web-sdk/v3/widget.js"></script>
         <script>
           // const ccaas = new UJET({ ... })
         </script>
         


**Tip:** If your production server has a content security policy, add `https://{your_ccaas_host}` to your `script-src` and `frame-src.`

## Get company key

  1. Sign into the Contact Center AI Platform portal using an account with administrator permissions.

  2. Go to **Settings > Developer Settings**.

  3. Copy the Company Key as `COMPANY_KEY`.




You can also get the company secret here. The secret is used in your backend server to create an authentication token endpoint. For more information see the [Authenticate](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-authenticate) section.

## Initializing

You can then initialize the CCAI Platform web SDK with the new `UJET(options)` method. If your portal is `https://{your_ccaas_host}`, then the host is
    
    
    https://{your_ccaas_host}:
    const ccaas = new UJET({
      companyId: "{COMPANY_KEY}",
      host: "https://{your_ccaas_host}",
      authenticate: getAuthToken,
    });
    

The options are the same as the [Headless web SDK Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide).

## Authentication

The `getAuthToken` is a function that calls upon a JWT signing mechanism from your backend:
    
    
    async function getAuthToken() {
      // YOU SHOULD HAVE THIS KIND OF API ON YOUR SERVER
      const resp = await fetch('/auth/token')
      const data = await resp.json()
      return { token: data.token }
    }
    

For more information see the [Authenticate](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-authenticate) section.

## Configure the SDK

Configure the web SDK using `ccaas.config({...})`.

The following code lists the properties for configuring the web SDK:
    
    
    export interface ConfigOptions {
      name?: string
      accent?: 'default' | 'blue' | 'green' | 'purple' | 'orange' | 'yellow' | 'gold' | 'red'
      logo?: string
      menuKey?: string
      ticketId?: string
      preferredChannel?: string
      disableAttachment?: boolean
      customData?: Record<string, any>
      signedCustomData?: string
      messages?: Record<string, unknown>
      disableLauncher?: boolean
      launcherOpenIcon?: string
      launcherCloseIcon?: string
      launcherLoadingIcon?: string
      optionsMenuIcon?: string
      confirmationIcon?: string
      enableMuteChat?: boolean
      tooltipIcon?: string
      hideNewConversation?: boolean
      hideDownloadTranscriptOptions?: boolean
      hideDownloadTranscriptPostChat?: boolean
    }
    

For more information, see [Supported Features](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-supported-features) and [Theme Customizations](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-theme-customization).

### Hide the button to start a new conversation at the end of a session

You can configure the web SDK to hide the **Start a new conversation** button in an end-user's chat window at the end of a session. To do this, include the `hideNewConversation` property with the `ccaas.config` method. For more information, see Configure the SDK.

### Hide the command to download a transcript during a session

You can configure the web SDK to hide the **Download transcript** command from the chat options menu in the end-user's chat window during a session. To do this, include the `hideDownloadTranscriptOptions` property with the `ccaas.config` method. For more information, see Configure the SDK.

### Hide the button to download a transcript at the end of a session

You can configure the web SDK to hide the **Download transcript** button in the end-user's chat window at the end of a session. To do this, include the `hideDownloadTranscriptPostChat` property with the `ccaas.config` method. For more information, see Configure the SDK.

## Mount the widget

It is required to prepare an empty element at the beginning:
    
    
    <div id="ccaas-widget"></div>
    

Then, we can mount the widget into this element:
    
    
    ccaas.mount('#ccaas-widget')
    

Use the [Headless web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide) to create your own chat and call widgets.

## Install

**Note:** If your production server has a content security policy, add `https://{your_ccaas_host}/` to your `frame-src`.

You can install the package with npm:
    
    
    npm install @ujet/websdk-headless --save
    

Or, you can use the script hosted on your CCAI Platform instance:
    
    
    <script src="https://{your_ccaas_host}/web-sdk/v3/headless.js"></script>
    
    <script>
      // const client = new HeadlessClient(...)
    </script>
    

## Integrate the SDK

  1. Sign into the Contact Center AI Platform portal using an account with administrator permissions.

  2. Go to **Settings > Developer Settings**.

  3. Copy the company key as `COMPANY_KEY`.




If your portal is `https://{your_ccaas_host}`, here is an example to get the company information:
    
    
    import { Client } from "@ujet/websdk-headless"
    
    async function authenticate() {
      const resp = await fetch("/your-auth-endpoint")
      const data = await resp.json()
      return { token: data.token }
    }
    
    const client = new Client({
      companyId: "COMPANY_KEY",
      host: "https://{your_ccaas_host}",
      authenticate: authenticate,
    })
    
    const company = await client.getCompany()
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
