---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-terraform-deployment/
title: Configure your VM image for Terraform deployment \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:26.071331+00:00
---

# Configure your VM image for Terraform deployment  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-terraform-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Configure your VM image for Terraform deployment Stay organized with collections  Save and categorize content based on your preferences. 

This article describes how to finish configuring and submit your VM image for deployment using Terraform.

## Determine how to create your deployment package

We recommend that you use Producer Portal's guided configuration option to create your deployment package directly in the Google Cloud console.

The guided configuration option supports simple VM products, such as single-VM deployments with basic firewall rules, but it doesn't support some complex features, such as deployments with multiple VMs and non-compute resources. If you need features that the guided configuration doesn't support, you can use the manual configuration option to either create your deployment package or to customize an existing package by adding additional capabilities to it.

### Switch between guided configuration and manual configuration

If you use Producer Portal's guided configuration option and later want to switch to manually configuring your deployment package, click **Go to manual configuration**.

## Complete your guided configuration

To finish configuring and submit a simple deployment package using the Google Cloud console, complete the following steps:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Terraform configuration** , next to the input field labeled **Cloud Storage Bucket** , click **Browse**.

If you've already created a Cloud Storage bucket, select it here.

If you don't have a Cloud Storage bucket, click the icon labeled **Create new bucket**. When you create a new bucket, you:

     * Select a name for the bucket.

     * Specify what region or regions the bucket stores data in.

     * Specify the storage class for your data.

     * Determine what level of granularity to apply to the Identity and Access Management (IAM) permissions for the bucket's data.

     * Configure optional advanced settings, such as encryption or data retention policies.

  3. Ensure that you [enable Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) for your Cloud Storage bucket.

  4. To save your bucket settings and continue configuring your deployment package, click **Configure**.

  5. Under **Choose the machine type** , you must specify a **Default zone** , **Minimum machine type** , and **Default machine type** for your VM product, along with the size and type of its boot disk.

  6. Under **Specify operating system** , you must specify the name and version of the OS your VM image uses, as well as the version number of the VM image.

  7. Optionally, under **Set up VM access** , you can specify site and administrator URLs, along with a username and password, that users can use to access the VM after deployment.

  8. Optionally, under **Configure networking** , you can specify settings for **IP forwarding** and configure **Firewall** rules.

  9. Optionally, under **Define next steps** , you can provide instructions for your product's users to guide them on getting started with your product. These instructions will be visible to them after they deploy your product.

  10. After you complete the previous steps, click **Generate** to create your deployment package.

If you need to make additional changes to your deployment package later, you can click **Edit** to make changes, and then click **Generate** to regenerate your deployment package with those changes applied.

  11. Validate the deployment package in Producer Portal.

  12. After Cloud Marketplace's validation of your deployment package has successfully completed, click **Publish** to start testing your deployment package.




## Complete your manual configuration

This section explains how to use the manual configuration option to create a deployment package and submit the package for review.

### Specify whether to use the default or a custom Terraform module

You can choose whether you want your customers to use the default or a custom Terraform module when they deploy your product.

If you choose to use the default Terraform module, Google Cloud provides your customers with autogenerated Terraform code that they can use to deploy your product.

If you choose to use a custom Terraform module, you must provide your own Terraform templates to your customer. You can choose to provide these templates in a form that customers can deploy by using the command-line interface (CLI), or with additional metadata that lets customers deploy modules directly from Cloud Marketplace.

To specify whether your customers should use the default or a custom Terraform module, and, for custom Terraform modules, how you want your customers to deploy the module, complete the following steps:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Terraform configuration** , under **Type** , select **Default** , **Custom (CLI deployment)** , or **Custom (UI deployment)**.




#### Requirements for custom Terraform modules

