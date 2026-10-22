---
url: https://docs.cloud.google.com/healthcare-api/docs/introduction/
title: Overview of the Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:40.868501+00:00
---

# Overview of the Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/introduction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Overview of the Cloud Healthcare API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Healthcare API provides industry-standard protocols and formats for ingesting, storing, analyzing, and integrating healthcare data with cloud-based applications. The API supports the following applications:

  * Healthcare machine learning applications
  * Data-level integration of healthcare systems
  * Secure storage and retrieval of healthcare and life science data, including electronic protected health information (ePHI) and other forms of PII



For many applications, the Cloud Healthcare API can provide a cloud-based alternative to on-premises stacks implementing the following standards:

  * Digital Imaging and Communications in Medicine (DICOM)
  * Fast Healthcare Interoperability Resources (FHIR) DSTU2, STU3, and R4 standards
  * Health Level Seven Version 2.x (HL7v2)



The Cloud Healthcare API simplifies data integration with existing systems and allows developers to focus on differentiating features, such as UX and intelligence.

## Data model

The API consists of three modalities that implement individual industry-wide standards:

  * Medical imaging data in the Digital Imaging and Communications in Medicine (DICOM) format
  * Clinical event messages in the Health Level Seven Version 2.x (HL7v2) format
  * Clinical resources in the Fast Healthcare Interoperability Resources (FHIR) format



Each modality has different structural and processing characteristics, but they are all backed by a standards-compliant data store that provides read, write, search, and other operations on the data.

The data stores corresponding to each modality reside in datasets, which are containers in your Google Cloud (Google Cloud) project that hold modality-specific healthcare data.

For more information, see [Projects, datasets, and data stores](https://docs.cloud.google.com/healthcare-api/docs/concepts/projects-datasets-data-stores).

## Features of the Cloud Healthcare API

This section describes the features that make up the Cloud Healthcare API and the primary purpose of each feature.

### Standards conformance

The Cloud Healthcare API implements a REST API for multiple healthcare modalities. For example:

  * The FHIR portion of the REST API conforms to the DSTU2, STU3, and R4 FHIR specifications.
  * The DICOM portion of the REST API conforms to DICOMweb, a web-based standard for exchanging medical images.



### Compliance with privacy regulations

The Cloud Healthcare API is covered by Google Cloud's security, privacy, and compliance assessments/certifications for industry standards, such as:

  * ISO 27001
  * ISO 27017
  * ISO 27018
  * PCI DSS



The Cloud Healthcare API is a covered service under the Google Cloud HIPAA BAA, which means that customers can use it with electronic protected health information (ePHI), with appropriate configuration. The Cloud Healthcare API has been developed according to Google's [security](https://docs.cloud.google.com/security/overview/whitepaper) and [privacy](https://docs.cloud.google.com/privacy) practices.

Google Cloud provides detailed guidance regarding [compliance with HIPAA in the US, the PIPEDA in Canada, and other global privacy standards](https://docs.cloud.google.com/security/compliance).

### Data location control

Data location is a core component of the API. You can select the storage location for each dataset from a list of currently available locations that correspond to distinct geographic areas aligned with Google Cloud's regional structure. Data stores exist in the same region as their parent dataset.

For more information, see [Regions](https://docs.cloud.google.com/healthcare-api/docs/concepts/regions).

### Security

The Cloud Healthcare API security model is based on Google's [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) system. IAM's fine-grained permissions give you complete control over what can be done with healthcare data, and by whom. To provide comprehensive threat detection and traffic management capabilities, there are also implementations of open source proxies for the [Apigee API Management system](https://apigee.com/). You can use these implementations to securely expose sensitive ePHI with patient and provider applications.

### Bulk import and export

The Cloud Healthcare API's DICOM and FHIR modalities support bulk import and export of data, making it easier to transfer data to and from [Cloud Storage](https://docs.cloud.google.com/storage).

You can also export FHIR resources and DICOM store metadata to [BigQuery](https://docs.cloud.google.com/bigquery). BigQuery lets you perform advanced data discovery and analytics workloads on large datasets.

For more information, see [Importing and exporting DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export) and [Exporting DICOM metadata](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery).

### Data de-identification

The Cloud Healthcare API supports de-identifying data at the dataset, FHIR store, and DICOM store level. De-identification using the Cloud Healthcare API simplifies the process of redacting sensitive information for research and other purposes. For more information, see [Data de-identification](https://docs.cloud.google.com/healthcare-api/docs/concepts/de-identification).

### Auditability

You can use [Cloud Logging](https://docs.cloud.google.com/logging) to audit administrative and data access requests.

For more information, see [Access control](https://docs.cloud.google.com/healthcare-api/docs/access-control) and [Viewing Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).

### High performance

Using Google Cloud's high-performance technology, the Cloud Healthcare API can scale to thousands of requests per second, even when accessing large volumes of data.

### High availability

Availability for mission-critical scenarios is made possible through Google Cloud's robust and highly redundant infrastructure.

### Durability

Cloud Healthcare API is designed for 99.999999999% annual durability. Durability is achieved by storing data across multiple disks located in different power and network failure domains.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
