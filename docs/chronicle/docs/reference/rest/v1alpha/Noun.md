---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun/
title: Noun \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:32.181146+00:00
---

# Noun  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Noun Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Domain
    * JSON representation
  * User
    * JSON representation
  * Attribute
    * JSON representation
  * Cloud
    * JSON representation
  * CloudEnvironment
  * Resource
    * JSON representation
  * ResourceType
  * Permission
    * JSON representation
  * PermissionType
  * Role
    * JSON representation
  * Type
  * AccountType
  * TimeOff
    * JSON representation
  * AuthenticationStatus
  * Role
  * Favicon
    * JSON representation
  * DNSRecord
    * JSON representation
  * SSLCertificate
    * JSON representation
  * CertSignature
    * JSON representation
  * Extension
    * JSON representation
  * AuthorityKeyId
    * JSON representation
  * Subject
    * JSON representation
  * EC
    * JSON representation
  * Validity
    * JSON representation
  * PublicKey
    * JSON representation
  * RSA
    * JSON representation
  * PopularityRank
    * JSON representation
  * Artifact
    * JSON representation
  * Tunnels
    * JSON representation
  * ArtifactClient
    * JSON representation
  * Url
    * JSON representation
  * Tracker
    * JSON representation
  * Browser
    * JSON representation
  * BrowserType
  * UrlVisitType
  * Cookie
    * JSON representation
  * CookieSameSite
  * Group
    * JSON representation
  * Process
    * JSON representation
  * File
    * JSON representation
  * FileMetadata
    * JSON representation
  * PeFileMetadata
    * JSON representation
  * FileMetadataPE
    * JSON representation
  * FileMetadataSection
    * JSON representation
  * FileMetadataImports
    * JSON representation
  * FileMetadataPeResourceInfo
    * JSON representation
  * StringToInt64MapEntry
    * JSON representation
  * FileMetadataSignatureInfo
    * JSON representation
  * SignerInfo
    * JSON representation
  * X509
    * JSON representation
  * FileType
  * ExifInfo
    * JSON representation
  * SignatureInfo
    * JSON representation
  * FileMetadataCodesign
    * JSON representation
  * PDFInfo
    * JSON representation
  * NtfsFileMetadata
    * JSON representation
  * TokenElevationType
  * Asset
    * JSON representation
  * Hardware
    * JSON representation
  * PlatformSoftware
    * JSON representation
  * Platform
  * Software
    * JSON representation
  * AssetType
  * DeploymentStatus
  * Registry
    * JSON representation
  * Type
  * Id
    * JSON representation
  * Investigation
    * JSON representation
  * Verdict
  * Reputation
  * Status
  * Reason



The Noun type is used to represent the different entities in an event: principal, src, target, observer, intermediary, and about. It stores attributes known about the entity. For example, if the entity is a device with multiple IP or MAC addresses, it stores the IP and MAC addresses that are relevant to the event.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "domain": {
        object ([Domain](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Domain))
      },
      "artifact": {
        object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Artifact))
      },
      "urlMetadata": {
        object ([Url](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Url))
      },
      "browser": {
        object ([Browser](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Browser))
      },
      "assetId": string,
      "user": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "userManagementChain": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
        }
      ],
      "group": {
        object ([Group](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Group))
      },
      "process": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process))
      },
      "processAncestors": [
        {
          object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process))
        }
      ],
      "asset": {
        object ([Asset](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Asset))
      },
      "ip": [
        string
      ],
      "natIp": [
        string
      ],
      "port": integer,
      "natPort": integer,
      "mac": [
        string
      ],
      "administrativeDomain": string,
      "namespace": string,
      "url": string,
      "file": {
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#File))
      },
      "email": string,
      "registry": {
        object ([Registry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Registry))
      },
      "application": string,
      "platform": enum ([Platform](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Platform)),
      "platformVersion": string,
      "platformPatchLevel": string,
      "cloud": {
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cloud))
      },
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
      },
      "ipLocation": [
        {
          object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
        }
      ],
      "ipGeoArtifact": [
        {
          object ([Artifact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Artifact))
        }
      ],
      "resource": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource))
      },
      "resourceAncestors": [
        {
          object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource))
        }
      ],
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "objectReference": {
        object ([Id](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Id))
      },
      "investigation": {
        object ([Investigation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Investigation))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Network))
      },
      "securityResult": [
        {
          object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/SecurityResult))
        }
      ]
    }  
  
Fields  
---  
`hostname` |  `string` Client hostname or domain name field. Hostname also doubles as the domain for remote entities. This field can be used as an entity indicator for asset entities.  
`domain` |  `object (`[Domain](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Domain)`)` Information about the domain.  
`artifact` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Artifact)`)` Information about an artifact.  
`urlMetadata` |  `object (`[Url](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Url)`)` Information about the URL.  
`browser` |  `object (`[Browser](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Browser)`)` Information about the browser.  
`assetId` |  `string` The asset ID. This field can be used as an entity indicator for asset entities.  
`user` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Information about the user.  
`userManagementChain[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Information about the user's management chain (reporting hierarchy). Note: userManagementChain is only populated when data is exported to BigQuery since recursive fields (e.g. user.managers) are not supported by BigQuery.  
`group` |  `object (`[Group](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Group)`)` Information about the group.  
`process` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process)`)` Information about the process.  
`processAncestors[]` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process)`)` Information about the process's ancestors ordered from immediate ancestor (parent process) to root. Note: processAncestors is only populated when data is exported to BigQuery since recursive fields (e.g. process.parent_process) are not supported by BigQuery.  
`asset` |  `object (`[Asset](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Asset)`)` Information about the asset.  
`ip[]` |  `string` A list of IP addresses associated with a network connection. This field can be used as an entity indicator for asset entities.  
`natIp[]` |  `string` A list of NAT translated IP addresses associated with a network connection.  
`port` |  `integer` Source or destination network port number when a specific network connection is described within an event.  
`natPort` |  `integer` NAT external network port number when a specific network connection is described within an event.  
`mac[]` |  `string` List of MAC addresses associated with a device. This field can be used as an entity indicator for asset entities.  
`administrativeDomain` |  `string` Domain which the device belongs to (for example, the Microsoft Windows domain).  
`namespace` |  `string` Namespace which the device belongs to, such as "AD forest". Uses for this field include Microsoft Windows AD forest, the name of subsidiary, or the name of acquisition. This field can be used along with an asset indicator to identify an asset.  
`url` |  `string` The URL.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#File)`)` Information about the file.  
`email` |  `string` Email address. Only filled in for securityResult.about  
`registry` |  `object (`[Registry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Registry)`)` Registry information.  
`application` |  `string` The name of an application or service. Some SSO solutions only capture the name of a target application such as "Atlassian" or "Chronicle".  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Platform)`)` Platform.  
`platformVersion` |  `string` Platform version. For example, "Microsoft Windows 1803".  
`platformPatchLevel` |  `string` Platform patch level. For example, "Build 17134.48"  
`cloud  
**(deprecated)**` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cloud)`)` This item is deprecated!Cloud metadata. Deprecated: cloud should be populated in entity Attribute as generic metadata (e.g. asset.attribute.cloud).  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` Physical location. For cloud environments, set the region in location.name.  
`ipLocation[]  
**(deprecated)**` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` This item is deprecated!Deprecated: use ipGeoArtifact.location instead.  
`ipGeoArtifact[]` |  `object (`[Artifact](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Artifact)`)` Enriched geographic information corresponding to an IP address. Specifically, location and network data.  
`resource` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource)`)` Information about the resource (e.g. scheduled task, calendar entry). This field should not be used for files, registry, or processes because these objects are already part of Noun.  
`resourceAncestors[]` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource)`)` Information about the resource's ancestors ordered from immediate ancestor (starting with parent resource).  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` This item is deprecated!Labels are key-value pairs. For example: key = "env", value = "prod". Deprecated: labels should be populated in entity Attribute as generic metadata (e.g. user.attribute.labels).  
`objectReference` |  `object (`[Id](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Id)`)` Finding to which the Analyst updated the feedback.  
`investigation` |  `object (`[Investigation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Investigation)`)` Analyst feedback/investigation for alerts.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Network)`)` Network details, including sub-messages with details on each protocol (for example, DHCP, DNS, or HTTP).  
`securityResult[]` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/SecurityResult)`)` A list of security results.  
  
## Domain

Information about a domain.

JSON representation  
---  
      
    
    {
      "name": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "registrar": string,
      "contactEmail": string,
      "whoisServer": string,
      "nameServer": [
        string
      ],
      "creationTime": string,
      "updateTime": string,
      "expirationTime": string,
      "auditUpdateTime": string,
      "status": string,
      "registrant": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "admin": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "tech": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "billing": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "zone": {
        object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
      },
      "whoisRecordRawText": string,
      "registryDataRawText": string,
      "ianaRegistrarId": integer,
      "privateRegistration": boolean,
      "categories": [
        string
      ],
      "favicon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon))
      },
      "jarm": string,
      "lastDnsRecords": [
        {
          object ([DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#DNSRecord))
        }
      ],
      "lastDnsRecordsTime": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SSLCertificate))
      },
      "lastHttpsCertificateTime": string,
      "popularityRanks": [
        {
          object ([PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PopularityRank))
        }
      ],
      "tags": [
        string
      ],
      "whoisTime": string
    }  
  
