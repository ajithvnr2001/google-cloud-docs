---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/
title: gcloud alpha dataproc workflow-templates \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:06.905968+00:00
---

# gcloud alpha dataproc workflow-templates  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc workflow-templates Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc workflow-templates - create and manage Dataproc workflow templates 
SYNOPSIS
    

`gcloud alpha dataproc workflow-templates` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create and manage Dataproc workflow templates. 
EXAMPLES
     To create a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/create) my_template

To instantiate a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates instantiate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/instantiate) my_template

To instantiate a workflow template from a file, run: 
    
    
    [gcloud alpha dataproc workflow-templates instantiate-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/instantiate-from-file) --file template.yaml

To delete a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/delete) my_template

To view the details of a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/describe) my_template

To see the list of all workflow templates, run: 
    
    
    [gcloud alpha dataproc workflow-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/list)

To remove a job from a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates remove-job](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/remove-job) my_template --step-id id

To update managed cluster in a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates set-managed-cluster](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-managed-cluster) my_template --num-masters 5

To update cluster selector in a workflow template, run: 
    
    
    [gcloud alpha dataproc workflow-templates set-cluster-selector](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-cluster-selector) my_template --cluster-labels environment=prod

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[add-job](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/add-job)`
     `(ALPHA)` Add Dataproc jobs to workflow template. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/create)`
     `(ALPHA)` Create a workflow template. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/delete)`
     `(ALPHA)` Delete a workflow template. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/describe)`
     `(ALPHA)` Describe a workflow template. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/export)`
     `(ALPHA)` Export a workflow template. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/get-iam-policy)`
     `(ALPHA)` Get IAM policy for a workflow template. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/import)`
     `(ALPHA)` Import a workflow template. 
`[instantiate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/instantiate)`
     `(ALPHA)` Instantiate a workflow template. 
`[instantiate-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/instantiate-from-file)`
     `(ALPHA)` Instantiate a workflow template from a file. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/list)`
     `(ALPHA)` List workflow templates. 
`[remove-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/remove-dag-timeout)`
     `(ALPHA)` Remove DAG timeout from a workflow template. 
`[remove-job](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/remove-job)`
     `(ALPHA)` Remove a job from workflow template. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/run)`
     `(ALPHA)` `(DEPRECATED)` Run a workflow template. 
`[set-cluster-selector](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-cluster-selector)`
     `(ALPHA)` Set cluster selector for the workflow template. 
`[set-dag-timeout](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-dag-timeout)`
     `(ALPHA)` Set DAG timeout on a workflow template. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-iam-policy)`
     `(ALPHA)` Set IAM policy for a template. 
`[set-managed-cluster](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/set-managed-cluster)`
     `(ALPHA)` Set a managed cluster for the workflow template. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc workflow-templates](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates)
    
    
    [gcloud beta dataproc workflow-templates](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
