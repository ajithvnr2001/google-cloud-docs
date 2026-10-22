---
url: https://docs.cloud.google.com/marketplace/docs/partners/vm/test-product/
title: Testing your VM product \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:20.315669+00:00
---

# Testing your VM product  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/vm/test-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Testing your VM product Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the process of testing your VM product before submitting it for review.

## Preview and test your product

To see how users will experience your product, preview and test the product. The preview walks you through the process of viewing and deploying your product, as a customer sees it.

To enable deployment previews for your product, the Cloud Storage object must be uploaded and validated in Producer Portal.

To preview and test your product:

  1. Open Producer Portal in the Google Cloud console:
         
         https://console.cloud.google.com/producer-portal?project=YOUR_PUBLIC_PROJECT_ID
         

Replace YOUR_PUBLIC_PROJECT_ID with the ID for the public project that you created for Cloud Marketplace—for example, `my-organization-public`.

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project and have the Editor (`roles/editor`) role for the project.
  2. In the list of products, click the name of your product.

  3. On the **Overview** page, click **Deployment package**.

  4. Verify that your deployment package was read and validated successfully and click **Deployment preview**.

  5. Review the deployment details and click **Deploy**.




Your preview is deployed.

After you've successfully deployed your product and verified that it behaves as you expect, you can exit your preview.

**Note:** If you've turned on **Use Marketplace owned images** for the product that you're previewing, then when your customers use your product, they access a Google-owned copy of the VM image you created. However, when you test your own product, Cloud Marketplace uses your original version of the VM image for your testing.

To delete the preview deployment, open the Deployment Manager page and delete the deployment.

## End-to-end testing

We recommend you test each of your products' end-to-end flows, to ensure a great customer experience.

You can start the following testing instructions as soon as your Partner Engineer informs you that your product is ready for end-to-end testing. 

Before starting testing procedures, verify that all testers have access to the product. If the product image(s) is not in your public project, ensure that each of the testers is added as a viewer to the development project which contains the product image(s). The testers need to be users of Cloud console, and must be added to the project.

### UI test plan

On the [Cloud Marketplace](https://cloud.google.com/marketplace) site, click **Explore Marketplace** and then search for your product(s). Ensure that the product card is visible in the search results, and that the information on the card is displayed correctly. If you have more than one product, the content of each product must be distinguishable from that of the other products.

  1. Go to the product details page by clicking on your product, and verify the following: 
     * The header is displayed with your name, category, estimated costs and **Launch** button.
     * The product description is displayed with a **Learn more** link that points to a specific product or service page on your website.
     * The tech stack is displayed, with the product type, version, last updated timestamp, and category ID and components, if applicable.
     * The **Pricing** section has the price breakdown, as well as working links to pricing and [free trial](https://cloud.google.com/free/?hl=en_US&_ga=2.158098680.-378933855.1562096601&_gac=1.202315427.1562683467.COn65saJqOMCFbubswodhicJmQ). 
       * The pricing details are correct, and the **Show more** arrow expands properly.
     * The **Maintenance & support** section clearly specifies whether the support is bundled into the pricing. The section has: 
       * A description of available support channels and their hours of service.
       * A link to your support site.
     * The **Terms of service** section includes a link to your End User License Agreement (EULA).



## Deployment flow

  1. Go to the product details page.
  2. Click **Launch** and fill in all of the applicable input fields to deploy the product. Ensure the following: 
     * The product has the same default machine type and disk size as are specified in the pricing table on the product details page.
     * Links work correctly.
     * HTTP and HTTPS ports are checked/unchecked accurately.
  3. Deploy the product on a default machine type, and verify that the product is deployed successfully. Ensure the following: 
     * You can SSH into the virtual machine instance.
     * Test the license key in an SSH session:  

           
           curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/licenses/?recursive=true
           

     * Application info is loaded. 
       * If the application has admin URL, log into the Admin console with the username/password.
       * Check that the specified ports are opened.
  4. Repeat above steps for different instance sizes (especially large and small) and regions. 
     * Repeat the above steps with cloned instances (cloned hard drives).



## Post-deployment next steps

If your product has any post-deployment next steps in its [Getting Started guide](https://docs.cloud.google.com/marketplace/docs/partners/vm/set-up-environment#getting-started-document), then you must also test these steps to ensure that the deployment of your product is successfully completed.

[ Previous arrow_back  Track your products' associated consumption  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking)

[ Next Submitting your product to Google Cloud Marketplace  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/vm/submitting)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
