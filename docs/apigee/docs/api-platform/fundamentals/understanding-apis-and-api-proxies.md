---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies/
title: Understanding APIs and API proxies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:04.336776+00:00
---

# Understanding APIs and API proxies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understanding APIs and API proxies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee lets you easily and quickly build RESTful APIs that can be consumed by app developers. You expose APIs on Apigee by building API proxies that act as managed 'facades' for backend services. This topic discusses the relationship between APIs and API proxies on Apigee.

**Video:** Check out this short video for an introduction to API proxies.

## What is an API?

An API is an interface that makes it easy for one application to _consume_ capabilities or data from another application. By defining stable, simplified entry points to application logic and data, APIs enable developers to easily access and reuse application logic built by other developers. In the case of _Web APIs_ , that logic and data is exposed over the network.

Since applications that consume APIs are sensitive to changes, APIs also imply a _contract_. The contract provides some level of assurance that, over time, the API will change in a predictable manner.

Apigee enables you to build APIs and if you have APIs already, expose them directly, while adding a management and visibility layer. If you have HTTP enabled services, such as SOA-based Web services, they can also be exposed as APIs via Apigee.

Apigee also enables you to build APIs by implementing applications hosted on the API Services platform—with no backend service involved. You can build these applications in JavaScript and Java.

**Best practice:** Apigee provides a wealth of information about APIs and best practices for developing and consuming them. To get started, see the [How to design APIs that developers love ](https://www.youtube.com/watch?v=kgIq02wP73s) or download the free eBook [ Web API Design: The Missing Link](https://cloud.google.com/files/apigee/apigee-web-api-design-the-missing-link-ebook.pdf).

## What is an API proxy?

You expose APIs on Apigee by implementing _API proxies_. API proxies decouple the app-facing API from your backend services, shielding those apps from backend code changes. As you make backend changes to your services, apps continue to call the same API without any interruption.

In an API proxy configuration, there are two types of endpoints: 

  * **ProxyEndpoint:** Defines the way client apps consume your APIs. You configure the ProxyEndpoint to define the URL of your API proxy. The proxy endpoint also determines whether apps access the API proxy over HTTP or HTTPS. You usually attach _policies_ to the ProxyEndpoint to enforce security, quota checks, and other types of access control and rate-limiting.
  * **TargetEndpoint:** Defines the way the API proxy interacts with your backend services. You configure the TargetEndpoint to forward requests to the proper backend service, including defining any security settings, HTTP or HTTPS protocol, and other connection information. You can attach _policies_ to the TargetEndpoint to ensure that response messages are properly formatted for the app that made the initial request.



You can visualize API proxies as shown by the graphic below: 

![HTTP requests enter through the proxy request endpoint, are passed to the target request endpoint,
    and then sent to the backend services. HTTP responses enter through the target response endpoint, are
    passed to the proxy response endpoint, and then back to the client.](https://docs.cloud.google.com/static/apigee/docs/images/ApigeeProxyModel.png)

## API proxy types

Apigee supports two proxy types:

  * **Standard proxies** include only [standard policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types). Standard proxies are suitable for lightweight API solutions and cannot be included in [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#limitations).
  * **Extensible proxies** include at least one [extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types) or flow hook. Extensible proxies can include much more functionality than standard proxies.



## How do you create an API proxy?

An API proxy consists of a bundle of XML configuration files and code (such as JavaScript and Java). Apigee provides several ways for you to create API proxies, including:

  * Using the [Apigee UI](https://apigee.google.com) to define an API proxy in a Graphical User Interface (GUI). For more, see [Build a simple API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy).
  * Creating XML files, along with any other supporting files, that define your API proxy and then importing them into Apigee.
  * Using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) to create your API proxies by making a series of REST requests to Apigee. 
  * Develop locally using Apigee in VS Code and deploy as an archive. For more information, see [Overview of local development with Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview)



## What is an API proxy revision?

**Warning:** Don't confuse the version of an API (that is, the public interface) with the _revision_ of an API proxy (that is, the internal number associated with a configuration). The two numbers are unrelated, and the revision number of an API proxy is totally opaque to apps that consume your API.

API proxy revisions provide a lightweight mechanism for managing the updates to the API proxy configuration as you iterate. Revisions are sequentially numbered, enabling you to revert a change by deploying a previous revision of your API proxy. Revisions let you deploy an API proxy into a production environment while continuing to create new revisions of that API proxy in a test environment. When you are ready, you can _promote_ the higher revision of your API proxy from test to prod.

## What is a policy?

Apigee enables you to control API behavior without writing any code by using [policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy). A policy is like a module that implements a specific, limited management function as part of the proxy request/response flow. Policies are designed to let you add common types of management capabilities to an API easily and reliably. Policies provide features like security, rate-limiting, transformation, and mediation capabilities, saving you from having to code and maintain this functionality on your own.

## Create your first API proxy

Apigee provides a set of tutorials that you can use to create your first API. Start with the [Build your first API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started). See also other [Get started topics](https://docs.cloud.google.com/apigee/docs/getstarted).

## Learn more

  * [API proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference)
  * [API development lifecycle](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/api-development-lifecycle)
  * [Key points of API proxy development](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/structure-api-proxies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
