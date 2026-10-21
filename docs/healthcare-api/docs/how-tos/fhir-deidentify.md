---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify/
title: De-identifying FHIR data \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:46.933702+00:00
---

# De-identifying FHIR data  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  De-identifying FHIR data Stay organized with collections  Save and categorize content based on your preferences. 

**Disclaimer** : This operation processes data using a mixture of rules-based and heuristic methods. Results may differ between resources and datasets due to factors like input data quality/consistency, heuristic-based algorithms, and others. This feature isn't guaranteed to satisfy any specific legal, regulatory, or compliance requirements, including requirements for the de-identification of data. It is the user's responsibility to ensure that they set the appropriate configuration parameters for the operation and evaluate the end result to determine whether it is acceptable for their use cases and any legal, regulatory, or compliance requirements they may have.

This page explains how to de-identify sensitive data in FHIR resources using the Cloud Healthcare API at the following levels:

  * At the dataset level using [`datasets.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/deidentify)
  * At the FHIR store level using [`fhirStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify)



This page also explains how to apply filters when de-identifying data at the FHIR store level.

**Note:** If [`configureSearch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores/configureSearch) is called on the destination FHIR store during an ongoing de-identification operation, the de-identified resources might be unsearchable using the newly configured custom search parameters.

## De-identification overview

### Dataset level de-identification

To de-identify FHIR data at the dataset level, call the [`datasets.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/deidentify) operation. The de-identification API call has the following components:

  * _The source dataset_ : A dataset containing FHIR stores with one or more resources that have sensitive data.
  * _The destination dataset_ : De-identification does not impact the original dataset or its data. Instead, de-identified copies of the original data are written to a new dataset, called the _destination dataset_.
  * _What to de-identify_ : Configuration parameters that specify how to process the dataset. You can configure these parameters by specifying them in a [`FhirConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirConfig) and/or [`TextConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#TextConfig) inside the [`DeidentifyConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#deidentifyconfig) object and passing it by either: 
    * Setting the `config` field of the request body
    * Storing it in Cloud Storage in a JSON format and specifying the location of the file in the bucket by using the `gcsConfigUri` field of the request body

**Note:** Using `gcsConfigUri` is only available in v1beta1 of the Cloud Healthcare API.

The majority of samples in this guide show how to de-identify FHIR data at the dataset level.

### FHIR store level de-identification

De-identifying FHIR data at the FHIR store level lets you have more control over which FHIR data is de-identified.

To de-identify FHIR data in a FHIR store, call the [`fhirStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify) method. The de-identification API call has the following components:

  * _The source FHIR store_ : A FHIR store containing one or more resources that have sensitive data.
  * _The destination FHIR store_ : De-identification does not impact the original FHIR store or its data. Instead, de-identified copies of the original data are written to the destination FHIR store. The destination FHIR store must already exist.
  * _What to de-identify_ : Configuration parameters that specify how to process the FHIR store. You can configure these parameters by specifying them in a [`FhirConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirConfig) and/or [`TextConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#TextConfig) inside the [`DeidentifyConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#deidentifyconfig) object and passing it by either: 
    * Setting the `config` field of the request body
    * Storing it in Cloud Storage in a JSON format and specifying the location of the file in the bucket by using the `gcsConfigUri` field of the request body

**Note:** Using `gcsConfigUri` is only available in v1beta1 of the Cloud Healthcare API.

For an example of how to de-identify FHIR data at the FHIR store level, see De-identifying data at the FHIR store level.

### Filters

You can de-identify a subset of data in a FHIR store by specifying a list of FHIR resource IDs in the `fhirStores.deidentify` request. For an example, see De-identifying a subset of a FHIR store.

## Sample FHIR resource used in this guide

The samples in this guide use a Patient ([DSTU2](https://www.hl7.org/fhir/dstu2/patient.html), [STU3](https://www.hl7.org/fhir/stu3/patient.html), and [R4](https://www.hl7.org/fhir/r4/patient.html)) resource in a FHIR store. The Patient has the properties shown in the following sample. The `id` value is generated by the server. If you create the Patient resource in your own FHIR store, the `id` value returned is different than the value shown in the sample Patient.
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "status": "generated",
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>"
      }
    }
    

## Default FHIR data de-identification

You can de-identify FHIR data using a "default" method that redacts common protected health information (PHI) in the resources in a FHIR store. The default method redacts the following information:

  * infoTypes specified in the default FHIR infoTypes
  * Paths specified in the default FHIR de-identification profile



The following samples show how to de-identify the Patient resource using the FHIR default method. When using the default method, use an empty `FhirConfig` inside the `DeidentifyConfig` object.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {}
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "",
          "district": "",
          "line": [
            ""
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "",
          "state": "CA",
          "text": "",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1981-02-24",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMA"
      },
      "name": [
        {
          "family": "",
          "given": [
            ""
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: [PERSON_NAME][PERSON_NAME][PERSON_NAME]</p><p><b>DateOfBirth</b>: 1981-02-24</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {}
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "",
          "district": "",
          "line": [
            ""
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "",
          "state": "CA",
          "text": "",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1981-02-24",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMA"
      },
      "name": [
        {
          "family": "",
          "given": [
            ""
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: [PERSON_NAME][PERSON_NAME][PERSON_NAME]</p><p><b>DateOfBirth</b>: 1981-02-24</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

You can see that the following values were transformed to de-identify the resource:

  * A new value was provided in the `birthDate` field using a [date shifting](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting) technique with a 100-day differential.
  * The value in `address.city` was redacted.
  * The value in `address.district` was redacted.
  * The value in `address.line` was redacted.
  * The value in `address.postalCode` was redacted.
  * The value in `address.text` was redacted.
  * The value in `name.family` was redacted.
  * The value in `name.given` was redacted.
  * The free text in the `text.div` field was modified to replace the patient's name with its [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), `[PERSON_NAME]`. The patient's birthdate value was transformed in the same way as the value in the `birthDate` field was transformed.



## De-identifying specific FHIR paths

To specify which FHIR paths to de-identify and how to transform them, configure the [`fieldMetadataList`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirConfig.FIELDS.field_metadata_list) in the `FhirConfig` object.

Inside the `fieldMetadataList`, you specify a period-separated list of field names or FHIR resource type names in a `paths` list. Next, you specify an [`Action`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#Action) value to apply to everything listed in `paths`. See the `Action` documentation for the possible values.

For information on how to set the `paths` field in the Cloud Healthcare API, see [`paths`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FieldMetadata.FIELDS.paths). The formatting of the values in `paths` is based on [FHIRPath](http://hl7.org/fhirpath/).

### Default FHIR de-identification profile

By default, if you do not specify any FHIR paths in `fieldMetadataList`, the Cloud Healthcare API applies the following de-identification profiles to select and transform FHIR paths. The profile that is applied depends on the FHIR version you're using. You can expand the following sections to see the profiles for the version you're using. You can also download the profiles ([DSTU2](https://docs.cloud.google.com/static/healthcare-api/docs/resources/dstu2_default_fhir_deidentify_config.txt), [STU3](https://docs.cloud.google.com/static/healthcare-api/docs/resources/stu3_default_fhir_deidentify_config.txt), and [R4](https://docs.cloud.google.com/static/healthcare-api/docs/resources/r4_default_fhir_deidentify_config.txt)).

DSTU2
    
    
    fhir {
      field_metadata_list {
        paths: "AuditEvent.Event.outcomeDesc"
        paths: "AuditEvent.Participant.altId"
        paths: "AuditEvent.Participant.Network.address"
        paths: "AuditEvent.Source.site"
        paths: "CarePlan.Activity.Detail.Scheduled.string"
        paths: "Claim.school"
        paths: "Claim.Coverage.businessArrangement"
        paths: "ClaimResponse.Coverage.businessArrangement"
        paths: "Composition.title"
        paths: "Composition.Section.title"
        paths: "ConceptMap.publisher"
        paths: "ConceptMap.copyright"
        paths: "Condition.Onset.string"
        paths: "Condition.Abatement.string"
        paths: "Conformance.publisher"
        paths: "Conformance.copyright"
        paths: "Contract.Signer.signature"
        paths: "Coverage.group"
        paths: "Coverage.plan"
        paths: "Coverage.subPlan"
        paths: "DataElement.publisher"
        paths: "DataElement.copyright"
        paths: "Device.udi"
        paths: "FamilyMemberHistory.Born.string"
        paths: "FamilyMemberHistory.Deceased.string"
        paths: "FamilyMemberHistory.Condition.Onset.string"
        paths: "HealthcareService.serviceName"
        paths: "HealthcareService.publicKey"
        paths: "ImagingStudy.Series.Instance.title"
        paths: "ImplementationGuide.publisher"
        paths: "ImplementationGuide.copyright"
        paths: "List.title"
        paths: "NamingSystem.publisher"
        paths: "NamingSystem.responsible"
        paths: "OperationDefinition.publisher"
        paths: "Questionnaire.publisher"
        paths: "Questionnaire.Group.linkId"
        paths: "SearchParameter.publisher"
        paths: "StructureDefinition.publisher"
        paths: "StructureDefinition.copyright"
        paths: "ValueSet.publisher"
        paths: "ValueSet.copyright"
        paths: "Address.text"
        paths: "Address.line"
        paths: "Address.city"
        paths: "Address.district"
        paths: "Address.postalCode"
        paths: "Annotation.text"
        paths: "Annotation.Author.string"
        paths: "ContactPoint.value"
        paths: "HumanName"
        paths: "Identifier.value"
        action: TRANSFORM
      }
      field_metadata_list {
        paths: "Appointment.comment"
        paths: "AppointmentResponse.comment"
        paths: "Claim.Coverage.preAuthRef"
        paths: "ClaimResponse.Note.text"
        paths: "ClaimResponse.Coverage.preAuthRef"
        paths: "ClinicalImpression.summary"
        paths: "ClinicalImpression.prognosis"
        paths: "ClinicalImpression.Finding.cause"
        paths: "ClinicalImpression.RuledOut.reason"
        paths: "Communication.Payload.Content.string"
        paths: "CommunicationRequest.Payload.Content.string"
        paths: "Condition.notes"
        paths: "Conformance.Rest.documentation"
        paths: "Conformance.Rest.Resource.Interaction.documentation"
        paths: "Conformance.Rest.Resource.SearchParam.documentation"
        paths: "Conformance.Rest.Interaction.documentation"
        paths: "Conformance.Messaging.documentation"
        paths: "Conformance.Messaging.Event.documentation"
        paths: "Conformance.Document.documentation"
        paths: "Contract.Term.text"
        paths: "DetectedIssue.detail"
        paths: "DeviceComponent.ProductionSpecification.productionSpec"
        paths: "DeviceUseRequest.notes"
        paths: "DeviceUseStatement.notes"
        paths: "DiagnosticReport.conclusion"
        paths: "DiagnosticReport.Image.comment"
        paths: "HealthcareService.comment"
        paths: "HealthcareService.extraDetails"
        paths: "HealthcareService.eligibilityNote"
        paths: "HealthcareService.programName"
        paths: "HealthcareService.availabilityExceptions"
        paths: "List.note"
        paths: "MedicationAdministration.note"
        paths: "MedicationDispense.note"
        paths: "MedicationOrder.note"
        paths: "MedicationStatement.note"
        paths: "NutritionOrder.OralDiet.instruction"
        paths: "NutritionOrder.Supplement.instruction"
        paths: "Observation.comments"
        paths: "Observation.Value.string"
        paths: "OperationDefinition.notes"
        paths: "OperationOutcome.Issue.diagnostics"
        paths: "PaymentReconciliation.disposition"
        paths: "PaymentReconciliation.Note.text"
        paths: "ProcessResponse.Notes.text"
        paths: "Provenance.Entity.display"
        paths: "Questionnaire.Group.text"
        paths: "Questionnaire.Group.Question.text"
        paths: "QuestionnaireResponse.Group.text"
        paths: "QuestionnaireResponse.Group.Question.text"
        paths: "QuestionnaireResponse.Group.Question.Answer.Value.string"
        paths: "RiskAssessment.mitigation"
        paths: "RiskAssessment.Prediction.rationale"
        paths: "Schedule.comment"
        paths: "Slot.comment"
        paths: "Specimen.Collection.comment"
        paths: "StructureDefinition.requirements"
        paths: "StructureDefinition.Mapping.comments"
        paths: "Subscription.criteria"
        paths: "Subscription.reason"
        paths: "Subscription.error"
        paths: "Subscription.Channel.header"
        paths: "ValueSet.requirements"
        paths: "ValueSet.Expansion.Parameter.Value.string"
        paths: "VisionPrescription.Dispense.notes"
        paths: "Attachment.title"
        paths: "Reference.display"
        action: INSPECT_AND_TRANSFORM
      }
    }
    

STU3
    
    
    fhir {
      field_metadata_list {
        paths: "ActivityDefinition.publisher"
        paths: "AllergyIntolerance.Onset.string"
        paths: "Appointment.comment"
        paths: "AppointmentResponse.comment"
        paths: "AuditEvent.outcomeDesc"
        paths: "AuditEvent.Agent.altId"
        paths: "AuditEvent.Agent.Network.address"
        paths: "AuditEvent.Source.site"
        paths: "CapabilityStatement.title"
        paths: "CapabilityStatement.publisher"
        paths: "CarePlan.title"
        paths: "Claim.Insurance.businessArrangement"
        paths: "ClaimResponse.Insurance.businessArrangement"
        paths: "CodeSystem.title"
        paths: "CodeSystem.publisher"
        paths: "CompartmentDefinition.title"
        paths: "CompartmentDefinition.publisher"
        paths: "Composition.title"
        paths: "Composition.Section.title"
        paths: "ConceptMap.title"
        paths: "ConceptMap.publisher"
        paths: "Condition.Onset.string"
        paths: "Condition.Abatement.string"
        paths: "Coverage.subscriberId"
        paths: "Coverage.dependent"
        paths: "Coverage.Group.group"
        paths: "Coverage.Group.subGroup"
        paths: "Coverage.Group.plan"
        paths: "Coverage.Group.subPlan"
        paths: "Coverage.Group.class"
        paths: "Coverage.Group.subClass"
        paths: "DataElement.publisher"
        paths: "DataElement.title"
        paths: "Device.Udi.deviceIdentifier"
        paths: "Device.Udi.carrierHRF"
        paths: "EligibilityRequest.businessArrangement"
        paths: "ExpansionProfile.publisher"
        paths: "ExplanationOfBenefit.Insurance.preAuthRef"
        paths: "FamilyMemberHistory.bornDate"
        paths: "FamilyMemberHistory.Born.string"
        paths: "FamilyMemberHistory.AgeType.string"
        paths: "FamilyMemberHistory.deceasedDate"
        paths: "FamilyMemberHistory.Deceased.string"
        paths: "FamilyMemberHistory.Condition.Onset.string"
        paths: "GraphDefinition.publisher"
        paths: "ImagingStudy.Series.Instance.title"
        paths: "ImplementationGuide.publisher"
        paths: "Library.title"
        paths: "Library.publisher"
        paths: "List.title"
        paths: "Location.name"
        paths: "Location.alias"
        paths: "Measure.title"
        paths: "Measure.publisher"
        paths: "MessageDefinition.title"
        paths: "MessageDefinition.publisher"
        paths: "NamingSystem.publisher"
        paths: "NamingSystem.responsible"
        paths: "OperationDefinition.publisher"
        paths: "Organization.alias"
        paths: "Patient.birthDate"
        paths: "Patient.deceased.dateTime"
        paths: "Person.birthDate"
        paths: "PlanDefinition.title"
        paths: "PlanDefinition.publisher"
        paths: "PlanDefinition.Action.title"
        paths: "Practitioner.birthDate"
        paths: "Questionnaire.title"
        paths: "Questionnaire.publisher"
        paths: "ResearchStudy.title"
        paths: "SearchParameter.publisher"
        paths: "ServiceDefinition.title"
        paths: "ServiceDefinition.publisher"
        paths: "StructureDefinition.title"
        paths: "StructureDefinition.publisher"
        paths: "StructureMap.title"
        paths: "StructureMap.publisher"
        paths: "TestReport.tester"
        paths: "TestReport.Participant.display"
        paths: "TestReport.Setup.SetupAction.Assert.detail"
        paths: "ValueSet.title"
        paths: "ValueSet.publisher"
        paths: "Address.text"
        paths: "Address.line"
        paths: "Address.city"
        paths: "Address.district"
        paths: "Address.postalCode"
        paths: "Annotation.text"
        paths: "Annotation.Author.string"
        paths: "ContactPoint.value"
        paths: "HumanName"
        paths: "Identifier.value"
        paths: "RelatedPerson.birthDate"
        action: TRANSFORM
      }
      field_metadata_list {
        paths: "AdverseEvent.SuspectEntity.causalityProductRelatedness"
        paths: "CapabilityStatement.Rest.documentation"
        paths: "CapabilityStatement.Rest.Resource.ResourceInteraction.documentation"
        paths: "CapabilityStatement.Rest.Resource.SearchParam.documentation"
        paths: "CapabilityStatement.Rest.SystemInteraction.documentation"
        paths: "CapabilityStatement.Messaging.documentation"
        paths: "CapabilityStatement.Messaging.Event.documentation"
        paths: "CapabilityStatement.Document.documentation"
        paths: "CarePlan.Activity.Detail.statusReason"
        paths: "CarePlan.Activity.Detail.Scheduled.string"
        paths: "ChargeItem.overrideReason"
        paths: "Claim.SpecialCondition.Value.string"
        paths: "Claim.Insurance.preAuthRef"
        paths: "ClaimResponse.Note.text"
        paths: "ClaimResponse.Insurance.preAuthRef"
        paths: "ClinicalImpression.summary"
        paths: "ClinicalImpression.Finding.basis"
        paths: "Communication.Payload.Content.string"
        paths: "CommunicationRequest.Payload.Content.string"
        paths: "CompartmentDefinition.Resource.documentation"
        paths: "Contract.Term.text"
        paths: "Coverage.network"
        paths: "Coverage.Group.groupDisplay"
        paths: "Coverage.Group.subGroupDisplay"
        paths: "Coverage.Group.planDisplay"
        paths: "Coverage.Group.subPlanDisplay"
        paths: "Coverage.Group.classDisplay"
        paths: "Coverage.Group.subClassDisplay"
        paths: "DetectedIssue.detail"
        paths: "DeviceComponent.ProductionSpecification.productionSpec"
        paths: "DiagnosticReport.conclusion"
        paths: "DiagnosticReport.Image.comment"
        paths: "ExplanationOfBenefit.SupportingInformation.Value.string"
        paths: "ExplanationOfBenefit.Note.text"
        paths: "Goal.statusReason"
        paths: "HealthcareService.comment"
        paths: "HealthcareService.extraDetails"
        paths: "HealthcareService.eligibilityNote"
        paths: "HealthcareService.programName"
        paths: "HealthcareService.availabilityExceptions"
        paths: "ImplementationGuide.Page.title"
        paths: "Library.usage"
        paths: "MeasureReport.Group.Stratifier.StratifierGroup.value"
        paths: "NamingSystem.UniqueId.comment"
        paths: "NutritionOrder.OralDiet.instruction"
        paths: "NutritionOrder.Supplement.instruction"
        paths: "NutritionOrder.EnteralFormula.administrationInstruction"
        paths: "Observation.comment"
        paths: "Observation.Value.string"
        paths: "OperationDefinition.comment"
        paths: "OperationOutcome.Issue.diagnostics"
        paths: "Parameters.Parameter.Value.string"
        paths: "PaymentReconciliation.disposition"
        paths: "PaymentReconciliation.Notes.text"
        paths: "PlanDefinition.usage"
        paths: "PractitionerRole.availabilityExceptions"
        paths: "ProcessResponse.ProcessNote.text"
        paths: "Questionnaire.Item.text"
        paths: "Questionnaire.Item.Option.Value.string"
        paths: "Questionnaire.Item.Initial.string"
        paths: "QuestionnaireResponse.Item.text"
        paths: "QuestionnaireResponse.Item.Answer.Value.string"
        paths: "RequestGroup.Action.textEquivalent"
        paths: "ResearchSubject.assignedArm"
        paths: "ResearchSubject.actualArm"
        paths: "RiskAssessment.mitigation"
        paths: "RiskAssessment.comment"
        paths: "RiskAssessment.Prediction.rationale"
        paths: "Schedule.comment"
        paths: "ServiceDefinition.usage"
        paths: "Slot.comment"
        paths: "Subscription.reason"
        paths: "Subscription.criteria"
        paths: "Subscription.error"
        paths: "Subscription.Channel.header"
        paths: "Task.Parameter.Value.string"
        paths: "Task.Output.Value.string"
        paths: "ValueSet.Compose.ConceptSet.ConceptReference.Designation.value"
        paths: "Attachment.title"
        paths: "Reference.display"
        paths: "Narrative.div"
        action: INSPECT_AND_TRANSFORM
      }
    }
    text {
      transformations {
        replace_with_info_type_config {
        }
      }
      transformations {
        info_types: "DATE"
        date_shift_config {
        }
      }
    }
    

R4
    
    
    fhir {
      field_metadata_list {
        paths: "ActivityDefinition.publisher"
        paths: "AllergyIntolerance.OnsetX.string"
        paths: "Appointment.comment"
        paths: "AppointmentResponse.comment"
        paths: "AuditEvent.outcomeDesc"
        paths: "AuditEvent.Agent.altId"
        paths: "AuditEvent.Agent.Network.address"
        paths: "AuditEvent.Source.site"
        paths: "CapabilityStatement.title"
        paths: "CapabilityStatement.publisher"
        paths: "CarePlan.title"
        paths: "ChargeItemDefinition.title"
        paths: "ChargeItemDefinition.publisher"
        paths: "Claim.Insurance.businessArrangement"
        paths: "ClaimResponse.Insurance.businessArrangement"
        paths: "CodeSystem.title"
        paths: "CodeSystem.publisher"
        paths: "CompartmentDefinition.publisher"
        paths: "Composition.title"
        paths: "Composition.Section.title"
        paths: "ConceptMap.title"
        paths: "ConceptMap.publisher"
        paths: "Condition.OnsetX.string"
        paths: "Condition.AbatementX.string"
        paths: "Contract.title"
        paths: "Contract.subtitle"
        paths: "Coverage.subscriberId"
        paths: "Coverage.dependent"
        paths: "Coverage.network"
        paths: "Device.distinctIdentifier"
        paths: "Device.serialNumber"
        paths: "Device.UdiCarrier.deviceIdentifier"
        paths: "Device.UdiCarrier.carrierHRF"
        paths: "DeviceDefinition.UdiDeviceIdentifier.deviceIdentifier"
        paths: "EffectEvidenceSynthesis.title"
        paths: "EffectEvidenceSynthesis.publisher"
        paths: "EventDefinition.title"
        paths: "EventDefinition.subtitle"
        paths: "EventDefinition.publisher"
        paths: "Evidence.title"
        paths: "Evidence.shortTitle"
        paths: "Evidence.subtitle"
        paths: "Evidence.publisher"
        paths: "EvidenceVariable.title"
        paths: "EvidenceVariable.shortTitle"
        paths: "EvidenceVariable.subtitle"
        paths: "EvidenceVariable.publisher"
        paths: "ExampleScenario.publisher"
        paths: "ExplanationOfBenefit.preAuthRef"
        paths: "ExplanationOfBenefit.Insurance.preAuthRef"
        paths: "FamilyMemberHistory.BornX.string"
        paths: "FamilyMemberHistory.AgeX.string"
        paths: "FamilyMemberHistory.DeceasedX.string"
        paths: "FamilyMemberHistory.Condition.OnsetX.string"
        paths: "GraphDefinition.publisher"
        paths: "ImagingStudy.Series.Instance.title"
        paths: "Immunization.OccurrenceX.string"
        paths: "ImplementationGuide.title"
        paths: "ImplementationGuide.publisher"
        paths: "ImplementationGuide.Manifest.ManifestPage.title"
        paths: "Library.title"
        paths: "Library.subtitle"
        paths: "Library.publisher"
        paths: "List.title"
        paths: "Location.alias"
        paths: "Measure.title"
        paths: "Measure.subtitle"
        paths: "Measure.publisher"
        paths: "MessageDefinition.title"
        paths: "MessageDefinition.publisher"
        paths: "NamingSystem.publisher"
        paths: "NamingSystem.responsible"
        paths: "OperationDefinition.title"
        paths: "OperationDefinition.publisher"
        paths: "Organization.alias"
        paths: "PlanDefinition.title"
        paths: "PlanDefinition.subtitle"
        paths: "PlanDefinition.publisher"
        paths: "PlanDefinition.Action.title"
        paths: "Procedure.PerformedX.string"
        paths: "Questionnaire.title"
        paths: "Questionnaire.publisher"
        paths: "ResearchDefinition.title"
        paths: "ResearchDefinition.shortTitle"
        paths: "ResearchDefinition.subtitle"
        paths: "ResearchDefinition.publisher"
        paths: "ResearchElementDefinition.title"
        paths: "ResearchElementDefinition.shortTitle"
        paths: "ResearchElementDefinition.subtitle"
        paths: "ResearchElementDefinition.publisher"
        paths: "ResearchStudy.title"
        paths: "RiskEvidenceSynthesis.title"
        paths: "RiskEvidenceSynthesis.publisher"
        paths: "SearchParameter.publisher"
        paths: "StructureDefinition.title"
        paths: "StructureDefinition.publisher"
        paths: "StructureMap.title"
        paths: "StructureMap.publisher"
        paths: "TerminologyCapabilities.title"
        paths: "TerminologyCapabilities.publisher"
        paths: "ValueSet.title"
        paths: "ValueSet.publisher"
        paths: "Address.text"
        paths: "Address.line"
        paths: "Address.city"
        paths: "Address.district"
        paths: "Address.postalCode"
        paths: "Annotation.AuthorX.string"
        paths: "ContactPoint.value"
        paths: "HumanName.text"
        paths: "HumanName.family"
        paths: "HumanName.given"
        paths: "HumanName.prefix"
        paths: "HumanName.suffix"
        paths: "Identifier.value"
        action: TRANSFORM
      }
      field_metadata_list {
        paths: "AdverseEvent.SuspectEntity.Causality.productRelatedness"
        paths: "Appointment.patientInstruction"
        paths: "AuditEvent.Entity.Detail.ValueX.string"
        paths: "CarePlan.Activity.Detail.ScheduledX.string"
        paths: "ChargeItem.overrideReason"
        paths: "Claim.SupportingInformation.ValueX.string"
        paths: "Claim.Insurance.preAuthRef"
        paths: "ClaimResponse.preAuthRef"
        paths: "ClaimResponse.Note.text"
        paths: "ClinicalImpression.summary"
        paths: "ClinicalImpression.Finding.basis"
        paths: "Communication.Payload.ContentX.string"
        paths: "CommunicationRequest.Payload.ContentX.string"
        paths: "CompartmentDefinition.Resource.documentation"
        paths: "Contract.Term.text"
        paths: "Contract.Term.ContractOffer.text"
        paths: "Contract.Term.ContractOffer.Answer.ValueX.string"
        paths: "Contract.Term.ContractAsset.condition"
        paths: "Contract.Term.ContractAsset.text"
        paths: "Contract.Term.ContractAsset.AssetContext.text"
        paths: "Contract.Term.ContractAsset.ValuedItem.payment"
        paths: "Contract.Term.Action.reason"
        paths: "CoverageEligibilityResponse.disposition"
        paths: "CoverageEligibilityResponse.preAuthRef"
        paths: "DetectedIssue.detail"
        paths: "DiagnosticReport.conclusion"
        paths: "DiagnosticReport.Media.comment"
        paths: "ExplanationOfBenefit.SupportingInformation.ValueX.string"
        paths: "ExplanationOfBenefit.Note.text"
        paths: "Goal.statusReason"
        paths: "HealthcareService.comment"
        paths: "HealthcareService.availabilityExceptions"
        paths: "ImplementationGuide.Definition.Page.title"
        paths: "Invoice.cancelledReason"
        paths: "Library.usage"
        paths: "MedicationKnowledge.AdministrationGuidelines.PatientCharacteristics.value"
        paths: "NamingSystem.UniqueId.comment"
        paths: "NutritionOrder.OralDiet.instruction"
        paths: "NutritionOrder.Supplement.instruction"
        paths: "NutritionOrder.EnteralFormula.administrationInstruction"
        paths: "Observation.ValueX.string"
        paths: "Observation.Component.ValueX.string"
        paths: "ObservationDefinition.QualifiedInterval.condition"
        paths: "OperationOutcome.Issue.diagnostics"
        paths: "Parameters.Parameter.ValueX.string"
        paths: "PaymentReconciliation.disposition"
        paths: "PaymentReconciliation.Notes.text"
        paths: "PlanDefinition.usage"
        paths: "PractitionerRole.availabilityExceptions"
        paths: "Questionnaire.Item.text"
        paths: "Questionnaire.Item.AnswerOption.ValueX.string"
        paths: "Questionnaire.Item.Initial.ValueX.string"
        paths: "QuestionnaireResponse.Item.text"
        paths: "QuestionnaireResponse.Item.Answer.ValueX.string"
        paths: "RequestGroup.Action.textEquivalent"
        paths: "ResearchDefinition.comment"
        paths: "ResearchDefinition.usage"
        paths: "ResearchElementDefinition.comment"
        paths: "ResearchElementDefinition.usage"
        paths: "ResearchElementDefinition.Characteristic.studyEffectiveDescription"
        paths: "ResearchElementDefinition.Characteristic.participantEffectiveDescription"
        paths: "ResearchSubject.assignedArm"
        paths: "ResearchSubject.actualArm"
        paths: "RiskAssessment.mitigation"
        paths: "RiskAssessment.Prediction.rationale"
        paths: "Schedule.comment"
        paths: "ServiceRequest.patientInstruction"
        paths: "Slot.comment"
        paths: "SpecimenDefinition.timeAspect"
        paths: "Subscription.reason"
        paths: "Subscription.criteria"
        paths: "Subscription.error"
        paths: "Subscription.Channel.header"
        paths: "Task.Parameter.ValueX.string"
        paths: "Task.Output.ValueX.string"
        paths: "ValueSet.Compose.ConceptSet.ConceptReference.Designation.value"
        paths: "Attachment.title"
        paths: "Reference.display"
        action: INSPECT_AND_TRANSFORM
      }
    }
    text {
      transformations {
        replace_with_info_type_config {
        }
      }
      transformations {
        info_types: "DATE"
        date_shift_config {
        }
      }
    }
    

### Using paths to de-identify resources

The following samples show how to configure the Patient resource de-identification with the following criteria:

  * The `HumanName` ([DSTU2](https://www.hl7.org/fhir/dstu2/datatypes.html#HumanName), [STU3](https://www.hl7.org/fhir/stu3/datatypes.html#HumanName), and [R4](https://www.hl7.org/fhir/r4/datatypes.html#HumanName)) values for the Patient resource have a `TRANSFORM` (redaction) automatically applied. For the sample patient, the HumanName values are `"family": "Smith"` and `"given": [ "Darcy" ]`.



No other values are provided in the `paths` list inside the `fieldMetadataList`, so the remaining data is unchanged.

The following samples show how to de-identify the Patient resource's HumanName values:

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': [
                {
                  'paths': [
                    'Patient.HumanName'
                  ],
                  'action': 'TRANSFORM'
                }
              ]
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "",
          "given": [
            ""
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': [
              {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'TRANSFORM'
              }
            ]
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "",
          "given": [
            ""
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

You can see that the following values were transformed to de-identify the resource:

  * The value in `name.family` was redacted.
  * The value in `name.given` was redacted.



However, unlike the sample in default FHIR de-identification, which transformed common PHI, the patient's `address`, `birthDate`, and the free text in `text.div` were not transformed because they were not added to the `paths` list in `fieldMetadataList`.

## Using infoTypes and primitive transformations with FHIR resources

The Cloud Healthcare API can use [_information types_ (infoTypes)](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) to define the data it scans when performing de-identification on FHIR resources. An infoType is a type of sensitive data, such as a patient name, email address, telephone number, identification number, or credit card number. The infoTypes used in the Cloud Healthcare API de-identification operation include those found in [Cloud Data Loss Prevention](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes).

Primitive transformations are rules that used for transforming an input value.

### Default FHIR infoTypes

The default infoTypes used when de-identifying FHIR data are:

  * `AGE`
  * `CREDIT_CARD_NUMBER`
  * `DATE`
  * `EMAIL_ADDRESS`
  * `IP_ADDRESS`
  * `LOCATION`
  * `MAC_ADDRESS`
  * `PASSPORT`
  * `PERSON_NAME`
  * `PHONE_NUMBER`
  * `SWIFT_CODE`
  * `US_DRIVERS_LICENSE_NUMBER`
  * `US_SOCIAL_SECURITY_NUMBER`
  * `US_VEHICLE_IDENTIFICATION_NUMBER`
  * `US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER`



The Cloud Healthcare API de-identifies sensitive text in FHIR resources using its standard infoTypes plus an additional custom infoType for accession numbers.

### Primitive transformation options

The Cloud Healthcare API primitive transformation options include:

  * [`RedactConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#redactconfig): Redacts a value by removing it.
  * [`CharacterMaskConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#charactermaskconfig): Masks a string either fully or partially by replacing input characters with a specified fixed character.
  * [`DateShiftConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#dateshiftconfig): Shifts dates by a random number of days, with the option to be consistent for the same context.
  * [`CryptoHashConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#cryptohashconfig): Uses SHA-256 to replace input values with a base64-encoded representation of a hashed output string generated using a given data encryption key.
  * [`ReplaceWithInfoTypeConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#replacewithinfotypeconfig): Replaces an input value with the name of its infoType.



### Specifying configurations in `TextConfig`

InfoTypes and primitive transformations are specified within an [`InfoTypeTransformation`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#infotypetransformation), which is an object inside the [`TextConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#TextConfig). Specify infoTypes in the `infoTypes` array as comma-separated values.

Specifying an infoType is optional. If you do not specify at least one infoType, the transformation applies to all built-in infoTypes in the data.

If you specify any infoTypes in `InfoTypeTransformation`, specify at least one primitive transformation.

The following sections show how to use the primitive transformations available in `InfoTypeTransformation` along with infoTypes to customize how FHIR resources are de-identified.

### `RedactConfig`

Specifying `redactConfig` redacts a given value by removing it completely. The `redactConfig` message has no arguments; specifying it enables transformation.

The following samples show how to redact the Patient resource's birthdate in the `Patient.text.div` field. This task is accomplished by setting the `DATE` infoType with the `Patient.text.div` path and the `redactConfig` transform.

After sending the de-identification request to the Cloud Healthcare API, the birthdate in the `Patient.text.div` value is redacted.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': {
                'paths': [
                  'Patient.text.div'
                ],
                'action': 'INSPECT_AND_TRANSFORM'
              }
            },
            'text': {
              'transformations': [
                {
                  'infoTypes': [
                    'DATE'
                  ],
                  'redactConfig': {}
                }
              ]
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: </p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': {
              'paths': [
                'Patient.text.div'
              ],
              'action': 'INSPECT_AND_TRANSFORM'
            }
          },
          'text': {
            'transformations': [
              {
                'infoTypes': [
                  'DATE'
                ],
                'redactConfig': {}
              }
            ]
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: </p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

The output shows that the value of `DateOfBirth` in `text.div` has been removed. This is in contrast to the sample in [De-identifying specific FHIR paths](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify#de-identifying_specific_fhir_paths) where the value of `DateOfBirth` in `text.div` was not removed using the default configuration.

### `CharacterMaskConfig`

Specifying `characterMaskConfig` replaces strings that correspond to the given infoTypes with a specified fixed character. For example, rather than redacting a patient's name or transforming it using cryptographic hashing, you can replace the name with a series of asterisks (`*`). Specify the fixed character as a value to the `maskingCharacter` field.

The following samples show how to expand on the sample used in [De-identifying specific FHIR paths](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify#de-identifying_specific_fhir_paths), but they now include setting the `PERSON_NAME` infoType with the `characterMaskConfig` transform. No fixed character is provided, so the masking defaults to using an asterisk. After sending the de-identification request to the Cloud Healthcare API, the values in `name.family` and `name.given` are replaced with asterisks.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'TRANSFORM'
              }
            },
            'text': {
              'transformations': [
                {
                  'infoTypes': [
                    'PERSON_NAME'
                  ],
                  'characterMaskConfig': {
                    'maskingCharacter': ''
                  }
                }
              ]
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "*****",
          "given": [
            "*****"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': {
              'paths': [
                'Patient.HumanName'
              ],
              'action': 'TRANSFORM'
            }
          },
          'text': {
            'transformations': [
              {
                'infoTypes': [
                  'PERSON_NAME'
                ],
                'characterMaskConfig': {
                  'maskingCharacter': ''
                }
              }
            ]
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "*****",
          "given": [
            "*****"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

The output shows that the values in `name.family` and `name.given` have been replaced with asterisks. This is in contrast to the sample in [De-identifying specific FHIR paths](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify#de-identifying_specific_fhir_paths) where the values in `name.family` and `name.given` were redacted.

### `DateShiftConfig`

The Cloud Healthcare API can transform dates by shifting them within a preset range. To keep date transformations consistent across de-identification runs, use `DateShiftConfig` with either of the following:

  * (Deprecated): A raw AES 128/192/256-bit base 64-encoded key.
  * (Recommended): A [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) (Cloud KMS) wrapped key. See [De-identifying and re-identifying sensitive text](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify) for an example on how to use Cloud KMS wrapped keys.



You must grant a role with the [`cloudkms.cryptoKeyVersions.useToDecrypt`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) permission to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to decrypt the Cloud KMS wrapped key. We recommend using the Cloud KMS CryptoKey Decrypter role (`roles/cloudkms.cryptoKeyDecrypter`). When you use Cloud KMS for cryptographic operations, charges apply. See [Cloud Key Management Service pricing](https://cloud.google.com/kms/pricing) for more information.

**Note:** Using `wrapped_key` in `DateShiftConfig` is only available in v1beta1 of the Cloud Healthcare API.

The Cloud Healthcare API uses this key to compute the amount by which dates, such as a patient's birthdate, are shifted within a 100-day differential.

If you don't provide a key, the Cloud Healthcare API generates its own key each time the de-identification operation runs on date values. This can result in inconsistent date outputs between runs.

The following samples show how to set the `DATE` infoType with the `DateShiftConfig` transform on the `Patient.birthDate` and `Patient.text.div` paths. After sending the de-identification request to the Cloud Healthcare API, the `birthDate` value and the birthdate in `Patient.text.div` will shift within plus or minus 100 days of the original birthdate, `1980-12-05`.

The cryptokey provided in the example, `U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU=`, is a raw AES-encrypted 256-bit base64-encoded key generated using the following command. When prompted, provide a password of your choosing to the command:
    
    
    echo -n "test" | openssl enc -e -aes-256-ofb -a -salt
    

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': {
                'paths': [
                  'Patient.birthDate',
                  'Patient.text.div'
                ],
                'action': 'INSPECT_AND_TRANSFORM'
              }
            },
            'text': {
              'transformations': {
                'infoTypes': [
                  'DATE'
                ],
                'dateShiftConfig': {
                  'cryptoKey': 'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
                }
              }
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1981-02-19",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1981-02-19</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': {
              'paths': [
                'Patient.HumanName',
                'Patient.text.div'
              ],
              'action': 'INSPECT_AND_TRANSFORM'
            }
          },
          'text': {
            'transformations': {
              'infoTypes': [
                'DATE'
              ],
              'dateShiftConfig': {
                'cryptoKey': 'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
              }
            }
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1981-02-19",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1981-02-19</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

The output shows that the value in `birthDate` and the birthdate in `Patient.text.div` have been transformed to a new value of `1981-02-19`. This transformation occurred as a result of combining the 100-day differential with the Patient ID and the provided `cryptoKey` value. The new values for `birthDate` and the birthdate in `Patient.text.div` are consistent for this Patient between de-identification runs as long as the same `cryptoKey` is provided.

### `CryptoHashConfig`

The Cloud Healthcare API can transform data by replacing values with cryptographic hashes (also called surrogate values). To do so, specify a `cryptoHashConfig` message.

You can leave the `cryptoHashConfig` empty, or you can provide it with either:

  * (Deprecated): A raw AES 128/192/256-bit base 64-encoded key.
  * (Recommended): A [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) (Cloud KMS) wrapped key. See [De-identifying and re-identifying sensitive text](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify) for an example on how to use Cloud KMS wrapped keys.



You must grant a role with the [`cloudkms.cryptoKeyVersions.useToDecrypt`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) permission to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to decrypt the Cloud KMS wrapped key. We recommend using the Cloud KMS CryptoKey Decrypter role (`roles/cloudkms.cryptoKeyDecrypter`). When you use Cloud KMS for cryptographic operations, charges apply. See [Cloud Key Management Service pricing](https://cloud.google.com/kms/pricing) for more information.

**Note:** Using `wrapped_key` in `CryptoHashConfig` is only available in v1beta1 of the Cloud Healthcare API.

Supplying a consistent key generates surrogate values that are consistent among de-identification runs. If you do not provide a key, the Cloud Healthcare API generates a new key each time the operation runs. Using a different key yields different surrogate values.

The following samples expand on the sample used in De-identifying specific FHIR paths, but they now include setting the `PERSON_NAME` infoType with the `cryptoKey` transform on the `Patient.HumanName` path. After sending the de-identification request to the Cloud Healthcare API, the `name.family` and `name.given` values are replaced with surrogate values.

The cryptokey provided in the example, `U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU=`, is a raw AES-encrypted 256-bit base64-encoded key generated using the following command. When prompted, provide a password of your choosing to the command:
    
    
    echo -n "test" | openssl enc -e -aes-256-ofb -a -salt
    

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'INSPECT_AND_TRANSFORM'
              }
            },
            'text': {
              'transformations': {
                'infoTypes': [
                  'PERSON_NAME'
                ],
                'cryptoHashConfig': {
                  'cryptoKey': 'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
                }
              }
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "NlVBV12Hhb5DD8WNqlTpXboFxzlUSlqAmYDet/jIViQ=",
          "given": [
            "FSH4D/IGb80a1rS0L0kqfC3DCDt6//17VPhIkOzH2pk="
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': {
              'paths': [
                'Patient.HumanName'
              ],
              'action': 'TRANSFORM'
            }
          },
          'text': {
            'transformations': {
              'infoTypes': [
                'PERSON_NAME'
              ],
              'cryptoHashConfig': {
                'cryptoKey': 'U2FsdGVkX19bS2oZsdbK9X5zi2utBn22uY+I2Vo0zOU='
              }
            }
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "NlVBV12Hhb5DD8WNqlTpXboFxzlUSlqAmYDet/jIViQ=",
          "given": [
            "FSH4D/IGb80a1rS0L0kqfC3DCDt6//17VPhIkOzH2pk="
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

The output shows that the values for `name.family` and `name.given` have been transformed using cryptographic hashing. This transformation occurred as a result of combining the Patient ID and the provided `cryptoKey` value. The new `name.family` and `name.given` values are consistent for this Patient between de-identification runs as long as the same `cryptoKey` is provided.

### `ReplaceWithInfoTypeConfig`

The Cloud Healthcare API can transform data by replacing values with the name of the value's `infoType`. You can do this by specifying a `replaceWithInfoTypeConfig` message.

The following samples expand on the sample used in De-identifying specific FHIR paths, but they define `replaceWithInfoType` transformation on `PERSON_NAME` and the `fieldMetadataList` path set to `Patient.HumanName`. After sending the de-identification request to the Cloud Healthcare API, the `name.family` and `name.given` values are replaced with the value's `infoType`.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'INSPECT_AND_TRANSFORM'
              }
            },
            'text': {
              'transformations': {
                'infoTypes': [
                  'PERSON_NAME'
                ],
                'replaceWithInfoType': {}
              }
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/fhir+json; charset=utf-8" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732"

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "[PERSON_NAME]",
          "given": [
            "[PERSON_NAME]"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': {
              'paths': [
                'Patient.HumanName'
              ],
              'action': 'TRANSFORM'
            }
          },
          'text': {
            'transformations': {
              'infoTypes': [
                'PERSON_NAME'
              ],
              'replaceWithInfoTypeConfig': {}
            }
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format: 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/SOURCE_DATASET_ID/operations/OPERATION_NUMBER",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dataset.DatasetService.DeidentifyDataset",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/viewer/CLOUD_LOGGING_URL"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifySummary",
        "successStoreCount": "1",
        "successResourceCount": "1"
      }
    }
    

Next, using the Patient ID, you can get the details for the Patient resource in the new destination dataset: 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DESTINATION_DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/r77433dd-dkeuc-633743nfd-383nfdsjds732" | ConvertTo-Json

The server returns the following response: 
    
    
    {
      "address": [
        {
          "city": "Anycity",
          "district": "Anydistrict",
          "line": [
            "123 Main Street"
          ],
          "period": {
            "start": "1990-12-05"
          },
          "postalCode": "12345",
          "state": "CA",
          "text": "123 Main Street Anycity, Anydistrict, CA 12345",
          "type": "both",
          "use": "home"
        }
      ],
      "birthDate": "1980-12-05",
      "gender": "female",
      "id": "r77433dd-dkeuc-633743nfd-383nfdsjds732",
      "meta": {
        "lastUpdated": "2018-01-01T2018-01-01T00:00:00+00:00",
        "versionId": "MTU0MDU4NTcxNjI2MTUxNDAwMAA"
      },
      "name": [
        {
          "family": "[PERSON_NAME]",
          "given": [
            "[PERSON_NAME]"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient",
      "text": {
        "div": "<div><p><b>Patient</b></p><p><b>Name</b>: Smith, Darcy</p><p><b>DateOfBirth</b>: 1980-12-05</p><p><b>Gender</b>: Female</p></div>",
        "status": "generated"
      }
    }
    

The output shows that the values for `name.family` and `name.given` have been replaced by value's infoType.

## De-identifying data at the FHIR store level

The preceding examples show how to de-identify FHIR data at the dataset level. To change a dataset de-identification request to a FHIR store de-identification request, make the following changes:

  * Modify the `destinationDataset` in the request body to `destinationStore`
  * Add `fhirStores/DESTINATION_FHIR_STORE_ID` at the end of the value in `destinationStore`
  * Add `fhirStores/SOURCE_FHIR_STORE_ID` when specifying the location of the source data.



For example:

**Dataset level de-identification:**
    
    
    'destinationDataset': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID'
    …
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID:deidentify"

**FHIR store level de-identification:**
    
    
    'destinationStore': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/DESTINATION_FHIR_STORE_ID'
    …
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/fhirStores/SOURCE_FHIR_STORE_ID:deidentify"

The following samples expand on De-identifying specific FHIR paths, but de-identification occurs on a single FHIR store and the de-identified data is copied to a new FHIR store. Note that the FHIR store referenced by DESTINATION_FHIR_STORE_ID must already exist.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationStore': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/DESTINATION_FHIR_STORE_ID',
         'config': {
            'fhir': {
              'fieldMetadataList': [
                {
                  'paths': [
                    'Patient.HumanName'
                  ],
                  'action': 'TRANSFORM'
                }
              ]
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/fhirStores/SOURCE_FHIR_STORE_ID:deidentify"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifyFhirStoreSummary"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationStore': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/DESTINATION_FHIR_STORE_ID',
        'config': {
          'fhir': {
            'fieldMetadataList': [
              {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'TRANSFORM'
              }
            ]
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/fhirStores/SOURCE_FHIR_STORE_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation ID. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifyFhirStoreSummary"
      }
    }
    

## De-identifying a subset of a FHIR store

When you de-identify FHIR data at the FHIR store level, you can de-identify a subset of the data by specifying a filter.

The filter takes the form of a list of FHIR resource IDs. You specify the IDs in a [`Resources`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify#resources) object inside of the [`FhirFilter`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify#FhirFilter) object.

The following sample expands on De-identifying data at the FHIR store level, but a list of two FHIR resource IDs (one for a Patient and one for an Observation) is provided that determines which resources are de-identified.

### curl
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'destinationStore': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/DESTINATION_FHIR_STORE_ID',
          'config': {
            'fhir': {
              'fieldMetadataList': [
                {
                  'action': 'TRANSFORM',
                  'paths': [
                    'Patient.HumanName'
                  ]
                }
              ]
            }
          },
          'resourceFilter': {
            'resources': {
              'resources': [
                'Patient/PATIENT_ID',
                'Observation/OBSERVATION_ID'
              ]
            }
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/fhirStores/SOURCE_FHIR_STORE_ID:deidentify"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifyFhirStoreSummary"
      }
    }
    

### PowerShell
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'destinationStore': 'projects/PROJECT_ID/locations/LOCATION/datasets/DESTINATION_DATASET_ID/fhirStores/DESTINATION_FHIR_STORE_ID',
        'resourceFilter': {
          'resources': {
            'resources': [
              'Patient/PATIENT_ID',
              'Observation/OBSERVATION_ID'
            ]
          }
        },
        'config': {
          'fhir': {
            'fieldMetadataList': [
              {
                'paths': [
                  'Patient.HumanName'
                ],
                'action': 'TRANSFORM'
              }
            ]
          }
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/fhirStores/SOURCE_FHIR_STORE_ID:deidentify" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation ID. You can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. After the de-identification process finishes, the response contains `"done": true`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/SOURCE_DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.deidentify.DeidentifyService.DeidentifyFhirStore",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.deidentify.DeidentifyFhirStoreSummary"
      }
    }
    

## De-identifying data in the Google Cloud console

You can de-identify data in the Google Cloud console either for a dataset or a FHIR store. The default FHIR de-identification configuration is used for de-identifying both datasets and FHIR stores. For more information, see Default FHIR data de-identification.

### De-identifying data for a dataset

To de-identify data for a dataset, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Choose **De-identify** from the **Actions** list for the dataset you are de-identifying.

The **De-identify Dataset** page displays.

  3. Select **Set destination dataset** and enter a name for the new dataset to store your de-identified data.

  4. Click **De-identify** to de-identify the data in the dataset.




### De-identifying data in a FHIR store

To de-identify data in a FHIR store, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the dataset for which you want to de-identify data.

  3. In the list of FHIR stores, choose **De-identify** from the **Actions** list for the FHIR store store you are de-identifying.

The **De-identify FHIR Store** page displays.

  4. Select **Set destination data store** and choose the dataset and FHIR store to which the de-identified data is saved.

**Note** : If you want to store your de-identified data in a new FHIR store, you must first create the new store and then select it as the destination FHIR store.

  5. Click **De-identify** to de-identify the data in the FHIR store.




## Troubleshooting FHIR de-identification operations

If errors occur during a FHIR de-identification operation, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If the entire operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
