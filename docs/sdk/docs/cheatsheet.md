---
url: https://docs.cloud.google.com/sdk/docs/cheatsheet/
title: The gcloud CLI cheat sheet \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:42.483356+00:00
---

# The gcloud CLI cheat sheet  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/cheatsheet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  The gcloud CLI cheat sheet Stay organized with collections  Save and categorize content based on your preferences. 

A roster of go-to commands for the Google Cloud CLI, the primary command-line tool for Google Cloud.

(Also included: introductory primer, understanding commands, and a [printable PDF](https://docs.cloud.google.com/static/sdk/docs/images/gcloud-cheat-sheet.pdf).)

## Cheat sheet

### Getting started

Get going with the gcloud CLI.

  * [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init): Initialize, authorize, and configure the gcloud CLI.
  * [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version): Display version and installed components.
  * [`gcloud components install`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install): Install specific components.
  * [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update): Update your gcloud CLI to the latest version.
  * [`gcloud config set project`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set): Set a default Google Cloud project to work on.
  * [`gcloud info`](https://docs.cloud.google.com/sdk/gcloud/reference/info): Display current gcloud CLI environment details.



### Help

gcloud CLI is happy to help.

  * [`gcloud help`](https://docs.cloud.google.com/sdk/gcloud/reference/help): Search the gcloud CLI reference documents for specific terms.
  * [`gcloud feedback`](https://docs.cloud.google.com/sdk/gcloud/reference/feedback): Provide feedback to the gcloud CLI team.
  * [`gcloud topic`](https://docs.cloud.google.com/sdk/gcloud/reference/topic): Supplementary help material for non-command topics like accessibility, filtering, and formatting.



### Personalization

Make the gcloud CLI your own; personalize your configuration with properties.

  * [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set): Define a property (like compute/zone) for the current configuration.
  * [`gcloud config get`](https://docs.cloud.google.com/sdk/gcloud/reference/config/get): Fetch the value of a gcloud CLI property.
  * [`gcloud config list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/list): Display all the properties for the current configuration.
  * [`gcloud config configurations create`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/create): Create a new named configuration.
  * [`gcloud config configurations list`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/list): Display a list of all available configurations.
  * [`gcloud config configurations activate`](https://docs.cloud.google.com/sdk/gcloud/reference/config/configurations/activate): Switch to an existing named configuration.



### Authorization and Credentials

Grant and revoke authorization to the gcloud CLI and manage credentials.

  * [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login): Authorize Google Cloud access for the gcloud CLI with Google Cloud user credentials and set the current account as active.
  * [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account): Authorize Google Cloud access similar to `gcloud auth login` but with service account credentials.
  * [`gcloud auth application-default`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default): Manage your Application Default Credentials (ADC) for Cloud Client Libraries.
  * [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list): List all credentialed accounts.
  * [`gcloud auth print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token): Display the current account's access token.
  * [`gcloud auth revoke`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke): Remove access credentials for an account.



### Projects

Manage project access policies.

  * [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe): Display metadata for a project (including its ID).
  * [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding): Add an IAM policy binding to a specified project.



### IAM

Configuring Identity and Access Management (IAM) preferences and service accounts.

  * [`gcloud iam list-grantable-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles): List IAM grantable roles for a resource.
  * [`gcloud iam roles create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/create): Create a custom role for a project or org.
  * [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create): Create a service account for a project.
  * [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding): Add an IAM policy binding to a service account.
  * [`gcloud iam service-accounts set-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy): Replace existing IAM policy binding.
  * [`gcloud iam service-accounts keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list): List a service account's keys.



### Docker & Google Kubernetes Engine (GKE)

Manage containerized applications on Kubernetes.

  * [`gcloud auth configure-docker`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/configure-docker): Register the gcloud CLI as a Docker credential helper.
  * [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create): Create a cluster to run GKE containers.
  * [`gcloud container clusters list`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/list): List clusters for running GKE containers.
  * [`gcloud container clusters get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials): Update `kubeconfig` to get `kubectl` to use a GKE cluster.
  * [`gcloud container images list-tags`](https://docs.cloud.google.com/sdk/gcloud/reference/container/images/list-tags): List tag and digest metadata for a container image.



### Virtual Machines & Compute Engine

Create, run, and manage VMs on Google Cloud infrastructure.

  * [`gcloud compute zones list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list): List Compute Engine zones.
  * [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create): Create a VM instance.
  * [`gcloud compute instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe): Display a VM instance's details.
  * [`gcloud compute instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list): List all VM instances in a project.
  * [`gcloud compute disks snapshot`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot): Create snapshot of persistent disks.
  * [`gcloud compute snapshots describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe): Display a snapshot's details.
  * [`gcloud compute snapshots delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete): Delete a snapshot.
  * [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh): Connect to a VM instance by using SSH.



### Serverless & App Engine

Build highly scalable applications on a fully managed serverless platform

  * [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy): Deploy your app's code and configuration to the App Engine server.
  * [`gcloud app versions list`](https://docs.cloud.google.com/sdk/gcloud/reference/app/versions/list): List all versions of all services deployed to the App Engine server.
  * [`gcloud app browse`](https://docs.cloud.google.com/sdk/gcloud/reference/app/browse): Open the current app in a web browser.
  * [`gcloud app create`](https://docs.cloud.google.com/sdk/gcloud/reference/app/create): Create an App Engine app within your current project.
  * [`gcloud app logs read`](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs/read): Display the latest App Engine app logs.



### Miscellaneous

Commands that might come in handy

  * [`gcloud kms decrypt`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/decrypt): Decrypt ciphertext (to a plaintext file) using a Cloud Key Management Service key.
  * [`gcloud logging logs list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/logs/list): List your project's logs.
  * [`gcloud sql backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe): Display info about a Cloud SQL instance backup.
  * [`gcloud sql export sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/sql): Export data from a Cloud SQL instance to a SQL file.



## Introductory primer

A quick primer for getting started with the gcloud CLI.

### Installing the Google Cloud CLI

Install the Google Cloud CLI with these [installation instructions](https://docs.cloud.google.com/sdk/docs/install).

### Flags, arguments, and other wondrous additions

Arguments can be positional arguments or flags:

  * **Positional args:** Set after command name; must respect order of positional args.
  * **Flags:** Set after positional args; order of flags doesn’t matter.

A flag can be either a:

    * _Name-value pair_ (`--foo=bar`), or
    * _Boolean_ (`--force/no-force`).

Additionally, flags can either be:

    * _Required_
    * _Optional:_ If an optional flag is not defined, the default value is used



### Global flags

Some flags are available throughout the gcloud CLI experience, like:

  * [`--help`](https://docs.cloud.google.com/sdk/gcloud/reference#--help): For when in doubt; display detailed help for a command.
  * [`--project`](https://docs.cloud.google.com/sdk/gcloud/reference#--project): If using a project other than the current one.
  * [`--quiet`](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet): Disabling interactive prompting (and applying default values for inputs).
  * [`--verbosity`](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity): Can set verbosity levels at `debug`, `info`, `warning`, `error`, `critical`, and `none`.
  * [`--version`](https://docs.cloud.google.com/sdk/gcloud/reference#--version): Display `gcloud` version information.
  * [`--format`](https://docs.cloud.google.com/sdk/gcloud/reference#--format): Set output format as `config`, `csv`, `default`, `diff`, `disable`, `flattened`, `get`, `json`, `list`, `multi`, `none`, `object`, `table`, `text`, `value`, or `yaml`.



### Cleaning up results

Get the most from your output with the [filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters), [format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats), limit, and sort-by flags.

For Compute Engine instances with prefix `us` and not machine type `f1-micro`:
    
    
    gcloud compute instances list --filter="zone ~ ^us AND -machineType:f1-micro"
    

For a list of projects created on or after 15 January 2018, sorted from oldest to newest, presented as a table with project number, project id and creation time columns with dates and times in local timezone:
    
    
    gcloud projects list --format="table(projectNumber,projectId,createTime.date(tz=LOCAL))"
    --filter="createTime>=2018-01-15T12:00:00" --sort-by=createTime
    

For a list of ten Compute Engine instances with a label `my-label` (of any value):
    
    
    gcloud compute instances list --filter="labels.my-label:*" --limit=10
    

## Understanding commands

The underlying patterns for gcloud CLI commands; to aid self-discovery of commands.

### Finding gcloud CLI commands

The gcloud CLI is a tree; non-leaf nodes are command groups and leaf nodes are commands. (Also, tab completion works for commands and resources!)

Most `gcloud` commands follow the following format:
    
    
    gcloud + release level (optional) + component + entity + operation + positional args + flags
    

For example: `gcloud + compute + instances + create + example-instance-1 + --zone=us-central1-a`

#### Release level

_Release Level_ refers to the command’s release status.

_Example:_ `alpha` for alpha commands, `beta` for beta commands, no release level needed for GA commands.

#### Component

_Component_ refers to the different Google Cloud services.

_Example:_ `compute` for Compute Engine, `app` for App Engine, etc.

#### Entity

_Entity_ refers to the plural form of an element or collection of elements under a component.

_Example:_ `disks`, `firewalls`, `images`, `instances`, `regions`, `zones` for compute

#### Operation

_Operation_ refers to the imperative verb form of the operation to be performed on the entity.

_Example:_ Common operations are `describe`, `list`, `create/update`, `delete/clear`, `import`, `export`, `copy`, `remove`, `add`, `reset`, `restart`, `restore`, `run`, and `deploy`.

#### Positional args

_Positional args_ refer to the required, order-specific arguments needed to execute the command.

_Example:_ `<INSTANCE_NAMES>` is the required positional argument for `gcloud compute instances create`.

#### Flags

_Flags_ refer to the additional arguments, `--flag-name(=value)`, passed in to the command after positional args.

_Example:_ `--machine-type=<MACHINE_TYPE>` and `--preemptible` are optional flags for `gcloud compute instances create`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
