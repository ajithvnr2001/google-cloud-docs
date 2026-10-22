---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare/
title: Cloud Healthcare API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:34.100192+00:00
---

# Cloud Healthcare API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Healthcare API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Healthcare API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Healthcare API roles

Role | Permissions  
---|---  
  
#### Healthcare Annotation Editor 

(`roles/healthcare.annotationEditor`) Create, delete, update, read and list annotations.  |  `healthcare.annotationStores.get` `healthcare.annotationStores.list` `healthcare.annotations.*`

  * `healthcare.annotations.create`
  * `healthcare.annotations.delete`
  * `healthcare.annotations.get`
  * `healthcare.annotations.list`
  * `healthcare.annotations.update`

`healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Annotation Reader 

(`roles/healthcare.annotationReader`) Read and list annotations in an Annotation store.  |  `healthcare.annotationStores.get` `healthcare.annotationStores.list` `healthcare.annotations.get` `healthcare.annotations.list` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Annotation Administrator 

(`roles/healthcare.annotationStoreAdmin`) Administer Annotation stores.  |  `healthcare.annotationStores.*`

  * `healthcare.annotationStores.create`
  * `healthcare.annotationStores.delete`
  * `healthcare.annotationStores.evaluate`
  * `healthcare.annotationStores.export`
  * `healthcare.annotationStores.get`
  * `healthcare.annotationStores.getIamPolicy`
  * `healthcare.annotationStores.import`
  * `healthcare.annotationStores.list`
  * `healthcare.annotationStores.setIamPolicy`
  * `healthcare.annotationStores.update`

`healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Annotation Store Viewer 

(`roles/healthcare.annotationStoreViewer`) List Annotation Stores in a dataset.  |  `healthcare.annotationStores.get` `healthcare.annotationStores.list` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

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
  
#### Healthcare Attribute Definition Reader 

(`roles/healthcare.attributeDefinitionReader`) Read AttributeDefinition objects in a consent store.  |  `healthcare.attributeDefinitions.get` `healthcare.attributeDefinitions.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

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
  
#### Healthcare Consent Artifact Editor 

(`roles/healthcare.consentArtifactEditor`) Edit ConsentArtifact objects.  |  `healthcare.consentArtifacts.create` `healthcare.consentArtifacts.get` `healthcare.consentArtifacts.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare Consent Artifact Reader 

(`roles/healthcare.consentArtifactReader`) Read ConsentArtifact objects in a consent store.  |  `healthcare.consentArtifacts.get` `healthcare.consentArtifacts.list` `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

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
  
#### Healthcare Consent Reader 

(`roles/healthcare.consentReader`) Read Consent objects in a consent store.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.consents.get` `healthcare.consents.list` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

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
  
#### Healthcare Consent Store Viewer 

(`roles/healthcare.consentStoreViewer`) List Consent Stores in a dataset.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

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
  
#### Healthcare Dataset Viewer 

(`roles/healthcare.datasetViewer`) List the Healthcare Datasets in a project.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Editor 

(`roles/healthcare.dicomEditor`) Edit DICOM images individually and in bulk.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.dicomWebDelete` `healthcare.dicomStores.dicomWebRead` `healthcare.dicomStores.dicomWebUpdate` `healthcare.dicomStores.dicomWebWrite` `healthcare.dicomStores.export` `healthcare.dicomStores.get` `healthcare.dicomStores.import` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Store Administrator 

(`roles/healthcare.dicomStoreAdmin`) Administer DICOM stores.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.create` `healthcare.dicomStores.deidentify` `healthcare.dicomStores.delete` `healthcare.dicomStores.dicomWebDelete` `healthcare.dicomStores.get` `healthcare.dicomStores.getIamPolicy` `healthcare.dicomStores.list` `healthcare.dicomStores.setIamPolicy` `healthcare.dicomStores.update` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Store Viewer 

(`roles/healthcare.dicomStoreViewer`) List DICOM Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.get` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare DICOM Viewer 

(`roles/healthcare.dicomViewer`) Retrieve DICOM images from a DICOM store.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.dicomStores.dicomWebRead` `healthcare.dicomStores.export` `healthcare.dicomStores.get` `healthcare.dicomStores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Resource Editor 

(`roles/healthcare.fhirResourceEditor`) Create, delete, update, read and search FHIR resources.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.create` `healthcare.fhirResources.delete` `healthcare.fhirResources.get` `healthcare.fhirResources.patch` `healthcare.fhirResources.translateConceptMap` `healthcare.fhirResources.update` `healthcare.fhirStores.executeBundle` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.fhirStores.searchResources` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Resource Reader 

(`roles/healthcare.fhirResourceReader`) Read and search FHIR resources.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.get` `healthcare.fhirResources.translateConceptMap` `healthcare.fhirStores.executeBundle` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.fhirStores.searchResources` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Store Administrator 

(`roles/healthcare.fhirStoreAdmin`) Administer FHIR resource stores.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirResources.purge` `healthcare.fhirStores.applyConsents` `healthcare.fhirStores.bulkDelete` `healthcare.fhirStores.configureSearch` `healthcare.fhirStores.create` `healthcare.fhirStores.deidentify` `healthcare.fhirStores.delete` `healthcare.fhirStores.deleteFhirOperation` `healthcare.fhirStores.explainDataAccess` `healthcare.fhirStores.export` `healthcare.fhirStores.get` `healthcare.fhirStores.getFhirOperation` `healthcare.fhirStores.getIamPolicy` `healthcare.fhirStores.import` `healthcare.fhirStores.list` `healthcare.fhirStores.rollback` `healthcare.fhirStores.setIamPolicy` `healthcare.fhirStores.update` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.cancel` `healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare FHIR Store Viewer 