Fields  
---  
`name` |  `string` The domain name. This field can be used as an entity indicator for Domain entities.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence)`)` The prevalence of the domain within the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First seen timestamp of the domain in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last seen timestamp of the domain in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`registrar` |  `string` Registrar name . FOr example, "Wild West Domains, Inc. (R120-LROR)", "GoDaddy.com, LLC", or "PDR LTD. D/B/A PUBLICDOMAINREGISTRY.COM".  
`contactEmail` |  `string` Contact email address.  
`whoisServer` |  `string` Whois server name.  
`nameServer[]` |  `string` Repeated list of name servers.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Domain creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last updated time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Expiration time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`auditUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Audit updated time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `string` Domain status. See [](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en)<https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en> for meanings of possible values  
`registrant` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Parsed contact information for the registrant of the domain.  
`admin` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Parsed contact information for the administrative contact for the domain.  
`tech` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Parsed contact information for the technical contact for the domain  
`billing` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Parsed contact information for the billing contact of the domain.  
`zone` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` Parsed contact information for the zone.  
`whoisRecordRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` WHOIS raw text.A base64-encoded string.  
`registryDataRawText` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Registry Data raw text.A base64-encoded string.  
`ianaRegistrarId` |  `integer` IANA Registrar ID. See [](https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml)<https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml>  
`privateRegistration` |  `boolean` Indicates whether the domain appears to be using a private registration service to mask the owner's contact information.  
`categories[]` |  `string` Categories assign to the domain as retrieved from VirusTotal.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon)`)` Includes difference hash and MD5 hash of the domain's favicon.  
`jarm` |  `string` Domain's JARM hash.  
`lastDnsRecords[]` |  `object (`[DNSRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#DNSRecord)`)` Domain's DNS records from the last scan.  
`lastDnsRecordsTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date when the DNS records list was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SSLCertificate)`)` SSL certificate object retrieved last time the domain was analyzed.  
`lastHttpsCertificateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the certificate was retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`popularityRanks[]` |  `object (`[PopularityRank](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PopularityRank)`)` Domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc  
`tags[]` |  `string` List of representative attributes.  
`whoisTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date of the last update of the WHOIS record.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## User

Information about a user.

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "userid": string,
      "userDisplayName": string,
      "firstName": string,
      "middleName": string,
      "lastName": string,
      "phoneNumbers": [
        string
      ],
      "personalAddress": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
      },
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute))
      },
      "firstSeenTime": string,
      "accountType": enum ([AccountType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AccountType)),
      "groupid": string,
      "groupIdentifiers": [
        string
      ],
      "windowsSid": string,
      "emailAddresses": [
        string
      ],
      "employeeId": string,
      "title": string,
      "companyName": string,
      "department": [
        string
      ],
      "officeAddress": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
      },
      "managers": [
        {
          object ([User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User))
        }
      ],
      "hireDate": string,
      "terminationDate": string,
      "timeOff": [
        {
          object ([TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#TimeOff))
        }
      ],
      "lastLoginTime": string,
      "lastPasswordChangeTime": string,
      "passwordExpirationTime": string,
      "accountExpirationTime": string,
      "accountLockoutTime": string,
      "lastBadPasswordAttemptTime": string,
      "userAuthenticationStatus": enum ([AuthenticationStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AuthenticationStatus)),
      "roleName": string,
      "roleDescription": string,
      "userRole": enum ([Role](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Role_1))
    }  
  
Fields  
---  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (e.g. a GUID, LDAP, OID, or similar). This field can be used as an entity indicator for user entities.  
`userid` |  `string` The ID of the user. This field can be used as an entity indicator for user entities.  
`userDisplayName` |  `string` The display name of the user (e.g. "John Locke").  
`firstName` |  `string` First name of the user (e.g. "John").  
`middleName` |  `string` Middle name of the user.  
`lastName` |  `string` Last name of the user (e.g. "Locke").  
`phoneNumbers[]` |  `string` Phone numbers for the user.  
`personalAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` Personal address of the user.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute)`)` Generic entity metadata attributes of the user.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first observed time for a user. The value is calculated on the basis of the first time the identifier was observed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountType` |  `enum (`[AccountType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AccountType)`)` Type of user account (for example, service, domain, or cloud). This is somewhat aligned to: [](https://attack.mitre.org/techniques/T1078/)<https://attack.mitre.org/techniques/T1078/>  
`groupid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the group that the user belongs to. Deprecated in favor of the repeated groupIdentifiers field.  
`groupIdentifiers[]` |  `string` Product object identifiers of the group(s) the user belongs to A vendor-specific identifier to uniquely identify the group(s) the user belongs to (a GUID, LDAP OID, or similar).  
`windowsSid` |  `string` The Microsoft Windows SID of the user. This field can be used as an entity indicator for user entities.  
`emailAddresses[]` |  `string` Email addresses of the user. This field can be used as an entity indicator for user entities.  
`employeeId` |  `string` Human capital management identifier. This field can be used as an entity indicator for user entities.  
`title` |  `string` User job title.  
`companyName` |  `string` User job company name.  
`department[]` |  `string` User job department  
`officeAddress` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` User job office location.  
`managers[]` |  `object (`[User](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#User)`)` User job manager(s).  
`hireDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment hire date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`terminationDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User job employment termination date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`timeOff[]` |  `object (`[TimeOff](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#TimeOff)`)` User time off leaves from active work.  
`lastLoginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last login timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastPasswordChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last password change timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`passwordExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User password expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account expiration timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`accountLockoutTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User account lockout timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBadPasswordAttemptTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` User last bad password attempt timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userAuthenticationStatus` |  `enum (`[AuthenticationStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AuthenticationStatus)`)` System authentication status for user.  
`roleName  
**(deprecated)**` |  `string` This item is deprecated!System role name for user. Deprecated: use attribute.roles.  
`roleDescription  
**(deprecated)**` |  `string` This item is deprecated!System role description for user. Deprecated: use attribute.roles.  
`userRole  
**(deprecated)**` |  `enum (`[Role](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Role_1)`)` This item is deprecated!System role for user. Deprecated: use attribute.roles.  
  
## Attribute

Attribute is a container for generic entity attributes including common attributes across core entities (such as, user or asset). For example, Cloud is a generic entity attribute since it can apply to an asset (for example, a VM) or a user (for example, an identity service account).

JSON representation  
---  
      
    
    {
      "cloud": {
        object ([Cloud](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cloud))
      },
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Permission))
        }
      ],
      "roles": [
        {
          object ([Role](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Role))
        }
      ],
      "creationTime": string,
      "lastUpdateTime": string
    }  
  
Fields  
---  
`cloud` |  `object (`[Cloud](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cloud)`)` Cloud metadata attributes such as project ID, account ID, or organizational hierarchy.  
`labels[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` Set of labels for the entity. Should only be used for product labels (for example, Google Cloud resource labels or Azure AD sensitivity labels. Should not be used for arbitrary key-value mappings.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Permission)`)` System permissions for IAM entity (human principal, service account, group).  
`roles[]` |  `object (`[Role](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Role)`)` System IAM roles to be assumed by resources to use the role's permissions for access control.  
`creationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was created or provisioned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the resource or entity was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Cloud

Metadata related to the cloud environment.

JSON representation  
---  
      
    
    {
      "environment": enum ([CloudEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CloudEnvironment)),
      "vpc": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource))
      },
      "project": {
        object ([Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource))
      },
      "availabilityZone": string
    }  
  
