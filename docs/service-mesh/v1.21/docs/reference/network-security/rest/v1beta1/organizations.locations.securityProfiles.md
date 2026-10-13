---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles
title: REST Resource: organizations.locations.securityProfiles \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:09.604927+00:00
---

# REST Resource: organizations.locations.securityProfiles  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles

You are viewing archived v1.21 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)



Send feedback 

#  REST Resource: organizations.locations.securityProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SecurityProfile
    * JSON representation
  * ThreatPreventionProfile
    * JSON representation
  * SeverityOverride
    * JSON representation
  * Severity
  * ThreatAction
  * ThreatOverride
    * JSON representation
  * ThreatType
  * ProfileType
  * Methods



## Resource: SecurityProfile

SecurityProfile is a resource that defines the behavior for one of many ProfileTypes. Next ID: 11

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "type": enum ([ProfileType](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ProfileType)),
    
      // Union field profile can be only one of the following:
      "threatPreventionProfile": {
        object ([ThreatPreventionProfile](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatPreventionProfile))
      }
      // End of list of possible types for union field profile.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfiles/{securityProfile}`.  
`description` |  `string` Optional. An optional description of the profile. Max length 512 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Resource creation timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last resource update timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`type` |  `enum (`[ProfileType](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ProfileType)`)` Immutable. The single ProfileType that the SecurityProfile resource configures.  
Union field `profile`. The behavior for the ProfileType that the SecurityProfile resource is meant to configure. This field must correspond to the ProfileType of the SecurityProfile. `profile` can be only one of the following:  
`threatPreventionProfile` |  `object (`[ThreatPreventionProfile](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatPreventionProfile)`)` The threat prevention configuration for the SecurityProfile.  
  
## ThreatPreventionProfile

ThreatPreventionProfile defines an action for specific threat signatures or severity levels.

JSON representation  
---  
      
    
    {
      "severityOverrides": [
        {
          object ([SeverityOverride](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#SeverityOverride))
        }
      ],
      "threatOverrides": [
        {
          object ([ThreatOverride](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatOverride))
        }
      ]
    }  
  
Fields  
---  
`severityOverrides[]` |  `object (`[SeverityOverride](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#SeverityOverride)`)` Optional. Configuration for overriding threats actions by severity match.  
`threatOverrides[]` |  `object (`[ThreatOverride](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatOverride)`)` Optional. Configuration for overriding threats actions by threatId match. If a threat is matched both by configuration provided in severityOverrides and threatOverrides, the threatOverrides action is applied.  
  
## SeverityOverride

Defines what action to take for a specific severity match.

JSON representation  
---  
      
    
    {
      "severity": enum ([Severity](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#Severity)),
      "action": enum ([ThreatAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatAction))
    }  
  
Fields  
---  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#Severity)`)` Required. Severity level to match.  
`action` |  `enum (`[ThreatAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatAction)`)` Required. Threat action override.  
  
## Severity

Severity level.

Enums  
---  
`SEVERITY_UNSPECIFIED` | Severity level not specified.  
`INFORMATIONAL` | Suspicious events that do not pose an immediate threat, but that are reported to call attention to deeper problems that could possibly exist.  
`LOW` | Warning-level threats that have very little impact on an organization's infrastructure. They usually require local or physical system access and may often result in victim privacy issues and information leakage.  
`MEDIUM` | Minor threats in which impact is minimized, that do not compromise the target or exploits that require an attacker to reside on the same local network as the victim, affect only non-standard configurations or obscure applications, or provide very limited access.  
`HIGH` | Threats that have the ability to become critical but have mitigating factors; for example, they may be difficult to exploit, do not result in elevated privileges, or do not have a large victim pool.  
`CRITICAL` | Serious threats, such as those that affect default installations of widely deployed software, result in root compromise of servers, and the exploit code is widely available to attackers. The attacker usually does not need any special authentication credentials or knowledge about the individual victims and the target does not need to be manipulated into performing any special functions.  
  
## ThreatAction

Threat action override.

Enums  
---  
`THREAT_ACTION_UNSPECIFIED` | Threat action not specified.  
`DEFAULT_ACTION` | The default action (as specified by the vendor) is taken.  
`ALLOW` | The packet matching this rule will be allowed to transmit.  
`ALERT` | The packet matching this rule will be allowed to transmit, but a threat_log entry will be sent to the consumer project.  
`DENY` | The packet matching this rule will be dropped, and a threat_log entry will be sent to the consumer project.  
  
## ThreatOverride

Defines what action to take for a specific threatId match.

JSON representation  
---  
      
    
    {
      "threatId": string,
      "type": enum ([ThreatType](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatType)),
      "action": enum ([ThreatAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatAction))
    }  
  
Fields  
---  
`threatId` |  `string` Required. Vendor-specific ID of a threat to override.  
`type` |  `enum (`[ThreatType](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatType)`)` Output only. Type of the threat (read only).  
`action` |  `enum (`[ThreatAction](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles#ThreatAction)`)` Required. Threat action override. For some threat types, only a subset of actions applies.  
  
## ThreatType

Type of threat.

Enums  
---  
`THREAT_TYPE_UNSPECIFIED` | Type of threat not specified.  
`UNKNOWN` | Type of threat is not derivable from threat ID. An override will be created for all types. Firewall will ignore overridden signature ID's that don't exist in the specific type.  
`VULNERABILITY` | Threats related to system flaws that an attacker might otherwise attempt to exploit.  
`ANTIVIRUS` | Threats related to viruses and malware found in executables and file types.  
`SPYWARE` | Threats related to command-and-control (C2) activity, where spyware on an infected client is collecting data without the user's consent and/or communicating with a remote attacker.  
`DNS` | Threats related to DNS.  
  
## ProfileType

The possible types that the SecurityProfile resource can configure.

Enums  
---  
`PROFILE_TYPE_UNSPECIFIED` | Profile type not specified.  
`THREAT_PREVENTION` | Profile type for threat prevention.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/create)`

|  Creates a new SecurityProfile in a given organization and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/delete)`

|  Deletes a single SecurityProfile.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/get)`

|  Gets details of a single SecurityProfile.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/list)`

|  Lists SecurityProfiles in a given organization and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/patch)`

|  Updates the parameters of a single SecurityProfile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
