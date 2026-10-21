---
url: https://docs.cloud.google.com/appengine/docs/standard/serving-static-files/
title: Storing and serving static files \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:49.010747+00:00
---

# Storing and serving static files  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/serving-static-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Storing and serving static files Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

Applications often need to serve static files such as JavaScript, images, and CSS in addition to handling dynamic requests. Apps in the standard environment can serve static files from a Google Cloud option like Cloud Storage, serve them directly, or use a third-party content delivery network (CDN).

Hosting your static site on Google Cloud can cost less than using a traditional hosting provider, as Google Cloud provides a [free tier](https://docs.cloud.google.com/free/docs/free-cloud-features). 

## Serving files from Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage) can host static assets for dynamic web apps. The benefits of using Cloud Storage instead of serving directly from your app include:

  * Cloud Storage essentially works as a [content delivery network](https://wikipedia.org/wiki/Content_delivery_network). This does not require any special configuration because by default any publicly readable object is cached in the global Cloud Storage network.
  * Your app's load will be reduced by offloading serving static assets to Cloud Storage. Depending on how many static assets you have and the frequency of access, this can reduce the cost of running your app by a significant amount.
  * Bandwidth charges for accessing content can often be less with Cloud Storage.



You can upload your assets to Cloud Storage by using the [Google Cloud CLI](https://docs.cloud.google.com/storage/docs/uploading-objects) or the [Cloud Storage API](https://docs.cloud.google.com/storage/docs).

The Google Cloud Client Library provides an idiomatic [client to Cloud Storage](https://docs.cloud.google.com/storage/docs/reference/libraries), for storing and retrieving data with Cloud Storage in an App Engine app.

### Example of serving from a Cloud Storage bucket

This example creates a Cloud Storage bucket and uploads static assets using the gcloud CLI:

  1. Create a bucket. It's common, but not required, to name your bucket after your project ID. The bucket name must be globally unique.
         
         gcloud storage buckets create gs://<var>your-bucket-name</var>
         

  2. Set the IAM policy to grant public read access to items in the bucket.
         
         gcloud storage buckets add-iam-policy-binding gs://<var>your-bucket-name</var> --member=allUsers --role=roles/storage.objectViewer
         

  3. Upload items to the bucket. The `rsync` command is typically the fastest and easiest way to upload and update assets. You could also use `cp`.
         
         gcloud storage rsync ./static gs://<var>your-bucket-name</var>/static --recursive
         




You can now access your static assets via `https://storage.googleapis.com/<var>your-bucket-name</var>/static/...`.

For more details on how to use Cloud Storage to serve static assets, including how to serve from a custom domain name, refer to [How to Host a Static Website](https://docs.cloud.google.com/storage/docs/website-configuration).

### Serving files from other Google Cloud services

You also have the option of using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) or other Google Cloud storage services.

## Serving files directly from your app

To serve static files in the standard environment, you define the handlers in your `app.yaml` file using either the [`static_dir`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_dir) or [`static_files`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_files) elements.

The content in the static files or static directories are unaffected by the scaling settings in your `app.yaml` file. Requests to static files or static directories are handled by the App Engine infrastructure directly, and do not reach the language runtime of the application.

### Configuring your static file handlers

To configure your app to serve the `./public` directory from the `/static` URL, you define a handler in your `app.yaml` file.

The following demonstrates how to serve the static files of a sample app's `./public` directory. The template for this app's `index.html` page instructs the browser to load the `main.css` file, for example:
    
    
    <link type="text/css" rel="stylesheet" href="/static/css/main.css">

The `./public` directory is defined in the `static_dir` element of the project's `app.yaml` file:
    
    
    handlers:
      - url: /favicon\.ico
        static_files: favicon.ico
        upload: favicon\.ico
    
      - url: /static
        static_dir: public
    
      - url: /.*
        secure: always
        redirect_http_response_code: 301
        script: auto

The `handlers` section in the above example handles three URL patterns:

  * The **/favicon.ico** handler maps a request specifically for `/favicon.ico` to a file named `favicon.ico` in the app's root directory.

  * The **/static** handler maps requests for URLs that start with `/static`. When App Engine receives a request for a URL beginning with `/static`, it maps the remainder of the path to files in the `./public` directory. If an appropriate file is found in the directory, the contents of that file are returned to the client.

  * The **/.** * handler matches all other URLs and directs them to your app.




URL path patterns are tested in the order they appear in `app.yaml`, therefore the pattern for your static files should be defined before the `/.*` pattern. For more information, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers).

Note that to use static handlers, you must either specify the [`entrypoint`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) element in `app.yaml` or specify a handler with [`script`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_script) set to `auto`.

## Serving from a third-party content delivery network

You can use any external third-party CDN to serve your static files and cache dynamic requests but your app might experience increased latency and cost.

For improved performance, you should use a third-party CDN that supports [CDN Interconnect](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
