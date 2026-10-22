---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/set-up-environment/
title: Set up your Google Cloud environment \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:35.979872+00:00
---

# Set up your Google Cloud environment  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/set-up-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Set up your Google Cloud environment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to set up your Google Cloud environment for your virtual machine (VM) product, which includes creating a workspace and Google Cloud Marketplace listing for your product.

## Set up your workspace

To set up your workspace, you create two Google Cloud projects:

  * A project for development and testing. For the project ID, use the format `PARTNER_NAME-dev`.
  * A project to create and host your final Compute Engine images. For the project ID, use the format `PARTNER_NAME-public`. Don't use this public project for anything other than hosting your Compute Engine mages.



For steps to create projects, see [Creating and managing Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

After you create the projects, configure the projects and provide details to Google: 1\. For each project, grant the Editor (`roles/editor`) and Service Management Admin (`roles/servicemanagement.admin`) roles to [cloud-commerce-marketplace-onboarding@twosync-src.google.com](mailto:cloud-commerce-marketplace-onboarding@twosync-src.google.com). Grant the Config Editor (`roles/servicemanagement.configEditor`) role to [cloud-commerce-producer@system.gserviceaccount.com](mailto:cloud-commerce-producer@system.gserviceaccount.com). For steps to grant access, see [Granting, changing and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  1. For each project, enable the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) to create and run VMs on Google Cloud.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  2. In the public project only, set a security contact. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

  3. Complete the [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform) to provide high-level details about the projects and your product. You only need to complete this form once.




## Create your product in Cloud Marketplace

To create and publish your product in Cloud Marketplace, you use Producer Portal. Your Partner Engineer enables it for you after you complete the [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform).

To publish your product in Producer Portal, you submit the following information for review:

  * **Product Details** : Add listing and marketing info about your product.
  * **Pricing** : Choose and specify your pricing model to determine how customers will pay you for your product.
  * **Deployment Package** : Submit details and specifications for the VM image that your customers deploy from Cloud Marketplace.



You can submit these reviews at any time and in any order. Some reviews might take up to two weeks for approval, so we recommend reviewing the requirements and getting started as early as possible.

At this stage, to proceed with the other reviews, you only need to create a Cloud Marketplace entry for your product. You can complete and submit the remaining product details for review at any time.

To create your product's Cloud Marketplace entry:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).
  2. At the top of the page, click **Add product**.

  3. Select **Virtual machine**.

  4. Under **Product name** , name your product and check the Product ID. The Product ID is used in the URL for your Cloud Marketplace listing.

**Caution:** The Product ID and product type cannot be changed after the product is created. You can change your product name before you submit it.
  5. Click **Create**. It might take a few seconds to create your product.




### Add product details

Your product details include your product listing on Cloud Marketplace, marketing information, and links to documentation. You can start editing details now and submit for review later.

To provide information for your Product Details review:

  1. In the list of products, click the name of your product.

  2. Under **Review: Product Details** , click **Edit**.

  3. In the **Product Info** tab, complete the details that appear in your product listing on Cloud Marketplace:

     * Enter a name, tagline, image, and overview description for your product.
     * Select **Category IDs** to allow customers to find your product under product categories or filters as they search Cloud Marketplace. You can select up to two Category IDs for a product.
  4. Complete the **Documentation** and **Product metadata** sections. To make it easier for users to find your product in Cloud Marketplace, add search keywords in the **Search keywords** box. The keywords must meet the following requirements:

     * They must be directly relevant to your product.
     * They must not include brand names or product names licensed by competitors of your product.

**Note:** Cloud Marketplace might require additional approvals for some categories of products. If you want to add your solution listing to a category that isn't listed in Producer Portal, submit a request by using the [special category request form](https://docs.google.com/forms/d/1-VwD1yyr_w5yWYIbx0OFzQOp7XgSPpa6IgaWbltoR90/edit?resourcekey=0-93_HVNitkydC9bBb6oZiIg).

It takes approximately 2-5 business days for the Partner Engineering team to review and approve your product details.

### Create a Getting Started document

Every product must be accompanied by a Google Cloud-specific **Getting Started document** that helps your customers with detailed deployment and configuration steps for your product. The documentation must be created and maintained by you on your website. We suggest that you co-brand the page with the Google Cloud logo, available on [Partner Network Hub](https://partners.cloud.google.com/resources/marketing). (Note that Partner Network Hub requires you to register to access the site.)

The document should provide step-by-step guidance for the customer's journey, starting with the product listing page on Cloud Marketplace and extending all the way through to the deployment and post-deployment maintenance of the product. We recommend including screenshots throughout the document, in addition to the text instructions.

The document should provide the customer with guidance on what inputs they must provide for a successful deployment, such as:

  * The recommended machine configuration, disk sizes, and zones.

  * If the customer has to open any ports (particularly 80 or 443).

  * Whether the required ports are opened by default, or the customer has to open them during the process of deployment.




### Add next steps

The document should list any additional commands needed to configure the product.

If your product requires a login, the document should outline if and how the customer will gain access to an administrator page or console URL, and how login credentials can be obtained.

**Note** : If a password is required to access an administrator page or console, the password must be auto-generated.

The document should also outline how the customer:

  * Can connect to the VM instance using SSH.

  * Can check the status or health of the app.




For additional guidance, you can refer to these example pages that have been developed for other products in Cloud Marketplace: 

  * [NGINX Getting Started Guide](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-plus-google-cloud-platform/)
  * [DataStax Getting Started Guide](https://github.com/DSPN/google-deployment-guide/blob/master/cloudlauncher.md).



### Submit your document

After you have finished the draft of your Getting Started document, email the URL of your draft to your assigned Partner Engineer for review and feedback.

[ Previous arrow_back  Overview and checklist  ](https://docs.cloud.google.com/marketplace/docs/partners/vm)

[ Next Choosing a pricing model  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
