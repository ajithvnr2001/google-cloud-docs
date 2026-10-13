---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript/
title: Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadInstallScript \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:42.407774+00:00
---

# Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadInstallScript  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.networkMonitoringProviders.monitoringPoints.downloadInstallScript Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * MonitoringPointType
  * StaticIpConfig
    * JSON representation
  * Try it!



Downloads an install script for MonitoringPoints for a given network monitoring provider.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/monitoringPoints:downloadInstallScript`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for DownloadInstallScriptRequest. Format: projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}  
  
### Query parameters

Parameters  
---  
`monitoringPointType` |  `enum (`[MonitoringPointType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript#MonitoringPointType)`)` Required. The type of the monitoring point.  
`hostname` |  `string` Required. The hostname of the MonitoringPoint, e.g. "test-vm"  
`password` |  `string` Optional. Password for logging into the MonitoringPoint.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/Shared.Types/TimeZone)`)` Optional. Time zone defined for the MonitoringPoint.  
`privateConnectivityEnabled` |  `boolean` Optional. For Google Cloud MPs, this field indicates whether the Monitoring Point is deployed in a Private Service Connect deployment. Not used for non-Google Cloud MPs.  
`ntpServerAddress` |  `string` Optional. Network Time Protocol a user can configure. If the user omits the field, the default is either NTP servers provided in the DHCP lease or a set of well-known NTP servers pre-configured on the monitoring point. This field can be an IP address or FQDN.  
`ntpServerSecondaryAddress` |  `string` Optional. Second NTP server.  
Union parameter `ip_address_configuration`. IP address configuration of the MonitoringPoint. `ip_address_configuration` can be only one of the following:  
`useDhcp` |  `boolean` Optional. Dynamic Host Configuration Protocol, is a network management protocol that automatically assigns IP addresses and other network configuration parameters to devices connecting to a network.  
`staticIpAddress` |  `object (`[StaticIpConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.monitoringPoints/downloadInstallScript#StaticIpConfig)`)` Optional. Static IP configured by the user.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkmanagement.monitoringPoints.downloadConfig`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## MonitoringPointType

The type of the monitoring point.

Enums  
---  
`MONITORING_POINT_TYPE_UNSPECIFIED` | This value should not be used.  
`CONTAINER` | Monitoring Point that runs in a Docker container.  
`KVM` | Monitoring Point that runs in a KVM hypervisor.  
`VMWARE` | Monitoring Point that runs in a VMware hypervisor.  
`HELM` | Monitoring Point that runs on a K8S Helm.  
`GCE_VM` | Monitoring Point that runs as a startup script in a Compute Engine VM.  
`AZURE_VM` | Monitoring Point that runs as a startup script in an Azure VM.  
`AWS_EC2` | Monitoring Point that runs as a startup script in an AWS EC2 instance.  
  
## StaticIpConfig

Static IP address configuration.

JSON representation  
---  
      
    
    {
      "ipAddress": string,
      "netmask": string,
      "gatewayAddress": string,
      "dnsServerAddress": string,
      "dnsServerSecondaryAddress": string,
      "domain": string
    }  
  
Fields  
---  
`ipAddress` |  `string` Required. IP address of the MonitoringPoint.  
`netmask` |  `string` Optional. Networkmask and CIDR range. Example: "255.255.255.0/24"  
`gatewayAddress` |  `string` Required. Gateway IP address. Example: "100.80.40.1".  
`dnsServerAddress` |  `string` Required. DNS server.  
`dnsServerSecondaryAddress` |  `string` Optional. Second DNS server.  
`domain` |  `string` Optional. Domain name of the MonitoringPoint.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
