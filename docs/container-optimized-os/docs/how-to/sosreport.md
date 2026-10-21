---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/sosreport/
title: Collecting debugging information using sosreport \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:16:41.806412+00:00
---

# Collecting debugging information using sosreport  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/sosreport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Collecting debugging information using sosreport Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS includes the `sosreport` utility, which collects information on demand to help you debug problems in a Container-Optimized OS virtual machine instance. The information is collected and stored locally on the filesystem of the instance. Google does not collect or store this data elsewhere.

If you open a support case with [Google Cloud support](https://docs.cloud.google.com/support) due to problems with your instance, you may be asked to provide the `sosreport` data as part of the investigation. This page shows you how to collect this information.

**Note:** Creating the report consumes CPU and memory resource, and storing the report consumes disk space and disk I/O bandwidth resource on the node. The amount of resource consumed cannot be easily estimated.**Note:** When troubleshooting node availability and startup issues, collecting `sosreport` might be challenging. Node auto-repair will terminate and re-create the node after some time of unavailability. See [Disabling node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable) if `sosreport` collection cannot be done before the node is terminated by auto-repair. If auto-repair cannot be disabled because the cluster is in release channel, contact Cloud Customer Care for assistance.

The output of `sosreport` is stored without encryption in a `.tar.xz` archive. The archive may contain personally identifiable information (PII), because it collects data from many critical system components (e.g. journald). The archive can be inspected on the instance, and most content is in plain text. The `sosreport` tool is open source, and you can [review its code](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/master/project-lakitu/app-admin/sosreport/).

## Collecting the sosreport data

To generate a sosreport:

  1. Connect to the instance using the `gcloud compute ssh` command.
         
         gcloud compute ssh [INSTANCE_NAME] --zone [ZONE] --project [PROJECT_ID]
         

  2. Check the OS version:
         
         sudo cat /etc/os-release| egrep -w 'NAME|VERSION'
         

The output is similar to the following:
         
         NAME="Container-Optimized OS"
         VERSION=105
         

  3. Run the `sos` command that corresponds to your OS version:




### COS 85 and earlier

Run the following `sosreport` command to collect the logs:
    
    
    sudo sosreport --all-logs --batch --tmp-dir=/var
    

If the previous command fails with `sosreport: command not found`, install the `sosreport` package and then run the previous `sosreport` command:
    
    
    sudo toolbox
    sudo apt install sosreport -y
    

### COS 105 and later

Run the following `sos` command to collect the logs:
    
    
    sudo sos report --all-logs --batch --tmp-dir=/var
    

If the previous command fails with `sos: command not found`, install the `sosreport` package and then run the previous `sos report` command:
    
    
    sudo toolbox
    sudo apt install sosreport -y
    

### Ubuntu-18 and earlier

Run the following `sosreport` command to collect the logs:
    
    
    sudo sosreport --all-logs --batch --tmp-dir=/var
    

If the previous command fails with `sosreport: command not found`, install the `sosreport` package and then run the previous `sosreport` command:
    
    
    sudo apt install sosreport
    

### Ubuntu-20 and later

Run the following `sos` command to collect the logs:
    
    
    sudo sos report --all-logs --batch --tmp-dir=/var
    

If the previous command fails with `sos: command not found`, install the `sosreport` package and then run the previous `sos report` command:
    
    
    sudo apt install sosreport
    

You can change the directory where the report is stored by passing a different directory to the `--tmp-dir` option. You can also change the command's default behavior by editing `/etc/sos.conf` on the instance.

The output is stored in a `.tar.xz` file in the directory you specify using the `--tmp-dir` option. The location and checksum of the `.tar.xz` file is shown on STDOUT.
    
    
    Your sosreport has been generated and saved in:
      /var/sosreport-cos-20181106231224.tar.xz
    
    The checksum is: 5a8b97c6020346a688254c8b04ef86ec
    

## Viewing the collected data

The report is owned by `root` and is not readable by other users. Use the following commands to change the owner to your current user and make it readable by you. Do not make it world-readable.
    
    
    TARBALL=[PATH/TO/TARBALL]
    sudo chown $(whoami) $TARBALL
    chmod +r $TARBALL
    

Then, if you want to view the content of the report on the node, you can extract it by running below command:
    
    
    tar xvf $TARBALL
    

The individual report files are now available in a directory in the same location as the `.tar.xz`. You can view the logs using commands such as `less`, or you can use commands such as `grep` to find information in them.

**Note:** If you plan to share the report with Google, please do not modify any files in the report. If you have to modify some files, please also tell us what was modified when sharing the report.

## Download the report

To download the report to your local machine, use the `gcloud compute scp` command:
    
    
    gcloud compute scp $(whoami)@[INSTANCE_NAME]:[PATH/TO/FILE] [LOCAL/PATH/TO/DIRECTORY]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
