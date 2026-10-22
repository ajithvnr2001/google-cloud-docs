---
url: https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls/
title: Secure your app with minimum TLS (standard environment) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:25.885586+00:00
---

# Secure your app with minimum TLS (standard environment)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/secure-minimum-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Secure your app with minimum TLS (standard environment) Stay organized with collections  Save and categorize content based on your preferences. 

To increase security, App Engine automatically opts your application into TLS version 1.2 and later, with supported cipher suites, and might permanently block insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked.

If your project is permanently blocked from using TLS version 1.1 and earlier, and you require additional time to switch to TLS 1.2 and later, contact Support.

For new applications, App Engine only allows secure traffic with TLS version 1.2 and later, with supported cipher suites, by default. If your application only requires TLS version 1.2 and later with the default supported cipher suites, you don't need to [configure](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless) a global external Application Load Balancer to route requests. However, if you need to support a different set of cipher suites, or require connection-level (handshake) rejection of insecure TLS versions for custom domains, configure a global external Application Load Balancer.

**Note:** If you update your application settings to enforce TLS version 1.2 and later, App Engine automatically rejects incoming requests that attempt to use older, less secure TLS versions 1.1 and earlier. For `appspot.com` domains, App Engine prevents the TLS handshake itself. For custom domains, this rejection causes a `400 Bad Request - The request was malformed` error after a successful TLS handshake, meaning the connection is established, but the request itself is denied. For custom domains, use the Google Cloud CLI to update the TLS versions allowed for your app. External SSL-checking sites might only verify a successful TLS handshake, and incorrectly imply that TLS version 1.1 and earlier are still supported.

## Supported TLS versions and cipher suites

The security of TLS connections depends on the negotiated cipher suite, a combination of cryptographic algorithms. These [cipher suites](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#predefined_profiles) are identified by IANA values, as detailed in the following table:

TLS version | IANA value | Cipher suite | TLS v1.3 | 0x1301 | TLS_AES_128_GCM_SHA256  
---|---|---  
0x1302 | TLS_AES_256_GCM_SHA384  
0x1303 | TLS_CHACHA20_POLY1305_SHA256  
TLS v1.2 | 0xCCA9 | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  
0xCCA8 | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256  
0xC02B | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  
0xC02F | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  
0xC02C | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  
0xC030 | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  
0xC009 | TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA  
0xC013  | TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA  
0xC00A | TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA  
0xC014 | TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA  
  
If you need to use a different or a less restrictive cipher suite, we recommend that you use a global external Application Load Balancer. For more information, see [Set up a classic Application Load Balancer with App Engine](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless) and [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#defining_an_ssl_policy) in the Cloud Load Balancing documentation.

## Update the TLS versions allowed for your app

App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For projects where older TLS versions have been permanently blocked, you can't use the following settings to update to an older TLS version. If your project requires older TLS versions, contact Support.

When you create or update your application, use the `--ssl-policy` flag to specify the minimum permitted TLS version.

To set a minimum TLS version while creating your app:
    
    
    gcloud app create --ssl-policy=TLS_VERSION
    

To set a minimum TLS version while updating your app:
    
    
    gcloud app update --ssl-policy=TLS_VERSION
    

Replace TLS_VERSION with `TLS_VERSION_1_2`. This only allows TLS version 1.2 and later, with modern cipher suites.

## Disable custom TLS versions and ciphers

If you use [Cloud Load Balancing and serverless NEGS](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to route traffic to your App Engine application, you can further restrict TLS versions or ciphers by defining an [SSL security policy](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) on your load balancer.

## What's next

  * To verify and manage SSL certificates, see [Secure custom domains with SSL](https://docs.cloud.google.com/appengine/docs/standard/securing-custom-domains-with-ssl).

  * To enable Cloud Load Balancing to manage incoming requests to your custom domain, see [Migrate App Engine custom domain to Cloud Load Balancing](https://docs.cloud.google.com/appengine/docs/standard/custom-domain-to-cloud-load-balancing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
