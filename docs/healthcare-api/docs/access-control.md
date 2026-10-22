---
url: https://docs.cloud.google.com/healthcare-api/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:05.606259+00:00
---

# Access control with IAM  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

The Cloud Healthcare API uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) for access control.

In the Cloud Healthcare API, access control can be configured at the project, dataset, or data store level. For example, you can grant access to all datasets within a project to a group of developers. To learn how to set up and use IAM with the Cloud Healthcare API, see [Controlling access](https://docs.cloud.google.com/healthcare-api/docs/how-tos/controlling-access) and [Controlling access to other products](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products).

For a detailed description of IAM and its features, see the [IAM documentation](https://docs.cloud.google.com/iam/docs). In particular, see the section on [managing IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Every Cloud Healthcare API method requires the caller to have the necessary permissions. See Permissions and Roles for more information.

## Permissions

The following tables list the IAM permissions that are associated with the Cloud Healthcare API. Method names are shortened in the table; each method's full name begins with `projects.locations.`.

### Consent store methods

Consent store method | Required permissions  
---|---  
`datasets.consentStores.checkDataAccess` | `healthcare.consentStores.checkDataAccess` on the requested consent store.  
`datasets.consentStores.create` | `healthcare.consentStores.create` on the parent dataset.  
`datasets.consentStores.delete` | `healthcare.consentStores.delete` on the requested consent store.  
`datasets.consentStores.evaluateUserConsents` | `healthcare.consentStores.evaluateUserConsents` on the requested consent store.  
`datasets.consentStores.get` | `healthcare.consentStores.get` on the requested consent store.  
`datasets.consentStores.getIamPolicy` | `healthcare.consentStores.getIamPolicy` on the requested consent store.  
`datasets.consentStores.list` | `healthcare.consentStores.list` on the parent dataset.  
`datasets.consentStores.patch` | `healthcare.consentStores.update` on the requested consent store.  
`datasets.consentStores.queryAccessibleData` | `healthcare.consentStores.queryAccessibleData` on the requested consent store.  
`datasets.consentStores.setIamPolicy` | `healthcare.consentStores.setIamPolicy` on the requested consent store.  
`datasets.consentStores.attributeDefinitions.create` | `healthcare.attributeDefinitions.create` on the parent consent store.  
`datasets.consentStores.attributeDefinitions.delete` | `healthcare.attributeDefinitions.delete` on the requested attribute definition resource.  
`datasets.consentStores.attributeDefinitions.get` | `healthcare.attributeDefinitions.get` on the requested attribute definition resource.  
`datasets.consentStores.attributeDefinitions.list` | `healthcare.attributeDefinitions.list` on the parent consent store.  
`datasets.consentStores.attributeDefinitions.patch` | `healthcare.attributeDefinitions.update` on the requested attribute definition resource.  
`datasets.consentStores.consentArtifacts.create` | `healthcare.consentArtifacts.create` on the parent consent store.  
`datasets.consentStores.consentArtifacts.delete` | `healthcare.consentArtifacts.delete` on the requested consent artifact resource.  
`datasets.consentStores.consentArtifacts.get` | `healthcare.consentArtifacts.get` on the requested consent artifact resource.  
`datasets.consentStores.consentArtifacts.list` | `healthcare.consentArtifacts.list` on the parent consent store.  
`datasets.consentStores.consents.create` | `healthcare.consents.create` on the parent consent store.  
`datasets.consentStores.consents.delete` | `healthcare.consents.delete` on the requested consent resource.  
`datasets.consentStores.consents.get` | `healthcare.consents.get` on the requested consent resource.  
`datasets.consentStores.consents.list` | `healthcare.consents.list` on the parent consent store.  
`datasets.consentStores.consents.patch` | `healthcare.consents.update` on the requested consent resource.  
`datasets.consentStores.consents.revoke` | `healthcare.consents.revoke` on the requested consent resource.  
`datasets.consentStores.userDataMappings.archive` | `healthcare.userDataMappings.archive` on the requested user data mapping resource.  
`datasets.consentStores.userDataMappings.create` | `healthcare.userDataMappings.create` on the parent consent store.  
`datasets.consentStores.userDataMappings.delete` | `healthcare.userDataMappings.delete` on the requested user data mapping resource.  
`datasets.consentStores.userDataMappings.get` | `healthcare.userDataMappings.get` on the requested user data mapping resource.  
`datasets.consentStores.userDataMappings.list` | `healthcare.userDataMappings.list` on the parent consent store.  
`datasets.consentStores.userDataMappings.patch` | `healthcare.userDataMappings.update` on the requested user data mapping resource.  
  
### Dataset methods

Datasets method | Required permissions  
---|---  
`datasets.create` | `healthcare.datasets.create` on the parent Google Cloud project.  
`datasets.deidentify` | 

  * `healthcare.datasets.deidentify` on the source dataset.
  * `healthcare.datasets.create` on the Google Cloud project containing the destination dataset.

  
`datasets.delete` | `healthcare.datasets.delete` on the requested dataset.  
`datasets.get` | `healthcare.datasets.get` on the requested dataset.  
`datasets.getIamPolicy` | `healthcare.datasets.getIamPolicy` on the requested dataset.  
`datasets.list` | `healthcare.datasets.list` on the parent Google Cloud project.  
`datasets.patch` | `healthcare.datasets.update` on the requested dataset.  
`datasets.setIAMPolicy` | `healthcare.datasets.setIamPolicy` on the requested dataset.  
  
### DICOM store methods

DICOM store method | Required permissions  
---|---  
`datasets.dicomStores.create` | `healthcare.dicomStores.create` on the parent dataset.  
`datasets.dicomStores.deidentify` | 

  * `healthcare.dicomStores.deidentify` on the source DICOM store.
  * `healthcare.dicomStores.dicomWebWrite` on the destination DICOM store.

  
`datasets.dicomStores.delete` | `healthcare.dicomStores.delete` on the requested DICOM store.  
`datasets.dicomStores.export` | 

  * `healthcare.dicomStores.export` on the requested DICOM store.
  * When exporting to Cloud Storage: `roles/storage.objectAdmin` granted to the project's **Cloud Healthcare Service Agent** service account. See [Exporting data to Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#exporting_data_to_cloud_storage) for instructions.
  * When exporting to BigQuery: `roles/bigquery.dataEditor` and `roles/bigquery.jobUser` granted to the project's **Cloud Healthcare Service Agent** service account. See [DICOM store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_store_bigquery_permissions) for instructions.

  
`datasets.dicomStores.get` | `healthcare.dicomStores.get` on the requested DICOM store.  
`datasets.dicomStores.getIamPolicy` | `healthcare.dicomStores.getIamPolicy` on the requested DICOM store.  
`datasets.dicomStores.import` | 

  * `healthcare.dicomStores.import` on the requested DICOM store.
  * `roles/storage.objectViewer` granted to the project's **Cloud Healthcare Service Agent** service account. See [Importing data from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#importing_data_from_cloud_storage) for instructions.

  
`datasets.dicomStores.list` | `healthcare.dicomStores.list` on the parent dataset.  
`datasets.dicomStores.patch` | `healthcare.dicomStores.update` on the requested DICOM store.  
`datasets.dicomStores.searchForInstances` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.searchForSeries` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.searchForStudies` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.setIamPolicy` | `healthcare.dicomStores.setIamPolicy` on the requested DICOM store.  
`datasets.dicomStores.storeInstances` | `healthcare.dicomStores.dicomWebWrite` on the requested DICOM store.  
`datasets.dicomStores.studies.delete` | `healthcare.dicomStores.dicomWebDelete` on the requested DICOM store.  
`datasets.dicomStores.studies.retrieveMetadata` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.retrieveStudy` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.searchForInstances` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.searchForSeries` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.storeInstances` | `healthcare.dicomStores.dicomWebWrite` on the requested DICOM store.  
`datasets.dicomStores.studies.updateInstances` | `healthcare.dicomStores.dicomWebUpdate` on the requested DICOM store.  
`datasets.dicomStores.studies.updateMetadata` | `healthcare.dicomStores.dicomWebUpdate` on the requested DICOM store.  
`datasets.dicomStores.studies.series.delete` | `healthcare.dicomStores.dicomWebDelete` on the requested DICOM store.  
`datasets.dicomStores.studies.series.retrieveMetadata` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.retrieveSeries` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.searchForInstances` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.updateMetadata` | `healthcare.dicomStores.dicomWebUpdate` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.delete` | `healthcare.dicomStores.dicomWebDelete` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.retrieveInstance` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.retrieveMetadata` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.retrieveRendered` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.updateMetadata` | `healthcare.dicomStores.dicomWebUpdate` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.frames.retrieveFrames` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.frames.retrieveRendered` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
`datasets.dicomStores.studies.series.instances.bulkdata.retrieveBulkdata` | `healthcare.dicomStores.dicomWebRead` on the requested DICOM store.  
  
### FHIR store methods

FHIR store method | Required permissions  
---|---  
`datasets.fhirStores.applyConsents` | `healthcare.fhirStores.applyConsents` on the requested FHIR store resource.  
`datasets.fhirStores.applyAdminConsents` | `healthcare.fhirStores.applyConsents` on the requested FHIR store resource.  
`datasets.fhirStores.configureSearch` | `healthcare.fhirStores.configureSearch` on the requested FHIR store.  
`datasets.fhirStores.create` | `healthcare.fhirStores.create` on the parent dataset.  
`datasets.fhirStores.deidentify` | 

  * `healthcare.fhirStores.deidentify` on the source FHIR store.
  * `healthcare.fhirResources.update` on the destination FHIR store.

  
`datasets.fhirStores.delete` | `healthcare.fhirStores.delete` on the requested FHIR store.  
`datasets.fhirStores.explainDataAccess` | `healthcare.fhirStores.explainDataAccess` on the requested FHIR store resource.  
`datasets.fhirStores.export` | 

  * `healthcare.fhirStores.export` on the requested FHIR store.
  * When exporting to Cloud Storage: `storage.objects.create`, `storage.objects.delete`, and `storage.objects.list` granted to the project's **Cloud Healthcare Service Agent** service account. See [Exporting FHIR resources to Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#exporting-fhir-resources) for instructions.
  * When exporting to BigQuery: `roles/bigquery.dataEditor` and `roles/bigquery.jobUser` granted to the project's **Cloud Healthcare Service Agent** service account. See [FHIR store BigQuery permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_bigquery_permissions) for instructions.

  
`datasets.fhirStores.get` | `healthcare.fhirStores.get` on the requested FHIR store.  
`datasets.fhirStores.getFHIRStoreMetrics` | `healthcare.fhirStores.get` on the requested FHIR store.  
`datasets.fhirStores.getIamPolicy` | `healthcare.fhirStores.getIamPolicy` on the requested FHIR store.  
`datasets.fhirStores.import` | 

  * `healthcare.fhirStores.import` on the requested FHIR store.
  * `storage.objects.get` and `storage.objects.list` granted to the project's **Cloud Healthcare Service Agent** service account. See [Importing FHIR resources from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#importing-fhir-resources) for instructions.

  
`datasets.fhirStores.list` | `healthcare.fhirStores.list` on the parent dataset.  
`datasets.fhirStores.patch` | `healthcare.fhirStores.update` on the requested FHIR store.  
`datasets.fhirStores.rollback` | `healthcare.fhirStores.rollback` on the requested FHIR store.  
`datasets.fhirStores.setIamPolicy` | `healthcare.fhirStores.setIamPolicy` on the requested FHIR store.  
`datasets.fhirStores.fhir.Encounter-everything` | `healthcare.fhirResources.get` on each resource returned.  
`datasets.fhirStores.fhir.Observation-lastn` | `healthcare.fhirStores.searchResources` on the parent FHIR store.  
`datasets.fhirStores.fhir.Patient-everything` | `healthcare.fhirResources.get` on each resource returned.  
`datasets.fhirStores.fhir.Resource-purge` | `healthcare.fhirResources.purge` on the requested FHIR store resource.  
`datasets.fhirStores.fhir.capabilities` | `healthcare.fhirStores.get` on the requested FHIR store.  
`datasets.fhirStores.fhir.conditionalDelete` | 

  * `healthcare.fhirStores.searchResources` on the parent FHIR store.
  * `healthcare.fhirResources.delete` on the requested FHIR store resource.

  
`datasets.fhirStores.fhir.conditionalPatch` | 

  * `healthcare.fhirStores.searchResources` on the parent FHIR store.
  * `healthcare.fhirResources.patch` on the requested FHIR store resource.

  
`datasets.fhirStores.fhir.conditionalUpdate` | 

  * `healthcare.fhirStores.searchResources` on the parent FHIR store.
  * `healthcare.fhirResources.update` on the requested FHIR store resource.

  
`datasets.fhirStores.fhir.create` | 

  * For conditional create interactions: `healthcare.fhirResources.create` and `healthcare.fhirStores.searchResources` on the parent FHIR store.
  * For create interactions: `healthcare.fhirResources.create` on the parent FHIR store.

  
`datasets.fhirStores.fhir.delete` | `healthcare.fhirResources.delete` on the requested FHIR store resource.  
`datasets.fhirStores.fhir.executeBundle` | `healthcare.fhirResources.executeBundle` on the requested FHIR store, and additional permissions (such as `healthcare.fhirResources.create` and `healthcare.fhirResources.update`) corresponding to individual operations within the bundle. If the API caller has `healthcare.fhirResources.create` permissions but not `healthcare.fhirResources.update` permissions, the caller can only execute bundles containing `healthcare.fhirResources.create` operations.  
`datasets.fhirStores.fhir.history` | `healthcare.fhirResources.get` on the requested FHIR store resource and each of its versions.  
`datasets.fhirStores.fhir.patch` | `healthcare.fhirResources.patch` on the requested FHIR store resource.  
`datasets.fhirStores.fhir.read` | `healthcare.fhirResources.get` on the requested FHIR store resource.  
`datasets.fhirStores.fhir.search` | `healthcare.fhirStores.searchResources` on the parent FHIR store.  
`datasets.fhirStores.fhir.update` | `healthcare.fhirResources.update` on the requested FHIR store resource.  
`datasets.fhirStores.fhir.vread` | `healthcare.fhirResources.get` on the requested FHIR store resource version.  
`datasets.fhirStores.fhir.Patient-consent-enforcement-status` | `healthcare.fhirResources.get` on the requested FHIR store patient resource.  
`datasets.fhirStores.fhir.Consent-enforcement-status` | `healthcare.fhirResources.get` on the requested FHIR store consent resource.  
  
### HL7v2 store methods

HL7v2 store method | Required permissions  
---|---  
`datasets.hl7V2Stores.create` | `healthcare.hl7V2Stores.create` on the parent dataset.  
`datasets.hl7V2Stores.delete` | `healthcare.hl7V2Stores.delete` on the requested HL7v2 store.  
`datasets.hl7V2Stores.export` | `healthcare.hl7V2Stores.export` on the requested HL7v2 store.  
`datasets.hl7V2Stores.get` | `healthcare.hl7V2Stores.get` on the requested HL7v2 store.  
`datasets.hl7V2Stores.import` | `healthcare.hl7V2Stores.import` on the requested HL7v2 store.  
`datasets.hl7V2Stores.list` | `healthcare.hl7V2Stores.list` on the parent dataset.  
`datasets.hl7V2Stores.patch` | `healthcare.hl7V2Stores.update` on the requested HL7v2 store.  
`datasets.hl7V2Stores.getIamPolicy` | `healthcare.hl7V2Stores.getIamPolicy` on the requested HL7v2 store.  
`datasets.hl7V2Stores.setIamPolicy` | `healthcare.hl7V2Stores.setIamPolicy` on the requested HL7v2 store.  
`datasets.hl7V2Stores.messages.create` | `healthcare.hl7V2Messages.create` on the parent HL7v2 store.  
`datasets.hl7V2Stores.messages.delete` | `healthcare.hl7V2Messages.delete` on the requested HL7v2 store message.  
`datasets.hl7V2Stores.messages.get` | `healthcare.hl7V2Messages.get` on the requested HL7v2 store message.  
`datasets.hl7V2Stores.messages.ingest` | `healthcare.hl7V2Messages.ingest` on the requested HL7v2 store message.  
`datasets.hl7V2Stores.messages.list` | `healthcare.hl7V2Messages.list` on the parent HL7v2 store.  
`datasets.hl7V2Stores.messages.patch` | `healthcare.hl7V2Messages.update` on the requested HL7v2 store message.  
  
### Location methods

Location method | Required permissions  
---|---  
`locations.get` | `healthcare.locations.get` on the requested location.  
`locations.list` | `healthcare.locations.list` on the parent Google Cloud project.  
  
### Healthcare Natural Language API methods

Healthcare Natural Language API method | Required permissions  
---|---  
`nlp.analyzeEntities` | `healthcare.nlpservice.analyzeEntities`  
  
### Operation methods

Operation method | Required permission  
---|---  
`datasets.operations.get` | `healthcare.operations.get` on the requested dataset.  
`datasets.operations.list` | `healthcare.operations.list` on the requested dataset.  
`datasets.operations.cancel` | `healthcare.operations.cancel` on the requested dataset.  
  
### De-identify methods

De-identify method | Required permission  
---|---  
`services.deidentify.deidentifyDicomInstance` | `healthcare.deidentify.run`  
`services.deidentify.deidentifyFhirResource` | `healthcare.deidentify.run`  
  
## Roles

The following tables list the Cloud Healthcare API IAM roles, including the permissions associated with each role. The roles `roles/owner`, `roles/editor`, and `roles/viewer` include permissions for other Google Cloud services. For more information about roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note:** Granting viewer roles at the store level, such as `roles/healthcare.dicomViewer`, does not also grant the role for the dataset. To view long-running operations for the dataset, you must also grant either the dataset viewer role, such as `roles/healthcare.datasetViewer`, or the data store viewer role, such as `roles/healthcare.dicomViewer`, for the dataset.

### Consent store roles

Consent store role | Permissions  
---|---  
  
#### Healthcare Consent Store Viewer 

(`roles/healthcare.consentStoreViewer`) List Consent Stores in a dataset.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Store Administrator 

(`roles/healthcare.consentStoreAdmin`) Administer Consent stores.  |  `healthcare.consentStores.*`

  * `healthcare.consentStores.checkDataAccess`
  * `healthcare.consentStores.create`
  * `healthcare.consentStores.delete`
  * `healthcare.consentStores.evaluateUserConsents`
  * `healthcare.consentStores.get`
  * `healthcare.consentStores.getIamPolicy`
  * `healthcare.consentStores.list`
  * `healthcare.consentStores.queryAccessibleData`
  * `healthcare.consentStores.setIamPolicy`
  * `healthcare.consentStores.update`

`healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Consents roles

Consents role | Permissions  
---|---  
  
#### Healthcare Attribute Definition Reader 

(`roles/healthcare.attributeDefinitionReader`) Read AttributeDefinition objects in a consent store.  |  `healthcare.attributeDefinitions.get` `healthcare.attributeDefinitions.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Attribute Definition Editor 

(`roles/healthcare.attributeDefinitionEditor`) Edit AttributeDefinition objects.  |  `healthcare.attributeDefinitions.*`

  * `healthcare.attributeDefinitions.create`
  * `healthcare.attributeDefinitions.delete`
  * `healthcare.attributeDefinitions.get`
  * `healthcare.attributeDefinitions.list`
  * `healthcare.attributeDefinitions.update`

`healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Artifact Reader 

(`roles/healthcare.consentArtifactReader`) Read ConsentArtifact objects in a consent store.  |  `healthcare.consentArtifacts.get` `healthcare.consentArtifacts.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Artifact Editor 

(`roles/healthcare.consentArtifactEditor`) Edit ConsentArtifact objects.  |  `healthcare.consentArtifacts.create` `healthcare.consentArtifacts.get` `healthcare.consentArtifacts.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Artifact Administrator 

(`roles/healthcare.consentArtifactAdmin`) Administer ConsentArtifact objects.  |  `healthcare.consentArtifacts.*`

  * `healthcare.consentArtifacts.create`
  * `healthcare.consentArtifacts.delete`
  * `healthcare.consentArtifacts.get`
  * `healthcare.consentArtifacts.list`

`healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Reader 

(`roles/healthcare.consentReader`) Read Consent objects in a consent store.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.consents.get` `healthcare.consents.list` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Editor 

(`roles/healthcare.consentEditor`) Edit Consent objects.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.consents.*`

  * `healthcare.consents.activate`
  * `healthcare.consents.create`
  * `healthcare.consents.delete`
  * `healthcare.consents.get`
  * `healthcare.consents.list`
  * `healthcare.consents.reject`
  * `healthcare.consents.revoke`
  * `healthcare.consents.update`

`healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare User Data Mapping Reader 

(`roles/healthcare.userDataMappingReader`) Read UserDataMapping objects in a consent store.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `healthcare.userDataMappings.get` `healthcare.userDataMappings.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare User Data Mapping Editor 

(`roles/healthcare.userDataMappingEditor`) Edit UserDataMapping objects.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `healthcare.userDataMappings.*`

  * `healthcare.userDataMappings.archive`
  * `healthcare.userDataMappings.create`
  * `healthcare.userDataMappings.delete`
  * `healthcare.userDataMappings.get`
  * `healthcare.userDataMappings.list`
  * `healthcare.userDataMappings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Datasets roles

Datasets role | Permissions  
---|---  
  
#### Healthcare Dataset Viewer 

(`roles/healthcare.datasetViewer`) List the Healthcare Datasets in a project.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Dataset Administrator 

(`roles/healthcare.datasetAdmin`) Administer Healthcare Datasets.  |  `healthcare.datasets.*`

  * `healthcare.datasets.create`
  * `healthcare.datasets.deidentify`
  * `healthcare.datasets.delete`
  * `healthcare.datasets.get`
  * `healthcare.datasets.getIamPolicy`
  * `healthcare.datasets.list`
  * `healthcare.datasets.setIamPolicy`
  * `healthcare.datasets.update`

`healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.*`

  * `healthcare.operations.cancel`
  * `healthcare.operations.get`
  * `healthcare.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### DICOM store roles

DICOM store role | Permissions  
---|---  
  
#### Healthcare DICOM Store Viewer 

(`roles/healthcare.dicomStoreViewer`) List DICOM Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.get` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Store Administrator 

(`roles/healthcare.dicomStoreAdmin`) Administer DICOM stores.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.create` `healthcare.dicomStores.deidentify` `healthcare.dicomStores.delete` `healthcare.dicomStores.dicomWebDelete` `healthcare.dicomStores.get` `healthcare.dicomStores.getIamPolicy` `healthcare.dicomStores.list` `healthcare.dicomStores.setIamPolicy` `healthcare.dicomStores.update` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Viewer 

(`roles/healthcare.dicomViewer`) Retrieve DICOM images from a DICOM store.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.dicomWebRead` `healthcare.dicomStores.export` `healthcare.dicomStores.get` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Editor 

(`roles/healthcare.dicomEditor`) Edit DICOM images individually and in bulk.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.dicomWebDelete` `healthcare.dicomStores.dicomWebRead` `healthcare.dicomStores.dicomWebUpdate` `healthcare.dicomStores.dicomWebWrite` `healthcare.dicomStores.export` `healthcare.dicomStores.get` `healthcare.dicomStores.import` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### FHIR store roles

FHIR store role | Permissions  
---|---  
  
#### Healthcare FHIR Store Viewer 

(`roles/healthcare.fhirStoreViewer`) List FHIR Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Store Administrator 

(`roles/healthcare.fhirStoreAdmin`) Administer FHIR resource stores.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.purge` `healthcare.fhirStores.applyConsents` `healthcare.fhirStores.bulkDelete` `healthcare.fhirStores.configureSearch` `healthcare.fhirStores.create` `healthcare.fhirStores.deidentify` `healthcare.fhirStores.delete` `healthcare.fhirStores.deleteFhirOperation` `healthcare.fhirStores.explainDataAccess` `healthcare.fhirStores.export` `healthcare.fhirStores.get` `healthcare.fhirStores.getFhirOperation` `healthcare.fhirStores.getIamPolicy` `healthcare.fhirStores.import` `healthcare.fhirStores.list` `healthcare.fhirStores.rollback` `healthcare.fhirStores.setIamPolicy` `healthcare.fhirStores.update` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Resource Reader 

(`roles/healthcare.fhirResourceReader`) Read and search FHIR resources.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.get` `healthcare.fhirResources.translateConceptMap` `healthcare.fhirStores.executeBundle` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.fhirStores.searchResources` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Resource Editor 

(`roles/healthcare.fhirResourceEditor`) Create, delete, update, read and search FHIR resources.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.create` `healthcare.fhirResources.delete` `healthcare.fhirResources.get` `healthcare.fhirResources.patch` `healthcare.fhirResources.translateConceptMap` `healthcare.fhirResources.update` `healthcare.fhirStores.executeBundle` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.fhirStores.searchResources` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### HL7v2 store roles

HL7v2 store role | Permissions  
---|---  
  
#### Healthcare HL7v2 Store Viewer 

(`roles/healthcare.hl7V2StoreViewer`) View HL7v2 Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare HL7v2 Store Administrator 

(`roles/healthcare.hl7V2StoreAdmin`) Administer HL7v2 Stores.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Stores.*`

  * `healthcare.hl7V2Stores.create`
  * `healthcare.hl7V2Stores.delete`
  * `healthcare.hl7V2Stores.export`
  * `healthcare.hl7V2Stores.get`
  * `healthcare.hl7V2Stores.getIamPolicy`
  * `healthcare.hl7V2Stores.import`
  * `healthcare.hl7V2Stores.list`
  * `healthcare.hl7V2Stores.rollback`
  * `healthcare.hl7V2Stores.setIamPolicy`
  * `healthcare.hl7V2Stores.update`

`healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare HL7v2 Message Ingest 

(`roles/healthcare.hl7V2Ingest`) Ingest HL7v2 messages received from a source network.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Messages.ingest` `healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare HL7v2 Message Consumer 

(`roles/healthcare.hl7V2Consumer`) List and read HL7v2 messages, update message labels, and publish new messages.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Messages.create` `healthcare.hl7V2Messages.get` `healthcare.hl7V2Messages.list` `healthcare.hl7V2Messages.update` `healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare HL7v2 Message Editor 

(`roles/healthcare.hl7V2Editor`) Read, write, and delete access to HL7v2 messages.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Messages.*`

  * `healthcare.hl7V2Messages.create`
  * `healthcare.hl7V2Messages.delete`
  * `healthcare.hl7V2Messages.get`
  * `healthcare.hl7V2Messages.ingest`
  * `healthcare.hl7V2Messages.list`
  * `healthcare.hl7V2Messages.update`

`healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Healthcare Natural Language API roles

Healthcare Natural Language API role | Permissions  
---|---  
  
#### Healthcare NLP Service Viewer Beta

(`roles/healthcare.nlpServiceViewer`) Extract and analyze medical entities from a given text.  |  `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.nlpservice.analyzeEntities` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud Healthcare Service Agent

The **Cloud Healthcare Service Agent** is a shared [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your project that Cloud Healthcare API uses to interact with other resources in Google Cloud.

For example, this service agent is used to read and write to Cloud Storage buckets, write to BigQuery, and to publish messages to Pub/Sub from the Cloud Healthcare API.

To execute any of the preceding actions, you must give the **Cloud Healthcare Service Agent** access to the relevant Cloud Storage bucket, BigQuery dataset, or Pub/Sub topic.

As you create a permission model for your project, remember that granting any of the roles listed below allows the user to invoke operations that run as the **Cloud Healthcare Service Agent** and have access to any data that the agent has access to:

  * `roles/healthcare.consentStoreAdmin`
  * `roles/healthcare.consentStoreViewer`
  * `roles/healthcare.dicomStoreEditor`
  * `roles/healthcare.dicomStoreViewer`
  * `roles/healthcare.fhirStoreAdmin`
  * `roles/healthcare.hl7V2StoreAdmin`



Similarly, assigning the following permissions to custom roles would also allow the user to invoke operations that will run as the **Cloud Healthcare Service Agent** :

  * `healthcare.consentStores.queryAccessibleData`
  * `healthcare.dicomStores.create`
  * `healthcare.dicomStores.update`
  * `healthcare.dicomStores.import`
  * `healthcare.dicomStores.export`
  * `healthcare.fhirStores.create`
  * `healthcare.fhirStores.update`
  * `healthcare.fhirStores.import`
  * `healthcare.fhirStores.export`
  * `healthcare.hl7V2Stores.create`
  * `healthcare.hl7V2Stores.update`



For example:

  * If a user has any import permissions, then the user can run operations that act as the **Cloud Healthcare Service Agent** if those operations access any Cloud Storage buckets that the **Cloud Healthcare Service Agent** has read access to.
  * If a user has any export permissions, then the user can run operations that act as the **Cloud Healthcare Service Agent** if those operations access any bucket that the service agent has write access to.
  * A user who has create or update data store permissions has the ability to configure Pub/Sub notification targets or BigQuery streaming destinations that are sent by the **Cloud Healthcare Service Agent** when changes are made to the data store.



As a best practice, leverage multiple projects to further isolate the permissions given to the **Cloud Healthcare Service Agent**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
