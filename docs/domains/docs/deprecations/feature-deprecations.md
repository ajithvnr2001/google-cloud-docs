---
url: https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations/
title: Deprecations and shut down features \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:37.852207+00:00
---

# Deprecations and shut down features  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Resources ](https://docs.cloud.google.com/domains/docs/resources)



Send feedback 

#  Deprecations and shut down features Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Cloud Domains. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature | Deprecation date | Shutdown date | Details  
---|---|---|---  
Google Domains as a Domain Name System (DNS) provider | October 19, 2023 |  | Google Domains as your Domain Name System (DNS) provider for your domains in Cloud Domains is retired, and some DNS features from Cloud Domains aren't supported. 

  1. New domain registrations cannot use the free DNS zone provided by Google Domains
  2. You can continue to use the existing domains names that use Google Domains as the DNS provider
  3. You can continue to use the Google Domains user interface to update the DNS settings until the domains are migrated to Squarespace

  
Domain forwarding (HTTP `301` and `302` response status codes) and email forwarding | October 19, 2023 | January 22, 2024 | Until the domain is migrated to Squarespace, you can use the Google Domains user interface to configure this setting. After the domains are migrated, you can continue using domain and email forwarding. However, you won't be able to change your domain forwarding or email forwarding settings.   
Dynamic DNS | October 19, 2023 | January 22, 2024 | You can continue using the Google Domains user interface to configure this setting until the domain is migrated to Squarespace. Afterward, Dynamic DNS updates doesn't work, and your domain points to the last known IP address before the retirement.   
Import domains | October 19, 2023 | January 22, 2024 | You can't import your existing registered domain from Google Domains to Cloud Domains.   
Export domains | October 19, 2023 | January 22, 2024 | You can't export a registered domain from Cloud Domains to Google Domains.   
Transfer domains | October 19, 2023 | January 22, 2024 | You can't transfer a registered domain from a third-party domain registrar to Cloud Domains.   
Contact privacy | October 19, 2023 |  | The `PRIVATE_CONTACT_DATA` setting for [contact privacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#ContactPrivacy) is changed to `REDACTED_CONTACT_DATA` when a domain is migrated to Squarespace.   
  
On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. After January 22, 2024, you can't use the retired features of Cloud Domains. For more information, see the [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq).

Google Domains as your Domain Name System (DNS) provider for your domains in Cloud Domains is being retired. This change doesn't affect your domains that use [Cloud DNS](https://docs.cloud.google.com/dns) as your DNS provider.

The following features from Google Domains aren't supported in Cloud Domains:

  * Domain forwarding (HTTP `301` and `302` response status codes)
  * Email forwarding
  * Dynamic DNS



If your domain continues to use [Google Domains DNS](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#googledomainsdns) after Google Domains DNS is retired, your last Google Domains DNS settings work, but you can't make any changes to your DNS records until you change your DNS provider. Similarly, domain forwarding and email forwarding work according to the last supported configuration, but you can't change your domain forwarding or email forwarding settings. Dynamic DNS updates no longer work, and dynamic DNS records point to the last known IP address before the retirement.

[Transfer-In](https://docs.cloud.google.com/domains/docs/transfer-domain-from-another-registrar) of your domain registrations from third-party domain registrars into Cloud Domains isn't possible. You can [transfer-out](https://docs.cloud.google.com/domains/docs/transfer-domain-to-another-registrar) your domain registrations to third-party domain registrars.

In addition, [import](https://docs.cloud.google.com/domains/docs/import-domains) of domain registrations from Google Domains to Cloud Domains or [export](https://docs.cloud.google.com/domains/docs/export-domains) of domain registrations from Cloud Domains to Google Domains isn't possible. You also can't move domain registrations with Cloud Domains between your Google Cloud projects.

You can't [delete a domain registration resource](https://docs.cloud.google.com/domains/docs/delete-domain) in Cloud Domains until it has expired. However, you can disable auto-renewal of domain registrations in Cloud Domains by using [Cloud Domains registration resource management settings](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#renewalmethod).

Domains that use the `PRIVATE_CONTACT_DATA` setting for [contact privacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#ContactPrivacy) are changed to use `REDACTED_CONTACT_DATA`. Your data is not shared with a third-party contact privacy provider, and it is instead shown as redacted in public contact databases like WHOIS.

Also, you can't use the Google Domains user interface to view and manage your domain registrations after your domain is migrated to Squarespace. You can continue to use the Google Cloud CLI, Cloud Domains, and the Google Cloud console to manage your domains.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