If you select to use custom Terraform modules, your custom module must meet the following requirements:

  * Your custom module must have a module which Cloud Marketplace can use to verify that it meets the requirements. For more information, see Test that your module passes verification.

  * Your module must have a variable named `project_id`, which stores the project ID that your customers use to deploy the module.

  * You must specify references to the names of your images as Terraform variables, with the format `projects/PROJECT_NAME/global/images/IMAGE_NAME`. The value of `default` must be set to the name of your VM image, so that the Cloud Marketplace-owned copy of the image can be substituted into the module when your VM product is published.

  * Your module must not depend on outside modules that aren't packaged with it.

  * Your module must use only the following approved providers:

    * `archive`
    * `cloud-init`
    * `dns`
    * `google`
    * `google-beta`
    * `http`
    * `null`
    * `random`
    * `time`
    * `tls`



For an example of a custom module that conforms to these requirements, visit the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/tree/master/examples/terraform/simple_cli_only).

#### Additional requirements for custom Terraform modules for UI deployment

If your custom module supports UI deployment, it must meet the following additional requirements:

  * Your module must contain a variable called `goog_cm_deployment_name`. Cloud Marketplace uses this variable to name your customers' deployments in their deployment page. You should use this variable to avoid resource naming collisions between multiple deployments in one project. For an example, see `goog_cm_deployment_name` in the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/1b375ce22059b90a26a15f8e8c035cb9f559f597/examples/terraform/wordpress/variables.tf#L23-L26).

  * In the file `metadata.display.yaml`, you must specify `ET_GCE_DISK_IMAGE` as the `xGoogleProperty` type for all image variables. For an example, see `metadata.display.yaml` in the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/terraform/wordpress/metadata.display.yaml#L120).

  * If your product contains multi-VM images or images that support multiple CPU architectures, you must add `enumValueLabels` so that your customers can select the VM image they want to use. For an example, see the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/b3f4fde2d11e5e38dda562e97486936385e582d0/examples/terraform/wordpress/metadata.display.yaml#L123-L127).

  * Your module must not depend on support for [Terraform provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax).




### Additional steps for custom Terraform modules

If you selected to use custom Terraform modules, you must complete the following additional steps to configure your VM image for deployment:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Terraform configuration** , under **Image Variables** , click **Add variable**.

