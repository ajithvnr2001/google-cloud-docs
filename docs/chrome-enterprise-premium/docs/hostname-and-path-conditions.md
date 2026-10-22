---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/hostname-and-path-conditions/
title: Using hostname and path conditions \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:11.520173+00:00
---

# Using hostname and path conditions  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/hostname-and-path-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  Using hostname and path conditions Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Limiting access based on URL hostname and path can only be done with the gcloud CLI.

This page describes hostname and path [Identity and Access Management (IAM) conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

You can secure Identity-Aware Proxy (IAP) resources using the hostname and path of a request URL. For example, the `request.path.startsWith` IAM condition can be used to only grant access to employees in the **Privileged Access** group if the URL path starts with `/admin`.

For more information about using hostname and path conditions, see [request attributes](https://docs.cloud.google.com/iam/docs/conditions-overview#request_attributes).

### String normalization

A URL has a hostname and path. For example, the URL `https://sheets.google.com/create?query=param` has a hostname of `sheets.google.com` and a path of `/create`.

Backends can interpret hostnames and paths in different ways. To remove ambiguity, IAP normalizes hostname and path strings when checking policies.

IAP performs two policy checks when a request has a non-normalized path. If the non-normalized path passes the policy check, IAP normalizes the path and a second policy check is performed. Access is granted if both the non-normalized and normalized paths pass the policy check.

For example, if a request has the path `/internal;some_param/admin`, IAP first performs a policy check on the non-normalized path (`/internal`). If that check passes, IAP performs a second policy check on the normalized path (`/internal/admin`).

#### Hostnames

Hostname normalization involves the following:

  * Removing trailing dots
  * Lowercasing characters
  * Converting to ASCII



Hostnames that include non-ASCII characters are further normalized using Punycode. You need to use Punycode to normalize your hostname string for a match to be made.

To normalize your hostname string with Punycode, use a converter like [Punycoder](https://www.punycoder.com/).

The following are examples of normalized hostnames:

  * `FOO.com` is normalized to `foo.com`
  * `café.fr` is normalized to `xn--caf-dma.fr`



#### Paths

Path normalization involves the following:

  * Removing path params
  * Resolving relative paths to their absolute equivalent



A path param includes all characters from a `;` to either the next `/` or the end of the path.

Requests that contain path sections starting with `..;` are considered invalid. For example, `/..;bar/` and `/bar/..;/` return the `HTTP 400: Bad Request` error.

The following are examples of normalized paths:

  * `/internal;some_param/admin` is normalized to `/internal/admin`
  * `/a/../b` is normalized to `/b`
  * `/bar;param1/baz;baz;param2` is normalized to `/bar/baz`



### Subdomain endings

A policy set with `request.host.endsWith("google.com")` matches to both `sub_domain.google.com` and `testgoogle.com`. If your goal is to limit your policy to only subdomains that end with `google.com`, set your policy to `request.host.endsWith(".google.com")`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
