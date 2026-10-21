---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp/
title: Healthcare Natural Language API \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:18.173231+00:00
---

# Healthcare Natural Language API  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/nlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Healthcare Natural Language API Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The Healthcare Natural Language API is deprecated and will be shut down on May 27, 2026. For more information, see [Deprecations](https://docs.cloud.google.com/healthcare-api/docs/deprecations). 

The Healthcare Natural Language API is a part of the Cloud Healthcare API that uses natural language models to extract healthcare information from medical text.

This conceptual guide explains the basics of using the Healthcare Natural Language API, including:

  * The types of requests you can make to the Healthcare Natural Language API
  * How to construct requests to the Healthcare Natural Language API
  * How to handle responses from the Healthcare Natural Language API



## Overview

The Healthcare Natural Language API extracts healthcare information from medical text. This healthcare information can include:

  * Medical concepts, such as medications, procedures, and medical conditions
  * Functional features, such as temporal relationships, subjects, and certainty assessments
  * Relations, such as side effects and medication dosage

**Note:** You don't need to create a dataset in the Cloud Healthcare API to use the Healthcare Natural Language API.

### Choosing between the Healthcare Natural Language API and AutoML Entity Extraction for Healthcare

The Healthcare Natural Language API offers pre-trained natural language models to extract medical concepts and relationships from medical text. The Healthcare Natural Language API maps text into a predefined set of _medical knowledge categories_.

