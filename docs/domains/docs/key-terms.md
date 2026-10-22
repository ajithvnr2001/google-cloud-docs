---
url: https://docs.cloud.google.com/domains/docs/key-terms/
title: Important terminology \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:27.531996+00:00
---

# Important terminology  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Important terminology Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page provides important terminology that applies to Cloud Domains. Review these terms to better understand how Cloud Domains works and the concepts on which it is built.

For more information, see the [Cloud Domains overview](https://docs.cloud.google.com/domains/docs/overview).

Cloud DNS
    Cloud DNS is a high-performance and resilient DNS hosting provider that you can use with Cloud Domains to publish your domain names to the global DNS namespace. For detailed information about Cloud DNS concepts and important terminology, see the [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
DNS hosting provider
    

A DNS hosting provider is a company that maintains DNS name servers.

**Caution:** Google Domains as your Domain Name System (DNS) provider for your domains in Cloud Domains is retired, and some DNS functionality from Cloud Domains is no longer supported. For more information, see [Cloud Domains feature deprecation](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations). 

If you choose Cloud DNS as your DNS provider, then Google is your DNS hosting provider. If you are using custom name servers, then the company responsible for those name servers acts as your DNS hosting provider.

domain ending or top-level domain (TLD)
    

A domain ending is the last label in a domain name, like `.com`. Thousands of endings exist, and each ending is controlled by a registry. Customers of a registrar purchase domain names that are a single label plus the domain ending, such as `google.com`.

Often, the domain ending is just a single label like `.com`, in which case the domain ending is also the top-level domain (TLD). In some cases, a registry controls a multi-label domain ending like `.co.uk`, and customers purchase domain names one level below that, like `google.co.uk`. While not always technically accurate, it is common to refer to all registry-controlled domain endings as TLDs.

For a detailed explanation of TLDs, see [Top-level domain](https://wikipedia.org/wiki/Top-level_domain).

domain name
    

A domain name is a character string comprised of several parts called labels that are separated by dots to represent the domain hierarchy. Domain names have a domain ending corresponding to their registry operator. Domain names can be equivalently written in either Unicode or Punycode.

Domain Name System (DNS)
    

The Domain Name System (DNS) is a hierarchical distributed database that stores IP addresses and other data and allows queries by name. To learn more about DNS, see the [DNS overview page](https://docs.cloud.google.com/dns/docs/dns-overview).

name servers
    

Name servers identify the location of your domain on the internet. A DNS name server stores DNS records for a domain name and responds with answers to queries against its database. For a detailed explanation of name servers, see [Name server](https://wikipedia.org/wiki/Name_server).

premium domains
    

Premium domains are domains offered for sale or resale at a premium price. There are two kinds of premium domains:

  * **Aftermarket premium domains:** Domains offered for resale by owners for a premium price. After the initial premium price, you can renew your domains at the regular annual renewal price.
  * **Registry premium domains:** Domains offered by the registry for a premium price. Usually, when you transfer, renew, restore, or add more years of registration to a domain, you're charged the initial premium price.


registrant
    

A registrant is the registered name holder of a DNS domain. A registrant holds the _rights_ to the domain for the duration of the registration period. Because a domain's registration can be renewed indefinitely (up to 10 years at a time), a registrant is often considered the _owner_ of the domain.

registrar
    

A registrar is an organization that manages the registration of domain names for one or more of the DNS registries. A registrar acts as an interface between a registrant (owner) and a registry (database of domains). Registrars sell domain names, provide registration services, and offer other value-added services applicable to domains. For details about registrars, see [Domain name registrars](https://wikipedia.org/wiki/Domain_name_registrar).

For Cloud Domains, domain registrations are provided by Squarespace. The registrar of record is often Squarespace but might vary based on the TLD. To determine the registrar of record for your domain, search the [WHOIS database](https://docs.cloud.google.com/domains/docs/key-terms#terms-whois).

registration
    

Registration is the process through which a registrant registers a domain with a DNS registrar. A registrant can register a domain for a period from one to ten years. When the registration period expires, the registrant can renew or extend the registration. The registrant must provide contact information to the registrar for inclusion in the WHOIS database.

To register a domain by using Cloud Domains, see [Register a domain](https://docs.cloud.google.com/domains/docs/register-domain). To edit your domain registration settings, see [Edit registrations](https://docs.cloud.google.com/domains/docs/edit-registration-settings).

registry
    

A registry is a database that contains registrant information for second-level DNS domains (`google.com`, `example.com`) beneath a given domain ending or TLD (`.com`). A registry can control any domain ending and can allow you to register domains under that domain ending—for example, `.co.uk` and `google.co.uk`.

A registry operator is an organization that maintains the administrative data for one or more top-level or lower-level DNS domains. For example, VeriSign is responsible for several top-level domains, including the `.com`, `.net`, and `.name` domains. A registry operator is given authority for a domain through [ICANN](https://www.icann.org/), a corporation responsible for managing functions that maintain the core infrastructure of the internet. For more details, see [ICANN](https://wikipedia.org/wiki/ICANN).

resource records
    

Resource records provide DNS-based information about the hardware and software components that point to and support your domain (such as hosts, name servers, web servers, and email servers). For detailed information about resource records, see [Records](https://docs.cloud.google.com/dns/docs/dns-overview#records).

For a list of record types supported by Cloud DNS, see [Supported record types](https://docs.cloud.google.com/dns/docs/records-overview#supported_dns_record_types).

Unicode and Punycode
    

Within the Domain Name System, for historical reasons, domain names are stored in [ASCII](https://wikipedia.org/wiki/ASCII). Internationalized Domain Names (IDNs) that are normally written in [Unicode](https://wikipedia.org/wiki/Unicode) are compressed into ASCII with a scheme called [Punycode](https://wikipedia.org/wiki/Punycode).

Domain names expressed in Punycode start with the characters `xn--`. For example, an IDN representation of the Unicode `example.ελ` is `example.xn--qxam` in Punycode.

The Punycode and Unicode versions of a domain name are equivalent and used in different contexts. For example, the name of each `Registration` resource ends in the Punycode version of the corresponding domain name. On the other hand, in user-facing contexts, the domain name is generally displayed in Unicode for ease of use.

WHOIS database
    

The WHOIS database stores information about DNS domains, such as the following:

  * Registration contact information for registrant, administrator, and technical contacts
  * The domain's registrar
  * Creation, update, and expiry dates



The WHOIS protocol, which is a query and response protocol used for querying databases that store details about registered domain users, is documented in [RFC 3912](https://tools.ietf.org/html/rfc3912).

For details about WHOIS, see the [ICANN WHOIS](https://whois.icann.org/about-whois) page. You can look up registered domain names and associated details on the [ICANN WHOIS database](https://lookup.icann.org/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
