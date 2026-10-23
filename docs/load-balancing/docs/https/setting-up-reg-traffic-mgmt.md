---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt/
title: Set up traffic management for regional external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:37.109756+00:00
---

# Set up traffic management for regional external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up traffic management for regional external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This document shows examples of using traffic management for some specific use cases. Many other use cases are possible.

The document contains examples for the following load balancers:

  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer
  * Cross-region internal Application Load Balancer



**Regional external Application Load Balancer versus regional internal Application Load Balancer.** For the regional load balancers' traffic management configuration, the [regional URL map API ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps) and the [ regional backend service API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices) documentation provides a full list of fields, including semantics regarding relationships, restrictions, and cardinality.

The only difference between these two load balancers is the load balancing scheme, as follows:

  * Regional external Application Load Balancers use `EXTERNAL_MANAGED`.
  * Regional internal Application Load Balancers use `INTERNAL_MANAGED`.



**Regional internal Application Load Balancer versus cross-region internal Application Load Balancer.** For the traffic management configuration:

  * Regional internal Application Load Balancers use the [regional URL map API ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps), and the [ regional backend service API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices) documentation provides a full list of fields, including semantics regarding relationships, restrictions, and cardinality.

  * Cross-region internal Application Load Balancers use [global URL map API ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps), and [ global backend service API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) documentation provides a full list of fields, including semantics regarding relationships, restrictions, and cardinality.


**Note:** For cross-region internal Application Load Balancers, you can use the examples provided in this document by replacing `regions/REGION/backendServices` with `global/backendServices`. 

In addition to the advanced routing features described on this page, [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) integrate with Service Extensions to let you [insert custom logic](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb) into the load balancing data path.

## Before you begin

Make sure that you understand how traffic management works. For more information, read [Traffic management overview for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional).

## Configure traffic management

Within your chosen configuration environment, you set up traffic management by using YAML configurations. A URL map and a backend service each has its own YAML file. Depending on your desired functionality, you need to write either a URL map YAML file, a backend service YAML file, or both.

For help writing these YAML files, you can use the examples on this page and the Cloud Load Balancing API documentation.

The Google Cloud console is not supported. 

For regional internal Application Load Balancers and regional external Application Load Balancers, the [regional URL map API ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps) and the [ regional backend service API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices) documentation provides a full list of fields, including semantics regarding relationships, restrictions, and cardinality.

### Use the YAML examples in the Google Cloud console

To use YAML examples in the Google Cloud console:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click **Create load balancer**.
  3. Complete the steps of the wizard to create a regional external Application Load Balancer.
  4. In the **Routing rules** configuration, select **Advanced host and path rule**.
  5. Click **Add host and path rule**. 
  6. Do one of the following:
     * In the **Path matcher** box, paste the YAML examples from this document.
     * Click the **Code guidance** link.
The **Path matcher YAML examples** page appears. You can paste examples from the **Path matcher YAML examples** page to the **Path matcher** box.
  7. Click **Done**.



## Map traffic to a single service

Send all traffic to a single service. Make sure to replace the placeholders.
    
    
        defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
        hostRules:
        - hosts:
          - '*'
          pathMatcher: matcher1
        name: URL_MAP_NAME
        pathMatchers:
        - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
          name: matcher1
          routeRules:
            - matchRules:
                - prefixMatch: /PREFIX
              priority: 1
              routeAction:
                weightedBackendServices:
                  - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                    weight: 100
    

## Split traffic between two services

Split traffic between two or among multiple services. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       name: URL_MAP_NAME
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
         - matchRules:
           - prefixMatch: /PREFIX
           priority: 2
           routeAction:
             weightedBackendServices:
             - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
               weight: 95
             - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_2
               weight: 5
    

## Configure a URL redirect

The following example returns a configurable 3xx response code. The example also sets the `Location` response header with the appropriate URI, replacing the host and path as specified in the redirect action.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: URL_MAP_NAME
       hostRules:
       - hosts:
         - "HOST TO REDIRECT FROM" # Use * for all hosts
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         defaultUrlRedirect:
           hostRedirect: "HOST TO REDIRECT TO" # Omit to keep the requested host
           pathRedirect: "PATH TO REDIRECT TO" # Omit to keep the requested path
           redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
           stripQuery: True
    

