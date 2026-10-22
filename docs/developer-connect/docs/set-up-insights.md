---
url: https://docs.cloud.google.com/developer-connect/docs/set-up-insights/
title: Set up Developer Connect insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:32.664407+00:00
---

# Set up Developer Connect insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/set-up-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Set up Developer Connect insights Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Developer Connect insights is [generally available](https://cloud.google.com/products#product-launch-stages) in all regions except `australia-southeast1`, `europe-west6`, `europe-west8`, `europe-west9`, and `southamerica-east1`.

This document describes how to set up Developer Connect insights, to make insights Developer Connect insights available to Gemini Cloud Assist investigations, and in Cloud Logging.

Learn more about [Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/insights). 

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Developer Connect API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com)

Enabling Developer Connect also enables the [Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/overview).

  8. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). 

If you've installed it previously, make sure you have the latest version installed by running `gcloud components update`.

  9. Create the Developer Connect service agent: 
         
         gcloud beta services identity create \
         --service=developerconnect.googleapis.com \
         --project=PROJECT_NUM

The role `roles/developerconnect.serviceAgent` is automatically added to this service agent.




### Required roles

If your insights configuration is scoped to an App Hub application managed by a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) (folder boundary):

  * **The user configuring insights** needs the following roles on the management project: 
    * Developer Connect Insights Admin (`roles/developerconnect.insightsAdmin`)
    * App Hub Viewer (`roles/apphub.viewer`)
  * **The Developer Connect Service Agent** needs the following roles: 
    * Developer Connect Service Agent role (`roles/developerconnect.serviceAgent`) and Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) on the management project.
    * Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) from the **folder** containing the management project.



If your insights configuration is scoped to an App Hub application managed by a host project:

**Note:** [App Hub host projects](https://docs.cloud.google.com/app-hub/docs/key-concepts#host-project) are legacy; using a [folder configured for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) is recommended.

  * **The user configuring insights** needs the following roles on the host project: 
    * Developer Connect Insights Admin (`roles/developerconnect.insightsAdmin`)
    * App Hub Viewer (`roles/apphub.viewer`)
  * **The Developer Connect Service Agent** needs the following roles: 
    * Developer Connect Service Agent role (`roles/developerconnect.serviceAgent`) and Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) on the host project.
    * Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) on all service projects.
    * If you're using existing resources (for example from Cloud Build or Artifact Registry) that aren't in the same folder, grant the Developer Connect Insights Agent role to the Developer Connect Service Agent from the host project in those projects.



If your insights configuration is scoped to individual target projects:

  * **The user configuring insights** needs the following roles on the host project: 
    * Developer Connect Insights Admin (`roles/developerconnect.insightsAdmin`).
  * **The Developer Connect Service Agent** needs the following roles: 
    * Developer Connect Service Agent role (`roles/developerconnect.serviceAgent`) and Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) on the host project.
    * Developer Connect Insights Agent role (`roles/developerconnect.insightsAgent`) on all target projects.



In order to view insights from the command line, **users viewing insights** need:

  * Developer Connect Insights Viewer (`roles/developerconnect.insightsViewer`) on the host project.
  * Container Analysis Occurrences Viewer role (`roles/containeranalysis.occurrences.viewer`) on the host project.



Individual tools might require additional Google Cloud or non-Google roles and permissions to use, or for specific use cases. If you encounter permissions errors, check with your administrator to make sure you have the correct roles and permissions.

Besides these roles and permissions, when you configure a new insights configuration using the interactive workflow, you must have permission to access all the resources you specify.

### Additional prerequisites

  * If you want your Developer Connect insights to be scoped to an App Hub application, you need to have or create that application.

