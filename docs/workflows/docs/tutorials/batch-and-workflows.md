---
url: https://docs.cloud.google.com/workflows/docs/tutorials/batch-and-workflows/
title: Run a Batch job using Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:46.576488+00:00
---

# Run a Batch job using Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/batch-and-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Workflows ](https://docs.cloud.google.com/workflows)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Run a Batch job using Workflows Stay organized with collections  Save and categorize content based on your preferences. 

[Batch](https://docs.cloud.google.com/batch) is a fully managed service that lets you schedule, queue, and execute [batch processing](https://en.wikipedia.org/wiki/Batch_processing) workloads on Compute Engine virtual machine (VM) instances. Batch provisions resources and manages capacity on your behalf, allowing your batch workloads to run at scale.

[Workflows](https://docs.cloud.google.com/workflows) allows you to execute the services you need in an order that you define described using the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax).

In this tutorial, you use the [Workflows connector for Batch](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview) to schedule and run a Batch job that executes six tasks in parallel on two Compute Engine VMs. Using both Batch and Workflows allows you to combine the advantages they offer and efficiently provision and orchestrate the entire process.

## Objectives

In this tutorial you will: 

  1. Create an Artifact Registry repository for a Docker container image.
  2. Get the code for the batch processing workload from GitHub: a sample program that generates prime numbers in batches of 10,000.
  3. Build the Docker image for the workload.
  4. Deploy and execute a workflow that does the following: 
     1. Creates a Cloud Storage bucket to store the results of the prime number generator.
     2. Schedules and runs a Batch job that runs the Docker container as six tasks in parallel on two Compute Engine VMs.
     3. Optionally deletes the Batch job after it has completed.
  5. Confirm that the results are as expected and that the batches of generated prime numbers are stored in Cloud Storage.



You can run most of the following commands in the Google Cloud console, or run all the commands using the Google Cloud CLI in either your terminal or Cloud Shell.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Batch](https://docs.cloud.google.com/batch)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

###  Console 

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the Artifact Registry, Batch, Cloud Build, Compute Engine, Workflow Executions, and Workflows APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,batch.googleapis.com,cloudbuild.googleapis.com,compute.googleapis.com,workflowexecutions.googleapis.com,workflows.googleapis.com)

  4. Create a service account for your workflow to use for authentication with other Google Cloud services and grant it the appropriate roles:

     1. In the Google Cloud console, go to the **Create service account** page.

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select your project.

     3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

In the **Service account description** field, enter a description. For example, `Service account for tutorial`.

     4. Click **Create and continue**.

     5. In the **Select a role** list, filter for the following roles to grant to the user-managed service account you created in the previous step:

        * **Batch job editor** : to edit Batch jobs.
        * **Logs Writer** : to write logs.
        * **Storage Admin** : to control Cloud Storage resources.

For additional roles, click add **Add another role** and add each additional role.

**Note:** The **Role** field affects which resources your service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs.
     6. Click **Continue**.

     7. To finish creating the account, click **Done**.

  5. Grant the IAM Service Account User role on the default service account to the user-managed service account created in the previous step. After you enabled the Compute Engine API, the default service account is the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`), and the permission is typically assigned through the `roles/iam.serviceAccountUser` role.

**Caution:** Assigning the [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) indirectly grants the role associated with the default service account to the user. For example, if the default service account has the Editor role, the user can then "act as" an Editor. To minimize the impact of these role assignments, we recommend configuring the default service account according to [the principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). For more information, see [Disable automatic role grants to default service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants).
     1. On the **Service Accounts** page, click the email address of the default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`).

     2. Click the **Permissions** tab.

     3. Click the person_add **Grant access** button.

     4. To add a new principal, enter the email address of your service account (`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`).

     5. In the **Select a role** list, select the **Service Accounts** > **Service Account User** role.

     6. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Enable the Artifact Registry, Batch, Cloud Build, Compute Engine Workflow Executions, and Workflows APIs.
         
         gcloud services enable artifactregistry.googleapis.com \
           batch.googleapis.com \
           cloudbuild.googleapis.com \
           compute.googleapis.com \
           workflowexecutions.googleapis.com \
           workflows.googleapis.com

  4. Create a service account for your workflow to use for authentication with other Google Cloud services and grant it the appropriate roles.

     1. Create the service account:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account.

     2. Grant roles to the user-managed service account you created in the previous step. Run the following command once for each of the following IAM roles:

        * `roles/batch.jobsEditor`: to edit Batch jobs.
        * `roles/logging.logWriter`: to write logs.
        * `roles/storage.admin`: to control Cloud Storage resources.
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
      --role=ROLE

