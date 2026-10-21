---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/connections/git-repository-links/create/
title: gcloud alpha developer-connect connections git-repository-links create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:44:36.944032+00:00
---

# gcloud alpha developer-connect connections git-repository-links create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/connections/git-repository-links/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha developer-connect connections git-repository-links create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha developer-connect connections git-repository-links create - create a git repository link 
SYNOPSIS
    

`gcloud alpha developer-connect connections git-repository-links create` (`GIT_REPOSITORY_LINK` : `--connection`=`CONNECTION` `--location`=`LOCATION`) `--clone-uri`=`CLONE_URI` [`--annotations`=[`ANNOTATIONS`,…]] [`--async`] [`--etag`=`ETAG`] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a git repository link. 
EXAMPLES
     To create a git repository link 'my-git-repository-link' in a connection `my-connection` in `us-central1` run: 

$ [gcloud alpha developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/connections/git-repository-links) \
    
    
    create my-git-repository-link \
    --clone-uri=https://github.com/my-org/my-repo.git \
    --connection=my-connection --location=us-central1

Or run: 

$ [gcloud alpha developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect/connections/git-repository-links) \
    
    
    create \
    projects/my-project/locations/us-central1/connections/\
    my-connection/gitRepositoryLinks/my-git-repository-link \
        --clone-uri=https://github.com/my-org/my-repo.git \
        --location=us-central1

POSITIONAL ARGUMENTS
    

GitRepositoryLink resource - Identifier. Resource name of the repository, in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GIT_REPOSITORY_LINK`
     ID of the gitRepositoryLink or fully qualified identifier for the gitRepositoryLink. 

To set the `git_repository_link` attribute: 

  * provide the argument `git_repository_link` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--connection`=`CONNECTION`
     The connection id of the gitRepositoryLink resource. 

To set the `connection` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--connection` on the command line. 


`--location`=`LOCATION`
     The location id of the gitRepositoryLink resource. 

To set the `location` attribute: 

  * provide the argument `git_repository_link` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--clone-uri`=`CLONE_URI`
     Git Clone URI. 
OPTIONAL FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     Allows clients to store small amounts of arbitrary data. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 
`--labels`=[`LABELS`,…]
     Labels as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--validate-only`
     If set, validate the request, but do not actually post it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `developerconnect/v1` API. The full documentation for this API can be found at: <http://cloud.google.com/developer-connect/docs/overview>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud developer-connect connections git-repository-links create](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/create)
    
    
    [gcloud beta developer-connect connections git-repository-links](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect/connections/git-repository-links) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
