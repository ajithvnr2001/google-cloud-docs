---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/register/
title: gcloud beta container fleet memberships register \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:19.159526+00:00
---

# gcloud beta container fleet memberships register  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/register/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container fleet memberships register Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container fleet memberships register - register a cluster with a fleet 
SYNOPSIS
    

`gcloud beta container fleet memberships register` (`MEMBERSHIP_NAME` : `--location`=`LOCATION`) (`--gke-cluster`=`LOCATION`/`CLUSTER_NAME` | `--gke-uri`=`GKE_URI` | [`--context`=`CONTEXT` : `--kubeconfig`=`KUBECONFIG`]) [`--install-connect-agent`] [`--internal-ip`] [`--manifest-output-file`=`MANIFEST_OUTPUT_FILE`] [`--proxy`=`PROXY`] [`--service-account-key-file`=`SERVICE_ACCOUNT_KEY_FILE` | [`--enable-workload-identity` : `--has-private-issuer` | `--public-issuer-url`=`PUBLIC_ISSUER_URL`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command registers a cluster with the fleet by: 
    
    
    1. Creating a Fleet Membership resource corresponding to the cluster.
    2. Adding in-cluster Kubernetes Resources that make the cluster exclusive
       to one fleet.
    3. Installing the Connect agent into this cluster (optional for GKE).

A successful registration implies that the cluster is now exclusive to a single Fleet. If the cluster is already registered to another Fleet, the registration will not be successful. 

To register a GKE cluster, use `--gke-cluster` or `--gke-uri` flag (no `--kubeconfig` flag is required). Connect agent will not be installed by default for GKE clusters. To install it, specify `--install-connect-agent`. The default value for `--location` is the same as the cluster's region or zone, can be specified as `global`. 

Anthos clusters on VMware, bare metal, AWS, and Azure are registered with a fleet when the clusters are created. To register Amazon EKS clusters, see [Attach your EKS cluster](https://cloud.google.com/anthos/clusters/docs/multi-cloud/attached/eks/how-to/attach-cluster). To regiser Microsoft Azure clusters, see [Attach your AKS cluster](https://cloud.google.com/anthos/clusters/docs/multi-cloud/attached/aks/how-to/attach-cluster). 

To register a third-party cluster, use --context flag (with an optional \--kubeconfig flag). Connect agent will always be installed for these clusters. 

If Connect agent is to be installed, its authentication needs to be configured by `--enable-workload-identity` or `--service-account-key-file`. For the latter case, the corresponding service account must have been granted `gkehub.connect` permissions. For more information about Connect agent, go to: <https://cloud.google.com/anthos/multicluster-management/connect/overview/>

Rerunning this command against the same cluster with the same MEMBERSHIP_NAME and target fleet is successful, and will upgrade the Connect agent if it is supposed to be installed and a newer version is available. Rerunning with `--enable-workload-identity` ensures that Workload Identity is enabled on the cluster. 

EXAMPLES
     Register a non-GKE cluster referenced from a specific kubeconfig file, and install the Connect agent: 
    
    
    gcloud beta container fleet memberships register my-cluster --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --service-account-key-file=/tmp/keyfile.json

Register a non-GKE cluster referenced from the default kubeconfig file, and install the Connect agent: 
    
    
    gcloud beta container fleet memberships register my-cluster --context=my-cluster-context --service-account-key-file=/tmp/keyfile.json

Register a non-GKE cluster, and install a specific version of the Connect agent: 
    
    
    gcloud beta container fleet memberships register my-cluster --context=my-cluster-context --version=gkeconnect_20190802_02_00 --service-account-key-file=/tmp/keyfile.json

Register a non-GKE cluster and output a manifest that can be used to install the Connect agent by kubectl: 
    
    
    gcloud beta container fleet memberships register my-cluster --context=my-cluster-context --manifest-output-file=/tmp/manifest.yaml --service-account-key-file=/tmp/keyfile.json

Register a GKE cluster referenced from a GKE URI: 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-uri=my-cluster-gke-uri

Register a GKE cluster referenced from a GKE URI, and install the Connect agent using service account key file: 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-uri=my-cluster-gke-uri --install-connect-agent --service-account-key-file=/tmp/keyfile.json

Register a GKE cluster and output a manifest that can be used to install the Connect agent by kubectl: 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-uri=my-cluster-gke-uri --enable-workload-identity --install-connect-agent --manifest-output-file=/tmp/manifest.yaml

Register a GKE cluster first, and install the Connect agent later. 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster
    
    
    gcloud beta container fleet memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster --install-connect-agent --enable-workload-identity

Register a GKE cluster, and install a specific version of the Connect agent: 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-cluster=my-cluster-region-or-zone/my-cluster --install-connect-agent --version=20220819-00-00 --service-account-key-file=/tmp/keyfile.json

Register a GKE cluster and output a manifest that can be used to install the Connect agent: 
    
    
    gcloud beta container fleet memberships register my-cluster --gke-uri=my-cluster-gke-uri --install-connect-agent --manifest-output-file=/tmp/manifest.yaml --service-account-key-file=/tmp/keyfile.json

POSITIONAL ARGUMENTS
    

Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MEMBERSHIP_NAME`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the membership resource, e.g. `us-central1`. If not specified, defaults to `global`. Not supported for GKE clusters, whose membership location will be the location of the cluster. To set the `location` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


REQUIRED FLAGS
    

Cluster identifier. 

Exactly one of these must be specified: 

`--gke-cluster`=`LOCATION`/`CLUSTER_NAME`
     The location/name of the GKE cluster. The location can be a zone or a region for e.g `us-central1-a/my-cluster`. 
`--gke-uri`=`GKE_URI`
     The URI of a GKE cluster that you want to register to Hub; for example, 'https://container.googleapis.com/v1/projects/my-project/locations/us-central1-a/clusters/my-cluster'. To obtain the URI, you can run 'gcloud container clusters list --uri'. Note that this should only be provided if the cluster being registered is a GKE cluster. The service will validate the provided URI to confirm that it maps to a valid GKE cluster." 
Or at least one of these can be specified: 

Non-GKE cluster identifier. 
`--context`=`CONTEXT`
     The cluster context as it appears in the kubeconfig file. You can get this value from the command line by running command: `kubectl config current-context`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kubeconfig`=`KUBECONFIG`
     The kubeconfig file containing an entry for the cluster. Defaults to $KUBECONFIG if it is set in the environment, otherwise defaults to $HOME/.kube/config. 
OPTIONAL FLAGS
    

`--install-connect-agent`
     If set to True for a GKE cluster, Connect agent will be installed in the cluster. No-op for Non-GKE clusters, where Connect agent will always be installed. 
`--internal-ip`
     Whether to use the internal IP address of the cluster endpoint. 
`--manifest-output-file`=`MANIFEST_OUTPUT_FILE`
     The full path of the file into which the Connect agent installation manifest should be stored. If this option is provided, then the manifest will be written to this file and will not be deployed into the cluster by gcloud, and it will need to be deployed manually. 
`--proxy`=`PROXY`
     The proxy address in the format of http[s]://{hostname}. The proxy must support the HTTP CONNECT method in order for this connection to succeed. 
At most one of these can be specified: 

`--service-account-key-file`=`SERVICE_ACCOUNT_KEY_FILE`
     The JSON file of a Google Cloud service account private key. This service account key is stored as a secret named ``creds-gcp`` in gke-connect namespace. To update the ``creds-gcp`` secret in gke-connect namespace with a new service account key file, run the following command: 

kubectl delete secret creds-gcp -n gke-connect 

kubectl create secret generic creds-gcp -n gke-connect \--from-file=creds-gcp.json=/path/to/file 

Or at least one of these can be specified: 

Workload Identity 
`--enable-workload-identity`
     Enable Workload Identity when registering the cluster with a fleet. Ensure that GKE Workload Identity is enabled on your GKE cluster, it is a requirement for using Workload Identity with memberships. Refer to the `Enable GKE Workload Identity` section in <https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable> \--service_account_key_file flag should not be set if this is set. 

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--has-private-issuer`
     Set to true for clusters where no publicly-routable OIDC discovery endpoint for the Kubernetes service account token issuer exists. 

When set to true, the gcloud command-line tool will read the private issuer URL and JSON Web Key Set (JWKS) (public keys) for validating service account tokens from the cluster's API server and upload both when creating the Membership. Google Cloud Platform will then use the JWKS, instead of a public OIDC endpoint, to validate service account tokens issued by this cluster. Note the JWKS establishes the uniqueness of issuers in this configuration, but issuer claims in tokens are still compared to the issuer URL associated with the Membership when validating tokens. 

Note the cluster's OIDC discovery endpoints ([KUBE-API-ADDRESS](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/register/)/.well-known/openid-configuration and [KUBE-API-ADDRESS](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/register/)/openid/v1/jwks) must still be network-accessible to the gcloud client running this command. 

`--public-issuer-url`=`PUBLIC_ISSUER_URL`
     Skip auto-discovery and register the cluster with this issuer URL. Use this option when the OpenID Provider Configuration and associated JSON Web Key Set for validating the cluster's service account JWTs are served at a public endpoint different from the cluster API server. Requires \--enable-workload-identity. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container fleet memberships register](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/register)
    
    
    [gcloud alpha container fleet memberships register](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships/register)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