(`roles/healthcare.fhirStoreViewer`) List FHIR Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.fhirStores.get` `healthcare.fhirStores.list` `healthcare.locations.*`

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
  
#### Healthcare HL7v2 Message Ingest 

(`roles/healthcare.hl7V2Ingest`) Ingest HL7v2 messages received from a source network.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Messages.ingest` `healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

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
  
#### Healthcare HL7v2 Store Viewer 

(`roles/healthcare.hl7V2StoreViewer`) View HL7v2 Stores in a dataset.  |  `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.hl7V2Stores.get` `healthcare.hl7V2Stores.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Healthcare NLP Service Viewer Beta

(`roles/healthcare.nlpServiceViewer`) Extract and analyze medical entities from a given text.  |  `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.nlpservice.analyzeEntities` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
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
  
#### Healthcare User Data Mapping Reader 

(`roles/healthcare.userDataMappingReader`) Read UserDataMapping objects in a consent store.  |  `healthcare.consentStores.checkDataAccess` `healthcare.consentStores.evaluateUserConsents` `healthcare.consentStores.get` `healthcare.consentStores.list` `healthcare.consentStores.queryAccessibleData` `healthcare.datasets.get` `healthcare.datasets.list` `healthcare.locations.*`

  * `healthcare.locations.get`
  * `healthcare.locations.list`

`healthcare.operations.get` `healthcare.userDataMappings.get` `healthcare.userDataMappings.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Healthcare Service Agent 

(`roles/healthcare.serviceAgent`) Gives the Healthcare Service Account access to networks, Kubernetes engine, and Pub/Sub resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudnotifications.activities.list` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.resourceMetadata.list` `pubsub.snapshots.seek` `pubsub.subscriptions.consume` `pubsub.topics.attachSubscription` `pubsub.topics.publish` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
## Cloud Healthcare API permissions

Permission | Included in roles  
---|---  
  
#### `healthcare.annotationStores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)   
  
#### `healthcare.annotationStores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)   
  
#### `healthcare.annotationStores.evaluate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotationStores.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotationStores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotationStores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotationStores.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)   
  
#### `healthcare.annotationStores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotationStores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)   
  
#### `healthcare.annotationStores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)   
  
#### `healthcare.annotations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)   
  
#### `healthcare.annotations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)   
  
#### `healthcare.annotations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.annotations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)   
  
#### `healthcare.attributeDefinitions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)   
  
#### `healthcare.attributeDefinitions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)   
  
#### `healthcare.attributeDefinitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.attributeDefinitions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.attributeDefinitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)   
  
#### `healthcare.consentArtifacts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)   
  
#### `healthcare.consentArtifacts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)   
  
#### `healthcare.consentArtifacts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentArtifacts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.checkDataAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)   
  
#### `healthcare.consentStores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)   
  
#### `healthcare.consentStores.evaluateUserConsents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.queryAccessibleData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consentStores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)   
  
#### `healthcare.consentStores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)   
  
#### `healthcare.consents.activate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.consents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.consents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.consents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.consents.reject`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.consents.revoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.consents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)   
  
#### `healthcare.datasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)   
  
#### `healthcare.datasets.deidentify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)   
  
#### `healthcare.datasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)   
  
#### `healthcare.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare Dataset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetViewer) (`roles/healthcare.datasetViewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.datasets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.datasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare Dataset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetViewer) (`roles/healthcare.datasetViewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.datasets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)   
  
#### `healthcare.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)   
  
#### `healthcare.dicomStores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.dicomStores.deidentify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.dicomStores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.dicomStores.dicomWebDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.dicomStores.dicomWebRead`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.dicomStores.dicomWebUpdate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)   
  
#### `healthcare.dicomStores.dicomWebWrite`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)   
  
#### `healthcare.dicomStores.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.dicomStores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.dicomStores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.dicomStores.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)   
  
#### `healthcare.dicomStores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.dicomStores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.dicomStores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)   
  
