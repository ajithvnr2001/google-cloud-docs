---
url: https://docs.cloud.google.com/tpu/docs/ctpu-reference/
title: CTPU Reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:27.021294+00:00
---

# CTPU Reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ctpu-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Reference ](https://docs.cloud.google.com/tpu/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CTPU Reference

## Overview

**Important:** The `ctpu` tool has been deprecated and the tool functionality has been replaced by corresponding [`gcloud compute tpus` commands](https://cloud.google.com/sdk/gcloud/reference/compute).

The open source `ctpu` tool is used to create a _flock_ of compute resources, which consist of a Compute Engine VM and one or more Cloud TPU devices. The tool is pre-installed in your Cloud shell.

You can find [documentation and code for `ctpu`](https://github.com/tensorflow/tpu/tree/master/tools/ctpu) on GitHub.

The `ctpu` tool uses the following syntax:
    
    
    ctpu <subcommand> <flags> <subcommand> <subcommand args> 

Following are the subcommands for `ctpu`:

## auth

Description
    Set or display authorization(s) for Cloud TPUs.
Usage
    
    
    
    ctpu auth <flags> <subcommand> <subcommand args>

Example
    
    
    
    ctpu auth list --project="my-project" --zone=us-central1-a
    ctpu auth list --project my-project --zone us-central1-a

Subcommands
    

The `ctpu auth` command supports the following subcommands:

  * add-bigtable - ensure Cloud TPU is authorized for Cloud Bigtable
  * add-gcs - ensure Cloud TPU is authorized for Cloud Storage
  * list - display Cloud TPU service account authorizations
  * commands - list all command names
  * flags - describe all known top-level flags
  * help - describe subcommands and their syntax


Optional Flags
    

The following are optional commands for `ctpu auth`. `name | project | zone`

## delete (rm)

Description
    Delete your Compute Engine VM and Cloud TPU.
Usage
    
    
    
    ctpu rm <flags>

Example
    
    
    
    ctpu rm --zone=us-central1-b

## help

Description
    List all `ctpu` subcommands and top level flags.
Usage
    
    
    
    ctpu help
    ctpu help <subcommand>

Example
    
    
    
    ctpu help   // list all ctpu subcommands and top level flags
    
    ctpu help auth   // list all flags that can be used with `ctpu auth`
    ctpu help up   // list all flags that can be used with `ctpu up`

## list (ls)

Description
    List all Compute Engine VMs and Cloud TPU in the specified zone.
Usage
    
    
    
    ctpu ls <flags>

Example
    
    
    
    ctpu ls --zone=us-central1-b

## pause (zz)

Description
    

Stop the Compute Engine VM, and delete your Cloud TPU. Stop charging for Cloud TPU usage until you run `ctpu up`.

    

To ensure that the Cloud TPU is stopped, you must specify the Cloud TPU name and the zone on the command line.

    **Important:** You will still be charged for the disk space consumed by your VM while it is paused.
Usage
    
    
    
    ctpu pause <name, zone>

Example
    
    
    
    ctpu pause --name=my-tpu --zone=us-central1-a  // pause the named TPU
    in the specified zone

## print-config (cfg)

Description
    Print onscreen the current configuration of the Cloud TPU name, project name, and zone.
Example
    
    
    
    ctpu print-config

## quota

Description
    Display a URL where you can see quotas.
Usage
    
    
    
    ctpu quota

Example
    
    
    
    ctpu quota
    Output: Quotas cannot currently be displayed within ctpu.
    To view your quota, open <url>
    Request additional quota from <url>

## restart

Description
    

Restarts a Cloud TPU that is still in the RUNNING state (shown in `ctpu status`), but has stopped running because of a hardware problem. Use `gcloud compute tpu start` or the START button on the **Compute Engine > TPUs** page in the Cloud console if the TPU is in the STOPPED state.

    

`restart` does not restart a preempted Cloud TPU. You need to run `ctpu delete` and `ctpu up` if your Cloud TPU has been preempted.

Usage
    
    
    
    ctpu restart <flags>

Example
    
    
    
    ctpu restart --zone=us-central1-a

## status (st)

Description
    

Query the GCP APIs (default zone only) to determine the current status of your Cloud TPU and Compute Engine VM.

    **Important:** If your resources are running in a non-default region or zone, you _must_ specify the `--zone` flag.
Usage
    

ctpu st

Example
    
    
    
    ctpu st --zone=us-central1-a
    Status message:
      Your cluster is running!
        Compute Engine VM:  RUNNING
        Cloud TPU:     RUNNING 

## tpu-locations

Description
    List all [zones](https://docs.cloud.google.com/tpu/docs/types-zones#types) where TPU types are available.
Usage
    ctpu tpu-locations
Output
    
    
    
    Cloud TPU Locations:
        asia-east1-c
        europe-west4-a
        us-central1-a
        us-central1-b
        us-central1-c

## tpu-sizes

Description
    List all available TPU sizes in specified zone. Some sizes are available only in [certain zones](https://docs.cloud.google.com/tpu/docs/types-zones#types). (default = default zone)
Usage
    
    
    
    tpu-sizes <zone>

Example
    
    
    
    ctpu tpu-sizes --zone=us-central1-a

## up

Description
    

Bring up a `ctpu` resource set. The first time you run `ctpu up` on a project, it takes longer than it will in future runs because it is performing tasks such as SSH key propagation and API turn-up.

  * Enables the Compute Engine and Cloud TPU services.
  * Creates a Compute Engine VM with the latest stable TensorFlow version pre-installed.
  * Assigns a default zone, such as `us-central1-b` based on your location.
  * Passes the name of the Cloud TPU to the Compute Engine VM as an environment variable (`TPU_NAME`).
  * Ensures your Cloud TPU has access to resources it needs from your Google Cloud project, by granting specific IAM roles to your Cloud TPU service account.
  * Performs a number of other checks.
  * Logs you into your new Compute Engine VM. Your shell prompt changes from `username@project` to `username@tpuname`.


    

You can run `ctpu up` as often as you like. For example, if you lose the SSH connection to the Compute Engine VM, run `ctpu up` to restore the connection. You _must_ specify a zone if your Compute Engine is not in the default zone. For example:

    
    
    
    $ ctpu up --zone=us-central1-a

Usage
    
    
    
    ctpu up <flags>

Example
    
    
    
    ctpu up --tpu-size=v2-8 --disk-size-gb=320 --preemptible

Flags
    

`--disk-size-gb`  
Configure the root volume size of your Compute Engine VM. Value must be an integer. (default = 250)

    

`--dry-run`  
Do not make changes; print only what would have happened.

    

`--forward-agent`  
Enable ssh agent forwarding when sshing into the Compute Engine VM. SSH Agent Forwarding enables access to shared repositories (such as GitHub) without having to place private keys on the Compute Engine VM. (default = true)

    

`--forward-ports`  
Automatically forward useful ports from the Compute Engine VM to your local machine. Ports forwarded are: 6006 (tensorboard), 8888 (jupyter notebooks), 8470 (TPU port), 8466 (TPU profiler port). (default = true)

    

`--gce-image`  
Override the automatically chosen Compute Engine Image. Use this flag when you are using your own custom images instead of the ones provided with the installed TensorFlow.

    

`--gcp-network`  
Specify the network in which the Cloud TPU and associated VM should be created. Refer to [Virtual Private Cloud (VPC) Network Overview](https://cloud.google.com/vpc/docs/vpc) for information on networks. (default = default network)

    

`--log-http`  
Print the full content of http request-response pairs. To enable the printout, set this flag to _true_. Use this flag when you need log output to file a bug report against `ctpu`. Refer to [`ctpu` README](https://github.com/tensorflow/tpu/tree/master/tools/ctpu) for details.

    

`--machine-type`  
Configure the size of your Compute Engine VM. A full list of machine types is available on the Cloud [Machine Types](https://cloud.google.com/compute/docs/machine-types) page. (default = n1-standard-2)

    

`--name`  
Override the name to use for VMs and Cloud TPU. (default = your username)

    

`--noconf`  
Skip confirmation.

    

[`--preemptible`](https://docs.cloud.google.com/tpu/docs/preemptible)  
Create a preemptible Cloud TPU node. A preemptible Cloud TPU costs less per hour than a non-preemptible one. Cloud TPU service can exit a preemptible device at any time. (default = non-preemptible)

    

`--preemptible-vm`  
Create a preemptible Compute Engine VM. A preemptible VM costs less per hour than a non-preemptible VM. The Compute Engine service can exit the VM instance at any time. (default = non-preemptible)

    

`--print-welcome`  
Always print the welcome message.

    

`--project`  
Override the GCP project name to use when allocating VMs and TPUs. Specify a value from cloud config or Compute Engine metadata, usually your project name. If a good value cannot be found, you must to provide a value on the command line.

    

`--tf-version`  
Set the version of TensorFlow to use when creating the Compute Engine VM and the Cloud TPU. (default = latest stable release)

    

`--tpu-only`  
Allocate a Cloud TPU only; use this only if you already have a VM available.

    

`--tpu-size`  
Configure the size and hardware version of a Cloud TPU.

    

`--use-dl-images`  
Use Deep Learning VM Images (refer docs: https://cloud.google.com/deep-learning-vm/) instead of TPU machine images. (default = TPU machine images)

    

`--vm-only`  
Allocate a VM only; use this when you are not ready to set up and pay for a TPU.

    

`--zone`  
Override the Compute Engine zone to use when allocating VMs and Cloud TPU. On the command line, run `ctpu help up` to view the list.

## version

Description
    Prints out the version of `ctpu` installed.
Usage
    
    
    
    ctpu version

Output
    
    
    
    ctpu version
    Output: ctpu version: 1.9

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
