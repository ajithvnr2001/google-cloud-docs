---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/workflow-function/
title: Workflow using Cloud Run functions \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:29.431472+00:00
---

# Workflow using Cloud Run functions  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/workflow-function/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Workflow using Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:**

  1. Create a Managed Service for Apache Spark workflow template that runs a wordcount job
  2. Create a node.js Cloud function to trigger the wordcount workflow when a file is added to Cloud Storage

Workflows are "fire and forget". If there are no exceptions when the function that triggers the workflow is submitted, Managed Service for Apache Spark will execute the workflow to completion. You do not need to wait on workflow completion within the triggering function.**Note:** Since the function is triggered by adding a new file to a bucket in Cloud Storage, and since the wordcount binary creates and outputs new files to Cloud Storage, to avoid recursion (wordcount processing its output files), this tutorial uses separate input and output buckets.

## Before you begin

If you haven't already done so, set up a Google Cloud project and two (**2**) Cloud Storage [buckets](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create).

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Compute Engine, Cloud Storage, and Cloud Run functions APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com,cloudfunctions.googleapis.com)

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

  10. Enable the Dataproc, Compute Engine, Cloud Storage, and Cloud Run functions APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage-component.googleapis.com,cloudfunctions.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Create or use two Cloud Storage buckets in your project

You will need two Cloud Storage buckets in your project: one for input files and another for output. 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**. 
  3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. In the **Choose where to store your data** section, do the following: 
        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
        2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following: 
        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  4. Click **Create**. 



## Create a workflow template

To create and define a [workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows), copy and run the following commands in a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true).

