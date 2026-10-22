---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide/
title: Headless web SDK guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:47.884178+00:00
---

# Headless web SDK guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Headless web SDK guide Stay organized with collections  Save and categorize content based on your preferences. 

The headless web SDK gives you the flexibility to extend and customize your company's support experience according to your needs. It contains all our familiar [web SDK features](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk) and provides the ability to build out the UI and UX to support them.

Installing and using the headless web SDK requires the support of your organization's web development team. To perform a successful integration and achieve optimal performance, Google recommends involving your qualified personnel.

In the context of software development, "headless" refers to a decoupled architecture where the frontend presentation layer (the "head") is separated from the backend logic and capabilities. In a headless architecture the backend, also known as the "headless" part, provides APIs that let you use its features and services.

An example is custom workflow automation. When an end-user initiates a chat, the `on("chat.message")` event is triggered. You can define custom automation triggers based on specific chat messages you've received. For example, if an end-user types "Escalate" in the chat, the event handler can automatically escalate the chat session to a higher-level support team, providing prompt attention to critical issues.

This guide walks you through the SDK's installation process, integration capabilities, and usage. For details about using the API, see the [Headless web SDK API documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api). A list of available events can be found on the [events page](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-events).

**Note:** Google only supports the latest three minor versions of the headless web SDK. To receive support, your website must be using one of these versions of the headless web SDK.

## Install the headless web SDK

You can install the package with npm:
    
    
    npm install @ujet/websdk-headless --save
    

Or, you can use the script hosted by UJET:
    
    
    <script src="https://websdk.ujet.co/v3/headless.js"></script>
    
    <script>
      // The hosted script exposes the client as the global `UJETClient`.
      // const client = new UJETClient(...)
    </script>
    

## Use the headless web SDK

To use the headless Web SDK, you can follow the example code provided:
    
    
    import { Client } from "@ujet/websdk-headless"
    
    async function authenticate() {
      const resp = await fetch("/your-auth-endpoint")
      const data = await resp.json()
      return { token: data.token }
    }
    
    const client = new Client({
      companyId: "YOUR-COMPANY-ID",
      tenant: "YOUR-TENANT-NAME",
      authenticate: authenticate,
    })
    
    // const company = await client.getCompany()
    // const menus = await client.getMenus()
    

