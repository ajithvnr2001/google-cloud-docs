---
url: https://docs.cloud.google.com/media-cdn/docs/troubleshooting-certificate-issuance/
title: Troubleshoot certificate issuance \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:21.848870+00:00
---

# Troubleshoot certificate issuance  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/troubleshooting-certificate-issuance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Troubleshoot certificate issuance Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve certificate issuance issues that might occur when you [issue and attach SSL (TLS) certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates#issue-cert), or provision certificates with [DNS authorizations](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates#dns-auth).

## Troubleshoot certificate issuance

The most common cause of failed issuance (or renewal) is due to invalid or missing DNS records, which prevent Certificate Manager from validating domain ownership.

  * Check that the DNS record can be reached via public DNS. The value of the `_acme-challenge` CNAME record (the underscore is required) for your domain should return the value provided in the `dnsResourceRecord.data` from when you created the authorization. You can [use Google Public DNS](https://dns.google/) to quickly check that the record is resolvable and valid.
  * Ensure that the domains you are requesting certificates for either match, or are subdomains of, the authorizations you are associating with the certificate request. For example, an authorization for `media.example.com` allows you to issue certificates for `media.example.com`, `uk.media.example.com` and `staging.media.example.com`, but _not_ `www.example.com`.
  * Existing [CAA records](https://docs.cloud.google.com/dns/docs/dnssec-advanced#caa) on your domain might prevent Certificate Manager from issuing certificates for your domain. You should ensure that there is a CAA record for `pki.goog` to allow Google to issue certificates for your authorized domains. If the issue is due to a CAA record restriction, the `failure_reason` field in the API response contains a value of `CAA`.
  * You can only attach certificates with scope `EDGE_CACHE` to an Edge Cache Service. If you did not explicitly specify a scope of `EDGE_CACHE` when creating the certificate, you must re-issue the certificate using an existing DNS authorization.



When creating a certificate with multiple domain names, any invalid domain authorization prevents the certificate from being issued or renewed. This ensures that all of your requested domains are included in the issued certificate. Make sure that the DNS record, domain name, and CAA record configuration are valid for each of the domains associated with a certificate.

## Failure reasons

The following table describes the failure reasons that might be returned when attempting to issue a certificate, their causes, and suggested fixes:

Type | Error | Troubleshooting Steps  
---|---|---  
DNS Authorization | CONFIG |  We were unable to validate the certificate via DNS. In most cases, this means the DNS record is missing, invalid (incorrectly copied), or you are trying to issue a certificate for a subdomain that is not a child of the authorized domain.   
DNS Authorization | CAA |  Certificate issuance is prohibited by the current set of [CAA records](/media-cdn/docs/ssl-certificates#caa-records-roots) associated with the domain or the CAA record might have only just been updated.   
DNS Authorization | RATE_LIMITED |  (Uncommon) You might be issuing certificates at a rate faster than accepted by the CA or domain (for example, tens per minute or more).   
Certificate | AUTHORIZATION_ISSUE |  The individual domain failed authorization. Check the value of **managed.authorizationAttemptInfo.failureReason** for the domain to understand why authorization might have failed.   
  
## What's next

  * Read [Configure SSL certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates).
  * Understand [client connectivity](https://docs.cloud.google.com/media-cdn/docs/client-connectivity) and protocol support.
  * Review how SSL (TLS) [connections are made](https://docs.cloud.google.com/media-cdn/docs/origins#supported_origins_and_protocols) to your origins.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
