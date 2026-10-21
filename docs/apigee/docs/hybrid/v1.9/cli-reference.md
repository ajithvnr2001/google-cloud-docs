---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cli-reference/
title: apigeectl \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:10:58.293188+00:00
---

# apigeectl  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cli-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  apigeectl Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cli-reference.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cli-reference.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cli-reference.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cli-reference.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cli-reference.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cli-reference.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cli-reference.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cli-reference.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cli-reference.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cli-reference.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cli-reference.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cli-reference.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cli-reference.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cli-reference.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cli-reference.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cli-reference.html)



`apigeectl` is a command‑line interface (CLI) for installing and managing Apigee hybrid in a Kubernetes cluster. For information on downloading and installing `apigeectl`, see [Download and install apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-apigeectl). 

**NOTE:** You must have [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) installed and set up on your Kubernetes administration machine to use the `apigeectl` command.

##  Scopes for applying `apigeectl`

By using `apigeectl` flags you control which scopes the command applies configuration changes to. For an overview of scopes within the Apigee hybrid runtime see the [Runtime service configuration overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/service-config). 

Scope| Components| `apigeectl` flag  
---|---|---  
**Storage** | Cassandra | `‑‑datastore`  
**In‑memory storage** | Redis | `‑‑redis`  
**Environment** | Runtime  
Synchronizer  
UDCA | `‑‑all‑envs`  
`‑‑env`  
**Organization** | Apigee Connect Agent  
MART  
Watcher | `‑‑org`  
**Reporting** | Logger  
Metrics | `‑‑telemetry`  
  
## apigeectl syntax
    
    
    apigeectl [command] [flags]

Where:

  * command: Specifies the operation you want to perform. For a complete list of commands, see apigeectl commands.

  * flags: Specifies command parameters. For a complete list of flags, see apigeectl flags.




## apigeectl commands

The following table lists the `apigeectl` commands:

