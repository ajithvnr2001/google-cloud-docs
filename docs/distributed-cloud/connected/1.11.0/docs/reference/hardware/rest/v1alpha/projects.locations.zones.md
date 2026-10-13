---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones
title: REST Resource: projects.locations.zones \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:23.514748+00:00
---

# REST Resource: projects.locations.zones  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.zones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Zone
    * JSON representation
  * State
  * ZoneNetworkConfig
    * JSON representation
  * Subnet
    * JSON representation
  * SubscriptionConfig
    * JSON representation
  * SubscriptionState
  * ProvisioningState
  * Methods



## Resource: Zone

A zone holding a set of hardware.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#State)),
      "contacts": [
        {
          object ([Contact](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/Contact))
        }
      ],
      "ciqUri": string,
      "networkConfig": {
        object ([ZoneNetworkConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#ZoneNetworkConfig))
      },
      "globallyUniqueId": string,
      "subscriptionConfigs": [
        {
          object ([SubscriptionConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#SubscriptionConfig))
        }
      ],
      "provisioningState": enum ([ProvisioningState](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#ProvisioningState)),
      "skipClusterProvisioning": boolean,
      "clusterIntentRequired": boolean,
      "clusterIntentVerified": boolean,
      "aiCapable": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of this zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when this zone was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when this zone was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels associated with this zone as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Optional. Human friendly display name of this zone.  
`state` |  `enum (`[State](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#State)`)` Output only. Current state for this zone.  
`contacts[]` |  `object (`[Contact](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/Contact)`)` Required. The zone points of contact (name, email, phone). Order-dependent: the first contact in the list is the primary contact, second is secondary, etc.  
`ciqUri` |  `string` Output only. Link to the Customer Intake Questionnaire (CIQ) sheet for this zone.  
`networkConfig` |  `object (`[ZoneNetworkConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#ZoneNetworkConfig)`)` Optional. Networking configuration for this zone.  
`globallyUniqueId` |  `string` Output only. Globally unique identifier generated for this Edge Zone.  
`subscriptionConfigs[]` |  `object (`[SubscriptionConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#SubscriptionConfig)`)` Output only. Subscription configurations for this zone.  
`provisioningState` |  `enum (`[ProvisioningState](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#ProvisioningState)`)` Output only. Provisioning state for configurations like MAC addresses.  
`skipClusterProvisioning` |  `boolean` Optional. Whether to skip the cluster provisioning step during factory turnup. If true, indicates that the Kubernetes cluster will be created after the zone's hardware is installed at the customer site.  
`clusterIntentRequired` |  `boolean` Output only. Indicates whether a valid cluster intent must be provided by the customer before accepting the order. If true, the order cannot be accepted until cluster intent is present. This is used to enforce early validation and prevent delays caused by missing configuration.  
`clusterIntentVerified` |  `boolean` Output only. Indicates whether the provided cluster intent has been successfully verified. This flag ensures cluster intent exists before order can be accepted.  
`aiCapable` |  `boolean` Output only. Indicates whether this zone is for Gemini on GDC Software cluster.  
  
## State

Valid states for a zone.

Enums  
---  
`STATE_UNSPECIFIED` | State of the Zone is unspecified.  
`ADDITIONAL_INFO_NEEDED` | More information is required from the customer to make progress.  
`PREPARING` | Google is preparing the Zone.  
`READY_FOR_CUSTOMER_FACTORY_TURNUP_CHECKS` | Factory turnup has succeeded.  
`CUSTOMER_FACTORY_TURNUP_CHECKS_STARTED` | The Zone is running factory turnup checks.  
`READY_FOR_SITE_TURNUP` | The Zone is ready for site turnup.  
`CUSTOMER_FACTORY_TURNUP_CHECKS_FAILED` | The Zone failed in factory turnup checks.  
`ACTIVE` | The Zone is available to use.  
`CANCELLED` | The Zone has been cancelled.  
  
## ZoneNetworkConfig

Networking configuration for a zone.

JSON representation  
---  
      
    
    {
      "machineMgmtIpv4Range": string,
      "kubernetesNodeIpv4Range": string,
      "kubernetesControlPlaneIpv4Range": string,
      "managementIpv4Subnet": {
        object ([Subnet](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#Subnet))
      },
      "kubernetesIpv4Subnet": {
        object ([Subnet](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#Subnet))
      },
      "dnsIpv4Addresses": [
        string
      ],
      "kubernetesPrimaryVlanId": integer
    }  
  
Fields  
---  
`machineMgmtIpv4Range` |  `string` Required. An IPv4 address block for machine management. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per machine in the Zone. Should be in `managementIpv4Subnet`, and disjoint with other address ranges.  
`kubernetesNodeIpv4Range` |  `string` Required. An IPv4 address block for kubernetes nodes. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per machine in the Zone. Should be in `kubernetesIpv4Subnet`, and disjoint with other address ranges.  
`kubernetesControlPlaneIpv4Range` |  `string` Required. An IPv4 address block for kubernetes control plane. Should be a private RFC1918 or public CIDR block large enough to allocate at least one address per cluster in the Zone. Should be in `kubernetesIpv4Subnet`, and disjoint with other address ranges.  
`managementIpv4Subnet` |  `object (`[Subnet](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#Subnet)`)` Required. An IPv4 subnet for the management network.  
`kubernetesIpv4Subnet` |  `object (`[Subnet](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#Subnet)`)` Optional. An IPv4 subnet for the kubernetes network. If unspecified, the kubernetes subnet will be the same as the management subnet.  
`dnsIpv4Addresses[]` |  `string` Optional. DNS nameservers. The GDC Infrastructure will resolve DNS queries via these IPs. If unspecified, Google DNS is used.  
`kubernetesPrimaryVlanId` |  `integer` Optional. Kubernetes VLAN ID. By default, the kubernetes node, including the primary kubernetes network, are in the same VLAN as the machine management network. For network segmentation purposes, these can optionally be separated.  
  
## Subnet

Represents a subnet.

JSON representation  
---  
      
    
    {
      "addressRange": string,
      "defaultGatewayIpAddress": string
    }  
  
Fields  
---  
`addressRange` |  `string` Required. Address range for this subnet in CIDR notation.  
`defaultGatewayIpAddress` |  `string` Required. Default gateway for this subnet.  
  
## SubscriptionConfig

A message to store a subscription configuration.

JSON representation  
---  
      
    
    {
      "subscriptionId": string,
      "billingId": string,
      "state": enum ([SubscriptionState](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#SubscriptionState))
    }  
  
Fields  
---  
`subscriptionId` |  `string` Output only. The unique identifier of the subscription.  
`billingId` |  `string` Output only. The Google Cloud Billing ID that the subscription is created under.  
`state` |  `enum (`[SubscriptionState](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#SubscriptionState)`)` Output only. The current state of the subscription.  
  
## SubscriptionState

Enum to represent the state of the subscription.

Enums  
---  
`SUBSCRIPTION_STATE_UNSPECIFIED` | State is unspecified.  
`ACTIVE` | Active state means that the subscription has been created successfully and billing is happening.  
`INACTIVE` | Inactive means that the subscription has been created successfully, but billing has not started yet.  
`ERROR` | The subscription is in an erroneous state.  
`FAILED_TO_RETRIEVE` | The subscription state failed to be retrieved. This may be a transient issue. The user should retry the request.  
`COMPLETED` | The subscription has been completed, because it has reached the end date.  
  
## ProvisioningState

Valid provisioning states for configurations like MAC addresses.

Enums  
---  
`PROVISIONING_STATE_UNSPECIFIED` | Provisioning state is unspecified.  
`PROVISIONING_REQUIRED` | Provisioning is required. Set by Google.  
`PROVISIONING_IN_PROGRESS` | Provisioning is in progress. Set by customer.  
`PROVISIONING_COMPLETE` | Provisioning is complete. Set by customer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/create)`

|  Creates a new zone in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/delete)`

|  Deletes a zone.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/get)`

|  Gets details of a zone.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/list)`

|  Lists zones in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/patch)`

|  Updates the parameters of a zone.  
  
### `[signal](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/signal)`

|  Signals the state of a zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
