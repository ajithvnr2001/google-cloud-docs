---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/token-claims/
title: Google Cloud Attestation token claims \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:26.116681+00:00
---

# Google Cloud Attestation token claims  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/token-claims/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Reference ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents)



Send feedback 

#  Google Cloud Attestation token claims Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the claims in Google Cloud Attestation tokens. The tokens are entity attestation tokens (EATs), which are encoded as JSON web tokens (JWTs). JWTs can be decoded using tools such as <https://jwt.io/>.

The claims are defined at the Google Cloud Attestation [`well-known` endpoint](https://confidentialcomputing.googleapis.com/.well-known/openid-configuration).

## Decoded token examples

The claims in a Google Cloud Attestation token are different depending on the Confidential Computing technology used in your Confidential VM instance.

### AMD SEV

The following is an example of a decoded AMD SEV attestation token:
    
    
    {
      "alg": "RS256",
      "kid": "6e66f1aededf736581df2599ee20387718978dcd",
      "typ": "JWT"
    }.
    {
      "aud": "AUDIENCE",
      "exp": 1715359550,
      "iat": 1715355950,
      "iss": "https://confidentialcomputing.googleapis.com",
      "nbf": 1698861565,
      "sub": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME",
      "eat_nonce": [
        "thisIsAcustomNonce",
        "thisIsAMuchLongerCustomNonceWithPaddingFor74Bytes0000000000000000000000000"
      ],
      "secboot": true,
      "oemid": 11129,
      "hwmodel": "GCP_AMD_SEV",
      "swname": "GCE",
      "eat_profile": "https://cloud.google.com/confidential-computing/confidential-vm/docs/token-claims",
      "submods": {
        "gce": {
          "zone": "ZONE",
          "project_id": "PROJECT_ID",
          "project_number": "PROJECT_NUMBER",
          "instance_name": "INSTANCE_NAME",
          "instance_id": "INSTANCE_ID"
        }
      },
      "google_service_accounts": [
        "470652426305-compute@developer.gserviceaccount.com"
      ]
    }
    

### Intel TDX

The following is an example of a decoded Intel TDX attestation token:
    
    
    {
      "alg": "RS256",
      "kid": "6e66f1aededf736581df2599ee20387718978dcd",
      "typ": "JWT"
    }.
    {
      "aud": "AUDIENCE",
      "exp": 1715359550,
      "iat": 1715355950,
      "iss": "https://confidentialcomputing.googleapis.com",
      "nbf": 1698861565,
      "sub": "//compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID",
      "eat_nonce": "thisIsAcustomNonce",
      "secboot": true,
      "oemid": 11129,
      "hwmodel": "GCP_INTEL_TDX",
      "swname": "GCE",
      "dbgstat": "disabled-since-boot",
      "eat_profile": "https://cloud.google.com/confidential-computing/confidential-vm/docs/token-claims",
      "submods": {
        "gce": {
          "zone": "ZONE",
          "project_number": "PROJECT_NUMBER",
          "instance_id": "INSTANCE_ID"
        }
      },
      "tdx": {
        "gcp_attester_tcb_date": "2026-06-01T00:00:00Z",
        "tcb_evaluation_data_number": 17,
        "fmspc": "00806F000000",
        "tee_tcb_svn": "06010300000000000000000000000000",
        "pcesvn": 11,
        "sgx_tcb_comp_svn": "08080202040100060000000000000000",
        "xfam": "e702060000000000",
        "tdattributes": "0000000000000000",
        "mrtd": "c68518a0ebb42136c12b2275164f8c72f25fa9a343922286a41b52bc7e4c2787e35b7782b132454191a27e366bc33e8a",
        "rtmr0": "a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1",
        "rtmr1": "b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2",
        "rtmr2": "c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3c3",
        "rtmr3": "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      },
      "google_service_accounts": [
        "470652426305-compute@developer.gserviceaccount.com"
      ]
    }
    

## Token claims

The following table describes the high-level claims in a Google Cloud Attestation token. These claims are compliant with the [OpenID Connect 1.0 specification](https://openid.net/specs/openid-connect-core-1_0.html).

`well-known` endpoint values | Description  
---|---  
`claims_supported` | See Top-level claims.  
`id_token_signing_alg_values_supported` |  The signing algorithms (`alg` values) supported by the token. Confidential VM supports the `RS256` algorithm.   
`issuer` |  The HTTPS scheme that Confidential VM uses as its issuer identifier. The value is `https://confidentialcomputing.googleapis.com`.   
`jwks_uri` |  The path to the public keys used to verify the token signature. You can publish these keys in a Cloud Storage bucket.  You can find the `jwks_uri` keys in [ https://www.googleapis.com/service_accounts/v1/metadata/jwk/signer@confidentialspace-sign.iam.gserviceaccount.com](https://www.googleapis.com/service_accounts/v1/metadata/jwk/signer@confidentialspace-sign.iam.gserviceaccount.com).  An example value is `https://example.storage.googleapis.com/jwks.json`.   
`response_types_supported` |  The list of supported Confidential VM response types. Confidential VM supports `id_token`.   
`scopes_supported` |  The [ OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) scope values that the Confidential VM instance supports. Confidential VM supports `openid` only.   
`subject_types_supported` |  The subject identifier types that Confidential VM supports. Confidential VM supports `public`.   
  
## Top-level claims

The following table describes the top-level supported claims in a Google Cloud Attestation token.

Claim | Type | Description  
---|---|---  
`aud` | String |  The audience. For the default token used with a workload identity pool, the audience is `https://sts.googleapis.com`. This token is fetched every hour by the launcher in the Confidential VM instance.  For tokens with custom audiences, the audience is echoed from the audience in the token request. The maximum length is 512 bytes.   
`dbgstat` | String | The debug status for the hardware. Not available for AMD SEV.  
`eat_nonce` | String or string array |  One or more nonces for the attestation token. The values are echoed from the token options sent in the custom token request. Each nonce must be between 10 to 74 bytes inclusive. A maximum of six nonces are allowed.   
`eat_profile` | String |  The URI of the Entity Attestation Token (EAT) profile defining the token schema. The value is `https://cloud.google.com/confidential-computing/confidential-vm/docs/token-claims`.   
`exp` | Int, Unix timestamp |  The expiration time on or after which the token must not be accepted for processing. The value is a JSON number that represents the number of seconds from `1970-01-01T0:0:0Z` as measured in UTC until the expiry time.   
`google_service_accounts` | String array |  The validated service accounts that are running the Confidential VM workload.   
`hwmodel` | String |  The unique identifier for the hardware token. The identifier must be one of the following values: 

  * `GCP_AMD_SEV`
  * `GCP_AMD_SEV_ES`
  * `GCP_SHIELDED_VM`
  * `GCP_INTEL_TDX`

  
`iat` | Int, Unix timestamp |  The time when the JWT was issued. The value is a JSON number that represents the number of seconds from `1970-01-01T0:0:0Z` as measured in UTC until the issue time.   
`iss` | String |  The issuer of the token, which is set to `https://confidentialcomputing.googleapis.com`.   
`nbf` | Int, Unix timestamp |  The time after which the JWT is allowed to be processed. The value is a JSON number that represents the number of seconds from `1970-01-01T0:0:0Z` as measured in UTC.   
`oemid` | Uint64 |  The Google [ Private Enterprise Number (PEN)](https://pen.iana.org/pen/PenApplication.page), which is `11129`.   
`secboot` | Boolean |  Whether Secure Boot is enabled, which makes sure that the firmware and operating system are authenticated during the VM boot process.   
`sub` | String |  The subject identifying the virtual machine instance:

  * For AMD SEV instances, this is the instance's [ selfLink](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) URL: `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME`. 
  * For Intel TDX instances, this is the Compute Engine Resource Name containing immutable numeric IDs: `//compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/INSTANCE_ID`. 

  
`submods` | Array |  An array of various claims. See Submod claims.   
`swname` | String |  The name of the approved operating system for the VM. The value is always `GCE`.  
`tdx` | Object |  An object containing claims for Intel TDX instances. See Intel TDX claims.   
  
## Intel TDX claims

The following table describes the `tdx` claims in a Google Cloud Attestation token for Intel TDX instances.

Claim | Type | Description  
---|---|---  
`tcb_evaluation_data_number` | Uint32 |  Monotonically increasing Intel [ TCB Evaluation Data Number](https://api.portal.trustedservices.intel.com/content/documentation.html#pcs-tcb-info-tdx-v4) associated with the platform's FMSPC from Intel TCB Info.   
`gcp_attester_tcb_date` | String | Timestamp (UTC) of the Intel TCB evaluation baseline.  
`mrtd`1 | String (hex) |  Measurement of the initial Trust Domain contents and virtual firmware (OVMF).   
`rtmr0`1 | String (hex) |  Runtime measurement register 0 (virtual firmware configuration and system parameters).   
`rtmr1` | String (hex) |  Runtime measurement register 1 (guest OS bootloader and kernel measurements).   
`rtmr2` | String (hex) |  Runtime measurement register 2 (initial RAM disk (initramfs) and kernel command-line).   
`rtmr3` | String (hex) |  Runtime measurement register 3 (customer runtime extensions and applications).   
`fmspc` | String (hex) |  6-byte Family-Model-Stepping SKU for Intel Provisioning Certification Service (PCS) lookup.   
`tee_tcb_svn` | String (hex) |  16-byte array of TDX TCB component security version numbers when the Trust Domain was launched.   
`pcesvn` | Uint16 | SVN of the Provisioning Certification Enclave (PCE).  
`sgx_tcb_comp_svn` | String (hex) |  16-byte array of Intel SGX TCB component security version numbers.   
`xfam` | String (hex) | 8-byte mask of enabled CPU extended features.  
`tdattributes` | String (hex) | 8-byte bitmap of TD execution attributes.  
  
1 Don't use these measurements in access policies. They are affected by changes in underlying infrastructure, such as firmware updates, which can happen at any time. These measurements are provided primarily for transparency purposes. 

## Submods claims

The following table describes the `submods` claims in a Google Cloud Attestation token.

Claim | Type | Description  
---|---|---  
`gce` | Object | See Compute Engine claims.  
  
### Compute Engine claims

The following table describes the `gce` claims in a Google Cloud Attestation token.

Claim | Type | Description  
---|---|---  
`instance_id` | String | The VM instance ID.  
`instance_name` | String | The VM instance name.  
`project_id` | String |  The [ project ID](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) for the project that the VM is running in.   
`project_number` | String | The project number for the project that the VM is running in.  
`zone` | String |  The Compute Engine zone where the Confidential VM instance is running.   
  
## What's next

  * See the IETF draft for [The Entity Attestation Token (EAT)](https://datatracker.ietf.org/doc/html/draft-ietf-rats-eat-22) for more information on attestation claims.

  * See the [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) for more information on OpenID token claims.

  * For more information about tokens and retrieving them, see [vTPM Attestation Codelab](https://codelabs.developers.google.com/codelabs/vtpm-remote-attestation-on-confidential-virtual-machine).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
