---
url: https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound/
title: Looker (Google Cloud core) outbound access to external services using Private Service Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:53.479920+00:00
---

# Looker (Google Cloud core) outbound access to external services using Private Service Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) outbound access to external services using Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

You can set up secure outbound connections (also known as [southbound traffic](https://docs.cloud.google.com/looker/docs/glossary#outbound-traffic)) from Looker (Google Cloud core) to external services by using Private Service Connect. The following Codelabs guide you through configuring these connections so that your Looker (Google Cloud core) instance can securely interact with external resources while maintaining private network connectivity.

Any self-hosted or on-premise repository or service that Looker (Google Cloud core) connects to through southbound access must be configured with a publicly trusted SSL certificate.

**Note:** In a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) environment, you must configure a [Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/overview) for the proxy load balancer to allow outbound connectivity to custom external services, such as SMTP.

  * [Codelab: Looker (Google Cloud core) PSC Southbound HTTPS Internet NEG SMTP](https://codelabs.developers.google.com/looker-psc-internet-neg-smtp)

In this codelab, you will create a southbound connection to Looker (Google Cloud core)'s SMTP service using an internal TCP proxy load balancer and internet network endpoint group (NEG) with the FQDN `notifications-pa.googleapis.com` invoked from a Looker (Google Cloud core) PSC as a Service Consumer.

  * [Codelab: Looker (Google Cloud core) PSC Southbound access to Cloud SQL PSC](https://codelabs.developers.google.com/looker-psc-cloudsql)

In this codelab, you will perform a southbound connection to Cloud SQL deployed with Private Service Connect as a Service Producer.

  * [Codelab: Looker (Google Cloud core) PSC Southbound SSH Internet NEG](https://codelabs.developers.google.com/looker-psc-internet-neg-ssh)

In this codelab, you will perform a southbound SSH connection to GitHub using an internal TCP proxy load balancer and internet network endpoint group (NEG) invoked from Looker (Google Cloud core) PSC as a Service Consumer.

  * [Codelab: Looker (Google Cloud core) PSC Southbound HTTPS Internet NEG](https://codelabs.developers.google.com/looker-psc-internet-neg-https)

In this codelab, you will perform a southbound HTTPS connection to GitHub using an internal TCP proxy load balancer and internet network endpoint group (NEG) invoked from a Looker (Google Cloud core) PSC as a Service Consumer.

  * [Codelab: Looker (Google Cloud core) PSC Southbound Hybrid NEG to on-premises](https://codelabs.developers.google.com/looker-psc-hybrid-neg-onprem)

In this codelab, you will perform a southbound connection to an on-premises Postgres database over H-VPN using an internal TCP proxy load balancer and hybrid network endpoint group (NEG) invoked from a Looker (Google Cloud core) PSC as a Service Consumer.

  * [Codelab: Looker (Google Cloud core) PSC Southbound HTTPS Internet NEG GitLab Self-Managed](https://codelabs.developers.google.com/looker-psc-internet-neg-https-gitlab-on-prem)

In this codelab, you will perform a southbound HTTPS connection to your GitLab self-managed environment by using an internal TCP proxy load balancer and internet network endpoint group (NEG) that is invoked from Looker (Google Cloud core) Private Service Connect as a service consumer.




## Troubleshooting

For information about troubleshooting southbound connections, see the [Troubleshooting southbound connections](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-psc-southbound-troubleshooting) documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
