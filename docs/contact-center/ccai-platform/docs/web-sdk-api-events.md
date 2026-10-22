---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-api-events/
title: Web SDK API events \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:06.698003+00:00
---

# Web SDK API events  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-api-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Web SDK API events Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    ujet.on(eventName, callback)
    
    ujet.off(eventName, callback)
    

## created

When Web SDK widget is created. Usually this happens when you click the launcher.

You can use this event to send authentication token:
    
    
    const ujet = new UJET({
      // ...
      // authenticate: getAuthToken
    })
    
    // when you didn't use `authenticate` option, you need to call
    // `.authenticate` method manually
    
    ujet.on('created, () => {
      fetch('/token').then(resp => {
        return resp.json()
      }).then(data => {
        ujet.authenticate({ token: data.token })
      })
    })
    

## authorized

This event happens when `.authenticate` method is called and responded with a `token` to Web SDK.

## ready

Web SDK has fetched `company` information, it is **ready** to use now.

## unread

Emit `unread` chat message count:
    
    
    ujet.on('unread', function(num) {
      console.log('has ' + num + ' unread messages')
    })
    

## close

When Web SDK has been closed. This event happens when you click "close" button in the SDK, or click the launcher to close SDK.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
