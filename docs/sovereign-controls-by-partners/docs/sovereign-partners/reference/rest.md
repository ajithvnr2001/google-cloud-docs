---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/
title: Cloud Controls Partner API \u00a0|\u00a0 Sovereign Controls by Partners guides for partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:56.708455+00:00
---

# Cloud Controls Partner API  |  Sovereign Controls by Partners guides for partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners)
  * [ Sovereign Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/guides)
  * [ Reference ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest)



Send feedback 

#  Cloud Controls Partner API Stay organized with collections  Save and categorize content based on your preferences. 

Provides insights about your customers and their Assured Workloads based on your Sovereign Controls by Partners offering.

  * REST Resource: v1beta.organizations.locations
  * REST Resource: v1beta.organizations.locations.customers
  * REST Resource: v1beta.organizations.locations.customers.workloads
  * REST Resource: v1beta.organizations.locations.customers.workloads.accessApprovalRequests
  * REST Resource: v1beta.organizations.locations.customers.workloads.violations
  * REST Resource: v1alpha.organizations.locations
  * REST Resource: v1alpha.organizations.locations.customers
  * REST Resource: v1alpha.organizations.locations.customers.workloads
  * REST Resource: v1alpha.organizations.locations.customers.workloads.accessApprovalRequests
  * REST Resource: v1alpha.organizations.locations.customers.workloads.violations
  * REST Resource: v1.organizations.locations
  * REST Resource: v1.organizations.locations.customers
  * REST Resource: v1.organizations.locations.customers.workloads
  * REST Resource: v1.organizations.locations.customers.workloads.accessApprovalRequests
  * REST Resource: v1.organizations.locations.customers.workloads.violations



## Service: cloudcontrolspartner.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://cloudcontrolspartner.googleapis.com/$discovery/rest?version=v1>
  * <https://cloudcontrolspartner.googleapis.com/$discovery/rest?version=v1beta>
  * <https://cloudcontrolspartner.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudcontrolspartner.googleapis.com`



## REST Resource: [v1beta.organizations.locations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations)

Methods  
---  
`[getPartner](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations/getPartner)` |  `GET /v1beta/{name=organizations/*/locations/*/partner}`   
Get details of a Partner.  
  
