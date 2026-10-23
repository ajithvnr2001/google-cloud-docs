---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup/
title: Integrate your app with Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:29.507133+00:00
---

# Integrate your app with Google Cloud Marketplace  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Integrate your app with Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

This section is an overview of the steps to integrate your app with Cloud Marketplace. At a high level, you integrate your app with Google Cloud in the following ways:

  * **Backend integration**

You must integrate your app's backend with the following Google APIs and services:

    * Integrate with Pub/Sub to receive notifications from Cloud Marketplace, such as when a user signs up for your product. Your Partner Engineer creates a Pub/Sub topic that you must subscribe to for notifications.

For information on subscribing to a Pub/Sub topic, see the [Pub/Sub Subscriber Guide](https://docs.cloud.google.com/pubsub/docs/subscriber).

    * Integrate with the Partner Procurement API to create accounts for customers, and to link these accounts with their Cloud Marketplace purchase. You must also use the Partner Procurement API to update the linked accounts when users change or cancel their subscription plans.

    * If you've chosen a usage-based pricing model, integrate with Service Control to report usage information.

For detailed information on integrating your app's backend with Cloud Marketplace, see [Configure your app's backend](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration).

For an example of integrating the backend of a basic product with Cloud Marketplace and a walkthrough of the sample code, see the [codelab for integrating a SaaS product](https://codelabs.developers.google.com/codelabs/gcp-marketplace-integrated-saas/#0).

  * **Frontend integration**

In your app's frontend, you must set up the following integrations:

    * Provide a sign up page to sign up accounts for new customers who buy your product through Cloud Marketplace. When users visit this page, Google sends a [JSON Web Token (JWT)](https://jwt.io/introduction/) containing the user's account ID. You use this account ID to link the user's account in your product with their Google Account, and also for Identity and Access Management (IAM).

**Note:** It's possible for a single user to have multiple Google Cloud account IDs, or for multiple users to share a common Google Cloud account ID, depending on how they or their organization have configured their usage of Google Cloud.
    * Provide a login page for your customers.

Optionally, you can choose to:

    * Integrate single sign-on (SSO), so that your customers can sign into your app using their Google Accounts. If you integrate SSO, when users sign in by using SSO, Google sends a [JSON Web Token (JWT)](https://jwt.io/introduction/) containing information about the user for you to verify.

For detailed information on integrating your app's frontend with Cloud Marketplace, see [Integrating your app's frontend](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration).




If you use App Lifecycle Manager to deploy and operate your SaaS product, you can also take advantage of streamlined validation and one-click tenant onboarding. For more information, see [Integrate with App Lifecycle Manager](https://docs.cloud.google.com/marketplace/docs/partners/integrate-app-lifecycle-manager).

## Before you begin

  * Verify that your Partner Engineer has enabled access to the Cloud Commerce Partner Procurement API. After your Partner Engineer has granted you access to the Partner Procurement API, you don't need to take any additional steps to enable the API in Google Cloud console.



## Integrate with Google APIs

You can integrate your app with Google APIs by [using client libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), which give you programmatic access to Google products. The client libraries are available for most popular development platforms, such as Java, Python, and .NET.

Install the client libraries for your platform from the [API Client Libraries page](https://developers.google.com/api-client-library/). With the client libraries, you can:

  * Connect to your Pub/Sub subscription, and handle incoming messages.
  * If you chose usage-based pricing, connect to the Service Control API to report usage data to Google.



To create linked accounts for customers, and to send and receive updates about user accounts, you must also integrate with the Partner Procurement API. Because the Partner Procurement API is restricted, you must build a new client library for the API.

To build a new client library, you must install the Google client libraries, and build a new library from the API discovery document. The discovery document for the Partner Procurement API is at this URL:
    
    
    https://cloudcommerceprocurement.googleapis.com/$discovery/rest?version=v1
    

For example, if you're building a Python client library for the Partner Procurement API, use the [`build()`](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build) method. For sample code that builds a client library, see the [codelab samples on GitHub](https://github.com/googlecodelabs/gcp-marketplace-integrated-saas/blob/master/python3/impl/step_2_account/app.py#L39).

[ Previous arrow_back  Choose and submit your pricing model  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing)

[ Next Integrate your app's frontend  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
