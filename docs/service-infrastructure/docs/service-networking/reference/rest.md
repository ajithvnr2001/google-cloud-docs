---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/
title: Service Networking API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:35.467299+00:00
---

# Service Networking API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Service Networking API Stay organized with collections  Save and categorize content based on your preferences. 

Provides automatic management of network configurations necessary for certain services.

  * REST Resource: v1.operations
  * REST Resource: v1.services
  * REST Resource: v1.services.connections
  * REST Resource: v1.services.dnsRecordSets
  * REST Resource: v1.services.dnsZones
  * REST Resource: v1.services.projects.global.networks
  * REST Resource: v1.services.projects.global.networks.dnsZones
  * REST Resource: v1.services.projects.global.networks.peeredDnsDomains
  * REST Resource: v1.services.roles



## Service: servicenetworking.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://servicenetworking.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://servicenetworking.googleapis.com`



## REST Resource: [v1.operations](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations/cancel)` |  `POST /v1/{name=operations/**}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations/delete)` |  `DELETE /v1/{name=operations/**}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations/get)` |  `GET /v1/{name=operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations/list)` |  `GET /v1/{name=operations}`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.services](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services)

Methods  
---  
`[addSubnetwork](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/addSubnetwork)` |  `POST /v1/{parent=services/*/*/*}:addSubnetwork`   
For service producers, provisions a new subnet in a peered service's shared VPC network in the requested region and with the requested size that's expressed as a CIDR range (number of leading bits of ipV4 network mask).  
`[disableVpcServiceControls](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/disableVpcServiceControls)` |  `PATCH /v1/{parent=services/*}:disableVpcServiceControls`   
Disables VPC service controls for a connection.  
`[enableVpcServiceControls](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/enableVpcServiceControls)` |  `PATCH /v1/{parent=services/*}:enableVpcServiceControls`   
Enables VPC service controls for a connection.  
`[searchRange](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/searchRange)` |  `POST /v1/{parent=services/*}:searchRange`   
Service producers can use this method to find a currently unused range within consumer allocated ranges.  
`[validate](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate)` |  `POST /v1/{parent=services/*}:validate`   
Service producers use this method to validate if the consumer provided network, project and requested range are valid.  
  
## REST Resource: [v1.services.connections](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/create)` |  `POST /v1/{parent=services/*}/connections`   
Creates a private connection that establishes a VPC Network Peering connection to a VPC network in the service producer's organization.  
`[deleteConnection](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/deleteConnection)` |  `POST /v1/{name=services/*/connections/*}`   
Deletes a private service access connection.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/list)` |  `GET /v1/{parent=services/*}/connections`   
List the private connections that are configured in a service consumer's VPC network.  
`[patch](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections/patch)` |  `PATCH /v1/{name=services/*/connections/*}`   
Updates the allocated ranges that are assigned to a connection.  
  
## REST Resource: [v1.services.dnsRecordSets](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets)

Methods  
---  
`[add](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/add)` |  `POST /v1/{parent=services/*}/dnsRecordSets:add`   
Service producers can use this method to add DNS record sets to private DNS zones in the shared producer host project.  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/get)` |  `GET /v1/{parent=services/*}/dnsRecordSets:get`   
Producers can use this method to retrieve information about the DNS record set added to the private zone inside the shared tenant host project associated with a consumer network.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/list)` |  `GET /v1/{parent=services/*}/dnsRecordSets:list`   
Producers can use this method to retrieve a list of available DNS RecordSets available inside the private zone on the tenant host project accessible from their network.  
`[remove](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/remove)` |  `POST /v1/{parent=services/*}/dnsRecordSets:remove`   
Service producers can use this method to remove DNS record sets from private DNS zones in the shared producer host project.  
`[update](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/update)` |  `POST /v1/{parent=services/*}/dnsRecordSets:update`   
Service producers can use this method to update DNS record sets from private DNS zones in the shared producer host project.  
  
## REST Resource: [v1.services.dnsZones](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsZones)

Methods  
---  
`[add](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsZones/add)` |  `POST /v1/{parent=services/*}/dnsZones:add`   
Service producers can use this method to add private DNS zones in the shared producer host project and matching peering zones in the consumer project.  
`[remove](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsZones/remove)` |  `POST /v1/{parent=services/*}/dnsZones:remove`   
Service producers can use this method to remove private DNS zones in the shared producer host project and matching peering zones in the consumer project.  
  
## REST Resource: [v1.services.projects.global.networks](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks)

Methods  
---  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/get)` |  `GET /v1/{name=services/*/projects/*/global/networks/*}`   
Service producers use this method to get the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP.  
`[getVpcServiceControls](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/getVpcServiceControls)` |  `GET /v1/{name=services/*/projects/*/global/networks/*}/vpcServiceControls`   
Consumers use this method to find out the state of VPC Service Controls.  
`[updateConsumerConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/updateConsumerConfig)` |  `PATCH /v1/{parent=services/*/projects/*/global/networks/*}:updateConsumerConfig`   
Service producers use this method to update the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP.  
  
## REST Resource: [v1.services.projects.global.networks.dnsZones](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones)

Methods  
---  
`[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/get)` |  `GET /v1/{name=services/*/projects/*/global/networks/*/dnsZones/*}`   
Service producers can use this method to retrieve a DNS zone in the shared producer host project and the matching peering zones in consumer project  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list)` |  `GET /v1/{parent=services/*/projects/*/global/networks/*}/dnsZones:list`   
* Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project.  
  
## REST Resource: [v1.services.projects.global.networks.peeredDnsDomains](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.peeredDnsDomains)

Methods  
---  
`[create](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.peeredDnsDomains/create)` |  `POST /v1/{parent=services/*/projects/*/global/networks/*}/peeredDnsDomains`   
Creates a peered DNS domain which sends requests for records in given namespace originating in the service producer VPC network to the consumer VPC network to be resolved.  
`[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.peeredDnsDomains/delete)` |  `DELETE /v1/{name=services/*/projects/*/global/networks/*/peeredDnsDomains/*}`   
Deletes a peered DNS domain.  
`[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.peeredDnsDomains/list)` |  `GET /v1/{parent=services/*/projects/*/global/networks/*}/peeredDnsDomains`   
Lists peered DNS domains for a connection.  
  
## REST Resource: [v1.services.roles](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles)

Methods  
---  
`[add](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.roles/add)` |  `POST /v1/{parent=services/*}/roles:add`   
Service producers can use this method to add roles in the shared VPC host project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
