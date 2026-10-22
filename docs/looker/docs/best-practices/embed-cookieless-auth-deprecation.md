---
url: https://docs.cloud.google.com/looker/docs/best-practices/embed-cookieless-auth-deprecation/
title: Embed cookieless authentication deprecation \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:22.684123+00:00
---

# Embed cookieless authentication deprecation  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/embed-cookieless-auth-deprecation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Embed cookieless authentication deprecation Stay organized with collections  Save and categorize content based on your preferences. 

Starting in Looker 24.14, scheduled to release on August 7, 2024, to address security considerations, the experimental [Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs) **Embed Cookieless Authentication** will be deprecated in favor of the [cookieless embedding](https://docs.cloud.google.com/looker/docs/cookieless-embed) feature.

If you have enabled the **Embed Cookieless Authentication** Labs feature, and you don't implement one of the following solutions for ensuring that your embed use case continues to work for all your embed users, when your instance is upgraded to Looker 24.14, all embedded iframes will automatically default to using cookies for authentication.

## Why does this matter?

Looker uses cookies for user authentication. If the Looker instance is on a different domain than the embedded iframe, the cookies are considered third-party cookies. Some browsers default to a cookie policy that blocks third-party cookies. When third-party cookies are blocked, it's not possible to authenticate the embedded iframe across different domains.

Matching the domains of the Looker instance and the embedded iframe causes the cookies to become first-party cookies, which are not blocked. For example, if you want to embed information on `https://mycompany.com`, Looker would have to share the same domain, such as `https://analytics.mycompany.com`.

## What do I need to do?

Implement one of the following solutions to ensure that your embed use case continues to work for all your embed users:

  * **Set up a custom domain for your Looker instance**.

You can set up a custom domain for your Looker instance that shares the same domain as your embed application. Configuring a custom domain causes the cookies that Looker uses to become first-party cookies, since the Looker domain matches the embed application domain. For example, if you are embedding on `analytics.mycompany.com`, you can set up a custom domain that changes your Looker URL from `mycompany.cloud.looker.com` to `looker.mycompany.com`.




To set up a custom domain on a Looker (original) instance that is hosted by Looker, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

**Note:** Customer-hosted instances will have to provide their own certificate for their custom domain and won't need to contact Looker Support.

To set up a custom domain on a Looker (Google Cloud core) instance, follow the instructions on the [Set up a custom domain for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) documentation page.

  * **Switch to using[cookieless embedding](https://docs.cloud.google.com/looker/docs/cookieless-embed)**.

Cookieless embedding uses a token-based approach for embed user authentication that bypasses Looker's dependency on browser cookies. This feature is generally available, but it requires embed application code changes to implement. For more information, see the [Cookieless embedding](https://docs.cloud.google.com/looker/docs/cookieless-embed) documentation page.




If you have any questions or need assistance, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

## Which solution is better for me?

For most embed use cases, setting up a custom domain is a simpler way to address third-party cookies. Cookieless embedding requires embed application code changes to implement.

One use case for [cookieless embedding](https://docs.cloud.google.com/looker/docs/cookieless-embed) is for customers who host their embed application on different domains for each of their customers. In this case, implementing cookieless embedding prevents the need to set up and maintain dozens or even hundreds of separate custom domains to allow third-party cookies.

If you have any questions or need assistance, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
