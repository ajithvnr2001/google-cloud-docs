---
url: https://docs.cloud.google.com/document-ai/docs/ce-validation/
title: Validation and correction \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:23.286426+00:00
---

# Validation and correction  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/ce-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Validation and correction Stay organized with collections  Save and categorize content based on your preferences. 

**Private beta:** This product is in private preview. You need to be on the allowlist to use this product. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Document AI to define custom business rules for validating document processing results. _Validation_ is a document processing process that executes your validation rules on the final extracted entities. _Correction_ is an optional process that attempts to improve extraction results based on the validation rule outcomes, increasing extraction accuracy.

_Validation rules_ can, for example, check if the sum of line item prices equals the total value, verify field consistency across multiple documents, or ensure that extracted fields are spatially aligned in a layout (such as within a horizontal block). Define business rules using the Common Expression Language (CEL), and generate them from natural language prompts.

**Note:** Document AI returns the boolean validation result for each rule.

## Enable validation and correction

You can enable validation and correction independently in the Document AI console. These settings apply to all `processDocument` requests for the selected processor version. However, you can override this behavior for individual requests using parameters in the `processDocument` API call.

Validation and correction configurations, including validation rules, are specific to each processor version. Note that all Google-managed pretrained processor versions share a common base configuration. When you create a new custom processor version (e.g., through fine-tuning), Document AI duplicates the base configuration, attaching it to the new version.

**Note:** Google-managed pretrained processor versions share a common base configuration. When you create a custom processor version (e.g., through fine-tuning), Document AI duplicates the base configuration, attaching it to the new version.

When validation is enabled, the results of all defined validation rules are included in the `ProcessDocument` response for both synchronous and batch requests. Correction can only be enabled if validation is also enabled. Document AI runs the correction process only if at least one validation rule fails for a given document. After correction, Document AI reruns the validation process to provide the final results. The pre- and post-correction validation results are available in the `processDocument` response in a revisions list.

**Caution:** Enabling Correction will likely increase processing latency.

## CEL validation rules

Validation rules are defined using expressions based on the Common Expression Language (CEL). CEL is a non-Turing complete expression language designed for simplicity and safety. Examples of rules you can define:

  * Sum of fields `A` equals field `B`.
  * Field `B` matches a specified regular expression pattern.
  * All subfields of every parent entity are horizontally aligned.



To simplify rule creation, generate CEL rules by providing prompts in natural language. This approach avoids the complexities of CEL syntax. The Document AI implementation of CEL might have slight differences from the standard specification. For detailed descriptions and examples, refer to [CEL rules reference](https://cel.dev/overview/cel-overview).

## Activate validation in the Google Cloud console

  1. In the Google Cloud console for an existing processor, select the **Validation & Correction** entry.

![ce-validation-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-1.png)

  2. Before processing a document, go to **Rule management.**

![ce-validation-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-2.png)

  3. Select the **Enable Validation** toggle.

  4. Optional: select the **Enable Correction** toggle.




### Rule creation

  1. Click **Add Rule**.

![ce-validation-6](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-3.png)

  2. In the rule creation form, enter a natural language prompt.

![ce-validation-5](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-4.png)

  3. Give the rule a name, and use [Common Expression Language (CEL)](https://cel.dev/overview/cel-overview) to define the behavior.

  4. Optional. Use the **edit Edit** or **delete Delete** options to manage existing rules.




### Copy configuration across processors

  1. In the **Rule management** section, click **file_upload Copy to another PV**.

![ce-validation-4](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-5.png)

  2. Select the processor name and version to copy the configuration to.

![ce-validation-3](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-6.png)




### Rule results

  1. In the **Manage Dataset** page, navigate to **Rule management**.

![ce-validation-7](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-7.png)

  2. Evaluate the total passed and failed tests.

  3. Check to see a breakdown of individual rule results.

  4. You can compare changes to see new entities created post correction in green, and modified entities in yellow.

![ce-validation-8](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-8.png)

  5. In the **Evaluate & test** section, there will be columns for scores both before and after activating correction.

![ce-validation-9](https://docs.cloud.google.com/static/document-ai/docs/images/create/ce-validation-9.png)




## Evaluation

Processor version evaluations include key metrics for both post-correction and pre-correction results if correction is enabled. Use these metrics to assess the impact of the correction process on extraction quality.

## What's next

  * Learn about [schema extraction](https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction).
  * Explore [derived signature detection](https://docs.cloud.google.com/document-ai/docs/ce-derived-signature).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
