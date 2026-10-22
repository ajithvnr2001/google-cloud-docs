---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/
title: Configurations Overview \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:08.813907+00:00
---

# Configurations Overview  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Configurations Overview Stay organized with collections  Save and categorize content based on your preferences. 

A configuration defines the structure of your deployment, including the type and properties of the resources that are part of the deployment, any templates the configuration should use, and additional subfiles that can be executed to create your final configuration. You must always specify a configuration in order to create a deployment.

In your configuration, you can define a variety of supported Google Cloud platform resources from different services in a single configuration file. Some example resources include:

  * All [Compute Engine](https://docs.cloud.google.com/compute/docs) resources including: 
    * [Autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler)
    * [Instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) and [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/manager)
  * [Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)
  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Cloud SQL](https://docs.cloud.google.com/cloud-sql)



For a full list of resources, consult this table of [Supported resource types](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types) or make a [`list()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/types/list) request to the [Types collection](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/types).

## Configuration language

You must write configuration files using [YAML](http://en.wikipedia.org/wiki/YAML) syntax. To learn how to create a configuration file, see [Create a Configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).

## Template languages

A configuration can import one or more template files that Deployment Manager will expand during deployment to create the final configuration. You can write templates in either Jinja or Python. It is possible to mix and match templates. A single configuration can import both Jinja and Python templates. A template can be a local file or a file hosted at a third-party URL.

Templates offer additional functionality, like the ability to use environment variables, the ability to define custom variables, the ability to use Python libraries, and so on.

For more information about templates, read [Creating a Basic Template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).

## Configuration limits

All configurations are expanded on the server side within a controlled environment that Deployment Manager maintains. In order to prevent abuse, this environment is closely managed by the Deployment Manager team and has some limitations:

  * Neither your original configuration nor your expanded configuration can exceed 1 MB.
  * Any configurations uploaded to Deployment Manager are limited in the amount of time the configuration can take to run and the amount of processing power the configuration consumes during expansion. If you run into this limitation, consider splitting your configuration into smaller templates, or simplify complex structures such as recursion and nested loops.
  * Any Python templates you use cannot make any system or network calls. These templates will automatically be rejected.



## What's next

  * Create a [simple configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).
  * Decide if you want to use [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).
  * If you are exposing your configuration to other users, consider [creating a schema](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas).
  * Learn how you can [host templates externally](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/hosting-templates-externally).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
