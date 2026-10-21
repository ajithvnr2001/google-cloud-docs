---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/ssh/
title: gcloud alpha compute instance-groups ssh \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:36:58.066337+00:00
---

# gcloud alpha compute instance-groups ssh  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups ssh Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups ssh - SSH into instances of a Compute Engine instance group 
SYNOPSIS
    

`gcloud alpha compute instance-groups ssh` `NAME` `--command`=`COMMAND` [`--batch-size`=`BATCH_SIZE`; default="all"] [`--container`=`CONTAINER`] [`--dry-run`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--force-key-file-overwrite`] [`--output-directory`=`OUTPUT_DIRECTORY`] [`--plain`] [`--ssh-flag`=`SSH_FLAG`] [`--ssh-key-file`=`SSH_KEY_FILE`] [`--strict-host-key-checking`=`STRICT_HOST_KEY_CHECKING`] [`--user`=`USER`] [`--internal-ip` | `--tunnel-through-iap`] [`--region`=`REGION` | `--zone`=`ZONE`] [`--ssh-key-expiration`=`SSH_KEY_EXPIRATION` | `--ssh-key-expire-after`=`SSH_KEY_EXPIRE_AFTER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instance-groups ssh` runs an SSH command concurrently on all running Compute Engine VM instances in a specified Instance Group (managed or unmanaged; unless `--batch-size` is specified). 

Within a batch, all instances are executed concurrently even if the command fails on some instances. When executing across multiple batches (via `--batch-size`), if the command fails on any instance in a batch, subsequent batches are not executed. After execution completes, a summary of succeeded, failed (with their exit codes), and skipped instances (formatted by batch when multiple batches are used) is printed to standard error. If the command succeeds on all target instances, `gcloud alpha compute instance-groups ssh` exits with status `0`. If the command fails on one or more instances, `gcloud alpha compute instance-groups ssh` exits with the first non-zero exit status encountered (`255` for SSH connection or client errors, or the remote command's non-zero exit code). 

EXAMPLES
     To run an SSH command concurrently on all instances in Instance Group `my-group` in zone `us-central1-a`, run: 
    
    
    gcloud alpha compute instance-groups ssh my-group --zone=us-central1-a --command="hostname"

To run an SSH command with a custom batch size on a regional Managed Instance Group `my-regional-mig` in region `us-central1`, run: 
    
    
    gcloud alpha compute instance-groups ssh my-regional-mig --region=us-central1 --command="uptime" --batch-size=4

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the instance group to operate on. 
REQUIRED FLAGS
    

`--command`=`COMMAND`
     Command to run concurrently on all instances in the specified Instance Group (unless `--batch-size` is specified). Runs the command on each target instance and then exits. 
OPTIONAL FLAGS
    

`--batch-size`=`BATCH_SIZE`; default="all"
     Batch size for simultaneous command execution on the client's side. This flag takes a value greater than 0 to specify the batch size to control concurrent connections, or the special keyword ``all`` to allow concurrent command execution on all instances in the Instance Group. If the command fails on any instance in a batch, subsequent batches are not executed. 
`--container`=`CONTAINER`
     The name or ID of a container inside of the virtual machine instance to connect to. This only applies to virtual machines that are using a Google Container-Optimized virtual machine image. For more information, see <https://cloud.google.com/compute/docs/containers>. 
`--dry-run`
     Print the equivalent scp/ssh command that would be run to stdout, instead of executing it. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--force-key-file-overwrite`
     If enabled, the gcloud command-line tool will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environments. 

If disabled, the files associated with a broken SSH key will not be regenerated and will fail in both interactive and non-interactive environments. 

`--output-directory`=`OUTPUT_DIRECTORY`
     Path to the directory to output the logs of the commands. 

The path can be relative or absolute. The directory must already exist. 

If not specified, standard output will be used. 

The logs will be written in files named {INSTANCE_NAME}.log. 

`--plain`
     Suppress the automatic addition of `ssh(1)`/`scp(1)` flags. This flag is useful if you want to take care of authentication yourself or use specific ssh/scp features. 
`--ssh-flag`=`SSH_FLAG`
     Additional flags to be passed to `ssh(1)`. It is recommended that flags be passed using an assignment operator and quotes. 

This flag will replace occurrences of ``%USER%``, ``%INSTANCE%``, ``%INTERNAL%``, ``%NAME%``, ``%ZONE%``, and ``%PROJECT%`` with their dereferenced values for each target instance. ``%NAME%``, ``%ZONE%``, and ``%PROJECT%`` are replaced with the instance name, zone, and project ID respectively. If connecting to the instance's external IP, then ``%INSTANCE%`` is replaced with that, otherwise it is replaced with the internal IP. ``%INTERNAL%`` is always replaced with the internal IP of the instance. 

`--ssh-key-file`=`SSH_KEY_FILE`
     The path to the SSH key file. By default, this is ``~/.ssh/google_compute_engine``. 
`--strict-host-key-checking`=`STRICT_HOST_KEY_CHECKING`
     Override the default behavior of StrictHostKeyChecking for the connection. By default, StrictHostKeyChecking is set to 'no' the first time you connect to an instance, and will be set to 'yes' for all subsequent connections. `STRICT_HOST_KEY_CHECKING` must be one of: `yes`, `no`, `ask`. 
`--user`=`USER`
     Username with which to SSH into the instances. If omitted, the default login user is used. 
At most one of these can be specified: 

`--internal-ip`
     Connect to instances using their internal IP addresses rather than their external IP addresses. Use this to connect from one instance to another on the same VPC network, over a VPN connection, or between two peered VPC networks. 

For this connection to work, you must configure your networks and firewall to allow SSH connections to the internal IP address of the instance to which you want to connect. 

To learn how to use this flag, see <https://cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances>. 

`--tunnel-through-iap`
     Tunnel the ssh connection through Cloud Identity-Aware Proxy for TCP forwarding. 

To learn more, see the [IAP for TCP forwarding documentation](https://cloud.google.com/iap/docs/tcp-forwarding-overview). 

At most one of these can be specified: 

`--region`=`REGION`
     Region of the instance group to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the instance group to operate on. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

At most one of these can be specified: 

`--ssh-key-expiration`=`SSH_KEY_EXPIRATION`
     The time when the ssh key will be valid until, such as "2017-08-29T18:52:51.142Z." This is only valid if the instance is not using OS Login. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--ssh-key-expire-after`=`SSH_KEY_EXPIRE_AFTER`
     The maximum length of time an SSH key is valid for once created and installed, e.g. 2m for 2 minutes. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