Command | Description  
---|---  
`apply` | Applies configurations for Apigee hybrid [runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/service-config) components to your Kubernetes cluster. `apigeectl apply` without flags will apply changes to all components in the cluster.  **apigeectl flags:** `‑‑all‑envs`, `‑‑datastore`, `‑‑dry‑run`, `‑‑env`, `‑f`, `‑‑file‑override‑config`, `‑‑help`, `‑‑org`, `‑‑print‑yaml`, `‑‑redis`, `‑‑settings virtualhosts`, `‑‑telemetry`, `‑‑v` **NOTE:** After a fresh install or an upgrade, you must call `apigeectl init` before calling `apigeectl apply`.   
`check‑ready` | Checks the status of the hybrid component pods. When all component pods are ready, the message "All containers ready" is output. For automated scripting, note that the command exits with a status of 0 when the containers are all ready. When there is at least one pod not ready, the command exits with a status of 1.  **apigeectl flags:** `‑f`, `‑‑file‑override‑config`, `‑‑help`, `‑‑v`  
`delete` | Deletes hybrid components from the cluster. Use the `‑‑all` flag to remove ALL of the components. If you omit `‑‑all`, only the Apigee‑specific components are removed (the components installed with `apigeectl init` are not deleted). Apigee‑specific components are the components that are installed with the `apply` command. `apigeectl delete` without any optional flags applies the `delete` command to all of the components deployed in the cluster. `apigeectl diagnostic delete ‑f OVERRIDES_FILE` deletes the `apigee‑diagnostic` namespace created by `apigeectl diagnostic`. The `‑f` / `‑‑file‑override‑config` flag is required with `apigeectl diagnostic delete` **apigeectl flags:** `‑‑all`, `‑‑all‑envs`, `‑‑datastore`, `‑‑env`, `‑f`, `‑‑file‑override‑config`, `‑‑help`, `‑‑org`, `‑‑redis`, `‑‑telemetry`, `‑‑v` For more information, see [Uninstall hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall.html).   
`diagnostic` | Invokes the Diagnostic collector, which captures diagnostic data on the Kubernetes components of an Apigee hybrid instance on demand and stores them in Google Cloud storage buckets. Diagnostic collector requires a named Google Cloud storage bucket, a service account with the **Storage Admin** role, and a `diagnostic:` stanza added to your `overrides` file. See: 

  * [Using the Diagnostic collector](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/diagnostic-collector)
  * [Configuration property reference: `diagnostic`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#diagnostic)

When you invoke Diagnostic collector, it creates an "`apigee‑diagnostic`" Kubernetes namespace. You must delete this with `apigeectl diagnostic delete` before invoking Diagnostic collector again. Invoke Diagnostic collector: 
    
    
    apigeectl diagnostic ‑f OVERRIDES_FILE

Delete Diagnostic collector: 
    
    
    apigeectl diagnostic delete ‑f OVERRIDES_FILE

**apigeectl flags:** `‑‑file‑override‑config`  
`encode` | Returns a list of encoded names of all the ApigeeDeployments for the specified organization or the specified environment within the specified organization. The encoded names include the name of the component with a hashed name of the organization and if using the `‑‑env` flag, a hashed name of the environment. Apigee hybrid creates hashed names of organizations and environments to be able to avoid namespace collisions.  You must use either the `‑‑org org‑name` or both the `‑‑org org‑name` with the `‑‑env env‑name` flags with `encode`. For example:
    
    
    ./apigeectl encode ‑‑org hybrid‑example
    List of ApigeeDeployments are:
      apigee‑connect‑agent‑hybrid‑example‑6a82f8a
      apigee‑mart‑hybrid‑example‑6a82f8a
      apigee‑watcher‑hybrid‑example‑6a82f8a
    
    
    ./apigeectl encode ‑‑org hybrid‑example ‑‑env example‑env
    List of ApigeeDeployments are:
      apigee‑runtime‑hybrid‑example‑example‑env‑9e87e2d
      apigee‑synchronizer‑hybrid‑example‑example‑env‑9e87e2d
      apigee‑udca‑hybrid‑example‑example‑env‑9e87e2d
    

**apigeectl flags:** `‑‑env`, `‑‑org`  
`help` | Prints online help.   
`init` | Installs Apigee Operators and CRDs in the apigee‑system namespace. Run `apigeectl init` after a fresh install or upgrade before running `apigeectl apply`.  **apigeectl flags:** `‑f`, `‑‑file‑override‑config`, `‑‑help`, `‑‑v`  
`version` | Prints the CLI version information.  **apigeectl flag:** `‑‑help`  
  
## apigeectl flags

The following table lists the `apigeectl` flags:

Flag | Description  
---|---  
`‑‑all` | `delete` only: Deletes the entire Apigee hybrid installation except ASM (Istio) and cert‑manager from your cluster.   
`‑‑all‑envs` | Applies the `apigeectl` command to all environments under the organization specified in your overrides config file.  
`‑‑datastore` | Applies the configuration to the datastore scope (Cassandra).  
`‑‑dry‑run` | Executes the specified command without changing the cluster. Use with `‑‑print‑yaml` to output the rendered object spec to a file.  `‑‑dry‑run` must be used with one of the two following values, depending on the version of kubectl you are running. Use `gcloud version` to check your kubectl version: 

  * kubectl version 1.17.x or older: `‑‑dry‑run=**true**`
  * kubectl version 1.18.x or newer: `‑‑dry‑run=**client**`

  
`‑‑env env‑name` | Applies the configuration to the specified environment. This flag will apply configuration to environment scope components apigee‑runtime, apigee‑synchronizer and apigee‑udca. `‑‑env` must be used with the `‑‑org` flag. For example: 
    
    
    apigeectl apply ‑‑org hybrid‑example ‑‑env example‑env \
          ‑f overrides/overrides.yaml  
  
`‑f  
‑‑file‑override‑config` | Specifies a YAML file containing custom configuration properties for the hybrid deployment. The default value is `./overrides.yaml`. An overrides file is required for the `apply`, `check‑ready`, `delete`, and `init` commands.  You must specify the full path with this flag. For more information, see [Managing runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/customize-services).  
`‑h  
‑‑help` | Displays help for the command.  
`‑‑org` | Applies the configuration to the specified organization. This flag will apply configuration to the org scope components apigee‑connect‑agent, apigee‑mart and apigee‑watcher. **Note:** When using `‑‑org` with `encode` you must include the organization ID. For example: 
    
    
    apigeectl encode ‑‑org example‑org  
  
`‑‑print‑yaml` | Prints the configuration template output to stdout. For an example that uses this flag, see Print the configuration to a file.  
`‑‑redis` | Applies the configuration to the in‑memory data storage scope (Redis).  
`‑‑restore` | Restores Cassandra to a previously saved snapshot specified by the `snapshotTimestamp` property in `restore` configuration of the `overrides.yaml` file. The backup is restored either from the Cloud Storage bucket or a remote server based on the `backup` configuration in the `overrides.yaml` file. For more information, see [Restoring a region from a backup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-single-region#restore-gcs).  
`‑s  
‑‑settings  _virtualhosts_` | Specifies a configuration to which the command applies. Currently, this flag is only supported for the `virtualhosts` configuration, which is part of the `runtime` component. Use this flag if you make changes to the `virtualhosts` property, and nothing else.  For example, if you make a change to the `virtualhosts` configuration in your overrides file, apply it to the cluster with this command:
    
    
    apigeectl apply ‑f my‑overrides.yaml ‑‑settings virtualhosts \
        ‑‑org example‑org ‑‑env example‑env  
  
`‑‑telemetry` | Applies the configuration for telemetry components like apigee‑logger and apigee‑metrics.  
`‑‑v int` | Prints verbose logs to std err. `_int_` is an integer that sets the level of verbosity. `_int_` is required with `‑‑v`. This option behaves identically to the `kubectl` `‑‑v` option. **Note:** This option replaces the deprecated `‑‑verbose` option.  
  
The `apigeectl` command uses `kubectl` behind the scenes to do its work. The `apigeectl` command options (`apply` and `delete`, and the use of YAML configuration files, are similar to their kubectl counterparts. To learn more about how objects are managed in a Kubernetes cluster, see the following topics:

  * [ Imperative Management of Kubernetes Objects Using Configuration Files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/)
  * [Overview of kubectl](https://kubernetes.io/docs/reference/kubectl/overview/)



##  Examples 

###  Initialize the cluster configuration 

Apply prerequisite component configurations to your cluster with `init`. You must run the `init` command before `apply`. 
    
    
    apigeectl init ‑f my_overrides.yaml

### Apply the cluster configuration

To apply hybrid configurations to your Kubernetes cluster, use the `apply` command. The first time you run `apply` all of the hybrid runtime components are created in your cluster. If you make configuration changes, rerun `apply` to apply only the changes or use flags to apply changes to a specific scope only.

The following example applies the configuration for hybrid runtime plane components to your cluster:
    
    
    apigeectl apply ‑f my_overrides.yaml

###  Apply the configuration for a single component 

To restrict the `apply` command to a particular component, use the flags described in apigeectl flags.

The following example only applies the configuration for the Cassandra component:
    
    
    apigeectl apply ‑‑datastore ‑f my_overrides.yaml

### Print the configuration to a file

If you're debugging an installation problem, it's useful to print out the entire cluster configuration to a file so that you can inspect the configuration settings. The `‑‑print‑yaml` flag prints the hybrid configuration to stdout, and the `‑‑dry‑run` flag allows the command to run without making any changes to the cluster.
    
    
    apigeectl apply ‑f my_overrides.yaml ‑‑dry‑run=client ‑‑print‑yaml > apigee‑hybrid.yaml

**NOTE:** It is a good practice to save a copy of the YAML output in source control for future reference. But be aware that the output file contains passwords and secrets that you may not want to store.

### Check pod status

The following example checks the status of pods deployed to your cluster:
    
    
    apigeectl check‑ready ‑f overrides/overrides.yaml
    All containers ready in namespace 'my-namespace'

### Delete hybrid from the cluster

For details, see [Uninstall hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/uninstall.html). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