Replace the following:

        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note:** The `--role` flag affects which resources your service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs.
  5. Grant the IAM Service Account User role on the default service account to the user-managed service account you created in the previous step. After you enabled the Compute Engine API, the default service account is the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`), and the permission is typically assigned through the `roles/iam.serviceAccountUser` role.

**Caution:** Assigning the [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) indirectly grants the role associated with the default service account to the user. For example, if the default service account has the Editor role, the user can then "act as" an Editor. To minimize the impact of these role assignments, we recommend configuring the default service account according to [the principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). For more information, see [Disable automatic role grants to default service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants).
         
         PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format='value(projectNumber)')
         gcloud iam service-accounts add-iam-policy-binding \
           $PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
           --role=roles/iam.serviceAccountUser




## Create an Artifact Registry repository

Create a repository to store your Docker container image.

###  Console 

  1. In the Google Cloud console, go to the **Repositories** page.

[Go to Repositories](https://console.cloud.google.com/artifacts)

  2. Click add **Create Repository**.

  3. Enter **containers** as the repository name.

  4. For **Format** , choose **Docker**.

  5. For **Location Type** , choose **Region**.

  6. In the **Region** list, select **us-central1**.

  7. Click **Create**.




###  gcloud 

Run the following command:
    
    
      gcloud artifacts repositories create containers \
        --repository-format=docker \
        --location=us-central1
    

You have created an Artifact Registry repository named `containers` in the `us-central1` region. For more information about supported regions, see [Artifact Registry locations](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations).

## Get the code samples

Google Cloud stores the application source code for this tutorial in GitHub. You can clone that repository or download the samples.

  1. Clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/batch-samples.git
         

Alternatively, you can [download the samples in the `main.zip` file](https://github.com/GoogleCloudPlatform/batch-samples/archive/refs/heads/main.zip) and extract it.

  2. Change to the directory that contains the sample code:
         
         cd batch-samples/primegen
         




You now have the source code for the application in your development environment.

## Build the Docker image using Cloud Build

The `Dockerfile` contains the information needed to build a Docker image using Cloud Build. Run the following command to build it:
    
    
    gcloud builds submit \
      -t us-central1-docker.pkg.dev/PROJECT_ID/containers/primegen-service:v1 PrimeGenService/
    

Replace `PROJECT_ID` with your Google Cloud project ID.

When the build is complete, you should see output similar to the following:
    
    
    DONE
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ID: a54818cc-5d14-467b-bfda-5fc9590af68c
    CREATE_TIME: 2022-07-29T01:48:50+00:00
    DURATION: 48S
    SOURCE: gs://project-name_cloudbuild/source/1659059329.705219-17aee3a424a94679937a7200fab15bcf.tgz
    IMAGES: us-central1-docker.pkg.dev/project-name/containers/primegen-service:v1
    STATUS: SUCCESS
    

Using a Dockerfile, you've built a Docker image named `primegen-service` and pushed the image to an Artifact Registry repository named `containers`.

## Deploy a workflow that schedules and runs a Batch job

The following workflow schedules and runs a Batch job that runs a Docker container as six tasks in parallel on two Compute Engine VMs. The result is the generation of six batches of prime numbers, stored in a Cloud Storage bucket.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow, such as `batch-workflow`.

  4. In the **Region** list, select **us-central1**.

  5. Select the **Service account** you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:

### YAML
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                   - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                   - region: "us-central1"
                   - imageUri: ${region + "-docker.pkg.dev/" + projectId + "/containers/primegen-service:v1"}
                   - jobId: ${"job-primegen-" + string(int(sys.now()))}
                   - bucket: ${projectId + "-" + jobId}
             - createBucket:
                 call: googleapis.storage.v1.buckets.insert
                 args:
                   query:
                     project: ${projectId}
                   body:
                     name: ${bucket}
             - logCreateBucket:
                 call: sys.log
                 args:
                   data: ${"Created bucket " + bucket}
             - logCreateBatchJob:
                 call: sys.log
                 args:
                   data: ${"Creating and running the batch job " + jobId}
             - createAndRunBatchJob:
                 call: googleapis.batch.v1.projects.locations.jobs.create
                 args:
                     parent: ${"projects/" + projectId + "/locations/" + region}
                     jobId: ${jobId}
                     body:
                       taskGroups:
                         taskSpec:
                           runnables:
                             - container:
                                 imageUri: ${imageUri}
                               environment:
                                 variables:
                                   BUCKET: ${bucket}
                         # Run 6 tasks on 2 VMs
                         taskCount: 6
                         parallelism: 2
                       logsPolicy:
                         destination: CLOUD_LOGGING
                 result: createAndRunBatchJobResponse
             # You can delete the batch job or keep it for debugging
             - logDeleteBatchJob:
                 call: sys.log
                 args:
                   data: ${"Deleting the batch job " + jobId}
             - deleteBatchJob:
                 call: googleapis.batch.v1.projects.locations.jobs.delete
                 args:
                     name: ${"projects/" + projectId + "/locations/" + region + "/jobs/" + jobId}
                 result: deleteResult
             - returnResult:
                 return:
                   jobId: ${jobId}
                   bucket: ${bucket}

### JSON
         
         {
           "main": {
             "params": [
               "args"
             ],
             "steps": [
               {
                 "init": {
                   "assign": [
                     {
                       "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                     },
                     {
                       "region": "us-central1"
                     },
                     {
                       "imageUri": "${region + \"-docker.pkg.dev/\" + projectId + \"/containers/primegen-service:v1\"}"
                     },
                     {
                       "jobId": "${\"job-primegen-\" + string(int(sys.now()))}"
                     },
                     {
                       "bucket": "${projectId + \"-\" + jobId}"
                     }
                   ]
                 }
               },
               {
                 "createBucket": {
                   "call": "googleapis.storage.v1.buckets.insert",
                   "args": {
                     "query": {
                       "project": "${projectId}"
                     },
                     "body": {
                       "name": "${bucket}"
                     }
                   }
                 }
               },
               {
                 "logCreateBucket": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Created bucket \" + bucket}"
                   }
                 }
               },
               {
                 "logCreateBatchJob": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Creating and running the batch job \" + jobId}"
                   }
                 }
               },
               {
                 "createAndRunBatchJob": {
                   "call": "googleapis.batch.v1.projects.locations.jobs.create",
                   "args": {
                     "parent": "${\"projects/\" + projectId + \"/locations/\" + region}",
                     "jobId": "${jobId}",
                     "body": {
                       "taskGroups": {
                         "taskSpec": {
                           "runnables": [
                             {
                               "container": {
                                 "imageUri": "${imageUri}"
                               },
                               "environment": {
                                 "variables": {
                                   "BUCKET": "${bucket}"
                                 }
                               }
                             }
                           ]
                         },
                         "taskCount": 6,
                         "parallelism": 2
                       },
                       "logsPolicy": {
                         "destination": "CLOUD_LOGGING"
                       }
                     }
                   },
                   "result": "createAndRunBatchJobResponse"
                 }
               },
               {
                 "logDeleteBatchJob": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Deleting the batch job \" + jobId}"
                   }
                 }
               },
               {
                 "deleteBatchJob": {
                   "call": "googleapis.batch.v1.projects.locations.jobs.delete",
                   "args": {
                     "name": "${\"projects/\" + projectId + \"/locations/\" + region + \"/jobs/\" + jobId}"
                   },
                   "result": "deleteResult"
                 }
               },
               {
                 "returnResult": {
                   "return": {
                     "jobId": "${jobId}",
                     "bucket": "${bucket}"
                   }
                 }
               }
             ]
           }
         }
         

  8. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch batch-workflow.JSON_OR_YAML

Replace `JSON_OR_YAML` with `yaml` or `json` depending on the format of your workflow.

  2. In a text editor, copy the following workflow to your source code file:

### YAML
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                   - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                   - region: "us-central1"
                   - imageUri: ${region + "-docker.pkg.dev/" + projectId + "/containers/primegen-service:v1"}
                   - jobId: ${"job-primegen-" + string(int(sys.now()))}
                   - bucket: ${projectId + "-" + jobId}
             - createBucket:
                 call: googleapis.storage.v1.buckets.insert
                 args:
                   query:
                     project: ${projectId}
                   body:
                     name: ${bucket}
             - logCreateBucket:
                 call: sys.log
                 args:
                   data: ${"Created bucket " + bucket}
             - logCreateBatchJob:
                 call: sys.log
                 args:
                   data: ${"Creating and running the batch job " + jobId}
             - createAndRunBatchJob:
                 call: googleapis.batch.v1.projects.locations.jobs.create
                 args:
                     parent: ${"projects/" + projectId + "/locations/" + region}
                     jobId: ${jobId}
                     body:
                       taskGroups:
                         taskSpec:
                           runnables:
                             - container:
                                 imageUri: ${imageUri}
                               environment:
                                 variables:
                                   BUCKET: ${bucket}
                         # Run 6 tasks on 2 VMs
                         taskCount: 6
                         parallelism: 2
                       logsPolicy:
                         destination: CLOUD_LOGGING
                 result: createAndRunBatchJobResponse
             # You can delete the batch job or keep it for debugging
             - logDeleteBatchJob:
                 call: sys.log
                 args:
                   data: ${"Deleting the batch job " + jobId}
             - deleteBatchJob:
                 call: googleapis.batch.v1.projects.locations.jobs.delete
                 args:
                     name: ${"projects/" + projectId + "/locations/" + region + "/jobs/" + jobId}
                 result: deleteResult
             - returnResult:
                 return:
                   jobId: ${jobId}
                   bucket: ${bucket}

### JSON
         
         {
           "main": {
             "params": [
               "args"
             ],
             "steps": [
               {
                 "init": {
                   "assign": [
                     {
                       "projectId": "${sys.get_env(\"GOOGLE_CLOUD_PROJECT_ID\")}"
                     },
                     {
                       "region": "us-central1"
                     },
                     {
                       "imageUri": "${region + \"-docker.pkg.dev/\" + projectId + \"/containers/primegen-service:v1\"}"
                     },
                     {
                       "jobId": "${\"job-primegen-\" + string(int(sys.now()))}"
                     },
                     {
                       "bucket": "${projectId + \"-\" + jobId}"
                     }
                   ]
                 }
               },
               {
                 "createBucket": {
                   "call": "googleapis.storage.v1.buckets.insert",
                   "args": {
                     "query": {
                       "project": "${projectId}"
                     },
                     "body": {
                       "name": "${bucket}"
                     }
                   }
                 }
               },
               {
                 "logCreateBucket": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Created bucket \" + bucket}"
                   }
                 }
               },
               {
                 "logCreateBatchJob": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Creating and running the batch job \" + jobId}"
                   }
                 }
               },
               {
                 "createAndRunBatchJob": {
                   "call": "googleapis.batch.v1.projects.locations.jobs.create",
                   "args": {
                     "parent": "${\"projects/\" + projectId + \"/locations/\" + region}",
                     "jobId": "${jobId}",
                     "body": {
                       "taskGroups": {
                         "taskSpec": {
                           "runnables": [
                             {
                               "container": {
                                 "imageUri": "${imageUri}"
                               },
                               "environment": {
                                 "variables": {
                                   "BUCKET": "${bucket}"
                                 }
                               }
                             }
                           ]
                         },
                         "taskCount": 6,
                         "parallelism": 2
                       },
                       "logsPolicy": {
                         "destination": "CLOUD_LOGGING"
                       }
                     }
                   },
                   "result": "createAndRunBatchJobResponse"
                 }
               },
               {
                 "logDeleteBatchJob": {
                   "call": "sys.log",
                   "args": {
                     "data": "${\"Deleting the batch job \" + jobId}"
                   }
                 }
               },
               {
                 "deleteBatchJob": {
                   "call": "googleapis.batch.v1.projects.locations.jobs.delete",
                   "args": {
                     "name": "${\"projects/\" + projectId + \"/locations/\" + region + \"/jobs/\" + jobId}"
                   },
                   "result": "deleteResult"
                 }
               },
               {
                 "returnResult": {
                   "return": {
                     "jobId": "${jobId}",
                     "bucket": "${bucket}"
                   }
                 }
               }
             ]
           }
         }
         

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy batch-workflow \
           --source=batch-workflow.yaml \
           --location=us-central1 \
           --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account you previously created.




## Execute the workflow

Executing a workflow runs the current workflow definition associated with the workflow.

### Console

  1. In the Google Cloud console, go to the **Workflows** page.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click the **batch-workflow** workflow to go to its details page.

  3. On the **Workflow details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

The workflow execution should take a few minutes.

**Note:** If you encounter an `IAM permission denied for service account` error in the `createBucket` step, this is likely due to a [propagation delay](https://docs.cloud.google.com/iam/docs/access-change-propagation). Wait a minute or two, and then try executing the workflow again.
  5. View the results of the workflow in the **Output** pane.

The results should look similar to the following:
         
         {
           "bucket": "project-name-job-primegen-TIMESTAMP",
           "jobId": "job-primegen-TIMESTAMP"
         }
         




### gcloud

  1. Execute the workflow:
         
         gcloud workflows run batch-workflow \
           --location=us-central1

The workflow execution should take a few minutes.

**Note:** If you encounter an `IAM permission denied for service account` error in the `createBucket` step, this is likely due to a [propagation delay](https://docs.cloud.google.com/iam/docs/access-change-propagation). Wait a minute or two, and then try executing the workflow again.
  2. You can [check the status of a long running execution](https://docs.cloud.google.com/workflows/docs/executing-workflow#check_the_status_of_executions).

  3. To get the status of the last completed execution, run the following command:
         
         gcloud workflows executions describe-last

The results should be similar to the following:
         
         name: projects/PROJECT_NUMBER/locations/us-central1/workflows/batch-workflow/executions/EXECUTION_ID
         result: '{"bucket":"project-name-job-primegen-TIMESTAMP","jobId":"job-primegen-TIMESTAMP"}'
         startTime: '2022-07-29T16:08:39.725306421Z'
         state: SUCCEEDED
         status:
           currentSteps:
           - routine: main
             step: returnResult
         workflowRevisionId: 000001-9ba
         




## List the objects in the output bucket

You can confirm that the results are as expected by listing the objects in your Cloud Storage output bucket.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click on the name of the bucket whose contents you want to view.

The results should be similar to the following, with six files in total, and each listing a batch of 10,000 prime numbers:
         
         primes-1-10000.txt
         primes-10001-20000.txt
         primes-20001-30000.txt
         primes-30001-40000.txt
         primes-40001-50000.txt
         primes-50001-60000.txt
         




### gcloud

  1. Retrieve your output bucket name:
         
         gcloud storage ls

The output is similar to the following: 
         
         gs://PROJECT_ID-job-primegen-TIMESTAMP/

  2. List the objects in your output bucket:
         
         gcloud storage ls gs://PROJECT_ID-job-primegen-TIMESTAMP/** --recursive

Replace `TIMESTAMP` with the timestamp returned by the previous command.

The output should be similar to the following, with six files in total, and each listing a batch of 10,000 prime numbers:
         
         gs://project-name-job-primegen-TIMESTAMP/primes-1-10000.txt
         gs://project-name-job-primegen-TIMESTAMP/primes-10001-20000.txt
         gs://project-name-job-primegen-TIMESTAMP/primes-20001-30000.txt
         gs://project-name-job-primegen-TIMESTAMP/primes-30001-40000.txt
         gs://project-name-job-primegen-TIMESTAMP/primes-40001-50000.txt
         gs://project-name-job-primegen-TIMESTAMP/primes-50001-60000.txt
         




## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

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



### Delete resources created in this tutorial

  1. Delete the Batch job:

     1. First retrieve the job name:
            
            gcloud batch jobs list --location=us-central1

The output should be similar to the following:
            
            NAME: projects/project-name/locations/us-central1/jobs/**job-primegen- TIMESTAMP**
            STATE: SUCCEEDED
            

Where `job-primegen-TIMESTAMP` is the name of the Batch job.

     2. Delete the job:
            
            gcloud batch jobs delete BATCH_JOB_NAME --location us-central1

  2. Delete the workflow:
         
         gcloud workflows delete WORKFLOW_NAME

  3. Delete the container repository:
         
         gcloud artifacts repositories delete REPOSITORY_NAME --location=us-central1

  4. Cloud Build uses Cloud Storage to store build resources. To delete a Cloud Storage bucket, refer to [Delete buckets](https://docs.cloud.google.com/storage/docs/deleting-buckets).




## What's next

  * [Learn more about Batch](https://docs.cloud.google.com/batch/docs).
  * [Learn more about Workflows](https://docs.cloud.google.com/workflows/docs/overview).
  * [Learn more about Workflows connectors](https://docs.cloud.google.com/workflows/docs/connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
