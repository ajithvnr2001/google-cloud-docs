---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-offerings/
title: Dataproc Container for Spark \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:31.982521+00:00
---

# Dataproc Container for Spark  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-offerings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Dataproc Container for Spark Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides a Dataproc Container for Spark. That is an Apache Spark environment for data processing. For more information about Apache Spark, see `https://spark.apache.org/`. Use containers of Dataproc Container for Spark to run new or existing Spark applications within a Distributed Cloud Kubernetes cluster with minimal alteration. If you are familiar with Spark tools, you can keep using them.

Define your Spark application in a YAML file, and Distributed Cloud allocates the resources for you. The Dataproc Container for Spark container starts in seconds. Spark executors scale up or shut down according to your needs.

Configure containers from Dataproc Container for Spark on Distributed Cloud to use specialized hardware, such as specialty hardware nodes or GPUs.

This document is for audiences within the application operator group who manage Apache Spark applications using the Dataproc Container for Spark service within GDC projects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before running Spark applications using Dataproc Container for Spark, you must make sure the service is available, request the necessary permissions, prepare your environment, and create a service account.

### Deploy the Dataproc Container for Spark service

The Platform Administrator (PA) must install Marketplace services for you before you can use the services. Contact your PA if you need Dataproc Container for Spark. See [Install a GDC Marketplace software package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-lifecycle#install-sw) for more information.

### Request IAM roles

Contact your Organization IAM Admin or Project IAM Admin to request the following roles based on the tasks you need to perform:

  * **Namespace Admin** (`namespace-admin`): create, update, and delete project resources within your project's namespace in the user cluster.
  * **Project Viewer** (`project-viewer`): view an existing project and its resources.



The Organization IAM Admin can grant these roles for any project within the organization. The Project IAM Admin can grant these roles within the scope of their specific project.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




### Configure service account for the Dataproc Container for Spark service

You must have a service account in user clusters to use the Dataproc Container for Spark service. The Dataproc Container for Spark creates a Spark driver pod to run a Spark application. A Spark driver pod needs a Kubernetes service account in the namespace of the pod with permissions to do the following actions:

  * Create, get, list, and delete executor pods.
  * Create a Kubernetes headless service for the driver.



Before running a Spark application, complete the following steps to ensure you have a service account with the previous permissions in the `foo` namespace:

  1. Create a service account for a Spark driver pod to use in the `foo` namespace:
         
         kubectl create serviceaccount spark --kubeconfig AO_USER_KUBECONFIG --namespace=foo
         

**Note:** The `foo` namespace corresponds to the Project `foo` namespace.
  2. Create a role for granting permissions to create, get, list, and delete executor pods, and create a Kubernetes headless service for the driver in the `foo` namespace:
         
         kubectl create role spark-driver --kubeconfig AO_USER_KUBECONFIG --verb=* \
         --resource=pods,services,configmaps,persistentvolumeclaims \
         --namespace=foo
         

  3. Create a role binding for granting the service account role access in the `foo` namespace:
         
         kubectl create --kubeconfig AO_USER_KUBECONFIG \
         rolebinding spark-spark-driver \
         --role=spark-driver --serviceaccount=foo:spark \
         --namespace=foo
         


**Caution:** Later, when creating `SparkApplication` and `ScheduledSparkApplication` custom resources in the `foo` namespace, specify the service account in the `.spec.driver.serviceAccount` field of the YAML file. For a sample YAML file of the `SparkApplication` specification, see Write a Spark application specification.

## Run sample Spark 3 applications

Containerizing Spark applications simplifies running big data applications on your premises using Distributed Cloud. As an Application Operator (AO), run Spark applications specified in GKE objects of the `SparkApplication` custom resource type.

To run and use an Apache Spark 3 application on Distributed Cloud, complete the following steps:

  1. Examine the `spark-operator` image in your project to find the `$DATAPROC_IMAGE` to reference in your Spark application:
         
         export DATAPROC_IMAGE=$(kubectl get pod --kubeconfig AO_USER_KUBECONFIG \
         --selector app.kubernetes.io/name=spark-operator -n foo \
         -o=jsonpath='{.items[*].spec.containers[0].image}' \
         | sed 's/spark-operator/dataproc/')
         

For example:
         
         export DATAPROC_IMAGE=10.200.8.2:10443/dataproc-service/private-cloud-devel/dataproc:3.1-dataproc-17
         

  2. Write a `SparkApplication` specification and store it in a YAML file. For more information, see the Write a Spark application specification section.

  3. Submit, run, and monitor your Spark application as configured in a `SparkApplication` specification on the GKE cluster with the `kubectl` command. For more information, see the Application examples section.

  4. Review the status of the application.

  5. Optional: Review the application logs. For more information, see the View the logs of a Spark 3 application section.

  6. Use the Spark application to collect and surface the status of the driver and executors to the user.




## Write a Spark application specification

A `SparkApplication` specification includes the following components:

  * The `apiVersion` field.
  * The `kind` field.
  * The `metadata` field.
  * The `spec` section.



For more information, see the _Writing a SparkApplication Spec_ on GitHub: <https://github.com/kubeflow/spark-operator/blob/gh-pages/docs/user-guide.md#writing-a-sparkapplication-spec>

## Application examples

This section includes the following examples with their corresponding `SparkApplication` specifications to run Spark applications:

  * Spark Pi
  * Spark SQL
  * Spark MLlib
  * SparkR



### Spark Pi

This section contains an example to run a compute-intensive Spark Pi application that estimates _𝛑_ (pi) by throwing darts in a circle.

Work through the following steps to run Spark Pi:

  1. Apply the following `SparkApplication` specification example in the user cluster:
         
         apiVersion: "sparkoperator.k8s.io/v1beta2"
         kind: SparkApplication
         metadata:
           name: spark-pi
           namespace: foo
         spec:
           type: Python
           pythonVersion: "3"
           mode: cluster
           image: "${DATAPROC_IMAGE?}"
           imagePullPolicy: IfNotPresent
           mainApplicationFile: "local:///usr/lib/spark/examples/src/main/python/pi.py"
           sparkVersion: "3.1.3"
           restartPolicy:
             type: Never
           driver:
             cores: 1
             coreLimit: "1000m"
             memory: "512m"
             serviceAccount: spark
           executor:
             cores: 1
             instances: 1
             memory: "512m"
         

  2. Verify that the `SparkApplication` specification example runs and completes in 1-2 minutes using the following command:
         
         kubectl --kubeconfig AO_USER_KUBECONFIG get SparkApplication spark-pi -n foo
         

  3. View the Driver Logs to see the result:
         
         kubectl --kubeconfig AO_USER_KUBECONFIG logs spark-pi-driver -n foo | grep "Pi is roughly"
         

An output is similar to the following:
         
         Pi is roughly 3.1407357036785184
         




For more information, see the following resources:

  * For the application code, see the article _Pi estimation_ from the Apache Spark documentation: `https://spark.apache.org/examples.html`.
  * For a sample Spark Pi YAML file, see Write a Spark application specification.



### Spark SQL

Work through the following steps to run Spark SQL:

  1. To run a Spark SQL application that selects the `1` value, use the following query:
         
         select 1;
         

  2. Apply the following `SparkApplication` specification example in the user cluster:
         
         apiVersion: "sparkoperator.k8s.io/v1beta2"
         kind: SparkApplication
         metadata:
           name: pyspark-sql-arrow
           namespace: foo
         spec:
           type: Python
           mode: cluster
           image: "${DATAPROC_IMAGE?}"
           imagePullPolicy: IfNotPresent
           mainApplicationFile: "local:///usr/lib/spark/examples/src/main/python/sql/arrow.py"
           sparkVersion: "3.1.3"
           restartPolicy:
             type: Never
           driver:
             cores: 1
             coreLimit: "1000m"
             memory: "512m"
             serviceAccount: spark
           executor:
             cores: 1
             instances: 1
             memory: "512m"
         

  3. Verify that the `SparkApplication` specification example runs and completes in less than one minute using the following command:
         
         kubectl --kubeconfig AO_USER_KUBECONFIG get SparkApplication pyspark-sql-arrow -n foo
         




### Spark MLlib

Work through the following steps to run Spark MLlib:

  1. Use the following Scala example to run a Spark MLlib instance that performs statistical analysis and prints a result to the console:
         
         import org.apache.spark.ml.linalg.{Matrix, Vectors}
         import org.apache.spark.ml.stat.Correlation
         import org.apache.spark.sql.Row
         
         val data = Seq(
           Vectors.sparse(4, Seq((0, 1.0), (3, -2.0))),
           Vectors.dense(4.0, 5.0, 0.0, 3.0),
           Vectors.dense(6.0, 7.0, 0.0, 8.0),
           Vectors.sparse(4, Seq((0, 9.0), (3, 1.0)))
         )
         
         val df = data.map(Tuple1.apply).toDF("features")
         val Row(coeff1: Matrix) = Correlation.corr(df, "features").head
         println(s"Pearson correlation matrix:\n $coeff1")
         
         val Row(coeff2: Matrix) = Correlation.corr(df, "features", "spearman").head
         println(s"Spearman correlation matrix:\n $coeff2")
         

  2. Apply the following `SparkApplication` specification example in the user cluster:
         
         apiVersion: "sparkoperator.k8s.io/v1beta2"
         kind: SparkApplication
         metadata:
           name: spark-ml
           namespace: foo
         spec:
           type: Scala
           mode: cluster
           image: "${DATAPROC_IMAGE?}"
           imagePullPolicy: IfNotPresent
           mainClass: org.apache.spark.examples.ml.SummarizerExample
           mainApplicationFile: "local:///usr/lib/spark/examples/jars/spark-examples_2.12-3.1.3.jar"
           sparkVersion: "3.1.3"
           restartPolicy:
             type: Never
           driver:
             cores: 1
             coreLimit: "1000m"
             memory: "512m"
             serviceAccount: spark
           executor:
             cores: 1
             instances: 1
             memory: "512m"
         

  3. Verify that the `SparkApplication` specification example runs and completes in less than one minute using the following command:
         
         kubectl --kubeconfig AO_USER_KUBECONFIG get SparkApplication spark-ml -n foo
         




### SparkR

Work through the following steps to run SparkR:

  1. Use the following example code to run a SparkR instance that loads a bundled dataset and prints the first line:
         
         library(SparkR)
         sparkR.session()
         df <- as.DataFrame(faithful)
         head(df)
         

  2. Apply the following `SparkApplication` specification example in the user cluster:
         
         apiVersion: "sparkoperator.k8s.io/v1beta2"
         kind: SparkApplication
         metadata:
           name: spark-r-dataframe
           namespace: foo
         spec:
           type: R
           mode: cluster
           image: "${DATAPROC_IMAGE?}"
           imagePullPolicy: Always
           mainApplicationFile: "local:///usr/lib/spark/examples/src/main/r/dataframe.R"
           sparkVersion: "3.1.3"
           restartPolicy:
             type: Never
           driver:
             cores: 1
             coreLimit: "1000m"
             memory: "512m"
             serviceAccount: spark
           executor:
             cores: 1
             instances: 1
             memory: "512m"
         

  3. Verify that the `SparkApplication` specification example runs and completes in less than one minute using the following command:
         
         kubectl --kubeconfig AO_USER_KUBECONFIG get SparkApplication spark-r-dataframe -n foo
         




## View the logs of a Spark 3 application

Spark has the following two log types that you can visualize:

  * Driver logs
  * Event logs



Use the terminal to run commands.

### Driver logs

Work through the following steps to view the driver logs of your Spark application:

  1. Find your Spark driver pod:
         
         kubectl -n spark get pods
         

  2. Open the logs from the Spark driver pod:
         
         kubectl -n spark logs DRIVER_POD
         

Replace `DRIVER_POD` with the name of the Spark driver pod that you found in the previous step.




### Event logs

You can find event logs at the path specified in the YAML file of the `SparkApplication` specification.

Work through the following steps to view the event logs of your Spark application:

  1. Open the YAML file of the `SparkApplication` specification.
  2. Locate the `spec` field in the file.
  3. Locate the `sparkConf` field nested in the `spec` field.
  4. Locate the value of the `spark.eventLog.dir` field nested in the `sparkConf` section.
  5. Open the path to view event logs.



For a sample YAML file of the `SparkApplication` specification, see Write a Spark application specification.

Contact your account manager for more information. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
