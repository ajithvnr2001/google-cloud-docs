---
url: https://docs.cloud.google.com/storage/docs/cors-configurations/
title: CORS configuration examples \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:47.996376+00:00
---

# CORS configuration examples  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cors-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  CORS configuration examples Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/cross-origin) [Setup](https://docs.cloud.google.com/storage/docs/using-cors)

This page shows example configurations for [Cross-origin resource sharing (CORS)](https://docs.cloud.google.com/storage/docs/cross-origin).

When you set a CORS configuration on a bucket, you allow interactions between resources from different origins, something that is normally prohibited in order to prevent malicious behavior. To learn how to structure a request that sets or edits a CORS configuration on a bucket, see the instructions in [Using CORS](https://docs.cloud.google.com/storage/docs/using-cors).

Note the following additional resources:

  * For the generalized format of a CORS configuration file, see the [bucket resource representation for JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations) or the [CORS configuration format for XML](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#cors-body).

  * When sending requests using the Google Cloud CLI, use the correct CORS file configuration structure.




## Basic CORS configuration

Say you have a dynamic website which users can access at `your-example-website.appspot.com`. You have an image file hosted in a Cloud Storage bucket named `your-example-bucket`. You'd like to use the image on your website, so you must apply a CORS configuration on `your-example-bucket` that enables your users' browsers to request resources from the bucket. Based on the following configuration, preflight requests are valid for 1 hour, and successful browser requests return the `Content-Type` of the resource in the response.

**Note:** When [creating a CORS configuration](https://docs.cloud.google.com/storage/docs/using-cors#configure-cors-bucket), you can [specify multiple origins, headers, and methods](https://docs.cloud.google.com/storage/docs/cross-origin#multiple-origins-methods-headers).

### JSON API
    
    
    {
      "cors": [
        {
          "origin": ["https://your-example-website.appspot.com"],
          "method": ["GET"],
          "responseHeader": ["Content-Type"],
          "maxAgeSeconds": 3600
        }
      ]
    }

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>https://your-example-website.appspot.com</Origin>
        </Origins>
        <Methods>
          <Method>GET</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>Content-Type</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>3600</MaxAgeSec>
      </Cors>
    </CorsConfig>

## Direct file uploads (for single-page applications)

Use this configuration when your frontend application needs to upload files directly to a bucket, which requires a `PUT` operation. This is a common need for single-page applications, where the application logic lives in the user's browser instead of in a backend server.

Note that `PUT` requests always trigger a preflight check.

### JSON API
    
    
    {
     "cors": [
        {
            "origin": ["https://www.example-website.appspot.com"],
            "method": ["PUT", "POST", "OPTIONS"],
            "responseHeader": ["Content-Type", "x-goog-resumable"],
            "maxAgeSeconds": 3600
          }
      ]
    }

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>https://your-example-website.appspot.com</Origin>
        </Origins>
        <Methods>
          <Method>PUT</Method>
          <Method>POST</Method>
          <Method>OPTIONS</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>Content-Type</ResponseHeader>
          <ResponseHeader>x-goog-resumable</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>3600</MaxAgeSec>
      </Cors>
    </CorsConfig>

### Client-side code sample

### JavaScript
    
    
    // Uploading a file using a Signed URL or direct PUT
    await fetch(gcsSignedUrl, {
      method: 'PUT',
      body: fileBlob,
      headers: {
        'Content-Type': 'application/pdf'
      }
    });

## Authenticated data access

Use this configuration if your application sends a bearer token or a Google Identity header to access protected (non-public) objects.

### JSON API
    
    
    {
     "cors": [
        {
            "origin": ["https://www.example-secure-app.appspot.com"],
            "method": ["GET", "HEAD"],
            "responseHeader": ["Authorization", "Content-Type"],
            "maxAgeSeconds": 3600
          }
      ]
    }

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>https://www.example-secure-app.appspot.com</Origin>
        </Origins>
        <Methods>
          <Method>GET</Method>
          <Method>HEAD</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>Authorization</ResponseHeader>
          <ResponseHeader>Content-Type</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>3600</MaxAgeSec>
      </Cors>
    </CorsConfig>

## Allowing access for multiple matching subdomains

Use this configuration if you have multiple development or staging environments that need access to the same bucket. Using the wildcard `*` when specifying a subdomain lets you match multiple subdomains. For example, `*.example.com` can be used to match `test.example.com` and `prod.example.com`.

### JSON API
    
    
    {
     "cors": [
        {
            "origin": ["https://*.example.com"],
            "method": ["GET", "POST", "OPTIONS"],
            "responseHeader": ["Content-Type", "x-goog-resumable"],
            "maxAgeSeconds": 3600
          }
      ]
    }

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>https://*.example.com</Origin>
        </Origins>
        <Methods>
          <Method>GET</Method>
          <Method>POST</Method>
          <Method>OPTIONS</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>Content-Type</ResponseHeader>
          <ResponseHeader>x-goog-resumable</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>3600</MaxAgeSec>
      </Cors>
    </CorsConfig>

## Allowing access for any origin

Use this configuration for public-facing data where restriction isn't required. Specifying the wildcard `*` as the origin allows requests from any origin. Note that with this configuration, requests to the bucket will fail if the client sets `credentials: include` in their request.

### JSON API
    
    
    {
     "cors": [
        {
            "origin": ["*"],
            "method": ["GET"],
            "responseHeader": ["Content-Type"],
            "maxAgeSeconds": 1800
          }
      ]
    }

### XML API
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <CorsConfig>
      <Cors>
        <Origins>
          <Origin>*</Origin>
        </Origins>
        <Methods>
          <Method>GET</Method>
        </Methods>
        <ResponseHeaders>
          <ResponseHeader>Content-Type</ResponseHeader>
        </ResponseHeaders>
        <MaxAgeSec>1800</MaxAgeSec>
      </Cors>
    </CorsConfig>

## CORS configuration structure for gcloud CLI

The [`gcloud storage buckets update --cors-file`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command expects a file containing only the list of CORS rules. When specifying a CORS configuration to be [set](https://docs.cloud.google.com/storage/docs/using-cors#configure-cors-bucket) using the Google Cloud CLI, remove the top level `"cors":` wrapper from the JSON file.

For example, this gcloud CLI command sets a CORS configuration on a bucket:
    
    
    gcloud storage buckets update gs://example_bucket --cors-file=example_cors_file.json

This is an example configuration for `example_cors_file.json` that uses the correct structure for the `gcloud storage buckets update --cors-file` command.
    
    
    [
        {
          "origin": ["https://your-example-website.appspot.com"],
          "method": ["GET"],
          "responseHeader": ["Content-Type"],
          "maxAgeSeconds": 3600
        }
    ]

## What's next

  * Learn more about [Cross Origin Resource Sharing (CORS)](https://docs.cloud.google.com/storage/docs/cross-origin).
  * [Set and view the CORS configuration](https://docs.cloud.google.com/storage/docs/using-cors) on a bucket.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
