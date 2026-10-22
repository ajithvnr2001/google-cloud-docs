---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-dm-deployment/
title: Configure your VM image for Deployment Manager deployment \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:27.877215+00:00
---

# Configure your VM image for Deployment Manager deployment  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-dm-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Configure your VM image for Deployment Manager deployment Stay organized with collections  Save and categorize content based on your preferences. 

If you [choose to support deployment with Deployment Manager](https://docs.cloud.google.com/marketplace/docs/partners/vm/create-deployment-package#select-deployment-options) for your VM product, you must complete the following steps.

**Caution:** The Deployment Manager Actions feature is [no longer supported](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions). If your product relies on this, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

## Determine how to create your deployment package

We recommend that you use Producer Portal's guided configuration option to create your deployment package directly in the Google Cloud console.

The guided configuration supports simple VM products, such as single-VM deployments with basic firewall rules, but it doesn't support some complex features, such as deployments with multiple VMs and custom configuration fields. If you need features that the guided configuration doesn't support, you can use the [open source `mpdev` tool](https://github.com/GoogleCloudPlatform/marketplace-tools) to either create your deployment package or to customize an existing package by adding additional capabilities to it.

We don't recommend using custom deployment templates that you created without using Google Cloud console or the Deployment Manager Autogen tool with Cloud Marketplace. We recommend that you create your deployment package directly in Google Cloud console.

### Switch between guided configuration and manual configuration

If you use Producer Portal's guided configuration option and later want to switch to manually configuring your deployment package, click **Go to manual configuration**.

When you switch, you can download the Autogen specification for the deployment package you created in the guided configuration, to use as a basis for your manual configuration.

**Note:** When you switch between the guided configuration and manually configuring your deployment package, you cancel any Validations that are running for your previous configuration method.

## Complete your guided configuration

To finish configuring and submit a simple deployment package using the Google Cloud console, complete the following steps:

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Deployment Manager configuration** , next to the input field labeled **Cloud Storage Bucket** , click **Browse**.

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

If you plan to switch to manual configuration, you can click **Download** to download the Autogen specification for the deployment package you created in the guided configuration, to use as a basis for your manual configuration.

  11. Submit the deployment package for review in Producer Portal. After you submit the package, it might take up to two weeks for Google to review and approve the package.




## Complete your manual configuration

This section explains how to use the `mpdev` tool to create a deployment package and submit the package for review.

The `mpdev` tool uses Deployment Manager [Autogen](https://github.com/GoogleCloudPlatform/deploymentmanager-autogen) to generate the Deployment Manager templates for your deployment package. The tool generates the deployment package based on an Autogen specification that contains the configuration inputs for your VM product.

At a high level, to generate and submit your deployment package, you must do the following:

  1. Create and configure a Cloud Storage bucket to store and manage access to the deployment package.
  2. Create an Autogen specification that includes the image details and deployment requirements for your VM product.
  3. Generate the deployment package based on your Autogen specification, and upload the package to the Cloud Storage bucket.
  4. Submit the deployment package for review in Producer Portal. After you submit the package, it might take up to two weeks for Google to review and approve the package.



The following sections explain how to complete the steps to generate and submit your deployment package.

### Before you begin

If you're using `mpdev` to create your deployment package, complete the following steps:

  1. Install the `mpdev` tool by following the instructions in the [`marketplace-tools` repository](https://github.com/GoogleCloudPlatform/marketplace-tools).

  2. Download the [Google Cloud SDK](https://docs.cloud.google.com/sdk/downloads).




### Create your Cloud Storage bucket

You must create the Cloud Storage bucket in the same public Google Cloud project that you use for Producer Portal and configure the bucket in the following ways:

  * Enable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for the bucket to protect your deployment package from being deleted or overwritten.
  * Grant the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectViewer`) role to `cloud-commerce-marketplace-onboarding@twosync-src.google.com`.



To create and configure a Cloud Storage bucket, run the following `gcloud storage` commands:
    
    
      BUCKET_NAME=YOUR_BUCKET_NAME
      gcloud storage buckets create gs://$BUCKET_NAME
      gcloud storage buckets update gs://$BUCKET_NAME --versioning
      gcloud storage buckets add-iam-policy-binding gs://$BUCKET_NAME --member=group:cloud-commerce-marketplace-onboarding@twosync-src.google.com --role=roles/storage.objectViewer
      

Where `YOUR_BUCKET_NAME` is the name you provide for the new bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

### Create your Autogen specification

To create your Autogen specification, we recommend that you use the [`single VM example`](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/deployment-manager/autogen/singlevm) in the `marketplace-tools` repository as your initial Autogen specification, and then customize the specification with your VM's configuration details.

For more complex use cases, you can set up [autocomplete in some integrated development environments (IDEs)](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/docs/setup-autocomplete.md) to help edit and validate `configurations.yaml` files.

**Note:** If your deployment contains multiple VMs, you can create and customize your Autogen specification based on the repository's [`multi VM example`](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/deployment-manager/autogen/multivm).

To create your Autogen specification from the `single VM example`:

  1. Check out the example's preconfigured Autogen specification into a local directory:
         
         PACKAGE=YOUR_PACKAGE_NAME
         mpdev pkg get https://github.com/GoogleCloudPlatform/marketplace-tools.git/examples/deployment-manager/autogen/singlevm $PACKAGE
         

Where `YOUR_PACKAGE_NAME` is the name that you provide for the local directory. For example, `my-deployment-package`.

  2. Update the specification with your VM's configuration details by modifying the `configurations.yaml` file with the following information:

     * The name of your VM image.
     * The `ID` for the public Google Cloud project that hosts your VM image, which is the same project that you use for Producer Portal.

For steps to update the VM image and Google Cloud project fields in the `configurations.yaml` file, refer to the `single VM example`'s [`README.md`](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/deployment-manager/autogen/singlevm#update-the-autogen-specification) file.

  3. If required for your product, customize additional fields, such as `passwords`, `deployInput`, and `postDeploy`. These fields are located under the [`DeploymentSpec`](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/deployment-manager/autogen/singlevm/configurations.yaml#L45) in the `configurations.yaml` file. To learn more about the fields available for customization, refer to the [Autogen reference documentation](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/docs/autogen-reference.md)).




### Generate your deployment package

After you create and customize the Autogen specification, use the specification to generate the Deployment Manager template files for your deployment package. To store the package, upload the package to the Cloud Storage bucket.

To generate and upload your deployment package:

  1. Set the output location for the deployment package to your Cloud Storage bucket:

**Note:** You can use the following command if you used one of the [`Autogen specification examples`](https://github.com/GoogleCloudPlatform/marketplace-tools/blob/master/examples/deployment-manager/autogen) in the `marketplace-tools` repository. If you created your Autogen specification manually, you must edit your specification file directly to update the output location.
         
         mpdev cfg set zipPath gs://BUCKET_NAME/OBJECT
         

Where BUCKET_NAME is the name of the bucket that you created for the package and OBJECT is the name that you provide for the Cloud Storage object, subject to [naming guidelines](https://docs.cloud.google.com/storage/docs/naming-objects).

  2. Generate the deployment package:
         
         mpdev apply -f $PACKAGE/configurations.yaml
         




The generated deployment package is zipped and uploaded to your bucket.

To verify that you configured the template properly, create a deployment by running the following command:
    
    
      TMPDIR=$(mktemp -d)
      unzip $PACKAGE/template.zip -d $TMPDIR
      gcloud deployment-manager deployments create $PACKAGE --config $TMPDIR/test_config.yaml
      

### Submit your deployment package for review in Producer Portal

After you've created and configured your deployment package, you must submit the package to Producer Portal so that the Cloud Marketplace team can review and approve the package.

  1. In Producer Portal, go to the **Deployment package** section.

  2. Under **Specify your Cloud Storage object location** , select the deployment package object that you previously uploaded.

  3. Click **Validate**. The validation process might take up to two hours to complete, and you can exit the screen while it is completing.

  4. After Producer Portal has successfully read your deployment package, you can click **Deployment preview** to [view how the customer sees your VM configuration](https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages).

  5. After the validation completes successfully, to submit the deployment package for review, click **Submit**. After you submit the package, it might take up to two weeks for Google to review and approve the package.




[ Previous arrow_back  Configure your VM image for Terraform deployment  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/configure-terraform-deployment)

[ Next Understand how customers see your deployment packages  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/customer-view-deployment-packages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
