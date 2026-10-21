---
url: https://docs.cloud.google.com/resource-manager/docs/best-practices-labels/
title: Best practices for labels \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:29.144129+00:00
---

# Best practices for labels  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/best-practices-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Best practices for labels Stay organized with collections  Save and categorize content based on your preferences. 

This document provides guidance on how to design an effective label strategy for your organization. Before you start creating labels, here are some general principles you can use when you organize your Google Cloud resources using labels.

## General principles for labels

### Always use labels

Although labels aren't mandatory, they are helpful in organizing and managing your Google Cloud resources. Labels can be used to track costs and identify resources. When you use labels for your resources, remember to follow strict labeling guidelines. We recommend that you create a formal labeling policy that aligns with key stakeholders in the organization. The example table shows what an organization-wide labeling policy looks like.

### Apply labels programmatically for consistency

When possible, apply labels programmatically. Tools such as Script and Terraform enable you to automate the label creation process and help enforce the labeling policy. These tools ensure that labels are applied consistently across all your resources. Use a case-sensitive format for labeling and apply it consistently across all resources.

### Standardize labels

Use a consistent and standard set of labels for all your resources. This makes it easier to search, filter, and manage your resources. To simplify your label strategy try not to use more than ten labels. Align your labels based on how you want to report costs. Consider using a standard set of label keys and values that work best for your organization. Your labels can cover business use cases such as environment, data-classification, cost-center, team, component, application, and compliance.

Note that standardizing on and adhering to a labeling policy is crucial for centrally-managed labels. Product teams and departments can also add custom labels to resources to share team-specific information. For more information, see Apply non-standard labels.

Here's an example of how you can define a standard set of values for each of the keys:

  * Environment: `prod/dev/staging`
  * Data-classification: `public/internal-only/confidential/restricted/na`
  * Cost center: `c23543`
  * Team: `shopping-cart`
  * Component: `frontend/cache/backend/database`
  * Application: `shopping-cart-payments`
  * Compliance: `pci-hipaa`



### Avoid confidential information

Protecting personally identifiable information (PII) is critical for security. Avoid storing PII or other confidential information in your labels.

### Apply non-standard labels

Although adhering to a label policy is crucial, labels can also be used to share information that is specific to a product team or department. In such a scenario, providing resource owners of individual teams the option to apply non-standard labels for each resource can help provide more context about the resource. This makes it easier to search, filter, and share information specific to these product teams or departments. For example, a single resource can have a set of standard labels such as `environment:prod`, `data-classification:restricted`, `cost-center:c23543`, `team:shopping-cart`, `app:shopping-cart-payments`, `component:database`, `compliance: pci`. The resource owner can add non-standard labels such as `version:5.0.1` and `replica:primary` to indicate the version of the database cluster and the node's replication status.

### Consider change implications

Your labeling strategy is likely to change in times of evolving business requirements. Be aware of the implications that these changes may have. For example, the addition of new cost centers, microservices, or new tools can impact your labeling strategy.

## Label naming scheme and pattern

Every organization has its own way of organizing resources. You can use labels to categorize the resources in your hierarchy in multiple ways, helping users to filter for the resources they need. When defining your label naming scheme, consider the following:

  * Environment, cost center, team, component, applications, compliance, and ownership associated with the resource.
  * Data classification of any data stored in the system. This is only applicable to stateful systems.
  * Labels that need to be applied at the specific resource level like Compute Engine, Cloud Storage bucket or at the project.
  * Flexibility to use optional labels, as needed, to provide more information on resources.



## Label encoding and supported characters

All key and value characters must use UTF-8 encoding. International characters are allowed. Keys must start with a lowercase letter or international character. Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.

## Example of defining labels

To define labels, here are some attributes that you need to keep in mind.

Field | Description  
---|---  
Label key | The label key is a unique identifier for a label. It must be a string with a minimum length of 1 character and a maximum length of 63 characters. The key cannot be empty. You can use a standard set of label keys that work best for your organization that cover business use cases like `environment`, `data-classification`, `cost-center`, `team`, `component`, `application` and `compliance`.  
Label value | The label value is the data associated with the key. It can be a string, number, or Boolean value. As a best practice, consider defining a set of values for each label key. This can help teams select and assign appropriate values for each key. For example, an `environment` key can have values such as `prod`, `staging`, `dev` or `tools`.  
Stakeholder | Identify the department which needs the label key for filtering resources or creating reports. For example, a Finance department in an organization would like to know the cost of running the `prod` environment. They would use the label _key:value_ pair `environment:prod`.  
Target resource | For each label, consider defining a target Google Cloud resource where the label _key:value_ pair should be applied. For example, the label key `environment` needs to be on each Google Cloud resource in your organization's production environment.  
Exception | Consider defining which label keys are mandatory on all resources and which keys are optional to apply. In the [example table](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels#example_labels_table), there are some label `key:value` pairs that are optional such as `environment:tools`. The label key `altostrat-team` can be considered optional when the label `altostrat-environment` has the label value set to `tools`.  
  
In the following label example, _altostrat_ corresponds to the name of the enterprise.

Label key | Label value | Stakeholder | Target resource | Exception  
---|---|---|---|---  
altostrat-environment | prod, sb1, staging, dev, tools | Finance | Google Cloud resources | No  
altostrat-data-classification | public, internal-only, confidential, restricted, na | Security | Buckets, databases, persistent disks with Compute Engine | No  
altostrat-cost-center | fin-us, mkt-eu, it-jp | Finance | Google Cloud resources | sandbox-folder  
altostrat-team | shopping-cart | Team lead | Google Cloud resources | Non-production environments, non-critical components  
altostrat-component | frontend, cache, application, database | Finance | Google Cloud resources | Optional  
altostrat-app | shopping-cart-payment | Finance | Google Cloud resources | No. There's an exception for multi-tenant resources where there is no 1:1 mapping with the application.  
altostrat-compliance | pci, hipaa | Security | Google Cloud resources | Optional  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
