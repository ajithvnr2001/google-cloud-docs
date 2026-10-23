---
url: https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication/
title: Configure private origin authentication \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:06.857132+00:00
---

# Configure private origin authentication  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Configure private origin authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of private origin authentication and instructions for using it with Cloud CDN.

Private origin authentication gives Cloud CDN long-term resource access to private Amazon S3 buckets or other compatible object stores. Using private origins prevents clients from bypassing Cloud CDN and accessing your origin directly.

This feature is supported for Cloud CDN with either a global external Application Load Balancer or a classic Application Load Balancer.

Private origin authentication is origin-facing, while [signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) and [signed cookies](https://docs.cloud.google.com/cdn/docs/using-signed-cookies) are client-facing. You can enable both for the same content. Private origin authentication limits non-CDN access to your origins and content. Signed URLs and cookies control which users can access Cloud CDN.

**Note:** This feature supports only the `GET`, `HEAD`, `OPTIONS`, and `TRACE` HTTP methods.

## Before you begin

  * Create a hash-based message authentication code (HMAC) key to authenticate requests and associate it with a service account. Make a note of the access key and secret.

See [Accessing AWS using your AWS credentials: Programmatic Access](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) in AWS documentation.

  * [Configure a load balancer with the external backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg#config-lb-external-backend).

If your object store expects a particular value for the HTTP request's `Host` header, make sure that it is configured in the backend service. If you don't configure a custom request header, the backend service preserves the `Host` header that the client used to connect to the external Application Load Balancer.

For configuration steps, see [Working with custom request headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#working-with-request). For a specific example, see [Configuring a load balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg#config-lb-external-backend).

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        




## Configure authentication for private origins

To configure private origin authentication, use the following instructions:

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to configure. The origin must be of the **Custom origin** type.

  3. On the **Origin details** page, click the **Edit** button.

  4. To navigate to the **Host and path rules** section, click **Next**.

  5. To navigate to the **Cache performance** section, click **Next**.

  6. In the **Private origin authentication** section, select **Authenticate requests to this origin with AWS Signature Version 4**. Then, specify the following information:

     * **Key ID** : access key for your Amazon S3 bucket or other compatible object store.
     * **Key** : the secret key used to authenticate to the object store. If you're using a private Cloud Storage bucket, specify the HMAC key.
     * **Key version** : a unique name to represent the key version.
     * **Region** : the region that your object store is located in—for example, `us-east-1`.
  7. Click **Done**.




### gcloud

  1. Export the backend configuration for your private origin into a YAML file by using the `gcloud compute backend-services export` command:
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
            [--destination=DESTINATION]
         

Replace `DESTINATION` with the name of the YAML file—for example, `my-private-origin.yaml`.

  2. To authenticate your backend requests by using the HMAC key, specify these additional configuration options in the `securitySettings` section of `backendServices`:
         
         securitySettings:
           awsV4Authentication:
             accessKeyId: ACCESS_KEY_ID
             accessKey: ACCESS_KEY
             [accessKeyVersion: ACCESS_KEY_VERSION]
             originRegion: REGION
         …]
         

Replace the following:

     * `ACCESS_KEY_ID`: the HMAC access key ID
     * `ACCESS_KEY`: the HMAC access key
     * `ACCESS_KEY_VERSION` (optional): a unique name that you can set to represent the key version
     * `REGION`: a valid region for your storage provider. For Amazon S3, the value is not a Google Cloud region.

The following snippet shows the contents of a sample `my-private-origin.yaml` file:
    
    name: shopping-cart-services
     backends:
       - description: cart-backend-1
         group: 'https://www.googleapis.com/compute/v1/projects/my-project-id/global/networkEndpointGroups/my-network-origin-group'
     securitySettings:
       awsV4Authentication:
         accessKeyId: AKIDEXAMPLE
         accessKey: c4afb1cc5771d871763a393e44b703571b55cc28424d1a5e86da6ed3c154a4b9
         accessKeyVersion: prod-access-key-v1.2
         originRegion: us-east-2
    

  3. To update your private origin, import the configuration to your backend service by using the `gcloud compute backend-services import` command:
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
            [--source=SOURCE]
         

Replace `SOURCE` with the name of the YAML file.




### API

To authenticate your backend requests by using the HMAC key, specify these additional configuration options in the `securitySettings` section of `backendServices`.

Use the [`Method: backendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [`Method: backendServices.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    securitySettings: {
      awsV4Authentication: {
        accessKeyId: ACCESS_KEY_ID,
        accessKey: ACCESS_KEY,
        [accessKeyVersion: ACCESS_KEY_VERSION],
        originRegion: REGION
      }
    }
    

Replace the following:

  * `ACCESS_KEY_ID`: the HMAC access key ID
  * `ACCESS_KEY`: the HMAC access key
  * `ACCESS_KEY_VERSION` (optional): a unique name that you can set to represent the key version
  * `REGION`: a valid region for your storage provider. For Amazon S3, the value is not a Google Cloud region.



The following snippet shows the contents of a sample JSON request body:
    
    
    securitySettings: {
      awsV4Authentication: {
        accessKeyId: "AKIDEXAMPLE",
        accessKey: "c4afb1cc5771d871763a393e44b703571b55cc28424d1a5e86da6ed3c154a4b9",
        accessKeyVersion: "prod-access-key-v1.2",
        originRegion: "us-east-2"
      }
    }
    

The service name is automatically set to `s3` for creating the signature. After these configurations are in place, Cloud CDN generates an HTTP Authorization header for all requests to your origin.

## Cache privately authenticated responses

You might want to ensure that privately authenticated content is cached by Cloud CDN.

To do this, set the [cache mode](https://docs.cloud.google.com/cdn/docs/using-cache-modes#cache-mode) to **Force cache all content** and specify a TTL, so that all content served from the origin is cached.

Alternatively, if you don't want to force all content to be cached the same way, change the cache mode to **Use origin setting based on Cache-Control headers** or **Cache static content** , and configure valid cache control headers on your origin-served content. For more information about how Cloud CDN evaluates these origin headers, see [Cache control header precedence](https://docs.cloud.google.com/cdn/docs/caching#cache-control-headers).

## What's next

  * [Web security best practices](https://docs.cloud.google.com/cdn/docs/web-security-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
