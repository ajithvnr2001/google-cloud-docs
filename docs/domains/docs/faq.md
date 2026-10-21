---
url: https://docs.cloud.google.com/domains/docs/faq/
title: Squarespace purchase of Google Domains FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:58.857040+00:00
---

# Squarespace purchase of Google Domains FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Resources ](https://docs.cloud.google.com/domains/docs/resources)



Send feedback 

#  Squarespace purchase of Google Domains FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This page provides help and answers to frequently asked questions about the Squarespace purchase of Google Domains registrations. For more information about deprecations and shut down features, see [Deprecations and shut down features](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations).

## How does the sale of Google Domains affect Cloud Domains?

Google Cloud continues to provide and support Cloud Domains following the [Squarespace purchase of Google Domains](https://support.google.com/domains/answer/13689670). Because Google Domains was the underlying domains registrar for Cloud Domains prior to Squarespace's purchase, there are some important changes that affect Cloud Domains.

Following the Squarespace purchase of Google Domains, Squarespace Domains is the registrar for your domains managed by Cloud Domains. Squarespace Domains is an independent domain registrar service provided by Squarespace. Your domain registrations with Cloud Domains and related data such as domain configurations and WHOIS data (which includes customer contact info and DNS delegation) are migrating to Squarespace Domains after a transition period which we anticipate completing no sooner than early 2024. Google and Squarespace are working to make the migration as seamless as possible.

After the migration, the information associated with your domain is governed by [Squarespace's Privacy Policy](https://www.squarespace.com/privacy), and the [Squarespace Terms of Service](https://www.squarespace.com/terms-of-service) applies to your registrations. No Google Cloud customer data is transferred to or exchanged with Squarespace.

Google continues to offer first-line customer support for Cloud Domains and is responsible for billing your account. Cloud Domains UI, Cloud Domains API, and Cloud Domains gcloud CLI continue to be supported.

## Are there changes to features after the Squarespace purchase of Google Domains?

After your domain registrations and related data are migrated to Squarespace, Cloud Domains continues to support searching and registering new domains, renewing existing domains, updating your contact, DNS settings, and transferring a registered domain to another registrar.

These activities rely on Squarespace Domains.

Squarespace has publicly committed to continue to use Google Cloud DNS infrastructure, so that the reliability and performance of DNS remains unchanged during the migration.

After the transition is complete, transferring domains from third-party registrars to Cloud Domains isn't supported. Furthermore, importing and exporting domains to and from Google Domains isn't supported.

## Whom do I contact for customer support for my domains?

Google Cloud continues to provide first-line customer support for all domains purchased through Cloud Domains. For more information, see [Support for Cloud Domains](https://docs.cloud.google.com/domains/docs/getting-support).

To get support for domains purchased directly through Google Domains contact [Squarespace support](https://support.squarespace.com/hc/en-us/articles/219648707-How-do-I-contact-Squarespace-Customer-Support).

## Can I continue to purchase domains using Cloud Domains?

Yes, you can continue to search and register for new domains using Cloud Domains. After migration, Google Cloud becomes a reseller of Squarespace Domains. When you buy new domains using Cloud Domains after migration, the registrar of record is Squarespace.

## What happens if my domain registered with Cloud Domains comes up for renewal?

Cloud Domains automatically renews your domains registered with Cloud Domains when they come up for renewal. But, you can turn off automatic renewal at any time.

## How can I disable automatic renewal of my domain?

To turn off automatic renewal of your domain, see [Turn off automatic renewal for a domain name](https://docs.cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew).

## What terms and conditions are applicable after the Squarespace purchase of Google Domains?

After the transaction closes, existing domain accounts are owned by Squarespace, and you can continue to manage your domains by using Cloud Domains. Google's [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://domains.google.com/tos) continue to apply.

After your domain is migrated, the information associated with your domain registrations—including domain configuration and WHOIS data, which includes customer contact info and DNS delegation—is governed by [Squarespace's Privacy Policy](https://www.squarespace.com/privacy), and [Squarespace's Terms of Service](https://www.squarespace.com/terms-of-service) apply to your registrations.

Ensure that you read [Squarespace's Terms of Service](https://www.squarespace.com/terms-of-service) and [Privacy Policy](https://www.squarespace.com/privacy).

Any new domain registrations purchased through Cloud Domains after the sale closes are governed by [Squarespace's Terms of Service](https://www.squarespace.com/terms-of-service) and, following migration, information associated with such domain registrations is governed by [Squarespace's Privacy Policy](https://www.squarespace.com/privacy).

## Are other Google Cloud services affected?

This change doesn't affect other Google Cloud services, including Cloud DNS.

## How do I manage domains purchased through a mix of Google Domains and Cloud Domains?

You can continue to manage domains that are registered with or imported to Cloud Domains by using Cloud Domains API.

## What happens to my domains on Cloud Domains that use Google Domains DNS as the DNS provider?

After each domain is migrated to Squarespace, if your domain uses Google Domains DNS, you can't make any changes to your DNS records. You must change your DNS provider to make changes.

DNS resolution continues to use the last successful configuration of your static DNS records. Domain forwarding and email forwarding use your last successful configuration, and you can no longer change these settings. Dynamic DNS updates no longer work, and dynamic DNS records point to the last known IP address before the retirement.

For new domain registrations, you cannot configure Google Domains DNS as your DNS provider. However, if you have already registered domains that use Google Domains, you can export your Google Domains DNS settings to Cloud DNS or another DNS provider. You can also export your domain and email forwarding configurations to another hosting provider. For more information, see [Migrate Google Domains DNS settings](https://docs.cloud.google.com/domains/docs/export-dns-settings).

## What changes do I need to make to my DNS provider settings for my domains in Cloud Domains?

If you use [Cloud DNS](https://docs.cloud.google.com/dns) or another third-party DNS provider for your domain using the [`CustomDNS` field](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#CustomDns), you don't need to take any action.

If you use Google Domains DNS as your DNS provider, we recommend updating your domain's [DNS setting](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#DnsSettings) to use Cloud DNS or another third-party DNS provider. For steps to migrate your DNS provider from Google Domains DNS to Cloud DNS, see [How do I update the DNS setting for my domain in Cloud Domains from Google Domains DNS to Cloud DNS](https://docs.cloud.google.com/domains/docs/export-dns-settings#migrate-dns-configuration).

If you use domain forwarding, email forwarding, or Dynamic DNS features from Google Domains DNS, migrate your DNS to Cloud Domains or a third-party DNS provider. For more information, see [Migrate Google Domains DNS settings](https://docs.cloud.google.com/domains/docs/export-dns-settings#export-forwarding).

## How do I update the DNS settings for my domain in Cloud Domains from Google Domains DNS to Cloud DNS?

To migrate your Google Domains DNS settings and export domain and email forwarding configurations, see [Migrate Google Domains DNS settings](https://docs.cloud.google.com/domains/docs/export-dns-settings#migrate-dns-configuration).

## What happens to my domains that use the deprecated privacy protection contact privacy settings?

Squarespace is the registrar for your domains managed by Cloud Domains. All domains with [Contact details Privacy Protection On](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#contactprivacy) are updated to [Limited info available to the public](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#contactprivacy).

This means that your contact data isn't shared with the third-party contacts-proxy provider, and all your contact details are marked as `REDACTED FOR PRIVACY` in the [WHOIS](https://docs.cloud.google.com/domains/docs/key-terms#terms-whois) database. The exceptions are the contact's country and state or province which are publicly visible. If you provide an organization name, it might be publicly visible.

## Can I import domain registrations from Google Domains to Cloud Domains?

No. You cannot import domain registrations from Google Domains to Cloud Domains.

## Can I import my domain registrations from Squarespace to Cloud Domains?

No. You cannot import or export domain registrations between Squarespace and Cloud Domains.

## Can I export domain registrations from Cloud Domains to Google Domains?

No. All domains managed by Google Domains are migrated to Squarespace, and you can't export a registered domain from Cloud Domains to Google Domains. For more information, see [Deprecations and shut down features](https://docs.cloud.google.com/domains/docs/export-domains).

## Can I move registrations in Cloud Domains between Google Cloud projects?

Domain registrations with Cloud Domains cannot be moved between Google Cloud projects.

## Can I delete a domain registration in Cloud Domains?

You can't [delete active domains from Cloud Domains](https://docs.cloud.google.com/domains/docs/delete-domain). You can transfer your domain registration to a third-party domain registrar or turn off automatic renewal of your domain.

## Can I transfer a registered domain from a third-party domain registrar to Cloud Domains?

You can't transfer a registered domain from another registrar.

## Can I transfer a registered domain from Cloud Domains to another registrar?

Yes, you can [transfer a registered domain to another registrar](https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar).

## Can I use Squarespace to manage my domain registrations with Cloud Domains?

You can't use Squarespace to view or manage your domains that are registered with Cloud Domains. To manage your domains in Cloud Domains, use the Google Cloud console, the Cloud Domains API, and the Google Cloud CLI.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
