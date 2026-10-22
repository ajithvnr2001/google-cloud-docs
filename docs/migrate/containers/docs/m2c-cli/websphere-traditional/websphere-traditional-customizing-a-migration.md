---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere-traditional/websphere-traditional-customizing-a-migration/
title: Customize migration plan for WebSphere traditional workloads \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:53.655422+00:00
---

# Customize migration plan for WebSphere traditional workloads  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere-traditional/websphere-traditional-customizing-a-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Customize migration plan for WebSphere traditional workloads

**Important:** The `websphere-traditional` plugin is now deprecated. For existing customers, this plugin is still supported till December 2023, after which it will no longer be available. If you're new to WebSphere workload modernization, then use the `websphere-container` plugin with the Migrate to Containers CLI instead.

## Before you begin

This topic assumes that you've already [created a migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the migration plan file.

## Edit the migration plan

After you have copied the file system and analyzed it, you can find the migration plan in the new directory that is created in the specified output path: ANALYSIS_OUTPUT_PATH/`config.yaml`.

Edit the migration plan as necessary and save the changes.

Review your migration plan's details and guiding comments to add information as needed.

Specifically, consider edits around the following sections.

## Select applications

On the migration plan, the application field represents the applications to migrate. If you do not want to migrate all applications, you can remove them.
    
    
    applications:
    - appName: hello-world-servlet-ear
      httpEndpoints:
      - httpPort: 9080
        httpsPort: 9443
        id: defaulthttpendpoint
      image:
        name: hello-world-servlet-ear
      path: /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/config/cells/m4a-twas-ndNode01Cell/applications/Hello-World-Servlet.ear
    …
    - appName: commons-ejb-ear-provided-ear
      httpEndpoints:
      - httpPort: 9080
        httpsPort: 9443
        id: defaulthttpendpoint
      image:
        name: commons-ejb-ear-provided-ear
      path: /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/config/cells/m4a-twas-ndNode01Cell/applications/commons-ejb-ear-provided.ear
      sharedLibraries:
      - /opt/IBM/WebSphere/AppServer/sharedJars/commons-io-2.8.0.jar
    
    

## Set the scanner options

In the migration plan, the `scannerOptions` field represents the argument to pass to the [IBM WebSphere Application Server Migration Toolkit for Application Binaries](https://www.ibm.com/support/pages/migration-toolkit-application-binaries). You can edit the arguments.
    
    
    scannerOptions:
      # Setting 'includeSensitiveData: true' will upload sensitive data, if exists, such as private keys, to the artifacts repository
      includeSensitiveData: false
      sourceAppServer: was90
    

**Note:** In order to collect sensitive data, in the migration plan, under `scannerOptions`, modify the value of `includeSensitiveData:` to be `true`. Notice that `set includeSensitiveData: true` will cause uploading sensitive artifacts into the user repository. On `liberty` and `openliberty`, the sensitive data will be stored in a secret file artifact that is used when building app container.

## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
