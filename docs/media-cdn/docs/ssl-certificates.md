---
url: https://docs.cloud.google.com/media-cdn/docs/ssl-certificates/
title: SSL (TLS) Certificates \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:27.194143+00:00
---

# SSL (TLS) Certificates  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/ssl-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  SSL (TLS) Certificates Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN has first-class support for serving TLS-encrypted (HTTPS) traffic from your own domain name, as well as support for [signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests). Media CDN is served from your own domain (_Bring-Your-Own_ or BYO domain), and does not need to be served from a Google-hosted domain.

  * There are no additional charges associated with serving SSL (TLS) traffic or obtaining Google-managed certificates: protecting end-user traffic should not be at a premium.
  * Media CDN supports both Google-managed certificates, allowing Google to manage rotation, keys and secure distribution to thousands of edge nodes, as well as self-managed (uploaded) certificates.
  * Each Service can support up to 5 SSL certificates.
  * Each managed certificate can have up to 100 names (Subject Alternative Names).

**Note:** Certificates can be issued or uploaded with Certificate Manager. Only certificates with a scope of `EDGE_CACHE` can be associated with an `EdgeCacheService`.

We recommend serving your Edge Cache service from dedicated hostnames (subdomains) and using separate managed certificates for your media domains as a good security practice.

### Create and issue certificates

To validate, issue, and attach a managed SSL (TLS) certificate to a Media CDN service, see [configuring SSL certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates).

### Certificate types

Media CDN supports two types of certificates:

  * **Managed certificates** , which Google can provision on your behalf for domain names you own. You do not need secure keys, and certificates are automatically renewed.
  * **Self-managed certificates** , which you upload to Certificate Manager directly. You are responsible for uploading a valid, publicly trusted certificate, as well as replacing the certificate prior to expiry.



Because managed certificates can be authorized and issued prior to directing traffic at Media CDN, you can provision certificates before cutting over your production traffic and avoid downtime.

**Note:** We strongly recommend using managed certificates, which avoid the risk of a certificate accidentally expiring and causing your user-facing requests to fail.

In some cases, such as where you require key-pinning in mobile applications, or support for legacy devices with outdated trust stores, you might need to use self-managed certificates. You can also use both managed and self-managed certificates on the same service if you have specific domain names (hosts) that require self-managed certificates.

### Authorizing certificate issuance

DNS authorization lets you verify domain ownership and provision Google-managed certificates even before your production environment is fully set up. This is particularly useful when you're migrating certificates to Google Cloud.

Certificate Manager verifies domain ownership through DNS records. Each DNS authorization stores information about a DNS record, and covers a single domain and its wildcard (for example, both `myorg.example.com` and `*.myorg.example.com`). A wildcard covers only the first subdomain level, and doesn't cover deeper subdomain levels. For example, `*.myorg.example.com` doesn't cover `sub.subdomain.myorg.example.com`.

When creating a Google-managed certificate, you can use one or more DNS authorizations to provision and renew certificates. If you have multiple certificates for a single domain, then you can use the same DNS authorization for all the certificates. However, your DNS authorizations must cover all domains listed in the certificate; if they don't, creating and renewing certificates will fail.

To set up DNS authorization, you must add a `CNAME` record to your DNS configuration. You can use this record to validate the subdomain under your target domain. The `CNAME` record points to a special Google Cloud domain that Certificate Manager uses to verify your domain ownership. When you create a DNS authorization, Certificate Manager returns this `CNAME` record and verifies your ownership.

Remember, the `CNAME` record also grants Certificate Manager the permission to provision and renew certificates for the target domain within your Google Cloud project. To revoke these permissions, remove the CNAME record from your DNS configuration.

**Note:** The validation sub-domain must be openly resolvable from the internet. Split-horizon or DNS firewall environments can interfere with certificate provisioning.

### Per-project DNS authorization

Per-project DNS authorization lets you manage certificates independently within each Google Cloud project. Using per-project DNS authorization, Certificate Manager can issue and handle certificates for each project separately. The DNS authorizations and certificates used within a project are self-contained and don't interact with artifacts from other projects.

To activate per-project DNS authorization, choose the `PER_PROJECT_RECORD` option when creating a DNS authorization. You will then receive a unique `CNAME` record that includes both a subdomain and a target specific to that project. You shoud add this `CNAME` record to the DNS zone of the relevant domain.

**Note:** Due to ongoing IETF standardization efforts for account-based DNS authorization, Google uses a custom implementation of account-based DNS authorization for per-project DNS authorizations.

### Multiple domains per certificate

