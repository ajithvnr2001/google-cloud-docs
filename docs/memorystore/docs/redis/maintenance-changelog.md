---
url: https://docs.cloud.google.com/memorystore/docs/redis/maintenance-changelog/
title: Memorystore for Redis maintenance changelogs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:13:34.111259+00:00
---

# Memorystore for Redis maintenance changelogs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/maintenance-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Resources ](https://docs.cloud.google.com/memorystore/docs/redis/resources)



Send feedback 

#  Memorystore for Redis maintenance changelogs Stay organized with collections  Save and categorize content based on your preferences. 

This page contains a log of maintenance changes. Memorystore for Redis releases maintenance updates for new features, security patches, bug fixes, performance improvements, and more.

You can perform maintenance updates by using [self-service maintenance](https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance). Memorystore for Redis also performs scheduled maintenance updates once every few months. You can set windows for when maintenance updates occur. For more information, see [Find and set maintenance windows](https://docs.cloud.google.com/memorystore/docs/redis/find-and-set-maintenance-windows).

To view the maintenance version, use the [`gcloud redis instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/instances/describe) command. The maintenance version appears next to the `maintenanceVersion` parameter. For more information, see [View instance information](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#view_instance_information). Also, to learn more about maintenance updates, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance).

To get the latest maintenance changes, add the URL for the [XML file](https://docs.cloud.google.com/static/feeds/memorystore-for-redis-maintenance-changelog.xml) of the maintenance changelog for Memorystore for Redis to your feed reader.

## 20260916_03_01

**Date released** | **Release type**  
---|---  
2026-10-09 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and the Redis binary to address the CVEs listed in Security patches.   
All Redis instances | Set the Redis host OS version to [cos-121-18867-584-3](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-584-3_).  
  
### Security patches

2026

  * [CVE-2026-80906](https://nvd.nist.gov/vuln/detail/CVE-2026-80906)
  * [CVE-2026-80904](https://nvd.nist.gov/vuln/detail/CVE-2026-80904)
  * [CVE-2026-80901](https://nvd.nist.gov/vuln/detail/CVE-2026-80901)
  * [CVE-2026-80893](https://nvd.nist.gov/vuln/detail/CVE-2026-80893)
  * [CVE-2026-80880](https://nvd.nist.gov/vuln/detail/CVE-2026-80880)
  * [CVE-2026-80876](https://nvd.nist.gov/vuln/detail/CVE-2026-80876)
  * [CVE-2026-80875](https://nvd.nist.gov/vuln/detail/CVE-2026-80875)
  * [CVE-2026-80865](https://nvd.nist.gov/vuln/detail/CVE-2026-80865)
  * [CVE-2026-80744](https://nvd.nist.gov/vuln/detail/CVE-2026-80744)
  * [CVE-2026-80742](https://nvd.nist.gov/vuln/detail/CVE-2026-80742)
  * [CVE-2026-80733](https://nvd.nist.gov/vuln/detail/CVE-2026-80733)
  * [CVE-2026-80731](https://nvd.nist.gov/vuln/detail/CVE-2026-80731)
  * [CVE-2026-80730](https://nvd.nist.gov/vuln/detail/CVE-2026-80730)
  * [CVE-2026-80726](https://nvd.nist.gov/vuln/detail/CVE-2026-80726)
  * [CVE-2026-80714](https://nvd.nist.gov/vuln/detail/CVE-2026-80714)
  * [CVE-2026-80691](https://nvd.nist.gov/vuln/detail/CVE-2026-80691)
  * [CVE-2026-80686](https://nvd.nist.gov/vuln/detail/CVE-2026-80686)
  * [CVE-2026-80681](https://nvd.nist.gov/vuln/detail/CVE-2026-80681)
  * [CVE-2026-80677](https://nvd.nist.gov/vuln/detail/CVE-2026-80677)
  * [CVE-2026-80669](https://nvd.nist.gov/vuln/detail/CVE-2026-80669)
  * [CVE-2026-80664](https://nvd.nist.gov/vuln/detail/CVE-2026-80664)
  * [CVE-2026-80646](https://nvd.nist.gov/vuln/detail/CVE-2026-80646)
  * [CVE-2026-80636](https://nvd.nist.gov/vuln/detail/CVE-2026-80636)
  * [CVE-2026-80630](https://nvd.nist.gov/vuln/detail/CVE-2026-80630)
  * [CVE-2026-80620](https://nvd.nist.gov/vuln/detail/CVE-2026-80620)
  * [CVE-2026-80619](https://nvd.nist.gov/vuln/detail/CVE-2026-80619)
  * [CVE-2026-80613](https://nvd.nist.gov/vuln/detail/CVE-2026-80613)
  * [CVE-2026-80603](https://nvd.nist.gov/vuln/detail/CVE-2026-80603)
  * [CVE-2026-80602](https://nvd.nist.gov/vuln/detail/CVE-2026-80602)
  * [CVE-2026-80589](https://nvd.nist.gov/vuln/detail/CVE-2026-80589)
  * [CVE-2026-80534](https://nvd.nist.gov/vuln/detail/CVE-2026-80534)
  * [CVE-2026-80529](https://nvd.nist.gov/vuln/detail/CVE-2026-80529)
  * [CVE-2026-74748](https://nvd.nist.gov/vuln/detail/CVE-2026-74748)
  * [CVE-2026-74746](https://nvd.nist.gov/vuln/detail/CVE-2026-74746)
  * [CVE-2026-74744](https://nvd.nist.gov/vuln/detail/CVE-2026-74744)
  * [CVE-2026-74743](https://nvd.nist.gov/vuln/detail/CVE-2026-74743)
  * [CVE-2026-74740](https://nvd.nist.gov/vuln/detail/CVE-2026-74740)
  * [CVE-2026-74739](https://nvd.nist.gov/vuln/detail/CVE-2026-74739)
  * [CVE-2026-74736](https://nvd.nist.gov/vuln/detail/CVE-2026-74736)
  * [CVE-2026-74730](https://nvd.nist.gov/vuln/detail/CVE-2026-74730)
  * [CVE-2026-74726](https://nvd.nist.gov/vuln/detail/CVE-2026-74726)
  * [CVE-2026-74724](https://nvd.nist.gov/vuln/detail/CVE-2026-74724)
  * [CVE-2026-74720](https://nvd.nist.gov/vuln/detail/CVE-2026-74720)
  * [CVE-2026-74718](https://nvd.nist.gov/vuln/detail/CVE-2026-74718)
  * [CVE-2026-74717](https://nvd.nist.gov/vuln/detail/CVE-2026-74717)
  * [CVE-2026-74714](https://nvd.nist.gov/vuln/detail/CVE-2026-74714)
  * [CVE-2026-74705](https://nvd.nist.gov/vuln/detail/CVE-2026-74705)
  * [CVE-2026-74700](https://nvd.nist.gov/vuln/detail/CVE-2026-74700)
  * [CVE-2026-74696](https://nvd.nist.gov/vuln/detail/CVE-2026-74696)
  * [CVE-2026-74683](https://nvd.nist.gov/vuln/detail/CVE-2026-74683)
  * [CVE-2026-74676](https://nvd.nist.gov/vuln/detail/CVE-2026-74676)
  * [CVE-2026-74675](https://nvd.nist.gov/vuln/detail/CVE-2026-74675)
  * [CVE-2026-74673](https://nvd.nist.gov/vuln/detail/CVE-2026-74673)
  * [CVE-2026-74672](https://nvd.nist.gov/vuln/detail/CVE-2026-74672)
  * [CVE-2026-74671](https://nvd.nist.gov/vuln/detail/CVE-2026-74671)
  * [CVE-2026-74670](https://nvd.nist.gov/vuln/detail/CVE-2026-74670)
  * [CVE-2026-74669](https://nvd.nist.gov/vuln/detail/CVE-2026-74669)
  * [CVE-2026-74668](https://nvd.nist.gov/vuln/detail/CVE-2026-74668)
  * [CVE-2026-74667](https://nvd.nist.gov/vuln/detail/CVE-2026-74667)
  * [CVE-2026-74666](https://nvd.nist.gov/vuln/detail/CVE-2026-74666)
  * [CVE-2026-74663](https://nvd.nist.gov/vuln/detail/CVE-2026-74663)
  * [CVE-2026-74660](https://nvd.nist.gov/vuln/detail/CVE-2026-74660)
  * [CVE-2026-74658](https://nvd.nist.gov/vuln/detail/CVE-2026-74658)
  * [CVE-2026-74657](https://nvd.nist.gov/vuln/detail/CVE-2026-74657)
  * [CVE-2026-74656](https://nvd.nist.gov/vuln/detail/CVE-2026-74656)
  * [CVE-2026-74636](https://nvd.nist.gov/vuln/detail/CVE-2026-74636)
  * [CVE-2026-74632](https://nvd.nist.gov/vuln/detail/CVE-2026-74632)
  * [CVE-2026-74630](https://nvd.nist.gov/vuln/detail/CVE-2026-74630)
  * [CVE-2026-74624](https://nvd.nist.gov/vuln/detail/CVE-2026-74624)
  * [CVE-2026-74620](https://nvd.nist.gov/vuln/detail/CVE-2026-74620)
  * [CVE-2026-74619](https://nvd.nist.gov/vuln/detail/CVE-2026-74619)
  * [CVE-2026-74616](https://nvd.nist.gov/vuln/detail/CVE-2026-74616)
  * [CVE-2026-74615](https://nvd.nist.gov/vuln/detail/CVE-2026-74615)
  * [CVE-2026-74614](https://nvd.nist.gov/vuln/detail/CVE-2026-74614)
  * [CVE-2026-74613](https://nvd.nist.gov/vuln/detail/CVE-2026-74613)
  * [CVE-2026-74612](https://nvd.nist.gov/vuln/detail/CVE-2026-74612)
  * [CVE-2026-74610](https://nvd.nist.gov/vuln/detail/CVE-2026-74610)
  * [CVE-2026-74608](https://nvd.nist.gov/vuln/detail/CVE-2026-74608)
  * [CVE-2026-74607](https://nvd.nist.gov/vuln/detail/CVE-2026-74607)
  * [CVE-2026-74606](https://nvd.nist.gov/vuln/detail/CVE-2026-74606)
  * [CVE-2026-74601](https://nvd.nist.gov/vuln/detail/CVE-2026-74601)
  * [CVE-2026-74599](https://nvd.nist.gov/vuln/detail/CVE-2026-74599)
  * [CVE-2026-74598](https://nvd.nist.gov/vuln/detail/CVE-2026-74598)
  * [CVE-2026-74597](https://nvd.nist.gov/vuln/detail/CVE-2026-74597)
  * [CVE-2026-74594](https://nvd.nist.gov/vuln/detail/CVE-2026-74594)
  * [CVE-2026-74589](https://nvd.nist.gov/vuln/detail/CVE-2026-74589)
  * [CVE-2026-74583](https://nvd.nist.gov/vuln/detail/CVE-2026-74583)
  * [CVE-2026-74582](https://nvd.nist.gov/vuln/detail/CVE-2026-74582)
  * [CVE-2026-74581](https://nvd.nist.gov/vuln/detail/CVE-2026-74581)
  * [CVE-2026-74580](https://nvd.nist.gov/vuln/detail/CVE-2026-74580)
  * [CVE-2026-74579](https://nvd.nist.gov/vuln/detail/CVE-2026-74579)
  * [CVE-2026-74569](https://nvd.nist.gov/vuln/detail/CVE-2026-74569)
  * [CVE-2026-74567](https://nvd.nist.gov/vuln/detail/CVE-2026-74567)
  * [CVE-2026-74566](https://nvd.nist.gov/vuln/detail/CVE-2026-74566)
  * [CVE-2026-74564](https://nvd.nist.gov/vuln/detail/CVE-2026-74564)
  * [CVE-2026-74557](https://nvd.nist.gov/vuln/detail/CVE-2026-74557)
  * [CVE-2026-74556](https://nvd.nist.gov/vuln/detail/CVE-2026-74556)
  * [CVE-2026-74550](https://nvd.nist.gov/vuln/detail/CVE-2026-74550)
  * [CVE-2026-74518](https://nvd.nist.gov/vuln/detail/CVE-2026-74518)
  * [CVE-2026-74516](https://nvd.nist.gov/vuln/detail/CVE-2026-74516)
  * [CVE-2026-74512](https://nvd.nist.gov/vuln/detail/CVE-2026-74512)
  * [CVE-2026-74492](https://nvd.nist.gov/vuln/detail/CVE-2026-74492)
  * [CVE-2026-74487](https://nvd.nist.gov/vuln/detail/CVE-2026-74487)
  * [CVE-2026-74485](https://nvd.nist.gov/vuln/detail/CVE-2026-74485)
  * [CVE-2026-74482](https://nvd.nist.gov/vuln/detail/CVE-2026-74482)
  * [CVE-2026-74481](https://nvd.nist.gov/vuln/detail/CVE-2026-74481)
  * [CVE-2026-74480](https://nvd.nist.gov/vuln/detail/CVE-2026-74480)
  * [CVE-2026-74476](https://nvd.nist.gov/vuln/detail/CVE-2026-74476)
  * [CVE-2026-74475](https://nvd.nist.gov/vuln/detail/CVE-2026-74475)
  * [CVE-2026-74474](https://nvd.nist.gov/vuln/detail/CVE-2026-74474)
  * [CVE-2026-74473](https://nvd.nist.gov/vuln/detail/CVE-2026-74473)
  * [CVE-2026-74472](https://nvd.nist.gov/vuln/detail/CVE-2026-74472)
  * [CVE-2026-74471](https://nvd.nist.gov/vuln/detail/CVE-2026-74471)
  * [CVE-2026-74406](https://nvd.nist.gov/vuln/detail/CVE-2026-74406)
  * [CVE-2026-74398](https://nvd.nist.gov/vuln/detail/CVE-2026-74398)
  * [CVE-2026-74397](https://nvd.nist.gov/vuln/detail/CVE-2026-74397)
  * [CVE-2026-74395](https://nvd.nist.gov/vuln/detail/CVE-2026-74395)
  * [CVE-2026-74384](https://nvd.nist.gov/vuln/detail/CVE-2026-74384)
  * [CVE-2026-74382](https://nvd.nist.gov/vuln/detail/CVE-2026-74382)
  * [CVE-2026-74376](https://nvd.nist.gov/vuln/detail/CVE-2026-74376)
  * [CVE-2026-74363](https://nvd.nist.gov/vuln/detail/CVE-2026-74363)
  * [CVE-2026-74359](https://nvd.nist.gov/vuln/detail/CVE-2026-74359)
  * [CVE-2026-74331](https://nvd.nist.gov/vuln/detail/CVE-2026-74331)
  * [CVE-2026-74330](https://nvd.nist.gov/vuln/detail/CVE-2026-74330)
  * [CVE-2026-74329](https://nvd.nist.gov/vuln/detail/CVE-2026-74329)
  * [CVE-2026-74327](https://nvd.nist.gov/vuln/detail/CVE-2026-74327)
  * [CVE-2026-74310](https://nvd.nist.gov/vuln/detail/CVE-2026-74310)
  * [CVE-2026-74308](https://nvd.nist.gov/vuln/detail/CVE-2026-74308)
  * [CVE-2026-74305](https://nvd.nist.gov/vuln/detail/CVE-2026-74305)
  * [CVE-2026-74297](https://nvd.nist.gov/vuln/detail/CVE-2026-74297)
  * [CVE-2026-74296](https://nvd.nist.gov/vuln/detail/CVE-2026-74296)
  * [CVE-2026-74288](https://nvd.nist.gov/vuln/detail/CVE-2026-74288)
  * [CVE-2026-74284](https://nvd.nist.gov/vuln/detail/CVE-2026-74284)
  * [CVE-2026-74271](https://nvd.nist.gov/vuln/detail/CVE-2026-74271)
  * [CVE-2026-74270](https://nvd.nist.gov/vuln/detail/CVE-2026-74270)
  * [CVE-2026-74267](https://nvd.nist.gov/vuln/detail/CVE-2026-74267)
  * [CVE-2026-74256](https://nvd.nist.gov/vuln/detail/CVE-2026-74256)
  * [CVE-2026-72502](https://nvd.nist.gov/vuln/detail/CVE-2026-72502)
  * [CVE-2026-72487](https://nvd.nist.gov/vuln/detail/CVE-2026-72487)
  * [CVE-2026-72473](https://nvd.nist.gov/vuln/detail/CVE-2026-72473)
  * [CVE-2026-72467](https://nvd.nist.gov/vuln/detail/CVE-2026-72467)
  * [CVE-2026-72466](https://nvd.nist.gov/vuln/detail/CVE-2026-72466)
  * [CVE-2026-72464](https://nvd.nist.gov/vuln/detail/CVE-2026-72464)
  * [CVE-2026-72460](https://nvd.nist.gov/vuln/detail/CVE-2026-72460)
  * [CVE-2026-72459](https://nvd.nist.gov/vuln/detail/CVE-2026-72459)
  * [CVE-2026-72450](https://nvd.nist.gov/vuln/detail/CVE-2026-72450)
  * [CVE-2026-72444](https://nvd.nist.gov/vuln/detail/CVE-2026-72444)
  * [CVE-2026-72437](https://nvd.nist.gov/vuln/detail/CVE-2026-72437)
  * [CVE-2026-72436](https://nvd.nist.gov/vuln/detail/CVE-2026-72436)
  * [CVE-2026-72435](https://nvd.nist.gov/vuln/detail/CVE-2026-72435)
  * [CVE-2026-72428](https://nvd.nist.gov/vuln/detail/CVE-2026-72428)
  * [CVE-2026-72427](https://nvd.nist.gov/vuln/detail/CVE-2026-72427)
  * [CVE-2026-72421](https://nvd.nist.gov/vuln/detail/CVE-2026-72421)
  * [CVE-2026-72419](https://nvd.nist.gov/vuln/detail/CVE-2026-72419)
  * [CVE-2026-72418](https://nvd.nist.gov/vuln/detail/CVE-2026-72418)
  * [CVE-2026-72416](https://nvd.nist.gov/vuln/detail/CVE-2026-72416)
  * [CVE-2026-72400](https://nvd.nist.gov/vuln/detail/CVE-2026-72400)
  * [CVE-2026-72392](https://nvd.nist.gov/vuln/detail/CVE-2026-72392)
  * [CVE-2026-72390](https://nvd.nist.gov/vuln/detail/CVE-2026-72390)
  * [CVE-2026-72389](https://nvd.nist.gov/vuln/detail/CVE-2026-72389)
  * [CVE-2026-72379](https://nvd.nist.gov/vuln/detail/CVE-2026-72379)
  * [CVE-2026-72351](https://nvd.nist.gov/vuln/detail/CVE-2026-72351)
  * [CVE-2026-72350](https://nvd.nist.gov/vuln/detail/CVE-2026-72350)
  * [CVE-2026-72349](https://nvd.nist.gov/vuln/detail/CVE-2026-72349)
  * [CVE-2026-72348](https://nvd.nist.gov/vuln/detail/CVE-2026-72348)
  * [CVE-2026-72347](https://nvd.nist.gov/vuln/detail/CVE-2026-72347)
  * [CVE-2026-72343](https://nvd.nist.gov/vuln/detail/CVE-2026-72343)
  * [CVE-2026-72342](https://nvd.nist.gov/vuln/detail/CVE-2026-72342)
  * [CVE-2026-72338](https://nvd.nist.gov/vuln/detail/CVE-2026-72338)
  * [CVE-2026-72330](https://nvd.nist.gov/vuln/detail/CVE-2026-72330)
  * [CVE-2026-72323](https://nvd.nist.gov/vuln/detail/CVE-2026-72323)
  * [CVE-2026-72322](https://nvd.nist.gov/vuln/detail/CVE-2026-72322)
  * [CVE-2026-72319](https://nvd.nist.gov/vuln/detail/CVE-2026-72319)
  * [CVE-2026-72318](https://nvd.nist.gov/vuln/detail/CVE-2026-72318)
  * [CVE-2026-72317](https://nvd.nist.gov/vuln/detail/CVE-2026-72317)
  * [CVE-2026-72310](https://nvd.nist.gov/vuln/detail/CVE-2026-72310)
  * [CVE-2026-72289](https://nvd.nist.gov/vuln/detail/CVE-2026-72289)
  * [CVE-2026-72284](https://nvd.nist.gov/vuln/detail/CVE-2026-72284)
  * [CVE-2026-72282](https://nvd.nist.gov/vuln/detail/CVE-2026-72282)
  * [CVE-2026-72256](https://nvd.nist.gov/vuln/detail/CVE-2026-72256)
  * [CVE-2026-72255](https://nvd.nist.gov/vuln/detail/CVE-2026-72255)
  * [CVE-2026-72254](https://nvd.nist.gov/vuln/detail/CVE-2026-72254)
  * [CVE-2026-72253](https://nvd.nist.gov/vuln/detail/CVE-2026-72253)
  * [CVE-2026-72252](https://nvd.nist.gov/vuln/detail/CVE-2026-72252)
  * [CVE-2026-72251](https://nvd.nist.gov/vuln/detail/CVE-2026-72251)
  * [CVE-2026-72250](https://nvd.nist.gov/vuln/detail/CVE-2026-72250)
  * [CVE-2026-72247](https://nvd.nist.gov/vuln/detail/CVE-2026-72247)
  * [CVE-2026-72225](https://nvd.nist.gov/vuln/detail/CVE-2026-72225)
  * [CVE-2026-72222](https://nvd.nist.gov/vuln/detail/CVE-2026-72222)
  * [CVE-2026-72221](https://nvd.nist.gov/vuln/detail/CVE-2026-72221)
  * [CVE-2026-72219](https://nvd.nist.gov/vuln/detail/CVE-2026-72219)
  * [CVE-2026-72218](https://nvd.nist.gov/vuln/detail/CVE-2026-72218)
  * [CVE-2026-72217](https://nvd.nist.gov/vuln/detail/CVE-2026-72217)
  * [CVE-2026-72172](https://nvd.nist.gov/vuln/detail/CVE-2026-72172)
  * [CVE-2026-72170](https://nvd.nist.gov/vuln/detail/CVE-2026-72170)
  * [CVE-2026-72166](https://nvd.nist.gov/vuln/detail/CVE-2026-72166)
  * [CVE-2026-72152](https://nvd.nist.gov/vuln/detail/CVE-2026-72152)
  * [CVE-2026-72138](https://nvd.nist.gov/vuln/detail/CVE-2026-72138)
  * [CVE-2026-72136](https://nvd.nist.gov/vuln/detail/CVE-2026-72136)
  * [CVE-2026-72135](https://nvd.nist.gov/vuln/detail/CVE-2026-72135)
  * [CVE-2026-72132](https://nvd.nist.gov/vuln/detail/CVE-2026-72132)
  * [CVE-2026-72110](https://nvd.nist.gov/vuln/detail/CVE-2026-72110)
  * [CVE-2026-72108](https://nvd.nist.gov/vuln/detail/CVE-2026-72108)
  * [CVE-2026-72106](https://nvd.nist.gov/vuln/detail/CVE-2026-72106)
  * [CVE-2026-72102](https://nvd.nist.gov/vuln/detail/CVE-2026-72102)
  * [CVE-2026-72099](https://nvd.nist.gov/vuln/detail/CVE-2026-72099)
  * [CVE-2026-72096](https://nvd.nist.gov/vuln/detail/CVE-2026-72096)
  * [CVE-2026-72084](https://nvd.nist.gov/vuln/detail/CVE-2026-72084)
  * [CVE-2026-72083](https://nvd.nist.gov/vuln/detail/CVE-2026-72083)
  * [CVE-2026-72068](https://nvd.nist.gov/vuln/detail/CVE-2026-72068)
  * [CVE-2026-72067](https://nvd.nist.gov/vuln/detail/CVE-2026-72067)
  * [CVE-2026-72066](https://nvd.nist.gov/vuln/detail/CVE-2026-72066)
  * [CVE-2026-72056](https://nvd.nist.gov/vuln/detail/CVE-2026-72056)
  * [CVE-2026-72053](https://nvd.nist.gov/vuln/detail/CVE-2026-72053)
  * [CVE-2026-72052](https://nvd.nist.gov/vuln/detail/CVE-2026-72052)
  * [CVE-2026-72051](https://nvd.nist.gov/vuln/detail/CVE-2026-72051)
  * [CVE-2026-72036](https://nvd.nist.gov/vuln/detail/CVE-2026-72036)
  * [CVE-2026-72030](https://nvd.nist.gov/vuln/detail/CVE-2026-72030)
  * [CVE-2026-72021](https://nvd.nist.gov/vuln/detail/CVE-2026-72021)
  * [CVE-2026-72020](https://nvd.nist.gov/vuln/detail/CVE-2026-72020)
  * [CVE-2026-72010](https://nvd.nist.gov/vuln/detail/CVE-2026-72010)
  * [CVE-2026-68480](https://nvd.nist.gov/vuln/detail/CVE-2026-68480)
  * [CVE-2026-68477](https://nvd.nist.gov/vuln/detail/CVE-2026-68477)
  * [CVE-2026-68476](https://nvd.nist.gov/vuln/detail/CVE-2026-68476)
  * [CVE-2026-68461](https://nvd.nist.gov/vuln/detail/CVE-2026-68461)
  * [CVE-2026-68432](https://nvd.nist.gov/vuln/detail/CVE-2026-68432)
  * [CVE-2026-68428](https://nvd.nist.gov/vuln/detail/CVE-2026-68428)
  * [CVE-2026-68425](https://nvd.nist.gov/vuln/detail/CVE-2026-68425)
  * [CVE-2026-68398](https://nvd.nist.gov/vuln/detail/CVE-2026-68398)
  * [CVE-2026-68388](https://nvd.nist.gov/vuln/detail/CVE-2026-68388)
  * [CVE-2026-68386](https://nvd.nist.gov/vuln/detail/CVE-2026-68386)
  * [CVE-2026-68343](https://nvd.nist.gov/vuln/detail/CVE-2026-68343)
  * [CVE-2026-68338](https://nvd.nist.gov/vuln/detail/CVE-2026-68338)
  * [CVE-2026-68336](https://nvd.nist.gov/vuln/detail/CVE-2026-68336)
  * [CVE-2026-68329](https://nvd.nist.gov/vuln/detail/CVE-2026-68329)
  * [CVE-2026-68325](https://nvd.nist.gov/vuln/detail/CVE-2026-68325)
  * [CVE-2026-68299](https://nvd.nist.gov/vuln/detail/CVE-2026-68299)
  * [CVE-2026-68284](https://nvd.nist.gov/vuln/detail/CVE-2026-68284)
  * [CVE-2026-68187](https://nvd.nist.gov/vuln/detail/CVE-2026-68187)
  * [CVE-2026-68186](https://nvd.nist.gov/vuln/detail/CVE-2026-68186)
  * [CVE-2026-68184](https://nvd.nist.gov/vuln/detail/CVE-2026-68184)
  * [CVE-2026-68166](https://nvd.nist.gov/vuln/detail/CVE-2026-68166)
  * [CVE-2026-68149](https://nvd.nist.gov/vuln/detail/CVE-2026-68149)
  * [CVE-2026-68147](https://nvd.nist.gov/vuln/detail/CVE-2026-68147)
  * [CVE-2026-68146](https://nvd.nist.gov/vuln/detail/CVE-2026-68146)
  * [CVE-2026-68145](https://nvd.nist.gov/vuln/detail/CVE-2026-68145)
  * [CVE-2026-68142](https://nvd.nist.gov/vuln/detail/CVE-2026-68142)
  * [CVE-2026-68138](https://nvd.nist.gov/vuln/detail/CVE-2026-68138)
  * [CVE-2026-68136](https://nvd.nist.gov/vuln/detail/CVE-2026-68136)
  * [CVE-2026-68132](https://nvd.nist.gov/vuln/detail/CVE-2026-68132)
  * [CVE-2026-68129](https://nvd.nist.gov/vuln/detail/CVE-2026-68129)
  * [CVE-2026-68118](https://nvd.nist.gov/vuln/detail/CVE-2026-68118)
  * [CVE-2026-68116](https://nvd.nist.gov/vuln/detail/CVE-2026-68116)
  * [CVE-2026-68096](https://nvd.nist.gov/vuln/detail/CVE-2026-68096)
  * [CVE-2026-68093](https://nvd.nist.gov/vuln/detail/CVE-2026-68093)
  * [CVE-2026-64604](https://nvd.nist.gov/vuln/detail/CVE-2026-64604)
  * [CVE-2026-64598](https://nvd.nist.gov/vuln/detail/CVE-2026-64598)
  * [CVE-2026-64597](https://nvd.nist.gov/vuln/detail/CVE-2026-64597)
  * [CVE-2026-64590](https://nvd.nist.gov/vuln/detail/CVE-2026-64590)
  * [CVE-2026-64589](https://nvd.nist.gov/vuln/detail/CVE-2026-64589)
  * [CVE-2026-64580](https://nvd.nist.gov/vuln/detail/CVE-2026-64580)
  * [CVE-2026-64579](https://nvd.nist.gov/vuln/detail/CVE-2026-64579)
  * [CVE-2026-64576](https://nvd.nist.gov/vuln/detail/CVE-2026-64576)
  * [CVE-2026-64572](https://nvd.nist.gov/vuln/detail/CVE-2026-64572)
  * [CVE-2026-64563](https://nvd.nist.gov/vuln/detail/CVE-2026-64563)
  * [CVE-2026-64562](https://nvd.nist.gov/vuln/detail/CVE-2026-64562)
  * [CVE-2026-64561](https://nvd.nist.gov/vuln/detail/CVE-2026-64561)
  * [CVE-2026-64560](https://nvd.nist.gov/vuln/detail/CVE-2026-64560)
  * [CVE-2026-64556](https://nvd.nist.gov/vuln/detail/CVE-2026-64556)
  * [CVE-2026-64554](https://nvd.nist.gov/vuln/detail/CVE-2026-64554)
  * [CVE-2026-64552](https://nvd.nist.gov/vuln/detail/CVE-2026-64552)
  * [CVE-2026-64548](https://nvd.nist.gov/vuln/detail/CVE-2026-64548)
  * [CVE-2026-64546](https://nvd.nist.gov/vuln/detail/CVE-2026-64546)
  * [CVE-2026-64545](https://nvd.nist.gov/vuln/detail/CVE-2026-64545)
  * [CVE-2026-64542](https://nvd.nist.gov/vuln/detail/CVE-2026-64542)
  * [CVE-2026-64538](https://nvd.nist.gov/vuln/detail/CVE-2026-64538)
  * [CVE-2026-64535](https://nvd.nist.gov/vuln/detail/CVE-2026-64535)
  * [CVE-2026-64534](https://nvd.nist.gov/vuln/detail/CVE-2026-64534)
  * [CVE-2026-64530](https://nvd.nist.gov/vuln/detail/CVE-2026-64530)
  * [CVE-2026-64514](https://nvd.nist.gov/vuln/detail/CVE-2026-64514)
  * [CVE-2026-64512](https://nvd.nist.gov/vuln/detail/CVE-2026-64512)
  * [CVE-2026-64508](https://nvd.nist.gov/vuln/detail/CVE-2026-64508)
  * [CVE-2026-64507](https://nvd.nist.gov/vuln/detail/CVE-2026-64507)
  * [CVE-2026-64476](https://nvd.nist.gov/vuln/detail/CVE-2026-64476)
  * [CVE-2026-64475](https://nvd.nist.gov/vuln/detail/CVE-2026-64475)
  * [CVE-2026-64474](https://nvd.nist.gov/vuln/detail/CVE-2026-64474)
  * [CVE-2026-64456](https://nvd.nist.gov/vuln/detail/CVE-2026-64456)
  * [CVE-2026-64448](https://nvd.nist.gov/vuln/detail/CVE-2026-64448)
  * [CVE-2026-64436](https://nvd.nist.gov/vuln/detail/CVE-2026-64436)
  * [CVE-2026-64435](https://nvd.nist.gov/vuln/detail/CVE-2026-64435)
  * [CVE-2026-64425](https://nvd.nist.gov/vuln/detail/CVE-2026-64425)
  * [CVE-2026-64423](https://nvd.nist.gov/vuln/detail/CVE-2026-64423)
  * [CVE-2026-64422](https://nvd.nist.gov/vuln/detail/CVE-2026-64422)
  * [CVE-2026-64413](https://nvd.nist.gov/vuln/detail/CVE-2026-64413)
  * [CVE-2026-64412](https://nvd.nist.gov/vuln/detail/CVE-2026-64412)
  * [CVE-2026-64411](https://nvd.nist.gov/vuln/detail/CVE-2026-64411)
  * [CVE-2026-64401](https://nvd.nist.gov/vuln/detail/CVE-2026-64401)
  * [CVE-2026-64387](https://nvd.nist.gov/vuln/detail/CVE-2026-64387)
  * [CVE-2026-64386](https://nvd.nist.gov/vuln/detail/CVE-2026-64386)
  * [CVE-2026-64385](https://nvd.nist.gov/vuln/detail/CVE-2026-64385)
  * [CVE-2026-64384](https://nvd.nist.gov/vuln/detail/CVE-2026-64384)
  * [CVE-2026-64383](https://nvd.nist.gov/vuln/detail/CVE-2026-64383)
  * [CVE-2026-64382](https://nvd.nist.gov/vuln/detail/CVE-2026-64382)
  * [CVE-2026-64381](https://nvd.nist.gov/vuln/detail/CVE-2026-64381)
  * [CVE-2026-64380](https://nvd.nist.gov/vuln/detail/CVE-2026-64380)
  * [CVE-2026-64379](https://nvd.nist.gov/vuln/detail/CVE-2026-64379)
  * [CVE-2026-64378](https://nvd.nist.gov/vuln/detail/CVE-2026-64378)
  * [CVE-2026-64375](https://nvd.nist.gov/vuln/detail/CVE-2026-64375)
  * [CVE-2026-64373](https://nvd.nist.gov/vuln/detail/CVE-2026-64373)
  * [CVE-2026-64371](https://nvd.nist.gov/vuln/detail/CVE-2026-64371)
  * [CVE-2026-64370](https://nvd.nist.gov/vuln/detail/CVE-2026-64370)
  * [CVE-2026-64368](https://nvd.nist.gov/vuln/detail/CVE-2026-64368)
  * [CVE-2026-64355](https://nvd.nist.gov/vuln/detail/CVE-2026-64355)
  * [CVE-2026-64352](https://nvd.nist.gov/vuln/detail/CVE-2026-64352)
  * [CVE-2026-64326](https://nvd.nist.gov/vuln/detail/CVE-2026-64326)
  * [CVE-2026-64324](https://nvd.nist.gov/vuln/detail/CVE-2026-64324)
  * [CVE-2026-64323](https://nvd.nist.gov/vuln/detail/CVE-2026-64323)
  * [CVE-2026-64322](https://nvd.nist.gov/vuln/detail/CVE-2026-64322)
  * [CVE-2026-64319](https://nvd.nist.gov/vuln/detail/CVE-2026-64319)
  * [CVE-2026-64317](https://nvd.nist.gov/vuln/detail/CVE-2026-64317)
  * [CVE-2026-64313](https://nvd.nist.gov/vuln/detail/CVE-2026-64313)
  * [CVE-2026-64306](https://nvd.nist.gov/vuln/detail/CVE-2026-64306)
  * [CVE-2026-64299](https://nvd.nist.gov/vuln/detail/CVE-2026-64299)
  * [CVE-2026-64298](https://nvd.nist.gov/vuln/detail/CVE-2026-64298)
  * [CVE-2026-64294](https://nvd.nist.gov/vuln/detail/CVE-2026-64294)
  * [CVE-2026-64287](https://nvd.nist.gov/vuln/detail/CVE-2026-64287)
  * [CVE-2026-64286](https://nvd.nist.gov/vuln/detail/CVE-2026-64286)
  * [CVE-2026-64279](https://nvd.nist.gov/vuln/detail/CVE-2026-64279)
  * [CVE-2026-64266](https://nvd.nist.gov/vuln/detail/CVE-2026-64266)
  * [CVE-2026-64247](https://nvd.nist.gov/vuln/detail/CVE-2026-64247)
  * [CVE-2026-64244](https://nvd.nist.gov/vuln/detail/CVE-2026-64244)
  * [CVE-2026-64227](https://nvd.nist.gov/vuln/detail/CVE-2026-64227)
  * [CVE-2026-64192](https://nvd.nist.gov/vuln/detail/CVE-2026-64192)
  * [CVE-2026-64189](https://nvd.nist.gov/vuln/detail/CVE-2026-64189)
  * [CVE-2026-64187](https://nvd.nist.gov/vuln/detail/CVE-2026-64187)
  * [CVE-2026-63830](https://nvd.nist.gov/vuln/detail/CVE-2026-63830)
  * [CVE-2026-63829](https://nvd.nist.gov/vuln/detail/CVE-2026-63829)
  * [CVE-2026-63828](https://nvd.nist.gov/vuln/detail/CVE-2026-63828)
  * [CVE-2026-63827](https://nvd.nist.gov/vuln/detail/CVE-2026-63827)
  * [CVE-2026-63824](https://nvd.nist.gov/vuln/detail/CVE-2026-63824)
  * [CVE-2026-63823](https://nvd.nist.gov/vuln/detail/CVE-2026-63823)
  * [CVE-2026-63810](https://nvd.nist.gov/vuln/detail/CVE-2026-63810)
  * [CVE-2026-63809](https://nvd.nist.gov/vuln/detail/CVE-2026-63809)
  * [CVE-2026-63807](https://nvd.nist.gov/vuln/detail/CVE-2026-63807)
  * [CVE-2026-63806](https://nvd.nist.gov/vuln/detail/CVE-2026-63806)
  * [CVE-2026-63802](https://nvd.nist.gov/vuln/detail/CVE-2026-63802)
  * [CVE-2026-63800](https://nvd.nist.gov/vuln/detail/CVE-2026-63800)
  * [CVE-2026-63795](https://nvd.nist.gov/vuln/detail/CVE-2026-63795)
  * [CVE-2026-63794](https://nvd.nist.gov/vuln/detail/CVE-2026-63794)
  * [CVE-2026-60002](https://nvd.nist.gov/vuln/detail/CVE-2026-60002)
  * [CVE-2026-60001](https://nvd.nist.gov/vuln/detail/CVE-2026-60001)
  * [CVE-2026-60000](https://nvd.nist.gov/vuln/detail/CVE-2026-60000)
  * [CVE-2026-59999](https://nvd.nist.gov/vuln/detail/CVE-2026-59999)
  * [CVE-2026-59997](https://nvd.nist.gov/vuln/detail/CVE-2026-59997)
  * [CVE-2026-59996](https://nvd.nist.gov/vuln/detail/CVE-2026-59996)
  * [CVE-2026-59995](https://nvd.nist.gov/vuln/detail/CVE-2026-59995)
  * [CVE-2026-59890](https://nvd.nist.gov/vuln/detail/CVE-2026-59890)
  * [CVE-2026-58470](https://nvd.nist.gov/vuln/detail/CVE-2026-58470)
  * [CVE-2026-58055](https://nvd.nist.gov/vuln/detail/CVE-2026-58055)
  * [CVE-2026-53400](https://nvd.nist.gov/vuln/detail/CVE-2026-53400)
  * [CVE-2026-53398](https://nvd.nist.gov/vuln/detail/CVE-2026-53398)
  * [CVE-2026-53397](https://nvd.nist.gov/vuln/detail/CVE-2026-53397)
  * [CVE-2026-53393](https://nvd.nist.gov/vuln/detail/CVE-2026-53393)
  * [CVE-2026-53392](https://nvd.nist.gov/vuln/detail/CVE-2026-53392)
  * [CVE-2026-53391](https://nvd.nist.gov/vuln/detail/CVE-2026-53391)
  * [CVE-2026-53388](https://nvd.nist.gov/vuln/detail/CVE-2026-53388)
  * [CVE-2026-53385](https://nvd.nist.gov/vuln/detail/CVE-2026-53385)
  * [CVE-2026-53381](https://nvd.nist.gov/vuln/detail/CVE-2026-53381)
  * [CVE-2026-53090](https://nvd.nist.gov/vuln/detail/CVE-2026-53090)
  * [CVE-2026-40356](https://nvd.nist.gov/vuln/detail/CVE-2026-40356)
  * [CVE-2026-40355](https://nvd.nist.gov/vuln/detail/CVE-2026-40355)
  * [CVE-2026-6019](https://nvd.nist.gov/vuln/detail/CVE-2026-6019)
  * [CVE-2026-3644](https://nvd.nist.gov/vuln/detail/CVE-2026-3644)
  * [CVE-2026-0992](https://nvd.nist.gov/vuln/detail/CVE-2026-0992)
  * [CVE-2026-0990](https://nvd.nist.gov/vuln/detail/CVE-2026-0990)
  * [CVE-2026-0989](https://nvd.nist.gov/vuln/detail/CVE-2026-0989)
  * [CVE-2026-0672](https://nvd.nist.gov/vuln/detail/CVE-2026-0672)



## 20260727_01_00

**Date released** | **Release type**  
---|---  
2026-08-12 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and the Redis binary to address the CVEs listed in Security patches.   
All Redis instances | Set the Redis host OS version to [cos-121-18867-528-21](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-528-21_).  
All Redis instances | Apply the security patch for [CVE-2026-66373](https://nvd.nist.gov/vuln/detail/CVE-2026-66373).  
  
### Security patches

2026

  * [CVE-2026-66373](https://nvd.nist.gov/vuln/detail/CVE-2026-66373)
  * [CVE-2026-56684](https://github.com/valkey-io/valkey/security/advisories/GHSA-53mc-f3m3-99vh)
  * [CVE-2026-53212](https://nvd.nist.gov/vuln/detail/CVE-2026-53212)
  * [CVE-2026-52969](https://nvd.nist.gov/vuln/detail/CVE-2026-52969)
  * [CVE-2026-48743](https://nvd.nist.gov/vuln/detail/CVE-2026-48743)
  * [CVE-2026-48706](https://nvd.nist.gov/vuln/detail/CVE-2026-48706)
  * [CVE-2026-48526](https://nvd.nist.gov/vuln/detail/CVE-2026-48526)
  * [CVE-2026-48497](https://nvd.nist.gov/vuln/detail/CVE-2026-48497)
  * [CVE-2026-48042](https://nvd.nist.gov/vuln/detail/CVE-2026-48042)
  * [CVE-2026-47778](https://nvd.nist.gov/vuln/detail/CVE-2026-47778)
  * [CVE-2026-47692](https://nvd.nist.gov/vuln/detail/CVE-2026-47692)
  * [CVE-2026-47221](https://nvd.nist.gov/vuln/detail/CVE-2026-47221)
  * [CVE-2026-47220](https://nvd.nist.gov/vuln/detail/CVE-2026-47220)
  * [CVE-2026-47207](https://nvd.nist.gov/vuln/detail/CVE-2026-47207)
  * [CVE-2026-47205](https://nvd.nist.gov/vuln/detail/CVE-2026-47205)
  * [CVE-2026-47204](https://nvd.nist.gov/vuln/detail/CVE-2026-47204)
  * [CVE-2026-46333](https://nvd.nist.gov/vuln/detail/CVE-2026-46333)
  * [CVE-2026-46300](https://nvd.nist.gov/vuln/detail/CVE-2026-46300)
  * [CVE-2026-46294](https://nvd.nist.gov/vuln/detail/CVE-2026-46294)
  * [CVE-2026-46243](https://nvd.nist.gov/vuln/detail/CVE-2026-46243)
  * [CVE-2026-46242](https://nvd.nist.gov/vuln/detail/CVE-2026-46242)
  * [CVE-2026-46234](https://nvd.nist.gov/vuln/detail/CVE-2026-46234)
  * [CVE-2026-46173](https://nvd.nist.gov/vuln/detail/CVE-2026-46173)
  * [CVE-2026-46033](https://nvd.nist.gov/vuln/detail/CVE-2026-46033)
  * [CVE-2026-45839](https://nvd.nist.gov/vuln/detail/CVE-2026-45839)
  * [CVE-2026-45447](https://nvd.nist.gov/vuln/detail/CVE-2026-45447)
  * [CVE-2026-45446](https://nvd.nist.gov/vuln/detail/CVE-2026-45446)
  * [CVE-2026-43503](https://nvd.nist.gov/vuln/detail/CVE-2026-43503)
  * [CVE-2026-43501](https://nvd.nist.gov/vuln/detail/CVE-2026-43501)
  * [CVE-2026-43499](https://nvd.nist.gov/vuln/detail/CVE-2026-43499)
  * [CVE-2026-42770](https://nvd.nist.gov/vuln/detail/CVE-2026-42770)
  * [CVE-2026-42766](https://nvd.nist.gov/vuln/detail/CVE-2026-42766)
  * [CVE-2026-42013](https://nvd.nist.gov/vuln/detail/CVE-2026-42013)
  * [CVE-2026-42012](https://nvd.nist.gov/vuln/detail/CVE-2026-42012)
  * [CVE-2026-42011](https://nvd.nist.gov/vuln/detail/CVE-2026-42011)
  * [CVE-2026-42010](https://nvd.nist.gov/vuln/detail/CVE-2026-42010)
  * [CVE-2026-42009](https://nvd.nist.gov/vuln/detail/CVE-2026-42009)
  * [CVE-2026-41567](https://nvd.nist.gov/vuln/detail/CVE-2026-41567)
  * [CVE-2026-34743](https://nvd.nist.gov/vuln/detail/CVE-2026-34743)
  * [CVE-2026-34182](https://nvd.nist.gov/vuln/detail/CVE-2026-34182)
  * [CVE-2026-33846](https://nvd.nist.gov/vuln/detail/CVE-2026-33846)
  * [CVE-2026-33845](https://nvd.nist.gov/vuln/detail/CVE-2026-33845)
  * [CVE-2026-31786](https://nvd.nist.gov/vuln/detail/CVE-2026-31786)
  * [CVE-2026-31527](https://nvd.nist.gov/vuln/detail/CVE-2026-31527)
  * [CVE-2026-27171](https://nvd.nist.gov/vuln/detail/CVE-2026-27171)
  * [CVE-2026-27143](https://nvd.nist.gov/vuln/detail/CVE-2026-27143)
  * [CVE-2026-11824](https://nvd.nist.gov/vuln/detail/CVE-2026-11824)
  * [CVE-2026-11822](https://nvd.nist.gov/vuln/detail/CVE-2026-11822)
  * [CVE-2026-7383](https://nvd.nist.gov/vuln/detail/CVE-2026-7383)
  * [CVE-2026-5260](https://nvd.nist.gov/vuln/detail/CVE-2026-5260)
  * [CVE-2026-4878](https://nvd.nist.gov/vuln/detail/CVE-2026-4878)
  * [CVE-2026-4046](https://nvd.nist.gov/vuln/detail/CVE-2026-4046)
  * [CVE-2026-3833](https://nvd.nist.gov/vuln/detail/CVE-2026-3833)
  * [CVE-2026-0915](https://nvd.nist.gov/vuln/detail/CVE-2026-0915)
  * [CVE-2026-0861](https://nvd.nist.gov/vuln/detail/CVE-2026-0861)



2025

  * [CVE-2025-68121](https://nvd.nist.gov/vuln/detail/CVE-2025-68121)
  * [CVE-2025-38584](https://nvd.nist.gov/vuln/detail/CVE-2025-38584)
  * [CVE-2025-15281](https://nvd.nist.gov/vuln/detail/CVE-2025-15281)
  * [CVE-2025-6297](https://nvd.nist.gov/vuln/detail/CVE-2025-6297)



2023

  * [CVE-2023-5981](https://nvd.nist.gov/vuln/detail/CVE-2023-5981)



## 20260507_00_00

**Date released** | **Release type**  
---|---  
2026-05-21 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and the Redis binary to address the CVEs listed in Security patches.   
All Redis instances | Set the Redis host OS version to [cos-121-18867-381-125](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-125_).  
  
### Security patches

2026

  * [CVE-2026-0994](https://nvd.nist.gov/vuln/detail/CVE-2026-0994)
  * [CVE-2026-1965](https://nvd.nist.gov/vuln/detail/CVE-2026-1965)
  * [CVE-2026-21441](https://nvd.nist.gov/vuln/detail/CVE-2026-21441)
  * [CVE-2026-22999](https://nvd.nist.gov/vuln/detail/CVE-2026-22999)
  * [CVE-2026-23001](https://nvd.nist.gov/vuln/detail/CVE-2026-23001)
  * [CVE-2026-23005](https://nvd.nist.gov/vuln/detail/CVE-2026-23005)
  * [CVE-2026-23011](https://nvd.nist.gov/vuln/detail/CVE-2026-23011)
  * [CVE-2026-23038](https://nvd.nist.gov/vuln/detail/CVE-2026-23038)
  * [CVE-2026-23054](https://nvd.nist.gov/vuln/detail/CVE-2026-23054)
  * [CVE-2026-23069](https://nvd.nist.gov/vuln/detail/CVE-2026-23069)
  * [CVE-2026-23085](https://nvd.nist.gov/vuln/detail/CVE-2026-23085)
  * [CVE-2026-23086](https://nvd.nist.gov/vuln/detail/CVE-2026-23086)
  * [CVE-2026-23095](https://nvd.nist.gov/vuln/detail/CVE-2026-23095)
  * [CVE-2026-23097](https://nvd.nist.gov/vuln/detail/CVE-2026-23097)
  * [CVE-2026-23099](https://nvd.nist.gov/vuln/detail/CVE-2026-23099)
  * [CVE-2026-23102](https://nvd.nist.gov/vuln/detail/CVE-2026-23102)
  * [CVE-2026-23103](https://nvd.nist.gov/vuln/detail/CVE-2026-23103)
  * [CVE-2026-23105](https://nvd.nist.gov/vuln/detail/CVE-2026-23105)
  * [CVE-2026-23107](https://nvd.nist.gov/vuln/detail/CVE-2026-23107)
  * [CVE-2026-23110](https://nvd.nist.gov/vuln/detail/CVE-2026-23110)
  * [CVE-2026-23112](https://nvd.nist.gov/vuln/detail/CVE-2026-23112)
  * [CVE-2026-23113](https://nvd.nist.gov/vuln/detail/CVE-2026-23113)
  * [CVE-2026-23119](https://nvd.nist.gov/vuln/detail/CVE-2026-23119)
  * [CVE-2026-23124](https://nvd.nist.gov/vuln/detail/CVE-2026-23124)
  * [CVE-2026-23154](https://nvd.nist.gov/vuln/detail/CVE-2026-23154)
  * [CVE-2026-23156](https://nvd.nist.gov/vuln/detail/CVE-2026-23156)
  * [CVE-2026-23168](https://nvd.nist.gov/vuln/detail/CVE-2026-23168)
  * [CVE-2026-23193](https://nvd.nist.gov/vuln/detail/CVE-2026-23193)
  * [CVE-2026-23198](https://nvd.nist.gov/vuln/detail/CVE-2026-23198)
  * [CVE-2026-23209](https://nvd.nist.gov/vuln/detail/CVE-2026-23209)
  * [CVE-2026-23212](https://nvd.nist.gov/vuln/detail/CVE-2026-23212)
  * [CVE-2026-23216](https://nvd.nist.gov/vuln/detail/CVE-2026-23216)
  * [CVE-2026-23231](https://nvd.nist.gov/vuln/detail/CVE-2026-23231)
  * [CVE-2026-23243](https://nvd.nist.gov/vuln/detail/CVE-2026-23243)
  * [CVE-2026-23245](https://nvd.nist.gov/vuln/detail/CVE-2026-23245)
  * [CVE-2026-23268](https://nvd.nist.gov/vuln/detail/CVE-2026-23268)
  * [CVE-2026-23269](https://nvd.nist.gov/vuln/detail/CVE-2026-23269)
  * [CVE-2026-23271](https://nvd.nist.gov/vuln/detail/CVE-2026-23271)
  * [CVE-2026-23274](https://nvd.nist.gov/vuln/detail/CVE-2026-23274)
  * [CVE-2026-23277](https://nvd.nist.gov/vuln/detail/CVE-2026-23277)
  * [CVE-2026-23292](https://nvd.nist.gov/vuln/detail/CVE-2026-23292)
  * [CVE-2026-23293](https://nvd.nist.gov/vuln/detail/CVE-2026-23293)
  * [CVE-2026-23296](https://nvd.nist.gov/vuln/detail/CVE-2026-23296)
  * [CVE-2026-23300](https://nvd.nist.gov/vuln/detail/CVE-2026-23300)
  * [CVE-2026-23303](https://nvd.nist.gov/vuln/detail/CVE-2026-23303)
  * [CVE-2026-23304](https://nvd.nist.gov/vuln/detail/CVE-2026-23304)
  * [CVE-2026-23340](https://nvd.nist.gov/vuln/detail/CVE-2026-23340)
  * [CVE-2026-23343](https://nvd.nist.gov/vuln/detail/CVE-2026-23343)
  * [CVE-2026-23351](https://nvd.nist.gov/vuln/detail/CVE-2026-23351)
  * [CVE-2026-23352](https://nvd.nist.gov/vuln/detail/CVE-2026-23352)
  * [CVE-2026-23359](https://nvd.nist.gov/vuln/detail/CVE-2026-23359)
  * [CVE-2026-23368](https://nvd.nist.gov/vuln/detail/CVE-2026-23368)
  * [CVE-2026-23381](https://nvd.nist.gov/vuln/detail/CVE-2026-23381)
  * [CVE-2026-23388](https://nvd.nist.gov/vuln/detail/CVE-2026-23388)
  * [CVE-2026-23391](https://nvd.nist.gov/vuln/detail/CVE-2026-23391)
  * [CVE-2026-23392](https://nvd.nist.gov/vuln/detail/CVE-2026-23392)
  * [CVE-2026-23397](https://nvd.nist.gov/vuln/detail/CVE-2026-23397)
  * [CVE-2026-23398](https://nvd.nist.gov/vuln/detail/CVE-2026-23398)
  * [CVE-2026-23401](https://nvd.nist.gov/vuln/detail/CVE-2026-23401)
  * [CVE-2026-23403](https://nvd.nist.gov/vuln/detail/CVE-2026-23403)
  * [CVE-2026-23404](https://nvd.nist.gov/vuln/detail/CVE-2026-23404)
  * [CVE-2026-23405](https://nvd.nist.gov/vuln/detail/CVE-2026-23405)
  * [CVE-2026-23406](https://nvd.nist.gov/vuln/detail/CVE-2026-23406)
  * [CVE-2026-23407](https://nvd.nist.gov/vuln/detail/CVE-2026-23407)
  * [CVE-2026-23408](https://nvd.nist.gov/vuln/detail/CVE-2026-23408)
  * [CVE-2026-23409](https://nvd.nist.gov/vuln/detail/CVE-2026-23409)
  * [CVE-2026-23410](https://nvd.nist.gov/vuln/detail/CVE-2026-23410)
  * [CVE-2026-23411](https://nvd.nist.gov/vuln/detail/CVE-2026-23411)
  * [CVE-2026-23439](https://nvd.nist.gov/vuln/detail/CVE-2026-23439)
  * [CVE-2026-23449](https://nvd.nist.gov/vuln/detail/CVE-2026-23449)
  * [CVE-2026-23452](https://nvd.nist.gov/vuln/detail/CVE-2026-23452)
  * [CVE-2026-23455](https://nvd.nist.gov/vuln/detail/CVE-2026-23455)
  * [CVE-2026-23456](https://nvd.nist.gov/vuln/detail/CVE-2026-23456)
  * [CVE-2026-23457](https://nvd.nist.gov/vuln/detail/CVE-2026-23457)
  * [CVE-2026-23458](https://nvd.nist.gov/vuln/detail/CVE-2026-23458)
  * [CVE-2026-23479](https://nvd.nist.gov/vuln/detail/CVE-2026-23479)
  * [CVE-2026-23631](https://nvd.nist.gov/vuln/detail/CVE-2026-23631)
  * [CVE-2026-25243](https://nvd.nist.gov/vuln/detail/CVE-2026-25243)
  * [CVE-2026-25588](https://nvd.nist.gov/vuln/detail/CVE-2026-25588)
  * [CVE-2026-25589](https://nvd.nist.gov/vuln/detail/CVE-2026-25589)
  * [CVE-2026-27135](https://nvd.nist.gov/vuln/detail/CVE-2026-27135)
  * [CVE-2026-27448](https://nvd.nist.gov/vuln/detail/CVE-2026-27448)
  * [CVE-2026-27459](https://nvd.nist.gov/vuln/detail/CVE-2026-27459)
  * [CVE-2026-28387](https://nvd.nist.gov/vuln/detail/CVE-2026-28387)
  * [CVE-2026-28388](https://nvd.nist.gov/vuln/detail/CVE-2026-28388)
  * [CVE-2026-28389](https://nvd.nist.gov/vuln/detail/CVE-2026-28389)
  * [CVE-2026-28390](https://nvd.nist.gov/vuln/detail/CVE-2026-28390)
  * [CVE-2026-29111](https://nvd.nist.gov/vuln/detail/CVE-2026-29111)
  * [CVE-2026-31392](https://nvd.nist.gov/vuln/detail/CVE-2026-31392)
  * [CVE-2026-31400](https://nvd.nist.gov/vuln/detail/CVE-2026-31400)
  * [CVE-2026-31402](https://nvd.nist.gov/vuln/detail/CVE-2026-31402)
  * [CVE-2026-31403](https://nvd.nist.gov/vuln/detail/CVE-2026-31403)
  * [CVE-2026-31414](https://nvd.nist.gov/vuln/detail/CVE-2026-31414)
  * [CVE-2026-31415](https://nvd.nist.gov/vuln/detail/CVE-2026-31415)
  * [CVE-2026-31416](https://nvd.nist.gov/vuln/detail/CVE-2026-31416)
  * [CVE-2026-31418](https://nvd.nist.gov/vuln/detail/CVE-2026-31418)
  * [CVE-2026-31421](https://nvd.nist.gov/vuln/detail/CVE-2026-31421)
  * [CVE-2026-31423](https://nvd.nist.gov/vuln/detail/CVE-2026-31423)
  * [CVE-2026-31424](https://nvd.nist.gov/vuln/detail/CVE-2026-31424)
  * [CVE-2026-31427](https://nvd.nist.gov/vuln/detail/CVE-2026-31427)
  * [CVE-2026-31428](https://nvd.nist.gov/vuln/detail/CVE-2026-31428)
  * [CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
  * [CVE-2026-31446](https://nvd.nist.gov/vuln/detail/CVE-2026-31446)
  * [CVE-2026-31447](https://nvd.nist.gov/vuln/detail/CVE-2026-31447)
  * [CVE-2026-31452](https://nvd.nist.gov/vuln/detail/CVE-2026-31452)
  * [CVE-2026-31453](https://nvd.nist.gov/vuln/detail/CVE-2026-31453)
  * [CVE-2026-31454](https://nvd.nist.gov/vuln/detail/CVE-2026-31454)
  * [CVE-2026-31466](https://nvd.nist.gov/vuln/detail/CVE-2026-31466)
  * [CVE-2026-31469](https://nvd.nist.gov/vuln/detail/CVE-2026-31469)
  * [CVE-2026-31496](https://nvd.nist.gov/vuln/detail/CVE-2026-31496)
  * [CVE-2026-31503](https://nvd.nist.gov/vuln/detail/CVE-2026-31503)
  * [CVE-2026-31504](https://nvd.nist.gov/vuln/detail/CVE-2026-31504)
  * [CVE-2026-31515](https://nvd.nist.gov/vuln/detail/CVE-2026-31515)
  * [CVE-2026-31521](https://nvd.nist.gov/vuln/detail/CVE-2026-31521)
  * [CVE-2026-31523](https://nvd.nist.gov/vuln/detail/CVE-2026-31523)
  * [CVE-2026-31528](https://nvd.nist.gov/vuln/detail/CVE-2026-31528)
  * [CVE-2026-31546](https://nvd.nist.gov/vuln/detail/CVE-2026-31546)
  * [CVE-2026-31555](https://nvd.nist.gov/vuln/detail/CVE-2026-31555)
  * [CVE-2026-31664](https://nvd.nist.gov/vuln/detail/CVE-2026-31664)
  * [CVE-2026-31665](https://nvd.nist.gov/vuln/detail/CVE-2026-31665)
  * [CVE-2026-31667](https://nvd.nist.gov/vuln/detail/CVE-2026-31667)
  * [CVE-2026-31671](https://nvd.nist.gov/vuln/detail/CVE-2026-31671)
  * [CVE-2026-31675](https://nvd.nist.gov/vuln/detail/CVE-2026-31675)
  * [CVE-2026-31680](https://nvd.nist.gov/vuln/detail/CVE-2026-31680)
  * [CVE-2026-31682](https://nvd.nist.gov/vuln/detail/CVE-2026-31682)
  * [CVE-2026-31738](https://nvd.nist.gov/vuln/detail/CVE-2026-31738)
  * [CVE-2026-31752](https://nvd.nist.gov/vuln/detail/CVE-2026-31752)
  * [CVE-2026-31789](https://nvd.nist.gov/vuln/detail/CVE-2026-31789)
  * [CVE-2026-31790](https://nvd.nist.gov/vuln/detail/CVE-2026-31790)
  * [CVE-2026-32597](https://nvd.nist.gov/vuln/detail/CVE-2026-32597)
  * [CVE-2026-33416](https://nvd.nist.gov/vuln/detail/CVE-2026-33416)
  * [CVE-2026-33636](https://nvd.nist.gov/vuln/detail/CVE-2026-33636)
  * [CVE-2026-33997](https://nvd.nist.gov/vuln/detail/CVE-2026-33997)
  * [CVE-2026-34040](https://nvd.nist.gov/vuln/detail/CVE-2026-34040)
  * [CVE-2026-3783](https://nvd.nist.gov/vuln/detail/CVE-2026-3783)
  * [CVE-2026-40225](https://nvd.nist.gov/vuln/detail/CVE-2026-40225)
  * [CVE-2026-40226](https://nvd.nist.gov/vuln/detail/CVE-2026-40226)
  * [CVE-2026-4105](https://nvd.nist.gov/vuln/detail/CVE-2026-4105)
  * [CVE-2026-43013](https://nvd.nist.gov/vuln/detail/CVE-2026-43013)
  * [CVE-2026-43026](https://nvd.nist.gov/vuln/detail/CVE-2026-43026)
  * [CVE-2026-43027](https://nvd.nist.gov/vuln/detail/CVE-2026-43027)
  * [CVE-2026-43028](https://nvd.nist.gov/vuln/detail/CVE-2026-43028)
  * [CVE-2026-43030](https://nvd.nist.gov/vuln/detail/CVE-2026-43030)
  * [CVE-2026-43035](https://nvd.nist.gov/vuln/detail/CVE-2026-43035)
  * [CVE-2026-43037](https://nvd.nist.gov/vuln/detail/CVE-2026-43037)
  * [CVE-2026-43038](https://nvd.nist.gov/vuln/detail/CVE-2026-43038)
  * [CVE-2026-43040](https://nvd.nist.gov/vuln/detail/CVE-2026-43040)
  * [CVE-2026-43043](https://nvd.nist.gov/vuln/detail/CVE-2026-43043)
  * [CVE-2026-43054](https://nvd.nist.gov/vuln/detail/CVE-2026-43054)
  * [CVE-2026-43066](https://nvd.nist.gov/vuln/detail/CVE-2026-43066)
  * [CVE-2026-43071](https://nvd.nist.gov/vuln/detail/CVE-2026-43071)
  * [CVE-2026-43077](https://nvd.nist.gov/vuln/detail/CVE-2026-43077)
  * [CVE-2026-43079](https://nvd.nist.gov/vuln/detail/CVE-2026-43079)
  * [CVE-2026-43085](https://nvd.nist.gov/vuln/detail/CVE-2026-43085)
  * [CVE-2026-43086](https://nvd.nist.gov/vuln/detail/CVE-2026-43086)
  * [CVE-2026-43089](https://nvd.nist.gov/vuln/detail/CVE-2026-43089)
  * [CVE-2026-43099](https://nvd.nist.gov/vuln/detail/CVE-2026-43099)
  * [CVE-2026-43112](https://nvd.nist.gov/vuln/detail/CVE-2026-43112)
  * [CVE-2026-43130](https://nvd.nist.gov/vuln/detail/CVE-2026-43130)
  * [CVE-2026-43139](https://nvd.nist.gov/vuln/detail/CVE-2026-43139)
  * [CVE-2026-43163](https://nvd.nist.gov/vuln/detail/CVE-2026-43163)
  * [CVE-2026-43187](https://nvd.nist.gov/vuln/detail/CVE-2026-43187)
  * [CVE-2026-43190](https://nvd.nist.gov/vuln/detail/CVE-2026-43190)
  * [CVE-2026-43215](https://nvd.nist.gov/vuln/detail/CVE-2026-43215)
  * [CVE-2026-43233](https://nvd.nist.gov/vuln/detail/CVE-2026-43233)
  * [CVE-2026-43240](https://nvd.nist.gov/vuln/detail/CVE-2026-43240)
  * [CVE-2026-43266](https://nvd.nist.gov/vuln/detail/CVE-2026-43266)
  * [CVE-2026-43278](https://nvd.nist.gov/vuln/detail/CVE-2026-43278)
  * [CVE-2026-43281](https://nvd.nist.gov/vuln/detail/CVE-2026-43281)
  * [CVE-2026-43284](https://nvd.nist.gov/vuln/detail/CVE-2026-43284)
  * [CVE-2026-43483](https://nvd.nist.gov/vuln/detail/CVE-2026-43483)



2025

  * [CVE-2025-10148](https://nvd.nist.gov/vuln/detail/CVE-2025-10148)
  * [CVE-2025-10966](https://nvd.nist.gov/vuln/detail/CVE-2025-10966)
  * [CVE-2025-13034](https://nvd.nist.gov/vuln/detail/CVE-2025-13034)
  * [CVE-2025-13601](https://nvd.nist.gov/vuln/detail/CVE-2025-13601)
  * [CVE-2025-13837](https://nvd.nist.gov/vuln/detail/CVE-2025-13837)
  * [CVE-2025-14017](https://nvd.nist.gov/vuln/detail/CVE-2025-14017)
  * [CVE-2025-14087](https://nvd.nist.gov/vuln/detail/CVE-2025-14087)
  * [CVE-2025-14512](https://nvd.nist.gov/vuln/detail/CVE-2025-14512)
  * [CVE-2025-14524](https://nvd.nist.gov/vuln/detail/CVE-2025-14524)
  * [CVE-2025-14819](https://nvd.nist.gov/vuln/detail/CVE-2025-14819)
  * [CVE-2025-14831](https://nvd.nist.gov/vuln/detail/CVE-2025-14831)
  * [CVE-2025-15079](https://nvd.nist.gov/vuln/detail/CVE-2025-15079)
  * [CVE-2025-22026](https://nvd.nist.gov/vuln/detail/CVE-2025-22026)
  * [CVE-2025-3576](https://nvd.nist.gov/vuln/detail/CVE-2025-3576)
  * [CVE-2025-37920](https://nvd.nist.gov/vuln/detail/CVE-2025-37920)
  * [CVE-2025-37980](https://nvd.nist.gov/vuln/detail/CVE-2025-37980)
  * [CVE-2025-38162](https://nvd.nist.gov/vuln/detail/CVE-2025-38162)
  * [CVE-2025-38201](https://nvd.nist.gov/vuln/detail/CVE-2025-38201)
  * [CVE-2025-38232](https://nvd.nist.gov/vuln/detail/CVE-2025-38232)
  * [CVE-2025-38248](https://nvd.nist.gov/vuln/detail/CVE-2025-38248)
  * [CVE-2025-38591](https://nvd.nist.gov/vuln/detail/CVE-2025-38591)
  * [CVE-2025-39764](https://nvd.nist.gov/vuln/detail/CVE-2025-39764)
  * [CVE-2025-40135](https://nvd.nist.gov/vuln/detail/CVE-2025-40135)
  * [CVE-2025-40251](https://nvd.nist.gov/vuln/detail/CVE-2025-40251)
  * [CVE-2025-6075](https://nvd.nist.gov/vuln/detail/CVE-2025-6075)
  * [CVE-2025-60753](https://nvd.nist.gov/vuln/detail/CVE-2025-60753)
  * [CVE-2025-68206](https://nvd.nist.gov/vuln/detail/CVE-2025-68206)
  * [CVE-2025-68239](https://nvd.nist.gov/vuln/detail/CVE-2025-68239)
  * [CVE-2025-68265](https://nvd.nist.gov/vuln/detail/CVE-2025-68265)
  * [CVE-2025-68725](https://nvd.nist.gov/vuln/detail/CVE-2025-68725)
  * [CVE-2025-68816](https://nvd.nist.gov/vuln/detail/CVE-2025-68816)
  * [CVE-2025-69644](https://nvd.nist.gov/vuln/detail/CVE-2025-69644)
  * [CVE-2025-69647](https://nvd.nist.gov/vuln/detail/CVE-2025-69647)
  * [CVE-2025-69648](https://nvd.nist.gov/vuln/detail/CVE-2025-69648)
  * [CVE-2025-71089](https://nvd.nist.gov/vuln/detail/CVE-2025-71089)
  * [CVE-2025-71118](https://nvd.nist.gov/vuln/detail/CVE-2025-71118)
  * [CVE-2025-71125](https://nvd.nist.gov/vuln/detail/CVE-2025-71125)
  * [CVE-2025-71161](https://nvd.nist.gov/vuln/detail/CVE-2025-71161)
  * [CVE-2025-71295](https://nvd.nist.gov/vuln/detail/CVE-2025-71295)
  * [CVE-2025-9820](https://nvd.nist.gov/vuln/detail/CVE-2025-9820)



2024

  * [CVE-2024-26822](https://nvd.nist.gov/vuln/detail/CVE-2024-26822)
  * [CVE-2024-37891](https://nvd.nist.gov/vuln/detail/CVE-2024-37891)



2023

  * [CVE-2023-53421](https://nvd.nist.gov/vuln/detail/CVE-2023-53421)
  * [CVE-2023-54285](https://nvd.nist.gov/vuln/detail/CVE-2023-54285)



## 20260220_00_01

**Date released** | **Release type**  
---|---  
2026-03-16 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and sidecar processes to address the CVEs listed in Security patches.   
All Redis instances | Set the Redis host OS version to [cos-121-18867-381-1](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-381-1_).  
  
### Security patches

2026

  * [CVE-2026-22796](https://nvd.nist.gov/vuln/detail/CVE-2026-22796)
  * [CVE-2026-22795](https://nvd.nist.gov/vuln/detail/CVE-2026-22795)



2025

  * [CVE-2025-9232](https://nvd.nist.gov/vuln/detail/CVE-2025-9232)
  * [CVE-2025-9230](https://nvd.nist.gov/vuln/detail/CVE-2025-9230)
  * [CVE-2025-8058](https://nvd.nist.gov/vuln/detail/CVE-2025-8058)
  * [CVE-2025-69421](https://nvd.nist.gov/vuln/detail/CVE-2025-69421)
  * [CVE-2025-69420](https://nvd.nist.gov/vuln/detail/CVE-2025-69420)
  * [CVE-2025-69419](https://nvd.nist.gov/vuln/detail/CVE-2025-69419)
  * [CVE-2025-69418](https://nvd.nist.gov/vuln/detail/CVE-2025-69418)
  * [CVE-2025-68973](https://nvd.nist.gov/vuln/detail/CVE-2025-68973)
  * [CVE-2025-68160](https://nvd.nist.gov/vuln/detail/CVE-2025-68160)
  * [CVE-2025-68156](https://nvd.nist.gov/vuln/detail/CVE-2025-68156)
  * [CVE-2025-68119](https://nvd.nist.gov/vuln/detail/CVE-2025-68119)
  * [CVE-2025-6395](https://nvd.nist.gov/vuln/detail/CVE-2025-6395)
  * [CVE-2025-61731](https://nvd.nist.gov/vuln/detail/CVE-2025-61731)
  * [CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
  * [CVE-2025-61728](https://nvd.nist.gov/vuln/detail/CVE-2025-61728)
  * [CVE-2025-61726](https://nvd.nist.gov/vuln/detail/CVE-2025-61726)
  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725)
  * [CVE-2025-6020](https://nvd.nist.gov/vuln/detail/CVE-2025-6020)
  * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187)
  * [CVE-2025-4802](https://nvd.nist.gov/vuln/detail/CVE-2025-4802)
  * [CVE-2025-47907](https://nvd.nist.gov/vuln/detail/CVE-2025-47907)
  * [CVE-2025-40909](https://nvd.nist.gov/vuln/detail/CVE-2025-40909)
  * [CVE-2025-32990](https://nvd.nist.gov/vuln/detail/CVE-2025-32990)
  * [CVE-2025-32989](https://nvd.nist.gov/vuln/detail/CVE-2025-32989)
  * [CVE-2025-32988](https://nvd.nist.gov/vuln/detail/CVE-2025-32988)
  * [CVE-2025-31115](https://nvd.nist.gov/vuln/detail/CVE-2025-31115)
  * [CVE-2025-22871](https://nvd.nist.gov/vuln/detail/CVE-2025-22871)
  * [CVE-2025-15467](https://nvd.nist.gov/vuln/detail/CVE-2025-15467)
  * [CVE-2025-1390](https://nvd.nist.gov/vuln/detail/CVE-2025-1390)
  * [CVE-2025-13151](https://nvd.nist.gov/vuln/detail/CVE-2025-13151)
  * [CVE-2025-10158](https://nvd.nist.gov/vuln/detail/CVE-2025-10158)



2024

  * [CVE-2024-9143](https://nvd.nist.gov/vuln/detail/CVE-2024-9143)
  * [CVE-2024-56406](https://nvd.nist.gov/vuln/detail/CVE-2024-56406)
  * [CVE-2024-45339](https://nvd.nist.gov/vuln/detail/CVE-2024-45339)
  * [CVE-2024-28835](https://nvd.nist.gov/vuln/detail/CVE-2024-28835)
  * [CVE-2024-24790](https://nvd.nist.gov/vuln/detail/CVE-2024-24790)
  * [CVE-2024-24784](https://nvd.nist.gov/vuln/detail/CVE-2024-24784)
  * [CVE-2024-22365](https://nvd.nist.gov/vuln/detail/CVE-2024-22365)
  * [CVE-2024-12133](https://nvd.nist.gov/vuln/detail/CVE-2024-12133)



2023

  * [CVE-2023-6992](https://nvd.nist.gov/vuln/detail/CVE-2023-6992)
  * [CVE-2023-6129](https://nvd.nist.gov/vuln/detail/CVE-2023-6129)
  * [CVE-2023-31484](https://nvd.nist.gov/vuln/detail/CVE-2023-31484)
  * [CVE-2023-24531](https://nvd.nist.gov/vuln/detail/CVE-2023-24531)



2021

  * [CVE-2021-24032](https://nvd.nist.gov/vuln/detail/CVE-2021-24032)
  * [CVE-2021-24031](https://nvd.nist.gov/vuln/detail/CVE-2021-24031)



## 20251110_01_00

**Date released** | **Release type**  
---|---  
2025-11-18 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances that have versions earlier than 7.0. | Contains an update to the envoy proxy agent to address the CVE listed in Security patches.  
  
### Security patches

2025

  * [CVE-2025-62409](https://nvd.nist.gov/vuln/detail/CVE-2025-62409)



## 20251007_00_00

**Date released** | **Release type**  
---|---  
2025-10-08 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh all versions of the Redis binary to address the CVEs listed in Security patches.  
  
### Security patches

2025

  * [CVE-2025-46817](https://nvd.nist.gov/vuln/detail/CVE-2025-46817)
  * [CVE-2025-46818](https://nvd.nist.gov/vuln/detail/CVE-2025-46818)
  * [CVE-2025-46819](https://nvd.nist.gov/vuln/detail/CVE-2025-46819)
  * [CVE-2025-49844](https://nvd.nist.gov/vuln/detail/CVE-2025-49844)



## 20250806_01_00

**Date released** | **Release type**  
---|---  
2025-08-29 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and the Redis binary to address the CVEs listed in Security patches.  
  
### Security patches

2025

  * [CVE-2025-1215](https://nvd.nist.gov/vuln/detail/CVE-2025-1215)
  * [CVE-2025-6965](https://nvd.nist.gov/vuln/detail/CVE-2025-6965)
  * [CVE-2025-22134](https://nvd.nist.gov/vuln/detail/CVE-2025-22134)
  * [CVE-2025-23266](https://nvd.nist.gov/vuln/detail/CVE-2025-23266)
  * [CVE-2025-24014](https://nvd.nist.gov/vuln/detail/CVE-2025-24014)
  * [CVE-2025-26603](https://nvd.nist.gov/vuln/detail/CVE-2025-26603)
  * [CVE-2025-27423](https://nvd.nist.gov/vuln/detail/CVE-2025-27423)
  * [CVE-2025-29768](https://nvd.nist.gov/vuln/detail/CVE-2025-29768)
  * [CVE-2025-32023](https://nvd.nist.gov/vuln/detail/CVE-2025-32023)
  * [CVE-2025-32462](https://nvd.nist.gov/vuln/detail/CVE-2025-32462)
  * [CVE-2025-32463](https://nvd.nist.gov/vuln/detail/CVE-2025-32463)



2024

  * [CVE-2024-5742](https://nvd.nist.gov/vuln/detail/CVE-2024-5742)
  * [CVE-2024-26130](https://nvd.nist.gov/vuln/detail/CVE-2024-26130)



## 20250701_00_01

**Date released** | **Release type**  
---|---  
2025-07-23 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and sidecar processes to address the CVEs listed in Security patches.  
  
### Security patches

2025

  * [CVE-2025-1181](https://nvd.nist.gov/vuln/detail/CVE-2025-1181)
  * [CVE-2025-1365](https://nvd.nist.gov/vuln/detail/CVE-2025-1365)
  * [CVE-2025-1371](https://nvd.nist.gov/vuln/detail/CVE-2025-1371)
  * [CVE-2025-1372](https://nvd.nist.gov/vuln/detail/CVE-2025-1372)
  * [CVE-2025-1377](https://nvd.nist.gov/vuln/detail/CVE-2025-1377)
  * [CVE-2025-1632](https://nvd.nist.gov/vuln/detail/CVE-2025-1632)
  * [CVE-2025-3198](https://nvd.nist.gov/vuln/detail/CVE-2025-3198)
  * [CVE-2025-4598](https://nvd.nist.gov/vuln/detail/CVE-2025-4598)
  * [CVE-2025-5914](https://nvd.nist.gov/vuln/detail/CVE-2025-5914)
  * [CVE-2025-6965](https://nvd.nist.gov/vuln/detail/CVE-2025-6965)
  * [CVE-2025-21726](https://nvd.nist.gov/vuln/detail/CVE-2025-21726)
  * [CVE-2025-21727](https://nvd.nist.gov/vuln/detail/CVE-2025-21727)
  * [CVE-2025-21756](https://nvd.nist.gov/vuln/detail/CVE-2025-21756)
  * [CVE-2025-21760](https://nvd.nist.gov/vuln/detail/CVE-2025-21760)
  * [CVE-2025-21762](https://nvd.nist.gov/vuln/detail/CVE-2025-21762)
  * [CVE-2025-21763](https://nvd.nist.gov/vuln/detail/CVE-2025-21763)
  * [CVE-2025-21764](https://nvd.nist.gov/vuln/detail/CVE-2025-21764)
  * [CVE-2025-21796](https://nvd.nist.gov/vuln/detail/CVE-2025-21796)
  * [CVE-2025-21812](https://nvd.nist.gov/vuln/detail/CVE-2025-21812)
  * [CVE-2025-21853](https://nvd.nist.gov/vuln/detail/CVE-2025-21853)
  * [CVE-2025-21867](https://nvd.nist.gov/vuln/detail/CVE-2025-21867)
  * [CVE-2025-21887](https://nvd.nist.gov/vuln/detail/CVE-2025-21887)
  * [CVE-2025-21891](https://nvd.nist.gov/vuln/detail/CVE-2025-21891)
  * [CVE-2025-21898](https://nvd.nist.gov/vuln/detail/CVE-2025-21898)
  * [CVE-2025-21919](https://nvd.nist.gov/vuln/detail/CVE-2025-21919)
  * [CVE-2025-21920](https://nvd.nist.gov/vuln/detail/CVE-2025-21920)
  * [CVE-2025-21922](https://nvd.nist.gov/vuln/detail/CVE-2025-21922)
  * [CVE-2025-21959](https://nvd.nist.gov/vuln/detail/CVE-2025-21959)
  * [CVE-2025-21962](https://nvd.nist.gov/vuln/detail/CVE-2025-21962)
  * [CVE-2025-21963](https://nvd.nist.gov/vuln/detail/CVE-2025-21963)
  * [CVE-2025-21964](https://nvd.nist.gov/vuln/detail/CVE-2025-21964)
  * [CVE-2025-21980](https://nvd.nist.gov/vuln/detail/CVE-2025-21980)
  * [CVE-2025-21997](https://nvd.nist.gov/vuln/detail/CVE-2025-21997)
  * [CVE-2025-21999](https://nvd.nist.gov/vuln/detail/CVE-2025-21999)
  * [CVE-2025-22005](https://nvd.nist.gov/vuln/detail/CVE-2025-22005)
  * [CVE-2025-22035](https://nvd.nist.gov/vuln/detail/CVE-2025-22035)
  * [CVE-2025-22056](https://nvd.nist.gov/vuln/detail/CVE-2025-22056)
  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868)
  * [CVE-2025-22870](https://nvd.nist.gov/vuln/detail/CVE-2025-22870)
  * [CVE-2025-29087](https://nvd.nist.gov/vuln/detail/CVE-2025-29087)
  * [CVE-2025-32414](https://nvd.nist.gov/vuln/detail/CVE-2025-32414)
  * [CVE-2025-32415](https://nvd.nist.gov/vuln/detail/CVE-2025-32415)
  * [CVE-2025-32728](https://nvd.nist.gov/vuln/detail/CVE-2025-32728)
  * [CVE-2025-37785](https://nvd.nist.gov/vuln/detail/CVE-2025-37785)
  * [CVE-2025-46836](https://nvd.nist.gov/vuln/detail/CVE-2025-46836)
  * [CVE-2025-47273](https://nvd.nist.gov/vuln/detail/CVE-2025-47273)
  * [CVE-2025-48060](https://nvd.nist.gov/vuln/detail/CVE-2025-48060)



2024

  * [CVE-2024-0553](https://nvd.nist.gov/vuln/detail/CVE-2024-0553)
  * [CVE-2024-0727](https://nvd.nist.gov/vuln/detail/CVE-2024-0727)
  * [CVE-2024-2398](https://nvd.nist.gov/vuln/detail/CVE-2024-2398)
  * [CVE-2024-2511](https://nvd.nist.gov/vuln/detail/CVE-2024-2511)
  * [CVE-2024-2961](https://nvd.nist.gov/vuln/detail/CVE-2024-2961)
  * [CVE-2024-4741](https://nvd.nist.gov/vuln/detail/CVE-2024-4741)
  * [CVE-2024-5535](https://nvd.nist.gov/vuln/detail/CVE-2024-5535)
  * [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254)
  * [CVE-2024-8176](https://nvd.nist.gov/vuln/detail/CVE-2024-8176)
  * [CVE-2024-23653](https://nvd.nist.gov/vuln/detail/CVE-2024-23653)
  * [CVE-2024-24786](https://nvd.nist.gov/vuln/detail/CVE-2024-24786)
  * [CVE-2024-26462](https://nvd.nist.gov/vuln/detail/CVE-2024-26462)
  * [CVE-2024-26739](https://nvd.nist.gov/vuln/detail/CVE-2024-26739)
  * [CVE-2024-26783](https://nvd.nist.gov/vuln/detail/CVE-2024-26783)
  * [CVE-2024-27280](https://nvd.nist.gov/vuln/detail/CVE-2024-27280)
  * [CVE-2024-27281](https://nvd.nist.gov/vuln/detail/CVE-2024-27281)
  * [CVE-2024-27282](https://nvd.nist.gov/vuln/detail/CVE-2024-27282)
  * [CVE-2024-28085](https://nvd.nist.gov/vuln/detail/CVE-2024-28085)
  * [CVE-2024-33599](https://nvd.nist.gov/vuln/detail/CVE-2024-33599)
  * [CVE-2024-33600](https://nvd.nist.gov/vuln/detail/CVE-2024-33600)
  * [CVE-2024-33601](https://nvd.nist.gov/vuln/detail/CVE-2024-33601)
  * [CVE-2024-33602](https://nvd.nist.gov/vuln/detail/CVE-2024-33602)
  * [CVE-2024-35866](https://nvd.nist.gov/vuln/detail/CVE-2024-35866)
  * [CVE-2024-36903](https://nvd.nist.gov/vuln/detail/CVE-2024-36903)
  * [CVE-2024-36927](https://nvd.nist.gov/vuln/detail/CVE-2024-36927)
  * [CVE-2024-37370](https://nvd.nist.gov/vuln/detail/CVE-2024-37370)
  * [CVE-2024-37371](https://nvd.nist.gov/vuln/detail/CVE-2024-37371)
  * [CVE-2024-40635](https://nvd.nist.gov/vuln/detail/CVE-2024-40635)
  * [CVE-2024-43840](https://nvd.nist.gov/vuln/detail/CVE-2024-43840)
  * [CVE-2024-48615](https://nvd.nist.gov/vuln/detail/CVE-2024-48615)
  * [CVE-2024-50063](https://nvd.nist.gov/vuln/detail/CVE-2024-50063)
  * [CVE-2024-50349](https://nvd.nist.gov/vuln/detail/CVE-2024-50349)
  * [CVE-2024-52006](https://nvd.nist.gov/vuln/detail/CVE-2024-52006)
  * [CVE-2024-53427](https://nvd.nist.gov/vuln/detail/CVE-2024-53427)
  * [CVE-2024-56549](https://nvd.nist.gov/vuln/detail/CVE-2024-56549)
  * [CVE-2024-57977](https://nvd.nist.gov/vuln/detail/CVE-2024-57977)
  * [CVE-2024-57979](https://nvd.nist.gov/vuln/detail/CVE-2024-57979)
  * [CVE-2024-58083](https://nvd.nist.gov/vuln/detail/CVE-2024-58083)



2023

  * [CVE-2023-1428](https://nvd.nist.gov/vuln/detail/CVE-2023-1428)
  * [CVE-2023-4039](https://nvd.nist.gov/vuln/detail/CVE-2023-4039)
  * [CVE-2023-4641](https://nvd.nist.gov/vuln/detail/CVE-2023-4641)
  * [CVE-2023-4806](https://nvd.nist.gov/vuln/detail/CVE-2023-4806)
  * [CVE-2023-4813](https://nvd.nist.gov/vuln/detail/CVE-2023-4813)
  * [CVE-2023-5678](https://nvd.nist.gov/vuln/detail/CVE-2023-5678)
  * [CVE-2023-7008](https://nvd.nist.gov/vuln/detail/CVE-2023-7008)
  * [CVE-2023-28320](https://nvd.nist.gov/vuln/detail/CVE-2023-28320)
  * [CVE-2023-29383](https://nvd.nist.gov/vuln/detail/CVE-2023-29383)
  * [CVE-2023-32731](https://nvd.nist.gov/vuln/detail/CVE-2023-32731)
  * [CVE-2023-32732](https://nvd.nist.gov/vuln/detail/CVE-2023-32732)
  * [CVE-2023-33953](https://nvd.nist.gov/vuln/detail/CVE-2023-33953)
  * [CVE-2023-39804](https://nvd.nist.gov/vuln/detail/CVE-2023-39804)
  * [CVE-2023-45288](https://nvd.nist.gov/vuln/detail/CVE-2023-45288)
  * [CVE-2023-45918](https://nvd.nist.gov/vuln/detail/CVE-2023-45918)
  * [CVE-2023-50387](https://nvd.nist.gov/vuln/detail/CVE-2023-50387)
  * [CVE-2023-50868](https://nvd.nist.gov/vuln/detail/CVE-2023-50868)
  * [CVE-2023-52927](https://nvd.nist.gov/vuln/detail/CVE-2023-52927)



2022

  * [CVE-2022-1304](https://nvd.nist.gov/vuln/detail/CVE-2022-1304)
  * [CVE-2022-3171](https://nvd.nist.gov/vuln/detail/CVE-2022-3171)
  * [CVE-2022-4415](https://nvd.nist.gov/vuln/detail/CVE-2022-4415)
  * [CVE-2022-24795](https://nvd.nist.gov/vuln/detail/CVE-2022-24795)
  * [CVE-2022-48303](https://nvd.nist.gov/vuln/detail/CVE-2022-48303)



2021

  * [CVE-2021-3997](https://nvd.nist.gov/vuln/detail/CVE-2021-3997)
  * [CVE-2021-20193](https://nvd.nist.gov/vuln/detail/CVE-2021-20193)
  * [CVE-2021-22569](https://nvd.nist.gov/vuln/detail/CVE-2021-22569)
  * [CVE-2021-22922](https://nvd.nist.gov/vuln/detail/CVE-2021-22922)
  * [CVE-2021-22923](https://nvd.nist.gov/vuln/detail/CVE-2021-22923)
  * [CVE-2021-31799](https://nvd.nist.gov/vuln/detail/CVE-2021-31799)
  * [CVE-2021-32740](https://nvd.nist.gov/vuln/detail/CVE-2021-32740)
  * [CVE-2021-33560](https://nvd.nist.gov/vuln/detail/CVE-2021-33560)
  * [CVE-2021-36084](https://nvd.nist.gov/vuln/detail/CVE-2021-36084)
  * [CVE-2021-36085](https://nvd.nist.gov/vuln/detail/CVE-2021-36085)
  * [CVE-2021-36086](https://nvd.nist.gov/vuln/detail/CVE-2021-36086)
  * [CVE-2021-36087](https://nvd.nist.gov/vuln/detail/CVE-2021-36087)
  * [CVE-2021-37600](https://nvd.nist.gov/vuln/detail/CVE-2021-37600)
  * [CVE-2021-41817](https://nvd.nist.gov/vuln/detail/CVE-2021-41817)



2020

  * [CVE-2020-1751](https://nvd.nist.gov/vuln/detail/CVE-2020-1751)
  * [CVE-2020-8130](https://nvd.nist.gov/vuln/detail/CVE-2020-8130)
  * [CVE-2020-10663](https://nvd.nist.gov/vuln/detail/CVE-2020-10663)
  * [CVE-2020-13529](https://nvd.nist.gov/vuln/detail/CVE-2020-13529)
  * [CVE-2020-14155](https://nvd.nist.gov/vuln/detail/CVE-2020-14155)
  * [CVE-2020-16156](https://nvd.nist.gov/vuln/detail/CVE-2020-16156)
  * [CVE-2020-19909](https://nvd.nist.gov/vuln/detail/CVE-2020-19909)
  * [CVE-2020-25613](https://nvd.nist.gov/vuln/detail/CVE-2020-25613)



2019

  * [CVE-2019-3843](https://nvd.nist.gov/vuln/detail/CVE-2019-3843)
  * [CVE-2019-3844](https://nvd.nist.gov/vuln/detail/CVE-2019-3844)
  * [CVE-2019-8457](https://nvd.nist.gov/vuln/detail/CVE-2019-8457)
  * [CVE-2019-9893](https://nvd.nist.gov/vuln/detail/CVE-2019-9893)
  * [CVE-2019-9923](https://nvd.nist.gov/vuln/detail/CVE-2019-9923)
  * [CVE-2019-12290](https://nvd.nist.gov/vuln/detail/CVE-2019-12290)
  * [CVE-2019-13627](https://nvd.nist.gov/vuln/detail/CVE-2019-13627)
  * [CVE-2019-14855](https://nvd.nist.gov/vuln/detail/CVE-2019-14855)
  * [CVE-2019-15847](https://nvd.nist.gov/vuln/detail/CVE-2019-15847)
  * [CVE-2019-17543](https://nvd.nist.gov/vuln/detail/CVE-2019-17543)
  * [CVE-2019-18276](https://nvd.nist.gov/vuln/detail/CVE-2019-18276)
  * [CVE-2019-19882](https://nvd.nist.gov/vuln/detail/CVE-2019-19882)
  * [CVE-2019-20386](https://nvd.nist.gov/vuln/detail/CVE-2019-20386)
  * [CVE-2019-20838](https://nvd.nist.gov/vuln/detail/CVE-2019-20838)



2018

  * [CVE-2018-7169](https://nvd.nist.gov/vuln/detail/CVE-2018-7169)
  * [CVE-2018-12886](https://nvd.nist.gov/vuln/detail/CVE-2018-12886)
  * [CVE-2018-18405](https://nvd.nist.gov/vuln/detail/CVE-2018-18405)
  * [CVE-2018-1000654](https://nvd.nist.gov/vuln/detail/CVE-2018-1000654)



2017

  * [CVE-2017-7245](https://nvd.nist.gov/vuln/detail/CVE-2017-7245)
  * [CVE-2017-7246](https://nvd.nist.gov/vuln/detail/CVE-2017-7246)
  * [CVE-2017-11164](https://nvd.nist.gov/vuln/detail/CVE-2017-11164)
  * [CVE-2017-16231](https://nvd.nist.gov/vuln/detail/CVE-2017-16231)



2016

  * [CVE-2016-1585](https://nvd.nist.gov/vuln/detail/CVE-2016-1585)



2013

  * [CVE-2013-4235](https://nvd.nist.gov/vuln/detail/CVE-2013-4235)



2007

  * [CVE-2007-2379](https://nvd.nist.gov/vuln/detail/CVE-2007-2379)



## 20250326_00_00

**Date released** | **Release type**  
---|---  
2025-03-26 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version and the Redis binary to address the CVEs listed in Security patches.  
  
### Security patches

2025

  * [CVE-2025-0395](https://nvd.nist.gov/vuln/detail/CVE-2025-0395)
  * [CVE-2025-0840](https://nvd.nist.gov/vuln/detail/CVE-2025-0840)
  * [CVE-2025-21631](https://nvd.nist.gov/vuln/detail/CVE-2025-21631)
  * [CVE-2025-21665](https://nvd.nist.gov/vuln/detail/CVE-2025-21665)
  * [CVE-2025-21666](https://nvd.nist.gov/vuln/detail/CVE-2025-21666)
  * [CVE-2025-21667](https://nvd.nist.gov/vuln/detail/CVE-2025-21667)
  * [CVE-2025-21669](https://nvd.nist.gov/vuln/detail/CVE-2025-21669)
  * [CVE-2025-21671](https://nvd.nist.gov/vuln/detail/CVE-2025-21671)
  * [CVE-2025-21683](https://nvd.nist.gov/vuln/detail/CVE-2025-21683)
  * [CVE-2025-21690](https://nvd.nist.gov/vuln/detail/CVE-2025-21690)
  * [CVE-2025-21716](https://nvd.nist.gov/vuln/detail/CVE-2025-21716)
  * [CVE-2025-21745](https://nvd.nist.gov/vuln/detail/CVE-2025-21745)
  * [CVE-2025-21779](https://nvd.nist.gov/vuln/detail/CVE-2025-21779)
  * [CVE-2025-21785](https://nvd.nist.gov/vuln/detail/CVE-2025-21785)
  * [CVE-2025-21791](https://nvd.nist.gov/vuln/detail/CVE-2025-21791)
  * [CVE-2025-21814](https://nvd.nist.gov/vuln/detail/CVE-2025-21814)
  * [CVE-2025-21844](https://nvd.nist.gov/vuln/detail/CVE-2025-21844)
  * [CVE-2025-21846](https://nvd.nist.gov/vuln/detail/CVE-2025-21846)
  * [CVE-2025-21858](https://nvd.nist.gov/vuln/detail/CVE-2025-21858)
  * [CVE-2025-21864](https://nvd.nist.gov/vuln/detail/CVE-2025-21864)
  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869)
  * [CVE-2025-26465](https://nvd.nist.gov/vuln/detail/CVE-2025-26465)
  * [CVE-2025-26466](https://nvd.nist.gov/vuln/detail/CVE-2025-26466)
  * [CVE-2025-27113](https://nvd.nist.gov/vuln/detail/CVE-2025-27113)



2024

  * [CVE-2024-0131](https://nvd.nist.gov/vuln/detail/CVE-2024-0131)
  * [CVE-2024-0134](https://nvd.nist.gov/vuln/detail/CVE-2024-0134)
  * [CVE-2024-0147](https://nvd.nist.gov/vuln/detail/CVE-2024-0147)
  * [CVE-2024-0149](https://nvd.nist.gov/vuln/detail/CVE-2024-0149)
  * [CVE-2024-0150](https://nvd.nist.gov/vuln/detail/CVE-2024-0150)
  * [CVE-2024-9287](https://nvd.nist.gov/vuln/detail/CVE-2024-9287)
  * [CVE-2024-9341](https://nvd.nist.gov/vuln/detail/CVE-2024-9341)
  * [CVE-2024-9407](https://nvd.nist.gov/vuln/detail/CVE-2024-9407)
  * [CVE-2024-9675](https://nvd.nist.gov/vuln/detail/CVE-2024-9675)
  * [CVE-2024-9681](https://nvd.nist.gov/vuln/detail/CVE-2024-9681)
  * [CVE-2024-10524](https://nvd.nist.gov/vuln/detail/CVE-2024-10524)
  * [CVE-2024-11053](https://nvd.nist.gov/vuln/detail/CVE-2024-11053)
  * [CVE-2024-12084](https://nvd.nist.gov/vuln/detail/CVE-2024-12084)
  * [CVE-2024-12085](https://nvd.nist.gov/vuln/detail/CVE-2024-12085)
  * [CVE-2024-12086](https://nvd.nist.gov/vuln/detail/CVE-2024-12086)
  * [CVE-2024-12087](https://nvd.nist.gov/vuln/detail/CVE-2024-12087)
  * [CVE-2024-12088](https://nvd.nist.gov/vuln/detail/CVE-2024-12088)
  * [CVE-2024-12747](https://nvd.nist.gov/vuln/detail/CVE-2024-12747)
  * [CVE-2024-13176](https://nvd.nist.gov/vuln/detail/CVE-2024-13176)
  * [CVE-2024-23653](https://nvd.nist.gov/vuln/detail/CVE-2024-23653)
  * [CVE-2024-26982](https://nvd.nist.gov/vuln/detail/CVE-2024-26982)
  * [CVE-2024-40896](https://nvd.nist.gov/vuln/detail/CVE-2024-40896)
  * [CVE-2024-40945](https://nvd.nist.gov/vuln/detail/CVE-2024-40945)
  * [CVE-2024-45306](https://nvd.nist.gov/vuln/detail/CVE-2024-45306)
  * [CVE-2024-45310](https://nvd.nist.gov/vuln/detail/CVE-2024-45310)
  * [CVE-2024-45337](https://nvd.nist.gov/vuln/detail/CVE-2024-45337)
  * [CVE-2024-46981](https://nvd.nist.gov/vuln/detail/CVE-2024-46981)
  * [CVE-2024-47745](https://nvd.nist.gov/vuln/detail/CVE-2024-47745)
  * [CVE-2024-47814](https://nvd.nist.gov/vuln/detail/CVE-2024-47814)
  * [CVE-2024-49861](https://nvd.nist.gov/vuln/detail/CVE-2024-49861)
  * [CVE-2024-49878](https://nvd.nist.gov/vuln/detail/CVE-2024-49878)
  * [CVE-2024-49926](https://nvd.nist.gov/vuln/detail/CVE-2024-49926)
  * [CVE-2024-49927](https://nvd.nist.gov/vuln/detail/CVE-2024-49927)
  * [CVE-2024-49946](https://nvd.nist.gov/vuln/detail/CVE-2024-49946)
  * [CVE-2024-49948](https://nvd.nist.gov/vuln/detail/CVE-2024-49948)
  * [CVE-2024-49949](https://nvd.nist.gov/vuln/detail/CVE-2024-49949)
  * [CVE-2024-49952](https://nvd.nist.gov/vuln/detail/CVE-2024-49952)
  * [CVE-2024-49954](https://nvd.nist.gov/vuln/detail/CVE-2024-49954)
  * [CVE-2024-49959](https://nvd.nist.gov/vuln/detail/CVE-2024-49959)
  * [CVE-2024-49994](https://nvd.nist.gov/vuln/detail/CVE-2024-49994)
  * [CVE-2024-49996](https://nvd.nist.gov/vuln/detail/CVE-2024-49996)
  * [CVE-2024-50010](https://nvd.nist.gov/vuln/detail/CVE-2024-50010)
  * [CVE-2024-50014](https://nvd.nist.gov/vuln/detail/CVE-2024-50014)
  * [CVE-2024-50024](https://nvd.nist.gov/vuln/detail/CVE-2024-50024)
  * [CVE-2024-50036](https://nvd.nist.gov/vuln/detail/CVE-2024-50036)
  * [CVE-2024-50038](https://nvd.nist.gov/vuln/detail/CVE-2024-50038)
  * [CVE-2024-50047](https://nvd.nist.gov/vuln/detail/CVE-2024-50047)
  * [CVE-2024-50055](https://nvd.nist.gov/vuln/detail/CVE-2024-50055)
  * [CVE-2024-50060](https://nvd.nist.gov/vuln/detail/CVE-2024-50060)
  * [CVE-2024-50072](https://nvd.nist.gov/vuln/detail/CVE-2024-50072)
  * [CVE-2024-50082](https://nvd.nist.gov/vuln/detail/CVE-2024-50082)
  * [CVE-2024-50083](https://nvd.nist.gov/vuln/detail/CVE-2024-50083)
  * [CVE-2024-50095](https://nvd.nist.gov/vuln/detail/CVE-2024-50095)
  * [CVE-2024-50099](https://nvd.nist.gov/vuln/detail/CVE-2024-50099)
  * [CVE-2024-50101](https://nvd.nist.gov/vuln/detail/CVE-2024-50101)
  * [CVE-2024-50110](https://nvd.nist.gov/vuln/detail/CVE-2024-50110)
  * [CVE-2024-50115](https://nvd.nist.gov/vuln/detail/CVE-2024-50115)
  * [CVE-2024-50131](https://nvd.nist.gov/vuln/detail/CVE-2024-50131)
  * [CVE-2024-50138](https://nvd.nist.gov/vuln/detail/CVE-2024-50138)
  * [CVE-2024-50141](https://nvd.nist.gov/vuln/detail/CVE-2024-50141)
  * [CVE-2024-50142](https://nvd.nist.gov/vuln/detail/CVE-2024-50142)
  * [CVE-2024-50143](https://nvd.nist.gov/vuln/detail/CVE-2024-50143)
  * [CVE-2024-50147](https://nvd.nist.gov/vuln/detail/CVE-2024-50147)
  * [CVE-2024-50151](https://nvd.nist.gov/vuln/detail/CVE-2024-50151)
  * [CVE-2024-50153](https://nvd.nist.gov/vuln/detail/CVE-2024-50153)
  * [CVE-2024-50154](https://nvd.nist.gov/vuln/detail/CVE-2024-50154)
  * [CVE-2024-50162](https://nvd.nist.gov/vuln/detail/CVE-2024-50162)
  * [CVE-2024-50163](https://nvd.nist.gov/vuln/detail/CVE-2024-50163)
  * [CVE-2024-50164](https://nvd.nist.gov/vuln/detail/CVE-2024-50164)
  * [CVE-2024-50186](https://nvd.nist.gov/vuln/detail/CVE-2024-50186)
  * [CVE-2024-50191](https://nvd.nist.gov/vuln/detail/CVE-2024-50191)
  * [CVE-2024-50192](https://nvd.nist.gov/vuln/detail/CVE-2024-50192)
  * [CVE-2024-50194](https://nvd.nist.gov/vuln/detail/CVE-2024-50194)
  * [CVE-2024-50195](https://nvd.nist.gov/vuln/detail/CVE-2024-50195)
  * [CVE-2024-50215](https://nvd.nist.gov/vuln/detail/CVE-2024-50215)
  * [CVE-2024-50228](https://nvd.nist.gov/vuln/detail/CVE-2024-50228)
  * [CVE-2024-50251](https://nvd.nist.gov/vuln/detail/CVE-2024-50251)
  * [CVE-2024-50256](https://nvd.nist.gov/vuln/detail/CVE-2024-50256)
  * [CVE-2024-50257](https://nvd.nist.gov/vuln/detail/CVE-2024-50257)
  * [CVE-2024-50262](https://nvd.nist.gov/vuln/detail/CVE-2024-50262)
  * [CVE-2024-50271](https://nvd.nist.gov/vuln/detail/CVE-2024-50271)
  * [CVE-2024-50272](https://nvd.nist.gov/vuln/detail/CVE-2024-50272)
  * [CVE-2024-50278](https://nvd.nist.gov/vuln/detail/CVE-2024-50278)
  * [CVE-2024-50279](https://nvd.nist.gov/vuln/detail/CVE-2024-50279)
  * [CVE-2024-50304](https://nvd.nist.gov/vuln/detail/CVE-2024-50304)
  * [CVE-2024-50602](https://nvd.nist.gov/vuln/detail/CVE-2024-50602)
  * [CVE-2024-53042](https://nvd.nist.gov/vuln/detail/CVE-2024-53042)
  * [CVE-2024-53052](https://nvd.nist.gov/vuln/detail/CVE-2024-53052)
  * [CVE-2024-53054](https://nvd.nist.gov/vuln/detail/CVE-2024-53054)
  * [CVE-2024-53066](https://nvd.nist.gov/vuln/detail/CVE-2024-53066)
  * [CVE-2024-53082](https://nvd.nist.gov/vuln/detail/CVE-2024-53082)
  * [CVE-2024-53093](https://nvd.nist.gov/vuln/detail/CVE-2024-53093)
  * [CVE-2024-53096](https://nvd.nist.gov/vuln/detail/CVE-2024-53096)
  * [CVE-2024-53099](https://nvd.nist.gov/vuln/detail/CVE-2024-53099)
  * [CVE-2024-53100](https://nvd.nist.gov/vuln/detail/CVE-2024-53100)
  * [CVE-2024-53113](https://nvd.nist.gov/vuln/detail/CVE-2024-53113)
  * [CVE-2024-53119](https://nvd.nist.gov/vuln/detail/CVE-2024-53119)
  * [CVE-2024-53121](https://nvd.nist.gov/vuln/detail/CVE-2024-53121)
  * [CVE-2024-53124](https://nvd.nist.gov/vuln/detail/CVE-2024-53124)
  * [CVE-2024-53128](https://nvd.nist.gov/vuln/detail/CVE-2024-53128)
  * [CVE-2024-53135](https://nvd.nist.gov/vuln/detail/CVE-2024-53135)
  * [CVE-2024-53136](https://nvd.nist.gov/vuln/detail/CVE-2024-53136)
  * [CVE-2024-53140](https://nvd.nist.gov/vuln/detail/CVE-2024-53140)
  * [CVE-2024-53166](https://nvd.nist.gov/vuln/detail/CVE-2024-53166)
  * [CVE-2024-53170](https://nvd.nist.gov/vuln/detail/CVE-2024-53170)
  * [CVE-2024-53589](https://nvd.nist.gov/vuln/detail/CVE-2024-53589)
  * [CVE-2024-53869](https://nvd.nist.gov/vuln/detail/CVE-2024-53869)
  * [CVE-2024-56664](https://nvd.nist.gov/vuln/detail/CVE-2024-56664)
  * [CVE-2024-57841](https://nvd.nist.gov/vuln/detail/CVE-2024-57841)
  * [CVE-2024-57890](https://nvd.nist.gov/vuln/detail/CVE-2024-57890)
  * [CVE-2024-57949](https://nvd.nist.gov/vuln/detail/CVE-2024-57949)
  * [CVE-2024-57951](https://nvd.nist.gov/vuln/detail/CVE-2024-57951)
  * [CVE-2024-57996](https://nvd.nist.gov/vuln/detail/CVE-2024-57996)
  * [CVE-2024-58005](https://nvd.nist.gov/vuln/detail/CVE-2024-58005)
  * [CVE-2024-58017](https://nvd.nist.gov/vuln/detail/CVE-2024-58017)



2023

  * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)
  * [CVE-2023-45288](https://nvd.nist.gov/vuln/detail/CVE-2023-45288)



## 20241107_00_00

**Date released** | **Release type**  
---|---  
2024-12-17 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version to address the CVEs listed in Security patches.  
  
### Security patches

2024

  * [CVE-2024-0126](https://nvd.nist.gov/vuln/detail/CVE-2024-0126)
  * [CVE-2024-0132](https://nvd.nist.gov/vuln/detail/CVE-2024-0132)
  * [CVE-2024-0133](https://nvd.nist.gov/vuln/detail/CVE-2024-0133)
  * [CVE-2024-2511](https://nvd.nist.gov/vuln/detail/CVE-2024-2511)
  * [CVE-2024-4603](https://nvd.nist.gov/vuln/detail/CVE-2024-4603)
  * [CVE-2024-4741](https://nvd.nist.gov/vuln/detail/CVE-2024-4741)
  * [CVE-2024-5535](https://nvd.nist.gov/vuln/detail/CVE-2024-5535)
  * [CVE-2024-6119](https://nvd.nist.gov/vuln/detail/CVE-2024-6119)
  * [CVE-2024-6197](https://nvd.nist.gov/vuln/detail/CVE-2024-6197)
  * [CVE-2024-6232](https://nvd.nist.gov/vuln/detail/CVE-2024-6232)
  * [CVE-2024-6345](https://nvd.nist.gov/vuln/detail/CVE-2024-6345)
  * [CVE-2024-6602](https://nvd.nist.gov/vuln/detail/CVE-2024-6602)
  * [CVE-2024-7264](https://nvd.nist.gov/vuln/detail/CVE-2024-7264)
  * [CVE-2024-7592](https://nvd.nist.gov/vuln/detail/CVE-2024-7592)
  * [CVE-2024-31227](https://nvd.nist.gov/vuln/detail/CVE-2024-31227)
  * [CVE-2024-31228](https://nvd.nist.gov/vuln/detail/CVE-2024-31228)
  * [CVE-2024-31449](https://nvd.nist.gov/vuln/detail/CVE-2024-31449)
  * [CVE-2024-37370](https://nvd.nist.gov/vuln/detail/CVE-2024-37370)
  * [CVE-2024-37371](https://nvd.nist.gov/vuln/detail/CVE-2024-37371)
  * [CVE-2024-38632](https://nvd.nist.gov/vuln/detail/CVE-2024-38632)
  * [CVE-2024-39472](https://nvd.nist.gov/vuln/detail/CVE-2024-39472)
  * [CVE-2024-41012](https://nvd.nist.gov/vuln/detail/CVE-2024-41012)
  * [CVE-2024-41057](https://nvd.nist.gov/vuln/detail/CVE-2024-41057)
  * [CVE-2024-41058](https://nvd.nist.gov/vuln/detail/CVE-2024-41058)
  * [CVE-2024-41073](https://nvd.nist.gov/vuln/detail/CVE-2024-41073)
  * [CVE-2024-41098](https://nvd.nist.gov/vuln/detail/CVE-2024-41098)
  * [CVE-2024-41957](https://nvd.nist.gov/vuln/detail/CVE-2024-41957)
  * [CVE-2024-41965](https://nvd.nist.gov/vuln/detail/CVE-2024-41965)
  * [CVE-2024-42268](https://nvd.nist.gov/vuln/detail/CVE-2024-42268)
  * [CVE-2024-42269](https://nvd.nist.gov/vuln/detail/CVE-2024-42269)
  * [CVE-2024-42270](https://nvd.nist.gov/vuln/detail/CVE-2024-42270)
  * [CVE-2024-42283](https://nvd.nist.gov/vuln/detail/CVE-2024-42283)
  * [CVE-2024-42285](https://nvd.nist.gov/vuln/detail/CVE-2024-42285)
  * [CVE-2024-42302](https://nvd.nist.gov/vuln/detail/CVE-2024-42302)
  * [CVE-2024-42307](https://nvd.nist.gov/vuln/detail/CVE-2024-42307)
  * [CVE-2024-42316](https://nvd.nist.gov/vuln/detail/CVE-2024-42316)
  * [CVE-2024-43817](https://nvd.nist.gov/vuln/detail/CVE-2024-43817)
  * [CVE-2024-43828](https://nvd.nist.gov/vuln/detail/CVE-2024-43828)
  * [CVE-2024-43837](https://nvd.nist.gov/vuln/detail/CVE-2024-43837)
  * [CVE-2024-43853](https://nvd.nist.gov/vuln/detail/CVE-2024-43853)
  * [CVE-2024-43854](https://nvd.nist.gov/vuln/detail/CVE-2024-43854)
  * [CVE-2024-43855](https://nvd.nist.gov/vuln/detail/CVE-2024-43855)
  * [CVE-2024-43856](https://nvd.nist.gov/vuln/detail/CVE-2024-43856)
  * [CVE-2024-43871](https://nvd.nist.gov/vuln/detail/CVE-2024-43871)
  * [CVE-2024-43873](https://nvd.nist.gov/vuln/detail/CVE-2024-43873)
  * [CVE-2024-43882](https://nvd.nist.gov/vuln/detail/CVE-2024-43882)
  * [CVE-2024-43889](https://nvd.nist.gov/vuln/detail/CVE-2024-43889)
  * [CVE-2024-43892](https://nvd.nist.gov/vuln/detail/CVE-2024-43892)
  * [CVE-2024-43893](https://nvd.nist.gov/vuln/detail/CVE-2024-43893)
  * [CVE-2024-43914](https://nvd.nist.gov/vuln/detail/CVE-2024-43914)
  * [CVE-2024-44940](https://nvd.nist.gov/vuln/detail/CVE-2024-44940)
  * [CVE-2024-44944](https://nvd.nist.gov/vuln/detail/CVE-2024-44944)
  * [CVE-2024-44947](https://nvd.nist.gov/vuln/detail/CVE-2024-44947)
  * [CVE-2024-44952](https://nvd.nist.gov/vuln/detail/CVE-2024-44952)
  * [CVE-2024-44958](https://nvd.nist.gov/vuln/detail/CVE-2024-44958)
  * [CVE-2024-44965](https://nvd.nist.gov/vuln/detail/CVE-2024-44965)
  * [CVE-2024-44970](https://nvd.nist.gov/vuln/detail/CVE-2024-44970)
  * [CVE-2024-44983](https://nvd.nist.gov/vuln/detail/CVE-2024-44983)
  * [CVE-2024-44985](https://nvd.nist.gov/vuln/detail/CVE-2024-44985)
  * [CVE-2024-44986](https://nvd.nist.gov/vuln/detail/CVE-2024-44986)
  * [CVE-2024-44987](https://nvd.nist.gov/vuln/detail/CVE-2024-44987)
  * [CVE-2024-44989](https://nvd.nist.gov/vuln/detail/CVE-2024-44989)
  * [CVE-2024-44990](https://nvd.nist.gov/vuln/detail/CVE-2024-44990)
  * [CVE-2024-45000](https://nvd.nist.gov/vuln/detail/CVE-2024-45000)
  * [CVE-2024-45003](https://nvd.nist.gov/vuln/detail/CVE-2024-45003)
  * [CVE-2024-45018](https://nvd.nist.gov/vuln/detail/CVE-2024-45018)
  * [CVE-2024-45021](https://nvd.nist.gov/vuln/detail/CVE-2024-45021)
  * [CVE-2024-45022](https://nvd.nist.gov/vuln/detail/CVE-2024-45022)
  * [CVE-2024-45025](https://nvd.nist.gov/vuln/detail/CVE-2024-45025)
  * [CVE-2024-45490](https://nvd.nist.gov/vuln/detail/CVE-2024-45490)
  * [CVE-2024-45491](https://nvd.nist.gov/vuln/detail/CVE-2024-45491)
  * [CVE-2024-45492](https://nvd.nist.gov/vuln/detail/CVE-2024-45492)
  * [CVE-2024-46679](https://nvd.nist.gov/vuln/detail/CVE-2024-46679)
  * [CVE-2024-46686](https://nvd.nist.gov/vuln/detail/CVE-2024-46686)
  * [CVE-2024-46721](https://nvd.nist.gov/vuln/detail/CVE-2024-46721)
  * [CVE-2024-46737](https://nvd.nist.gov/vuln/detail/CVE-2024-46737)
  * [CVE-2024-46738](https://nvd.nist.gov/vuln/detail/CVE-2024-46738)
  * [CVE-2024-46743](https://nvd.nist.gov/vuln/detail/CVE-2024-46743)
  * [CVE-2024-46744](https://nvd.nist.gov/vuln/detail/CVE-2024-46744)
  * [CVE-2024-46750](https://nvd.nist.gov/vuln/detail/CVE-2024-46750)
  * [CVE-2024-46763](https://nvd.nist.gov/vuln/detail/CVE-2024-46763)
  * [CVE-2024-46800](https://nvd.nist.gov/vuln/detail/CVE-2024-46800)
  * [CVE-2024-46829](https://nvd.nist.gov/vuln/detail/CVE-2024-46829)
  * [CVE-2024-46848](https://nvd.nist.gov/vuln/detail/CVE-2024-46848)
  * [CVE-2024-46855](https://nvd.nist.gov/vuln/detail/CVE-2024-46855)
  * [CVE-2024-47678](https://nvd.nist.gov/vuln/detail/CVE-2024-47678)
  * [CVE-2024-47679](https://nvd.nist.gov/vuln/detail/CVE-2024-47679)
  * [CVE-2024-47682](https://nvd.nist.gov/vuln/detail/CVE-2024-47682)
  * [CVE-2024-47684](https://nvd.nist.gov/vuln/detail/CVE-2024-47684)
  * [CVE-2024-47685](https://nvd.nist.gov/vuln/detail/CVE-2024-47685)
  * [CVE-2024-47692](https://nvd.nist.gov/vuln/detail/CVE-2024-47692)
  * [CVE-2024-47693](https://nvd.nist.gov/vuln/detail/CVE-2024-47693)
  * [CVE-2024-47696](https://nvd.nist.gov/vuln/detail/CVE-2024-47696)
  * [CVE-2024-47701](https://nvd.nist.gov/vuln/detail/CVE-2024-47701)
  * [CVE-2024-47705](https://nvd.nist.gov/vuln/detail/CVE-2024-47705)
  * [CVE-2024-47706](https://nvd.nist.gov/vuln/detail/CVE-2024-47706)
  * [CVE-2024-47707](https://nvd.nist.gov/vuln/detail/CVE-2024-47707)
  * [CVE-2024-47710](https://nvd.nist.gov/vuln/detail/CVE-2024-47710)
  * [CVE-2024-47727](https://nvd.nist.gov/vuln/detail/CVE-2024-47727)
  * [CVE-2024-47728](https://nvd.nist.gov/vuln/detail/CVE-2024-47728)
  * [CVE-2024-47734](https://nvd.nist.gov/vuln/detail/CVE-2024-47734)
  * [CVE-2024-47737](https://nvd.nist.gov/vuln/detail/CVE-2024-47737)
  * [CVE-2024-47739](https://nvd.nist.gov/vuln/detail/CVE-2024-47739)
  * [CVE-2024-47742](https://nvd.nist.gov/vuln/detail/CVE-2024-47742)
  * [CVE-2024-47743](https://nvd.nist.gov/vuln/detail/CVE-2024-47743)
  * [CVE-2024-48957](https://nvd.nist.gov/vuln/detail/CVE-2024-48957)
  * [CVE-2024-48958](https://nvd.nist.gov/vuln/detail/CVE-2024-48958)
  * [CVE-2024-49850](https://nvd.nist.gov/vuln/detail/CVE-2024-49850)
  * [CVE-2024-49851](https://nvd.nist.gov/vuln/detail/CVE-2024-49851)
  * [CVE-2024-49858](https://nvd.nist.gov/vuln/detail/CVE-2024-49858)
  * [CVE-2024-49860](https://nvd.nist.gov/vuln/detail/CVE-2024-49860)
  * [CVE-2024-49870](https://nvd.nist.gov/vuln/detail/CVE-2024-49870)
  * [CVE-2024-49875](https://nvd.nist.gov/vuln/detail/CVE-2024-49875)
  * [CVE-2024-49881](https://nvd.nist.gov/vuln/detail/CVE-2024-49881)
  * [CVE-2024-49883](https://nvd.nist.gov/vuln/detail/CVE-2024-49883)
  * [CVE-2024-49884](https://nvd.nist.gov/vuln/detail/CVE-2024-49884)
  * [CVE-2024-49889](https://nvd.nist.gov/vuln/detail/CVE-2024-49889)
  * [CVE-2024-49936](https://nvd.nist.gov/vuln/detail/CVE-2024-49936)
  * [CVE-2024-49967](https://nvd.nist.gov/vuln/detail/CVE-2024-49967)
  * [CVE-2024-49975](https://nvd.nist.gov/vuln/detail/CVE-2024-49975)
  * [CVE-2024-49978](https://nvd.nist.gov/vuln/detail/CVE-2024-49978)
  * [CVE-2024-49983](https://nvd.nist.gov/vuln/detail/CVE-2024-49983)
  * [CVE-2024-49993](https://nvd.nist.gov/vuln/detail/CVE-2024-49993)
  * [CVE-2024-50000](https://nvd.nist.gov/vuln/detail/CVE-2024-50000)
  * [CVE-2024-50001](https://nvd.nist.gov/vuln/detail/CVE-2024-50001)
  * [CVE-2024-50002](https://nvd.nist.gov/vuln/detail/CVE-2024-50002)
  * [CVE-2024-50006](https://nvd.nist.gov/vuln/detail/CVE-2024-50006)
  * [CVE-2024-50015](https://nvd.nist.gov/vuln/detail/CVE-2024-50015)
  * [CVE-2024-50019](https://nvd.nist.gov/vuln/detail/CVE-2024-50019)
  * [CVE-2024-50033](https://nvd.nist.gov/vuln/detail/CVE-2024-50033)
  * [CVE-2024-50035](https://nvd.nist.gov/vuln/detail/CVE-2024-50035)
  * [CVE-2024-50039](https://nvd.nist.gov/vuln/detail/CVE-2024-50039)
  * [CVE-2024-50045](https://nvd.nist.gov/vuln/detail/CVE-2024-50045)
  * [CVE-2024-50046](https://nvd.nist.gov/vuln/detail/CVE-2024-50046)



2023

  * [CVE-2023-7256](https://nvd.nist.gov/vuln/detail/CVE-2023-7256)
  * [CVE-2023-27043](https://nvd.nist.gov/vuln/detail/CVE-2023-27043)
  * [CVE-2023-52889](https://nvd.nist.gov/vuln/detail/CVE-2023-52889)



## 20240724_00_00

**Date released** | **Release type**  
---|---  
2024-08-21 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis host OS version to address the CVEs listed in Security patches.  
  
### Security patches

2024

  * [CVE-2024-0607](https://nvd.nist.gov/vuln/detail/CVE-2024-0607)
  * [CVE-2024-0853](https://nvd.nist.gov/vuln/detail/CVE-2024-0853)
  * [CVE-2024-2511](https://nvd.nist.gov/vuln/detail/CVE-2024-2511)
  * [CVE-2024-4741](https://nvd.nist.gov/vuln/detail/CVE-2024-4741)
  * [CVE-2024-6197](https://nvd.nist.gov/vuln/detail/CVE-2024-6197)
  * [CVE-2024-6345](https://nvd.nist.gov/vuln/detail/CVE-2024-6345)
  * [CVE-2024-6387](https://nvd.nist.gov/vuln/detail/CVE-2024-6387)



## 20240503_00_00

**Date released** | **Release type**  
---|---  
2024-05-10 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | Refresh the Redis Debian OS version to address the CVEs listed in Security patches.  
  
### Security patches

2023

  * [CVE-2023-3576](https://nvd.nist.gov/vuln/detail/CVE-2023-3576)
  * [CVE-2023-39804](https://nvd.nist.gov/vuln/detail/CVE-2023-39804)
  * [CVE-2023-40745](https://nvd.nist.gov/vuln/detail/CVE-2023-40745)
  * [CVE-2023-41175](https://nvd.nist.gov/vuln/detail/CVE-2023-41175)
  * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)
  * [CVE-2023-46218](https://nvd.nist.gov/vuln/detail/CVE-2023-46218)
  * [CVE-2023-47038](https://nvd.nist.gov/vuln/detail/CVE-2023-47038)



2022

  * [CVE-2022-48303](https://nvd.nist.gov/vuln/detail/CVE-2022-48303)



## 20240411_00_00

**Date released** | **Release type**  
---|---  
2024-04-12 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
Redis 7.2 instances only | Add reliability and performance improvements for [vector search](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search).  
  
## 20240328_00_00

**Date released** | **Release type**  
---|---  
2024-03-28 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
Redis 7.2 instances only | Add reliability and performance improvements for [vector search](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search).  
  
## 20240220_00_00

**Date released** | **Release type**  
---|---  
2024-02-20 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | 

  * Set the Redis host OS version to [cos-105-17412-294-10](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105#cos-105-17412-294-10_).
  * General reliability improvements.

  
  
### Security patches

2024

  * [CVE-2024-0193](https://nvd.nist.gov/vuln/detail/CVE-2024-0193)
  * [CVE-2024-0584](https://nvd.nist.gov/vuln/detail/CVE-2024-0584)
  * [CVE-2024-0646](https://nvd.nist.gov/vuln/detail/CVE-2024-0646)
  * [CVE-2024-1085](https://nvd.nist.gov/vuln/detail/CVE-2024-1085)
  * [CVE-2024-1086](https://nvd.nist.gov/vuln/detail/CVE-2024-1086)
  * [CVE-2024-22195](https://nvd.nist.gov/vuln/detail/CVE-2024-22195)



2023

  * [CVE-2023-1077](https://nvd.nist.gov/vuln/detail/CVE-2023-1077)
  * [CVE-2023-2156](https://nvd.nist.gov/vuln/detail/CVE-2023-2156)
  * [CVE-2023-4733](https://nvd.nist.gov/vuln/detail/CVE-2023-4733)
  * [CVE-2023-4734](https://nvd.nist.gov/vuln/detail/CVE-2023-4734)
  * [CVE-2023-4735](https://nvd.nist.gov/vuln/detail/CVE-2023-4735)
  * [CVE-2023-4736](https://nvd.nist.gov/vuln/detail/CVE-2023-4736)
  * [CVE-2023-4738](https://nvd.nist.gov/vuln/detail/CVE-2023-4738)
  * [CVE-2023-4750](https://nvd.nist.gov/vuln/detail/CVE-2023-4750)
  * [CVE-2023-4752](https://nvd.nist.gov/vuln/detail/CVE-2023-4752)
  * [CVE-2023-4781](https://nvd.nist.gov/vuln/detail/CVE-2023-4781)
  * [CVE-2023-5344](https://nvd.nist.gov/vuln/detail/CVE-2023-5344)
  * [CVE-2023-5441](https://nvd.nist.gov/vuln/detail/CVE-2023-5441)
  * [CVE-2023-5535](https://nvd.nist.gov/vuln/detail/CVE-2023-5535)
  * [CVE-2023-5678](https://nvd.nist.gov/vuln/detail/CVE-2023-5678)
  * [CVE-2023-5717](https://nvd.nist.gov/vuln/detail/CVE-2023-5717)
  * [CVE-2023-6040](https://nvd.nist.gov/vuln/detail/CVE-2023-6040)
  * [CVE-2023-6111](https://nvd.nist.gov/vuln/detail/CVE-2023-6111)
  * [CVE-2023-6531](https://nvd.nist.gov/vuln/detail/CVE-2023-6531)
  * [CVE-2023-6817](https://nvd.nist.gov/vuln/detail/CVE-2023-6817)
  * [CVE-2023-6915](https://nvd.nist.gov/vuln/detail/CVE-2023-6915)
  * [CVE-2023-6931](https://nvd.nist.gov/vuln/detail/CVE-2023-6931)
  * [CVE-2023-6932](https://nvd.nist.gov/vuln/detail/CVE-2023-6932)
  * [CVE-2023-7104](https://nvd.nist.gov/vuln/detail/CVE-2023-7104)
  * [CVE-2023-7192](https://nvd.nist.gov/vuln/detail/CVE-2023-7192)
  * [CVE-2023-31022](https://nvd.nist.gov/vuln/detail/CVE-2023-31022)
  * [CVE-2023-34324](https://nvd.nist.gov/vuln/detail/CVE-2023-34324)
  * [CVE-2023-34969](https://nvd.nist.gov/vuln/detail/CVE-2023-34969)
  * [CVE-2023-35945](https://nvd.nist.gov/vuln/detail/CVE-2023-35945)
  * [CVE-2023-40546](https://nvd.nist.gov/vuln/detail/CVE-2023-40546)
  * [CVE-2023-40547](https://nvd.nist.gov/vuln/detail/CVE-2023-40547)
  * [CVE-2023-40548](https://nvd.nist.gov/vuln/detail/CVE-2023-40548)
  * [CVE-2023-40549](https://nvd.nist.gov/vuln/detail/CVE-2023-40549)
  * [CVE-2023-40550](https://nvd.nist.gov/vuln/detail/CVE-2023-40550)
  * [CVE-2023-40551](https://nvd.nist.gov/vuln/detail/CVE-2023-40551)
  * [CVE-2023-42754](https://nvd.nist.gov/vuln/detail/CVE-2023-42754)
  * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)
  * [CVE-2023-45322](https://nvd.nist.gov/vuln/detail/CVE-2023-45322)
  * [CVE-2023-46218](https://nvd.nist.gov/vuln/detail/CVE-2023-46218)
  * [CVE-2023-46813](https://nvd.nist.gov/vuln/detail/CVE-2023-46813)
  * [CVE-2023-46838](https://nvd.nist.gov/vuln/detail/CVE-2023-46838)
  * [CVE-2023-46862](https://nvd.nist.gov/vuln/detail/CVE-2023-46862)
  * [CVE-2023-48795](https://nvd.nist.gov/vuln/detail/CVE-2023-48795)
  * [CVE-2023-51384](https://nvd.nist.gov/vuln/detail/CVE-2023-51384)
  * [CVE-2023-51385](https://nvd.nist.gov/vuln/detail/CVE-2023-51385)
  * [CVE-2023-52071](https://nvd.nist.gov/vuln/detail/CVE-2023-52071)



2022

  * [CVE-2022-42010](https://nvd.nist.gov/vuln/detail/CVE-2022-42010)
  * [CVE-2022-42011](https://nvd.nist.gov/vuln/detail/CVE-2022-42011)
  * [CVE-2022-42012](https://nvd.nist.gov/vuln/detail/CVE-2022-42012)



## 20231114_00_00

**Date released** | **Release type**  
---|---  
2023-11-14 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
Redis 6.x instances only | Set the OSS Redis patch version to [6.2.14](https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES).  
Redis 7.0 instances only | Set the OSS Redis patch version to [7.0.14](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES).  
All Redis instances |  Set the Redis host OS version to [cos-105-17412-226-10](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105#cos-105-17412-226-10_). General reliability improvements.  
  
### Security patches

2023

  * [CVE-2023-0361](https://nvd.nist.gov/vuln/detail/CVE-2023-0361)
  * [CVE-2023-2163](https://nvd.nist.gov/vuln/detail/CVE-2023-2163)
  * [CVE-2023-3117](https://nvd.nist.gov/vuln/detail/CVE-2023-3117)
  * [CVE-2023-3338](https://nvd.nist.gov/vuln/detail/CVE-2023-3338)
  * [CVE-2023-4015](https://nvd.nist.gov/vuln/detail/CVE-2023-4015)
  * [CVE-2023-4016](https://nvd.nist.gov/vuln/detail/CVE-2023-4016)
  * [CVE-2023-4206](https://nvd.nist.gov/vuln/detail/CVE-2023-4206)
  * [CVE-2023-4207](https://nvd.nist.gov/vuln/detail/CVE-2023-4207)
  * [CVE-2023-4208](https://nvd.nist.gov/vuln/detail/CVE-2023-4208)
  * [CVE-2023-4244](https://nvd.nist.gov/vuln/detail/CVE-2023-4244)
  * [CVE-2023-4569](https://nvd.nist.gov/vuln/detail/CVE-2023-4569)
  * [CVE-2023-4622](https://nvd.nist.gov/vuln/detail/CVE-2023-4622)
  * [CVE-2023-4623](https://nvd.nist.gov/vuln/detail/CVE-2023-4623)
  * [CVE-2023-4921](https://nvd.nist.gov/vuln/detail/CVE-2023-4921)
  * [CVE-2023-23914](https://nvd.nist.gov/vuln/detail/CVE-2023-23914)
  * [CVE-2023-28736](https://nvd.nist.gov/vuln/detail/CVE-2023-28736)
  * [CVE-2023-28938](https://nvd.nist.gov/vuln/detail/CVE-2023-28938)
  * [CVE-2023-29499](https://nvd.nist.gov/vuln/detail/CVE-2023-29499)
  * [CVE-2023-32611](https://nvd.nist.gov/vuln/detail/CVE-2023-32611)
  * [CVE-2023-32636](https://nvd.nist.gov/vuln/detail/CVE-2023-32636)
  * [CVE-2023-32643](https://nvd.nist.gov/vuln/detail/CVE-2023-32643)
  * [CVE-2023-32665](https://nvd.nist.gov/vuln/detail/CVE-2023-32665)
  * [CVE-2023-38039](https://nvd.nist.gov/vuln/detail/CVE-2023-38039)
  * [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545)
  * [CVE-2023-39189](https://nvd.nist.gov/vuln/detail/CVE-2023-39189)
  * [CVE-2023-39192](https://nvd.nist.gov/vuln/detail/CVE-2023-39192)
  * [CVE-2023-39194](https://nvd.nist.gov/vuln/detail/CVE-2023-39194)
  * [CVE-2023-40217](https://nvd.nist.gov/vuln/detail/CVE-2023-40217)
  * [CVE-2023-42752](https://nvd.nist.gov/vuln/detail/CVE-2023-42752)
  * [CVE-2023-42753](https://nvd.nist.gov/vuln/detail/CVE-2023-42753)
  * [CVE-2023-42756](https://nvd.nist.gov/vuln/detail/CVE-2023-42756)
  * [CVE-2023-45863](https://nvd.nist.gov/vuln/detail/CVE-2023-45863)



2022

  * [CVE-2022-3821](https://nvd.nist.gov/vuln/detail/CVE-2022-3821)
  * [CVE-2022-4269](https://nvd.nist.gov/vuln/detail/CVE-2022-4269)
  * [CVE-2022-4415](https://nvd.nist.gov/vuln/detail/CVE-2022-4415)
  * [CVE-2022-29458](https://nvd.nist.gov/vuln/detail/CVE-2022-29458)
  * [CVE-2022-47007](https://nvd.nist.gov/vuln/detail/CVE-2022-47007)
  * [CVE-2022-47008](https://nvd.nist.gov/vuln/detail/CVE-2022-47008)
  * [CVE-2022-47010](https://nvd.nist.gov/vuln/detail/CVE-2022-47010)
  * [CVE-2022-47011](https://nvd.nist.gov/vuln/detail/CVE-2022-47011)
  * [CVE-2022-48063](https://nvd.nist.gov/vuln/detail/CVE-2022-48063)
  * [CVE-2022-48064](https://nvd.nist.gov/vuln/detail/CVE-2022-48064)
  * [CVE-2022-48065](https://nvd.nist.gov/vuln/detail/CVE-2022-48065)



2020

  * [CVE-2020-22916](https://nvd.nist.gov/vuln/detail/CVE-2020-22916)



2018

  * [CVE-2018-1121](https://nvd.nist.gov/vuln/detail/CVE-2018-1121)
  * [CVE-2018-17075](https://nvd.nist.gov/vuln/detail/CVE-2018-17075)
  * [CVE-2018-17142](https://nvd.nist.gov/vuln/detail/CVE-2018-17142)
  * [CVE-2018-17143](https://nvd.nist.gov/vuln/detail/CVE-2018-17143)
  * [CVE-2018-17846](https://nvd.nist.gov/vuln/detail/CVE-2018-17846)
  * [CVE-2018-17847](https://nvd.nist.gov/vuln/detail/CVE-2018-17847)
  * [CVE-2018-17848](https://nvd.nist.gov/vuln/detail/CVE-2018-17848)



## 20230821_00_00

**Date released** | **Release type**  
---|---  
2023-08-21 | Automatic maintenance  
  
### Summary

Covered instances | Summary  
---|---  
All Redis instances | 

  * Set the Redis host OS version to [cos-105-17412-156-23](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105#cos-105-17412-156-23_n).
  * General reliability improvements.

  
  
### Security patches

2023

  * [CVE-2023-1206](https://nvd.nist.gov/vuln/detail/CVE-2023-1206)
  * [CVE-2023-3611](https://nvd.nist.gov/vuln/detail/CVE-2023-3611)
  * [CVE-2023-3623](https://nvd.nist.gov/vuln/detail/CVE-2023-3623)
  * [CVE-2023-3776](https://nvd.nist.gov/vuln/detail/CVE-2023-3776)
  * [CVE-2023-3812](https://nvd.nist.gov/vuln/detail/CVE-2023-3812)
  * [CVE-2023-3817](https://nvd.nist.gov/vuln/detail/CVE-2023-3817)
  * [CVE-2023-3995](https://nvd.nist.gov/vuln/detail/CVE-2023-3995)
  * [CVE-2023-4004](https://nvd.nist.gov/vuln/detail/CVE-2023-4004)
  * [CVE-2023-4128](https://nvd.nist.gov/vuln/detail/CVE-2023-4128)
  * [CVE-2023-4147](https://nvd.nist.gov/vuln/detail/CVE-2023-4147)
  * [CVE-2023-4194](https://nvd.nist.gov/vuln/detail/CVE-2023-4194)
  * [CVE-2023-4387](https://nvd.nist.gov/vuln/detail/CVE-2023-4387)
  * [CVE-2023-4459](https://nvd.nist.gov/vuln/detail/CVE-2023-4459)
  * [CVE-2023-29491](https://nvd.nist.gov/vuln/detail/CVE-2023-29491)
  * [CVE-2023-38408](https://nvd.nist.gov/vuln/detail/CVE-2023-38408)



2022

  * [CVE-2022-3623](https://nvd.nist.gov/vuln/detail/CVE-2022-3623)
  * [CVE-2022-28737](https://nvd.nist.gov/vuln/detail/CVE-2022-28737)



2016

  * [CVE-2016-4074](https://nvd.nist.gov/vuln/detail/CVE-2016-4074)



2015

  * [CVE-2015-8863](https://nvd.nist.gov/vuln/detail/CVE-2015-8863)



## 20230727_00_00

**Date released** | **Release type**  
---|---  
2023-07-27 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
Redis 6.x instances only | Set the OSS Redis patch version to [6.2.13](https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES).  
Redis 7.0 instances only | Set the OSS Redis patch version to [7.0.12](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES).  
All Redis instances |  Set the Redis host OS version to [cos-105-17412-156-4](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105#cos-105-17412-156-4_). General reliability improvements.  
  
### Security patches

2023

  * [CVE-2023-1786](https://nvd.nist.gov/vuln/detail/CVE-2023-1786)
  * [CVE-2023-1972](https://nvd.nist.gov/vuln/detail/CVE-2023-1972)
  * [CVE-2023-2124](https://nvd.nist.gov/vuln/detail/CVE-2023-2124)
  * [CVE-2023-2426](https://nvd.nist.gov/vuln/detail/CVE-2023-2426)
  * [CVE-2023-2609](https://nvd.nist.gov/vuln/detail/CVE-2023-2609)
  * [CVE-2023-2610](https://nvd.nist.gov/vuln/detail/CVE-2023-2610)
  * [CVE-2023-2650](https://nvd.nist.gov/vuln/detail/CVE-2023-2650)
  * [CVE-2023-3090](https://nvd.nist.gov/vuln/detail/CVE-2023-3090)
  * [CVE-2023-3268](https://nvd.nist.gov/vuln/detail/CVE-2023-3268)
  * [CVE-2023-3390](https://nvd.nist.gov/vuln/detail/CVE-2023-3390)
  * [CVE-2023-20867](https://nvd.nist.gov/vuln/detail/CVE-2023-20867)
  * [CVE-2023-24329](https://nvd.nist.gov/vuln/detail/CVE-2023-24329)
  * [CVE-2023-25515](https://nvd.nist.gov/vuln/detail/CVE-2023-25515)
  * [CVE-2023-25516](https://nvd.nist.gov/vuln/detail/CVE-2023-25516)
  * [CVE-2023-27534](https://nvd.nist.gov/vuln/detail/CVE-2023-27534)
  * [CVE-2023-28319](https://nvd.nist.gov/vuln/detail/CVE-2023-28319)
  * [CVE-2023-28320](https://nvd.nist.gov/vuln/detail/CVE-2023-28320)
  * [CVE-2023-28321](https://nvd.nist.gov/vuln/detail/CVE-2023-28321)
  * [CVE-2023-28322](https://nvd.nist.gov/vuln/detail/CVE-2023-28322)
  * [CVE-2023-28484](https://nvd.nist.gov/vuln/detail/CVE-2023-28484)
  * [CVE-2023-28856](https://nvd.nist.gov/vuln/detail/CVE-2023-28856)
  * [CVE-2023-29402](https://nvd.nist.gov/vuln/detail/CVE-2023-29402)
  * [CVE-2023-29403](https://nvd.nist.gov/vuln/detail/CVE-2023-29403)
  * [CVE-2023-29404](https://nvd.nist.gov/vuln/detail/CVE-2023-29404)
  * [CVE-2023-29405](https://nvd.nist.gov/vuln/detail/CVE-2023-29405)
  * [CVE-2023-29491](https://nvd.nist.gov/vuln/detail/CVE-2023-29491)
  * [CVE-2023-31248](https://nvd.nist.gov/vuln/detail/CVE-2023-31248)
  * [CVE-2023-32233](https://nvd.nist.gov/vuln/detail/CVE-2023-32233)
  * [CVE-2023-34256](https://nvd.nist.gov/vuln/detail/CVE-2023-34256)
  * [CVE-2023-35001](https://nvd.nist.gov/vuln/detail/CVE-2023-35001)
  * [CVE-2023-36824](https://nvd.nist.gov/vuln/detail/CVE-2023-36824)



2022

  * [CVE-2022-24834](https://nvd.nist.gov/vuln/detail/CVE-2022-24834)
  * [CVE-2022-45061](https://nvd.nist.gov/vuln/detail/CVE-2022-45061)



2021

  * [CVE-2021-28861](https://nvd.nist.gov/vuln/detail/CVE-2021-28861)



2020

  * [CVE-2020-10735](https://nvd.nist.gov/vuln/detail/CVE-2020-10735)



2015

  * [CVE-2015-20107](https://nvd.nist.gov/vuln/detail/CVE-2015-20107)



## 20230508_00_00

**Date released** | **Release type**  
---|---  
2023-05-08 | Automatic maintenance  
  
### Summary

Covered instances | Summary  
---|---  
Redis 5.x instances only | Set the OSS Redis patch version to [5.0.14](https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES).  
All Redis instances |  Set the Redis host OS version to [cos-105-17412-1-71](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105#cos-105-17412-1-71_). General reliability improvements.  
  
### Security patches

2023

  * [CVE-2023-0180](https://nvd.nist.gov/vuln/detail/CVE-2023-0180)
  * [CVE-2023-0183](https://nvd.nist.gov/vuln/detail/CVE-2023-0183)
  * [CVE-2023-0184](https://nvd.nist.gov/vuln/detail/CVE-2023-0184)
  * [CVE-2023-0185](https://nvd.nist.gov/vuln/detail/CVE-2023-0185)
  * [CVE-2023-0187](https://nvd.nist.gov/vuln/detail/CVE-2023-0187)
  * [CVE-2023-0188](https://nvd.nist.gov/vuln/detail/CVE-2023-0188)
  * [CVE-2023-0189](https://nvd.nist.gov/vuln/detail/CVE-2023-0189)



2022

  * [CVE-2022-1154](https://nvd.nist.gov/vuln/detail/CVE-2022-1154)
  * [CVE-2022-1160](https://nvd.nist.gov/vuln/detail/CVE-2022-1160)
  * [CVE-2022-1304](https://nvd.nist.gov/vuln/detail/CVE-2022-1304)
  * [CVE-2022-1381](https://nvd.nist.gov/vuln/detail/CVE-2022-1381)
  * [CVE-2022-1420](https://nvd.nist.gov/vuln/detail/CVE-2022-1420)
  * [CVE-2022-1586](https://nvd.nist.gov/vuln/detail/CVE-2022-1586)
  * [CVE-2022-1587](https://nvd.nist.gov/vuln/detail/CVE-2022-1587)
  * [CVE-2022-1616](https://nvd.nist.gov/vuln/detail/CVE-2022-1616)
  * [CVE-2022-1619](https://nvd.nist.gov/vuln/detail/CVE-2022-1619)
  * [CVE-2022-1620](https://nvd.nist.gov/vuln/detail/CVE-2022-1620)
  * [CVE-2022-1621](https://nvd.nist.gov/vuln/detail/CVE-2022-1621)
  * [CVE-2022-1629](https://nvd.nist.gov/vuln/detail/CVE-2022-1629)
  * [CVE-2022-1664](https://nvd.nist.gov/vuln/detail/CVE-2022-1664)
  * [CVE-2022-1674](https://nvd.nist.gov/vuln/detail/CVE-2022-1674)
  * [CVE-2022-1720](https://nvd.nist.gov/vuln/detail/CVE-2022-1720)
  * [CVE-2022-1733](https://nvd.nist.gov/vuln/detail/CVE-2022-1733)
  * [CVE-2022-1735](https://nvd.nist.gov/vuln/detail/CVE-2022-1735)
  * [CVE-2022-1769](https://nvd.nist.gov/vuln/detail/CVE-2022-1769)
  * [CVE-2022-1771](https://nvd.nist.gov/vuln/detail/CVE-2022-1771)
  * [CVE-2022-1785](https://nvd.nist.gov/vuln/detail/CVE-2022-1785)
  * [CVE-2022-1796](https://nvd.nist.gov/vuln/detail/CVE-2022-1796)
  * [CVE-2022-1851](https://nvd.nist.gov/vuln/detail/CVE-2022-1851)
  * [CVE-2022-1886](https://nvd.nist.gov/vuln/detail/CVE-2022-1886)
  * [CVE-2022-1898](https://nvd.nist.gov/vuln/detail/CVE-2022-1898)
  * [CVE-2022-1927](https://nvd.nist.gov/vuln/detail/CVE-2022-1927)
  * [CVE-2022-1942](https://nvd.nist.gov/vuln/detail/CVE-2022-1942)
  * [CVE-2022-2124](https://nvd.nist.gov/vuln/detail/CVE-2022-2124)
  * [CVE-2022-2125](https://nvd.nist.gov/vuln/detail/CVE-2022-2125)
  * [CVE-2022-2126](https://nvd.nist.gov/vuln/detail/CVE-2022-2126)
  * [CVE-2022-2129](https://nvd.nist.gov/vuln/detail/CVE-2022-2129)
  * [CVE-2022-2928](https://nvd.nist.gov/vuln/detail/CVE-2022-2928)
  * [CVE-2022-2929](https://nvd.nist.gov/vuln/detail/CVE-2022-2929)
  * [CVE-2022-3715](https://nvd.nist.gov/vuln/detail/CVE-2022-3715)
  * [CVE-2022-22943](https://nvd.nist.gov/vuln/detail/CVE-2022-22943)
  * [CVE-2022-23218](https://nvd.nist.gov/vuln/detail/CVE-2022-23218)
  * [CVE-2022-23219](https://nvd.nist.gov/vuln/detail/CVE-2022-23219)
  * [CVE-2022-26280](https://nvd.nist.gov/vuln/detail/CVE-2022-26280)
  * [CVE-2022-29824](https://nvd.nist.gov/vuln/detail/CVE-2022-29824)
  * [CVE-2022-34903](https://nvd.nist.gov/vuln/detail/CVE-2022-34903)
  * [CVE-2022-37434](https://nvd.nist.gov/vuln/detail/CVE-2022-37434)
  * [CVE-2022-37454](https://nvd.nist.gov/vuln/detail/CVE-2022-37454)
  * [CVE-2022-40768](https://nvd.nist.gov/vuln/detail/CVE-2022-40768)
  * [CVE-2022-41723](https://nvd.nist.gov/vuln/detail/CVE-2022-41723)
  * [CVE-2022-41725](https://nvd.nist.gov/vuln/detail/CVE-2022-41725)
  * [CVE-2022-42898](https://nvd.nist.gov/vuln/detail/CVE-2022-42898)
  * [CVE-2022-43750](https://nvd.nist.gov/vuln/detail/CVE-2022-43750)
  * [CVE-2022-44638](https://nvd.nist.gov/vuln/detail/CVE-2022-44638)



2021

  * [CVE-2021-3997](https://nvd.nist.gov/vuln/detail/CVE-2021-3997)
  * [CVE-2021-3999](https://nvd.nist.gov/vuln/detail/CVE-2021-3999)
  * [CVE-2021-4122](https://nvd.nist.gov/vuln/detail/CVE-2021-4122)
  * [CVE-2021-4160](https://nvd.nist.gov/vuln/detail/CVE-2021-4160)
  * [CVE-2021-20270](https://nvd.nist.gov/vuln/detail/CVE-2021-20270)
  * [CVE-2021-27291](https://nvd.nist.gov/vuln/detail/CVE-2021-27291)
  * [CVE-2021-33574](https://nvd.nist.gov/vuln/detail/CVE-2021-33574)
  * [CVE-2021-43396](https://nvd.nist.gov/vuln/detail/CVE-2021-43396)



2020

  * [CVE-2020-17437](https://nvd.nist.gov/vuln/detail/CVE-2020-17437)



2018

  * [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032)



2004

  * [CVE-2004-0971](https://nvd.nist.gov/vuln/detail/CVE-2004-0971)



## 20230322_00_00

**Date released** | **Release type**  
---|---  
2023-03-29 | Self-service  
  
### Summary

Covered instances | Summary  
---|---  
Redis 6.x instances only | Set the OSS Redis patch version to [6.2.11](https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES). This patch includes fixes to   
[CVE-2023-25155](https://nvd.nist.gov/vuln/detail/CVE-2023-25155) and [CVE-2022-36021](https://nvd.nist.gov/vuln/detail/CVE-2022-36021).  
All Redis instances | Set the Redis host OS version to [cos-97-16919-235-36](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97#cos-97-16919-235-36_).  
  
### Security patches

2023

  * [CVE-2023-0049](https://nvd.nist.gov/vuln/detail/CVE-2023-0049)
  * [CVE-2023-0051](https://nvd.nist.gov/vuln/detail/CVE-2023-0051)
  * [CVE-2023-0054](https://nvd.nist.gov/vuln/detail/CVE-2023-0054)
  * [CVE-2023-0215](https://nvd.nist.gov/vuln/detail/CVE-2023-0215)
  * [CVE-2023-0286](https://nvd.nist.gov/vuln/detail/CVE-2023-0286)
  * [CVE-2023-0288](https://nvd.nist.gov/vuln/detail/CVE-2023-0288)
  * [CVE-2023-0433](https://nvd.nist.gov/vuln/detail/CVE-2023-0433)
  * [CVE-2023-0461](https://nvd.nist.gov/vuln/detail/CVE-2023-0461)
  * [CVE-2023-0512](https://nvd.nist.gov/vuln/detail/CVE-2023-0512)
  * [CVE-2023-1127](https://nvd.nist.gov/vuln/detail/CVE-2023-1127)
  * [CVE-2023-1170](https://nvd.nist.gov/vuln/detail/CVE-2023-1170)
  * [CVE-2023-1175](https://nvd.nist.gov/vuln/detail/CVE-2023-1175)
  * [CVE-2023-1264](https://nvd.nist.gov/vuln/detail/CVE-2023-1264)
  * [CVE-2023-1355](https://nvd.nist.gov/vuln/detail/CVE-2023-1355)
  * [CVE-2023-23454](https://nvd.nist.gov/vuln/detail/CVE-2023-23454)
  * [CVE-2023-23586](https://nvd.nist.gov/vuln/detail/CVE-2023-23586)
  * [CVE-2023-23931](https://nvd.nist.gov/vuln/detail/CVE-2023-23931)
  * [CVE-2023-25155](https://nvd.nist.gov/vuln/detail/CVE-2023-25155)
  * [CVE-2023-26604](https://nvd.nist.gov/vuln/detail/CVE-2023-26604)
  * [CVE-2023-28466](https://nvd.nist.gov/vuln/detail/CVE-2023-28466)



2022

  * [CVE-2022-0001](https://nvd.nist.gov/vuln/detail/CVE-2022-0001)
  * [CVE-2022-0002](https://nvd.nist.gov/vuln/detail/CVE-2022-0002)
  * [CVE-2022-0128](https://nvd.nist.gov/vuln/detail/CVE-2022-0128)
  * [CVE-2022-0156](https://nvd.nist.gov/vuln/detail/CVE-2022-0156)
  * [CVE-2022-0158](https://nvd.nist.gov/vuln/detail/CVE-2022-0158)
  * [CVE-2022-0168](https://nvd.nist.gov/vuln/detail/CVE-2022-0168)
  * [CVE-2022-0185](https://nvd.nist.gov/vuln/detail/CVE-2022-0185)
  * [CVE-2022-0261](https://nvd.nist.gov/vuln/detail/CVE-2022-0261)
  * [CVE-2022-0264](https://nvd.nist.gov/vuln/detail/CVE-2022-0264)
  * [CVE-2022-0318](https://nvd.nist.gov/vuln/detail/CVE-2022-0318)
  * [CVE-2022-0319](https://nvd.nist.gov/vuln/detail/CVE-2022-0319)
  * [CVE-2022-0359](https://nvd.nist.gov/vuln/detail/CVE-2022-0359)
  * [CVE-2022-0361](https://nvd.nist.gov/vuln/detail/CVE-2022-0361)
  * [CVE-2022-0368](https://nvd.nist.gov/vuln/detail/CVE-2022-0368)
  * [CVE-2022-0392](https://nvd.nist.gov/vuln/detail/CVE-2022-0392)
  * [CVE-2022-0393](https://nvd.nist.gov/vuln/detail/CVE-2022-0393)
  * [CVE-2022-0407](https://nvd.nist.gov/vuln/detail/CVE-2022-0407)
  * [CVE-2022-0408](https://nvd.nist.gov/vuln/detail/CVE-2022-0408)
  * [CVE-2022-0413](https://nvd.nist.gov/vuln/detail/CVE-2022-0413)
  * [CVE-2022-0443](https://nvd.nist.gov/vuln/detail/CVE-2022-0443)
  * [CVE-2022-0492](https://nvd.nist.gov/vuln/detail/CVE-2022-0492)
  * [CVE-2022-0494](https://nvd.nist.gov/vuln/detail/CVE-2022-0494)
  * [CVE-2022-0572](https://nvd.nist.gov/vuln/detail/CVE-2022-0572)
  * [CVE-2022-0617](https://nvd.nist.gov/vuln/detail/CVE-2022-0617)
  * [CVE-2022-0629](https://nvd.nist.gov/vuln/detail/CVE-2022-0629)
  * [CVE-2022-0685](https://nvd.nist.gov/vuln/detail/CVE-2022-0685)
  * [CVE-2022-0696](https://nvd.nist.gov/vuln/detail/CVE-2022-0696)
  * [CVE-2022-0696](https://nvd.nist.gov/vuln/detail/CVE-2022-0696)
  * [CVE-2022-0714](https://nvd.nist.gov/vuln/detail/CVE-2022-0714)
  * [CVE-2022-0729](https://nvd.nist.gov/vuln/detail/CVE-2022-0729)
  * [CVE-2022-0778](https://nvd.nist.gov/vuln/detail/CVE-2022-0778)
  * [CVE-2022-0847](https://nvd.nist.gov/vuln/detail/CVE-2022-0847)
  * [CVE-2022-0850](https://nvd.nist.gov/vuln/detail/CVE-2022-0850)
  * [CVE-2022-0854](https://nvd.nist.gov/vuln/detail/CVE-2022-0854)
  * [CVE-2022-0886](https://nvd.nist.gov/vuln/detail/CVE-2022-0886)
  * [CVE-2022-0943](https://nvd.nist.gov/vuln/detail/CVE-2022-0943)
  * [CVE-2022-0995](https://nvd.nist.gov/vuln/detail/CVE-2022-0995)
  * [CVE-2022-1011](https://nvd.nist.gov/vuln/detail/CVE-2022-1011)
  * [CVE-2022-1012](https://nvd.nist.gov/vuln/detail/CVE-2022-1012)
  * [CVE-2022-1055](https://nvd.nist.gov/vuln/detail/CVE-2022-1055)
  * [CVE-2022-1116](https://nvd.nist.gov/vuln/detail/CVE-2022-1116)
  * [CVE-2022-1271](https://nvd.nist.gov/vuln/detail/CVE-2022-1271)
  * [CVE-2022-1292](https://nvd.nist.gov/vuln/detail/CVE-2022-1292)
  * [CVE-2022-1353](https://nvd.nist.gov/vuln/detail/CVE-2022-1353)
  * [CVE-2022-1508](https://nvd.nist.gov/vuln/detail/CVE-2022-1508)
  * [CVE-2022-1516](https://nvd.nist.gov/vuln/detail/CVE-2022-1516)
  * [CVE-2022-1729](https://nvd.nist.gov/vuln/detail/CVE-2022-1729)
  * [CVE-2022-1786](https://nvd.nist.gov/vuln/detail/CVE-2022-1786)
  * [CVE-2022-1998](https://nvd.nist.gov/vuln/detail/CVE-2022-1998)
  * [CVE-2022-2068](https://nvd.nist.gov/vuln/detail/CVE-2022-2068)
  * [CVE-2022-2097](https://nvd.nist.gov/vuln/detail/CVE-2022-2097)
  * [CVE-2022-2175](https://nvd.nist.gov/vuln/detail/CVE-2022-2175)
  * [CVE-2022-2182](https://nvd.nist.gov/vuln/detail/CVE-2022-2182)
  * [CVE-2022-2183](https://nvd.nist.gov/vuln/detail/CVE-2022-2183)
  * [CVE-2022-2206](https://nvd.nist.gov/vuln/detail/CVE-2022-2206)
  * [CVE-2022-2207](https://nvd.nist.gov/vuln/detail/CVE-2022-2207)
  * [CVE-2022-2208](https://nvd.nist.gov/vuln/detail/CVE-2022-2208)
  * [CVE-2022-2210](https://nvd.nist.gov/vuln/detail/CVE-2022-2210)
  * [CVE-2022-2231](https://nvd.nist.gov/vuln/detail/CVE-2022-2231)
  * [CVE-2022-2257](https://nvd.nist.gov/vuln/detail/CVE-2022-2257)
  * [CVE-2022-2264](https://nvd.nist.gov/vuln/detail/CVE-2022-2264)
  * [CVE-2022-2284](https://nvd.nist.gov/vuln/detail/CVE-2022-2284)
  * [CVE-2022-2285](https://nvd.nist.gov/vuln/detail/CVE-2022-2285)
  * [CVE-2022-2286](https://nvd.nist.gov/vuln/detail/CVE-2022-2286)
  * [CVE-2022-2287](https://nvd.nist.gov/vuln/detail/CVE-2022-2287)
  * [CVE-2022-2288](https://nvd.nist.gov/vuln/detail/CVE-2022-2288)
  * [CVE-2022-2289](https://nvd.nist.gov/vuln/detail/CVE-2022-2289)
  * [CVE-2022-2304](https://nvd.nist.gov/vuln/detail/CVE-2022-2304)
  * [CVE-2022-2327](https://nvd.nist.gov/vuln/detail/CVE-2022-2327)
  * [CVE-2022-2343](https://nvd.nist.gov/vuln/detail/CVE-2022-2343)
  * [CVE-2022-2344](https://nvd.nist.gov/vuln/detail/CVE-2022-2344)
  * [CVE-2022-2345](https://nvd.nist.gov/vuln/detail/CVE-2022-2345)
  * [CVE-2022-2503](https://nvd.nist.gov/vuln/detail/CVE-2022-2503)
  * [CVE-2022-2509](https://nvd.nist.gov/vuln/detail/CVE-2022-2509)
  * [CVE-2022-2522](https://nvd.nist.gov/vuln/detail/CVE-2022-2522)
  * [CVE-2022-2526](https://nvd.nist.gov/vuln/detail/CVE-2022-2526)
  * [CVE-2022-2571](https://nvd.nist.gov/vuln/detail/CVE-2022-2571)
  * [CVE-2022-2580](https://nvd.nist.gov/vuln/detail/CVE-2022-2580)
  * [CVE-2022-2581](https://nvd.nist.gov/vuln/detail/CVE-2022-2581)
  * [CVE-2022-2598](https://nvd.nist.gov/vuln/detail/CVE-2022-2598)
  * [CVE-2022-2602](https://nvd.nist.gov/vuln/detail/CVE-2022-2602)
  * [CVE-2022-2816](https://nvd.nist.gov/vuln/detail/CVE-2022-2816)
  * [CVE-2022-2817](https://nvd.nist.gov/vuln/detail/CVE-2022-2817)
  * [CVE-2022-2819](https://nvd.nist.gov/vuln/detail/CVE-2022-2819)
  * [CVE-2022-2845](https://nvd.nist.gov/vuln/detail/CVE-2022-2845)
  * [CVE-2022-2849](https://nvd.nist.gov/vuln/detail/CVE-2022-2849)
  * [CVE-2022-2862](https://nvd.nist.gov/vuln/detail/CVE-2022-2862)
  * [CVE-2022-2874](https://nvd.nist.gov/vuln/detail/CVE-2022-2874)
  * [CVE-2022-2889](https://nvd.nist.gov/vuln/detail/CVE-2022-2889)
  * [CVE-2022-2905](https://nvd.nist.gov/vuln/detail/CVE-2022-2905)
  * [CVE-2022-2923](https://nvd.nist.gov/vuln/detail/CVE-2022-2923)
  * [CVE-2022-2938](https://nvd.nist.gov/vuln/detail/CVE-2022-2938)
  * [CVE-2022-2946](https://nvd.nist.gov/vuln/detail/CVE-2022-2946)
  * [CVE-2022-2959](https://nvd.nist.gov/vuln/detail/CVE-2022-2959)
  * [CVE-2022-2977](https://nvd.nist.gov/vuln/detail/CVE-2022-2977)
  * [CVE-2022-2980](https://nvd.nist.gov/vuln/detail/CVE-2022-2980)
  * [CVE-2022-2982](https://nvd.nist.gov/vuln/detail/CVE-2022-2982)
  * [CVE-2022-3016](https://nvd.nist.gov/vuln/detail/CVE-2022-3016)
  * [CVE-2022-3028](https://nvd.nist.gov/vuln/detail/CVE-2022-3028)
  * [CVE-2022-3037](https://nvd.nist.gov/vuln/detail/CVE-2022-3037)
  * [CVE-2022-3099](https://nvd.nist.gov/vuln/detail/CVE-2022-3099)
  * [CVE-2022-3104](https://nvd.nist.gov/vuln/detail/CVE-2022-3104)
  * [CVE-2022-3107](https://nvd.nist.gov/vuln/detail/CVE-2022-3107)
  * [CVE-2022-3134](https://nvd.nist.gov/vuln/detail/CVE-2022-3134)
  * [CVE-2022-3153](https://nvd.nist.gov/vuln/detail/CVE-2022-3153)
  * [CVE-2022-3169](https://nvd.nist.gov/vuln/detail/CVE-2022-3169)
  * [CVE-2022-3176](https://nvd.nist.gov/vuln/detail/CVE-2022-3176)
  * [CVE-2022-3234](https://nvd.nist.gov/vuln/detail/CVE-2022-3234)
  * [CVE-2022-3235](https://nvd.nist.gov/vuln/detail/CVE-2022-3235)
  * [CVE-2022-3256](https://nvd.nist.gov/vuln/detail/CVE-2022-3256)
  * [CVE-2022-3278](https://nvd.nist.gov/vuln/detail/CVE-2022-3278)
  * [CVE-2022-3296](https://nvd.nist.gov/vuln/detail/CVE-2022-3296)
  * [CVE-2022-3297](https://nvd.nist.gov/vuln/detail/CVE-2022-3297)
  * [CVE-2022-3324](https://nvd.nist.gov/vuln/detail/CVE-2022-3324)
  * [CVE-2022-3352](https://nvd.nist.gov/vuln/detail/CVE-2022-3352)
  * [CVE-2022-3524](https://nvd.nist.gov/vuln/detail/CVE-2022-3524)
  * [CVE-2022-3586](https://nvd.nist.gov/vuln/detail/CVE-2022-3586)
  * [CVE-2022-3625](https://nvd.nist.gov/vuln/detail/CVE-2022-3625)
  * [CVE-2022-3705](https://nvd.nist.gov/vuln/detail/CVE-2022-3705)
  * [CVE-2022-3821](https://nvd.nist.gov/vuln/detail/CVE-2022-3821)
  * [CVE-2022-4141](https://nvd.nist.gov/vuln/detail/CVE-2022-4141)
  * [CVE-2022-4285](https://nvd.nist.gov/vuln/detail/CVE-2022-4285)
  * [CVE-2022-4292](https://nvd.nist.gov/vuln/detail/CVE-2022-4292)
  * [CVE-2022-4304](https://nvd.nist.gov/vuln/detail/CVE-2022-4304)
  * [CVE-2022-4378](https://nvd.nist.gov/vuln/detail/CVE-2022-4378)
  * [CVE-2022-4450](https://nvd.nist.gov/vuln/detail/CVE-2022-4450)
  * [CVE-2022-4696](https://nvd.nist.gov/vuln/detail/CVE-2022-4696)
  * [CVE-2022-23471](https://nvd.nist.gov/vuln/detail/CVE-2022-23471)
  * [CVE-2022-23648](https://nvd.nist.gov/vuln/detail/CVE-2022-23648)
  * [CVE-2022-23960](https://nvd.nist.gov/vuln/detail/CVE-2022-23960)
  * [CVE-2022-24448](https://nvd.nist.gov/vuln/detail/CVE-2022-24448)
  * [CVE-2022-24769](https://nvd.nist.gov/vuln/detail/CVE-2022-24769)
  * [CVE-2022-23308](https://nvd.nist.gov/vuln/detail/CVE-2022-23308)
  * [CVE-2022-22576](https://nvd.nist.gov/vuln/detail/CVE-2022-22576)
  * [CVE-2022-21505](https://nvd.nist.gov/vuln/detail/CVE-2022-21505)
  * [CVE-2022-20409](https://nvd.nist.gov/vuln/detail/CVE-2022-20409)
  * [CVE-2022-27239](https://nvd.nist.gov/vuln/detail/CVE-2022-27239)
  * [CVE-2022-27666](https://nvd.nist.gov/vuln/detail/CVE-2022-27666)
  * [CVE-2022-27774](https://nvd.nist.gov/vuln/detail/CVE-2022-27774)
  * [CVE-2022-27775](https://nvd.nist.gov/vuln/detail/CVE-2022-27775)
  * [CVE-2022-27776](https://nvd.nist.gov/vuln/detail/CVE-2022-27776)
  * [CVE-2022-27778](https://nvd.nist.gov/vuln/detail/CVE-2022-27778)
  * [CVE-2022-27779](https://nvd.nist.gov/vuln/detail/CVE-2022-27779)
  * [CVE-2022-27780](https://nvd.nist.gov/vuln/detail/CVE-2022-27780)
  * [CVE-2022-27781](https://nvd.nist.gov/vuln/detail/CVE-2022-27781)
  * [CVE-2022-27782](https://nvd.nist.gov/vuln/detail/CVE-2022-27782)
  * [CVE-2022-28893](https://nvd.nist.gov/vuln/detail/CVE-2022-28893)
  * [CVE-2022-29154](https://nvd.nist.gov/vuln/detail/CVE-2022-29154)
  * [CVE-2022-29162](https://nvd.nist.gov/vuln/detail/CVE-2022-29162)
  * [CVE-2022-29217](https://nvd.nist.gov/vuln/detail/CVE-2022-29217)
  * [CVE-2022-29458](https://nvd.nist.gov/vuln/detail/CVE-2022-29458)
  * [CVE-2022-29581](https://nvd.nist.gov/vuln/detail/CVE-2022-29581)
  * [CVE-2022-29582](https://nvd.nist.gov/vuln/detail/CVE-2022-29582)
  * [CVE-2022-29869](https://nvd.nist.gov/vuln/detail/CVE-2022-29869)
  * [CVE-2022-30115](https://nvd.nist.gov/vuln/detail/CVE-2022-30115)
  * [CVE-2022-30594](https://nvd.nist.gov/vuln/detail/CVE-2022-30594)
  * [CVE-2022-31030](https://nvd.nist.gov/vuln/detail/CVE-2022-31030)
  * [CVE-2022-32149](https://nvd.nist.gov/vuln/detail/CVE-2022-32149)
  * [CVE-2022-32205](https://nvd.nist.gov/vuln/detail/CVE-2022-32205)
  * [CVE-2022-32206](https://nvd.nist.gov/vuln/detail/CVE-2022-32206)
  * [CVE-2022-32207](https://nvd.nist.gov/vuln/detail/CVE-2022-32207)
  * [CVE-2022-32208](https://nvd.nist.gov/vuln/detail/CVE-2022-32208)
  * [CVE-2022-32221](https://nvd.nist.gov/vuln/detail/CVE-2022-32221)
  * [CVE-2022-32296](https://nvd.nist.gov/vuln/detail/CVE-2022-32296)
  * [CVE-2022-33743](https://nvd.nist.gov/vuln/detail/CVE-2022-33743)
  * [CVE-2022-33744](https://nvd.nist.gov/vuln/detail/CVE-2022-33744)
  * [CVE-2022-35252](https://nvd.nist.gov/vuln/detail/CVE-2022-35252)
  * [CVE-2022-35260](https://nvd.nist.gov/vuln/detail/CVE-2022-35260)
  * [CVE-2022-35737](https://nvd.nist.gov/vuln/detail/CVE-2022-35737)
  * [CVE-2022-35977](https://nvd.nist.gov/vuln/detail/CVE-2022-35977)
  * [CVE-2022-36021](https://nvd.nist.gov/vuln/detail/CVE-2022-36021)
  * [CVE-2022-36123](https://nvd.nist.gov/vuln/detail/CVE-2022-36123)
  * [CVE-2022-36946](https://nvd.nist.gov/vuln/detail/CVE-2022-36946)
  * [CVE-2022-39188](https://nvd.nist.gov/vuln/detail/CVE-2022-39188)
  * [CVE-2022-40303](https://nvd.nist.gov/vuln/detail/CVE-2022-40303)
  * [CVE-2022-40304](https://nvd.nist.gov/vuln/detail/CVE-2022-40304)
  * [CVE-2022-40320](https://nvd.nist.gov/vuln/detail/CVE-2022-40320)
  * [CVE-2022-40897](https://nvd.nist.gov/vuln/detail/CVE-2022-40897)
  * [CVE-2022-41222](https://nvd.nist.gov/vuln/detail/CVE-2022-41222)
  * [CVE-2022-42328](https://nvd.nist.gov/vuln/detail/CVE-2022-42328)
  * [CVE-2022-42329](https://nvd.nist.gov/vuln/detail/CVE-2022-42329)
  * [CVE-2022-42915](https://nvd.nist.gov/vuln/detail/CVE-2022-42915)
  * [CVE-2022-43945](https://nvd.nist.gov/vuln/detail/CVE-2022-43945)
  * [CVE-2022-46663](https://nvd.nist.gov/vuln/detail/CVE-2022-46663)
  * [CVE-2022-47929](https://nvd.nist.gov/vuln/detail/CVE-2022-47929)
  * [CVE-2022-47946](https://nvd.nist.gov/vuln/detail/CVE-2022-47946)
  * [CVE-2022-48303](https://nvd.nist.gov/vuln/detail/CVE-2022-48303)



2021

  * [CVE-2021-3580](https://nvd.nist.gov/vuln/detail/CVE-2021-3580)
  * [CVE-2021-3669](https://nvd.nist.gov/vuln/detail/CVE-2021-3669)
  * [CVE-2021-3711](https://nvd.nist.gov/vuln/detail/CVE-2021-3711)
  * [CVE-2021-3732](https://nvd.nist.gov/vuln/detail/CVE-2021-3732)
  * [CVE-2021-3743](https://nvd.nist.gov/vuln/detail/CVE-2021-3743)
  * [CVE-2021-3753](https://nvd.nist.gov/vuln/detail/CVE-2021-3753)
  * [CVE-2021-3872](https://nvd.nist.gov/vuln/detail/CVE-2021-3872)
  * [CVE-2021-3875](https://nvd.nist.gov/vuln/detail/CVE-2021-3875)
  * [CVE-2021-3903](https://nvd.nist.gov/vuln/detail/CVE-2021-3903)
  * [CVE-2021-3927](https://nvd.nist.gov/vuln/detail/CVE-2021-3927)
  * [CVE-2021-3928](https://nvd.nist.gov/vuln/detail/CVE-2021-3928)
  * [CVE-2021-3968](https://nvd.nist.gov/vuln/detail/CVE-2021-3968)
  * [CVE-2021-3973](https://nvd.nist.gov/vuln/detail/CVE-2021-3973)
  * [CVE-2021-3974](https://nvd.nist.gov/vuln/detail/CVE-2021-3974)
  * [CVE-2021-3984](https://nvd.nist.gov/vuln/detail/CVE-2021-3984)
  * [CVE-2021-4001](https://nvd.nist.gov/vuln/detail/CVE-2021-4001)
  * [CVE-2021-4002](https://nvd.nist.gov/vuln/detail/CVE-2021-4002)
  * [CVE-2021-4019](https://nvd.nist.gov/vuln/detail/CVE-2021-4019)
  * [CVE-2021-4037](https://nvd.nist.gov/vuln/detail/CVE-2021-4037)
  * [CVE-2021-4069](https://nvd.nist.gov/vuln/detail/CVE-2021-4069)
  * [CVE-2021-4083](https://nvd.nist.gov/vuln/detail/CVE-2021-4083)
  * [CVE-2021-4136](https://nvd.nist.gov/vuln/detail/CVE-2021-4136)
  * [CVE-2021-4148](https://nvd.nist.gov/vuln/detail/CVE-2021-4148)
  * [CVE-2021-4154](https://nvd.nist.gov/vuln/detail/CVE-2021-4154)
  * [CVE-2021-4155](https://nvd.nist.gov/vuln/detail/CVE-2021-4155)
  * [CVE-2021-4157](https://nvd.nist.gov/vuln/detail/CVE-2021-4157)
  * [CVE-2021-4159](https://nvd.nist.gov/vuln/detail/CVE-2021-4159)
  * [CVE-2021-4166](https://nvd.nist.gov/vuln/detail/CVE-2021-4166)
  * [CVE-2021-4173](https://nvd.nist.gov/vuln/detail/CVE-2021-4173)
  * [CVE-2021-4187](https://nvd.nist.gov/vuln/detail/CVE-2021-4187)
  * [CVE-2021-4192](https://nvd.nist.gov/vuln/detail/CVE-2021-4192)
  * [CVE-2021-4193](https://nvd.nist.gov/vuln/detail/CVE-2021-4193)
  * [CVE-2021-4203](https://nvd.nist.gov/vuln/detail/CVE-2021-4203)
  * [CVE-2021-4209](https://nvd.nist.gov/vuln/detail/CVE-2021-4209)
  * [CVE-2021-20208](https://nvd.nist.gov/vuln/detail/CVE-2021-20208)
  * [CVE-2021-20321](https://nvd.nist.gov/vuln/detail/CVE-2021-20321)
  * [CVE-2021-20322](https://nvd.nist.gov/vuln/detail/CVE-2021-20322)
  * [CVE-2021-22543](https://nvd.nist.gov/vuln/detail/CVE-2021-22543)
  * [CVE-2021-22570](https://nvd.nist.gov/vuln/detail/CVE-2021-22570)
  * [CVE-2021-22600](https://nvd.nist.gov/vuln/detail/CVE-2021-22600)
  * [CVE-2021-22876](https://nvd.nist.gov/vuln/detail/CVE-2021-22876)
  * [CVE-2021-22890](https://nvd.nist.gov/vuln/detail/CVE-2021-22890)
  * [CVE-2021-22897](https://nvd.nist.gov/vuln/detail/CVE-2021-22897)
  * [CVE-2021-22898](https://nvd.nist.gov/vuln/detail/CVE-2021-22898)
  * [CVE-2021-22924](https://nvd.nist.gov/vuln/detail/CVE-2021-22924)
  * [CVE-2021-22926](https://nvd.nist.gov/vuln/detail/CVE-2021-22926)
  * [CVE-2021-26341](https://nvd.nist.gov/vuln/detail/CVE-2021-26341)
  * [CVE-2021-28714](https://nvd.nist.gov/vuln/detail/CVE-2021-28714)
  * [CVE-2021-28715](https://nvd.nist.gov/vuln/detail/CVE-2021-28715)
  * [CVE-2021-31879](https://nvd.nist.gov/vuln/detail/CVE-2021-31879)
  * [CVE-2021-33656](https://nvd.nist.gov/vuln/detail/CVE-2021-33656)
  * [CVE-2021-34556](https://nvd.nist.gov/vuln/detail/CVE-2021-34556)
  * [CVE-2021-35477](https://nvd.nist.gov/vuln/detail/CVE-2021-35477)
  * [CVE-2021-38205](https://nvd.nist.gov/vuln/detail/CVE-2021-38205)
  * [CVE-2021-38561](https://nvd.nist.gov/vuln/detail/CVE-2021-38561)
  * [CVE-2021-40528](https://nvd.nist.gov/vuln/detail/CVE-2021-40528)
  * [CVE-2021-41103](https://nvd.nist.gov/vuln/detail/CVE-2021-41103)
  * [CVE-2021-41190](https://nvd.nist.gov/vuln/detail/CVE-2021-41190)
  * [CVE-2021-41617](https://nvd.nist.gov/vuln/detail/CVE-2021-41617)
  * [CVE-2021-43527](https://nvd.nist.gov/vuln/detail/CVE-2021-43527)
  * [CVE-2021-43618](https://nvd.nist.gov/vuln/detail/CVE-2021-43618)
  * [CVE-2021-43784](https://nvd.nist.gov/vuln/detail/CVE-2021-43784)
  * [CVE-2021-43816](https://nvd.nist.gov/vuln/detail/CVE-2021-43816)
  * [CVE-2021-45346](https://nvd.nist.gov/vuln/detail/CVE-2021-45346)
  * [CVE-2021-45402](https://nvd.nist.gov/vuln/detail/CVE-2021-45402)
  * [CVE-2021-45485](https://nvd.nist.gov/vuln/detail/CVE-2021-45485)
  * [CVE-2021-46828](https://nvd.nist.gov/vuln/detail/CVE-2021-46828)
  * [CVE-2021-46848](https://nvd.nist.gov/vuln/detail/CVE-2021-46848)



2020

  * [CVE-2020-13529](https://nvd.nist.gov/vuln/detail/CVE-2020-13529)
  * [CVE-2020-14387](https://nvd.nist.gov/vuln/detail/CVE-2020-14387)
  * [CVE-2020-36516](https://nvd.nist.gov/vuln/detail/CVE-2020-36516)



2019

  * [CVE-2019-9924](https://nvd.nist.gov/vuln/detail/CVE-2019-9924)
  * [CVE-2019-17594](https://nvd.nist.gov/vuln/detail/CVE-2019-17594)
  * [CVE-2019-17595](https://nvd.nist.gov/vuln/detail/CVE-2019-17595)
  * [CVE-2019-18276](https://nvd.nist.gov/vuln/detail/CVE-2019-18276)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
