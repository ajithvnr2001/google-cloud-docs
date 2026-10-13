---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/
title: Certificate Authority API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:13.510359+00:00
---

# Certificate Authority API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-private-ca/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Certificate Authority API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  5.2.0  4.4.0  4.3.0  4.2.0  4.1.2  3.1.0  3.0.0  2.5.0  2.4.1  2.3.7 

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority

[![npm version](https://img.shields.io/npm/v/@google-cloud/security-private-ca.svg)](https://www.npmjs.org/package/@google-cloud/security-private-ca)

Certificate Authority API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/CHANGELOG.md).

  * [Certificate Authority API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/privateca/latest)



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
  3. [Enable the Certificate Authority API API](https://console.cloud.google.com/flows/enableapi?apiid=privateca.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/security-private-ca
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
activate certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.activate_certificate_authority.js)  
create ca pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.create_ca_pool.js)  
create certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.create_certificate.js)  
create certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.create_certificate_authority.js)  
create certificate template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.create_certificate_template.js)  
delete ca pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.delete_ca_pool.js)  
delete certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.delete_certificate_authority.js)  
delete certificate template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.delete_certificate_template.js)  
disable certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.disable_certificate_authority.js)  
enable certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.enable_certificate_authority.js)  
fetch ca certs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.fetch_ca_certs.js)  
fetch certificate authority csr | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.fetch_certificate_authority_csr.js)  
get ca pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.get_ca_pool.js)  
get certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.get_certificate.js)  
get certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.get_certificate_authority.js)  
get certificate revocation list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.get_certificate_revocation_list.js)  
get certificate template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.get_certificate_template.js)  
list ca pools | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.list_ca_pools.js)  
list certificate authorities | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.list_certificate_authorities.js)  
list certificate revocation lists | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.list_certificate_revocation_lists.js)  
list certificate templates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.list_certificate_templates.js)  
list certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.list_certificates.js)  
revoke certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.revoke_certificate.js)  
undelete certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.undelete_certificate_authority.js)  
update ca pool | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.update_ca_pool.js)  
update certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.update_certificate.js)  
update certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.update_certificate_authority.js)  
update certificate revocation list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.update_certificate_revocation_list.js)  
update certificate template | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1/certificate_authority_service.update_certificate_template.js)  
activate certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.activate_certificate_authority.js)  
create certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.create_certificate.js)  
create certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.create_certificate_authority.js)  
disable certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.disable_certificate_authority.js)  
enable certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.enable_certificate_authority.js)  
fetch certificate authority csr | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.fetch_certificate_authority_csr.js)  
get certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.get_certificate.js)  
get certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.get_certificate_authority.js)  
get certificate revocation list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.get_certificate_revocation_list.js)  
get reusable config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.get_reusable_config.js)  
list certificate authorities | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.list_certificate_authorities.js)  
list certificate revocation lists | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.list_certificate_revocation_lists.js)  
list certificates | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.list_certificates.js)  
list reusable configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.list_reusable_configs.js)  
restore certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.restore_certificate_authority.js)  
revoke certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.revoke_certificate.js)  
schedule delete certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.schedule_delete_certificate_authority.js)  
update certificate | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.update_certificate.js)  
update certificate authority | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.update_certificate_authority.js)  
update certificate revocation list | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-security-privateca/samples/generated/v1beta1/certificate_authority_service.update_certificate_revocation_list.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/security-private-ca@legacy-8` installs client libraries for versions compatible with Node.js 8.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
