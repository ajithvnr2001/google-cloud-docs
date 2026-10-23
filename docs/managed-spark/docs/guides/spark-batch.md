---
url: https://docs.cloud.google.com/managed-spark/docs/guides/spark-batch/
title: Submit an Apache Spark batch workload \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:18.580011+00:00
---

# Submit an Apache Spark batch workload  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/spark-batch/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Submit an Apache Spark batch workload Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to submit a batch workload on Managed Service for Apache Spark compute infrastructure that scales resources as needed.

## Before you begin

Set up your project and, if needed, grant Identity and Access Management roles.

### Set up your project

Perform one or more of the following steps as needed:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc)




### Grant IAM roles if needed

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to submit a serverless batch workload, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to submit a serverless batch workload, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Submit a Spark batch workload

You can use the Google Cloud console, the Google Cloud CLI, or the REST API to create and submit a Managed Service for Apache Spark batch workload.

**Note:** You can use the [**Create batch from template**](https://console.cloud.google.com/dataproc/templates/createBatch) page in the console to run submit a batch based on a saved template. For more information, see [Managed Service for Apache Spark templates ](https://docs.cloud.google.com/managed-spark/docs/templates/templates).

### Console

  1. In the Google Cloud console, [go to Managed Service for Apache Spark Batches](https://console.cloud.google.com/dataproc/batches).

  2. Click **Create**.

  3. Submit a Spark batch workload that computes the approximate value of pi by selecting and filling in the following fields:

     * **Batch Info:**
       * **Batch ID** : Specify an ID for your batch workload. This value must be 4-63 lowercase characters. Valid characters are `/[a-z][0-9]-/`.
       * **Region** : Select a [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload will run.
     * **Container:**
       * **Batch type** : Spark.
       * **Runtime version** : Confirm or select the `3.0` runtime version.
       * **Main class** : 
             
             org.apache.spark.examples.SparkPi

       * **Jar files** (this file is pre-installed in the Managed Service for Apache Spark execution environment). 
             
             file:///usr/lib/spark/examples/jars/spark-examples.jar

       * **Arguments** : 1000.
     * **Execution Configuration:** Select **Service Account**. By default, the batch will run using the [Compute Engine default service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account). You can specify a custom service account. The default or custom service account must have the [Dataproc Worker role](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#required-dataproc-worker-role).
     * **Network configuration:** Select a **subnetwork** in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the specified subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).
     * **Properties:** Enter the `Key` (property name) and `Value` of [supported Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties) to set on your Spark batch workload. Note: Unlike Managed Service for Apache Spark [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties), Managed Service for Apache Spark workload properties don't include a `spark:` prefix.
     * **Other options:**
       * You can configure the batch workload to use an external [self-managed **Hive Metastore**](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc).
       * You can use a [Persistent History Server (PHS)](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server). The PHS must be located in the region where you run batch workloads.
  4. Click **Submit** to run the Spark batch workload.




### gcloud

To submit a Spark batch workload to compute the approximate value of `pi`, run the following gcloud CLI [`gcloud dataproc batches submit spark`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit) command locally in a terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true).
    
    
    gcloud dataproc batches submit spark \
        --region=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
        --version=3.0 \
        --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
        --class=org.apache.spark.examples.SparkPi \
        -- 1000
    

Replace the following: 

  * REGION: Specify the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your workload will run.
  * **Other options:** You can add [`gcloud dataproc batches submit spark`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark) flags to specify other workload options and Spark properties. 
    * [`--jars`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--jars): The example JAR file is pre-installed in the Spark execution environment, The `1000` command argument passed to the SparkPi workload specifies 1000 iterations of the pi estimation logic (workload input arguments are included after the "-- ").
    * [`--subnet`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/sessions/create#--subnet): You can add this flag to specify the name of a subnet in the session region. If you don't specify a subnet, Managed Service for Apache Spark selects the `default` subnet in the session region. Managed Service for Apache Spark enables [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnet. For network connectivity requirements, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network#open_subnet_connectivity).
    * [`--tags`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--tags): You can add this flag to specify network tags for traffic control. Use network tags to limit connectivity. In production, the recommended practice is to limit firewall rules to the IP addresses used by your Spark workloads.
    * [`--properties`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--properties): You can add this flag to enter [supported Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties) for your Spark batch workload to use.
    * [`--deps-bucket`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--deps-bucket): You can add this flag to specify a Cloud Storage bucket where Managed Service for Apache Spark will upload workload dependencies. The `gs://` URI prefix of the bucket is not required; you can specify the bucket path or bucket name. Managed Service for Apache Spark uploads the local file(s) to a `/dependencies` folder in the bucket before running the batch workload. **Note:** This flag is **required** if your batch workload references files on your local machine.
    * [`--ttl`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--ttl): You can add the [`--ttl`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit#--ttl) flag to specify the duration of the batch lifetime. When the workload exceeds this duration, it is unconditionally terminated without waiting for ongoing work to finish. Specify the duration using a `s`, `m`, `h`, or `d` (seconds, minutes, hours, or days) suffix. The minimum value is 10 minutes (`10m`), and the maximum value is 14 days (`14d`). 
      * **1.1 or 2.0 runtime batches:** If `--ttl` is not specified for a 1.1 or 2.0 runtime batch workload, the workload is allowed to run until it exits naturally (or run forever if it doesn't exit).
      * **2.1+ runtime batches:** If `--ttl` is not specified for a 2.1 or later runtime batch workload, it defaults to `4h`.
    * [`--service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--service-account): You can specify a [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account) to use to run your workload. If you don't specify a service account, the workload runs under the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Your service account must have the [Dataproc Worker role](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account#required-dataproc-worker-role). 
    * **Hive Metastore** : The following command configures a batch workload to use an external [self-managed Hive Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/attach-dataproc) using a standard Spark configuration. 
          
          gcloud dataproc batches submit spark\
              --properties=spark.sql.catalogImplementation=hive,spark.hive.metastore.uris=METASTORE_URI,spark.hive.metastore.warehouse.dir=WAREHOUSE_DIR> \
              other args ...
                  

    * **[Persistent History Server](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server):**
      1. The following command creates a PHS on a single-node Managed Service for Apache Spark cluster. The PHS must be located in the region where you run batch workloads, and the Cloud Storage bucket-name must exist. 
             
             gcloud dataproc clusters create PHS_CLUSTER_NAME \
                 --region=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
                 --single-node \
                 --enable-component-gateway \
                 --properties=spark:spark.history.fs.logDirectory=gs://bucket-name/phs/*/spark-job-history
                          

      2. Submit a batch workload, specifying your running Persistent History Server. 
             
             gcloud dataproc batches submit spark \
                 --region=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
                 --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
                 --class=org.apache.spark.examples.SparkPi \
                 --history-server-cluster=projects/project-id/regions/region/clusters/PHS-cluster-name \
                 -- 1000
                           

    * [**Runtime version**](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions#how_to_choose_a_runtime_version): Use the [`--version`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark#--version) flag to specify the Managed Service for Apache Spark runtime version for the workload. 
          
          gcloud dataproc batches submit spark \
              --region=[REGION](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
              --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
              --class=org.apache.spark.examples.SparkPi \
              --version=VERSION
              -- 1000
                      




### API

This section shows how to create a batch workload to compute the approximate value of `pi` using the Managed Service for Apache Spark [`batches.create``](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/create)

Before using any of the request data, make the following replacements: 

  * project-id: A Google Cloud project ID.
  * region: A Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where Managed Service for Apache Spark will run the workload.

**Notes:**

    * PROJECT_ID: Your Google Cloud project ID. Project IDs are listed in the **Project info** section on the Google Cloud console [Dashboard](https://console.cloud.google.com/home/dashboard).
    * REGION: The session region.



HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches

Request JSON body: 
    
    
    {
      "sparkBatch":{
        "args":[
          "1000"
        ],
        "runtimeConfig": {
          "version": "2.3",
        },
        "jarFileUris":[
          "file:///usr/lib/spark/examples/jars/spark-examples.jar"
        ],
        "mainClass":"org.apache.spark.examples.SparkPi"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "name":"projects/project-id/locations/region/batches/batch-id",
      "uuid":",uuid",
      "createTime":"2021-07-22T17:03:46.393957Z",
      "sparkBatch":{
        "mainClass":"org.apache.spark.examples.SparkPi",
        "args":[
          "1000"
        ],
        "jarFileUris":[
          "file:///usr/lib/spark/examples/jars/spark-examples.jar"
        ]
      },
      "runtimeInfo":{
        "outputUri":"gs://dataproc-.../driveroutput"
      },
      "state":"SUCCEEDED",
      "stateTime":"2021-07-22T17:06:30.301789Z",
      "creator":"account-email-address",
      "runtimeConfig":{
        "version":"2.3",
        "properties":{
          "spark:spark.executor.instances":"2",
          "spark:spark.driver.cores":"2",
          "spark:spark.executor.cores":"2",
          "spark:spark.app.name":"projects/project-id/locations/region/batches/batch-id"
        }
      },
      "environmentConfig":{
        "peripheralsConfig":{
          "sparkHistoryServerConfig":{
          }
        }
      },
      "operation":"projects/project-id/regions/region/operation-id"
    }
    

**How the workload calculates Pi** : The Spark workload estimates a value of Pi using the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method). It generates `x,y` points on a coordinate plane that models a circle enclosed by a unit square. The input argument (`1000`) determines the number of x,y pairs to generate; the more pairs generated, the greater the accuracy of the estimation. For more information, see [Estimating Pi using the Monte Carlo Method](https://academo.org/demos/estimating-pi-monte-carlo/) and see [JavaSparkPi.java on GitHub](https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/JavaSparkPi.java).

## Estimate workload costs

Managed Service for Apache Spark workloads consume Data Compute Unit (DCU) and shuffle storage resources. For an example that outputs Managed Service for Apache Spark [UsageMetrics](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeInfo#UsageMetrics) to estimate workload resource consumption and costs, see [Managed Service for Apache Spark pricing](https://cloud.google.com/managed-spark/pricing).

## What's next

Learn about:

  * [Manage your data workload lifecycle in VS Code](https://docs.cloud.google.com/data-cloud-extension/vs-code/overview) using Google Cloud Data Agent Kit
  * [Build data pipelines with Data Agent Kit](https://docs.cloud.google.com/data-cloud-extension/vs-code/build-pipelines)
  * [Run PySpark code in BigQuery Studio notebooks](https://docs.cloud.google.com/bigquery/docs/use-spark)
  * [Managed Service for Apache Spark quotas](https://docs.cloud.google.com/managed-spark/quotas)
  * [Spark properties](https://docs.cloud.google.com/managed-spark/docs/concepts/properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
