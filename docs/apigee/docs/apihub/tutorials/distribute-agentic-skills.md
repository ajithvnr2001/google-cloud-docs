---
url: https://docs.cloud.google.com/apigee/docs/apihub/tutorials/distribute-agentic-skills/
title: Distribute agentic skills with API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:08.057112+00:00
---

# Distribute agentic skills with API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/tutorials/distribute-agentic-skills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Distribute agentic skills with API hub Stay organized with collections  Save and categorize content based on your preferences. 

As AI agents extend their capabilities through retrievable bundles of instructions, organizations face a new operational challenge to distribute these agentic skills safely at scale. Current workarounds lack centralized auditing, security, and unified discovery.

Because skills resemble standard API specs, you can use [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) as the catalog and authority for these skills. API hub indexes and serves the manifests while delegating storage of the zipped skill contents to Cloud Storage.

By combining API hub and Cloud Storage, you can establish an enterprise skill registry with the following capabilities:

  * **Centralized discovery:** A single directory to register and search skills using attributes or natural language.
  * **Fine-grained governance:** Use your existing Identity and Access Management rules to control who can publish or consume skills.
  * **Security:** Ensure skills are signed and verified before execution, preventing unauthorized alterations.
  * **Observability:** Every skill update or registration is automatically logged in Cloud Audit Logs.



This tutorial describes how to use two open-source skills, `skill-finder` and `skill-publisher`, to turn API hub into a skills registry. You can find samples and files for this tutorial on [Apigee's GitHub](https://github.com/apigee/devrel/tree/main/references/apigee-skills-serving#apigee-skills-serving) repository.

## Architecture components

  * **API hub** : Indexes skill manifest metadata and exposes search filters.
  * **Cloud Storage** : Stores the zipped, signed skill packages (`.skill` archives) in a secure, replicated storage bucket.
  * **`skill-finder`** : A consumer-side client utility that runs on the agent. It queries API hub, verifies the Ed25519 signature of a package against a local trust root, and installs the files into the local runtime skills directory.
  * **`skill-publisher`** : An author-side pipeline utility. It compresses a local skill directory, signs the manifest, uploads the package to Cloud Storage, and registers the metadata in API hub.



## Objectives

In this tutorial, you will complete the following steps:

  * Step 1: Install skills to turn API hub into a skills registry
  * Step 2: Provision your Google Cloud project
  * Step 3: Browse the catalog or add new skills



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Apigee](https://docs.cloud.google.com/apigee/pricing)
  * [ Cloud Storage](https://docs.cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Before you complete this tutorial, ensure that you have the following:

  1. An active Google Cloud project with [API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision) provisioned.
  2. A Cloud Storage bucket to store your signed skill bundles.
  3. The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed and configured on your local machine.
  4. A local private-public key pair for signing your skill packages.
  5. The IAM roles **API Hub Editor** (`roles/apihub.editor`) and **Storage Object Creator** (`roles/storage.objectCreator`) on the target project.



## Step 1: Install skills to turn API hub into a skills registry

Run the following command to download the installer and configure both the `skill-finder` and `skill-publisher` tools. You can replace `--runtime gemini` with other agent runtimes.
    
    
    curl -fsSL https://raw.githubusercontent.com/apigee/devrel/main/\
    references/apigee-skills-serving/bin/install-skill-finder.sh \
    | bash -s -- --runtime gemini

## Step 2: Provision your Google Cloud project

Clone the repository and run the provisioning script to enable APIs, create the storage bucket, register the attribute taxonomy, and generate your Ed25519 key pair:
    
    
    git clone https://github.com/apigee/devrel.git
    
    
    cd devrel/references/apigee-skills-serving
    
    
    bash bin/provision.sh --project PROJECT_ID --yes

The `provision.sh` script automatically sets up the environment, generates an Ed25519 signing key pair, stores the private key locally, and publishes the default example skills.

## Step 3: Browse the catalog or add new skills

After registering your skills, you can query the API hub catalog or publish new skills directly from your AI agent runtime.

For example, asking the following prompt: _"What skills are available in API hub?"_ runs `skill-finder` in **list mode** to search API hub and display a markdown table of matching skills. See the [GitHub repository](https://github.com/apigee/devrel/tree/main/references/apigee-skills-serving#shipped-skills) for a list of sample skills and their purpose.

Using API hub as a skills registry provides a unified discovery catalog, end-to-end security, and cross-runtime portability for your AI agent skills.

## Limitations and considerations

  * **Keyword-based search** : By default, API hub uses keyword overlap and attribute filtering. For semantic search, integrate a vector database component separately.
  * **Per-deployment trust root** : The Ed25519 trust root is specific to each deployment.
  * **Manual key rotation** : Although API hub supports multi-key trust roots allowing zero-downtime key rotation, the rollover process is not automated. For more information, see [Key rotation with zero downtime](https://github.com/apigee/devrel/blob/main/references/apigee-skills-serving/docs/provisioning.md#key-rotation-with-zero-downtime).



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
