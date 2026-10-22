---
url: https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name/
title: Verifying a domain name \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:34.413476+00:00
---

# Verifying a domain name  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/verify-domain-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Verifying a domain name Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/verify-domain-name "View this page for the Cloud Endpoints gRPC docs")

If you already own a domain name (such as `example.com`), and you want to use this domain name as the name of your Cloud Endpoints service, you must prove that you are authorized to use the domain. If you don't have your own domain name, you can use a [domain managed by Google](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints#using_a_domain_managed_by_google), in which case you don't have to verify ownership.

This page describes how to verify your ownership of a domain name that you want to use for your API running on Google Cloud.

## Service name requirements

Typically, you configure your Endpoints service name to be the same as your domain name. Endpoints has the following requirements for the service name:

  * The maximum length of the domain name is 253 characters. 
  * The domain name must start with a lowercase letter. 
  * Each section in the domain name, which is delimited by dots, has the following requirements: 
    * Must start with a lowercase letter. 
    * Must not end with a dash. 
    * The remaining characters can be lowercase letters, numbers, or dashes. 
    * The maximum length is 63 characters. 



## Verifying ownership

Only the user account that has verified ownership of the domain name can deploy the Endpoints configuration initially. After that first deployment, you can grant the more restrictive **Service Config Editor** role to a user, group, or service account. See [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access) for more information.

To verify that you own the domain name:

  1. Go to [Search Console](https://search.google.com/search-console/welcome).

  2. Click **Domain**.

  3. Enter your domain name.

**Important:** Don't include protocol identifiers such as `http://` or `https://`. Enter only the domain name, such as `example.com` or a subdomain, such as `api.example.com`.
  4. Click **Continue**.

  5. On the **Record Type** Dropdown in the **Verify domain ownership via DNS record** banner, use the **Recommended methods** option if possible.

  6. Sign in to your Domain name provider and complete the verification process per the instructions. Your Domain name provide may be eligible for [AutoDNS](https://developers.google.com/search/blog/2019/09/auto-dns-verification).

![Search Console UI](https://docs.cloud.google.com/static/endpoints/docs/images/searchconsole.png)

  7. Follow the directions provided on **Search Console** until you complete your domain's verification.


**Important:** The domain name verification is automatically re-confirmed about every 30 days. If you remove the verification string from your DNS settings, you lose the ability to change the configuration within the Google Cloud console. However, if this happens, the serving setup for the domain doesn't change and the app continues to serve over that domain.

## Delegating to developers

After you are verified as a domain owner in Search Console, you can optionally delegate access to subdomains to developers within the organization. This allows those developers to create Endpoints APIs without having to verify domain ownership themselves.

For more information on delegating, see [Managing users, owners, and permissions](https://support.google.com/webmasters/answer/2453966?ref_topic=4564315).

## Configuring your domain for SSL

You might want to configure your domain for SSL. Note that some types of [authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users) require SSL.

## What's next

  * [Serving an API from your domain name](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
