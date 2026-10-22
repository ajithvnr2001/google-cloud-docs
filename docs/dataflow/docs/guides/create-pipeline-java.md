---
url: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java/
title: Create a Dataflow pipeline using Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:27.341774+00:00
---

# Create a Dataflow pipeline using Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Dataflow pipeline using Java

This document shows you how to set up your Google Cloud project, create an example pipeline built with the Apache Beam SDK for Java, and run the example pipeline on the Dataflow service. The pipeline reads a text file from Cloud Storage, counts the number of unique words in the file, and then writes the word counts back to Cloud Storage. For an introduction to the WordCount pipeline, see the [How to use WordCount in Apache Beam](https://www.youtube.com/watch?v=RTIOW1fIhkM) video.

This tutorial requires Maven, but it's also possible to convert the example project from Maven to Gradle. To learn more, see [ Optional: Convert from Maven to Gradle](https://beam.apache.org/get-started/quickstart-java/#optional-convert-from-maven-to-gradle).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=dataflow--quickstart-beam--quickstart-beam-java)

* * *

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

  7. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Cloud Pub/Sub, Cloud Datastore, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api bigquery pubsub datastore.googleapis.com cloudresourcemanager.googleapis.com

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

  15. Enable the Dataflow, Compute Engine, Cloud Logging, Cloud Storage, Google Cloud Storage JSON, BigQuery, Cloud Pub/Sub, Cloud Datastore, and Cloud Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow compute_component logging storage_component storage_api bigquery pubsub datastore.googleapis.com cloudresourcemanager.googleapis.com

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

  20. Copy the following, as you need them in a later section: 
     * Your Cloud Storage bucket name.
     * Your Google Cloud project ID. To find this ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  21. Download and install the [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) version 11. (Dataflow continues to support version 8.) Verify that the [`JAVA_HOME`](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/envvars001.html) environment variable is set and points to your JDK installation.
  22. Download and install [Apache Maven](https://maven.apache.org/download.cgi), following Maven's [installation guide](https://maven.apache.org/install.html) for your specific operating system. 



## Get the pipeline code

The [ Apache Beam SDK](https://beam.apache.org/get-started/beam-overview/) is an open source programming model for data processing pipelines. You define these pipelines with an Apache Beam program and can choose a runner, such as Dataflow, to run your pipeline.

  1. In your shell or terminal, use the [Maven Archetype Plugin](https://maven.apache.org/archetype/maven-archetype-plugin/) to create a Maven project on your computer that contains the Apache Beam SDK's `WordCount` examples: 
         
         mvn archetype:generate \
             -DarchetypeGroupId=org.apache.beam \
             -DarchetypeArtifactId=beam-sdks-java-maven-archetypes-examples \
             -DarchetypeVersion=2.77.0 \
             -DgroupId=org.example \
             -DartifactId=word-count-beam \
             -Dversion="0.1" \
             -Dpackage=org.apache.beam.examples \
             -DinteractiveMode=false
         

The command creates a new directory called `word-count-beam` under your current directory. The `word-count-beam` directory contains a simple `pom.xml` file and a series of example pipelines that count words in text files.

  2. Verify that your `word-count-beam` directory contains the `pom.xml` file: 

### Linux or macOS
         
         cd word-count-beam/
         ls

The output is the following:
         
         pom.xml   src

### Windows
         
         cd word-count-beam/
         dir

The output is the following:
         
         pom.xml   src

  3. Verify that your Maven project contains the example pipelines: 

### Linux or macOS
         
         ls src/main/java/org/apache/beam/examples/

The output is the following:
         
         DebuggingWordCount.java   WindowedWordCount.java   common
         MinimalWordCount.java   WordCount.java

### Windows
         
         dir src/main/java/org/apache/beam/examples/

The output is the following:
         
         DebuggingWordCount.java   WindowedWordCount.java   common
         MinimalWordCount.java   WordCount.java




For a detailed introduction to the Apache Beam concepts that are used in these examples, see the [Apache Beam WordCount Example](https://beam.apache.org/get-started/wordcount-example/). The instructions in the next sections use [ `WordCount.java`](https://github.com/apache/beam/blob/master/examples/java/src/main/java/org/apache/beam/examples/WordCount.java).

## Run the pipeline locally

  * In your shell or terminal, run the `WordCount` pipeline locally from your `word-count-beam` directory: 
        
        mvn compile exec:java \
            -Dexec.mainClass=org.apache.beam.examples.WordCount \
            -Dexec.args="--output=counts"
        

The output files have the prefix `counts` and are written to the `word-count-beam` directory. They contain unique words from the input text and the number of occurrences of each word.




## Run the pipeline on the Dataflow service

  * In your shell or terminal, build and run the `WordCount` pipeline on the Dataflow service from your `word-count-beam` directory: 
        
        mvn -Pdataflow-runner compile exec:java \
            -Dexec.mainClass=org.apache.beam.examples.WordCount \
            -Dexec.args="--project=PROJECT_ID \
            --gcpTempLocation=gs://BUCKET_NAME/temp/ \
            --output=gs://BUCKET_NAME/output \
            --runner=DataflowRunner \
            --region=REGION"
        

Replace the following:

    * `PROJECT_ID`: your Google Cloud project ID
    * `BUCKET_NAME`: the name of your Cloud Storage bucket
    * `REGION`: a [Dataflow region](https://docs.cloud.google.com/dataflow/docs/resources/locations), like `us-central1`
**Note:**
    * To specify a [user-managed worker service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#user-managed), include the `--serviceAccount` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options). User-managed worker service accounts are recommended for production workloads. If you don't specify a worker service account when you create a job, Dataflow uses the [Compute Engine default service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#default-service-account).
    * Unless specified through the `network` option, the Dataflow runner runs jobs in the `default` Virtual Private Cloud network.



## View your results

  1. In the Google Cloud console, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

The **Jobs** page shows the details of all the available jobs, including the status. The **wordcount** job's **Status** is **Running** at first, and then updates to **Succeeded**.

  2. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

The **Buckets** page displays the list of all the storage buckets in your project.

  3. Click the storage bucket that you created.  


The **Bucket details** page shows the output files and staging files that your Dataflow job created.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the project

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the quickstart. 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to keep the Google Cloud project that you used in this quickstart, then delete the individual resources: 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 
  4. Revoke the roles that you granted to the Compute Engine default service account. Run the following command once for each of the following IAM roles:

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

  * Learn about [the Apache Beam programming model](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model).
  * Learn how to [use Apache Beam to build pipelines](https://docs.cloud.google.com/dataflow/docs/guides/use-beam).
  * Work through [the WordCount and Mobile Gaming examples](https://docs.cloud.google.com/dataflow/docs/samples/beam-samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
