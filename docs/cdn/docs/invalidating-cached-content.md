---
url: https://docs.cloud.google.com/cdn/docs/invalidating-cached-content/
title: Invalidate cached content \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:36.409047+00:00
---

# Invalidate cached content  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/invalidating-cached-content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Invalidate cached content Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to invalidate your Cloud CDN cached content.

For example, if a file located at `/images/file.jpg` has been cached and needs to be invalidated, you can use several methods to invalidate it, depending on whether you want to affect only that file or a wider scope. In each case, you can invalidate for all hostnames or for only one hostname.

To learn more about cache invalidation, see [Cache invalidation overview](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview).

## Before you begin

You can use the Google Cloud CLI or the Google Cloud console to perform invalidations.

You can access the Google Cloud CLI in two ways:

  * Install the Google Cloud CLI by following the instructions at [Installing with `apt-get`](https://docs.cloud.google.com/sdk/docs/downloads-apt-get). If you haven't used the Google Cloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

  * Use [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which comes with `gcloud` already installed.




#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.urlMaps.get`
  * `compute.urlMaps.invalidateCache`
  * `compute.urlMaps.list`



**Roles**

  * `roles/compute.networkAdmin`
  * `roles/compute.loadBalancerAdmin`



To create a custom role with the required permissions, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

To add a predefined role, use the [IAM quickstart](https://docs.cloud.google.com/iam/docs/grant-role-console).

**Note:** If you're using a global external Application Load Balancer with Shared VPC cross-project service referencing, see [Invalidation with Shared VPC cross-project service referencing](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview#request-cache-invalidation-shared-vpc).

## Invalidate only one file

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click an origin.

  3. Click the **Cache invalidation** tab.

  4. For **Associated load balancers** , select the load balancer.

  5. Under **Specify objects to invalidate** , do the following:

     * For **Host** , unless you want to invalidate the path for all hostnames, specify a hostname.
     * For **Path** , specify the path and the filename—for example, `/images/file.jpg`.
  6. Click **Invalidate**.




###  gcloud 

Use the [`gcloud compute url-maps invalidate-cdn-cache` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache).

To specify only one file for invalidation, use the `--path` flag with the filename.
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --path "/images/file.jpg"
    

Replace `URL_MAP_NAME` with the name of your URL map. To list your URL maps, use the `gcloud compute url-maps list` command.

To invalidate for only one host, add the `--host` flag—for example, `--host host1.com`.
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --host host1.com \
        --path "/images/file.jpg"
    

By default, the Google Cloud CLI waits until the invalidation has completed. To perform the invalidation in the background, append `--async` to the command line.

###  API 

Use the [`urlMaps.invalidateCache` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/invalidateCache).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME/invalidateCache
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `URL_MAP_NAME`: the name of the URL map



To specify a file for invalidation, use the following sample JSON request body:
    
    
    {
      "path": "/images/file.jpg"
    }
    

To invalidate the file for only one host, use the following sample JSON request body:
    
    
    {
      "host": "host1.com",
      "path": "/images/file.jpg"
    }
    

## Invalidate the whole directory

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click an origin.

  3. Click the **Cache invalidation** tab.

  4. For **Associated load balancers** , select the load balancer.

  5. Under **Specify objects to invalidate** , do the following:

     * For **Host** , unless you want to invalidate the path for all hostnames, specify a hostname.
     * For **Path** , specify the path and an asterisk as a wildcard—for example, `/images/*`.
  6. Click **Invalidate**.




###  gcloud 

Use the [`gcloud compute url-maps invalidate-cdn-cache` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache).
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --path "/images/*"
    

Replace `URL_MAP_NAME` with the name of your URL map.

To invalidate for only one host, add the `--host` flag—for example, `--host host1.com`.
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --host host1.com \
        --path "/images/*"
    

###  API 

Use the [`urlMaps.invalidateCache` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/invalidateCache).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME/invalidateCache
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `URL_MAP_NAME`: the name of the URL map



To specify a directory for invalidation, use the following sample JSON request body:
    
    
    {
      "path": "/images/*"
    }
    

To invalidate a directory for only one host, use the following sample JSON request body:
    
    
    {
      "host": "host1.com",
      "path": "/images/*"
    }
    

## Invalidate by cache tags

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click an origin.

  3. Click the **Cache invalidation** tab.

  4. For **Associated load balancers** , select the load balancer.

  5. Under **Specify objects to invalidate** , for **Cache tags** , specify one or more tags to invalidate. Use spaces or commas to separate tags.

  6. Click **Invalidate**.




###  gcloud 

Use the [`gcloud beta compute url-maps invalidate-cdn-cache` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/invalidate-cdn-cache).
    
    
    gcloud beta compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --tags=TAGS
    

Replace the following:

  * `URL_MAP_NAME`: the name of the URL map
  * `TAGS`: a tag or a comma-separated list of tags; alternatively, you can specify this flag up to 10 times



For example, if the backend response includes a `Cache-Tag` header with an opaque user ID, such as a UUID4 or another form of GUID, you can invalidate all content for a specific user by using the `tag` flag. Additionally, to invalidate content for only one host, such as for your staging environment, add the `--host` flag.
    
    
    gcloud beta compute url-maps invalidate-cdn-cache url_map_1 \
        --tags="1115b8f4-f804-4861-9629-8cb9aecdeeb3" \
        --host="host1.com"
    

###  API 

Use the [`urlMaps.invalidateCache` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/urlMaps/invalidateCache).
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME/invalidateCache
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `URL_MAP_NAME`: the name of the URL map



To specify cache tags for invalidation, use the following sample JSON request body:
    
    
    {
      "cacheTags": [
        "tag1",
        "tag2"
      ]
    }
    

You can specify a single tag or a comma-separated list of tags.

To invalidate by cache tags for only one host, use the following sample JSON request body:
    
    
    {
      "host": "host1.com",
      "path": "tag1,tag2"
    }
    

## Invalidate everything

Although you can invalidate everything, it's potentially risky. Evaluate your requirements carefully before you proceed.

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click an origin.

  3. Click the **Cache invalidation** tab.

  4. For **Associated load balancers** , select the load balancer.

  5. Under **Specify objects to invalidate** , do the following:

     * For **Host** , unless you want to invalidate the path for all hostnames, specify a hostname.
     * For **Path** , use an asterisk—for example, `/*`.
  6. Click **Invalidate** and then click **Confirm** to indicate that you want Cloud CDN to invalidate everything.




###  gcloud 

Use the [`gcloud compute url-maps invalidate-cdn-cache` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache).
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --path "/*"
    

Replace the following:

  * `URL_MAP_NAME`: the name of the URL map
  * `/*`: the URL path that you want to invalidate; doesn't include the hostname; the path can use an explicit filename or an asterisk as a wildcard



To invalidate for only one host, add the `--host` flag—for example, `--host host1.com`.
    
    
    gcloud compute url-maps invalidate-cdn-cache URL_MAP_NAME \
        --host host1.com \
        --path "/*"
    

###  API 

Use the [`urlMaps.invalidateCache` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/invalidateCache).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_NAME/invalidateCache
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `URL_MAP_NAME`: the name of the URL map



To specify a URL path for invalidation, use the following sample JSON request body:
    
    
    {
      "path": "/*"
    }
    

To invalidate the URL path for only one host, use the following sample JSON request body:
    
    
    {
      "host": "host1.com",
      "path": "/*"
    }
    

## See the status of your invalidation request

Cloud CDN emits two log lines per invalidation, one when the invalidation is accepted and the other when it's complete. The first has the host and path information.

To see the status of your invalidation request or find a definitive list of recently submitted requests, you can use Cloud Logging or Cloud Monitoring.

###  Console 

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click an origin.

  3. Click the **Cache invalidation** tab.

  4. To see the status and results of the invalidation request, click **Go to Cloud Logging**.




###  gcloud 

The following is a sample command that uses Logging to read audit logs. To enable and view audit logs, see [Cloud CDN audit logging](https://docs.cloud.google.com/cdn/docs/audit-logging).
    
    
    gcloud logging read 'protoPayload.methodName="v1.compute.urlMaps.invalidateCache"' \
        --limit=10
    

The following is a sample query that uses Monitoring:
    
    
    protoPayload.serviceName="compute.googleapis.com"
    protoPayload.methodName="v1.compute.urlMaps.invalidateCache"
    

## What's next

  * To check whether Cloud CDN is serving responses from cache, see [Viewing logs](https://docs.cloud.google.com/cdn/docs/logging).
  * To learn about which content is cacheable or non-cacheable, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
