---
url: https://docs.cloud.google.com/load-balancing/docs/custom-constraints/
title: Manage Cloud Load Balancing resources using custom constraints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:47.679367+00:00
---

# Manage Cloud Load Balancing resources using custom constraints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Manage Cloud Load Balancing resources using custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `compute.googleapis.com/BackendBucket`
  * `compute.googleapis.com/BackendService`
  * `compute.googleapis.com/ForwardingRule`
  * `compute.googleapis.com/HealthCheck`
  * `compute.googleapis.com/NetworkEndpointGroup`
  * `networkservices.googleapis.com/ServiceLbPolicy`
  * `compute.googleapis.com/SslPolicy`
  * `compute.googleapis.com/TargetInstance`
  * `compute.googleapis.com/TargetPool`
  * `compute.googleapis.com/TargetTcpProxy`
  * `compute.googleapis.com/TargetSslProxy`
  * `compute.googleapis.com/TargetHttpProxy`
  * `compute.googleapis.com/TargetHttpsProxy`
  * `compute.googleapis.com/TargetGrpcProxy`
  * `compute.googleapis.com/UrlMap`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

### Benefits

  * Cost management: use custom organization policies to restrict the health check probe frequency.
  * Security, compliance, and governance: you can use custom organization policies to enforce policies. For example:

    * To enforce the usage of specific health check protocols or port ranges
    * To disallow certain backend traffic protocols
    * To require that backend buckets have Cloud CDN enabled
    * To require forwarding rules to use specific Network Service Tiers



## Limitations

  * Legacy health checks ([Legacy global (HTTP)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks) and [Legacy global (HTTPS)](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks)) are not supported.

  * For Compute Engine SSL policy resources, custom constraints are also enforced on the `UPDATE` method.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cloud Load Balancing supported resources

For Cloud Load Balancing, you can set custom constraints on the following resources and fields. 

