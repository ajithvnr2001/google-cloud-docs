---
url: https://docs.cloud.google.com/source-repositories/docs/migration-guides/
title: Cloud Source Repositories migration details \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:01.964230+00:00
---

# Cloud Source Repositories migration details  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/migration-guides/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Cloud Source Repositories migration details Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Source Repositories is End of Sale. In preparation for the deprecation of this service, this page outlines migration options for multiple use cases. A shutdown date will be communicated at least one year before the shutdown occurs to provide time for you to successfully migrate to an alternative product.

All users must migrate their repositories before the shutdown date. Review the following migration options to begin planning your migration.

## Migration guides

  * ### [Migrate to Secure Source Manager This guide provides the necessary steps to successfully migrate a Git repository, including all repository information, from Cloud Source Repositories to Secure Source Manager.  ](https://docs.cloud.google.com/source-repositories/docs/csr-ssm-migration-guide)
  * ### [Translate Cloud Source Repositories roles and permissions to Secure Source Manager This guide explains how roles and permissions in Cloud Source Repositories map to those in Secure Source Manager.  ](https://docs.cloud.google.com/source-repositories/docs/csr-ssm-permission-mapping)



## Determine your repository usage

To plan your migration, first identify all of your Cloud Source Repositories. You can view your repositories by going to the [Source Repositories page](https://source.cloud.google.com) and using the project selector to search for projects that contain repositories. To access a repository, you need the appropriate Identity and Access Management (IAM) permissions, such as Project Owner or Source Repository Administrator.

After you identify a repository, determine if it is still in use or connected to a build system. If a repository is not in use, delete it. Deleting unused repositories helps with the deprecation process and stops future notifications.

## Migration paths by use case

The following table maps common Cloud Source Repositories use cases to recommended migration paths.

Use case | Migration path  
---|---  
Software development | [Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) or a third-party source code management system.  
Integrating with Cloud Build | If your Cloud Source Repositories are a mirror of an external repository used to trigger Cloud Build, see [Connect Cloud Build to your source code management system](https://docs.cloud.google.com/build/docs/triggers) or set up a [webhook trigger](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events).  
Kubernetes config sync and other infrastructure as code use cases | [Artifact Registry OCI](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry) / [Helm](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry), [Secure Source Manager](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/grant-access-git) or other source code management systems.  
Backing up source code repositories | A third-party backup solution. For an example, see [Configuring backups on your instance](https://docs.github.com/en/enterprise-server@3.17/admin/backing-up-and-restoring-your-instance/configuring-backups-on-your-instance) in the GitHub documentation.  
Private network connectivity | For use cases, see [Developer Connect and Service Directory](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise-private).  
If you need manual triggers, Pub/Sub, webhook, or terraform support, see [Cloud Build Repositories](https://docs.cloud.google.com/build/docs/repositories#feature-support).  
If you are using Cloud Source Repositories to connect Cloud Build Repositories to GitHub Enterprise in a private network, see [Build repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network?generation=2nd-gen).  
For infrastructure as code and private network support see [Artifact Registry OCI](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry) and [Helm](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry).  
Using Cloud Debugger or Error Reporting | Connect to another Git provider.  
  
## What's next

  * [Secure Source Manager overview](https://docs.cloud.google.com/secure-source-manager/docs/overview)
  * [Use Git with Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/use-git)
  * [Create an instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
