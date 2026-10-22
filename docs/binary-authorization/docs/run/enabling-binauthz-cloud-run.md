---
url: https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run/
title: Enable Binary Authorization for Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:19.201484+00:00
---

# Enable Binary Authorization for Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Enable Binary Authorization for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to set up Binary Authorization to enforce policy-based deployment of Cloud Run services and jobs.

**Note:** After Binary Authorization is enabled, it enforces any update to the Cloud Run service. When you implement a change that affects traffic, Binary Authorization enforces deployment on any Cloud Run revision receiving traffic.

## Before you begin

Set up Cloud Run and enable APIs, by doing the following:

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=/binary-authorization/docs/run/enabling-binauthz-cloud-run)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=/binary-authorization/docs/run/enabling-binauthz-cloud-run)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Enable Binary Authorization on an existing Cloud Run service

You can enable Binary Authorization enforcement on an existing service. To activate enforcement after enabling it, you might need to deploy a revision or update service traffic.

You can enable Binary Authorization enforcement on an existing service using the Google Cloud console or Google Cloud CLI:

###  Console 

  1. Go to the Cloud Run page in the Google Cloud console.

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. Click the service.

  3. Click the **Security** tab.

  4. To enable Binary Authorization enforcement on the service, click **Enable**.

  5. Optional: To configure the Binary Authorization policy, click **Configure Policy**.




###  gcloud 

Enable Binary Authorization on the service and deploy it:
    
    
    gcloud run services update SERVICE_NAME --binary-authorization=default
    

Replace `SERVICE_NAME` with a name for your service.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `run.googleapis.com/binary-authorization:` annotation as follows:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           annotations:
             run.googleapis.com/binary-authorization: POLICY
           name: SERVICE
         spec:
           template:

Replace the following:

     * SERVICE: the name of your Cloud Run
     * POLICY: set to `default`
  3. Replace the service with its new configuration using the following command:



    
    
    gcloud run services replace service.yaml

**Note:** We recommend that you [require Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run) by configuring an organization policy to do so. Binary Authorization can be disabled by Cloud Run developers if the policy is not configured.

## Enable Binary Authorization on an existing Cloud Run job

You can enable Binary Authorization enforcement on an existing job using the Google Cloud console or Google Cloud CLI:

###  Console 

  1. Go to the Cloud Run jobs page in the Google Cloud console.

[Go to Cloud Run](https://console.cloud.google.com/run/jobs?enableapi=true)

  2. Click the job to open the job details.

  3. Click the **Configuration** tab.

  4. Under _Binary Authorization_ , select a policy from the policy list.

  5. Click **Apply** to enable Binary Authorization enforcement on the job.

  6. Optional: To configure the Binary Authorization policy, click **Configure Policy**.




###  gcloud 

Enable Binary Authorization on the job:
    
    
    gcloud run jobs update JOB_NAME --binary-authorization=POLICY
    

Replace the following:

  * `JOB_NAME`: the name of your job.
  * `POLICY`: the policy you want to apply. Use the value `default` to use the default policy.



We recommend that you [require Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run) by configuring an organization policy to do so. Binary Authorization can be disabled by Cloud Run developers if the policy is not configured.

### View the policy

To view the policy, click **View policy**.

For more information, see [Configuring a Binary Authorization policy](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console).

### Service or job deploy failure

If your service or job fails to deploy because it violates the Binary Authorization policy, you might see an error like the following:
    
    
    Revision REVISION_NAME uses an unauthorized container image.
    Container image IMAGE_NAME is not authorized by policy.
    

**Note:** The service or job displays a red exclamation point, but the service continues to serve the previously serving healthy revision.

The error also contains information about why the image violated the policy. In this case, you can [use breakglass](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run) to bypass policy enforcement and deploy the image.

**Note:** Using breakglass creates a log entry. [View breakglass events in Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run).

## Enable Binary Authorization on a new service

You can enable Binary Authorization on a new service using the Google Cloud console or Google Cloud CLI:

###  Console 

  1. Go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)

  2. Click **Create service**.

  3. In the _Create service_ form :

     1. Select Cloud Run as your development platform.
     2. Select the region where you want your service located.
     3. Enter the service name.
     4. Click **Next** to continue to the _Configure the service's first revision_ page.
     5. Select **Deploy one revision from an existing container image**.
     6. Enter or select the image to deploy.
     7. Expand the **Advanced settings** section.
     8. Click the **Security** tab.
     9. Select the **Verify container deployment with Binary Authorization** checkbox.

