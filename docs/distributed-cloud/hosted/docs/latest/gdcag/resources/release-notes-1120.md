---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1120/
title: Google Distributed Cloud air-gapped release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:26.561809+00:00
---

# Google Distributed Cloud air-gapped release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-1120/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped release notes Stay organized with collections  Save and categorize content based on your preferences. 

## February 16, 2024 [GDC 1.12.0]

* * *

Announcement

  * Google Distributed Cloud air-gapped 1.12.0 is now available.  
See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped. 
  * Google Distributed Cloud air-gapped 1.12.0 supports two operating systems: 
    * Ubuntu 20231205
    * Rocky Linux 20231208



* * *

Security

Updated Canonical Ubuntu OS image version to 20231208 to apply the latest security patches and important updates. To take advantage of the bug and security vulnerability fixes, you must upgrade all nodes with each release. The following security vulnerabilities are fixed: 

  * [CVE-2022-40090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40090)
  * [CVE-2023-23583](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23583)
  * [CVE-2023-31085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31085)
  * [CVE-2023-3576](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3576)
  * [CVE-2023-37920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-37920)
  * [CVE-2023-38469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38469)
  * [CVE-2023-38470](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38470)
  * [CVE-2023-38471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38471)
  * [CVE-2023-38472](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38472)
  * [CVE-2023-38473](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38473)
  * [CVE-2023-40217](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-40217)
  * [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)
  * [CVE-2023-45871](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45871)
  * [CVE-2023-47038](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-47038)
  * [CVE-2023-5981](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5981)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2020-24736](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24736)
  * [CVE-2020-29509](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29509)
  * [CVE-2020-29511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29511)
  * [CVE-2020-29652](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-29652)
  * [CVE-2021-29923](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29923)
  * [CVE-2021-31525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31525)
  * [CVE-2021-33195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33195)
  * [CVE-2021-33196](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33196)
  * [CVE-2021-33197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33197)
  * [CVE-2021-33198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-33198)
  * [CVE-2021-34558](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34558)
  * [CVE-2021-36221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36221)
  * [CVE-2021-38297](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38297)
  * [CVE-2021-38561](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-38561)
  * [CVE-2021-39293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39293)
  * [CVE-2021-41771](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41771)
  * [CVE-2021-41772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-41772)
  * [CVE-2021-43565](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43565)
  * [CVE-2021-44716](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44716)
  * [CVE-2022-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1705)
  * [CVE-2022-1962](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1962)
  * [CVE-2022-2879](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2879)
  * [CVE-2022-2880](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2880)
  * [CVE-2022-3063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3063)
  * [CVE-2022-21235](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21235)
  * [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698)
  * [CVE-2022-23471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23471)
  * [CVE-2022-23524](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23524)
  * [CVE-2022-23525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23525)
  * [CVE-2022-23526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23526)
  * [CVE-2022-23648](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23648)
  * [CVE-2022-23772](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23772)
  * [CVE-2022-23773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23773)
  * [CVE-2022-23806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23806)
  * [CVE-2022-24675](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24675)
  * [CVE-2022-24921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24921)
  * [CVE-2022-27191](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27191)
  * [CVE-2022-27664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27664)
  * [CVE-2022-28131](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28131)
  * [CVE-2022-28327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-28327)
  * [CVE-2022-29526](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29526)
  * [CVE-2022-30580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30580)
  * [CVE-2022-30630](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30630)
  * [CVE-2022-30631](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30631)
  * [CVE-2022-30632](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30632)
  * [CVE-2022-30633](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30633)
  * [CVE-2022-30635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30635)
  * [CVE-2022-31030](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31030)
  * [CVE-2022-32148](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32148)
  * [CVE-2022-32149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32149)
  * [CVE-2022-32189](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32189)
  * [CVE-2022-41715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41715)
  * [CVE-2022-41717](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41717)
  * [CVE-2022-41721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)
  * [CVE-2022-41723](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41723)
  * [CVE-2022-41724](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41724)
  * [CVE-2022-41725](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41725)
  * [CVE-2022-41912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41912)
  * [CVE-2022-48174](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-48174)
  * [CVE-2023-1667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1667)
  * [CVE-2023-2253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2253)
  * [CVE-2023-2283](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2283)
  * [CVE-2023-2603](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2603)
  * [CVE-2023-2975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-2975)
  * [CVE-2023-3446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3446)
  * [CVE-2023-3817](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3817)
  * [CVE-2023-3978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3978)
  * [CVE-2023-22036](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22036)
  * [CVE-2023-22041](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22041)
  * [CVE-2023-22049](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22049)
  * [CVE-2023-24532](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24532)
  * [CVE-2023-24534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24534)
  * [CVE-2023-24536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24536)
  * [CVE-2023-24537](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24537)
  * [CVE-2023-24538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24538)
  * [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24539)
  * [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24540)
  * [CVE-2023-25153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25153)
  * [CVE-2023-25165](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25165)
  * [CVE-2023-25173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25173)
  * [CVE-2023-25193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25193)
  * [CVE-2023-26604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-26604)
  * [CVE-2023-27533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27533)
  * [CVE-2023-27535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27535)
  * [CVE-2023-27536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27536)
  * [CVE-2023-27538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27538)
  * [CVE-2023-28321](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28321)
  * [CVE-2023-28484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28484)
  * [CVE-2023-28840](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28840)
  * [CVE-2023-28841](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28841)
  * [CVE-2023-28842](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-28842)
  * [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29400)
  * [CVE-2023-29402](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29402)
  * [CVE-2023-29403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29403)
  * [CVE-2023-29404](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29404)
  * [CVE-2023-29405](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29405)
  * [CVE-2023-29406](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29406)
  * [CVE-2023-29409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29409)
  * [CVE-2023-29469](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29469)
  * [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491)
  * [CVE-2023-36054](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36054)
  * [CVE-2023-39318](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39318)
  * [CVE-2023-39319](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39319)
  * [CVE-2023-39323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39323)
  * [CVE-2023-39325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39325)
  * [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)
  * [CVE-2023-39417](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39417)
  * [CVE-2023-39533](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39533)
  * [CVE-2023-45142](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45142)
  * [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)
  * [CVE-2023-45287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45287)
  * [CVE-2023-48795](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-48795)
  * [CVE-2023-49568](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49568)
  * [CVE-2023-49569](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-49569)
  * [CVE-2023-51385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51385)



