---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir/
title: FHIR \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:16.767013+00:00
---

# FHIR  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  FHIR Stay organized with collections  Save and categorize content based on your preferences. 

[Fast Healthcare Interoperability Resources (FHIR)](https://www.hl7.org/fhir/) is a healthcare data standard with an application programming interface (API) for representing and exchanging electronic health records (EHR). FHIR is an information network that lets you link data across systems and a communication network that lets you exchange data between systems.

FHIR includes the following:

  * An HTTP-based RESTful protocol
  * Data representation that uses JSON, XML, and RDF



For more details about FHIR, see the most recently published version of the [FHIR specification](http://hl7.org/fhir).

## Importance of FHIR in healthcare information technology

Healthcare IT systems often don't share the same data models. As healthcare data becomes more digitized, solving incompatibilities between different systems becomes expensive and time-consuming.

FHIR defines a common data model and REST architecture so that different healthcare systems can share and integrate data. FHIR is designed to be flexible and adaptable, so that it can be used in a wide range of settings and with different health care information systems.

FHIR uses _resources_ to represent discrete medical, administrative, infrastructural, or financial data elements. Each resource is linked to a unique identifier, making it simpler for applications to access and modify the same data. Resources can be compiled and distributed to different healthcare providers in formats that comply with their respective data models.

FHIR is a valuable tool for improving the interoperability of healthcare IT systems. It can help to reduce costs, improve efficiency, and improve the quality of care.

## Benefits of FHIR

### Interoperability across devices and platforms

FHIR accommodates the exchange of healthcare data from monolithic data silos to open APIs. FHIR is the primary healthcare data standard with open APIs for accessing, searching, and modifying electronic health records (EHR) and exchanging data between healthcare IT systems.

FHIR lets EHR to be exchanged between healthcare providers and consumers on platforms such as the following:

  * EHR-based data sharing
  * Mobile apps
  * Cloud-based applications
  * Wearable devices



The FHIR API also lets third-party apps integrate with existing systems.

### Compatibility with legacy standards

FHIR evolved from HL7 Version 2 messaging and HL7 Version 3 Clinical Document Architecture (HL7 CDA). FHIR can be used in partnership with HL7v2 and HL7 CDA.

For more information on the relationship between FHIR and other HL7 standards, see [Appendix: The Relationship between FHIR and other HL7 Standards](https://www.hl7.org/fhir/comparison.html).

### Decipherable and useful data

Because FHIR is implemented on top of the HTTPS protocol, you can retrieve and dissect FHIR resources to support machine learning, AI, and other forms of data analytics. These capabilities let you generate a deeper and more versatile understanding of your healthcare data.

### Efficient data exchange

FHIR's resource-based approach facilitates more efficient and accurate data exchange. Because FHIR uses a uniform standard for health information, it lets you build custom templates from the shared base resources, and it eliminates inconsistency in data templates. This uniformity improves the accuracy and readability of data in data exchanges across health systems.

FHIR eliminates the need to individually modify the data template of every health IT system by exchanging data as resources. FHIR exposes resources such as patients, admissions, and medications as _services_. Therefore, consumer mobile apps can use `GET` and `POST` requests to retrieve and manipulate only the relevant data.

## FHIR architecture

### FHIR stores

A _FHIR store_ is a data store in the Cloud Healthcare API that holds FHIR resources. FHIR stores exist inside datasets.

The [`FhirStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores) resource provides a representation of a FHIR store's attributes. For each FHIR store, you can choose options such as:

  * Enabling the `updateCreate` capability ([DSTU2](https://www.hl7.org/fhir/DSTU2/conformance-definitions.html#Conformance.rest.resource.updateCreate), [STU3](https://www.hl7.org/fhir/STU3/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate), [R4](https://www.hl7.org/fhir/R4/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate), [R5](https://www.hl7.org/fhir/R5/capabilitystatement-definitions.html#CapabilityStatement.rest.resource.updateCreate)).
  * Publishing changes to the FHIR store to a [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) topic.
  * Requiring [referential integrity](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity).
  * Enabling resource versioning ([DSTU2](http://hl7.org/fhir/DSTU2/resource.html#Meta), [STU3](http://hl7.org/fhir/STU3/resource.html#Meta), [R4](http://hl7.org/fhir/R4/resource.html#Meta), [R5](http://hl7.org/fhir/R5/resource.html#Meta)).



The state of these configuration options is shown in the FHIR store's capability statement ([STU3](https://www.hl7.org/fhir/STU3/capabilitystatement.html) or [R4](https://www.hl7.org/fhir/R4/capabilitystatement.html) or [R5](https://www.hl7.org/fhir/R5/capabilitystatement.html)) or [conformance statement (DSTU2)](https://hl7.org/fhir/DSTU2/conformance.html).

### FHIR resources

FHIR uses _resources_ to organize data formats and elements. Each resource has the following properties:

  * A shared method for defining and representing data, built upon data types consisting of reusable clusters of elements.
  * A common set of metadata, providing technical and structural context.
  * A human-readable text representation that uses HTML as a fallback display option for clinical safety.



FHIR specifies a base set of resources that can be combined in various ways to meet the data model demands of healthcare providers. It also provides representations of clinical observations and documents. FHIR does not aim to encompass every possible document or data type. Instead, FHIR first supports most clinical and billing use cases. You can then extend your FHIR implementation to meet additional clinical or organizational needs.

### FHIR profiles

Using extensions, applications can customize the existing resources and describe their specifications with profiles. Profiles are a set of instructions in addition to the existing core specification for resources that fall under a specific use and context. The Cloud Healthcare API enforces profiles by validating resources against the constraints in the relevant profile.

For instance, recording a patient's ethnicity is not allowed in certain regions, but required in others. Using profiles, the FHIR base specification can define and require an "ethnicity" extension in accordance with the regional policies. Therefore, profiles help countries, regions, districts, and organizations customize data in accordance with their healthcare data regulations and needs.

You can use profiles to do the following:

  * Extend and restrict the FHIR API by defining additional operations, specify required pre-existing search parameters, and add new search parameters.
  * Extend and restrict resources by defining extensions of resources and changing the cardinality of fields.



A collection of profiles can be published as an implementation guide. Implementation guides are both machine- and human-readable. They can be exchanged and searched using REST and used to generate code and user interfaces.

For more information on FHIR extensions, see [FHIR extensions](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-extensions).

## FHIR base URL implementation

As shown in the official FHIR documentation ([DSTU2](https://www.hl7.org/fhir/dstu2/http.html#general), [STU3](https://www.hl7.org/fhir/STU3/http.html#general), and [R4](https://www.hl7.org/fhir/R4/http.html#general)), a FHIR Service Base URL uses the format `http(s)://server/PATH`. For example, `https://server/path/Observation`.

The Cloud Healthcare API uses a base URL that aligns with this standard. The Cloud Healthcare API base URL contains the following parts:

  * The endpoint for the Cloud Healthcare API
  * The version of the Cloud Healthcare API
  * The project ID
  * The name of a dataset
  * The dataset's location
  * The name of a FHIR store
  * The `/fhir` suffix



The following table shows the format of a FHIR Service Base URL and its equivalent base URL in the Cloud Healthcare API:

FHIR Service Base URL| Cloud Healthcare API equivalent URL  
---|---  
`http(s)://server/PATH` | `https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir`  
  
To get information about a patient using the FHIR RESTful API, make an HTTP `GET` request. The following table shows the format to use to get this information using the FHIR Service Base URL and its equivalent base URL in the Cloud Healthcare API:

FHIR Service Base URL| Cloud Healthcare API equivalent URL  
---|---  
`http(s)://server/path/Patient/PATIENT_ID` | `https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID`  
  
## FHIR conformance

For more information on the FHIR DSTU2, STU3, and R4 implementations in the Cloud Healthcare API, see the [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir).

## Integrating with OMOP

OMOP Common Data Model (OMOP CDM) is a standard developed by Observational Health Data Sciences and Informatics (OHDSI). It is primarily used for observational clinical data. The OHDSI tool suite can assist common analytics use cases such as cohort definition, cohort generation, and population effect estimation. It is a commonly used data model in genomics and pharmaceutical research due to its expansive terminology and genetics support.

See the following resources for more details about OMOP:

  * [OMOP common data model](https://www.ohdsi.org/data-standardization/the-common-data-model/)
  * [OMOP common data model and standardized vocabularies](https://www.ohdsi.org/2019-tutorials-omop-common-data-model-and-standardized-vocabularies/)
  * [Getting started with OHDSI](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:getting_started)



By integrating FHIR and OMOP, clinical data from EHRs and other sources in the FHIR format can be used as research data in the OMOP standard. Specific fields and data elements in OMOP can also be integrated into existing data in FHIR.

You can use the [open-sourced Cloud Healthcare API Data Harmonization mapping engine](https://github.com/GoogleCloudPlatform/healthcare-data-harmonization) to perform the following tasks:

  * Harmonizing data to the OMOP CDM and others.
  * Configuring data mapping for FHIR-to-OMOP data conversion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
