---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage/
title: Track the lineage of pipeline artifacts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:24.233703+00:00
---

# Track the lineage of pipeline artifacts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Track the lineage of pipeline artifacts Stay organized with collections  Save and categorize content based on your preferences. 

Each pipeline run created using Agent Platform Pipelines has several associated artifacts and parameters, such as models, datasets, pipeline templates, and components. The lineage of a pipeline artifact includes the factors that contributed to its creation, as well as artifacts and metadata derived from the artifact. For example, a model's lineage can include the following:

  * The training, test, and evaluation data used to create the model.

  * The hyperparameters used during model training.

  * Metadata recorded from the training and evaluation process, such as the model's accuracy.

  * Artifacts that descend from this model, such as the results of batch predictions.




You can use this metadata to help answer questions like the following:

  * Why did a certain pipeline run produce an especially accurate model?

  * Which pipeline run produced the most accurate model, and what hyperparameters were used to train the model?

  * Depending on the steps in your pipeline, you might be able to answer system governance questions. For example, you could use metadata to determine which version of your model was in production at a given point in time.




To view and analyze the pipeline artifact lineage, you can use either Vertex ML Metadata or Knowledge Catalog.

The following table outlines the differences between Vertex ML Metadata and Knowledge Catalog:

Feature | Vertex ML Metadata | Knowledge Catalog  
---|---|---  
Types of pipeline metadata captured | All input and output artifacts produced by a pipeline run. | Input and output artifacts that can be mapped to fully qualified names (FQNs) supported by Knowledge Catalog, generally by using Google Cloud Pipeline Components.  
Geography | Single region reads. | Global reads, that is, across multiple regions.  
Projects | Single project reads. | Organization-wide reads across multiple projects.  
Integrated services | Integrated with Agent Platform Pipelines, Gemini Enterprise Agent Platform Experiments, Gemini Enterprise Agent Platform Model Registry, and Datasets. | Integrated with multiple Google Cloud products, such as Gemini Enterprise Agent Platform, BigQuery, Managed Service for Apache Airflow, and Managed Service for Apache Spark.  
Opt-in? | No, always on. | Opt-in per project by enabling the Data Lineage API.  
  
## Map Vertex ML Metadata artifacts to Knowledge Catalog

To map Vertex ML Metadata artifacts to FQNs in Knowledge Catalog, you need to do the following:

  * Use Google Cloud Pipeline Components while creating Agent Platform models and managed datasets.

  * Use custom schema titles (`google.VertexDataset` or `google.VertexModel`) while specifying the model or managed dataset resource name in the `metadata` field, as illustrated in the following sample:



    
    
    {
      "name": "projects/example-project/locations/us-central1/metadataStores/default/artifacts/example-artifact",
      "displayName": "My dataset",
      "uri": "https://us-central1-aiplatform.googleapis.com/v1/projects/example-project/locations/us-central1/datasets/example-dataset",
       ...
      "schemaTitle": "google.VertexDataset",
      "schemaVersion": "0.0.1",
      "metadata": {
        "resourceName": "projects/example-project/locations/us-central1/datasets/example-dataset"
      }
    }
    

## Analyze the lineage of pipeline artifacts using Vertex ML Metadata

When you run a pipeline using Agent Platform Pipelines, the artifacts and parameters of your pipeline run are stored using Vertex ML Metadata. Vertex ML Metadata makes it easier to analyze the _lineage_ of your pipeline's artifacts, by saving you the difficulty of keeping track of your pipeline's metadata.

If you're new to Vertex ML Metadata, read the [introduction to Vertex ML Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction).

For a step-by-step tutorial on analyzing artifacts and metadata generated across your Agent Platform Pipelines executions, see the [Using Vertex ML Metadata with Agent Platform Pipelines](https://codelabs.developers.google.com/vertex-mlmd-pipelines#0) codelab. 

Follow these instructions to view the lineage graph for a pipeline artifact using Vertex ML Metadata:

  1. In the Google Cloud console, in the Gemini Enterprise Agent Platform section, go to the **Metadata** page.

[Go to Metadata](https://console.cloud.google.com/agent-platform/metadata)

The Metadata page lists the artifacts that have been created in the **default** metadata store.

  2. In the **Region** drop-down list, select the region that your run was created in.

  3. Click the **Display name** of an artifact to see its lineage graph.

A static graph showing the artifacts and executions that are a part of this lineage graph appears.

  4. Click an artifact or execution to learn more about it.




## Analyze the lineage of pipeline artifacts using Knowledge Catalog

Knowledge Catalog discovers metadata from Google Cloud resources, which include Agent Platform Pipelines artifacts like models, managed datasets, and other Google Cloud resources discoverable in Knowledge Catalog. You can discover these artifacts using the metadata search capability of Knowledge Catalog and view their lineage graphs.

For more information about the Knowledge Catalog metadata search capability, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

Note that Knowledge Catalog might not be available in all regions where Agent Platform Pipelines is supported. If Knowledge Catalog is unsupported in your region, use Vertex ML Metadata. [View the list of supported regions for Knowledge Catalog.](https://docs.cloud.google.com/dataplex/docs/locations)

Follow these instructions to view the lineage graph for a pipeline artifact on Knowledge Catalog:

  1. To launch a Knowledge Catalog search query in the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Use the filters to search for the artifacts. For example, you can use the **Data types** filter to specify the type of artifact, such as model, dataset, or BigQuery table. For more information, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

You can also [define your query in the search field](https://docs.cloud.google.com/dataplex/docs/search-syntax).

  3. To view the lineage of an artifact, click the name of the artifact, and then click the **Lineage** tab.

On the lineage graph, Agent Platform processes are preceded by ![Agent Platform lineage icon](https://docs.cloud.google.com/static/dataplex/images/vertex-lineage-icon.png). These include pipeline artifacts, pipeline components, and pipeline templates.

     * To view the details of a process, click the process in the lineage graph.

**Note:** The process details are available only if the process has been catalogued in Knowledge Catalog using a fully qualified name (FQN).
     * For processes based on pipeline tasks from pipeline runs, you can do the following:

       * View the pipeline run in Agent Platform by clicking **Open in Agent Platform** in the **Details tab**. To view the runtime details of a pipeline run, such as states, timestamps, and attributes, click **More**. To view the pipeline run in Agent Platform, click **Open in Agent Platform**.
     * For processes based on a pipeline template, you can do the following:

       * View the template details in Agent Platform by clicking **Open in Agent Platform** in the **Details tab**.

       * View the list of pipeline tasks created in pipeline runs in the **Runs** tab. To view the details of the pipeline template in Agent Platform, click **More** , and then click **Open in Agent Platform**.




## What's next

  * Learn how to [run a pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/run-pipeline).
  * Get started [visualizing and analyzing pipeline results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/visualize-pipeline).
  * Learn how to [build a machine learning pipeline](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
