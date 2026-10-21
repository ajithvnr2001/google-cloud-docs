---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/genomics-single-cell/
title: Run a genomics analysis in a JupyterLab notebook \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:26.104934+00:00
---

# Run a genomics analysis in a JupyterLab notebook  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/genomics-single-cell/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Run a genomics analysis in a JupyterLab notebook Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to run a single-cell genomics analysis using [Dask](https://dask.org/), [NVIDIA RAPIDS](https://rapids.ai/), and GPUs, which you can configure on [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc). You can configure Managed Service for Apache Spark to run Dask either with its standalone scheduler or with YARN for resource management.

This tutorial configures Managed Service for Apache Spark with a hosted [JupyterLab](https://jupyter.org/) instance to run a notebook featuring a single-cell genomics analysis. Using a Jupyter Notebook on Managed Service for Apache Spark lets you combine the interactive capabilities of Jupyter with the workload scaling that Managed Service for Apache Spark enables. With Managed Service for Apache Spark, you can scale out your workloads from one to many machines, which you can configure with as many GPUs as you need.

This tutorial is intended for data scientists and researchers. It assumes that you are experienced with Python and have basic knowledge of the following:

  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc)
  * [Dask](https://dask.org/)
  * [RAPIDS](https://rapids.ai/)
  * [Jupyter Notebooks](https://jupyter.org/)



## Objectives

  * Create a Managed Service for Apache Spark instance which is configured with GPUs, JupyterLab, and open source components.
  * Run a [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/rilango/batching/notebooks/1M_brain_gpu_analysis_uvm.ipynb) on Managed Service for Apache Spark.



## Costs

In this document, you use the following billable components of Google Cloud: 

* [Managed Service for Apache Spark](https://cloud.google.com/managed-spark/pricing)
* [Cloud Storage](https://cloud.google.com/storage/pricing)
* [GPUs](https://cloud.google.com/compute/gpus-pricing)

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc)




## Prepare your environment

  1. Select a [location](https://docs.cloud.google.com/storage/docs/locations) for your resources. 
         
         REGION=REGION
         

  2. Create a Cloud Storage bucket. 
         
         gcloud storage buckets create gs://BUCKET --location=REGION
         

  3. Copy the following [initialization actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) to your bucket. 
         
         SCRIPT_BUCKET=gs://goog-dataproc-initialization-actions-REGION
         gcloud storage cp ${SCRIPT_BUCKET}/gpu/install_gpu_driver.sh BUCKET/gpu/install_gpu_driver.sh
         gcloud storage cp ${SCRIPT_BUCKET}/dask/dask.sh BUCKET/dask/dask.sh
         gcloud storage cp ${SCRIPT_BUCKET}/rapids/rapids.sh BUCKET/rapids/rapids.sh
         gcloud storage cp ${SCRIPT_BUCKET}/python/pip-install.sh BUCKET/python/pip-install.sh
         




## Create a Managed Service for Apache Spark cluster with JupyterLab and open source components

  1. [Create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) a Managed Service for Apache Spark cluster.


    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region REGION \
        --image-version 2.0-ubuntu18 \
        --master-machine-type n1-standard-32 \
        --master-accelerator type=nvidia-tesla-t4,count=4 \
        --initialization-actions
    BUCKET/gpu/install_gpu_driver.sh,BUCKET/dask/dask.sh,BUCKET/rapids/rapids.sh,BUCKET/python/pip-install.sh
    \
        --initialization-action-timeout=60m \
        --metadata
    gpu-driver-provider=NVIDIA,dask-runtime=yarn,rapids-runtime=DASK,rapids-version=21.06,PIP_PACKAGES="scanpy==1.8.1,wget" \
        --optional-components JUPYTER \
        --enable-component-gateway \
        --single-node
    

The cluster has the following properties:

  * `--region`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where your cluster is located.
  * `--image-version`: `2.0-ubuntu18`, the [cluster image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#debian_images)
  * `--master-machine-type`: `n1-standard-32`, the main [machine type](https://docs.cloud.google.com/compute/docs/machine-types).
  * `--master-accelerator`: the type and count of [GPUs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/gpus) on the main node, four `nvidia-tesla-t4` GPUs.
  * `--initialization-actions`: the Cloud Storage paths to the installation scripts that install GPU drivers, Dask, RAPIDS, and extra dependencies.
  * `--initialization-action-timeout`: the timeout for the initialization actions.
  * `--metadata`: passed to the initialization actions to configure the cluster with NVIDIA GPU drivers, the standalone scheduler for Dask, and RAPIDS version `21.06`.
  * `--optional-components`: configures the cluster with the [Jupyter optional component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/jupyter).
  * `--enable-component-gateway`: allows access to web UIs on the cluster.
  * `--single-node`: configures the cluster as a single node (no workers).



## Access the Jupyter Notebook

  1. Open the **Clusters** page in the Managed Service for Apache Spark Google Cloud console.   
[Open Clusters page](https://console.cloud.google.com/dataproc/clusters)
  2. Click your cluster and click the **Web Interfaces** tab.
  3. Click **JupyterLab**.
  4. Open a [new terminal](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html) in JupyterLab.
  5. Clone the `clara-parabricks/rapids-single-cell-examples` [repository](https://github.com/clara-parabricks/rapids-single-cell-examples) and check out the `managed-spark/multi-gpu` branch. 
         
         git clone https://github.com/clara-parabricks/rapids-single-cell-examples.git
         git checkout managed-spark/multi-gpu
         

  6. In JupyterLab, navigate to the [rapids-single-cell-examples/notebooks](https://github.com/clara-parabricks/rapids-single-cell-examples) repository and open the [1M_brain_gpu_analysis_uvm.ipynb](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/rilango/batching/notebooks/1M_brain_gpu_analysis_uvm.ipynb) Jupyter Notebook.

  7. To clear all the outputs in the notebook, select **Edit > Clear All Outputs**

  8. Read the instructions in the cells of the notebook. The notebook uses Dask and RAPIDS on Managed Service for Apache Spark to guide you through a single-cell RNA-seq workflow on 1 million cells, including processing and visualizing the data. To learn more, see [Accelerating Single Cell Genomic Analysis using RAPIDS](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

  1. [Delete your Managed Service for Apache Spark cluster.](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#deleting_a_cluster)
         
         gcloud dataproc clusters delete cluster-name \
             --region=region
         

  2. Delete the bucket: 
         
         gcloud storage buckets delete BUCKET_NAME

**Important:** Your bucket must be empty before you can delete it.



## What's next

  * Discover more about [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc).
  * Explore reference architectures, diagrams, tutorials, and best practices. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
