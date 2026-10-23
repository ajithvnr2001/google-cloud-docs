---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-parameters/
title: Parameterization of workflow templates \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:22.385427+00:00
---

# Parameterization of workflow templates  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-parameters/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Parameterization of workflow templates Stay organized with collections  Save and categorize content based on your preferences. 

If your [workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview) will be run multiple times with different values, you can avoid having to edit the workflow each time by defining parameters in the template (parameterizing the template). Then, you can pass different values for the parameters each time you run the template.

Parameters can be added to your workflow template when you create or update the template. 

## Parameterizable Fields

The following Managed Service for Apache Spark workflow template fields can be parameterized:

  * Labels
  * File URIs
  * [Managed cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster) name. Managed Service for Apache Spark will use the user-supplied name as the name prefix, and append random characters to create a unique cluster name. The cluster is deleted at the end of the workflow.
  * Job properties
  * Job arguments
  * Script variables (in HiveJob, SparkSqlJob, and PigJob)
  * Main class (in HadoopJob and SparkJob)
  * Zone (in ClusterSelector)
  * Number of Instances (`numInstances`) in a master or worker instance group.

Parameterizing cluster selector labels lets you choose the cluster where the workflow will run each time you run the workflow (see [Using cluster selectors with workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors)).

## Parameter attributes

