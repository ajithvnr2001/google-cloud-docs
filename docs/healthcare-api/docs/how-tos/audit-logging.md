---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging/
title: Cloud Healthcare API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:55.393587+00:00
---

# Cloud Healthcare API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Cloud Healthcare API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Cloud Healthcare API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Cloud Healthcare API audit logs use the service name `healthcare.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="healthcare.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Healthcare API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.healthcare.v1.consent.ConsentService.GetConsentStore`  
`google.cloud.healthcare.v1.consent.ConsentService.ListConsentStores`  
`google.cloud.healthcare.v1.dataset.DatasetService.GetDataset`  
`google.cloud.healthcare.v1.dataset.DatasetService.ListDatasets`  
`google.cloud.healthcare.v1.dicom.DicomService.GetDicomStore`  
`google.cloud.healthcare.v1.dicom.DicomService.GetDicomStoreMetrics`  
`google.cloud.healthcare.v1.dicom.DicomService.ListDicomStores`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ExplainDataAccess`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStore`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStoreMetrics`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ListFhirStores`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ExecuteBundle`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetCapabilityStatement`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2Store`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListHl7V2Stores`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentStore`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentStores`  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.GetDataset`  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.ListDatasets`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStore`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStoreMetrics`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.ListDicomStores`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExplainDataAccess`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStore`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStoreMetrics`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ListFhirStores`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ExecuteBundle`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetCapabilityStatement`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2Store`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListHl7V2Stores`  
`google.cloud.location.Locations.GetLocation`  
`google.cloud.location.Locations.ListLocations`  
`google.iam.v1.IAMPolicy.GetIamPolicy`  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.healthcare.v1.consent.ConsentService.CreateConsentStore`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentStore`  
`google.cloud.healthcare.v1.consent.ConsentService.UpdateConsentStore`  
`google.cloud.healthcare.v1.dataset.DatasetService.CreateDataset` (LRO)  
`google.cloud.healthcare.v1.dataset.DatasetService.DeleteDataset`  
`google.cloud.healthcare.v1.dataset.DatasetService.UpdateDataset`  
`google.cloud.healthcare.v1.dicom.DicomService.CreateDicomStore`  
`google.cloud.healthcare.v1.dicom.DicomService.DeleteDicomStore`  
`google.cloud.healthcare.v1.dicom.DicomService.UpdateDicomStore`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyAdminConsents` (LRO)  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyConsents` (LRO)  
`google.cloud.healthcare.v1.fhir.FhirStoreService.CreateFhirStore`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.DeleteFhirStore`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.UpdateFhirStore`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateHl7V2Store`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteHl7V2Store`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateHl7V2Store`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentStore`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentStore`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsentStore`  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.CreateDataset` (LRO)  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.DeleteDataset`  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.UpdateDataset`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.CreateDicomStore`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.DeleteDicomStore`  
`google.cloud.healthcare.v1beta1.dicom.DicomService.UpdateDicomStore`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyAdminConsents` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyConsents` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.CreateFhirStore`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.DeleteFhirStore`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.UpdateFhirStore`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateHl7V2Store`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteHl7V2Store`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateHl7V2Store`  
`google.iam.v1.IAMPolicy.SetIamPolicy`  
`DATA_READ` | `google.cloud.healthcare.v1.consent.ConsentService.CheckDataAccess`  
`google.cloud.healthcare.v1.consent.ConsentService.EvaluateUserConsents`  
`google.cloud.healthcare.v1.consent.ConsentService.GetAttributeDefinition`  
`google.cloud.healthcare.v1.consent.ConsentService.GetConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.GetConsentArtifact`  
`google.cloud.healthcare.v1.consent.ConsentService.GetUserDataMapping`  
`google.cloud.healthcare.v1.consent.ConsentService.ListAttributeDefinitions`  
`google.cloud.healthcare.v1.consent.ConsentService.ListConsentArtifacts`  
`google.cloud.healthcare.v1.consent.ConsentService.ListConsentRevisions`  
`google.cloud.healthcare.v1.consent.ConsentService.ListConsents`  
`google.cloud.healthcare.v1.consent.ConsentService.ListUserDataMappings`  
`google.cloud.healthcare.v1.consent.ConsentService.QueryAccessibleData` (LRO)  
`google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData` (LRO)  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.GetSeriesMetrics`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.GetStudyMetrics`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveFrames`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstance`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstanceMetadata`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedFrames`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedInstance`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeries`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeriesMetadata`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudy`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudyMetadata`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForInstances`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForSeries`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForStudies`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources` (LRO)  
`google.cloud.healthcare.v1.fhir.rest.FhirService.CheckConsentEnforcementStatus`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalDeleteResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalPatchResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalUpdateResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResourceVersion`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetPatientEverything`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.GetResourceVersion`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ListResourceVersions`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.SearchResources`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ValidateResource`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages` (LRO)  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetMessage`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListMessages`  
`google.cloud.healthcare.v1.nlp.NlpService.AnalyzeEntities`  
`google.cloud.healthcare.v1.storageinfo.StorageInfoService.GetStorageInfo`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CheckDataAccess`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.EvaluateUserConsents`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.GetAttributeDefinition`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentArtifact`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.GetUserDataMapping`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListAttributeDefinitions`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentArtifacts`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentRevisions`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsents`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ListUserDataMappings`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.QueryAccessibleData` (LRO)  
`google.cloud.healthcare.v1beta1.dicom.DicomService.ExportDicomData` (LRO)  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetSeriesMetrics`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetStudyMetrics`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveBulkdata`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveFrames`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstance`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstanceMetadata`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedFrames`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedInstance`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeries`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeriesMetadata`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudy`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudyMetadata`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForInstances`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForSeries`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForStudies`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResources` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResourcesHistory` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckConsentEnforcementStatus`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapSearchTranslate`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapTranslate`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalDeleteResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalPatchResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalUpdateResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResourceVersion`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetEncounterEverything`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetLastNObservations`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetPatientEverything`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResourceVersion`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListIncomingReferences`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListResourceVersions`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.SearchResources`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ValidateResource`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.BatchGetMessages`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ExportMessages` (LRO)  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetMessage`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListMessages`  
`google.cloud.healthcare.v1beta1.nlp.NlpService.AnalyzeEntities`  
`google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.GetStorageInfo`  
`DATA_WRITE` | `google.cloud.healthcare.v1.consent.ConsentService.ActivateConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.ArchiveUserDataMapping`  
`google.cloud.healthcare.v1.consent.ConsentService.CreateAttributeDefinition`  
`google.cloud.healthcare.v1.consent.ConsentService.CreateConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.CreateConsentArtifact`  
`google.cloud.healthcare.v1.consent.ConsentService.CreateUserDataMapping`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteAttributeDefinition`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentArtifact`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentRevision`  
`google.cloud.healthcare.v1.consent.ConsentService.DeleteUserDataMapping`  
`google.cloud.healthcare.v1.consent.ConsentService.RejectConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.RevokeConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.UpdateAttributeDefinition`  
`google.cloud.healthcare.v1.consent.ConsentService.UpdateConsent`  
`google.cloud.healthcare.v1.consent.ConsentService.UpdateUserDataMapping`  
`google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset` (LRO)  
`google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore` (LRO)  
`google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore` (LRO)  
`google.cloud.healthcare.v1.dicom.DicomService.ImportDicomData` (LRO)  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteInstance`  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteSeries` (LRO)  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteStudy` (LRO)  
`google.cloud.healthcare.v1.dicomweb.DicomWebService.StoreInstances`  
`google.cloud.healthcare.v1.fhir.FhirStoreService.ImportResources` (LRO)  
`google.cloud.healthcare.v1.fhir.FhirStoreService.RollbackFhirResources` (LRO)  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalDeleteResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalPatchResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalUpdateResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.CreateBinaryResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.CreateResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResourceVersions`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.ExecuteBundle`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.PatchResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateBinaryResource`  
`google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateResource`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateMessage`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteMessage`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ImportMessages` (LRO)  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.IngestMessage`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.RollbackHl7V2Messages`  
`google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateMessage`  
`google.cloud.healthcare.v1.storageinfo.StorageInfoService.SetBlobStorageSettings` (LRO)  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ActivateConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.ArchiveUserDataMapping`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CreateAttributeDefinition`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentArtifact`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.CreateUserDataMapping`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteAttributeDefinition`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentArtifact`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentRevision`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteUserDataMapping`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.RejectConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.RevokeConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateAttributeDefinition`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsent`  
`google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateUserDataMapping`  
`google.cloud.healthcare.v1beta1.dataset.DatasetService.DeidentifyDataset` (LRO)  
`google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyDicomStore` (LRO)  
`google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyFhirStore` (LRO)  
`google.cloud.healthcare.v1beta1.dicom.DicomService.ImportDicomData` (LRO)  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteInstance`  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteSeries` (LRO)  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteStudy` (LRO)  
`google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.StoreInstances`  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResources` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResourcesHistory` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.FhirStoreService.RollbackFhirResources` (LRO)  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalDeleteResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalPatchResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalUpdateResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateBinaryResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResourceVersions`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ExecuteBundle`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.PatchResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateBinaryResource`  
`google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateResource`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateMessage`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteMessage`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ImportMessages` (LRO)  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.IngestMessage`  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.RollbackHl7V2Messages` (LRO)  
`google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateMessage`  
`google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.SetBlobStorageSettings` (LRO)  
`google.longrunning.Operations.CancelOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Healthcare API.

### `google.cloud.healthcare.v1.consent.ConsentService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.consent.ConsentService`.

#### `ActivateConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ActivateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.activate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ActivateConsent" `  