Resource | Field  
---|---  
compute.googleapis.com/BackendBucket |  `resource.bucketName`  
`resource.cdnPolicy.bypassCacheOnRequestHeaders.headerName`  
`resource.cdnPolicy.cacheKeyPolicy.includeHttpHeaders`  
`resource.cdnPolicy.cacheKeyPolicy.queryStringWhitelist`  
`resource.cdnPolicy.cacheMode`  
`resource.cdnPolicy.clientTtl`  
`resource.cdnPolicy.defaultTtl`  
`resource.cdnPolicy.maxTtl`  
`resource.cdnPolicy.negativeCaching`  
`resource.cdnPolicy.negativeCachingPolicy.code`  
`resource.cdnPolicy.negativeCachingPolicy.ttl`  
`resource.cdnPolicy.requestCoalescing`  
`resource.cdnPolicy.serveWhileStale`  
`resource.cdnPolicy.signedUrlCacheMaxAgeSec`  
`resource.compressionMode`  
`resource.customResponseHeaders`  
`resource.description`  
`resource.enableCdn`  
`resource.loadBalancingScheme`  
`resource.name`  
compute.googleapis.com/BackendService |  `resource.affinityCookieTtlSec`  
`resource.backends.balancingMode`  
`resource.backends.capacityScaler`  
`resource.backends.description`  
`resource.backends.failover`  
`resource.backends.maxConnections`  
`resource.backends.maxConnectionsPerEndpoint`  
`resource.backends.maxConnectionsPerInstance`  
`resource.backends.maxRate`  
`resource.backends.maxRatePerEndpoint`  
`resource.backends.maxRatePerInstance`  
`resource.backends.maxSessions`  
`resource.backends.maxSessionsPerEndpoint`  
`resource.backends.maxSessionsPerInstance`  
`resource.backends.maxUtilization`  
`resource.backends.preference`  
`resource.backends.trafficDuration`  
`resource.cdnPolicy.bypassCacheOnRequestHeaders.headerName`  
`resource.cdnPolicy.cacheKeyPolicy.includeHost`  
`resource.cdnPolicy.cacheKeyPolicy.includeHttpHeaders`  
`resource.cdnPolicy.cacheKeyPolicy.includeNamedCookies`  
`resource.cdnPolicy.cacheKeyPolicy.includeProtocol`  
`resource.cdnPolicy.cacheKeyPolicy.includeQueryString`  
`resource.cdnPolicy.cacheKeyPolicy.queryStringBlacklist`  
`resource.cdnPolicy.cacheKeyPolicy.queryStringWhitelist`  
`resource.cdnPolicy.cacheMode`  
`resource.cdnPolicy.clientTtl`  
`resource.cdnPolicy.defaultTtl`  
`resource.cdnPolicy.maxTtl`  
`resource.cdnPolicy.negativeCaching`  
`resource.cdnPolicy.negativeCachingPolicy.code`  
`resource.cdnPolicy.negativeCachingPolicy.ttl`  
`resource.cdnPolicy.requestCoalescing`  
`resource.cdnPolicy.serveWhileStale`  
`resource.cdnPolicy.signedUrlCacheMaxAgeSec`  
`resource.circuitBreakers.maxConnections`  
`resource.circuitBreakers.maxPendingRequests`  
`resource.circuitBreakers.maxRequests`  
`resource.circuitBreakers.maxRequestsPerConnection`  
`resource.circuitBreakers.maxRetries`  
`resource.compressionMode`  
`resource.connectionDraining.drainingTimeoutSec`  
`resource.connectionTrackingPolicy.connectionPersistenceOnUnhealthyBackends`  
`resource.connectionTrackingPolicy.enableStrongAffinity`  
`resource.connectionTrackingPolicy.idleTimeoutSec`  
`resource.connectionTrackingPolicy.trackingMode`  
`resource.consistentHash.httpCookie.name`  
`resource.consistentHash.httpCookie.path`  
`resource.consistentHash.httpCookie.ttl.nanos`  
`resource.consistentHash.httpCookie.ttl.seconds`  
`resource.consistentHash.minimumRingSize`  
`resource.customRequestHeaders`  
`resource.customResponseHeaders`  
`resource.description`  
`resource.enableCDN`  
`resource.failoverPolicy.disableConnectionDrainOnFailover`  
`resource.failoverPolicy.dropTrafficIfUnhealthy`  
`resource.failoverPolicy.failoverRatio`  
`resource.haPolicy.fastIPMove`  
`resource.haPolicy.leader.backendGroup`  
`resource.haPolicy.leader.networkEndpoint.instance`  
`resource.iap.enabled`  
`resource.iap.oauth2ClientId`  
`resource.ipAddressSelectionPolicy`  
`resource.loadBalancingScheme`  
`resource.localityLbPolicies.customPolicy.data`  
`resource.localityLbPolicies.customPolicy.name`  
`resource.localityLbPolicies.policy.name`  
`resource.logConfig.enable`  
`resource.logConfig.optionalFields`  
`resource.logConfig.optionalMode`  
`resource.logConfig.sampleRate`  
`resource.maxStreamDuration.nanos`  
`resource.maxStreamDuration.seconds`  
`resource.name`  
`resource.outlierDetection.baseEjectionTime.nanos`  
`resource.outlierDetection.baseEjectionTime.seconds`  
`resource.outlierDetection.consecutiveGatewayFailure`  
`resource.outlierDetection.enforcingConsecutiveErrors`  
`resource.outlierDetection.enforcingConsecutiveGatewayFailure`  
`resource.outlierDetection.enforcingSuccessRate`  
`resource.outlierDetection.maxEjectionPercent`  
`resource.outlierDetection.successRateMinimumHosts`  
`resource.outlierDetection.successRateRequestVolume`  
`resource.outlierDetection.successRateStdevFactor`  
`resource.portName`  
`resource.protocol`  
`resource.securitySettings.awsV4Authentication.accessKeyId`  
`resource.securitySettings.awsV4Authentication.accessKeyVersion`  
`resource.securitySettings.subjectAltNames`  
`resource.sessionAffinity`  
`resource.strongSessionAffinityCookie.name`  
`resource.strongSessionAffinityCookie.path`  
`resource.strongSessionAffinityCookie.ttl.nanos`  
`resource.strongSessionAffinityCookie.ttl.seconds`  
`resource.subsetting.policy`  
`resource.timeoutSec`  
compute.googleapis.com/ForwardingRule |  `resource.allowGlobalAccess`  
`resource.allowPscGlobalAccess`  
`resource.allPorts`  
`resource.description`  
`resource.IPProtocol`  
`resource.ipVersion`  
`resource.isMirroringCollector`  
`resource.loadBalancingScheme`  
`resource.metadataFilters.filterLabels.name`  
`resource.metadataFilters.filterLabels.value`  
`resource.metadataFilters.filterMatchCriteria`  
`resource.name`  
`resource.networkTier`  
`resource.noAutomateDnsZone`  
`resource.portRange`  
`resource.ports`  
`resource.serviceDirectoryRegistrations.namespace`  
`resource.serviceDirectoryRegistrations.service`  
`resource.serviceDirectoryRegistrations.serviceDirectoryRegion`  
`resource.serviceLabel`  
`resource.sourceIpRanges`  
`resource.target`  
compute.googleapis.com/HealthCheck |  `resource.checkIntervalSec`  
`resource.description`  
`resource.grpcHealthCheck.grpcServiceName`  
`resource.grpcHealthCheck.port`  
`resource.grpcHealthCheck.portSpecification`  
`resource.healthyThreshold`  
`resource.http2HealthCheck.host`  
`resource.http2HealthCheck.port`  
`resource.http2HealthCheck.portSpecification`  
`resource.http2HealthCheck.proxyHeader`  
`resource.http2HealthCheck.requestPath`  
`resource.http2HealthCheck.response`  
`resource.httpHealthCheck.host`  
`resource.httpHealthCheck.port`  
`resource.httpHealthCheck.portSpecification`  
`resource.httpHealthCheck.proxyHeader`  
`resource.httpHealthCheck.requestPath`  
`resource.httpHealthCheck.response`  
`resource.httpsHealthCheck.host`  
`resource.httpsHealthCheck.port`  
`resource.httpsHealthCheck.portSpecification`  
`resource.httpsHealthCheck.proxyHeader`  
`resource.httpsHealthCheck.requestPath`  
`resource.httpsHealthCheck.response`  
`resource.logConfig.enable`  
`resource.name`  
`resource.sourceRegions`  
`resource.sslHealthCheck.port`  
`resource.sslHealthCheck.portSpecification`  
`resource.sslHealthCheck.proxyHeader`  
`resource.sslHealthCheck.request`  
`resource.sslHealthCheck.response`  
`resource.tcpHealthCheck.port`  
`resource.tcpHealthCheck.portSpecification`  
`resource.tcpHealthCheck.proxyHeader`  
`resource.tcpHealthCheck.request`  
`resource.tcpHealthCheck.response`  
`resource.timeoutSec`  
`resource.type`  
`resource.unhealthyThreshold`  
compute.googleapis.com/NetworkEndpointGroup |  `resource.annotations`  
`resource.appEngine.service`  
`resource.appEngine.urlMask`  
`resource.appEngine.version`  
`resource.cloudFunction.function`  
`resource.cloudFunction.urlMask`  
`resource.cloudRun.service`  
`resource.cloudRun.tag`  
`resource.cloudRun.urlMask`  
`resource.defaultPort`  
`resource.description`  
`resource.name`  
`resource.network`  
`resource.networkEndpointType`  
`resource.pscData.producerPort`  
`resource.pscTargetService`  
`resource.subnetwork`  
compute.googleapis.com/SslPolicy |  `resource.customFeatures`  
`resource.description`  
`resource.minTlsVersion`  
`resource.name`  
`resource.profile`  
compute.googleapis.com/TargetGrpcProxy |  `resource.description`  
`resource.name`  
`resource.validateForProxyless`  
compute.googleapis.com/TargetHttpProxy |  `resource.description`  
`resource.httpKeepAliveTimeoutSec`  
`resource.name`  
`resource.proxyBind`  
compute.googleapis.com/TargetHttpsProxy |  `resource.description`  
`resource.httpKeepAliveTimeoutSec`  
`resource.name`  
`resource.proxyBind`  
`resource.quicOverride`  
`resource.tlsEarlyData`  
compute.googleapis.com/TargetInstance |  `resource.description`  
`resource.name`  
`resource.natPolicy`  
compute.googleapis.com/TargetPool |  `resource.description`  
`resource.failoverRatio`  
`resource.name`  
`resource.sessionAffinity`  
compute.googleapis.com/TargetSslProxy |  `resource.description`  
`resource.name`  
`resource.proxyHeader`  
compute.googleapis.com/TargetTcpProxy |  `resource.description`  
`resource.name`  
`resource.proxyBind`  
`resource.proxyHeader`  
compute.googleapis.com/UrlMap |  `resource.defaultCustomErrorResponsePolicy.errorResponseRules.matchResponseCodes`  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules.overrideResponseCode`  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules.path`  
`resource.defaultRouteAction.corsPolicy.allowCredentials`  
`resource.defaultRouteAction.corsPolicy.allowHeaders`  
`resource.defaultRouteAction.corsPolicy.allowMethods`  
`resource.defaultRouteAction.corsPolicy.allowOriginRegexes`  
`resource.defaultRouteAction.corsPolicy.allowOrigins`  
`resource.defaultRouteAction.corsPolicy.disabled`  
`resource.defaultRouteAction.corsPolicy.exposeHeaders`  
`resource.defaultRouteAction.corsPolicy.maxAge`  
`resource.defaultRouteAction.faultInjectionPolicy.abort.httpStatus`  
`resource.defaultRouteAction.faultInjectionPolicy.abort.percentage`  
`resource.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos`  
`resource.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds`  
`resource.defaultRouteAction.faultInjectionPolicy.delay.percentage`  
`resource.defaultRouteAction.maxStreamDuration.nanos`  
`resource.defaultRouteAction.maxStreamDuration.seconds`  
`resource.defaultRouteAction.retryPolicy.numRetries`  
`resource.defaultRouteAction.retryPolicy.perTryTimeout.nanos`  
`resource.defaultRouteAction.retryPolicy.perTryTimeout.seconds`  
`resource.defaultRouteAction.retryPolicy.retryConditions`  
`resource.defaultRouteAction.timeout.nanos`  
`resource.defaultRouteAction.timeout.seconds`  
`resource.defaultRouteAction.urlRewrite.hostRewrite`  
`resource.defaultRouteAction.urlRewrite.pathPrefixRewrite`  
`resource.defaultRouteAction.urlRewrite.pathTemplateRewrite`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToRemove`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace`  
`resource.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToRemove`  
`resource.defaultRouteAction.weightedBackendServices.weight`  
`resource.defaultUrlRedirect.hostRedirect`  
`resource.defaultUrlRedirect.httpsRedirect`  
`resource.defaultUrlRedirect.pathRedirect`  
`resource.defaultUrlRedirect.prefixRedirect`  
`resource.defaultUrlRedirect.redirectResponseCode`  
`resource.defaultUrlRedirect.stripQuery`  
`resource.description`  
`resource.headerAction.requestHeadersToAdd.headerName`  
`resource.headerAction.requestHeadersToAdd.headerValue`  
`resource.headerAction.requestHeadersToAdd.replace`  
`resource.headerAction.requestHeadersToRemove`  
`resource.headerAction.responseHeadersToAdd.headerName`  
`resource.headerAction.responseHeadersToAdd.headerValue`  
`resource.headerAction.responseHeadersToAdd.replace`  
`resource.headerAction.responseHeadersToRemove`  
`resource.hostRules.description`  
`resource.hostRules.hosts`  
`resource.hostRules.pathMatcher`  
`resource.name`  
`resource.pathMatchers.defaultCustomErrorResponsePolicy.errorResponseRules.matchResponseCodes`  
`resource.pathMatchers.defaultCustomErrorResponsePolicy.errorResponseRules.overrideResponseCode`  
`resource.pathMatchers.defaultCustomErrorResponsePolicy.errorResponseRules.path`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.allowCredentials`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.allowHeaders`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.allowMethods`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.allowOriginRegexes`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.allowOrigins`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.disabled`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.exposeHeaders`  
`resource.pathMatchers.defaultRouteAction.corsPolicy.maxAge`  
`resource.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.httpStatus`  
`resource.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.percentage`  
`resource.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos`  
`resource.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds`  
`resource.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.percentage`  
`resource.pathMatchers.defaultRouteAction.maxStreamDuration.nanos`  
`resource.pathMatchers.defaultRouteAction.maxStreamDuration.seconds`  
`resource.pathMatchers.defaultRouteAction.retryPolicy.numRetries`  
`resource.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.nanos`  
`resource.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.seconds`  
`resource.pathMatchers.defaultRouteAction.retryPolicy.retryConditions`  
`resource.pathMatchers.defaultRouteAction.timeout.nanos`  
`resource.pathMatchers.defaultRouteAction.timeout.seconds`  
`resource.pathMatchers.defaultRouteAction.urlRewrite.hostRewrite`  
`resource.pathMatchers.defaultRouteAction.urlRewrite.pathPrefixRewrite`  
`resource.pathMatchers.defaultRouteAction.urlRewrite.pathTemplateRewrite`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToRemove`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToRemove`  
`resource.pathMatchers.defaultRouteAction.weightedBackendServices.weight`  
`resource.pathMatchers.defaultUrlRedirect.hostRedirect`  
`resource.pathMatchers.defaultUrlRedirect.httpsRedirect`  
`resource.pathMatchers.defaultUrlRedirect.pathRedirect`  
`resource.pathMatchers.defaultUrlRedirect.prefixRedirect`  
`resource.pathMatchers.defaultUrlRedirect.redirectResponseCode`  
`resource.pathMatchers.defaultUrlRedirect.stripQuery`  
`resource.pathMatchers.description`  
`resource.pathMatchers.headerAction.requestHeadersToAdd.headerName`  
`resource.pathMatchers.headerAction.requestHeadersToAdd.headerValue`  
`resource.pathMatchers.headerAction.requestHeadersToAdd.replace`  
`resource.pathMatchers.headerAction.requestHeadersToRemove`  
`resource.pathMatchers.headerAction.responseHeadersToAdd.headerName`  
`resource.pathMatchers.headerAction.responseHeadersToAdd.headerValue`  
`resource.pathMatchers.headerAction.responseHeadersToAdd.replace`  
`resource.pathMatchers.headerAction.responseHeadersToRemove`  
`resource.pathMatchers.name`  
`resource.pathMatchers.pathRules.customErrorResponsePolicy.errorResponseRules.matchResponseCodes`  
`resource.pathMatchers.pathRules.customErrorResponsePolicy.errorResponseRules.overrideResponseCode`  
`resource.pathMatchers.pathRules.customErrorResponsePolicy.errorResponseRules.path`  
`resource.pathMatchers.pathRules.paths`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.allowCredentials`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.allowHeaders`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.allowMethods`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.allowOriginRegexes`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.allowOrigins`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.disabled`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.exposeHeaders`  
`resource.pathMatchers.pathRules.routeAction.corsPolicy.maxAge`  
`resource.pathMatchers.pathRules.routeAction.faultInjectionPolicy.abort.httpStatus`  
`resource.pathMatchers.pathRules.routeAction.faultInjectionPolicy.abort.percentage`  
`resource.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.fixedDelay.nanos`  
`resource.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.fixedDelay.seconds`  
`resource.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.percentage`  
`resource.pathMatchers.pathRules.routeAction.maxStreamDuration.nanos`  
`resource.pathMatchers.pathRules.routeAction.maxStreamDuration.seconds`  
`resource.pathMatchers.pathRules.routeAction.retryPolicy.numRetries`  
`resource.pathMatchers.pathRules.routeAction.retryPolicy.perTryTimeout.nanos`  
`resource.pathMatchers.pathRules.routeAction.retryPolicy.perTryTimeout.seconds`  
`resource.pathMatchers.pathRules.routeAction.retryPolicy.retryConditions`  
`resource.pathMatchers.pathRules.routeAction.timeout.nanos`  
`resource.pathMatchers.pathRules.routeAction.timeout.seconds`  
`resource.pathMatchers.pathRules.routeAction.urlRewrite.hostRewrite`  
`resource.pathMatchers.pathRules.routeAction.urlRewrite.pathPrefixRewrite`  
`resource.pathMatchers.pathRules.routeAction.urlRewrite.pathTemplateRewrite`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToRemove`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToRemove`  
`resource.pathMatchers.pathRules.routeAction.weightedBackendServices.weight`  
`resource.pathMatchers.pathRules.urlRedirect.hostRedirect`  
`resource.pathMatchers.pathRules.urlRedirect.httpsRedirect`  
`resource.pathMatchers.pathRules.urlRedirect.pathRedirect`  
`resource.pathMatchers.pathRules.urlRedirect.prefixRedirect`  
`resource.pathMatchers.pathRules.urlRedirect.redirectResponseCode`  
`resource.pathMatchers.pathRules.urlRedirect.stripQuery`  
`resource.pathMatchers.routeRules.customErrorResponsePolicy.errorResponseRules.matchResponseCodes`  
`resource.pathMatchers.routeRules.customErrorResponsePolicy.errorResponseRules.overrideResponseCode`  
`resource.pathMatchers.routeRules.customErrorResponsePolicy.errorResponseRules.path`  
`resource.pathMatchers.routeRules.description`  
`resource.pathMatchers.routeRules.headerAction.requestHeadersToAdd.headerName`  
`resource.pathMatchers.routeRules.headerAction.requestHeadersToAdd.headerValue`  
`resource.pathMatchers.routeRules.headerAction.requestHeadersToAdd.replace`  
`resource.pathMatchers.routeRules.headerAction.requestHeadersToRemove`  
`resource.pathMatchers.routeRules.headerAction.responseHeadersToAdd.headerName`  
`resource.pathMatchers.routeRules.headerAction.responseHeadersToAdd.headerValue`  
`resource.pathMatchers.routeRules.headerAction.responseHeadersToAdd.replace`  
`resource.pathMatchers.routeRules.headerAction.responseHeadersToRemove`  
`resource.pathMatchers.routeRules.matchRules.fullPathMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.exactMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.headerName`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.invertMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.prefixMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.presentMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.rangeMatch.rangeEnd`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.rangeMatch.rangeStart`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.regexMatch`  
`resource.pathMatchers.routeRules.matchRules.headerMatches.suffixMatch`  
`resource.pathMatchers.routeRules.matchRules.ignoreCase`  
`resource.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name`  
`resource.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value`  
`resource.pathMatchers.routeRules.matchRules.metadataFilters.filterMatchCriteria`  
`resource.pathMatchers.routeRules.matchRules.pathTemplateMatch`  
`resource.pathMatchers.routeRules.matchRules.prefixMatch`  
`resource.pathMatchers.routeRules.matchRules.queryParameterMatches.exactMatch`  
`resource.pathMatchers.routeRules.matchRules.queryParameterMatches.name`  
`resource.pathMatchers.routeRules.matchRules.queryParameterMatches.presentMatch`  
`resource.pathMatchers.routeRules.matchRules.queryParameterMatches.regexMatch`  
`resource.pathMatchers.routeRules.matchRules.regexMatch`  
`resource.pathMatchers.routeRules.priority`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.allowCredentials`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.allowHeaders`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.allowMethods`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.allowOriginRegexes`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.allowOrigins`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.disabled`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.exposeHeaders`  
`resource.pathMatchers.routeRules.routeAction.corsPolicy.maxAge`  
`resource.pathMatchers.routeRules.routeAction.faultInjectionPolicy.abort.httpStatus`  
`resource.pathMatchers.routeRules.routeAction.faultInjectionPolicy.abort.percentage`  
`resource.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.fixedDelay.nanos`  
`resource.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.fixedDelay.seconds`  
`resource.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.percentage`  
`resource.pathMatchers.routeRules.routeAction.maxStreamDuration.nanos`  
`resource.pathMatchers.routeRules.routeAction.maxStreamDuration.seconds`  
`resource.pathMatchers.routeRules.routeAction.retryPolicy.numRetries`  
`resource.pathMatchers.routeRules.routeAction.retryPolicy.perTryTimeout.nanos`  
`resource.pathMatchers.routeRules.routeAction.retryPolicy.perTryTimeout.seconds`  
`resource.pathMatchers.routeRules.routeAction.retryPolicy.retryConditions`  
`resource.pathMatchers.routeRules.routeAction.timeout.nanos`  
`resource.pathMatchers.routeRules.routeAction.timeout.seconds`  
`resource.pathMatchers.routeRules.routeAction.urlRewrite.hostRewrite`  
`resource.pathMatchers.routeRules.routeAction.urlRewrite.pathPrefixRewrite`  
`resource.pathMatchers.routeRules.routeAction.urlRewrite.pathTemplateRewrite`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToRemove`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToRemove`  
`resource.pathMatchers.routeRules.routeAction.weightedBackendServices.weight`  
`resource.pathMatchers.routeRules.urlRedirect.hostRedirect`  
`resource.pathMatchers.routeRules.urlRedirect.httpsRedirect`  
`resource.pathMatchers.routeRules.urlRedirect.pathRedirect`  
`resource.pathMatchers.routeRules.urlRedirect.prefixRedirect`  
`resource.pathMatchers.routeRules.urlRedirect.redirectResponseCode`  
`resource.pathMatchers.routeRules.urlRedirect.stripQuery`  
`resource.tests.description`  
`resource.tests.expectedOutputUrl`  
`resource.tests.expectedRedirectResponseCode`  
`resource.tests.headers.name`  
`resource.tests.headers.value`  
`resource.tests.host`  
`resource.tests.path`  
networkservices.googleapis.com/ServiceLbPolicy |  `resource.autoCapacityDrain.enable`  
`resource.description`  
`resource.failoverConfig.failoverHealthThreshold`  
`resource.loadBalancingAlgorithm`  
`resource.name`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.enforceTCPHealthCheckPort1024`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.enforceTCPHealthCheckPort1024`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `compute.googleapis.com/HealthCheck`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.tcpHealthCheck.port >= 1024"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.enforceTCPHealthCheckPort1024`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint that requires TCP health check ports to be `1024` or higher, preventing the use of well-known ports (`0`-`1023`).

