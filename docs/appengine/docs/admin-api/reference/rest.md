---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/
title: App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:53.279653+00:00
---

# App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  App Engine Admin API Stay organized with collections  Save and categorize content based on your preferences. 

Provisions and manages developers' App Engine applications.

  * REST Resource: v1.apps
  * REST Resource: v1.apps.authorizedCertificates
  * REST Resource: v1.apps.authorizedDomains
  * REST Resource: v1.apps.domainMappings
  * REST Resource: v1.apps.firewall.ingressRules
  * REST Resource: v1.apps.locations
  * REST Resource: v1.apps.operations
  * REST Resource: v1.apps.services
  * REST Resource: v1.apps.services.versions
  * REST Resource: v1.apps.services.versions.instances
  * REST Resource: v1beta.apps
  * REST Resource: v1beta.apps.authorizedCertificates
  * REST Resource: v1beta.apps.authorizedDomains
  * REST Resource: v1beta.apps.domainMappings
  * REST Resource: v1beta.apps.firewall.ingressRules
  * REST Resource: v1beta.apps.locations
  * REST Resource: v1beta.apps.operations
  * REST Resource: v1beta.apps.services
  * REST Resource: v1beta.apps.services.versions
  * REST Resource: v1beta.apps.services.versions.instances



## Service: appengine.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://appengine.googleapis.com/$discovery/rest?version=v1>
  * <https://appengine.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://appengine.googleapis.com`