#### `ArchiveUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ArchiveUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.archive - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ArchiveUserDataMapping" `  




#### `CheckDataAccess`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CheckDataAccess`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.checkDataAccess - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CheckDataAccess" `  




#### `CreateAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CreateAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CreateAttributeDefinition" `  




#### `CreateConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CreateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CreateConsent" `  




#### `CreateConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CreateConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CreateConsentArtifact" `  




#### `CreateConsentStore`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CreateConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CreateConsentStore" `  




#### `CreateUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.CreateUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.CreateUserDataMapping" `  




#### `DeleteAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteAttributeDefinition" `  




#### `DeleteConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteConsent" `  




#### `DeleteConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentArtifact" `  




#### `DeleteConsentRevision`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentRevision" `  




#### `DeleteConsentStore`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteConsentStore" `  




#### `DeleteUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.DeleteUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.DeleteUserDataMapping" `  




#### `EvaluateUserConsents`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.EvaluateUserConsents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.evaluateUserConsents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.EvaluateUserConsents" `  




#### `GetAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.GetAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.GetAttributeDefinition" `  




#### `GetConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.GetConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.GetConsent" `  




#### `GetConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.GetConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.GetConsentArtifact" `  




#### `GetConsentStore`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.GetConsentStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.GetConsentStore" `  




