---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/
title: gcloud alpha container binauthz \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:40.847270+00:00
---

# gcloud alpha container binauthz  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container binauthz Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container binauthz - manage attestations for Binary Authorization on Google Cloud Platform 
SYNOPSIS
    

`gcloud alpha container binauthz` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Binary Authorization is a feature which allows binaries to run on Google Cloud Platform only if they are appropriately attested. Binary Authorization is configured by creating a policy. 
EXAMPLES
     This example assumes that you have created a keypair using gpg, usually by running `gpg --gen-key …`, with `Name-Email` set to `attesting_user@example.com` for your attestor. 

First, some convenience variables for brevity: 
    
    
    ATTESTING_USER="attesting_user@example.com"
    DIGEST="000000000000000000000000000000000000000000000000000000000000abcd"
    ARTIFACT_URL="gcr.io/example-project/example-image@sha256:${DIGEST}"
    ATTESTOR_NAME="projects/example-project/attestors/canary"

Export your key's fingerprint (note this may differ based on version and implementations of gpg): 
    
    
    gpg \
        --with-colons \
        --with-fingerprint \
        --force-v4-certs \
        --list-keys \
        "${ATTESTING_USER}" | grep fpr | cut --delimiter=':' --fields 10

This should produce a 40 character, hexidecimal encoded string. See <https://tools.ietf.org/html/rfc4880#section-12.2> for more information on key fingerprints. 

Create your attestation payload: 
    
    
    gcloud alpha container binauthz create-signature-payload \
        --artifact-url="${ARTIFACT_URL}" \
      > example_payload.txt

Create a signature from your attestation payload: 
    
    
    gpg \
      --local-user "${ATTESTING_USER}" \
      --armor \
      --clearsign \
      --output example_signature.pgp \
      example_payload.txt

Upload the attestation: 
    
    
    gcloud alpha container binauthz attestations create \
      --public-key-id=${KEY_FINGERPRINT} \
      --signature-file=example_signature.pgp \
      --artifact-url="${ARTIFACT_URL}" \
      --attestor=${ATTESTOR_NAME}

List the attestation by artifact URL. `--format` can be passed to output the attestations as json or another supported format: 
    
    
    gcloud alpha container binauthz attestations list \
      --artifact-url="${ARTIFACT_URL}" \
      --format=yaml
    
      ---
      - |
        -----BEGIN PGP PUBLIC KEY BLOCK-----
        Version: GnuPG v1
        … SNIP …
        -----END PGP PUBLIC KEY BLOCK-----
      - |
        -----BEGIN PGP SIGNED MESSAGE-----
        Hash: SHA1
        … SNIP …
        -----BEGIN PGP SIGNATURE-----
        Version: GnuPG v1
        … SNIP …
        -----END PGP SIGNATURE-----

List all artifact URLs on the project for which Container Analysis Occurrences exist. This list includes the list of all URLs with BinAuthz attestations: 
    
    
    gcloud alpha container binauthz attestations list
    
      ---
      <https://gcr.io/example-project/example-image@sha256:000000000000000000000000000000000000000000000000000000000000abcd>
      …

Listing also works for kind=ATTESTATION_AUTHORITY attestations, just pass the attestor: 
    
    
    gcloud alpha container binauthz attestations list \
      --artifact-url="${ARTIFACT_URL}" \
      --attestor=${ATTESTOR_NAME} \
      --format=yaml
    
      …

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[attestations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestations)`
     `(ALPHA)` Create and manage Google Binary Authorization attestations. 
`[attestors](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/attestors)`
     `(ALPHA)` Create and manage Google Binary Authorization Attestors. 
`[policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/policy)`
     `(ALPHA)` Create and manage Google Binary Authorization policies. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create-signature-payload](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/create-signature-payload)`
     `(ALPHA)` Create a JSON container image signature object. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container binauthz](https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz)
    
    
    [gcloud beta container binauthz](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
