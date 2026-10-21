---
url: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/export/
title: Export and import resources to Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:18.571252+00:00
---

# Export and import resources to Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Export and import resources to Config Connector

This page describes the `config-connector export` command and how to use it to export Google Cloud resources into YAML files, which you can subsequently import into Config Connector. If you already have access to the resource's YAML file, follow the steps in [Managing and deleting resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources) to acquire the resource instead.

## Limitations

Not all resources support the `export` command. To get a list of supported resources, run `config-connector print-resources`.

**Tip:** If a resource is not supported by `export`, but is supported by `bulk-export`, you can try [filtering an Asset Inventory export with `bulk-export`](https://docs.cloud.google.com/config-connector/docs/how-to/import-export/bulk-export#discovering_resources_to_import).

## Before you begin

  1. [Install the `config-connector` CLI tool](https://docs.cloud.google.com/config-connector/docs/how-to/import-export/overview).
  2. To simplify commands, set your default namespace by running the following command: 
         
         kubectl config set-context --current --namespace NAMESPACE_NAME

Replace `NAMESPACE_NAME` with your namespace name.
  3. Get the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) for the resource that you want to export. If you don't know the resource's full name, you might be able to find it with one of the following methods: 
     * [Use Cloud Asset Inventory to search for a resource](https://docs.cloud.google.com/asset-inventory/docs/search-resources).
     * Use the `describe` or `list` command for the resource, for example `gcloud pubsub topics describe sample-topic --format "value(name)"`.
     * Check the resource's product documentation for a guide on getting the resource ID, for example [Getting a Cloud Key Management Service resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids).



## Export a resource

You can use the `config-connector` CLI tool to export an existing resource into a YAML file.

To export a resource into a YAML file, run the following command:
    
    
    config-connector export RESOURCE_ID
    

Replace `RESOURCE_ID` with the full name of the resource that you want to export.

The command outputs the resource in YAML format that can be used by Config Connector. The output should resemble the following example:
    
    
    apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
    kind: PubSubTopic
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: my-example-project
      name: sample-topic
    

## Import a resource into Config Connector

After you have the YAML file for the resource that you want Config Connector to acquire, complete the following steps:

  1. Pass your resource into Config Connector by running the following command:
         
         config-connector export RESOURCE_ID | kubectl apply -f -  --namespace NAMESPACE
         

Replace `NAMESPACE` with the namespace that Config Connector manages resources from.

  2. Confirm that Config Connector is managing the resource by running the following command:
         
         kubectl describe RESOURCE_TYPE RESOURCE_NAME
         

Replace the following:

     * `RESOURCE_TYPE`: the resource type, for example `pubsubtopic`.
     * `RESOURCE_NAME`: the resource name. This doesn't have to be the full resource name.



After Config Connector acquires the resource, you can manage that resource by following the steps in [Managing and deleting resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources).

## `config-connector` CLI tool optional fields

When running the `config-connector export` command, you can pass the following optional fields:
    
    
    config-connector export RESOURCE_NAME \
        --output FILENAME \
        --oauth2-token TOKEN \
        --iam-format [policy | policymember | none] \
        --filter-deleted-iam-members [true | false] \
        --verbose
    

  * `--output`: An optional output path that disables standard output. When a file, the result contains all the command output; when a directory, the directory contains a new file for each resource in the output.
  * `--oauth2-token`: An [OAUTH2 token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) as the Google Cloud identity. By default, `config-connector` uses the [Google Cloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate).
  * `--iam-format`: Specifies the kind of IAM resources output with your export. Options are [`policy`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicy) (default), [`policymember`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicymember), or `none`.
  * `--filter-deleted-iam-members`: Specifies whether to filter out deleted IAM principals. Options are `true` or `false`. The default value is `false`.
  * `--verbose`: Enables verbose logging.



## What's next

  * Read about how Config Connector [acquires existing Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource).
  * [Learn about the resources that Config Connector supports](https://docs.cloud.google.com/config-connector/docs/reference/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
