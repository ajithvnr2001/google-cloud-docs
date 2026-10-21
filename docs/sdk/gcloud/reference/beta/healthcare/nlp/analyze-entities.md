---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/nlp/analyze-entities/
title: gcloud beta healthcare nlp analyze-entities \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:41.465299+00:00
---

# gcloud beta healthcare nlp analyze-entities  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/nlp/analyze-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta healthcare nlp analyze-entities Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta healthcare nlp analyze-entities - find and analyze medical entities in a document 
SYNOPSIS
    

`gcloud beta healthcare nlp analyze-entities` [`LOCATION`] `--document-content`=`DOCUMENT_CONTENT` `--nlp-service`=`NLP_SERVICE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Find and analyze medical entities in a document. 
EXAMPLES
     To inspect input text for medical concepts and relations run: 
    
    
    gcloud beta healthcare nlp analyze-entities --document-content="Example" --nlp-service="projects/my-project/locations/my-location/services/nlp"

POSITIONAL ARGUMENTS
    

Nlp resource - Cloud Healthcare NL API service be evaluated. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `location` on the command line with a fully specified name; 
  * set the property `healthcare/location` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`LOCATION`]
     ID of the nlp or fully qualified identifier for the nlp. 

To set the `location` attribute: 

  * provide the argument `location` on the command line; 
  * set the property `healthcare/location`. 


REQUIRED FLAGS
    

`--document-content`=`DOCUMENT_CONTENT`
     The input text to be analyzed. 
`--nlp-service`=`NLP_SERVICE`
     The NLP Service name to be used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `healthcare/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/healthcare>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha healthcare nlp analyze-entities](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare/nlp/analyze-entities)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
