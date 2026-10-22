---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade/
title: Upgrade from web SDK version 2 to web SDK version 3 \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:42.983634+00:00
---

# Upgrade from web SDK version 2 to web SDK version 3  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Upgrade from web SDK version 2 to web SDK version 3 Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to upgrade from web SDK version to 2 web SDK version 3. If you're installing the web SDK for the first time, see [Web SDK v3 Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-guide).

**Important:** The installation and utilization of our headless SDK require the support of your organization's engineering team.

## Web SDK v3 capabilities

Here are some web SDK v3 capabilities that don't exist in web SDK v2:

  * **Custom forms** : Agents can send custom data collection forms directly within the web chat interface. For more information, see [Data collection forms](https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-collection-forms).

  * **Downloadable transcripts** : Let end-users download their chat transcripts directly from the widget. For more information, see [Download chat transcripts using the web SDK and mobile SDKs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#download_chat_transcripts_using_the_web_sdk_and_mobile_sdks).

  * **Advanced proactive chat triggers** : Use advanced proactive chat triggers—for example, specifying the queue language or using complex AND-OR logic for URL keywords. For more information, see [Proactive Web SDK Triggers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/proactive-web-sdk-triggers).




## Upgrade to web SDK v3

First, locate this script within your source code:
    
    
    <script type="module" src="https://websdk.ujet.co/v2/loader.js"></script>
    

Then, replace it with the following:
    
    
    <script type="module" src="https://{your_ccaas_host}/web-sdk/v3/widget.js"></script>
    

## Notable differences

The web SDK v3 is built directly on top of the UJET headless client. Because the widget UI uses this headless structure, you can access and call all the underlying methods and listen to events that the Headless SDK supports by targeting `ccaas.client`.

This section outlines key differences between version 2 and 3 of the web SDK.

### Initialize

**Note:** V2 uses the exact same initialization as v3.

#### v2
    
    
    const ccas = new UJET({
      "companyId": "{companyId}",
      "host": "https://{your_ccaas_host}",
      "authenticate": getAuthToken
    })
    

#### v3
    
    
    var ccas = new UJET({
      "companyId": "{companyId}",
      "host": "https://{your_ccaas_host}",
      "authenticate": getAuthToken
    })
    
    // v3 has a mount point
    // ccaas.mount(HTMLElement | string)
    ccaas.mount('#ccaas-widget')
    

### Options

When you initiate the web SDK, you specify options. This section describes the differences between version 2 and 3 of the web SDK.

#### v2

N/A for v2.

#### v3

In v3, the initialization options are the same as the Headless SDK.
    
    
    interface ClientOption {
      companyId: string;
      authenticate: () => Promise<TokenResponse>;
      tenant?: string;
      host?: string;
      lang?: string;
      bridge?: string;
      cobrowse?: {
        enabled: boolean;
        template?: string;
        messages?: CobrowseMessages;
        api?: string;
        license?: string;
        trustedOrigins?: string[];
        capabilities?: string[];
        registration?: boolean;
        redactedViews?: string[];
        unredactedViews?: string[];
      };
    }
    

**Important:** With web SDK v3, certain options from v2, such as `customData` and `disableAttachment` are now included in the `ccaas.config()` option.

Extra options can be configured with `ccaas.config()` method:
    
    
    ccaas.config({
      disableAttachment: true
    })
    

Available config options:
    
    
    interface ConfigOptions {
      accent?: AccentColor;
      logo?: string;
      menuKey?: string;
      ticketId?: string;
      preferredChannel?: string;
      disableAttachment?: boolean;
      customData?: string | Record<string, any>;
      messages?: Record<string, unknown>;
      reCaptchaSiteKey?: string;
    }
    

### Methods

In v2, there are a few extra methods on the loader, such as:
    
    
    ccaas.createCobrowseCode()
    ccaas.fetchWaitTimes({id: 123})
    

In v3, the widget UI is using a headless client, you can call all methods that the Headless SDK supports.
    
    
    const client = ccaas.client
    client.getCompany()
    client.loadOngoingChat()
    

See [Headless web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide) to learn more.

### Events

In v2, you can listen to events with:
    
    
    ccaas.on('chat:update', (chat) => {
      console.log(chat)
    })
    

In v3, you can listen to events with the headless client:
    
    
    const client = ccaas.client
    
    client.on('chat.updated', (chat) => {
      console.log(chat)
    })
    

See [Headless web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide) to learn about more events.

### Theme customization

Web SDK v3 has an updated approach to theme customization. For more information, see [Theme customization](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-theme-customization).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
