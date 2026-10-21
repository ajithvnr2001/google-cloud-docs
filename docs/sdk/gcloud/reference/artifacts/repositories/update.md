---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update/
title: gcloud artifacts repositories update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:13.827351+00:00
---

# gcloud artifacts repositories update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts repositories update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts repositories update - update an Artifact Registry repository 
SYNOPSIS
    

`gcloud artifacts repositories update` (`REPOSITORY` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--disable-remote-validation`] [`--immutable-tags`] [`--remote-password-secret-version`=`REMOTE_PASSWORD_SECRET_VERSION`] [`--remote-username`=`REMOTE_USERNAME`] [`--severity`=`SEVERITY`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--upstream-policy-file`=`FILE`] [`--allow-vulnerability-scanning` | `--disable-vulnerability-scanning`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--clear-platform-logs` | `--disable-platform-logs` | `--enable-platform-logs`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the description or labels for an Artifact Registry repository. 

This command can fail for the following reasons: 

  * A repository with this name does not exist. 
  * The active account does not have permission to update repositories. 


EXAMPLES
     To update a repository with the name `my-repo` under the current project, run: 
    
    
    gcloud artifacts repositories update my-repo --description="New description"

POSITIONAL ARGUMENTS
    

Repository resource - The Artifact Registry repository to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--description`=`DESCRIPTION`
     Description for the repository. 
`--disable-remote-validation`
     Do not make an HTTP request to validate the remote upstream. Not recommended when setting a custom remote upstream unless you are absolutely sure your upstream URI and any auth is valid. 
`--immutable-tags`
     (Docker only) Prevent changes to tagged images in the repository. Tags cannot be deleted or moved to a different image digest, and tagged images cannot be deleted. 
`--remote-password-secret-version`=`REMOTE_PASSWORD_SECRET_VERSION`
     Secret Manager secret version that contains password for the remote repository upstream. 
`--remote-username`=`REMOTE_USERNAME`
     Remote Repository upstream registry username. 
`--severity`=`SEVERITY`
     The minimum severity level of logs to generate. This flag is only applicable when using --enable-platform-logs. `SEVERITY` must be one of: 

`error`
     Log events with severity ERROR or higher. 
`info`
     Log events with severity INFO or higher. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--upstream-policy-file`=`FILE`
     (Virtual Repositories only) is the upstreams for the Virtual Repository. Example of the file contents: [ { "id": "test1", "repository": "projects/p1/locations/us-central1/repositories/repo1", "priority": 1 }, { "id": "test2", "repository": "projects/p2/locations/us-west2/repositories/repo2", "priority": 2 } ] 
At most one of these can be specified: 

`--allow-vulnerability-scanning`
     Allow vulnerability scanning on the repository. 
`--disable-vulnerability-scanning`
     Disable vulnerability scanning on the repository. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud artifacts repositories update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud artifacts repositories update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--clear-platform-logs`
     Clear platform logging settings for the repository to fall back to project settings. 
`--disable-platform-logs`
     Disable platform logging for the repository. 
`--enable-platform-logs`
     Enable platform logging for the repository. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `artifactregistry/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/artifacts/docs/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts repositories update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories/update)
    
    
    [gcloud beta artifacts repositories update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
