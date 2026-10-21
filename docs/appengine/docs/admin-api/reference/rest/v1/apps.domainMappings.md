---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings
title: REST Resource: apps.domainMappings \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:54.571901+00:00
---

# REST Resource: apps.domainMappings  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  REST Resource: apps.domainMappings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DomainMapping
    * JSON representation
  * SslSettings
    * JSON representation
  * SslManagementType
  * ResourceRecord
    * JSON representation
  * RecordType
  * Methods



## Resource: DomainMapping

A domain serving an App Engine application.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "sslSettings": {
        object ([SslSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#SslSettings))
      },
      "resourceRecords": [
        {
          object ([ResourceRecord](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#ResourceRecord))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Full path to the `DomainMapping` resource in the API. Example: `apps/myapp/domainMapping/example.com`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the domain serving the application. Example: `example.com`.  
`sslSettings` |  `object (`[SslSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#SslSettings)`)` SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.  
`resourceRecords[]` |  `object (`[ResourceRecord](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#ResourceRecord)`)` The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## SslSettings

SSL configuration for a `DomainMapping` resource.

JSON representation  
---  
      
    
    {
      "certificateId": string,
      "sslManagementType": enum ([SslManagementType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#SslManagementType)),
      "pendingManagedCertificateId": string
    }  
  
Fields  
---  
`certificateId` |  `string` ID of the `AuthorizedCertificate` resource configuring SSL for the application. Clearing this field will remove SSL support.By default, a managed certificate is automatically created for every domain mapping. To omit SSL support or to configure SSL manually, specify `SslManagementType.MANUAL` on a `CREATE` or `UPDATE` request. You must be authorized to administer the `AuthorizedCertificate` resource to manually map it to a `DomainMapping` resource. Example: `12345`.  
`sslManagementType` |  `enum (`[SslManagementType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#SslManagementType)`)` SSL management type for this domain. If `AUTOMATIC`, a managed certificate is automatically provisioned. If `MANUAL`, `certificateId` must be manually specified in order to configure SSL for this domain.  
`pendingManagedCertificateId` |  `string` ID of the managed `AuthorizedCertificate` resource currently being provisioned, if applicable. Until the new managed certificate has been successfully provisioned, the previous SSL state will be preserved. Once the provisioning process completes, the `certificateId` field will reflect the new managed certificate and this field will be left empty. To remove SSL support while there is still a pending managed certificate, clear the `certificateId` field with an `UpdateDomainMappingRequest`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## SslManagementType

The SSL management type for this domain.

Enums  
---  
`SSL_MANAGEMENT_TYPE_UNSPECIFIED` | Defaults to `AUTOMATIC`.  
`AUTOMATIC` | SSL support for this domain is configured automatically. The mapped SSL certificate will be automatically renewed.  
`MANUAL` | SSL support for this domain is configured manually by the user. Either the domain has no SSL support or a user-obtained SSL certificate has been explictly mapped to this domain.  
  
## ResourceRecord

A DNS resource record.

JSON representation  
---  
      
    
    {
      "name": string,
      "rrdata": string,
      "type": enum ([RecordType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#RecordType))
    }  
  
Fields  
---  
`name` |  `string` Relative name of the object affected by this record. Only applicable for `CNAME` records. Example: 'www'.  
`rrdata` |  `string` Data for this record. Values vary by record type, as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1).  
`type` |  `enum (`[RecordType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings#RecordType)`)` Resource record type. Example: `AAAA`.  
  
## RecordType

A resource record type.

Enums  
---  
`RECORD_TYPE_UNSPECIFIED` | An unknown resource record.  
`A` | An A resource record. Data is an IPv4 address.  
`AAAA` | An AAAA resource record. Data is an IPv6 address.  
`CNAME` | A CNAME resource record. Data is a domain name to be aliased.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/create)`

|  Maps a domain to an application.  
  
### `[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/delete)`

|  Deletes the specified domain mapping.  
  
### `[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/get)`

|  Gets the specified domain mapping.  
  
### `[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/list)`

|  Lists the domain mappings on an application.  
  
### `[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/patch)`

|  Updates the specified domain mapping.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
