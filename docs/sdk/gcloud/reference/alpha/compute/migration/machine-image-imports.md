---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/
title: gcloud alpha compute migration machine-image-imports \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:42:28.934135+00:00
---

# gcloud alpha compute migration machine-image-imports  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute migration machine-image-imports Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute migration machine-image-imports - imports machine images to Google Compute Engine from Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha compute migration machine-image-imports` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud migration vms machine-image-imports provides a more robust and better supported method for importing machine images to Google Compute Engine. Other image-related operations (for example, list) can be done using gcloud compute images, as usual. 

The commands use VM Migration API which supports importing of a machine image from a Google Cloud Storage file (gs://…) to a target project. VM Migration API must be enabled in your project. 

`gcloud migration vms machine-image-imports create` creates a machine Image Import resource with a nested Image Import Job resource. The Image Import Job resource tracks the machine image import progress. After the Image Import Job completes, successfully or otherwise, there's no further use for the Image Import resource. 

The machine image is imported to a Google Cloud Project, desginated by the Target Project resource. To get a list of Target Projects, run the gcloud alpha migration vms target-projects list command. Use the Google Cloud console to add target project resources. For information on adding target projects, see <https://cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/target-project>. 

A project can support up to a certain number of Image Import resources per project. Hence it's recommended to delete an Image Import resource after the Image Import Job is complete to avoid reaching the Image Import resources limit. Deletion of Image Import resource does not affect the imported machine image. For more information about the image import resource, see <https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import>. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/create)`
     `(ALPHA)` import machine images to Google Compute Engine. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/delete)`
     `(ALPHA)` delete an Image Import resource. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/describe)`
     `(ALPHA)` describe an Image Import. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/migration/machine-image-imports/list)`
     `(ALPHA)` list Image Imports. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud compute migration machine-image-imports](https://docs.cloud.google.com/sdk/gcloud/reference/compute/migration/machine-image-imports)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
