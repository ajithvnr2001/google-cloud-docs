---
url: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-go/
title: Create a Dataflow pipeline using Go \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:20.793925+00:00
---

# Create a Dataflow pipeline using Go  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Dataflow pipeline using Go

This page shows you how to use the Apache Beam SDK for Go to build a program that defines a pipeline. Then, you run the pipeline locally and on the Dataflow service. For an introduction to the WordCount pipeline, see the [How to use WordCount in Apache Beam](https://www.youtube.com/watch?v=RTIOW1fIhkM) video.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api cloudresourcemanager.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api cloudresourcemanager.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Grant roles to your Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.objectAdmin`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

     * Replace `PROJECT_ID` with your project ID.
     * Replace `PROJECT_NUMBER` with your project number. To find your project number, see [Identify projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) or use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.
     * Replace `SERVICE_ACCOUNT_ROLE` with each individual role.
  19. Create a Cloud Storage bucket and configure it as follows:
     * Set the storage class to `S` (Standard). 
     * Set the storage location to the following: `US` (United States). 
     * Replace `BUCKET_NAME` with a unique bucket name. Don't include sensitive information in the bucket name because the bucket namespace is global and publicly visible. 
    
    gcloud storage buckets create gs://BUCKET_NAME --default-storage-class STANDARD --location US

  20. Copy the Google Cloud project ID and the Cloud Storage bucket name. You need these values later in this quickstart.




## Set up your development environment

The Apache Beam SDK is an open source programming model for data pipelines. You define a pipeline with an Apache Beam program and then choose a runner, such as Dataflow, to run your pipeline.

We recommend that you use the latest version of Go when working with the Apache Beam SDK for Go. If you don't have the latest version of Go installed, use Go's [Download and install guide](https://go.dev/doc/install) to download and install Go for your specific operating system.

To verify the version of Go that you have installed, run the following command in your local terminal:
    
    
    go version

## Run the Beam wordcount example

The Apache Beam SDK for Go includes a [`wordcount` pipeline example](https://github.com/apache/beam/blob/master/sdks/go/examples/wordcount/wordcount.go). The `wordcount` example does the following:

  1. Reads a text file as input. By default, it reads a text file located in a Cloud Storage bucket with the resource name `gs://dataflow-samples/shakespeare/kinglear.txt`.
  2. Parses each line into words.
  3. Performs a frequency count on the tokenized words.



To run the latest version of the Beam `wordcount` example on your local machine, perform the following steps:

  1. Use the `git clone` command to clone the `apache/beam` GitHub repository:
         
         git clone https://github.com/apache/beam.git

  2. Switch to the `beam/sdks/go` directory:
         
         cd beam/sdks/go

  3. Use the following command to run the pipeline:
         
         go run examples/wordcount/wordcount.go \
           --input gs://dataflow-samples/shakespeare/kinglear.txt \
           --output outputs

The `input` flag specifies the file to read, and the `output` flag specifies the filename for the frequency count output.




After the pipeline completes, view the output results:
    
    
    more outputs*

To exit, press `q`.

## Modify the pipeline code

The Beam `wordcount` pipeline distinguishes between uppercase and lowercase words. The following steps show how to create your own Go module, modify the `wordcount` pipeline so that the pipeline is not case-sensitive, and run it on Dataflow.

### Create a Go module

To make changes to the pipeline code, follow these steps.

  1. Create a directory for your Go module in a location of your choice:
         
         mkdir wordcount
         cd wordcount

  2. Create a Go module. For this example, use `example/dataflow` as the module path.
         
         go mod init example/dataflow

  3. Download the latest copy of the [`wordcount` code](https://github.com/apache/beam/blob/master/sdks/go/examples/wordcount/wordcount.go) from the Apache Beam GitHub repository. Put this file into the `wordcount` directory you created.

  4. If you are using a non-Linux operating system, you must get the [Go `unix` package](https://pkg.go.dev/golang.org/x/sys/unix). This package is required to run pipelines on the Dataflow service.
         
         go get -u golang.org/x/sys/unix

  5. Ensure that the `go.mod` file matches the module's source code:
         
         go mod tidy




### Run the unmodified pipeline

Verify the unmodified `wordcount` pipeline runs locally.

  1. From the terminal, build and run the pipeline locally:
         
         go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \
              --output outputs

  2. View the output results:
         
         more outputs*

  3. To exit, press `q`.




### Change the pipeline code

To change the pipeline so that it is not case-sensitive, modify the code to apply the [`strings.ToLower`](https://pkg.go.dev/strings#ToLower) function to all words.

  1. In an editor of your choice, open the `wordcount.go` file.

  2. Examine the `init` block (comments have been removed for clarity):
         
         func init() {
            register.DoFn3x0[context.Context, string, func(string)](&extractFn{})
            register.Function2x1(formatFn)
            register.Emitter1[string]()
          }
         

  3. Add a new line to register the `strings.ToLower` function:
         
         func init() {
            register.DoFn3x0[context.Context, string, func(string)](&extractFn{})
            register.Function2x1(formatFn)
            register.Emitter1[string]()
            **register.Function1x1(strings.ToLower)**
          }
         

  4. Examine the `CountWords` function:
         
         func CountWords(s beam.Scope, lines beam.PCollection) beam.PCollection {
            s = s.Scope("CountWords")
         
            // Convert lines of text into individual words.
            col := beam.ParDo(s, &extractFn{SmallWordLength: *smallWordLength}, lines)
         
            // Count the number of times each word occurs.
            return stats.Count(s, col)
          }
         

  5. To lowercase the words, add a [ParDo](https://pkg.go.dev/github.com/apache/beam/sdks/go/pkg/beam#ParDo) that applies `strings.ToLower` to every word:
         
         func CountWords(s beam.Scope, lines beam.PCollection) beam.PCollection {
            s = s.Scope("CountWords")
         
            // Convert lines of text into individual words.
            col := beam.ParDo(s, &extractFn{SmallWordLength: *smallWordLength}, lines)
         
            **// Map all letters to lowercase.
            lowercaseWords := beam.ParDo(s, strings.ToLower, col)**
         
            // Count the number of times each word occurs.
            return stats.Count(s, **lowercaseWords**)
          }
         

  6. Save the file.




### Run the updated pipeline locally

Run your updated `wordcount` pipeline locally and verify the output has changed.

  1. Build and run the modified `wordcount` pipeline:
         
         go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \
              --output outputs

  2. View the output results of the modified pipeline. All words should be lowercase.
         
         more outputs*

  3. To exit, press `q`.




### Run the pipeline on the Dataflow service

To run the updated `wordcount` example on the Dataflow service, use the following command:
    
    
    go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \
        --output gs://BUCKET_NAME/results/outputs \
        --runner dataflow \
        --project PROJECT_ID \
        --region DATAFLOW_REGION \
        --staging_location gs://BUCKET_NAME/binaries/

Replace the following:

  * `BUCKET_NAME`: the Cloud Storage bucket name.

  * `PROJECT_ID`: the Google Cloud project ID.

  * `DATAFLOW_REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job. For example, `europe-west1`. For a list of available locations, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). The `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.


**Note:** To specify a [user-managed worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#user-managed), include the `--service_account_email` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options). User-managed worker service accounts are recommended for production workloads. If you don't specify a worker service account when you create a job, Dataflow uses the [Compute Engine default service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#default-service-account).

## View your results

You can see a list of your Dataflow jobs in Google Cloud console. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow)

The **Jobs** page displays details of your `wordcount` job, including a status of **Running** at first, and then **Succeeded**.

When you run a pipeline using Dataflow, your results are stored in a Cloud Storage bucket. View the output results by using either the Google Cloud console or the local terminal.

### Console

To view your results in the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

From the list of buckets in your project, click the storage bucket that you created earlier. The output files that your job created are displayed in the `results` directory.

### Terminal

View the results from your terminal or by using Cloud Shell.

  1. To list the output files, use the [`gcloud storage ls` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls):
         
         gcloud storage ls gs://BUCKET_NAME/results/outputs* --long

Replace `BUCKET_NAME` with the name of the specified output Cloud Storage bucket.

  2. To view the results in the output files, use the [`gcloud storage cat` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat):
         
         gcloud storage cat gs://BUCKET_NAME/results/outputs*




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

**Note:** If you followed this quickstart in a new project, then you can [delete the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects). 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 
  4. If you keep your project, revoke the roles that you granted to the Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.objectAdmin`
    
    gcloud projects remove-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
        --role=SERVICE_ACCOUNT_ROLE

  5. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  6. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * [Programming model for Apache Beam](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model)
  * [Setting pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options)
  * [Pipeline options reference](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options)
  * [Deploying a pipeline](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
