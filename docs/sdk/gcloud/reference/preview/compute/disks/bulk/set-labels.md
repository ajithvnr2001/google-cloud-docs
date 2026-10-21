---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/bulk/set-labels/
title: gcloud preview compute disks bulk set-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:50.089740+00:00
---

# gcloud preview compute disks bulk set-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/disks/bulk/set-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute disks bulk set-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute disks bulk set-labels - add or remove labels on multiple Compute Engine disks 
SYNOPSIS
    

`gcloud preview compute disks bulk set-labels` (`--source`=`SOURCE` | `--disks`=[`DISK_NAME`,…] `--labels`=[`KEY`=`VALUE`,…]) [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute disks bulk set-labels` allows you to add or remove labels on multiple Compute Engine disks in a single zone. Labels are key-value pairs that help you organize your Google Cloud resources. 

You can specify the disks and their labels in two ways: 

1\. By providing a JSON file using the `--source` flag. Each request in the JSON list must specify the disk `name` and `labels`, and may optionally include `label_fingerprint` for optimistic concurrency control. 

2\. By providing a list of disk names using the `--disks` flag and the labels to apply using the `--labels` flag. 

EXAMPLES
     To set the labels `env=production` and `team=sre` on `disk-1` and `disk-2` in zone `us-central1-a`, run: 
    
    
    gcloud preview compute disks bulk set-labels --zone=us-central1-a --disks=disk-1,disk-2 --labels=env=production,team=sre

To clear all labels on `disk-3` and `disk-4` in zone `europe-west1-b` provide an empty value to --labels, run: 
    
    
    gcloud preview compute disks bulk set-labels --zone=europe-west1-b --disks=disk-3,disk-4 --labels=''

If a disk has multiple labels and you want to remove particular labels, specify all the labels that you want to keep and omit the labels that you want to remove. This is because the `gcloud preview compute disks bulk set-labels` command replaces the entire label map. 

For example, if `disk-5` has the labels `env=production` and `team=sre`, then to remove the `env` label, include the `team=sre` label in the `--labels` argument: 
    
    
    gcloud preview compute disks bulk set-labels --zone=us-central1-a --disks=disk-5 --labels=team=sre

To set labels based on a JSON file named `disk_labels.json`, run: 

Example `disk_labels.json` content:
    
    
    [
      {
        "name": "disk-1",
        "labels": { "env": "production", "team": "sre" },
        "label_fingerprint": "42WmSpB8rSM="
      },
      {
        "name": "disk-2",
        "labels": { "env": "production", "team": "sre" }
      }
    ]
    
    
    gcloud preview compute disks bulk set-labels --zone=us-central1-a --source=disk_labels.json

To clear all labels on `disk-3` and `disk-4` in zone `europe-west1-b` provide an empty labels value in the JSON file, run: 

Example `disk_labels.json` content:
    
    
    [
      {
        "name": "disk-3",
        "labels": {}
      },
      {
        "name": "disk-4",
        "labels": {}
      }
    ]
    
    
    gcloud preview compute disks bulk set-labels --zone=europe-west1-b --source=disk_labels.json

To remove the `env` label from `disk-5` using a JSON file, omit the `env` label and include all the labels that you want to keep. 

Example `disk_labels.json` content:
    
    
    [
      {
        "name": "disk-5",
        "labels": { "team": "sre" }
      }
    ]
    
    
    gcloud preview compute disks bulk set-labels --zone=us-central1-a --source=disk_labels.json

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--source`=`SOURCE`
     Path to a JSON file containing a list of disk label update requests. Each request object must specify "name" and "labels", and may optionally include "label_fingerprint". 
Or at least one of these can be specified: 

`--disks`=[`DISK_NAME`,…]
     Comma-separated list of disk names to update. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to set on all specified disks. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--zone`=`ZONE`
     Zone of the disk to update labels. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute disks bulk set-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/set-labels)
    
    
    [gcloud alpha compute disks bulk set-labels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/bulk/set-labels)
    
    
    [gcloud beta compute disks bulk set-labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/bulk/set-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
