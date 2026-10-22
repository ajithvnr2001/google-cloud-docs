---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/shared-responsibility-model/
title: Shared responsibility model \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:14.775529+00:00
---

# Shared responsibility model  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/shared-responsibility-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Shared responsibility model Stay organized with collections  Save and categorize content based on your preferences. 

Google and your Google Distributed Cloud (GDC) air-gapped operator distribute services through the Distributed Cloud Marketplace for your benefit. The responsibility model for Marketplace services is different from other services on the Distributed Cloud platform.

### Google and Distributed Cloud operator responsibilities

Google ensures that Marketplace services go through the same rigorous security scans as the rest of Distributed Cloud. When vulnerabilities are detected in a Marketplace service, Google works with the relevant vendor to fix the vulnerabilities. Depending on your contract, your Distributed Cloudoperator might implement additional processes and security measures on Marketplace services. Google ensures that Marketplace services are compatible with Distributed Cloud, and can be deployed in a recommended way. Google ensures that once a software vendor makes a new version of their software available, that new version is included in the Distributed Cloud Marketplace in a timely manner.

### Vendor responsibilities

The software vendor documents how you can comply with specific policy regimes with their product. For example, this can take the form of a technical implementation guide that targets a specific compliance regime.

It is the responsibility of the software vendor to patch vulnerabilities in their own product, and to provide Google with the patched version so that we can distribute it in the Distributed Cloud Marketplace.

If included in your contract with a software vendor, it is their responsibility to provide you support. Google and your Distributed Cloud operator support the Distributed Cloud Marketplace systems, but not the Marketplace services themselves, unless provided by Google directly.

### User responsibility

It is essential that the user is aware of the compliance regime to which they are subject, and that they consult the documentation that the software vendor provides related to their compliance regime, if available.

The user is obligated to configure the Marketplace service in accordance with their own policies and the compliance regimes to which they are subject.

It is the responsibility of the user to obtain licenses from the relevant software vendor for any Marketplace service that requires licenses.

Once installed and running, Marketplace services are considered user workloads. They run in the user environment and are their responsibility. Google provides features to install, update, and uninstall Marketplace services, but it is the user responsibility to use the features. Unless specified in the contract with Distributed Cloud operator, they don't actively monitor user workloads and don't fix issues that arise.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
