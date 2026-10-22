---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-api/
title: Web SDK API reference \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:55.924651+00:00
---

# Web SDK API reference  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Web SDK API reference Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API methods of the web SDK.

## Initialize the web SDK

Use the following code to initialize the web SDK:
    
    
        const ujet = new UJET({
          companyId: '',
          // ...
        })
    

**Note:** You can only initialize one instance of the web SDK per web page.

## Options

This section contains the options that you can pass when you initialize the web SDK.

### `companyId`

**Required**

To retrieve `companyId` from the CCAI Platform portal, follow these steps:

  1. Sign in to the CCAI Platform portal with an administrator account.

  2. Go to **Settings > Developer settings**

  3. Copy **Company Key**
         
         new UJET({
           companyId: '{​ COMPANY KEY }​',
         })
         




### `tenant`

**Recommended**

Tenant is the subdomain of your Contact Center AI Platform (CCAI Platform) instance, also known as your environment. For example, if CCAI Platform portal is `https://acme.ccaiplatform.com/`, then `acme` is the tenant. See the following example:
    
    
    ```sh
    new UJET({
      companyId: '....',
      tenant: 'acme',
    })
    ```
    

### `host`

**Optional**

`host` is the API endpoint that is used by the web SDK. If you have set `tenant`, there is no need to set `host`.
    
    
    new UJET({
      companyId: '....',
      host: 'https://acme.api.ccaiplatform.com',
    })
    

If you have set `tenant`, and not `host`, the web SDK will configure the `host` value according to `tenant`. See the following example:
    
    
    https://{tenant}.api.ccaiplatform.com
    

### `authenticate`

**Optional**

`authenticate` is a function that returns a JWT token with a promise. See the following example:
    
    
    new UJET({
      // ...
      authenticate: getAuthToken,
    })
    
    function getAuthToken () {
      return fetch('/ujet/token').then(function(resp) {
        return resp.json()
      })
    }
    

Authentication is required in the web SDK, but the `authenticate` option is optional. You can call `ujet.authenticate` in the `created` event:
    
    
    var ujet = new UJET({ ... })
    ujet.on('created', function() {
      getAuthToken().then({ token } => {
        ujet.authenticate({ token })
      })
    })
    

### `lang`

**Optional**

The default language for the end-user. See the following example:
    
    
    new UJET({
      // ...
      lang: 'ja',
    })
    

### `user`

**Optional**

See the following example:
    
    
    new UJET({
      companyId: '....',
      user: {
        identifier: '...',
        name: '...',
        email: '...',
      },
    })
    

### `launcher`

**Optional**

The `launcher` option can be `false` or an object. See the following `launcher` options:
    
    
    right: string,
    bottom: string,
    cssText: string,
    chatIcon: url,
    closeIcon: url,
    style: {
      '--background-color': color,
      '--icon-color': color,
    }
    

To disable the CCAI Platform default launcher, you can set this option to `false`. See the following example:
    
    
    const ujet = new UJET({
      companyId: '...',
      launcher: false,
    })
    // use your own button: `<button id="start-chat">Chat with Me</button>`
    document.querySelector('#start-chat').addEventListener('click', function() {
      ujet.open()
    })
    

Alternatively, you can customize our built-in launcher. See the following example:
    
    
    new UJET({
      companyId: '...',
      launcher: {
        // cssText: 'body{color:red}',
        // chatIcon: 'https://example.com/logo.svg',
        // closeIcon: 'https://example.com/static/close.svg',
        // right: '50px',
        // bottom: '50px',
        style: {
          '--icon-color': '#FFF',
          '--background-color': '#F1684A',
        }
      },
    })
    

### `logo`

**Recommended**

Your company's logo URL. See the following example:
    
    
    new UJET({
      logo: 'https://example.com/logo.svg',
    })
    

### `style`

**Optional**

Use the `style` option to customize the web SDK widget. See the following example:
    
    
        new UJET({
          // ...
          style: {
            // links: ['https://example.com/font.css'],
            '--primary-font': '',
            '--primary-color': '',
            '--link-color': '',
            '--logo-shadow': '',
          }
        })
    

### `customData`

**Optional**