[Workflow template parameters](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#templateparameter) are defined with the following required and optional attributes:

name (required)
    A unix-style variable name. This name will be used as a key when providing a value for the parameter later.
fields (required)
    A list of fields that this parameter will replace (see Parameterizable Fields for a list of fields that can be parameterized). Each field is specified as a "field path" (see Field Path Syntax for the syntax to use to specify a field path). Note that a field is allowed to appear in at most one parameter's list of field paths.
description (optional)
    Brief description of the parameter.
validation (optional)
    Rules used to validate a parameter value, which can be one of:  


  1. a list of allowed values  

  2. a list of regular expressions that a value must match.



### Field path syntax

A field path is similar in syntax to a [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask). For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Field paths can reference fields using the following syntax:

  * Managed cluster name:

    * placement.managedCluster.clusterName
  * Values in maps can be referenced by key, for example:  


    * labels['key']
    * placement.clusterSelector.clusterLabels['key']
    * placement.managedCluster.labels['key']
    * jobs['step-id'].labels['key']
  * Jobs in the jobs list can be referenced by step-id.  


    * jobs['step-id'].hadoopJob.mainJarFileUri
    * jobs['step-id'].hiveJob.queryFileUri
    * jobs['step-id'].pySparkJob.mainPythonFileUri
    * jobs['step-id'].hadoopJob.jarFileUris[0]
    * jobs['step-id'].hadoopJob.archiveUris[0]
    * jobs['step-id'].hadoopJob.fileUris[0]
    * jobs['step-id'].pySparkJob.pythonFileUris[0]

    * Items in repeated fields can be referenced by a zero-based index, for example:  


    * jobs['step-id'].sparkJob.args[0]

    * Other examples:

    * jobs['step-id'].hadoopJob.args[0]

    * jobs['step-id'].hadoopJob.mainJarFileUri

    * jobs['step-id'].hadoopJob.properties['key']

    * jobs['step-id'].hiveJob.scriptVariables['key']

    * placement.clusterSelector.zone




You can't parameterize maps and repeated fields in their entirety. Only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

`placement.clusterSelector.clusterLabels`  
`jobs['step-id'].sparkJob.args`

## Parameterize a workflow template

You parameterize a workflow template by defining template parameters with the Dataproc API or the Google Cloud CLI.

### gcloud command

You can define workflow template parameters by creating, or exporting with the Google Cloud CLI and editing, a workflow template YAML file, then importing the file with the Google Cloud CLI to create or update the template. See [Using YAML files](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-yamls) for more information.

**Example 1: Parameterized managed-cluster template example**

The following is a sample teragen-terasort [managed-cluster workflow](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster) template YAML file with four defined parameters: CLUSTER, NUM_ROWS, GEN_OUT, and SORT_OUT. Two versions are listed: one **BEFORE** and the other **AFTER** parameterization.

### Before
    
    
    placement:
      managedCluster:
        clusterName: my-managed-cluster
        config:
          gceClusterConfig:
            zoneUri: us-central1-a
    jobs:
    - hadoopJob:
        args:
        - teragen
        - '10000'
        - hdfs:///gen/
        mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
      stepId: teragen
    - hadoopJob:
        args:
        - terasort
        - hdfs:///gen/
        - hdfs:///sort/
        mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
      prerequisiteStepIds:
      - teragen
      stepId: terasort
    

### After
    
    
    placement:
      managedCluster:
        clusterName: 'to-be-determined'
        config:
          gceClusterConfig:
            zoneUri: us-central1-a
    jobs:
    - hadoopJob:
        args:
        - teragen
        - '10000'
        - hdfs:///gen/
        mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
      stepId: teragen
    - hadoopJob:
        args:
        - terasort
        - hdfs:///gen/
        - hdfs:///sort/
        mainJarFileUri: file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar
      prerequisiteStepIds:
      - teragen
      stepId: terasort
    **parameters:
    - description: The managed cluster name prefix
      fields:
      - placement.managedCluster.clusterName
      name: CLUSTER
    - description: The number of rows to generate
      fields:
      - jobs['teragen'].hadoopJob.args[1]
      name: NUM_ROWS
      validation:
        values:
          values:
          - '1000'
          - '10000'
          - '100000'
    - description: Output directory for teragen
      fields:
      - jobs['teragen'].hadoopJob.args[2]
      - jobs['terasort'].hadoopJob.args[1]
      name: GEN_OUT
      validation:
        regex:
          regexes:
          - hdfs:///.*
    - description: Output directory for terasort
      fields:
      - jobs['terasort'].hadoopJob.args[2]
      name: SORT_OUT
      validation:
        regex:
          regexes:
          - hdfs:///.***

**Example 2: Cluster selector workflow template example**

The following is a parameterized sample teragen-terasort [cluster-selector workflow](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/cluster-selectors#adding_a_cluster_selector_to_a_template) template YAML file with three defined parameters: CLUSTER, NUM_ROWS, and OUTPUT_DIR.
    
    
    placement:
      clusterSelector:
        clusterLabels:
          goog-dataproc-cluster-name: 'to-be-determined'
    jobs:
      - stepId: teragen
        hadoopJob:
          args:
          - 'teragen'
          - 'tbd number of rows'
          - 'tbd output directory'
    **parameters:
    - name: CLUSTER
      fields:
      - placement.clusterSelector.clusterLabels['goog-dataproc-cluster-name']
    - name: NUM_ROWS
      fields:
      - jobs['teragen'].hadoopJob.args[1]
    - name: OUTPUT_DIR
      fields:
      - jobs['teragen'].hadoopJob.args[2]**
    

After creating or editing a YAML file that defines a workflow template with template parameters, use the following gcloud command to import the YAML file to create or update the parameterized template.
    
    
    gcloud dataproc workflow-templates import template-ID or template-name \
        --region=region \
        --source=template.yaml
    

You can pass either the [WorkflowTemplate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates#resource-workflowtemplate) `id` or the fully qualified template resource `name` ("projects/projectId/regions/region/workflowTemplates/template_id") to the command. If a template resource with the same template name exists, it will be overwritten (updated) and its version number will be incremented. If a template with the same template name does not exist, it will be created.

You can't use the Google Cloud CLI to run a workflow directly from a YAML file that defines a parameterized workflow template (see [Instantiate a workflow using a YAML file](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-yamls#instantiate_a_workflow_using_a_yaml_file). You must first import the YAML file, then pass parameters to the workflow template when you instantiate it as explained in this and the following subsections.

### Rest API

You can define one or more [WorkflowTemplate.parameters](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates#WorkflowTemplate) in a [workflowTemplates.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/create) or a [workflowTemplates.update](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/update) API request.

The following is a sample `workflowTemplates.create` request to create a teragen-terasort workflow template with four defined parameters: CLUSTER, NUM_ROWS, GEN_OUT, and SORT_OUT.
    
    
    POST https://dataproc.googleapis.com/v1/projects/my-project/locations/us-central1/workflowTemplates
    {
      "id": "my-template",
      "jobs": [
        {
          "stepId": "teragen",
          "hadoopJob": {
            "mainJarFileUri": "file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
            "args": [
              "teragen",
              "10000",
              "hdfs:///gen/"
            ]
          }
        },
        {
          "stepId": "terasort",
          "prerequisiteStepIds": [
            "teragen"
          ],
          "hadoopJob": {
            "mainJarFileUri": "file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
            "args": [
              "terasort",
              "hdfs:///gen/",
              "hdfs:///sort/"
            ]
          }
        }
      ],
      "parameters": [
        {
          "name": "CLUSTER",
          "fields": [
            "placement.managedCluster.clusterName"
          ],
          "description": "The managed cluster name prefix"
        },
        {
          "name": "NUM_ROWS",
          "fields": [
            "jobs['teragen'].hadoopJob.args[1]"
          ],
          "description": "The number of rows to generate",
          "validation": {
            "values": {
              "values": [
                "1000",
                "10000",
                "100000"
              ]
            }
          }
        },
        {
          "name": "GEN_OUT",
          "fields": [
            "jobs['teragen'].hadoopJob.args[2]",
            "jobs['terasort'].hadoopJob.args[1]"
          ],
          "description": "Output directory for teragen",
          "validation": {
            "regex": {
              "regexes": [
                "hdfs:///.*"
              ]
            }
          }
        },
        {
          "name": "SORT_OUT",
          "fields": [
            "jobs['terasort'].hadoopJob.args[2]"
          ],
          "description": "Output directory for terasort",
          "validation": {
            "regex": {
              "regexes": [
                "hdfs:///.*"
              ]
            }
          }
        }
      ],
      "placement": {
        "managedCluster": {
          "clusterName": "to-be-determined",
          "config": {
            "gceClusterConfig": {
              "zoneUri": "us-central1-a"
            }
          }
        }
      }
    }
    

## Pass parameters to a parameterized template

You can pass a different set of parameter values each time you run a parameterized workflow template. You must provide a value for each parameter defined in the template.

### gcloud Command

You can pass a map of parameter names to values to the [gcloud dataproc workflow-templates instantiate ](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/instantiate) command with the `--parameters` flag. All parameter values defined in the template must be supplied. The supplied values will override values specified in the template.

**Parameterized managed-cluster template example**
    
    
    gcloud dataproc workflow-templates instantiate my-template \
        --region=region \
        --parameters=CLUSTER=cluster,NUM_ROWS=1000,GEN_OUT=hdfs:///gen_20180601/,SORT_OUT=hdfs:///sort_20180601
    

**Parameterized cluster-selector template example**
    
    
    gcloud dataproc workflow-templates instantiate \
      --parameters CLUSTER=my-cluster,NUM_ROWS=10000,OUTPUT_DIR=hdfs://some/dir
        

### Rest API

You can pass a [`parameters` map](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/instantiate#request-body) of parameter `names` to `values` to the Managed Service for Apache Spark [workflowTemplates.instantiate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/instantiate) API. All parameter values defined in the template must be supplied. The supplied values will override values specified in the template.

You cannot pass parameters to a parameterized workflow template using the [workflowTemplates.instantiateinline](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.workflowTemplates/instantiateInline) API.. 

**Example:**
    
    
    POST https://dataproc.googleapis.com/v1/projects/my-project/regions/us-central1/workflowTemplates/my-template:instantiate
    {
      "parameters": {
        "CLUSTER": "clusterA",
        "NUM_ROWS": "1000",
        "GEN_OUT": "hdfs:///gen_20180601/",
        "SORT_OUT": "hdfs:///sort_20180601/"
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
