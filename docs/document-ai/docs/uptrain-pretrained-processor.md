---
url: https://docs.cloud.google.com/document-ai/docs/uptrain-pretrained-processor/
title: Uptrain a pretrained processor \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:16.542313+00:00
---

# Uptrain a pretrained processor  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/uptrain-pretrained-processor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Uptrain a pretrained processor

Using the [Invoice Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor), you can uptrain a pretrained processor to improve accuracy. You begin with a pre-made model, then train it with your data, adding custom fields. Invoice formats are diverse, and uptraining a generic Invoice Parser with your data can improve accuracy on specific formats and allow the parser to extract fields that aren't supported by the pre-trained model. Sample data is provided, but you can follow the same procedures using your own data.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/ai/document-ai?tutorial=document-ai--documentai-workbench_uptraining_console)

* * *

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

To get the permissions that you need to uptrain a pretrained processor, ask your administrator to grant you the following IAM roles on your project: 

  * [Document AI Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If you want to access input files stored in a different project, then you need to grant additional roles to the Document AI service agent. For more information, see [Cross project file access setup](https://docs.cloud.google.com/document-ai/docs/setup#cross_project_file_access_setup).

## Create a processor

  1. In the Google Cloud console navigation menu, select **Document AI** and select **Processor Gallery**.

[Processor Gallery](https://console.cloud.google.com/ai/document-ai/processor-library)

  2. In the **Processor Gallery** , search for**Invoice Parser** and select **Create**.

![uptrain-a-legacy-processor-1](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-1.png)

  3. Enter a **Processor name** , such as `invoice-parser-for-uptraining`.

  4. Select the region closest to you.

  5. Select **Create**. The **Processor Details** tab appears.

![uptrain-a-legacy-processor-2](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-2.png)




## Create a Cloud Storage bucket for the dataset

In order to train this new processor, you must create a dataset with training and testing data to help the processor identify the entities that you want to extract.

This dataset requires a new [Cloud Storage bucket](https://docs.cloud.google.com/storage). Don't use the same bucket as the one where your documents are stored.

  1. Go to your processor's **Train** tab.

  2. Select **Set Dataset Location**. You are prompted to select or create an empty Cloud Storage bucket or folder.

![uptrain-a-legacy-processor-3](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-3.png)

  3. Select **Browse** to open **Select folder**.

  4. Select **Create a new bucket** and follow the prompts to create a new bucket. For more information on creating a Cloud Storage bucket, refer to [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

**Note:** A bucket is the top-level storage entity, in which you can nest folders. Instead of creating and selecting a bucket, you could also create and select an empty folder inside an existing bucket, if you prefer. Refer to [simulated folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders).

After you create the bucket, the **Select folder** page appears for that bucket.

  5. On the **Select folder** page for your bucket, select the **Select** at the bottom of the dialog.

![uptrain-a-legacy-processor-4](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-4.png)

  6. Make sure the **destination path** is populated with the bucket name you selected. Select **Create Dataset**. The dataset might take up to several minutes to create.

![uptrain-a-legacy-processor-5](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-5.png)



  * **Proceed directly to uptraining** : Skip to import pre-labeled data. Instead of importing a sample document, use tools to manually label the fields, and add the document to the training data.

  * **Manually label and add documents to the training set** : Before you proceed with uptraining, continue to Import a sample document for manual labeling, completing the instructions there.




## Import a sample document for manual labeling

Next, import a sample invoice PDF file into your dataset. You label the fields in this document to assist the subsequent uptraining process.

In this guide, you are provided with a representative file to be the sample document.

  1. On the **Train** tab, select **Import documents**.

![uptrain-a-legacy-processor-6](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-6.png)

  2. For this example, enter this bucket name in **Source path**. This links directly to one document.
         
         cloud-samples-data/documentai/codelabs/uptraining/pdfs
         

  3. For **Data split** , select **Unassigned**. The document in this folder is not assigned to either the testing or training set. Leave **Import with auto-labeling** unchecked.

  4. Select **Import**. Document AI reads the documents from the bucket into the dataset. It does not modify the import bucket or read from the bucket after the import is complete.




When you import documents, you can optionally assign the documents to the **Training** or **Test** set when imported, or wait to assign them later.

If you want to delete a document or documents that you have imported, select them on the **Train** tab, and select **Delete**.

For more information about preparing your data for import, refer to the [Data preparation guide](https://docs.cloud.google.com/document-ai/docs/workbench/create-dataset).

## Define processor schema

Your dataset might not contain all of the labels supported by the Invoice Parser. If so, you must mark the labels that aren't used as `Inactive` before you begin training. You can also add one or more custom labels before you begin uptraining.

  1. On the **Train** tab, select **Edit Schema** in the lower left. The **Manage labels** page opens.

  2. To disable unused labels, select the checkboxes for the fields that are **not** on the following list, and then select **Disable**. The following fields should remain enabled:
         
         invoice_date
         line_item
           amount
           description
         receiver_address
         receiver_name
         supplier_address
         supplier_name
         total_amount
         

**Note:** Labels cannot be deleted. Instead, you can disable any label you don't want to use.

  3. Select **Save** when the labels are complete.

![uptrain-a-legacy-processor-7](https://docs.cloud.google.com/static/document-ai/docs/images/manage/uptrain-a-legacy-processor-7.png)

  4. Select the **Back Arrow** to return to the **Train** page.




## Label a document

The process of selecting text in a document, and applying labels is known as _annotation_.

  1. Return to the **Train** tab, and select a document to open the **Label management** console.

  2. Next, you select from the schema label in the left-hand panel that corresponds to the value you want to annotate, and apply the label.

  3. Use the **Bounding box** tool by default, or the **Select text** tool for multi-line values, to select the content and apply the label.

For example, in this invoice, the text "McWilliam Piping International Piping Company" should be assigned the label `supplier_name`. You can use the text filter to search for label names.

**Note:** The **Select text** tool does not work for all text values, so use the **Bounding box** if appropriate. You can also select non-text fields such as checkboxes using the **Bounding box** tool.

  4. Review the detected text values to ensure that they reflect the correct text from the document.

     * When you select text that corresponds to a label, make sure you include only the relevant text. For example, for an `invoice_id` label, don't include characters like `#` that often precede the numeric value. Don't include currency symbols like `$` for money.

       * Make sure you annotate all instances of an entity. For example, `supplier_name` or `invoice_id` might occur multiple times in the document, and each instance should be annotated.
  5. Repeat for each field that you want to label.




Here is an example of the full set of labels with corresponding text.

**Label Name** | **Text**  
---|---  
`supplier_name` | McWilliam Piping International Piping Company  
`supplier_address` | 14368 Pipeline Ave Chino, CA 91710  
`invoice_id` | 10001  
`due_date` | 2020-01-02  
`line_item/description` | Knuckle Couplers  
`line_item/quantity` | 9  
`line_item/unit_price` | 74.43  
`line_item/amount` | 669.87  
`line_item/description` | PVC Pipe 12 Inch  
`line_item/quantity` | 7  
`line_item/unit_price` | 15.90  
`line_item/amount` | 111.30  
`line_item/description` | Copper Pipe  
`line_item/quantity` | 7  
`line_item/unit_price` | 91.20  
`line_item/amount` | 638.40  
`net_amount` | 1,419.57  
`total_tax_amount` | 113.57  
`total_amount` | 1,533.14  
`currency` | $  
  
  1. Select **Mark as Labeled** when you have finished annotating the document.

On the **Train** tab, the left-hand panel shows that 1 document has been labeled.




## Assign annotated document to the training set

Now that you have labeled this example document, you can assign it to the training set.

  1. On the **Train** tab, select the **Select All** checkbox.

  2. From the **Assign to Set** list, select **Training**.




In the left-hand panel, you can find that 1 document has been assigned to the training set.

## Import pre-labeled data to the training and test sets

Document AI uptraining requires a minimum of 10 documents in both the training and test sets, along with 10 instances of each label in each set.

It's recommended that you have at least 50 documents in each set, with 50 instances of each label, for best performance. More training data generally equates to higher accuracy.

In this guide, you are provided with pre-labeled data. If working on your own project, you have to determine how to label your data. Refer to [Labeling options](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#labeling_options).

  1. Select **Import documents**.

  2. Enter the following path in **Source path**. This bucket contains pre-labeled documents in the [Document JSON](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) format.
         
         cloud-samples-data/documentai/Custom/Invoices/JSON
         

  3. From the **Data split** list, select **Auto-split**. This automatically splits the documents to have 80% in the training set, and 20% in the test set. Leave **Import with auto-labeling** unchecked.

  4. Select **Import**. The import might take several minutes. Afterward, you find the documents on the **Train** tab.




## Optional: Auto-label newly imported documents

When importing unlabeled documents for a processor with an existing deployed processor version, you can use [Auto-labeling](https://docs.cloud.google.com/document-ai/docs/workbench/label-documents#auto-label) to save time on labeling.

  1. On the **Train** page, **Import documents**.

  2. Copy and paste the following Cloud Storage path. This directory contains five unlabeled invoice PDFs. From the **Data split** drop-down list, select **Training**.
         
         cloud-samples-data/documentai/Custom/Invoices/PDF_Unlabeled
         

  3. In the **Auto-labeling** section, select the **Import with auto-labeling** checkbox.

  4. Select an existing processor version to label the documents.

     * For example: `pretrained-invoice-v1.3-2022-07-15`
  5. Select **Import** and wait for the documents to import. You can leave this page and return later.

     * When complete, the documents appear in the **Train** page in the **Auto-labeled** section.
  6. You cannot use auto-labeled documents for training or testing without marking them as labeled. Go to the **Auto-labeled** section to view the auto-labeled documents.

  7. Select the first document to enter the labeling console.

  8. Verify the label to ensure it is correct. Adjust if it is incorrect.

  9. Select **Mark as Labeled** when finished.

  10. Repeat the label verification for each auto-labeled document, then return to the **Train** page to use the data for training.




## Train the processor

Now that you have imported the training and test data, you can train the processor. Because training might take several hours, make sure you have set up the processor with the appropriate data and labels before you begin training.

  1. Select **Uptrain New Version**.

  2. In the **Version name** field, enter a name for this processor version, such as `invoice-uptrain-1`.

  3. (Optional) Select **View Label Stats** to find information about the document labels. That can help determine your coverage. Select **Close** to return to the training setup.

  4. Select **Start training** You can check the status on the right-hand panel.

The **Dataset management** page opens. You can view the training status on the right side. Training will likely take a few to several hours, depending on the size of your dataset. You can leave this page and return later.




## Deploy the processor version

  1. After training is complete, navigate to the **Manage Versions** tab. You can view details about the version you just trained.

  2. Select the three vertical dots on the right of the version you want to deploy, and select **Deploy version**.

  3. Select **Deploy** from the popup window.

Deployment takes a few minutes to complete.




## Evaluate and test the processor

  1. After deployment is complete, navigate to the **Evaluate & Test** tab.

On this page, you can view evaluation metrics including the F1 score, Precision and Recall for the full document, and individual labels. For more information about evaluation and statistics, refer to [Evaluate processor](https://docs.cloud.google.com/document-ai/docs/workbench/evaluate).

  2. Download a document that has not been involved in previous training or testing so that you can use it to evaluate the processor version. If using your own data, you would use a document set aside for this purpose.

[ file_download Download PDF ](https://storage.googleapis.com/cloud-samples-data/documentai/Custom/Invoices/ams.pdf)

  3. Select **Upload Test Document** and select the document you just downloaded.

The **Invoice Parser analysis** page opens. The screen output demonstrate how well the document was classified.

You can also re-run the evaluation against a different test set or processor version.




## Use the processor

You have successfully created and uptrained an Invoice Parser processor.

You can manage your custom-trained processor versions just like any other processor version, such as when migrating to a newer processor when one is deprecated. For more information, refer to [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions).

You can [Send a processing request](https://docs.cloud.google.com/document-ai/docs/send-request) to your custom processor, and the [response can be handled the same as other entity extraction processors](https://docs.cloud.google.com/document-ai/docs/handle-response#entities_nested_entities_and_normalized_values).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your processor and project if you don't need them.

If you created a new project to learn about Document AI and you no longer need the project, [delete the project][delete-project].

If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account:

  1. In the Google Cloud console navigation menu, select **Document AI** and select **My Processors**. 

  2. Select **More actions** in the same row as the processor you want to delete.

  3. Select **Delete processor** , enter the processor name, then select **Delete** again to confirm.




## What's next

  * [Document AI Python Client Library](https://docs.cloud.google.com/python/docs/reference/documentai/latest)
  * [Document AI Samples](https://github.com/GoogleCloudPlatform/document-ai-samples)



[ Previous arrow_back  Train and evaluate  ](https://docs.cloud.google.com/document-ai/docs/training-overview)

[ Next Evaluate performance  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/evaluate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
