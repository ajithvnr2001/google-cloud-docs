---
url: https://docs.cloud.google.com/scheduler/docs/tut-workflows/
title: Schedule Workflows \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:59.643262+00:00
---

# Schedule Workflows  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/tut-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Schedule Workflows Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to use Cloud Scheduler to automatically execute [Workflows](https://docs.cloud.google.com/workflows) so that a workflow runs on a particular schedule, in this case every 5 minutes.

## Objectives

  1. Create and deploy a workflow that can receive runtime arguments.
  2. Create a Cloud Scheduler job that triggers your workflow and executes it every 5 minutes, passing in JSON arguments in the correct format.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine)
  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. [Set up your environment](https://docs.cloud.google.com/scheduler/docs/setup) for Cloud Scheduler, including creating an App Engine app. 
  2. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com&redirect=https%3A//cloud.google.com/scheduler/docs/CS-tut-workflows)

  3. Set the default location used in this tutorial: 
         
         gcloud config set workflows/location REGION

Replace `REGION` with the supported Workflows [location](https://docs.cloud.google.com/workflows/docs/locations) of your choice. 
  4. Create a service account for Workflows to use; for example, `sa-name`. 
         
         gcloud iam service-accounts create sa-name

  5. Grant your service account the `workflows.invoker` role so that the account has permission to trigger your workflow: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
               --member "serviceAccount:sa-name@PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/workflows.invoker"

Replace `PROJECT_ID` with your Google Cloud project ID. 
  6. Grant the `logging.logWriter` role to the service account. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
               --member "serviceAccount:sa-name@PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/logging.logWriter"




## Create a workflow that receives runtime arguments

A workflow definition is made up of a series of steps described using the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax), which can be written in either YAML or JSON format. After creating a workflow, you deploy it to make it available for execution.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click **Create**.

  3. Enter `myFirstWorkflow` as a name for your new workflow.

  4. Select **us-east1** for the region.

  5. Select the service account you created previously.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow.

### YAML
         
         main:
           params: [args]
           steps:
             - step1:
                 assign:
                   - outputVar: ${"Hello, " + args.firstName + " " + args.lastName + "!"}
             - step2:
                 return: ${outputVar}

### JSON
         
         {
           "main": {
             "params": [
               "args"
             ],
             "steps": [
               {
                 "step1": {
                   "assign": [
                     {
                       "outputVar": "${\"Hello \" + args.firstName + \" \" + args.lastName}"
                     }
                   ]
                 }
               },
               {
                 "step2": {
                   "return": "${outputVar}"
                 }
               }
             ]
           }
         }
           

This workflow returns a "Hello" greeting to a person whose first and last name you pass as runtime arguments.

  8. Click **Deploy**.




### gcloud

  1. Open a terminal.
  2. Save the following workflow definition as a YAML or JSON file, such as myFirstWorkflow.yaml or myFirstWorkflow.json.

### YAML
         
         main:
           params: [args]
           steps:
             - step1:
                 assign:
                   - outputVar: ${"Hello, " + args.firstName + " " + args.lastName + "!"}
             - step2:
                 return: ${outputVar}

### JSON
         
         {
           "main": {
             "params": [
               "args"
             ],
             "steps": [
               {
                 "step1": {
                   "assign": [
                     {
                       "outputVar": "${\"Hello \" + args.firstName + \" \" + args.lastName}"
                     }
                   ]
                 }
               },
               {
                 "step2": {
                   "return": "${outputVar}"
                 }
               }
             ]
           }
         }
           

This workflow returns a "Hello" greeting to a person whose first and last name you pass as runtime arguments.

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy myFirstWorkflow \
             --location=us-east1 \
             --source=myFirstWorkflow.yaml_OR_json \
             --service-account=sa-name@PROJECT_ID.iam.gserviceaccount.com

Replace `yaml_OR_json` with `yaml` or `json` depending on the format of the Workflows definition file that you created previously.




## Schedule the workflow

Create a Cloud Scheduler job that triggers your workflow, using the service account you previously created.

### Console

  1. In the Google Cloud console, go to the **Cloud Scheduler** page:

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Click **Create Job**.

  3. Set the **Name** to `my-workflow-job`.

  4. For **Region** , select **us-east1 (South Carolina)**.

  5. For **Frequency** , enter: 
         
         */5 * * * *

This will execute the job every 5 minutes. The interval is defined using [unix-cron](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules) format.
  6. For **Timezone** , select a country and timezone.

For example, select United States and Los Angeles or **Pacific Daylight Time (PDT)**.

  7. Click **Continue**.

  8. For **Target type** , select **HTTP**.

  9. For **URL** , enter: 
         
         https://workflowexecutions.googleapis.com/v1/projects/PROJECT_ID/locations/us-east1/workflows/myFirstWorkflow/executions
         

  10. Leave the **HTTP method** at the default of **POST**.

  11. Add the following two **HTTP headers** :

     * Name: `Content-Type` and Value: `application/octet-stream`
     * Name: `User-Agent` and Value: `Google-Cloud-Scheduler`
  12. For **Body** , enter: 
         
         {"argument": "{\"firstName\":\"Sherlock\", \"lastName\":\"Holmes\"}"}
         

This passes a JSON encoding of the workflow's arguments; in this case, the first name, "Sherlock", and the last name, "Holmes". The double quotation marks inside the string are escaped using backslashes (\\).

  13. For **Auth header** , select **Add OAuth token**.

  14. Enter the service account you previously created. 
         
         sa-name@PROJECT_ID.iam.gserviceaccount.com
         

You don't have to specify the **Scope** as the default of `https://www.googleapis.com/auth/cloud-platform` is used.
  15. Accept all the other defaults and click **Create**.




### gcloud

Schedule a job called `my-workflow-job` by entering the following command:
    
    
    gcloud scheduler jobs create http my-workflow-job \
        --location="us-east1" \
        --schedule="*/5 * * * *" \
        --uri="https://workflowexecutions.googleapis.com/v1/projects/PROJECT_ID/locations/us-east1/workflows/myFirstWorkflow/executions" \
        --message-body="{\"argument\": \"{\\\"firstName\\\":\\\"Sherlock\\\", \\\"lastName\\\":\\\"Holmes\\\"}\"}" \
        --time-zone="America/Los_Angeles" \
        --oauth-service-account-email="sa-name@PROJECT_ID.iam.gserviceaccount.com"

The interval is defined using [unix-cron](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules) format.

The `message-body` flag is used to pass a JSON encoding of the workflow's arguments; in this case, the first name, "Sherlock", and the last name, "Holmes". The double quotation marks inside the string are escaped using backslashes (\\).

Your workflow now executes every 5 minutes.

For more information about the `gcloud scheduler` flags, as well as how to apply call logging so that each call step during the execution of your workflow is logged, see [Schedule a workflow](https://docs.cloud.google.com/workflows/docs/schedule-workflow) and the `gcloud` [reference](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/http).

**Note:** Each execution of a workflow incurs costs, as detailed in [Workflows pricing](https://cloud.google.com/workflows/pricing). To stop incurring costs from a scheduled workflow, delete the Cloud Scheduler job.

## Run the job and verify the results

### Console

  1. In the Google Cloud console, go to the **Cloud Scheduler** page:

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

If the job is not displayed, you might have to refresh the page.

  2. For the job named `my-workflow-job`, click **Run now**.

You should see the **Result** value update to **Success**.

  3. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  4. From the list of workflows, click **myFirstWorkflow** to open its details page.

The execution state of your workflow should be **Succeeded**.

  5. Click the workflow's execution ID to open the details page and view the results of the workflow in the Output pane.

The output should be "Hello, Sherlock Holmes!".




### gcloud

  1. Run the Cloud Scheduler job to execute the workflow:
         
         gcloud scheduler jobs run my-workflow-job --location="us-east1"
         

  2. Retrieve the execution ID for your workflow:
         
         gcloud workflows executions list myFirstWorkflow
         

The output should resemble the following with the execution ID in bold:
         
         projects/316710615161/locations/us-east1/workflows/myFirstWorkflow/executions/**138b31e1-f3bb-4ba7-a6da-008d0cb4a320**

  3. Retrieve the results of the workflow's execution: 
         
         gcloud workflows executions describe EXECUTION_ID --workflow myFirstWorkflow

Replace `EXECUTION_ID` with the execution ID returned in the previous step.

The output should resemble the following: 
         
         argument: '{"firstName":"Sherlock","lastName":"Holmes"}'
         endTime: '2021-09-09T15:15:00.869350639Z'
         name: projects/316710615161/locations/us-east1/workflows/myFirstWorkflow/executions/138b31e1-f3bb-4ba7-a6da-008d0cb4a320
         result: '"Hello, Sherlock Holmes!"'
         startTime: '2021-09-09T15:15:00.839175480Z'
         state: SUCCEEDED
         workflowRevisionId: 000001-4f9




Congratulations! You have successfully created a Cloud Scheduler job that automatically runs a workflow on a particular schedule.

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

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



### Delete the Cloud Scheduler job

  1. Go to the **Cloud Scheduler** page in the Google Cloud console.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Select the checkbox next to your job.

  3. Click **Delete** at the top of the page and confirm your deletion.




### Delete the Workflows workflow

  1. Go to the **Workflows** page in the Google Cloud console.

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Select your workflow.

  3. Click **Delete** at the top of the page; type your workflow's name, and confirm your deletion.




### Disable the App Engine app

Disabling an App Engine app stops your application from running instances and serving requests while retaining application data and settings.

  1. Go to the **Application settings** page in the Google Cloud console.

[Go to Application settings](https://console.cloud.google.com/appengine/settings)

  2. Click **Disable application**.

  3. Follow the prompts.




## What's next

  * Learn more about [Workflows](https://docs.cloud.google.com/workflows/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