## REST Resource: [v1beta.organizations.locations.customers](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers/get)` |  `GET /v1beta/{name=organizations/*/locations/*/customers/*}`   
Gets details of a single customer  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers/list)` |  `GET /v1beta/{parent=organizations/*/locations/*}/customers`   
Lists customers of a partner identified by its Google Cloud organization ID  
  
## REST Resource: [v1beta.organizations.locations.customers.workloads](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads/get)` |  `GET /v1beta/{name=organizations/*/locations/*/customers/*/workloads/*}`   
Gets details of a single workload  
`[getEkmConnections](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads/getEkmConnections)` |  `GET /v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/ekmConnections}`   
Gets the EKM connections associated with a workload  
`[getPartnerPermissions](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads/getPartnerPermissions)` |  `GET /v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/partnerPermissions}`   
Gets the partner permissions granted for a workload  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads/list)` |  `GET /v1beta/{parent=organizations/*/locations/*/customers/*}/workloads`   
Lists customer workloads for a given customer org id  
  
## REST Resource: [v1beta.organizations.locations.customers.workloads.accessApprovalRequests](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads.accessApprovalRequests)

Methods  
---  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads.accessApprovalRequests/list)` |  `GET /v1beta/{parent=organizations/*/locations/*/customers/*/workloads/*}/accessApprovalRequests`   
Lists access requests associated with a workload  
  
## REST Resource: [v1beta.organizations.locations.customers.workloads.violations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads.violations)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads.violations/get)` |  `GET /v1beta/{name=organizations/*/locations/*/customers/*/workloads/*/violations/*}`   
Gets details of a single Violation.  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1beta/organizations.locations.customers.workloads.violations/list)` |  `GET /v1beta/{parent=organizations/*/locations/*/customers/*/workloads/*}/violations`   
Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of {customer} & {workload}.  
  
## REST Resource: [v1alpha.organizations.locations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations)

Methods  
---  
`[getPartner](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations/getPartner)` |  `GET /v1alpha/{name=organizations/*/locations/*/partner}`   
Get details of a Partner.  
  
## REST Resource: [v1alpha.organizations.locations.customers](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers/get)` |  `GET /v1alpha/{name=organizations/*/locations/*/customers/*}`   
Gets details of a single customer  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers/list)` |  `GET /v1alpha/{parent=organizations/*/locations/*}/customers`   
Lists customers of a partner identified by its Google Cloud organization ID  
  
## REST Resource: [v1alpha.organizations.locations.customers.workloads](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads/get)` |  `GET /v1alpha/{name=organizations/*/locations/*/customers/*/workloads/*}`   
Gets details of a single workload  
`[getEkmConnections](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads/getEkmConnections)` |  `GET /v1alpha/{name=organizations/*/locations/*/customers/*/workloads/*/ekmConnections}`   
Gets the EKM connections associated with a workload  
`[getPartnerPermissions](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads/getPartnerPermissions)` |  `GET /v1alpha/{name=organizations/*/locations/*/customers/*/workloads/*/partnerPermissions}`   
Gets the partner permissions granted for a workload  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads/list)` |  `GET /v1alpha/{parent=organizations/*/locations/*/customers/*}/workloads`   
Lists customer workloads for a given customer org id  
  
## REST Resource: [v1alpha.organizations.locations.customers.workloads.accessApprovalRequests](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads.accessApprovalRequests)

Methods  
---  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads.accessApprovalRequests/list)` |  `GET /v1alpha/{parent=organizations/*/locations/*/customers/*/workloads/*}/accessApprovalRequests`   
Lists access requests associated with a workload  
  
## REST Resource: [v1alpha.organizations.locations.customers.workloads.violations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads.violations)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads.violations/get)` |  `GET /v1alpha/{name=organizations/*/locations/*/customers/*/workloads/*/violations/*}`   
Gets details of a single Violation.  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1alpha/organizations.locations.customers.workloads.violations/list)` |  `GET /v1alpha/{parent=organizations/*/locations/*/customers/*/workloads/*}/violations`   
Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of {customer} & {workload}.  
  
## REST Resource: [v1.organizations.locations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations)

Methods  
---  
`[getPartner](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations/getPartner)` |  `GET /v1/{name=organizations/*/locations/*/partner}`   
Get details of a Partner.  
  
## REST Resource: [v1.organizations.locations.customers](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers/get)` |  `GET /v1/{name=organizations/*/locations/*/customers/*}`   
Gets details of a single customer  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers/list)` |  `GET /v1/{parent=organizations/*/locations/*}/customers`   
Lists customers of a partner identified by its Google Cloud organization ID  
  
## REST Resource: [v1.organizations.locations.customers.workloads](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads/get)` |  `GET /v1/{name=organizations/*/locations/*/customers/*/workloads/*}`   
Gets details of a single workload  
`[getEkmConnections](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads/getEkmConnections)` |  `GET /v1/{name=organizations/*/locations/*/customers/*/workloads/*/ekmConnections}`   
Gets the EKM connections associated with a workload  
`[getPartnerPermissions](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads/getPartnerPermissions)` |  `GET /v1/{name=organizations/*/locations/*/customers/*/workloads/*/partnerPermissions}`   
Gets the partner permissions granted for a workload  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads/list)` |  `GET /v1/{parent=organizations/*/locations/*/customers/*}/workloads`   
Lists customer workloads for a given customer org id  
  
## REST Resource: [v1.organizations.locations.customers.workloads.accessApprovalRequests](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads.accessApprovalRequests)

Methods  
---  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads.accessApprovalRequests/list)` |  `GET /v1/{parent=organizations/*/locations/*/customers/*/workloads/*}/accessApprovalRequests`   
Lists access requests associated with a workload  
  
## REST Resource: [v1.organizations.locations.customers.workloads.violations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads.violations)

Methods  
---  
`[get](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads.violations/get)` |  `GET /v1/{name=organizations/*/locations/*/customers/*/workloads/*/violations/*}`   
Gets details of a single Violation.  
`[list](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads.violations/list)` |  `GET /v1/{parent=organizations/*/locations/*/customers/*/workloads/*}/violations`   
Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of {customer} & {workload}.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
