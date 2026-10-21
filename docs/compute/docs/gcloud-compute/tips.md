---
url: https://docs.cloud.google.com/compute/docs/gcloud-compute/tips/
title: gcloud compute usage tips \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:04.337569+00:00
---

# gcloud compute usage tips  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gcloud-compute/tips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  gcloud compute usage tips Stay organized with collections  Save and categorize content based on your preferences. 

This page contains tips that might be useful when you use the `gcloud` command-line tool to manage your Compute Engine resources. For a complete list of all available `gcloud compute` flags and commands, you can use the built-in command help (`--help`) or the published [reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute), or the [gcloud core documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Fetching information about resources

You can fetch information about Compute Engine resources in two ways: using the `list` command to return a list of resources and using the `describe` command to return details about one specific resource.

### Fetching resources with `list` commands

The `list` commands are designed to return a human-readable table of the most relevant data for the requested resources. You can optionally [filter](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) your results to return a shorter list with more relevant results.

Regular expression filtering for names
    You can use [RE2 syntax](https://github.com/google/re2/wiki/Syntax) to match resource names (for example, instance or disk names). Refer to the [`gcloud compute instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) command.
Command Flags
    `--limit`
    

The maximum number of results to return. This flag is particularly useful when used with the `--sort-by` flag as described in the Fetching resources with describe commands section.

    

`--sort-by SORT_BY`

    

A field to sort by, if applicable. To perform a descending-order sort, prefix the value with a tilde ("~"). This flag interacts with other flags that are applied in this order: `--flatten`,`--sort-by`, `--filter`, `--limit`.

### Fetching resources with `describe` commands

The `describe` commands are designed for displaying data about one resource. You must provide the name of the resource in the `describe` command. If you can't remember the resource name, you can run a `list` command to get a list of resources. For example, the following two commands illustrate a scenario when you can list images to get an image name and its associated project so that you can provide these as inputs to a `describe` command:
    
    
    gcloud compute images list
    
    
    
    NAME                                PROJECT        FAMILY     DEPRECATED STATUS
    ...
    centos-7-v20170620                  centos-cloud   centos-7              READY
    ...
    debian-9-stretch-v20170619          debian-cloud   debian-9              READY
    ...
    
    
    
    gcloud compute images describe debian-9-stretch-v20170619 --project debian-cloud
    

The default output from `describe` commands is YAML format, but you can use the `--format` flag to choose between JSON, YAML, and text output formats. JSON formatted output can be useful if you are parsing the output, while text formatted output puts each property on a separate line.
    
    
    gcloud compute regions describe us-central1 --format json
    
    
    
    {
      "creationTimestamp": "2013-09-06T10:36:54.847-07:00",
      "description": "us-central1",
      "id": "6837843067389011605",
      "kind": "compute#region",
      "name": "us-central1",
      ...
      "status": "UP",
      "zones": [
        "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a",
        "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-b",
        "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f"
      ]
    }

### Examples

#### Examples of `list` commands

When you list resources, you get an easy-to-read table of summary data. For example, to return summary data about instances in your project, use the [`instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) command:
    
    
    gcloud compute instances list
    
    
    
    NAME               ZONE          MACHINE_TYPE  INTERNAL_IP    EXTERNAL_IP     STATUS
    example-instance   asia-east1-b  e2-standard-2 10.240.95.199  107.167.182.44  RUNNING
    example-instance2  us-central1-a e2-standard-2 10.240.173.254 23.251.148.121  RUNNING
    test-instance      us-central1-a e2-standard-2 10.240.118.207 23.251.153.172  RUNNING

You can filter results from `list` commands with regular expressions by including the [`--filter`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) flag with a `key ~ value` operator. For example, filter the list of instances to include only the instances with "test" in the instance name:
    
    
    gcloud compute instances list --filter="name ~ .*test.*"
    
    
    
    NAME           ZONE          MACHINE_TYPE  INTERNAL_IP    EXTERNAL_IP     STATUS
    test-instance  us-central1-a e2-standard-2 10.240.118.207 23.251.153.172  RUNNING

To return a list of zone operations that have a `status` of `DONE` and don't have an `httpStatus` of `200`, apply a `zone` filter on an [`operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) command, then `grep` the results:
    
    
    gcloud compute operations list --filter="zone:(us-central1-a)" | grep DONE | grep -v 200
    
    
    
    NAME                                                    HTTP_STATUS TYPE   TARGET                               STATUS
    operation-1397752585735-4f73fa25b4b58-f0920fd5-254d709f 400         delete us-central1-a/disks/example-instance DONE
    operation-1398357613036-4f7cc80cb41e0-765bcba6-34bbd040 409         insert us-central1-a/instances/i-1          DONE
    operation-1398615481237-4f8088aefbe08-cc300dfa-2ce113cf 409         insert us-central1-a/instances/i-2          DONE

To get a list of list of disks in `us-central1-a`, sorted in descending order by name (`--sort-by ~NAME`), use a [`disks list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list) command:
    
    
    gcloud compute disks list --sort-by ~NAME --filter="zone:(us-central1-a)"
    

In some scenarios, you may want to have the full URI link to the resource, such as requests where you are passing the output from a `list` command to another command or application that takes a list of resource links. To show full URI resource links, use the `--uri` flag with a `list` command.
    
    
    gcloud compute instances list --uri --filter="name~'^example-.*'"
    
    
    
    https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-instance1
    https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-instance2

To use the previous `list` command output within a command that deletes instances, use:
    
    
    gcloud compute instances delete $(gcloud compute instances list --uri --filter="name~'^example-.*'")
    

#### Examples of `describe` commands

To get details about just one instance, specify the instance, including zone. For example, to return information about the instance named "example-instance" in the "asia-east1-b" zone, you can use [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) command:
    
    
    gcloud compute instances describe example-instance --zone asia-east1-b
    

By default, this returns YAML output. To change the output to JSON or text (one property per line) use the `--format` flag. For example, to return text output for the same instance, use:
    
    
    gcloud compute instances describe example-instance --zone asia-east1-b --format text
    
    
    
    ---
    canIpForward:                                False
    creationTimestamp:                           2014-04-19T06:43:04.087-07:00
    disks[0].autoDelete:                         False
    disks[0].boot:                               True
    disks[0].deviceName:                         example-instance
    ...

To get details about a specific operation, use the [`operations list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list) command to find the fully qualified URI of the operation:
    
    
    gcloud compute operations list --filter="zone:(us-central1-a)"
    
    
    
    NAME                                                    TYPE   TARGET                                      HTTP_STATUS STATUS
    operation-1406155165815-4fee4032850d9-7b78077c-a170c5c0 delete us-central1-a/instances/example-instance    200         DONE
    operation-1406155180632-4fee4040a67c1-bf581ed8-ab5af2b8 delete us-central1-a/instances/example-instance-2  200         DONE
    ...

Then use the URI in an [`operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/describe) command:
    
    
    gcloud compute operations describe \
    operation-1406155165815-4fee4032850d9-7b78077c-a170c5c0 --zone us-central1-a
    
    
    
    endTime: '2014-07-23T15:40:02.463-07:00'
    id: '31755455923038965'
    insertTime: '2014-07-23T15:39:25.910-07:00'
    kind: compute#operation
    name: operation-1406155165815-4fee4032850d9-7b78077c-a170c5c0
    operationType: delete
    progress: 100
    ...

The following command gets instance settings in JSON format (`--format json`).
    
    
    gcloud compute instances describe example-instance \
        --zone us-central1-a
        --format json
    
    
    
    {
       ...
       "name": "example-instance",
       "networkInterfaces": [
        {
          "accessConfigs": [
            {
              "kind": "compute#accessConfig",
              "name": "external-nat",
              "natIP": "107.167.187.66",
              "type": "ONE_TO_ONE_NAT"
            }
          ],
          "name": "nic0",
          "network": "https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default",
          "networkIP": "10.240.111.51"
        }
       ],
       ...
       "status": "RUNNING"
       ...
    }

## Checking which user you are authorized as

Use the following command to find out which account you are authorizes as, use:
    
    
    gcloud auth list
    

## Revoking a refresh token

To revoke the credentials for an account on the machine where you are using the Google Cloud CLI, use:
    
    
    gcloud auth revoke
    

This will force you to use re-authenticate using `gcloud init`.

You can also revoke permission for the gcloud CLI to access your resources. You might do this, if your refresh tokens are compromised, for example. To revoke permission for the gcloud CLI:

  1. Log into your [Google Account](https://myaccount.google.com/) page.
  2. Click **Security** and then click **View all** in the **Account permissions** section.
  3. Select **Google Cloud SDK** and click **Revoke Access**.



## Rebooting an instance

To reset an instance named "example-instance" in the "us-central1-a" zone, use the [`instances reset`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/reset) command:
    
    
    gcloud compute instances reset example-instance --zone us-central1-a
    

For information about the implications of a reset, read the [Reset an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
