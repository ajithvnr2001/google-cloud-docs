---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/
title: gcloud beta dataproc workflow-templates \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:58.284614+00:00
---

# gcloud beta dataproc workflow-templates  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc workflow-templates Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc workflow-templates - create and manage Dataproc workflow templates 
SYNOPSIS
    

`gcloud beta dataproc workflow-templates` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create and manage Dataproc workflow templates. 
EXAMPLES
     To create a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/create) my_template

To instantiate a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates instantiate](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/instantiate) my_template

To instantiate a workflow template from a file, run: 
    
    
    [gcloud beta dataproc workflow-templates instantiate-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/instantiate-from-file) --file template.yaml

To delete a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/delete) my_template

To view the details of a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/describe) my_template

To see the list of all workflow templates, run: 
    
    
    [gcloud beta dataproc workflow-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/list)

To remove a job from a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates remove-job](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/remove-job) my_template --step-id id

To update managed cluster in a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates set-managed-cluster](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-managed-cluster) my_template --num-masters 5

To update cluster selector in a workflow template, run: 
    
    
    [gcloud beta dataproc workflow-templates set-cluster-selector](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-cluster-selector) my_template --cluster-labels environment=prod

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[add-job](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job)`
     `(BETA)` Add Dataproc jobs to workflow template. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/create)`
     `(BETA)` Create a workflow template. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/delete)`
     `(BETA)` Delete a workflow template. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/describe)`
     `(BETA)` Describe a workflow template. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/export)`
     `(BETA)` Export a workflow template. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/get-iam-policy)`
     `(BETA)` Get IAM policy for a workflow template. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/import)`
     `(BETA)` Import a workflow template. 
`[instantiate](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/instantiate)`
     `(BETA)` Instantiate a workflow template. 
`[instantiate-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/instantiate-from-file)`
     `(BETA)` Instantiate a workflow template from a file. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/list)`
     `(BETA)` List workflow templates. 
`[remove-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/remove-dag-timeout)`
     `(BETA)` Remove DAG timeout from a workflow template. 
`[remove-job](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/remove-job)`
     `(BETA)` Remove a job from workflow template. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/run)`
     `(BETA)` `(DEPRECATED)` Run a workflow template. 
`[set-cluster-selector](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-cluster-selector)`
     `(BETA)` Set cluster selector for the workflow template. 
`[set-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-dag-timeout)`
     `(BETA)` Set DAG timeout on a workflow template. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-iam-policy)`
     `(BETA)` Set IAM policy for a template. 
`[set-managed-cluster](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/set-managed-cluster)`
     `(BETA)` Set a managed cluster for the workflow template. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc workflow-templates](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates)
    
    
    [gcloud alpha dataproc workflow-templates](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
