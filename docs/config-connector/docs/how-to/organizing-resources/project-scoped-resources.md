---
url: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/project-scoped-resources/
title: Project-scoped resources \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:57.405126+00:00
---

# Project-scoped resources  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/project-scoped-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Project-scoped resources

Config Connector can manage your resources at the project, folder, or organization level. In order for Config Connector to determine where to create your resources, it first checks for a [scope-defining field](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#scope-defining_field) in your resource spec, if not found, then checks for a [scope-defining annotation](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#scope-defining_annotation).

**Note:** The scope concept does not apply to all Config Connector resources. See [Exceptions](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview#exceptions) for more details. You can check the [resource reference page](https://docs.cloud.google.com/config-connector/docs/reference/resources) to see if a resource supports the `spec.projectRef` field or `cnrm.cloud.google.com/project-id` annotation.

## Specify `projectRef` field

Most project-scoped Config Connector resources support a field named `projectRef` in its CRD spec. Use this field to specify the Google Cloud project that you want to create the resource in.

If the Google Cloud project is also managed in the same cluster with the the [Project](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/resourcemanager/project) CRD, you can specify the project as a Kubernetes resource reference:
    
    
    ...
    spec:
      projectRef:
        name: PROJECT_RESOURCE_NAME
        namespace: PROJECT_RESOURCE_NAMESPACE
    ...
    

This approach makes it possible to use Config Connector and create a Google Cloud project with its child resources in one single apply operation. The namespace field is optional if the project Kubernetes resource is in the same Kubernetes namespace as your project-scoped resource.

If the Google Cloud project is not managed as a Kubernetes resource in the same cluster, you can use the `external` field to directly specify the project ID. The exact format of the value may be different depending on the resource type. Two most common formats are "PROJECT_ID" and "projects/PROJECT_ID". See an example of "projects/PROJECT_ID" below:
    
    
    ...
    spec:
      projectRef:
        external: "projects/PROJECT_ID"
    ...
    

## Annotate resource configuration

If the Config Connector resource is project-scoped but does not support `projectRef` field, you can set the project ID to the resource configuration using the `project-id` annotation:
    
    
    ...
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: PROJECT_ID
    ...
    

Here is an example of what a `FooBar` resource's YAML looks like with this annotation in it:
    
    
    apiVersion: foo.cnrm.cloud.google.com/v1beta1
    kind: FooBar
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: PROJECT_ID
      name: foobarname
    

## Annotate namespace configuration

You can set a default project ID for newly-created resources by annotating your Kubernetes namespace. If any of the resources in the namespace have this annotation explicitly set in its own configuration, the resource-level annotation overwrites the namespace-level annotation. 

To annotate the namespace using command line, run the following command:
    
    
    kubectl annotate namespace NAMESPACE_NAME cnrm.cloud.google.com/project-id=PROJECT_ID
    

Replace the following:

  * `NAMESPACE_NAME`: your namespace name
  * `PROJECT_ID`: your Google Cloud project ID



Alternatively, you can apply a YAML manifest containing the annotation. Copy the YAML below into a file:
    
    
    apiVersion: v1
    kind: Namespace
    metadata:
      annotations:
        cnrm.cloud.google.com/project-id: PROJECT_ID
      name: NAMESPACE_NAME
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `NAMESPACE_NAME`: your namespace name



After you have created the file, apply it to your cluster.

**Note:** You must create the namespace and annotation before applying any resources to the namespace.

## Using the namespace name as the project ID

If neither the resource nor the namespace specifies a project ID, then Config Connector uses the namespace's name as the project ID. This default behavior is supported by Config Connector but we don't recommend it since the implicit default of project ID can be confusing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
