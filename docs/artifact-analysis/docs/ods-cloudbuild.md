---
url: https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild/
title: Use On-Demand Scanning in your Cloud Build pipeline \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:10.078825+00:00
---

# Use On-Demand Scanning in your Cloud Build pipeline  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Use On-Demand Scanning in your Cloud Build pipeline Stay organized with collections  Save and categorize content based on your preferences. 

Using On-Demand Scanning as part of your Cloud Build pipeline allows you to block builds if the container image has vulnerabilities with a severity matching a predefined level.

This tutorial shows you how to use Cloud Build to build your container image from the source code, scan it for vulnerabilities, check the severity levels of the vulnerabilities, and push the image to Artifact Registry if there are no vulnerabilities of a specific severity level.

We recommend that you create a new Google Cloud project for this tutorial, and complete the steps in an isolated environment.

## Objectives

  * Build an image with Cloud Build.
  * Scan the built image with On-Demand Scanning.
  * Assess acceptable vulnerability levels.
  * Store the image in Artifact Registry.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ On-Demand Scanning](https://docs.cloud.google.com/artifact-analysis/pricing)
  * [ Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [ Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the On-Demand Scanning, Cloud Build, and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=ondemandscanning.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

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

  10. Enable the On-Demand Scanning, Cloud Build, and Artifact Registry APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=ondemandscanning.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Required roles

The service account that you use with Cloud Build requires the following roles:

  * [On-Demand Scanning Admin](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#granting_a_role_using_the_iam_page) (`roles/ondemandscanning.admin`)

  * [Artifact Registry Writer](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) (`roles/artifactregistry.writer`)




The default Cloud Build service account has the required permissions for Artifact Registry repositories in the same project. If your repositories are in the same project that you use for Cloud Build, you only need to grant the On-Demand Scanning Admin role.

If you are using a user-provided service account for Cloud Build, you need to grant both roles.

**Note:** This tutorial assumes that [all services](https://docs.cloud.google.com/artifact-analysis/docs/ods-cloudbuild#costs) are within the same project.

## Prepare your source file

For this tutorial you are going to build an image from a Dockerfile. A Dockerfile is a source file that contains instructions for Docker to build an image.

  1. Open a terminal, create a new directory named `ods-tutorial`, and navigate to it:
         
         mkdir ods-tutorial && cd ods-tutorial
         

  2. Create a file named `Dockerfile` with the following contents:
         
         # Debian10 image
         FROM gcr.io/google-appengine/debian10:latest
         
         # Ensures that the built image is always unique
         RUN apt-get update && apt-get -y install uuid-runtime && uuidgen > /IAMUNIQUE
         




## Create an Artifact Registry repository

  1. Set the project ID to the same project where you enabled the APIs:
         
         gcloud config set project PROJECT_ID
         

  2. Create a Docker repository named `ods-build-repo` in the location `us-central1`:
         
         gcloud artifacts repositories create ods-build-repo --repository-format=docker \
         --location=us-central1 --description="Repository for scan and build"
         

  3. Verify that your repository was successfully created:
         
         gcloud artifacts repositories list
         




## Build and scan

In this section you will [run your build pipeline](https://docs.cloud.google.com/build/docs/building/build-containers) using a build config file. A build config file instructs Cloud Build how to perform several tasks based on your specifications.

  1. In the `ods-tutorial/` folder, create the file `cloudbuild.yaml` with the following contents:
         
         steps:
            - id: build
              name: gcr.io/cloud-builders/docker
              entrypoint: /bin/bash
              args:
              - -c
              - |
                docker build -t us-central1-docker.pkg.dev/$_PROJECT_ID/ods-build-repo/ods-test:latest -f ./Dockerfile . &&
                docker image inspect us-central1-docker.pkg.dev/$_PROJECT_ID/ods-build-repo/ods-test:latest --format \
                '{{index .RepoTags 0}}@{{.Id}}' > /workspace/image-digest.txt &&
                cat image-digest.txt
            - id: scan
              name: gcr.io/google.com/cloudsdktool/cloud-sdk
              entrypoint: /bin/bash
              args:
              - -c
              - |
                gcloud artifacts docker images scan us-central1-docker.pkg.dev/$_PROJECT_ID/ods-build-repo/ods-test:latest \
                --format='value(response.scan)' > /workspace/scan_id.txt
            - id: severity check
              name: gcr.io/google.com/cloudsdktool/cloud-sdk
              entrypoint: /bin/bash
              args:
              - -c
              - |
                gcloud artifacts docker images list-vulnerabilities $(cat /workspace/scan_id.txt) \
                --format='value(vulnerability.effectiveSeverity)' | if grep -Exq $_SEVERITY; \
                then echo 'Failed vulnerability check' && exit 1; else exit 0; fi
            - id: push
              name: gcr.io/cloud-builders/docker
              entrypoint: /bin/bash
              args:
              - -c
              - |
                docker push us-central1-docker.pkg.dev/$_PROJECT_ID/ods-build-repo/ods-test:latest
         images: ['us-central1-docker.pkg.dev/$_PROJECT_ID/ods-build-repo/ods-test:latest']
         
         

This file includes the location and repository previously created in Artifact Registry. If you decide to use different values, modify the `cloudbuild.yaml` file accordingly. The values for `PROJECT_ID` and `SEVERITY` are passed to the script in the build command.

  2. Specify the vulnerability [`SEVERITY` levels](https://docs.cloud.google.com/artifact-analysis/docs/severity-levels) you want to block and start your build.

**Caution:** This pipeline configuration only blocks builds based on the severity levels that you explicitly define. If you only specify one severity value, vulnerabilities classified at higher severity ratings may still exist in your image, and they won't block your build.

You can use the following values for `SEVERITY`:

     * `CRITICAL`
     * `HIGH`
     * `MEDIUM`
     * `LOW`

You can specify multiple severities by using a regular expression.

In the following example, you specify both the `CRITICAL` and `HIGH` severity values. This instructs Cloud Build to check for vulnerabilities that are classified at or above the `HIGH` severity level.
    
    gcloud builds submit --substitutions=_PROJECT_ID=PROJECT_ID,_SEVERITY='"CRITICAL|HIGH"' \
    --config cloudbuild.yaml
    

Where

     * PROJECT_ID is your project ID.
     * SEVERITY allows you to set the severity levels that you want to block. If On-Demand Scanning finds vulnerabilities that match any of the specified severity levels, your build fails.



## Understand your results

When you set your `SEVERITY` value to `CRITICAL|HIGH`, after On-Demand Scanning scans for vulnerabilities, it will see if there are any at the `HIGH` level and the more severe `CRITICAL` level. If no matching vulnerabilities are found in your image, your build succeeds and Cloud Build pushes your image to Artifact Registry.

The output is similar to the following:
    
    
    DONE
    --------------------------------------------------------------------------------------------------------------------------------------------
    
    ID                                    CREATE_TIME                DURATION  SOURCE                                                                                         IMAGES                                                                        STATUS
    abb3ce73-6ae8-41d1-9080-7d74a7ecd7bc  2021-03-15T06:50:32+00:00  1M48S     gs://ods-tests_cloudbuild/source/1615791031.906807-a648d10faf4a46d695c163186a6208d5.tgz  us-central1-docker.pkg.dev/ods-tests/ods-build-repo/ods-test (+1 more)  SUCCESS
    

If On-Demand Scanning finds `HIGH` or `CRITICAL` vulnerabilities in your image, then the `scan` build step fails, subsequent build steps do not start, and Cloud Build does not push an image to Artifact Registry.

The output is similar to the following:
    
    
    Step #2 - "severity check": Failed vulnerability check
    Finished Step #2 - "severity check"
    ERROR
    ERROR: build step 2 "gcr.io/cloud-builders/gcloud" failed: step exited with non-zero status: 1
    

In this tutorial, your results may vary, because the sample source code is a publicly available Linux distribution, `debian10:latest`. Linux distributions and related [vulnerability data](https://cve.mitre.org/) receive updates on an ongoing basis.

To learn about additional Google Cloud tools and best practices to help protect your software supply chain, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

For more information on Linux vulnerability management best practices, you can use free online training provided by the Linux Foundation. See [Developing Secure Software](https://training.linuxfoundation.org/training/developing-secure-software-lfd121/).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

Before you remove the repository, ensure that any images you want to keep are available in another location.

To delete the repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the `ods-build-repo` repository.

  3. Click **Delete**.




###  gcloud 

To delete `ods-build-repo` the repository, run the following command:
    
    
    gcloud artifacts repositories delete ods-build-repo --location=us-central1
    

## What's next

  * [Scan images with On-Demand Scanning and see the vulnerability information](https://docs.cloud.google.com/artifact-analysis/docs/on-demand-scanning-howto).
  * [Automatically scan images in your registry](https://docs.cloud.google.com/artifact-analysis/docs/ar-quickstart).
  * [Sign container images with the Kritis Signer and Binary Authorization](https://github.com/grafeas/kritis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
