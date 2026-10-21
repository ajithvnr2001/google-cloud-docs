---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/create/
title: gcloud beta artifacts repositories create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:05.535558+00:00
---

# gcloud beta artifacts repositories create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts repositories create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts repositories create - create an Artifact Registry repository 
SYNOPSIS
    

`gcloud beta artifacts repositories create` (`REPOSITORY` : `--location`=`LOCATION`) `--repository-format`=`REPOSITORY_FORMAT` [`--allow-snapshot-overwrites`] [`--async`] [`--description`=`DESCRIPTION`] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--version-policy`=`VERSION_POLICY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Artifact Registry repository. 

This command can fail for the following reasons: 

  * A repository with the same name already exists. 
  * The active account does not have permission to create repositories. 
  * A valid repository format was not provided. 


EXAMPLES
     To create a repository with the name `my-repo` under the current project, run: 
    
    
    gcloud beta artifacts repositories create my-repo

To create repository `my-repo` with a KMS key `projects/my-project/locations/us/keyRings/my-kr/cryptoKeys/my-key`, run: 
    
    
    gcloud beta artifacts repositories create my-repo --kms-key=projects/my-project/locations/us/keyRings/my-kr/cryptoKeys/my-key

POSITIONAL ARGUMENTS
    

Repository resource - The Artifact Registry repository to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REPOSITORY`
     ID of the repository or fully qualified identifier for the repository. 

To set the `repository` attribute: 

  * provide the argument `repository` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the repository. Overrides the default artifacts/location property value for this command invocation. To configure the default location, use the command: gcloud config set artifacts/location. To set the `location` attribute: 

  * provide the argument `repository` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `artifacts/location`. 


REQUIRED FLAGS
    

`--repository-format`=`REPOSITORY_FORMAT`
     Format of the repository. REPOSITORY_FORMAT must be one of: 
    
    
    apt
       APT package format.
    docker
       Docker image format.
    googet
       GooGet package format.
    kfp
       KFP package format.
    maven
       Maven package format.
    npm
       NPM package format.
    python
       Python package format.
    yum
       YUM package format.

OPTIONAL FLAGS
    

`--allow-snapshot-overwrites`
     (Maven only) Allow repository users to publish a snapshot that overwrites the same snapshot version in the repository. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description for the repository. 
`--kms-key`=`KMS_KEY`
     Name of the encryption key that's used for encrypting the contents of the repository. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--version-policy`=`VERSION_POLICY`
     (Maven only) The package versions that the repository will store. `VERSION_POLICY` must be one of: 

`none`
     (Maven only) The repository doesn't validate the version type. 
`release`
     (Maven only) The repository accepts release versions only. 
`snapshot`
     (Maven only) The repository accepts snapshot versions only. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `artifactregistry/v1beta2` API. The full documentation for this API can be found at: <https://cloud.google.com/artifacts/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts repositories create](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create)
    
    
    [gcloud alpha artifacts repositories create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
