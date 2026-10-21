---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management/
title: Configure advanced traffic management with Envoy \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:35.664428+00:00
---

# Configure advanced traffic management with Envoy  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure advanced traffic management with Envoy

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

The configuration is supported for Preview customers but we don't recommended it for new Cloud Service Mesh users. For more information, see the [Cloud Service Mesh service routing overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview).

This document provides information about how to configure advanced traffic management for Cloud Service Mesh deployments that use Envoy.

## Before you begin

Before you configure advanced traffic management, follow the instructions in [Prepare to set up Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup), including configuring Cloud Service Mesh and any virtual machine (VM) hosts or Google Kubernetes Engine (GKE) clusters that you need. Create the required Google Cloud resources.

Advanced traffic management feature availability differs according to the request protocol that you choose. This protocol is configured when you configure routing by using the target HTTP or HTTPS proxy, target gRPC proxy, or target TCP proxy resource:

  * With the target HTTP proxy and target HTTPS proxy, all the features described in this document are available.
  * With the target gRPC proxy, some features are available.
  * With the target TCP proxy, no advanced traffic management features are available.



For more information, see [Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/docs/service-routing/features) and [Advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management). For an end-to-end setup guide, see [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).

## Set up traffic splitting

These instructions assume the following:

  * Your Cloud Service Mesh deployment has a URL map called `review-url-map`.
  * The URL map sends all traffic to one backend service called `review1`, which serves as the default backend service.
  * You plan to route 5% of traffic to a new version of a service. That service is running on a backend VM or endpoint in a network endpoint group (NEG) associated with the backend service `review2`.
  * No host rules or path matchers are used.



If you are splitting traffic to a new service that has not been referenced by the URL map before, first add the new service to `weightedBackendServices` and give it a weight of `0`. Then, gradually increase the weight assigned to that service.

To set up traffic splitting, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click **Routing rule maps**.

  3. Click add**Create routing rule map**.

  4. On the **Create a routing rule map** page, enter a **Name**.

  5. In the **Protocol** menu, select **HTTP**.

  6. Select an existing forwarding rule.

  7. Under **Routing rules** , select **Advanced host, path and route rule**.

  8. Under **Hosts and path matchers** , click add**Add hosts and path matcher**. This adds a new path matcher that you can configure to split traffic.

  9. Add the following settings to the **Path matcher** field:
         
         - defaultService: global/backendServices/review1
               name: matcher1
               routeRules:
               - priority: 2
                 matchRules:
                 - prefixMatch: ''
                 routeAction:
                  weightedBackendServices:
                  - backendService: global/backendServices/review1
                    weight: 95
                  - backendService: global/backendServices/review2
                    weight: 5
         

  10. Click **Done**.

  11. Click **Save**.




After you are satisfied with the new version, you can gradually adjust the weights of the two services and eventually send all traffic to `review2`.