AutoML Entity Extraction for Healthcare lets you create a custom entity extraction model trained using your own annotated medical text and using your own categories. For more information, see the [AutoML Entity Extraction for Healthcare documentation](https://docs.cloud.google.com/natural-language/automl/docs/automl-healthcare).

## Available locations

The Healthcare Natural Language API is available in the following locations:

Location name | Location description  
---|---  
[`asia-south1`](https://cloud.google.com/about/locations/?region=asia-pacific#asia-pacific) | Mumbai, India  
[`australia-southeast1`](https://cloud.google.com/about/locations/?region=asia-pacific#asia-pacific) | Sydney, Australia  
[`europe-west2`](https://cloud.google.com/about/locations/?region=europe#europe) | London, UK  
[`europe-west4`](https://cloud.google.com/about/locations/?region=europe#europe) | Netherlands  
[`northamerica-northeast1`](https://cloud.google.com/about/locations/?region=americas#americas) | Montréal, Canada  
[`us-central1`](https://cloud.google.com/about/locations/?region=americas#americas) | Iowa, USA  
  
## Healthcare Natural Language API features

The Healthcare Natural Language API inspects medical text for medical concepts and relations. You perform entity analysis using the [`analyzeEntities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities) method.

### Entity analysis requests

The Healthcare Natural Language API is a REST API and consists of JSON requests and responses. The following sections show how to extract different medical insights from a given medical text:

  * [Extract entities, relations, and contextual attributes](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#extract-entities)
  * [Include licensed vocabularies](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#licensed-vocab)
  * [Extract output as a FHIR R4 bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#alternative-output-format)



The entity analysis request contains the following fields:

  * [`documentContent`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#body.request_body.FIELDS.document_content): The data for the request, which consists of medical text. The maximum size of the medical text is 20,000 Unicode characters.
  * [`licensedVocabularies[]`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#body.request_body.FIELDS.licensed_vocabularies): Optional. The [SNOMED CT](https://en.wikipedia.org/wiki/SNOMED_CT) vocabulary. Available only for US users.
  * [`alternativeOutputFormat`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#body.request_body.FIELDS.alternative_output_format): Optional. The FHIR bundle format.



### Entity analysis response fields

The entity analysis returns a set of detected medical knowledge mentions, medical concepts, and relations between medical knowledge mentions, including the following:

  * `entityMentions`: occurrences of medical knowledge entities in the source medical text. Each entity mention has the following fields:

    * `mentionId`: a unique identifier for an entity mention in the response.
    * `type`: the medical knowledge category of the entity mention.
    * `text`: consists of the `textContent` field, and describes the excerpt of the medical text containing the entity mention, and `offset`, the location of the entity mention in the source medical text.
    * `temporalAssessment`: specifies how the linked entity relates to the entity mention, one of `CURRENT`, `CLINICAL_HISTORY`, `FAMILY_HISTORY`, `UPCOMING`, or `OTHER`.
    * `certaintyAssessment`: the negation or qualification of the medical concept, one of `LIKELY`, `SOMEWHAT_LIKELY`, `UNCERTAIN`, `SOMEWHAT_UNLIKELY`, `UNLIKELY`, or `CONDITIONAL`.
    * `subject`: specifies the subject that the medical concept relates to, one of `PATIENT`, `FAMILY_MEMBER`, or `OTHER`.
    * `linkedEntities`: a list of medical concepts that might be related to this entity mention. Linked entities specify the `entityId`, which links a medical concept to an an entity in `entities`.
  * `entities`: describes the medical concepts from the linked entities fields. Each entity is described using the following fields:

    * `entityId`: a unique identifier from the `linkedEntities` field.
    * `preferredTerm`: a preferred term for the medical concept.
    * `vocabularyCodes`: the representation of the medical concept in supported medical vocabularies.
  * `relationships`: define directed relationships between entity mentions. In the sample, the subject of the relationship is "Insulin regimen human" and the object of the relationship is "5 units".

  * `confidence`: an indication of the model's confidence in the relationship as a number between 0 and 1.




Apart from the listed fields, the response might also contain the `additionalInfo` field, which states any additional description about the entity mention type. See Additional information.

### Supported languages

The Healthcare Natural Language API only supports extracting healthcare information from English text.

### Supported medical vocabularies

The Healthcare Natural Language API supports the following medical vocabularies:

  * Foundational Model of Anatomy
  * Gene Ontology
  * HUGO Gene Nomenclature Committee
  * Human Phenotype Ontology
  * ICD-10 Procedure Coding System
  * ICD-10-CM
  * ICD-9-CM
  * LOINC
  * MeSH
  * MedlinePlus Health Topics
  * Metathesaurus Names
  * NCBI Taxonomy
  * NCI Thesaurus
  * National Drug File
  * Online Mendelian Inheritance in Man
  * RXNORM
  * SNOMED CT (available for US users only)



### Supported medical knowledge categories

The Healthcare Natural Language API assigns a medical knowledge category to the `entityMentions.type` field. A list of supported medical knowledge categories is as follows. The entity mention types that belong to the oncology, social determinants of health (SDOH), and protected health information (PHI) groups are only available in [Preview](https://cloud.google.com/products#product-launch-stages):

Group  | Medical knowledge category  | Description   
---|---|---  
General  | `ANATOMICAL_STRUCTURE` | A complex part of the human body, such as cells, organs, and systems.   
`BODY_FUNCTION` | A function carried out by the human body.   
`BF_RESULT` | The result of a body function.   
`BODY_MEASUREMENT` | A normal measurement of the human body, such as vital signs, obtained without any complex tests or procedures using basic instruments, such as a thermometer or a stethoscope.   
`BM_RESULT` | The result of a body measurement.   
`BM_UNIT` | The unit for a body measurement.   
`BM_VALUE` | The value of a body measurement.   
`LABORATORY_DATA` | The results of testing a bodily sample.   
`LAB_RESULT` | A qualitative description of laboratory data, such as "increased", "decreased", "positive", or "negative".   
`LAB_VALUE` | The value of an instance of the laboratory data.   
`LAB_UNIT` | The unit of measurement for the laboratory value.   
`MEDICAL_DEVICE` | A physical or virtual instrument.   
`MEDICINE` | A drug or other preparation for the treatment or prevention of a disease.   
`MED_DOSE` | A dose of a medication.   
`MED_DURATION` | The period of administration of a medication.   
`MED_FORM` | The physical characteristics of a specific medication.   
`MED_FREQUENCY` | The frequency at which a medication is taken.   
`MED_ROUTE` | A location in the body where a medication is administered.   
`MED_STATUS` | The status of an existing medication, such as "continue", "start", "restart", "stop", "switch", "increase", and "decrease".   
`MED_STRENGTH` | The amount of active ingredient in a dose of a medication.   
`MED_UNIT` | The unit of measurement for the active ingredient in a medication.   
`MED_TOTALDOSE` | The quantity of medication to take at one time.   
`PROBLEM` | A medical condition, including findings and diseases.   
`PROCEDURE` | A diagnostic or treatment procedure.   
`PROCEDURE_RESULT` | The results of a procedure.   
`PROC_METHOD` | The method used to conduct a procedure.   
`SEVERITY` | The severity of the medical condition.   
`SUBSTANCE_ABUSE` | A description of abuse of a psychoactive substance.   
Oncology (Preview)  | `CLINICAL_STATUS` | The status of a cancer case such as "active", "recurring", "relapsing", and "resolved".   
`DATE` | A date annotation, such as the date of diagnosis, date of procedure, or date of a radiation treatment. It extracts all the elements of a date and might not include the year.   
`DIMENSIONS` | The measurements of a tumor, a mass, or an abnormal growth.   
`GENE_STUDIED` | The genes studied which directly or indirectly lead to tumor formation, such as BRCA1, p53, and ALK.   
`HISTOLOGICAL_GRADE` | A classification system to grade the appearance of a cancerous cell.   
`LAB_SPECIMEN` | Biological material collected from the body for testing or sampling.   
`RADIATION_DOSAGE` | The amount of radiation given to a patient.   
`ONSET` | A date annotation to represent the date when a patient first observed cancer-related problems.   
`VARIATION_CODE` | A code given to the specific genomic variant that's detected under a major coding system such as [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) and [HGVS](https://varnomen.hgvs.org/).   
Social determinants of health (SDoH) (Preview)  | `AGE` | An age identifier. It includes phrases describing age, such as "looks younger than stated age", "middle-aged", "78 years old", or "teen". Note: HIPAA classifies the age of a person as PHI only when it's above 90. For more information, see [Summary of the HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html).   
`FAMILY` | Phrases describing the patient's family structure or relatives, such as "married with two kids", "brother", "wife", "supportive parents", or "divorced".   
`LIVING_SITUATION` | Phrases describing the patient's living situation, such as "with roommates", "has 24/7 homecare nurse", or "moved recently".   
`SOCIAL_IDENTITY` | Phrases describing the patient's or the family's social identity including race, ethnicity, sexual orientation, religion, nationality, languages spoken or not spoken, or country of origin.   
`PHYSICAL_APPEARANCE` | Phrases describing the patient's or the family's most noticeable or evident physical trait, such as "scar on the right cheek", "Down's syndrome", "obese", or "left leg amputated".   
`OCCUPATION ` | Phrases describing the patient's or family's occupation and employment status, such as "retired mother", "worked as a welder for 20 years", or "lost job last year".   
Protected health information (PHI) (Preview)  | `PERSON_NAME` | A generic name identifier for a person. Includes titles, such as "Dr.", "Mrs.", or "MD"   
`ORGANIZATION_NAME` | An identifier for a medical organization that collects PHI, such as a clinic, nursing home, or hospital.   
`GENERIC_ID` | A generic ID that identifies medical records, patients, doctors, hospitals, such as the patient's SSN, or a provider's number.   
`LOCATION` | A geographic location that might contain names and numbers for buildings, streets, cities, states, or ZIP code.   
`PHONE_NUMBER` | A number to indicate a phone number, fax number, or pager number.   
`EMAIL_ADDRESS` | An email address identifier.   
`URL` | A website's address.   
`ZIPCODE` | A ZIP code identifier.   
  
### Supported functional feature categories

The Healthcare Natural Language API can infer functional features, or attributes, of an entity mention from context. For example, in the statement "Kusuma's mother has diabetes", the condition "diabetes" has the functional feature of `subject` `FAMILY_MEMBER`.

#### Temporal relationships

Temporal relationships, returned in the `temporalAssessment` field, describe how this entity mention relates to the subject temporally.

The Healthcare Natural Language API supports the following temporal relationships:

  * `CURRENT`
  * `CLINICAL_HISTORY`
  * `FAMILY_HISTORY`
  * `UPCOMING`
  * `OTHER`



#### Subjects

Subjects, returned in the `subject` field, describe the individual the entity mention relates to.

The Healthcare Natural Language API supports the following subjects:

  * `PATIENT`
  * `FAMILY_MEMBER`
  * `OTHER`



#### Certainty assessments

Certainty assessments, returned in the `certaintyAssessment` field, describe the original note taker's confidence. For example, if the original note contains "The patient has a sore throat", the certainty assessment returns a `LIKELY` value to indicate the note taker's confidence that it was likely that the patient had a sore throat. If the original note contains "The patient does not have a sore throat", the certainty assessment returns an `UNLIKELY` value to indicate the note taker's confidence that it was unlikely that the patient had a sore throat.

Certainty assessments can be one of the following values:

  * `LIKELY`
  * `SOMEWHAT_LIKELY`
  * `UNCERTAIN`
  * `SOMEWHAT_UNLIKELY`
  * `UNLIKELY`
  * `CONDITIONAL`



#### Additional information

The `additionalInfo` field provides additional details about an entity mention. For example, the `additionalInfo` field for a `DATE` entity mention might consist of details about the type of the date, categorized as one of the following:

  * `ADMISSION_DATE`
  * `CONSULTATION_DATE`
  * `DISCHARGE_DATE`
  * `SERVICE_DATE`
  * `VISIT_DATE`
  * `DIAGNOSIS_DATE`
  * `MED_STARTED_DATE`
  * `MED_ENDED_DATE`
  * `NOTE_DATE`
  * `PROCEDURE_DATE`
  * `RADIATION_STARTED_DATE`
  * `RADIATION_ENDED_DATE`
  * `STAGE_DATE`



### Supported relationships between entity mentions

The Healthcare Natural Language API can infer relationships between entity mentions based on the surrounding medical text. In the response, the subject of the relationship is identified by `subjectId` and the object of the relationship is identified by `objectId`.

The Healthcare Natural Language API supports the following relationships between entity mentions:

Subject | Object  
---|---  
`ANATOMICAL_STRUCTURE` | `MEDICAL_DEVICE`  
`BODY_FUNCTION` | `BF_RESULT`  
`BODY_MEASUREMENT` | `BM_RESULT`  
`BODY_MEASUREMENT` | `BM_UNIT`  
`BODY_MEASUREMENT` | `BM_VALUE`  
`LABORATORY_DATA` | `LAB_RESULT`  
`LABORATORY_DATA` | `LAB_UNIT`  
`LABORATORY_DATA` | `LAB_VALUE`  
`MEDICINE` | `MED_DOSE`  
`MEDICINE` | `MED_DURATION`  
`MEDICINE` | `MED_FORM`  
`MEDICINE` | `MED_FREQUENCY`  
`MEDICINE` | `MED_ROUTE`  
`MEDICINE` | `MED_STATUS`  
`MEDICINE` | `MED_STRENGTH`  
`MEDICINE` | `MED_TOTALDOSE`  
`MEDICINE` | `MED_UNIT`  
`PROBLEM` | `ANATOMICAL_STRUCTURE`  
`PROBLEM` | `MEDICINE`  
`PROBLEM` | `PROCEDURE`  
`PROBLEM` | `SEVERITY`  
`PROCEDURE` | `ANATOMICAL_STRUCTURE`  
`PROCEDURE` | `PROC_METHOD`  
`PROCEDURE` | `PROCEDURE_RESULT`  
`SUBSTANCE_ABUSE` | `SEVERITY`  
  
## Healthcare Natural Language API output as a FHIR bundle

When you request the `analyzeEntities` method with the [`alternativeOutputFormat`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.services.nlp/analyzeEntities#body.request_body.FIELDS.alternative_output_format) field set to `FHIR_BUNDLE`, the response includes the following JSON objects:

  * The entity mentions, the entities, and the relationships
  * A FHIR R4 bundle represented as a string, that includes all the entities, the entity mentions, and the relationships in JSON format



To create the FHIR R4 bundle, the Healthcare Natural Language API maps the entity mentions, entities, and relationships to FHIR resources and their elements. The following table lists some of these mappings.

Healthcare Natural Language API entity mentions | Medical Knowledge Category | FHIR R4 resources and elements  
---|---|---  
`PROBLEM` |  | `Condition`  
`PROBLEM` |  | `Condition.category`  
`PROBLEM` |  | `Condition.status`  
`PROBLEM` | `ANATOMICAL_STRUCTURE` | `Condition.bodySite`  
`PROBLEM` | `ANATOMICAL_STRUCTURE` | `Condition.evidence`  
`PROBLEM` | `SEVERITY` | `Condition.severity`  
`PROCEDURE` |  | `Procedure`  
`PROCEDURE` |  | `Procedure.status`  
`PROCEDURE` |  | `Procedure.code`  
`PROCEDURE` | `ANATOMICAL_STRUCTURE` | `Procedure.bodySite`  
`PROCEDURE` | `MEDICAL_DEVICE` | `Procedure.usedCode`  
`PROCEDURE` | `PROBLEM` | `Procedure.reasonReference`  
`MEDICINE` |  | `MedicationStatement`  
`MEDICINE` |  | `MedicationStatement.status`  
`MEDICINE` |  | `MedicationStatement.medication`  
`MEDICINE` | `PROBLEM` | `MedicationStatement.reasonReference`  
`MEDICINE` | `MED_DOSE` | `MedicationStatement.dosage.doseAndRate.doseQuantity`  
`MEDICINE` | `MED_FREQUENCY` | `MedicationStatement.dosage.text`  
`MEDICINE` | `MED_ROUTE` | `MedicationStatement.dosage.route`  
`MEDICINE` | `MED_STRENGTH` | `MedicationStatement.dosage.doseAndRate.doseQuantity`  
`MEDICINE` | `MED_UNIT` | `MedicationStatement.dosage.doseAndRate.doseQuantity`  
  
To extract entities from text as a FHIR R4 bundle, see [Extract output as a FHIR R4 bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/nlp#alternative-output-format).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