## REST Resource: [v1.apps](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/create)` |  `POST /v1/apps`   
Creates an App Engine application for a Google Cloud Platform project.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/get)` |  `GET /v1/{name=apps/*}`   
Gets information about an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/patch)` |  `PATCH /v1/{name=apps/*}`   
Updates the specified Application resource.  
`[repair](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps/repair)` |  `POST /v1/{name=apps/*}:repair`   
Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account.  
  
## REST Resource: [v1.apps.authorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates/create)` |  `POST /v1/{parent=apps/*}/authorizedCertificates`   
Uploads the specified SSL certificate.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates/delete)` |  `DELETE /v1/{name=apps/*/authorizedCertificates/*}`   
Deletes the specified SSL certificate.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates/get)` |  `GET /v1/{name=apps/*/authorizedCertificates/*}`   
Gets the specified SSL certificate.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates/list)` |  `GET /v1/{parent=apps/*}/authorizedCertificates`   
Lists all SSL certificates the user is authorized to administer.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedCertificates/patch)` |  `PATCH /v1/{name=apps/*/authorizedCertificates/*}`   
Updates the specified SSL certificate.  
  
## REST Resource: [v1.apps.authorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains)

Methods  
---  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list)` |  `GET /v1/{parent=apps/*}/authorizedDomains`   
Lists all domains the user is authorized to administer.  
  
## REST Resource: [v1.apps.domainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/create)` |  `POST /v1/{parent=apps/*}/domainMappings`   
Maps a domain to an application.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/delete)` |  `DELETE /v1/{name=apps/*/domainMappings/*}`   
Deletes the specified domain mapping.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/get)` |  `GET /v1/{name=apps/*/domainMappings/*}`   
Gets the specified domain mapping.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/list)` |  `GET /v1/{parent=apps/*}/domainMappings`   
Lists the domain mappings on an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings/patch)` |  `PATCH /v1/{name=apps/*/domainMappings/*}`   
Updates the specified domain mapping.  
  
## REST Resource: [v1.apps.firewall.ingressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/batchUpdate)` |  `POST /v1/{name=apps/*/firewall/ingressRules}:batchUpdate`   
Replaces the entire firewall ruleset in one bulk operation.  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/create)` |  `POST /v1/{parent=apps/*}/firewall/ingressRules`   
Creates a firewall rule for the application.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/delete)` |  `DELETE /v1/{name=apps/*/firewall/ingressRules/*}`   
Deletes the specified firewall rule.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/get)` |  `GET /v1/{name=apps/*/firewall/ingressRules/*}`   
Gets the specified firewall rule.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/list)` |  `GET /v1/{parent=apps/*}/firewall/ingressRules`   
Lists the firewall rules of an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules/patch)` |  `PATCH /v1/{name=apps/*/firewall/ingressRules/*}`   
Updates the specified firewall rule.  
  
## REST Resource: [v1.apps.locations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.locations/get)` |  `GET /v1/{name=apps/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.locations/list)` |  `GET /v1/{name=apps/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.apps.operations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.operations/get)` |  `GET /v1/{name=apps/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.operations/list)` |  `GET /v1/{name=apps/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.apps.services](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services)

Methods  
---  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/delete)` |  `DELETE /v1/{name=apps/*/services/*}`   
Deletes the specified service and all enclosed versions.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/get)` |  `GET /v1/{name=apps/*/services/*}`   
Gets the current configuration of the specified service.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/list)` |  `GET /v1/{parent=apps/*}/services`   
Lists all the services in the application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/patch)` |  `PATCH /v1/{name=apps/*/services/*}`   
Updates the configuration of the specified service.  
  
## REST Resource: [v1.apps.services.versions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/create)` |  `POST /v1/{parent=apps/*/services/*}/versions`   
Deploys code and resource files to a new version.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/delete)` |  `DELETE /v1/{name=apps/*/services/*/versions/*}`   
Deletes an existing Version resource.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/get)` |  `GET /v1/{name=apps/*/services/*/versions/*}`   
Gets the specified Version resource.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/list)` |  `GET /v1/{parent=apps/*/services/*}/versions`   
Lists the versions of a service.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch)` |  `PATCH /v1/{name=apps/*/services/*/versions/*}`   
Updates the specified Version resource.  
  
## REST Resource: [v1.apps.services.versions.instances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances)

Methods  
---  
`[debug](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/debug)` |  `POST /v1/{name=apps/*/services/*/versions/*/instances/*}:debug`   
Enables debugging on a VM instance.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/delete)` |  `DELETE /v1/{name=apps/*/services/*/versions/*/instances/*}`   
Stops a running instance.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/get)` |  `GET /v1/{name=apps/*/services/*/versions/*/instances/*}`   
Gets instance information.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions.instances/list)` |  `GET /v1/{parent=apps/*/services/*/versions/*}/instances`   
Lists the instances of a version.  
  
## REST Resource: [v1beta.apps](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps/create)` |  `POST /v1beta/apps`   
Creates an App Engine application for a Google Cloud Platform project.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps/get)` |  `GET /v1beta/{name=apps/*}`   
Gets information about an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps/patch)` |  `PATCH /v1beta/{name=apps/*}`   
Updates the specified Application resource.  
`[repair](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps/repair)` |  `POST /v1beta/{name=apps/*}:repair`   
Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account.  
  
## REST Resource: [v1beta.apps.authorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/create)` |  `POST /v1beta/{parent=apps/*}/authorizedCertificates`   
Uploads the specified SSL certificate.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/delete)` |  `DELETE /v1beta/{name=apps/*/authorizedCertificates/*}`   
Deletes the specified SSL certificate.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/get)` |  `GET /v1beta/{name=apps/*/authorizedCertificates/*}`   
Gets the specified SSL certificate.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/list)` |  `GET /v1beta/{parent=apps/*}/authorizedCertificates`   
Lists all SSL certificates the user is authorized to administer.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedCertificates/patch)` |  `PATCH /v1beta/{name=apps/*/authorizedCertificates/*}`   
Updates the specified SSL certificate.  
  
## REST Resource: [v1beta.apps.authorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains)

Methods  
---  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.authorizedDomains/list)` |  `GET /v1beta/{parent=apps/*}/authorizedDomains`   
Lists all domains the user is authorized to administer.  
  
## REST Resource: [v1beta.apps.domainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/create)` |  `POST /v1beta/{parent=apps/*}/domainMappings`   
Maps a domain to an application.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/delete)` |  `DELETE /v1beta/{name=apps/*/domainMappings/*}`   
Deletes the specified domain mapping.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/get)` |  `GET /v1beta/{name=apps/*/domainMappings/*}`   
Gets the specified domain mapping.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/list)` |  `GET /v1beta/{parent=apps/*}/domainMappings`   
Lists the domain mappings on an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.domainMappings/patch)` |  `PATCH /v1beta/{name=apps/*/domainMappings/*}`   
Updates the specified domain mapping.  
  
## REST Resource: [v1beta.apps.firewall.ingressRules](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules)

Methods  
---  
`[batchUpdate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/batchUpdate)` |  `POST /v1beta/{name=apps/*/firewall/ingressRules}:batchUpdate`   
Replaces the entire firewall ruleset in one bulk operation.  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/create)` |  `POST /v1beta/{parent=apps/*}/firewall/ingressRules`   
Creates a firewall rule for the application.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/delete)` |  `DELETE /v1beta/{name=apps/*/firewall/ingressRules/*}`   
Deletes the specified firewall rule.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/get)` |  `GET /v1beta/{name=apps/*/firewall/ingressRules/*}`   
Gets the specified firewall rule.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/list)` |  `GET /v1beta/{parent=apps/*}/firewall/ingressRules`   
Lists the firewall rules of an application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.firewall.ingressRules/patch)` |  `PATCH /v1beta/{name=apps/*/firewall/ingressRules/*}`   
Updates the specified firewall rule.  
  
## REST Resource: [v1beta.apps.locations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.locations/get)` |  `GET /v1beta/{name=apps/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.locations/list)` |  `GET /v1beta/{name=apps/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta.apps.operations](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.operations/get)` |  `GET /v1beta/{name=apps/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.operations/list)` |  `GET /v1beta/{name=apps/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.apps.services](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services)

Methods  
---  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services/delete)` |  `DELETE /v1beta/{name=apps/*/services/*}`   
Deletes the specified service and all enclosed versions.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services/get)` |  `GET /v1beta/{name=apps/*/services/*}`   
Gets the current configuration of the specified service.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services/list)` |  `GET /v1beta/{parent=apps/*}/services`   
Lists all the services in the application.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services/patch)` |  `PATCH /v1beta/{name=apps/*/services/*}`   
Updates the configuration of the specified service.  
  
## REST Resource: [v1beta.apps.services.versions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions)

Methods  
---  
`[create](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions/create)` |  `POST /v1beta/{parent=apps/*/services/*}/versions`   
Deploys code and resource files to a new version.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions/delete)` |  `DELETE /v1beta/{name=apps/*/services/*/versions/*}`   
Deletes an existing Version resource.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions/get)` |  `GET /v1beta/{name=apps/*/services/*/versions/*}`   
Gets the specified Version resource.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions/list)` |  `GET /v1beta/{parent=apps/*/services/*}/versions`   
Lists the versions of a service.  
`[patch](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions/patch)` |  `PATCH /v1beta/{name=apps/*/services/*/versions/*}`   
Updates the specified Version resource.  
  
## REST Resource: [v1beta.apps.services.versions.instances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions.instances)

Methods  
---  
`[debug](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions.instances/debug)` |  `POST /v1beta/{name=apps/*/services/*/versions/*/instances/*}:debug`   
Enables debugging on a VM instance.  
`[delete](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions.instances/delete)` |  `DELETE /v1beta/{name=apps/*/services/*/versions/*/instances/*}`   
Stops a running instance.  
`[get](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions.instances/get)` |  `GET /v1beta/{name=apps/*/services/*/versions/*/instances/*}`   
Gets instance information.  
`[list](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1beta/apps.services.versions.instances/list)` |  `GET /v1beta/{parent=apps/*/services/*/versions/*}/instances`   
Lists the instances of a version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