### Create the custom constraint

  1. To define a custom constraint, create a file named `constraint-tcp-health-check-ports.yaml`.
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.enforceTCPHealthCheckPort1024
         resource_types:
         – compute.googleapis.com/HealthCheck
         condition: "resource.tcpHealthCheck.port >= 1024"
         method_types:
         – CREATE
         – UPDATE
         action_type: ALLOW
         display_name: Only TCP health check ports >= 1024 allowed.
         description: Prevent TCP health checks on well-known ports.

Replace ORGANIZATION_ID with your organization ID.

  2. Apply the custom constraint.
         
         gcloud org-policies set-custom-constraint constraint-tcp-health-check-ports
         




### Create the organization policy

  1. To define an organization policy, create a file named `policy-tcp-health-check-ports.yaml`. In this example we enforce this constraint at the project level but you might also set this at the organization or folder level.
         
         name: projects/PROJECT_ID/policies/custom.enforceTCPHealthCheckPort1024
         spec:
           rules:
           – enforce: true

Replace `PROJECT_ID` with your project ID.

  2. Enforce the organization policy.
         
         gcloud org-policies set-policy policy-tcp-health-check-ports
         

  3. Verify that the organization policy exists.
         
         gcloud org-policies list --project PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT: custom.enforceTCPHealthCheckPort1024
         LIST_POLICY: SET
         BOOLEAN_POLICY: -
         ETAG: CNHuh7kGEJiatFo=-
         