#### `GetUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.GetUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.GetUserDataMapping" `  




#### `ListAttributeDefinitions`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListAttributeDefinitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListAttributeDefinitions" `  




#### `ListConsentArtifacts`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListConsentArtifacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListConsentArtifacts" `  




#### `ListConsentRevisions`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListConsentRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListConsentRevisions" `  




#### `ListConsentStores`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListConsentStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListConsentStores" `  




#### `ListConsents`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListConsents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListConsents" `  




#### `ListUserDataMappings`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.ListUserDataMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.ListUserDataMappings" `  




#### `QueryAccessibleData`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.QueryAccessibleData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.queryAccessibleData - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.QueryAccessibleData" `  




#### `RejectConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.RejectConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.reject - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.RejectConsent" `  




#### `RevokeConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.RevokeConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.revoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.RevokeConsent" `  




#### `UpdateAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.UpdateAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.UpdateAttributeDefinition" `  




#### `UpdateConsent`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.UpdateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.UpdateConsent" `  




#### `UpdateConsentStore`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.UpdateConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.UpdateConsentStore" `  




#### `UpdateUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1.consent.ConsentService.UpdateUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.consent.ConsentService.UpdateUserDataMapping" `  




### `google.cloud.healthcare.v1.dataset.DatasetService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.dataset.DatasetService`.

#### `CreateDataset`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.CreateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.CreateDataset" `  




#### `DeidentifyDataset`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.create - ADMIN_WRITE`
    * `healthcare.datasets.deidentify - DATA_WRITE`
    * `healthcare.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset" `  




#### `DeleteDataset`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.DeleteDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.DeleteDataset" `  




#### `GetDataset`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.GetDataset" `  




#### `ListDatasets`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.ListDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.datasets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.ListDatasets" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.healthcare.v1.dataset.DatasetService.UpdateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dataset.DatasetService.UpdateDataset" `  




