---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites/
title: Before you begin \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:53.720797+00:00
---

# Before you begin  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Before you can set up and deploy API proxies with Apigee, you must meet the following prerequisites:

Done? | Prerequisite | Description  
---|---|---  
| **Google Cloud billing account** | You must have a Google Cloud account with active billing. This applies whether you want to provision a production or evaluation organization. While an evaluation organization does not itself incur any charges against your account, some APIs used by the organization do; for example, the Compute Engine API.  **Note:** If you provision an eval org, the organization that you create will expire after 60 days. At that time, the organization will be deleted.For more information, see [Create a new billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account#create_a_new_billing_account).  
| **Google Cloud project** |  Create a new Google Cloud project. When you do, be sure to note the project ID and project number. You'll need the ID and number later in this process. **Note:** If you are an existing Apigee paid subscription customer with an existing Apigee organization provisioned in a Google Cloud project, and you want to create an org in a new Google Cloud project, contact Apigee sales to enable your subscription entitlement to enable Apigee for the new project. If the project is not enabled, you will get an error when you try to create an organization in the new project.Project names must adhere to the following guidelines:

  * Start with a lower-case letter. For example, `my-org` is OK, but `_my-org` is not.
  * Include the following characters only: 
        
        [a-z]   Lower-case letters
        [0-9]   Numbers
        -       Hyphens

For example:
        
        VALID NAMES        INVALID NAMES
        my-project         my_project        No underscores
        first-project      1st-project       Cannot start with a number
        google-project     project@google    No special chars except hyphens


For more information, see [Creating a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).  
| **Software** | Install the following software on your administrative machine:

  * [Google Cloud SDK](https://docs.cloud.google.com/sdk/install) (required for command line provisioning steps)
  * [`curl`](https://curl.haxx.se/) (recommended)

  
| **Permissions** | The individual who provisions Apigee must have or be granted certain [Google Cloud IAM permissions](https://docs.cloud.google.com/iam/docs/permissions-reference) to be successful. For details, see [About Apigee provisioning permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[project ID]: A unique, user-assigned ID that can be used by Google APIs. If
  you do not specify a project ID during project creation, a project ID will be generated
  automatically.