### Test the policy

  1. Test the constraint by creating a TCP health check on port 80.
         
         gcloud compute health-checks create tcp my-tcp-health-check \
             --project=PROJECT_ID \
             --region=us-central1 \
             --port=80 \
             --check-interval=5s \
             --timeout=5s \
             --healthy-threshold=4 \
             --unhealthy-threshold=5 \
         

The operation is disallowed and the output is similar to the following:
         
         ERROR: (gcloud.compute.healthChecks.create) Could not fetch resource:
         – Operation denied by custom org policies: [customConstraints/custom.enforceTCPHealthCheckPort1024]: Only TCP health check ports >= 1024 allowed.
         




## Example custom organization policies for common use cases

The following table provides the syntax for some common custom constraints. 

Description | Constraint syntax  
---|---  
Require all backend buckets to have Cloud CDN enabled | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.backendBucketEnableCdn
        resourceTypes:
        - compute.googleapis.com/BackendBucket
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.enableCdn == true"
        actionType: ALLOW
        displayName: Require all backend buckets to have Cloud CDN enabled
        description: All backend buckets must have Cloud CDN enabled.
          
  
Disallow the use of HTTP and TCP as backend service protocols | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.backendBucketEnableCdn
        resourceTypes:
        - compute.googleapis.com/BackendService
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.protocol == 'HTTP' || resource.protocol == 'TCP'"
        actionType: DENY
        displayName: Disallow the use of HTTP and TCP as backend service protocols
        description: Backend services cannot configure HTTP or TCP as the backend service protocol.
          
  
