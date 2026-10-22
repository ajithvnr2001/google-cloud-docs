---
url: https://docs.cloud.google.com/document-ai/docs/workflows/
title: Build a document processing pipeline with Workflows \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:41.931416+00:00
---

# Build a document processing pipeline with Workflows  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build a document processing pipeline with Workflows

If you are using Document AI to build workflows that involve several steps to process documents, you might want to use serverless orchestration to manage your workflow.

[Workflows](https://docs.cloud.google.com/workflows) links a series of tasks together in an order you define. It requires no infrastructure management and scales seamlessly on demand, including scaling down to zero. With its pay-per-use pricing model, you only pay for execution time.

Workflows provides a built-in [connector for the Document AI API](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/Overview). Connectors don't require additional code aside from defining the steps using a config file. Connectors handle the formatting of requests, hiding the details of the API. Connectors also provide built-in behavior for authentication, handling retries and [long-running operations](https://docs.cloud.google.com/workflows/docs/connectors#lro).

For more information, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

This guide processes a set of sample invoices using the [Invoice Parser](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor) processor with [batch processing](https://docs.cloud.google.com/document-ai/docs/send-request#batch-process)

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/ai/document-ai?tutorial=document-ai--documentai_workflows)

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

  5. Enable the Document AI, Cloud Storage, Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=documentai.googleapis.com,storage.googleapis.com,workflows.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Document AI, Cloud Storage, Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=documentai.googleapis.com,storage.googleapis.com,workflows.googleapis.com)




### Required roles

