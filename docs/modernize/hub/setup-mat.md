---
url: https://docs.cloud.google.com/modernize/hub/setup-mat/
title: Set up Mainframe Assessment Tool \u00a0|\u00a0 Modernization Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:47.651138+00:00
---

# Set up Mainframe Assessment Tool  |  Modernization Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/modernize/hub/setup-mat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Google Cloud Modernize ](https://docs.cloud.google.com/modernize/hub)
  * [ Modernization Hub ](https://docs.cloud.google.com/modernize/hub)
  * [ Guides ](https://docs.cloud.google.com/modernize/hub/overview)



Send feedback 

#  Set up Mainframe Assessment Tool Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use the guided setup companion in Google Cloud Modernization Hub to deploy and configure a Mainframe Assessment Tool instance in your Google Cloud project.

The Mainframe Assessment Tool analyzes legacy mainframe artifacts, such as COBOL, PL/I, Assembler, JCL, and DB2 schemas to generate detailed inventory reports, dependency maps, and modernization complexity scores. Modernization Hub simplifies onboarding by guiding you through MAT prerequisites, generating verified Google Cloud CLI deployment commands, and launching the setup workflow in your environment.

## Before you begin

Before deploying an Mainframe Assessment Tool instance, make sure that your Google Cloud project meets the necessary Identity and Access Management (IAM), API, settings bucket, and billing prerequisites.

### Verify project prerequisites

  1. In the Google Cloud console, select or create a Google Cloud project.
  2. Make sure that billing is enabled for your project.
  3. Verify that your user account has sufficient permissions to provision Compute Engine resources, configure service accounts, and enable Google Cloud APIs. For detailed MAT infrastructure and role requirements, see [Configure your Google Cloud project for Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project).



### Enable required APIs

To use Modernization Hub and deploy MAT, enable the required Google Cloud service APIs in your project:
    
    
    gcloud services enable \
        cloudbuild.googleapis.com \
        storage.googleapis.com \
        compute.googleapis.com \
        logging.googleapis.com \
        aiplatform.googleapis.com \
        cloudresourcemanager.googleapis.com \
        --project=PROJECT_ID
    

Replace PROJECT_ID with your Google Cloud project ID.

### Required roles

To access the Modernization Hub console interface, provision MAT analysis virtual machines, and manage job state files, make sure that your project's service accounts and your user account have the required roles on your project.

To get the permissions that you need to provision MAT analysis virtual machines and manage assessment jobs, ask your administrator to grant you the following IAM roles on your project: 

  * Provision MAT analysis virtual machines: Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) 
  * Route traffic through Google's proxy to the MAT virtual machine: IAP-secured Tunnel User (`roles/iap.tunnelResourceAccessor`) 
  * Submit setup or assessment jobs (`cloudbuild.builds.create`) and view build logs: Cloud Build Editor (`roles/cloudbuild.builds.editor`) 
  * Read input archives, write and read output reports, and update `.pb` state files: Storage Object User (`roles/storage.objectUser`) 
  * Run Cloud Build and Compute Engine virtual machines under the project's default service accounts: Service Account User (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Configure a workspace settings bucket

Register a designated Cloud Storage bucket on the **Modernization Hub > Settings** page (for example, `gs://PROJECT_ID-modernization-hub`) to store the workspace binary state files (`mainframe_jobs.pb`, `dotnet_jobs.pb`, and `java_jobs.pb`).

## Generate your MAT deployment script

The Modernization Hub companion interface creates customized deployment scripts based on your target project and regional preferences. To generate your setup script, follow these steps:

  1. In the console, go to the **Modernization Hub** page:

[ Go to Modernization Hub ](https://console.cloud.google.com/modernization-hub)

  2. On the landing page, locate the **Mainframe Assessment Tool** card and click **Setup Environment**.

  3. In the guided discovery panel, review the checklist of prerequisites from the Mainframe Assessment Tool documentation.

  4. In the **Deployment configuration** section, specify your target environment parameters:

     * **Project ID** : Select the Google Cloud project where you want to deploy the MAT instance.
     * **Region** : Select a target region for your MAT virtual machine and storage buckets (for example, `us-central1`).
  5. Review the generated deployment commands displayed in the **Script preview** pane. The preview shows the exact gcloud CLI commands used to provision the MAT instance and supporting infrastructure.




## Execute deployment scripts and verify setup

You can deploy your MAT instance using either automated console execution or manual command-line execution:

  * **Automated console execution** : In the Modernization Hub companion UI, click **Execute Setup Script**. The console runs the provisioned deployment commands within your Google Cloud project and displays live execution logs.
  * **Manual CLI execution** : If you prefer to run the deployment in your own terminal, click **Copy script** in the preview pane and run the commands in Cloud Shell or your local terminal environment.



After the deployment script finishes provisioning your resources, the companion interface displays a **Launch MAT** button. Click **Launch MAT** to open the web interface of your newly deployed Mainframe Assessment Tool instance.

## What's next

After you deploy your MAT instance, use the official Mainframe Assessment Tool documentation to upload your mainframe artifacts and execute assessments:

  * Learn how to [configure your project and upload source files](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project).
  * Follow instructions to [perform a mainframe assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).
  * Learn how to [review and export assessment results](https://docs.cloud.google.com/mainframe-assessment-tool/docs/review-results).
  * Explore mainframe de-risking and parallel validation using [Dual Run](https://docs.cloud.google.com/dual-run/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
