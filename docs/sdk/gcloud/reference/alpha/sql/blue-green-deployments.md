---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/
title: gcloud alpha sql blue-green-deployments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:27.876297+00:00
---

# gcloud alpha sql blue-green-deployments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql blue-green-deployments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql blue-green-deployments - provide commands for managing Cloud SQL blue-green deployments 
SYNOPSIS
    

`gcloud alpha sql blue-green-deployments` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Blue-green deployment is a strategy that minimizes database downtime when you make changes, like major version upgrades, by copying a production environment to a separate, synchronized staging environment. 

With blue-green deployments, you can make changes to a staging environment-the green environment-without affecting the production environment-the blue environment. When you're ready, you can switch over with low downtime, promoting the staging environment to be the new production environment. 

These commands help you manage the lifecycle of creating the green environment, testing, switching over, and cleaning up old resources in Cloud SQL. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/create)`
     `(ALPHA)` Creates a Cloud SQL blue-green deployment. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/delete)`
     `(ALPHA)` Deletes a Cloud SQL blue-green deployment. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/describe)`
     `(ALPHA)` Retrieves information about a Cloud SQL blue-green deployment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/list)`
     `(ALPHA)` Lists Cloud SQL blue-green deployments. 
`[switchover](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/switchover)`
     `(ALPHA)` Performs switchover for a Cloud SQL blue-green deployment. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta sql blue-green-deployments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/blue-green-deployments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
