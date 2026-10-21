---
url: https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem/
title: Binary Authorization for on-premises clusters overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:10.941240+00:00
---

# Binary Authorization for on-premises clusters overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Binary Authorization for on-premises clusters overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes Binary Authorization for [on-premises clusters](https://docs.cloud.google.com/anthos/clusters/doc) that are created as part of Google Distributed Cloud. To configure Binary Authorization for your clusters, see the following:

  * [Set up Binary Authorization policy enforcement on VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy) (version 1.28 or later)
  * [Set up Binary Authorization policy enforcement on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/binary-authorization-policy) (version 1.16 or later)
  * [Legacy manual setup for on-premises clusters](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem) (deprecated)



Binary Authorization for on-premises clusters is a Google Cloud product that extends [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)'s hosted, deploy-time enforcement to Google Distributed Cloud.

## Architecture

Binary Authorization for on-premises clusters connects clusters to the Binary Authorization enforcer, running on Google Cloud. It works by relaying requests to run container images from on-premises clusters to the Binary Authorization enforcement API.

[ ![Binary Authorization for Distributed Cloud showing
              a configuration with one user control plane deployed.](https://docs.cloud.google.com/static/binary-authorization/docs/images/binauthz-for-gke-on-prem.svg)](https://docs.cloud.google.com/static/binary-authorization/docs/images/binauthz-for-gke-on-prem.svg) Binary Authorization for Distributed Cloud architecture with one user control plane. (Click to enlarge)

Binary Authorization installs the Binary Authorization Module, which runs as a Kubernetes [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) in your cluster.

When the Kubernetes API server for the cluster processes a request to run a Pod, it sends an admission request, through the control plane, to the Binary Authorization Module.

The module then forwards the admission request to the hosted Binary Authorization API.

On Google Cloud, the API receives the request and forwards it to the Binary Authorization enforcer. The enforcer then checks that the request satisfies the Binary Authorization policy. If it does, the Binary Authorization API returns an "allow" response. Otherwise the API returns a "reject" response.

On premises, the Binary Authorization Module receives the response. If the Binary Authorization Module and all of the other admission webhooks allow the deploy request, the container image is allowed to deploy.

For more information about validating admission webhooks, see [Using Admission Controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).

## Webhook failure policy

When a failure prevents communication with Binary Authorization, a webhook-specific failure policy determines if the container is allowed to deploy. Configuring the failure policy to allow the container image to deploy is known as _fail open_. Configuring the failure policy to deny the container image from deploying is known as _fail close_.

**Note:** By default, the Binary Authorization Module is configured to fail open.

To configure the Binary Authorization Module for fail close, modify the `manifest.yaml` file and change the `failurePolicy` from `Ignore` to `Fail`, then deploy the manifest file.

You can [update the failure policy](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem#update-failure-policy) in the Binary Authorization Module.

## What's next

  * To configure Binary Authorization on VMware, see [Set up Binary Authorization policy enforcement on VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy).
  * To configure Binary Authorization on bare metal, see [Set up Binary Authorization policy enforcement on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/binary-authorization-policy).
  * For legacy manual installations, see [Set up for on-premises clusters (deprecated)](https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem).
  * To learn more about Google Distributed Cloud, see the [Google Distributed Cloud overview](https://docs.cloud.google.com/distributed-cloud/docs).
  * To learn more about Binary Authorization, see [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
