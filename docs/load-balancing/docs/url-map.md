---
url: https://docs.cloud.google.com/load-balancing/docs/url-map/
title: Use URL maps \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:37.319624+00:00
---

# Use URL maps  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/url-map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use URL maps Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud URL maps. A URL map is a set of rules for routing incoming HTTP(S) requests to specific backend services or backend buckets. A minimal URL map matches all incoming request paths (`/*`).

Before following this guide, familiarize yourself with [URL map concepts](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

**Note:** This page describes how to configure a specific load balancer component or feature before or after you've already created a load balancer. Working with specific components is useful for advanced configurations and necessary for some configuration options. Before using the information on this page, know the [type of Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) that you need.

URL maps are used with the following Google Cloud products:

  * [External Application Load Balancer (global, classic, and regional modes)](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)


  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/traffic-director-concepts)



URL maps used with global external Application Load Balancers, regional external Application Load Balancers, internal Application Load Balancers, and Cloud Service Mesh also support several advanced traffic management features. For more information, see [URL map concepts: Advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#advanced-traffic-management).

## URL map defaults

URL maps have two defaults, as described in the following table.

Default type | Setting | Meaning  
---|---|---  
URL map default | `gcloud compute url-maps create` `--default-service | --default-backend-bucket` | The specified default backend service or backend bucket is used if none of the path matchers or host rules match the incoming URL.  
Path matcher default | `gcloud compute url-maps add-path-matcher` `--default-service | --default-backend-bucket` | The specified default backend service or backend bucket is used if the URL's path matches a path matcher, but none of the specified `--path-rules` match.  
  
## Host rules

A host rule defines a set of hosts to match requests against.

In a host rule, the hostname must be a fully qualified domain name (FQDN). The hostname can't be an IPv4 or IPv6 address. For example:

  * Works: `example.com`
  * Works: `web.example.com`
  * Works: `*.example.com`
  * Doesn't work: `35.244.221.250`



## Configure URL maps

A URL map can send traffic to [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) or [backend buckets](https://docs.cloud.google.com/load-balancing/docs/backend-bucket). **Important:** If you originally set up your load balancer in the Google Cloud console, the URL map's name is the same as your load balancer's name.

###  Console 

To add a URL map using the Google Cloud console, perform the following steps:

  1. Go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. Select **Host and path rules**.
  5. Click **Add host and path rule**.
  6. Fill in the **Host** field, **Paths** field, or both, and select a **backend service** or **backend bucket**.

     1. Enter a fully qualified **Host name** , for example `web.example.com`.
     2. Enter the path—for example, `/video`.
     3. On the **Host and path rules** page, in the **Backends** menu, select an available backend service or backend bucket.
**Note:** If a backend service or backend bucket is not added to the URL map's host and path rules, the backend service or backend bucket remains unused by the load balancer, so you won't see it on the load balancer's **Details** and **Edit** pages.
  7. Look for the blue checkmark to the left of **Host and Path Rules** and click the **Update** button.




###  gcloud 

To add a URL map using the Google Cloud CLI, use the [`url-maps create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create) command:
    
    
    gcloud compute url-maps create URL_MAP_NAME \
       (--default-backend-bucket=DEFAULT_BACKEND_BUCKET | --default-service=DEFAULT_SERVICE) \
       [--description DESCRIPTION] \
       [--global | --region=REGION]
    

For regional external Application Load Balancers and internal Application Load Balancers, make sure to include the `--region` flag when you create the URL map.

To create a path matcher, use the [`gcloud compute url-maps add-path-matcher`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher) command:
    
    
    gcloud compute url-maps add-path-matcher URL_MAP_NAME \
       (--default-backend-bucket=DEFAULT_BACKEND_BUCKET | --default-service=DEFAULT_SERVICE) \
       --path-matcher-name PATH_MATCHER \
       [--path-rules="PATH=SERVICE or BUCKET"]
    

This command requires a default backend service or backend bucket to which it can send unmatched requests. The `--path-rules` flag defines mappings between request paths and backend services or buckets. The following example routes the request paths `/video/` and `/video/*` to the `video-service` backend service:
    
    
    --path-rules="/video=video-service,/video/*=video-service"
    

To create a host rule, use the [`gcloud compute url-maps add-host-rule`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule) command:
    
    
    gcloud compute url-maps add-host-rule URL_MAP_NAME \
        --hosts=[HOSTS] --path-matcher-name=PATH_MATCHER
    

For example, the following `--hosts` value matches requests against `www.example.com` and any subdomain of `altostrat.com`:
    
    
    --hosts=[*.altostrat.com,www.example.com]
    

To change the default service or default bucket of a URL map, use the `url-maps set-default-service` command:
    
    
    gcloud compute url-maps set-default-service URL_MAP_NAME
      (--default-backend-bucket=DEFAULT_BACKEND_BUCKET
      | --default-service=DEFAULT_SERVICE)[GCLOUD_WIDE_FLAG ...]
    

###  Terraform 

To create a global URL map, use the [google_compute_url_map resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_url_map). 
    
    
    # url map
    resource "google_compute_url_map" "default" {
      name            = "http-lb"
      default_service = google_compute_backend_bucket.default.id
    }

To create a regional URL map, use the [google_compute_region_url_map resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_url_map). 
    
    
    resource "google_compute_region_url_map" "default" {
      name            = "regional-l7-xlb-map"
      region          = "us-west1"
      default_service = google_compute_region_backend_service.default.id
    }

## Validate the URL map configuration

**Note:** The [`gcloud compute url-maps validate`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate) command is not supported for the regional external Application Load Balancer and the internal Application Load Balancer.

Before deploying a URL map, make sure you validate the URL map configuration to ensure that the map is routing requests to the appropriate backends as intended. You can do this by adding tests to the URL map configuration. You can experiment with different URL map rules and run as many tests as needed to be confident that the map will route traffic appropriately when it is deployed. Additionally, if any rule changes are needed in the future, you can test those changes before actually going live with the new configuration.

Use the [`gcloud compute url-maps validate`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate) command to validate URL map configuration. This command only tests the configuration provided. Irrespective of whether the tests pass or fail, no changes are saved to the deployed URL map. This behavior is unlike other URL map commands (`edit`, `import`), which also run the same tests but will actually save the new configuration if tests pass. When you want to test a new routing configuration without making changes to the deployed URL map, use the `validate` command.

The `validate` command lets you test advanced route configurations such as routing based on headers and query parameters, HTTP to HTTPS redirects, and URL rewrites.

###  Console 

You can't use the Google Cloud console to validate URL map configuration. Use `gcloud` or the REST API instead.

###  gcloud 

To validate your URL map configuration use the [`gcloud compute url-maps validate`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate) command.

For the global external Application Load Balancer:
    
    
    gcloud compute url-maps validate --source PATH_TO_URL_MAP_CONFIG_FILE \
        --load-balancing-scheme=EXTERNAL_MANAGED \
        --global
    

For the classic Application Load Balancer:
    
    
    gcloud compute url-maps validate --source PATH_TO_URL_MAP_CONFIG_FILE \
        --load-balancing-scheme=EXTERNAL \
        --global
    

  * PATH_TO_URL_MAP_CONFIG_FILE: Replace with a path to the file that contains the URL map configuration for validation.



### Validate changes to an existing load balancer's URL map

If you have an existing load balancer that needs changes to the URL map, you can test those configuration changes before making them live.

  1. Export the load balancer's existing URL map to a YAML file.
         
         gcloud compute url-maps export URL_MAP_NAME \
            --destination PATH_TO_URL_MAP_CONFIG_FILE \
            --global
         

  2. Edit the YAML file with new configuration. For example, if you want to edit an external Application Load Balancer and send all requests with the path `/video` to a new backend service called `video-backend-service`, you can add tests to the URL map configuration as follows:

Existing URL map configuration with a single default `web-backend-service`:
         
         kind: compute#urlMap
          name: URL_MAP_NAME
          defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/web-backend-service
          

Edited URL map configuration with added path matcher and tests for both the default `web-backend-service` and the new `video-backend-service` backend service:
         
         kind: compute#urlMap
          name: URL_MAP_NAME
          defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/web-backend-service
          hostRules:
          - hosts:
            - '*'
            pathMatcher: pathmap
          pathMatchers:
          - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/web-backend-service
            name: pathmap
            pathRules:
            - paths:
              - /video
              - /video/*
              service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/video-backend-service
          tests:
          - description: Test routing to existing web service
            host: foobar
            path: /
            service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/web-backend-service
          - description: Test routing to new video service
            host: foobar
            path: /video
            service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendService/video-backend-service
         

  3. Validate the new configuration.
         
         gcloud compute url-maps validate --source PATH_TO_URL_MAP_CONFIG_FILE
         

If all tests pass successfully, you should see a success message such as:
         
         Successfully validated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/URL_MAP_CONFIG_FILE_NAME]
         

If the tests fail, an error message appears. Make the required fixes to the URL map config file and try validating again.
         
         Error: Invalid value for field 'urlMap.tests': ''.
         Test failure: Expect URL 'HOST/PATH' to map to service 'EXPECTED_BACKEND_SERVICE', but actually mapped to 'ACTUAL_BACKEND_SERVICE'.
         

  4. Once you know that the new configuration works and does not impact your existing setup, you can import it into the URL map. Note that this step also deploys the URL map with the new configuration.
         
         gcloud compute url-maps import URL_MAP_NAME \
            --source PATH_TO_URL_MAP_CONFIG_FILE \
            --global
         




## Add tests to a URL map

**Note:** Adding tests to URL maps is not supported for the regional external Application Load Balancer and the internal Application Load Balancer.

You can add configuration tests to a URL map to ensure that your URL map routes requests to the backend services or backend buckets as intended.

This section describes how to add tests to a URL map that has already been deployed. If you want to test new changes to a URL map without actually deploying the map, see Validate URL map configuration.

When you edit your URL map, the tests run, and an error message appears if a test fails:
    
    
    Error: Invalid value for field 'urlMap.tests': ''.
    Test failure: Expect URL 'HOST/PATH' to map to service 'EXPECTED_BACKEND_SERVICE', but actually mapped to 'ACTUAL_BACKEND_SERVICE'.
    

Adding tests to URL maps is optional.

###  Console 

To run tests from the Google Cloud console:

  1. Go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. Click **Routing rules**. For a classic Application Load Balancer, this is **Host and path rules**.
  5. Click **Show configuration tests**.
  6. Click **Add configuration test**. Add the following test URLs and backends: 
     * **Test host and path 1** `example.com` and **Backend** `www-service.`
     * **Test host and path 2** `example.net` and **Backend** `www-service.`
     * **Test host and path 3** `example.net/web` and **Backend** `www-service.`
     * **Test host and path 4** `example.com/videos` and **Backend** `video-service.`
     * **Test host and path 5** `example.com/videos/browse` and **Backend** `video-service.`
     * **Test host and path 6** `example.net/static` and **Backend** `static-service.`
     * **Test host and path 7** `example.net/static/images` and **Backend** `static-service.`
  7. Look for the blue checkmark to the left of **Routing rules** and click the **Update** button. For a classic Application Load Balancer, look for the blue check next to **Host and path rules**.



###  gcloud 

To add tests to your URL map using the Google Cloud CLI, use the [`gcloud compute url-maps edit`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit) command:
    
    
    gcloud compute url-maps edit URL_MAP_NAME
    

This launches a text editor. For external Application Load Balancers, your tests must use the following format:
    
    
      tests:
        - host: example.com
        service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/www-service
        - host: example.net
        service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/www-service
        - host: example.com
          path: /videos
          service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-service
        - host: example.com
          path: /videos/browse
          service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-service
        - host: example.net
          path: /web
          service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/www-service
        - host: example.net
          path: /static
          service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/static-service
        - host: example.net
          path: /static/images
          service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/static-service
    

Note that if you don't specify a host in a host rule, then URLs from all hosts (both example.com and example.net) can match. If you do have host rules, then you must create rules that match both example.com and example.net.

## List URL maps

###  Console 

You can't list all of your URL maps in the Google Cloud console.

###  gcloud 

To display a list of URL maps using the Google Cloud CLI, use the [`url-maps list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/list) command.
    
    
    gcloud compute url-maps list
    

## Get information about a URL map

###  Console 

To get information about a URL map, perform the following steps:

  1. Go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. View the **Host and path rules**.



###  gcloud 

To get information about a single URL map using the Google Cloud CLI, use the [`url-maps describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/describe) command.
    
    
    gcloud compute url-maps describe URL_MAP_NAME
    

## Delete a URL map

You can delete a URL map only after you've deleted all target proxies that reference it. For more information, see [Deleting a target proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies#delete_a_target_proxy).

###  Console 

To delete a URL map, perform the following steps:

  1. Go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. On the **Load Balancer Details** page, view the **Host and path rules**.
  5. Click the "X" to the right of a URL map to delete it. The URL map disappears.
  6. Look for the blue checkmark to the left of **Host and Path Rules** and click the **Update** button.



###  gcloud 

To delete a URL map using the Google Cloud CLI, use the [`url-maps delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/delete) command. Before you can delete a URL map, any target HTTP proxies that reference the URL map must first be deleted.
    
    
    gcloud compute url-maps delete URL_MAP_NAME [--quiet]
    

### Delete a path matcher

###  Console 

To delete a path matcher, perform the following steps:

  1. Go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. Select **Host and path rules**.
  5. In the **Paths** field for an existing URL map, click the "x" on the path matcher's name.
  6. Look for the blue checkmark to the left of **Host and Path Rules** and click the **Update** button.



###  gcloud 

To delete a path matcher, use the [`gcloud compute url-maps remove-path-matcher`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher) command:
    
    
    gcloud compute url-maps remove-path-matcher URL_MAP_NAME \
       [--path-matcher-name PATH_MATCHER]
    

### Delete a host rule

###  Console 

To delete a host rule, perform the following steps:

  1. If you're not already on the **Host and path rules** page, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the **Name** of a load balancer.
  3. On the **Load Balancer Details** page, click **edit Edit** for the selected load balancer.
  4. Select **Host and path rules**.
  5. In the **Hosts** field for an existing URL map, click the "x" on the host's name.
  6. Look for the blue checkmark to the left of **Host and Path Rules** and click the **Update** button.



###  gcloud 

To delete a host rule from your URL map, use the [`gcloud compute url-maps remove-host-rule`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule) command:
    
    
    gcloud compute url-maps remove-host-rule URL_MAP_NAME --host=HOST
    

For example, to remove a host rule that contains the host `altostrat.com` from a URL map named `my-map`, you would run the following command:
    
    
    gcloud compute url-maps remove-host-rule my-map --host altostrat.com
    

## Traffic management guides

Not all URL map features are available for all products. URL maps are used with load balancers to support several advanced traffic management features, not all of which are supported on the classic Application Load Balancer.

Use the following table to learn about the URL map features for management works.

Product | URL map features and traffic management guides  
---|---  
Global external Application Load Balancer | [Load balancer features: Routing and traffic management](https://docs.cloud.google.com/load-balancing/docs/features#routing_and_traffic_management) [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global) [Setting up traffic management](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt) [ Setting up a URL redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#url-redirect) [ Setting up an HTTP-to-HTTPS redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-http-https-redirect) [Hostname and path](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) [Routing requests](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#routing_requests_to_backends) [Cookies](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#http-cookie)  
Classic Application Load Balancer | [Load balancer features: Routing and traffic management](https://docs.cloud.google.com/load-balancing/docs/features#routing_and_traffic_management) [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management) [ Setting up a URL redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-redirects-classic) [ Setting up an HTTP-to-HTTPS redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-http-https-redirect) [Hostname and path](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) [Header and query parameter-based routing](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-query-and-header-routing)  
Regional external Application Load Balancer | [Load balancer features: Routing and traffic management](https://docs.cloud.google.com/load-balancing/docs/features#routing_and_traffic_management) [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional) [Setting up traffic management](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt) [ Setting up a URL redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#url-redirect) [ Setting up an HTTP-to-HTTPS redirect](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect) [Hostname and path](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) [Routing requests](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional#routing_requests_to_backends) [Cookies](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#http-cookie)  
Internal Application Load Balancer | [Load balancer features: Routing and traffic management](https://docs.cloud.google.com/load-balancing/docs/features#routing_and_traffic_management) [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal/traffic-management#traffic-mgmt-components) [Setting up traffic management](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management) [ Setting up URL redirects](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#url-redirect) [ Setting up HTTP-to_HTTPS redirects](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect) [Cookies](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#http-cookie) [Hostname and path](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps)  
Cloud Service Mesh | [Cloud Service Mesh features: Routing and traffic management](https://docs.cloud.google.com/service-mesh/docs/features#load_balancing) [Advanced traffic management overview](https://docs.cloud.google.com/service-mesh/docs/advanced-traffic-management) [Configuring advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/configure-advanced-traffic-management)  
  
## API and gcloud CLI reference

In addition to the Google Cloud console, you can use the API and gcloud CLI to create URL maps.

### API

For descriptions of the properties and methods available to you when working with URL maps through the REST API, see the following:

Product | API documentation  
---|---  
External Application Load Balancer | [urlMaps](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps)  
Internal Application Load Balancer | [regionUrlMaps](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps)  
Cloud Service Mesh | [urlMaps](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps)  
**Note:** In the URL map API, `HttpRouteRuleMatch` means an instance of `pathMatchers[].routeRules[].matchRules[]`.

### gcloud CLI

For the Google Cloud CLI in the Google Cloud CLI, see the following:

  * [gcloud compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps)


  * Global: `--global`


  * Regional: `--region=[REGION]`



For advanced traffic management, use YAML files and import them with the [`gcloud compute url-maps import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/import) command.

## What's next

  * See [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) for information on how URL maps work.
  * See [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https) for information on how URL maps work in external Application Load Balancers.
  * See [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal) for information on how URL maps work in internal Application Load Balancers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
