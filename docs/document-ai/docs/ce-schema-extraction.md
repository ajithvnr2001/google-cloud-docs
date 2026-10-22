---
url: https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction/
title: Automated schema generation \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:20.609754+00:00
---

# Automated schema generation  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Automated schema generation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Document AI's automated schema generation lets you automatically generate a document's schema from a test document you supply. Then, you can approve or decline the schema and edit it manually. This saves time and effort when defining the document schema for your custom processor and lets you focus on refining the schema.

Automated schema generation also has a wider knowledge base on creating high quality schemas. This can potentially improve document extraction quality.

## Generate a schema

If you haven't already snapshotted or fine-tuned your processor, take the following steps. 

**Note:** If you've snapshotted or fine-tuned the processor, the option in the first step isn't displayed. The existing fields can't be deleted.

  1. On the **Get started** tab, select **Generate schema from document**. The **Edit schema** page opens.

![cde-schema-generation-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-schema-generation-1.png)

  2. Use the input field to select a local file file to generate the schema, or use the **Browse** option to upload a sample document.

![cde-schema-generation-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-schema-generation-2.png)

**Tip:** Enter a prompt in **Generate a schema prompt** to provide additional input and direction for the generator.
  3. Select **Generate Schema**.

  4. Review the generated schema preview. You can choose accept or reject the schema with **Apply schema** or **Abort schema** , to try again with a different sample document or prompt.

![cde-schema-generation-3](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-schema-generation-3.png)

**Tip:** You can use the **View More** more_vert option by each field to edit the auto-generated schema after applying it.
  5. Optional: If the resulting schema doesn't serve your needs, or requires more than manual editing, you can enter a prompt in **Generate a schema prompt** to provide additional input and direction for the generator. Try prompts such as: specifying the document type, stating the most important parts of the document, or suggesting a target number of entities.




## What's next

  * Learn about [uptraining a specialized processor](https://docs.cloud.google.com/document-ai/docs/uptrain-pretrained-processor).
  * Explore [validation and correction](https://docs.cloud.google.com/document-ai/docs/ce-validation).



[ Previous arrow_back  Custom extractor mechanisms  ](https://docs.cloud.google.com/document-ai/docs/ce-mechanisms)

[ Next Custom-based extraction  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/custom-based-extraction)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