Fields  
---  
`environment` |  `enum (`[CloudEnvironment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CloudEnvironment)`)` The Cloud environment.  
`vpc  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource)`)` This item is deprecated!The cloud environment VPC. Deprecated.  
`project  
**(deprecated)**` |  `object (`[Resource](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Resource)`)` This item is deprecated!The cloud environment project information. Deprecated: Use Resource.resource_ancestors  
`availabilityZone` |  `string` The cloud environment availability zone (different from region which is location.name).  
  
## CloudEnvironment

The service provider environment.

Enums  
---  
`UNSPECIFIED_CLOUD_ENVIRONMENT` | Default.  
`GOOGLE_CLOUD_PLATFORM` | Google Cloud Platform.  
`AMAZON_WEB_SERVICES` | Amazon Web Services.  
`MICROSOFT_AZURE` | Microsoft Azure.  
  
## Resource

Information about a resource such as a task, Cloud Storage bucket, database, disk, logical policy, or something similar.

JSON representation  
---  
      
    
    {
      "type": string,
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ResourceType)),
      "resourceSubtype": string,
      "id": string,
      "name": string,
      "parent": string,
      "productObjectId": string,
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute))
      }
    }  
  
Fields  
---  
`type  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use resourceType instead.  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ResourceType)`)` Resource type.  
`resourceSubtype` |  `string` Resource sub-type (e.g. "BigQuery", "Bigtable").  
`id  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use resource.name or resource.product_object_id.  
`name` |  `string` The full name of the resource. For example, Google Cloud: //cloudresourcemanager.googleapis.com/projects/wombat-123, and AWS: arn:aws:iam::123456789012:user/johndoe.  
`parent  
**(deprecated)**` |  `string` This item is deprecated!The parent of the resource. For a database table, the parent is the database. For a storage object, the bucket name. Deprecated: use resourceAncestors.name.  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (a GUID, OID, or similar) This field can be used as an entity indicator for a Resource entity.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute)`)` Generic entity metadata attributes of the resource.  
  
## ResourceType

The type of resource.

Enums  
---  
`UNSPECIFIED` | Default type.  
`MUTEX` | Mutex.  
`TASK` | Task.  
`PIPE` | Named pipe.  
`DEVICE` | Device.  
`FIREWALL_RULE` | Firewall rule.  
`MAILBOX_FOLDER` | Mailbox folder.  
`VPC_NETWORK` | VPC Network.  
`VIRTUAL_MACHINE` | Virtual machine.  
`STORAGE_BUCKET` | Storage bucket.  
`STORAGE_OBJECT` | Storage object.  
`DATABASE` | Database.  
`TABLE` | Data table.  
`CLOUD_PROJECT` | Cloud project.  
`CLOUD_ORGANIZATION` | Cloud organization.  
`SERVICE_ACCOUNT` | Service account.  
`ACCESS_POLICY` | Access policy.  
`CLUSTER` | Cluster.  
`SETTING` | Settings.  
`DATASET` | Dataset.  
`BACKEND_SERVICE` | Endpoint that receive traffic from a load balancer or proxy.  
`POD` | Pod, which is a collection of containers. Often used in Kubernetes.  
`CONTAINER` | Container.  
`FUNCTION` | Cloud function.  
`RUNTIME` | Runtime.  
`IP_ADDRESS` | IP address.  
`DISK` | Disk.  
`VOLUME` | Volume.  
`IMAGE` | Machine image.  
`SNAPSHOT` | Snapshot.  
`REPOSITORY` | Repository.  
`CREDENTIAL` | Credential, e.g. access keys, ssh keys, tokens, certificates.  
`LOAD_BALANCER` | Load balancer.  
`GATEWAY` | Gateway.  
`SUBNET` | Subnet.  
`USER` | User.  
  
## Permission

System permission for resource access and modification.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([PermissionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PermissionType))
    }  
  
Fields  
---  
`name` |  `string` Name of the permission (e.g. chronicle.analyst.updateRule).  
`description` |  `string` Description of the permission (e.g. 'Ability to update detect rules').  
`type` |  `enum (`[PermissionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PermissionType)`)` Type of the permission.  
  
## PermissionType

High level categorizations of permission type.

Enums  
---  
`UNKNOWN_PERMISSION_TYPE` | Default permission type.  
`ADMIN_WRITE` | Administrator write permission.  
`ADMIN_READ` | Administrator read permission.  
`DATA_WRITE` | Data resource access write permission.  
`DATA_READ` | Data resource access read permission.  
  
## Role

System role for resource access and modification.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Type))
    }  
  
Fields  
---  
`name` |  `string` System role name for user.  
`description` |  `string` System role description for user.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Type)`)` System role type for well known roles.  
  
## Type

Well-known system roles.

Enums  
---  
`TYPE_UNSPECIFIED` | Default user role.  
`ADMINISTRATOR` | Product administrator with elevated privileges.  
`SERVICE_ACCOUNT` | System service account for automated privilege access.  
  
## AccountType

User Account Type.

Enums  
---  
`ACCOUNT_TYPE_UNSPECIFIED` | Default user account type.  
`DOMAIN_ACCOUNT_TYPE` | A human account part of some domain in directory services.  
`LOCAL_ACCOUNT_TYPE` | A local machine account.  
`CLOUD_ACCOUNT_TYPE` | A SaaS service account type (such as Slack or GitHub).  
`SERVICE_ACCOUNT_TYPE` | A non-human account for data access.  
`DEFAULT_ACCOUNT_TYPE` | A system built in default account.  
  
## TimeOff

System record for leave/time-off from a Human Capital Management (HCM) system.

JSON representation  
---  
      
    
    {
      "interval": {
        object ([Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval))
      },
      "description": string
    }  
  
Fields  
---  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Interval)`)` Interval duration of the leave.  
`description` |  `string` Description of the leave if available (e.g. 'Vacation').  
  
## AuthenticationStatus

Authentication status, can be used to describe the status of authentication for a user or particular credential.

Enums  
---  
`UNKNOWN_AUTHENTICATION_STATUS` | The default authentication status.  
`ACTIVE` | The authentication method is in active state.  
`SUSPENDED` | The authentication method is in suspended/disabled state.  
`NO_ACTIVE_CREDENTIALS` | The authentication method has no active credentials.  
`DELETED` | The authentication method has been deleted.  
  
## Role

User system roles.

Enums  
---  
`UNKNOWN_ROLE` | Default user role.  
`ADMINISTRATOR` | Product administrator with elevated privileges.  
`SERVICE_ACCOUNT` | System service account for automated privilege access. Deprecated: not a role, instead set User.account_type.This item is deprecated!  
  
## Favicon

Difference hash and MD5 hash of the domain's favicon.

JSON representation  
---  
      
    
    {
      "rawMd5": string,
      "dhash": string
    }  
  
Fields  
---  
`rawMd5` |  `string` Favicon's MD5 hash.  
`dhash` |  `string` Difference hash.  
  
## DNSRecord

DNS record.

JSON representation  
---  
      
    
    {
      "type": string,
      "value": string,
      "ttl": string,
      "priority": string,
      "retry": string,
      "refresh": string,
      "minimum": string,
      "expire": string,
      "serial": string,
      "rname": string
    }  
  
Fields  
---  
`type` |  `string` Type.  
`value` |  `string` Value.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Time to live.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`priority` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Priority.  
`retry` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Retry.  
`refresh` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Refresh.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`minimum` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`expire` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Expire.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`serial` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Serial.  
`rname` |  `string` Rname.  
  
## SSLCertificate

SSL certificate.

JSON representation  
---  
      
    
    {
      "certSignature": {
        object ([CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CertSignature))
      },
      "extension": {
        object ([Extension](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Extension))
      },
      "certExtensions": {
        object
      },
      "firstSeenTime": string,
      "issuer": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Subject))
      },
      "ec": {
        object ([EC](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#EC))
      },
      "serialNumber": string,
      "signatureAlgorithm": string,
      "size": string,
      "subject": {
        object ([Subject](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Subject))
      },
      "thumbprint": string,
      "thumbprintSha256": string,
      "validity": {
        object ([Validity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Validity))
      },
      "version": string,
      "publicKey": {
        object ([PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PublicKey))
      }
    }  
  
Fields  
---  
`certSignature` |  `object (`[CertSignature](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CertSignature)`)` Certificate's signature and algorithm.  
`extension  
**(deprecated)**` |  `object (`[Extension](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Extension)`)` This item is deprecated!(DEPRECATED) certificate's extension.  
`certExtensions` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Certificate's extensions.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date the certificate was first retrieved by VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issuer` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Subject)`)` Certificate's issuer data.  
`ec` |  `object (`[EC](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#EC)`)` EC public key information.  
`serialNumber` |  `string` Certificate's serial number hexdump.  
`signatureAlgorithm` |  `string` Algorithm used for the signature (for example, "sha1RSA").  
`size` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Certificate content length.  
`subject` |  `object (`[Subject](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Subject)`)` Certificate's subject data.  
`thumbprint` |  `string` Certificate's content SHA1 hash.  
`thumbprintSha256` |  `string` Certificate's content SHA256 hash.  
`validity` |  `object (`[Validity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Validity)`)` Certificate's validity period.  
`version` |  `string` Certificate version (typically "V1", "V2" or "V3").  
`publicKey` |  `object (`[PublicKey](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PublicKey)`)` Public key information.  
  
## CertSignature

Certificate's signature and algorithm.

JSON representation  
---  
      
    
    {
      "signature": string,
      "signatureAlgorithm": string
    }  
  
Fields  
---  
`signature` |  `string` Signature.  
`signatureAlgorithm` |  `string` Algorithm.  
  
## Extension

Certificate's extensions.

JSON representation  
---  
      
    
    {
      "ca": boolean,
      "subjectKeyId": string,
      "authorityKeyId": {
        object ([AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AuthorityKeyId))
      },
      "keyUsage": string,
      "caInfoAccess": string,
      "crlDistributionPoints": string,
      "extendedKeyUsage": string,
      "subjectAlternativeName": string,
      "certificatePolicies": string,
      "netscapeCertComment": string,
      "certTemplateNameDc": string,
      "netscapeCertificate": boolean,
      "peLogotype": boolean,
      "oldAuthorityKeyId": boolean
    }  
  
Fields  
---  
`ca` |  `boolean` Whether the subject acts as a certificate authority (CA) or not.  
`subjectKeyId` |  `string` Identifies the public key being certified.  
`authorityKeyId` |  `object (`[AuthorityKeyId](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AuthorityKeyId)`)` Identifies the public key to be used to verify the signature on this certificate or CRL.  
`keyUsage` |  `string` The purpose for which the certified public key is used.  
`caInfoAccess` |  `string` Authority information access locations are URLs that are added to a certificate in its authority information access extension.  
`crlDistributionPoints` |  `string` CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.  
`extendedKeyUsage` |  `string` One or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.  
`subjectAlternativeName` |  `string` Contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.  
`certificatePolicies` |  `string` Different certificate policies will relate to different applications which may use the certified key.  
`netscapeCertComment` |  `string` Used to include free-form text comments inside certificates.  
`certTemplateNameDc` |  `string` BMP data value "DomainController". See MS Q291010.  
`netscapeCertificate` |  `boolean` Identify whether the certificate subject is an SSL client, an SSL server, or a CA.  
`peLogotype` |  `boolean` Whether the certificate includes a logotype.  
`oldAuthorityKeyId` |  `boolean` Whether the certificate has an old authority key identifier extension.  
  
## AuthorityKeyId

Identifies the public key to be used to verify the signature on this certificate or CRL.

JSON representation  
---  
      
    
    {
      "keyid": string,
      "serialNumber": string
    }  
  
Fields  
---  
`keyid` |  `string` Key hexdump.  
`serialNumber` |  `string` Serial number hexdump.  
  
## Subject

Subject data.

JSON representation  
---  
      
    
    {
      "countryName": string,
      "commonName": string,
      "locality": string,
      "organization": string,
      "organizationalUnit": string,
      "stateOrProvinceName": string
    }  
  
Fields  
---  
`countryName` |  `string` C: Country name.  
`commonName` |  `string` CN: CommonName.  
`locality` |  `string` L: Locality.  
`organization` |  `string` O: Organization.  
`organizationalUnit` |  `string` OU: OrganizationalUnit.  
`stateOrProvinceName` |  `string` ST: StateOrProvinceName.  
  
## EC

EC public key information.

JSON representation  
---  
      
    
    {
      "oid": string,
      "pub": string
    }  
  
Fields  
---  
`oid` |  `string` Curve name.  
`pub` |  `string` Public key hexdump.  
  
## Validity

Defines certificate's validity period.

JSON representation  
---  
      
    
    {
      "expiryTime": string,
      "issueTime": string
    }  
  
Fields  
---  
`expiryTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Expiry date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`issueTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Issue date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## PublicKey

Subject public key info.

JSON representation  
---  
      
    
    {
      "algorithm": string,
      "rsa": {
        object ([RSA](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#RSA))
      }
    }  
  
Fields  
---  
`algorithm` |  `string` Any of "RSA", "DSA" or "EC". Indicates the algorithm used to generate the certificate.  
`rsa` |  `object (`[RSA](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#RSA)`)` RSA public key information.  
  
## RSA

RSA public key information.

JSON representation  
---  
      
    
    {
      "keySize": string,
      "modulus": string,
      "exponent": string
    }  
  
Fields  
---  
`keySize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Key size.  
`modulus` |  `string` Key modulus hexdump.  
`exponent` |  `string` Key exponent hexdump.  
  
## PopularityRank

Domain's position in popularity ranks for sources such as Alexa, Quantcast, or Statvoo.

JSON representation  
---  
      
    
    {
      "giver": string,
      "rank": string,
      "ingestionTime": string
    }  
  
Fields  
---  
`giver` |  `string` Name of the rank serial number hexdump.  
`rank` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Rank position.  
`ingestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the rank was ingested.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Artifact

Information about an artifact. The artifact can only be an IP.

JSON representation  
---  
      
    
    {
      "ip": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Network))
      },
      "asOwner": string,
      "asn": string,
      "jarm": string,
      "lastHttpsCertificate": {
        object ([SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SSLCertificate))
      },
      "lastHttpsCertificateDate": string,
      "regionalInternetRegistry": string,
      "tags": [
        string
      ],
      "whois": string,
      "whoisDate": string,
      "tunnels": [
        {
          object ([Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Tunnels))
        }
      ],
      "anonymous": boolean,
      "artifactClient": {
        object ([ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ArtifactClient))
      },
      "risks": [
        string
      ]
    }  
  
Fields  
---  
`ip` |  `string` IP address of the artifact. This field can be used as an entity indicator for an external destination IP entity.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence)`)` The prevalence of the artifact within the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First seen timestamp of the IP in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last seen timestamp of the IP address in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` Location of the Artifact's IP address.  
`network` |  `object (`[Network](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Network)`)` Network information related to the Artifact's IP address.  
`asOwner` |  `string` Owner of the Autonomous System to which the IP address belongs.  
`asn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Autonomous System Number to which the IP address belongs.  
`jarm` |  `string` The JARM hash for the IP address. (<https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a)>.  
`lastHttpsCertificate` |  `object (`[SSLCertificate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SSLCertificate)`)` SSL certificate information about the IP address.  
`lastHttpsCertificateDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Most recent date for the certificate in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`regionalInternetRegistry` |  `string` RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).  
`tags[]` |  `string` Identification attributes  
`whois` |  `string` WHOIS information as returned from the pertinent WHOIS server.  
`whoisDate` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Date of the last update of the WHOIS record in VirusTotal.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tunnels[]` |  `object (`[Tunnels](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Tunnels)`)` VPN tunnels.  
`anonymous` |  `boolean` Whether the VPN tunnels are configured for anonymous browsing or not.  
`artifactClient` |  `object (`[ArtifactClient](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ArtifactClient)`)` Entity or software accessing or utilizing network resources.  
`risks[]` |  `string` This field lists potential risks associated with the network activity.  
  
