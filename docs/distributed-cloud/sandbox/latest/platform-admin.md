---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/platform-admin/
title: Set up the Platform Admin account \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:07.579292+00:00
---

# Set up the Platform Admin account  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/platform-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Set up the Platform Admin account Stay organized with collections  Save and categorize content based on your preferences. 

Your GDC Sandbox instance is populated with several accounts. One of them is the Platform Admin account, with the email address `fop-platform-admin@example.com`. This page describes how to configure this account with the necessary permissions for creating projects and performing other administration tasks.

## Set up Platform Admin permissions

The following steps will set up your administrator account with the roles necessary to manage projects, users, storage, and other resources.

**Warning:** don't remove the Platform Admin account `fop-platform-admin@example.com`, or remove the `Organization IAM Admin` role from this account. This will lock out the instance.

You can set up your administrator account using the GDC console, or the command line tool `gdcloud`.

###  GDC console 

  1. Navigate to your GDC console as described In [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect).
  2. Select **Access**.
  3. Select **fop-platform-admin@example.com** and click **Edit Roles**.
  4. Click **Add Another Role** to add more roles.

     1. To provide the Platform Admin with the necessary rights to create projects and perform other administrative tasks, add the following roles: 
        * Org Network Policy Admin
        * Organization IAM Admin
        * Bucket Admin
        * Organization DB Admin
        * Project Creator
        * Project Editor
        * User Cluster Admin
        * Organization Grafana Viewer
     2. To provide the Platform Admin with the necessary rights to create and test specific services, add roles specific to those services.
     3. Click **Save**.
  5. Click **Submit**.




###  gdcloud 

  1. Ensure you have the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud) installed.
  2. Sign in using [gdcloud auth login](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud).
  3. Set up role bindings for an organization:
         
         gdcloud organizations add-iam-policy-binding ORGANIZATION \
           --member=user:fop-platform-admin@example.com \
           --role=ROLE
         

Replace the following variables:

     * `ORGANIZATION`: the name of the organization for which you're setting up the role binding.
     * `ROLE`: the name of the predefined or custom role you want to assign to the user.
  4. To provide the Platform Admin with the necessary rights to create projects and perform other administrative tasks, add the following roles:
         
         gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=org-network-policy-admin
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=organization-iam-admin
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=bucket-admin
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=organization-db-admin
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=project-creator
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=project-editor
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=user-cluster-admin
         
           gdcloud organizations add-iam-policy-binding org-1 \
                     --member=user:fop-platform-admin@example.com \
                     --role=organization-grafana-viewer
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
