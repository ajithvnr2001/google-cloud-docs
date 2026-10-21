---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/product-search/products/update/
title: gcloud alpha ml vision product-search products update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:47:58.045959+00:00
---

# gcloud alpha ml vision product-search products update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/product-search/products/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ml vision product-search products update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ml vision product-search products update - update a product 
SYNOPSIS
    

`gcloud alpha ml vision product-search products update` (`PRODUCT` : `--location`=`LOCATION`) [`--add-product-labels`=[`KEY`=`VALUE`,…]] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--clear-product-labels` | `--remove-product-labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` update a product. 
EXAMPLES
     To change the display name to 'new-display--name', and description to 'new-description' of product 'my-product' in location 'us-east1', run: 
    
    
    gcloud alpha ml vision product-search products update my-product --location=us-east1 --display-name='new-display-name' --description='new-description'

To add labels 'color=blue' to and remove 'weight=10lbs' from product 'my-product' in location 'us-east1', run: 
    
    
    gcloud alpha ml vision product-search products update my-product --location=us-east1 --add-product-labels='color=blue' --remove-product-labels='weight=10lbs'

To clear all labels from product 'my-product' in location 'us-east1', run: 
    
    
    gcloud alpha ml vision product-search products update my-product --location=us-east1 --clear-product-labels

POSITIONAL ARGUMENTS
    

Product resource - The product to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `product` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PRODUCT`
     ID of the product or fully qualified identifier for the product. 

To set the `product` attribute: 

  * provide the argument `product` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of product. 

To set the `location` attribute: 

  * provide the argument `product` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--add-product-labels`=[`KEY`=`VALUE`,…]
     List of product labels to add. If a label already exists, it is silently ignored. 

For example, to add the product labels 'foo=baz' and 'baz=qux': 
    
    
    gcloud alpha ml vision product-search products update --add-product-labels='foo=baz,baz=qux'

To change the product label 'foo=baz' to 'foo=qux': 
    
    
    gcloud alpha ml vision product-search products update --remove-product-labels='foo=baz' --add-product-labels='foo-qux'

`--description`=`DESCRIPTION`
     An optional description of this product. It can be up to 4096 characters long. 
`--display-name`=`DISPLAY_NAME`
     The display name of this product. It must not be empty and can be up to 4096 characters long. 
At most one of these can be specified: 

`--clear-product-labels`
     Remove all product labels. If `--add-product-labels` is also specified, then `--clear-product-labels` is applied first. 

For example, to remove all product labels: 
    
    
    gcloud alpha ml vision product-search products update --clear-product-labels

To set the product labels to exactly "foo" and "baz": 
    
    
    gcloud alpha ml vision product-search products update --clear-product-labels --add-product-labels='foo=bar,baz=qux'

`--remove-product-labels`=[`KEY`=`VALUE`,…]
     List of product labels to remove. If `--add-product-labels` is also specified, then `--remove-product-labels` is applied first. If a label does not exist it is silently ignored. Because each key can be associated with multiple values, both key and value need to be specified to remove the product label. 

For example, to remove the product labels 'foo=baz' and 'baz=qux': 
    
    
    gcloud alpha ml vision product-search products update --remove-product-labels='foo=baz,baz=qux'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta ml vision product-search products update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/product-search/products/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
