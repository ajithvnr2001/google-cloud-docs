---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/register/
title: gcloud alpha container attached clusters register \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:14.866300+00:00
---

# gcloud alpha container attached clusters register  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/register/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container attached clusters register Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container attached clusters register - register an Attached cluster 
SYNOPSIS
    

`gcloud alpha container attached clusters register` (`CLUSTER` : `--location`=`LOCATION`) `--distribution`=`DISTRIBUTION` `--fleet-project`=`FLEET_PROJECT` `--platform-version`=`PLATFORM_VERSION` (`--context`=`CONTEXT` : `--kubeconfig`=`KUBECONFIG`) (`--has-private-issuer` | `--issuer-url`=`ISSUER_URL`) [`--admin-groups`=[`GROUP`,…]] [`--admin-users`=[`USER`,…]] [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]] [`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`] [`--description`=`DESCRIPTION`] [`--enable-managed-prometheus`] [`--logging`=`COMPONENT`,[`COMPONENT`,…]] [`--system-component-labels`=[`LABEL`,…]] [`--system-component-tolerations`=[`TOLERATION`,…]] [`--tags`=`TAG`,[`TAG`,…]] [`--validate-only`] [`--disable-cloud-monitoring` | `--enable-cloud-monitoring`] [`--proxy-secret-name`=`PROXY_SECRET_NAME` `--proxy-secret-namespace`=`PROXY_SECRET_NAMESPACE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Register an Attached cluster. 
EXAMPLES
     Register a cluster to a fleet. 

To register a cluster with a private OIDC issuer, run: 
    
    
    gcloud alpha container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --has-private-issuer

To register a cluster with a public OIDC issuer, run: 
    
    
    gcloud alpha container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --issuer-url=https://ISSUER_URL

To specify a kubeconfig file, run: 
    
    
    gcloud alpha container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --has-private-issuer --kubeconfig=KUBECONFIG_PATH

To register and set cluster admin users, run: 
    
    
    gcloud alpha container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --issuer-url=https://ISSUER_URL --admin-users=USER1,USER2

To specify custom tolerations and labels for system component pods, run: 
    
    
    gcloud alpha container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --system-component-tolerations=TOLERATIONS --system-component-labels=LABELS

where TOLERATIONS have the format:
    
    
    key=value:Effect:NoSchedule (examples: key1=value1:Equal:NoSchedule,key2:Exists:PreferNoSchedule, :Exists:NoExecute)
     and LABELS have the format:key=value (examples: key1=value1,key2="")

POSITIONAL ARGUMENTS
    

Cluster resource - cluster to register. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location for the cluster. 

To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_attached/location`. 


REQUIRED FLAGS
    

`--distribution`=`DISTRIBUTION`
     Set the base platform type of the cluster to attach. 

Examples: 
    
    
    gcloud alpha container attached clusters register --distribution=aks
    gcloud alpha container attached clusters register --distribution=eks
    gcloud alpha container attached clusters register --distribution=generic

`--fleet-project`=`FLEET_PROJECT`
     ID or number of the Fleet host project where the cluster is registered. 
`--platform-version`=`PLATFORM_VERSION`
     Platform version to use for the cluster. 

To retrieve a list of valid versions, run: 
    
    
    [gcloud alpha container attached get-server-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/get-server-config) --location=LOCATION

Replace ``LOCATION`` with the target Google Cloud location for the cluster. 

kubectl config 

This must be specified. 

`--context`=`CONTEXT`
     Context to use in the kubeconfig. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kubeconfig`=`KUBECONFIG`
     Path to the kubeconfig file. 

If not provided, the default at ~/.kube/config will be used. 

OIDC config 

Exactly one of these must be specified: 

`--has-private-issuer`
     Indicates no publicly routable OIDC discovery endpoint exists for the Kubernetes service account token issuer. 

If this flag is set, gcloud will read the issuer URL and JWKs from the cluster's api server. 

`--issuer-url`=`ISSUER_URL`
     Issuer url of the cluster to attach. 
OPTIONAL FLAGS
    

`--admin-groups`=[`GROUP`,…]
     Groups of users that can perform operations as a cluster administrator. 
`--admin-users`=[`USER`,…]
     Users that can perform operations as a cluster administrator. 
`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the cluster. 
`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`
     Set Binary Authorization evaluation mode for this cluster. `BINAUTHZ_EVALUATION_MODE` must be one of: `DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`. 
`--description`=`DESCRIPTION`
     Description for the cluster. 
`--enable-managed-prometheus`
     Enables managed collection for Managed Service for Prometheus in the cluster. 

See <https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke> for more info. 

Managed Prometheus is enabled by default for cluster versions 1.27 or greater, use --no-enable-managed-prometheus to disable. 

`--logging`=`COMPONENT`,[`COMPONENT`,…]
     Set the components that have logging enabled. 

Examples: 
    
    
    gcloud alpha container attached clusters register --logging=SYSTEM
    gcloud alpha container attached clusters register --logging=SYSTEM,WORKLOAD
    gcloud alpha container attached clusters register --logging=NONE

`COMPONENT` must be one of: `NONE`, `SYSTEM`, `WORKLOAD`. 

`--system-component-labels`=[`LABEL`,…]
     Kubernetes labels to be applied to system component pods. 
`--system-component-tolerations`=[`TOLERATION`,…]
     Kubernetes tolerations to be applied to system component pods. 
`--tags`=`TAG`,[`TAG`,…]
     Tag keys/values directly bound to this resource. 

The short name of a tag key or value can have a maximum length of 256 characters. The permitted character set for the short name includes UTF-8 encoded Unicode characters except single quotes, double quotes, backslashes, and forward slashes. 

`--validate-only`
     Validate the cluster to create, but don't actually perform it. 
Cloud Monitoring Config 

At most one of these can be specified: 

`--disable-cloud-monitoring`
     Disables managed collection for Cloud Monitoring in the cluster. 

Cloud Monitoring is enabled by default for all clusters. Beginning with cluster version 1.31, use --disable-cloud-monitoring to disable. 

`--enable-cloud-monitoring`
     Enables managed collection for Cloud Monitoring in the cluster. 

Cloud Monitoring is enabled by default for all clusters. Beginning with cluster version 1.31, use --disable-cloud-monitoring to disable. 

Proxy config 
`--proxy-secret-name`=`PROXY_SECRET_NAME`
     Name of the Kubernetes secret that contains the HTTP/HTTPS proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--proxy-secret-namespace`=`PROXY_SECRET_NAMESPACE`
     Namespace of the Kubernetes secret that contains the HTTP/HTTPS proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud container attached clusters register](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
