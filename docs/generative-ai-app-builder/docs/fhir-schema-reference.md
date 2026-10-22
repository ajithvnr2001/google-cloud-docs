---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference/
title: Healthcare FHIR R4 data schema reference \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:40.314069+00:00
---

# Healthcare FHIR R4 data schema reference  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Healthcare FHIR R4 data schema reference Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

Agent Search supports a subset of [FHIR R4 resources](https://hl7.org/fhir/R4/). This page lists the supported FHIR resources and elements. For each resource, this page shows a table of the Google-defined schema configuration, with the following details:

  * A check mark to indicate whether the elements are indexable, searchable, and retrievable, by default. To understand these field settings, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).
  * A check mark to indicate whether the elements are considered as input fields when an LLM answer is generated. That is, to generate the input prompt for the LLM answer, these fields are retrieved from the documents. This field cannot be configured as part of the schema configuration.



## Edit the schema configuration

To edit the schema configuration, select the **Custom schema** option when you [create the data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc). You can edit the schema configuration when you create the data store or later.

## Resource-level specification

Agent Search supports the following resources and resource references:

  * Resources: 
    * AllergyIntolerance
    * Appointment
    * Basic
    * CarePlan
    * Composition
    * Condition
    * DiagnosticReport
    * DocumentReference
    * Encounter
    * ImagingStudy
    * Immunization
    * MedicationAdministration
    * MedicationDispense
    * MedicationRequest
    * MedicationStatement
    * Observation
    * Patient
    * Procedure
    * ServiceRequest
  * Resource references: 
    * Binary
    * Medication
    * Practitioner



## Data-store-level specification

The following properties within the data store are supported.

Property | Indexable | Searchable | Retrievable  
---|---|---|---  
`id` | ✔ | — | ✔  
`resource_type` | ✔ | — | ✔  
`resource_datetime` | ✔ | — | ✔  
`patient_id` | ✔ | — | ✔  
  
## Field-level specification

