---
url: https://docs.cloud.google.com/modernize/hub/assess-dotnet/
title: Assess .NET applications for modernization \u00a0|\u00a0 Modernization Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:54.562767+00:00
---

# Assess .NET applications for modernization  |  Modernization Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/modernize/hub/assess-dotnet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Google Cloud Modernize ](https://docs.cloud.google.com/modernize/hub)
  * [ Modernization Hub ](https://docs.cloud.google.com/modernize/hub)
  * [ Guides ](https://docs.cloud.google.com/modernize/hub/overview)



Send feedback 

#  Assess .NET applications for modernization Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use Google Cloud Modernization Hub to assess ASP.NET and .NET Framework applications for Linux containerization and modernization to a cross-platform .NET release.

Many enterprise .NET applications depend on Windows-specific APIs, IIS server configurations, or legacy .NET Framework libraries that prevent direct deployment to Linux containers. An automated assessment in Modernization Hub analyzes your source code to identify blockers, evaluate NuGet package compatibility, and recommend refactoring paths for Cloud Run or Google Kubernetes Engine.

## When to use a .NET application assessment

Run a .NET application assessment when you plan to do any of the following modernization tasks:

  * **Replatforming to Linux containers** : Identify Windows-only dependencies (such as Windows Registry access, `System.Drawing`, or Active Directory integrations) before containerizing applications for Cloud Run or GKE.
  * **Upgrading .NET Framework versions** : Evaluate effort and compatibility gaps when migrating from .NET Framework 4.x to modern, cross-platform .NET releases (.NET 10 or later).
  * **Decoupling monolithic architectures** : Discover tightly coupled WCF services, Windows Services, or legacy web forms that require refactoring into cloud-native microservices.



## Before you begin

Before you start a .NET assessment job, enable the required APIs, verify your project Identity and Access Management (IAM) permissions, register a workspace settings bucket, and upload your source code archive to Cloud Storage.

### Enable required APIs

To use Modernization Hub, enable the required Google Cloud service APIs in your project:
    
    
    gcloud services enable \
        aiplatform.googleapis.com \
        artifactregistry.googleapis.com \
        cloudbuild.googleapis.com \
        cloudresourcemanager.googleapis.com \
        compute.googleapis.com \
        logging.googleapis.com \
        storage.googleapis.com \
        --project=PROJECT_ID
    

Replace PROJECT_ID with your Google Cloud project ID.

### Required roles

Running an assessment requires distinct IAM permissions for two identities using Cloud Build and Gemini Enterprise Agent Platform:

  * **Authenticated console user (initiating the job and accessing buckets)** : 
    * Storage Admin (`roles/storage.admin`)
    * Service Account User (`roles/iam.serviceAccountUser`)
    * Cloud Build Editor (`roles/cloudbuild.builds.editor`)
  * **Dedicated service account (executing the assessment container)** : 
    * Agent Platform User (`roles/aiplatform.user`)
    * Storage Object User (`roles/storage.objectUser`) or Storage Admin (`roles/storage.admin`)



To get the permissions that you need to initiate an assessment and execute the analysis container, ask your administrator to grant you the following IAM roles on your project: 

  * **User** — Manage source archives and bucket configurations: Storage Admin (`roles/storage.admin`) 
  * **User** — Attach the dedicated service account to the job: Service Account User (`roles/iam.serviceAccountUser`) 
  * **User** — Submit assessment jobs (`cloudbuild.builds.create`) and view logs: Cloud Build Editor (`roles/cloudbuild.builds.editor`) 
  * **Service account** — Execute the `codmod` container: Agent Platform User (`roles/aiplatform.user`) 
  * **Service account** — Read source archives and write assessment reports: Storage Object User (`roles/storage.objectUser`) or Storage Admin (`roles/storage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to initiate an assessment and execute the analysis container. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to initiate an assessment and execute the analysis container:

  * **User** (Cloud Storage, Cloud Build, and IAM): 
    * `storage.objects.get` (To download or read files)
    * `storage.objects.list` (To list files within the bucket)
    * `storage.objects.create` (To upload or create new files)
    * `storage.objects.update` (To modify metadata of existing files)
    * `storage.objects.delete` (To delete or overwrite files)
    * `storage.buckets.get` (View bucket-level configurations)
    * `cloudbuild.builds.create` (To submit assessment jobs)
    * `iam.serviceAccounts.actAs` (To attach the service account to the job)
  * **Service account** (Agent Platform and Cloud Storage): 
    * `aiplatform.endpoints.predict` (To run AI-assisted code analysis)
    * `storage.objects.get` (To read or download source archives)
    * `storage.objects.list` (To list files in the input folder)
    * `storage.objects.create` (To write assessment reports)
    * `storage.objects.delete` (To delete temporary files)



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Configure a workspace settings bucket

Register a designated Cloud Storage bucket on the **Modernization Hub > Settings** page (for example, `gs://PROJECT_ID-modernization-hub`) to store the workspace binary state files (`dotnet_jobs.pb`, `java_jobs.pb`, and `mainframe_jobs.pb`).

### Review codebase size limits

To maintain optimal performance and cost efficiency, the `codmod` assessment engine enforces the following scale and archive guidelines:

  * **Maximum codebase size:** Approximately **6 million lines of code (LOC)** per assessment job. If your repository exceeds 6 million LOC, split the codebase into smaller, independent solutions or modules before uploading.
  * **Clean archive structure:** Exclude compiled binaries, package caches, and version control metadata (such as `bin/`, `obj/`, `node_modules/`, `.vs/`, and `.git/`) from your zip file so that only source files and build configurations are analyzed.



### Prepare and upload your .NET source archive

Package your .NET codebase as a zip file that excludes build outputs, and upload the file to a Cloud Storage bucket in your project.

  1. On your local machine, create a zip file of your repository using one of the following methods:

     * **Using Git (recommended)** :
           
           git archive --format=zip -o repository.zip HEAD
           

     * **Using the`zip` CLI**:
           
           zip -r repository.zip . \
               -x "*.git*" "*/bin/*" "*/obj/*" "*/node_modules/*" "*.vs/*"
           

  2. Upload the zip file to your target Cloud Storage bucket by using the Google Cloud CLI:
         
         gcloud storage cp repository.zip \
             gs://INPUT_BUCKET/codebase/repository.zip
         

Replace INPUT_BUCKET with the name of your target Cloud Storage bucket.




## Run an assessment

To run an assessment job, follow these steps:

  1. In the console, go to the **Modernization Hub** page.

[ Go to Modernization Hub ](https://console.cloud.google.com/modernization-hub)

  2. On the landing page, locate the **.NET Modernization** card and click **Start assessment**.

  3. In the **Job name** field, enter a unique name for your assessment job.

  4. In the **Source code location** field, select a Cloud Storage bucket containing your source code as a zip file.

  5. In the **Report location** field, select a Cloud Storage bucket to save the generated assessment reports.

  6. From the **Modernization recipe** list, select a modernization recipe.

  7. From the **Location** list, select a region for your assessment job.

  8. In the **Service account** field, select a dedicated service account with the required IAM roles listed in the Required roles section. Cloud Build runs the assessment job under this service account, which requires Agent Platform User and Cloud Storage permissions.

  9. Click **Generate Report**.

The console starts a background assessment container to analyze your project. The job status appears in the **Assessment history** table.




## Monitor job status and view reports

Depending on the size of your codebase, assessment jobs typically complete within a few minutes. The background container terminates automatically after it finishes processing.

To view your assessment results, follow these steps:

  1. In the **Assessment history** table on the Modernization Hub page, locate your assessment job.
  2. When the **Status** column changes to **Completed** , click **Download Report**.
  3. Select your preferred output format: 
     * **HTML report** : An interactive summary that lets you filter incompatible Windows APIs, inspect file-by-file blocker lists, and view remediation suggestions.
     * **Markdown report** : A formatted executive summary suitable for sharing with stakeholders and architectural review boards.



## Review the assessment report

The assessment report categorizes your application's migration readiness into the following areas:

  * **Overall compatibility score:** the percentage of source lines and dependencies that can migrate to cross-platform .NET without modification.
  * **Blocker breakdown:** specific Windows dependencies that require refactoring, such as: 
    * Windows Communication Foundation (WCF) server implementations.
    * ASP.NET Web Forms or ASP.NET MVC legacy pipelines.
    * Windows Registry calls (`Microsoft.Win32`).
  * **NuGet dependency analysis:** a detailed inventory of existing NuGet packages indicating whether each package supports the target .NET version or requires replacement.
  * **Recommended actions:** suggested code transformations and migration paths to prepare your application for containerization on Google Cloud.



## Refactor .NET code with Antigravity

After you generate an assessment report, you can use [Antigravity](https://antigravity.google/) with specialized .NET agentic skills to automate code conversion from .NET Framework to cross-platform .NET.

Before you run agentic refactoring workflows, make sure that you meet the following prerequisites:

  * **Antigravity environment:** install the [Antigravity IDE or Antigravity CLI (`agy`)](https://antigravity.google/docs/cli/overview) and configure authentication with your Google Cloud project.
  * **Assessment artifacts:** download your `codmod` assessment report and place it in your local repository workspace so the agent can reference identified blockers and dependency upgrade paths.
  * **.NET modernization skills:** load the `codmod` .NET modernization skill (`SKILL.md`) into your Antigravity workspace settings. To request preview access to the latest .NET modernization agent skills, contact [modernization-hub-feedback-external@google.com](mailto:modernization-hub-feedback-external@google.com).



## What's next

  * Learn how to [assess Java applications](https://docs.cloud.google.com/modernize/hub/assess-java).
  * Learn how to [set up Mainframe Assessment Tool (MAT)](https://docs.cloud.google.com/modernize/hub/setup-mat).
  * Explore AI-assisted code transformation using [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
