---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections
title: REST Resource: projects.locations.connections \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:30.323924+00:00
---

# REST Resource: projects.locations.connections  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
  * Methods



## Resource: Connection

A data connection to allow the DLP API to profile data in locations that require additional configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.ConnectionState)),
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudSql": {
        object ([CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlProperties))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the connection: `projects/{project}/locations/{location}/connections/{name}`.  
`state` |  `enum (`[ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.ConnectionState)`)` Required. The connection's state in its lifecycle.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. Set if status == ERROR, to provide additional details. Will store the last 10 errors sorted with the most recent first.  
Type of connection. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudSql` |  `object (`[CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlProperties)`)` Connect to a Cloud SQL instance.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/create)`

|  Create a Connection to an external data source.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/delete)`

|  Delete a Connection.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/get)`

|  Get a Connection by name.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/list)`

|  Lists Connections in a parent.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/patch)`

|  Update a Connection.  
  
### `[search](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/search)`

|  Searches for Connections in a parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
