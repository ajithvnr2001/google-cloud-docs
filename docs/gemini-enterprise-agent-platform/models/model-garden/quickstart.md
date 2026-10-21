---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/quickstart/
title: Test model capabilities in Model Garden \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:57.291354+00:00
---

# Test model capabilities in Model Garden  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Test model capabilities in Model Garden Stay organized with collections  Save and categorize content based on your preferences. 

Model Garden provides several options for you to quickly view and test model capabilities. For supported models, you can try demo playgrounds or launch demo applications called Model Garden Spaces that you can share with others to showcase a model's capabilities. 

Playgrounds are powered by predeployed Gemini Enterprise Agent Platform [online prediction endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions) and don't incur charges. When you open the model card for a supported model, you can use the **Try out** panel to quickly test the model's capabilities by sending a text prompt. You can also set some of the most common parameters such as temperature and number of output tokens. The playground is limited to text input and output only.

When you launch Spaces, you have a working web application that's ready to use with far less manual effort than deploying a model and building an app to use the model's endpoint. Model Garden deploys your selected model in Gemini Enterprise Agent Platform and deploys the sample app on a Cloud Run instance that uses the deployed model's endpoint. The application can also use existing endpoints, or a MaaS endpoint.

## Before you begin

This tutorial requires you to set up a Google Cloud project and enable the Agent Platform API.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Gemini Enterprise Agent Platform, Artifact Registry, Cloud Build, Cloud Logging, and Cloud Run Admin APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,run.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Gemini Enterprise Agent Platform, Artifact Registry, Cloud Build, Cloud Logging, and Cloud Run Admin APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,run.googleapis.com)

  10. If you want to try Model Garden Spaces, then verify that the Compute Engine default service account has the required permissions to launch Spaces.



### Required roles

To test model capabilities in Model Garden, ensure that both you and the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) have the required IAM roles.

#### Required roles for users

To get the permissions that you need to test model capabilities in Model Garden, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Required roles for the Compute Engine default service account

The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used to launch Spaces.

To ensure that the Compute Engine default service account has the necessary permissions to launch Spaces, ask your administrator to grant the following IAM roles to the Compute Engine default service account on your Google Cloud project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Agent Platform Service Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.serviceAgent) (`roles/aiplatform.serviceAgent`)
  * [Cloud Build Service Account ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the Compute Engine default service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Try a Playground

  1. In the Google Cloud console, go to a supported model's model card, such as the **Gemma 2** model card.

[Go to Gemma 2](https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemma2)

  2. In the **Try out** panel:

     1. For **Region** , accept the default or choose your region.
     2. For **Endpoint** , select **Demo playground**.
     3. In the **Prompt** box, enter `Why is the sky blue?`.
     4. Expand the **Advanced options** section and view the default parameters.

![The try out panel for Gemma 2b-it](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/model-garden/images/try-out-gemma.png)

  3. Click **Submit**. The output appears below the Submit button.




## Try Spaces

**Note:** Spaces is only available for projects that aren't parented by an organization. To learn how to create a project without an organization, see [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

To launch a model, open the model card for the supported model, and in the **Try out Spaces** panel, click a Space to launch one. You are charged for the machines that are used for the deployment and for the Cloud Run instance that's hosting the app.

You can launch Spaces with models such as Gemini, Gemma, Llama, and Stable Diffusion.

### Launch Spaces

Launch Spaces to test and experiment with a model from a sample Gradio application.

  1. In the Google Cloud console, go to Model Garden to view a model's model card.

[Go to Model Garden](https://console.cloud.google.com/agent-platform/model-garden)

  2. Select the model to use. Supported models have a **Try out Spaces** panel, such as the **Gemma 3** model card.

[Go to Gemma 3](https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemma3)

  3. Click rocket_launch **Run** to launch a Space.

     1. You can choose to **Require authentication** (via [Identity Aware Proxy](https://docs.cloud.google.com/iap/docs/enabling-cloud-run)) or **Allow public access**. For more information, see [Enable APIs for the first deployment and grant permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/deploy-vais-prompt#enable_apis_for_the_first_deployment_and_grant_permissions).
**Important:** When using the app, don't include sensitive or personally identifiable information in your prompts.
     1. Click **Create new service** to start the deployment. You can monitor the deployment status from the model card.
  4. After the Spaces status changes to **Ready** , click it to view details about the deployment.

For basic protection, the web application requires a secret key that must be appended to the URL when submitting prompts. This secret key is provided in the **Secret key** field.

     1. Click **Open** to start using the app. You can send prompts to the model and view its responses from within the app.

You can share the URL so that others can try the app too.

     1. To close access to the app, click edit **Edit** in the **Access control** field.

In the **Security** tab for your Cloud Run application, select **Require authentication** and then click **Save**. The application is no longer available through the URL. Visits to the URL result in a 403 error (forbidden).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps.

### Delete Spaces

To clean up Spaces, you must delete both the model's resources and the sample application's resources on Cloud Run.

#### Delete model resources

From within the Gradio app, you can delete model endpoints to clean up Gemini Enterprise Agent Platform resources. Then, you need to delete the Cloud Run service to stop and delete the Gradio app.

To manually delete Gemini Enterprise Agent Platform resources, see [Undeploy models and delete resources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/use-models#undeploy).

#### Delete Cloud Run service

Delete resources related to a service, including all revision of the service. Deleting a service doesn't include items like container images from Artifact Registry. For more information see, [Managing services](https://docs.cloud.google.com/run/docs/managing/services) in the Cloud Run documentation.

  1. In the Google Cloud console, view the list of Cloud Run services:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Locate the service to delete, and then select it.

  3. Click delete **Delete**. This deletes all revisions of the service.




### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

See an [overview of Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