### `google.cloud.healthcare.v1.deidentify.DeidentifyService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.deidentify.DeidentifyService`.

#### `DeidentifyDicomStore`

  * **Method** : `google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.deidentify - DATA_WRITE`
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyDicomStore" `  




#### `DeidentifyFhirStore`

  * **Method** : `google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.deidentify - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore" `  




### `google.cloud.healthcare.v1.dicom.DicomService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.dicom.DicomService`.

#### `CreateDicomStore`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.CreateDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.CreateDicomStore" `  




#### `DeleteDicomStore`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.DeleteDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.DeleteDicomStore" `  




#### `ExportDicomData`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData" `  




#### `GetDicomStore`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.GetDicomStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.GetDicomStore" `  




#### `GetDicomStoreMetrics`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.GetDicomStoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.GetDicomStoreMetrics" `  




#### `ImportDicomData`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.ImportDicomData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.ImportDicomData" `  




#### `ListDicomStores`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.ListDicomStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.ListDicomStores" `  




#### `UpdateDicomStore`

  * **Method** : `google.cloud.healthcare.v1.dicom.DicomService.UpdateDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicom.DicomService.UpdateDicomStore" `  




### `google.cloud.healthcare.v1.dicomweb.DicomWebService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.dicomweb.DicomWebService`.

#### `DeleteInstance`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteInstance" `  




#### `DeleteSeries`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteSeries" `  




#### `DeleteStudy`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteStudy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteStudy" `  




#### `GetSeriesMetrics`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.GetSeriesMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.GetSeriesMetrics" `  




#### `GetStudyMetrics`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.GetStudyMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.GetStudyMetrics" `  




#### `RetrieveFrames`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveFrames" `  




#### `RetrieveInstance`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstance" `  




#### `RetrieveInstanceMetadata`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstanceMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveInstanceMetadata" `  




#### `RetrieveRenderedFrames`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedFrames" `  




#### `RetrieveRenderedInstance`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveRenderedInstance" `  




#### `RetrieveSeries`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeries" `  




#### `RetrieveSeriesMetadata`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeriesMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveSeriesMetadata" `  




#### `RetrieveStudy`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudy" `  




#### `RetrieveStudyMetadata`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudyMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.RetrieveStudyMetadata" `  




#### `SearchForInstances`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForInstances" `  




#### `SearchForSeries`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForSeries" `  




#### `SearchForStudies`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForStudies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.SearchForStudies" `  




#### `StoreInstances`

  * **Method** : `google.cloud.healthcare.v1.dicomweb.DicomWebService.StoreInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.dicomweb.DicomWebService.StoreInstances" `  




### `google.cloud.healthcare.v1.fhir.FhirStoreService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.fhir.FhirStoreService`.

#### `ApplyAdminConsents`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyAdminConsents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.applyConsents - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyAdminConsents" `  




#### `ApplyConsents`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyConsents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.applyConsents - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ApplyConsents" `  




#### `CreateFhirStore`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.CreateFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.CreateFhirStore" `  




#### `DeleteFhirStore`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.DeleteFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.DeleteFhirStore" `  




#### `ExplainDataAccess`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ExplainDataAccess`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.explainDataAccess - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ExplainDataAccess" `  




#### `ExportResources`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ExportResources" `  




#### `GetFhirStore`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStore" `  




#### `GetFhirStoreMetrics`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.GetFhirStoreMetrics" `  




#### `ImportResources`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ImportResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ImportResources" `  




#### `ListFhirStores`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.ListFhirStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.ListFhirStores" `  




#### `RollbackFhirResources`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.RollbackFhirResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.rollback - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.RollbackFhirResources" `  




#### `UpdateFhirStore`

  * **Method** : `google.cloud.healthcare.v1.fhir.FhirStoreService.UpdateFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.FhirStoreService.UpdateFhirStore" `  




### `google.cloud.healthcare.v1.fhir.rest.FhirService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.fhir.rest.FhirService`.

#### `CheckConsentEnforcementStatus`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.CheckConsentEnforcementStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.CheckConsentEnforcementStatus" `  




#### `CheckPatientConsentEnforcementStatus`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus" `  




#### `ConditionalDeleteResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalDeleteResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.delete - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalDeleteResource" `  




#### `ConditionalPatchResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalPatchResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.patch - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalPatchResource" `  




#### `ConditionalUpdateResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalUpdateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ConditionalUpdateResource" `  




