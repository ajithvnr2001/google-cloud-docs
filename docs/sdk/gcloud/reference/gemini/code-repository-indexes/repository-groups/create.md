---
url: https://docs.cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create/
title: gcloud gemini code-repository-indexes repository-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:03:00.526302+00:00
---

# gcloud gemini code-repository-indexes repository-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/gemini/code-repository-indexes/repository-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud gemini code-repository-indexes repository-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud gemini code-repository-indexes repository-groups create - create a repository group for a given code repository index instance 
SYNOPSIS
    

`gcloud gemini code-repository-indexes repository-groups create` (`REPOSITORY_GROUP` : `--code-repository-index`=`CODE_REPOSITORY_INDEX` `--location`=`LOCATION`) [`--async`] [`--labels`=[`LABELS`,…]] [`--repositories`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`]] [`--request-id`=`REQUEST_ID`] [`--resources`=[`authConfig`=`AUTHCONFIG`],[`connection`=`CONNECTION`],[`sourceConfig`=`SOURCECONFIG`],[`type`=`TYPE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a repository group for a given code repository index instance. 
EXAMPLES
     To create a repository group `my-repository-group` for a code repository index instance `my-instance` in project `my-project` and location `us-central1` with one Developer Connect repository and branch pattern `.*`, run: 
    
    
    gcloud gemini code-repository-indexes repository-groups create my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1 --repositories=branchPattern=.*,resource=developerconnect.googleapis.com/projects/<PROJECT>/locations/<LOCATION>/connections/<CONNECTION>/gitRepositoryLinks/<REPOSITORY>

Developer Connect Git repository resource must already exist. Refer to [Developer Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details. 

To create a repository group `my-repository-group` for a code repository index instance `my-instance` in project `my-project` and location `us-central1` with a fully qualified name, run: 
    
    
    gcloud gemini code-repository-indexes repository-groups create projects/my-project/locations/us-central1/codeRepositoryIndexes/my-instance/repositoryGroups/my-repository-group --repositories=branchPattern=.*,resource=developerconnect.googleapis.com/projects/<PROJECT>/locations/<LOCATION>/connections/<CONNECTION>/gitRepositoryLinks/<REPOSITORY>

Developer Connect Git repository resource must already exist. Refer to [Developer Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details. 

To create a repository group `my-repository-group` for a code repository index instance `my-instance` in project `my-project` and location `us-central1` with Developer Connect repositories defined in a separate file, run: 
    
    
    gcloud gemini code-repository-indexes repository-groups create my-repository-group --code-repository-index=my-instance --project=my-project --location=us-central1 --repositories=@/path/to/repositories.json

Developer Connect Git repository resource must already exist. Refer to [Developer Connect documentation](http://cloud.google.com/developer-connect/docs/connect-repo) for more details. 

POSITIONAL ARGUMENTS
    

RepositoryGroup resource - Identifier. name of resource The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `repository_group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REPOSITORY_GROUP`
     ID of the repositoryGroup or fully qualified identifier for the repositoryGroup. 

To set the `repository_group` attribute: 

  * provide the argument `repository_group` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--code-repository-index`=`CODE_REPOSITORY_INDEX`
     The codeRepositoryIndex id of the repositoryGroup resource. 

To set the `code-repository-index` attribute: 

  * provide the argument `repository_group` on the command line with a fully specified name; 
  * provide the argument `--code-repository-index` on the command line. 


`--location`=`LOCATION`
     The location id of the repositoryGroup resource. 

To set the `location` attribute: 

  * provide the argument `repository_group` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
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

`--repositories`=[`branchPattern`=`BRANCHPATTERN`],[`resource`=`RESOURCE`]
     List of repositories to group. 

`branchPattern`
     The Git branch pattern used for indexing in RE2 syntax. See <https://github.com/google/re2/wiki/syntax> for syntax. 
`resource`
     The DeveloperConnect repository full resource name, relative resource name or resource URL to be indexed. 
`Shorthand Example:`
    
    
    --repositories=branchPattern=string,resource=string --repositories=branchPattern=string,resource=string

`JSON Example:`
    
    
    --repositories='[{"branchPattern": "string", "resource": "string"}]'

`File Example:`
    
    
    --repositories=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--resources`=[`authConfig`=`AUTHCONFIG`],[`connection`=`CONNECTION`],[`sourceConfig`=`SOURCECONFIG`],[`type`=`TYPE`]
     List of third party connection resources. 

`authConfig`
     The authentication configuration for the resource. 

`apiToken`
     API Token based authentication. 

`tokenSecretResource`
     The secret key for the API token. Example: projects/<project>/secrets/<secret>/versions/<version>. 
`username`
     The username for the API token. 
`connection`
     The DeveloperConnect connection full resource name, relative resource name or resource URL to be indexed. 
`sourceConfig`
     The source configuration for the resource. 

`confluenceConfig`
     Confluence source configuration. 

`pageId`
     The optional page ID of the Confluence page. 
`spaceKey`
     The space key of the Confluence space. 
`uri`
     The host address of the Confluence instance. 
`type`
     The type of the 3p resource. 
`Shorthand Example:`
    
    
    --resources=authConfig={apiToken={tokenSecretResource=string,username=string}},connection=string,sourceConfig={confluenceConfig={pageId=string,spaceKey=string,uri=string}},type=string --resources=authConfig={apiToken={tokenSecretResource=string,username=string}},connection=string,sourceConfig={confluenceConfig={pageId=string,spaceKey=string,uri=string}},type=string

`JSON Example:`
    
    
    --resources='[{"authConfig": {"apiToken": {"tokenSecretResource": "string", "username": "string"}}, "connection": "string", "sourceConfig": {"confluenceConfig": {"pageId": "string", "spaceKey": "string", "uri": "string"}}, "type": "string"}]'

`File Example:`
    
    
    --resources=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudaicompanion/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/gemini>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