* * *

Security

Updated the `gcr.io/distroless/base` base image to digest `sha256:eda29d6da91216123f1c1841b7c7a7abe1eece155cfe8d20d2a29e5daf9ad497` to apply the latest security patches and important updates.

* * *

Change

**Add-on Manager** : 

  * The Google Distributed Cloud version is updated to 1.28.0-gke.435 to apply the latest security patches and important updates. 

See [Google Distributed Cloud 1.28.0-gke.435 release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver-1#release_1280-gke435) for details.




**Build and package** : 

  * The Golang version is upgraded to 1.20.



  * Google Distributed Cloud air-gapped 1.12.0 adds additional Software Bills Of Materials (SBOMs) to output and updates logic to ensure such SBOMs are published in the future.



  * Google Distributed Cloud air-gapped 1.12.0 adds `gdch_notice_license_files` tar files to upload manifests.




**Inventory management** :

  * Google Distributed Cloud air-gapped 1.12.0 adds validations for hardware version 3.0 connection listings.
  * Google Distributed Cloud air-gapped 1.12.0 updates console server management port pattern to allow LAN1A and LAN2A.
  * Google Distributed Cloud air-gapped 1.12.0 adds a message to mitigate the confusion of PA850 active and passive modes.
  * Google Distributed Cloud air-gapped 1.12.0 supports a breakout cassette in validation.
  * Google Distributed Cloud air-gapped 1.12.0 adds validation of the permanent firewall to management firewall connection.
  * Google Distributed Cloud air-gapped 1.12.0 adds an OI Classless Inter-Domain Routing (CIDR) prompt to the Customer Intake Questionnaire generator.
  * Google Distributed Cloud air-gapped 1.12.0 improves an error message on mac address missing failure to mitigate preflight check instability when validating hsm and mgmtsw connection.



**Operations Center IT organization** : 

  * The Operations Center IT organization has the following name updates:

    * Operations Center (OC) has been renamed to Operations Suite Facility (OIF).

    * OC Core has been renamed to Operations Suite Infrastructure Core Rack (OIR).

    * Operations Center IT (OCIT) has been renamed to Operations Suite Infrastructure (OI).

    * OCIT has been renamed to OI.

For more information, see [Terminology](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/operations-center-setup-30/setup-intro#terms).

  * Google Distributed Cloud air-gapped 1.12.0 updates the Userlock configuration script to permit the use of a failover server.

  * Google Distributed Cloud air-gapped 1.12.0 pre-creates additional Operations Suite Infrastructure (OI) security groups to allow fine-grained access across OI systems.




**System artifact registry** :

  * Google Distributed Cloud air-gapped 1.12.0 removes `-f` (`--force`) short flag from CLI assets.



**Version update** :

  * The Debian-based image version is updated to bookworm-v1.0.0-gke.3.




* * *

Feature

**Certificate manager** : 

  * Introduced configuration of the key size in a web-tls certificate for organizations.



**Database Service** : 

  * Support for point-in-time recovery (PITR) for its Oracle databases.
  * Support for Postgres advanced migration to migrate on-premises databases to databases managed by the GDC database service. 



**Logging** : 

  * Added the [Log Query gRPC API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-logs#query-logs-from-api) to programmatically query operational and audit logs from the API endpoints.
  * Included the capability to [export PA logs to an external SIEM system](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/export-logs-external).



**Marketplace** : 

  * MongoDB Enterprise Advanced (BYOL) is now available on the Google Distributed Cloud air-gapped 1.12.0 Marketplace.  
It is a collection of products and services that drive security, efficiency, and put you in control of your MongoDB databases. 



**Object storage** : 

  * Added new image required to host upgrade files in the object storage software.
  * Added an encryption version label to bucket webhooks. 
  * Added a reconciler for object credential rotation. 



**Operations Suite Infrastructure Core Services (OIC)**

  * Google Distributed Cloud air-gapped 1.12.0 collects OIC logs in Grafana.
  * Google Distributed Cloud air-gapped 1.12.0 moves the `Copy-BareMetalFiles.ps1` script from installation documentation to scripts in `private-cloud/operations/dsc/`.

**Platform security**

  * A web TLS certificate for a root admin cluster is issued by the Google Distributed Cloud air-gapped internal public key infrastructure.



**Security compliance** : 

  * Google Distributed Cloud air-gapped 1.12.0 introduces port security required to pass a security assessment.



**Ticketing system**

  * Updated scheduled jobs in ServiceNow to stagger when they are run to prevent database spikes.
  * Infrastructure Operator receives an alert when a meta monitoring incident in ServiceNow is stale.



**Upgrade**

  * Added the **Upgrade Status** dashboard for Infrastructure Operators and Platform Administrators.
  * Added a command for triggering user cluster upgrade.



**Vertex AI** : 

  * Added [online predictions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions) preview to serve requests using your own prediction models on a set of supported containers.
  * Added [Document Translate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-dvs) preview to translate formatted PDF documents directly and preserve the original formatting and layout in translations.
  * Included support for [backing and restoring notebook data](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data) in the home directory of Vertex AI Workbench JupyterLab instances. 



**Virtual machine management**

  * Added [Windows OS support](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-manage-windows-vm) for virtual machines to create, import, and connect to a Windows VM.



* * *

Fixed

**Billing** :

  * Fixed the issue with the `onetimeusage` job always failing at updating labels on the `onetimeusage` object, causing failure alerts.


  * Fixed the issue causing the aggregate cost for a custom resource (CR) to duplicate when the job restarts after the cost of the CR writes to the database, before the label updates to processed.



**Hardware security module** :

  * Fixed the issue causing the hardware security module to frequently toggle between the `ServicesNotStarted` and `ready` states.



**Hybrid identity** :

  * Fixed the issue with network configuration in identity pods.



**Inventory management** :

  * Fixed the issue with the license parser not parsing object storage files whose license JSON text spreads multiple lines.
  * Fixed the issue with hardware 3.0 CellCfg CableType Validation regular expression.
  * Fixed the issue with including bootstrapper node in hardware validation.
  * Fixed the issue with root admin cluster node having `SecureBootEnable` turned off after server bootstrapping.



**Operations Suite Infrastructure Core Services (OIC)**

  * Fixed the issue with `Initialize-BareMetalHost.ps1` not detecting that a reboot is required.
  * Fixed the issue with an enterprise CA root and not issuing a req file to submit for an offline CA root.
  * Fixed the issue where the OIC VM creation process left Hyper-V time synchronization enabled.



**Ticketing system**

  * Fixed MariaDB Audit issue.



**Upgrade**

  * Fixed the issue with Identity and Access Management (IAM) alerts by adding IAM postflight upgrade checks.



**Virtual machine management**

  * Fixed the issue with the VM status previously showing `PendingIPAllocation` if the VM is not able to be scheduled. After the fix, the VM status shows `ErrorUnscheduable`. 
  * Fixed the issue with the incorrect object storage secret being used in VM image import operations. 



* * *

Issue

**Backup and restore** :

  * Alerts for a backup repository may fire even when the repository is healthy. 



**Cluster management** :

  * The `machine-init` job fails during cluster provisioning. 



**Physical servers** :

  * The root admin cluster update progress is stuck at node upgrade, specifically `NodeBIOSFirmwareUpgradeCompleted`. 



**Database Service** :

  * Database Service workloads operate within the system cluster, which could result in database workloads sharing compute infrastructure with other database instances and various control plane systems. 



**Harbor as a service (HAAS)** :

  * Being a preview feature of Google Distributed Cloud air-gapped 1.12.0, HaaS is not expected to operate in production environments.  
The preinstall job fails by design to prevent the subcomponents from reconciling properly, which prevents users from using HaaS.   
It is expected to find HaaS subcomponents in the reconciling state, which does not impact the functionality of other components. 



**Firewall** :

  * During customer deployment, the `secret.yaml` file administrator username must be `admin`, and instead contains `TO-BE-FILLED` after the first creation. The `admin` username must be used to initialize the first configuration onto the firewall. 



**Hardware security module** :

  * Deactivated trial licenses are still detectable in CipherTrust Manager, triggering false expiration warnings. 
  * When [deleting a KMS `CTMKey`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/hsm#delete-ctmkey), the PA might encounter unexpected behaviors, including the KMS service not starting for the organization. 
  * A rotatable secret for hardware security modules is in an unknown state. 
  * HSM internal certificate authority rotations get stuck and don't complete. 



**Logging** :

  * After [enabling logs export to an external SIEM destination](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/export-logs-external), the forwarded logs don't contain any Kubernetes API server logs. 



**Monitoring** :

  * Node Exporter certificates might not become ready when creating an organization. 
  * Some metrics from the user clusters are not collected. This issue affects the user VM clusters but not the system cluster. 
  * The metrics storage class is incorrectly defined in the configuration. 
  * The `mon-prober-backend-prometheus-config` ConfigMap gets reset to include no probe jobs, and alert `MON-A0001` is triggered. 



**Node platform** :

  * The node upgrade fails due to an outdated `lvm.conf` file. 



**Physical servers** :

  * The root admin cluster update progress is stuck at node upgrade, specifically `NodeBIOSFirmwareUpgradeCompleted`. 


  * When installing a server manually, the server installation might get stuck. 



**Upgrade** :

  * Node upgrade fails for `NodeOSInPlaceUpgradeCompleted`. 
  * Switch upgrade fails to run command `install add bootflash://..`
  * Several pods in a system cluster might get stuck in the `TaintToleration` state. 



**Upper networking** :

  * A user VM cluster gets stuck in the `ContainerCreating` state with the `FailedCreatePodSandBox` warning. 



**Vertex AI** :

  * The `MonitoringTarget` shows a `Not Ready` status when user clusters are being created, causing pre-trained APIs to continually show an `Enabling` state in the user interface. 



**VM Backup and Restore** :

  * Role-based access control (RBAC) and schema settings in the VM manager is stopping users from starting VM backup and restore processes. 


  * The VM image import fails at the image translation step due to insufficient disk size and timeout on obj storage proxy response. 



**SIEM** :

  * OCLCM Preinstall jobs repeatedly fail on feature gate check. 



* * *

Deprecated

**Performance** : 

  * Google Distributed Cloud air-gapped 1.12.0 deprecates the ability to execute `provision key` benchmarks.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
