---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.LoadBalancerBackendInfoOrBuilder
title: Interface LoadBalancerBackendInfoOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:00.215907+00:00
---

# Interface LoadBalancerBackendInfoOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.LoadBalancerBackendInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LoadBalancerBackendInfoOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 
    
    
    public interface LoadBalancerBackendInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackendBucketUri()
    
    
    public abstract String getBackendBucketUri()

URI of the backend bucket this backend targets (if applicable).

`string backend_bucket_uri = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backendBucketUri.  
  
### getBackendBucketUriBytes()
    
    
    public abstract ByteString getBackendBucketUriBytes()

URI of the backend bucket this backend targets (if applicable).

`string backend_bucket_uri = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backendBucketUri.  
  
### getBackendServiceUri()
    
    
    public abstract String getBackendServiceUri()

URI of the backend service this backend belongs to (if applicable).

`string backend_service_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backendServiceUri.  
  
### getBackendServiceUriBytes()
    
    
    public abstract ByteString getBackendServiceUriBytes()

URI of the backend service this backend belongs to (if applicable).

`string backend_service_uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backendServiceUri.  
  
### getHealthCheckFirewallsConfigState()
    
    
    public abstract LoadBalancerBackendInfo.HealthCheckFirewallsConfigState getHealthCheckFirewallsConfigState()

Output only. Health check firewalls configuration state for the backend. This is a result of the static firewall analysis (verifying that health check traffic from required IP ranges to the backend is allowed or not). The backend might still be unhealthy even if these firewalls are configured. Please refer to the documentation for more information: <https://cloud.google.com/load-balancing/docs/firewall-rules>

` .google.cloud.networkmanagement.v1beta1.LoadBalancerBackendInfo.HealthCheckFirewallsConfigState health_check_firewalls_config_state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LoadBalancerBackendInfo.HealthCheckFirewallsConfigState](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.LoadBalancerBackendInfo.HealthCheckFirewallsConfigState)` | The healthCheckFirewallsConfigState.  
  
### getHealthCheckFirewallsConfigStateValue()
    
    
    public abstract int getHealthCheckFirewallsConfigStateValue()

Output only. Health check firewalls configuration state for the backend. This is a result of the static firewall analysis (verifying that health check traffic from required IP ranges to the backend is allowed or not). The backend might still be unhealthy even if these firewalls are configured. Please refer to the documentation for more information: <https://cloud.google.com/load-balancing/docs/firewall-rules>

` .google.cloud.networkmanagement.v1beta1.LoadBalancerBackendInfo.HealthCheckFirewallsConfigState health_check_firewalls_config_state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for healthCheckFirewallsConfigState.  
  
### getHealthCheckUri()
    
    
    public abstract String getHealthCheckUri()

URI of the health check attached to this backend (if applicable).

`string health_check_uri = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The healthCheckUri.  
  
### getHealthCheckUriBytes()
    
    
    public abstract ByteString getHealthCheckUriBytes()

URI of the health check attached to this backend (if applicable).

`string health_check_uri = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for healthCheckUri.  
  
### getInstanceGroupUri()
    
    
    public abstract String getInstanceGroupUri()

URI of the instance group this backend belongs to (if applicable).

`string instance_group_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceGroupUri.  
  
### getInstanceGroupUriBytes()
    
    
    public abstract ByteString getInstanceGroupUriBytes()

URI of the instance group this backend belongs to (if applicable).

`string instance_group_uri = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instanceGroupUri.  
  
### getInstanceUri()
    
    
    public abstract String getInstanceUri()

URI of the backend instance (if applicable). Populated for instance group backends, and zonal NEG backends.

`string instance_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceUri.  
  
### getInstanceUriBytes()
    
    
    public abstract ByteString getInstanceUriBytes()

URI of the backend instance (if applicable). Populated for instance group backends, and zonal NEG backends.

`string instance_uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instanceUri.  
  
### getName()
    
    
    public abstract String getName()

Display name of the backend. For example, it might be an instance name for the instance group backends, or an IP address and port for zonal network endpoint group backends.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Display name of the backend. For example, it might be an instance name for the instance group backends, or an IP address and port for zonal network endpoint group backends.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetworkEndpointGroupUri()
    
    
    public abstract String getNetworkEndpointGroupUri()

URI of the network endpoint group this backend belongs to (if applicable).

`string network_endpoint_group_uri = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The networkEndpointGroupUri.  
  
### getNetworkEndpointGroupUriBytes()
    
    
    public abstract ByteString getNetworkEndpointGroupUriBytes()

URI of the network endpoint group this backend belongs to (if applicable).

`string network_endpoint_group_uri = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for networkEndpointGroupUri.  
  
### getPscGoogleApiTarget()
    
    
    public abstract String getPscGoogleApiTarget()

PSC Google API target this PSC NEG backend targets (if applicable).

`string psc_google_api_target = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pscGoogleApiTarget.  
  
### getPscGoogleApiTargetBytes()
    
    
    public abstract ByteString getPscGoogleApiTargetBytes()

PSC Google API target this PSC NEG backend targets (if applicable).

`string psc_google_api_target = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pscGoogleApiTarget.  
  
### getPscServiceAttachmentUri()
    
    
    public abstract String getPscServiceAttachmentUri()

URI of the PSC service attachment this PSC NEG backend targets (if applicable).

`string psc_service_attachment_uri = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pscServiceAttachmentUri.  
  
### getPscServiceAttachmentUriBytes()
    
    
    public abstract ByteString getPscServiceAttachmentUriBytes()

URI of the PSC service attachment this PSC NEG backend targets (if applicable).

`string psc_service_attachment_uri = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pscServiceAttachmentUri.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
