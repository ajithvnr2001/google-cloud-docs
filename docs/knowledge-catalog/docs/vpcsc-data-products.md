---
url: https://docs.cloud.google.com/knowledge-catalog/docs/vpcsc-data-products/
title: Use VPC Service Controls with data products \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:50.024163+00:00
---

# Use VPC Service Controls with data products  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/vpcsc-data-products/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use VPC Service Controls with data products Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure VPC Service Controls to secure your data products.

Use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to prevent data exfiltration and ensure that communication between data products, data assets, and users stays within authorized perimeters.

A [data product](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview) is a logical grouping of resources (data assets) that can span multiple projects. When your projects belong to different VPC Service Controls perimeters, you must configure ingress and egress rules to allow the Dataplex API to manage resources and metadata.

## Before you begin

  * Familiarize yourself with the [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Understand the [data products concepts](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Ensure you have the necessary permissions to [manage VPC Service Controls perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) and [Knowledge Catalog resources](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).



## Service perimeter rules for creating data products

The following projects define the communication boundaries required to create a data product across service perimeters:

  * **Project R (Caller):** the project where the user, service account, or application resides that initiates the create request.

  * **Project E (Data product):** the project that hosts the data product resource.




![An illustration showing two service perimeters. Perimeter 1 contains
  Project R \(Caller\) and perimeter 2 contains Project E \(Data product\).](https://docs.cloud.google.com/static/knowledge-catalog/images/vpcsc-create-data-products.png)

To create a data product in a different project than your caller project, configure the following ingress and egress rules:

Project | Rule required  
---|---  
**Project R** | Egress rule for **Project E**  
**Project E** | Ingress rule for **Project R**  
  
## Service perimeter rules for managing data assets

When you manage data assets (such as adding a BigQuery table to a data product), the architecture involves three distinct project roles:

  * **Project R (Caller):** the project initiating the asset management request.

  * **Project D (Data product):** the project hosting the data product that groups the assets. An asset in a data product is a pointer to a physical data resource, such as a BigQuery dataset, table, or view. A data product can contain one or more assets.

  * **Project S (Source resource):** the project where the actual data resource is located.




![An illustration showing three service perimeters. Perimeter 1 contains
  Project R \(Caller\), perimeter 2 contains Project D \(Data product\), and
  perimeter 3 contains Project S \(Source resource\).](https://docs.cloud.google.com/static/knowledge-catalog/images/vpcsc-manage-data-assets.png)

When you add or manage a data asset that resides in a different project than the data product, you must bridge the communication between all three projects by configuring the following ingress and egress rules:

Project | Rules required  
---|---  
**Project R** | Egress rule for **Project D**  
Egress rule for **Project S**  
**Project D** | Ingress rule for **Project R**  
Egress rule for **Project S**  
**Project S** | Ingress rule for **Project R**  
Ingress rule for **Project D**  
  
## Service perimeter rules for adding aspects and metadata to a data product

The following projects define the communication boundaries required to attach metadata and aspects to a data product across service perimeters:

  * **Project R (Caller):** the project initiating the request to attach an aspect.

  * **Project D (Data product):** the project hosting the data product receiving the aspect.

  * **Project A (Aspect type):** the project where the specific aspect type (the metadata schema) is defined and stored.




![An illustration showing three service perimeters. Perimeter 1 contains
  Project R \(Caller\), perimeter 2 contains Project D \(Data product\), and
  perimeter 3 contains Project A \(Aspect type\).](https://docs.cloud.google.com/static/knowledge-catalog/images/vpcsc-add-aspects.png)

To attach aspects when these projects reside in separate perimeters, configure the following ingress and egress rules:

Project | Rules required  
---|---  
**Project R** | Egress rule for **Project D**  
Egress rule for **Project A**  
**Project D** | Ingress rule for **Project R**  
Egress rule for **Project A**  
**Project A** | Ingress rule for **Project R**  
Ingress rule for **Project D**  
  
## Service perimeter rules for consuming data products

For data product consumers to access data products protected by VPC Service Controls, you must allowlist the consumer project or the specific user identities. To grant this access to data product consumers, configure ingress rules in the data product's service perimeter.

## Limitations

  * Data products don't support method-based rules. To ensure functionality, you must allow all methods (`*`) for the `dataplex.googleapis.com` service in your [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). For example:
        
        ingressTo:
        operations:
        - methodSelectors:
          - method: '*'
          serviceName: dataplex.googleapis.com
        resources:
        - projects/PROJECT_ID
        

  * If your underlying BigQuery resources are protected by service perimeters, you must configure ingress and egress rules for the `bigquery.googleapis.com` service. For example:
        
        ingressTo:
        operations:
        - methodSelectors:
          - method: '*'
          serviceName: bigquery.googleapis.com
        resources:
        - projects/PROJECT_ID
        

**Note:** Ingress and egress rules for BigQuery aren't required when you are only creating a data product.



## What's next

  * Learn more about [data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Understand the [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
