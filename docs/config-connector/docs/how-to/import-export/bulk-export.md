---
url: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/bulk-export/
title: Bulk importing and exporting existing Google Cloud resources \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:21.142707+00:00
---

# Bulk importing and exporting existing Google Cloud resources  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/import-export/bulk-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bulk importing and exporting existing Google Cloud resources

This page describes the `config-connector bulk-export` command and how to use it to export Google Cloud resources into Config Connector YAML files which you can subsequently import into Config Connector.

`config-connector bulk-export` uses [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview)'s [Export](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-cloud-storage) functionality to discover existing Google Cloud resources. You can provide a Cloud Asset Inventory export or `config-connector` can perform the export on your behalf.

Cloud Asset Inventory exports JSON structures. Each structure has the name of the resource, its Asset Inventory type, and its ancestor resources: projects, folders, and organization. To discover the types supported by asset inventory, see [Supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types).

## Limitations

Not all resources support the `bulk-export` command. To get a list of supported resources, run `config-connector print-resources`.

## Before you begin

  1. [Install the `config-connector tool`](https://docs.cloud.google.com/config-connector/docs/how-to/import-export/overview#installing-config-connector)

  2. If you want to use the `config-connector` tool to export directly from Cloud Asset Inventory, enable the Cloud Asset Inventory API on your Google Cloud Identity's project with `gcloud`.
         
         gcloud services enable cloudasset.googleapis.com
         




## Bulk export example

In this example, you create a PubSubTopic with the Google Cloud CLI and then import it into Config Connector.

  1. Create a topic named `sample-topic` with the Google Cloud CLI:
         
         gcloud pubsub topics create sample-topic
         

You receive confirmation that the topic has been created.
         
         Created topic [projects/PROJECT_ID/topics/sample-topic].
         

In the output, `PROJECT_ID` is replaced with your Google Cloud project.

  2. Get the topic's Google Cloud resource name and save it into an environment variable with the following command:
         
         TOPIC_RESOURCE_NAME=$(gcloud pubsub topics describe sample-topic --format "value(name)")
         

  3. To identify objects, the `config-connector` tool uses Cloud Asset Inventory JSON structures. Save the topic asset's JSON structure into an environment variable:
         
         TOPIC_ASSET='{"name":"//pubsub.googleapis.com/'"${TOPIC_RESOURCE_NAME}"'","asset_type":"pubsub.googleapis.com/Topic"}'
         

  4. Pass the asset into `config-connector bulk-export` by running the following command:
         
         echo ${TOPIC_ASSET} | config-connector bulk-export
         

The output is a Config Connector resource in YAML format.
         
         ---
         apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
         kind: PubSubTopic
         metadata:
           annotations:
             cnrm.cloud.google.com/project-id: PROJECT_ID
           name: sample-topic
         ...
         

In the output, `PROJECT_ID` is replaced with your Google Cloud project.

  5. You can pass this resource into Config Connector with `kubectl apply -f -`. To pass the resource directly, run the following command:
         
         echo ${TOPIC_ASSET} | config-connector bulk-export | kubectl apply -f -  --namespace CC_NAMESPACE
         

Replace CC_NAMESPACE with the namespace that Config Connector manages resources from.

Config Connector [acquires the resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource).

  6. Confirm that Config Connector is managing the resource with [`kubectl describe`](https://docs.cloud.google.com/config-connector/docs/how-to/get-resource-info):
         
         kubectl describe pubsubtopic sample-topic --namespace CC_NAMESPACE
         

Replace `CC_NAMESPACE` with the namespace that Config Connector manages resources from.




### Cleaning up

You can delete your PubSubTopic with `config-connector bulk-export` and `kubectl delete`.
    
    
    echo ${TOPIC_ASSET} | config-connector bulk-export | kubectl delete -f - --namespace CC_NAMESPACE
    

Replace `CC_NAMESPACE` with the namespace that Config Connector manages resources from.

## Discovering resources to import

When importing resources, you can perform a [Cloud Asset Inventory export](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-cloud-storage#exporting_an_asset_snapshot) and supply the results to `config-connector bulk-export` or have `config-connector bulk-export` perform one on your behalf.

### Importing from an Cloud Asset Inventory export

You can provide an asset inventory export by providing a path to a local file containing the export or piping the results of an export to `config-connector` on STDIN.

### Importing from a local file

You can provide an [asset inventory export](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-cloud-storage#exporting_an_asset_snapshot) to `config-connector bulk-export` by using a local file with the `--input` parameter.
    
    
    config-connector bulk-export --input ASSET_INVENTORY_EXPORT
    

Replace `ASSET_INVENTORY_EXPORT` with the filename of your Cloud Asset Inventory export.

### Importing from STDIN

To provide an asset inventory export on STDIN, pipe the results of an export to `config-connector bulk-export`. For example, if your export is in a local file named `export.json`, pipe the contents of the file to `config-connector bulk-export` without supplying any of the export parameters.
    
    
    cat export.json | config-connector bulk-export
    

#### Filtering an Asset Inventory export on STDIN

To filter an asset inventory export, you can use the [`jq`](https://stedolan.github.io/jq/) tool and pipe to input the results to `config-connector bulk-export`. For example, if you want to only import PubSubTopic assets from the file EXPORT_FILE, run the following command:
    
    
    cat EXPORT_FILE | jq '. | select( .asset_type == "pubsub.googleapis.com/Topic" )' | config-connector bulk-export
    

## Exporting an inventory with config-connector

The `config-connector bulk-export` tool can export resources from a Google Cloud [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

**Note:** You might not have permissions to export all of the resources in your project, folder, or organization. If you encounter an `error converting asset`, try the same command with the option `-on-error continue`.

### Exporting your project

To export all resources from your project, use the `--project` parameter.
    
    
    config-connector bulk-export --project PROJECT_ID
    

Replace `PROJECT_ID` with your Google Cloud project.

### Exporting your folder

To export all resources from a folder, use the `--folder` parameter.
    
    
    config-connector bulk-export --folder FOLDER_NUMBER
    

Replace `FOLDER_NUMBER` with your Google Cloud folder number.

### Exporting your organization

To export all resources from your organization, use the `--organization` parameter.
    
    
    config-connector bulk-export --organization ORGANIZATION_ID
    

Replace `ORGANIZATION_ID` with your Google Cloud organization ID.

### Cloud Storage location

Asset inventory export's output location is a [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) URI. When `config-connector bulk-export` performs an export, it uses a Cloud Storage bucket. By default, `config-connector bulk-export` creates a temporary bucket. You can also specify the bucket name.

#### Temporary Cloud Storage bucket

If you do not provide the `--storage-key` parameter, `config-connector bulk-export` creates a temporary Cloud Storage bucket on your behalf. The bucket is created in the default location for storage buckets; the `US` [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr). The bucket is deleted when the export is complete.

#### Specifying a temporary bucket

To specify a bucket, use a Cloud Storage URI with the `storage-key` parameter. If the URI is only the name of the bucket, then a name is generated for the export storage object. If the URI is a full path to a storage object, then the full path is used.
    
    
    config-connector bulk-export --storage-key gs://BUCKET_NAME
    

## Output

The output from the `config-connector bulk-export` command is Config Connector resources in YAML format. The YAML file is written to STDOUT by default. You can direct the output of resources to files with the `output` option.

### Output to a single file

When you set the `--output` parameter, `config-connector bulk-export` writes its results to a single file if one of the following is true:

  * The file specified by `output` exists and is a [`regular`](https://en.wikipedia.org/wiki/Unix_file_types) file.
  * The file specified by `output` does not exist and the parent directory represented by `output` does exist.



### Output to a directory

`config-connector` writes its results to multiple files when the `--output` parameter is a directory that ends in a `/`. `config-connector bulk-export` creates one file per resource, and file names match their resource names.
    
    
    config-connector bulk-export --project PROJECT_ID --on-error continue --output OUTPUT_DIRECTORY/
    

Replace `PROJECT_ID` with your Google Cloud project.

For example, to output assets from the project `my-project` to the `sample` directory, run the following command:
    
    
    config-connector bulk-export --project my-project --on-error continue --output sample/
    

## Command-line options

The `config-connector bulk-export` command has the following options:
    
    
    config-connector bulk-export
        --input FILENAME \
        --output FILENAME \
        --storage-key gs://BUCKET_NAME \
        --project PROJECT_ID \
        --folder FOLDER_NUMBER \
        --organization ORGANIZATION_ID \
        --oauth2-token TOKEN \
        --on-error [halt | continue | ignore] \
        --iam-format [policy | policymember | none] \
        --filter-deleted-iam-members [true | false] \
        --verbose
    

  * `--input`: Cloud Asset Inventory input file.
  * `--output`: An optional output file path that disables standard output. When a file, the result contains all the command output; when a directory, the directory will contain a new file for each resource in the output.
  * `--storage-key`: Target temporary Cloud Storage bucket for export.
  * `--project`: Google Cloud project ID to export
  * `--folder`: Google Cloud folder ID to export
  * `--organization`: Google Cloud organization ID to export.
  * `--oauth2-token`: An [OAUTH2 token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) as the Google Cloud identity. By default, `config-connector` uses the [Google Cloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate).
  * `--on-error`: Control the behavior when a recoverable error occurs. Options are 'continue', 'halt', or 'ignore'. 
    * `halt`: stop execution on any error (default)
    * `continue`: continue processing resources, print the error to STDERR
    * `ignore`: continue processing resources and don't print the error
  * `--iam-format`: Specifies the kind of IAM resources output with your export. Options are [`policy`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicy) (default), [`policymember`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicymember), or `none`.
  * `--filter-deleted-iam-members`: Specifies whether to filter out deleted IAM principals. Options are `true` or `false`. The default value is `false`.
  * `--verbose`: Enables verbose logging.



## What's next

  * Read about how Config Connector [acquires existing Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource)
  * Learn about [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) and [Exporting assets to Cloud Storage](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-cloud-storage).
  * [Learn about the resources that Config Connector supports](https://docs.cloud.google.com/config-connector/docs/reference/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
