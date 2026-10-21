---
url: https://docs.cloud.google.com/looker/docs/embed-getting-started/
title: Get started with embedding Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:58:52.403005+00:00
---

# Get started with embedding Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/embed-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Get started with embedding Looker Stay organized with collections  Save and categorize content based on your preferences. 

**Knowledge check:** This page assumes you understand the basics of Inline Frame HTML Element <iframe>, window.postMessage(), and Javascript. Check out the MDN web documentation on [iframes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) and [postmessaging](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) to familiarize yourself with these concepts. 

We provide options for you to embed Looker content in your host application using iframes. Each option differs in how you manage and interact with your iframe and authorize or authenticate your user. If you are not sure which option to start with, check out the suggested learning path at the end of this page.

## Your iframe embedding options

Every option supports theming and can embed [dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards), [LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards), [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks), query visualizations, and [extensions](https://docs.cloud.google.com/looker/docs/extension-overview).

### Private embedding

  * You manage your iframe directly.
  * You may use window.postMessage() to interact with your iframe.
  * Your user must authenticate or authorize with Looker directly or with Looker using signed embedding with an identity provider.



[Get started with private embedding](https://docs.cloud.google.com/looker/docs/gs-private-embedding)

### Signed embedding

  * You manage your iframe directly.
  * You may use window.postMessage() to interact with your iframe.
  * You generate a unique iframe src url for every embed user session. This one-time-use URL creates a new Looker embed user or updates an existing one.
  * You must authenticate or authorize the user outside of Looker, for example, through your host application's identity provider using signed embedding.



[Get started with signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding)

### Signed embedding with Embed SDK (Recommended)

  * You use the Embed SDK's convenient Javascript API to **manage** and **interact** with your iframe.
  * You generate a unique URL for every embed user session. This one-time-use URL creates a new Looker embed user or updates an existing one. The Embed SDK helps automate part of the URL generation.
  * You must authenticate or authorize the user outside of Looker, for example, through your host application's identity provider using signed embedding.



[Get started with signed embedding with the Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk-intro)

## Suggested learning path

We suggest you get started in this order:

[1\. Get started with private embedding](https://docs.cloud.google.com/looker/docs/gs-private-embedding)

Private embedding will provide a basic understanding of Looker embedding.

[2\. Get started with signed embedding with Embed SDK](https://github.com/looker-open-source/embed-sdk#readme)

Signed Embedding and the Embed SDK are more advanced concepts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
