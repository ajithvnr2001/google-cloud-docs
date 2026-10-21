---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workstations/ssh/
title: gcloud alpha workstations ssh \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:42.244630+00:00
---

# gcloud alpha workstations ssh  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workstations/ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha workstations ssh Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha workstations ssh - SSH into a running workstation 
SYNOPSIS
    

`gcloud alpha workstations ssh` (`WORKSTATION` : `--cluster`=`CLUSTER` `--config`=`CONFIG` `--region`=`REGION`) [`--command`=`COMMAND`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--local-host-port`=`LOCAL_HOST_PORT`; default="localhost:0"] [`--port`=`PORT`; default=22] [`--ssh-flag`=`SSH_FLAG`] [`--start-workstation`] [`--user`=`USER`; default="user"] [`GCLOUD_WIDE_FLAG …`] [-- `SSH_ARGS` …]
DESCRIPTION
     `(ALPHA)` SSH into a running workstation. 

Note that arguments for the `NO_PROXY` environment variable must be FQDNs. 

EXAMPLES
     To ssh into a running workstation, run: 
    
    
    gcloud alpha workstations ssh WORKSTATION

To specify the workstation port, run: 
    
    
    gcloud alpha workstations ssh WORKSTATION --port=22

To ssh into a running workstation with a username, run: 
    
    
    gcloud alpha workstations ssh WORKSTATION --user=my-user

To run a command on the workstation, such as getting a snapshot of the guest's process tree, run:
    
    
    gcloud alpha workstations ssh WORKSTATION --command="ps -ejH"

POSITIONAL ARGUMENTS
    

Workstation resource - The group of arguments defining a workstation The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `workstation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`WORKSTATION`
     ID of the workstation or fully qualified identifier for the workstation. 

To set the `workstation` attribute: 

  * provide the argument `workstation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     The cluster for the workstation. 

To set the `cluster` attribute: 

  * provide the argument `workstation` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line; 
  * set the property `workstations/cluster`. 


`--config`=`CONFIG`
     The config for the workstation. 

To set the `config` attribute: 

  * provide the argument `workstation` on the command line with a fully specified name; 
  * provide the argument `--config` on the command line; 
  * set the property `workstations/config`. 


`--region`=`REGION`
     The region for the workstation. 

To set the `region` attribute: 

  * provide the argument `workstation` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `workstations/region`. 


[-- `SSH_ARGS` …]
     Flags and positionals passed to the underlying ssh implementation. 

The '--' argument must be specified between gcloud specific args on the left and SSH_ARGS on the right. 

FLAGS
    

`--command`=`COMMAND`
     A command to run on the workstation. 

Runs the command on the target workstation and then exits. 

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--local-host-port`=`LOCAL_HOST_PORT`; default="localhost:0"
     `LOCAL_HOST:LOCAL_PORT` on which gcloud should bind and listen for connections that should be tunneled. 

`LOCAL_PORT` may be omitted, in which case it is treated as 0 and an arbitrary unused local port is chosen. The colon also may be omitted in that case. 

If `LOCAL_PORT` is 0, an arbitrary unused local port is chosen. 

`--port`=`PORT`; default=22
     The port on the workstation to which traffic should be sent. 
`--ssh-flag`=`SSH_FLAG`
     Additional flags to be passed to `ssh(1)`. It is recommended that flags be passed using an assignment operator and quotes. Example: 
    
    
    gcloud alpha workstations ssh --ssh-flag="-vvv" --ssh-flag="-L 80:localhost:80"

`--start-workstation`
     If set, automatically starts the workstation if it is currently stopped. 
`--user`=`USER`; default="user"
     The username with which to SSH. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud workstations ssh](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/ssh)
    
    
    [gcloud beta workstations ssh](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workstations/ssh)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
