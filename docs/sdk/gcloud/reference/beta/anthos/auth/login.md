---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/anthos/auth/login/
title: gcloud beta anthos auth login \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:09.311848+00:00
---

# gcloud beta anthos auth login  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/anthos/auth/login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta anthos auth login Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta anthos auth login - authenticate clusters using the Anthos client 
SYNOPSIS
    

`gcloud beta anthos auth login` [`--no-browser`] [`--cluster`=`CLUSTER`] [`--dry-run`] [`--kubeconfig`=`KUBECONFIG`] [`--login-config`=`LOGIN_CONFIG`] [`--login-config-cert`=`LOGIN_CONFIG_CERT`] [`--remote-bootstrap`=`REMOTE_BOOTSTRAP`] [`--server`=`SERVER`] [`--set-preferred-auth`] [`--user`=`USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Authenticate clusters using the Anthos client. 
EXAMPLES
     To add credentials to default kubeconfig file: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml

To add credentials to custom kubeconfig file: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml --kubeconfig=my.kubeconfig

To generate the commands without executing them: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml --dry-run

To add credentials to default kubeconfig file using server side login: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --server=<server-url>

To add credentials to custom kubeconfig file using server side login: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --server=<server-url> --kubeconfig=my.kubeconfig

To add credentials to custom kubeconfig file with server side login using a remote-device for login: 
    
    
    gcloud beta anthos auth login --cluster=testcluster --server=<server-url> --kubeconfig=my.kubeconfig --no-browser

FLAGS
    

`--no-browser`
     Option to indicate login completion on a second device with browser.Used with `server` option. 
`--cluster`=`CLUSTER`
     Cluster to authenticate against. If no cluster is specified, the command will print a list of available options. 
`--dry-run`
     Print out the generated kubectl commands but do not execute them. 
`--kubeconfig`=`KUBECONFIG`
     Specifies the destination kubeconfig file where credentials will be stored. 
`--login-config`=`LOGIN_CONFIG`
     Specifies the configuration yaml file for login. Can be a file path or a URL. 
`--login-config-cert`=`LOGIN_CONFIG_CERT`
     Specifies the CA certificate file to be added to trusted pool for making HTTPS connections to a `--login-config` URL. 
`--remote-bootstrap`=`REMOTE_BOOTSTRAP`
     Option to complete login that was started using `no-browser` optionon a remote device that does not have a browser. 
`--server`=`SERVER`
     Specifies the URL of API server of the cluster to authenticate against. 
`--set-preferred-auth`
     If set, forces update of preferred authentication for given cluster 
`--user`=`USER`
     If configuring multiple user accounts in the same kubecconfig file, you can specify a user to differentiate between them. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud anthos auth login](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/auth/login)
    
    
    [gcloud alpha anthos auth login](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/anthos/auth/login)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
