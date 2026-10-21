---
url: https://docs.cloud.google.com/document-warehouse/docs/
title: Document AI Warehouse overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:32:12.379701+00:00
---

# Document AI Warehouse overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/document-warehouse/docs/overview)



Send feedback 

#  Document AI Warehouse overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

## Conceptual Overview

Document AI Warehouse is an integrated, cloud-based platform to store, search, organize, govern and analyze documents and their structured metadata (called Properties). Documents include structured (e.g. forms, invoices) and unstructured (e.g. contracts, research papers) and their Properties (metadata) includes AI-extracted data from documents and manually or AI-assigned tags (for example, account number, loan ID, document type).

## Key Benefits and Features

Document AI Warehouse offers several advantages over legacy repositories. Following are some features and benefits:

  * **API-first: single integrated API** to manage documents and their properties (extracted or tagged metadata), that integrates into your workflows and applications.
  * **Metadata Management** : to manage extracted and tagged metadata.
  * **Governance** : integrated with IAM and corporate directories 
    * Fine-grained Access Control (permissions) at the document and folder levels can be assigned to users and groups to view, edit, manage (share, delete) documents.
    * Document AI Warehouse is integrated with IAM (Cloud Identity), so that users and groups can be provisioned into Cloud Identity
    * Users/groups can also be federated/synced into Cloud Identity from an enterprise LDAP / identity provider such Azure AD, Active Directory and Keycloak.
  * **Search** : the product supports rich semantic search, including the following features: 
    * Full-text search
    * Filtering search results by Properties (date, numeric, enum, text). Filters can be combined with `AND` and `OR` operators
    * Semantic search - support common synonyms and misspellings, stemmings. Quotes (" ") may be used in the query to specify exact matching keywords
    * Custom synonyms - industry-specific or company-specific terms, for example.
    * Search within a root-folder hierarchy
    * Operators for search keywords: `""` exact match, `|` or, `+` and, `-` exclude
  * **Organization** : **Flexible Folder management**
    * Documents can be cataloged into one or more folders, based on application (for example, an ID card is placed in a KYC folder, Loan folder, Bank Account folder), without replicating the document.
    * These folders have their own Properties and Access Control, independent from Document properties and access control.
    * The folders can be nested in one or more hierarchies [for example, AllLoans->State->Branch->Loans or LoanTypes->Loans].
    * Users can search for documents within a folder hierarchy e.g. search within AllLoans->State
  * **UI** * \- the product includes Web-accessible UI with the following features: 
    * Doc Explorer: search documents, filter search results, select documents to bulk-update properties or delete
    * Doc Viewer: view documents, view/update its properties,assign ACLs, add to folders
    * Upload: upload documents and run them through a DocAI** extractor (either OCR or a supported specialized parser such as Invoice DocAI).
    * Folder Explorer: add documents to one or more folders, explore folder hierarchy.
    * Embeddable UI: the Doc Explorer and the Doc Viewer (for PDFs) components can be integrated in customer's applications
  * **Connectors** *** to common on-premise and cloud repositories: We provide a Cloud Storage to Document AI Warehouse connector (as a separate template based on [Google Workflows](https://cloud.google.com/workflows)) that can be customized/extended to other repositories. We also work with partners to provide out-of-box connectors to repositories such as Sharepoint, Amazon S3, IBM FileNet and others, to ingest and index documents.
  * **Migrate vs Federate flexibility** : The product supports a flexible architecture such that your document content can be migrated to Document AI Warehouse or stay-in-place if there are constraints in migrating content (we simply index the content and metadata)
  * **Integrated with Document Workflows** \- this integrates with Google Workflows and other document processing workflows by supporting: 
    * **Properties** \- that represent the state of a document in a workflow and APIs that workflows can use to update the state of documents
    * **Doc Explorer interface** \- to track the progress of documents through a workflow pipeline, enabling a human to inspect, manage failures and stalled documents in the workflow pipeline.
    * **Conditional Notifications** \- where documents meeting a certain conditions can trigger/notify a workflow via a Pub/Sub topic or a Web API call: for example, Trigger: OnUpdate; Condition: (DocType=Invoice and TotalAmount>$1000) -> send Pub/Sub Notification
  * **Policy Management and Compliance Enforcement** : conditional notifications and scheduled notifications can be used to trigger workflows that enforce policies (for example, records management, retention and disposition, legal holds) on specific documents in Document AI Warehouse.
  * **Files supported** \- Text PDFs, Images (scanned PDFs, TIFF files, JPEG files), Office (DOCX, PPTX, XLSX) files - run through OCR and indexed. 
    * Note - while the product focus is documents, it is also used to manage associated images (e.g. in verticals such as Insurance, Engg, Construction, Research, etc).
  * **Integrated with DocAI** : Document AI Warehouse is integrated with Document AI processors at several levels:

    * **Document AI processing in UI** : Document AI Warehouse UI enables users to upload either scanned PDFs/TIFFs or special document types, both of which are automatically extracted by Document AI OCR or specialized processors respectively before the document is indexed into Document AI Warehouse.
    * **Managing batch Document AI pipelines** ***: Document AI Warehouse integrates with Workflows to provide templates that process batch pipelines of documents through Document AI extraction and classification. This is non-trivial because it entails long-running (LRO) operations and asynchronous API calls that need to be managed for failures and retries. The Workflows template orchestrates such pipelines. Document AI Warehouse UI may be used to search and track the document flow through such pipelines, visualize the Document AI output for failures in each step of the pipeline and take action on stalled/failed documents.



*The UI is in Preview and expected to go GA soon.

**OCR and other document extractors are available in Document AI products but not included in Document AI Warehouse.

***These features are not part of Document AI Warehouse. These features are enabled by external open source components and scripts that customers can deploy or customize and are not implemented within Document AI Warehouse. 

## Disclaimers and Known Limitations

For more information about Disclaimers and Known Limitations, see [Disclaimers and Known Limitations](https://docs.cloud.google.com/document-warehouse/docs/disclaimers-limitations)

## Terminology

Following are terms used in Document AI Warehouse.

**Terms, Concepts** | **Definition, Examples**  
---|---  
Document  | A record in Document AI Warehouse that users can search, manage, and enforce access control on. It comprises the raw document and some associated metadata.  [Images stored in Document AI Warehouse are also referred to as "Documents"]   
Raw Document [Content]  | The raw content file (pdf/image/binary/blob) of the Document.   
Schema [Document Type]  | Each document is of a certain document type and is specified by a schema. E.g. an Invoice contains the following schema: Supplier Name, Vendor Name, Invoice Amount, etc.   
Property [Metadata]  | Fields of the Document Schema that may either be extracted from the document or enriched (labeled) by users. Currently Metadata includes the following types: Free Text values, Enum, Numeric, Date, Map (a JSON hierarchy of key-value pairs). We plan to support Boolean, Money, and other types going forward.   
Doc extractors (DocAI and others)  | Documents may be extracted by an AI pipeline, so that the extractions can be ingested and managed in Document AI Warehouse (as Metadata) along with the Raw Document. The extraction can be done by

  * Document AI Specialized parsers (for Procurement forms, Lending forms, others) 
  * OCR, AutoML, Forms parser (for images such as TIFF/PNG/etc.) 
  * Other custom models 
  * Text extracting tools for specialized document formats such as PDFs, Office documents and others.  Note that Document AI Warehouse can work with any extraction pipeline that calls Document AI Warehouse APIs to ingest/update documents.

  
Folders  | A folder is a virtual collection of documents (virtual because the same document can be contained in one or more folders). It has a "Document Type/Schema" and contains metadata and Access Control Lists just like documents.  A user needs Edit permission to the Folder and View permission to the Document), in order to add a Document to a Folder   
Links  | Links are used to **add documents to folders** or to **link related documents** together. Links do not have a "Link Type"   
Related Documents  | Documents can be related by directional links from one document to another.   
Link Permissions  | A user needs Edit permission to the Link-from object (e.g. Folder) and View permission to the Link-To object (e.g. Document), in order to add a Document to a Folder   
Policy  | A policy evaluated when a document/folder is created/updated, and is used to validate or update document metadata, ACLs or add/move/remove docs from folders. A policy comprises:

  * A Trigger, for example, upon DocUpdate/DocCreate 
  * Condition, for example, Invoice.Amount <$1000 
  * Action, for example, Update Doc Metadata, Return Condition Evaluation, Add Doc to Folder, etc.  A policy is typically associated with a Document Type.  It is expressed in a low-code Common Expression Language (JSON format, specified later)

  
Notification Policy  | Is a special type of policy where the Action is publishing a message to a Pub/Sub} Topic when a certain condition is met. Consuming applications / workflows may consume the message to trigger actions on the documents or other parts of a business workflow.   
Policy Engine, Policy APIs  | Engine: The server that evaluates policies and takes actions  API: Admin API used to create/update/read/delete policies.   
Faceted Search  | A Facet is a metadata filter used in a search query. For example, search for Bank Statements from "Month = March 2021" and "Branch State = CA" filters the Search results by these 2 facets.

  * Facet is typically an enumerated field.. We will support Date and Numeric facets in future releases. 
  * Facets for a Document type are specified in the Document Schema by Admins (via Admin API)

  
Semantic Search  | Semantic search supports synonyms or "semantically related" terms in the search query. E.g. "Driver license" returns "driver permit".   
Search Histogram  | Histogram is a search API feature that returns the distribution (counts) of search results by facet. For example, the Search results for Driver License returns the histogram "CA 500, NV 150, …"   
Universal Access vs Doc-level Access Control  | Two access modes are supported in Document AI Warehouse for each project

  1. Universal access - any user can access any document in the project. The API is access-controlled to user accounts or service accounts but no document-level permissions 
  2. Doc-level ACL - users are granted document-level permissions. Each document has R/U/D permissions assigned to users/groups.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
