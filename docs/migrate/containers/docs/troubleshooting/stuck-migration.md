---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/stuck-migration/
title: Migration process stuck during a Compute Engine migration \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:03:52.188022+00:00
---

# Migration process stuck during a Compute Engine migration  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/stuck-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migration process stuck during a Compute Engine migration

During Compute Engine to Google Kubernetes Engine migrations, Migrate to Containers may fail to recognize the UUID of the source VM's disk. You can add it manually:

  1. Load the logs for the pod using kubectl or Stackdriver.

  2. If you see the message `[hcrunner] - Failed to find boot partition`, continue with the following steps.

**Note:** `hcrunner` is only used in the Linux flow. If you're migrating a Windows workload and there is mention of `hcrunner` in the logs, then you need to set the OS type as Windows when creating the migration.
  3. Find the UUID for the boot disk printed in one of the messages, which will be a string of hexadecimal values. In the example below, the UUID is `e823158e-f290-4f91-9c3d-6f33367ae0da`.
         
         [util] - SHELL OUTPUT: {"name": "/dev/sdb1", "partflags": null, "parttype":
         "0x83", "uuid": "<strong>e823158e-f290-4f91-9c3d-6f33367ae0da</strong>",
         "fstype": "ext4"}
         

  4. Delete the existing workload using its YAML file:
         
         kubectl delete -f
         

  5. Open the YAML file in a text editor and find the section named `env`.

  6. Add the following:
         
         - name: "HC_BOOTDEVICE_UUID"
               value: ""
         



  * If you see the message `touch: cannot touch '/vlsdata/etc/fstab': No such file or directory`, check the following:

    * Your CSI driver workloads have a status of OK in the console.
    * Your workload is in the same cluster as your Migrate to Containers deployment.
  * If you see one of the following messages, delete the workload's failing `PersistentVolumeClaim` and recreate it.

    * `hcutil.Error: Failed mount -o rw None /vlsdata (32) (Output:mount: /vlsdata: special device None does not exist.`
    * `[hcrunner] - [Errno 30] Read-only file system: '/vlsdata/rootdir/etc/dhcp/dhclient-up-hooks`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
