---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/product-search/images/create/
title: gcloud beta ml vision product-search images create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:39:02.893826+00:00
---

# gcloud beta ml vision product-search images create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/product-search/images/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml vision product-search images create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml vision product-search images create - create a reference image 
SYNOPSIS
    

`gcloud beta ml vision product-search images create` (`REFERENCE_IMAGE` : `--location`=`LOCATION` `--product`=`PRODUCT`) `--storage-location`=`STORAGE_LOCATION` [`--bounding-polygon`=[`normalized-vertices`=`NORMALIZED-VERTICES`],[`vertices`=`VERTICES`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` create a reference image. 
EXAMPLES
     To create a reference image 'my-image' in product 'my-product' in the location 'us-east1' from image of 'gs://my-bucket/image.jpg' with two bounding polygons, run: 
    
    
    gcloud beta ml vision product-search images create my-image --location=my-location --product=my-product --storage-location=gs://my-bucket/image.jpg --flags-file=my-flags.yaml

The content of 'my-flags.yaml' is as following: 
    
    
    - --bounding-polygon:
        vertices:
          - {x: 0, y: 0}
          - {x: 0, y: 10}
          - {x: 10, y: 0}
          - {x: 10, y: 10}
    - --bounding-polygon:
        normalized-vertices:
          - {x: 0.8, y: 0.8}
          - {x: 0.8, y: 1}
          - {x: 1, y: 0.8}
          - {x: 1, y: 1}

POSITIONAL ARGUMENTS
    

Reference image resource - Reference image to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `reference_image` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REFERENCE_IMAGE`
     ID of the reference image or fully qualified identifier for the reference image. 

To set the `reference_image` attribute: 

  * provide the argument `reference_image` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of reference image. 

To set the `location` attribute: 

  * provide the argument `reference_image` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--product`=`PRODUCT`
     The ID of product. 

To set the `product` attribute: 

  * provide the argument `reference_image` on the command line with a fully specified name; 
  * provide the argument `--product` on the command line. 


REQUIRED FLAGS
    

`--storage-location`=`STORAGE_LOCATION`
     The Google Cloud Storage URI of the reference image. The URI must start with 'gs://'. 
OPTIONAL FLAGS
    

`--bounding-polygon`=[`normalized-vertices`=`NORMALIZED-VERTICES`],[`vertices`=`VERTICES`]
     Bounding polygon around the areas of interest in the reference image. If this field is empty, the system will try to detect regions of interest. This flag is repeatable to specify multiple bounding polygons. At most 10 bounding polygons will be used. 

A bounding polygon can be specified by a list of vertices or normalized vertices or both. A vertex (x, y) represents a 2D point in the image. x, y are integers and are in the same scale as the original image. The normalized vertex coordinates are relative to original image and range from 0 to 1. 

Because of the complexity of this flag, it should be specified with the `--flags-file`. See $ [gcloud topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) for details. See the examples section for how to use `--bounding-polygon` in `--flags-file`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ml vision product-search images create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/product-search/images/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
