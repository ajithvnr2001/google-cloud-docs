---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/architecture/
title: Migrate to Containers CLI architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:46.656455+00:00
---

# Migrate to Containers CLI architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Containers CLI architecture 

This page provides a high-level description of how Migrate to Containers CLI transforms your applications residing on virtual machine (VM) instances into artifacts that you can use to deploy your application components from the source environment to a target cluster on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) or [GKE Enterprise](https://docs.cloud.google.com/anthos).

## Migrate to Containers CLI components

Modernization using Migrate to Containers CLI spans across three steps: Transformation, Workload deployment, and Maintenance.

![process architecture](https://docs.cloud.google.com/migrate/containers/docs/images/process_architecture.png)

  1. **Transformation** \-- Migrate to Containers CLI is used to transform a VM-based application component into a container-based application component ready to be deployed. This spans across five phases:

     1. **Copy** \-- Copy the file system of the target machine to the local machine.
     2. **Analyze** \-- Analyze the file system to create a migration plan.
     3. **Edit** \-- Edit the plan to modify the migration outputs to fit your needs.
     4. **Generate** \-- Generate artifacts such as Docker files, Docker contexts, Kubernetes deployment files and Skaffold configuration.
     5. **Migrate data** \-- Copy the data files into persistent volumes. This is optional.
  2. **Workload deployment** \-- You can deploy Migrated container workloads on any GKE or GKE Enterprise cluster meeting the minimum requirements. The migration artifacts can include one or more Dockerfiles, one or more Kubernetes deployment specs, and a Skaffold configuration file.

  3. **Maintenance** \-- After you migrate container workloads, you typically perform optimization and maintenance operations. The extracted workload content and the generated Dockerfile can be integrated in a CI/CD pipeline for efficient image-based maintenance.




## What's next

  * Learn about [reviewing compatible OS, workloads, and Kubernetes versions](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/compatible-components).
  * Learn how to [discover, collect, and assess VMware VMs for migration](https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-quickstart).
  * Learn how to [migrate a VM](https://docs.cloud.google.com/migrate/containers/docs/migrate-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
