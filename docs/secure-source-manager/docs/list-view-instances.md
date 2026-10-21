---
url: https://docs.cloud.google.com/secure-source-manager/docs/list-view-instances/
title: List and view instances \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:09.251059+00:00
---

# List and view instances  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/list-view-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  List and view instances Stay organized with collections  Save and categorize content based on your preferences. 

You can use the gcloud CLI to list all Secure Source Manager instances in your project. For more information on Secure Source Manager instances, see the [Secure Source Manager overview][ssm-overview].

## Required roles

To get the permissions that you need to list instances, ask your administrator to grant you the [Secure Source Manager Instance Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`) IAM role on the instance project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## List instances in project

Run the following command to get a list of Secure Source Manager instances in your project:
    
    
    gcloud source-manager instances list --region=REGION
    

Replace `REGION` with the location you want to list the instances from.

The response will look like the following:
    
    
    INSTANCE_ID: my-instance
    LOCATION: us-central1
    STATE: ACTIVE
    CREATE_TIME: 2023-02-27T20:57:52
    UPDATE_TIME: 2023-02-27T21:11:59
    HTML_HOST: my-instance-098765432109.us-central1.sourcemanager.dev
    

You can access the instance by entering the value of `HTML_HOST` in a browser address bar.

## Get instance details

Run the following command to get details of an instance:
    
    
    gcloud source-manager instances describe INSTANCE_ID \
        --region=REGION
    

Replace the following:

  * `INSTANCE_ID` with the name of your instance.
  * `REGION` with the location of your instance. For information on supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).



The response includes details of your instance similar to the following:
    
    
    createTime: '2023-02-27T20:57:52.310148676Z'
    hostConfig:
      api: my-instance-123456789098-api.us-central1.sourcemanager.dev
      gitHttp: my-instance-123456789098-git.us-central1.sourcemanager.dev
      gitSsh: my-instance-123456789098-ssh.us-central1.sourcemanager.dev
      html: my-instance-123456789098.us-central1.sourcemanager.dev
    name: projects/my-project/locations/us-central1/instances/my-instance
    state: ACTIVE
    updateTime: '2023-02-27T21:11:59.538591815Z'
    
    

## What's next

  * [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).
  * [Create and clone a repository](https://docs.cloud.google.com/secure-source-manager/docs/create-clone-repository).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