#### `CreateBinaryResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.CreateBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.CreateBinaryResource" `  




#### `CreateResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.CreateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.CreateResource" `  




#### `DeleteResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResource" `  




#### `DeleteResourceVersions`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResourceVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.DeleteResourceVersions" `  




#### `ExecuteBundle`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ExecuteBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.executeBundle - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ExecuteBundle" `  




#### `GetBinaryResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResource" `  




#### `GetBinaryResourceVersion`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResourceVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetBinaryResourceVersion" `  




#### `GetCapabilityStatement`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetCapabilityStatement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetCapabilityStatement" `  




#### `GetPatientEverything`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetPatientEverything`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetPatientEverything" `  




#### `GetResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetResource" `  




#### `GetResourceVersion`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.GetResourceVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.GetResourceVersion" `  




#### `ListResourceVersions`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ListResourceVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ListResourceVersions" `  




#### `PatchResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.PatchResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.patch - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.PatchResource" `  




#### `SearchResources`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.SearchResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.SearchResources" `  




#### `UpdateBinaryResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateBinaryResource" `  




#### `UpdateResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.UpdateResource" `  




#### `ValidateResource`

  * **Method** : `google.cloud.healthcare.v1.fhir.rest.FhirService.ValidateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.fhir.rest.FhirService.ValidateResource" `  




### `google.cloud.healthcare.v1.hl7v2.Hl7V2Service`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.hl7v2.Hl7V2Service`.

#### `CreateHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateHl7V2Store" `  




#### `CreateMessage`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.CreateMessage" `  




#### `DeleteHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteHl7V2Store" `  




#### `DeleteMessage`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.DeleteMessage" `  




#### `ExportMessages`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ExportMessages" `  




#### `GetHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2Store`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2Store" `  




#### `GetHl7V2StoreMetrics`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics" `  




#### `GetMessage`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.GetMessage" `  




#### `ImportMessages`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ImportMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ImportMessages" `  




#### `IngestMessage`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.IngestMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.ingest - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.IngestMessage" `  




#### `ListHl7V2Stores`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListHl7V2Stores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListHl7V2Stores" `  




#### `ListMessages`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.ListMessages" `  




#### `RollbackHl7V2Messages`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.RollbackHl7V2Messages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.rollback - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.RollbackHl7V2Messages" `  




#### `UpdateHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateHl7V2Store" `  




#### `UpdateMessage`

  * **Method** : `google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.hl7v2.Hl7V2Service.UpdateMessage" `  




### `google.cloud.healthcare.v1.nlp.NlpService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.nlp.NlpService`.

#### `AnalyzeEntities`

  * **Method** : `google.cloud.healthcare.v1.nlp.NlpService.AnalyzeEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.nlpservice.analyzeEntities - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.nlp.NlpService.AnalyzeEntities" `  




### `google.cloud.healthcare.v1.storageinfo.StorageInfoService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1.storageinfo.StorageInfoService`.

#### `GetStorageInfo`

  * **Method** : `google.cloud.healthcare.v1.storageinfo.StorageInfoService.GetStorageInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.storageinfo.StorageInfoService.GetStorageInfo" `  




#### `SetBlobStorageSettings`

  * **Method** : `google.cloud.healthcare.v1.storageinfo.StorageInfoService.SetBlobStorageSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1.storageinfo.StorageInfoService.SetBlobStorageSettings" `  




### `google.cloud.healthcare.v1beta1.consent.ConsentService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.consent.ConsentService`.

#### `ActivateConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ActivateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.activate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ActivateConsent" `  




#### `ArchiveUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ArchiveUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.archive - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ArchiveUserDataMapping" `  




#### `CheckDataAccess`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CheckDataAccess`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.checkDataAccess - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CheckDataAccess" `  




#### `CreateAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CreateAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CreateAttributeDefinition" `  




#### `CreateConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsent" `  




#### `CreateConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentArtifact" `  




#### `CreateConsentStore`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CreateConsentStore" `  




#### `CreateUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.CreateUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.CreateUserDataMapping" `  




#### `DeleteAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteAttributeDefinition" `  




#### `DeleteConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsent" `  




#### `DeleteConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentArtifact" `  




#### `DeleteConsentRevision`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentRevision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentRevision" `  




#### `DeleteConsentStore`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteConsentStore" `  




#### `DeleteUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.DeleteUserDataMapping" `  




