---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy/
title: Identity Platform multi-tenancy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:04.260812+00:00
---

# Identity Platform multi-tenancy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Identity Platform multi-tenancy

Identity Platform lets you add Google-grade authentication to your apps and services, making it easier to secure user accounts and securely managing credentials.

Multi-tenancy takes this concept one step further. Using tenants, you can create unique silos of users and configurations within a single Identity Platform project. These silos might represent different customers, business units, subsidiaries, or some other division. Multi-tenancy is most commonly used in business-to-business (B2B) apps.

## Understanding tenants

You can use Identity Platform tenants to establish a data isolation boundary between resource hierarchies. Each tenant has its own:

  * Unique identifier
  * Users
  * Identity providers and authentication methods
  * Auditing and IAM configuration
  * Quota allocation
  * Identity Platform usage breakdown



This allows tenants to operate autonomously from one another, with different configurations and users, even though they are part of the same project.

## Supported sign-in methods

Identity Platform tenants support many of the same authentication methods as non-tenant instances of Identity Platform. Currently supported providers include:

  * Email/password
  * Social Providers (such as Google, Microsoft, and LinkedIn)
  * SAML Federation
  * OpenId Connect Federation



## Limitations

Identity Platform tenants don't support the following features:

  * Disabling account linking
  * Adding a blocking function specific to a given tenant



In addition, you can't disable user signup or user deletion from the Google Cloud console. However, you can configure these settings through the API.

## What's next

  * [Enable multi-tenancy and create a tenant](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart)
  * [Sign in users with tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-authentication)
  * [Create sign-in page for multiple tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-ui)
  * [Migrate existing users to a tenant](https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants)
  * [Manage tenants programmatically](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
