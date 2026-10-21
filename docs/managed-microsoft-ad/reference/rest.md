---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/
title: Managed Service for Microsoft Active Directory API \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:48.908242+00:00
---

# Managed Service for Microsoft Active Directory API  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Managed Service for Microsoft Active Directory API Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Microsoft Active Directory API is used for managing a highly available, hardened service running Microsoft Active Directory (AD).

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.global.domains
  * REST Resource: v1beta1.projects.locations.global.domains.backups
  * REST Resource: v1beta1.projects.locations.global.domains.sqlIntegrations
  * REST Resource: v1beta1.projects.locations.global.operations
  * REST Resource: v1beta1.projects.locations.global.peerings
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.global.domains
  * REST Resource: v1.projects.locations.global.domains.backups
  * REST Resource: v1.projects.locations.global.domains.sqlIntegrations
  * REST Resource: v1.projects.locations.global.operations
  * REST Resource: v1.projects.locations.global.peerings



## Service: managedidentities.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://managedidentities.googleapis.com/$discovery/rest?version=v1>
  * <https://managedidentities.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://managedidentities.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.global.domains](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains)

Methods  
---  
`[attachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/attachTrust)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:attachTrust`   
Adds an AD trust to a domain.  
`[checkMigrationPermission](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/checkMigrationPermission)` |  `POST /v1beta1/{domain=projects/*/locations/global/domains/*}:checkMigrationPermission`   
CheckMigrationPermission API gets the current state of DomainMigration  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/create)` |  `POST /v1beta1/{parent=projects/*/locations/global}/domains`   
Creates a Microsoft AD domain.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/domains/*}`   
Deletes a domain.  
`[detachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/detachTrust)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:detachTrust`   
Removes an AD trust.  
`[disableMigration](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/disableMigration)` |  `POST /v1beta1/{domain=projects/*/locations/global/domains/*}:disableMigration`   
Disable Domain Migration  
`[domainJoinMachine](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/domainJoinMachine)` |  `POST /v1beta1/{domain=projects/*/locations/global/domains/*}:domainJoinMachine`   
DomainJoinMachine API joins a Compute Engine VM to the domain  
`[enableMigration](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/enableMigration)` |  `POST /v1beta1/{domain=projects/*/locations/global/domains/*}:enableMigration`   
Enable Domain Migration  
`[extendSchema](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/extendSchema)` |  `POST /v1beta1/{domain=projects/*/locations/global/domains/*}:extendSchema`   
Extend Schema for Domain  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/get)` |  `GET /v1beta1/{name=projects/*/locations/global/domains/*}`   
Gets information about a domain.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/global/domains/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[getLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/getLdapssettings)` |  `GET /v1beta1/{name=projects/*/locations/global/domains/*}/ldapssettings`   
Gets the domain ldaps settings.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/list)` |  `GET /v1beta1/{parent=projects/*/locations/global}/domains`   
Lists domains in a project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/patch)` |  `PATCH /v1beta1/{domain.name=projects/*/locations/global/domains/*}`   
Updates the metadata and configuration of a domain.  
`[reconfigureTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/reconfigureTrust)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:reconfigureTrust`   
Updates the DNS conditional forwarder.  
`[resetAdminPassword](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/resetAdminPassword)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:resetAdminPassword`   
Resets a domain's administrator password.  
`[restore](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/restore)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:restore`   
RestoreBackup restores domain mentioned in the RestoreBackupRequest  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/global/domains/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/global/domains/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[updateLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/updateLdapssettings)` |  `PATCH /v1beta1/{ldapsSettings.name=projects/*/locations/global/domains/*}/ldapssettings`   
Patches a single ldaps settings.  
`[validateTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains/validateTrust)` |  `POST /v1beta1/{name=projects/*/locations/global/domains/*}:validateTrust`   
Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.  
  
## REST Resource: [v1beta1.projects.locations.global.domains.backups](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups)

Methods  
---  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/create)` |  `POST /v1beta1/{parent=projects/*/locations/global/domains/*}/backups`   
Creates a Backup for a domain.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/domains/*/backups/*}`   
Deletes identified Backup.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/get)` |  `GET /v1beta1/{name=projects/*/locations/global/domains/*/backups/*}`   
Gets details of a single Backup.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/global/domains/*/backups/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/list)` |  `GET /v1beta1/{parent=projects/*/locations/global/domains/*}/backups`   
Lists Backup in a given project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/patch)` |  `PATCH /v1beta1/{backup.name=projects/*/locations/global/domains/*/backups/*}`   
Updates the labels for specified Backup.  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/global/domains/*/backups/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/global/domains/*/backups/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.global.domains.sqlIntegrations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.sqlIntegrations)

Methods  
---  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.sqlIntegrations/get)` |  `GET /v1beta1/{name=projects/*/locations/global/domains/*/sqlIntegrations/*}`   
Gets details of a single sqlIntegration.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.sqlIntegrations/list)` |  `GET /v1beta1/{parent=projects/*/locations/global/domains/*}/sqlIntegrations`   
Lists SqlIntegrations in a given domain.  
  
## REST Resource: [v1beta1.projects.locations.global.operations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/global/operations}`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.global.peerings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings)

Methods  
---  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/create)` |  `POST /v1beta1/{parent=projects/*/locations/global}/peerings`   
Creates a Peering for Managed AD instance.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/global/peerings/*}`   
Deletes identified Peering.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/get)` |  `GET /v1beta1/{name=projects/*/locations/global/peerings/*}`   
Gets details of a single Peering.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/global/peerings/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/list)` |  `GET /v1beta1/{parent=projects/*/locations/global}/peerings`   
Lists Peerings in a given project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/patch)` |  `PATCH /v1beta1/{peering.name=projects/*/locations/global/peerings/*}`   
Updates the labels for specified Peering.  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/global/peerings/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/global/peerings/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.global.domains](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains)

