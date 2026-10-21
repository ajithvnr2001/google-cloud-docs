---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains
title: REST Resource: projects.locations.global.domains \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:12.888179+00:00
---

# REST Resource: projects.locations.global.domains  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  REST Resource: projects.locations.global.domains Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Domain
    * JSON representation
  * State
  * Trust
    * JSON representation
  * TrustType
  * TrustDirection
  * State
  * Methods



## Resource: Domain

Represents a managed Microsoft Active Directory domain. If the domain is being changed, it will be placed into the UPDATING state, which indicates that the resource is being reconciled. At this point, Get will reflect an intermediate state.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "authorizedNetworks": [
        string
      ],
      "reservedIpRange": string,
      "locations": [
        string
      ],
      "admin": string,
      "fqdn": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#State)),
      "statusMessage": string,
      "trusts": [
        {
          object ([Trust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#Trust))
        }
      ],
      "auditLogsEnabled": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. The unique name of the domain using the form: `projects/{projectId}/locations/global/domains/{domainName}`.  
`labels` |  `map (key: string, value: string)` Optional. Resource labels that can contain user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`authorizedNetworks[]` |  `string` Optional. The full names of the Google Compute Engine [networks](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using domains.patch. The domain is only available on networks listed in `authorizedNetworks`. If CIDR subnets overlap between networks, domain creation will fail.  
`reservedIpRange` |  `string` Required. The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in [Domain].[authorizedNetworks].  
`locations[]` |  `string` Required. Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/] e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.  
`admin` |  `string` Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used.  
`fqdn` |  `string` Output only. The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the instance was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The last update time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#State)`)` Output only. The current state of this domain.  
`statusMessage` |  `string` Output only. Additional information about the current status of this domain, if available.  
`trusts[]` |  `object (`[Trust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#Trust)`)` Output only. The current trusts associated with the domain.  
`auditLogsEnabled` |  `boolean` Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled.  
  
## State

Represents the different states of a managed domain.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | The domain is being created.  
`READY` | The domain has been created and is fully usable.  
`UPDATING` | The domain's configuration is being updated.  
`DELETING` | The domain is being deleted.  
`REPAIRING` | The domain is being repaired and may be unusable. Details can be found in the `statusMessage` field.  
`PERFORMING_MAINTENANCE` | The domain is undergoing maintenance.  
`UNAVAILABLE` | The domain is not serving requests.  
  
## Trust

Represents a relationship between two domains. This allows a controller in one domain to authenticate a user in another domain. If the trust is being changed, it will be placed into the UPDATING state, which indicates that the resource is being reconciled. At this point, Get will reflect an intermediate state.

JSON representation  
---  
      
    
    {
      "targetDomainName": string,
      "trustType": enum ([TrustType](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#TrustType)),
      "trustDirection": enum ([TrustDirection](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#TrustDirection)),
      "selectiveAuthentication": boolean,
      "targetDnsIpAddresses": [
        string
      ],
      "trustHandshakeSecret": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#State_1)),
      "stateDescription": string,
      "lastTrustHeartbeatTime": string
    }  
  
Fields  
---  
`targetDomainName` |  `string` Required. The fully qualified target domain name which will be in trust with the current domain.  
`trustType` |  `enum (`[TrustType](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#TrustType)`)` Required. The type of trust represented by the trust resource.  
`trustDirection` |  `enum (`[TrustDirection](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#TrustDirection)`)` Required. The trust direction, which decides if the current domain is trusted, trusting, or both.  
`selectiveAuthentication` |  `boolean` Optional. The trust authentication type, which decides whether the trusted side has forest/domain wide access or selective access to an approved set of resources.  
`targetDnsIpAddresses[]` |  `string` Required. The target DNS server IP addresses which can resolve the remote domain involved in the trust.  
`trustHandshakeSecret` |  `string` Required. The trust secret used for the handshake with the target domain. This will not be stored.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the instance was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The last update time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains#State_1)`)` Output only. The current state of the trust.  
`stateDescription` |  `string` Output only. Additional information about the current state of the trust, if available.  
`lastTrustHeartbeatTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The last heartbeat time when the trust was known to be connected.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## TrustType

Represents the different inter-forest trust types.

Enums  
---  
`TRUST_TYPE_UNSPECIFIED` | Not set.  
`FOREST` | The forest trust.  
`EXTERNAL` | The external domain trust.  
  
## TrustDirection

Represents the direction of trust. See [System.DirectoryServices.ActiveDirectory.TrustDirection](https://docs.microsoft.com/en-us/dotnet/api/system.directoryservices.activedirectory.trustdirection?view=netframework-4.7.2) for more information.

Enums  
---  
`TRUST_DIRECTION_UNSPECIFIED` | Not set.  
`INBOUND` | The inbound direction represents the trusting side.  
`OUTBOUND` | The outboud direction represents the trusted side.  
`BIDIRECTIONAL` | The bidirectional direction represents the trusted / trusting side.  
  
## State

Represents the different states of a domain trust.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | The domain trust is being created.  
`UPDATING` | The domain trust is being updated.  
`DELETING` | The domain trust is being deleted.  
`CONNECTED` | The domain trust is connected.  
`DISCONNECTED` | The domain trust is disconnected.  
  
## Methods  
  
---  
  
### `[attachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/attachTrust)`

|  Adds an AD trust to a domain.  
  
### `[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/create)`

|  Creates a Microsoft AD domain.  
  
### `[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/delete)`

|  Deletes a domain.  
  
### `[detachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/detachTrust)`

|  Removes an AD trust.  
  
### `[extendSchema](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/extendSchema)`

|  Extend Schema for Domain  
  
### `[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/get)`

|  Gets information about a domain.  
  
### `[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[getLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/getLdapssettings)`

|  Gets the domain ldaps settings.  
  
### `[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/list)`

|  Lists domains in a project.  
  
### `[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/patch)`

|  Updates the metadata and configuration of a domain.  
  
### `[reconfigureTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/reconfigureTrust)`

|  Updates the DNS conditional forwarder.  
  
### `[resetAdminPassword](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/resetAdminPassword)`

|  Resets a domain's administrator password.  
  
### `[restore](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/restore)`

|  RestoreDomain restores domain backup mentioned in the RestoreDomainRequest  
  
### `[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[updateLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/updateLdapssettings)`

|  Patches a single ldaps settings.  
  
### `[validateTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/validateTrust)`

|  Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