#### `healthcare.fhirResources.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)   
  
#### `healthcare.fhirResources.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)   
  
#### `healthcare.fhirResources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirResources.patch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)   
  
#### `healthcare.fhirResources.purge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirResources.translateConceptMap`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirResources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)   
  
#### `healthcare.fhirStores.applyConsents`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.bulkDelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.configureSearch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.deidentify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.deleteFhirOperation`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.executeBundle`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.explainDataAccess`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.getFhirOperation`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.rollback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.searchResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.fhirStores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.fhirStores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)   
  
#### `healthcare.hl7V2Messages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)   
  
#### `healthcare.hl7V2Messages.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)   
  
#### `healthcare.hl7V2Messages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Messages.ingest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)   
  
#### `healthcare.hl7V2Messages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Messages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)   
  
#### `healthcare.hl7V2Stores.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.hl7V2Stores.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.hl7V2Stores.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Stores.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Stores.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Stores.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.hl7V2Stores.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.hl7V2Stores.rollback`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.hl7V2Stores.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.hl7V2Stores.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare Dataset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetViewer) (`roles/healthcare.datasetViewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Healthcare NLP Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.nlpServiceViewer) (`roles/healthcare.nlpServiceViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare Dataset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetViewer) (`roles/healthcare.datasetViewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Healthcare NLP Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.nlpServiceViewer) (`roles/healthcare.nlpServiceViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.nlpservice.analyzeEntities`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare NLP Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.nlpServiceViewer) (`roles/healthcare.nlpServiceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)   
  
#### `healthcare.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare Annotation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationEditor) (`roles/healthcare.annotationEditor`)  [Healthcare Annotation Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationReader) (`roles/healthcare.annotationReader`)  [Healthcare Annotation Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreAdmin) (`roles/healthcare.annotationStoreAdmin`)  [Healthcare Annotation Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.annotationStoreViewer) (`roles/healthcare.annotationStoreViewer`)  [Healthcare Attribute Definition Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionEditor) (`roles/healthcare.attributeDefinitionEditor`)  [Healthcare Attribute Definition Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.attributeDefinitionReader) (`roles/healthcare.attributeDefinitionReader`)  [Healthcare Consent Artifact Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactAdmin) (`roles/healthcare.consentArtifactAdmin`)  [Healthcare Consent Artifact Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactEditor) (`roles/healthcare.consentArtifactEditor`)  [Healthcare Consent Artifact Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentArtifactReader) (`roles/healthcare.consentArtifactReader`)  [Healthcare Consent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentEditor) (`roles/healthcare.consentEditor`)  [Healthcare Consent Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentReader) (`roles/healthcare.consentReader`)  [Healthcare Consent Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreAdmin) (`roles/healthcare.consentStoreAdmin`)  [Healthcare Consent Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.consentStoreViewer) (`roles/healthcare.consentStoreViewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Healthcare Dataset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetViewer) (`roles/healthcare.datasetViewer`)  [Healthcare DICOM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomEditor) (`roles/healthcare.dicomEditor`)  [Healthcare DICOM Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreAdmin) (`roles/healthcare.dicomStoreAdmin`)  [Healthcare DICOM Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomStoreViewer) (`roles/healthcare.dicomStoreViewer`)  [Healthcare DICOM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.dicomViewer) (`roles/healthcare.dicomViewer`)  [Healthcare FHIR Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceEditor) (`roles/healthcare.fhirResourceEditor`)  [Healthcare FHIR Resource Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirResourceReader) (`roles/healthcare.fhirResourceReader`)  [Healthcare FHIR Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreAdmin) (`roles/healthcare.fhirStoreAdmin`)  [Healthcare FHIR Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.fhirStoreViewer) (`roles/healthcare.fhirStoreViewer`)  [Healthcare HL7v2 Message Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Consumer) (`roles/healthcare.hl7V2Consumer`)  [Healthcare HL7v2 Message Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Editor) (`roles/healthcare.hl7V2Editor`)  [Healthcare HL7v2 Message Ingest](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2Ingest) (`roles/healthcare.hl7V2Ingest`)  [Healthcare HL7v2 Store Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreAdmin) (`roles/healthcare.hl7V2StoreAdmin`)  [Healthcare HL7v2 Store Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.hl7V2StoreViewer) (`roles/healthcare.hl7V2StoreViewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare Dataset Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.datasetAdmin) (`roles/healthcare.datasetAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.userDataMappings.archive`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)   
  
#### `healthcare.userDataMappings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)   
  
#### `healthcare.userDataMappings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)   
  
#### `healthcare.userDataMappings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.userDataMappings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)  [Healthcare User Data Mapping Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingReader) (`roles/healthcare.userDataMappingReader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `healthcare.userDataMappings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Healthcare User Data Mapping Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/healthcare#healthcare.userDataMappingEditor) (`roles/healthcare.userDataMappingEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