## Tunnels

VPN tunnels.

JSON representation  
---  
      
    
    {
      "provider": string,
      "type": string
    }  
  
Fields  
---  
`provider` |  `string` The provider of the VPN tunnels being used.  
`type` |  `string` The type of the VPN tunnels.  
  
## ArtifactClient

Entity or software accessing or utilizing network resources.

JSON representation  
---  
      
    
    {
      "behaviors": [
        string
      ],
      "proxies": [
        string
      ]
    }  
  
Fields  
---  
`behaviors[]` |  `string` The behaviors of the client accessing the network.  
`proxies[]` |  `string` The type of proxies used by the client.  
  
## Url

Url.

JSON representation  
---  
      
    
    {
      "url": string,
      "categories": [
        string
      ],
      "favicon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon))
      },
      "htmlMeta": {
        object
      },
      "lastFinalUrl": string,
      "lastHttpResponseCode": integer,
      "lastHttpResponseContentLength": string,
      "lastHttpResponseContentSha256": string,
      "lastHttpResponseCookies": {
        object
      },
      "lastHttpResponseHeaders": {
        object
      },
      "tags": [
        string
      ],
      "title": string,
      "trackers": [
        {
          object ([Tracker](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Tracker))
        }
      ]
    }  
  
Fields  
---  
`url` |  `string` URL.  
`categories[]` |  `string` Categorisation done by VirusTotal partners.  
`favicon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon)`)` Difference hash and MD5 hash of the URL's.  
`htmlMeta` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Meta tags (only for URLs downloading HTML).  
`lastFinalUrl` |  `string` If the original URL redirects, where does it end.  
`lastHttpResponseCode` |  `integer` HTTP response code of the last response.  
`lastHttpResponseContentLength` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Length in bytes of the content received.  
`lastHttpResponseContentSha256` |  `string` URL response body's SHA256 hash.  
`lastHttpResponseCookies` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Website's cookies.  
`lastHttpResponseHeaders` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Headers and values of the last HTTP response.  
`tags[]` |  `string` Tags.  
`title` |  `string` Webpage title.  
`trackers[]` |  `object (`[Tracker](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Tracker)`)` Trackers found in the URL in a historical manner.  
  
## Tracker

URL Tracker.

JSON representation  
---  
      
    
    {
      "tracker": string,
      "id": string,
      "timestamp": string,
      "url": string
    }  
  
Fields  
---  
`tracker` |  `string` Tracker name.  
`id` |  `string` Tracker ID, if available.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Tracker ingestion date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`url` |  `string` Tracker script URL.  
  
## Browser

Information about a browser.

JSON representation  
---  
      
    
    {
      "browserType": enum ([BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#BrowserType)),
      "browserVersion": string,
      "firstVisitTime": string,
      "lastVisitTime": string,
      "profile": string,
      "typed": boolean,
      "visitType": enum ([UrlVisitType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#UrlVisitType)),
      "hidden": boolean,
      "requestOriginUri": string,
      "visitCount": string,
      "visitCountCriteria": string,
      "indexedContent": string,
      "firstBookmarkedTime": string,
      "cookies": [
        {
          object ([Cookie](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cookie))
        }
      ]
    }  
  
Fields  
---  
`browserType` |  `enum (`[BrowserType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#BrowserType)`)` The browser that recorded the history entry (e.g. "Chrome", "Firefox", "Safari", etc.).  
`browserVersion` |  `string` The browser version.  
`firstVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the initial visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastVisitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the most recent visit to the URL.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`profile` |  `string` The browser profile associated with the history entry.  
`typed` |  `boolean` A boolean value indicating if the URL was typed by the user.  
`visitType` |  `enum (`[UrlVisitType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#UrlVisitType)`)` Describes the type of navigation or visit (e.g., direct, redirect, etc.).  
`hidden` |  `boolean` A boolean value indicating if the history entry is hidden.  
`requestOriginUri` |  `string` Indicates the URI from which the current visit originated.  
`visitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of times the Url has been visited.  
`visitCountCriteria` |  `string` Describes the criteria used to calculate the visitCount.  
`indexedContent` |  `string` Represents the textual content of a web page. This field should be kept short. Large strings may affect latency and payload sizes.  
`firstBookmarkedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp indicating the first time the URL was bookmarked.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cookies[]` |  `object (`[Cookie](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Cookie)`)` Information about the cookies.  
  
## BrowserType

The name of the browser.

Enums  
---  
`BROWSER_TYPE_UNSPECIFIED` | Default value.  
`CHROME` | Chrome.  
`FIREFOX` | Firefox.  
`SAFARI` | Safari.  
`INTERNET_EXPLORER` | Internet Explorer.  
`EDGE` | Edge.  
`OPERA` | Opera.  
  
## UrlVisitType

The type of visit to a URL.

Enums  
---  
`URL_VISIT_TYPE_UNSPECIFIED` | Default value.  
`LINK` | The user clicked a link.  
`TYPED` | The user typed a URL.  
`AUTO_BOOKMARK` | The user bookmarked the URL.  
`AUTO_SUBFRAME` | Loaded in a nested subframe by the parent frame.  
`MANUAL_SUBFRAME` | Loaded in a nested subframe by the user.  
`GENERATED` | The user clicked on auto generated link in browser address bar.  
`AUTO_TOPLEVEL` | The page was loaded through command line or is the starting page.  
`FORM_SUBMIT` | The user submitted a form.  
`RELOAD` | The user reloaded the page.  
`KEYWORD` | The Url was generated by a keyword search configured by user.  
`KEYWORD_GENERATED` | Corresponds to a visit generated by a keyword search.  
  
## Cookie

Browser cookie.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string,
      "domain": string,
      "path": string,
      "expirationTime": string,
      "httpOnly": boolean,
      "secure": boolean,
      "maxAge": string,
      "sameSite": enum ([CookieSameSite](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CookieSameSite)),
      "session": boolean,
      "partitioned": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique name identifying the cookie.  
`value` |  `string` The data stored within the cookie.  
`domain` |  `string` The domain for which the cookie is valid.  
`path` |  `string` The URL path for which the cookie is valid.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The date and time when the cookie will expire.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`httpOnly` |  `boolean` Indicates if the cookie is inaccessible via client-side scripts (e.g., JavaScript).  
`secure` |  `boolean` Indicates if the cookie should only be sent over secure HTTPS connections.  
`maxAge` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The maximum age of the cookie in seconds.  
`sameSite` |  `enum (`[CookieSameSite](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#CookieSameSite)`)` Affects cross-site request behavior.  
`session` |  `boolean` Indicates if the cookie is persistent.  
`partitioned` |  `boolean` Shows if the cookies is stored using partitioned storage.  
  
## CookieSameSite

The SameSite attribute of a cookie.

Enums  
---  
`COOKIE_SAME_SITE_UNSPECIFIED` | Default value.  
`STRICT` | Corresponds to SameSite=Strict.  
`LAX` | Corresponds to SameSite=Lax.  
`NONE` | Corresponds to SameSite=None.  
  
## Group

Information about an organizational group.

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "creationTime": string,
      "groupDisplayName": string,
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute))
      },
      "emailAddresses": [
        string
      ],
      "windowsSid": string
    }  
  
Fields  
---  
`productObjectId` |  `string` Product globally unique user object identifier, such as an LDAP Object Identifier.  
`creationTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Group creation time. Deprecated: creationTime should be populated in Attribute as generic metadata.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`groupDisplayName` |  `string` Group display name. e.g. "Finance".  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute)`)` Generic entity metadata attributes of the group.  
`emailAddresses[]` |  `string` Email addresses of the group.  
`windowsSid` |  `string` Microsoft Windows SID of the group.  
  
## Process

Information about a process.

