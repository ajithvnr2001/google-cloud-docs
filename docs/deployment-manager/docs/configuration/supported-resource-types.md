---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types/
title: Supported resource types \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:13.624867+00:00
---

# Supported resource types  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Supported resource types Stay organized with collections  Save and categorize content based on your preferences. 

Deployment Manager uses the underlying APIs of each Google Cloud service to deploy your resources. For example, to create Compute Engine virtual machine instances, Deployment Manager makes a call to the Compute Engine API to create the instance, and then adds it to your deployment.

**Note:** If you want to create more types of resources in your deployments, consider using [Google Cloud type providers (beta)](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#basetypes), which adds support for more Google Cloud resources. For a list of supported type providers, see [Supported Google Cloud type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

## Resources for project creation

If you are creating projects using Deployment Manager, you can use the following virtual resource types to enable APIs in your project, or change the billing information for your project.

Resource Type| Description| Example| Reference| `deploymentmanager.v2.virtual.enableService` | Enable a service API. You must create a virtual resource for every API that you want to enable. | [Example in GitHub](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/blob/master/google/resource-snippets/serviceusage-v1/enable.jinja) | [Documentation](https://docs.cloud.google.com/service-management/reference/rest/v1/services/enable)  
---|---|---|---  
`deploymentmanager.v2.virtual.projectBillingInfo` | Modify the billing information for the project. |  | [Documentation](https://docs.cloud.google.com/billing/reference/rest/v1/projects/updateBillingInfo)  
  
## APIs for supported resources

The table below is a list of resource types that you can create in your deployments. To determine the properties you can set in Deployment Manager for a particular API, you must use the respective API's documentation as a guide.

For steps to use an API's resource representation to create your configuration, see [Declaring resource properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).

For examples of deployments that use these resources, see the [Deployment Manager GitHub Repository](https://github.com/GoogleCloudPlatform/deploymentmanager-samples).

**Note:** Some of the following types have names which are similar to, but different from, the names of their associated API collections. If you use the API collection name instead of the type name provided by Deployment Manager (for example, `compute.v1.addresses` instead of `compute.v1.address`), you might encounter unexpected behavior from your deployments, so be careful to ensure that you use type names as defined by Deployment Manager.

For a full list of supported resource types, including resources that are in alpha, run the [`types list`](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager/types/list) command in `gcloud`:
    
    
    gcloud deployment-manager types list
    

Resource Type| Reference| `appengine.v1.version` | [Documentation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)  
---|---  
`bigquery.v2.dataset` | [Documentation](https://docs.cloud.google.com/bigquery/docs/reference/v2/datasets)  
`bigquery.v2.table` | [Documentation](https://docs.cloud.google.com/bigquery/docs/reference/v2/tables)  
`bigtableadmin.v2.instance` | [Documentation](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances)  
`bigtableadmin.v2.instance.table` | [Documentation](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables)  
`cloudresourcemanager.v1.project` | [Documentation](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects)  
`compute.beta.address` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/addresses)  
`compute.beta.autoscaler` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/autoscalers)  
`compute.beta.backendBucket` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/backendBuckets)  
`compute.beta.backendService` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/backendServices)  
`compute.beta.disk` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/disks)  
`compute.beta.firewall` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/firewalls)  
`compute.beta.forwardingRule` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/forwardingRules)  
`compute.beta.globalAddress` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/globalAddresses)  
`compute.beta.globalForwardingRule` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/globalForwardingRules)  
`compute.beta.healthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/healthChecks)  
`compute.beta.httpHealthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/httpHealthChecks)  
`compute.beta.httpsHealthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/httpsHealthChecks)  
`compute.beta.image` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/images)  
`compute.beta.instance` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/instances)  
`compute.beta.instanceGroup` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/instanceGroups)  
`compute.beta.instanceGroupManager` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/instanceGroupManagers)  
`compute.beta.instanceTemplate` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/instanceTemplates)  
`compute.beta.network` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/networks)  
`compute.beta.regionAutoscaler` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/regionAutoscalers)  
`compute.beta.regionBackendService` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/regionBackendServices)  
`compute.beta.regionInstanceGroup` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/regionInstanceGroups)  
`compute.beta.regionInstanceGroupManager` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/regionInstanceGroupManagers)  
`compute.beta.route` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/routes)  
`compute.beta.router` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/routers)  
`compute.beta.sslCertificate` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/sslCertificates)  
`compute.beta.subnetwork` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/subnetworks)  
`compute.beta.targetHttpProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetHttpProxies)  
`compute.beta.targetHttpsProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetHttpsProxies)  
`compute.beta.targetInstance` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetInstances)  
`compute.beta.targetPool` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetPools)  
`compute.beta.targetSslProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetSslProxies)  
`compute.beta.targetVpnGateway` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/targetVpnGateways)  
`compute.beta.urlMap` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/urlMaps)  
`compute.beta.vpnTunnel` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/vpnTunnels)  
`compute.beta.xpnHost` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/projects/enableXpnHost)  
`compute.beta.xpnResource` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/beta/projects/enableXpnResource)  
`compute.v1.address` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/addresses)  
`compute.v1.autoscaler` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/autoscalers)  
`compute.v1.backendService` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/backendServices)  
`compute.v1.disk` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/disks)  
`compute.v1.firewall` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/firewalls)  
`compute.v1.forwardingRule` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/forwardingRules)  
`compute.v1.globalAddress` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/globalAddresses)  
`compute.v1.globalForwardingRule` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/globalForwardingRules)  
`compute.v1.healthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/healthChecks)  
`compute.v1.httpHealthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/httpHealthChecks)  
`compute.v1.httpsHealthCheck` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/httpsHealthChecks)  
`compute.v1.image` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/images)  
`compute.v1.instance` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/instances)  
`compute.v1.instanceGroup` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroups)  
`compute.v1.instanceGroupManager` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers)  
`compute.v1.instanceTemplate` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/instanceTemplates)  
`compute.v1.network` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/networks)  
`compute.v1.regionAutoscaler` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/regionAutoscalers)  
`compute.v1.regionBackendService` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/regionBackendServices)  
`compute.v1.regionInstanceGroup` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroups)  
`compute.v1.regionInstanceGroupManager` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers)  
`compute.v1.route` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/routes)  
`compute.v1.router` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/routers)  
`compute.v1.sslCertificate` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/sslCertificates)  
`compute.v1.subnetwork` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/subnetworks)  
`compute.v1.targetHttpProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetHttpProxies)  
`compute.v1.targetHttpsProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetHttpsProxies)  
`compute.v1.targetInstance` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetInstances)  
`compute.v1.targetPool` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools)  
`compute.v1.targetSslProxy` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetSslProxies)  
`compute.v1.targetVpnGateway` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/targetVpnGateways)  
`compute.v1.urlMap` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/urlMaps)  
`compute.v1.vpnTunnel` | [Documentation](https://docs.cloud.google.com/compute/docs/reference/latest/vpnTunnels)  
`container.v1.cluster` | [Documentation](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters)  
`container.v1.nodePool` | [Documentation](https://docs.cloud.google.com/kubernetes-engine/reference/rest/v1/projects.zones.clusters.nodePools)  
`dataproc.v1.cluster` | [Documentation](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters)  
`dns.v1.managedZone` | [Documentation](https://docs.cloud.google.com/dns/api/v1/managedZones)  
`iam.v1.serviceAccount` | [Documentation](https://docs.cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts)  
`iam.v1.serviceAccounts.key` | [Documentation](https://docs.cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys)  
`logging.v2.metric` | [Documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics)  
`logging.v2.sink` | [Documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks)  
`pubsub.v1.subscription` | [Documentation](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)  
`pubsub.v1.topic` | [Documentation](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)  
`runtimeconfig.v1beta1.config` | [Documentation](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs)  
`runtimeconfig.v1beta1.variable` | [Documentation](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables)  
`runtimeconfig.v1beta1.waiter` | [Documentation](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters)  
`spanner.v1.instance` | [Documentation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)  
`sqladmin.v1beta4.database` | [Documentation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/v1beta4/databases)  
`sqladmin.v1beta4.instance` | [Documentation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/v1beta4/instances)  
`sqladmin.v1beta4.user` | [Documentation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/v1beta4/users)  
`storage.v1.bucket` | [Documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)  
`storage.v1.bucketAccessControl` | [Documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/bucketAccessControls)  
`storage.v1.defaultObjectAccessControl` | [Documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls)  
`storage.v1.object` | [Documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects)  
`storage.v1.objectAccessControl` | [Documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/objectAccessControls)  
  
## What's next

  * Create a [configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file).
  * Try the Deployment Manager [quickstart](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment).
  * Go through the [Step-by-step guide](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide).
  * For sample deployments that you can adapt to your requirements, see the [Deployment Manager GitHub Repository](https://github.com/GoogleCloudPlatform/deploymentmanager-samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