#### `EvaluateUserConsents`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.EvaluateUserConsents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.evaluateUserConsents - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.EvaluateUserConsents" `  




#### `GetAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.GetAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.GetAttributeDefinition" `  




#### `GetConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsent" `  




#### `GetConsentArtifact`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentArtifact`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentArtifact" `  




#### `GetConsentStore`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.GetConsentStore" `  




#### `GetUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.GetUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.GetUserDataMapping" `  




#### `ListAttributeDefinitions`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListAttributeDefinitions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListAttributeDefinitions" `  




#### `ListConsentArtifacts`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentArtifacts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentArtifacts.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentArtifacts" `  




#### `ListConsentRevisions`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentRevisions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentRevisions" `  




#### `ListConsentStores`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsentStores" `  




#### `ListConsents`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsents`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListConsents" `  




#### `ListUserDataMappings`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.ListUserDataMappings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.ListUserDataMappings" `  




#### `QueryAccessibleData`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.QueryAccessibleData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.queryAccessibleData - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.QueryAccessibleData" `  




#### `RejectConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.RejectConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.reject - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.RejectConsent" `  




#### `RevokeConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.RevokeConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.revoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.RevokeConsent" `  




#### `UpdateAttributeDefinition`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateAttributeDefinition`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.attributeDefinitions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateAttributeDefinition" `  




#### `UpdateConsent`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsent`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consents.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsent" `  




#### `UpdateConsentStore`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsentStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateConsentStore" `  




#### `UpdateUserDataMapping`

  * **Method** : `google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateUserDataMapping`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.userDataMappings.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.consent.ConsentService.UpdateUserDataMapping" `  




### `google.cloud.healthcare.v1beta1.dataset.DatasetService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.dataset.DatasetService`.

#### `CreateDataset`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.CreateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.CreateDataset" `  




#### `DeidentifyDataset`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.DeidentifyDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.create - ADMIN_WRITE`
    * `healthcare.datasets.deidentify - DATA_WRITE`
    * `healthcare.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.DeidentifyDataset" `  




#### `DeleteDataset`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.DeleteDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.DeleteDataset" `  




#### `GetDataset`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.GetDataset`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.datasets.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.GetDataset" `  




#### `ListDatasets`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.ListDatasets`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.datasets.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.ListDatasets" `  




#### `UpdateDataset`

  * **Method** : `google.cloud.healthcare.v1beta1.dataset.DatasetService.UpdateDataset`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.datasets.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dataset.DatasetService.UpdateDataset" `  




### `google.cloud.healthcare.v1beta1.deidentify.DeidentifyService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.deidentify.DeidentifyService`.

#### `DeidentifyDicomStore`

  * **Method** : `google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyDicomStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.deidentify - DATA_WRITE`
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyDicomStore" `  




#### `DeidentifyFhirStore`

  * **Method** : `google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyFhirStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.deidentify - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.deidentify.DeidentifyService.DeidentifyFhirStore" `  




### `google.cloud.healthcare.v1beta1.dicom.DicomService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.dicom.DicomService`.

#### `CreateDicomStore`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.CreateDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.CreateDicomStore" `  




#### `DeleteDicomStore`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.DeleteDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.DeleteDicomStore" `  




#### `ExportDicomData`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.ExportDicomData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.ExportDicomData" `  




#### `GetDicomStore`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStore" `  




#### `GetDicomStoreMetrics`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.GetDicomStoreMetrics" `  




#### `ImportDicomData`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.ImportDicomData`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.ImportDicomData" `  




#### `ListDicomStores`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.ListDicomStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.ListDicomStores" `  




#### `UpdateDicomStore`

  * **Method** : `google.cloud.healthcare.v1beta1.dicom.DicomService.UpdateDicomStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.dicomStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicom.DicomService.UpdateDicomStore" `  




### `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService`.

#### `DeleteInstance`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteInstance" `  




#### `DeleteSeries`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteSeries" `  




#### `DeleteStudy`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteStudy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebDelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.DeleteStudy" `  




#### `GetSeriesMetrics`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetSeriesMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetSeriesMetrics" `  




#### `GetStudyMetrics`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetStudyMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.GetStudyMetrics" `  




#### `RetrieveBulkdata`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveBulkdata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveBulkdata" `  




#### `RetrieveFrames`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveFrames" `  




