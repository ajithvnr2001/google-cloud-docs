---
url: https://docs.cloud.google.com/document-ai/docs/ce-derived-signature/
title: Custom extractor with generative AI \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:57.340305+00:00
---

# Custom extractor with generative AI  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/ce-derived-signature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Custom extractor with generative AI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Derived field and signature detection

The [public preview](https://cloud.google.com/products#product-launch-stages) derived fields feature enables Document AI customers to configure a field to be populated through intelligent inference or generation based on document context, rather than direct text extraction.

This release also adds another feature to detect the presence of signatures in documents. You can use the new `signature` entity type to specify a schema for such entities. The signature entities are derived using visual cues from the document.

## Derived fields in the custom extractor

Custom extractor supports derived fields in the following models:

  * `pretrained-foundation-model-v1.5-2025-05-05` as Preview
  * `pretrained-foundation-model-v1.5-pro-2025-06-20` as Preview
  * `pretrained-foundation-model-v3.5-2026-05-26` as Preview



You can enable these features in the console UI when creating or editing labels in your document schema.

_Derived Fields_ is a powerful feature that lets you extract information that isn't explicitly written in a document. This lets you configure a field to be populated through intelligent inference or generation based on the document's overall context. This goes beyond rudimentary text extraction and supports advanced use cases, such as:

  * Deducing the country from an address.
  * Counting the total number of items in a table.
  * Detecting if an ID card is a "Real ID".



## Schema creation example

Here is an example of creating a schema for derived fields for such use cases and the expected output, using a [US driver's license](https://storage.googleapis.com/cloud-samples-data/documentai/codelabs/specialized-processors/license.pdf).

  1. Select the `Derived` method when creating a schema element.

![cde-signature-detection-derived-field-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-1.png)

  2. Add descriptive labels to improve performance.

![cde-signature-detection-derived-field-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-2.png)

  3. Derived fields such as signatures don't require setting bounding boxes when labeling documents. For **Value** , select **Detected**.

![cde-signature-detection-derived-field-3](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-3.png)

  4. For derived fields other than signatures, you can enter any **Value** as part of labeling to define the possible outputs.

![cde-signature-detection-derived-field-4](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-4.png)




The expected output will look similar to this, with the presence of a signature returned as "Detected" or "", and derived fields returned as text as the label's description prompts request.

![cde-signature-detection-derived-field-5](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-5.png)

### Extract versus derived overview

When you define an entity in your processor schema, you can choose a method for how its value is populated.

  * **Extract:** This is the default method. It works when the entity's value should be extracted directly from the document text. The system identifies the text and populates fields like `textAnchor` and `pageAnchor` to show its location.

  * **Derived:** This method is used when the entity's value needs to be inferred from the document's content. Since the value is not directly present in the text, the `textAnchor` and `pageAnchor` fields aren't populated.




### Example use case: finding a currency code

Imagine you need to identify the currency code (for example, USD, CAD, EUR) for transactions in your documents.

  * **When to use`Extract`**: If the documents consistently contain unambiguous currency symbols or codes like "USD" or "€", use the `Extract` method to find and extract that exact text.

  * **When to use`Derived`**: If a document uses an ambiguous symbol like "$" (which could refer to USD, CAD, AUD, etc.) or has no symbol at all, use the `Derived` method. The model analyzes the document's context—such as a billing address or company location—to infer the correct ISO 4217 currency code.




### Example use case: custom normalization instructions

Imagine you need to extract information from the document in a different format than the rest of the document. Most use cases should already be handled by [normalization logic](https://docs.cloud.google.com/document-ai/docs/normalization). For edge cases which aren't covered, these entities can be returned in a custom output format you define using derived fields. For example, you can strip dashes from numbers using the prompt: _Return the number without all non-numeric characters._

![cde-signature-detection-derived-field-6](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-derived-signature-6.png)

Similarly, the invoice date can be normalized using a derived field with the description: _Return the invoice date in yyyy-mm-dd (ISO 8601) format. The date format in the invoice will be in local date format. Use the invoice origin country to derive the local date format._

### Configuration best practices

To get the best results with derived fields, we strongly recommend that you write a clear, instructional `description` for the property in your schema during [labeling](https://docs.cloud.google.com/document-ai/docs/label-documents). This helps to guide the model in its derivation task.

In the currency code example, you can create a field with the name `currency_code` and provide the following description: "Find the ISO 4217 currency code of the amount values in the document, using contextual signals present in the document, like currency symbols and addresses."

### Limitations

Derived fields are generated on a per-page basis. This means that use cases requiring information from across multiple pages are not fully supported. For example, if you configure a derived field to summarize a document, it generates a separate summary for each individual page rather than one cohesive summary for the entire document. This limitation applies to any field where the value must be derived using cross-page information.

## Signature detection in custom extractor

Document AI's custom extractor supports signature detection in custom extractor models `pretrained-foundation-model-v1.4-2025-02-05` and `pretrained-foundation-model-v1.5-2025-05-05`. You can enable this feature in the console UI when creating or editing labels in your document schema.

**Signature detection** is a feature that lets you determine if a signature is present in your documents. This feature verifies that a signature exists by analyzing visual cues, rather than extracting text.

### How signature detection works

To enable this functionality, a `signature` data type is available when defining your processor schema. The processor's behavior depends on whether a signature is detected in the document.

If a signature is found, the extractor returns a signature entity in its response. For a field named `has_signed`, the response object has the following structure:
    
    
    "has_signed": {
      "mention_text": "Detected",
      "confidence": <confidence_score_between 0 to 1>,
      "normalized_value": {
        "text": "Detected",
        "signature_value": true
      }
    }
    

If a signature isn't found, the entity isn't returned in the processor's response.

### Configure and set up key requirements

To set up signature detection:

  1. **Define the schema:** In your processor schema, add a new entity for the signature you want to detect.
  2. **Set data type:** Select Signature as the data type for this new entity.
  3. **Set method to derived:** Entities with the `signature` data type can only use the `Derived` method. Because the model infers the signature's presence visually, it doesn't extract a text value. Therefore, fields like `textAnchor` and `pageAnchor` aren't populated for signature entities.

**Note:** Signature detection is only possible if the `Derived` method is set.

### Example use case

Imagine you are processing contracts and need to verify that they have been signed. You can create a schema field named `is_contract_signed` and set its data type to `signature`. When you process a signed contract, the response includes an `is_contract_signed` entity, confirming the signature's presence. If no signature is present, this entity is absent from the response. This lets you quickly flag unsigned documents for review.

## What's next

Learn about [uptraining a specialized processor](https://docs.cloud.google.com/document-ai/docs/uptrain-pretrained-processor).

[ Previous arrow_back  Custom extractor with generative AI  ](https://docs.cloud.google.com/document-ai/docs/ce-with-genai)

[ Next CEL dialect for document validation  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/ce-cel-validation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
