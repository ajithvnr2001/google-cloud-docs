---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/use-yamls/
title: Use YAML files with workflows \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:52.478602+00:00
---

# Use YAML files with workflows  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/use-yamls/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use YAML files with workflows Stay organized with collections  Save and categorize content based on your preferences. 

You can define a workflow template in a YAML file, then instantiate the template to run the workflow. You can also import and export a workflow template YAML file to create and update a Managed Service for Apache Spark workflow template resource.

Also see [Using inline Managed Service for Apache Spark workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/inline-workflows) for other ways to run a workflow without creating a workflow template resource.

### Run a workflow using a YAML file

To run a workflow without first creating a workflow template resource, use the [gcloud dataproc workflow-templates instantiate-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate-from-file) command.

  1. Define your workflow template in a YAML file. The YAML file must include all required [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates) fields except the `id` field, and it must also exclude the `version` field and all output-only fields. In the following workflow example, the `prerequisiteStepIds` list in the `terasort` step ensures the `terasort` step will only begin after the `teragen` step completes successfully. 
         
         jobs:
         - hadoopJob:
             args:
             - teragen
             - '1000'
             - hdfs:///gen/
             mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
           stepId: teragen
         - hadoopJob:
             args:
             - terasort
             - hdfs:///gen/
             - hdfs:///sort/
             mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
           stepId: terasort
           prerequisiteStepIds:
             - teragen
         placement:
           managedCluster:
             clusterName: my-managed-cluster
             config:
               gceClusterConfig:
                 zoneUri: us-central1-a
         

  2. Run the workflow: 
         
         gcloud dataproc workflow-templates instantiate-from-file \
             --file=TEMPLATE_YAML \
             --region=REGION
         




### Instantiate a workflow using a YAML file with Managed Service for Apache Spark Auto Zone Placement

  1. Define your workflow template in a YAML file. This YAML file is the same as the previous YAML file, except the `zoneUri` field is set to the empty string ('') to allow Managed Service for Apache Spark [Auto Zone Placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) to select the zone for the cluster. 
         
         jobs:
         - hadoopJob:
             args:
             - teragen
             - '1000'
             - hdfs:///gen/
             mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
           stepId: teragen
         - hadoopJob:
             args:
             - terasort
             - hdfs:///gen/
             - hdfs:///sort/
             mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
           stepId: terasort
           prerequisiteStepIds:
             - teragen
         placement:
           managedCluster:
             clusterName: my-managed-cluster
             config:
               gceClusterConfig:
                 zoneUri: ''
         

  2. Run the workflow. When using Auto Placement, you must pass a [region](https://docs.cloud.google.com/managed-spark/docs/concepts/regional-endpoints) to the `gcloud` command. 
         
         gcloud dataproc workflow-templates instantiate-from-file \
             --file=TEMPLATE_YAML \
             --region=REGION
         




### Import and export a workflow template YAML file

You can import and export workflow template YAML files. Typically, a workflow template is first exported as a YAML file, then the YAML is edited, and then the edited YAML file is imported to update the template.

  1. [Export the workflow template](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/export) to a YAML file. During the export operation, the `id` and `version` fields, and all output-only fields are filtered from the output and do not appear in the exported YAML file. 
         
         gcloud dataproc workflow-templates export TEMPLATE_ID or TEMPLATE_NAME \
             --destination=TEMPLATE_YAML \
             --region=REGION
         

You can pass either the [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) `id` or the fully qualified template resource `name` ("projects/PROJECT_ID/regions/REGION/workflowTemplates/TEMPLATE_ID") to the command. If you omit the `--destination` flag, the output is directed to `stdout`, so the following command will also export the template to a YAML file: 
         
         gcloud dataproc workflow-templates export TEMPLATE_ID or TEMPLATE_NAME \
             --region=REGION > TEMPLATE_YAML
         
         

  2. Edit the YAML file locally. Note that the `id`, `version`, and output-only fields, which were filtered from the YAML file when the template was exported, are disallowed in the imported YAML file.

  3. [Import the updated workflow template](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/import) YAML file: 
         
         gcloud dataproc workflow-templates import TEMPLATE_ID or TEMPLATE_NAME \
             --source=TEMPLATE_YAML \
             --region=REGION
         

You can pass either the [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) `id` or the fully qualified template resource `name` ("projects/PROJECT_ID/regions/region/workflowTemplates/TEMPLATE_ID") to the command. The template resource with the same template name will be overwritten (updated) and its version number will be incremented. If a template with the same template name does not exist, it will be created.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
