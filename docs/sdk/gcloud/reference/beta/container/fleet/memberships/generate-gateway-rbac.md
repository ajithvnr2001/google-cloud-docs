---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/generate-gateway-rbac/
title: gcloud beta container fleet memberships generate-gateway-rbac \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:30:22.201320+00:00
---

# gcloud beta container fleet memberships generate-gateway-rbac  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/generate-gateway-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container fleet memberships generate-gateway-rbac Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container fleet memberships generate-gateway-rbac - generate RBAC policy files for connected clusters by the user 
SYNOPSIS
    

`gcloud beta container fleet memberships generate-gateway-rbac` (`--anthos-support` | `--groups`=`GROUPS` | `--users`=`USERS`) [`--apply`] [`--context`=`CONTEXT`] [`--kubeconfig`=`KUBECONFIG`] [`--membership`=`MEMBERSHIP`] [`--rbac-output-file`=`RBAC_OUTPUT_FILE`] [`--revoke`] [`--role`=`ROLE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta container fleet memberships generate-gateway-rbac generates RBAC policies to be used by Connect Gateway API. 

Upon success, this command will write the output RBAC policy to the designated local file in dry run mode. 

Override RBAC policy: Y to override previous RBAC policy, N to stop. If overriding the --role, Y will clean up the previous RBAC policy and then apply the new one. 

EXAMPLES
     The current implementation supports multiple modes: 

Dry run mode to generate the RBAC policy file, and write to local directory: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --rbac-output-file=./rbac.yaml

Dry run mode to generate the RBAC policy, and print on screen: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin

Anthos support mode, generate the RBAC policy file with read-only permission for TSE/Eng to debug customers' clusters: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --anthos-support

Apply mode, generate the RBAC policy and apply it to the specified cluster: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply

Revoke mode, revoke the RBAC policy for the specified users: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --revoke

The role to be granted to the users can either be cluster-scoped or namespace-scoped. To grant a namespace-scoped role to the users in dry run mode, run: 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=role/mynamespace/namespace-reader

The users provided can be using a Google identity (only email) or using external identity providers (starting with "principal://iam.googleapis.com"): 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,principal://iam.googleapis.com/locations/global/workforcePools/pool/subject/user --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply

The groups can be provided as a Google identity (only email) or an external identity (starting with "principalSet://iam.googleapis.com"): 
    
    
    gcloud beta container fleet memberships generate-gateway-rbac --membership=my-cluster --groups=group@example.com,principalSet://iam.googleapis.com/locations/global/workforcePools/pool/group/ExampleGroup --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--anthos-support`
     If specified, this command will generate RBAC policy file for anthos support. 
`--groups`=`GROUPS`
     Group email address or third-party IAM group principal. 
`--users`=`USERS`
     User's email address, service account email address, or third-party IAM subject principal. 
OPTIONAL FLAGS
    

`--apply`
     If specified, this command will generate RBAC policy and apply to the specified cluster. 
`--context`=`CONTEXT`
     The cluster context as it appears in the kubeconfig file. You can get this value from the command line by running command: `kubectl config current-context`. 
`--kubeconfig`=`KUBECONFIG`
     The kubeconfig file containing an entry for the cluster. Defaults to $KUBECONFIG if it is set in the environment, otherwise defaults to $HOME/.kube/config. 
`--membership`=`MEMBERSHIP`
     Membership name to assign RBAC policy with. 
`--rbac-output-file`=`RBAC_OUTPUT_FILE`
     If specified, this command will execute in dry run mode and write to the file specified with this flag: the generated RBAC policy will not be applied to Kubernetes clusters,instead it will be written to the designated local file. 
`--revoke`
     If specified, this command will revoke the RBAC policy for the specified users. 
`--role`=`ROLE`
     Namespace scoped role or cluster role. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container fleet memberships generate-gateway-rbac](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac)
    
    
    [gcloud alpha container fleet memberships generate-gateway-rbac](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships/generate-gateway-rbac)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