Require forwarding rules to use Standard Tier | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.forwardingRulesStandardTier
        resourceTypes:
        - compute.googleapis.com/ForwardingRule
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.networkTier == 'STANDARD'"
        actionType: ALLOW
        displayName: Require forwarding rules to use Standard Tier
        description: Forwarding rules must use the Standard Network Service Tier.
          
  
Require all health check protocols to occur on port 1024 or higher | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.healthCheckPortMin1024
        resourceTypes:
        - compute.googleapis.com/HealthCheck
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.tcpHealthCheck.port >= 1024 && resource.httpHealthCheck.port >= 1024 && resource.httpsHealthCheck.port >= 1024 && resource.sslHealthCheck.port >= 1024 && resource.sslHealthCheck.port >= 1024 &&resource.http2HealthCheck.port >= 1024 && resource.grpcHealthCheck.port >= 1024"
        actionType: ALLOW
        displayName: Require port 1024 or greater for all health checks
        description: All health check protocols must use a port of 1024 or higher, to avoid well-known ports.
          
  
Disallow gRPC health checks | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.disallowGRPCHealthChecks
        resourceTypes:
        - compute.googleapis.com/HealthCheck
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.type == 'GRPC'"
        actionType: DENY
        displayName: Disallow GRPC health checks
        description: Health checks aren't allowed to use GRPC.
          
  
