---
url: https://docs.cloud.google.com/media-cdn/docs/quickstart/
title: Set up a Media CDN service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:24.298361+00:00
---

# Set up a Media CDN service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Set up a Media CDN service Stay organized with collections  Save and categorize content based on your preferences. 

This quickstart shows you how to set up a Media CDN service in front of a Cloud Storage bucket. You can use this configuration for testing or as the basis for a production environment.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=media-cdn--quickstart)

* * *

This page walks you through the following procedures:

  1. Create a Cloud Storage bucket to store your content.
  2. Enable the required services.
  3. Create an `EdgeCacheOrigin` resource to connect Media CDN to your bucket.
  4. Create an `EdgeCacheService` resource to configure request routing and caching for content in the origin.
  5. Test whether a response is being cached.



## Before you begin

Make sure that you have the following:

  * [Access to Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview#request-access) for your current project.

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed. Use version 345.0.0 or later.

If required, use `gcloud version` to check the version and `gcloud components update` to update your installed gcloud CLI.

The gcloud CLI provides the [`gcloud edge-cache` sub-command group](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache) for managing both new and existing Media CDN configurations.

  * The Identity and Access Management (IAM) permissions required to create Media CDN resources.




### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant the following roles:

**Note:** These roles are visible only in projects where [Media CDN is enabled](https://docs.cloud.google.com/media-cdn/docs/overview#request-access).

  * `roles/networkservices.edgeCacheAdmin`: Access to create, update, delete, and manage all Edge Cache resources.
  * `roles/networkservices.edgeCacheUser`: Access to view and use Edge Cache resources.
  * `roles/networkservices.edgeCacheViewer`: Read-only access to Edge Cache resources.



**To create storage bucket**

  * [Storage Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



**To enable SSL on Media CDN**

  * [Certificate Manager Editor role](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager#certificatemanager.editor) (`roles/certificatemanager.editor`)



You might also be able to get the required permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Create a Cloud Storage bucket

Media CDN content can originate from locations such as a Cloud Storage bucket, a third-party storage location, or a load balancer.

In this quickstart, we'll store content in a Cloud Storage bucket.

  1. [Create a publicly accessible Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) and name it `my-bucket`.

If you prefer not to make your Cloud Storage bucket publicly accessible, you must give Media CDN permissions to access the bucket. For more information, see [Using private Cloud Storage buckets](https://docs.cloud.google.com/media-cdn/docs/configure-origin#private-storage-buckets).

  2. Upload a file into the bucket.


**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

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

## Create an `EdgeCacheOrigin` resource

Create an origin that points to your Cloud Storage bucket.

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Origins** tab.

  3. Click **Create origin**.

  4. Enter the name for the origin as `cloud-storage-origin`.

  5. Optional: Enter a description for the origin.

  6. For **Origin address** , choose **Select a Google Cloud Storage bucket** , browse to the Cloud Storage bucket named `my-bucket`, and then click **Select**.

If you have an external origin instead, choose **Specify an FQDN or IP address** , and then enter the FQDN or IP address.

  7. Click **Create origin**.




After approximately 10 minutes, the newly created `EdgeCacheOrigin` resource appears in the list of origins in your project on the **Origins** page.

To update an origin address, click the origin, and then click edit**Edit**.

###  gcloud 

Use the [`gcloud edge-cache origins create` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/create):
    
    
    gcloud edge-cache origins create ORIGIN \
        --origin-address="ADDRESS"
    

Replace the following:

  * `ORIGIN`: the name of the new origin
  * `ADDRESS`: the bucket name, `gs://my-bucket`



If you have an external origin instead, replace ADDRESS with the FQDN or IP address.

To view the newly created origin, use the [`gcloud edge-cache origins list` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/list).

To update the origin address, use the [`gcloud edge-cache origins update` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/update).

**Note:** Media CDN can take up to 10 minutes to create the origin.

###  API 

Use the [`edgeCacheOrigins.create` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins/create):
    
    
    POST https://networkservices.googleapis.com/v1/PARENT/edgeCacheOrigins?edgeCacheOriginId=ORIGIN_ID
    {
      "name": "ORIGIN_ID",
      "originAddress: "ADDRESS"
    }
    

Replace the following:

  * `PARENT`: the parent resource in the format `projects/PROJECT/locations/global`
  * `ORIGIN_ID`: the short name of the new origin
  * `ADDRESS`: the bucket name, `gs://my-bucket`

If you have an external origin instead, replace `ADDRESS` with the FQDN or IP address.




To view the newly created origin, use the [`edgeCacheOrigins.list` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins/list).

To update the origin address, use the [`edgeCacheOrigins.patch` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins/patch).

**Note:** Media CDN can take up to 10 minutes to create the origin

###  Terraform 
    
    
    resource "google_network_services_edge_cache_origin" "default" {
      name           = "cloud-storage-origin"
      origin_address = "gs://my-bucket-${random_id.unique_suffix.hex}"
    }

## Create an `EdgeCacheService` resource

Your `EdgeCacheService` resource configures routing, certificate, and caching settings, and can point to `EdgeCacheOrigin` resources.

Create a basic `EdgeCacheService` resource that does the following:

  * Caches all responses from our configured origin for one hour
  * Sets an `x-cache-status` response header that returns the cache status (such as `HIT` or `MISS`)



Optionally, [register a domain name](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#register-domain) for this service.

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.

  3. Click **Create service**.

  4. Enter a unique name for your service—for example, `my-service`—and then click **Next**.

  5. In the **Routing** section, click **Add host rule** , and then enter one or more host domain names.

  6. For **Hosts** , enter a host domain name—for example, `web.example.com`.

  7. Click **Add route rule**.

     1. For **Priority** , specify `1`.
     2. Click **Add match condition** , for **Path match** , specify `/`, and then click **Done**.
     3. Select **Fetch from an Origin** , and then select the origin that you configured.
     4. Click **Add-on actions**.
     5. For **Header action** , click **Add an item**. Then, do the following: 
        1. For **Type** , select **Response headers to add**.
        2. Click **Add header**.
        3. For **Name** , specify `x-cache-status`, and for **Value** , specify `{cdn_cache_status}`.
        4. Click **Done**.
     6. For **Route action** , click **Add an item**. Then, do the following: 
        1. For **Type** , select **CDN policy**.
        2. For **Cache mode** , select **FORCE_CACHE_ALL**.
        3. Click **Done**.
     7. Click **Save**.
  8. Click **Create service**.




The newly created `EdgeCacheService` resource appears on the **Services** page in the list of services in your project.

**Note:** Media CDN can take up to 10 minutes to create the service

###  gcloud 

  1. In Cloud Shell, use a text editor to create a local file called `my-service.yaml`.

Such a file indicates the following:

     * How routing works—by first matching the host and then the path
     * How caching works—based on the cache mode and TTL
     * How requests and responses are modified—for example, by inserting the `cdn_cache_status` variable into a response header
  2. Paste the following sample content into the file, and then save it:
         
         name: SERVICE
         routing:
           hostRules:
           - hosts:
             - DOMAIN 
             pathMatcher: routes
           pathMatchers:
           - name: routes
             routeRules:
             - priority: 1
               matchRules:
               - prefixMatch: /
               origin: ORIGIN
               routeAction:
                 cdnPolicy:
                   cacheMode: CACHE_ALL_STATIC
                   defaultTtl: 3600s
               headerAction:
                 responseHeadersToAdd:
                 - headerName: "x-cache-status"
                   headerValue: "{cdn_cache_status}"
         

Replace the following:

     * `SERVICE`: name of the service
     * `DOMAIN`: the domain for the new service

If you specify the domain name, Media CDN responds with a `404` error for other hosts.

     * `ORIGIN`: the name of the related origin

  3. Use the [`gcloud edge-cache services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import) with the YAML file:
         
         gcloud edge-cache services import SERVICE \
             --source=my-service.yaml
         

To view the newly created service in the list of `EdgeCacheService` resources in your project, use the [`gcloud edge-cache services list` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/list).

**Note:** Media CDN can take up to 10 minutes to create the service



###  API 

Use the [`edgeCacheServices.create` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/create):
    
    
    POST https://networkservices.googleapis.com/v1/PARENT/edgeCacheServices?edgeCacheServiceId=SERVICE_NAME
    {
      "name": "SERVICE_NAME",
      "routing": {
        "hostRules": [
          {
            "hosts": ["DOMAIN"],
            "pathMatcher": "routes"
          }
        ],
        "pathMatchers": [
          {
            "name": "routes",
            "routeRules": [
              {
                "priority": "1",
                "matchRules": [
                  {
                    "prefixMatch": "/"
                  }
                ],
                "origin": "ORIGIN",
                "routeAction": {
                   "cdnPolicy": {
                     "cacheMode": "CACHE_ALL_STATIC",
                     "defaultTtl": "3600s"
                   }
                }
                "headerAction": {
                  "responseHeadersToAdd": [
                    {
                      "headerName": "x-cache-status",
                      "headerValue": "{cdn_cache_status}"
                    }
                  ]
                },
              }
            ]
          }
        ]
      }
    }
    

Replace the following:

  * `PARENT`: the parent resource in the format `projects/PROJECT/locations/global`
  * `SERVICE_NAME`: the name of the service
  * `DOMAIN`: the domain for the new service

If you specify the domain name, Media CDN responds with a `404` error for other hosts.

  * `ORIGIN_NAME`: the name of the related origin




To view the newly created service in the list of `EdgeCacheService` resources in your project, use the [`edgeCacheServices.list` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/list).

**Note:** Media CDN can take up to 10 minutes to create the service

###  Terraform 
    
    
    resource "google_network_services_edge_cache_service" "default" {
      name = "cloud-media-service"
      routing {
        host_rule {
          hosts        = ["googlecloudexample.com"]
          path_matcher = "routes"
        }
        path_matcher {
          name = "routes"
          route_rule {
            description = "a default route rule, priority=10 (low)"
            priority    = 10
            match_rule {
              prefix_match = "/"
            }
            origin = google_network_services_edge_cache_origin.default.name
            route_action {
              cdn_policy {
                cache_mode  = "CACHE_ALL_STATIC"
                default_ttl = "3600s"
              }
            }
            header_action {
              response_header_to_add {
                header_name  = "x-cache-status"
                header_value = "{cdn_cache_status}"
              }
            }
          }
        }
      }
    }

It might take several minutes for your first service to be created. Media CDN provisions dedicated IP addresses and pushes your configuration to thousands of edge locations. Subsequent updates to a service, such as changing a route configuration or matching parameters, are faster.

### Retrieve the IP addresses

To view the IP addresses for your newly created service, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.

  3. For the IP addresses of your service, see the **Addresses** cell.

If the cell is empty, refresh the browser.




###  gcloud 

Use the [`gcloud edge-cache services describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/describe):
    
    
    gcloud edge-cache services describe SERVICE
    

Replace SERVICE with the name of the service.

The output shows the IP addresses assigned to your service:
    
    
    ipv4Addresses:
        IPV4_ADDRESS
    ipv6Addresses:
        IPV6_ADDRESS
    name: projects/my-project/locations/global/edgeCacheServices/SERVICE
    ...
    

###  API 

Use the [`edgeCacheServices.get` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/get):
    
    
    GET https://networkservices.googleapis.com/v1/SERVICE_NAME
    

Replace `SERVICE_NAME` with the full name of the service. Use the following format:
    
    
    projects/PROJECT/locations/global/edgeCacheServices/SERVICE_NAME
    

Replace `SERVICE_NAME` with the short name of the service.

The retrieved details include the IP addresses assigned to the service:
    
    
    ipv4Addresses:
        IPV4_ADDRESS
    ipv6Addresses:
        IPV6_ADDRESS
    

## Test whether a response is being cached

Before testing the service, make sure that you have [cacheable content](https://docs.cloud.google.com/media-cdn/docs/caching) stored at your origin so that Media CDN can retrieve it.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

To test that your service is correctly configured to cache content, use the `curl` command-line tool to issue requests and check the responses. `curl` is also available in [Cloud Shell](https://docs.cloud.google.com/shell) in the Google Cloud console.

If you'd like to use your `EdgeCacheService` with your domain, you can assign the IP address of the `EdgeCacheService` to a domain record. For instructions, see [Set up your domain using Cloud DNS](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#set-up-domain). After you've set up your domain, access your content with the following `curl` command:
    
    
    curl -svo /dev/null "http://DOMAIN_NAME/FILENAME"
    

If you did not configure DNS to point to your provisioned IP addresses, use the `resolve` option to override the address that `curl` uses.
    
    
    curl -svo /dev/null --resolve DOMAIN_NAME:80:IP_ADDRESS "http://DOMAIN_NAME/FILENAME"
    

Replace the following:

  * `DOMAIN_NAME` : the host domain you specified while creating the service
  * `IP_ADDRESS`: the IP address of the service as visible in the **Addresses** column in the list of services
  * `FILENAME`: the name of the file you uploaded to the bucket



Example:
    
    
    curl -svo /dev/null --resolve web.example.com:80:34.104.37.129 "http://web.example.com/file.mp4"
    

The command initially produces output similar to the following, with the status `miss`, because Media CDN doesn't have the requested data already retrieved from the origin:
    
    
    < HTTP/2 200 OK
    ...
    < x-cache-status: den;miss
    ...
    

When you submit the same request again any number of times, it produces an output similar to the following, with the status `hit`:
    
    
    < HTTP/2 200 OK
    ...
    < x-cache-status: den;hit
    ...
    

If it doesn't show the status `hit`, check the following:

  * The response is cacheable.
  * The configured cache mode allows caching of the content.
  * The origin isn't setting cache directives that prevent caching. For more information, see [Cache configuration](https://docs.cloud.google.com/media-cdn/docs/caching).



You've now tested a basic `EdgeCacheService` resource that can serve content globally. A production-grade service might need [SSL (TLS) certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates), multiple origins, and a [Google Cloud Armor security policy](https://docs.cloud.google.com/media-cdn/docs/security-policies).

## Optional: Clean up

Delete any resources that you don't intend to use again.

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.

  3. Select your service, and then click **Delete**.

  4. Click the **Origins** tab.

  5. Select your origin, and then click **Delete**.




###  gcloud 

  1. To list the resources that you created, use the [`gcloud edge-cache origins list` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/list) and the [`gcloud edge-cache services list` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/list).

  2. To delete the service, use the [`gcloud edge-cache services delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/delete):
         
         gcloud edge-cache services delete SERVICE
         

Replace `SERVICE` with the name of the service.

  3. To delete the origin, use the [`gcloud edge-cache origins delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete):
         
         gcloud edge-cache origins delete ORIGIN
         

Replace `ORIGIN` with the name of the origin.




###  API 

  1. To list the resources that you created, use the [`edgeCacheServices.list` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/list) and the [`edgeCacheOrigins.list` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/list).

  2. To delete the service, use the [`edgeCacheServices.delete` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/delete):
         
         DELETE https://networkservices.googleapis.com/v1/SERVICE_NAME
         

Replace `SERVICE_NAME` with the full name of the service. Use the following format:
         
         projects/PROJECT/locations/global/edgeCacheServices/SERVICE_NAME
         

Replace `SERVICE_NAME` with the short name of the service.

  3. To delete the origin, use the [`edgeCacheOrigins.delete` method](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins/delete):
         
         DELETE https://networkservices.googleapis.com/v1/ORIGIN
         

Replace `ORIGIN` with the full name of the origin. Use the following format:
         
         projects/PROJECT/locations/global/edgeCacheOrigins/ORIGIN_ID
         

Replace `ORIGIN_ID` with the short name of the origin.




Repeat this process for any other resources that you created and don't intend to use again, such as the Cloud Storage bucket.

## What's next

  * [Issue and attach an SSL (TLS) certificate](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) to your `EdgeCacheService`.
  * [View request logs](https://docs.cloud.google.com/media-cdn/docs/logging) with Cloud Logging.
  * [Configure signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) to protect your content.
  * [Optimize cache keys and TTLs](https://docs.cloud.google.com/media-cdn/docs/caching) and improve cache hit rates.
  * [Configure advanced route matching](https://docs.cloud.google.com/media-cdn/docs/routing) and create additional origins.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
