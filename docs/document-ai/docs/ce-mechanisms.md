---
url: https://docs.cloud.google.com/document-ai/docs/ce-mechanisms/
title: Custom extractor mechanisms \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:20.478475+00:00
---

# Custom extractor mechanisms  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/ce-mechanisms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Custom extractor mechanisms

You can create custom extractors that are specifically suited to your documents, and trained and evaluated with your data. This processor identifies and extracts entities from your documents. You can then use this trained processor on additional documents.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Document AI, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=documentai.googleapis.com,storage.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Document AI, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=documentai.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to create a custom classifier, ask your administrator to grant you the following IAM roles on your project: 

  * [Document AI Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If you want to access input files stored in a different project, then you need to grant additional roles to the Document AI service agent. For more information, see [Cross project file access setup](https://docs.cloud.google.com/document-ai/docs/setup#cross_project_file_access_setup).

## Create a processor

  1. In the Google Cloud console, in the Document AI section, go to the **Workbench** page.

[Workbench](https://console.cloud.google.com/ai/document-ai/workbench)

  2. For **custom extractor** , select **Create processor**.

![updated-cde-2.0-path-to-docai-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-1.png)

  3. In the **Create processor** menu, enter a name for your processor, such as `my-custom-document-extractor`.

![updated-cde-2.0-path-to-docai-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-2.png)

  4. Select the region closest to you.

  5. Optional: Open **Advanced options**.

     * You have the option to let Google create a Cloud Storage bucket for you, or you can [create your own](https://docs.cloud.google.com/storage/docs/creating-buckets). For this tutorial, select **Google-managed storage**.

     * You also have the option to use Google-managed or [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). For this tutorial, select **Google-managed encryption key**.

  6. Select **Create** to create your processor.




## Document-level prompts

A document-level prompt provides a way to describe the document overall to bring deep business knowledge to the model and improve extraction quality. It can contain some general field information, for example: **All the address fields are located in the USA.**

**Tip:** Use the field description for more specific extraction details.

While prompts can provide information to the model, they shouldn't be used to check that rules or conditions are met. Example: **all prices should sum up to the total price.** The document-level prompt is added to the overall prompt and should be treated as document-level hints, rather than a full prompt.

### Provide a document-level prompt

  1. In the Google Cloud console, go to the **Get started** tab.

  2. To input the document prompt click **Edit** near the document prompt input field.

![cde-document-level-prompt-1](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-document-level-prompt-1.png)

  3. In the side-panel, provide a prompt that describes the document as a whole.

![cde-document-level-prompt-2](https://docs.cloud.google.com/static/document-ai/docs/images/create/cde-document-level-prompt-2.png)


**Note:** The prompt is limited to 500 characters, so be clear and concise in your prompt.

## Define processor fields

You are now on the **Processor overview** page of the processor you just created.

![updated-cde-2.0-path-to-docai-3](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-3.png)

You can specify the fields you want the processor to extract and begin labeling documents.

  1. Select the **Get started** tab. The **fields** menu appears.

  2. Select **Create new field**.

  3. Enter the name for the field. Select the **Data type** and the **Occurrence**. Give the label a descriptive, distinct **Description**. Property description lets you provide additional context, insights, and prior knowledge for each entity to improve extraction accuracy and performance.


**Note:** Good examples of property descriptions include location information and text patterns of the property values, which help disambiguate potential sources of confusion in the document, guiding the model with rules that ensure more reliable and consistent extractions, regardless of the specific document structure or content variations.![updated-cde-2.0-path-to-docai-9](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-9.png)

  1. Select **Create**. Refer to [Define processor schema](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#define_processor_schema) for detailed instructions on creating and editing a schema.

**Note:** Generative AI (foundation and fine-tuned) models use the field name and description to form the underlying prompt, so the field names are semantically critical. See [name fields for generative AI extraction](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#name-fields).

  1. Create each of the following labels for the processor schema.

Name | Data Type | Occurrence  
---|---|---  
`control_number` | Number | Optional multiple  
`employees_social_security_number` | Number | Required multiple  
`employer_identification_number` | Number | Required multiple  
`employers_name_address_and_zip_code` | Address | Required multiple  
`federal_income_tax_withheld` | Money | Required multiple  
`social_security_tax_withheld` | Money | Required multiple  
`social_security_wages` | Money | Required multiple  
`wages_tips_other_compensation` | Money | Required multiple  
  
You can also create and use [other types of labels](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#labeling_options) in your processor schema, such as checkboxes and [tabular entities](https://docs.cloud.google.com/document-ai/docs/workbench/create-dataset#parent-child). For example, the W-2 forms contain **statutory employee** , **retirement plan** , and **third party sick pay** check boxes that you could also add to the schema.

![updated-cde-2.0-path-to-docai-4](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-4.png)




## Upload a sample document

Test with a sample document.

  1. Select **Upload sample document**.

  2. In the sidebar, select **Import documents from Cloud Storage**.

  3. For this example, enter this bucket name in **Source path**. This links directly to one document.
         
         cloud-samples-data/documentai/Custom/W2/PDF/W2_XL_input_clean_2950.pdf
         

  4. Select **Import**.




You are redirected to the labeling console.

## Label a document

The process of selecting text in a document and applying labels is known as _annotation_ or _labeling_.

  1. When you're at the labeling console, notice that many of the labels are already populated. This is because the default custom extractor model type is a foundation model, which can perform zero-shot prediction, that is, without training.

**Note:** Your results might look slightly different than the sample image.

![updated-cde-2.0-path-to-docai-5](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-5.png)

  2. To use the suggested labels, hold the pointer over each label in the side panel, and select the check mark to confirm the label is correct. Don't edit the text, even if the OCR reads the text incorrectly.

  3. In this example, the values at the bottom of the document were not identified automatically, so you need to label them manually.

  4. Use the icons in the toolbar above the document to label. Use the **bounding box** tool by default, or the **Select text** tool for multi-line values, to select the content and apply the label.

**Note:** The **select text** tool does not work for all text values, so use the **bounding box** if appropriate. You can also select non-text fields such as checkboxes using the **bounding box** tool.
  5. After text is selected, then a drop-down menu appears with all defined fields (entities) for you to select one. In this example, the value of `wages_tips_other_compensation` is selected with the bounding box tool, and that label is applied.

![updated-cde-2.0-path-to-docai-6](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-6.png)

  6. Review the detected text values to ensure that they reflect the correct location of text for each field. The labeled W2 document should look like this when complete:

![updated-cde-2.0-path-to-docai-7](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-7.png)

**Note:** If we were labeling for production review purposes, then incorrect OCR should be edited.
  7. If needed, you can select **Create new field** to add a new field to the schema from this page.

  8. Select **Mark as labeled** when you have finished annotating the document. You are redirected to the **Get started** tab.




## Build processor version using foundation model

After labeling a single document, you can create a processor version using the pretrained foundation model to extract entities.

  1. Select the **Build** tab.

![updated-cde-2.0-path-to-docai-8](https://docs.cloud.google.com/static/document-ai/docs/images/create/updated-cde-2.0-path-to-docai-8.png)

  2. Under **Call foundation model** , select **Create new version**.

  3. Enter a name for your processor version, such as `w2-foundation-model`.

  4. Select **Create version**. It takes a few minutes to create.

**Note:** After you create a processor version, you can't change or delete fields you have created. You can disable them on the fields page if you no longer need them.
  5. Optional: select the **Deploy & use** tab. On this page, you can view the available processor versions and the deployment status of the new version.




## Use generative AI to auto-label documents

The foundation model can accurately extract fields for a variety of document types, but you can also provide additional training data to improve the accuracy of the model for specific document structures.

Custom extractor uses the label names you define and previous annotations to make it quicker and easier to label documents at scale with [auto-labeling](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#auto-label).

  1. Go to the **Build** page.

  2. Select **Import documents**.

  3. In the sidebar, select **Import documents from Google Cloud Storage**.

  4. Enter this bucket name containing your documents.

  5. From the **Data split** list, select **Auto-split**. This automatically splits the documents to have 80% in the training set and 20% in the test set.

  6. In the **Auto-labeling** section, select the **Import with auto-labeling** checkbox.

  7. Select the foundation model processor version to label the documents.

  8. select **Import** and wait for the documents to import. You can leave this page and return later.

  9. You must verify the auto-labeled documents before you can use them for training or testing. Select **Start labeling** to view the auto-labeled documents.

  10. To use the suggested labels, hold the pointer over each annotation, and select the check mark to confirm the label is correct. For training purposes, don't edit the values if they don't match the document text. Only change the bounding box if the wrong text was selected.

  11. Select **Mark as labeled** when you have finished annotating the document.

  12. Repeat for each auto-labeled document.




## Import prelabeled training documents

  1. Go to the **Build** page.

  2. Select **Import documents**.

  3. In the sidebar, select **Import documents from Cloud Storage**.

  4. Enter your path in **Source path** containing your documents. This bucket should contain prelabeled documents in the [Document JSON](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) format.

  5. From the **Data split** list, select **Auto-split**. This automatically splits the documents to have 80% in the training set, and 20% in the test set. Leave **Import with auto-labeling** unchecked.

  6. Select **Import**. Import takes several minutes.




## Optional: View and manage dataset

  1. From the **Build** page, you can access the **Manage dataset** console to view and edit all documents and labels in the dataset.



## Train custom model based processor

Training might take several hours. Make sure you have set up the processor with the appropriate data and labels before you begin training.

  1. For information about the dataset requirements, under **Train a custom model** , select **Create new version** or **View full requirements**. This is not a generative AI model. At least 10 training instances and 10 test instances of each field are required for a custom model based processor.

  2. In the **Version name** field, enter a name for this processor version, such as `w2-custom-model`.

  3. Optional: select **View label stats** to find information about the document labels. That can help determine your coverage. Select **Close** to return to the training setup.

  4. Under **Model training method** , select **Model based**.

  5. Select **Start training**. Training takes a few hours. You can close this page and come back later.

  6. Optional: select the **Deploy & use** tab. On this page, you can view the available processor versions and the training status of the new version.




## Deploy the processor version

  1. After training is complete, select the **Deploy & use** tab.

  2. Select the checkbox on the left of the version you want to deploy, and select **Deploy**.

  3. Select **Deploy** from the dialog window. Deployment takes a few minutes.

  4. When the version is deployed, you can set it as the **Default version** , or you can provide the version ID when processing documents with the API.




## Evaluate and test the processor

  1. Select the **Evaluate** tab to test the processor version. On this page, you can view evaluation metrics including the F1 score, precision and recall for the full document, and individual labels. For more information about evaluation and statistics, refer to [evaluate processor](https://docs.cloud.google.com/document-ai/docs/workbench/evaluate).

  2. Select the **Version** selector and select the version using the foundation model.

  3. Download a document that has not been involved in previous training or testing so that you can use it to evaluate the processor version. If using your own data, you would use a document set aside for this purpose.

[ file_download Download PDF ](https://storage.googleapis.com/cloud-samples-data/documentai/LendingDocAI/W2Parser/W2_XL_input_clean_1000.pdf)

  4. Select **Upload Test Document** and select the document you just downloaded. The **Custom Document Extractor analysis** page opens. The screen output demonstrates how well the document was extracted.

  5. Test the document again using the version with a custom trained model.




## Use the processor

You have successfully created and trained a custom extractor processor.

You can manage your custom trained processor versions just like any other processor version. For more information, refer to [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).

To use the Document AI API:

  * Follow the code samples in [send a processing request](https://docs.cloud.google.com/document-ai/docs/send-request) to use online or batch processing. 
    * Refer to [Quotas and limits](https://docs.cloud.google.com/document-ai/quotas#processor_limits) for the number of pages supported for online and batch processing.
  * Follow the custom extractor code sample in [Handle the processing response](https://docs.cloud.google.com/document-ai/docs/handle-response#cde) to get the extracted entities from the processor.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your processor and project if you don't need them.

If you created a new project to learn about Document AI and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account:

  1. In the Google Cloud console navigation menu, select **Document AI** and select **My Processors**. 

  2. Select **More actions** in the same row as the processor you want to delete.

  3. Select **Delete processor** , enter the processor name, then select **Delete** again to confirm.




## What's next

For details, see [Guides](https://docs.cloud.google.com/document-ai/docs/how-to). Explore [automated schema extraction](https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction). For automated version upgrades, see [](https://docs.cloud.google.com/document-ai/docs/training-overview#upgrade-ui)

[ Previous arrow_back  Custom extractor overview  ](https://docs.cloud.google.com/document-ai/docs/custom-extractor-overview)

[ Next Automated schema extraction  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/ce-schema-extraction)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
