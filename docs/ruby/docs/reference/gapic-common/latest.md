---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/
title: Google API Extensions for Ruby \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:23.563064+00:00
---

# Google API Extensions for Ruby  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google API Extensions for Ruby Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Generated API Client common code (gapic-common) is a set of modules which aids the development of APIs for clients and servers based on [gRPC](http://grpc.io) and Google API conventions.

Application code will rarely need to use most of the classes within this library directly, but code generated automatically from the API definition files in [Google APIs](https://github.com/googleapis/googleapis/) can use services such as page streaming to provide a more convenient and idiomatic API surface to callers.

## Supported Ruby Versions

This library is supported on Ruby 3.2+.

Google provides official support for Ruby versions that are actively supported by Ruby Core—that is, Ruby versions that are either in normal maintenance or in security maintenance, and not end of life. Older versions of Ruby _may_ still work, but are unsupported and not recommended. See <https://www.ruby-lang.org/en/downloads/branches/> for details about the Ruby support schedule.

## Post-Quantum Key Exchange

Clients built on this library negotiate the hybrid post-quantum key exchange group `X25519MLKEM768` — classical X25519 paired with ML-KEM-768 ([NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final)) — over TLS 1.3. No application code changes are required, because the handshake belongs to the transport layer. The two transports source that support differently:

Transport | Cryptographic provider | Requirement | Enforced by this gem?  
---|---|---|---  
gRPC | BoringSSL, vendored inside the `grpc` gem | `grpc >= 1.83` | Yes  
REST | Host system OpenSSL, via `Net::HTTP` and Faraday | OpenSSL `>= 3.5` | No  
  
gRPC clients get post-quantum key exchange automatically: `gapic-common` depends on `grpc >= 1.83`, the first release to offer `X25519MLKEM768` in the TLS ClientHello by default.

The REST requirement cannot be expressed as a gem dependency. Ruby's `openssl` is a default gem bound to whatever `libssl` the host provides, and ML-KEM first ships in OpenSSL 3.5. On an older host, REST connections negotiate classical X25519 instead — a safe fallback rather than an error, but not post-quantum. To check the OpenSSL your Ruby is linked against:
    
    
    ruby -ropenssl -e 'puts OpenSSL::OPENSSL_LIBRARY_VERSION'
    

## Contributing

Contributions to this library are always welcome and highly encouraged.

See the [CONTRIBUTING](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/CONTRIBUTING "CONTRIBUTING") documentation for more information on how to get started.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be stable and will not have backwards-incompatible changes introduced in subsequent minor releases.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
