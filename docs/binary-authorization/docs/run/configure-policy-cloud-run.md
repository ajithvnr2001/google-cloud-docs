---
url: https://docs.cloud.google.com/binary-authorization/docs/run/configure-policy-cloud-run/
title: Quickstart: Configure a Binary Authorization policy with Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:59.171720+00:00
---

# Quickstart: Configure a Binary Authorization policy with Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/run/configure-policy-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a Binary Authorization policy with Cloud Run

This quickstart shows how to configure and test a basic [rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) in a Binary Authorization [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) with Cloud Run.

In this quickstart, you use Binary Authorization to control deployment of a Cloud Run service.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Run, Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/run/configure-policy-cloud-run)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Run, Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/run/configure-policy-cloud-run)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Create a service with Binary Authorization enabled

To create a Cloud Run service with Binary Authorization enabled, do the following:

  1. [Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. Click **Create service** to display the _Create service_ form:

![image](https://docs.cloud.google.com/static/run/docs/images/create-service-form.png)

In the form that displays, do the following:

     1. Select Cloud Run as your development platform.
     2. Select the [region](https://cloud.google.com/about/locations) where you want your service located.
     3. Specify the name you want to give to your service—for example, `test-service`.
     4. Click **Next** to continue to the _Configure the service's first revision_ page.

In the form, do the following:

        1. Select **Deploy one revision from an existing container image**.
        2. Use `us-docker.pkg.dev/cloudrun/container/hello` as the container image.

**Note:** The example image name is for demonstration purposes. We recommend that you use Binary Authorization to deploy only images that you maintain.
        3. Expand the **Advanced settings** section.

        4. Click the **Security** tab.

        5. Select the **Verify container deployment with Binary Authorization** checkbox:

![image](https://docs.cloud.google.com/static/binary-authorization/docs/images/cloud-run-advanced-settings-rectangle.png)

**Note:** If your [organization policy requires Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run), the checkbox is disabled.

By default, the Binary Authorization policy allows all images to be deployed.

        6. Click **Next** to continue to the _Configure how this service is triggered_ page:

![image](https://docs.cloud.google.com/static/run/docs/images/create-service-form3.png)

        7. Select **Allow public access** to be able to open the result in your web browser

        8. Click **Create** to deploy the image to Cloud Run and wait for the deployment to finish.

Your service is deployed. Revisions are subject to Binary Authorization policy enforcement.




## Update the Binary Authorization policy to disallow all images

The Binary Authorization policy contains a default rule. This rule governs the deployment of the Cloud Run service you just created.

By default, the rule allows all container images to be deployed.

To view the default policy, do the following:

  1. [Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

![Screenshot of policy tab showing default rule](https://docs.cloud.google.com/static/binary-authorization/docs/images/default-rule-policy-tab.png)

  2. Click **Edit Policy**.

  3. In **Project Default Rule** , note that the option **Allow All Images** is selected.

![Screenshot of the option to choose a default rule type](https://docs.cloud.google.com/static/binary-authorization/docs/images/default-rule-select-evaluation-mode-allow.png)




Now, modify the policy to _block all images from being deployed_ , by doing the following:

  1. Go to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/policy)

  2. Click **Edit Policy**.

  3. In **Default rule** , select **Disallow All Images**.

![Screenshot of the option to choose a default rule type](https://docs.cloud.google.com/static/binary-authorization/docs/images/default-rule-select-evaluation-mode-disallow.png)

  4. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

## Redeploy the service

Test the updated policy by deploying a new revision.

To deploy the image, do the following:

  1. [Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. Click the name of the service you deployed earlier in this guide.

  3. Click Edit and deploy new revision.

  4. Click **Deploy**.




You see an error message similar to the following:
    
    
    Service update rejected by Binary Authorization policy: Revision
    REVISION uses unauthorized container image. Container image 'us-docker.pkg.dev/cloudrun/container/hello@SHA' is not authorized by policy. Denied by an ALWAYS_DENY admission rule
    

## Reset the policy to allow all images

To reset the policy to allow all images, do the following:

  1. Go to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/policy)

  2. Click **Edit Policy**.

  3. Select **Allow All Images**.

  4. To save the policy, click **Save Policy**.




You can now deploy images.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To delete the service you created in Cloud Run, do the following:

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. Locate the service you want to delete in the services list, and click its checkbox to select it.

  3. Click **Delete**. This deletes all revisions of the service.




To disable Binary Authorization, see [Disabling Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/run/disabling-binauthz-cloud-run).

## What's next

  * Use [breakglass](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run) to bypass Binary Authorization enforcement.

  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).

  * [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

  * Configure the Binary Authorization policy by using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

  * [View Binary Authorization for Cloud Run events in Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
