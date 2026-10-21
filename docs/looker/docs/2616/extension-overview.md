---
url: https://docs.cloud.google.com/looker/docs/2616/extension-overview/
title: Looker extension overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:14:10.174226+00:00
---

# Looker extension overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2616/extension-overview/

You are viewing documentation for Looker 26.16. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2616/intro)



Send feedback 

#  Looker extension overview Stay organized with collections  Save and categorize content based on your preferences. 

> These extensions are different from [LookML extends/extensions](https://docs.cloud.google.com/looker/docs/2616/reusing-code-with-extends), the code organization syntax used when modeling data in LookML.

Looker extensions allow you to provide highly customized and integrated experiences to your Looker instance's users.

A dedicated Looker page becomes your canvas, with a wide array of tools at your disposal, including the ability to:

  * Run JavaScript code 
  * Access the Looker APIs through a pre-authenticated client
  * Leverage [Looker components](https://docs.cloud.google.com/looker/docs/2616/components) for seamless UI
  * Make HTTP calls from the client or through a convenient server proxy
  * Authenticate with third-party services via OAuth
  * Use additional [extension framework features](https://docs.cloud.google.com/looker/docs/2616/intro-to-extension-framework#extension_framework_features)



Simultaneously, detailed sandboxing controls and built-in user permissioning allow your instance's administrators to be confident about what data is accessible to application developers and end users.

## Using extensions

The first step to using a Looker extension is authoring a JavaScript-based client-side application that uses the APIs that are exposed by Looker's extension framework.

The quickest way to get up and running with such an application is with our [`create-looker-extension`](https://www.npmjs.com/package/create-looker-extension) command line tool, which will set you up with a boilerplate codebase, including the necessary build tooling to bundle your application code via webpack. The tool lets you choose between either JavaScript or TypeScript, and lets you select whether to use React.

Once your codebase is ready to go, you can load it into your Looker instance in one of three ways:

  * During development, you can use a [URL](https://docs.cloud.google.com/looker/docs/2616/reference/param-manifest-application#url) to reference a locally hosted web server for quick and convenient development.
  * You can build a JS bundle and [load the file through your LookML project](https://docs.cloud.google.com/looker/docs/2616/reference/param-manifest-application#file).
  * You can deploy the JS file to a remote server or content delivery network (CDN) and then [reference it by URL](https://docs.cloud.google.com/looker/docs/2616/reference/param-manifest-application#url). This option is often the most convenient when used together with continuous deployment automation from your extension's codebase.



## Try it out

Want to see Looker extensions in action before writing any code? Several [Looker-published extensions](https://marketplace.looker.com/marketplace/directory?Type=applications) can be [installed with one click](https://docs.cloud.google.com/looker/docs/2616/marketplace) into your Looker instance from the Looker Marketplace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
