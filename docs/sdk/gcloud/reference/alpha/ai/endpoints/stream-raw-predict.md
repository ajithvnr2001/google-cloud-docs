---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/stream-raw-predict/
title: gcloud alpha ai endpoints stream-raw-predict \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:20.899828+00:00
---

# gcloud alpha ai endpoints stream-raw-predict  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/stream-raw-predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai endpoints stream-raw-predict Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai endpoints stream-raw-predict - run Vertex AI online stream raw prediction 
SYNOPSIS
    

`gcloud alpha ai endpoints stream-raw-predict` (`ENDPOINT` : `--region`=`REGION`) `--request`=`REQUEST` [`--http-headers`=[`HEADER`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha ai endpoints stream-raw-predict` sends a stream raw prediction request to a Vertex AI endpoint. The request can be given on the command line or read from a file or stdin. 
EXAMPLES
     To predict against an endpoint ``123`` under project ``example`` in region ``us-central1``, reading the request from the command line, run: 
    
    
    gcloud alpha ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --request='{
        "instances": [
          { "values": [1, 2, 3, 4], "key": 1 },
          { "values": [5, 6, 7, 8], "key": 2 }
        ]
      }'

If the request body was in the file ``input.json``, run: 
    
    
    gcloud alpha ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --request=@input.json

To send the image file ``image.jpeg`` and set the `content type`, run: 
    
    
    gcloud alpha ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --http-headers=Content-Type=image/jpeg --request=@image.jpeg

POSITIONAL ARGUMENTS
    

Endpoint resource - The endpoint to do online stream raw prediction. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `name` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the endpoint. 

To set the `region` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--request`=`REQUEST`
     The request to send to the endpoint. 

If the request starts with the letter '`@`', the rest should be a file name to read the request from, or '`@-`' to read from `stdin`. If the request body actually starts with '`@`', it must be placed in a file. 

If required, the `Content-Type` header should also be set appropriately, particularly for binary data. 

OPTIONAL FLAGS
    

`--http-headers`=[`HEADER`=`VALUE`,…]
     List of header and value pairs to send as part of the request. For example, to set the `Content-Type` and `X-Header`: 
    
    
    --http-headers=Content-Type="application/json",X-Header=Value

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai endpoints stream-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-raw-predict)
    
    
    [gcloud beta ai endpoints stream-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