**Note:** This checkbox might be disabled if your organization policy is set to require [Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run).
     10. Optional: Click **Configure policy** to configure the Binary Authorization policy. To learn more about configuring a policy, see [Configuring a policy](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console).

     11. Deploy the service.




###  gcloud 

Enable Binary Authorization on the service and deploy it:
    
    
      gcloud run deploy SERVICE_NAME --image=IMAGE_URL --binary-authorization=default --region=REGION
    

Replace the following:

  * `SERVICE_NAME`: a name for your service.
  * `IMAGE_URL`: the image you want to deploy.
  * `REGION`: the region in which you want to deploy your service.



## Enable Binary Authorization on a new job

You can enable Binary Authorization on a new job using one of the following:

###  Console 

  1. Go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs?enableapi=true)

  2. Click **Create Job** to display the **Create job** form.

     1. In the form, specify the container image containing the job code or select from a list of containers previously deployed.
     2. The job name is automatically generated from the container image. You can edit or change the job name as needed. A job name cannot be changed after the job is created.
     3. Select the region where you want your job located.
     4. Specify the number of tasks that you want to run in the job. All of the tasks must succeed for the job to succeed. By default, the tasks execute in parallel.
  3. Click **Container, Variables & Secrets, Connections, Security** to set additional job properties.

     * Click the **Settings** tab. In the **Resources** section, configure the following:

       1. In the **Memory** menu, specify the amount of memory required. The default is the minimum required, 512 MiB.
       2. In the **CPU** menu, specify the amount of CPU required. The default is the minimum required, 1 CPU.
     * In the **Task capacity** section:

       1. Under **Task timeout** , specify the maximum amount of time in seconds that the task can run, up to 168 hours (7 days). Each task must complete within the specified time. The default is 10 minutes.

       2. Under **Number of retries per failed task** , specify the number of retries in case of task failures. The default is 3 retries.

     * In the **Parallelism** section:

       1. In most cases you can select **Run as many tasks concurrently as possible** ,.
       2. If you need to set a lower limit due to scaling constraints on resources your job accesses, select **Limit the maximum number of concurrent tasks** and specify the number of concurrent tasks in the **Custom parallelism limit** field.
  4. When you are finished configuring your job, click **Create** to create the job in Cloud Run.

  5. To execute the job, see [execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs) or [execute jobs on a schedule](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule).




### gcloud

  1. Create a new job with Binary Authorization enabled:
         
         gcloud run jobs create JOB_NAME \
           --image IMAGE_URL OPTIONS \
           --binary-authorization=POLICY \
           --region=REGION

Replace the following:

     * `JOB_NAME`: the name of the job you want to create. You can omit this parameter, but you will be prompted for the job name if you omit it.
     * `POLICY`: the policy you want to apply. Use the value `default` to use the default policy.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `REGION`: the region where this job will run.
     * `OPTIONS`: any of the available options described in the Cloud Run [job creation page](https://docs.cloud.google.com/run/docs/create-jobs#command-line).
  2. Wait for the job creation to finish. Upon successful completion, the console displays a success message.

  3. To execute the job, see [Execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs) or [execute jobs on a schedule](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule).




When you create a new job, the Cloud Run [service agent](https://docs.cloud.google.com/iam/docs/service-agents) needs to be able to access the container, which is the case by default.

### YAML

  1. Create a new `job.yaml` file with this content:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
           annotations:
             run.googleapis.com/binary-authorization: POLICY
         spec:
           template:
             spec:
               containers:
               - image: IMAGE

Replace the following:

     * JOB: the name of your Cloud Run job
     * IMAGE: the URL of your container image
     * POLICY: set to `default`
  2. Deploy the new job using the following command:
         
         gcloud run jobs replace job.yaml




## What's next

  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * Configure the Binary Authorization policy using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).
  * [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations) to deploy only signed container images.
  * [Watch a video](https://www.youtube.com/watch?v=b7GdpEEvGDQ) on how to use Binary Authorization in Cloud Run so that only approved builds are deployed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
