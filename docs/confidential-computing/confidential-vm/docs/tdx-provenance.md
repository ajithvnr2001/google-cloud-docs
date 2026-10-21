---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/tdx-provenance/
title: Verify an Intel TDX VM instance runs on Google Cloud \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:27.813730+00:00
---

# Verify an Intel TDX VM instance runs on Google Cloud  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/tdx-provenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Verify an Intel TDX VM instance runs on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

To determine that an Intel TDX Confidential VM instance is running on Google Cloud, you need to establish its _provenance_. Establishing provenance involves the following checks:

  * **Quote verification and challenge binding** : Verify the authenticity of the Intel TDX quote by using the embedded Intel root certificate, and optionally verify freshness against an expected challenge in the quote's `REPORT_DATA` field.

  * **Host provenance verification** : Extract the platform provisioning ID (PPID) from the quote's embedded PCK certificate. Use the PPID to fetch the host registry JSON document from a Cloud Storage bucket to verify provenance.

  * **Instance provenance verification** : Use the project number, zone, and instance ID (PZID) of the Confidential VM instance to calculate a SHA-384 digest, and then verify that the digest matches the `MR_OWNER` field value in the Intel TDX quote.




## Verify provenance remotely

We recommend using the [`gceprovenance`](https://github.com/google/go-tdx-guest/tree/main/tools/gceprovenance) tool to determine the provenance of Intel TDX machines. The tool automates extracting the required values and fetching the provenance document.

To verify provenance remotely using `gceprovenance`, complete the following instructions:

  1. Clone the `go-tdx-guest` GitHub repository to your remote verifier:
         
         git clone https://github.com/google/go-tdx-guest.git
         

  2. Depending on your guest operating system, you might need to install some Go dependencies to build the tools in `go-tdx-guest`. How you do this changes depending on your operating system. For example, the following commands install the necessary dependencies on Ubuntu:
         
         sudo apt update
         sudo apt install golang-go build-essential
         

  3. Build the `gceprovenance` tool:
         
         go build -C go-tdx-guest/tools/gceprovenance .
         

  4. Generate a 64-byte challenge that the Intel TDX Confidential VM instance must bind to its quote:
         
         head -c 64 /dev/urandom > challenge.bin
         

  5. Send the challenge file to the Intel TDX Confidential VM instance you want to verify.

  6. On the Intel TDX Confidential VM instance, pass the challenge file as input (`inblob`) to the Linux ConfigFS at `/sys/kernel/config/tsm/report/`:
         
         sudo mkdir -p /sys/kernel/config/tsm/report/report0
         sudo sh -c 'cat challenge.bin > /sys/kernel/config/tsm/report/report0/inblob'
         

The challenge is then written into the quote's `REPORT_DATA` field by the system.

  7. Retrieve the raw quote bytes from the resulting `outblob` file, and clean up the `report0` directory:
         
         sudo cat /sys/kernel/config/tsm/report/report0/outblob > quote.bin
         sudo rmdir /sys/kernel/config/tsm/report/report0
         

  8. Query the local metadata server for the instance ID, project number, and zone of the Confidential VM instance:
         
         PROJECT_NUMBER=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/numeric-project-id" -H "Metadata-Flavor: Google")
         INSTANCE_ID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/id" -H "Metadata-Flavor: Google")
         ZONE_PATH=$(curl -s "http://metadata.google.internal/computeMetadata/v1/instance/zone" -H "Metadata-Flavor: Google")
         ZONE=$(basename "$ZONE_PATH")
         

  9. Send the quote binary (`quote.bin`), the project number, the instance ID, and the zone to the remote verifier.

  10. On the remote verifier, convert your challenge to a 128-character hexadecimal string, and then pass it to `gceprovenance`. The tool then verifies the quote's signature and provenance bindings:
         
         CHALLENGE_HEX=$(hexdump -v -e '/1 "%02x"' challenge.bin)
         ./go-tdx-guest/tools/gceprovenance/gceprovenance verify \
             -quote PATH_TO_QUOTE \
             -instance projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID \
             -challenge $CHALLENGE_HEX
         

Provide the following:

     * `PATH_TO_QUOTE`: The path to the supplied quote file.

     * `PROJECT_NUMBER`: The supplied project number.

     * `ZONE`: The supplied zone.

     * `INSTANCE_ID`: The supplied Confidential VM instance ID.

**Note:** The `gceprovenance` tool performs a basic quote authenticity check by verifying the quote's signature and the embedded certificate chain. For complete TCB evaluation, certificate revocation list (CRL) checks, or RTMR verification, use the `check` CLI tool or the `verify` package in the [`go-tdx-guest` repository](https://github.com/google/go-tdx-guest/) to verify the quote.

A succesful response looks similar to the following:
    
    GCE TDX provenance verification: OK
    
    Instance
      Zone: ZONE
      Project: PROJECT_NUMBER
      Instance ID: INSTANCE_ID
    
    Checks
      Quote verification: OK
      REPORT_DATA challenge: OK
      Host registry document: found
      PZID binding: OK
    
    PPID: PPID
    Quote: tdx_quote.bin
    Host registry: host_registry.json
    




For other `gceprovenance` commands, see the [GitHub repository](https://github.com/google/go-tdx-guest/tree/main/tools/gceprovenance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
