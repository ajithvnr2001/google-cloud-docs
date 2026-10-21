---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/
title: gcloud compute instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:42:59.703732+00:00
---

# gcloud compute instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances - read and manipulate Compute Engine virtual machine instances 
SYNOPSIS
    

`gcloud compute instances` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Read and manipulate Compute Engine virtual machine instances. 

For more information about virtual machine instances, see the [virtual machine instances documentation](https://cloud.google.com/compute/docs/instances/). 

See also: [Instances API](https://cloud.google.com/compute/docs/reference/rest/v1/instances). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[bulk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk)`
     Manipulate multiple Compute Engine virtual machines with single command executions. 
`[network-interfaces](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces)`
     Read and manipulate Compute Engine instance network interfaces. 
`[ops-agents](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents)`
     Manage Google Cloud Observability agents for Compute Engine VM instances. 
`[os-inventory](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory)`
     Read Compute Engine OS Inventory Data and Related Resources. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[add-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-access-config)`
     Create a Compute Engine virtual machine access configuration. 
`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-iam-policy-binding)`
     Add IAM policy binding to a Compute Engine instance. 
`[add-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels)`
     Add labels to Google Compute Engine virtual machine instances. 
`[add-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata)`
     Add or update instance metadata. 
`[add-resource-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-resource-policies)`
     Add resource policies to Compute Engine VM instances. 
`[add-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags)`
     Add tags to Compute Engine virtual machine instances. 
`[attach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk)`
     Attach a disk to an instance. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create)`
     Create Compute Engine virtual machine instances. 
`[create-with-container](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container)`
     `(DEPRECATED)` Creates Compute Engine virtual machine instances running container images. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete)`
     Delete Compute Engine virtual machine instances. 
`[delete-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete-access-config)`
     Delete an access configuration from a virtual machine network interface. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe)`
     Describe a virtual machine instance. 
`[detach-disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk)`
     Detach disks from Compute Engine virtual machine instances. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export)`
     Export a Compute Engine virtual machine instance's configuration to a file. 
`[get-guest-attributes](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-guest-attributes)`
     Get the Guest Attributes for a compute instance. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-iam-policy)`
     Get the IAM policy for a Compute Engine instance. 
`[get-screenshot](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-screenshot)`
     Capture a screenshot (JPEG image) of the virtual machine instance's display. 
`[get-serial-port-output](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output)`
     Read output from a virtual machine instance's serial port. 
`[get-shielded-identity](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-shielded-identity)`
     Get the Shielded identity for a Compute Engine instance. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import)`
     Create Compute Engine virtual machine instances from virtual appliance in OVA/OVF format. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list)`
     List Compute Engine instances. 
`[list-referrers](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list-referrers)`
     List referrers to a Compute Engine virtual machine instance. 
`[perform-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/perform-maintenance)`
     Perform maintenance of Google Compute Engine instance. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-iam-policy-binding)`
     Remove IAM policy binding from a Compute Engine instance. 
`[remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-labels)`
     Remove labels from Google Compute Engine virtual machine instances. 
`[remove-metadata](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-metadata)`
     Remove instance metadata. 
`[remove-resource-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies)`
     Remove resource policies from Compute Engine VM instances. 
`[remove-tags](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-tags)`
     Remove tags from Compute Engine virtual machine instances. 
`[report-host-as-faulty](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/report-host-as-faulty)`
     Report a host as faulty to start the repair process. 
`[reset](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/reset)`
     Reset a virtual machine instance. 
`[resume](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/resume)`
     Resume a virtual machine instance. 
`[send-diagnostic-interrupt](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/send-diagnostic-interrupt)`
     Send a diagnostic interrupt to a virtual machine instance. 
`[set-disk-auto-delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-disk-auto-delete)`
     Set auto-delete behavior for disks. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-iam-policy)`
     Set IAM policy for a Compute Engine instance. 
`[set-machine-resources](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-resources)`
     Set machine resources for a Compute Engine virtual machine instance. 
`[set-machine-type](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type)`
     Set machine type for Compute Engine virtual machines. 
`[set-name](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-name)`
     Set the name of a Compute Engine virtual machine. 
`[set-scheduling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling)`
     Set scheduling options for Compute Engine virtual machines. 
`[set-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account)`
     Set a service account and access scopes for a Compute Engine VM instance. 
`[simulate-maintenance-event](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event)`
     Simulate host maintenance of VM instances. 
`[start](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start)`
     Start a stopped virtual machine instance. 
`[stop](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop)`
     Stop a virtual machine instance. 
`[suspend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/suspend)`
     Suspend a virtual machine instance. 
`[tail-serial-port-output](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/tail-serial-port-output)`
     Periodically fetch new output from a virtual machine instance's serial port and display it as it becomes available. 
`[test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/test-iam-permissions)`
     Test IAM permissions for a Compute Engine instance. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update)`
     Update a Compute Engine virtual machine. 
`[update-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-access-config)`
     Update a Compute Engine virtual machine access configuration. 
`[update-container](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-container)`
     `(DEPRECATED)` Updates Compute Engine virtual machine instances running container images. 
`[update-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file)`
     Update a Compute Engine virtual machine instance using a configuration file. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances)
    
    
    [gcloud beta compute instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances)
    
    
    [gcloud preview compute instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
