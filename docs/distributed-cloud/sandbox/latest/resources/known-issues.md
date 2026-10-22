---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/known-issues/
title: Known issues \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:17.928355+00:00
---

# Known issues  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)
  * [ Resources ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/resources/release-notes)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

Environment scope and capabilities of Google Distributed Cloud (GDC) Sandbox:

  * **Persistence** : GDC Sandbox is non-persistent and is refreshed incrementally on a monthly basis. When environments are refreshed, they're returned to a default state, meaning you'll need to redeploy your configurations. It's recommended to save your configs, code, and containers in a code repository which also enables your low-high development into production environments.
  * **Resources** : This release limits the amount of the following resources: 
    * One organization.
    * One tenant.
    * Two Kubernetes clusters.
  * **Users** : To ensure adequate usage of shared resources, users are limited to a maximum of 25.
  * **Sensitive Data** : Users must consent to EULA prior to accessing GDC Sandbox. We recommend you not use GDC Sandbox for sensitive data or production workloads as it's intended for test, development, and training purposes.
  * **IO experience** : GDC Sandbox only supports the Application Operator (AO) or end-user [Persona](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/overview#personas) experience of GDC Sandbox.



## Known issues:

  1. Project Network Policy state is always reflected as `Not Read` on the UI irrespective of its status. Use the API or CLI to check for the true status.
  2. If the steps mentioned in [Access the environment](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect#access-environment) to install certificates haven't been followed yet, the following error will be seen while uploading a file to a bucket (object storage): `Check network speed to ensure your file size is within limits and certificates are properly set`. You can either install the certificates or follow this workaround:

     1. On the browser in your GDC Sandbox, open the web page `https://objectstorage.org-1.zone1.google.gdch.test` and accept the certificate.
     2. Try the file upload again.
     3. If you still encounter issues like `ErrPresignSignatureNotRecognized`, try disabling TLS verification using `gdcloud config set storage/s3_insecure_skip_tls_verify true`.
  3. Login timeout: The authentication might time out on both UI and CLI if the environment is not accessed for a few minutes.

     1. For UI timeout: Clear browser cache and refresh the browser.
     2. For gdcloud timeout: Sign in again. See [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect).
  4. The only supported storage class for [creating PersistentVolumeClaim objects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/application/ao-user/containers/create-stateful-workloads#request-storage-in-statefulset) is `standard-rwo: ReadWriteOnce`. The `standard-rwx: ReadWriteMany` storage class is not supported.

  5. After you set `auth/login_config_cert_path` using `gdcloud config set`, the value is unset after running a `gdcloud auth login`. The workaround for this issue is to always add `--login-config-cert=/tmp/org-1-web-tls-ca.cert` while running `gdcloud auth login`.

  6. Unable to launch Chrome after login into RDP. Try the following workaround:

     1. Remove `~/.local/share/keyrings`
     2. Launch Chrome with the command:
    
    /opt/google/chrome/google-chrome --password-store=basic
    

  7. If the Organization IAM Admin role is removed from the `fop-platform-admin@example.com` user, the role cannot be re-assigned and the user will lose access to most features. Contact GDC Sandbox support in this case.

  8. The web browser fails to open on the gateway instance. Likely cause: the gateway has run out of disk space. In most cases, the space is overloaded with dangling containers, volumes and images. Try the following fix to clean up some space:
         
         docker images prune -a
         docker volumes prune
         docker containers prune
         

  9. Attempts to connect to the Virtual Machine (VM) using `gcloud compute ssh` will fail. Instead, use `sshuttle` as described in [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/virtual-machine#connect_to_a_vm).

  10. If the [service account authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/service-identity#authorize-sa-key) fails with `dial tcp: lookup service-accounts.org-1.google.gdch.test on with no such host`, change the `token_uri` to `https://service-accounts.org-1.zone1.google.gdch.test/authenticate` in the KEY_FILE having application default credentials.

  11. The GPU hosts maintain architectural isolation from the rest of the ecosystem. Data plane services (such as DBS and Object Storage) and general-purpose VMs are explicitly excluded from accessing the resources where the GPU workloads run.

  12. Sandbox audit logs are only temporarily available each time after provisioning or refreshing the sandbox. Officially, audit logging in the sandbox is an unsupported use case because it is a PA / IO persona feature, and the sandbox's goal is to help test the AO persona.

     1. To work around this issue, refresh or reprovision the sandbox environment to temporarily restore access to audit logs, or perform a rollout restart of the StatefulSet:
            
            kubectl rollout restart statefulset -n obs-system audit-logs-loki-io
            




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
