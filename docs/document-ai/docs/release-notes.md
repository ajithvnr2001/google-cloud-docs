---
url: https://docs.cloud.google.com/document-ai/docs/release-notes/
title: Document AI release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:41.016625+00:00
---

# Document AI release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/document-ai/docs/resources)



Send feedback 

#  Document AI release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Document AI. We recommend that Document AI developers periodically check this list for any new announcements.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/duai-release-notes.xml) directly. 

## September 21, 2026

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model `pretrained-foundation-model-v3.1-lite-2026-07-15` powered by Gemini 3.1 Flash Lite LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version supports fine-tuning and is serving multi-region locations in the US and EU.

CMEK is not fully supported in all regions, support requires being allowlisted. Contact your Google Cloud account team for more information.

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/custom-based-extraction) page.

v1 & v1beta3

Feature

[Gemini layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) model `pretrained-layout-parser-v3.1-lite-2026-08-11`is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## July 17, 2026

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model `pretrained-foundation-model-v3.5-2026-05-26` powered by Gemini 3.5 Flash LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version has ML processing capabilities in the US and EU.

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/custom-based-extraction) page.

## June 04, 2026

v1 & v1beta3

Feature

Custom extractor offers document validation and correction in [Preview](https://cloud.google.com/products/#product-launch-stages).

This feature allows you to enhance extraction accuracy with validation rules and document data using Common Expression Language (CEL) dialect.

For more information, see [CEL dialect for document validation](https://docs.cloud.google.com/document-ai/docs/ce-common-expression-validation).

## May 27, 2026

v1 & v1beta3

Feature

[Layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) image and table annotations is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

Layout parser can identify if there are images or tables in parsed documents. When found, images and tables are annotated as a descriptive block of text with the information depicted in the image and table.

## March 31, 2026

v1beta3

Feature

Upgrading fine tuned [custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) processors is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

The feature allows you to fine tune a new processor version with a newer base version, while keeping the configurations of the previously fine-tuned processor version selected. This is available through the UI in the **Deploy & use** tab in the console.

This is currently supported for upgrading `pretrained-foundation-model-v1.4-2025-02-05` to `pretrained-foundation-model-v1.5-2025-05-05`.

For more information, see [training overview](https://docs.cloud.google.com/document-ai/docs/training-overview#upgrade-ui).

## March 27, 2026

v1 & v1beta3

Feature

[Custom splitter](https://docs.cloud.google.com/document-ai/docs/custom-splitter) model `pretrained-splitter-v1.5-2025-07-14` is available in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## March 23, 2026

v1 & v1beta3

Feature

[Custom classifier](https://docs.cloud.google.com/document-ai/docs/custom-classifier) models `pretrained-classifier-v1.6-2026-03-09` and `pretrained-classifier-v1.6-pro-2026-03-09` are available in [Preview](https://cloud.google.com/products/#product-launch-stages).

v1 & v1beta3

Feature

[Custom splitter](https://docs.cloud.google.com/document-ai/docs/custom-splitter) models `pretrained-splitter-v1.6-2026-03-09` and `pretrained-splitter-v1.6-pro-2026-03-09` are available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## March 03, 2026

v1 & v1beta3

Feature

Custom classifier model `pretrained-classifier-v1.5-2025-08-05` is available as [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

For more information about available models, see the [custom classifier](https://docs.cloud.google.com/document-ai/docs/custom-classifier) page.

## February 17, 2026

v1 & v1beta3

Deprecated

Document AI legacy processors will be discontinued on **June 30, 2026**. To preempt the risk of service failure while using legacy processors, we recommend transitioning to more stable, higher-quality processors.

The affected versions are:

Type | Version  
---|---  
Identity parsers | `pretrained-us-passport-v1.0-2021-06-14`  
`pretrained-fr-driver-license-v1.0-2021-06-14`  
Tax and finance parsers  | `pretrained-1099misc-v1.1-2021-12-10`  
`pretrained-1099nec-v1.0-2021-08-11`  
`pretrained-1099r-v2.0-2022-07-25`  
`pretrained-1099int-v1.1-2021-12-10`  
`pretrained-ssa1099-v1.0-2021-08-09`  
`pretrained-1099g-v1.0-2021-05-27`  
`pretrained-1099g-v1.1-2021-12-10`  
`pretrained-1120-v3.0-2022-04-26`  
`pretrained-w9-v1.0-2020-09-25`  
`pretrained-w9-v1.1-2021-12-10`  
`pretrained-w9-v1.2-2022-01-27`  
`pretrained-w9-v2.0-2022-06-23`  
Mortage and banking parsers | `pretrained-mortgage-statement-v1.0-2021-10-17`  
Procurement  | `pretrained-utility-v1.1-2021-04-09`  
`pretrained-utility-v1.2-2022-12-15`  
Splitting  | `pretrained-procurement-splitter-v1.1-2021-04-09`  
`pretrained-procurement-splitter-v1.2-2022-08-19`  
`pretrained-lending-document-split-v1.0-2021-12-08`  
`pretrained-lending-document-split-v2.0-2021-12-09`  
Summary | `pretrained-foundation-model-v1.0-2023-08-22`  
  
To ensure uninterrupted service and benefit from improved extraction quality, we recommend you migrate to the following later versions before **June 30, 2026** : 

  * **Enterprise Document OCR:** Migrate to [`pretrained-ocr-v2.1-2024-08-07`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr).

  * **Expense parser:** Migrate to [`pretrained-expense-v1.3.2-2024-09-11`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser).

  * **Custom classifier:** Migrate to [`pretrained-classifier-v1.5-2025-08-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_CUSTOM_CLASSIFICATION_PROCESSOR).

  * **Custom splitter:** Migrate to [`pretrained-splitter-v1.5-2025-07-14`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_CUSTOM_SPLITTING_PROCESSOR).

  * **Invoice parser:** Migrate to [`pretrained-invoice-v2.0-2023-12-06`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor).

  * **Pay slip parser:** Migrate to [`pretrained-paystub-v3.0-2023-12-06`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser).

  * **Bank statement parser:** Migrate to [`pretrained-bankstatement-v5.0-2023-12-06`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser).




To learn more about the migration process, refer to [Manage processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).

If you have any questions or require assistance, contact us at [Google Cloud support](https://docs.cloud.google.com/support-hub).

## February 16, 2026

v1 & v1beta3

Feature

The [layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) web interface is in [Preview](https://cloud.google.com/products/#product-launch-stages).

It supports a document view display for processed PDF files and supports visualizing the document's parsed JSON, block layout, and image or table annotation data in a user-friendly interface. Bounding box support only exists for version processor `pretrained-layout-parser-v1.0-2024-06-03`.

It also supports modifying the input layout config to allow for configuring the table and image annotation feature directly from the interface.

## February 09, 2026

v1 & v1beta3

Feature

[Layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) model `pretrained-layout-parser-v1.6-2026-01-13` powered by Gemini 3 Flash LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version has ML processing capabilities in the US and EU.

**Note:** This processor version uses the Vertex AI Gemini global endpoint and is not compliant with Data Residency (DMZ) standards. For example, requests in US and EU endpoints might route to anywhere globally.

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/custom-based-extraction) page.

## January 27, 2026

v1 & v1beta3

Feature

[Layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) model `pretrained-layout-parser-v1.6-pro-2025-12-01` powered by Gemini 3 Pro LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version has ML processing capabilities in the US and EU.

**Note:** This processor version uses the Vertex AI Gemini global endpoint and is not compliant with Data Residency (DMZ) standards. For example, requests in US and EU endpoints might route to anywhere globally.

For more information about available models, see the [layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) page.

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model `pretrained-foundation-model-v1.6-pro-2025-12-01` powered by Gemini 3 Pro LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version has ML processing capabilities in the US and EU.

**Note:** This processor version uses the Vertex AI Gemini global endpoint and is not compliant with Data Residency (DMZ) standards. For example, requests in US and EU endpoints might route to anywhere globally.

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) page.

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model `pretrained-foundation-model-v1.6-2026-01-13` powered by Gemini 3 Flash LLM is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

This processor version has ML processing capabilities in the US and EU.

**Note:** This processor version uses the Vertex AI Gemini global endpoint and is not compliant with Data Residency (DMZ) standards. For example, requests in US and EU endpoints might route to anywhere globally.

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/custom-based-extraction) page.

## January 12, 2026

v1 & v1beta3

Feature

Document AI is introducing document-level prompting for custom document processors. This feature allows you to provide an overall description of the document to inject deep business knowledge into the model, leading to improved extraction quality.

Document-level prompting offers improved accuracy by giving the model necessary context for extraction at the document level. This allows for easily supplied general information, such as geographical limitations (for example, _all the address fields are located in the USA_), to guide the model.

For more details, refer to the documentation on custom extractor mechanisms and [document-level prompting](https://docs.cloud.google.com/document-ai/docs/ce-mechanisms#document-level-prompts).

## December 15, 2025

v1 & v1beta3

Feature

A monitoring dashboard web interface is available in [Preview](https://cloud.google.com/products/#product-launch-stages) to monitor at the project and processor level.

You can monitor a number of metrics, such as number of successfully processed pages and sync processing latency, across fields like `location`, `processor_type`, and `processor_id` over time. 

For more information, see [monitoring dashboard](https://docs.cloud.google.com/document-ai/docs/evaluate#monitoring_dashboard).

## November 12, 2025

v1beta3

Feature

Automated schema extraction for custom extractor processors is in [Preview](https://cloud.google.com/products/#product-launch-stages).

This feature allows you to automatically extract a document schema from a test document you supply. Then, you can approve or decline the schema and edit it manually. This saves time and effort when defining the document schema for your custom processor and allows you to focus on refining the schema.

When creating a custom extractor processor, find the **Generate from document** option in the **Get started** tab of the Google Cloud console.

## November 07, 2025

v1 & v1beta3

Feature

[Gemini layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) is in [Preview](https://cloud.google.com/products/#product-launch-stages). The Gemini layout parser gives better layout quality on table recognition, reading order and text recognition on PDF files. You can enable the feature by default by selecting layout parser processor version `pretrained-layout-parser-v1.4-2024-08-25`, `pretrained-layout-parser-v1.5-2025-08-25` or `pretrained-layout-parser-v1.5-pro-2025-08-25` for your processor.

## November 04, 2025

v1 & v1beta3

Feature

Layout parser support for DOCX, PPTX, XLSX, and XLSM file types in Document AI is in General Availability [(GA)](https://cloud.google.com/products/#product-launch-stages). It makes content like paragraphs, tables, lists, and structural elements like headings, page headers, and footers easily accessible. It also creates context-aware chunks that facilitate information retrieval in a range of generative AI and discovery applications.

For more information, see [Process documents with Layout Parser](https://cloud.google.com/document-ai/docs/layout-parse-chunk).

## October 31, 2025

v1 & v1beta3

Feature

[Custom splitter](https://docs.cloud.google.com/document-ai/docs/custom-splitter) model `pretrained-splitter-v1.5-2025-07-14` with zero-shot splitting, classification and confidence scores is available as Release Candidate ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## October 17, 2025

v1 & v1beta3

Feature

[Layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) lets you parse images and tables as annotations in [Preview](https://cloud.google.com/products/#product-launch-stages).

Layout parser can identify if there are images or tables in parsed documents. When found, images and tables are annotated as a descriptive block of text with the information depicted in the image and table.

## October 06, 2025

v1 & v1beta3

Announcement

Capacity reservation is available for Document AI in [Preview](https://cloud.google.com/products/#product-launch-stages). This lets you grant capacity to selected processors and maintain a steady real-time, high-volume processing flow for document processing requests. 

For the necessary steps, read the [Make a capacity reservation request section](https://cloud.google.com/document-ai/capacity-reservation) of "Quotas".

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model `pretrained-foundation-model-v1.5.1-2025-08-07` with improved adaptive few-shot learning is available as Release Candidate ([Preview](https://cloud.google.com/products/#product-launch-stages)).

v1 & v1beta3

Feature

Support for confidence scores in [Custom classifier](https://docs.cloud.google.com/document-ai/docs/custom-classifier) models `pretrained-foundation-model-v1.4-2025-05-16` and `pretrained-classifier-v1.5-2025-08-05` is in [Preview](https://cloud.google.com/products/#product-launch-stages).

For best performance, use them with fine-tuned models.

## September 23, 2025

v1 & v1beta3

Feature

[Custom classifier](https://docs.cloud.google.com/document-ai/docs/custom-classifier) model [`pretrained-classifier-v1.5-2025-08-05`](https://docs.cloud.google.com/document-ai/docs/custom-classifier#models) powered by Gemini 2.5 Flash is in [Preview](https://cloud.google.com/products/#product-launch-stages). It has ML processing available for US and EU regions, a maximum page limit of [30](https://docs.cloud.google.com/document-ai/limits#classification_processors) pages, and processing requests of [120](https://docs.cloud.google.com/document-ai/quotas#service_tiers) pages per minute.

Unlike the prior custom classifier, which used classical machine learning, this version features a new platform. It accommodates:

  * High accuracy immediately, based on the document classes you define.
  * Few-shot learning to further improve accuracy.
  * Use of descriptions when labeling for more context and insight for document classes.
  * More accurate results with the same training dataset on the fine-tuned generative AI model, compared to the trained version.
  * Autolabeling documents for fine-tuning and evaluation.
  * Generative AI to fine-tune and heighten accuracy. 



For more information on processor versions, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).

## September 10, 2025

v1 & v1beta3

Deprecated

Custom Extractor version [`pretrained-foundation-model-v1.4-2025-02-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) will no longer be accessible on **February 5, 2026**. 

To avoid service disruptions, migrate to a later version such as `pretrained-foundation-model-v1.5-2025-05-05` or `pretrained-foundation-model-v1.5-pro-2025-06-20`. To learn more about the migration process, refer to [Manage processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).

## September 09, 2025

v1beta3 & v1

Announcement

Document AI supports [two service tiers](https://docs.cloud.google.com/document-ai/quotas#service_tiers) and associated quotas: provisioned and best effort tiers.

The base is the provisioned tier quota, which provides 120 pages per minute for Gemini 2.0 and 2.5 Flash LLM and 30 pages per minute for Gemini 2.5 Pro LLM. 

If you require more volume, best effort tier quota provides 120 pages per minute for Gemini 2.0 2.5 Flash and 60 pages per minute for Gemini 2.5 Pro. It's only used when the provisioned quota has been exhausted. This applies to the `BestEffortOnlineProcessDocumentPagesPerMinutePerProjectUS` and `EU` quotas and, in the console, `best_effort_online_process_document_pages_us` and `eu`.

Best effort can get up to 240 pages per minute for [custom data extractor models](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) v1.4 and v1.5 with a quota increase request (QIR). You can make a QIR by contacting your sales team representative.

There is no service level agreement [(SLA)](https://cloud.google.com/document-ai/sla) for best effort tier.

## September 03, 2025

v1beta3 & v1

Feature

Custom extractor model `pretrained-foundation-model-v1.5-pro-2025-06-20` is available as General Availability ([GA](https://cloud.google.com/products/#product-launch-stages)).

For more information about available models, see the [custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) page.

## August 29, 2025

v1

Feature

Derived entity and signature detection are now supported in [custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) models `pretrained-foundation-model-v1.4-2025-02-05` as General Availability [(GA)](https://cloud.google.com/products/#product-launch-stages) and in `pretrained-foundation-model-v1.5-2025-05-05`, as well as `pretrained-foundation-model-v1.5-pro-2025-06-20` as Preview.

Signature detection lets you identify handwritten signatures by using visual cues in the document. Derived entity detection lets you deduce entities by inference without requiring the value to be explicitly present in the text. You can use this feature to deduce the country in an address, counting items in a table, or detecting if an ID is fake.

These can be enabled in the console when creating labels or by using the [`DocumentSchema.EntityType`](https://docs.cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#entitytype) resource in the API.

For more information, read [Custom extractor with derived fields](https://docs.cloud.google.com/document-ai/docs/ce-derived-signature) and [choose label attributes](https://docs.cloud.google.com/document-ai/docs/create-dataset#choose_label_attributes).

## July 22, 2025

v1 & v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model [`pretrained-foundation-model-v1.5-pro-2025-06-20`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) powered by Gemini 2.5 Pro is in [Preview](https://cloud.google.com/products/#product-launch-stages). It has ML processing available for US and EU regions, a maximum page limit of [30](https://docs.cloud.google.com/document-ai/limits#classification_processors) pages, and processing requests of [30](https://docs.cloud.google.com/document-ai/quotas#service_tiers) pages per minute.

For more information, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions#import).

## July 04, 2025

v1 & v1beta3

Feature

Document AI [VPC service controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) (VPC-SC) integration now supports identity groups.

For more information on setting up VPC-SC identity groups, read [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).

v1 & v1beta3

Feature

Document AI now supports [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) (IAM) deny policies. These policies allow you to define deny rules that prevent certain principals from using certain permissions to access Google Cloud resources, regardless of the roles they're granted.

For more information, read [Deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) overview and [Document AI security and compliance](https://docs.cloud.google.com/document-ai/docs/security).

## July 03, 2025

v1 & v1beta3

Feature

The Document AI CDE processor now supports merging the child entities of nested entities that extend across several pages. This is supported in custom extractor model [`pretrained-foundation-model-v1.5-2025-05-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde).

This change is automatic in all processors.

For customers with existing v1.5 processors, to make use of this feature, you must relabel the nested entities in different pages. 

To learn more about the labeling process, refer to [Label documents](https://docs.cloud.google.com/document-ai/docs/label-documents).

## June 30, 2025

v1 & v1beta3

Feature

[Custom Extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai) model [`pretrained-foundation-model-v1.5-2025-05-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) is in General Availability ([GA](https://cloud.google.com/products/#product-launch-stages)) and has fine-tuning available for the US and EU.

From version v1.4 and later, we will use a new quota for online processing called [`Number of online process document pages per minute per processor type and model version`](https://docs.cloud.google.com/document-ai/quotas#quotas_list). This quota will be enforced at a per-page and per-foundation model level. There will be no change to the batch processing quota.

These can be enabled in the console when creating labels and by using the [`DocumentSchema.EntityType`](https://docs.cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#entitytype).

For more information, read [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions#import).

## June 19, 2025

v1 & v1beta3

Feature

We've increased the maximum file size for [online processing](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) requests from 20 MB to 40 MB. This applies to all types of processors.

For more information, see the Document AI [limits](https://docs.cloud.google.com/document-ai/limits#content_limits) page.

## May 19, 2025

v1 & v1beta3

Feature

Cross-regions importing of fine-tuned models is now supported for processor versions based on Gemini 1.5 and later, such as [custom extractors](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models) `pretrained-foundation-model-v1.2-2024-05-10` and later.

For more information, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions#import).

## May 05, 2025

v1 & v1beta3

Feature

Custom extractor model `pretrained-foundation-model-v1.5-2025-04-25` powered by Gemini 2.5 Flash LLM is available as Public Preview in US regions. The custom extractor model supports a quota of up to 15 pages per minute for online process requests. 

For more information about available models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

## April 08, 2025

v1

Announcement

Previous Custom Extractor versions `pretrained-foundation-model-v1.0-2023-08-22` and `pretrained-foundation-model-v1.1-2024-03-12` will be deprecated on **April 9, 2025**. To ensure uninterrupted service, prediction traffic to these versions, including any fine-tuned variants, will be automatically redirected to the latest version, [`pretrained-foundation-model-v1.4-2025-02-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde).

For guidance on how to fine-tune a new version, refer to the [fine tuning documentation](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#fine-tuning).

## April 02, 2025

v1 & v1beta3

Feature

All processors can now extend the Maximum page limit for online and synchronous requests up to 30 pages.

To do so, enable `imageless_mode` in [ProcessRequest](https://docs.cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#processrequest).

For [Custom Extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai), you will need to first request to be allowlisted for this feature by filling out the form [Allowlist Request for 30 Page limit in CDE](https://docs.google.com/forms/d/e/1FAIpQLSc_-HpG6nqVHeLLVPa1HQETD1V_Bi7vUxSnrL2zY7TbpWUfJg/viewform?usp=header).

## March 24, 2025

v1

Deprecated

As we launch Custom Extractor version `pretrained-foundation-model-v1.4-2025-02-05` in GA with fine tuning (in [Preview](https://cloud.google.com/products/#product-launch-stages)), these versions will no longer be accessible effective **September 24, 2025** :

  * `pretrained-foundation-model-v1.2-2024-05-10`
  * `pretrained-foundation-model-v1.3-2024-08-31`



To avoid service disruptions, migrate to a later version, such as [`pretrained-foundation-model-v1.4-2025-02-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde). To learn more about the migration process, refer to our [Manage processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions) documentation.

Customers and projects can access `pretrained-foundation-model-v1.2-2024-05-10` and `pretrained-foundation-model-v1.3-2024-08-31` until September 24, 2025. This includes the ability to create tuning jobs and access fine-tuned processor versions.

Starting **March 24, 2025** :

  * Newly created processor versions using `pretrained-foundation-model-v1.2-2024-05-10` can only be used for batch processing.
  * Newly created processor versions using `pretrained-foundation-model-v1.2-2024-05-10 and pretrained-foundation-model-v1.3-2024-08-31` will have a quota limit of 120 pages per minute.



This update requires planning, but if you have questions or need assistance, contact [Google Cloud support](https://docs.cloud.google.com/support/docs).

## March 19, 2025

v1

Feature

Custom Extractor model [`pretrained-foundation-model-v1.4-2025-02-05`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) is in General Availability (GA), and has fine-tuning available in [Preview](https://cloud.google.com/products/#product-launch-stages) for the US and EU.

From version v1.4 and later, we will use a new quota for online processing called [`Number of online process document pages per minute per processor_type_and_model_version`](https://docs.cloud.google.com/document-ai/quotas#quotas_list). This quota will be enforced at a per-page and per-foundation model level. There will be no change to the batch processing quota.

## February 14, 2025

v1

Feature

Custom extractor model `pretrained-foundation-model-v1.4-2025-02-05` powered by Gemini 2.0 Flash LLM is available as Public Preview in US and EU regions with improved accuracy. The Custom Extractor Model supports a quota of up to 120 pages per minute for online process requests.

For more information about available models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

## February 03, 2025

v1

Feature

Model `pretrained-ocr-v2.1-2024-08-07` has General Availability (GA) in the US and EU.

For more information about available models, see [Enterprise Document OCR](https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr) and [Regional and multi-regional support availability](https://docs.cloud.google.com/document-ai/docs/regions).

v1

Feature

Model `pretrained-ocr-v2.1.1-2025-01-31` is available as a Release Candidate in the regions `asia-south1`, `australia-southeast1`, `europe-west2`, `europe-west3` and `northamerica-northeast1`.

For more information about available models, see [Enterprise Document OCR](https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr).

## January 27, 2025

v1.3

Feature

For processor versions `pretrained-foundation-model-v1.2-2024-05-10` and `pretrained-foundation-model-v1.3-2024-08-31` [custom extractors](https://docs.cloud.google.com/document-ai/docs/custom-extractor-overview), [customer-managed encryption keys](https://docs.cloud.google.com/document-ai/docs/cmek) (CMEK) is now supported when importing fine-tuned processor versions.

For more information, see [Import processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions#import).

## January 23, 2025

v1

Breaking

Effective **January 27, 2025** , new and existing processors require explicit `storage.objects.get` permissions to access Google Cloud Storage buckets for training dataset imports and offline/batch processing.

You will need to review your use of training dataset imports and offline/batch processing to verify that the users of these APIs have appropriate permissions to access Google Cloud Storage buckets.

Ensure that users of these APIs have been granted one of the [predefined](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) or [legacy](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#legacy-roles) Cloud Storage roles that includes the `storage.objects.get` permission (such as [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)). You can assign these roles in the Permissions tab of the relevant Cloud Storage bucket.

We understand that this update requires planning, but we're here to support you during this process. If you have questions or need assistance, contact [Google Cloud support](https://docs.cloud.google.com/support-hub).

## December 19, 2024

v1

Feature

[Property description](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#custom_extractor_with_property_descriptions) is now Generally Available (GA) as part of the [custom extractor](https://docs.cloud.google.com/document-ai/docs/custom-extractor-overview) in both the Document AI section of the Google Cloud console and the API, with additional support for parent entities in hierarchies.

[Property description](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#custom_extractor_with_property_descriptions) allows you to provide additional context, insights, and prior knowledge for each entity to improve extraction accuracy.

## December 12, 2024

v1

Feature

You can copy processor versions of `pretrained-foundation-model-v1.2-2024-05-10` and `pretrained-foundation-model-v1.3-2024-08-31` between projects by following the steps in [Import a processor version](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions#import).

## October 22, 2024

v1.3

Feature

The Document AI section of the Google Cloud console now allows you to configure property descriptions as part of the [Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#custom_extractor_with_property_descriptions) processor-creation process.

Property description allows you to provide additional context, insights, and prior knowledge for each entity to improve extraction accuracy.

Property descriptions can be edited after schema creation. After you update the property descriptions, you will need to either call the pretrained models or create or fine-tune a new processor version for the changes to take effect.

## October 01, 2024

v1

Feature

Custom Extractor [`pretrained-foundation-model-v1.2-2024-05-10`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) and [`pretrained-foundation-model-v1.3-2024-08-31`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) are now Stable versions.

v1.2 and v1.3 now have the following features:

  * Fine-tuning is now available in Public preview. 
  * They were internally upgraded to a higher quality model.
  * The labeling system has been upgraded to use the latest version of the OCR model.



v1.2 is recommended for the best quality. v1.3 is recommended for the lowest latency.

We recommend creating a new processor and relabeling the training and evaluation documents to benefit from both the improved quality with the new processor versions of Custom Extractor (v1.2 and v1.3) and the enhanced labeling system.

## September 26, 2024

v1

Deprecated

The following earlier versions of Document AI Enterprise Document Optical Character Recognition (OCR) and Expense Parser will be discontinued in the United States (US) and European Union (EU) starting **April 30, 2025.**

Enterprise Document OCR:

  * `pretrained-ocr-v1.0-2020-09-23`
  * `pretrained-ocr-v1.1-2022-09-12`



Expense Parser:

  * `pretrained-expense-v1.2-2022-02-18`
  * `pretrained-expense-v1.3-2022-07-15`
  * `pretrained-expense-v1.4-2022-11-18`



We upgraded the underlying vision model for these versions to an OCR module available in the US and EU.

To ensure uninterrupted service and benefit from improved extraction quality, we recommend you migrate to the following later versions before **April 30, 2025** : 

Enterprise Document OCR (US and EU):

  * Migrate to the latest version of OCR processors: [`pretrained-ocr-v2.0-2023-06-02`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr) or [`pretrained-ocr-v2.1-2024-08-07`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr).



Expense Parser (US and EU):

  * Migrate to the later versions of Expense Parser: [`pretrained-expense-v1.3.2-2024-09-11`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser) or [`pretrained-expense-v1.4.2-2024-09-12`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser).
  * Or migrate to the latest versions of Custom Extractor: [`pretrained-foundation-model-v1.2-2024-05-10`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) or [`pretrained-foundation-model-v1.3-2024-08-31`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde).



To learn more about the migration process, refer to our [Manage processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions) documentation.

If you have any questions or require assistance, contact us at [Google Cloud support](https://docs.cloud.google.com/support-hub).

v1

Deprecated

Effective **April 9, 2025** , the following Custom Extractor versions will no longer be accessible:

  * `pretrained-foundation-model-v1.0-2023-08-22`
  * `pretrained-foundation-model-v1.1-2024-03-12`



You will need to migrate to a later version to avoid any service disruptions, such as [`pretrained-foundation-model-v1.2-2024-05-10`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) and [`pretrained-foundation-model-v1.3-2024-08-31`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) for improved quality from the latest proprietary vision models and foundation models.

We understand that this update requires planning, but we're here to support you during this process. If you have questions or need assistance, contact [Google Cloud support](https://docs.cloud.google.com/support-hub).

## September 23, 2024

v1

Feature

Models `pretrained-expense-v1.3.2-2024-09-11` and `pretrained-expense-v1.4.2-2024-09-12` are available as Release Candidates (RC) for Expense Parser. They are upgrades over v1.3 and v1.4 with an enhanced underlying vision model.

For more information about available models, see [Expense parser processor versions](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser).

## September 20, 2024

v1beta3

Feature

[Custom extractor](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#custom_extractor_with_property_descriptions) now features property descriptions.

Property description allows you to provide additional context, insights, and prior knowledge for each entity to improve extraction accuracy.

Good examples of property descriptions include location information and text patterns of the property values, which help disambiguate potential sources of confusion in the document, guiding the model with rules that ensure more reliable and consistent extractions, regardless of the specific document structure or content variations.

## August 23, 2024

v1

Feature

Model `pretrained-foundation-model-v1.3-2024-08-31` is available as a Release Candidate (RC) for custom extractor. Recommended for those who want the lowest latency and best speed.

For more information about available models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

v1

Feature

Model `pretrained-ocr-v2.1-2024-08-07` is available as RC version of the Document AI OCR 2.1 processor. It has three key improvements:

  * Better printed text recognition.
  * More precise checkbox detection.
  * More accurate reading order.



## August 21, 2024

v1

Feature

Date and Currency Normalization for custom extractor

With this release, the model will deduce the region information from the document and use it to disambiguate the date and currency formats in the following ways:

  * This release will enable the support of region based date and currency normalization of entities with datetime and currency data types in Custom Document Extractor (CDE) Generative AI based processor versions v1.1 and v1.2.
  * Currently CDE Generative AI based processor supports date and currency normalization but it defaults to US date format and USD respectively in case the values are ambiguous. In other words, if a date can be parsed in mm/dd/yyyy and dd/mm/yyyy formats, it will use mm/dd/yyyy format for normalization. Similarly if $ can be mean USD or CAD, it would default to USD.



For more information, go to the [Entity Normalization](https://docs.cloud.google.com/document-ai/docs/normalization) page.

## July 18, 2024

v1

Feature

For custom extractor with generative AI, model `pretrained-foundation-model-v1.1-2024-03-12` provides fine-tuning for US/EU in Public preview. For more information about custom extractor models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

## June 04, 2024

v1

Feature

Layout Parser in Document AI is generally available. The Document AI Layout Parser transforms documents in various formats into structured representations. It makes content like paragraphs, tables, lists, and structural elements like headings, page headers, and footers easily accessible. It also creates context-aware chunks that facilitate information retrieval in a range of generative AI and discovery applications. 

For more information, see [Process documents with Layout Parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk).

## May 28, 2024

v1beta3

Change

Model `pretrained-foundation-model-v1.2-2024-05-10` is available for custom extractor. Recommended for using the largest supported token limits, employing the best quality in identifying entities, or experimenting with newer models.

For more information about available models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

## May 06, 2024

v1beta3

Feature

Batch processing with Layout Parser is available. For more about Layout Parser, see [Process documents with Layout Parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk).

v1beta3

Feature

Model `pretrained-foundation-model-v1.1-2024-03-12` is available for custom extractor. For more information about available models, see [Custom extractor model versions](https://docs.cloud.google.com/document-ai/docs/ce-with-genai#models).

## May 01, 2024

v1beta3

Feature

Online processing is available for Layout Parser in Document AI. The Document AI Layout Parser transforms documents in various formats into structured representations, making content like paragraphs, tables, lists, and structural elements like headings, page headers, and footers easily accessible, and creating context-aware chunks that facilitate information retrieval in a range of generative AI and discovery applications. For more information, see [Process documents with Layout Parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk).

## April 02, 2024

v1

Feature

Fine tuning generative AI models within the Custom Extractor is now supported in GA. For more information, see [custom processors](https://cloud.google.com/document-ai/docs/processors-list#custom_processors) and [fine tuning pricing](https://docs.cloud.google.com/document-ai/pricing#fine-tuning-charges).

## February 29, 2024

v1

Feature

The Custom Extractor with generative AI is now available in the asia-southeast1 (Singapore) regions. For more information, see [Custom processors](https://docs.cloud.google.com/document-ai/docs/processors-list#custom_processors).

v1

Feature

See the model type, generative or custom, powering a Custom Extractor processor version by [getting the model type from the processorVersions API](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors.processorVersions#modeltype).

v1

Feature

The Custom Extractor supports three levels of nesting so you can easily extract structured data from complex documents and tables (earnings reports, tax forms, invoices, resumes, etc.). Learn how to use [three levels of nesting](https://docs.cloud.google.com/document-ai/docs/workbench/cde-with-genai#three-level_nesting).

## February 16, 2024

v1

Announcement

Enterprise Document OCR version 2.0, `pretrained-ocr-v2.0-2023-06-02`, is now Generally Available and ready for production workloads.

Please migrate OCR workloads to this new processor version.

## January 09, 2024

v1

Feature

The Custom Extractor with generative AI has [General Availability](https://cloud.google.com/products/#product-launch-stages) and is ready for production workloads. For more information, see the [Custom Extractor with generative AI](https://docs.cloud.google.com/document-ai/docs/workbench/cde-with-genai) or check out [the demo](https://docs.cloud.google.com/document-ai#demo).

  * As foundation models evolve, so will versions available within the Custom Extractor. For more information, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).
  * Fine tuning the foundation model within the Custom Extractor is still available, in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Fine tune and train by document type](https://docs.cloud.google.com/document-ai/docs/workbench/cde-with-genai#fine_tune_and_train_by_document_type).



v1

Change

To better support production workloads, we reduced prices for the Custom Extractor, Custom Classifier, Custom Splitter, and Form Parser. For more information, see [Document AI pricing](https://cloud.google.com/document-ai/pricing#document-ai-pricing).

v1

Feature

Developers can now specify pages Document AI should process within a document. For more information, see [IndividualPageSelector within V1 API ProcessOptions](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions#individualpageselector).

## December 20, 2023

v1beta3

Feature

Custom Extractor supports fine tuning ([Preview](https://cloud.google.com/products/#product-launch-stages)) so that you can customize foundation model results for user specific documents. This feature is available in the US region. For more information, see [Fine tune and train by document type](https://docs.cloud.google.com/document-ai/docs/workbench/cde-with-genai#fine_tune_and_train_by_document_type).

v1beta3

Feature

Custom Extractor with genAI is now available in the EU and `northamerica-northeast1` regions. For more information, see [Custom processors](https://docs.cloud.google.com/document-ai/docs/processors-list#custom_processors).

v1beta3

Feature

You can now [demo](https://docs.cloud.google.com/document-ai#demo) genAI-powered extraction results within Custom Extractor along with output from other Document AI products such as OCR, Form Parser, and ID processing.

## December 07, 2023

v1

Change

Enterprise Document OCR version 2.0, pretrained-ocr-v2.0-2023-06-02, has an upgraded OCR engine and model improvements. This upgrade better supports high-volume workloads.

## September 25, 2023

v1

Announcement

We are launching an RC version of the `pretrained-invoice-v1.5-2023-09-15` invoice processor. It includes:

  * Improved base-entity extraction model for documents in English.
  * Line-item grouping quality improvements.
  * Better support for multi-line, multi-segment entities such as addresses and line-item descriptions.
  * Enforcement of occurrence type `OPTIONAL_ONCE` / `REQUIRED_ONCE` for properties of nested entities.
  * Updated OCR engine.



## September 21, 2023

v1

Feature

Launched Document AI Enterprise Document OCR v2.0 and OCR add ons in Preview. 

Enterprise Document OCR launched a Release Candidate, `pretrained-ocr-v2.0-2023-06-02`, which includes: 

  * Upgraded OCR model, optimized for various document use cases.
  * Visual-element detector for boxed characters, which can increase quality up to 10% for documents with text boxes. 



For more details, see the [documentation](https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr), including the [user guide](https://docs.cloud.google.com/document-ai/docs/process-documents-ocr).

OCR add ons are available from the Enterprise Document OCR processor when using `pretrained-ocr-v2.0-2023-06-02`. These include: 

  * Checkbox extraction: Detects and extracts status (marked/unmarked) in the Enterprise Document OCR response.
  * Math OCR: Identifies, recognizes, and extracts formulas from documents in LaTeX output format. 
  * Font-style detection: Identifies word-level font properties, including type, style, handwriting, weight, and color.



For more details, see the [documentation](https://docs.cloud.google.com/document-ai/docs/ocr-add-ons).

## August 25, 2023

v1

Feature

Document AI Workbench is now powered by generative AI with two feature launches:

Document AI Workbench Summarizer is in Preview:

  * The Summarizer provides summaries for documents up to 250 pages long.
  * You can customize summaries based on your preferences for length (brief, moderate, comprehensive) and format (paragraph, bullet points).
  * See the [user guide](https://docs.cloud.google.com/document-ai/docs/workbench/build-summarizer-processor) for more information.



Document AI Workbench custom extractor is in preview:

  * Custom extractor with generative AI can help extract data from documents with free-form text (e.g., contracts) and complex layouts (e.g., invoices, W2s, bills of lading).
  * The pretrained processor version, which uses generative AI, can be used out of the box without any training. Post a document to the endpoint with a list of fields to get structured data.
  * Customize results by confirming content in about five documents. Workbench leverages the examples to improve accuracy using few-shot prediction.
  * Extract information from documents up to 200 pages long through the asynchronous API.
  * To get started, create or use an existing custom extractor to leverage a processor version.
  * See the [how-to guide](https://docs.cloud.google.com/document-ai/docs/workbench/build-custom-processor), [labeling best practices](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#labeling), and training [use cases](https://docs.cloud.google.com/document-ai/docs/workbench/training-overview#training_models).
  * Current limitations of generative AI extraction within the custom extractor: 
    * Only the English language is supported.
    * Region availability is currently only in the US.
    * While in preview, we recommend that you only extract up to 50 entities per endpoint with generative AI.
    * When uploading a sample document to define fields and preview results on the **Get started** page, there can be long latencies. We're working to reduce this latency.



In addition, template-based training is available in GA within the custom extractor:

  * Template-based training provides accurate predictions for documents with no layout variation (such as an application form).
  * Only six labeled documents are needed to train and use a template-based processor version.
  * See the [user guide](https://docs.cloud.google.com/document-ai/docs/workbench/cde-template-based-guide) and training [use cases](https://docs.cloud.google.com/document-ai/docs/workbench/training-overview#training_models).



## August 18, 2023

v1

Feature

**Expense processor**

A new RC version `pretrained-expense-v1.3.1-2023-08-11` of the Expense processor is now available in the `asia-southeast1` region for Expense Parser customers. 

This release includes an improved region-based normalization, which results in an average improvement of up to a 15% accuracy on normalized date and currency entities over the current stable version.

## August 01, 2023

v1

Feature

Launched the following Document AI Workbench features:

  * Create and train models programmatically with more public APIs, including: 

    * DatasetSchema APIs: [`UpdateDatasetSchema`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.dataset/updateDatasetSchema), [`GetDatasetSchema`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.dataset/getDatasetSchema). To create schema, use the `UpdateDatasetSchema` API (a singleton resource).

    * Dataset APIs: [`UpdateDataset`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors/updateDataset), [`ImportDocuments`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.dataset/importDocuments), [`GetDocument`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.dataset/getDocument), [`BatchDeleteDocuments`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.dataset/batchDeleteDocuments). Until we release a `ListDocument` API, use confirmations from the `ImportDocuments` API to create a list of documents in your dataset. 

  * Selective labeling within Custom Document Extractor (CDE) helps you prepare a diverse set of training and test documents. Import 125+ documents to a CDE dataset, then CDE recommends documents you should label based on clustering results. Selective labeling only supports new documents imported into your dataset. If you would like recommendations for documents already in your dataset, then delete and re-import them. 

  * Quick Tables within CDE helps you train models faster by labeling a table in bulk by applying the first row pattern to the rest of the table.

  * Get started with a new processor by using a default storage option for your dataset. You can still configure your own Cloud Storage location using advanced options.




## July 28, 2023

v1

Change

Launched an update to the RC release `pretrained-invoice-v1.4-2022-10-21` of the invoice processor, available to all Document AI users. 

This release includes the features of the Stable version, with an average improvement of 0.03 to 0.05 micro F1 (approximately 5% to 9%) on line item entities.

## July 18, 2023

v1

Feature

The following Form Parser (`pretrained-form-parser-v2.0-2022-11-10`) features are Generally Available ([GA](https://cloud.google.com/products/#product-launch-stages)):

  * General field extraction: You can extract 11 different types of entities from documents.
  * Enhanced check-box detection.
  * Internationalization support that covers more than 200 languages.
  * Upgraded key-value pair (KVP) detection model.



v1

Feature

Form parser v2.1 (`pretrained-form-parser-v2.1-2023-06-26`) is in [Public Preview](https://cloud.google.com/products/#product-launch-stages), which uses our native PDF text extraction model on PDF documents.

v1

Issue

The Form Parser features has the following limitations:

  * Check-box doesn't support radio buttons and might not reliably parse all selection marks or keyless checkboxes.
  * If there is a key without a value, the model might not parse it.
  * The quality of KVP parsing might be higher for Latin languages than others.
  * For tables, only simple tables are supported (no support for merged cells).



## July 17, 2023

v1

Feature

The Custom Document Splitter (CDS) within Document AI Workbench is now Generally Available (GA) for production use cases to split and classify multiple documents within a single file. With this release, all Workbench processors currently offered (Custom Document Extractor, Custom Document Classifier, and Custom Document Splitter) are available in GA. 

Launched the following features for CDS:

  * CDS now supports up to 1,000-page documents for async/batch prediction and up to 200-page documents when importing, labeling, training, or evaluating.
  * CDS model evaluation for document split and classification 
  * Prepare a CDS training dataset faster by bulk labeling documents at import across multiple folders.



Released the the following enhancements for CDS:

  * Improved labeling and evaluation experience with the ability to review overall document splits and classifications while viewing individual pages in a side-by-side view.
  * Document names are now used in error messaging to improve troubleshooting.
  * Hyphens are allowed in schema names.



## June 29, 2023

v1

Feature

**Identity Document AI (IDAI) photo copy detection in ID proofing ([Preview](https://cloud.google.com/products/#product-launch-stages))**

Updated the `pretrained-id-proofing-v1.1-2023-05-18` ID proofing processor for all Document AI users. 

This processor includes a new output entity `fraud_signals_photocopy_detection` that signals if an attached image might be a photocopy. The entity can be one of the following values: `POSSIBLE_PHOTOCOPY`, `PASS`, or `INCONCLUSIVE`.

## June 28, 2023

v1

Feature

Support for DOCX is in [Preview](https://cloud.google.com/products/#product-launch-stages). You can synchronously process DOCX files that are up to 15 pages, or asynchronously process DOCX files that are up to 30. For access, send us a [request](https://forms.gle/nPUcJC8gJ2zwh6yK7).

v1

Issue

The document OCR native text from digital PDF feature contains the following known issues:

  * For a small number of documents, word order in lines of text that are reported by native text extraction might be inaccurate.
  * Invisible text that is embedded in a native PDF might be extracted.
  * Japanese documents that contain currency symbols, such as Yen, might be incorrectly extracted as `/`.
  * Apostrophe symbols might be missing in word and/or line results. 
  * Native text extraction might report different word and/or line results compared to image-based OCR on an identical document.



v1

Feature

Added fixes to our `doc.proto-to-vision.proto` conversion tool, which facilitates migration from Vision API `TextDetection` to document OCR.

v1

Feature

The following document OCR features are Generally Available ([GA](https://cloud.google.com/products/#product-launch-stages)). Use document OCR's configurations to optimize for stability, quality, and specific response requirements.

  * Intelligent document-quality analysis
  * Native text from digital PDF
  * Symbol-level extraction
  * Language hints



## April 25, 2023

v1

Feature

Launched the following features to improve the usability of the Document AI Workbench Custom Document Extractor (CDE):

  * CDE now supports an additional 42 global languages.
  * CDE lets you import processor versions across projects and processors to easily manage development and production environments.
  * CDE can automatically label documents in a dataset by using a deployed processor version to help you quickly prepare training data.



Document AI Workbench Custom Document Extractor (CDE) has also made the following enhancements:

  * The asynchronous prediction API can now extract data from documents up to 200 pages long. 
  * Improved the accuracy of extracting checkboxes.



## April 17, 2023

v1

Announcement

**Identity Document AI (IDAI) pricing change**

We are changing the price of our US-related identity document processors. The new price is on the [pricing page](https://cloud.google.com/document-ai/pricing#identity).

## March 27, 2023

v1beta3

Change

For the Document AI OCR Processor (Doc OCR), you can enable document quality assessments for all processor versions instead of a specific processor version, such as `pretrained-ocr-v1.1-2022-09-12`. If you enable document quality assessment, Doc OCR produces a quality score that's based on the document's readability. Quality scores range from 0 to 1, where 1 is perfect quality. Quality scores are returned in the `image_quality_scores` field on the `Page` object. All detected issues are labeled as `quality` or `defect` and sorted in descending order by confidence value. To use this feature, set `process_options.ocr_config.enable_image_quality_scores= true` in your API request to the OCR Processor.

v1beta3

Feature

The Document AI OCR Processor (Doc OCR) now has the following features:

  * The OCR Processor supports _language hints_. The OCR engine prefers your specified languages over inferred languages. To use this feature, set `process_options.ocr_config.hints.language_hints` with a list of BCP-47 language codes in your API request to the OCR Processor.
  * The OCR Processor supports the option to populate symbol-level data in the document response. If enabled, the field `document.pages.symbols` is populated. To use this feature, set `process_options.ocr_config.enable_symbol=true` in your API request to the OCR Processor.
  * A proto converter tool that converts a `Document proto` to an `AnnotateFileResponse` proto. This conversion lets you compare the responses between the Document AI OCR processor with the Vision API, which can help you migrate to the Document AI OCR processor from Vision API with minimal downstream changes. For details, see [Document AI Toolbox](https://docs.cloud.google.com/document-ai/docs/handle-response#code_samples_6).
  * The OCR Processor supports a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. You can choose the layout algorithm that best suits your needs. To use this feature, set `process_options.ocr_config.advanced_ocr_options= legacy_layout` in your API request to the OCR Processor.



## February 21, 2023

v1

Change

This launch upgrades the lifecycle stage of the Custom Document Extractor (CDE) component of the DocAI Workbench from Public Preview to Generally Available (GA). CDE covers essential workflows for developing custom document extraction processors with end-to-end UI support:

  * Data import
  * Schema creation and annotation
  * Processor model training
  * Evaluation and troubleshooting
  * Model deployment and version management
  * Human-in-the-loop (HITL) integration for "last-mile" processor quality assurance



v1

Feature

Notable new Generally Available Custom Document Extractor (CDE) features include:

  * Public APIs
  * Automatic schema label creation from pre-labeled documents
  * Schema label data type and occurrence editable pre-training 
  * New DocAI Toolkit with a labeled document converter



The following features have been upgraded:

  * Processor gallery
  * Schema editor 
  * Labeling UI
  * Training pipeline
  * Manage versions table



## January 10, 2023

v1beta3 & v1

Change

The Form Parser Release Candidate version has been renamed to `pretrained-form-parser-v2.0-2022-11-10`. See [Document AI release notes--December 12, 2022](https://docs.cloud.google.com/document-ai/docs/release-notes#December_12_2022) for more information about this release.

## December 22, 2022

v1beta3

Announcement

We are launching a public preview version of the purchase order processor, `pretrained-purchase-order-v1.1-2022-06-17`, with the following features:

  * Support for uptraining to improve, add, and remove entities in the schema.
  * Support for uptraining to add support for unsupported languages.
  * Improvements to overall performance.



## December 19, 2022

v1beta3

Feature

The Document AI OCR Processor has the following new features:

  * The OCR Processor now supports extracting embedded text from digital PDFs in public preview. A fallback to the optical OCR model is automatically triggered to extract text in the regions when the PDF being processed contains non-digital text. To opt into this feature, set [`process_options.ocr_config.enable_native_pdf_parsing=true`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/ProcessOptions#OcrConfig) in your API request to the OCR Processor.

  * Added advanced versioning support to the Document AI OCR, which enables OCR users to pin to a historical model version. When enabled, OCR outputs are guaranteed to be consistent and virtually frozen, with zero behavioral drifts. To enable advanced versioning, select the release candidate version `pretrained-ocr-v1.2-2022-11-10` in your Document AI console.




v1beta3

Issue

Known issues with the digital PDF feature of the Document AI OCR Processor:

  * On a small number of documents, the word ordering within lines of text as reported by native text extraction might be wrong.

  * On certain documents, invisible text embedded in a native PDF may be reported. 

  * On certain Japanese documents, currency symbols such as Yen might be incorrectly extracted as `/`.

  * On certain documents, apostrophe symbols may be missing in word/line results. 

  * On certain documents, native text extraction might report different word/line results than those obtained by image-based OCR on an identical document.




## December 15, 2022

v1

Change

We are launching the Release candidate version, `pretrained-utility-v1.2-2022-12-15` of the utility processor. This version includes the following features:

  * Removal of three entities from schema: `delivery_date`, `receiver_email`, `receiver_phone`
  * Improvements to overall performance



The utility processor version `pretrained-utility-v1.1-2021-04-09` continues to serve as the current, latest Stable version.

## December 12, 2022

v1beta3

Feature

The Form Parser now supports Generic Entity Extraction in Public Preview, covering the following entity types: 

  * `email`: email address
  * `phone`: phone number
  * `url`: website URLs
  * `date_time`: partial or full date/time/period
  * `address`: full address or street address in a single line
  * `person`: partial or full name of a person
  * `organization`: full name of an organization
  * `quantity`: a number specifying quantity or percentage
  * `price`: a number specifying monetary amount
  * `id`: a number specifying identity
  * `page_number`: a number specifying page number



v1beta3

Feature

The Form Parser has the following feature enhancements:

  * The Form Parser key-value pair (entity and checkbox) extraction and table extraction now support 200+ languages that are supported by the underlying multi-language OCR model. This language expansion is in Public Preview, with key-value pair internationalization backed by quality benchmarks in selected languages such as Simplified Chinese, Traditional Chinese, Japanese, and Korean. 

  * Table extraction in Form Parser is now powered by an enhanced vision-based table parsing model.




These enhanced features are automatically enabled for Form Parser processor version `pretrained-parser-v2.0-2022-11-10` and all future versions. Note that this is a Release Candidate version, which is subject to further changes before graduating to the Stable version.

## December 08, 2022

v1

Feature

[Invoice Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor) and [Expense Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor) are now available in the following [single-region locations](https://docs.cloud.google.com/document-ai/docs/regions):

  * `australia-southeast1` (Sydney)
  * `northamerica-northeast1` (Montréal)



## November 21, 2022

v1

Announcement

**Expense Parser Releases**

As of November 18, 2022, for the Expense Parser, we have promoted our v1.3 Release Candidate version to a Stable version so that more customers can use it confidently. 

**New Stable version**

Features in the new Stable Expense Parser, `pretrained-expense-v1.3-2022-07-15`:

  * Support for a new language, Japanese, which has been requested by multiple customers.

  * Better entity performance

  * Addition of 3 new entity types (`line_item/quantity`, `payment_type`, `credit_card_last_four_digits`)

  * Better support for hotel and car-rental related expenses 




**New Release Candidate version**

Along with this Stable version, we are also launching a new Release Candidate version of the Expense Parser, `pretrained-expense-v1.4-2022-11-18`, with the following new features, in addition to the features in the Stable version:

  * Improvements to overall performance

  * Support for two (2) new languages, Italian and Portuguese

  * Support for Uptraining to improve or add/remove entities in the schema

  * Support for Uptraining to add support for unsupported languages

  * Addition of 3 new entity types (`traveler_name`, `reservation_id`, `line_item/transaction_date`)

  * Maximum pages (online/synchronous requests) limit has been increased to 15.




**Deprecation of the old Stable version**

The `pretrained-expense-v1.1-2021-04-09` version of the Expense Parser will be deprecated following this release. 

**Invoice Parser Updates**

The previous Stable invoice processor version, `pretrained-invoice-v1.1-2021-04-09`, is deprecated as of November 22, 2022.

v1beta3

Change

The Invoice Parser, for v1.3 and v1.4, now has the following quotas and limits:

  * Maximum pages (online/synchronous requests): 15
  * Maximum pages (batch/offline/asynchronous requests): 200



## November 16, 2022

v1beta3

Announcement

The Identity Document Proofing Processor is now available in Public Preview.

v1beta3

Feature

The Identity Document Proofing Processor is designed to help predict the validity of ID documents with four different signals:

  * `is_identity_document detection`: predict whether an image contains a recognized identity document. 
  * `suspicious_words detection`: predict whether words are present that aren't typical on IDs.
  * `image_manipulation detection`: predict whether the image was altered or tampered via an image editing tool.
  * `online_duplicate detection`: predict whether the image can be found online.



## November 11, 2022

v1beta3

Change

New stable W2 processor version with the following enhancements:

  * Breaks down long entities such as addresses into fine-grained sub-entities: `StreetAddressOrPostalBox`, `AdditionalStreetAddressOrPostalBox`, `City`, `State`, and `Zip`. This modification not only improves accuracy, but also entity specificity.
  * Handles wider variations of W2 forms including multi-copies (2,3,4-ups) issued by various payroll vendors.
  * Introduces 8 new entities for Box 12 that represent both codes and values.



v1beta3

Change

New stable Payslip processor version with the following enhancements:

  * Bonus, commissions, holiday, overtime, regular pay and vacation are now part of `earning_item/earning_this_period` and `earning_item/earning_ytd`. Captures all types of earnings beyond those categories, and maps them to their respective earning rates, hours and pay (both for the period and year-to-date). 
  * Returns year-to-date and current period taxes and deductions.
  * Direct deposits are linked to the corresponding bank account numbers.
  * Returns page numbers, state and federal tax exemptions and filing statuses.



## October 31, 2022

v1

Feature

A new Release Candidate (RC) version of the Document OCR Processor, `pretrained-ocr-v1.1-2022-09-12`, is available in the US and EU. This RC can detect document defects.

  * If the document is considered to be defective, the API now returns the same 5 document defect types supported by the [Intelligent Document Quality Processor](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-quality-processor): 
    * `quality/defect_blurry`
    * `quality/defect_noisy`
    * `quality/defect_dark`
    * `quality/defect_faint`
    * `quality/defect_text_too_small`
  * In addition, it now supports 3 more defect types: 
    * `quality/defect_document_cutoff`
    * `quality/defect_text_cutoff`
    * `quality/defect_glare`
  * The defect detection results are in the `image_quality_scores` field on the `Page` object in the returned JSON. This additional feature adds latency comparable to OCR processing to the `process` call.



## October 21, 2022

v1

Feature

As of October 21, 2022, we have promoted our v1.3 Release Candidate version to a Stable version of the Invoice processor. 

Features in the new Stable Invoice processor, version `pretrained-invoice-v1.3-2022-07-15`.

  * Support for seven new languages: Italian, Portuguese, Romanian, Swedish, Estonian, Latvian, and Lithuanian.

  * Support for uptraining using Document AI Workbench. See [Uptrain a specialized processor](https://docs.cloud.google.com/document-ai/docs/workbench/uptrain-processor).

  * Improvements to currency and date normalization.

  * Improvements to line item extraction.

  * Quotas and limits

    * Maximum pages (online/synchronous requests): 15
    * Maximum pages (batch/offline/asynchronous requests): 200
    * Regional availability 
      * US (Multi-region), Europe (Multi-region)



Alongside this Stable version, we are launching a Release Candidate version, `pretrained-invoice-v1.4-2022-10-21`.

## October 10, 2022

v1beta3

Issue

**Known issue (Document Labeling)**

  * If you delete one or more documents, and these documents selected for deletion are all associated with an active labeling job, then all documents in that dataset will also be deleted, even if you did not select them for deletion. This is true regardless of the number of documents selected.

**Workaround:** Do not delete documents during an active labeling job. You can track active labeling jobs on the **Dataset management** page, under the category **Labeling tasks** , located on the right side of the page. If you absolutely must delete documents during an active labeling job, ensure that you also select at least one document that is **NOT** part of this active labeling job. Then, only the non-associated documents will be deleted, and the remaining documents in the dataset will be preserved.




## September 29, 2022

v1beta3

Announcement

This launch upgrades the lifecycle stage of the Custom Document Extractor (CDE) component of the DocAI Workbench from Private Preview to Public Preview. CDE covers essential workflows for developing custom document extraction processors with E2E UI support:

  * Data import
  * Schema creation and annotation
  * Processor model training
  * Evaluation and troubleshooting
  * Model deployment and version management
  * Human-in-the-loop (HITL) integration for "last-mile" processor quality assurance



v1beta3

Feature

Notable new Public Preview Custom Document Extractor (CDE) features include:

  * Progressive data import
  * Direct import of annotated .json files as training or test datasets
  * Data labeling platform integration
  * Dataset export with metadata preserved
  * Auto-labeling using a trained processor version at import to minimize manual annotation efforts
  * Tabular entity end-to-end support
  * Checkbox boolean annotation, training, and extraction
  * Fuzzy matching for more flexible model evaluation
  * Exportable / downloadable model evaluation metrics



The following features have been upgraded:

  * Data import
  * Schema creation and annotation
  * Processor model training
  * Evaluation and troubleshooting
  * Model deployment and version management
  * Human-in-the-loop (HITL) integration for "last-mile" processor quality assurance



v1beta3

Issue

**Known issues**

  * During labeling, checkboxes default to a state that does not reflect the selected or unselected states in the corresponding documents.

**Workaround:** Label all checkboxes within a schema, regardless of whether they are selected or unselected, for optimal checkbox extraction quality and accurate evaluation. When annotating a checkbox by drawing its bounding box, all checkboxes in the CDE annotation user interface will default to an unselected state, and you must manually update the selected or unselected state as necessary.

  * If a processor is deleted when there is an active labeling task ongoing, the task does not stop automatically. Labelers and Labeler Managers will still see the task in their labeling and manager consoles. 

**Workaround:** Cancel the active labeling task before you delete the processor. Otherwise, navigate to the manager console to pause or delete the corresponding task queue. Any documents labeled from that task after the processor is deleted will be unretrievable.

  * Some discrepancies might exist between pretrained and uptrained versions of a processor. 

  * On the **Evaluate & Test** tab, the evaluation does not show as complete until you click **Refresh Table**. 

  * If you cannot choose a specialist pool due to no chooser for the specialists, clicking **Continue** causes an error. 

**Workaround:** Click **Task Details** to go back and fill in remaining details.

  * Support for nested entities is limited to data arranged in a tabular format. Other layouts are currently not supported.

Any mention of "nested entities" in previous versions of the Document AI Workbench documentation have been replaced with "tabular entities" to reflect the table-based nesting capabilities for this launch.

  * If you see this message, "This processor does not currently support uptraining or evaluation capabilities" on a processor in the **Processor gallery** , this means that only the prediction endpoint is available at this time.

  * In some cases, `required_once` and `optional_once` entities appear multiple times in a document, with the same value copied to multiple locations. While one annotation is s sufficient when annotating a test set for evaluation, all copies should be annotated to ensure higher recall for trained models. 

**Workaround:** Annotate all instances of an entity within a doc. This will support both Evaluation and Training without any infrastructure changes. 

  * Existing Human in the Loop (HITL) configurations for **Label-level filters** do not automatically populate to new processor configurations. 

**Workaround:** If you require changes to the configuration, navigate to the **Human-In-The-Loop** tab. Under **Set filters** , select **Label-level filters** and click **Set Label Filters**. A **Label-level filters** page opens. Manually edit this table to configure all of the labels needed for validation and review. 

  * Support for handwritten entity detection such as signatures, dates, and initials are limited and may require additional configuration for proper evaluation. 

**Workaround:** When evaluating pretrained processors, the **Value** should be manually updated to `YES` if the entity is present, or `NO` otherwise. For uptrained processor versions, the **Value** should be kept as detected by OCR. This issue affects W9, HUD92900B, SSA-1099, and VBA26-0551 processors.

  * When you attempt to select a specialist pool for a labeling task, and there are missing fields in the form, and then click **Continue** , you might get an error.

**Workaround:** Click **Task Details** , and enter the missing details in the form. You can then successfully create a labeling task.




## September 15, 2022

v1beta3

Feature

**Schema support for checkboxes and nested entitites**

  * Customers using Document AI Workbench, and processors for Purchase Order (PO), Invoice, or Expense, now have access to a new schema. This schema enables customers to label checkboxes, if they are defined in the schema, and to accurately represent nested entities, such as parent-child relationships, on the HITL annotation and review console. As additional processors adapt the new schema, these release notes will be updated to include those. 



**Nested entities**

  * The Annotation console now supports labeling for nested entities. The left panel is refreshed with a new look for nested rows to represent nested entities. The value of "parent" will now be the concatenation of all its "children". The parent is effectively a container for all of its children.



## September 01, 2022

v1 & v1beta3

Announcement

We are standarding our release processes and naming conventions for processor versions. For more information, see [Manage processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor).

## July 27, 2022

v1

Announcement

**New Release Candidate (RC) versions for PDAI Invoice and Expense processors - July 2022**

We have launched new RC versions of Invoice parser and Expense parser on July 15, 2022. These can be accessed in the following way:

  * Invoice parser: `pretrained-next-uptrainable`
  * Expense parser: `pretrained-next`



Here are the details about the contents of the RC version updates:

Processor | New Languages | New Entities  
---|---|---  
Invoice: `pretrained-next-uptrainable` | Italian, Portuguese, Romanian, Swedish  | N/A  
Expense: `pretrained-next` | Japanese  | Support for hotel and car rental folios  
  
Payment information entities: Last 4 digits of credit card, payment type   
  
The current limit for uptrainable processors is as follows (it is different from the pre-trained version). We are gathering customer feedback to increase the async limit.

**Quotas and limits**

Maximum pages (online/synchronous requests): | 10  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 15  
  
## June 30, 2022

v1

Feature

**VPC Service Control support**

Document AI **VPC Service Controls** provide additional security for your resources and services. To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To learn about the limitations when using Document AI with VPC Service Controls, see the [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

## June 13, 2022

v1beta3

Feature

**New Identity Processor (Preview)**

The [France Passport Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_french-passport-parser) is now available in limited preview.

v1

Change

Document AI is now generally available (GA) in the following new locations:

  * `asia-south1` (Mumbai)
  * `australia-southeast1` (Sydney)



You must request access to use the new locations. For more information, see [Regional and multi-regional support](https://docs.cloud.google.com/document-ai/docs/regions).

## June 10, 2022

v1beta3

Change

The [Contract Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_contract-parser) is now more accurate, can extract more fields and supports higher page limits.

## June 01, 2022

v1

Announcement

**Identity DocAI General availability (GA) release**

The following Identity DocAI processors are now [Generally Available](https://cloud.google.com/products/#product-launch-stages) (GA).

  * [US Driver License Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_us-driver-license-parser)
  * [US Passport Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_us-passport-parser)



For more information, see [Document AI for Identity](https://solutions/identity-doc-ai).

## April 21, 2022

v1

Change

**Document OCR processor**

The changes from the _Google Default Next_ version have been applied to the _Google default_ version.

The previous _Google default_ version can still be accessed until July 21, 2022 as _pretrained-legacy_. After July 21, 2022, that version will be removed.

For more information about using different versions of the processor, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor) .

For the original announcement of this change, see the [January 14, 2022 release note](https://docs.cloud.google.com/document-ai/docs/release-notes#January_14_2022).

## April 08, 2022

v1

Feature

**New Version of Lending W2 Processor**

We have released a new _Release Candidate_ version of the [W2 Processor](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_w2-parser). This version is experimental and has the following features: 

  * Quality improvement on `SSN` and `EIN` fields.
  * Support for box 12 fields, including both codes and values.
  * Fine grained predictions of `EmployeeName`, `EmployeeAddress`, and `EmployerNameAndAddress` which are no longer part of the output and replaced with additional fields.



## March 25, 2022

v1

Feature

**New & Updated** processors available

The following [Lending DocAI processors](https://docs.cloud.google.com/document-ai/docs/processors-list#lending_processors) are now available for trusted testers. Access to the trusted testers program is limited and granted on a case by case basis. If you would like to be considered please fill out the [DocAI Processor Access Request Form](https://docs.google.com/forms/d/e/1FAIpQLSc_6s8jsHLZWWE0aSX0bdmk24XDoPiE_oq5enDApLcp1VKJ-Q/viewform):

**_New_** Experimental processors to support new document types:

  * Form VA Loan Discharge Statement Processor
  * Form USDA Conditional Statement Processor
  * Form 1017 Processor
  * Form Biweekly Payment Rider Processor
  * Form VBA26 1805 Processor
  * Form VBA26 6393 Processor
  * Form MERS Rider Processor



**_Updated_** Experimental processors:

  * Form 4506-T Processor
  * Form 4506-C Processor
  * Form HUD54114 Processor
  * Form HUD92900WS Processor
  * Form HUD92800 Processor
  * Form 1040-NR Processor
  * Form HUD92900LT Processor
  * Form VBA26 8923 Processor
  * Form HUD92900A Processor
  * FORM_1005_PROCESSOR



## March 10, 2022

v1

Change

Document AI is now generally available (GA) in the following new locations:

  * `europe-west3`
  * `asia-southeast1`



You must request access to use the new locations. For more information, see [Regional and multi-regional support](https://docs.cloud.google.com/document-ai/docs/regions).

## February 18, 2022

v1

Change

**New Versions of Procurement Processors**

We have launched a new _Google Pretrained_ version of the following procurement processors with various quality improvements:

  * [Invoice parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor)
  * [Expense parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser)



The changes from the old _Google default next_ version have been applied to the new _Google Pretrained_ version. The old _Google default_ version is still available and will not be deprecated for at least 180 days.

## January 26, 2022

v1 & v1beta3

Feature

Enrichment using the Knowledge Graph is now [Generally Available](https://cloud.google.com/products/#product-launch-stages). 

For more information, see [Enterprise Knowledge Graph field enrichment](https://docs.cloud.google.com/document-ai/docs/enrichment).

## January 14, 2022

v1

Change

**Document OCR processor**

We have updated the _Google default next_ version with quality improvements. Consequently, you have 90 days from today to test the new model before the changes are applied to the _Google default_ version. After that, the original _Google default_ version will be available for another 90 days as _legacy_. For more information about the processor and its versions, see the [Document OCR processor](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr).

For more information about using different versions of the processor, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor).

For the original announcement of this change, see the [November 5, 2021 release note](https://docs.cloud.google.com/document-ai/docs/release-notes#November_05_2021).

## December 15, 2021

v1beta3 & v1

Feature

**New Lending Processors (Preview)**

The following new processors are now available in [Preview](https://cloud.google.com/products#product-launch-stages). To request API access, fill out and submit the [Document AI limited access customer request form](https://docs.google.com/forms/d/e/1FAIpQLSc_6s8jsHLZWWE0aSX0bdmk24XDoPiE_oq5enDApLcp1VKJ-Q/viewform?gxids=7826).

  * 1040 Schedule D Parser
  * HOA Statement Parser
  * HUD-92900B Parser
  * SSA-89 Parser
  * VBA26-0551 Parser



The following is available through the Cloud console. 

  * Investment and retirement statement parser



v1beta3 & v1

Feature

**New Versions of Lending Processors**

We have launched new versions of the following lending processors, in General Availability [(GA)](https://cloud.google.com/products#product-launch-stages).

  * [Bank Statement Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser)
  * [Pay Slip Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser)
  * [W2 Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_w2-parser)



These new versions use a new lending document splitting and classification model with improved quality and support for more document types.

## November 10, 2021

v1

Change

We have lowered the price for many processors. For more information, see the [Pricing](https://cloud.google.com/document-ai/pricing) page.

## November 05, 2021

v1

Feature

**New Lending Processor (Preview)**

The [Mortgage statement parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_mortgage-statement-parser) is now available in limited preview.

v1

Feature

We have release a new version of the [Document OCR Processor](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr) called _Google default next_. This version changes the distribution of confidence scores in the response. You have 90 days from today to test the new model before the changes are applied to the _Google default_ version . After that event, the original version will still be available for another 90 days as _legacy_. For more information about using different versions of the processor, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor).

v1

Feature

The following procurement processors are now publicly accessible: 

  * [Expense Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser)
  * [Invoice Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor)



## October 15, 2021

v1beta3

Feature

**Contract DocAI (Preview) released**

The [Contract parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_contract-parser) is now available.

## October 06, 2021

v1

Feature

Document AI is now generally available (GA) in the following new locations:

  * `europe-west2`
  * `northamerica-northeast1`



You must request access to use the new locations. For more information, see [Regional and multi-regional support](https://docs.cloud.google.com/document-ai/docs/regions).

## September 01, 2021

v1

Feature

Document AI now supports [Data Residency](https://cloud.google.com/terms/data-residency), [VPC-SC](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_documentai), [Access Transparency](https://docs.cloud.google.com/cloud-provider-access-management/access-transparency/docs/supported-services), and [CMEK](https://docs.cloud.google.com/document-ai/docs/cmek).

## August 20, 2021

v1

Feature

**New processor versions**

We have added new versions of the following processors:

  * [Bank statement parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser): improved model quality
  * [Pay slip parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser): improved model quality and extraction of three additional fields: `net_pay`, `net_pay_ytd`, and `employee_account_number`.



v1

Feature

**Managing processor versions**

You can now switch between different versions of a processor. For more information, see [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor).

v1

Feature

**Human in the Loop (HITL) support for Lending DocAI processors**

The following [Lending DocAI processors](https://docs.cloud.google.com/document-ai/docs/processors-list#lending_processors) now support [Human in the Loop](https://docs.cloud.google.com/document-ai/hitl) (HITL):

  * 1003 parser
  * 1040 Parser
  * 1040 Schedule C parser
  * 1040 Schedule E parser
  * 1099-DIV parser
  * 1099-G parser
  * 1099-INT parser
  * 1099-MISC parser
  * Bank Statement parser
  * Pay Stub parser
  * W2 parser
  * W9 parser



v1

Feature

**New Lending DocAI processors**

The following [Lending DocAI (LDAI) processors](https://docs.cloud.google.com/document-ai/docs/processors-list#lending_processors) are now available in limited [Preview](https://cloud.google.com/products#section-22):

  * 1065 parser
  * 1099-NEC parser
  * 1099-R parser
  * 1120 parser
  * 1120-S parser
  * SSA-1099 parser



Additionally, the [LDAI Document Splitter and Classifier](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_lending-splitter-classifier) has been updated to support the new LDAI processors as well as the following processors:

  * US Driver License Parser
  * US Passport Parser



v1

Feature

**Knowledge Graph support**

The following processors now support [Knowledge Graph](https://docs.cloud.google.com/document-ai/docs/enrichment) enrichment:

  * Bank Statement
  * Pay Slip
  * W2 Parser
  * W9 Parser



## July 30, 2021

v1

Feature

The [Invoice Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor) now extracts a new field `invoice_type` that indicates the type of the input document.

## July 02, 2021

v1

Change

**Change in processor documentation**

The location of individual processor information has changed. You can now find individual processor documentation for all solutions (General, Procurement, Lending) in the following locations:

  * [Overview](https://docs.cloud.google.com/document-ai/docs/processor-overview)
  * [Full processor and detail list](https://docs.cloud.google.com/document-ai/docs/processors-list)
  * [Limits, file types, and versions supported](https://docs.cloud.google.com/document-ai/docs/file-types)
  * [Fields detected](https://docs.cloud.google.com/document-ai/docs/fields)
  * [Sample processor output](https://docs.cloud.google.com/document-ai/docs/output)



v1

Feature

Human in the Loop (HITL) now supports priority queues for each processor, based on the urgency of each document. For more information, see [HITL](https://docs.cloud.google.com/document-ai/hitl).

## June 09, 2021

v1

Feature

**VPC Service Controls**

Integration with Document AI [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_documentai) is now generally available.

## April 09, 2021

v1

Announcement

**Procurement DocAI General availability (GA) release**

Procurement DocAI (PDAI) solution is now available in private General Availability (GA).

This includes the following processors:

  * [Invoice parser](https://docs.cloud.google.com/document-ai/docs/invoice-parser)
  * [Expense parser](https://docs.cloud.google.com/document-ai/docs/expense-parser) (formerly Receipt parser)
  * [Procurement document splitter & classifier](https://docs.cloud.google.com/document-ai/docs/procurement-splitter)
  * [Utility parser](https://docs.cloud.google.com/document-ai/docs/utility-parser)



v1

Announcement

**Human in the Loop (HITL) support for Procurement DocAI processors**

Procurement DocAI processors now support Human in the Loop (HITL) AI platform functionality supporting human revisions of predictions.

v1

Change

**Invoice parser behavior update**

The invoice parser behavior has been updated to include the following features:

  * Offers extended support for the following languages (in addition to English): 
    * French
    * Dutch
    * German
    * Spanish
  * Improves supplier parsing accuracy with Knowledge Graph support.
  * Improves prediction quality (accuracy).
  * Extends the header and line item [fields extracted](https://docs.cloud.google.com/document-ai/docs/invoice-parser#annotations) by the parser.
  * Increased the number of pages for online processing (10 pages) and offline processing (200 pages).
  * Increased the number of documents per batch in offline processing (50 documents).



v1

Change

**Expense parser (Receipt parser) behavior update**

The expense parser behavior has been updated to include the following features:

  * Renamed Receipt parser to Expense parser.
  * Improved prediction quality.
  * Improved prediction quality for English, French, and Dutch for more expense types (for example hotel statements).



v1

Announcement

**Human in the Loop (HITL) AI General Availability (GA) released**

HITL AI is now available in Private General Availability (GA) for human review of Invoice, Expense, and Utility parser predictions.

**Features:**

  * HITL configuration enhanced to designate which fields need review and whether a field is mandatory, saving review time.
  * Labeler UI highlights the fields below a confidence score and supports single-click confirmation to improve review efficiency.
  * Labeling Manager shows analytics and metrics by task and by labeler to streamline HITL operations.



## April 02, 2021

v1

Feature

**Lending DocAI General Availability (GA) released**

Lending DocAI is now General Availability. See the [documentation](https://docs.cloud.google.com/document-ai/docs) for more information.

v1

Feature

**Lending DocAI processors added**

The following Lending DocAI processors are now available:

  * [Pay stub parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser)
  * [Bank statement parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser)
  * [1040 Schedule C parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_1040-schedule-c-parser)
  * [1099-DIV parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_1099-div-parser)
  * [1099-G parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_1099-g-parser)
  * [1099-INT parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_1099-int-parser)



## March 31, 2021

v1

Feature

**Document AI General availability (GA) released**

Document AI is now General Availability (GA).

## January 14, 2021

v1beta3

Feature

**New Procurement DocAI processor released in limited Preview**

The following Procurement DocAI processor is now available in limited Preview:

  * Procurement document splitter



For more information, see the [processor documentation](https://docs.cloud.google.com/document-ai/docs/procurement-splitter).

## January 11, 2021

v1beta3

Change

**Lending processors behavior update**

The behavior of the following processors has been updated:

  * 1003 parser
  * 1040 parser
  * 1099-MISC parser
  * W2 parser
  * W9 parser



Now, if these processors are given a multi-page input file and contains a page that is the correct document type _and_ one of the supported versions the processor performs entity extraction for that page; subsequent applicable pages will _not_ be processed. If the prcoessor doesn't find any applicable documents in the input file it returns an error message.

## October 29, 2020

v1beta3

Feature

**Document AI Preview released**

The following beta and preview features are available in API version **v1beta3** :

  * **Procurement DocAI processors** : Invoice parser and receipt parser.



## October 16, 2020

v1beta3

Feature

**Document AI Preview released**

The following beta and preview features are available in API version **v1beta3** :

  * **General processors** : Document OCR (Optical Character Recognition), form parser, and document splitter.
  * **Lending processors** : W9, 1040, W2, 1099-MISC, and 1003 parsers, as well as lending document splitter & classifier.



v1beta3

Issue

**`uri` field unavailable**

  * Sending a request with the [`uri`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/Document) field is currently not supported for **v1beta3**. Any updates to the availability of the `uri` field will be announced here.



**Workaround** : Send requests with image information in the `content` field (base64 encoded information).

## August 24, 2020

v1beta2

Change

**Form Parser model updates**

The [Form Parser](https://docs.cloud.google.com/document-ai/docs/process-forms) model has been updated. The model update includes the following features:

  * Improved OCR quality for English detection.
  * Improved key-value pair, checkbox, and table parsing detection quality, particularly for rotated images and handwritten text.
  * Decreased latency for complex tables.



## August 20, 2020

v1beta2

Change

**Invoice Parsing updates**

  * Document AI now supports [normalized values](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta2/Document#normalizedvalue) for certain entities returned from Invoice Parsing requests.
  * We have improved [confidence scores](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta2/Document#entity) for entities returned from Invoice Parsing requests.



## July 04, 2020

v1beta2

Change

**Invoice Parsing Beta model upgrade**

The Invoice Parsing Beta model has been upgraded. This model upgrade results in higher quality results for the [entities](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta2/Document#Entity) and [entityRelations](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta2/Document#EntityRelation). There is no API change.

See the [product documentation](https://cloud.google.com/solutions/document-ai/docs/process-invoices) for more information.

## April 14, 2020

v1beta2

Feature

**Document AI Beta released**

The following beta features are available in API version **v1beta2** :

  * **Document processing** : You can use the API to [parse forms](https://cloud.google.com/solutions/document-ai/docs/process-forms) or [tables](https://cloud.google.com/solutions/document-ai/docs/process-tables) from PDF, TIFF, or GIF documents. 
  * **Regional support** : The API now offers multi-regional support (`us` and `eu`) for all features. [Using a multi-region endpoint](https://cloud.google.com/solutions/document-ai/docs/regions) enables you to configure the API to store and process your data in the United States or European Union.



v1beta2

Feature

**Invoice processing Beta**

  * Invoice processing is now available as a restricted feature. See [Parsing invoices](https://cloud.google.com/solutions/document-ai/docs/process-invoices) for more information.



[ Previous arrow_back  Deprecations  ](https://docs.cloud.google.com/document-ai/docs/deprecation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
