---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-firmware/
title: Verify a Confidential VM instance's firmware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:47.607311+00:00
---

# Verify a Confidential VM instance's firmware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-firmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Verify a Confidential VM instance's firmware Stay organized with collections  Save and categorize content based on your preferences. 

The firmware for all Confidential VM instances is UEFI, and based on the [Open Virtual Machine Firmware](https://github.com/tianocore/tianocore.github.io/wiki/OVMF) project. The firmware is managed by Google to maintain security, performance, and stability.

Google-managed firmware also ensures consistency of the values stored in the measurement registers on the root of trust for a Confidential VM instance. This helps to prevent Confidential Computing workloads from being blocked by attestation verification when a Confidential VM instance's firmware is updated.

To help establish that your Confidential VM instance is running on genuine Google-managed firmware, you can perform the following tasks:

  * Retrieve a Google-signed _launch endorsement_ on Confidential VM instances with AMD SEV-SNP or Intel TDX enabled. A launch endorsement contains precomputed and signed measurements related to the firmware.

  * Verify the launch endorsement by comparing against architecture-specific measurements.

  * Verify the UEFI binary is endorsed by Google and unmodified.




In addition to remote attestation, you can include firmware verification as part of your security policy that determines whether a Confidential VM instance should have access to protected resources.

## Retrieve launch endorsements

You can retrieve launch endorsements using Google tools, or your own.

### Retrieve launch endorsements with Google tools

To retrieve a launch endorsement from an AMD SEV-SNP or Intel TDX Confidential VM instance using Google tools:

  1. [Use SSH to connect to your Confidential VM instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).

  2. Use either [Go-TPM-Tools](https://github.com/google/go-tpm-tools) (AMD SEV-SNP or Intel TDX) or [SEV Guest](https://github.com/google/go-sev-guest) (AMD SEV-SNP) to retrieve an attestation report and associated certificates.

  3. Use [`gcetcbendorsement`](https://github.com/google/gce-tcb-verifier/tree/main/gcetcbendorsement/) to extract the UEFI endorsement from the attestation and store it in a file. You can then verify that the endorsement is rooted to Google and that the attestation report's measurement is among the signed measurements.




### Retrieve launch endorsements with your own tools

To retrieve a launch endorsement using your own tools, complete the following instructions.

### AMD SEV-SNP

  1. [Make an extended guest request](https://www.kernel.org/doc/html/latest/virt/coco/sev-guest.html) to the AMD Secure Processor to retrieve an attestation report.

  2. Extract the report's 384-bit measurement stored at offset `90h`. For more information, see [SEV Secure Nested Paging Firmware ABI Specification](https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/specifications/56860.pdf), chapter 7.3, table 22.

  3. Use the 384-bit measurement to download a serialized reference launch endorsement from the following Cloud Storage bucket:
         
         gs://gce_tcb_integrity/ovmf_x64_csm/sevsnp/384_BIT_MEASUREMENT.binarypb
         

**Note:** This Cloud Storage bucket is only hosted in one region, `us-west1`. It is a best-effort backup established for transparency purposes.
  4. Decode the BINARYPB file with a tool like [protoc](https://grpc.io/docs/protoc-installation/), using the `VMLaunchEndorsement` message definition:
         
         message VMLaunchEndorsement {
           bytes serialized_uefi_golden = 1;
           bytes signature = 2;
         }
         




#### Alternative launch endorsement locations

The launch endorsement might also be made available in a GUID table in the AMD SEV-SNP certificate delivery mechanism. It has the following GUID:

`9f4116cd-c503-4f5a-8f6f-fb68882f4ce2`

The GUID table is documented in the [AMD Guest-Hypervisor Communication Block specification](https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/specifications/56421.pdf), in the SNP Extended Guest Request section.

There might also be references to local and remote locations of the launch endorsement in the Trusted Computing Group PC client event log, found in the SP800-155 event as documented in [TCG PC Client Platform Firmware Profile Specification Version 1.06 Revision 52](https://trustedcomputinggroup.org/wp-content/uploads/PC-Client-Platform-Firmware-Profile-Version-1.06-Revision-52_pub.pdf).

### Intel TDX

  1. Make a [configfs-tsm report](https://www.kernel.org/doc/Documentation/ABI/testing/configfs-tsm) entry:
         
         name=/sys/kernel/config/tsm/report/report0
         mkdir "${name}"
         cat "${your_nonce_file}" > "${name}/inblob"
         cat "${name}/outblob" > "${your_quote_destination}"
         

  2. Extract the quote's 384-bit trust domain measurement MRTD stored at offset `b8h` (for TDX Module 1.5). For more information, see [TDX DCAP quoting library](https://download.01.org/intel-sgx/latest/dcap-latest/linux/docs/Intel_TDX_DCAP_Quoting_Library_API.pdf).

  3. Use the 384-bit measurement to download a serialized reference launch endorsement from the following Cloud Storage bucket:
         
         gs://gce_tcb_integrity/ovmf_x64_csm/tdx/384_BIT_MEASUREMENT.binarypb
         

**Note:** This Cloud Storage bucket is only hosted in one region, `us-west1`. It is a best-effort backup established for transparency purposes.
  4. Decode the launch endorsement with a tool like [protoc](https://grpc.io/docs/protoc-installation/), using the `VMLaunchEndorsement` message definition:
         
         message VMLaunchEndorsement {
           bytes serialized_uefi_golden = 1;
           bytes signature = 2;
         }
         




## Launch endorsement example

A launch endorsement looks similar to the following example:
    
    
    VMLaunchEndorsement:
    serialized_uefi_golden: "SERIALIZED_BYTES"
    signature: "LAUNCH_ENDORSEMENT_SIGNATURE_BYTES"
    

### UEFI golden measurements

The `serialized_uefi_golden` field contains a serialized version of multiple values, as defined by the following protocol buffer:
    
    
    message VMGoldenMeasurement {
      google.protobuf.Timestamp timestamp = 1;
    
      // The changelist number this UEFI was built from.
      uint64 cl_spec = 2;
    
      // DER format certificate of the key that signed this document.
      bytes cert = 4;
    
      // SHA-384 digest of the UEFI binary without TEE-specifics about launch.
      bytes digest = 5;
    
      // A sequence of PEM-encoded certificates of keys used in cert in Root ...
      // final intermediate order. The last certificate will have a signed cert.
      bytes ca_bundle = 6;
    
      VMSevSnp sev_snp = 7;
    
      VMTdx tdx = 8;
    }
    

The `VMSevSnp` field in the `VMGoldenMeasurement` message is defined by the following protocol buffer:
    
    
    message VMSevSnp {
      // The Google-reported security version number of this UEFI on SEV-SNP.
      uint32 svn = 1;
    
      // Expected MEASUREMENT report field values given [key]-many VMSAs at launch.
      map<uint32, bytes> measurements = 2; // bytes size 48
    
      // A UUID that Google uses for its CVM UEFIs
      bytes family_id = 3; // size 16
    
      // A UUID to name this specific release of the UEFI image. This is randomly
      // generated with each build.
      bytes image_id = 4; // size 16
    
      // The launch policy that verifiers should expect with this UEFI.
      uint64 policy = 5;
    
      // Optional. PEM-encoded certs for Identity..Author..Root. If a singleton,
      // only an Id-key is used.
      bytes ca_bundle = 6;
    }
    

The `VMTdx` field in the `VMGoldenMeasurement` message is defined by the following protocol buffer:
    
    
    message VMTdx {
      message Measurement {
        // The amount of RAM in GiB provided to the VM. This is relevant to the
        // construction of the measured TDHOB page that includes memory region
        // resource attributes.
        uint32 ram_gib = 1;
        // If true, EFI_UNACCEPTED_MEMORY not presented to guest.
        // All memory is accepted by the firmware. Relevant to the TDHOB page
        // since the resource attribute will include
        // EFI_RESOURCE_ATTRIBUTE_NEEDS_EARLY_ACCEPT.
        bool early_accept = 2;
        // The SHA-384 digest of the measurement operations for the VM at launch.
        bytes mrtd = 3;
      }
      // The Google-reported security version number of this UEFI on TDX.
      uint32 svn = 1;
    
      // Expected MRTD report field values given legal configurations.
      repeated Measurement measurements = 2;
    }
    

To unpack and decode these values from the `serialized_uefi_golden field` with your own tooling, complete the following steps:

  1. Allocate a new `VMGoldenMeasurement` message.

  2. Unmarshal `serialized_uefi_golden` into the message.




Alternatively, you can use the ` [ gcetcbendorsement](https://github.com/google/gce-tcb-verifier/tree/main/gcetcbendorsement/) inspect ` command.

## Verify launch endorsements

After retrieving a launch endorsement, verify its signature, and then integrate its measurements into your security policy where appropriate.

### Verify a launch endorsement signature

You can verify a launch endorsement's signature by including the [Compute Engine Confidential Computing trusted computing base root key certificate](https://pki.goog/cloud_integrity/GCE-cc-tcb-root_1.crt) in your trust anchors.

**Note:** Root key rotations are accompanied by a [Mandatory Service Announcement](https://docs.cloud.google.com/advisory-notifications/docs/security-msas-overview). Old root keys won't certify signing keys 6 months after rotation.

The `cert` field of the `VMGoldenMeasurement` in the launch endorsement contains a DER-encoded X.509v3 certificate of the endorsement-signing key's public key. The certificate is signed by the root key.

You can use [gcetcbendorsement](https://github.com/google/gce-tcb-verifier/tree/main/gcetcbendorsement/) to show which `openssl` commands to run to verify the signature. For example, if you run the following command:
    
    
    gcetcbendorsement verify --show LAUNCH_ENDORSEMENT_FILENAME.binarypb
    

You should receive a response similar to the following example:
    
    
    openssl verify -CAfile <(openssl x509 -outform pem -in <(curl https://pki.goog/cloud_integrity/GCE-cc-tcb-root_1.crt)) \
        <(gcetcbendorsement inspect mask "LAUNCH_ENDORSEMENT_FILENAME.binarypb" --path=cert) \
        && \
        openssl pkeyutl -verify -pkeyopt rsa_padding_mode:pss \
            -pkeyopt rsa_pss_saltlen:32 -pkeyopt digest:sha256 -pkeyopt rsa_mgf1_md:sha256 -pubin \
            -inkey <(openssl x509 -pubkey -nocert -outform pem -in <(gcetcbendorsement inspect mask "LAUNCH_ENDORSEMENT_FILENAME.binarypb" --path=cert)) \
            -sigfile <(gcetcbendorsement inspect signature "LAUNCH_ENDORSEMENT_FILENAME.binarypb") -keyform PEM \
            -in <(openssl dgst -sha256 -binary <(gcetcbendorsement inspect payload "LAUNCH_ENDORSEMENT_FILENAME.binarypb")
    

If you prefer to use your own tooling, you can replace the `gcetcbendorsement inspect` commands used in the response with your own protocol buffer extraction logic for the named fields of the deserialized `VMGoldenMeasurement` message.

### Verify launch endorsement measurements

The sample code for how a launch endorsement is created is available at the [`gce-tcb-verifier` GitHub repository](https://github.com/google/gce-tcb-verifier). You can use this to understand how Google has derived the measurements from the UEFI, and to incorporate relevant measurements into your security policy.

For example, you might check that the firmware is signed by the firmware vendor, and compare the architecture-specific measurements against precomputed and signed values provided in the `VMLaunchEndorsement` message.

Although Compute Engine virtual firmware is upgraded on reset, the PCR0 value doesn't change. Because of this, the `svn` value of the firmware in the signed measurement might differ from the `EV_S_CRTM_VERSION` measured to PCR0, and the `EV_POST_CODE` event in the firmware blob digest is skipped.

## Verify a Confidential VM instance's UEFI binary

  1. From a launch endorsement, unpack the `serialized_uefi_golden` value into a `VMGoldenMeasurement`. For examples, see the [implementation in Go](https://github.com/google/gce-tcb-verifier/blob/main/proto/endorsement/endorsement.pb.go), or the protoc compilation of [`endorsement.proto`](https://github.com/google/gce-tcb-verifier/blob/main/proto/endorsement.proto) for another language that supports protocol buffers.

  2. Retrieve the digest value from `VMGoldenMeasurement`. This is the SHA-384 digest of the UEFI binary that the Confidential VM instance is running on.

  3. Use the SHA-384 digest to download the firmware binary from the following Cloud Storage bucket:

`gs://gce_tcb_integrity/ovmf_x64_csm/UEFI_BINARY_DIGEST.fd`

**Note:** This Cloud Storage bucket is only hosted in one region, `us-west1`. It is a best-effort backup established for transparency purposes.
  4. If it's a valid URL and the firmware downloads, perform an SHA-384 hash on the firmware binary. If it matches the digest from the golden measurement, the firmware running on your Confidential VM instance is running unmodified.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
