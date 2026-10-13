---
url: https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check/
title: Performing health checks \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:54.734082+00:00
---

# Performing health checks  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Performing health checks Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee supports two health check approaches. The right one for you depends on how client traffic reaches Apigee. 

  * **Active health check:** For architectures that route client traffic to Apigee through a Google Cloud load balancer backed by a managed instance group (MIG). The load balancer (or your client) actively probes one of the `/healthz/*` endpoints to determine instance / environment health, and the load balancer fails over between regions. If your architecture uses MIGs, continue to use active health check. 
  * **PSC health check:** For architectures that route client traffic to Apigee through Private Service Connect (PSC). Apigee monitors the regional instances for you and updates the per-region health state automatically. No client- or load-balancer-initiated probes are required. If your architecture uses PSC, opt in to PSC health check. 



Select a tab to learn more. 

### Active health check

Apigee exposes active health checks at different levels, which you can leverage depending upon the use case. 

  1. **Regional-level / Apigee instance health check:** Returns the health of overall Apigee instance in a region.
  2. **Environment-level health checks:** Returns the health of a particular environment in the Apigee instance.
  3. **Custom health check through an API proxy:** For complex use cases, you can configure a dedicated API proxy as a custom health check endpoint.



#### Performing a regional-level health check

Apigee offers a regional-level / Apigee instance health check to assess the overall health status of the Apigee instance in a specific region. This health check pattern, widely used by load balancers, determines the health status of Apigee instances and performs regional failovers. You can perform a regional-level health check by constructing the request as follows: 

  * Health check path: `/healthz/ingress`
  * Add request header: `User-Agent: GoogleHC`.


    
    
    $ curl -H 'User-Agent: GoogleHC' https://$HOST/healthz/ingress
    Apigee Ingress is healthy

where, `$HOST` represents the host name defined in the [Apigee environment group](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with) that is served by the load balancer.  Note: This API call to determine the regional-level health check will not be counted against your overall Apigee usage. If the Apigee instance is healthy, the response `"HTTP/2 200"` with `"Apigee Ingress is healthy"` is returned. 

#### Performing an environment-level health check

Apigee offers an environment-level health check to assess the health of a particular environment served by the Apigee instance. This health check pattern is preferred when you want to perform regional failovers based on the health of certain critical/selective environments. You can perform an environment-level health check by calling any valid API proxy in an environment by constructing the request as follows: 

  * Prepend `/healthz/` to the proxy basepath.
  * Add request header: `User-Agent: GoogleHC`.



For example, assume that `/catalog` is a valid proxy basepath that is deployed in an environment. To do a health check, call the proxy like this: 
    
    
    $ curl -H 'User-Agent: GoogleHC' https://$HOST/healthz/catalog
    Server Ready

where, `$HOST` represents the host name defined in the [Apigee environment group](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with) that is served by the load balancer.  Note: This proxy API call to determine the environment-level health check will not execute the proxy, and will not be counted against your overall Apigee usage. The basepath `/catalog` is used only for routing the API to the correct environment. If the environment is healthy, the response `"HTTP/2 200"` with `"Server Ready"` is returned. 

#### Performing a custom health check through an API proxy

If you want to perform any additional validations, you can define custom health check logic in an API proxy deployed to an environment. For example, you might fail the healthcheck when multiple environments are down. Or, you could fail the healthcheck based on target health or latency. 

In this case, you can perform the health check by making a regular API call to that proxy. 

For example, assume that you want to check the health of an environment called `prod`. Deploy an API proxy to that environment with the basepath `/healthcheck-prod`. To check the health of the `prod` environment served by Apigee instance, call the proxy like this: 
    
    
    $ curl https://$HOST/healthcheck-prod

where, `$HOST` represents the host name defined in the [Apigee environment group](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with) that is served by the load balancer.  Note: The API calls with custom health checks will be counted against your overall Apigee usage. And, you don't need to provide the `"User-Agent"` header. 

#### Usage notes

