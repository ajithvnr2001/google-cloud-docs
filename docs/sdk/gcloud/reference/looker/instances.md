---
url: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/
title: gcloud looker instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:33:04.852602+00:00
---

# gcloud looker instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud looker instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud looker instances - manage Looker instances 
SYNOPSIS
    

`gcloud looker instances` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create an instance with the name `my-looker-instance`, with an edition of "LOOKER_CORE_STANDARD", run: 
    
    
    [gcloud looker instances create](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/create) my-looker-instance --oauth-client-id='looker' --oauth-client-secret='looker' --edition="core-standard" --async

Note: It is `recommended` that the `--async` argument is provided when creating a Looker instance. 

To delete an instance with the name `my-looker-instance`, run: 
    
    
    [gcloud looker instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/delete) my-looker-instance --async

To display the details for an instance with name `my-looker-instance`, run: 
    
    
    [gcloud looker instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/describe) my-looker-instance

To restart an instance with the name `my-looker-instance`, run: 
    
    
    [gcloud looker instances restart](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/restart) my-looker-instance --async

To update an instance with the name `my-looker-instance`, run: 
    
    
    [gcloud looker instances update](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update) my-looker-instance --async

To restore a backup with id of `7e504e66-c389-4d8d` that belongs to an instance named `my-looker-instance`, in the region `us-central1`, run: 

$ [gcloud looker instances restore](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/restore) my-looker-instance \
    
    
    --backup="7e504e66-c389-4d8" --region="us-central1" --async

To export an instance with the name `my-looker-instance`, run: 
    
    
    [gcloud looker instances export](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/export) my-looker-instance --target-gcs-uri='gs://bucketName/folderName' --kms-key='projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key'

To import an instance with the name `my-looker-instance`, run: 
    
    
    [gcloud looker instances import](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/import) my-looker-instance --source-gcs-uri='gs://bucketName/folderName'

To list all the instances, run: 
    
    
    [gcloud looker instances list](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/create)`
     Create a Looker instance. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/delete)`
     Delete a Looker instance. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/describe)`
     Show metadata for a Looker instance. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/export)`
     Export a Looker instance. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/import)`
     Import a Looker instance. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/list)`
     List Looker instances. 
`[restart](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/restart)`
     Restart a Looker instance. 
`[restore](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/restore)`
     Restore a Looker instance from a backup. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/update)`
     Update a Looker instance. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha looker instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/looker/instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
