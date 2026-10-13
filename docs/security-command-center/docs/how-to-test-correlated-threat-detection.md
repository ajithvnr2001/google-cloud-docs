---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-correlated-threat-detection/
title: Test Correlated Threats \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:37.326914+00:00
---

# Test Correlated Threats  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-correlated-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test Correlated Threats Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how you can verify that Correlated Threats is working by emulating threats to intentionally trigger Security Command Center detectors and create findings. These threat findings then create Correlated Threats issues for each rule.

To learn more about Correlated Threats, see [Correlated Threats overview](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview). If you want to generate findings that produce Correlated Threats, you must enable the appropriate threat detection services in [Security Command Center settings](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

## Set up your environment

These testing procedures require both a GKE cluster and the ability to provision Compute Engine VMs. Ensure that your test cluster is on a supported version of Google Kubernetes Engine (GKE). For more information, see [Using a supported GKE version](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).

Before you test Correlated Threats, you need to first select a project with the appropriate GKE cluster, activate Cloud Shell, and set several environment variables. To do this, follow these steps:

  1. Go to the [Google Cloud console](https://console.cloud.google.com/projectselector2).

[Go to the Google Cloud console](https://console.cloud.google.com/projectselector2)

  2. Select the project where you want to test the Correlated Threats.

  3. Click **Activate Cloud Shell**. ![](https://docs.cloud.google.com/static/security-command-center/images/activate-cloud-shell.svg)

  4. In Cloud Shell, set environment variables.

     1. Specify the project, zone, and GKE cluster to use for testing:
            
            export PROJECT=PROJECT_ID
            export ZONE=ZONE
            export CLUSTER_NAME=CLUSTER_NAME
            

     2. Obtain the credentials for your cluster:
            
            gcloud container clusters get-credentials $CLUSTER_NAME \
                --zone $ZONE \
                --project $PROJECT
            




## Emulate a cryptocurrency mining attack

This section describes how to emulate cryptocurrency mining and create a Correlated Threats issue using the Google Cloud console and Cloud Shell. To do this, you first activate Cloud Shell, select a project, and then perform the test.

To test Correlated Threats by emulating cryptocurrency mining, follow these steps:

  1. Set up your environment

  2. To trigger a cryptocurrency Correlated Threats issue, create two findings: `Impact: suspicious crypto mining activity using the stratum protocol` and `Malware: Cryptomining Bad IP`. To trigger these two findings, run the following commands:
         
         tag="correlated-threat-test-crypto-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
         kubectl run \
              --restart=Never \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- bash -c \
              "apt-get update ; apt-get install -y curl ; cp /bin/ls /tmp/curl; /tmp/curl --url=stratum+tcp ; for i in {1..5}; do curl 34.66.147.47 > /dev/null; done; sleep infinity"
         

It can take up to an hour for the Correlated Threats issue to appear.

  3. After the Correlated Threats issue is generated, perform cleanup by running the following command to delete the Kubernetes Pod used for testing.
         
         kubectl delete pod "$tag"
         




## Emulate a malware attack

This section describes how to emulate a malware attack and create a Correlated Threats issue using the Google Cloud console and Cloud Shell. To do this, first activate Cloud Shell, select a project, and then perform the test.

To test Correlated Threats by emulating a malware attack, follow these steps:

  1. Set up your environment.

  2. To trigger a malware Correlated Threats issue, you create two findings: `Execution: Local Reconnaissance Tool Execution` and `Execution: Added Malicious Binary Executed`. To create an Ubuntu 24.04 Pod in your GKE cluster and trigger these two findings, run the following commands:
         
         tag="correlated-threat-test-malware-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
         eicar='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
         kubectl run \
              --restart=Never \
              --image marketplace.gcr.io/google/ubuntu2404:latest \
              "$tag" -- sh -c \
              "cp /bin/ls /tmp/linenum.sh; /tmp/linenum.sh; touch /tmp/test_mal_file; echo -n '$eicar' > /tmp/test_mal_file; chmod 700 /tmp/test_mal_file; /tmp/test_mal_file; sleep infinity"
         

It can take up to an hour for the Correlated Threats issue to appear.

  3. After the correlated threat issue is generated, perform cleanup by running the following command to delete the Kubernetes Pod used for testing.
         
         kubectl delete pod "$tag"
         




## Emulate a lateral movement attack on GKE

This section describes how to emulate a lateral movement attack on GKE and create a Correlated Threats issue using the Google Cloud console and Cloud Shell. To do this, you first activate Cloud Shell, select a project, and then perform the test.

To test Correlated Threats by emulating a lateral movement attack, follow these steps:

  1. Set up your environment.

  2. To trigger a lateral movement Correlated Threats issue, you create two findings: `Privilege Escalation: Launch of privileged Kubernetes container` and `Execution: Container Escape`. To create an Ubuntu Pod in your GKE cluster and trigger these two findings, run the following commands:
         
         tag="correlated-threat-test-podlatmove-$(date -u +%Y-%m-%d-%H-%M-%S-utc)"
         kubectl run \
              --restart=Never \
              --image marketplace.gcr.io/google/ubuntu2404:latest "$tag" \
              --privileged \
              -- bash -c \
                 "cp /bin/ls /tmp/botb-linux-amd64; sleep 300; /tmp/botb-linux-amd64 -autopwn; sleep infinity"
         

It can take up to an hour for the Correlated Threats issue to appear.

  3. After the Correlated Threats issue is generated, perform cleanup by running the following command to delete the Kubernetes Pod used for testing.
         
         kubectl delete pod "$tag"
         




## Emulate a lateral movement attack on Compute Engine

This section describes how to emulate a lateral movement attack on Compute Engine and create a Correlated Threats issue using the Google Cloud console and Cloud Shell. To do this, you first activate Cloud Shell, select a project, and then perform the test.

To test Correlated Threats by emulating a lateral movement attack, follow these steps:

  1. Set up your environment.

  2. Create a file named `lateral_movement_test.sh` with the following content. This script creates multiple Compute Engine VMs and generates the following two findings: `Lateral Movement: Modified Boot Disk Attached to Instance` and `Malware: Bad IP`.
         
         #!/bin/bash
         # emulates a boot disk swap followed by malicious IP to trigger correlated threats.
         
         set -euo pipefail
         
         # --- Default values ---
         readonly IMAGE_FAMILY="debian-12"
         readonly IMAGE_PROJECT="debian-cloud"
         TIMESTAMP=$(date +%s)
         TARGET_INSTANCE_NAME="target-vm-${TIMESTAMP}"
         WORKER_INSTANCE_NAME="worker-vm-${TIMESTAMP}"
         PROJECT_ID=""
         ZONE=""
         
         # --- Usage function ---
         usage() {
           echo "Usage: $0 --project_id <PROJECT_ID> --zone <ZONE> [OPTIONS]"
           echo "emulates a boot disk swap followed by malicious IP to trigger correlated threats."
           echo
           echo "Required arguments:"
           echo "  --project_id <PROJECT_ID>  Your Google Cloud Project ID"
           echo "  --zone <ZONE>              The Google Cloud zone to create resources in (e.g., us-central1-a)"
           echo
           echo "Optional arguments:"
           echo "  --help                   Display this help message"
         }
         
         # --- Function to run gcloud commands with --quiet ---
         run_gcloud() {
           echo "Running: gcloud $*"
           gcloud "$@" --quiet
         }
         
         main() {
           # --- Parse arguments ---
           while [[ $# -gt 0 ]]; do
             case "$1" in
               --project_id)
                 PROJECT_ID="$2"
                 shift 2
                 ;;
               --zone)
                 ZONE="$2"
                 shift 2
                 ;;
               --help)
                 usage
                 exit 0
                 ;;
               *)
                 echo "Unknown option: $1" >&2
                 usage >&2
                 exit 1
                 ;;
             esac
           done
         
           # --- Validate required arguments ---
           if [[ -z "${PROJECT_ID}" ]]; then
             echo "Error: --project_id is required." >&2
             usage >&2
             exit 1
           fi
         
           if [[ -z "${ZONE}" ]]; then
             echo "Error: --zone is required." >&2
             usage >&2
             exit 1
           fi
         
           # The boot disk name defaults to the instance name
           BOOT_DISK_NAME=$TARGET_INSTANCE_NAME
         
           echo "Starting script with the following settings:"
           echo "PROJECT_ID:           ${PROJECT_ID}"
           echo "ZONE:                 ${ZONE}"
           echo "TARGET_INSTANCE_NAME: ${TARGET_INSTANCE_NAME}"
           echo "WORKER_INSTANCE_NAME: ${WORKER_INSTANCE_NAME}"
           echo "BOOT_DISK_NAME:       ${BOOT_DISK_NAME}"
           echo "IMAGE_FAMILY:         ${IMAGE_FAMILY}"
           echo "IMAGE_PROJECT:        ${IMAGE_PROJECT}"
           echo "--------------------------------------------------"
         
           # Set context
           gcloud config set project "${PROJECT_ID}"
           gcloud config set compute/zone "${ZONE}"
         
           echo "Step 1: Create target VM: ${TARGET_INSTANCE_NAME}"
           run_gcloud compute instances create "${TARGET_INSTANCE_NAME}" \
             --image-family="${IMAGE_FAMILY}" \
             --image-project="${IMAGE_PROJECT}" \
             --no-address
         
           echo "Step 2: Create worker VM: ${WORKER_INSTANCE_NAME}"
           run_gcloud compute instances create "${WORKER_INSTANCE_NAME}" \
             --image-family="${IMAGE_FAMILY}" \
             --image-project="${IMAGE_PROJECT}" \
             --no-address
         
           echo "Step 3: Stop target VM: ${TARGET_INSTANCE_NAME}"
           run_gcloud compute instances stop "${TARGET_INSTANCE_NAME}"
         
           echo "Step 4: Detach boot disk from target VM"
           run_gcloud compute instances detach-disk "${TARGET_INSTANCE_NAME}" --disk="${BOOT_DISK_NAME}"
         
           echo "Step 5: Attach disk to worker VM: ${WORKER_INSTANCE_NAME}"
           run_gcloud compute instances attach-disk "${WORKER_INSTANCE_NAME}" --disk="${BOOT_DISK_NAME}"
         
           echo " << At this point, the disk is attached to the worker VM >>"
           echo " << Malicious modifications could theoretically be made here >>"
         
           echo "Step 6: Detach disk from worker VM"
           run_gcloud compute instances detach-disk "${WORKER_INSTANCE_NAME}" --disk="${BOOT_DISK_NAME}"
         
           echo "Step 7: Re-attach disk to target VM as boot disk"
           run_gcloud compute instances attach-disk "${TARGET_INSTANCE_NAME}" --disk="${BOOT_DISK_NAME}" --boot
         
           echo "Step 8: Start target VM"
           run_gcloud compute instances start "${TARGET_INSTANCE_NAME}"
         
           echo -n "Step 9: Wait for instance SSH to be available"
           until gcloud compute ssh "${TARGET_INSTANCE_NAME}" --command="true" 2>/dev/null; do
             echo -n "."
             sleep 2
           done
           echo
         
           echo "Step 10: Trigger bad IP findings"
           run_gcloud compute ssh "${TARGET_INSTANCE_NAME}" \
             --command="for i in {1..5}; do curl 34.66.147.47 > /dev/null 2>/dev/null; done;"
         
           echo "Step 11: Delete worker VM: ${WORKER_INSTANCE_NAME}"
           run_gcloud compute instances delete "${WORKER_INSTANCE_NAME}"
         
           echo "--- Testing Complete ---"
           echo "The script has completed executing the patterns to trigger a correlated"
           echo "threats issue. Check the Security Command Center Issues page."
           echo
           echo "After observing the issue, delete the target VM using:"
           echo "  gcloud compute instances delete ${TARGET_INSTANCE_NAME}"
         
           echo "${TARGET_INSTANCE_NAME}" > ./.lateral_movement_test_name
         }
         
         main "$@"
         

  3. Make the script executable:
         
         chmod +x lateral_movement_test.sh
         

  4. To generate findings, run the script:
         
         ./lateral_movement_test.sh --project_id $PROJECT --zone $ZONE
         

It can take up to an hour for the Correlated Threats issue to appear.

  5. After the issue is generated, perform cleanup using the command provided in the output of the test script:
         
         gcloud compute instances delete $(cat .lateral_movement_test_name) && rm -f .lateral_movement_test_name
         




## What's next

  * Learn how [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) works.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