Developer Connect insights supports all App Hub [setup models](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models) for applications. We recommend using a [folder configured for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) so that you can use Gemini Cloud Assist and other [application-centric features](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

You can also scope your Developer Connect insights to a project instead of to an App Hub application.

  * You must use Cloud Build and a supported source code management system (GitHub, GitLab, or Bitbucket).

  * Your build must generate provenance in order to include provenance information in the logs.

This can come from any of the following sources:

    * Use Cloud Build and Artifact Registry.

You can use Cloud Build to build your image. The build must be initiated using a trigger, and the build process must generate provenance. Artifacts generated by your build are stored in Artifact Registry.

    * Use GitHub attestations.

If you use version 4 or later of the [`docker/build-push-action`](https://docs.docker.com/build/ci/github-actions/attestations/), the action automatically adds provenance attestations to your image.

Alternatively, you can use the [`actions/attest-build-provenance`](https://github.com/actions/attest-build-provenance) with the `push-to-registry` option to publish the provenance attestation to the container registry, where Developer Connect insights can read it, regardless of the registry provider.

    * Use the `docker buildx provenance` flag.

[Learn more](https://docs.docker.com/build/metadata/attestations/slsa-provenance/)

    * Use the `docker buildx` registry exporter. 

And set `oci-artifact` to `true`. [Learn more](https://docs.docker.com/build/exporters/image-registry/)

GitHub attestations must come from a repository that's publicly available. The `docker buildx` artifact must be publicly available in the container registry.

You can still use Developer Connect insights without provenance, but the insights are less useful

  * Gemini Cloud Assist

Developer Connect insights enhances the Gemini Cloud Assist experience by adding application deployment events to the investigation context. You can enable Gemini Cloud Assist to use Developer Connect insights with [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations).

  * If your Developer Connect insights will be scoped to an App Hub application, then your insights configuration must be in the same project as that application.

If it's scoped by project, then the configuration doesn't need to be in the same project as the project in scope.

Having your other applicable resources (for example, Developer Connect insights, Google Kubernetes Engine clusters, Cloud Run services, Cloud Build, Artifact Registry repositories) in the same location is recommended but not required.




## Limitations

The following limitations are in effect for Developer Connect insights configurations:

  * You can have a maximum of 50 insights configurations in a single project.

  * For project-scoped configurations, a single configuration can track a maximum of 5 projects.

  * A single insights configuration can track a maximum of 3000 runtimes.




## Create your application in App Hub

This is relevant only if you're scoping your Developer Connect insights to an App Hub application.

  1. [Set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub). We recommend using a [folder configured for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) so that you can use Gemini Cloud Assist and other [application-centric features](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

  2. Create an App Hub application.

     * To create an application from existing Google Cloud resources, see [Register resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources).
     * To design and deploy a new application, you can use [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview).



## Configure Developer Connect insights for your application

Create a Developer Connect insights insight using the following command:
    
    
    gcloud developer-connect insights-configs create DCI_CONFIG_NAME \
           --project PROJECT_ID \
           --app-hub-application APP_HUB_APPLICATION_NAME \
           --target-projects TARGET_PROJECT_IDS \
           --location LOCATION
    

Where:

  * DCI_CONFIG_NAME is a name for the insight configuration that will be generated.

  * PROJECT_ID is the ID of the project in which you're creating the Developer Connect insights configuration.

  * APP_HUB_APPLICATION_NAME is the fully-qualified name of the App Hub application you created previously.

This is only applicable if you're scoping this insights configuration to an App Hub application rather than to a project.

  * TARGET_PROJECT_IDS is the comma-separated list of IDs of the projects to which you're scoping this the Developer Connect insights configuration.

This is only applicable if you're scoping this insights configuration to projects rather than to an App Hub application. A single configuration can track a maximum of 5 projects.

  * LOCATION is the region in which you want to create this insight configuration.




This command triggers an auto-discovery process, which finds all the App Hub workloads and services in your project. This process also confirms whether you have the necessary permissions.

This command also returns an OPERATION_ID, which you can use to check the status of the configuration.

You can check the status of your Developer Connect insights configuration:
    
    
    gcloud developer-connect operations describe OPERATION_ID
    

Where OPERATION_ID is the fully-specified operation ID that was returned from the `gcloud developer-connect insights-configs create` command.

This operation is a receipt of the initial request. The `response` field inside it is a snapshot of the resource at the exact moment the creation task was accepted. To get the state of the discovery process run the `insights-configs describe` command.

After the auto-discovery process has finished, you can check the status of this Developer Connect insights by running following command:
    
    
    gcloud developer-connect insights-configs describe DCI_CONFIG_NAME \
           --location=REGION
    

Where:

  * DCI_CONFIG_NAME is the name you used for the `gcloud developer-connect insights-configs create` command.

  * REGION is the region in which you created the configuration.




## What's next

  * [Find out more](https://docs.cloud.google.com/developer-connect/docs/insights) about Developer Connect insights
  * Learn how to [use Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/use-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
