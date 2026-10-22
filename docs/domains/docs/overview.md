---
url: https://docs.cloud.google.com/domains/docs/overview/
title: Cloud Domains overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:53.195191+00:00
---

# Cloud Domains overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Cloud Domains overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page provides an overview of Cloud Domains features and capabilities. Cloud Domains lets you register and configure a domain in Google Cloud.

Cloud Domains is available in all the countries where Google Cloud is available.

## Benefits of using Cloud Domains

Cloud Domains provides the following benefits:

  * Lets you register a domain through Google Cloud and seamlessly attach it to any application. You can perform these steps by calling the Cloud Domains API or by using the Google Cloud CLI or the Google Cloud console.

  * Bills your domains through the same Cloud Billing account that you already have. Cloud Domains also lets you automatically review your registered domain as long as your Cloud Billing account stays active.

  * Is available in all locations where Google Cloud is available.

  * Lets you manage domain registrations per project, not per individual. You can manage one or more of your domains in Cloud Domains as part of a single project. Cloud Domains allows team collaboration because the domain is associated with the project. You can use Identity and Access Management (IAM) to manage all permissions in one place.

  * Supports programmatic access to domain registration, letting you integrate your systems. You can control access to the API by using standard Google Cloud permissions and quotas.

  * For detailed pricing information, see [Pricing](https://cloud.google.com/domains/pricing).

If you use Cloud DNS to configure your domain name servers, [Cloud DNS bills you separately](https://cloud.google.com/dns/pricing).




## Supported use cases

You can use Cloud Domains to do the following:

  * Search for available domains.
  * Buy a domain name.
  * Manage your registration.
  * Optional: Transfer your domain from Cloud Domains to another registrar.



## DNS providers

[Name servers](https://docs.cloud.google.com/domains/docs/key-terms#terms-name-servers) identify the location of your domain on the internet and define your domain's DNS providers. When you register a domain with Cloud Domains, you must choose a DNS provider for the domain. The following table summarizes the DNS provider options in Cloud Domains.

**Caution:** Google Domains as your Domain Name System (DNS) provider for your domains in Cloud Domains is retired, and some DNS functionality from Cloud Domains is no longer supported. For more information, see [Cloud Domains feature deprecation](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations). 

DNS provider | Description | Cost  
---|---|---  
**Cloud DNS** | Google recommends that you use Cloud DNS as your DNS provider for all your name servers. | Additional Cloud DNS charges apply. For details, see [ the Cloud DNS pricing page.](https://docs.cloud.google.com/dns/pricing)  
**Custom name servers** | If you choose this option, you can use Cloud Domains to configure your name servers, and then use a third-party DNS provider to configure your DNS resource records.  | Check with your DNS provider.  
  
For instructions about registering a domain, see [Register a domain](https://docs.cloud.google.com/domains/docs/register-domain).

## Supported domain endings (TLDs)

Cloud Domains supports all the domain endings listed in the [Pricing table](https://cloud.google.com/domains/pricing#pricing-table). Any domain ending that is not listed on the Cloud Domains pricing page is not supported.

## Automatic renewal

After you set up [Cloud Billing](https://docs.cloud.google.com/billing/docs) and complete your domain registration, Cloud Domains automatically sets up the registration to renew every year. Automatic renewal helps you keep ownership of your domain by not missing a payment. You can turn off automatic renewal after you've registered your domain. For more information, see [Turn off automatic renewal for a domain name](https://docs.cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew).

If your domain expired within the past 30 days, you can renew it using the Google Cloud CLI or the Cloud Domains API. The domain's new expiry date is one year after the previous expiry date, and you are charged the yearly price for renewal. For more information, see [Renew a recently expired domain](https://docs.cloud.google.com/domains/docs/renew-expired-domain).

## Pricing

During the registration process, the price for each domain is available. The total cost is calculated on the registration page as you add domains to your cart. Prices vary based on TLDs. For example, if you buy `example.com`, `example.blog`, and `example.art`, the cost of each of these domains might be different because the TLDs `.com`, `.blog`, and `.art` have different costs.

For detailed pricing information, see [Pricing](https://cloud.google.com/domains/pricing). For billing, see [Billing questions](https://docs.cloud.google.com/domains/docs/billing-questions).

## DNS security (DNSSEC)

Cloud Domains supports DNSSEC, which protects your domains from spoofing and cache poisoning attacks. When you use a validating resolver like [Google Public DNS](https://developers.google.com/speed/public-dns), DNSSEC provides strong authentication (but not encryption) of domain lookups. For more information about DNSSEC, see the [DNSSEC overview](https://docs.cloud.google.com/dns/docs/dnssec).

If you use Cloud DNS to provide name servers for Cloud Domains, you can enable or disable managed DNSSEC when you create a public zone for your domain. For instructions, see [Create a public zone](https://docs.cloud.google.com/dns/docs/zones#create-pub-zone).

## Contact information

**Note:** Starting in August 2025: For generic TLD domains, the [ICANN Registration Data Policy](https://www.icann.org/en/contracted-parties/consensus-policies/registration-data-policy) no longer requires both administrative and technical registrant contact information. If you submit administrative and technical contact information, it is ignored for generic TLD domains.  
  
There are no changes for country-code TLD domains and all contact information continues to be required. 

When you register a domain, you must submit contact information for that domain. There are three types of contact information:

  * **Registrant:** owner of the domain
  * **Admin:** (only required for country-code TLD domains) person responsible for administrative decisions about the domain
  * **Technical:** (only required for country-code TLD domains) person responsible for technical changes to the domain



You can choose to enter the same information for all three types of contacts for a domain or choose to enter different contact details for each type of contact. You can also [modify the settings](https://docs.cloud.google.com/domains/docs/edit-registration-settings#editing_contact_settings) as needed.

Accurate contact information is key because the registrant is the _rightful owner of the domain_. Access to the registrant's contact information, including email, phone number, or mailing address, can be used to gain management access to the domain.

Your contact information also enables [ICANN](https://www.icann.org/) to reach you in case of any problems. This information becomes the public contact information for your domain in the [WHOIS](https://docs.cloud.google.com/domains/docs/key-terms#terms-whois) database. You can control the amount of information available to the public by choosing the appropriate [privacy protection](https://docs.cloud.google.com/domains/docs/overview#privacy-protection) settings.

## Privacy protection

When you register a domain, [ICANN](https://www.icann.org/) requires Cloud Domains to publish the registrant's name and other contact information in the [WHOIS database](https://docs.cloud.google.com/domains/docs/key-terms#terms-whois). The WHOIS database is open to the public, which means that published contact information is available to anyone at any time.

Cloud Domains provides three privacy-protection options for most domain suffixes (for example, `.com`, `.net`) that let you make some, none, or all of your information private.

Privacy option | Description  
---|---  
**Privacy protection on** |  **Caution:** If your domain uses the `PRIVATE_CONTACT_DATA` setting for [contact privacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#ContactPrivacy), it is changed to `REDACTED_CONTACT_DATA` when the domains are migrated to Squarespace. Your data is not shared with a third-party contact privacy provider and is instead shown as redacted in public contact databases like WHOIS. For more information, see [Cloud Domains feature deprecation](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations).  Choosing this option ensures that your contact information is not available to the public. To help protect your contact information and prevent spam, a third party provides alternate (proxy) contact information for your domain in the public directory. The third-party provider forwards all messages that are sent to your proxy contact information to the actual private contact information.  Cloud Domains does not offer privacy protection for all domain endings or [top-level domains (TLDs)](https://docs.cloud.google.com/domains/docs/key-terms#terms-tld). [Registries](https://docs.cloud.google.com/domains/docs/key-terms#terms-registry), the organizations that manage domain endings, have policies prohibiting the use of privacy protection for certain TLDs.   
**Limit your info available to the public** | Choosing this option makes limited non-identifying information available to the public. The actual information available publicly depends on the domain that you have chosen. If you provide an organization name, it might be publicly visible.   
**Make all contact info public** | Choosing this option makes all your contact information available to the public through the [WHOIS database](https://docs.cloud.google.com/domains/docs/key-terms#terms-whois).   
  
For information about how to use contact privacy, see the [`ContactPrivacy`](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#contactprivacy) section in the reference documentation.

## Access control

Google Cloud offers IAM, which lets you assign access to specific Google Cloud resources and prevents unwanted access to other resources.

For details about access control and how to manage access for Cloud Domains, see [Roles and permissions](https://docs.cloud.google.com/domains/docs/access-control).

## What's next

  * To get started with Cloud Domains, see the [Quickstart](https://docs.cloud.google.com/domains/docs/buy-register-domain).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).
  * To learn more about Cloud DNS, see the [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
