---
url: https://docs.cloud.google.com/config-connector/docs/concepts/namespaces-and-projects/
title: Namespaces and Google Cloud projects \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:12.492990+00:00
---

# Namespaces and Google Cloud projects  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/namespaces-and-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Namespaces and Google Cloud projects

Config Connector creates Google Cloud resources using Kubernetes configuration. These resources are organized in [Kubernetes Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

## How Config Connector uses Namespaces

Config Connector can use the annotations on the resource's `Namespace` to determine what project, folder, or organization to create the resources in. The `Namespace`'s annotation will only be applied if the resource configuration does not already specify where to create the resource. For more information, see [Organizing resources with projects and folders](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview)

For example, if you want to create a Cloud SQL Instance with a name of `mySQL` in your project with a project ID of `myProject`, then run this command to annotate your namespace:
    
    
    kubectl annotate namespace \
     NAMESPACE_NAME cnrm.cloud.google.com/project-id="myProject"
    

Replace `NAMESPACE_NAME` with your Namespace name.

Then, create a Config Connector `SQLInstance` with a name of `mySQL` in your namespace. Config Connector creates a corresponding Cloud SQL instance in your specified Google Cloud project, based on the configured namespace annotation.

## Using Namespaces with projects, folders, and organizations

Google Cloud supports organizing resources at the [Project, Folder, and Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail) levels. You can add Annotations to your Config Connector Namespaces to map resources to a [Project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects), a [Folder](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) or [Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

To learn more, see [Organizing resources with projects, folders, or organizations](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
