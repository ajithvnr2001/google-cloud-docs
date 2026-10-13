---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/
title: Cloud Key Management Service (KMS) API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:13.367669+00:00
---

# Cloud Key Management Service (KMS) API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Cloud Key Management Service (KMS) API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/kms.svg)](https://www.npmjs.org/package/@google-cloud/kms)

Cloud Key Management Service (KMS) API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/CHANGELOG.md).

  * [Cloud Key Management Service (KMS) API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/kms/latest)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Cloud Key Management Service (KMS) API API](https://console.cloud.google.com/flows/enableapi?apiid=cloudkms.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/kms
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
create key handle | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey.create_key_handle.js)  
get key handle | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey.get_key_handle.js)  
list key handles | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey.list_key_handles.js)  
get autokey config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey_admin.get_autokey_config.js)  
show effective autokey config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey_admin.show_effective_autokey_config.js)  
update autokey config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/autokey_admin.update_autokey_config.js)  
create ekm connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.create_ekm_connection.js)  
get ekm config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.get_ekm_config.js)  
get ekm connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.get_ekm_connection.js)  
list ekm connections | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.list_ekm_connections.js)  
update ekm config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.update_ekm_config.js)  
update ekm connection | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.update_ekm_connection.js)  
verify connectivity | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/ekm_service.verify_connectivity.js)  
approve single tenant hsm instance proposal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.approve_single_tenant_hsm_instance_proposal.js)  
create single tenant hsm instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.create_single_tenant_hsm_instance.js)  
create single tenant hsm instance proposal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.create_single_tenant_hsm_instance_proposal.js)  
delete single tenant hsm instance proposal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.delete_single_tenant_hsm_instance_proposal.js)  
execute single tenant hsm instance proposal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.execute_single_tenant_hsm_instance_proposal.js)  
get single tenant hsm instance | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.get_single_tenant_hsm_instance.js)  
get single tenant hsm instance proposal | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.get_single_tenant_hsm_instance_proposal.js)  
list single tenant hsm instance proposals | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.list_single_tenant_hsm_instance_proposals.js)  
list single tenant hsm instances | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/hsm_management.list_single_tenant_hsm_instances.js)  
asymmetric decrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.asymmetric_decrypt.js)  
asymmetric sign | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.asymmetric_sign.js)  
create crypto key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.create_crypto_key.js)  
create crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.create_crypto_key_version.js)  
create import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.create_import_job.js)  
create key ring | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.create_key_ring.js)  
decapsulate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.decapsulate.js)  
decrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.decrypt.js)  
delete crypto key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.delete_crypto_key.js)  
delete crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.delete_crypto_key_version.js)  
destroy crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.destroy_crypto_key_version.js)  
encrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.encrypt.js)  
generate random bytes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.generate_random_bytes.js)  
get crypto key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_crypto_key.js)  
get crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_crypto_key_version.js)  
get import job | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_import_job.js)  
get key ring | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_key_ring.js)  
get public key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_public_key.js)  
get retired resource | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.get_retired_resource.js)  
import crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.import_crypto_key_version.js)  
list crypto key versions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.list_crypto_key_versions.js)  
list crypto keys | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.list_crypto_keys.js)  
list import jobs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.list_import_jobs.js)  
list key rings | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.list_key_rings.js)  
list retired resources | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.list_retired_resources.js)  
mac sign | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.mac_sign.js)  
mac verify | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.mac_verify.js)  
raw decrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.raw_decrypt.js)  
raw encrypt | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.raw_encrypt.js)  
restore crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.restore_crypto_key_version.js)  
update crypto key | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.update_crypto_key.js)  
update crypto key primary version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.update_crypto_key_primary_version.js)  
update crypto key version | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-kms/samples/generated/v1/key_management_service.update_crypto_key_version.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/kms@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
