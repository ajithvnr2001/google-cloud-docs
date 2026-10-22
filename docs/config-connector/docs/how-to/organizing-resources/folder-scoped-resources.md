---
url: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/folder-scoped-resources/
title: Folder-scoped resources \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:19.592562+00:00
---

# Folder-scoped resources  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/folder-scoped-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Folder-scoped resources

Config Connector can manage your resources at the project, folder, or organization level. In order for Config Connector to determine where to create your resources, it first checks for a [scope-defining field](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#scope-defining_field) in your resource spec, if not found, then checks for a [scope-defining annotation](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#scope-defining_annotation).

**Note:** The scope concept does not apply to all Config Connector resources. See [Exceptions](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#exceptions) for more details. You can check the [resource reference page](https://docs.cloud.google.com/config-connector/docs/reference/resources) to see if a resource supports the `spec.folderRef` field or `cnrm.cloud.google.com/folder-id` annotation.

## Specify `folderRef` field

Most folder-scoped Config Connector resources support a field named `folderRef` in its CRD spec. Use this field to specify the Google Cloud folder you want to create the resource in.

If the Google Cloud folder is also being managed in the same cluster via the [Folder](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/resourcemanager/folder) CRD, you can specify the folder as a Kubernetes resource reference:
    
    
    ...
    spec:
      folderRef:
        name: FOLDER_RESOURCE_NAME
        namespace: FOLDER_RESOURCE_NAMESPACE
    ...
    

This approach makes it possible to use Config Connector and create a Google Cloud folder with its child resources in one single apply operation. The namespace field is optional if the Config Connector Folder resource is in the same Kubernetes namespace as your folder-scoped resource.

If the Google Cloud folder is not being managed as a Kubernetes resource in the same cluster, you can use the `external` field to directly specify the folder ID. The exact format of the value may be different depending on the resource type. Two most common formats are "FOLDER_ID" and "folders/FOLDER_ID". See an example of "FOLDER_ID" below:
    
    
    ...
    spec:
      folderRef:
        external: "FOLDER_ID"
    ...
    

## Annotate resource configuration

If the Config Connector resource is folder-scoped but does not support the `folderRef` field, you can set the folder ID to the resource configuration using the `folder-id` annotation:
    
    
    ...
    metadata:
      annotations:
        cnrm.cloud.google.com/folder-id: FOLDER_ID
    ...
    

The following example shows what a resource's YAML configuration looks like with this annotation:
    
    
    apiVersion: SERVICE_NAME.cnrm.cloud.google.com/v1beta1
    kind: RESOURCE_KIND
    metadata:
      annotations:
        cnrm.cloud.google.com/folder-id: FOLDER_ID
      name: RESOURCE_NAME
    

Replace the following:

  * `SERVICE_NAME`: the Google Cloud service name for the resource
  * `RESOURCE_KIND`: the kind of the Config Connector resource
  * `FOLDER_ID`: your Google Cloud folder ID
  * `RESOURCE_NAME`: the name of the resource



## Annotate namespace configuration

You can set a default folder ID for newly-created resources by annotating your Kubernetes namespace. If any of the resources in the namespace have this annotation explicitly set in its own configuration, the resource-level annotation overwrites the namespace-level annotation. 

To annotate the namespace using command line, run the following command:
    
    
    kubectl annotate namespace NAMESPACE_NAME cnrm.cloud.google.com/folder-id=FOLDER_ID
    

Replace the following:

  * `NAMESPACE_NAME`: your namespace name
  * `FOLDER_ID`: your Google Cloud folder ID



Alternatively, you can apply a YAML manifest containing the annotation. Copy the YAML below into a file:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      annotations:
        cnrm.cloud.google.com/folder-id: FOLDER_ID
      name: NAMESPACE_NAME
    

Replace the following:

  * `FOLDER_ID`: your Google Cloud folder ID
  * `NAMESPACE_NAME`: your namespace name



After you have created the file, apply it to your cluster.

**Note:** You must create the namespace and annotation before applying any resources into the namespace.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