The Client class accepts several options (you can customize according to your requirements):
    
    
    interface ClientOption {
      companyId: string;
      authenticate: () => Promise<TokenResponse>;
      tenant?: string;
      host?: string;
      lang?: string;
      bridge?: string;
      version?: string;
      cobrowse?: {
        enabled?: boolean;
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
    

## Enable logging

During implementation and testing it might be necessary to gather additional information in the console log. To enable logging for the headless SDK, import `Logger` and `consoleLoggerHandler` by adding the following code to your web application:
    
    
    import {Logger, consoleLoggerHandler } from '@ujet/websdk-headless'
    Logger.addHandler(consoleLoggerHandler)
    

## Configure Screen Share

You can enable and configure Screen Share using the headless web SDK.

The following code sample shows you how to enable Screen Share:
    
    
    new Client({
      // ...
      cobrowse: {
        enabled: true,
        license: 'YOUR_SCREEN_SHARE_LICENSE'
      }
    })
    

The following code sample show the options for Screen Share:
    
    
    interface CobrowseOption {
      enabled: boolean
      template?: string
      confirmSessionTemplate?: string
      confirmRemoteControlTemplate?: string
      confirmFullDeviceTemplate?: string
      sessionControlsTemplate?: string
      root?: Element
      messages?: {
        confirmSessionTitle: string;
        confirmSessionContent: string;
        confirmRemoteControlTitle: string;
        confirmRemoteControlContent: string;
        confirmFullDeviceTitle: string;
        confirmFullDeviceContent: string;
        allowText: string;
        denyText: string;
        endSessionText: string;
      }
      api?: string
      license?: string
      trustedOrigins?: string[]
      capabilities?: string[]
      registration?: boolean
      redactedViews?: string[]
      unredactedViews?: string[]
    }
    

### Custom template

You can customize the Screen Share dialog template using the `template` option from the preceding code sample.

The following example shows the default template:
    
    
    <dialog open class="cobrowse-dialog">
      <h1>$title</h1>
      <div class="cobrowse-dialog_content">$content</div>
      <div class="cobrowse-dialog_footer">
        <button class="cobrowse-dialog_allow js-cobrowse-allow">$allow</button>
        <button class="cobrowse-dialog_deny js-cobrowse-deny">$deny</button>
      </div>
    </dialog>
    

You can use this template to configure a dialog that requests approval from the end-user for the following:

  * Start a Screen Share session

  * Start a remote control Screen Share session

  * Start a full device Screen Share session




Here are the template options:

  * `confirmSessionTemplate`: For confirming a Screen Share session.

  * `confirmRemoteControlTemplate`: For confirming a remote control Screen Share session.

  * `confirmFullDeviceTemplate`. For confirming a full device Screen Share session.

  * `sessionControlsTemplate`: For the session controls button. Here's the default template: `<button class="cobrowse-end js-cobrowse-end">$end</button>`




### Messages

The following message variables are used in Custom templates:

  * `$title`

  * `$content`

  * `$allow`

  * `$deny`




The following example shows how these variables are applied:
    
    
    {
      confirmSessionTitle: string;  // $title
      confirmSessionContent: string;  // $content
      confirmRemoteControlTitle: string;  // $title
      confirmRemoteControlContent: string;  // $content
      confirmFullDeviceTitle: string;  // $title
      confirmFullDeviceContent: string;  // $content
      allowText: string;  // $allow
      denyText: string;  // $deny
      endSessionText: string;  // $end
    }
    

The following example shows the default English variable values:
    
    
    {
      "confirmSessionTitle": "Screen Share Session Request",
      "confirmSessionContent": "Do you want to share your current screen with the agent?",
      "endSessionText": "End Screen Share Session",
      "confirmRemoteControlTitle": "Remote Access Request",
      "confirmRemoteControlContent": "The agent would like to have access to your currently shared screen to further assist you. Do you want to allow this?",
      "confirmFullDeviceTitle": "Screen Share Request",
      "confirmFullDeviceContent": "Do you want to share your full screen with the agent? The agent will not be able to control anything on the screen.",
      "allowText": "Allow",
      "denyText": "Deny"
    }
    

### Properties

Name | Description  
---|---  
`deviceId` | The device's id, determined by the headless SDK on initialization.  
`lang` | The current Client's language configuration. If lang is passed in configuration, it becomes read-only.  
`chat` | Only has a value when there is an ongoing chat.  
`cobrowse` | The underlying CobrowseIO client, available after cobrowse has been initialized  
  
### Events

Name | Description  
---|---  
`destroy` | Destroys the communicator and all event listeners.  
`on` | Adds event handler for provided event.  
`off` | Removes event handler for provided event.  
  
Use `.destroy` method to remove iframe and all event listeners
    
    
    client.destroy()
    

Use the `.on` method to track the events.
    
    
    client.on('chat.updated', someFunc)
    

Remove the event handler with `.off`:
    
    
    client.off('chat.updated', someFunc)
    

## Custom data configuration

The custom_data option lets you pass arbitrary key-value pair data to the web SDK.

**Usage**

You can provide custom data as either an object (unsigned) or a string (signed) when creating a chat:
    
    
    interface ChatRequest {
      lang?: string;
      trigger_id?: string;
      ticket_id?: string;
      email?: string;
      greeting?: string;
      cobrowsable?: boolean;
      custom_data?: {
        signed?: string;
        unsigned?: Record<string, any>;
      };
    }
    

See the following example:
    
    
    const custom_data = {
      unsigned: {
        version: {
          label: 'Version',
          value: '1.0.0'
        }
      },
      signed: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' // JWT or other signed payload
    }
    
    try {
      const chat: Chat = await client.createChat(123, { custom_data })
    } catch (error) {
      // handle error
    }
    

**Note:** Custom data is typically sent with session-creation requests for backend processing.

## External chatbot transfer

There are some cases where you might want to maintain history and interactions from other chat providers. You can do this by using the `custom_data object`.

See the following example:
    
    
    const custom_data = {
      unsigned: {
        external_chat_transfer: {
          greeting_override: "Please hold while we connect you with a human agent.",
          agent: {
            name: "Agent Name",
            avatar: "https://ujet.s3.amazonaws.com/default-virtual-agent-avatar-1.png"
          },
          transcript: [
            {
              sender: "agent",
              timestamp: "2021-03-15 12:00:00Z",
              content: [
                {
                  type: "text",
                  text: "Hello! How can I help you today?"
                },
                {
                  type: "buttons",
                  buttons: [
                    {
                      label: "Create New Order",
                      selected: false
                    },
                    {
                      label: "Check Order Status",
                      selected: true
                    },
                    {
                      label: "Check Account Balance",
                      selected: false
                    },
                  ]
                }
              ]
            },
            {
              sender: "end_user",
              timestamp: "2021-03-15 12:00:15Z",
              content: [
                {
                  type: "text",
                  text: "Check Order Status"
                }
              ]
            },
            {
              sender: "agent",
              timestamp: "2021-03-15 12:00:16Z",
              content: [
                {
                  type: "text",
                  text: "I can help you with that, what's your order number?"
                }
              ]
            },
            {
              sender: "end_user",
              timestamp: "2021-03-15 12:00:20Z",
              content: [
                {
                  type: "media",
                  media: {
                    type: "image",
                    url: "https://ujet.s3.amazonaws.com/default-virtual-agent-avatar-1.png"
                  }
                }
              ]
            }
          ]
        }
      },
      signed: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' // JWT or other signed payload
    }
    
    try {
      const chat: Chat = await client.createChat(123, { custom_data })
    } catch (error) {
      // handle error
    }
    

## Reference implementation

For a reference implementation of the web SDK, see [ccaas-web-headless-sdk-sample](https://github.com/ayushbisaria/ccaas-web-headless-sdk-sample.git) on GitHub.

This repository contains a demonstration of a chat application built using a CCAI Platform Web Headless SDK. It showcases a basic client-server architecture where the Node.js backend handles secure authentication and configuration delivery, while the pure JavaScript frontend provides the chat user interface.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
