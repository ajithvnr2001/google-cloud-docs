---
url: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-from-cloud-foundry-to-cloud-run/
title: Cloud Foundry to Cloud Run migration overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:45.528793+00:00
---

# Cloud Foundry to Cloud Run migration overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-from-cloud-foundry-to-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Cloud Foundry to Cloud Run migration overview Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Foundry to Cloud Run migration guides provide background information on the differences between Cloud Foundry services and Cloud Run services, and show what you need to do to migrate Cloud Foundry applications to run in a container on Cloud Run. These migration pages do not cover data migration.

## Cloud Foundry applications eligible for migration

Cloud Run is designed to run stateless HTTP or HTTP/2 applications. Your Cloud Foundry application cannot be migrated unless it meets the following criteria:

  * Uses HTTP or HTTP/2 (including gRPC).
  * Listens for traffic based on the `PORT` environment variable.
  * Doesn't require routing on different paths to different applications.
  * Doesn't require legacy Cloud Foundry "route services" for proxying traffic.
  * Doesn't require an instance ID or a particular startup order.
  * Doesn't need individual instances to be addressable.
  * Can be started without side-effects to the environment, for example, starting a database migration.



## Understanding the differences between Cloud Foundry and Cloud Run

Although Cloud Foundry and Cloud Run both share a similar source deployment experience, there are crucial differences in how the platforms approach workload containerization, application configuration and service definitions. Cloud Foundry and Cloud Run differences are shown in the following table:

App Component | Cloud Foundry | Cloud Run   
Container image deploy | Cloud Run   
Source deploy Dockerfile | Cloud Run   
Source deploy buildpacks  
---|---|---|---|---  
Containerization | CF Buildpacks v2 | N/A | Cloud Build | Cloud Build  
Base Image |  [cflinuxfs3](https://github.com/cloudfoundry/cflinuxfs3) (Ubuntu 18.04)   
[cflinuxfs4](https://github.com/cloudfoundry/cflinuxfs4) (Ubuntu 22.04)  |  Bring your own container image |  Dockerfile specified |  Ubuntu 18.04 or Ubuntu 22.04  
Service Definition | `manifest.yaml` | `service.yaml`  
Ignore list | `.cfignore` | `.gcloudignore`  
Service Metadata | `VCAP_*` environment variables | Workload Identity, Cloud Secrets  
Supported container formats | Droplet | Docker Image Manifest V2, Schema 1, Schema 2, and OCI formats  
  
## How to migrate

To migrate a Cloud Foundry application:

  1. [Choose a strategy for building OCI-compliant containers](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy)
  2. [Migrate to OCI-compliant containers](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-to-oci-containers)
  3. [Convert the manifest](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration#convert-manifest-to-service)
  4. [Attach backing services](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration#attach_any_backing_services)
  5. [Deploy the service to Cloud Run](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration#deploy)



## Sample migration

The [Spring Music example](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/spring-music-migration-example) uses core components of Cloud Foundry to rebuild Spring Music as an OCI compatible image and deploy it to Cloud Run. This sample follows the [lift and shift](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy#modifying_cloud_foundry) OCI compliancy strategy.

## What's Next

[Choose your containerization strategy](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
