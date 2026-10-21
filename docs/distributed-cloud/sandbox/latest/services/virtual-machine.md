---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/virtual-machine/
title: Deploy a VM workload \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:13:52.661607+00:00
---

# Deploy a VM workload  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/virtual-machine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Deploy a VM workload Stay organized with collections  Save and categorize content based on your preferences. 

You can create, deploy, and connect to your test virtual machines (VM) workloads in GDC Sandbox (GDC Sandbox). To create and start a test VM workload, follow the steps in [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/vms/create-a-vm/create-and-start).

To view a list of images GDC Sandbox provides, run:
    
    
    kubectl --kubeconfig KUBECONFIG get
    virtualmachineimage.virtualmachine.gdc.goog -n gpc-system
    

Replace `KUBECONFIG` with the path of your kubeconfig file for the Management API server.

## Connect to a VM

  1. Follow the steps in [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/vms/connect-to-vm/connect-to-a-vm#api) to:

     1. Create an SSH key pair and a username.
     2. Upload your key to the VM and create a Kubernetes resource (VirtualMachineAccessRequest) with your public key, username, and time to live (TTL) value for the key.
  2. Initiate a secure tunnel. If you have a running instance of `sshuttle` as described in [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect), terminate that process.
         
         sshuttle -r zone1-org-1-data@GDC_SANDBOX_INSTANCE_NAME --no-latency-control \
               --ssh-cmd 'gcloud compute ssh --project PROJECT_NAME --zone ZONE --tunnel-through-iap' \
               10.200.0.0/16 --dns
         

Replace the following with the values provided to you by the GDC Sandbox team:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone containing your GDC Sandbox environment.
  3. While the command is running, run the ssh command to the VM instance in another terminal
         
         ssh -i PATH_TO_PRIVATE_KEY USERNAME@EXTERNAL_IP
         

Replace the following values:

     * `PATH_TO_PRIVATE_KEY` with the path to the private SSH key file that corresponds to the public key you added to the VM.
     * `USERNAME` with the username that you specified when you created the SSH key. For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP` with the external [ingress IP address](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/vms/connect-to-vm/ip-addresses#ingress) of the VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