#### `RetrieveInstance`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstance" `  




#### `RetrieveInstanceMetadata`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstanceMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveInstanceMetadata" `  




#### `RetrieveRenderedFrames`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedFrames`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedFrames" `  




#### `RetrieveRenderedInstance`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedInstance`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveRenderedInstance" `  




#### `RetrieveSeries`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeries" `  




#### `RetrieveSeriesMetadata`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeriesMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveSeriesMetadata" `  




#### `RetrieveStudy`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudy" `  




#### `RetrieveStudyMetadata`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudyMetadata`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.RetrieveStudyMetadata" `  




#### `SearchForInstances`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForInstances" `  




#### `SearchForSeries`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForSeries`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForSeries" `  




#### `SearchForStudies`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForStudies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.SearchForStudies" `  




#### `StoreInstances`

  * **Method** : `google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.StoreInstances`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.dicomweb.DicomWebService.StoreInstances" `  




### `google.cloud.healthcare.v1beta1.fhir.FhirStoreService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.fhir.FhirStoreService`.

#### `ApplyAdminConsents`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyAdminConsents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.applyConsents - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyAdminConsents" `  




#### `ApplyConsents`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyConsents`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.applyConsents - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ApplyConsents" `  




#### `ConfigureSearch`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.configureSearch - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ConfigureSearch" `  




#### `CreateFhirStore`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.CreateFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.CreateFhirStore" `  




#### `DeleteFhirStore`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.DeleteFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.DeleteFhirStore" `  




#### `ExplainDataAccess`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExplainDataAccess`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.explainDataAccess - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExplainDataAccess" `  




#### `ExportResources`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResources" `  




#### `ExportResourcesHistory`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResourcesHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ExportResourcesHistory" `  




#### `GetFhirStore`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStore`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStore" `  




#### `GetFhirStoreMetrics`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.GetFhirStoreMetrics" `  




#### `ImportResources`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResources" `  




#### `ImportResourcesHistory`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResourcesHistory`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ImportResourcesHistory" `  




#### `ListFhirStores`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ListFhirStores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.ListFhirStores" `  




#### `RollbackFhirResources`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.RollbackFhirResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.rollback - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.RollbackFhirResources" `  




#### `UpdateFhirStore`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.FhirStoreService.UpdateFhirStore`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.fhirStores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.FhirStoreService.UpdateFhirStore" `  




### `google.cloud.healthcare.v1beta1.fhir.rest.FhirService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.fhir.rest.FhirService`.

#### `CheckConsentEnforcementStatus`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckConsentEnforcementStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckConsentEnforcementStatus" `  




#### `CheckPatientConsentEnforcementStatus`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CheckPatientConsentEnforcementStatus" `  




#### `ConceptMapSearchTranslate`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapSearchTranslate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.translateConceptMap - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapSearchTranslate" `  




#### `ConceptMapTranslate`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapTranslate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.translateConceptMap - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConceptMapTranslate" `  




#### `ConditionalDeleteResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalDeleteResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.delete - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalDeleteResource" `  




#### `ConditionalPatchResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalPatchResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.patch - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalPatchResource" `  




#### `ConditionalUpdateResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalUpdateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ConditionalUpdateResource" `  




#### `CreateBinaryResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateBinaryResource" `  




#### `CreateResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.CreateResource" `  




#### `DeleteResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResource" `  




#### `DeleteResourceVersions`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResourceVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.purge - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.DeleteResourceVersions" `  




#### `ExecuteBundle`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ExecuteBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.create - DATA_WRITE`
    * `healthcare.fhirResources.update - DATA_WRITE`
    * `healthcare.fhirStores.executeBundle - ADMIN_READ`
    * `healthcare.fhirStores.import - DATA_WRITE`
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ExecuteBundle" `  




#### `GetBinaryResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResource" `  




#### `GetBinaryResourceVersion`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResourceVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetBinaryResourceVersion" `  




#### `GetCapabilityStatement`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetCapabilityStatement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetCapabilityStatement" `  




#### `GetEncounterEverything`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetEncounterEverything`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetEncounterEverything" `  




#### `GetLastNObservations`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetLastNObservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetLastNObservations" `  




#### `GetPatientEverything`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetPatientEverything`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetPatientEverything" `  




#### `GetResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResource" `  




#### `GetResourceVersion`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResourceVersion`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.GetResourceVersion" `  




