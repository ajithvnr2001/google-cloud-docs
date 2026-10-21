---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/bmctl/
title: bmctl command reference \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:59.738474+00:00
---

# bmctl command reference  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/bmctl/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  bmctl command reference Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/bmctl)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/bmctl)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



`bmctl` is a command line tool for Google Distributed Cloud that simplifies cluster creation and management. This document is a comprehensive reference for `bmctl` commands and related flags.

## Before you begin

`bmctl` uses [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication#adc) to validate the `location` value in the cluster spec (`clusterOperations.location`) when it isn't set to `global`. This validation is required for many `bmctl` commands. For ADC to work, you need to do one of the following:

  * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable on you admin workstation to the path of a service account credential file.

  * Use gcloud CLI your user credentials as Application Default Credentials (ADC):
        
        gcloud auth application-default login
        




Some `bmctl` commands let you specify a path to a credentials file with a flag.

## backup

Back up Anthos clusters on bare metal information.

#### Options
    
    
      -h, --help   help for backup
    

### backup cluster

Back up an Anthos on bare metal cluster and save the backup into a tar file.
    
    
    backup cluster [flags]
    

#### Options
    
    
          --backup-file string                      path to the output backup files.
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
          --use-disk                                Perform the backup using the disk instead of in-memory buffer. This option only works when the command is run by the root user or with sudo.
          --yes                                     Perform the backup and do not prompt for confirmation (non-interactive mode).
    

For more information about backing up and restoring clusters with `bmctl`, see [Back up and restore clusters with bmctl](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/bmctl-backup-restore).

## check

Perform preflight or health checks on your clusters or your infrastructure.

#### Options
    
    
      -h, --help   help for check
    

### check add-ons

Check the operational health of cluster add-ons, such as `stackdriver-log-aggregator`, `stackdriver-log-forwarder`, and `gke-connect-agent`. 
    
    
    check add-ons [flags]
    

#### Examples
    
    
    # Do a health check for add-ons
    bmctl check add-ons --cluster=cluster1
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for add-ons
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### check cluster

Check the health of a cluster or generate a cluster snapshot.
    
    
    check cluster [flags]
    

#### Examples
    
    
    # Do a health check for cluster.
    bmctl check cluster --cluster=cluster1
    # Take a snapshot of the cluster (requires admin cluster to be available).
    bmctl check cluster --snapshot --cluster=cluster1 --admin-kubeconfig=admin-kubeconfig
    # Take a snapshot of the cluster nodes only (does not require admin cluster to be available).
    bmctl check cluster --snapshot --cluster=cluster1 --snapshot-config=snapshot-config
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --login-user string                       The user to login to each node. This will be ignored when admin-kubeconfig is set. (default "root")
          --node-ssh-key string                     The file contains ssh key to the nodes to capture snapshots against. While this flag is fully optional, when provided, nodes must also be provided.
          --nodes strings                           The comma-separated IP address list of the nodes to capture snapshots against. While this flag is fully optional, when provided, node-ssh-key must also be provided.
          --quiet                                   During snapshot run suppress logging to stdout.  (Console log is available in 'bmctl_diagnose_snapshot.log' file part of the snapshot)
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
          --service-account-key-file string         The service account key file for uploading the snapshot. Please make sure this service account has the "roles/storage.admin" of its parent project for creating a Cloud Storage bucket and writing object to the bucket. Note that:
                                                    - this flag is defaulted to the environment variable GOOGLE_APPLICATION_CREDENTIALS, if not provided.
                                                    - this flag is ignored, if "--upload-to" flag is empty.
          --since duration                          This Only returns logs newer than a relative duration like 5s, 4m, or 3h. It defaults to all logs.
          --snapshot                                Takes a snapshot of the cluster's logs, configurations and other data if true.
          --snapshot-config string                  The config file of the snapshot. When this flag is omitted, a default configuration is applied.
          --snapshot-dry-run                        In dry-run mode, the command does not take the snapshot. Instead, it prints out the actions to be taken and the snapshot configuration.
          --snapshot-output string                  The output file of the snapshot.
          --snapshot-scenario string                The scenario of the snapshot. This is ignored when --config flag is specified. The supported scenarios are:
                                                    - system: snapshot of system components, including their logs
                                                    - all: snapshot of all pods, including their logs (default "system")
          --snapshot-temp-output-dir string         The temporary landing directory for snapshot.
          --upload-to string                        The Cloud Storage bucket name for uploading the snapshot. A new bucket will be created if it doesn't exist. Please follow the naming guidelines here(https://cloud.google.com/storage/docs/naming-buckets). 
    

### check config

Check the cluster configuration file.
    
    
    check config [flags]
    

#### Examples
    
    
    # Do check for cluster1.yaml file
    bmctl check config --cluster=cluster1
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for config
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### check gcp

Cluster connectivity to Google Cloud health check.
    
    
    check gcp [flags]
    

#### Examples
    
    
    # Do a machines' Google Cloud connectivity health check for cluster
    bmctl check gcp --cluster=cluster1
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for gcp
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### check kubernetes

Kubernetes health check.
    
    
    check kubernetes [flags]
    

#### Examples
    
    
    # Do a kubernetes health check for cluster
    bmctl check kubernetes --cluster=cluster1
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for kubernetes
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### check nodes

Check nodes health.
    
    
    check nodes [flags]
    

#### Examples
    
    
    # Do a health check for some provisioned nodes
    bmctl check nodes --addresses=192.168.0.1,192.168.0.4
    

#### Options
    
    
          --addresses strings                       Node addresses, addresses should be a comma separated list, each address needs be a single IP address(e.g., 192.168.0.1)
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for nodes
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### check preflight

Preflight check.

#### Synopsis

Preflight check.
    
    
    check preflight [flags]
    

#### Examples
    
    
    # Do a preflight check for cluster1.yaml in bmctl-workspace/cluster1
    bmctl check preflight --cluster=cluster1. If kubeconfig flag (for example, --kubeconfig=bmctl-workspace/cluster1/cluster1-kubeconfig) is included, the command will trigger a preflight check for upgrading the cluster
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for preflight
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

For more information about preflight checks, see [Understand preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight).

## create

Create a cluster configuration file, a cluster, or a Kubernetes service account (KSA).

#### Options
    
    
      -h, --help   help for create
    

### create cluster

Create a cluster from a cluster configuration file.

#### Synopsis

Create Anthos bare metal resources. This command will emit a kubeconfig of created cluster. Be sure to keep this file safe as it contains credentials for your cluster. This command requires serviceusage.services.get permission to check API enablement for your Google Cloud project.
    
    
    create cluster [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --force                                   If true, ignore errors from preflight checks and validation except for Google Cloud check errors.
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

For more information about creating clusters, see [Cluster creation overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview).

### create config

Create a cluster configuration file. By default, this file is created in the bmctl-workspace/ folder.
    
    
    create config [flags]
    

#### Options
    
    
      -c, --cluster cluster name      Cluster name, must consist of lower case alphanumeric characters or '-', start with an alphabetic character, and end with an alphanumeric character
          --create-service-accounts   Auto create Google Cloud service accounts keys, if they do not already exist in workspace
          --enable-apis               Auto enable APIs used by Anthos Bare Metal cluster, for the Google Cloud project specified by project-id flag
          --force                     Overwrite existing config
      -h, --help                      help for config
          --project-id string         Google Cloud project where the new cluster will connect with via GKE hub and stackdriver logging/monitoring, required if --create-service-accounts or --enable-apis is true
    

### create ksa

Create a Kubernetes service account with the cluster-admin role of the target cluster. The default name of the Kubernetes service account is “kubernetes-service-account”, so the “--name” flag is optional. The command generates a bearer token that you can use to log in to the cluster. By default, the bearer token is stored in the bmctl-workspace/ folder.
    
    
    create ksa [flags]
    

#### Options
    
    
      -c, --cluster string      Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml.
      -h, --help                help for ksa
          --ksa-name string     Name of the kubernetes service account and default value is kubernetes-service-account. (default "kubernetes-service-account")
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

## disable

Disable Anthos VM Runtime in a cluster.

#### Options
    
    
      -h, --help   help for disable
    

### disable vmruntime

Disable Anthos VM Runtime in a cluster.
    
    
    disable vmruntime [flags]
    

#### Options
    
    
          --force               If true, delete all VM resources and disable vmruntime.
      -h, --help                help for vmruntime
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

For more information about enabling and disabling VM Runtime on GDC, see [Enable or disable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/enable-disable).

## enable

Enable Anthos VM Runtime in a cluster.

#### Options
    
    
      -h, --help   help for enable
    

### enable vmruntime

Enable Anthos VM Runtime in a cluster.
    
    
    enable vmruntime [flags]
    

#### Options
    
    
      -h, --help                help for vmruntime
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

For more information about enabling and disabling VM Runtime on GDC, see [Enable or disable VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/enable-disable).

## enroll

Enroll a cluster so that it can be managed by the Anthos On-Prem API.

#### Options
    
    
      -h, --help   help for enroll
    

### enroll cluster

Enroll a cluster so that it can be managed by the Anthos On-Prem API. This enrollment enables cluster management through clients, such as the Google Cloud console and the gcloud CLI.
    
    
    enroll cluster [flags]
    

#### Options
    
    
      -c, --cluster string                 Cluster name.
          --cluster-resource-name string   Unique cluster name within a Google Cloud project/fleet. It is defaulted to be the same as the --cluster-name and they should be the same if possible. In case there is already another cluster with the same name enrolled in the project/fleet previously (under another admin cluster), this flag can be used to rename the cluster within the Google Cloud project/fleet.
      -h, --help                           help for cluster
          --kubeconfig string              Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --location location              The Google Cloud location to enroll the user cluster. The "us-west1" location is the default. (default us-west1)
    

For more information about enrolling a cluster, see [Configure a cluster to be managed by the Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/enroll-cluster).

## get

Get a cluster configuration or cluster credentials.

#### Options
    
    
      -h, --help   help for get
    

### get config

Get the cluster configuration file. The command pulls custom resources of the target cluster and emits a configuration file.
    
    
    get config [flags]
    

#### Options
    
    
      -c, --cluster string      Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml.
      -h, --help                help for config
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

### get credentials

Get target cluster credentials. The command creates a kubeconfig file in the / folder on the admin workstation.
    
    
    get credentials [flags]
    

#### Options
    
    
      -c, --cluster string      Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml.
      -h, --help                help for credentials
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

## install

Performs software installation operations.

#### Options
    
    
      -h, --help   help for install
    

### install virtctl

Install virtctl into the current machine as a kubectl plugin. The virtctl plugin supports basic VM operations, such as create, connect, and change power state.
    
    
    install virtctl [flags]
    

#### Options
    
    
      -d, --dst-dir string   The dir virtctl binary to be installed, this path must be a valid one within PATH env variable
      -h, --help             help for virtctl
    

## move

Move Anthos bare metal resources and all dependencies between management clusters.

  * Target cluster namespace can contain additional resources, conflicting resources are replaced.


    
    
    move [flags]
    

#### Options
    
    
          --cluster-move-timeout duration    Cluster move timeout, default value is 15m. The input should contain the duration unit, e.g. 3600s, 60m or 1h. (default 15m0s)
          --from-kubeconfig string           kubeconfig file path for the source management cluster. If unspecified, will use the default discovered kubeconfig.
          --from-kubeconfig-context string   Context to be used within the kubeconfig file for the source management cluster. If empty, current context will be used.
      -h, --help                             help for move
      -n, --namespace string                 The namespace where the cluster resources are stored. If unspecified, the current context's namespace is used.
          --to-kubeconfig string             kubeconfig file path for the destination management cluster.
          --to-kubeconfig-context string     Context to be used within the kubeconfig file for the destination management cluster. If empty, current context will be used.
    

## push

Push docker images to a private registry.

#### Options
    
    
      -h, --help   help for push
    

### push images

Push local container images tar file to a private registry.
    
    
    push images [flags]
    

#### Options
    
    
          --cacert string             Private registry CA certificate file path.
          --dry-run                   Dry run.
          --email string              Email for private registry.
          --force-push                If set to true, will always push images even if images already exist in registry.
      -h, --help                      help for images
          --need-credential           Whether credential is needed for private registry. (default true)
          --password string           Password for private registry authentication.
      -r, --private-registry string   Private registry path that stores all Anthos Bare Metal images.
                                      Format should be <registry-name>/<optional-registry-namespace>.
          --source string             Path to Anthos Bare Metal container images compressed file.
      -t, --threads int               Push images with multiple threads. (default 4)
          --username string           Username for private registry authentication.
    

### register bootstrap

Register bootstrap cluster to the Hub API.

#### Synopsis

Register the bootstrap cluster to the Hub API. This command registers a local Kind cluster as an admin cluster. The command waits for a cluster to be created in the Google Cloud console and exits once the cluster is created successfully.
    
    
    register bootstrap [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string            Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string        Bootstrap cluster service CIDR (default "10.96.0.0/27")
          --cloud-operation-service-account-key string   Optional, service account key file used to access Google cloud service, service account key specified by environment variable GOOGLE_APPLICATION_CREDENTIALS will be used to fetch or create the Service account.
          --gcr-service-account-key string               Optional, service account key file used to pull GCR images, service account key specified by environment variable GOOGLE_APPLICATION_CREDENTIALS will be used to fetch or create the Service account.
          --gke-agent-service-account-key string         Optional, service account key file used to connect the GKE cluster in Google Cloud, service account key specified by environment variable GOOGLE_APPLICATION_CREDENTIALS will be used to fetch or create the Service account.
          --gke-register-service-account-key string      Optional, service account key file used to register the cluster in Google Cloud, service account key specified by environment variable GOOGLE_APPLICATION_CREDENTIALS will be used to fetch or create the Service account.
          --gkehub-endpoint gkehub-endpoint              Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                         help for bootstrap
          --ignore-validation-errors                     A validation error override, allowing to proceed despite the validation errors.
          --name string                                  Mandatory, Name of the bootstrap cluster. bmctl will register the bootstrap cluster with this name with GKE Connect.
          --project-id string                            Optional, Google Cloud project for GKE Connect. bmctl will register this bootstrap cluster into Google Cloud project temporarily, and un-register it after cluster is provisioned successfully.
          --registry-mirror-ca string                    Registry mirror CA file.
          --registry-mirror-credential string            Registry mirror credential file.
          --registry-mirror-endpoint string              Registry mirror endpoint.
          --reuse-bootstrap-cluster                      If true, use existing bootstrap cluster.
          --ssh-client-cert string                       Optional, Path of the SSH certificate. ABM will use this ssh key certificate while sshing in the machines.
          --ssh-key string                               Mandatory, Path of the SSH key. ABM will use this ssh key while sshing in the machines.
    

## reset

Reset cluster machines to the state prior to installation.

#### Synopsis

This command tries to undo changes performed in prior installation attempts. It's a best effort attempt meant to be used to recover from partial installation failures.
    
    
    reset [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for reset
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### reset bootstrap

Delete the bootstrap cluster.
    
    
    reset bootstrap [flags]
    

#### Examples
    
    
    bmctl reset bootstrap
    

#### Options
    
    
      -h, --help   help for bootstrap
    

### reset nodes

Reset specified nodes to the state that they were in prior to installing Anthos clusters on bare metal.
    
    
    reset nodes [flags]
    

#### Examples
    
    
    bmctl reset nodes --addresses 10.200.0.3,10.200.0.4 --ssh-private-key-path /root/.ssh/id_rsa --login-user root --gcr-service-account-key gcr.json
    

#### Options
    
    
          --addresses strings                       Node addresses, addresses should be a comma separated list, each address needs be a single IP address(e.g., 192.168.0.1)
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --force                                   Optional. If provided, nodes will be forcefully removed from the cluster without running reset jobs.
          --gcr-service-account-key string          Optional, path to the service account json key to pull gcr images. Mutually exclusive with --cluster flag. If not provided, the environment variable GOOGLE_APPLICATION_CREDENTIALS will be used.
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for nodes
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --login-user string                       login user to use to connect to the nodes. Mutually exclusive with --cluster flag. Optional and should be used together with --ssh-private-key-path. Default to root.
          --registry-mirror-ca string               Registry mirror CA file.
          --registry-mirror-credential string       Registry mirror credential file.
          --registry-mirror-endpoint string         Registry mirror endpoint.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
          --ssh-private-key-path string             path to the ssh private key to connect to the nodes. Either --cluster or --ssh-private-key-path should be provided, but not both. Use this flag to reset the machines if the original cluster yaml is no longer available.
    

For more information about using `bmctl reset nodes` to return cluster nodes to their pre-installation state or deleting clusters, see [Reset nodes and delete clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16).

## restore

Restore a cluster or attempt to regain quorum for a cluster.

#### Synopsis

Restore an Anthos on bare metal cluster. When used without the cluster sub-command, this command attempts to restore a high-availability cluster from a quorum loss. When used with the cluster sub-command, the command restores a cluster from a backup file.
    
    
    restore [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --control-plane-node string               IP for the surviving host address, should be a single IP address(e.g., 192.168.0.1).
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for restore
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       kubeconfig file path for the management cluster. This only needs to be provided if restoring a broken user cluster.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

### restore cluster

Restore an Anthos on bare metal cluster from a backup file.
    
    
    restore cluster [flags]
    

#### Options
    
    
          --backup-file string                      path to the backup file of the cluster.
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       path to the kubeconfig of the management cluster.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
          --use-disk                                Perform the restore using the disk instead of in-memory buffer. This option only works when the command is run by the root user or with sudo.
    

For more information about backing up and restoring clusters with `bmctl`, see [Back up and restore clusters with bmctl](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/bmctl-backup-restore).

## unenroll

Unenroll a cluster.

#### Options
    
    
      -h, --help   help for unenroll
    

### unenroll cluster

Unenroll an Anthos on bare metal cluster. This command disables the ability to manage the cluster with the Anthos On-Prem API. Unenrollment disables the ability to manage the cluster through the Google Cloud console and the gcloud CLI.
    
    
    unenroll cluster [flags]
    

#### Options
    
    
      -c, --cluster string      Cluster name.
      -h, --help                help for cluster
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

## update

Update Anthos clusters on bare metal resources.

#### Options
    
    
      -h, --help   help for update
    

### update cluster

Update cluster and node pool configurations. This command applies the changes made in the cluster configuration file. By default, the configuration file, .yaml is stored in the bmctl-workspace// folder on the admin workstation.
    
    
    update cluster [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

For more information about updating clusters with `bmctl`, see [Update clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters). To see which cluster configuration files are mutable, see [Cluster configuration field reference](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref#cluster_configuration_fields).

### update credentials

Update cluster credentials.

#### Synopsis

Update credentials of Anthos on bare metal clusters. This command updates admin cluster credentials and the credentials of user clusters managed by the admin cluster.
    
    
    update credentials [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string                      Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string                  Bootstrap cluster service CIDR (default "10.96.0.0/27")
          --cloud-operations-service-account-key-path string       New credential: path to cloud operations service account  key.
      -c, --cluster cluster name                                   Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gcr-key-path string                                    New credential: path to GCR service account key.
          --gke-connect-agent-service-account-key-path string      New credential: path to gke connect agent service account key.
          --gke-connect-register-service-account-key-path string   New credential: path to gke connect register service account key.
          --gkehub-endpoint gkehub-endpoint                        Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                                   help for credentials
          --ignore-validation-errors                               A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                                      Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                                If true, use existing bootstrap cluster.
          --ssh-private-key-path string                            New credential: path to ssh private key.
    

### update credentials certificate-authorities

Update certificate authorities on Anthos on bare metal clusters.

#### Options
    
    
      -h, --help   help for certificate-authorities
    

#### Options inherited from parent commands
    
    
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

### update credentials certificate-authorities rotate

Rotate certificate authorities.
    
    
    update credentials certificate-authorities rotate [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for rotate
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
    

#### Options inherited from parent commands
    
    
          --kubeconfig string   Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
    

## upgrade

Upgrade an Anthos on bare metal cluster in-place to a new version.

#### Options
    
    
      -h, --help   help for upgrade
    

### upgrade cluster

Upgrade an Anthos on bare metal cluster.

#### Synopsis

Upgrade an Anthos on bare metal cluster. This command reads the target version from the cluster configuration file and upgrades the target cluster to the specified version. All other changes in the cluster configuration file are ignored. The command requires serviceusage.services.get permission to check API enablement for the Google Cloud project specified in the configuration file.
    
    
    upgrade cluster [flags]
    

#### Options
    
    
          --bootstrap-cluster-pod-cidr string       Bootstrap cluster pod CIDR (default "192.168.122.0/24")
          --bootstrap-cluster-service-cidr string   Bootstrap cluster service CIDR (default "10.96.0.0/27")
      -c, --cluster cluster name                    Cluster name, cluster config is expected to be placed under <workspace dir>/<cluster name>/<cluster name>.yaml
          --cluster-update-timeout duration         Cluster update timeout, default value is 24h. The input should contain the duration unit, e.g. 3600s, 60m or 1h. (default 24h0m0s)
          --force                                   If true, ignore errors from preflight checks.
          --gkehub-endpoint gkehub-endpoint         Sets the URL endpoint for GKEHub API HTTP requests. Can be set to "prod", "staging" or "autopush". The "prod" endpoint is the default. (default prod)
      -h, --help                                    help for cluster
          --ignore-validation-errors                A validation error override, allowing to proceed despite the validation errors.
          --kubeconfig string                       Optional, path to the kubeconfig file for the admin cluster. IF not provided, will fall back to read env var ANTHOS_ADMIN_KUBECONFIG.
          --reuse-bootstrap-cluster                 If true, use existing bootstrap cluster.
          --skip-bootstrap-cidr-check               If true, skip checking CIDR and the number of nodes to determine whether upgrade would succeed.
    

For more information about cluster upgrades, see the following documentation:

  * [Upgrade clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade)
  * [Best practices for Google Distributed Cloud cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices)
  * [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle)



## version

Print the bmctl version.
    
    
    version [flags]
    

#### Options
    
    
      -h, --help            help for version
      -o, --output string   Output format of version string. Support version, commit.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