**For regional-level and environment-level healthchecks:** If they are performed by the [Google Cloud load balancers](https://cloud.google.com/load-balancing/docs/choosing-load-balancer#summary-of-google-cloud-load-balancers), the load balancer sets the correct `User-Agent` header. If your own client consumes these health check API calls, you need to make sure the correct `User-Agent` is set. 

**For Apigee hybrid** : The health check feature is only available for version 1.4 and higher. 

### PSC health check

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Apigee supports health checking with Private Service Connect (PSC), enabling automatic cross-region failover for multi-region deployments. If you have multiple Apigee instances across multiple regions, you can opt in to PSC health checks so that traffic automatically fails over to a healthy region when the Apigee instance in the active region becomes unhealthy. No request from your client or load balancer is required to trigger the check. Google Cloud monitors the instance continuously on your behalf and updates the health state automatically. 

The PSC health check feature is configured on the Apigee backend. You do not need to deploy any additional resources, write any code, or change your API proxies. 

#### Prerequisites

  * You have an Apigee Pay-as-you-go or Subscription organization.
  * Your organization has two or more Apigee instances, each in a different Google Cloud region.
  * Your client traffic reaches Apigee through Private Service Connect (PSC).
  * Every environment, environment group, API proxy, shared flow, and resource is deployed identically across all Apigee instances that participate in failover. Inconsistent deployments can cause unexpected behavior when traffic shifts between regions.



#### How to enable

PSC health check is an opt-in feature managed by Google. To request enablement for your organization, contact your Apigee account team or [Apigee Support](https://docs.apigee.com/api-platform/troubleshoot/support). If enabled, automatic regional failover is active for all instances in your organization. No further configuration is required. 

#### Testing recommendations

Because PSC health check introduces immediate, automatic regional failover that directly affects traffic routing, we recommend that you test the feature in a non-production Apigee environment before enabling it for your production organization. Verify that failover and recovery behave as expected for your API traffic patterns and that your client applications handle the transition transparently. 

To simulate a failover scenario and validate your setup, contact your Apigee account team or [Apigee Support](https://docs.apigee.com/api-platform/troubleshoot/support). The team can assist you in inducing failure conditions in a controlled environment so that you can observe the failover behavior before enabling the feature in production. 

#### How failover works

When PSC health check determines that the Apigee instance in your active region is unhealthy, client traffic is immediately and automatically routed to a healthy Apigee instance in another region. When the unhealthy instance recovers, traffic returns to the original region. The failover and recovery happen transparently to your client applications. 

**Important:** Failover is immediate and automatic once PSC health check is enabled. There is no configurable delay or toggle to control failover timing. If the Apigee instance in a region becomes unhealthy, the Google Cloud load balancer stops routing traffic to that region without additional intervention. Ensure that your architecture supports cross-region traffic routing before opting in. 

#### Current limitations

  * PSC health check currently detects only complete regional infrastructure outages. It does not trigger on incidents where traffic can still flow, even if the traffic is degraded in error rates or latency. Broader component-level health checking is planned for a future release.



#### Verifying health state in Cloud Logging

You can observe the per-region health status events for your Apigee instances in [Cloud Logging](https://cloud.google.com/logging/docs/view/logs-explorer-interface). In the Logs Explorer for the Google Cloud project that hosts your Apigee organization, run the following filter: 
    
    
    resource.type="compute.googleapis.com/NetworkEndpointGroupV2"

For more information, see [Monitor composite health check logs](https://docs.cloud.google.com/vpc/docs/monitor-composite-health#logs). 

For each region, look at the `healthState` field on the matching log entries. A value of `HEALTHY` indicates that the Apigee instance in that region is reachable and serving traffic. Other values indicate that PSC health check is not currently routing traffic to that region. 

Note: PSC health check does not consume any of your Apigee API call quota and is not counted against your overall Apigee usage. For details, see the [composite health check limitations documentation](https://docs.cloud.google.com/vpc/docs/about-composite-health#limitations) and the [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
