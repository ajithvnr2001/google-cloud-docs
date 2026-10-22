---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects/
title: Create Harbor projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:20.430402+00:00
---

# Create Harbor projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create Harbor projects Stay organized with collections  Save and categorize content based on your preferences. 

In Harbor, a project serves as a logical unit for organizing and managing a collection of container images. It provides a way to group related artifacts together and apply specific policies, access controls, and replication rules to the entire collection. Images cannot be pushed or pulled to Harbor before a project is created.

## Before you begin

Before you begin, you must initialize your identity with the Harbor registry by signing in to the Harbor UI at least once.

**Warning:** Attempting to create a Harbor project without first initializing your Harbor identity can cause the process to fail or remain pending.

### Required IAM role

To create Harbor projects and manage image namespaces, contact your IAM Project Admin to request the **Harbor Project Creator** (`harbor-project-creator`) role, which lets you create, get, and watch Harbor projects in the project namespace. This role includes the required permissions to define new image namespaces so you can establish security boundaries for your containerized applications.

## Create a Harbor project

Create a Harbor project using the GDC console or the gdcloud CLI.

###  Console 

In the GDC console, follow these steps:

  1. Click the **Harbor Container Registry** link in the **CI/CD** section in the navigation menu.
  2. Click **Create a Harbor project**.
  3. Enter the name of the project.
  4. Optional: Vulnerability scanning is enabled by default. To disable automatic vulnerability scanning for Harbor projects, click the **Enable vulnerability scanning for the project** toggle. For more information, see [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities).
  5. Click **Create**.
  6. A confirmation message appears stating your project is created successfully.
  7. After your Harbor project is created, sign in to the Harbor UI to confirm that you can view the Harbor project.



###  gdcloud 

Create the Harbor project:
    
    
      gdcloud harbor harbor-projects create HARBOR_PROJECT \
        --project=PROJECT \
        --instance=INSTANCE
    

Replace the following:

  * `HARBOR_PROJECT`: the name of the Harbor project to create.
  * `PROJECT`: the name of the GDC project.
  * `INSTANCE`: the name of the instance.



## What's next

After you create a Harbor project, configure your Docker and Helm clients to connect to your Harbor registry:

  * [Configure Docker to trust the Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust)
  * [Sign in to Docker and Helm](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
