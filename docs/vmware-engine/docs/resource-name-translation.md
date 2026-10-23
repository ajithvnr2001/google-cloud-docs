---
url: https://docs.cloud.google.com/vmware-engine/docs/resource-name-translation/
title: Resource Name Translation \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:52.534736+00:00
---

# Resource Name Translation  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/resource-name-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resource Name Translation

Currently, Google Cloud VMware Engine resource names for existing private clouds don't follow a standardized naming convention. However, in order to support new features in the future, Google Cloud VMware Engine will convert the resource names for private clouds to a standardized format that is more consistent with Google Cloud. Specifically, this resource name translation will make minor changes to the names of resources in your project, such as:

  * Changing capital letters to lowercase
  * Changing white space to hyphens 



While name translation has no impact to your private cloud, if you have custom scripts or automations that refer to private cloud resources, you will need to update the scripts with the new names. For example, a resource named _Customer Private Cloud 03_ will need the new translated name of _customer-private-cloud-03_.

**Note:** Resource name changes are permanent and can't be changed once created.

## Making your name translation selection

Before you can access the Google Cloud CLI or VMware Engine API, you will be prompted to make your name translation selection in the VMware Engine portal if you have resources that need translation. There are three options for name translation:

  1. No choice is made
  2. Opting in
  3. Opting out



When no choice is made, the following message is displayed:

"Resources in your project will need to have a name translation to allow access to the Google Cloud CLI and Google VMware Engine API. This name translation will take place in 2 weeks. Changing the resource names may impact scripts or workflows that referenced the resource name. Click here for **details**."

If you choose to opt in, the following message is displayed:

"USERNAME has selected to translate the resource names in your project. This is required to allow access to the Google Cloud CLI and Google VMware Engine API. The name translation will take place on DATE. Changing the resource names may impact scripts or workflows that reference the resource name. Click here for **details**."

If you choose to opt out, the following message is displayed:

"USERNAME has selected NOT to translate the resource names in your project. This is required to allow access to the Google Cloud CLI and Google VMware Engine API. You have until DATE to change that decision. Changing the resource names may impact scripts or workflows that reference the resource name. Click here for **details**."

Clicking **details** at the end of each message displays a list of existing resource names and proposed new names.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
