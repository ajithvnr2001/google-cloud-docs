---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/jupyter/
title: Managed Service for Apache Spark optional Jupyter component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:24.963121+00:00
---

# Managed Service for Apache Spark optional Jupyter component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/jupyter/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Jupyter component Stay organized with collections  Save and categorize content based on your preferences. 

You can install additional components like Jupyter when you create a Managed Service for Apache Spark cluster using the [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) feature. This page describes the Jupyter component.

The [Jupyter](http://jupyter.org/) component is a Web-based **single-user** notebook for interactive data analytics and supports the [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) Web UI. The Jupyter Web UI is available on port `8123` on the cluster's first master node.

**Launch notebooks for multiple users.** You can create a Managed Service for Apache Spark-enabled [Vertex AI Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create-dataproc-enabled) or [install the Managed Service for Apache Spark JupyterLab plugin](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions) on a VM to serve notebooks to multiple users.

**Configure Jupyter.** Jupyter can be configured by providing `dataproc:jupyter` [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties). To reduce the risk of remote code execution over unsecured notebook server APIs, the default `dataproc:jupyter.listen.all.interfaces` cluster property setting is `false`, which restricts connections to `localhost (127.0.0.1)` when the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) is enabled (Component Gateway activation is required when installing the Jupyter component).

The Jupyter notebook provides a Python kernel to run [Spark](https://spark.apache.org/) code, and a PySpark kernel. By default, notebooks are [saved in Cloud Storage](https://github.com/src-d/jgscm) in the Managed Service for Apache Spark staging bucket, which is specified by the user or [auto-created](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#auto-created_staging_bucket) when the cluster is created. The location can be changed at cluster creation time using the [`dataproc:jupyter.notebook.gcs.dir`](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc-properties) cluster property.

**Work with data files.** You can use a Jupyter notebook to work with data files that have been [uploaded to Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects). Since the [Cloud Storage connector](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage) is pre-installed on a Managed Service for Apache Spark cluster, you can reference the files directly in your notebook. Here's an example that accesses CSV files in Cloud Storage:
    
    
    df = spark.read.csv("gs://bucket/path/file.csv")
    df.show()
    

See [Generic Load and Save Functions](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html) for PySpark examples.

## Install Jupyter

Install the component when you create a Managed Service for Apache Spark cluster. The Jupyter component requires activation of the Managed Service for Apache Spark [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways).

**Note:** Only when using [image version 1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#unsupported-dataproc-image-versions), installation of the Jupyter component also requires installation of the [Anaconda](https://docs.cloud.google.com/managed-spark/docs/concepts/components/anaconda) component.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Jupyter Notebook** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Jupyter component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.

**Latest default image version example**

The following example installs the Jupyter component on a cluster that uses the latest default image version.
    
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=JUPYTER \
        --region=region \
        --enable-component-gateway \
        ... other flags
    

### REST API

The Jupyter component can be installed through the Dataproc API using [`SoftwareConfig.Component`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

  * Set the [EndpointConfig.enableHttpPortAccess](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#endpointconfig) property to `true` as part of the `clusters.create` request to enable connecting to the Jupyter notebook Web UI using the [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways).



## Open the Jupyter and JupyterLab UIs

Click the [Google Cloud console Component Gateway links](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways#viewing_and_accessing_component_gateway_urls) to open in your local browser the Jupyter notebook or JupyterLab UI running on the cluster master node.

**Select "GCS" or "Local Disk" to create a new Jupyter Notebook in either location.**

## Attach GPUs to master and worker nodes

You can [add GPUs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/gpus) to your cluster's master and worker nodes when using a Jupyter notebook to:

  1. Preprocess data in Spark, then collect a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) onto the master and run [TensorFlow](https://www.tensorflow.org/)
  2. Use Spark to orchestrate TensorFlow runs in parallel
  3. Run [Tensorflow-on-YARN](https://github.com/criteo/tf-yarn)
  4. Use with other machine learning scenarios that use GPUs



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
