---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.EndpointOrBuilder
title: Interface EndpointOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:35.206108+00:00
---

# Interface EndpointOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.EndpointOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EndpointOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 
    
    
    public interface EndpointOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppEngineVersion()
    
    
    public abstract Endpoint.AppEngineVersionEndpoint getAppEngineVersion()

An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpoint app_engine_version = 11; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.AppEngineVersionEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpoint)` | The appEngineVersion.  
  
### getAppEngineVersionOrBuilder()
    
    
    public abstract Endpoint.AppEngineVersionEndpointOrBuilder getAppEngineVersionOrBuilder()

An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpoint app_engine_version = 11; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.AppEngineVersionEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpointOrBuilder)` |   
  
### getCloudFunction()
    
    
    public abstract Endpoint.CloudFunctionEndpoint getCloudFunction()

A [Cloud Function](https://cloud.google.com/functions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpoint cloud_function = 10; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.CloudFunctionEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpoint)` | The cloudFunction.  
  
### getCloudFunctionOrBuilder()
    
    
    public abstract Endpoint.CloudFunctionEndpointOrBuilder getCloudFunctionOrBuilder()

A [Cloud Function](https://cloud.google.com/functions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpoint cloud_function = 10; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.CloudFunctionEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpointOrBuilder)` |   
  
### getCloudRunJob()
    
    
    public abstract String getCloudRunJob()

A [Cloud Run](https://cloud.google.com/run) [job](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job) URI. Applicable only to source endpoint. The format is: projects/{project}/locations/{location}/jobs/{job}

`string cloud_run_job = 24;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudRunJob.  
  
### getCloudRunJobBytes()
    
    
    public abstract ByteString getCloudRunJobBytes()

A [Cloud Run](https://cloud.google.com/run) [job](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job) URI. Applicable only to source endpoint. The format is: projects/{project}/locations/{location}/jobs/{job}

`string cloud_run_job = 24;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudRunJob.  
  
### getCloudRunRevision()
    
    
    public abstract Endpoint.CloudRunRevisionEndpoint getCloudRunRevision()

A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpoint cloud_run_revision = 12; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.CloudRunRevisionEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpoint)` | The cloudRunRevision.  
  
### getCloudRunRevisionOrBuilder()
    
    
    public abstract Endpoint.CloudRunRevisionEndpointOrBuilder getCloudRunRevisionOrBuilder()

A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpoint cloud_run_revision = 12; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.CloudRunRevisionEndpointOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpointOrBuilder)` |   
  
### getCloudSqlInstance()
    
    
    public abstract String getCloudSqlInstance()

A [Cloud SQL](https://cloud.google.com/sql) instance URI.

`string cloud_sql_instance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudSqlInstance.  
  
### getCloudSqlInstanceBytes()
    
    
    public abstract ByteString getCloudSqlInstanceBytes()

A [Cloud SQL](https://cloud.google.com/sql) instance URI.

`string cloud_sql_instance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudSqlInstance.  
  
### getDmsPrivateConnection()
    
    
    public abstract String getDmsPrivateConnection()

A [DMS Private Connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections) name format: projects/{project}/locations/{location}/privateConnections/{privateConnection}.

`string dms_private_connection = 22;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dmsPrivateConnection.  
  
### getDmsPrivateConnectionBytes()
    
    
    public abstract ByteString getDmsPrivateConnectionBytes()

A [DMS Private Connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections) name format: projects/{project}/locations/{location}/privateConnections/{privateConnection}.

`string dms_private_connection = 22;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dmsPrivateConnection.  
  
### getForwardingRule()
    
    
    public abstract String getForwardingRule()

A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Applicable only to destination endpoint. Format: `projects/{project}/global/forwardingRules/{id}` or `projects/{project}/regions/{region}/forwardingRules/{id}`

`string forwarding_rule = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The forwardingRule.  
  
### getForwardingRuleBytes()
    
    
    public abstract ByteString getForwardingRuleBytes()

A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Applicable only to destination endpoint. Format: `projects/{project}/global/forwardingRules/{id}` or `projects/{project}/regions/{region}/forwardingRules/{id}`

`string forwarding_rule = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for forwardingRule.  
  
### getForwardingRuleTarget()
    
    
    public abstract Endpoint.ForwardingRuleTarget getForwardingRuleTarget()

Output only. Specifies the type of the target of the forwarding rule.

` optional .google.cloud.networkmanagement.v1beta1.Endpoint.ForwardingRuleTarget forwarding_rule_target = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.ForwardingRuleTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.ForwardingRuleTarget)` | The forwardingRuleTarget.  
  
### getForwardingRuleTargetValue()
    
    
    public abstract int getForwardingRuleTargetValue()

Output only. Specifies the type of the target of the forwarding rule.

` optional .google.cloud.networkmanagement.v1beta1.Endpoint.ForwardingRuleTarget forwarding_rule_target = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for forwardingRuleTarget.  
  
### getFqdn()
    
    
    public abstract String getFqdn()

DNS endpoint of [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Requires gke_master_cluster to be set, can't be used simultaneoulsly with ip_address or network. Applicable only to destination endpoint.

`string fqdn = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fqdn.  
  
### getFqdnBytes()
    
    
    public abstract ByteString getFqdnBytes()

DNS endpoint of [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Requires gke_master_cluster to be set, can't be used simultaneoulsly with ip_address or network. Applicable only to destination endpoint.

`string fqdn = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fqdn.  
  
### getGkeMasterCluster()
    
    
    public abstract String getGkeMasterCluster()

A cluster URI for [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

`string gke_master_cluster = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gkeMasterCluster.  
  
### getGkeMasterClusterBytes()
    
    
    public abstract ByteString getGkeMasterClusterBytes()

A cluster URI for [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).

`string gke_master_cluster = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gkeMasterCluster.  
  
### getGkePod()
    
    
    public abstract String getGkePod()

A [GKE Pod](https://cloud.google.com/kubernetes-engine/docs/concepts/pod) URI.

`string gke_pod = 21;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gkePod.  
  
### getGkePodBytes()
    
    
    public abstract ByteString getGkePodBytes()

A [GKE Pod](https://cloud.google.com/kubernetes-engine/docs/concepts/pod) URI.

`string gke_pod = 21;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gkePod.  
  
### getInstance()
    
    
    public abstract String getInstance()

A Compute Engine instance URI.

`string instance = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instance.  
  
### getInstanceBytes()
    
    
    public abstract ByteString getInstanceBytes()

A Compute Engine instance URI.

`string instance = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instance.  
  
### getIpAddress()
    
    
    public abstract String getIpAddress()

The IP address of the endpoint, which can be an external or internal IP.

`string ip_address = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ipAddress.  
  
### getIpAddressBytes()
    
    
    public abstract ByteString getIpAddressBytes()

The IP address of the endpoint, which can be an external or internal IP.

`string ip_address = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ipAddress.  
  
### getLoadBalancerId()
    
    
    public abstract String getLoadBalancerId()

Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers.

`optional string load_balancer_id = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The loadBalancerId.  
  
### getLoadBalancerIdBytes()
    
    
    public abstract ByteString getLoadBalancerIdBytes()

Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers.

`optional string load_balancer_id = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for loadBalancerId.  
  
### getLoadBalancerType()
    
    
    public abstract LoadBalancerType getLoadBalancerType()

Output only. Type of the load balancer the forwarding rule points to.

` optional .google.cloud.networkmanagement.v1beta1.LoadBalancerType load_balancer_type = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LoadBalancerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.LoadBalancerType)` | The loadBalancerType.  
  
### getLoadBalancerTypeValue()
    
    
    public abstract int getLoadBalancerTypeValue()

Output only. Type of the load balancer the forwarding rule points to.

` optional .google.cloud.networkmanagement.v1beta1.LoadBalancerType load_balancer_type = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for loadBalancerType.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

A VPC network URI. For source endpoints, used according to the `network_type`. For destination endpoints, used only when the source is an external IP address endpoint, and the destination is an internal IP address endpoint.

`string network = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

A VPC network URI. For source endpoints, used according to the `network_type`. For destination endpoints, used only when the source is an external IP address endpoint, and the destination is an internal IP address endpoint.

`string network = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkType()
    
    
    public abstract Endpoint.NetworkType getNetworkType()

For source endpoints, type of the network where the endpoint is located. Not relevant for destination endpoints.

`.google.cloud.networkmanagement.v1beta1.Endpoint.NetworkType network_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Endpoint.NetworkType](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.Endpoint.NetworkType)` | The networkType.  
  
### getNetworkTypeValue()
    
    
    public abstract int getNetworkTypeValue()

For source endpoints, type of the network where the endpoint is located. Not relevant for destination endpoints.

`.google.cloud.networkmanagement.v1beta1.Endpoint.NetworkType network_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for networkType.  
  
### getPort()
    
    
    public abstract int getPort()

The IP protocol port of the endpoint. Only applicable when protocol is TCP or UDP.

`int32 port = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The port.  
  
### getProjectId()
    
    
    public abstract String getProjectId()

For source endpoints, endpoint project ID. Used according to the `network_type`. Not relevant for destination endpoints.

`string project_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The projectId.  
  
### getProjectIdBytes()
    
    
    public abstract ByteString getProjectIdBytes()

For source endpoints, endpoint project ID. Used according to the `network_type`. Not relevant for destination endpoints.

`string project_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for projectId.  
  
### getRedisCluster()
    
    
    public abstract String getRedisCluster()

A [Redis Cluster](https://cloud.google.com/memorystore/docs/cluster) URI. Applicable only to destination endpoint.

`string redis_cluster = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The redisCluster.  
  
### getRedisClusterBytes()
    
    
    public abstract ByteString getRedisClusterBytes()

A [Redis Cluster](https://cloud.google.com/memorystore/docs/cluster) URI. Applicable only to destination endpoint.

`string redis_cluster = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for redisCluster.  
  
### getRedisInstance()
    
    
    public abstract String getRedisInstance()

A [Redis Instance](https://cloud.google.com/memorystore/docs/redis) URI. Applicable only to destination endpoint.

`string redis_instance = 17;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The redisInstance.  
  
### getRedisInstanceBytes()
    
    
    public abstract ByteString getRedisInstanceBytes()

A [Redis Instance](https://cloud.google.com/memorystore/docs/redis) URI. Applicable only to destination endpoint.

`string redis_instance = 17;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for redisInstance.  
  
### hasAppEngineVersion()
    
    
    public abstract boolean hasAppEngineVersion()

An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpoint app_engine_version = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appEngineVersion field is set.  
  
### hasCloudFunction()
    
    
    public abstract boolean hasCloudFunction()

A [Cloud Function](https://cloud.google.com/functions). Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpoint cloud_function = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudFunction field is set.  
  
### hasCloudRunRevision()
    
    
    public abstract boolean hasCloudRunRevision()

A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) Applicable only to source endpoint.

` .google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpoint cloud_run_revision = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudRunRevision field is set.  
  
### hasForwardingRuleTarget()
    
    
    public abstract boolean hasForwardingRuleTarget()

Output only. Specifies the type of the target of the forwarding rule.

` optional .google.cloud.networkmanagement.v1beta1.Endpoint.ForwardingRuleTarget forwarding_rule_target = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the forwardingRuleTarget field is set.  
  
### hasLoadBalancerId()
    
    
    public abstract boolean hasLoadBalancerId()

Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers.

`optional string load_balancer_id = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loadBalancerId field is set.  
  
### hasLoadBalancerType()
    
    
    public abstract boolean hasLoadBalancerType()

Output only. Type of the load balancer the forwarding rule points to.

` optional .google.cloud.networkmanagement.v1beta1.LoadBalancerType load_balancer_type = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loadBalancerType field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