**Note:**

  * The commands specify the "us-central1" [region](https://docs.cloud.google.com/compute/docs/regions-zones#available). You can specify a different region or delete the `--region` flag if you have previously run [`gcloud config set compute/region`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#compute) to set the region property.
  * The "-- " (dash dash space) sequence passes arguments to the jar file. The `wordcount input_bucket output_dir` command will run the jar's wordcount application on text files contained in the Cloud Storage `input_bucket`, then output wordcount files to an `output_bucket`. You will parameterize the wordcount input bucket argument to allow your function to supply this argument.



  1. Create the workflow template. 
         
         gcloud dataproc workflow-templates create wordcount-template \
               --region=us-central1
           

  2. Add the wordcount job to the workflow template. 
     1. Specify your output-bucket-name before running the command (your function will supply the input bucket). After you insert the output-bucket-name, the output bucket argument should read as follows: `gs://your-output-bucket/wordcount-output"`. 
     2. The "count" step ID is required, and identifies the added hadoop job. 
            
            gcloud dataproc workflow-templates add-job hadoop \
                          --workflow-template=wordcount-template \
                          --step-id=count \
                          --jar=file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar \
                          --region=us-central1 \
                          -- wordcount gs://input-bucket gs://output-bucket-name/wordcount-output
                    

  3. Use a [managed](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview#managed_cluster), [single-node](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) cluster to run the workflow. Managed Service for Apache Spark will create the cluster, run the workflow on it, then delete the cluster when the workflow completes. 
         
         gcloud dataproc workflow-templates set-managed-cluster wordcount-template \
                 --cluster-name=wordcount \
                 --single-node \
                 --region=us-central1
             

  4. Click the `wordcount-template` name on the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/templates) page in the Google Cloud console to open the **Workflow template details** page. Confirm the wordcount-template attributes. ![workflow template details page](https://docs.cloud.google.com/static/managed-spark/images/wordcount-template.png)



## Parameterize the workflow template

[Parameterize](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-parameters) the input bucket variable to pass to the workflow template.

  1. Export the workflow template to a `wordcount.yaml` text file for parameterization. 
         
         gcloud dataproc workflow-templates export wordcount-template \
             --destination=wordcount.yaml \
             --region=us-central1
         

  2. Using a text editor, open `wordcount.yaml`, then add a `parameters` block to the end of YAML file so that the Cloud Storage INPUT_BUCKET_URI can be passed as `args[1]` to the wordcount binary when the workflow is triggered. 

A sample exported YAML file is shown, below. You can take one of two approaches to update your template:

     1. Copy then paste the entire file to replace your exported `wordcount.yaml` **after replacing your-output_bucket with your output bucket name**, OR
     2. Copy then paste only the `parameters` section to the end of your exported `wordcount.yaml` file. 
. 
    
    jobs:
    - hadoopJob:
        args:
        - wordcount
        - gs://input-bucket
        - gs://your-output-bucket/wordcount-output
        mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
      stepId: count
    placement:
      managedCluster:
        clusterName: wordcount
        config:
          softwareConfig:
            properties:
              dataproc:dataproc.allow.zero.workers: 'true'
    parameters:
    - name: INPUT_BUCKET_URI
      description: wordcount input bucket URI
      fields:
      - jobs['count'].hadoopJob.args[1]
    

  3. Import the parameterized `wordcount.yaml` text file. Type 'Y'es when asked to overwrite the template. 
         
         gcloud dataproc workflow-templates import  wordcount-template \
             --source=wordcount.yaml \
             --region=us-central1
         




## Create a Cloud function

  1. Open the **[Cloud Run functions](https://console.cloud.google.com/functions/list)** page in the Google Cloud console, then click CREATE FUNCTION.

  2. On the **Create function** page, enter or select the following information:

     1. **Name:** wordcount
     2. **Memory allocated:** Keep the default selection.
     3. **Trigger:**
        * Cloud Storage
        * Event Type: Finalize/Create
        * Bucket: Select your input bucket (see Create a Cloud Storage bucket in your project). When a file is added to this bucket, the function will trigger the workflow. The workflow will run the wordcount application, which will process all text files in the bucket.
     4. **Source code:**

        * Inline editor
        * Runtime: Node.js 8
        * `INDEX.JS` tab: Replace the default code snippet with the following code, then **edit the`const projectId` line to supply -your-project-id- (without a leading or trailing "-")**.
    
    const dataproc = require('@google-cloud/dataproc').v1;
    
    exports.startWorkflow = (data) => {
     const projectId = '-your-project-id-'
     const region = 'us-central1'
     const workflowTemplate = 'wordcount-template'
    
    const client = new dataproc.WorkflowTemplateServiceClient({
       apiEndpoint: `${region}-dataproc.googleapis.com`,
    });
    
    const file = data;
    console.log("Event: ", file);
    
    const inputBucketUri = `gs://${file.bucket}/${file.name}`;
    
    const request = {
      name: client.projectRegionWorkflowTemplatePath(projectId, region, workflowTemplate),
      parameters: {"INPUT_BUCKET_URI": inputBucketUri}
    };
    
    client.instantiateWorkflowTemplate(request)
      .then(responses => {
        console.log("Launched Dataproc Workflow:", responses[1]);
      })
      .catch(err => {
        console.error(err);
      });
    };
    

        * `PACKAGE.JSON` tab: Replace the default code snippet with the following code.
    
    {
      "name": "dataproc-workflow",
      "version": "1.0.0",
      "dependencies":{ "@google-cloud/dataproc": ">=1.0.0"}
    }
    

        * Function to execute: Insert: "startWorkflow".
     5. Click CREATE.




## Test your function

  1. Copy public file `rose.txt` to your bucket to trigger the function. Insert your-input-bucket-name (the bucket used to trigger your function) in the command. 
         
         gcloud storage cp gs://pub/shakespeare/rose.txt gs://your-input-bucket-name
         

  2. Wait 30 seconds, then run the following command to verify the function completed successfully. 
         
         gcloud functions logs read wordcount
         
         
         ...
         Function execution took 1348 ms, finished with status: 'ok'
         

  3. To view the function logs from the [Functions](https://console.cloud.google.com/functions/list) list page in the Google Cloud console, click the `wordcount` function name, then click VIEW LOGS on the **Function details** page. ![](https://docs.cloud.google.com/static/managed-spark/images/function-logs.png)

  4. You can view the `wordcount-output` folder in your output bucket from the [Storage browser](https://console.cloud.google.com/storage/browser) page in the Google Cloud console. ![](https://docs.cloud.google.com/static/managed-spark/images/wordcount-output-bucket.png)

**Note:** The wordcount job will fail if the `wordcount-output` folder exists. Before re-running the workflow by re-triggering your function, first delete the `wordcount-output` folder in your output bucket.
  5. After the workflow completes, job details persist in the Google Cloud console. Click the `count...` job listed on the Managed Service for Apache Spark [Jobs](https://console.cloud.google.com/dataproc/jobs) page to view workflow job details. ![](https://docs.cloud.google.com/static/managed-spark/images/workflow-job.png)




## Clean up

The workflow in this tutorial deletes its managed cluster when the workflow completes. To avoid recurring costs, you can delete other resources associated with this tutorial.

### Delete a project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete Cloud Storage buckets

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the checkbox for the bucket that you want to delete. 
  3. To delete the bucket, click delete **Delete** , and then follow the instructions. 



### Delete your workflow template
    
    
    gcloud dataproc workflow-templates delete wordcount-template \
        --region=us-central1
    

### Delete your Cloud function

Open the **[Cloud Run functions](https://console.cloud.google.com/functions/list)** page in the Google Cloud console, select the box to the left of the `wordcount` function, then click **Delete**.

## What's next

  * See [Overview of Managed Service for Apache Spark workflow templates](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview).
  * See [Workflow scheduling solutions](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-schedule-solutions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
