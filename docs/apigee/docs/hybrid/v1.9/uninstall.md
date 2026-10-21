---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall/
title: Uninstall hybrid runtime \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:56:49.911024+00:00
---

# Uninstall hybrid runtime  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Uninstall hybrid runtime Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/uninstall.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/uninstall.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/uninstall.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/uninstall.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/uninstall.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/uninstall.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/uninstall.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/uninstall.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/uninstall.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/uninstall.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/uninstall.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/uninstall.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/uninstall.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/uninstall.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/uninstall.html)



**NOTE:** To uninstall successfully, you must have kubectl version 1.11.x or later installed.

To delete **Apigee components within a specific scope** , use `apigeectl` with the flags for the scope that includes those components: 

  * `--all-envs`: all environment-scope components in all the environments under the organization named in the override config file
  * `--datastore`: Cassandra.
  * `--env env-name`: the environment-scope components: Runtime, Synchronizer, and UDCA
  * `--org`: the organization-scope components: Apigee Connect Agent, Mart, and Watcher
  * `--settings virtualhosts`: `virtualhost` settings only
  * `--telemetry`: Logger and Metrics



For example: 
    
    
    apigeectl delete -f your_overrides_file.yaml --org --env env-name

To delete **only the Apigee components** from the cluster, use this command: 
    
    
    apigeectl delete -f your_overrides_file.yaml

Use the following commands to delete **the entire Apigee hybrid installation except cert-manager** from your cluster:

  1. Run `apigeectl delete` with the default scope: 
         
         apigeectl delete -f your_overrides_file.yaml

  2. Verify that the Apigee hybrid components were deleted: 
         
         kubectl -n apigee get apigeedatastore,apigeeredis,apigeetelemetry,org,env,arc

Your output should be empty

  3. Run `apigeectl delete` again with `--all`: 
         
         apigeectl delete --all -f your_overrides_file.yaml




To uninstall cert-manager, see [Uninstalling on Kubernetes](https://cert-manager.io/docs/installation/uninstall/kubernetes/) in the cert-manager documentation. 

For more information about the `apigeectl` command, see [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference).

Use the following command to remove cert-manager: 
    
    
    kubectl -n cert-manager delete secret apigee-ca

If you have a multi-region installation, and you want to install Apigee hybrid again on the same region, you need to follow the instructions for copying the `apigee-ca` secret in [Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region#set-up-the-new-region).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