Prevent high frequency health check probes | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.minHealthCheckFrequency
        resourceTypes:
        - compute.googleapis.com/HealthCheck
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.checkIntervalSec >= 30"
        actionType: ALLOW
        displayName: Disallow fast health check probes
        description: Prevent health checks from having a probe frequency under 30 seconds.
          
  
Disallow client HTTPS keepalive timeout values greater than 1000 seconds | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.clientHTTPSKeepalive1000Sec
        resourceTypes:
        - compute.googleapis.com/TargetHttpsProxy
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.httpKeepAliveTimeoutSec > 1000"
        actionType: DENY
        displayName: Disallow client HTTPS keepalive timeout greater than 1000 seconds
        description: Disallow client HTTPS keepalive timeout values greater than 1000 seconds.
          
  
Require URL maps to have a custom error response policy for HTTP `500` status codes | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.urlMapCustomResponseHTTP500
        resourceTypes:
        - compute.googleapis.com/UrlMaps
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.defaultCustomErrorResponsePolicy.errorResponseRule.exists(value, value.matchResponseCode == 500)"
        actionType: ALLOW
        displayName: Require URL maps to have a custom error response policy for HTTP 500 errors
        description: URL maps must have a custom error response policy configured for HTTP 500 errors.
          
  
Require target instances to have a name that starts with the string "targetInstance" | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.targetInstanceConstraint
        resourceTypes:
        - compute.googleapis.com/TargetInstance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.name.startsWith('targetInstance')"
        actionType: ALLOW
        displayName: Require target instances to have a name that starts with the string "targetInstance"
        description: Target instances must have resource names that start with the string "targetInstance"
          
  
