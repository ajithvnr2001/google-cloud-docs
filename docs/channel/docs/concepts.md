---
url: https://docs.cloud.google.com/channel/docs/concepts/
title: Concepts \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:33.675687+00:00
---

# Concepts  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Concepts Stay organized with collections  Save and categorize content based on your preferences. 

## Types of resellers

Your account has been provisioned either as a direct reseller (1-tier) or a distributor (2-tier). You can confirm your account type in the Settings page of your Partner Sales Console. Direct resellers show as `RESELLER`, while distributors show as `DISTRIBUTOR`.

## General Channel Services concepts

![Channel Services concepts](https://docs.cloud.google.com/static/channel/docs/images/channel-services-concepts.png)

**Figure 1.** Diagram of the relationship between the Channel Services concepts presented in this document.

### Accounts

An account is the top-level entity and maps to your reseller domain. All other resources are rooted under it. You will need your `account_id` — found in the Settings page of your Partner Sales Console — when making calls to the Cloud Channel API.

### Customers

Customers, typically a company, are the end-users of Google Cloud products you place orders for. In an n-tier resale channel hierarchy, customers are the leaf nodes.

### Entitlements

Entitlements represent services that are billed to you, but used by one of your Customers.

For a SaaS offering like Google Workspace, an entitlement would be a subscription for one of the services (e.g. Google Workspace Business Starter or Cloud Identity Premium).

For an IaaS offering like Google Cloud Platform, an entitlement would be a consumption-based billing account that customers can use for their projects.

### Offers

Offers represent what you are allowed to sell. An Offer and a Customer are the main components of an Entitlement.

Offers are a combination of a SKU and a pricing model. For example, a single product with various payment plans or discount levels would have as many offers as there are permutations of the product and the plans or discounts.

For Google Workspace, offers don't change price. When prices change, new `offerId`s are generated.

### Reseller domain

A reseller domain is a Google Workspace instance where you can manage access privileges to your Partner Sales Console.

### Channel partner links

Channel partner links are only applicable to distributors.

Channel Partner Links represent the connection between a distributor and their authorized indirect resellers. Distributors are required to register their channel partners with Google.

Contact your Partner Manager for more details on this process.

## API-specific concepts

### Cloud identities

A _cloud identity_ is the footprint for Google Workspace and Chrome customers, and the foundational set of customer features, including access to admin.google.com and user management.

You must provision a cloud identity with Google Workspace-specific data before creating an entitlement for a Google Workspace or Chrome product.

**Caution:** Cloud identities are different from the Cloud Identity product offerings.

### Operations

Operations are also called _long-running operations_ (LRO). They are used throughout the Cloud Channel API, as many actions triggered by API calls are not instantaneous, and can take longer than default client timeouts.

Operations are asynchronous API calls. Endpoints that use operations might return either HTTP 4xx errors (due to synchronous validation) or an HTTP 200 code with an `Operation` resource, and the operation's identifier. To get the status of an operation, use the `operations.get` method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
