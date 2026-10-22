---
url: https://docs.cloud.google.com/build/docs/release-channels/
title: Cloud Build release channels \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:55.314312+00:00
---

# Cloud Build release channels  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/release-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud Build release channels Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to control how often your build workers are updated with new versions of the base operating system and Docker. By selecting a release channel, you can achieve a balance between resilient build processes and up-to-date security and functionality.

You can also choose specific worker versions rather than channels.

**Note:** Release channels manage only the underlying worker VM host environment. You retain full control over software versions inside your build step ontainers.

## Available channels

The following are the release channels available:

Channel | Update frequency | Uses  
---|---|---  
`regular` | Within four weeks after each version becomes available | The default channel, and the recommended channel for security compliance. Frequent updates require that your CI processes are kept up to date with new versions.  
`rapid` | Always the newest version available | Get the latest security updates and features as soon as they're available. New base OS and Docker versions can break CI process and have other issues.  
`stable` | Once per year, typically in February | This channel prioritizes stability over new features, helping your CI process be more resilient. However, there is a higher risk of exposure to vulnerabilities. The underlying Docker versions might not receive patches from Docker.  
  
See Available releases to see what release is in each channel.

**Important:** Until 2027-03-28, you'll use the `legacy` version by default. After that date, you use the `regular` release channel by default. You can still specify a different release channel or version in your build config or when you invoke a build (in the default pool), or in the private pool configuration.

## Specify a release channel or version

When you choose one of the three release _channels_ , you're choosing how frequently to update both the Docker version and the worker-image operating system. When you choose a release _version_ , you're choosing the specific versions of Docker and Debian for the worker image.

You can specify either the channel or the release version. There are three places where you can specify them:

  * In the private pool

If you're using a private pool, you can specify either the channel or the release version in the private pool, either by [updating the private pool configuration](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#workerrelease) or by selecting a channel or version when you create or update the pool in the Google Cloud console. If you do this, that channel or version is then used for all builds using that pool, and you can't override it in the build config or on the command line.

  * In the build config

If you're using the default pool, you can specify the channel or version in the build config file. That channel or version is then used for all builds invoked using that build config.

  * On the command line when invoking a build

When you invoke a build using `gcloud builds submit`, you can include the `--worker-release` flag. The value you provide for this flag overrides what you configure in the build config file. You can't use this flag if the build is running in a private pool, because the pool decides which release to use.




###  private pool 

**To specify a release version or channel for your private pool:**

Update your private pool configuration using the following command:
    
    
    gcloud builds worker-pools update PRIVATEPOOL_ID \
           --worker-release=CHANNEL_OR_VERSION \
           --region=REGION \
           --project=PROJECT_ID
    

Replace the following:

**PRIVATEPOOL_ID** with the ID of the private pool you'll use to run builds using this channel.

**CHANNEL_OR_VERSION** with the name of the channel you want to use: `regular`, `rapid`, or `stable`, or with a specific version number.

**REGION** with the region where your private pool is located.

**PROJECT_ID** with the ID of the project that contains your private pool.

###  build config 

**To specify a release version or channel in your[build configuration file](https://docs.cloud.google.com/build/docs/build-config-file-schema):**

Add the following property, under the [`options`](https://docs.cloud.google.com/build/docs/build-config-file-schema#options) stanza:
    
    
    steps:
      # ...
    options:
      workerRelease: CHANNEL_OR_VERSION
    

Replace CHANNEL_OR_VERSION with the name of the channel you want to use: `regular`, `rapid`, or `stable`, or with a specific version number.

**Note:** If you're using a private pool, you can't set the release channel in the build config file. You can only specific the release channel in the build config if you're using the default pool.

###  build invocation 

**To specify a release channel in your build invocation:**

Add the following flag to your `gcloud builds submit` command:
    
    
    --worker-release=CHANNEL_OR_VERSION
    

Replace CHANNEL_OR_VERSION with the name of the channel you want to use: `regular`, `rapid`, or `stable`, or with a specific version number.

**Note:** If you're using a private pool, you can't set the release channel on the command line when you invoke a build. You can only specify the release channel or version on the command line if you're using the default pool.

## Available releases

The following table lists the available worker versions, the channels that support each version, and the underlying versions of Docker and Debian for each:

Release version | Channels | Supported until | Underlying versions  
---|---|---|---  
`2026.09` | `rapid`, `regular`, `stable` | 2029-09-30 | Docker Engine 29  
Debian 13  
`legacy` |  | 2028-03-31 | Docker Engine 20.10  
Debian 11  
  
## What's next

  * [Learn more](https://docs.cloud.google.com/build/docs/build-config-file-schema) about the build configuration file.
  * [Learn more](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema) about the private pool configuration file.
  * [Learn about](https://docs.cloud.google.com/build/docs/shared-responsibility) about the Cloud Build shared responsibility model.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
