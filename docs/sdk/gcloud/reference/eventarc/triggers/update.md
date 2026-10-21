---
url: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update/
title: gcloud eventarc triggers update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:20:46.751180+00:00
---

# gcloud eventarc triggers update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/triggers/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud eventarc triggers update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud eventarc triggers update - update an Eventarc trigger 
SYNOPSIS
    

`gcloud eventarc triggers update` (`TRIGGER` : `--location`=`LOCATION`) [`--async`] [`--event-data-content-type`=`EVENT_DATA_CONTENT_TYPE`] [`--event-filters`=[`ATTRIBUTE`=`VALUE`,…]] [`--event-filters-path-pattern`=[`ATTRIBUTE`=`PATH_PATTERN`,…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--clear-max-retry-attempts` | `--max-retry-attempts`=`MAX_RETRY_ATTEMPTS`] [`--clear-service-account` | `--service-account`=`SERVICE_ACCOUNT`] [`--destination-gke-namespace`=`DESTINATION_GKE_NAMESPACE` `--destination-gke-service`=`DESTINATION_GKE_SERVICE` `--clear-destination-gke-path` | `--destination-gke-path`=`DESTINATION_GKE_PATH` | `--destination-run-region`=`DESTINATION_RUN_REGION` `--destination-run-service`=`DESTINATION_RUN_SERVICE` `--clear-destination-run-path` | `--destination-run-path`=`DESTINATION_RUN_PATH` | `--destination-workflow`=`DESTINATION_WORKFLOW` `--destination-workflow-location`=`DESTINATION_WORKFLOW_LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an Eventarc trigger. 
EXAMPLES
     To update the trigger ``my-trigger`` by setting its destination Cloud Run service to ``my-service``, run: 
    
    
    gcloud eventarc triggers update my-trigger --destination-run-service=my-service

POSITIONAL ARGUMENTS
    

Trigger resource - The trigger to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `trigger` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TRIGGER`
     ID of the trigger or fully qualified identifier for the trigger. 

To set the `trigger` attribute: 

  * provide the argument `trigger` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the Eventarc trigger, which should be either ``global`` or one of the supported regions. Alternatively, set the [eventarc/location] property. 

To set the `location` attribute: 

  * provide the argument `trigger` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--event-data-content-type`=`EVENT_DATA_CONTENT_TYPE`
     Depending on the event provider, you can specify the encoding of the event data payload that will be delivered to your destination, to either be encoded in ``application/json`` or ``application/protobuf``. The default encoding is ``application/json``. Note that for custom sources or third-party providers, or for direct events from Cloud Pub/Sub, this formatting option is not supported. 
`--event-filters`=[`ATTRIBUTE`=`VALUE`,…]
     The trigger's list of filters that apply to CloudEvents attributes. This flag can be repeated to add more filters to the list. Only events that match all these filters will be sent to the destination. The filters must include the ``type`` attribute, as well as any other attributes that are expected for the chosen type. 
`--event-filters-path-pattern`=[`ATTRIBUTE`=`PATH_PATTERN`,…]
     The trigger's list of filters in path pattern format that apply to CloudEvent attributes. This flag can be repeated to add more filters to the list. Only events that match all these filters will be sent to the destination. Currently, path pattern format is only available for the resourceName attribute for Cloud Audit Log events. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud eventarc triggers update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud eventarc triggers update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
The retry policy configuration for the trigger. Can only be set for Cloud Run destinations. At most one of these can be specified: 

`--clear-max-retry-attempts`
     Clear the maximum number of delivery attempts for the trigger. 
`--max-retry-attempts`=`MAX_RETRY_ATTEMPTS`
     The maximum number of delivery attempts. The only valid value is 1. 
At most one of these can be specified: 

`--clear-service-account`
     Clear the IAM service account associated with the trigger. 
`--service-account`=`SERVICE_ACCOUNT`
     The IAM service account email associated with the trigger. 
Flags for updating the destination to which events should be sent. 

At most one of these can be specified: 

Flags for updating a GKE service destination. 
`--destination-gke-namespace`=`DESTINATION_GKE_NAMESPACE`
     Namespace that the destination GKE service is running in. If not specified, the ``default`` namespace is used. 
`--destination-gke-service`=`DESTINATION_GKE_SERVICE`
     Name of the destination GKE service that receives the events for the trigger. 
At most one of these can be specified: 

`--clear-destination-gke-path`
     Clear the relative path on the destination GKE service to which the events for the trigger should be sent. 
`--destination-gke-path`=`DESTINATION_GKE_PATH`
     Relative path on the destination GKE service to which the events for the trigger should be sent. Examples: ``/route``, ``route``, ``route/subroute``. 
Flags for updating a Cloud Run fully-managed resource destination. 
`--destination-run-region`=`DESTINATION_RUN_REGION`
     Region in which the destination Cloud Run service can be found. If not specified, it is assumed that the service is in the same region as the trigger. 
`--destination-run-service`=`DESTINATION_RUN_SERVICE`
     Name of the Cloud Run fully-managed service that receives the events for the trigger. The service must be in the same project as the trigger. 
At most one of these can be specified: 

`--clear-destination-run-path`
     Clear the relative path on the destination Cloud Run service to which the events for the trigger should be sent. 
`--destination-run-path`=`DESTINATION_RUN_PATH`
     Relative path on the destination Cloud Run service to which the events for the trigger should be sent. Examples: ``/route``, ``route``, ``route/subroute``. 
Flags for updating a Cloud Workflows destination. 
`--destination-workflow`=`DESTINATION_WORKFLOW`
     ID of the workflow that receives the events for the trigger. The workflow must be in the same project as the trigger. 
`--destination-workflow-location`=`DESTINATION_WORKFLOW_LOCATION`
     Location that the destination workflow is running in. If not specified, it is assumed that the workflow is in the same location as the trigger. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
