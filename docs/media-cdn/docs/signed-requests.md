---
url: https://docs.cloud.google.com/media-cdn/docs/signed-requests/
title: Use signed requests \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:06.736064+00:00
---

# Use signed requests  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/signed-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Use signed requests Stay organized with collections  Save and categorize content based on your preferences. 

To create a signed request, compose a string that includes parameters that describe the content that you want to protect and the expiration time of the signed value. You then include the composed string in your request. Media CDN then verifies that your signed request is valid before acting upon it.

### Signed request requirements

Signed requests must meet the following requirements:

  * Have a `GET`, `HEAD`, or `OPTIONS` HTTP method. Other methods are not supported.

  * Have an expiration time set in the future. Due to potential clock synchronization differences, as well as client network conditions (for example, disconnects and retries), we recommend setting timestamps no less than one minute into the future, or no less than the length of the video stream, whichever is greater.

  * Have a signature that can be verified by a key or secret in an `EdgeCacheKeyset`.




You cannot sign other HTTP methods, such as `POST`, `PUT`, or `DELETE` requests. If you need to issue signed URLs for user-facing uploads, see the [Cloud Storage documentation for signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## Configure signed requests

The following sections detail how to configure, sign, and validate signed requests.

### Generate keys

[Create the keys](https://docs.cloud.google.com/media-cdn/docs/create-keys) that Media CDN uses to sign requests.

### Create a keyset

[Create the keyset](https://docs.cloud.google.com/media-cdn/docs/create-keyset) that Media CDN uses for signed requests.

### Require signed requests

To allow only signed requests to access a resource, you can attach a list of keys to a route and set the `signedRequestMode` to one of the following:

  * `REQUIRE_SIGNATURES` for signed requests not using tokens.

  * `REQUIRE_TOKENS` for signed requests using tokens.




Enabling signed requests on a route enforces that all requests are signed or present a token. Requests without a valid signature (such as an invalid key name, expired signature or token, mismatched signature, and so on), fail.

An `EdgeCacheKeyset` can contain multiple keys to allow for key rotation. Valid requests signed with any listed key are accepted, and keys are tried in order. For more information about key rotation, see [Rotate secrets](https://docs.cloud.google.com/media-cdn/docs/rotate-secrets).

When the `signedRequestMode` is set to `REQUIRE_SIGNATURES` or `REQUIRE_TOKENS`, Media CDN validates both cache hits and misses. This includes all requests to the origin.

Following is an example of a Media CDN configuration that enforces signed requests on a given PathMatcher (route):
    
    
    gcloud edge-cache services describe prod-media-service
    

Output: 
    
    
    ...
      routeAction:
        cdnPolicy:
          cacheMode: CACHE_ALL_STATIC
          signedRequestMode: REQUIRE_SIGNATURES
          signedRequestKeyset: prod-vod-keyset

For information on creating tokens for signed requests, see [Generate tokens](https://docs.cloud.google.com/media-cdn/docs/generate-tokens).

To disable request signing, you can set the `signedRequestMode` to `DISABLED` and delete the reference to the `signedRequestKeyset`.

### Validate requests at the origin

When a route is configured with a signing mode of `REQUIRE_SIGNATURES`, Media CDN validates that every matching request has a valid signature. The lack of a signature is treated as an invalid signature for these routes.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

To prevent cases where signing is misconfigured, and where a user attempts to access your origin directly, we recommend that you validate that requests are signed at the origin as well. A _defense in depth_ approach to content protection helps prevent unauthorized access and download of your licensed and paid content.

For URL-based signing methods, where the signature is part of the query parameters or embedded as a URL path component, the signature and related parameters are removed from the URL before the request is sent to the origin. This prevents the signature from causing routing issues when the origin is handling the request. To validate these requests, you can inspect the `x-client-request-url` request header, which includes the original (signed) client request URL prior to the removal of the signed components.

**Note:** If you are using Cloud Storage and have removed the `allUsers` (public access) permission, Cloud Storage rejects unauthenticated, public access to content on your behalf.

To validate requests at the origin, use the same validation code as part of your request signing endpoints, which also helps mitigate key mismatch and issues due to key rotation.

### Rotate keys

As a best practice, [rotate or update the secrets](https://docs.cloud.google.com/media-cdn/docs/rotate-secrets) used by Media CDN regularly. We recommend rotating keys every 30 to 60 days, but it isn't strictly required.

## What's next

  * To read more about how to enable and access Media CDN logs, including how to filter and query across your logs, see [Logging](https://docs.cloud.google.com/media-cdn/docs/logging).

  * To configure Media CDN and a private Cloud Storage bucket, see [Origin connectivity and shielding](https://docs.cloud.google.com/media-cdn/docs/origins).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