To get the permissions that you need to create a custom classifier, ask your administrator to grant you the following IAM roles on your project: 

  * [Document AI Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Workflows Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.editor) (`roles/workflows.editor`)
  * Create a new service account: [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** If you want to access input files stored in a different project, then you need to grant additional roles to the Document AI service agent. For more information, see [Cross project file access setup](https://docs.cloud.google.com/document-ai/docs/setup#cross_project_file_access_setup).

## Create an Invoice Parser

Use the Google Cloud console to create a new Invoice Parser. Refer to the [creating and managing processors](https://docs.cloud.google.com/document-ai/docs/create-processor) page for more information.

  1. In the Google Cloud console navigation menu, click **Document AI** and select **Processor Gallery**.

[Processor Gallery](https://console.cloud.google.com/ai/document-ai/processor-library)

  2. In the **Processor Gallery** , search for**Invoice Parser** and select **Create**.

![Create invoice
processor](https://docs.cloud.google.com/static/document-ai/docs/images/create-invoice-parser.png)

  3. Enter a **Processor name** , such as `workflows-invoice-processor`.

  4. Select the region (`location` in the Document AI API) to host the processor.

  5. Click **Create**. The **Processor Details** tab appears.

  6. Copy your **Processor ID**. You must use this in your code later.

![Processor ID](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/GetProcessorID.png)




## Configure output bucket in Cloud Storage

When using [batch (asynchronous) processing](https://docs.cloud.google.com/document-ai/docs/send-request#batch-process), the input and output files must be stored in Cloud Storage. The following bucket contains sample files to use as input for this guide:
    
    
    gs://cloud-samples-data/documentai/workflows
    

Configure a bucket to store the output files in your project.

  1. Follow the [Create Buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) guide in the Cloud Storage documentation to create a bucket, or use a bucket that already exists.

  2. Create a [folder](https://docs.cloud.google.com/storage/docs/objects#simulated-folders) in the bucket (for example, `docai-workflows-output`).




## Create workflow

  1. Open the **Workflows dashboard** in the Google Cloud console.

[Go to the Workflows dashboard](https://console.cloud.google.com/workflows)

  2. Click **Create** to create your first workflow. The **Create Workflow** page appears.

![Workflows Create](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/WorkflowsCreate.png)

  3. Rename the workflow to `docai-workflows-quickstart`.

  4. Add a description, and select a service account if you have one for this project.

     1. If you don't have a service account, select **Create New Service Account**. 
        * Name your service account, and select **Create and Continue**. ![CreateServiceAccount](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/CreateServiceAccount.png)
        * Give it the following roles:
        * `Document AI API User`
        * `Workflows Invoker`
        * `Logs Writer`
        * `Service Usage Consumer`
        * ![ServiceAccountRoles](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/ServiceAccountRoles.png)
  5. On the **Create Workflow** page, click **Next**.




## Define workflow

  1. In the **Workflows editor** , clear the default YAML and paste in the code below:
         
         main:
           params: [input]
           steps:
             - start:
                 call: sys.log
                 args:
                   text: ${input}
             - vars:
                 assign:
                   - input_gcs_bucket: ${input.inputBucket}
                   - output_gcs_bucket: ${input.outputBucket}
                   - processor_id: ${input.processorId}
                   - location: ${input.location}
                   - project_id: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
             - batch_process:
                 call: googleapis.documentai.v1.projects.locations.processors.batchProcess
                 args:
                   name: ${"projects/" + project_id + "/locations/" + location + "/processors/" + processor_id}
                   location: ${location}
                   body:
                     inputDocuments:
                       gcsPrefix:
                         gcsUriPrefix: ${input_gcs_bucket}
                     documentOutputConfig:
                       gcsOutputConfig:
                         gcsUri: ${output_gcs_bucket}
                     skipHumanReview: true
                 result: batch_process_resp
             - return:
                 return: ${batch_process_resp}
         


![WorkflowsEditor](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/WorkflowsEditor.png)

  1. Select **Deploy**.



## Test workflow

Now that the workflow has been deployed, you should be on the **Workflow details** page.

  1. Click **Execute** at the top of the page to go to the **Execute workflow** page. This page allows you to test your workflow in the console.

  2. Replace the placeholder variables in the following input JSON:

     * OUTPUT_BUCKET_PATH: The full path to output bucket and folder created earlier.
     * PROCESSOR_ID: The processor ID for the processor created earlier.
     * LOCATION: The region for the processor created earlier.
    
    {
      "inputBucket": "gs://cloud-samples-data/documentai/workflows",
      "outputBucket": "OUTPUT_BUCKET_PATH",
      "processorId": "PROCESSOR_ID",
      "location": "LOCATION"
    }
    

  3. Copy/Paste the JSON into the **input textbox**.

  4. Click **Execute** at the bottom of the workflow to test your input and wait for a moment for the process to complete.

  5. Once the workflow finishes, the output JSON should look something like this.
         
         {
           "done": true,
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessMetadata",
             "createTime": "2023-02-24T18:31:18.521764Z",
             "individualProcessStatuses": [
               {
                 "humanReviewStatus": {
                   "state": "SKIPPED"
                 },
                 "inputGcsSource": "gs://cloud-samples-data/documentai/workflows/baking_technologies_invoice.pdf",
                 "outputGcsDestination": "OUTPUT_BUCKET_PATH/11119195367705871803/0",
                 "status": {}
               },
               {
                 "humanReviewStatus": {
                   "state": "SKIPPED"
                 },
                 "inputGcsSource": "gs://cloud-samples-data/documentai/workflows/generic_invoice.pdf",
                 "outputGcsDestination": "OUTPUT_BUCKET_PATH/11119195367705871803/1",
                 "status": {}
               },
               {
                 "humanReviewStatus": {
                   "state": "SKIPPED"
                 },
                 "inputGcsSource": "gs://cloud-samples-data/documentai/workflows/google_invoice.pdf",
                 "outputGcsDestination": "OUTPUT_BUCKET_PATH/11119195367705871803/2",
                 "status": {}
               }
             ],
             "state": "SUCCEEDED",
             "updateTime": "2023-02-24T18:31:52.543163Z"
           },
           "name": "projects/PROJECT_ID/locations/LOCATION/operations/11119195367705871803",
           "response": {
             "@type": "type.googleapis.com/google.cloud.documentai.v1.BatchProcessResponse"
           }
         }
         

  6. Open your output storage bucket, you will see the output for each invoice processed in a folder named after the Operation ID. ![BatchGCSOutput](https://docs.cloud.google.com/static/document-ai/docs/images/workflows/BatchGCSOutput.png)

  7. Within this folder there will be subfolders, one for each document processed from the input batch containing [`Document`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) JSON file(s).

  8. You may inspect each JSON file or write code to use the relevant fields for your use case. Refer to the [handle the processing response guide](https://docs.cloud.google.com/document-ai/docs/handle-response) for more information.

  9. You can now link additional steps in the workflow to further process the output, such as inserting the extracted entities into a database for analytics.

  10. Refer to the [Workflows Documentation](https://docs.cloud.google.com/workflows/docs/overview) for more information on how to trigger workflows.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your processor, bucket, workflow, and project if you do not need them.

## What's next

  * Learn more about [Workflows](https://docs.cloud.google.com/workflows/docs/overview)
  * Learn more about the [Document AI Workflows Connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/Overview)
  * See a list and descriptions of currently [available processors](https://docs.cloud.google.com/document-ai/docs/processor-overview).
  * Learn how to [handle the processing response](https://docs.cloud.google.com/document-ai/docs/handle-response).



[ Previous arrow_back  Custom metadata  ](https://docs.cloud.google.com/document-ai/docs/custom-metadata-labels)

[ Next Manage processor versions  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
