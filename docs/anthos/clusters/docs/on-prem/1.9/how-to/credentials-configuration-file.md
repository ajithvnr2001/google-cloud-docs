---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file/
title: Credentials configuration file \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:54.922417+00:00
---

# Credentials configuration file  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/credentials-configuration-file/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Credentials configuration file Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/credentials-configuration-file)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/credentials-configuration-file)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes the fields in a credentials configuration file for Google Distributed Cloud.

You use a credentials configuration file to hold usernames and passwords. Here are some examples of how you would use a credentials configuration file:

  * In your [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/admin-cluster-configuration-file), specify a file that holds credentials for your vCenter server.

  * In your admin cluster configuration file, specify a file that holds credentials for your private Docker registry.




**Template**

Click to see a template for a credentials configuration file.
    
    
    apiVersion: v1
    kind: "CredentialFile"
    items:
    - name: ""
      username: ""
      password: ""
    - name: ""
      username: ""
      password: ""
    - ...

Keeping credentials in a file that is separate from your cluster configuration file helps to limit the number of people who have access to the credentials.

## Filling in the fields in a credentials configuration file

In your credentials configuration file, enter fields values as described in this section.

## `items`

Array of objects, each of which holds a username and password.

### `items[0].name`

String. A name of your choice for the object. For example:
    
    
    items:
    - name: "vcenter-creds"
    

### `items[0].username`

String. A username. For example:
    
    
    items:
    - name: "vcenter-creds"
      username: "my-vcenter-account"
    

### `items[0].password`

String. A password. For example:
    
    
    items:
    - name: "vcenter-creds"
      passwords: "U$icUKEW#INE"
    

## Example of a credentials configuration file

Here's an example of a credentials configuration file that holds three sets of credentials.
    
    
    apiVersion: v1
    kind: "CredentialFile"
    items:
    - name: "vcenter-creds"
      username: "my-vcenter-account"
      password: "U$icUKEW#INE"
    - name: "f5-creds"
      username: "my-f5-account"
      password: "exvQVx^@L%F1"
    - name: "private-registry-creds"
      username: "my-registry-account"
      password: "kIJGS&uRm2Vh"
    

Notice that each block of credentials has a name. In your admin cluster configuration file, you specify the name of a credentials block in a `fileRef.entry` field.

Here's an example that shows portions of an admin cluster configuration file. You can see that the file specifies three blocks of credentials, all of which are in the same credentials file:
    
    
    vCenter:
      credentials:
        fileRef:
          path: "my-folder/my-creds.yaml"
          entry: "vcenter-creds"
    ...
    loadBalancer:
      f5BigIP:
        credentials:
          fileRef:
            path: "my-folder/my-creds.yaml"
            entry: "f5-creds"
    ...
    privateRegistry:
      credentials:
        fileRef:
          path: "my-folder/my-creds.yaml"
          entry: "private-registry-creds"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
