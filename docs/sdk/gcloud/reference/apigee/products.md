---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/
title: gcloud apigee products \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:12:25.172858+00:00
---

# gcloud apigee products  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee products Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee products - manage Apigee API products 
SYNOPSIS
    

`gcloud apigee products` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage Apigee API products. 

`gcloud apigee products` manipulates API products. These are collections of deployed API resources, combined with quota settings and metadata, used to deliver customized and productized API bundles to the developer community. 

EXAMPLES
     To list all API products in the active Cloud Platform project, run: 
    
    
    [gcloud apigee products list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/list)

To create an API product named ``my-apis`` by answering interactive prompts about its included proxies and access policies, run: 
    
    
    [gcloud apigee products create](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/create) my-apis

To create an API product named ``prod-apis`` that makes every API proxy deployed to the ``prod`` environment publicly available, run: 
    
    
    [gcloud apigee products create](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/create) prod-apis --environments=prod --all-proxies --public-access

To get a JSON object describing an existing API product, run: 
    
    
    [gcloud apigee products describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/describe) PRODUCT_NAME --organization=ORG_NAME --format=json

To add another API proxy to an existing API product, run: 
    
    
    [gcloud apigee products update](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/update) PRODUCT_NAME --add-api=API_NAME

To edit the publicly visible name and description of an API product, run: 
    
    
    [gcloud apigee products update](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/update) PRODUCT_NAME --display-name="New Name" --description="A new description of this product."

To make an existing product publicly visible and automatically allow developers access to it, run: 
    
    
    [gcloud apigee products update](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/update) PRODUCT_NAME --public-access --automatic-approval

To delete an existing API product, run: 
    
    
    [gcloud apigee products delete](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/delete) PRODUCT_NAME

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/create)`
     Create an Apigee API product. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/delete)`
     Delete an Apigee API product. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/describe)`
     Describe an Apigee API product. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/list)`
     List Apigee API products. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/products/update)`
     Update an existing Apigee API product. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha apigee products](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/products)
    
    
    [gcloud beta apigee products](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/products)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