Agent Search supports a subset of FHIR data elements within each of the supported FHIR resources. The following sections list the supported elements for all the supported FHIR resources and mention whether the elements are indexable, searchable, and retrievable under these conditions:

  * If repeated elements have an empty index or `[]`, all instances of this element are supported. For example, in an AllergyIntolerance resource, all instances of `clinicalStatus.coding[].code` are supported.
  * If repeated elements have a specific index or `[0]`, only the first instance is supported. For example, in a Composition resource only the first instance of `author[0].display` is supported.
  * Relative resource references are supported with the format `Resource/resourceId`. For example, `subject.reference` must have the value as `Patient/034AB16`.
  * [Absolute references](https://build.fhir.org/references.html#literal) are only supported for Binary resources and with data type set to `attachment`. Absolute references are only supported for Cloud Storage locations that conform to the following pattern: `gs://BUCKET_NAME/FILE_PATH`.
  * [Internal or logical references](https://build.fhir.org/references.html#logical) aren't supported and such reference aren't resolved.



### AllergyIntolerance

The following elements within the AllergyIntolerance resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`asserter.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`asserter.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`clinicalStatus.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`clinicalStatus.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`clinicalStatus.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`patient.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`reaction[].description` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`reaction[].manifestation[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`reaction[].severity` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`recordedDate` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`recorder.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`recorder.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`verificationStatus.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`verificationStatus.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`verificationStatus.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
  
### Appointment

The following elements within the Appointment resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`appointmentType.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`appointmentType.coding[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`appointmentType.coding[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`comment` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`created` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`description` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`participant[].actor.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`participant[].type[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`participant[].type[].coding[].display` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`participant[].type[].coding[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`participant[].type[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`reasonCode[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`reasonCode[].coding[].display` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`reasonCode[].coding[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`reasonCode[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`serviceCategory[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`serviceCategory[].coding[].display` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`serviceCategory[].coding[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`serviceCategory[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`start` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
  
### Basic

The following elements within the Basic resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`author.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`author.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`code.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`created` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`text.div` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
  
### CarePlan

The following elements within the CarePlan resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`activity[].detail.description` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`activity[].progress[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`addresses[].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`addresses[].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`author.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`author.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`created` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`description` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`goal[].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`goal[].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`period.end` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`period.start` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`text.div` |  —  |  —  |  ✔  |  —  |  —  |  —   
`title` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
  
### Composition

The following elements within the Composition resource are supported.

**Note:** For a Composition resource to be indexable, it must have the `section[].text.div` element.Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`author[0].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`author[0].reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`category[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`date` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`section[].text.div` |  —  |  ✔  |  ✔  |  ✔  |  —  |  This field must be present for the resource to be indexable.   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`title` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`type.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`type.coding[].display` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`type.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`type.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
  
### Condition

The following elements within the Condition resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`asserter.display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`asserter.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`bodySite[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`bodySite[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`bodySite[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`bodySite[].text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`clinicalStatus.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`clinicalStatus.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`clinicalStatus.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`onsetDateTime` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`onsetPeriod.end` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`onsetPeriod.start` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`recordedDate` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`recorder.display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`recorder.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`verificationStatus.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`verificationStatus.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`verificationStatus.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
  
### DiagnosticReport

The following elements within the DiagnosticReport resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`category[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`conclusion` |  —  |  ✔  |  ✔  |  ✔  |  —  |  This only applies when `presentedForm[0].data` isn't available.   
`effectiveDateTime` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`imagingStudy[].imagingStudyId` |  —  |  —  |  ✔  |  —  |  —  |  —   
`issued` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`performer[0].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`performer[0].reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`presentedForm[0].data` |  —  |  ✔  |  —  |  ✔  |  —  |  Needs to be base64 encoded. Can contain a path.   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### DocumentReference

The following elements within the DocumentReference resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`authenticator.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`authenticator.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`author[0].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`author[0].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`content[0].attachment.contentType` |  —  |  —  |  ✔  |  ✔  |  —  |  Supported mime types:

  * application/json
  * application/pdf
  * application/rtf
  * application/xhtml+xml
  * application/xml
  * image/bmp
  * image/gif
  * image/jpeg
  * image/png
  * image/tiff
  * text/html
  * text/plain
  * text/xml

  
`content[0].attachment.creation` |  —  |  —  |  ✔  |  —  |  —  |  —   
`content[0].attachment.data` |  —  |  ✔  |  —  |  ✔  |  —  |  Needs to be base64 encoded.   
`content[0].attachment.title` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`content[0].attachment.url` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`content[0].format.code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`content[0].format.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`content[0].format.system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`context.encounter[].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`context.period.end` |  —  |  —  |  ✔  |  —  |  —  |  —   
`context.period.start` |  —  |  —  |  ✔  |  —  |  —  |  —   
`custodian.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`custodian.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`date` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`description` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`docStatus` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`type.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`type.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`type.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`type.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
  
### Encounter

The following elements within the Encounter resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`class.code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`class.display` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`class.system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`location[].location.display` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`location[].location.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`participant[0].individual.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`participant[0].individual.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`participant[].type[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`participant[].type[].coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`participant[].type[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`participant[].type[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`period.end` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`period.start` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`reasonCode[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`reasonCode[].coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`reasonCode[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`reasonCode[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`serviceType.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`serviceType.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`serviceType.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`serviceType.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`status` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`type[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`type[].coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`type[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`type[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
  
### ImagingStudy

The following elements within the ImagingStudy resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`description` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`endpoint[0].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`modality[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`modality[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`modality[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`procedureCode[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`procedureCode[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`procedureCode[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`procedureCode[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`referrer.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`referrer.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`started` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### Immunization

The following elements within the Immunization resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`manufacturer.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`manufacturer.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  —  |  ✔  |  —  |  —  |  —   
`occurrenceDateTime` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`occurrenceString` |  —  |  —  |  ✔  |  —  |  —  |  —   
`patient.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`primarySource` |  —  |  —  |  ✔  |  —  |  —  |  —   
`recorded` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`vaccineCode.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`vaccineCode.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`vaccineCode.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`vaccineCode.text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
  
### MedicationAdministration

The following elements within the MedicationAdministration resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`category.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`context.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.dose.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.dose.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.method.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.method.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.method.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.method.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.rateQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.rateQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.route.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.route.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.route.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.route.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.site.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.site.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.site.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage.site.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`effectiveDateTime` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`effectivePeriod.end` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`effectivePeriod.start` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationCodeableConcept.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationReference.display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`medicationReference.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Medication only.   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`performer[0].actor.display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`performer[0].actor.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`request.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### MedicationDispense

The following elements within the MedicationDispense resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`category.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`context.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`daysSupply.code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`daysSupply.system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`daysSupply.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`daysSupply.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].doseQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].doseQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].rateQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].rateQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].method.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].method.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].method.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].method.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].route.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].route.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].route.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].route.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].site.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].site.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].site.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosageInstruction[].site.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationCodeableConcept.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationReference.display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`medicationReference.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Medication only.   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`quantity.code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`quantity.system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`quantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`quantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`status` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`statusReasonCodeableConcept.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReasonCodeableConcept.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`statusReasonCodeableConcept.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReasonCodeableConcept.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`whenHandedOver` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
  
### MedicationRequest

The following elements within the MedicationRequest resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`authoredOn` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`category[].coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].doseQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].doseAndRate[].doseQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].patientInstruction` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].route.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosageInstruction[].timing.code.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationCodeableConcept.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`medicationReference.display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`medicationReference.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Medication only.   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`reportedBoolean` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`reportedReference.display` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`reportedReference.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`requester.display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`requester.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`status` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### MedicationStatement

The following elements within the MedicationStatement resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`category.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category.text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`context.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dateAsserted` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].doseAndRate[].doseQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].doseAndRate[].doseQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].patientInstruction` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].route.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage[].route.coding[].display` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].route.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`dosage[].route.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`dosage[].timing.code.text` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`effectiveDateTime` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`effectivePeriod.end` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`effectivePeriod.start` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationCodeableConcept.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`medicationReference.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`medicationReference.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`status` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
  
### Observation

The following elements within the Observation resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`category[].coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`code.coding[].system` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`component[].code.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`component[].code.coding[].display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`component[].code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`component[].code.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`component[].valueQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`component[].valueQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`effectiveDateTime` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`issued` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`performer[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`performer[].reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`status` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
`valueQuantity.unit` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`valueQuantity.value` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`valueString` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
  
### Patient

The following elements within the Patient resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`active` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`birthDate` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`gender` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].type.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].type.coding[].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].type.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].type.text` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`name[].family` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`name[].given[]` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`name[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
  
### Procedure

The following elements within the Procedure resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`basedOn[].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`basedOn[].reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`bodySite[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`bodySite[].coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`bodySite[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`bodySite[].text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`category.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`category.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].code` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  —  |  —  |  —   
`encounter.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`identifier[].value` |  —  |  —  |  ✔  |  —  |  —  |  —   
`location.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`location.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`performedDateTime` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`performer[0].actor.display` |  —  |  ✔  |  ✔  |  —  |  —  |  —   
`performer[0].actor.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`recorder.display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`recorder.reference` |  —  |  —  |  ✔  |  —  |  —  |  —   
`status` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].code` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].display` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`statusReason.text` |  —  |  —  |  ✔  |  —  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### ServiceRequest

The following elements within the ServiceRequest resource are supported. 

Element | Indexable | Searchable | Retrievable | LLM Input | Reference Support | Constraint  
---|---|---|---|---|---|---  
`authoredOn` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`category[].coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`category[].coding[].display` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`category[].coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`category[].text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`code.coding[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`code.coding[].display` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`code.coding[].system` |  —  |  —  |  ✔  |  —  |  —  |  —   
`code.text` |  ✔  |  ✔  |  ✔  |  ✔  |  —  |  —   
`id` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`intent` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`meta.source` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`meta.tag[].code` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`meta.tag[].display` |  ✔  |  —  |  ✔  |  ✔  |  —  |  —   
`meta.tag[].system` |  ✔  |  —  |  ✔  |  —  |  —  |  —   
`note[].text` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`priority` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`requester.display` |  —  |  ✔  |  ✔  |  ✔  |  —  |  —   
`requester.reference` |  —  |  —  |  ✔  |  —  |  ✔  |  Practitioner only.   
`status` |  —  |  —  |  ✔  |  ✔  |  —  |  —   
`subject.reference` |  ✔  |  —  |  ✔  |  —  |  ✔  |  Patient only.   
  
### References

Agent Search resolves specific references to make search comprehensive. For example, you can search for a practitioner name and find the resources that refer to that practitioner. The following resources are supported in the context of references. Further, only the elements specified within the resources are used when searching for the resources containing the references. 

**Resource** | **Element** | **Retrievable** | **Indexable** | **Searchable** | **Constraints**  
---|---|---|---|---|---  
Binary  | `id` | —  | —  | —  | —   
Binary  | `contentType` | ✔  | —  | —  | 

  * application/json
  * application/pdf
  * application/rtf
  * application/xhtml+xml
  * application/xml
  * image/bmp
  * image/gif
  * image/jpeg
  * image/png
  * image/tiff
  * text/html
  * text/plain
  * text/xml

  
Binary  | `data` | ✔  | —  | ✔  | —   
Location  | `id` | ✔  | —  | —  | —   
Location  | `name` | ✔  | ✔  | ✔  | —   
Medication  | `id` | —  | —  | —  | —   
Medication  | `text` | ✔  | ✔  | ✔  | —   
Medication  | `code.coding[].code` | ✔  | ✔  | —  | —   
Medication  | `code.coding[].system` | ✔  | —  | —  | —   
Medication  | `code.coding[].display` | ✔  | —  | ✔  | —   
Practitioner  | `id` | ✔  | —  | —  | —   
Practitioner  | `name[0].family` | ✔  | ✔  | ✔  | First instance of the name only.   
Practitioner  | `name[0].given[]` | ✔  | ✔  | ✔  | First instance of the name only.   
Practitioner  | `name[0].text` | ✔  | ✔  | ✔  | First instance of the name only.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