To enable Terraform deployment of your product, you must have [turned on usage of Marketplace owned images](https://docs.cloud.google.com/marketplace/docs/partners/vm/create-deployment-package#select-vm-image). Cloud Marketplace uses the variable you add here to swap in the Marketplace owned version of your VM image when a customer deploys your product.

  3. In the **Image Variable** text field, enter a name for your variable, such as "image".

  4. In your custom Terraform module, set the default value of the variable that you created in the previous step to the name of the VM image for your product, in the format `projects/YOUR_PROJECT/global/images/YOUR_IMAGE`.

  5. Under **Specify your GCS object location** , click **Browse**.

If you've already created a Cloud Storage bucket, select it here.

If you don't have a Cloud Storage bucket, click the icon labeled **Create new bucket**. When you create a new bucket, you:

     * Select a name for the bucket.

     * Specify what region or regions the bucket stores data in.

     * Specify the storage class for your data.

     * Determine what level of granularity to apply to the Identity and Access Management (IAM) permissions for the bucket's data.

     * Configure optional advanced settings, such as encryption or data retention policies.

  6. Ensure that [Object Versioning is enabled](https://docs.cloud.google.com/storage/docs/using-object-versioning) for your Cloud Storage bucket.

  7. To save your bucket settings and continue configuring your deployment package, click **Configure**.

  8. Under **Required roles** , specify the IAM roles your customers must have to deploy your product.




### (UI deployment only) Create metadata for your custom Terraform module

For your custom module to support UI deployment, you must create and add metadata that Cloud Marketplace uses to correctly parse your module and render it in the UI for your customer.

To create and add this metadata, you can use the open source [CFT CLI tool](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata). To use CFT to create and add metadata to your custom modules, complete the following steps:

  1. Install the CFT CLI tool. For more information, visit the [CFT CLI documentation](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#pkg-overview). We recommend that you specify the value of `VERSION` to be `latest`, and set `PLATFORM` to one of the following values:

     * `linux`

     * `windows`

     * `darwin`

  2. Run the following command:
         
         cft blueprint metadata -p TF_PACKAGE_PATH -q -d --nested=false
         

In the previous command, the `-p` flag provides a path for the Terraform package, the `-q` flag generates metadata without needing information for a remote repository, the `-d` flag generates the `metadata.display.yaml` file, and the `--nested=false` flag generates metadata for the root module, skipping any modules in the `modules/` folder.




After you complete the previous steps, the CFT CLI tool generates two new files: `metadata.yaml` and `metadata.display.yaml`.

#### Customize your custom Terraform module's metadata

Cloud Marketplace uses the file `metadata.display.yaml` to customize the form that customers use to deploy your product through the UI. If you want to customize this form, after you create your metadata, you can alter the values of the fields in `metadata.display.yaml`. For details of the available customization options, visit the open source [BlueprintUI documentation](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#BlueprintUI), or see the [BlueprintUI schema](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/cli/bpmetadata/schema/gcp-blueprint-metadata.json).

We recommend that you use the extension [`GooglePropertyExtensions`](https://pkg.go.dev/github.com/GoogleCloudPlatform/cloud-foundation-toolkit/cli/bpmetadata#GooglePropertyExtension) to alter your metadata. `GooglePropertyExtensions` lets you use Google Cloud-specific validations, such as enforcing that customers can only select Virtual Private Cloud (VPC) networks that already exist in their project. For an example, see the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/1b375ce22059b90a26a15f8e8c035cb9f559f597/examples/terraform/wordpress/metadata.display.yaml#L28-L171).

#### Validate your custom module's metadata

To validate your custom module's metadata, run the following command:
    
    
    cft blueprint metadata -p TF_PACKAGE_PATH -v
    

In the previous command, the `-p` flag provides a path for the Terraform package, and the `-v` flag validates all metadata files under the provided path based on the [`BlueprintMetadata` schema](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/cli/bpmetadata/schema/gcp-blueprint-metadata.json).

### Test that your module passes verification

Your custom module passes the verification if the following command runs successfully:
    
    
    terraform plan -var project_id=YOUR_PROJECT -var-file marketplace_test.tfvars
    

In the previous command, `marketplace_test.tfvars` is a Terraform variables file that only Cloud Marketplace uses, solely for this verification of the module. If your template declares any variables that don't have a default value, and you don't set a value for those variables, then the command doesn't run successfully. To ensure that the command runs successfully, you can create a `marketplace_test.tfvars` file to set values for the variables that your template declares. For an example `marketplace_test.tfvars` file, see the [sample custom Terraform module](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/1b375ce22059b90a26a15f8e8c035cb9f559f597/examples/terraform/wordpress/marketplace_test.tfvars).

#### (Optional) (CLI deployment only) Include a test module

Optionally, if your custom module supports CLI deployment, you can choose to include a folder named `examples/marketplace_test`. You might want to do this if your product needs to include a separate test module for verifying its capabilities. If you include this folder, then for your module to pass the verification, the following command must run successfully:
    
    
    terraform -chdir=examples/marketplace_test plan -var project_id=YOUR_PROJECT
    

## Validate and test your deployment

After you've created and configured your deployment package, you must validate and test it before the Cloud Marketplace team can review and approve it.

  1. In Producer Portal, go to the **Deployment package** section.

  2. Click **Validate**. The validation process can take up to two hours to complete, and you can exit the screen while it runs.

  3. After the validation has completed successfully, click **Deployment preview** to test your deployment.




## What's next

After you've successfully validated and tested your deployment, you can click **Publish** to submit your overall product for review and publication on Cloud Marketplace. For details, see [Submit your product](https://docs.cloud.google.com/marketplace/docs/partners/vm/submitting).

[ Previous arrow_back  Building your VM image  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/build-vm-image)

[ Next Configure your VM image for Deployment Manager deployment  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-dm-deployment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