#### `ListIncomingReferences`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListIncomingReferences`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListIncomingReferences" `  




#### `ListResourceVersions`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListResourceVersions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ListResourceVersions" `  




#### `PatchResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.PatchResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.patch - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.PatchResource" `  




#### `SearchResources`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.SearchResources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirStores.searchResources - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.SearchResources" `  




#### `UpdateBinaryResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateBinaryResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateBinaryResource" `  




#### `UpdateResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.UpdateResource" `  




#### `ValidateResource`

  * **Method** : `google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ValidateResource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.fhirResources.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.fhir.rest.FhirService.ValidateResource" `  




### `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service`.

#### `BatchGetMessages`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.BatchGetMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.BatchGetMessages" `  




#### `CreateHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateHl7V2Store" `  




#### `CreateMessage`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.CreateMessage" `  




#### `DeleteHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteHl7V2Store" `  




#### `DeleteMessage`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.DeleteMessage" `  




#### `ExportMessages`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ExportMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.export - DATA_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ExportMessages" `  




#### `GetHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2Store`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2Store" `  




#### `GetHl7V2StoreMetrics`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetHl7V2StoreMetrics" `  




#### `GetMessage`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.GetMessage" `  




#### `ImportMessages`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ImportMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.import - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ImportMessages" `  




#### `IngestMessage`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.IngestMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.ingest - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.IngestMessage" `  




#### `ListHl7V2Stores`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListHl7V2Stores`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListHl7V2Stores" `  




#### `ListMessages`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListMessages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.ListMessages" `  




#### `RollbackHl7V2Messages`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.RollbackHl7V2Messages`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.rollback - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.RollbackHl7V2Messages" `  




#### `UpdateHl7V2Store`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateHl7V2Store`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.hl7V2Stores.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateHl7V2Store" `  




#### `UpdateMessage`

  * **Method** : `google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateMessage`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.hl7V2Messages.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.hl7v2.Hl7V2Service.UpdateMessage" `  




### `google.cloud.healthcare.v1beta1.nlp.NlpService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.nlp.NlpService`.

#### `AnalyzeEntities`

  * **Method** : `google.cloud.healthcare.v1beta1.nlp.NlpService.AnalyzeEntities`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.nlpservice.analyzeEntities - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.nlp.NlpService.AnalyzeEntities" `  




### `google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService`

The following audit logs are associated with methods belonging to `google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService`.

#### `GetStorageInfo`

  * **Method** : `google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.GetStorageInfo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebRead - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.GetStorageInfo" `  




#### `SetBlobStorageSettings`

  * **Method** : `google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.SetBlobStorageSettings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.dicomStores.dicomWebWrite - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.healthcare.v1beta1.storageinfo.StorageInfoService.SetBlobStorageSettings" `  




### `google.cloud.location.Locations`

The following audit logs are associated with methods belonging to `google.cloud.location.Locations`.

#### `GetLocation`

  * **Method** : `google.cloud.location.Locations.GetLocation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.locations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.GetLocation" `  




#### `ListLocations`

  * **Method** : `google.cloud.location.Locations.ListLocations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.locations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.location.Locations.ListLocations" `  




### `google.iam.v1.IAMPolicy`

The following audit logs are associated with methods belonging to `google.iam.v1.IAMPolicy`.

#### `GetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.GetIamPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.consentStores.getIamPolicy - ADMIN_READ`
    * `healthcare.datasets.getIamPolicy - ADMIN_READ`
    * `healthcare.dicomStores.getIamPolicy - ADMIN_READ`
    * `healthcare.fhirStores.getIamPolicy - ADMIN_READ`
    * `healthcare.hl7V2Stores.getIamPolicy - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.GetIamPolicy" `  




#### `SetIamPolicy`

  * **Method** : `google.iam.v1.IAMPolicy.SetIamPolicy`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `healthcare.consentStores.setIamPolicy - ADMIN_WRITE`
    * `healthcare.datasets.setIamPolicy - ADMIN_WRITE`
    * `healthcare.dicomStores.setIamPolicy - ADMIN_WRITE`
    * `healthcare.fhirStores.setIamPolicy - ADMIN_WRITE`
    * `healthcare.hl7V2Stores.setIamPolicy - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.iam.v1.IAMPolicy.SetIamPolicy" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.operations.cancel - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `healthcare.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
