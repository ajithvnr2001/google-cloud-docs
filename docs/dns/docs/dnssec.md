---
url: https://docs.cloud.google.com/dns/docs/dnssec/
title: DNS Security Extensions (DNSSEC) overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:05.598734+00:00
---

# DNS Security Extensions (DNSSEC) overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/dnssec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  DNS Security Extensions (DNSSEC) overview Stay organized with collections  Save and categorize content based on your preferences. 

The Domain Name System Security Extensions (DNSSEC) is a feature of the Domain Name System (DNS) that authenticates responses to domain name lookups. It does _not_ provide privacy protections for those lookups, but prevents attackers from manipulating or poisoning the responses to DNS requests.

To protect domains from spoofing and poisoning attacks, enable and configure DNSSEC in the following places:

  1. The DNS zone. If you [enable DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling) for a zone, Cloud DNS automatically manages the creation and rotation of DNSSEC keys (DNSKEY records) and the signing of zone data with resource record digital signature (RRSIG) records.

  2. The top-level domain (TLD) registry (for `example.com`, this would be `.com`). In your TLD registry, you must have a DS record that authenticates a DNSKEY record in your zone. Do this by [activating DNSSEC](https://docs.cloud.google.com/dns/docs/registrars#add-ds) at your domain registrar.

  3. The DNS resolver. For full DNSSEC protection, you must use a DNS resolver that _validates_ signatures for DNSSEC-signed domains. You can enable validation for individual systems or your local caching resolvers if you administer your network's DNS services.

For more information about DNSSEC validation, see the following resources:

     * [Do you have DNSSEC validation enabled?](https://blog.apnic.net/2017/05/11/dnssec-validation-enabled/)
     * [Deploying DNSSEC with BIND and Ubuntu Server (Part 1)](https://blog.apnic.net/2019/05/23/how-to-deploying-dnssec-with-bind-and-ubuntu-server/)
     * [DNSSEC Guide: Chapter 3. Validation](https://dnsinstitute.com/documentation/dnssec-guide/ch03s03.html)
     * [DNSSEC](https://wiki.debian.org/DNSSEC)

You can also configure systems to use public resolvers that validate DNSSEC, notably [Google Public DNS](https://developers.google.com/speed/public-dns/docs/using) and [Verisign Public DNS](https://www.verisign.com/security-services/public-dns/index.xhtml).




The second point limits the domain names where DNSSEC can work. Both the registrar and registry must support DNSSEC for the TLD that you are using. If you cannot add a DS record through your domain registrar to activate DNSSEC, enabling DNSSEC in Cloud DNS has no effect.

Before enabling DNSSEC, check the following resources:

  * The DNSSEC documentation for both your domain registrar and TLD registry
  * The [Google Cloud community tutorial's](https://github.com/GoogleCloudPlatform/community/blob/master/archived/dnssec-cloud-dns-domains/index.md#domain_registrar-specific_instructions) domain registrar-specific instructions
  * The [ICANN list](https://www.icann.org/search/#!/?searchText=domain%20registrar%20DNSSEC%20support) of domain registrar DNSSEC support to confirm DNSSEC support for your domain.



If the TLD registry supports DNSSEC, but your registrar does not (or does not support it for that TLD), you might be able to transfer your domains to a different registrar that does. After you have completed that process, you can activate DNSSEC for the domain.

## Management operations

For step-by-step instructions for managing DNSSEC, see the following resources:

  * To change the DNSSEC state of the zone from `Transfer` to `On`, see [Leaving DNSSEC transfer state](https://docs.cloud.google.com/dns/docs/dnssec-config#leaving-transfer).

  * To enable DNSSEC for delegated subdomains, see [Delegating DNSSEC-signed subdomains](https://docs.cloud.google.com/dns/docs/dnssec-advanced#subdelegation).




## Record set types enhanced by DNSSEC

For more information about record set types and other record types, see the following resources:

  * To control which public certificate authorities (CAs) can generate TLS or other certificates for your domain, see [CAA records](https://docs.cloud.google.com/dns/docs/dnssec-advanced#caa).

  * To enable opportunistic encryption through IPsec tunnels, see [IPSECKEY records](https://docs.cloud.google.com/dns/docs/dnssec-advanced#ipseckey).




## DNS record types with DNSSEC-secured zones

For more information about DNS record types and other record types, see the following resource:

  * To enable SSH client applications to validate SSH servers, see [SSHFP records](https://docs.cloud.google.com/dns/docs/dnssec-advanced#sshfp).



## Migration or transfer of DNSSEC-enabled zones

Cloud DNS supports migrating DNSSEC-enabled zones where DNSSEC has been activated at the domain registry without breaking the chain of trust. You can migrate zones to or from other DNS operators that also support migration.

  * To migrate a DNSSEC-signed zone to Cloud DNS, see [Migrate DNSSEC-signed zones to Cloud DNS](https://docs.cloud.google.com/dns/docs/dnssec-migrate#migrating-to).

  * To migrate a DNSSEC-signed zone to another DNS operator, see [Migrate DNSSEC-signed zones from Cloud DNS](https://docs.cloud.google.com/dns/docs/dnssec-migrate#migrating-from).




If your existing domain is hosted by your registrar, we recommend migrating the name servers to Cloud DNS before transferring to another registrar.

## What's next

  * To view DNSSEC key records, see [View DNSSEC keys](https://docs.cloud.google.com/dns/docs/dnskeys).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
