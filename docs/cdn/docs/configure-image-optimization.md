---
url: https://docs.cloud.google.com/cdn/docs/configure-image-optimization/
title: Getting started \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:55.529216+00:00
---

# Getting started  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/configure-image-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Getting started Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you to get started with Cloud CDN image optimization, explaining how to configure image optimization and list of supported operations with examples.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Prerequisites

For Cloud CDN image optimization to work, ensure that the following prerequisites are met:

  * Cloud CDN cache policy must be enabled on the URL route or the associated backend service or bucket, and the image optimization feature must be active on that URL map route.

  * Image optimization is supported for Global External Application Load Balancers only. classic Application Load Balancer is not supported.

  * The client request must include an Accept header indicating it can receive image content, such as `image/webp`, `image/avif`, `image/*`, or `*/*`.

  * The origin server must respond with an `HTTP 200` status code and a supported image `Content-Type` header.

  * The `imop` query parameter must be included in the URL and contain one or more valid transformation operations.




## Configure image optimization

Image optimization requires an active caching enabled. Ensure that you configure at least one of the following:

  * Backend-based caching: make sure the backend has **Enable Cloud CDN** checked.

  * URL map-level caching: ensure that a cache policy is configured at the [URL map level](https://docs.cloud.google.com/cdn/docs/caching#cache-policies-url-maps) for the specific path where you plan to enable image optimization.




### gcloud

You must add configurations to your YAML file and import it to the URL map as image optimization policies are defined inside the routeAction object.

Export your existing URL map configuration to a local `YAML` file:
    
    
    gcloud beta compute url-maps export YOUR_URL_MAP_NAME \
        --global \
        --destination my-url-map.yaml
    

Edit the `my-url-map.yaml` file in a text editor and add the `imageOptimizationPolicy` field to the selected `routeAction` or `defaultRouteAction` sections.
    
    
    name: image-matcher
    routeRules:
      - description: ImageOptimizationService
        matchRules:
          - prefixMatch: /images/
        priority: 1
        routeAction:
          imageOptimizationPolicy:
            queryParameterInterpretation: ENABLED
    

Import the updated URL map
    
    
    gcloud beta compute url-maps import YOUR_URL_MAP_NAME \
        --global \
        --source my-url-map.yaml
    

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your global external Application Load Balancer.
  3. Click **Edit** edit.
  4. Navigate to the **Backend configuration** tab.
  5. **Configure caching:** Image optimization requires active caching to save successfully. Choose and configure one of the following, for image optimization to work. 
     * **Backend-based:** Ensure **Enable Cloud CDN** is selected in your **Backend Service** configurations.
     * **URL map level:**
       1. Navigate to **Routing rules** and select **Advanced host and path rule**.
       2. Define a cache policy at URL map level on the route where you are enabling image optimization.



Depending on your routing architecture, select one of the routing rules:

**To use the default routing rule, do the following:**

  1. In the **Host and path rules** section, under **Action** , select **Route traffic to a single backend mode** , and then select a backend from the list.
  2. Expand the **Image optimization section** (collapsed by default).
  3. Select the **Enable Image optimization** checkbox.



**To use the custom routing rule, do the following:**

  1. In the **Host and path rules** section, select **Add host and path rule**.
  2. In the **Hosts field** , enter * to match all hostnames.
  3. In the **Path matcher** section, use the YAML editor to define your configuration.
  4. Click **Code guidance** below the YAML editor for guidance on the code.
  5. Copy the snippet and paste it into the YAML editor.
  6. Update the placeholder values.



**Review configurations**

  1. Review your configurations.
  2. Click **Done** to close the sub-editor.
  3. Click **Update** to save your configurations.



## Supported image formats

Cloud CDN image optimization supports a wide range of input formats from your origin server. While most formats can be used for processing and output, some formats are Input only and cannot be used as target output formats.

The following image formats are supported from your origin server:

Format | Content-Type Header | Input/output | Usecase scenario  
---|---|---|---  
**gif** | `image/gif` | Input and output | Standard animated/still format. Animated frames can be extracted using the `Freeze` operation.  
**png** | `image/png` | Input and output | Lossless format, ideal for transparency, logos, and digital art.  
**webp** | `image/webp` | Input and output | Modern, web-optimized format with both lossy and lossless compression.  
**jpeg** | `image/jpeg` | Input and output | Standard photographic format.  
**brunsli** | `image/x-j` | Input and output | High-efficiency lossless JPEG repacking format.  
**tiff** | `image/tiff` | Input and output | High-quality tag-based raster format.  
**avif** | `image/avif` | Input and output | High-efficiency next-generation image format.  
**bmp** | `image/bmp` | **Input only** | Cannot be specified as an output format. Convert to WEBP or JPEG using `?imop=Convert,format=webp`.  
**ico** | `text/ico`, `image/ico`, `image/icon`, `application/ico`, `image/x-icon`, `image/vnd.microsoft.icon` | **Input only** | Icon container format. Cannot be exported; convert to a supported output format for delivery.  
**jp2k** | `image/jp2` | **Input only** | JPEG 2000 format. Must be explicitly converted using a `Convert` operation.  
**heif** | `image/heif` | **Input only** | High Efficiency Image Format. Must be converted before edge delivery.  
**Note:** If a requested output format is not natively supported, or if the source format is _Input Only_ , a `Convert` operation must be explicitly defined in your `imop` query parameter to specify a supported output format For example: `?imop=Convert,format=webp`.

## Image transformation URL

To perform dynamic image transformations, add the `imop` query parameter to your image URL. This parameter holds a transformation string, which consists of one or more operations applied in sequence.

The transformation string uses the following format rules:

  * Use a semicolon (`;`) to separate each individual operation.
  * Use a comma (`,`) to separate the internal parameters within each individual operation.
  * Only one operation of a given type can be included in a single query string.



The baseline syntax uses the following structure:
    
    
    ?imop=[OPERATION_1];[OPERATION_2];...[OPERATION_N]

To perform multiple actions on an image simultaneously, append a chained parameter string to the image URL. For example, to resize an image to _800 pixels_ wide, set the compression quality to 85, and convert the format to `WebP`, append the parameter string.

For example,
    
    
    https://www.example.com/image.jpg?imop=Resize,width=800;Compress,quality=85;Convert,format=webp;

## Policy structure

The image optimization policy acts as the core configuration wrapper containing every property relevant to the functionality of the image optimization feature.

**Name** | **Description** | **Configuration**  
---|---|---  
`queryParameterInterpretation` | Enum value that determines whether the query parameter for image optimization will be interpreted in the data plane. | **Required**. If set to **DISABLED** , query parameters for transformation will be ignored by the policy, effectively disabling this feature. If set to **ENABLED** , this feature will be enabled.  
  
### Policy dependencies and validation

The image optimization policy has a dependency on Cloud CDN caching. For this feature to work, a **Cache Policy** must be explicitly set on one of two locations:

  * The same URL map route where the Image optimization policy is being configured.

  * A backend service or backend bucket related to that exact route.




The image optimization policy is applied strictly in conjunction with the active, underlying Cache Policy.

**Note:** Configuration of an image optimization policy automatically returns a configuration validation error if a Cache Policy is not actively enabled on either the same route or on its associated backend service or bucket.

## Image optimization ordering rules

Operations listed in the `imop` query parameter are processed from left to right, with the exception of the following absolute system overrides:

  * **metadata** and **scale** operations are always executed first.
  * **canvas** operations are always executed last.



All input assets undergo automatic normalization before these transformations execute. EXIF orientation markers and ICC color profiles are applied directly to the image pixels before any metadata is stripped, ensuring coordinate integrity remains accurate for subsequent structural actions.

**Note:** only one operation of a given type is allowed per request.

## What's next

  * [Supported formats](https://docs.cloud.google.com/cdn/docs/image-opt-supportedops)
  * [Limitations](https://docs.cloud.google.com/cdn/docs/image-opt-limitations)
  * [Image optimization use cases](https://docs.cloud.google.com/cdn/docs/image-opt-use-cases)
  * [Securing image transformation requests](https://docs.cloud.google.com/cdn/docs/image-opt-security)
  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
