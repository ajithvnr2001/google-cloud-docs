---
url: https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access/
title: Access Assured OSS packages using a virtual repository \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:16.526579+00:00
---

# Access Assured OSS packages using a virtual repository  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Access Assured OSS packages using a virtual repository Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about [setting up a virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) in an Artifact Registry instance in one of your own projects to access and download the Assured OSS packages. For more information about repository options, see [Assured OSS repository options](https://docs.cloud.google.com/assured-open-source-software/docs/overview#aoss-repository-options).

Virtual repositories are supported in the free tier only. In the premium tier, Assured OSS repositories are provisioned automatically.

## Before you begin

If you want to use a virtual repository to access the Assured OSS packages, do the following:

  * Provide the [Artifact Registry Service Agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account) details for the project you want to use in the Assured OSS [Customer Enablement form](https://developers.google.com/assured-oss#get-started). The Artifact Registry Service Agent is a Google-managed service account that acts on behalf of Artifact Registry when interacting with Google Cloud services. Virtual repositories use the service to authenticate to upstream repositories. The service agent requires read access to the Assured OSS Artifact Registry repository.

  * You can enable the service agent access during your initial enrollment by including the service agent details as one of the service accounts you want to have access to Assured OSS.

  * If you have already enabled Assured OSS access without including the service agent details, return to the Assured OSS enablement website and create a new enablement request for the service agent with its specific details.

  * For instructions to find the name of the existing service agent or create a new service agent for your project, see [Artifact Registry service account](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account).




## Set up a virtual repository

  1. [Create a virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo#create) in the same Google Cloud region where the Assured OSS Artifact Registry repository resides. Use the project whose service agent has read access to the Assured OSS Artifact Registry repository.

  2. In the `policies.json` file, add the following configuration to give the virtual repository access to the Assured OSS Artifact Registry repository:

     * Configuration for the Java repository:
    
    {
      "id" : "AOSS Java",
      "repository" : "projects/cloud-aoss/locations/us/repositories/cloud-aoss-java",
      "priority" : 100
    }
    

     * Configuration for the Python repository:
    
    {
      "id" : "AOSS Python",
      "repository" : "projects/cloud-aoss/locations/us/repositories/cloud-aoss-python",
      "priority" : 100
    }
    

     * Configuration for the Go repository:
    
    {
      "id" : "AOSS Go",
      "repository" : "projects/cloud-aoss/locations/us/repositories/assuredoss-go-free",
      "priority" : 100
    }
    

  3. Download the Java, Python, and Go packages using the virtual repository. For instructions on downloading the packages, see the following topics:

     * [Download Java packages](https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages)
     * [Download Python packages](https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages)
     * [Download Go packages](https://docs.cloud.google.com/assured-open-source-software/docs/download-go-packages)



## Access packages not available in Assured OSS

If you want access to packages that aren't available in the Artifact Registry repository for Assured OSS, you can do the following:

  * Assured OSS is also pre-configured with Assured OSS as the preferred repository and canonical public repositories, such as Maven Central or PyPI, as secondary repositories. To use this feature ([Preview](https://cloud.google.com/products#product-launch-stages)), you can point to a single URL:

    * For Java, use `https://us-maven.pkg.dev/cloud-aoss/java`
    * For Python, use `https://us-python.pkg.dev/cloud-aoss/python`
    * For Go, use `https://us-go.pkg.dev/cloud-aoss/go`



## What's next

  * [Supported Java and Python packages](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages)
  * [Supported Go packages](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages-go)
  * [Access security metadata using Artifact Analysis API](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis)
  * [Access security metadata using Cloud Storage](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage)
  * [Subscribe to notifications](https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications)
  * [Artifact signature overview](https://docs.cloud.google.com/assured-open-source-software/docs/package-signature-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
