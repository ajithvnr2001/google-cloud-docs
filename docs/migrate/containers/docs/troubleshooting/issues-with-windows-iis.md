---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/issues-with-windows-iis/
title: Issues with Windows IIS services migration \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:18.061665+00:00
---

# Issues with Windows IIS services migration  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/issues-with-windows-iis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issues with Windows IIS services migration

This document describes workarounds for some issues that you might encounter while migrating Windows IIS services.

## Windows IIS deployment marked not ready

The deployment of Windows IIS workloads might be marked as not ready due to short timeouts. If you're deploying your workloads using Skaffold, then the deployment might show as failed.

As a workaround for this issue, increase the readiness probe timeout and period using PowerShell:
    
    
    foreach ($file in (Get-ChildItem . -Recurse -Include "deployment_spec.yaml")) { (Get-Content $file).replace("periodSeconds: 10", "periodSe
    conds: 30").replace("timeoutSeconds: 1", "timeoutSeconds: 10") | Set-Content $file }
    

## Skaffold build for Windows images fails

Skaffold build for Windows images might fail on a Windows machine because Skaffold tries to pull the base image for the wrong target.

If this issue occurs, you might see an error message similar to the following message:
    
    
    Checking cache...
     - migrated-image-6jc3z: Error checking cache.
    getting hash for artifact "migrated-image-6jc3z": getting dependencies for "migrated-image-6jc3z": parsing ONBUILD instructions: retrieving image "mcr.microsoft.com/dotnet/framework/aspnet:4.8": no child with platform linux/amd64 in index mcr.microsoft.com/dotnet/framework/aspnet:4.8
    

As a workaround for this issue, pull the image manually using the `docker pull` command, and run the Skaffold build again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
