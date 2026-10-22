---
url: https://docs.cloud.google.com/storage/docs/cross-origin/
title: Cross-origin resource sharing (CORS) \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:05.989953+00:00
---

# Cross-origin resource sharing (CORS)  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cross-origin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cross-origin resource sharing (CORS) Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/using-cors) [Configuration samples](https://docs.cloud.google.com/storage/docs/cors-configurations)

Cross-Origin Resource Sharing (CORS) enables client-side web applications to access resources from different origins. Cloud Storage supports the CORS specification, letting you configure your buckets to share resources securely with scripts from other origins. For example, you can use CORS to enable your web application `https://example-app.appspot.com` to access a resource at the origin `https://example-data.storage.googleapis.com`.

For more information about CORS configuration components, see [Set Bucket CORS](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#cors-body).

## How CORS works

Use CORS when you want your website to fetch files, images, or scripts directly from a Cloud Storage bucket using a browser-based request.

### Allowing access across domains

By default, web browsers enforce a security measure called [same-origin policy](https://www.w3.org/Security/wiki/Same_Origin_Policy). Same-origin policy prevents a script on one website from interacting with resources on a different domain. Although this protects users from malicious sites, it also blocks legitimate requests. For example, if your web application `https://example-app.appspot.com` attempts to access a resource at the origin `https://example-data.storage.googleapis.com`, the browser will block the request by default because the domains don't match.

The [CORS specification](https://fetch.spec.whatwg.org/#http-cors-protocol) provides a way for servers to tell the browser, "I trust this specific domain, so go ahead and allow the request."

Cloud Storage lets you set a CORS configuration on your bucket. When configured, Cloud Storage sends specific HTTP headers back to the browser (such as `Access-Control-Allow-Origin`) that authorize the browser to share the bucket's resources with your web application.

### Request types

CORS requests operate in two ways: simple and preflighted. A [simple request](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) proceeds directly, while a [preflighted request](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests) first sends a preliminary request to obtain permission.

#### Simple requests

The following process occurs when a browser makes a simple request to Cloud Storage:

  1. The browser adds the `Origin` header to the request. The `Origin` header contains the origin of the resource seeking to share the Cloud Storage bucket's resources, for example, `Origin:https://www.example-app.appspot.com`.

  2. Cloud Storage compares the HTTP method of the request and the value of the `Origin` header to the **Methods** and **Origins** information in the target bucket's CORS configuration to see if there are matches. If there are, Cloud Storage includes the `Access-Control-Allow-Origin` header in its response. The `Access-Control-Allow-Origin` header contains the value of the `Origin` header from the initial request.

  3. The browser receives the response and checks to see if the `Access-Control-Allow-Origin` value matches the domain specified in the original request. If they do match, the request succeeds. If they don't match, or if the `Access-Control-Allow-Origin` header is not present in the response, the request fails.




#### Preflighted requests

A request is preflighted if any of the following circumstances are true:

  * It uses methods other than `GET`, `HEAD` or `POST`.
  * It uses the `POST` method with a `Content-Type` other than `text/plain`, `application/x-www-form-urlencoded`, or `multipart/form-data`.
  * It sets custom headers. For example, `X-PINGOTHER`.



A preflighted request performs the following steps first. If it is successful, it then follows the same process as a simple request:

  1. The browser sends an `OPTIONS` request containing the `Requested Method` and `Requested Headers` of the primary request.

  2. Cloud Storage responds back with the values of the HTTP methods and headers allowed by the targeted resource. If any of the method or header values in the preflight request aren't in the set of methods and headers allowed by the targeted resource, the request fails, and the primary request isn't sent.




For a more complete description of CORS requests, read the [Fetch](https://fetch.spec.whatwg.org/#http-cors-protocol) spec.

## Cloud Storage CORS support

Cloud Storage lets you set CORS configurations at the bucket level. The JSON API and XML API endpoints handle CORS requests and return response headers differently. Understand these behaviors to configure your buckets effectively:

  * JSON API endpoints always allow CORS requests and return default values in the CORS response headers, regardless of the configuration set on the bucket.

  * XML API endpoints only allow CORS requests based on the configuration on the bucket and return specific CORS header values in response to that configuration.

  * The authenticated browser download endpoint `storage.cloud.google.com` does not allow CORS requests. Note that the Google Cloud console provides this endpoint for each object's public URL link.




You can use either of the following XML API request URLs to obtain a response from Cloud Storage that contains the CORS headers:
    
    
    storage.googleapis.com/BUCKET_NAME
    
    
    BUCKET_NAME.storage.googleapis.com

For information about XML API request URLs, see [Request Endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints).

## Components of a CORS configuration

When using the XML API, the values you set on your bucket's CORS configuration determine the CORS headers Cloud Storage returns in an HTTP response. When using the JSON API, Cloud Storage does not evaluate your bucket's configuration and instead returns default header values.

The following table describes the fields in a CORS configuration and the response behavior of the XML and JSON APIs. To learn how these fields are used, see [CORS configuration examples](https://docs.cloud.google.com/storage/docs/cors-configurations).

Field1 | Description | XML API response behavior | JSON API response behavior  
---|---|---|---  
`origin` | Specify origins that you want to allow for cross origin resource sharing with this Cloud Storage bucket. For example, `https://origin1.example.com`. | If the origin in a browser's request matches an origin in your CORS configuration, Cloud Storage returns `Access-Control-Allow-Origin` to the browser. If there is no match, Cloud Storage does not include `Access-Control-Allow-Origin` in the response. You can supply a wildcard value that grants access to all origins: `<Origin>*</Origin>`. | Cloud Storage returns the `Access-Control-Allow-Origin` header set to the origin of the request.  
`method` | Specify HTTP methods that you want to allow for cross origin resource sharing with this Cloud Storage bucket. The value is returned in the `Access-Control-Allow-Methods` header in response to successful preflight requests. Since `OPTIONS` is a standard method that browsers use to initiate preflight requests, you shouldn't specify `OPTIONS` in your CORS configuration. | Cloud Storage supports the following methods: `DELETE`, `GET`, `HEAD`, `POST`, `PUT`. Cloud Storage checks the methods sent from the browser in the `Access-Control-Request-Methods` header against the bucket's CORS configuration. If there is no match, Cloud Storage returns a `200` response code without CORS response headers. | Cloud Storage returns the `Access-Control-Allow-Methods` header set to the following methods: `DELETE`, `GET`, `HEAD`, `PATCH`, `POST`, `PUT`.   
`responseHeader` | Specify which headers you want to allow for cross origin resource sharing with this Cloud Storage bucket. The value is returned in the `Access-Control-Allow-Headers` header in response to successful preflight requests. | For preflight requests, Cloud Storage checks the headers sent from the browser in the `Access-Control-Request-Headers` header against the bucket's CORS configuration. If there is no match, Cloud Storage doesn't return CORS response headers. | Cloud Storage returns the `Access-Control-Allow-Headers` header set equal to the values specified by the `Access-Control-Request-Headers` header.  
`maxAgeSeconds` (optional) | Specify the number of seconds the browser is allowed to make requests before it must repeat the preflight request. This is also known as the cache expiry time. This value is returned in the `Access-Control-Max-Age` header in responses to preflight requests. For example, `3600` sets the cache expiry time to 1 hour. | Cloud Storage returns the `Access-Control-Max-Age` header with the specified cache expiry time. If you omit this field, Cloud Storage returns the default value of `3600`. | Cloud Storage returns the `Access-Control-Max-Age` header with the default value of `3600`.  
  
1 Names documented in the Field column are specific to the JSON API. When using the XML API to set a CORS configuration, use the [XML-specific format](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#cors-body).

### Specifying multiple origins, methods, or headers

To learn how to set multiple origins, methods, or headers in a CORS configuration, see the following list:

  * When using the JSON API, you can specify multiple origins, methods, or headers by using a comma-separated array. For example, `"method": ["GET", "PUT"]`.

**Caution:** When you set a CORS configuration using the JSON API, requests from all origins are accepted regardless of the `origin` field value in the CORS configuration.
  * When using the XML API, you can specify multiple origins, methods, or headers by using separate elements. For example:
        
        <Methods>
          <Method>PUT</Method>
          <Method>GET</Method>
        </Methods>

  * To allow requests to be made from any origin, set the origin to the wildcard `*`. For example, `"origin": ["*"]` in the JSON API or `<Origin>*</Origin>` in the XML API. While this origin is helpful for testing configurations, in most cases, you'll want to restrict request origins to prevent unwanted usage of your resources.




## Additional considerations

The following table describes considerations when making requests using credentials or access control headers:

Property or header | Description | XML API response behavior | JSON API response behavior  
---|---|---|---  
Credentials | Cookies, authorization headers, or TLS client certificates. | Cloud Storage never returns the `Access-Control-Allow-Credentials` header. CORS credentials are not supported by the XML API. | For simple requests, if the CORS request is approved, the `Access-Control-Allow-Credentials` header is set to true. For preflight requests, if `Access-Control-Request-Method` is empty, Cloud Storage sets `Access-Control-Allow-Credentials` to true and rejects the request with `404 - Not Found`.  
Exposed headers | For preflight requests, the `Access-Control-Request-Headers` request header indicates which headers a future CORS request might include. The `Access-Control-Expose-Headers` response header is included in the server's response and indicates to the client which headers can be exposed. | For simple requests, `Access-Control-Expose-Headers` lists the values of the response headers in your CORS configuration. | For simple requests, `Access-Control-Expose-Headers` returns the values specified in `Access-Control-Request-Headers` if they are part of a list of common HTTP headers.  
  
## Allowing buckets to access external resources

Sometimes, you might want to allow scripts hosted in Cloud Storage to access static resources that are hosted on a website external to Cloud Storage. In this scenario, the website serves CORS headers so that content on `storage.googleapis.com` is allowed access.

As a best practice, you should dedicate a specific bucket for this data access. This approach prevents your site from inadvertently over-exposing static resources to all of `storage.googleapis.com`. For example, if you want to dedicate a bucket named `mybucket` for data access, you should have the website serve the CORS header `Access-Control-Allow-Origin: https://mybucket.storage.googleapis.com` instead of `Access-Control-Allow-Origin: https://storage.googleapis.com`.

## Client-side CORS support

Most browsers use the `XMLHttpRequest` object to make a cross-domain request. `XMLHttpRequest` takes care of all the work of inserting the right headers and handling the CORS interaction with the server. You don't have to add any new code to take advantage of CORS support on Cloud Storage buckets.

## What's next

  * Learn how to [enable CORS for your bucket](https://docs.cloud.google.com/storage/docs/using-cors).
  * Explore [CORS configuration examples](https://docs.cloud.google.com/storage/docs/cors-configurations), including an example that removes the CORS configuration on a bucket.
  * Learn how to [troubleshoot CORS requests](https://docs.cloud.google.com/storage/docs/troubleshooting#access-bucket-with-cors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