###  gcloud 

  1. Run the [`gcloud export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command to get the URL map configuration:
         
         gcloud compute url-maps export review-url-map \
             --destination=review-url-map-config.yaml
         

  2. Add the following section to the `review-url-map-config.yaml` file:
         
         hostRules:
              - description: ''
               hosts:
                - '*'
              pathMatcher: matcher1
              pathMatchers:
              - defaultService: global/backendServices/review1
                name: matcher1
                routeRules:
                - priority: 2
                  matchRules:
                  - prefixMatch: ''
                  routeAction:
                   weightedBackendServices:
                   - backendService: global/backendServices/review1
                     weight: 95
                   - backendService: global/backendServices/review2
                     weight: 5
         

  3. Update the URL map:
         
         gcloud compute url-maps import review-url-map \
             --source=review-url-map-config.yaml
         




After you are satisfied with the new version, you can gradually adjust the weights of the two services and eventually send all traffic to `review2`.

## Set up a partial release

Use a partial deployment process, sometimes called _canarying_ , to release a new software version to a small fraction of servers before you release the new version to the balance of your production servers.

A partial release uses `weightedBackendServices`. To enable a partial release, designate a backend service as the test, or canary, service and give it a low weight, for example, 2 or 5. Deploy your new software version to those servers only. When you are satisfied that the new version is free of issues, deploy it to the remainder of your services.

  * To enable a partial release, use the following YAML code sample:


    
    
    pathMatchers:
         - defaultService: DEFAULT_SERVICE_URL
           name: matcher1
           routeRules:
           - matchRules:
             - prefixMatch: '/'
             routeAction:
              weightedBackendServices:
              - backendService: BACKEND_SERVICE_PARTIAL_URL
                weight: 2
              - backendService: BACKEND_SERVICE_URL
                weight: 98
    

  * `DEFAULT_SERVICE_URL` is the default URL for your service.
  * `BACKEND_SERVICE_PARTIAL_URL` is the URL for the backend service that receives 2% of traffic.
  * `BACKEND_SERVICE_URL` is the URL for the backend service that receives 98% of traffic.



## Set up blue-green deployments

Blue-green deployments are release models that reduce the time needed for switching production traffic to a new release of a service, or to a rollback of a prior release of the service. These deployments keep both versions of the service available in production and shift traffic from one to the other.

Blue-green deployments use `weightedBackendServices`. In the YAML example that follows, backends to `SERVICE_BLUE_URL` are fully deployed with the current production release and the backends to `SERVICE_GREEN_URL` are fully deployed with the new release. In the configuration in the example, the `GREEN` deployment receives 100% of the production traffic. If you find issues, you can reverse the weights for the two deployments, which effectively reverts the defective `GREEN` release and reinstates the known-good `BLUE` release. In either case, traffic can be shifted quickly because both versions are available to receive traffic.

  * To enable a blue-green deployment, use the following YAML code sample:


    
    
    pathMatchers:
         - defaultService: DEFAULT_SERVICE_URL
           name: matcher1
           routeRules:
           - matchRules:
             - prefixMatch: '/'
             routeAction:
              weightedBackendServices:
              - backendService: BACKEND_SERVICE_BLUE_URL
                weight: 0
              - backendService: BACKEND_SERVICE_GREEN_URL
                weight: 100
    

  * `DEFAULT_SERVICE_URL` is the default URL for your service.
  * `BACKEND_SERVICE_BLUE_URL` is the URL for the backend service that receives none of your traffic.
  * `BACKEND_SERVICE_GREEN_URL` is the URL for the backend service that receives 100% of your traffic.



## Set up traffic mirroring

Use traffic mirroring when you want traffic to be directed to two different backend services for the purposes of debugging or testing new services.

In the following example, all requests are sent to `SERVICE_URL` and to `MIRROR_SERVICE_URL`. Only the responses from `SERVICE_URL` are sent back to the client. `MIRROR_SERVICE_URL` has no client impact.

To set up traffic mirroring, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click **Routing rule maps**.

  3. Click add**Create routing rule map**.

  4. On the **Create a routing rule map** page, enter a **Name**.

  5. In the **Protocol** list, select **HTTP**.

  6. Select an existing forwarding rule.

  7. Under **Routing rules** , select **Advanced host, path and route rule**.

  8. Under **Hosts and path matchers** , click add**Add hosts and path matcher**. This adds a new path matcher that you can configure to mirror traffic.

  9. Add the following settings to the **Path matcher** field:
         
         - defaultService: DEFAULT_SERVICE_URL
               name: matcher1
               routeRules:
               - matchRules:
                 - prefixMatch: '/'
                 routeAction:
                  weightedBackendServices:
                  - backendService: BACKEND_SERVICE_URL
                    weight: 100
                  requestMirrorPolicy:
                    backendService: BACKEND_SERVICE_MIRROR_URL
         

     * `DEFAULT_SERVICE_URL` is the default URL for your service.
     * `BACKEND_SERVICE_URL` is the URL for the backend that is mirrored.
     * `BACKEND_SERVICE_MIRROR_URL` is the URL for the backend service that you mirror to.
  10. Click **Done**.

  11. Click **Save**.




###  gcloud 

  1. Run the [`gcloud export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command to get the URL map configuration:
         
         gcloud compute url-maps export review-url-map \
             --destination=review-url-map-config.yaml
         

  2. Add the following section to the `review-url-map-config.yaml` file:
         
         hostRules:
              - description: ''
               hosts:
                - '*'
              pathMatcher: matcher1
              pathMatchers:
             - defaultService: DEFAULT_SERVICE_URL
               name: matcher1
               routeRules:
               - matchRules:
                 - prefixMatch: '/'
                 routeAction:
                  weightedBackendServices:
                  - backendService: BACKEND_SERVICE_URL
                    weight: 100
                  requestMirrorPolicy:
                    backendService: BACKEND_SERVICE_MIRROR_URL
         

     * `DEFAULT_SERVICE_URL` is the default URL for your service.
     * `BACKEND_SERVICE_URL` is the URL for the backend that is mirrored.
     * `BACKEND_SERVICE_MIRROR_URL` is the URL for the backend service that you mirror to.
  3. Update the URL map:
         
         gcloud compute url-maps import review-url-map \
             --source=review-url-map-config.yaml
         




## Set up circuit breaking

Circuit breaking lets you set failure thresholds to prevent client requests from overloading your backends. After requests reach a limit that you set, the client stops allowing new connections or sending additional requests, giving your backends time to recover.

As a result, circuit breaking prevents cascading failures by returning an error to the client rather than overloading a backend. This lets some traffic be served while providing time for managing the overload situation, such as handling a traffic spike by increasing capacity through autoscaling.

In the following example, you set the circuit breakers as follows:

  * Maximum requests per connection: 100
  * Maximum number of connections: 1000
  * Maximum pending requests: 200
  * Maximum requests: 1000
  * Maximum retries: 3



To set up circuit breaking, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click the name of the backend service that you want to update.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Under **Circuit breakers** , select the **Enable** checkbox.

  6. Click edit**Edit**.

     1. In **Max requests per connection** , enter `100`.
     2. In **Max connections** , enter `1000`.
     3. In **Max pending requests** , enter `200`.
     4. In **Max requests** , enter `1000`.
     5. In **Max retries** , enter `3`.
  7. Click **Save** , and then click **Save** again.




###  gcloud 

  1. Run the `gcloud export` command to export the backend service configuration. Replace `BACKEND_SERVICE_NAME` with the name of the backend service.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
              --destination=BACKEND_SERVICE_NAME-config.yaml --global
         

  2. Update the `BACKEND_SERVICE_NAME`.yaml file as follows:
         
         affinityCookieTtlSec: 0
          backends:
          - balancingMode: UTILIZATION
            capacityScaler: 1.0
             group:https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroups/INSTANCE_GROUP_NAME
            maxUtilization: 0.8
          circuitBreakers:
            maxConnections: 1000
            maxPendingRequests: 200
            maxRequests: 1000
            maxRequestsPerConnection: 100
            maxRetries: 3
          connectionDraining:
            drainingTimeoutSec: 300
          healthChecks:
            - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/healthChecks/HEALTH_CHECK_NAME
          loadBalancingScheme: INTERNAL_SELF_MANAGED
          localityLbPolicy: ROUND_ROBIN
          name: BACKEND_SERVICE_NAME
          port: 80
          portName: http
          protocol: HTTP
          sessionAffinity: NONE
          timeoutSec: 30
         

  3. Update the backend service config file:
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
             --source=BACKEND_SERVICE_NAME-config.yaml --global
         




## Set up session affinity based on `HTTP_COOKIE`

Advanced traffic management enables you to configure session affinity based on a provided cookie.

To set up session affinity using `HTTP_COOKIE`, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click the name of the backend service that you want to update.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Under **Session affinity** , select **HTTP cookie**.

  6. Under **Locality Load balancing policy** , select **Ring hash**.

     1. In the **HTTP Cookie name** field, enter `http_cookie`.
     2. In the **HTTP Cookie path** field, enter `/cookie_path`.
     3. In the **HTTP Cookie TTL** field, enter `100`.
     4. In the **Minimum ring size** field, enter `10000`.
  7. Click **Save**.




###  gcloud 

  1. Run the `gcloud export` command to export the backend service configuration. Replace `BACKEND_SERVICE_NAME` with the name of the backend service.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
             --destination=BACKEND_SERVICE_NAME-config.yaml --global
         

  2. Update the `YAML` file as follows:
         
         sessionAffinity: 'HTTP_COOKIE'
         localityLbPolicy: 'RING_HASH'
         consistentHash:
         httpCookie:
           name: 'http_cookie'
           path: '/cookie_path'
           ttl:
             seconds: 100
             nanos: 30
         minimumRingSize: 10000
         

  3. Import the backend service config file:
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
             --source=BACKEND_SERVICE_NAME-config.yaml --global
         




## Set up outlier detection

Outlier detection controls the eviction of unhealthy hosts from the load-balancing pool. Cloud Service Mesh does this by using a set of policies that specify the criteria for the eviction of unhealthy backend VMs or endpoints in NEGs, along with criteria defining when a backend or endpoint is considered healthy enough to receive traffic again.

In the following example, the backend service has one instance group as its backend. The outlier detection setting specifies that outlier detection analysis is run every second. If an endpoint returns five consecutive `5xx` errors, it is ejected from load-balancing consideration for 30 seconds for the first time. The real ejection time for the same endpoint is 30 seconds times the number of times that it is ejected.

To set up outlier detection on the backend service resource, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click the name of a service.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Select the **Outlier detection** checkbox.

  6. Click edit**Edit**.

     1. Set **Consecutive errors** to `5`.
     2. Set **Interval** to `1000` milliseconds.
     3. Set **Base ejection time** to `30000` milliseconds.
  7. Click **Save** , and then click **Save** again.




###  gcloud 

  1. Run the `gcloud export` command to export the backend service configuration. Replace `BACKEND_SERVICE_NAME` with the name of the backend service.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
             --destination=BACKEND_SERVICE_NAME-config.yaml --global
         

  2. Update the `YAML` file as follows, substituting the name of the backend service for `BACKEND_SERVICE_NAME`:
         
         name: BACKEND_SERVICE_NAME
         loadBalancingScheme: INTERNAL_SELF_MANAGED
         backends:
         - balancingMode: UTILIZATION
          capacityScaler: 1.0
          group: $INSTANCE_GROUP_URL
         healthChecks:
         - $HEALTH_CHECK_URL
         port: 80
         portName: http
         protocol: HTTP
         outlierDetection:
          consecutiveErrors: 5,
          interval:
              seconds: 1,
              nanos: 0
          baseEjectionTime:
              seconds: 30,
              nanos: 0
         

  3. Import the backend service config file:
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
             --source=BACKEND_SERVICE_NAME-config.yaml --global
         




## Set the locality load-balancing policy

Use the locality load-balancing policy to choose a load-balancing algorithm based on the locality weight and priority provided by Cloud Service Mesh. For example, you can perform weighted round robin among healthy endpoints or do consistent hashing.

In the following example, the backend service has one instance group as its backend. The locality load-balancing policy is set to `RING_HASH`.

To set the locality load-balancing policy, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click the name of a service.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Under **Traffic policy** , in the **Locality load balancing policy** menu, select **Ring hash**.

  6. Click **Save**.




###  gcloud 

  1. Run the `gcloud export` command to export the backend service configuration. Replace `BACKEND_SERVICE_NAME` with the name of the backend service.
         
         gcloud compute backend-services export BACKEND_SERVICE_NAME \
             --destination=BACKEND_SERVICE_NAME-config.yaml --global
         

  2. Update the `BACKEND_SERVICE_NAME`.yaml file as follows:
         
         name: shopping-cart-service
         loadBalancingScheme: INTERNAL_SELF_MANAGED
         backends:
         - balancingMode: UTILIZATION
          capacityScaler: 1.0
          group: $INSTANCE_GROUP_URL
         healthChecks:
         - $HEALTH_CHECK_URL
         port: 80
         portName: http
         protocol: HTTP
         localityLbPolicy: RING_HASH
         

  3. Import the backend service config file:
         
         gcloud compute backend-services import BACKEND_SERVICE_NAME \
             --source=BACKEND_SERVICE_NAME-config.yaml --global
         




For more information about how the locality load-balancing policy works, see the documentation for the [backendService resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

## Set up URL redirect

These instructions assume the following:

  * Your Cloud Service Mesh deployment has a URL map called `review-url-map`.
  * The URL map sends all traffic to one backend service called `review1`, which serves as the default backend service.
  * You want to redirect traffic from one host to another.



To set up URL redirect, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. Click **Routing rule maps**.

  3. Click add**Create routing rule map**.

  4. On the **Create a routing rule map** page, enter a **Name**.

  5. In the **Protocol** menu, select **HTTP**.

  6. Select an existing forwarding rule.

  7. Under **Routing rules** , select **Advanced host, path and route rule**.

  8. Under **Hosts and path matchers** , click add**Add hosts and path matcher**. This adds a new path matcher that redirects traffic.

  9. Add the following settings to the **Path matcher** field:
         
         - defaultService: global/backendServices/review1
               name: matcher1
               routeRules:
               - matchRules:
                 - prefixMatch: ''
                 urlRedirect:
                  hostRedirect: '[REDIRECT_HOST]'
                  pathRedirect: '[REDIRECT_URL]'
                  redirectResponseCode: 'FOUND',
                 stripQuery: True
         

  10. Click **Done**.

  11. Click **Save**.




###  gcloud 

  1. Run the [`gcloud export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command to get the URL map configuration:
         
         gcloud compute url-maps export review-url-map \
             --destination=review-url-map-config.yaml
         

  2. Add the following section to the `review-url-map-config.yaml` file:
         
         hostRules:
              - description: ''
               hosts:
                - '*'
              pathMatcher: matcher1
              pathMatchers:
             - defaultService: global/backendServices/review1
               name: matcher1
               routeRules:
               - matchRules:
                 - prefixMatch: ''
                 urlRedirect:
                  hostRedirect: '[REDIRECT_HOST]'
                  pathRedirect: '[REDIRECT_URL]'
                  redirectResponseCode: 'FOUND',
                 stripQuery: True
         

  3. Update the URL map:
         
         gcloud compute url-maps import review-url-map \
             --source=review-url-map-config.yaml
         




## Set up traffic steering with URL rewrite

Traffic steering allows you to direct traffic to different backend services based on request attributes such as header values. In addition, you can configure actions such as rewriting the URL in the request before the request is directed to the backend service.

In the following example, the request is directed to `SERVICE_ANDROID_URL` if the request path prefixed with `/mobile/` and the `User-Agent` of the request contain `Android`. Before sending the request to the backend service, the URL prefix can be changed to `REWRITE_PATH_ANDROID` example, `/android/`. However, if the path is prefixed with `/mobile/` and has a `User-Agent` containing `iPhone`, traffic is directed to `SERVICE_IPHONE_URL` and the URL prefix is changed to `REWRITE_PATH_IPHONE`. All other requests that are prefixed with `/mobile/` and have a `User-Agent` with a value other than Android or iPhone are directed to `SERVICE_GENERIC_DEVICE_URL`.
    
    
    pathMatchers:
         - defaultService: [DEFAULT_SERVICE_URL]
           name: matcher1
           routeRules:
           - matchRules:
             - prefixMatch: /mobile/
               headerMatches:
               - headerName: User-Agent
                 regexMatch: .*Android.*
             service: $[SERVICE_ANDROID_URL]
             routeAction:
               urlRewrite:
                 pathPrefixRewrite: [REWRITE_PATH_ANDROID]
           - matchRules:
             - prefixMatch: /mobile/
               headerMatches:
               - headerName: User-Agent
                 regexMatch: .*iPhone.*
             service: [SERVICE_IPHONE_URL]
             routeAction:
               urlRewrite:
                 pathPrefixRewrite: [REWRITE_PATH_IPHONE]
           - matchRules:
             - prefixMatch: /mobile/
             service: [SERVICE_GENERIC_DEVICE_URL]
    

## Set up fault injection

Fault injection lets you inject either or both of a fixed delay or a forced stop, called an abort, to a particular route to test the resilience of an application.

In the example that follows, all requests are sent to `SERVICE_URL`, with a fixed delay of 10 seconds added to 100% of the requests. The client sending the requests sees that all responses are delayed by 10 seconds. Additionally, a stop fault with a `Service Unavailable` 503 response is applied to 50% of the requests. The client sees that 50% of their requests receive a 503 response. These requests don't reach the backend service at all.
    
    
    pathMatchers:
         - defaultService: [DEFAULT_SERVICE_URL]
           name: matcher1
           routeRules:
           - matchRules:
             - prefixMatch: '/'
             routeAction:
              weightedBackendServices:
              - backendService: [SERVICE_URL]
                weight: 100
              faultInjectionPolicy:
                delay:
                  fixedDelay:
                    seconds: 10
                    nanos: 0
                  percentage: 100
                abort:
                  httpStatus: 503
                  percentage: 50
    

## Set up config filtering based on `MetadataFilters` match

`MetadataFilters` are enabled with forwarding rules and `HttpRouteRuleMatch`. Use this feature to control a particular forwarding rule or route rule so that the control plane sends the forwarding rule or route rule only to proxies whose node metadata matches the metadata filter setting. If you do not specify any `MetadataFilters`, the rule is sent to all Envoy proxies.

This feature makes it easy to operate a staged deployment of a configuration. For example, create a forwarding rule named `forwarding-rule1`, which you want to be pushed only to Envoys whose node metadata contains `app: review` and `version: canary`.

**Note:** There is a limitation on importing forwarding rules. For more information, see [Advanced traffic management limitations](https://docs.cloud.google.com/service-mesh/docs/service-routing/limitations#advanced-traffic-management) in the Cloud Service Mesh limitations document.

To add `MetadataFilters` to a forwarding rule, follow these steps:

###  gcloud 

  1. Run the `gcloud export` command to get the forwarding rule config:
         
         gcloud compute forwarding-rules export forwarding-rule1 \
             --destination=forwarding-rule1-config.yaml \
             --global
         

  2. Delete the forwarding rule:
         
         gcloud compute forwarding-rules delete forwarding-rule1 \
             --global
         

  3. Update the `forwarding-rule1-config.yaml` file.

The following example creates a `MATCH_ALL` metadata filter:
         
         metadataFilters:
          - filterMatchCriteria: 'MATCH_ALL'
            filterLabels:
            - name: 'app'
              value: 'review'
            - name: 'version'
              value: 'canary'
         

The following example creates a `MATCH_ANY` metadata filter:
         
         metadataFilters:
          - filterMatchCriteria: 'MATCH_ANY'
            filterLabels:
            - name: 'app'
              value: 'review'
            - name: 'version'
              value: 'production'
         

  4. Remove all output-only fields from the `forwarding-rule1-config.yaml` file. For more information, see the documentation for [`gcloud compute forwarding-rules import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/import).

  5. Run the `gcloud import` command to update the `forwarding-rule1-config.yaml` file:
         
         gcloud compute forwarding-rules import forwarding-rule1 \
             --source=forwarding-rule1-config.yaml \
             --global
         

  6. Use these instructions to add node metadata to Envoy before starting Envoy. Only a string value is supported.

a. For a VM-based deployment, in `bootstrap_template.yaml`, add the following under the `metadata` section:
         
         app: 'review'
            version: 'canary'
         

b. For a Google Kubernetes Engine-based or Kubernetes-based deployment, in `trafficdirector_istio_sidecar.yaml`, add the following under the `env` section:
         
         - name: ISTIO_META_app
              value: 'review'
            - name: ISTIO_META_version
              value: 'canary'
         




### Metadata filtering examples

Use the following instructions for a scenario in which multiple projects are in the same Shared VPC network and you want each service project's Cloud Service Mesh resources to be visible to proxies in the same project.

The Shared VPC setup is as follows:

  * Host project name: `vpc-host-project`
  * Service projects: `project1`, `project2`
  * Backend services with backend instances or endpoints running an xDS compliant proxy in `project1` and `project2`



To configure Cloud Service Mesh to isolate `project1`, follow these steps:

###  gcloud 

  1. Create all forwarding rules in `project1` with the following metadata filter:
         
         metadataFilters:
              - filterMatchCriteria: 'MATCH_ALL'
                filterLabels
                - name: 'project_name'
                  value: 'project1'
                - name: 'version'
                  value: 'production'
         

  2. When you configure the proxies deployed to instances or endpoints in `project1`, include the following metadata in the node metadata section of the bootstrap file:
         
         project_name: 'project1'
            version: 'production'
         

  3. Verify that the proxies already deployed in `project2` did not receive the forwarding rule created in the first step. To do this, try to access services in `project1` from a system running a proxy in `project2`. For information about verifying that a Cloud Service Mesh configuration is functioning correctly, see [Verifying the configuration](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-gce-vms#verifying_the_configuration).




To test a new configuration on a subset of proxies before you make it available to all proxies, follow these steps:

###  gcloud 

  1. Start the proxies that you are using for testing with the following node metadata. Do not include this node metadata for proxies that you are not using for testing.
         
         version: 'test'
         

  2. For each new forwarding rule that you want to test, include the following metadata filter:
         
         metadataFilters:
           - filterMatchCriteria: 'MATCH_ALL'
             filterLabels:
             - name: 'version'
               value: 'test'
         

  3. Test the new configuration by sending traffic to the test proxies, and make any necessary changes. If the new configuration is working correctly, only the proxies that you test receive the new configuration. The remaining proxies do not receive the new configuration and are not able to use it.

  4. When you confirm that the new configuration works correctly, remove the metadata filter associated with it. This lets all proxies receive the new configuration.




## Troubleshooting

Use this information to troubleshoot when traffic is not being routed according to the route rules and traffic policies that you configured.

Symptoms:

  * Increased traffic to services in rules above the rule in question.
  * An unexpected increase in `4xx` and `5xx` HTTP responses for a given route rule.



Solution: Because route rules are interpreted in priority order, review the priority assigned to each rule.

When you define route rules, check to be sure that rules with higher priority (that is, with lower priority numbers) do not inadvertently route traffic that would otherwise have been routed by a subsequent route rule. Consider the following example:

  * First route rule

    * Route rule match pathPrefix = `/shopping/`
    * Redirect action: send traffic to backend service `service-1`
    * Rule priority: `4`
  * Second route rule

    * Route rule match regexMatch = `/shopping/cart/ordering/.*`
    * Redirect action: send traffic to backend service `service-2`
    * Rule priority: `8`



In this case, a request with the path `/shopping/cart/ordering/cart.html` is routed to `service-1`. Even though the second rule would have matched, it is ignored because the first rule had priority.

## Block traffic between services

If you want to block traffic between Service A and Service B, and your deployment is on GKE, set up service security and use an authorization policy to block traffic between services. For complete instructions, see [Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/docs/security-overview) and the setup instructions with [Envoy](https://docs.cloud.google.com/service-mesh/docs/security-envoy-setup) and [proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/security-proxyless-setup).

## What's next

  * To help you resolve Cloud Service Mesh configuration issues, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