Methods  
---  
`[attachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/attachTrust)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:attachTrust`   
Adds an AD trust to a domain.  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/create)` |  `POST /v1/{parent=projects/*/locations/global}/domains`   
Creates a Microsoft AD domain.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/delete)` |  `DELETE /v1/{name=projects/*/locations/global/domains/*}`   
Deletes a domain.  
`[detachTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/detachTrust)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:detachTrust`   
Removes an AD trust.  
`[extendSchema](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/extendSchema)` |  `POST /v1/{domain=projects/*/locations/global/domains/*}:extendSchema`   
Extend Schema for Domain  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/get)` |  `GET /v1/{name=projects/*/locations/global/domains/*}`   
Gets information about a domain.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/global/domains/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[getLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/getLdapssettings)` |  `GET /v1/{name=projects/*/locations/global/domains/*}/ldapssettings`   
Gets the domain ldaps settings.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/list)` |  `GET /v1/{parent=projects/*/locations/global}/domains`   
Lists domains in a project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/patch)` |  `PATCH /v1/{domain.name=projects/*/locations/global/domains/*}`   
Updates the metadata and configuration of a domain.  
`[reconfigureTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/reconfigureTrust)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:reconfigureTrust`   
Updates the DNS conditional forwarder.  
`[resetAdminPassword](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/resetAdminPassword)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:resetAdminPassword`   
Resets a domain's administrator password.  
`[restore](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/restore)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:restore`   
RestoreDomain restores domain backup mentioned in the RestoreDomainRequest  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/global/domains/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/global/domains/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[updateLdapssettings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/updateLdapssettings)` |  `PATCH /v1/{ldapsSettings.name=projects/*/locations/global/domains/*}/ldapssettings`   
Patches a single ldaps settings.  
`[validateTrust](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/validateTrust)` |  `POST /v1/{name=projects/*/locations/global/domains/*}:validateTrust`   
Validates a trust state, that the target domain is reachable, and that the target domain is able to accept incoming trust requests.  
  
## REST Resource: [v1.projects.locations.global.domains.backups](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups)

Methods  
---  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/create)` |  `POST /v1/{parent=projects/*/locations/global/domains/*}/backups`   
Creates a Backup for a domain.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/delete)` |  `DELETE /v1/{name=projects/*/locations/global/domains/*/backups/*}`   
Deletes identified Backup.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/get)` |  `GET /v1/{name=projects/*/locations/global/domains/*/backups/*}`   
Gets details of a single Backup.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/global/domains/*/backups/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/list)` |  `GET /v1/{parent=projects/*/locations/global/domains/*}/backups`   
Lists Backup in a given project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/patch)` |  `PATCH /v1/{backup.name=projects/*/locations/global/domains/*/backups/*}`   
Updates the labels for specified Backup.  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/global/domains/*/backups/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.backups/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/global/domains/*/backups/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.global.domains.sqlIntegrations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations)

Methods  
---  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations/get)` |  `GET /v1/{name=projects/*/locations/global/domains/*/sqlIntegrations/*}`   
Gets details of a single sqlIntegration.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.sqlIntegrations/list)` |  `GET /v1/{parent=projects/*/locations/global/domains/*}/sqlIntegrations`   
Lists SqlIntegrations in a given domain.  
  
## REST Resource: [v1.projects.locations.global.operations](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.operations/cancel)` |  `POST /v1/{name=projects/*/locations/global/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/global/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.operations/get)` |  `GET /v1/{name=projects/*/locations/global/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.operations/list)` |  `GET /v1/{name=projects/*/locations/global/operations}`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.global.peerings](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings)

Methods  
---  
`[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/create)` |  `POST /v1/{parent=projects/*/locations/global}/peerings`   
Creates a Peering for Managed AD instance.  
`[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/delete)` |  `DELETE /v1/{name=projects/*/locations/global/peerings/*}`   
Deletes identified Peering.  
`[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/get)` |  `GET /v1/{name=projects/*/locations/global/peerings/*}`   
Gets details of a single Peering.  
`[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/global/peerings/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/list)` |  `GET /v1/{parent=projects/*/locations/global}/peerings`   
Lists Peerings in a given project.  
`[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/patch)` |  `PATCH /v1/{peering.name=projects/*/locations/global/peerings/*}`   
Updates the labels for specified Peering.  
`[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/global/peerings/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.peerings/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/global/peerings/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
