---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/detect-product/
title: gcloud beta ml vision detect-product \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:39:01.270365+00:00
---

# gcloud beta ml vision detect-product  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/detect-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml vision detect-product Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml vision detect-product - detect products within an image 
SYNOPSIS
    

`gcloud beta ml vision detect-product` `IMAGE_PATH` `--category`=[`CATEGORY`,…] (`--product-set`=`PRODUCT_SET` : `--product-set-location`=`PRODUCT_SET_LOCATION`) [`--bounding-polygon`=`BOUNDING_POLYGON`] [`--filter`=`FILTER`] [`--max-results`=`MAX_RESULTS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` detect products within an image 
EXAMPLES
     To detect product in image 'gs://my-bucket/my-image.jpg' by searching in product set 'my-product-set', in category 'toys', run: 
    
    
    gcloud beta ml vision detect-product gs://my-bucket/my-image.jpg --product-set='my-product-set' --product-set-location=us-east1 --category='toys'

POSITIONAL ARGUMENTS
    

`IMAGE_PATH`
     Path to the image to be analyzed. This can be either a local path or a URL. If you provide a local file, the contents will be sent directly to Google Cloud Vision. If you provide a URL, it must be in Google Cloud Storage format (gs://bucket/object) or an HTTP URL (<http://..>. or https://…) 
REQUIRED FLAGS
    

`--category`=[`CATEGORY`,…]
     Product category to search in. `CATEGORY` must be one of: `apparel`, `homegoods`, `toys`. 
Product set resource - The product set to be searched for similar images. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--product-set` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--product-set`=`PRODUCT_SET`
     ID of the product set or fully qualified identifier for the product set. 

To set the `product-set` attribute: 

  * provide the argument `--product-set` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--product-set-location`=`PRODUCT_SET_LOCATION`
     The location of the product set. 

To set the `location` attribute: 

  * provide the argument `--product-set` on the command line with a fully specified name; 
  * provide the argument `--product-set-location` on the command line. 


OPTIONAL FLAGS
    

`--bounding-polygon`=`BOUNDING_POLYGON`
     Bounding polygon around the areas of interest in the image. If it is not specified, system discretion will be applied. A bounding polygon can be specified by a list of vertices or normalized vertices. A vertex (x, y) represents a 2D point in the image. x, y are integers and are in the same scale as the original image. The normalized vertex coordinates are relative to orginal image and range from 0 to 1. For example, \--bounding-polygon=0.,0.,0.,0.3,0.3,0.,0.3,0.3 specifies a polygon with 4 normalized vertices - (0., 0.), (0., 0.3), (0.3, 0.), (0.3, 0.3). Notice that the decimal point is needed for normalized vertex coordindates. 
`--filter`=`FILTER`
     Filter expression to restrict search results based on product labels. ANDs of ORs of key-value expressions are supported, where expressions within an OR must have the same key. Expressions separated by AND must have different keys. An '=' should be used to connect the key and value. For example, '(color = red OR color = blue) AND brand = Google' is acceptable, but not '(color = red OR brand = Google)' or 'color: red'. 
`--max-results`=`MAX_RESULTS`
     Maximum number of results to be provided. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ml vision detect-product](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-product)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