Custom data can be sent with a chat when the chat is started. See the following example:
    
    
    new UJET({
      // ...
      customData: {
        version: {
          label: 'Version',
          value: '1.1.0'
        },
        platform: {
          label: 'Platform',
          value: navigator.platform
        }
      }
    })
    

### `disableAttachment`

**Optional**

If `disableAttachment` is set to `true`, the web SDK won't allow the end-user to upload photos, videos, or other attachments in chats. See the following example:
    
    
        new UJET({
          companyId: '....',
          disableAttachment: true,
        })
    

### `right`

**Optional**

Position right of the widget, not the launcher. Adjust this value according to `launcher.right`. See the following example:
    
    
    new UJET({
      right: '50px',
    })
    

### `bottom`

**Optional**

Position below the widget, not the launcher. Adjust this value according to `launcher.bottom`. See the following example:
    
    
    new UJET({
      bottom: '150px',
    })
    

### `translation`

**Optional**

Use the translation capability of the web SDK. See the followint example:
    
    
    new UJET({
      translation: {
        "en": {
          "ujet_start_title": "English!",
          "ujet_greeting": "Hi there!"
        },
        "es": {
          "ujet_start_title": "¡Español!",
          "ujet_greeting": "¡Hola!"
        },
        "fr": {
          "ujet_start_title": "Français!",
          "ujet_greeting": "Salut!"
        },
        "de": {
          "ujet_start_title": "Deutsche!",
          "ujet_greeting": "Hallo!"
        },
        "ja": {
          "ujet_start_title": "日本語！",
          "ujet_greeting": "こんにちは！"
        }
      }
    })
    

## Methods

This section contains the methods of the `UJET` object:

### `.on(event, callback)`

Run the `callback` when receives the given `event`:
    
    
    ujet.on('ready', function() {
      console.log('widget is ready')
    })
    

Find all events in events documentation.

### `.off(event, callback)`

Remove the given `callback` from event listeners.
    
    
    function ready() {
      console.log('widget is ready')
    }
    
    ujet.on('ready', ready)
    ujet.off('ready', ready)
    

### `.authenticate(authData)`

Send `token` value to the widget. This method is usually called in `created` event:
    
    
    ujet.on('created', function() {
      fetchToken().then(function(token) {
        ujet.authenticate({ token: token })
      })
    })
    

### `.authenticate(authFunction)`

You can also pass a function to the `.authenticate` method. This function should return a `promise` of the `token`:
    
    
    ujet.on('created', function() {
      ujet.authenticate(function(callback) {
        return fetchToken().then(function(token) {
          return { token: token }
        })
      })
    })
    

### `.start({ menuKey, ticketId })`

The widget is started when the end-user clicks the launcher, but it can also be started with the following code:
    
    
    // if end user stayed in the web page for 10 senconds
    setTimeout(function() {
      ujet.start({ menuKey: 'help' })
    }, 10000)
    

If `.start` with a `menuKey`, the widget goes directly to that queue.

### `.open()`

`.open` is similar to `.start`, but it won't accept any parameters.
    
    
    setTimeout(function() {
      ujet.open()
    }, 10000)
    

### `.close()`

Minimize the widget programmatically:
    
    
    ujet.on('chat:status', function(status) {
      if (status === 'timeout') {
        ujet.close()
      })
    })
    

### `.destroy()`

Destroy the web SDK. That is, remove it from current web page.

### `.registerHook(event, fn)`

The `event` in `.registerHook` is different from the one in `.on`. This function is usually used when you want to use your own launcher:
    
    
    // <button id="launcher">Click to open</button>
    
    const ujet = new UJET({
      // ...
      launcher: false,
    })
    
    const launcher = document.getElementById('launcher')
    launcher.addEventListener('click', function() {
      if (ujet.status === 'open') {
        ujet.close()
      } else {
        ujet.open()
      }
    });
    
    ujet.registerHook('loading', function () {
      launcher.textContent = 'loading'
    })
    
    ujet.registerHook('open', function () {
      launcher.textContent = 'Click to close'
    })
    
    ujet.registerHook('close', function () {
      launcher.textContent = 'Click to open'
    })
    

## Translation

Here is a list of available keys for customizing translation:

  * `ujet_start_title`

  * `ujet_greeting`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
