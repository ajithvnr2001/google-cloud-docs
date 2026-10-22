---
url: https://docs.cloud.google.com/cdn/docs/web-security-best-practices/
title: Web security best practices \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:51.345156+00:00
---

# Web security best practices  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/web-security-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Web security best practices Stay organized with collections  Save and categorize content based on your preferences. 

## Best practices for web security

Cloud CDN and Cloud Load Balancing can help you meet web security best practices, whether you're serving content from Compute Engine instances, a Cloud Storage bucket, or an external origin located outside of Google Cloud.

### Set security headers

The HTTP specification has a number of headers that control the following:

  * Client behavior
  * How content is embedded
  * How content is served across domains
  * Whether to always use TLS (HTTPS) when connecting to that domain



These controls are typically represented as HTTP response headers, which you can set for each backend (_origin_ , in CDN terms) as [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) for your external Application Load Balancer and Cloud CDN deployment.

If you are using Cloud Storage and serving web content from your bucket, you can use Cloud CDN [in front of your storage bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket) to set web security headers and cache popular content.

The most useful web security headers are defined in the following table.

Header name | Description | Example usage  
---|---|---  
`Strict-Transport-Security` (HSTS) |  Ensures that your domains have valid SSL (TLS) certificates before you set this header. Informs clients that they must connect to your domain directly over HTTPS (SSL/TLS), avoiding the need to redirect from HTTP to HTTPS, which is slower and introduces the risk of a person-in-the-middle attack. Setting this header is effectively irreversible. After caching this header, modern browser clients don't attempt non-HTTPS connections, and users can't access any domain that they received this header for, even if SSL is down. This behavior prevents an attacker from downgrading the secure protocol to the unprotected HTTP (known as a _downgrade attack_). When serving the `Strict-Transport-Security` header, use caution when adding the `includeSubdomains` or `preload` directives. These directives require any subdomain to use HTTPS, including any internal sites on the same domain. For example, `support.example.com` when served from `example.com`.  |  Require clients to connect directly over HTTPS for all future connections, caching this directive for up to two years:  `Strict-Transport-Security: max-age=3104000`  
`X-Frame-Options` | Indicate whether a browser can render a page in a <frame>, <iframe>, <embed>, or <object>. This helps to prevent _click-jacking_ attacks, by not letting your content be embedded into other sites. |  Deny all iframing of your site: `X-Frame-Options: DENY` Allow only your site to iframe (embed) itself: `X-Frame-Options: SAMEORIGIN`  
`Content-Security-Policy` |  To evaluate your site's Content Security Policy, you can use Google's [CSP Evaluator](https://csp-evaluator.withgoogle.com/) tool.  | Don't allow in-line scripts, and only load scripts over HTTPS: `Content-Security-Policy: default-src https:`  
  
Use caution when introducing new security headers to existing websites, because they can break third-party scripts, embedded content (for example, in iframes), or other aspects of your sites. Before making changes to your production traffic, we recommend creating a second instance of your backend bucket or backend service and testing.

You can read more about web security headers and best practices on [web.dev](https://web.dev/secure/) as well on Mozilla's [infosec site](https://infosec.mozilla.org/guidelines/web_security).

### TLS and certificate management

[Managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) have the following characteristics:

  * Are provided at no cost
  * Can be easily deployed to your load balancers
  * Automatically renew
  * Are globally distributed to all of Google's edge locations



TLS provides authenticity by validating that data has not been modified in transit. TLS certificates provide confidentiality by making sure that an eavesdropper cannot determine what is being exchanged between users and servers. This is important for user privacy and security.

With SSL certificates, you can benefit from modern transport protocols, such as [HTTP/2](https://developers.google.com/web/fundamentals/performance/http2) and Google's [QUIC protocol](https://cloud.google.com/blog/products/gcp/introducing-quic-support-https-load-balancing), both of which require SSL (TLS). These protocols directly improve the performance of web content, media delivery (such as streaming video), and reliability over congested networks.

Google Cloud supports modern TLS protocols (such as TLS 1.3) across Cloud Load Balancing and Cloud CDN services.

You can use [SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies) to raise the minimum version of TLS. We recommend raising the version to TLS v1.2, if you don't need to support older clients, such as embedded devices or older (more than 10 years old) non-browser clients. Globally, TLS v1.0 and TLS v1.1 represent less than 0.5% of connections across Google Cloud. If you need to identify or associate specific clients with outdated versions of TLS, you can use the `{tls_version}` [variable in a request header](https://docs.cloud.google.com/load-balancing/docs/user-defined-request-headers#variables). You can then log this information.

## What's next

  * To check whether Cloud CDN is serving responses from cache, see [Viewing logs](https://docs.cloud.google.com/cdn/docs/logging).
  * To learn about which content is cacheable or non-cacheable, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).
  * To see Cloud CDN's points of presence, see [Cache locations](https://docs.cloud.google.com/cdn/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