JSON representation  
---  
      
    
    {
      "pid": string,
      "parentPid": string,
      "parentProcess": {
        object ([Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process))
      },
      "file": {
        object ([File](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#File))
      },
      "commandLine": string,
      "commandLineHistory": [
        string
      ],
      "productSpecificProcessId": string,
      "accessMask": string,
      "integrityLevelRid": string,
      "euid": string,
      "ruid": string,
      "egid": string,
      "rgid": string,
      "pgid": string,
      "sessionLeaderPid": string,
      "tty": string,
      "tokenElevationType": enum ([TokenElevationType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#TokenElevationType)),
      "productSpecificParentProcessId": string
    }  
  
Fields  
---  
`pid` |  `string` The process ID. This field can be used as an entity indicator for process entities.  
`parentPid  
**(deprecated)**` |  `string` This item is deprecated!The ID of the parent process. Deprecated: use parentProcess.pid instead.  
`parentProcess` |  `object (`[Process](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Process)`)` Information about the parent process.  
`file` |  `object (`[File](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#File)`)` Information about the file in use by the process.  
`commandLine` |  `string` The command line command that created the process. This field can be used as an entity indicator for process entities.  
`commandLineHistory[]` |  `string` The command line history of the process.  
`productSpecificProcessId` |  `string` A product specific process id.  
`accessMask` |  `string` A bit mask representing the level of access.  
`integrityLevelRid` |  `string` The Microsoft Windows integrity level relative ID (RID) of the process.  
`euid` |  `string` The effective user ID of the process.  
`ruid` |  `string` The real user ID of the process.  
`egid` |  `string` The effective group ID of the process.  
`rgid` |  `string` The real group ID of the process.  
`pgid` |  `string` The identifier that points to the process group ID leader.  
`sessionLeaderPid` |  `string` The process ID of the session leader process.  
`tty` |  `string` The teletype terminal which the command was executed within.  
`tokenElevationType` |  `enum (`[TokenElevationType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#TokenElevationType)`)` The elevation type of the process on Microsoft Windows. This determines if any privileges are removed when UAC is enabled.  
`productSpecificParentProcessId  
**(deprecated)**` |  `string` This item is deprecated!A product specific id for the parent process. Please use parentProcess.product_specific_process_id instead.  
  
## File

Information about a file.

JSON representation  
---  
      
    
    {
      "sha256": string,
      "md5": string,
      "sha1": string,
      "size": string,
      "fullPath": string,
      "mimeType": string,
      "fileMetadata": {
        object ([FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadata))
      },
      "securityResult": {
        object ([SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/SecurityResult))
      },
      "peFile": {
        object ([FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataPE))
      },
      "ssdeep": string,
      "vhash": string,
      "ahash": string,
      "authentihash": string,
      "symhash": string,
      "fileType": enum ([FileType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileType)),
      "capabilitiesTags": [
        string
      ],
      "names": [
        string
      ],
      "tags": [
        string
      ],
      "lastModificationTime": string,
      "createTime": string,
      "lastAccessTime": string,
      "prevalence": {
        object ([Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence))
      },
      "firstSeenTime": string,
      "lastSeenTime": string,
      "statMode": string,
      "statInode": string,
      "statDev": string,
      "statNlink": string,
      "statFlags": integer,
      "lastAnalysisTime": string,
      "embeddedUrls": [
        string
      ],
      "embeddedDomains": [
        string
      ],
      "embeddedIps": [
        string
      ],
      "exifInfo": {
        object ([ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ExifInfo))
      },
      "signatureInfo": {
        object ([SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SignatureInfo))
      },
      "pdfInfo": {
        object ([PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PDFInfo))
      },
      "firstSubmissionTime": string,
      "lastSubmissionTime": string,
      "mainIcon": {
        object ([Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon))
      },
      "ntfs": {
        object ([NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#NtfsFileMetadata))
      }
    }  
  
Fields  
---  
`sha256` |  `string` The SHA256 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`md5` |  `string` The MD5 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`sha1` |  `string` The SHA1 hash of the file, as a hex-encoded string. This field can be used as an entity indicator for file entities.  
`size` |  `string` The size of the file in bytes.  
`fullPath` |  `string` The full path identifying the location of the file on the system. This field can be used as an entity indicator for file entities.  
`mimeType` |  `string` The MIME (Multipurpose Internet Mail Extensions) type of the file, for example "PE", "PDF", or "powershell script".  
`fileMetadata  
**(deprecated)**` |  `object (`[FileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadata)`)` This item is deprecated!Metadata associated with the file. Deprecate FileMetadata in favor of using fields in File.  
`securityResult` |  `object (`[SecurityResult](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/SecurityResult)`)` Google Cloud Threat Intelligence (GCTI) security result for the file including threat context and detection metadata.  
`peFile` |  `object (`[FileMetadataPE](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataPE)`)` Metadata about the Portable Executable (PE) file.  
`ssdeep` |  `string` Ssdeep of the file  
`vhash` |  `string` Vhash of the file.  
`ahash  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. Use authentihash instead.  
`authentihash` |  `string` Authentihash of the file.  
`symhash` |  `string` SymHash of the file. Used for Mach-O (e.g. MacOS) binaries, to identify similar files based on their symbol table.  
`fileType` |  `enum (`[FileType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileType)`)` FileType field.  
`capabilitiesTags[]` |  `string` Capabilities tags.  
`names[]` |  `string` Names fields.  
`tags[]` |  `string` Tags for the file.  
`lastModificationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastAccessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the file was accessed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`prevalence` |  `object (`[Prevalence](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Prevalence)`)` Prevalence of the file hash in the customer's environment.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was first seen in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was last seen in the customer's environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`statMode` |  `string` The mode of the file. A bit string indicating the permissions and privileges of the file.  
`statInode` |  `string` The file identifier. Unique identifier of object within a file system.  
`statDev` |  `string` The file system identifier to which the object belongs.  
`statNlink` |  `string` Number of links to file.  
`statFlags` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` User defined flags for file.  
`lastAnalysisTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp the file was last analysed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`embeddedUrls[]` |  `string` Embedded urls found in the file.  
`embeddedDomains[]` |  `string` Embedded domains found in the file.  
`embeddedIps[]` |  `string` Embedded IP addresses found in the file.  
`exifInfo` |  `object (`[ExifInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#ExifInfo)`)` Exif metadata from different file formats extracted by exiftool.  
`signatureInfo` |  `object (`[SignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SignatureInfo)`)` File signature information extracted from different tools.  
`pdfInfo` |  `object (`[PDFInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PDFInfo)`)` Information about the PDF file structure.  
`firstSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` First submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSubmissionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last submission time of the file.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mainIcon` |  `object (`[Favicon](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Favicon)`)` Icon's relevant hashes.  
`ntfs` |  `object (`[NtfsFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#NtfsFileMetadata)`)` NTFS metadata.  
  
## FileMetadata

Metadata about a file. Place metadata about different file types here, for example data from the Microsoft Windows VersionInfo block or digital signer details. Use a different sub-message per file type.

JSON representation  
---  
      
    
    {
      "pe": {
        object ([PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PeFileMetadata))
      }
    }  
  
Fields  
---  
`pe  
**(deprecated)**` |  `object (`[PeFileMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PeFileMetadata)`)` This item is deprecated!Metadata for Microsoft Windows PE files. Deprecate PeFileMetadata in favor of single File proto.  
  
## PeFileMetadata

Metadata about a Microsoft Windows Portable Executable.

JSON representation  
---  
      
    
    {
      "importHash": string
    }  
  
Fields  
---  
`importHash` |  `string` Hash of PE imports.  
  
## FileMetadataPE

Metadata about the Portable Executable (PE) file.

JSON representation  
---  
      
    
    {
      "imphash": string,
      "entryPoint": string,
      "entryPointExiftool": string,
      "compilationTime": string,
      "compilationExiftoolTime": string,
      "section": [
        {
          object ([FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSection))
        }
      ],
      "imports": [
        {
          object ([FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataImports))
        }
      ],
      "resource": [
        {
          object ([FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataPeResourceInfo))
        }
      ],
      "resourcesTypeCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#StringToInt64MapEntry))
        }
      ],
      "resourcesLanguageCount": [
        {
          object ([StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#StringToInt64MapEntry))
        }
      ],
      "resourcesTypeCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "resourcesLanguageCountStr": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "signatureInfo": {
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSignatureInfo))
      }
    }  
  
Fields  
---  
`imphash` |  `string` Imphash of the file.  
`entryPoint` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.pe-entry-point.  
`entryPointExiftool` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` info.exiftool.EntryPoint.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.pe-timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`compilationExiftoolTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` info.exiftool.TimeStamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`section[]` |  `object (`[FileMetadataSection](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSection)`)` FilemetadataSection fields.  
`imports[]` |  `object (`[FileMetadataImports](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataImports)`)` FilemetadataImports fields.  
`resource[]` |  `object (`[FileMetadataPeResourceInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataPeResourceInfo)`)` FilemetadataPeResourceInfo fields.  
`resourcesTypeCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resourcesTypeCountStr.  
`resourcesLanguageCount[]  
**(deprecated)**` |  `object (`[StringToInt64MapEntry](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#StringToInt64MapEntry)`)` This item is deprecated!Deprecated: use resourcesLanguageCountStr.  
`resourcesTypeCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` Number of resources by resource type. Example: RT_ICON: 10, RT_DIALOG: 5  
`resourcesLanguageCountStr[]` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` Number of resources by language. Example: NEUTRAL: 20, ENGLISH US: 10  
`signatureInfo  
**(deprecated)**` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSignatureInfo)`)` This item is deprecated!FilemetadataSignatureInfo field. deprecated, user File.signature_info instead.  
  
## FileMetadataSection

File metadata section.

JSON representation  
---  
      
    
    {
      "name": string,
      "entropy": number,
      "rawSizeBytes": string,
      "virtualSizeBytes": string,
      "md5Hex": string
    }  
  
Fields  
---  
`name` |  `string` Name of the section.  
`entropy` |  `number` Entropy of the section.  
`rawSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Raw file size in bytes.  
`virtualSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Virtual file size in bytes.  
`md5Hex` |  `string` MD5 hex of the file.  
  
## FileMetadataImports

File metadata imports.

JSON representation  
---  
      
    
    {
      "library": string,
      "functions": [
        string
      ]
    }  
  
Fields  
---  
`library` |  `string` Library field.  
`functions[]` |  `string` Function field.  
  
## FileMetadataPeResourceInfo

File metadata for PE resource.

JSON representation  
---  
      
    
    {
      "sha256Hex": string,
      "filetypeMagic": string,
      "languageCode": string,
      "entropy": number,
      "fileType": string
    }  
  
Fields  
---  
`sha256Hex` |  `string` SHA256_hex field..  
`filetypeMagic` |  `string` Type of resource content, as identified by the magic Python module.  
`languageCode` |  `string` Human-readable version of the language and sublanguage identifiers, as defined in the Microsoft Windows PE specification. Examples: | Language | Sublanguage | Field value | | LANG_NEUTRAL | SUBLANG_NEUTRAL | NEUTRAL | | LANG_FRENCH | - | FRENCH | | LANG_ENGLISH | SUBLANG_ENGLISH US | ENGLISH US |  
`entropy` |  `number` Entropy of the resource.  
`fileType` |  `string` File type. Note that this value may not match any of the well-known type identifiers defined in the ResourceType enum.  
  
## StringToInt64MapEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Key field.  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Value field.  
  
## FileMetadataSignatureInfo

Signature information.

JSON representation  
---  
      
    
    {
      "verificationMessage": string,
      "verified": boolean,
      "signer": [
        string
      ],
      "signers": [
        {
          object ([SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SignerInfo))
        }
      ],
      "x509": [
        {
          object ([X509](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#X509))
        }
      ]
    }  
  
Fields  
---  
`verificationMessage` |  `string` Status of the certificate. Valid values are "Signed", "Unsigned" or a description of the certificate anomaly, if found.  
`verified` |  `boolean` True if verificationMessage == "Signed"  
`signer[]  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: use signers field.  
`signers[]` |  `object (`[SignerInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#SignerInfo)`)` File metadata signer information. The order of the signers matters. Each element is a higher level authority, being the last the root authority.  
`x509[]` |  `object (`[X509](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#X509)`)` List of certificates.  
  
## SignerInfo

File metadata related to the signer information.

JSON representation  
---  
      
    
    {
      "name": string,
      "status": string,
      "validUsage": string,
      "certIssuer": string
    }  
  
Fields  
---  
`name` |  `string` Common name of the signers/certificate. The order of the signers matters. Each element is a higher level authority, the last being the root authority.  
`status` |  `string` It can say "Valid" or state the problem with the certificate if any (e.g. "This certificate or one of the certificates in the certificate chain is not time valid.").  
`validUsage` |  `string` Indicates which situations the certificate is valid for (e.g. "Code Signing").  
`certIssuer` |  `string` Company that issued the certificate.  
  
## X509

File certificate.

JSON representation  
---  
      
    
    {
      "name": string,
      "algorithm": string,
      "thumbprint": string,
      "certIssuer": string,
      "serialNumber": string
    }  
  
Fields  
---  
`name` |  `string` Certificate name.  
`algorithm` |  `string` Certificate algorithm.  
`thumbprint` |  `string` Certificate thumbprint.  
`certIssuer` |  `string` Issuer of the certificate.  
`serialNumber` |  `string` Certificate serial number.  
  
## FileType

The file type, for example Microsoft Windows executable.

Enums  
---  
`FILE_TYPE_UNSPECIFIED` | File type is UNSPECIFIED.  
`FILE_TYPE_PE_EXE` | File type is PE_EXE.  
`FILE_TYPE_PE_DLL` | Although DLLs are actually portable executables, this value enables the file type to be identified separately. File type is PE_DLL.  
`FILE_TYPE_MSI` | File type is MSI.  
`FILE_TYPE_NE_EXE` | File type is NE_EXE.  
`FILE_TYPE_NE_DLL` | File type is NE_DLL.  
`FILE_TYPE_DOS_EXE` | File type is DOS_EXE.  
`FILE_TYPE_DOS_COM` | File type is DOS_COM.  
`FILE_TYPE_COFF` | File type is COFF.  
`FILE_TYPE_ELF` | File type is ELF.  
`FILE_TYPE_LINUX_KERNEL` | File type is LINUX_KERNEL.  
`FILE_TYPE_RPM` | File type is RPM.  
`FILE_TYPE_LINUX` | File type is LINUX.  
`FILE_TYPE_MACH_O` | File type is MACH_O.  
`FILE_TYPE_JAVA_BYTECODE` | File type is JAVA_BYTECODE.  
`FILE_TYPE_DMG` | File type is DMG.  
`FILE_TYPE_DEB` | File type is DEB.  
`FILE_TYPE_PKG` | File type is PKG.  
`FILE_TYPE_PYC` | File type is PYC.  
`FILE_TYPE_LNK` | File type is LNK.  
`FILE_TYPE_DESKTOP_ENTRY` | File type is DESKTOP_ENTRY.  
`FILE_TYPE_JPEG` | File type is JPEG.  
`FILE_TYPE_TIFF` | File type is TIFF.  
`FILE_TYPE_GIF` | File type is GIF.  
`FILE_TYPE_PNG` | File type is PNG.  
`FILE_TYPE_BMP` | File type is BMP.  
`FILE_TYPE_GIMP` | File type is GIMP.  
`FILE_TYPE_IN_DESIGN` | File type is Adobe InDesign.  
`FILE_TYPE_PSD` | File type is PSD. Adobe Photoshop.  
`FILE_TYPE_TARGA` | File type is TARGA.  
`FILE_TYPE_XWD` | File type is XWD.  
`FILE_TYPE_DIB` | File type is DIB.  
`FILE_TYPE_JNG` | File type is JNG.  
`FILE_TYPE_ICO` | File type is ICO.  
`FILE_TYPE_FPX` | File type is FPX.  
`FILE_TYPE_EPS` | File type is EPS.  
`FILE_TYPE_SVG` | File type is SVG.  
`FILE_TYPE_EMF` | File type is EMF.  
`FILE_TYPE_WEBP` | File type is WEBP.  
`FILE_TYPE_DWG` | File type is DWG.  
`FILE_TYPE_DXF` | File type is DXF.  
`FILE_TYPE_THREEDS` | File type is 3DS.  
`FILE_TYPE_OGG` | File type is OGG.  
`FILE_TYPE_FLC` | File type is FLC.  
`FILE_TYPE_FLI` | File type is FLI.  
`FILE_TYPE_MP3` | File type is MP3.  
`FILE_TYPE_FLAC` | File type is FLAC.  
`FILE_TYPE_WAV` | File type is WAV.  
`FILE_TYPE_MIDI` | File type is MIDI.  
`FILE_TYPE_AVI` | File type is AVI.  
`FILE_TYPE_MPEG` | File type is MPEG.  
`FILE_TYPE_QUICKTIME` | File type is QUICKTIME.  
`FILE_TYPE_ASF` | File type is ASF.  
`FILE_TYPE_DIVX` | File type is DIVX.  
`FILE_TYPE_FLV` | File type is FLV.  
`FILE_TYPE_WMA` | File type is WMA.  
`FILE_TYPE_WMV` | File type is WMV.  
`FILE_TYPE_RM` | File type is RM. RealMedia type.  
`FILE_TYPE_MOV` | File type is MOV.  
`FILE_TYPE_MP4` | File type is MP4.  
`FILE_TYPE_T3GP` | File type is T3GP.  
`FILE_TYPE_WEBM` | File type is WEBM.  
`FILE_TYPE_MKV` | File type is MKV.  
`FILE_TYPE_PDF` | File type is PDF.  
`FILE_TYPE_PS` | File type is PS.  
`FILE_TYPE_DOC` | File type is DOC.  
`FILE_TYPE_DOCX` | File type is DOCX.  
`FILE_TYPE_PPT` | File type is PPT.  
`FILE_TYPE_PPTX` | File type is PPTX.  
`FILE_TYPE_XLS` | File type is XLS.  
`FILE_TYPE_XLSX` | File type is XLSX.  
`FILE_TYPE_RTF` | File type is RTF.  
`FILE_TYPE_PPSX` | File type is PPSX.  
`FILE_TYPE_ODP` | File type is ODP.  
`FILE_TYPE_ODS` | File type is ODS.  
`FILE_TYPE_ODT` | File type is ODT.  
`FILE_TYPE_HWP` | File type is HWP.  
`FILE_TYPE_GUL` | File type is GUL.  
`FILE_TYPE_ODF` | File type is ODF.  
`FILE_TYPE_ODG` | File type is ODG.  
`FILE_TYPE_ONE_NOTE` | File type is ONE_NOTE.  
`FILE_TYPE_OOXML` | File type is OOXML.  
`FILE_TYPE_SLK` | File type is SLK.  
`FILE_TYPE_EBOOK` | File type is EBOOK.  
`FILE_TYPE_LATEX` | File type is LATEX.  
`FILE_TYPE_TTF` | File type is TTF.  
`FILE_TYPE_EOT` | File type is EOT.  
`FILE_TYPE_WOFF` | File type is WOFF.  
`FILE_TYPE_CHM` | File type is CHM.  
`FILE_TYPE_ZIP` | File type is ZIP.  
`FILE_TYPE_GZIP` | File type is GZIP.  
`FILE_TYPE_BZIP` | File type is BZIP.  
`FILE_TYPE_RZIP` | File type is RZIP.  
`FILE_TYPE_DZIP` | File type is DZIP.  
`FILE_TYPE_SEVENZIP` | File type is SEVENZIP.  
`FILE_TYPE_CAB` | File type is CAB.  
`FILE_TYPE_JAR` | File type is JAR.  
`FILE_TYPE_RAR` | File type is RAR.  
`FILE_TYPE_MSCOMPRESS` | File type is MSCOMPRESS.  
`FILE_TYPE_ACE` | File type is ACE.  
`FILE_TYPE_ARC` | File type is ARC.  
`FILE_TYPE_ARJ` | File type is ARJ.  
`FILE_TYPE_ASD` | File type is ASD.  
`FILE_TYPE_BLACKHOLE` | File type is BLACKHOLE.  
`FILE_TYPE_KGB` | File type is KGB.  
`FILE_TYPE_ZLIB` | File type is ZLIB.  
`FILE_TYPE_TAR` | File type is TAR.  
`FILE_TYPE_ZST` | File type is ZST.  
`FILE_TYPE_LZFSE` | File type is LZFSE.  
`FILE_TYPE_PYTHON_WHL` | File type is PYTHON_WHL.  
`FILE_TYPE_PYTHON_PKG` | File type is PYTHON_PKG.  
`FILE_TYPE_MSIX` | File type is MSIX, new Windows app package format.  
`FILE_TYPE_TEXT` | File type is TEXT.  
`FILE_TYPE_SCRIPT` | File type is SCRIPT.  
`FILE_TYPE_PHP` | File type is PHP.  
`FILE_TYPE_PYTHON` | File type is PYTHON.  
`FILE_TYPE_PERL` | File type is PERL.  
`FILE_TYPE_RUBY` | File type is RUBY.  
`FILE_TYPE_C` | File type is C.  
`FILE_TYPE_CPP` | File type is CPP.  
`FILE_TYPE_JAVA` | File type is JAVA.  
`FILE_TYPE_SHELLSCRIPT` | File type is SHELLSCRIPT.  
`FILE_TYPE_PASCAL` | File type is PASCAL.  
`FILE_TYPE_AWK` | File type is AWK.  
`FILE_TYPE_DYALOG` | File type is DYALOG.  
`FILE_TYPE_FORTRAN` | File type is FORTRAN.  
`FILE_TYPE_JAVASCRIPT` | File type is JAVASCRIPT.  
`FILE_TYPE_POWERSHELL` | File type is POWERSHELL.  
`FILE_TYPE_VBA` | File type is VBA.  
`FILE_TYPE_M4` | File type is M4.  
`FILE_TYPE_OBJETIVEC` | File type is OBJETIVEC.  
`FILE_TYPE_JMOD` | File type is JMOD.  
`FILE_TYPE_MAKEFILE` | File type is MAKEFILE.  
`FILE_TYPE_INI` | File type is INI.  
`FILE_TYPE_CLJ` | File type is CLJ.  
`FILE_TYPE_PDB` | File type is PDB.  
`FILE_TYPE_SQL` | File type is SQL.  
`FILE_TYPE_NEKO` | File type is NEKO.  
`FILE_TYPE_WER` | File type is WER.  
`FILE_TYPE_GOLANG` | File type is GOLANG.  
`FILE_TYPE_M3U` | File type is M3U.  
`FILE_TYPE_BAT` | File type is BAT, Windows .bat/.cmd (old files are tagged as SHELLSCRIPT).  
`FILE_TYPE_MSC` | File type is MSC, Microsoft Management Console (MMC).  
`FILE_TYPE_RDP` | File type is RDP, Microsoft Remote Desktop Protocol (RDP) file.  
`FILE_TYPE_SYMBIAN` | File type is SYMBIAN.  
`FILE_TYPE_PALMOS` | File type is PALMOS.  
`FILE_TYPE_WINCE` | File type is WINCE.  
`FILE_TYPE_ANDROID` | File type is ANDROID.  
`FILE_TYPE_IPHONE` | File type is IPHONE.  
`FILE_TYPE_HTML` | File type is HTML.  
`FILE_TYPE_XML` | File type is XML.  
`FILE_TYPE_SWF` | File type is SWF.  
`FILE_TYPE_FLA` | File type is FLA.  
`FILE_TYPE_COOKIE` | File type is COOKIE.  
`FILE_TYPE_TORRENT` | File type is TORRENT.  
`FILE_TYPE_EMAIL_TYPE` | File type is EMAIL_TYPE.  
`FILE_TYPE_OUTLOOK` | File type is OUTLOOK.  
`FILE_TYPE_SGML` | File type is SGML.  
`FILE_TYPE_JSON` | File type is JSON.  
`FILE_TYPE_CSV` | File type is CSV.  
`FILE_TYPE_HTA` | File type is HTA (HTML Application).  
`FILE_TYPE_INTERNET_SHORTCUT` | File type is MSHTML .url.  
`FILE_TYPE_CAP` | File type is CAP.  
`FILE_TYPE_ISOIMAGE` | File type is ISOIMAGE.  
`FILE_TYPE_SQUASHFS` | File type is SQUASHFS.  
`FILE_TYPE_VHD` | File type is VHD.  
`FILE_TYPE_APPLE` | File type is APPLE.  
`FILE_TYPE_MACINTOSH` | File type is MACINTOSH.  
`FILE_TYPE_APPLESINGLE` | File type is APPLESINGLE.  
`FILE_TYPE_APPLEDOUBLE` | File type is APPLEDOUBLE.  
`FILE_TYPE_MACINTOSH_HFS` | File type is MACINTOSH_HFS.  
`FILE_TYPE_APPLE_PLIST` | File type is APPLE_PLIST.  
`FILE_TYPE_MACINTOSH_LIB` | File type is MACINTOSH_LIB.  
`FILE_TYPE_APPLESCRIPT` | File type is APPLESCRIPT.  
`FILE_TYPE_APPLESCRIPT_COMPILED` | File type is APPLESCRIPT_COMPILED .  
`FILE_TYPE_CRX` | File type is CRX.  
`FILE_TYPE_XPI` | File type is XPI.  
`FILE_TYPE_ROM` | File type is ROM.  
`FILE_TYPE_IPS` | File type is IPS.  
`FILE_TYPE_PEM` | File type is PEM.  
`FILE_TYPE_PGP` | File type is PGP.  
`FILE_TYPE_CRT` | File type is CRT.  
  
## ExifInfo

Exif information.

JSON representation  
---  
      
    
    {
      "originalFile": string,
      "product": string,
      "company": string,
      "fileDescription": string,
      "entryPoint": string,
      "compilationTime": string
    }  
  
Fields  
---  
`originalFile` |  `string` original file name.  
`product` |  `string` product name.  
`company` |  `string` company name.  
`fileDescription` |  `string` description of a file.  
`entryPoint` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` entry point.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Compilation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SignatureInfo

File signature information extracted from different tools.

JSON representation  
---  
      
    
    {
      "sigcheck": {
        object ([FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSignatureInfo))
      },
      "codesign": {
        object ([FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataCodesign))
      }
    }  
  
Fields  
---  
`sigcheck` |  `object (`[FileMetadataSignatureInfo](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataSignatureInfo)`)` Signature information extracted from the sigcheck tool.  
`codesign` |  `object (`[FileMetadataCodesign](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#FileMetadataCodesign)`)` Signature information extracted from the codesign utility.  
  
## FileMetadataCodesign

File metadata from the codesign utility.

JSON representation  
---  
      
    
    {
      "id": string,
      "format": string,
      "compilationTime": string,
      "teamId": string
    }  
  
Fields  
---  
`id` |  `string` Code sign identifier.  
`format` |  `string` Code sign format.  
`compilationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Code sign timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`teamId` |  `string` The assigned team identifier of the developer who signed the application.  
  
## PDFInfo

Information about the PDF file structure. See [](https://developers.virustotal.com/reference/pdfInfo)<https://developers.virustotal.com/reference/pdfInfo>

JSON representation  
---  
      
    
    {
      "js": string,
      "javascript": string,
      "launchActionCount": string,
      "objectStreamCount": string,
      "endobjCount": string,
      "header": string,
      "acroform": string,
      "autoaction": string,
      "embeddedFile": string,
      "encrypted": string,
      "flash": string,
      "jbig2Compression": string,
      "objCount": string,
      "endstreamCount": string,
      "pageCount": string,
      "streamCount": string,
      "openaction": string,
      "startxref": string,
      "suspiciousColors": string,
      "trailer": string,
      "xfa": string,
      "xref": string
    }  
  
Fields  
---  
`js` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JS tags found in the PDF file. Should be the same as javascript field in normal scenarios.  
`javascript` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JavaScript tags found in the PDF file. Should be the same as the js field in normal scenarios.  
`launchActionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /Launch tags found in the PDF file.  
`objectStreamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of object streams.  
`endobjCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of object definitions (endobj keyword).  
`header` |  `string` PDF version.  
`acroform` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /AcroForm tags found in the PDF.  
`autoaction` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /AA tags found in the PDF.  
`embeddedFile` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /EmbeddedFile tags found in the PDF.  
`encrypted` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Whether the document is encrypted or not. This is defined by the /Encrypt tag.  
`flash` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /RichMedia tags found in the PDF.  
`jbig2Compression` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /JBIG2Decode tags found in the PDF.  
`objCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of objects definitions (obj keyword).  
`endstreamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of defined stream objects (stream keyword).  
`pageCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of pages in the PDF.  
`streamCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of defined stream objects (stream keyword).  
`openaction` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of /OpenAction tags found in the PDF.  
`startxref` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of startxref keywords in the PDF.  
`suspiciousColors` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of colors expressed with more than 3 bytes (CVE-2009-3459).  
`trailer` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of trailer keywords in the PDF.  
`xfa` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of \XFA tags found in the PDF.  
`xref` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of xref keywords in the PDF.  
  
## NtfsFileMetadata

NTFS-specific file metadata.

JSON representation  
---  
      
    
    {
      "changeTime": string,
      "filenameCreateTime": string,
      "filenameModifyTime": string,
      "filenameAccessTime": string,
      "filenameChangeTime": string
    }  
  
Fields  
---  
`changeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS MFT entry changed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute created timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameModifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute modified timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameAccessTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute accessed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filenameChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` NTFS $FILE_NAME attribute changed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## TokenElevationType

The elevation type of the process's token. See <https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-tokenElevationType>

Enums  
---  
`UNKNOWN` | An undetermined token type.  
`TYPE_1` | A full token with no privileges removed or groups disabled.  
`TYPE_2` | An elevated token with no privileges removed or groups disabled. Used when running as administrator.  
`TYPE_3` | A limited token with administrative privileges removed and administrative groups disabled.  
  
## Asset

Information about a compute asset such as a workstation, laptop, phone, virtual desktop, or VM.

JSON representation  
---  
      
    
    {
      "productObjectId": string,
      "hostname": string,
      "assetId": string,
      "ip": [
        string
      ],
      "mac": [
        string
      ],
      "natIp": [
        string
      ],
      "firstSeenTime": string,
      "hardware": [
        {
          object ([Hardware](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Hardware))
        }
      ],
      "platformSoftware": {
        object ([PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PlatformSoftware))
      },
      "software": [
        {
          object ([Software](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Software))
        }
      ],
      "location": {
        object ([Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location))
      },
      "category": string,
      "type": enum ([AssetType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AssetType)),
      "networkDomain": string,
      "creationTime": string,
      "firstDiscoverTime": string,
      "lastDiscoverTime": string,
      "systemLastUpdateTime": string,
      "lastBootTime": string,
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label))
        }
      ],
      "deploymentStatus": enum ([DeploymentStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#DeploymentStatus)),
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Vulnerability))
        }
      ],
      "attribute": {
        object ([Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute))
      }
    }  
  
Fields  
---  
`productObjectId` |  `string` A vendor-specific identifier to uniquely identify the entity (a GUID or similar). This field can be used as an entity indicator for asset entities.  
`hostname` |  `string` Asset hostname or domain name field. This field can be used as an entity indicator for asset entities.  
`assetId` |  `string` The asset ID. Value must contain the ':' character. For example, cs:abcdd23434. This field can be used as an entity indicator for asset entities.  
`ip[]` |  `string` A list of IP addresses associated with an asset. This field can be used as an entity indicator for asset entities.  
`mac[]` |  `string` List of MAC addresses associated with an asset. This field can be used as an entity indicator for asset entities.  
`natIp[]` |  `string` List of NAT IP addresses associated with an asset.  
`firstSeenTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first observed time for an asset. The value is calculated on the basis of the first time the identifier was observed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`hardware[]` |  `object (`[Hardware](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Hardware)`)` The asset hardware specifications.  
`platformSoftware` |  `object (`[PlatformSoftware](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#PlatformSoftware)`)` The asset operating system platform software.  
`software[]` |  `object (`[Software](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Software)`)` The asset software details.  
`location` |  `object (`[Location](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Location)`)` Location of the asset.  
`category` |  `string` The category of the asset (e.g. "End User Asset", "Workstation", "Server").  
`type` |  `enum (`[AssetType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#AssetType)`)` The type of the asset (e.g. workstation or laptop or server).  
`networkDomain` |  `string` The network domain of the asset (e.g. "corp.acme.com")  
`creationTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!Time the asset was created or provisioned. Deprecate: creationTime should be populated in Attribute as generic metadata.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`firstDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was first discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDiscoverTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last discovered (by asset management/discoverability software).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`systemLastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset system or OS was last updated. For all other operations that are not system updates (such as resizing a VM), use Attribute.last_update_time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastBootTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the asset was last boot started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels[]  
**(deprecated)**` |  `object (`[Label](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Label)`)` This item is deprecated!Metadata labels for the asset. Deprecated: labels should be populated in Attribute as generic metadata.  
`deploymentStatus` |  `enum (`[DeploymentStatus](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#DeploymentStatus)`)` The deployment status of the asset for device lifecycle purposes.  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Vulnerability)`)` Vulnerabilities discovered on asset.  
`attribute` |  `object (`[Attribute](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Attribute)`)` Generic entity metadata attributes of the asset.  
  
## Hardware

Hardware specification details for a resource, including both physical and virtual hardware.

JSON representation  
---  
      
    
    {
      "serialNumber": string,
      "manufacturer": string,
      "model": string,
      "cpuPlatform": string,
      "cpuModel": string,
      "cpuClockSpeed": string,
      "cpuMaxClockSpeed": string,
      "cpuNumberCores": string,
      "ram": string
    }  
  
Fields  
---  
`serialNumber` |  `string` Hardware serial number.  
`manufacturer` |  `string` Hardware manufacturer.  
`model` |  `string` Hardware model.  
`cpuPlatform` |  `string` Platform of the hardware CPU (e.g. "Intel Broadwell").  
`cpuModel` |  `string` Model description of the hardware CPU (e.g. "2.8 GHz Quad-Core Intel Core i5").  
`cpuClockSpeed` |  `string` Clock speed of the hardware CPU in MHz.  
`cpuMaxClockSpeed` |  `string` Maximum possible clock speed of the hardware CPU in MHz.  
`cpuNumberCores` |  `string` Number of CPU cores.  
`ram` |  `string` Amount of the hardware ramdom access memory (RAM) in Mb.  
  
## PlatformSoftware

Platform software information about an operating system.

JSON representation  
---  
      
    
    {
      "platform": enum ([Platform](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Platform)),
      "platformVersion": string,
      "platformPatchLevel": string
    }  
  
Fields  
---  
`platform` |  `enum (`[Platform](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Platform)`)` The platform operating system.  
`platformVersion` |  `string` The platform software version ( e.g. "Microsoft Windows 1803").  
`platformPatchLevel` |  `string` The platform software patch level ( e.g. "Build 17134.48", "SP1").  
  
## Platform

Operating system platform.

Enums  
---  
`UNKNOWN_PLATFORM` | Default value.  
`WINDOWS` | Microsoft Windows.  
`MAC` | macOS.  
`LINUX` | Linux.  
`GCP` | Deprecated: see cloud.environment.This item is deprecated!  
`AWS` | Deprecated: see cloud.environment.This item is deprecated!  
`AZURE` | Deprecated: see cloud.environment.This item is deprecated!  
`IOS` | IOS  
`ANDROID` | Android  
`CHROME_OS` | Chrome OS  
  
## Software

Information about a software package or application.

JSON representation  
---  
      
    
    {
      "name": string,
      "version": string,
      "permissions": [
        {
          object ([Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Permission))
        }
      ],
      "description": string,
      "vendorName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the software.  
`version` |  `string` The version of the software.  
`permissions[]` |  `object (`[Permission](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Permission)`)` System permissions granted to the software. For example, "android.permission.WRITE_EXTERNAL_STORAGE"  
`description` |  `string` The description of the software.  
`vendorName` |  `string` The name of the software vendor.  
  
## AssetType

The role type of the asset.

Enums  
---  
`ROLE_UNSPECIFIED` | Unspecified asset role.  
`WORKSTATION` | A workstation or desktop.  
`LAPTOP` | A laptop computer.  
`IOT` | An IOT asset.  
`NETWORK_ATTACHED_STORAGE` | A network attached storage device.  
`PRINTER` | A printer.  
`SCANNER` | A scanner.  
`SERVER` | A server.  
`TAPE_LIBRARY` | A tape library device.  
`MOBILE` | A mobile device such as a mobile phone or PDA.  
  
## DeploymentStatus

Deployment status states.

Enums  
---  
`DEPLOYMENT_STATUS_UNSPECIFIED` | Unspecified deployment status.  
`ACTIVE` | Asset is active, functional and deployed.  
`PENDING_DECOMISSION` | Asset is pending decommission and no longer deployed.  
`DECOMISSIONED` | Asset is decommissioned.  
  
## Registry

Information about a registry key or value.

JSON representation  
---  
      
    
    {
      "registryKey": string,
      "registryValueName": string,
      "registryValueData": string,
      "registryValueType": enum ([Type](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Type_1))
    }  
  
Fields  
---  
`registryKey` |  `string` Registry key associated with an application or system component (e.g., HKEY_, HKCU\Environment...).  
`registryValueName` |  `string` Name of the registry value associated with an application or system component (e.g. TEMP).  
`registryValueData` |  `string` Data associated with a registry value (e.g. %USERPROFILE%\Local Settings\Temp).  
`registryValueType` |  `enum (`[Type](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Type_1)`)` Type of the registry value.  
  
## Type

Type of the registry value. These values are based on the Windows Registry value types: <https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types>

Enums  
---  
`TYPE_UNSPECIFIED` | Default registry value type used when the type is unknown.  
`NONE` | The registry value is not set and only the key exists.  
`SZ` | A null-terminated string.  
`EXPAND_SZ` | A null-terminated string that contains unexpanded references to environment variables  
`BINARY` | Binary data in any form.  
`DWORD` | A 32-bit number.  
`DWORD_LITTLE_ENDIAN` | A 32-bit number in little-endian format.  
`DWORD_BIG_ENDIAN` | A 32-bit number in big-endian format.  
`LINK` | A null-terminated Unicode string that contains the target path of a symbolic link.  
`MULTI_SZ` | A sequence of null-terminated strings, terminated by an empty string  
`RESOURCE_LIST` | A device driver resource list.  
`QWORD` | A 64-bit number.  
`QWORD_LITTLE_ENDIAN` | A 64-bit number in little-endian format.  
  
## Id

Identifier to identify a UDM object like a UDM event, Entity, Collection. The full identifier for persistence is created by setting the 32 most significant bits as the Id.Namespace enum This is a convenience wrapper to define the id space enum values and provide an easy interface for RPCs, most persistence use cases should use a denormalized form.

JSON representation  
---  
      
    
    {
      "namespace": enum ([Namespace](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Namespace)),
      "id": string,
      "stringId": string
    }  
  
Fields  
---  
`namespace` |  `enum (`[Namespace](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Namespace)`)` Namespace the id belongs to.  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Full raw ID.A base64-encoded string.  
`stringId` |  `string` Some ids are stored as strings that are not able to be translated to bytes, so store these separately. Ex. detection id of the form de_aaaaaaaa-aaaa...  
  
## Investigation

Represents the aggregated state of an investigation such as categorization, severity, and status. Can be expanded to include analyst assignment details and more.

JSON representation  
---  
      
    
    {
      "comments": [
        string
      ],
      "verdict": enum ([Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Verdict)),
      "reputation": enum ([Reputation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Reputation)),
      "severityScore": integer,
      "status": enum ([Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Status)),
      "priority": enum ([Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Priority)),
      "rootCause": string,
      "reason": enum ([Reason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Reason)),
      "riskScore": integer,
      "id": string
    }  
  
Fields  
---  
`comments[]` |  `string` Comment added by the Analyst.  
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Verdict)`)` Describes reason a finding investigation was resolved.  
`reputation` |  `enum (`[Reputation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Reputation)`)` Describes whether a finding was useful or not-useful.  
`severityScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Severity score for a finding set by an analyst.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Status)`)` Describes the workflow status of a finding.  
`priority` |  `enum (`[Priority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Priority)`)` Priority of the Alert or Finding set by analyst.  
`rootCause` |  `string` Root cause of the Alert or Finding set by analyst.  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Noun#Reason)`)` Reason for closing the Case or Alert.  
`riskScore` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Risk score for a finding set by an analyst.  
`id` |  `string` Identifier for the investigation  
  
## Verdict

LINT.IfChange Categorization options for the validity of a finding (for example, whether it reflects an actual security incident).

Enums  
---  
`VERDICT_UNSPECIFIED` | An unspecified verdict.  
`TRUE_POSITIVE` | A categorization of the finding as a "true positive".  
`FALSE_POSITIVE` | A categorization of the finding as a "false positive".  
  
## Reputation

Categorization options for the usefulness of a finding.

Enums  
---  
`REPUTATION_UNSPECIFIED` | An unspecified reputation.  
`USEFUL` | A categorization of the finding as useful.  
`NOT_USEFUL` | A categorization of the finding as not useful.  
  
## Status

Describes status of a finding.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified finding status.  
`NEW` | New finding.  
`REVIEWED` | When a finding has feedback.  
`CLOSED` | When an analyst closes an finding.  
`OPEN` | Open. Used to indicate that a Case / Alert is open.  
  
## Reason

Reason for closing an Alert or Case in the SOAR product.

Enums  
---  
`REASON_UNSPECIFIED` | Default reason.  
`REASON_NOT_MALICIOUS` | Case or Alert not malicious.  
`REASON_MALICIOUS` | Case or Alert is malicious.  
`REASON_MAINTENANCE` | Case or Alert is under maintenance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
