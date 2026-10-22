---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/publishing-overview/
title: Publishing overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:57.573912+00:00
---

# Publishing overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/publishing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Publishing overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

_Publishing_ is the process of making your APIs available to app developers for consumption. 

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

**Video:** The following video provides a high-level introduction to API publishing.

Publishing APIs involves the following tasks, described in this topic:

  1. Create the API products that bundle your APIs.
  2. Register app developers.
  3. Register developer apps.
  4. Provide documentation and community support for your APIs.



## Task 1: Create an API product

The first task in publishing is to create an API product. An API product is a collection of API resources that are offered as a package to app developers for consumption. Create API products by using the Apigee API or UI. (See [What is an API product?](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) to learn more about API products.)

![A left-to-right sequence diagram showing a developer, an app, APIs,
    and backend services. The API icon and resources are highlighted. A dotted line
    points from the developer to an icon of an app the developer has built. Arrows from and
    back to the app show the request and response flow to an API icon, with an app key positioned
    above the request. The API icon and resources are highlighted. Below the API icon are two sets
    of resource paths grouped into two API products: Location product and Media product.
    The Location product has resources for /countries, /cities, and /languages, and the Media
    product has resources for /books, /magazines, and /movies. To the right of the API are the
    backend resources the API is calling, including a database, an enterprise service bus, app
    servers, and a generic backend.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/APIProduct_v14.png)

In this figure, the API consists of two products, each containing three API resources.

As an API provider, you are responsible for building the APIs and API products to handle access control, usage restrictions, and any other business requirements. For example, you might:

  * Release a free API product that allows read-only access to its API resources.
  * Release a second API product for a low price that allows read/write access to the same API resources as the free version but with a low access limit, such as 1000 requests per day.
  * Release a third API product for a higher price that allows read/write access the same API resource but with a high access limit.



The important thing to remember is that Apigee gives you the flexibility to create API products that match the business requirements of your APIs.

For more information on creating API products, see [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products).

## Task 2: Register an app developer

A developer creates the apps that consume your APIs. An app developer registers on Apigee before they can register their app. When they register their app, they receive an API key that will give the app access to the API. 

Through the app registration process, you control who has access to your APIs. At any time, you can delete an app developer, which invalidates all API keys associated with that developer, therefore denying that developer access to your APIs.

![A left-to-right sequence diagram showing a developer, an app, APIs,
    and backend services. The developer icon is highlighted. A dotted line points from the
    highlighted developer to an icon of an app the developer has built. Arrows from and
    back to the app show the request and response flow to an API icon, with an app key positioned
    above the request. Below the API icon are two sets
    of resource paths grouped into two API products: Location product and Media product.
    The Location product has resources for /countries, /cities, and /languages, and the Media
    product has resources for /books, /magazines, and /movies. To the right of the API are the
    backend resources the API is calling, including a database, an enterprise service bus, app
    servers, and a generic backend.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/devApp_v14.png)

As an API provider, you decide how to register developers. For example, you can use a manual registration process that requires a potential developer to contact your organization to register. The potential developer must supply all necessary information, such as an email address, first and last name. If you approve the developer’s request, you can use the Apigee UI to manually register the developer. See [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product) for more.

## Task 3: Register a developer app

Before an app can access your APIs, the app must be registered. However, only a registered developer can register an app.

![A left-to-right sequence diagram showing a developer, an app, APIs,
    and backend services. The app, request/response, and API key arrows are highlighted. A dotted
    line points from the developer to an icon of an app the developer has built. Arrows from and
    back to the app show the request and response flow to an API icon, with an app key positioned
    above the request. The API icon and resources are highlighted. Below the API icon are two sets
    of resource paths grouped into two API products: Location product and Media product.
    The Location product has resources for /countries, /cities, and /languages, and the Media
    product has resources for /books, /magazines, and /movies. To the right of the API are the
    backend resources the API is calling, including a database, an enterprise service bus, app
    servers, and a generic backend.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/registerApp_v14.png)

At the time of app registration, the developer selects one or more API products. For example, you might publish multiple API products corresponding to different types of services and pricing plans. The app developer can then pick and choose from the list of available API products.

**Note:** Apigee does not require that you to let the developer associate multiple API products with an app. Your publishing plan can be structured such that the developer can select only a single API product. Or, you can automatically assign a default API product to all apps so that the developer does not even get to choose one.

In response to registering the app on Apigee, Apigee assigns a unique API key to the app. The app must pass that API key as part of every request to an API resource. The key is authenticated and, if valid, the request is granted. At any time, you as the service provider can revoke the key so that the app can no longer access your APIs.

As an API provider, you decide how you want to register apps. You could:

  * Use a manual process that requires a developer to contact your organization to register their app. In response, you would send the developer the API key, possibly by email.
  * Use the Apigee API to integrate app registration functionality and key delivery into your website.
  * For a paid Apigee account, use the Apigee Developer Services portal which has built in support for app registration and API key delivery.

**Note:** As a best practice, there is a 1-1 correlation between the app that the developer registers on Apigee and the actual client app that they build. However, this correlation is not enforced by Apigee. For example, a developer registers a single app on Apigee, associated that app with an API product, and receives back an API key. The developer is free to use the API key from any client app.

For more information, see [Registering apps and managing API keys](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api).

## Task 4: Document your APIs

An important consideration for publishing API products is providing documentation and a developer feedback mechanism. Developer portals with social publishing features are increasingly being used for communication with the development community. This includes communicating static content, such as API documentation and terms-of-use, as well as dynamic community-contributed content such as blogs and forums, as well as customer support features.

![A left-to-right sequence diagram showing a developer, an app, APIs,
    and backend services. The developer icon is highlighted. Below the developer is a box that
    represents a developer portal. The portal contains API documentation, samples, tutorials,
    API reference, and other. The portal also contains blogs, forums, and a support portal.
    A dotted line points from the highlighted developer to an icon of an app the developer has
    built. Arrows from and back to the app show the request and response flow to an API icon,
    with an app key positioned above the request. Below the API icon are two sets
    of resource paths grouped into two API products: Location product and Media product.
    The Location product has resources for /countries, /cities, and /languages, and the Media
    product has resources for /books, /magazines, and /movies. To the right of the API are the
    backend resources the API is calling, including a database, an enterprise service bus, app
    servers, and a generic backend.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/docAPIs_v14.png)

You can build your own website to deploy your documentation or, if you have a paid Apigee account, you can use the **Apigee Developer Services portal**. The portal has built-in support for documentation, blogs, forums, and other types of content required to support your developer community.

**SmartDocs** lets you document your APIs on the Developer Services portal in a way that makes the API documentation fully interactive. Interactive documentation with SmartDocs means portal users can:

  * Read about the API
  * Send a live request to the API
  * View a live response returned from the API



For more information, refer to the following sections:

  * **Integrated portal** : [Publishing your APIs](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis)
  * **Drupal 10** : [Document your APIs](https://www.drupal.org/docs/8/modules/apigee-edge/document-your-apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
