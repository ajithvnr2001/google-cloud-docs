---
url: https://docs.cloud.google.com/cdn/docs/image-opt-security/
title: Secure image transformation requests \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:42.197737+00:00
---

# Secure image transformation requests  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/image-opt-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Secure image transformation requests Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you to ensure more granular control over who can view your content and for how long. You can use Cloud CDN Signed URLs and Service Extensions for secure, time-limited access to your optimized images.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Standard, unsigned URLs let users manually change or remove query parameter strings in their browser. If your business logic relies on image transformations for privacy or access controls, unsigned queries introduce following risks:

  * **Metadata leakage** : An attacker could remove parameters such as `metadata,preserve=none` to retrieve hidden GPS coordinates or sensitive camera information contained in the source file.

  * **Bypassing visual redaction** : If you use parameters to hide faces, license plates, or confidential backgrounds with cropping, resizing, or blurring, a user could remove those parameters to view the unredacted image.




You can use signed URLs and Service Extensions to prevent unwanted transformation requests.

### Prevention with signed URLs

To mitigate these risks, configure Cloud CDN Signed URLs to protect your routes. When a URL is signed, the entire `imop` query parameter configuration string becomes part of the cryptographic signature that Cloud CDN validates on every request. If a user tries to change operations or parameters, for example `sizes`, Cloud CDN automatically validates the cryptographic signature and rejects the request, returning an `HTTP 403 Forbidden` status code.

For more information, refer to [Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls).

### Allowlisting with Service Extensions

Service Extensions lets developers inject custom programmable logic into the Cloud CDN data plane. This custom logic enables advanced request manipulation and security enforcement before the image optimization feature processes the request.

Service Extensions allows parsing the `imop` query string and matching its parameters against a fixed allowlist. For example, it can only permit predefined responsive widths, `200`, `400`, or `800`.

The following example demonstrates how an unauthorized request tries to bypass your edge cache and how Service Extensions handles such requests:

  1. A client requests an uncached, nonstandard image size:

`image.jpg?imop=Resize,width=401`

  2. Service Extensions intercepts the request at the Cloud CDN edge. It parses the query string to extract the `transformation parameter: width=401`.

  3. Service Extensions compares `401` against your predefined responsive design breakpoints:

  4. Allowed list: `200`, `400`, `800`

  5. Upon detecting that `401` is not in the allowlist, Service Extensions immediately terminates the request and returns an **HTTP 403 (Forbidden)** error or removes the parameters to serve the original image.




The request is not processed, which prevents edge compute exhaustion.

For more information, refer to [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview).

## What's next

  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
