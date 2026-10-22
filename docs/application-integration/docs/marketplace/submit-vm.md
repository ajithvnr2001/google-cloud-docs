---
url: https://docs.cloud.google.com/application-integration/docs/marketplace/submit-vm/
title: Submit the VM image for approval \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:25.929825+00:00
---

# Submit the VM image for approval  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/marketplace/submit-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Submit the VM image for approval

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to submit the virtual machine (VM) image for approval in the Producer Portal.

## Submit the VM image

  1. Add a new product on the [Producer Portal](https://console.cloud.google.com/producer-portal/overview). **Note:** If you can't access Producer Portal, verify that you've selected the correct project. If you still can't access it, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Application Integration](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. Select Virtual Machine as the product type and provide a unique name for the product. Follow these guidelines for the product name and product overview: 
     * The product name must match the application or soure for which you build the connector. For example, if you build a connector for Salesforce, use Salesforce in the product name.
     * Don't use reserved keywords such as "plugin" in the product name.
     * The product overview must mention that this product is for Integration Connectors or Application Integration. 
  3. Specify the product details. For guidelines about how to enter the product details, see [Add product details](https://docs.cloud.google.com/marketplace/docs/partners/vm/set-up-environment#add_product_details). 
  4. Create the deployment package.
  5. Select a [pricing model](https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing).
  6. [Submit your product to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/vm/submitting). 



### Create the deployment package

  1. Select the VM image created earlier in the **Deployment Image Source** section. This image must be the same as the image mentioned in the autogen configuration.
  2. For the deployment package, select **Manual configuration for more complex products**. You can't use guided configuration as this product requires a startup script.
  3. In the **Type** section, select **Custom (UI deployment)**.
  4. In the **Image Variable** field, enter `source_image`.
  5. To upload the deployment package, do the following: 
     1. Create a [ Cloud Storage bucket](https://console.cloud.google.com/storage/create-bucket).
     2. To zip the terraform module, run the following command: 
            
            cd solution_folder
              zip .zip ./*
              

Ensure that only the files are zipped and not the parent folder.

     3. To upload the zip file to the Cloud Storage bucket, run the following command: 
            
            gcloud storage cp MODULE_NAME.zip gs://BUCKET_NAME
              

  6. In the Producer Portal, in the **Specify your GCS object location** field, browse and select the uploaded object.
  7. In the **Required roles** section, select the role for the Compute Admin role (`roles/compute.admin`).
  8. To validate the deployment module, click **Validate**.
  9. To view the UI and deploy the VM product for testing, click **Deployment preview**. This page will be the same as what the consumers will see while setting up the connector VM.



## What's next

  * Learn how to [submit a publish request for the connector](https://docs.cloud.google.com/integration-connectors/docs/marketplace/publish-custom-connector).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
