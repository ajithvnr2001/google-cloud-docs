---
url: https://docs.cloud.google.com/document-ai/docs/enrichment/
title: Enrichment \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:08.600123+00:00
---

# Enrichment  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/enrichment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Enrichment Stay organized with collections  Save and categorize content based on your preferences. 

Document AI uses [Enterprise Knowledge Graph](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview) to normalize and enrich entity extraction results (for supported fields). For example, the addresses `123 Main St Apt 1` and `123 Main street # 1` could be normalized to the same standardized address.

For each supported field, Document AI also returns a [`normalizedValue`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#normalizedvalue) in addition to the raw extracted field, normalizing the literal text. This contains the data in a standardized format to reduce post-processing.

Most data belongs to one of the following categories:

  * Money
  * Date
  * Timestamp
  * Address
  * Boolean
  * Integer
  * Float



## Sample response

The enriched values can be found in the [`entities.normalizedValue`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#NormalizedValue) field as shown in the following truncated sample:
    
    
    {
      "entities": [
        {
          "textAnchor": {
            "textSegments": [ ... ],
            "content": "Google Singapore"
          },
          "type": "employer_name",
          "mentionText": "Google Singapore",
          "confidence": 0.69933707,
          "pageAnchor": {
            "pageRefs": [
              {
                "boundingPoly": {
                  "normalizedVertices": [ ... ]
                }
              }
            ]
          },
          "id": "9",
          "normalizedValue": {
            "text": "Google Asia Pacific, Singapore"
          }
        }
      ]
    }
    

In the sample, the original `employer_name` "Google Singapore" has been normalized to "Google Asia Pacific, Singapore".

In the Google Cloud console, the enriched and normalized fields are annotated with _G_. For example:

![enrichment](https://docs.cloud.google.com/static/document-ai/docs/images/get_started/enrichment-1.png)Sample normalized field shown in the web application. 

## Supported processors

Here are the processors and fields that support entity enrichment.

**Note:** Enriched fields are subject to change with new processor versions. Follow the [Release notes](https://docs.cloud.google.com/document-ai/docs/release-notes) for Document AI updates.

Processors | Enriched fields  
---|---  
  
### Bank Statement Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Lending  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser)  
  
  * `bank_address`
  * `bank_name`

  
  
### W2 Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Lending  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_w2-parser)  
  
  * `EmployerNameAndAddress`
  * `EIN`

  
  
### Pay Slip Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Lending  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser)  
  
  * `employer_address`
  * `employer_name`

  
  
### Expense Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Procurement  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser)  
  
  * `supplier_address`
  * `supplier_name`
  * `supplier_phone`

  
  
### Invoice Parser

| **Category** | Pretrained  
---|---  
**Solution type** | Procurement  
**Functions** | OCR, Entity Extraction  
**[Release stage](https://cloud.google.com/products#product-launch-stages)** | General availability  
**Access status** | Public lock_open  
**Full processor details** | [Detailed entry](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor)  
  
  * `supplier_address`
  * `supplier_name`
  * `supplier_phone`

  
  
[ Previous arrow_back  Setup  ](https://docs.cloud.google.com/document-ai/docs/setup)

[ Next Normalization  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/normalization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