Certificates issued by Certificate Manager allow you to specify multiple domain names (hostnames) on the same certificate as [Subject Alternative Names](https://en.wikipedia.org/wiki/Subject_Alternative_Name).

You can add multiple domains to a certificate by specifying a list of domains when creating a certificate, as well as any matching authorizations required.

**Key Point:** You must attach authorizations that cover **all** of the domains listed on the certificate. A certificate with unauthorized names cannot be issued.

Each authorization only covers the exact domain (for example, `video.example.com`) and the wildcard (`*.example.com`). It does not cover any explicit subdomains. If you want a certificate for `eu.video.example.com`, for example, you must set up another DNS authorization for the `eu.video.example.com` domain.

The following examples show how to attach an authorization for `video.example.com` and `eu.video.example.com`:

###  gcloud 

Use the `gcloud certificate-manager certificates` command:
    
    
    gcloud certificate-manager certificates create video-example-com \
        --domains="video.example.com,eu.video.example.com" \
        --dns-authorizations="video-example-com-auth,eu-video-example-com-auth" \
        --scope=EDGE_CACHE
    

This creates a certificate with the DNS authorization in the`AUTHORIZING` state and the certificate in the `PROVISIONING` state:
    
    
    managed:
    authorizationAttemptInfo:
    - domain: video.example.com
      state: AUTHORIZED
    dnsAuthorizations:
    - projects/123456/locations/global/dnsAuthorizations/video-example-com-auth
    - projects/123456/locations/global/dnsAuthorizations/eu-video-example-com-auth
    domains:
    - video.example.com
    state: PROVISIONING
    scope: EDGE_CACHE
    subjectAlternativeNames:
    - video.example.com

Domains can't share a DNS authorization. You must specify multiple domains and authorizations. Certificate Manager determines which domains require which authorizations.

To learn how certificates are issued and activated, see [Configure SSL (TLS) certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates).

### Certificate renewal

Managed certificates are automatically renewed by Certificate Manager. Renewed certificates are automatically pushed to Google's global edge for each active service you have configured.

  * `EDGE_CACHE` certificates have a short validity period (30 days) to improve security and compliance, compared to the current industry standard of 90 days (with a 60-day renewal interval).
  * Certificate renewal is typically initiated when the certificate is 10 days from expiring.
  * You do not need to take action when a certificate is renewed; the new certificate automatically replaces the existing certificate before the expiration date, with zero impact to your live traffic.



Because the issuance pipeline revalidates domain control before renewal, ensure that you do not delete the DNS records configured for DNS authorization. Deleting the record used to demonstrate DCV (Domain Control Validation) results in the inability to renew your certificates and prevents clients from connecting over HTTPS (TLS) when the certificate expires.

### CAA records and roots

To check compatibility with client devices, including older smart TVs, smartphones and streaming boxes, you can find the full set of root CAs that Google uses at [pki.goog](https://pki.goog/repository/).

To allow Certificate Manager and Media CDN to issue certificates for a domain with existing CAA records, add the `pki.goog` CAA record:
    
    
    DOMAIN_NAME. CAA 0 issue "pki.goog"
    

Domains that do not have existing CAA records do not need to add this record, but we recommend it as a best practice.

Read more about [CAA records](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa).

### Certificate limits

You can issue up to 1,000 managed certificates and 1,000 DNS authorizations per project. For other related limits and quotas, see the [Quotas and limits](https://docs.cloud.google.com/media-cdn/quotas) documentation .

### Supported TLS versions

Media CDN supports the following TLS versions:

TLS Version | Supported | Included Ciphers  
---|---|---  
SSL 3.0 | No |  N/A (not supported)   
TLS 1.0 | No |  N/A (not supported)   
TLS 1.1 | No |  N/A (not supported)   
TLS 1.2  | ✔ |  TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384   
TLS 1.3 | ✔ |  TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256   
  
Additionally:

  * Devices that don't support modern versions of TLS (such as TLS 1.3) automatically negotiate a supported TLS version.
  * TLS 1.2 is the minimum supported TLS version for Media CDN.
  * Media CDN does not support attaching SSL policies to a service.



### Troubleshoot certificate issuance

If you face any errors with certificate issuance, see how to [troubleshoot certificate issuance issues](https://docs.cloud.google.com/media-cdn/docs/troubleshooting-certificate-issuance).

## What's next

  * Read [Configure SSL certificates](https://docs.cloud.google.com/media-cdn/docs/configure-ssl-certificates).
  * Understand [client connectivity](https://docs.cloud.google.com/media-cdn/docs/client-connectivity) and protocol support.
  * Review how SSL (TLS) [connections are made](https://docs.cloud.google.com/media-cdn/docs/origins#supported_origins_and_protocols) to your origins.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
