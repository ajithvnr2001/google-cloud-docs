---
url: https://docs.cloud.google.com/media-cdn/docs/configuration/
title: Configuration overview \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:01.901453+00:00
---

# Configuration overview  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configuration overview Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN offers content delivery, cache off-load, origin shielding, request authorization and integration with Google Cloud external Application Load Balancers, Logging, and Monitoring platforms.

Media CDN provides several REST API resources:

  * `EdgeCacheService`, responsible for client-facing configuration (TLS, IP addressing), routing, [CDN configuration](https://docs.cloud.google.com/media-cdn/docs/caching) (cache modes, TTLs, signing), and [security policies](https://docs.cloud.google.com/media-cdn/docs/security-policies).
  * `EdgeCacheOrigin`, responsible for per-origin configuration for any HTTP-based origin, as well as retry conditions when content is not available or reachable. For example, as part of a redundant video packager configuration.
  * (Optional) `EdgeCacheKeyset`, which contains a set of public keys used for [validating that client requests were signed](https://docs.cloud.google.com/media-cdn/docs/signed-requests) by your infrastructure / CMS. `EdgeCacheKeysets` are associated with an `EdgeCacheService`, and can be used across multiple services.



These resources are represented in the following example, which shows the `EdgeCacheService` terminating traffic, and routing to different `EdgeCacheOrigins`.

![An example configuration with an `EdgeCacheService` that terminates
   traffic, checks for signed requests with an optional `EdgeCacheKeyset`, and
   routes requests to three different `EdgeCacheOrigins`.](https://docs.cloud.google.com/static/media-cdn/images/keyset-route-rule.svg)An example configuration with an `EdgeCacheService` that terminates traffic, checks for signed requests with an optional `EdgeCacheKeyset`, and routes requests to three different `EdgeCacheOrigins`.

## Permissions

You must have the Identity and Access Management permissions required to create Media CDN resources. Media CDN has the following predefined IAM roles:

  * `roles/networkservices.edgeCacheAdmin`
  * `roles/networkservices.edgeCacheUser`
  * `roles/networkservices.edgeCacheViewer`

**Note:** These roles are visible only in projects where [Media CDN is enabled](https://docs.cloud.google.com/media-cdn/docs/overview#request-access).

## Enable the required services

To configure and deploy Media CDN services, you need to enable both the [Network Services API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) and the [Certificate Manager API](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest) for your project.

### Console

  1. Enable the Network Services API.

[Enable the API](https://console.cloud.google.com/apis/library/networkservices.googleapis.com)

  2. Enable the Certificate Manager API.

[Enable the API](https://console.cloud.google.com/apis/library/certificatemanager.googleapis.com)




### gcloud

  1. Enable the Network Services API:
         
         gcloud services enable networkservices.googleapis.com
         

  2. Enable the Certificate Manager API:
         
         gcloud services enable certificatemanager.googleapis.com
         




For more information about enabling and disabling services, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable).

## Example configuration

The following list of resources describes a representative Media CDN configuration:

  * **An`EdgeCacheOrigin`:**

    * A Cloud Storage-based origin that retries cache fetches against an alternative origin (AWS S3) if the object isn't in Cloud Storage (for example, HTTP 404) or a 5xx error is encountered.
  * **One`EdgeCacheKeyset`, which contains:**

    * Two Ed25519 public keys, which are used to validate signed requests.
    * In the example configuration, you can rotate keys each month, keeping two keys in production.
  * **One`EdgeCacheService` with two routes, including:**

    * A route for manifests, associated with the Cloud Storage origin, with short cache TTLs.
    * A route for video segments, protected by signed requests, and associated with the Cloud Storage origin, configured to cache all responses.
  * **IPv4, IPv6, logging enabled (default), and a managed SSL certificate configured**




The following example shows the `gcloud` output for this configuration:
    
    
    gcloud edge-cache origins describe prod-media-origin
    
    
    
    id: "2295067926314745283"
    creationTimestamp: "2019-11-13T09:53:48.757-08:00"
    name: "prod-media-origin"
    description: ""
    originAddress: "gs://bucket_name/"
    failoverOrigin: "s3-origin"
    retryConditions: [HTTP_5XX, NOT_FOUND]
    originProtocol: HTTP2
    timeouts:
      connectTimeout: 5s
      maxAttemptsTimeout: 10
      responseTimeout: 6s
    
    
    
    id: "2295067926314745283"
    creationTimestamp: "2019-11-13T09:53:48.757-08:00"
    name: "s3-origin"
    description: ""
    originAddress: "media.example.com.s3.amazonaws.com"
    retryConditions: [HTTP_5XX, NOT_FOUND]
    originProtocol: HTTP2
    
    
    
    gcloud edge-cache keysets describe prod-keyset
    
    
    
    id: "2295067926314745283"
    creationTimestamp: "2019-11-13T09:53:48.757-08:00"
    name: "prod-keyset"
    publicKeys:
      - name: "sept-2020-key"
        value: "DThVLjhAKm3VYOvLBAwFZ5XbjVyF98Ias8NZU0WEM9w="
      - name: "aug-2020-key"
        value: "3nQa82ScYgDDAxJrKCqumSEg60VNODGR5dGAveJWsw4="
    
    
    
    gcloud edge-cache services describe prod-media-service
    
    
    
    name: "prod-media-service"
    edgeSslCertificates:
      - "media-example-com-cert"
      - "video-serving-example-com-cert"
    requireTls: true
    routing:
      hostRules:
      - description: "prod hostnames"
        hosts:
          - "media.example.com"
          - "video-serving.example.net"
        pathMatcher: "routes"
      pathMatchers:
      - name: "routes"
        routeRules:
        - priority: 1
          description: "prod video segments"
          origin: "prod-media-origin"
          matchRules:
          - pathTemplateMatch: "/**.ts" # HLS segments
          - pathTemplateMatch: "/**.m4s" # DASH / CMAF segments
          routeAction:
            cdnPolicy:
              cacheMode: "FORCE_CACHE_ALL"
              clientTtl: 3600s
              defaultTtl: 86400s
              signedRequestMode: REQUIRE_SIGNATURES
              signedRequestKeySet: "prod-keyset"
          headerAction:
            responseHeadersToAdd:
            - headerName: cache-status
              headerValue: "{cdn_cache_status}"
            - headerName: proxy-status
              headerValue: "{proxy_status}"
        - priority: 2
          description: "prod manifest endpoints"
          origin: "prod-media-origin"
          matchRules:
          - pathTemplateMatch: "/**.m3u8" # HLS playlists
          - pathTemplateMatch: "/**.mpd" # DASH manifests
          routeAction:
            urlRewrite:
              pathPrefixRewrite: "/output/manifests"
            cdnPolicy:
              cacheMode: "CACHE_ALL_STATIC"
              clientTtl: 10s
              defaultTtl: 30s
              maxTtl: 120s
          headerAction:
            responseHeadersToAdd:
            - headerName: cache-status
              headerValue: "{cdn_cache_status}"
            - headerName: proxy-status
              headerValue: "{proxy_status}"
        - priority: 3 # catch all routes should be the lowest priority route
          description: "catch all route"
          origin: "prod-media-origin"
          matchRules:
          - prefixMatch: /
          headerAction:
            responseHeadersToAdd:
            - headerName: cache-status
              headerValue: "{cdn_cache_status}"
            - headerName: proxy-status
              headerValue: "{proxy_status}"
    

## Configuration options for Media CDN

To configure Media CDN, you can use the following tools:

  * Google Cloud console
  * Imported YAML or JSON files
  * The APIs directly



### Use the Google Cloud console

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

For instructions that describe how to configure Media CDN in the Google Cloud console, see the [quickstart](https://docs.cloud.google.com/media-cdn/docs/quickstart).

### Import and export configurations

The gcloud CLI lets you export and import configurations from YAML or JSON files, enabling integration with continuous delivery systems or by using [infrastructure-as-code](https://docs.cloud.google.com/solutions/managing-infrastructure-as-code) tooling. You can duplicate configurations, test an isolated service in a staging environment before updating your production environment, and snapshot configurations into version control.

Output only fields are not imported, and are implicitly excluded when importing a configuration. Specifically:

  * IP addresses are not imported, as they are dedicated to each service. Services cannot share IP addresses.
  * The `selfLink` of the resource, which is based on the resource name.
  * The `id` of the resource, which is automatically generated.



To export a service, `EdgeCacheOrigin` or `EdgeCacheKeyset`, use the `export` sub-command for each resource. For example, to export a service configuration:
    
    
    gcloud edge-cache services export SERVICE_NAME \
        --destination=my-service.yaml
    
    
    
    Exported [projects/my-project/locations/global/edgeCacheServices/SERVICE_NAME] to 'my-service.yaml'.
    

Similarly, you can import an existing service configuration, either as a new service or as an update-in-place for an existing service:
    
    
    gcloud edge-cache services import new-staging-service \
        --source=my-service.yaml
    

## Use asynchronous API operations

By default, `gcloud` commands that create, update or delete a resource are blocking, and only return once the task is complete (for both success and failure). The REST API is asynchronous by default.

In some cases, you might want to make these requests asynchronously. You can provide the `--async` flag, which causes the command to return immediately with an operation ID. You can use this ID to check and poll to confirm whether the task succeeded, whether it returned an error, and what the error message was.

You inspect an individual operation (by its ID) to understand the error in detail. For example, if you configure a `logConfig.sampleRate` without also setting `logConfig.enable = true`, you can expect the following error to be returned:
    
    
    gcloud edge-cache operations describe operation-1611525680496-5b9ac8fbb7f58-90a7a822-f0c1e8c6
    
    
    
    done: true
    error:
      message: "Logs sample rate must not be specified without enabling logging."
    name: projects/my-project/locations/global/operations/operation-1611525680496-5b9ac8fbb7f58-90a7a822-f0c1e8c6
    

To view all recent operations, their status, and completion, you can run the following command:
    
    
    gcloud edge-cache operations list
    
    
    
    END_TIME  ID                                                       TARGET  DONE
              operation-1611095421009-5b9486244bf21-cc6b5924-628b8e2a          True
              operation-1611096056610-5b94888273fe6-2da85286-8c810f8e          True
              operation-1611095551517-5b9486a0c251e-c2e1bbbb-de4aa8a5          True
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