## Mirror traffic

In addition to forwarding the request to the selected backend service, you can send an identical request to the configured mirror backend service on a _fire and forget_ basis. This means that the load balancer doesn't wait for a response from the backend to which it sends the mirrored request. Request mirroring is useful for testing a new version of a backend service. You can also use it to debug production errors on a debug version of your backend service, rather than on the production version.

By default, the mirrored backend service receives _all_ requests, even if the original traffic is being split between multiple weighted backend services. You can configure the mirrored backend service to receive only a percentage of the requests by using the optional `mirrorPercent` flag to specify the percentage of requests to be mirrored expressed as a value between 0 and 100.0.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: 1
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               requestMirrorPolicy:
                 backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_2
                 mirrorPercent: 50.0
    

Note the following limitations when using traffic mirroring:

  * Traffic mirroring is supported when both backend services have managed instance groups, zonal NEGs, or hybrid NEGs backends. It is not supported for internet NEGs, serverless NEGs, and Private Service Connect backends.
  * Requests to the mirrored backend service do not generate any logs or metrics for Cloud Logging and Cloud Monitoring. 



## Rewrite the requested URL

Rewrite the hostname portion of the URL, the path portion of the URL, or both, before sending a request to the selected backend service. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               urlRewrite:
                 hostRewrite: "new-host-name.com" # Omit to keep the requested host
                 pathPrefixRewrite: "/new-path/" # Omit to keep the requested path
    

**Note:** The `pathPrefixRewrite` route action is best suited for use with `prefixMatch` rules where it can effectively modify the matched prefix only. We don't recommend using `fullPathMatch` rules with `pathPrefixRewrite`. 

## Retry a request

Configure the conditions under which the load balancer retries failed requests, how long the load balancer waits before retrying, and the maximum number of retries permitted.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               retryPolicy:
                 retryConditions: 502, 504
                 numRetries: 3
                 perTryTimeout:
                   seconds: 1
                   nanos: 500000000
    

## Specify the route timeout

Specify the timeout for the selected route. Timeout is computed from the time the request is fully processed until the response is fully processed. Timeout includes all retries. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               timeout:
                 seconds: 30
                 nanos: 500000000
    

## Configure fault injection

Introduce errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               faultInjectionPolicy:
                 delay:
                   fixedDelay:
                     seconds: 10
                     nanos: 500000000
                   percentage: 25
                 abort:
                   httpStatus: 503
                   percentage: 50
    

## Configure CORS

Configure cross-origin resource sharing (CORS) policies to handle settings for enforcing CORS requests.
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
               corsPolicy:
                   allowOrigins: my-domain.com
                   allowMethods: GET, POST
                   allowHeaders: Authorization, Content-Type
                   maxAge: 1200
                   allowCredentials: True
    

## Add and remove request and response headers

Add and remove request headers before sending a request to the backend service. Also add and remove response headers after receiving a response from the backend service.

Regional external Application Load Balancers and internal Application Load Balancers also support the use of variables in custom headers. You can specify one or more variables in the custom header value (`headerValue`) fields that are then translated to their corresponding per-request values. For a list of supported header values, see [Create custom headers in URL maps](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-regional).
    
    
       defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
       name: regional-lb-map
       region: region/REGION
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
                   weight: 100
                   headerAction:
                     requestHeadersToAdd:
                     - headerName: header-1-name
                       headerValue: header-1-value
                       replace: True
                     requestHeadersToRemove:
                     - header-2-name
                     - header-3-name
                     responseHeadersToAdd:
                     - headerName: header-4-name
                       headerValue: header-4-value
                       replace: True
                    responseHeadersToRemove:
                    - header-5-name
                    - header-6-name
    

## Configure outlier detection

Specify the criteria for eviction of unhealthy backend VMs or endpoints in NEGs, along with criteria defining when a backend or endpoint is considered healthy enough to receive traffic again. Make sure to replace the placeholders.
    
    
        loadBalancingScheme: LOAD_BALANCING_SCHEME
        localityLbPolicy: RANDOM
        name: projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE_1
        outlierDetection:
          baseEjectionTime:
            nanos: 0
            seconds: '30'
          consecutiveErrors: 5
          consecutiveGatewayFailure: 3
          enforcingConsecutiveErrors: 2
          enforcingConsecutiveGatewayFailure: 100
          enforcingSuccessRate: 100
          interval:
            nanos: 0
            seconds: '1'
          maxEjectionPercent: 50
          successRateMinimumHosts: 5
          successRateRequestVolume: 100
          successRateStdevFactor: 1900
        region: region/REGION
    

