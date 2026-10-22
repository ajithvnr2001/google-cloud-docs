---
url: https://docs.cloud.google.com/certificate-manager/docs/domain-authorization/
title: Domain authorization types for Google-managed certificates \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:53.542423+00:00
---

# Domain authorization types for Google-managed certificates  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/domain-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Domain authorization types for Google-managed certificates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how domain authorization works with Google-managed certificates. The page compares load balancer authorization to DNS authorization and explains how Certificate Manager verifies domain ownership using each method.

Certificate Manager lets you prove ownership of domains for which you want to issue Google-managed certificates in one of the following ways:

  * **Load balancer authorization** : deploy the certificate directly to a supported load balancer without creating a DNS record. This method is faster to configure, but it doesn't support wildcard certificates or regional certificates. Additionally, Certificate Manager can only provision certificates after the load balancer has been fully set up and is serving network traffic.

  * **DNS authorization** : deploy the certificate directly to a supported load balancer after creating dedicated DNS records for verification of domain ownership. Using this method, Certificate Manager can provision certificates in advance, before the target proxy is ready to serve network traffic.




Domain authorization doesn't apply to Google-managed certificates issued by Certificate Authority Service. For more information about such certificates, see [Deploy a global Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas).

## Load balancer authorization

Load balancer authorization is the simplest method for issuing a Google-managed certificate. This method minimizes changes to your DNS configuration, but only provisions the TLS (SSL) certificate after the load balancer configuration is complete. This method also makes load balancer authorization ideal for new environments with no existing production traffic.

To create Google-managed certificates with load balancer authorization, your deployment must meet the following requirements:

  * The Google-managed certificate must be accessible on port 443 from all IP addresses serving the target domain; otherwise, provisioning fails. For example, if you have separate load balancers for IPv4 and IPv6, you must assign the same Google-managed certificate to each of them.
  * You must explicitly specify the IP addresses of your load balancers in your DNS configuration, which prevents [multi-perspective domain validation failures](https://docs.cloud.google.com/certificate-manager/docs/troubleshooting#multi-perspective-domain-validation). Intermediate layers, such as CDN, can cause unpredictable behavior.
  * The target domain must be openly resolvable from the Internet. Split-horizon or DNS firewall environments can interfere with certificate provisioning.



## DNS authorization

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

## Compare load balancer authorization with DNS authorization

Certificate Manager lets you prove ownership of domains for which you want to issue Google-managed certificates as described in the following table.

| Load balancer authorization | DNS authorization  
---|---|---  
**Setup complexity** | Load balancer authorization doesn't require additional configuration steps or changes to your DNS configuration. | Requires you to create a DNS authorization and add its corresponding CNAME record to your DNS configuration.  
**Network security** | The load balancer must be fully accessible from the internet on port 443, including the DNS configuration for all domains served by the certificate. Load balancer authorization doesn't work with other configurations. | Works with highly complex configurations, such as ports other than 443 and CDN layers in front of the target proxy.  
**Provisioning speed** | You can provision certificates only after the load balancer is fully set up and serving network traffic. | You can provision certificates in advance, before the target proxy is ready to serve network traffic.  
**Wildcard certificates** | Not supported | Supported  
  
## What's next

  * [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations)
  * [Deploy a global Google-managed certificate with load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth)
  * [Deploy a global Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
