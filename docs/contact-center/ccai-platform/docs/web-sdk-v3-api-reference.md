---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-api-reference/
title: API reference \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:30.665294+00:00
---

# API reference  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-api-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  API reference Stay organized with collections  Save and categorize content based on your preferences. 

The interface of the `ccaas` web SDK instance.

## Properties

This section contains some of the properties you might use.

### version

The version of the web SDK.
    
    
    console.log(ccaas.VERSION)
    

### client

This is an instance of the [Headless client](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide), it contains everything available on a headless client.

Here is an example:
    
    
    const client = ccaas.client
    const chat = await client.loadOngoingChat()
    

## Methods

Available methods on the widget instance.

### .config

Update the configuration of the widget.
    
    
    ccaas.config({
      accent: 'green'
    })
    

For more information see the [Configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#configuration-web-sdk) section.

### .mount

Mount the widget on the given element. For example, on your webpage:
    
    
    <div id="my-ccaas"></div>
    

Then, you can mount the web SDK widget with:
    
    
    ccaas.mount('#my-ccaas')
    

### .unmount

Remove the web SDK widget from your webpage.
    
    
    ccaas.unmount()
    

### .destroy

Unmount and destroy everything.
    
    
    ccaas.destroy()
    

### .show

Display the widget UI.
    
    
    ccaas.show()
    

### .hide

Hide the widget UI.
    
    
    ccaas.hide()
    

### .start

Show and start the widget with the given options.
    
    
    interface StartOption {
      menuKey?: string;
      ticketId?: string;
      preferredChannel?: string;
    }
    

Example:
    
    
    ccaas.start({ menuKey: 'vip' })
    

## Events

This section describes the events available in the web SDK. For a complete list of events available in the headless web SDK, see [Headless web SDK events](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events).

Use the `.on` method to add an event listener. See the following example:
    
    
    const trackChat = (chat) => {
      console.log(chat)
    }
    
    ccaas.on('chat.updated', trackChat)
    

Use the `.off` method to remove an event listener. See the following example:
    
    
    ccaas.off('chat.updated', trackChat)
    

The `.on` and `.off` methods are aliases for the headless web SDK's `.on` and `.off` methods. For more information, see [Headless web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide).

### visible

Emitted when the widget visibility changes (opens or closes).

The following example shows the `visible` event:
    
    
    ccaas.on('visible', (visible) => {
      console.log(visible)  // true or false
    })
    

### chat.unread

Emitted when the unread message count changes.

The following example shows the `chat.unread` event:
    
    
    ccaas.on('chat.unread', (count) => {
      console.log(count)
    })
    

### exited

Emitted when the end-user closes the widget and the session ends.

The following example shows the `exited` event:
    
    
    ccaas.on('exited', () => {
      // widget was exited
    })
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