## Configure circuit breaking

Circuit breaking lets you set failure thresholds to prevent client requests from overloading your backends. After requests reach a limit that you've set, the load balancer stops allowing new connections or sending additional requests, giving your backends time to recover. Thus, circuit breaking prevents cascading failures by returning an error to the client rather than overloading a backend. This allows some traffic to be served while providing time for managing the overload situation, such as handling a traffic spike by increasing capacity through autoscaling.

Set upper limits on requests per connection as well as the volume of connections to a backend service. Also limit the number of pending requests and retries.
    
    
        loadBalancingScheme: LOAD_BALANCING_SCHEME # EXTERNAL_MANAGED or INTERNAL_MANAGED
        localityLbPolicy: RANDOM
        affinityCookieTtlSec: 0
        backends:
        - balancingMode: UTILIZATION
          capacityScaler: 1.0
          group: region/REGION/instanceGroups/INSTANCE_GROUP
          maxUtilization: 0.8
        circuitBreakers:
          maxConnections: 1000
          maxPendingRequests: 200
          maxRequests: 1000
          maxRequestsPerConnection: 100
          maxRetries: 3
        connectionDraining:
          drainingTimeoutSec: 0
        healthChecks:
        - region/REGION/healthChecks/HEALTH_CHECK
    

## Set up traffic splitting: detailed steps

This example demonstrates the following steps:

  1. Create distinct templates for different services.

  2. Create instance groups for those templates.

  3. Create routing rules that set up 95% / 5% traffic splitting.

  4. Send curl commands showing that the traffic split percentages roughly match the configuration.




These instructions assume the following:

  * The region is `us-west1`.
  * A target proxy and forwarding rule have been created, along with a URL map named `regional-lb-map`.

  * The URL map sends all traffic to one backend service, called `red-service`, which is the default backend service.

  * You set up an alternate path that sends 5% of the traffic to `blue-service` and 95% of traffic to `green-service`.

  * A path matcher is used.

  * You are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.




### Define the services

The following bash function creates a backend service, including the instance template and the managed instance group.

These instructions assume that an HTTP health check (`regional-lb-basic-check`) has been created. For instructions, see [Set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb). 
    
    
    function make_service() {
      local name="$1"
      local region="$2"
      local zone="$3"
      local network="$4"
      local subnet="$5"
      local subdir="$6"
    
      www_dir="/var/www/html/$subdir"
    
      (set -x; \
      gcloud compute instance-templates create "${name}-template" \
        --region="$region" \
        --network="$network" \
        --subnet="$subnet" \
        --tags=allow-ssh,load-balanced-backend \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --metadata=startup-script="#! /bin/bash
      apt-get update
      apt-get install apache2 -y
      a2ensite default-ssl
      a2enmod ssl
      sudo mkdir -p $www_dir
      /bin/hostname | sudo tee ${www_dir}index.html
      systemctl restart apache2"; \
      gcloud compute instance-groups managed create \
        "${name}-instance-group" \
        --zone="$zone" \
        --size=2 \
        --template="${name}-template"; \
      gcloud compute backend-services create "${name}-service" \
        --load-balancing-scheme=LOAD_BALANCING_SCHEME\
        --protocol=HTTP \
        --health-checks=regional-lb-basic-check \
        --health-checks-region="$region" \
        --region="$region"; \
      gcloud compute backend-services add-backend "${name}-service" \
        --balancing-mode='UTILIZATION' \
        --instance-group="${name}-instance-group" \
        --instance-group-zone="$zone" \
        --region="$region")
    }
    

### Create the services

Call the function to make three services, `red`, `green`, and `blue`. The `red` service acts as the default service for requests to `/`. The `green` and `blue` services are both set up on `/PREFIX` to handle 95% and 5% of the traffic, respectively.
    
    
    make_service red us-west1 us-west1-a lb-network backend-subnet ""
    make_service green us-west1 us-west1-a lb-network backend-subnet /PREFIX
    make_service blue us-west1 us-west1-a lb-network backend-subnet /PREFIX
    

### Create the URL map

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add)

  2. Click the **regional-lb-map** link.

  3. Click **Edit** edit .