Require target pools to have a CLIENT_IP session affinity | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.targetPoolConstraint
        resourceTypes:
        - compute.googleapis.com/TargetPool
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.sessionAffinity == 'CLIENT_IP'"
        actionType: ALLOW
        displayName: Require target pools to use CLIENT_IP session affinity
        description: Target pools must use CLIENT_IP session affinity
          
  
Restrict the minimum TLS version to 1.2 | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictLbTlsVersion
        resource_types: compute.googleapis.com/SslPolicy
        methodTypes:
        - CREATE
        - UPDATE
        condition: resource.minTlsVersion == "TLS_1_2"
        action_type: ALLOW
        display_name: Restrict Load Balancing TLS version to 1.2
        description: Only allow SSL policies to be created or updated if the minimum TLS version is 1.2 where this custom constraint is enforced.
          
  
Allow the creation of an SSL resource if the following conditions are met:

  * The minimum TLS version is set to 1.2
  * The SSL policy has a **CUSTOM** profile that lets you select SSL features individually
  * The SSL policy does not include the ChaCha20-Poly1305 cipher suite

| 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictLbTlsCapabilities
        resourceTypes:
        - compute.googleapis.com/SslPolicy
        methodTypes:
        - CREATE
        - UPDATE
        condition: resource.minTlsVersion == "TLS_1_2" && resource.profile == "CUSTOM" && !resource.customFeatures.exists(feature, feature.contains("CHACHA20_POLY1305"))
        actionType: ALLOW
        displayName: Restrict Load Balancing TLS Capabilities
        description: Only allow SSL Policy resources to be created or updated if the minimum TLS version is 1.2, profile is CUSTOM, and no ChaCha20-Poly1305 cipher suite is used where this custom constraint is enforced.
          
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
