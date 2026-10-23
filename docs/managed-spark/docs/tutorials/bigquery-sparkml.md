---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-sparkml/
title: Use Apache Spark ML for machine learning \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:29.734373+00:00
---

# Use Apache Spark ML for machine learning  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-sparkml/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use Apache Spark ML for machine learning Stay organized with collections  Save and categorize content based on your preferences. 

The [BigQuery Connector for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/bigquery#available_connectors) allows Data Scientists to blend the power of the seamlessly scalable SQL engine with [Apache Spark Machine Learning](https://spark.apache.org/docs/2.0.0/ml-guide.html) capabilities. In this tutorial, we show how to use Managed Service for Apache Spark, BigQuery and Apache Spark ML to perform machine learning on a [dataset](http://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes). 

## Objectives

Use linear regression to build a model of birth weight as a function of five factors: 

  * gestation weeks
  * mother's age
  * father's age
  * mother's weight gain during pregnancy
  * [Apgar score](https://en.wikipedia.org/wiki/Apgar_score)



Use the following tools:

  * BigQuery, to prepare the linear regression input table, which is written to your Google Cloud project
  * Python, to query and manage data in BigQuery
  * Apache Spark, to access the resulting linear regression table
  * Spark ML, to build and evaluate the model
  * Managed Service for Apache Spark PySpark job, to invoke Spark ML functions



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine
  * Managed Service for Apache Spark
  * BigQuery



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

A Managed Service for Apache Spark cluster has the Spark components, including Spark ML, installed. To set up a Managed Service for Apache Spark cluster and run the code in this example, you will need to do (or have done) the following:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Dataproc, BigQuery, Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,bigquery.googleapis.com,compute_component)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. Enable the Dataproc, BigQuery, Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,bigquery.googleapis.com,compute_component)

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Create a [Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster) in your project. Your cluster should be running a [Managed Service for Apache Spark version](https://docs.cloud.google.com/managed-spark/docs/concepts/dataproc-versions) with Spark 2.0 or higher, (includes machine learning libraries).



## Create a subset of BigQuery natality data

In this section, you create a dataset in your project, then create a table in the dataset to which you copy a subset of birth rate data from the publicly available [natality](https://docs.cloud.google.com/bigquery/sample-tables) BigQuery dataset. Later in this tutorial you will use the subset data in this table to predict birth weight as a function of maternal age, paternal age, and gestation weeks.

You can create the data subset using the Google Cloud console or running a Python script on your local machine.

### Console

  1. Create a dataset in your project.

     1. [Go to the BigQuery Web UI](https://console.cloud.google.com/bigquery).
     2. In the left navigation panel, click your project name, then click **CREATE DATASET**.
     3. In the **Create dataset** dialog: 
        1. For **Dataset ID** , enter "natality_regression".
        2. For **Data location** , you can choose a [location](https://docs.cloud.google.com/bigquery/docs/dataset-locations) for the dataset. The default value location is `US multi-region`. After a dataset is created, the location cannot be changed.
        3. For **Default table expiration** , choose one of the following options: 
           * **Never** (default): You must delete the table manually.
           * **Number of days** : The table will be deleted after the specified number days from its creation time.
        4. For **Encryption** , choose one of the following options: 
           * **Google-owned and Google-managed encryption key** (default).
           * **Customer-managed key** : See [Protecting data with Cloud KMS keys](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).
        5. Click **Create dataset**. You cannot add a description or a label when you create a dataset using the Web UI. After the dataset is created, you can [add a description](https://docs.cloud.google.com/bigquery/docs/managing-datasets#update-dataset-description), and [add a label](https://docs.cloud.google.com/bigquery/docs/labels#creating_and_updating_dataset_labels).
  2. Run a query against the public natality dataset, then save the query results in a new table in your dataset.

     1. Copy and paste the following query into the Query Editor, then click Run. 
            
            CREATE OR REPLACE TABLE natality_regression.regression_input as
            SELECT
            weight_pounds,
            mother_age,
            father_age,
            gestation_weeks,
            weight_gain_pounds,
            apgar_5min
            FROM
            `bigquery-public-data.samples.natality`
            WHERE
            weight_pounds IS NOT NULL
            AND mother_age IS NOT NULL
            AND father_age IS NOT NULL
            AND gestation_weeks IS NOT NULL
            AND weight_gain_pounds IS NOT NULL
            AND apgar_5min IS NOT NULL
            

     2. After the query completes (in approximately one minute), the results are saved as "regression_input" BigQuery table in the `natality_regression` dataset in your project. ![](https://docs.cloud.google.com/static/managed-spark/images/natality-regression-table.png)



### Python

Before trying this sample, follow the Python setup instructions in the [Managed Service for Apache Spark quickstart using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries). For more information, see the [Managed Service for Apache Spark Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataproc/latest). 

To authenticate to Managed Service for Apache Spark, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

  1. See [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup) for instructions on installing Python and the Google Cloud Client Library for Python (needed to run the code). Installing and using a Python `virtualenv` is recommended.

  2. Copy and paste the `natality_tutorial.py` code, below, into a `python` shell on your local machine. Press the `<return>` key in the shell to run the code to create a "natality_regression" BigQuery dataset in your default Google Cloud project with a "regression_input" table that is populated with a subset of the public `natality` data.

**Setting up to run the application code locally:**
     * Run `gcloud config list project` to see the name of your default project.
     * Run `gcloud config set project project-name` to change the default project.
     * Run `gcloud auth application-default login` to set application credentials to your user account. 
    
    """Create a Google BigQuery linear regression input table.
    
    In the code below, the following actions are taken:
    * A new dataset is created "natality_regression."
    * A query is run against the public dataset,
        bigquery-public-data.samples.natality, selecting only the data of
        interest to the regression, the output of which is stored in a new
        "regression_input" table.
    * The output table is moved over the wire to the user's default project via
        the built-in BigQuery Connector for Spark that bridges BigQuery and
        Cloud Dataproc.
    """
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Create a new Google BigQuery client using Google Cloud Platform project
    # defaults.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # Prepare a reference to a new dataset for storing the query results.
    dataset_id = "natality_regression"
    dataset_id_full = f"{client.project}.{dataset_id}"
    
    dataset = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html)(dataset_id_full)
    
    # Create the new BigQuery dataset.
    dataset = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)(dataset)
    
    # Configure the query job.
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)()
    
    # Set the destination table to where you want to store query results.
    # As of google-cloud-bigquery 1.11.0, a fully qualified table ID can be
    # used in place of a TableReference.
    job_config.destination = f"{dataset_id_full}.regression_input"
    
    # Set up a query in Standard SQL, which is the default for the BigQuery
    # Python client library.
    # The query selects the fields of interest.
    query = """
        SELECT
            weight_pounds, mother_age, father_age, gestation_weeks,
            weight_gain_pounds, apgar_5min
        FROM
            `bigquery-public-data.samples.natality`
        WHERE
            weight_pounds IS NOT NULL
            AND mother_age IS NOT NULL
            AND father_age IS NOT NULL
            AND gestation_weeks IS NOT NULL
            AND weight_gain_pounds IS NOT NULL
            AND apgar_5min IS NOT NULL
    """
    
    # Run the query.
    client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(query, job_config=job_config)  # Waits for the query to finish

  3. Confirm the creation of the `natality_regression` dataset and the `regression_input` table. ![](https://docs.cloud.google.com/static/managed-spark/images/natality-regression-table.png)




## Run a linear regression

In this section, you'll run a PySpark linear regression by submitting the job to Managed Service for Apache Spark using the Google Cloud console or by running the `gcloud` command from a local terminal.

### Console

  1. Copy and paste the following code into a new `natality_sparkml.py` file on your local machine. 
         
         """Run a linear regression using Apache Spark ML.
         
         In the following PySpark (Spark Python API) code, we take the following actions:
         
           * Load a previously created linear regression (BigQuery) input table
             into our Cloud Dataproc Spark cluster as an RDD (Resilient
             Distributed Dataset)
           * Transform the RDD into a Spark Dataframe
           * Vectorize the features on which the model will be trained
           * Compute a linear regression using Spark ML
         
         """
         from pyspark.context import SparkContext
         from pyspark.ml.linalg import Vectors
         from pyspark.ml.regression import LinearRegression
         from pyspark.sql.session import SparkSession
         # The imports, above, allow us to access SparkML features specific to linear
         # regression as well as the Vectors types.
         
         
         # Define a function that collects the features of interest
         # (mother_age, father_age, and gestation_weeks) into a vector.
         # Package the vector in a tuple containing the label (`weight_pounds`) for that
         # row.
         def vector_from_inputs(r):
           return (r["weight_pounds"], Vectors.dense(float(r["mother_age"]),
                                                     float(r["father_age"]),
                                                     float(r["gestation_weeks"]),
                                                     float(r["weight_gain_pounds"]),
                                                     float(r["apgar_5min"])))
         
         sc = SparkContext()
         spark = SparkSession(sc)
         
         # Read the data from BigQuery as a Spark Dataframe.
         natality_data = spark.read.format("bigquery").option(
             "table", "natality_regression.regression_input").load()
         # Create a view so that Spark SQL queries can be run against the data.
         natality_data.createOrReplaceTempView("natality")
         
         # As a precaution, run a query in Spark SQL to ensure no NULL values exist.
         sql_query = """
         SELECT *
         from natality
         where weight_pounds is not null
         and mother_age is not null
         and father_age is not null
         and gestation_weeks is not null
         """
         clean_data = spark.sql(sql_query)
         
         # Create an input DataFrame for Spark ML using the above function.
         training_data = clean_data.rdd.map(vector_from_inputs).toDF(["label",
                                                                      "features"])
         training_data.cache()
         
         # Construct a new LinearRegression object and fit the training data.
         lr = LinearRegression(maxIter=5, regParam=0.2, solver="normal")
         model = lr.fit(training_data)
         # Print the model summary.
         print("Coefficients:" + str(model.coefficients))
         print("Intercept:" + str(model.intercept))
         print("R^2:" + str(model.summary.r2))
         model.summary.residuals.show()

  2. Copy the local `natality_sparkml.py` file to a Cloud Storage bucket in your project. 
         
         gcloud storage cp natality_sparkml.py gs://bucket-name
         

Instead of copying the file to a user bucket in your project, you can copy it to the [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) that Managed Service for Apache Spark created when you created your cluster.
  3. Run the regression from the Managed Service for Apache Spark [Submit a job](https://console.cloud.google.com/dataproc/jobs/jobsSubmit) page.

     1. In the **Main python file** field, insert the `gs://` URI of the Cloud Storage bucket where your copy of the `natality_sparkml.py` file is located.

     2. Select `PySpark` as the **Job type**.

     3. Insert `gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar` in the **Jar files** field. This makes the spark-bigquery-connector available to the PySpark application at runtime to allow it to read BigQuery data into a Spark DataFrame.  The 2.12 jar is compatible with Dataproc clusters created with the 1.5 or later image. If your Dataproc cluster was created with the 1.3 or 1.4 image, specify the 2.11 jar instead (`gs://spark-lib/bigquery/spark-bigquery-latest_2.11.jar`). 

     4. Fill in the **Job ID** , **Region** , and **Cluster** fields.

     5. Click **Submit** to run the job on your cluster.




When the job completes, the linear regression output model summary appears in the Managed Service for Apache Spark Job details window. **Model Summary Terminology:**

  * **R^2:** a measure for how much of the "signal" the model captures.
  * **Residuals:** the difference between the prediction of the model and the actual value for each point that was used to fit the model. 

![](https://docs.cloud.google.com/static/managed-spark/images/regression-console-output.png)

### gcloud

  1. Copy and paste the following code into a new `natality_sparkml.py` file on your local machine. 
         
         """Run a linear regression using Apache Spark ML.
         
         In the following PySpark (Spark Python API) code, we take the following actions:
         
           * Load a previously created linear regression (BigQuery) input table
             into our Cloud Dataproc Spark cluster as an RDD (Resilient
             Distributed Dataset)
           * Transform the RDD into a Spark Dataframe
           * Vectorize the features on which the model will be trained
           * Compute a linear regression using Spark ML
         
         """
         from pyspark.context import SparkContext
         from pyspark.ml.linalg import Vectors
         from pyspark.ml.regression import LinearRegression
         from pyspark.sql.session import SparkSession
         # The imports, above, allow us to access SparkML features specific to linear
         # regression as well as the Vectors types.
         
         
         # Define a function that collects the features of interest
         # (mother_age, father_age, and gestation_weeks) into a vector.
         # Package the vector in a tuple containing the label (`weight_pounds`) for that
         # row.
         def vector_from_inputs(r):
           return (r["weight_pounds"], Vectors.dense(float(r["mother_age"]),
                                                     float(r["father_age"]),
                                                     float(r["gestation_weeks"]),
                                                     float(r["weight_gain_pounds"]),
                                                     float(r["apgar_5min"])))
         
         sc = SparkContext()
         spark = SparkSession(sc)
         
         # Read the data from BigQuery as a Spark Dataframe.
         natality_data = spark.read.format("bigquery").option(
             "table", "natality_regression.regression_input").load()
         # Create a view so that Spark SQL queries can be run against the data.
         natality_data.createOrReplaceTempView("natality")
         
         # As a precaution, run a query in Spark SQL to ensure no NULL values exist.
         sql_query = """
         SELECT *
         from natality
         where weight_pounds is not null
         and mother_age is not null
         and father_age is not null
         and gestation_weeks is not null
         """
         clean_data = spark.sql(sql_query)
         
         # Create an input DataFrame for Spark ML using the above function.
         training_data = clean_data.rdd.map(vector_from_inputs).toDF(["label",
                                                                      "features"])
         training_data.cache()
         
         # Construct a new LinearRegression object and fit the training data.
         lr = LinearRegression(maxIter=5, regParam=0.2, solver="normal")
         model = lr.fit(training_data)
         # Print the model summary.
         print("Coefficients:" + str(model.coefficients))
         print("Intercept:" + str(model.intercept))
         print("R^2:" + str(model.summary.r2))
         model.summary.residuals.show()

  2. Copy the local `natality_sparkml.py` file to a Cloud Storage bucket in your project. 
         
         gcloud storage cp natality_sparkml.py gs://bucket-name
         

Instead of copying the file to a user bucket in your project, you can copy it to the [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) that Managed Service for Apache Spark created when you created your cluster.
  3. Submit the Pyspark job to Managed Service for Apache Spark by running the `gcloud` command, shown below, from a terminal window on your local machine.

     1. The **\--jars** flag value makes the spark-bigquery-connector available to the PySpark jobv at runtime to allow it to read BigQuery data into a Spark DataFrame. 
            
            gcloud dataproc jobs submit pyspark \
                gs://your-bucket/natality_sparkml.py \
                --cluster=cluster-name \
                --region=region \
                --jars=gs://spark-lib/bigquery/spark-bigquery-with-dependencies_SCALA_VERSION-CONNECTOR_VERSION.jar
            

The 2.12 jar is compatible with Dataproc clusters created with the 1.5 or later image. If your Dataproc cluster was created with the 1.3 or 1.4 image, specify the 2.11 jar instead. See [Make the connector available to your application](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example#make_the_connector_available_to_your_application) for more information. 



The linear regression output (model summary) appears in the terminal window when the job completes. **Model Summary Terminology:**

  * **R^2:** a measure for how much of the "signal" the model captures.
  * **Residuals:** the difference between the prediction of the model and the actual value for each point that was used to fit the model.


    
    
    <<< # Print the model summary.
    ... print "Coefficients:" + str(model.coefficients)
    Coefficients:[0.0166657454602,-0.00296751984046,0.235714392936,0.00213002070133,-0.00048577251587]
    <<< print "Intercept:" + str(model.intercept)
    Intercept:-2.26130330748
    <<< print "R^2:" + str(model.summary.r2)
    R^2:0.295200579035
    <<< model.summary.residuals.show()
    +--------------------+
    |           residuals|
    +--------------------+
    | -0.7234737533344147|
    |  -0.985466980630501|
    | -0.6669710598385468|
    |  1.4162434829714794|
    |-0.09373154375186754|
    |-0.15461747949235072|
    | 0.32659061654192545|
    |  1.5053877697929803|
    |  -0.640142797263989|
    |   1.229530260294963|
    |-0.03776160295256...|
    | -0.5160734239126814|
    | -1.5165972740062887|
    |  1.3269085258245008|
    |  1.7604670124710626|
    |  1.2348130901905972|
    |   2.318660276655887|
    |  1.0936947030883175|
    |  1.0169768511417363|
    | -1.7744915698181583|
    +--------------------+
    only showing top 20 rows.
    
      
    

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



### Delete the Managed Service for Apache Spark cluster

See [Delete a cluster](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#delete_a_cluster).

## What's next

  * See [Spark job tuning tips](https://docs.cloud.google.com/managed-spark/docs/support/spark-job-tuning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