### Configure the new routing rules

  1. Under **Routing rules** , select **Advanced host and path rule**.
  2. Under **Hosts and path rule** , to create the default action, set the **Service** to `red-service`.
  3. Click **Done**.
  4. Click **Add host and path rule**.
  5. In the **Hosts** field, enter the IP address of your load balancer's forwarding rule.
  6. Paste the following YAML content into the **Path matcher** box:
         
         defaultService: projects/PROJECT_ID/regions/us-west1/backendServices/red-service
         name: matcher1
         routeRules:
         - priority: 2
           matchRules:
             - prefixMatch: /PREFIX
           routeAction:
             weightedBackendServices:
               - backendService: projects/PROJECT_ID/regions/us-west1/backendServices/green-service
                 weight: 95
               - backendService: projects/PROJECT_ID/regions/us-west1/backendServices/blue-service
                 weight: 5
         

  7. Click **Done**.

  8. Click **Update**.




###  gcloud 

  1. Export the existing URL map using the [`gcloud compute url-maps export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command:
         
         gcloud compute url-maps export regional-lb-map \
           --destination=regional-lb-map-config.yaml \
           --region=us-west1
         

  2. Update the URL map file `regional-lb-map-config.yaml` by adding this to the end of the file:
         
         hostRules:
         - hosts:
           - '*'
           pathMatcher: matcher1
         pathMatchers:
         - defaultService: projects/PROJECT_ID/regions/us-west1/backendServices/red-service
           name: matcher1
           routeRules:
           - priority: 2
             matchRules:
               - prefixMatch: /PREFIX
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/regions/us-west1/backendServices/green-service
                   weight: 95
                 - backendService: projects/PROJECT_ID/regions/us-west1/backendServices/blue-service
                   weight: 5
         

  3. Update the URL map using the [`gcloud compute url-maps import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/import) command:
         
         gcloud compute url-maps import regional-lb-map \
            --region=us-west1 \
            --source=regional-lb-map-config.yaml
         




### Test the configuration

To test the configuration, first ensure that requests to the load balancer's IP address set up earlier are handled by the default `red` configuration.

Then check to make sure that requests sent to `FORWARDING_RULE_IP_ADDRESS/PREFIX` are split as expected.

## Set up session affinity based on `HTTP_COOKIE`

Traffic control enables you to configure session affinity based on a provided cookie. To configure HTTP_COOKIE based session affinity for a backend service named `red-service`, follow these directions.

  1. Use the [`gcloud compute backend-services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command to get the backend service configuration.
         
         gcloud compute backend-services export red-service \
             --destination=red-service-config.yaml \
             --region=us-west1
         

  2. Update the `red-service-config.yaml` file as follows:
         
         sessionAffinity: 'HTTP_COOKIE'
         localityLbPolicy: 'RING_HASH'
         consistentHash:
          httpCookie:
           name: 'http_cookie'
           path: '/cookie_path'
           ttl:
             seconds: 100
             nanos: 500000000
          minimumRingSize: 10000
         

  3. In the `red-service-config.yaml` file, delete the following line:
         
         sessionAffinity: NONE
         

  4. Update the backend service configuration file:
         
         gcloud compute backend-services import red-service \
             --source=red-service-config.yaml \
             --region=us-west1
         




## Troubleshooting

Use this information for troubleshooting when traffic is not being routed according to the route rules and traffic policies that you configured.

For information about logging and monitoring, see [External HTTP(S) logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring). 

Symptoms:

  * Increased traffic to services in rules above the rule in question.
  * An unexpected increase in 4xx and 5xx HTTP responses for a given route rule.



Solution: Check the order of your route rules. Route rules are interpreted in the order in which they are specified.

Route rules within a URL map are interpreted in the order in which they are specified. This is different from the way that path rules are interpreted by longest prefix match. For a path rule, internal Application Load Balancers will only select a single path rule; however, when you use route rules, more than one might apply.

When you define route rules, check to be sure that rules at the top of the list don't inadvertently route traffic that would otherwise have been routed by a subsequent route rule. The service that receives misdirected traffic would likely reject requests, and the service in your route rules would receive reduced traffic or no traffic at all.

## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
