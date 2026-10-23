---
url: https://docs.cloud.google.com/rust/docs/post-quantum-cryptography/
title: Post-quantum cryptography (PQC) support \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:24.118411+00:00
---

# Post-quantum cryptography (PQC) support  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/post-quantum-cryptography/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Post-quantum cryptography (PQC) support Stay organized with collections  Save and categorize content based on your preferences. 

To protect against the "Store Now, Decrypt Later" threat, Google Cloud is implementing Post-Quantum Cryptography (PQC) across its services. For more information on Google Cloud's approach, see [Post-Quantum Cryptography on Google Cloud](https://cloud.google.com/security/resources/post-quantum-cryptography).

## Post-quantum key exchange

To support post-quantum key exchange, the Google Cloud client libraries use a hybrid key exchange mechanism combining ML-KEM-768 with classical X25519 for TLS 1.3 connections.

### Rust SDK support

No additional configuration or code changes are required when using standard client library releases (released on or after January 28, 2026). The underlying TLS engine (`rustls` with the default `aws-lc-rs` provider) automatically negotiates post-quantum key exchange when connecting to supported Google Cloud services.

If you override the cryptography provider (for example, by configuring `rustls` to use `ring`), post-quantum key exchange will be disabled unless your chosen provider explicitly supports it. For more information, see [Switch the default crypto provider](https://docs.cloud.google.com/rust/docs/switch-rustls-crypto-provider).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
