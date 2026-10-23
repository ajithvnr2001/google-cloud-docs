---
url: https://docs.cloud.google.com/run/docs/triggering/https-request/
title: Invoke with an HTTPS Request \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:36.895200+00:00
---

# Invoke with an HTTPS Request  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/https-request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Invoke with an HTTPS Request Stay organized with collections  Save and categorize content based on your preferences. 

After you create a service or function, Cloud Run provides you with an HTTPS endpoint for the service. You can enable the service to run in response to HTTPS requests.

All Cloud Run services have a stable HTTPS URL, which represents the default HTTPS endpoint for the service, though you can [configure custom domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains) as well.

Some of the use cases include the following:

  * Custom RESTful web API
  * Private microservice
  * HTTP middleware or reverse proxy for your web applications
  * Pre-packaged web application



## Create public services

Creating a public service on Cloud Run requires the following:

  * Access to the service from the public internet
  * A URL intended for public use



To make a service public, [set your service to allow unauthenticated (public) access](https://docs.cloud.google.com/run/docs/authenticating/public).

## Service URL

Cloud Run assigns a hash-based non-deterministic URL to all services. If the service name length allows it, Cloud Run also assigns a deterministic URL to the service.

You can [disable these default `run.app` URLs](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url).

You can retrieve your service's URL by clicking the service name in the Google Cloud console or by running the following command in the gcloud CLI:
    
    
    gcloud run services describe SERVICE --format 'value(status.url)'
    

The deterministic URL is given priority when displayed.

If the Cloud Run service was created as a function with the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis), the service is also assigned a [`cloudfunctions.net`](https://docs.cloud.google.com/run/docs/functions/comparison#concepts) URL.

### Deterministic URL

The deterministic URL lets you predict the service URL before the service is created, which can be useful for service-to-service communication.

The deterministic URL is only available for DNS segments of 63 characters or less. The DNS segment contains the service name, the project number, and any traffic tag or tags.

The deterministic URL for a Cloud Run service has the following format:
    
    
    https://[TAG---]SERVICE_NAME-PROJECT_NUMBER.REGION.run.app

where:

  * TAG is the optional [traffic tag](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags) for the revision that you are requesting.
  * PROJECT_NUMBER is the Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * SERVICE_NAME is the name of the Cloud Run service.
  * REGION is the name of the region, such as `europe-west1`.



### Non-deterministic URL

Non-deterministic URLs do _not_ have a deterministic format, meaning that because the URL's second field is a random hash, you cannot predict what the full URL will be before you deploy the services. After you deploy the service, however, the URL remains stable.

The non-deterministic URL for a Cloud Run service has the format `https://[TAG---]SERVICE_IDENTIFIER.run.app`, where TAG refers to the optional [traffic tag](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags) for the revision that you are requesting, and SERVICE_IDENTIFIER is a stable and unique identifier for a Cloud Run service. Don't parse the SERVICE_IDENTIFIER as it does not have a fixed format, and the logic for SERVICE_IDENTIFIER generation is subject to change.

## Response streaming

Cloud Run supports streaming HTTP responses. No configuration is required to enable the feature. The server has to respond with a `Transfer-Encoding: chunked` response header.

## HTTP to HTTPS redirect

Cloud Run redirects all HTTP requests to HTTPS but terminates TLS before they reach your web service. If your service generates a web resources that refers to other web resources with unsecured URLs (`http://`), your page might be subject to [mixed content warnings or errors](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/what-is-mixed-content). Use the `https` protocol for all reference web URIs or account for proxy directives in the HTTP Request such as the `X-Forwarded-Proto` HTTP header.

## HTTP and HTTP/2

By default, Cloud Run downgrades HTTP/2 requests to HTTP/1 when those requests are sent to the container. If you want to explicitly set your service to use HTTP/2 end-to-end, refer to [Using HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2).

## Create private services

Creating a private service on Cloud Run requires you to limit access to the service by leveraging the [IAM invoker permission](https://docs.cloud.google.com/run/docs/reference/iam/permissions).

You can also limit access to a service using application-level authorization and authentication mechanism, for example, using [Identity Platform](https://docs.cloud.google.com/identity-platform).

### Test private services

The easiest way for you to test private services is to use the [Cloud Run proxy in Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/proxy). This proxies the private service to `http://localhost:8080` (or to the port specified with `--port`), providing the token of the active account or another token you specify. This lets you use a web browser or a tool like `curl`. This is the recommended way to test privately a website or API in your browser.

You can proxy a service locally using the following command line in a Linux, macOS, [WSL (preferred)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), or [cygwin](https://cygwin.com/install.html) environment:
    
    
    gcloud run services proxy SERVICE --project PROJECT-ID

You can also test private services without the proxy by using a tool like `curl`, passing an auth token in the `Authorization` header:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL

**Note:** To use the `curl` command on Microsoft Windows, you might need the [WSL (preferred)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or [cygwin](https://cygwin.com/install.html) command line.

### Private service to service

A Cloud Run service can call another Cloud Run service with [service-to-service authentication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

### Sample code that invokes a private service

For code samples that shows how to obtain an ID token and make an HTTP request to a private service, refer to the topic [Authenticating service-to-service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## Using a middleware to enhance your service

HTTPS proxies can offload common functionality from an HTTP service, such as caching, request validation, or authorization. For microservices, many HTTP proxies are part of an [API Gateway](https://wikipedia.org/wiki/API_management) solution or a service mesh such as [Istio](https://istio.io/).

Google Cloud products that you can use to enhance your Cloud Run service include:

  * [API Gateway](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-console), which you can use to create, secure, and monitor APIs to use as proxies to other Cloud Run services.

  * [Firebase Hosting](https://firebase.google.com/docs/hosting), which you can use to build a web application frontend to use with [Cloud Run as a dynamic backend](https://firebase.google.com/docs/hosting/cloud-run).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
