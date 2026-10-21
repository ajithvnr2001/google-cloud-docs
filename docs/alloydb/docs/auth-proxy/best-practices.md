---
url: https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices/
title: Best practices for using the AlloyDB Auth Proxy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:21.165371+00:00
---

# Best practices for using the AlloyDB Auth Proxy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Best practices for using the AlloyDB Auth Proxy Stay organized with collections  Save and categorize content based on your preferences. 

To maintain secure, reliable connections to your AlloyDB for PostgreSQL instances in production and development environments, follow these best practices when you deploy and manage the AlloyDB Auth Proxy.

## Keep the Auth Proxy client up-to-date

Google releases new versions of the Auth Proxy monthly. You can find the current version by checking the [AlloyDB Auth Proxy GitHub releases page](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/releases).

Use automation to update the Auth Proxy version and test the new version in non-production environments before promoting the change to production.

## Run the Auth Proxy client as a persistent service or sidecar

In production, you should run the Auth Proxy client as a persistent service or sidecar.

If the Auth Proxy client process is stopped, then all existing connections through it are dropped, and your application cannot create any more connections to the AlloyDB instance with the AlloyDB Auth Proxy. To prevent this scenario, run the Auth Proxy client as a persistent service, so that if the Auth Proxy client exits for any reason, it is automatically restarted.

Based on where you are running the client, use the following options:

  * For Auth Proxy client running on Linux VMs, use a service such as `systemd`, `upstart`, or `supervisor`.
  * For Windows workloads, run the Auth Proxy client as a Windows Service. See [Running the Auth Proxy as a Windows Service](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#windows-service) for more information.
  * For Kubernetes setups, run the Auth Proxy client as a sidecar.



## Run the Auth Proxy client on the same machine as your workload

The Auth Proxy client assumes it runs on the same machine as the workload. Any client traffic to the Auth Proxy will be unencrypted. Traffic from the Auth Proxy to the AlloyDB is encrypted using mTLS.

Make sure any client of the Auth Proxy is located on the same machine so that no unencrypted traffic leaves the machine. The AlloyDB Auth Proxy should be co-located with a client that wants to access your AlloyDB instance.

## Use a distinct service account for each workload

The AlloyDB Auth Proxy uses the environment's Identity and Access Management (IAM) principal to create a secure tunnel to an AlloyDB instance. To follow the principle of least privilege, each workload, such as a web app or a backend data processing app, must use a distinct service account. The use of a distinct service account ensures that each workload's permissions can be managed (or revoked) separately.

## Don't deploy the AlloyDB Auth Proxy as a bottleneck

It may be tempting to deploy the AlloyDB Auth Proxy on a shared VM and use it to route all traffic from a number of workloads to your AlloyDB instance. However, this approach is insecure and creates a single point of failure.

When multiple clients end up using the same IAM principal that the Auth Proxy uses, identifying the workload that is actually accessing your AlloyDB instance becomes difficult, making this approach insecure.

This approach creates a single point of failure because if the AlloyDB Auth Proxy is overloaded with a burst of traffic, all client connections will be negatively affected.

Instead, deploy an Auth Proxy client on each machine that needs a secure connection either as a sidecar or persistent service.

## Reduce AlloyDB Auth Proxy log output for production deployments

If you need to limit the size of the AlloyDB Auth Proxy logs, then set the `--verbose=false` option when you start the AlloyDB Auth Proxy. Note that using this option reduces the effectiveness of the AlloyDB Auth Proxy output in diagnosing connection issues.

## Read the AlloyDB Auth Proxy help message

The AlloyDB Auth Proxy includes many additional features and includes an extensive help message with details. Run the `alloydb-auth-proxy --help` command to discover additional configuration options.

## Engage with the development team on GitHub

If you believe you have found a bug or have a feature request, then you may engage with the development team on the [AlloyDB Auth Proxy GitHub repository](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
