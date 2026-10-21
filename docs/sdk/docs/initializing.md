---
url: https://docs.cloud.google.com/sdk/docs/initializing/
title: Initialize the gcloud CLI \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:53:02.560770+00:00
---

# Initialize the gcloud CLI  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/initializing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Initialize the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

After you [install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), you can perform initial setup tasks by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init). The `gcloud init` command performs the following steps: 

  * Authenticates with user account credentials, and then authorizes the gcloud CLI to access Google Cloud resources on your behalf. You can also do this separately with the [`gcloud auth login`](https://docs.cloud.google.com/sdk/docs/authenticate) command.

  * Sets up a gcloud CLI [configuration](https://docs.cloud.google.com/sdk/docs/configurations) and sets core [properties](https://docs.cloud.google.com/sdk/docs/properties) such as the active account, the current project, and if applicable, the default Compute Engine region and zone.




If you've already initialized the gcloud CLI, running `gcloud init` again lets you change existing settings or create a new configuration.

## Initialize the gcloud CLI

To initialize the gcloud CLI:

  1. Run `gcloud init`:
         
         gcloud init

If you're using a remote terminal session, add the `--console-only flag`. This flag provides the URL to the authentication and authorization flow instead of attempting to open it in your default browser. 
         
         gcloud init --console-only

  2. Create or select a configuration if prompted.

For new gcloud CLI installations, `gcloud init` creates a configuration named `default` for you and sets it as the active configuration. If you have existing configurations, `gcloud init` prompts you to choose between the following options: 

     * Re-initialize the active configuration.
     * Switch to another configuration and re-initialize it.
     * Create a new configuration.
  3. Complete the authentication and authorization steps when prompted.

If you have previously authorized access to Google Cloud, you might be prompted to sign in again and grant access in a web browser, or to select an existing account. 

If you used the `--console-only` flag and sign-in is required, copy and paste the provided authorization URL into another browser window and follow the prompts. 

  4. Choose a Google Cloud project if prompted.

If you only have access to one project—including the default project for your user account—`gcloud init` selects it for you. 

Otherwise, you can select a project from a list of projects on which you have the **Owner** , **Editor** , or **Viewer** roles. If you have access to more than 200 projects, you're prompted to enter a project ID, create a new project, or list projects. 

**Note** : If you choose to create a project, you also need to [ enable billing on your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project) to use Google Cloud services. 
  5. Choose a default Compute Engine zone if prompted. If you don't have the Compute Engine API enabled or you already have a default zone in your [ project-level metadata](https://docs.cloud.google.com/compute/docs/metadata), this step is skipped. 




## View configuration properties

To view the properties set through the `gcloud init` command, use the [`gcloud config list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/list) command. The command returns an output similar to the following example:
    
    
    [compute]
    region = us-east1
    zone = us-east1-b
    [core]
    account = dana@example.com
    disable_usage_reporting = False
    project = example-project
    

## What's next

  * To learn more about authentication for the gcloud CLI, see [Authentication for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate).

  * To learn more about authorizing Application Default Credentials (ADC) for Cloud Client Libraries and Google API Client Libraries, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

  * To learn more about managing configurations, see [Manage gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/configurations).

  * To learn more about managing properties, see [Manage gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
