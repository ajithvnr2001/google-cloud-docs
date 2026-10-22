---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects/
title: Create Harbor projects \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:06.758894+00:00
---

# Create Harbor projects  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/create-harbor-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create Harbor projects Stay organized with collections  Save and categorize content based on your preferences. 

This document guides developers and administrators on how to create and verify Harbor projects using the GDC console or the gdcloud CLI. 

You can store, secure, and distribute your container images in Google Distributed Cloud (GDC) air-gapped appliance by organizing them into Harbor projects inside the preconfigured `tear-harbor` instance. In Harbor, a project serves as a logical unit to group related artifacts, manage your images, and apply specific policies, access controls, and replication rules.

The `tear` system project provides `tear-harbor` as the only Harbor instance available—a single, preconfigured registry for your entire appliance—so you don't need to provision, upgrade, or maintain separate Harbor instances for each customer project. This centralized architecture eliminates infrastructure overhead and lets you manage image namespaces, access controls, and vulnerability scanning from one shared registry. To use this shared registry for workloads in any customer project, you must have your Harbor roles created in the `tear` project and create your Harbor projects directly in the `tear` project.

## Before you begin

Before you begin, make sure you meet the following requirements:

  * **Recommended knowledge** : Make sure you are familiar with the concepts and architecture covered in [Managed Harbor Service overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/mhs-overview). Understanding that Harbor is a shared resource hosted in the `tear` project is essential, because all Harbor role assignments and project creation tasks must target the `tear` project.
  * **Initialize your Harbor identity** : You must sign in to the Harbor UI at least once before you attempt to create projects in the console. The initial login initializes your identity with the Harbor registry. For more information, see Get the Harbor instance URL and Initialize your Harbor identity.

**Warning:** Attempting to create a Harbor project without first initializing your Harbor identity can cause the process to fail or remain pending.



### Required IAM role

To create a Harbor project—including a Harbor project that you intend to use in a customer project—you must have the Harbor Project Creator (`harbor-project-creator`) Identity and Access Management (IAM) role created and granted in the `tear` project to access the `tear-harbor` instance. This role provides create, get, and watch permissions for Harbor project custom resources within the `tear-harbor` instance in the `tear` project, which lets you define new image namespaces and establish security boundaries for your containerized applications.

To request access in the `tear` project, contact your Project IAM Admin.

### Get the Harbor instance URL

To sign in to the Harbor UI or use the gdcloud CLI to manage images, you need the external endpoint URL of the registry instance:

  1. Using the gdcloud CLI, get the Harbor instance URL:
         
         gdcloud harbor instances describe tear-harbor --project=tear
         

The output is similar to the following, which typically contains the `externalEndpoint` field:
         
         externalEndpoint: https://harbor.tear.example.com
         

  2. Copy the `externalEndpoint` URL to access the Harbor UI through your browser and to [establish client trust authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-trust#configure-docker-to-trust-harbor-root-ca).




If you don't have gdcloud CLI access, contact your Infrastructure Operator (IO) for support.

### Initialize your Harbor identity

Sign in to the Harbor UI at least once to synchronize your identity. This initial login registers your user profile in the Harbor database so the system recognizes your permissions:

  1. In a browser, navigate to the registry URL.
  2. Sign in using your GDC credentials.



## Create a Harbor project

Because `tear-harbor` in the `tear` project is the only Harbor instance available and serves as the shared registry for the entire appliance, you must create all Harbor projects in the `tear` project—including Harbor projects that store images for workloads in other customer projects. Create a Harbor project using the GDC console or the gdcloud CLI.

###  Console 

In the GDC console, follow these steps in the `tear` project:

  1. Select the `tear` project.
  2. Click the **Harbor Container Registry** link in the **CI/CD** section in the navigation menu.
  3. Click **Create a Harbor project**.
  4. Enter the name of the Harbor project.
  5. Optional: Vulnerability scanning is enabled by default. To disable automatic vulnerability scanning for Harbor projects, click the **Enable vulnerability scanning for the project** toggle. For more information, see [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/scan-vulnerabilities).
  6. Click **Create**. A confirmation message appears stating that your project is created.
  7. Sign in to the Harbor UI to confirm that you can view the Harbor project.



###  gdcloud 

Create the Harbor project in the `tear` project:
    
    
    gdcloud harbor harbor-projects create HARBOR_PROJECT \
      --project=tear \
      --instance=tear-harbor
    

Replace `HARBOR_PROJECT` with the name of the Harbor project to create.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
