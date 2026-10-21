---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters/
title: Managed Service for Apache Spark cluster image version lists \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:55.893761+00:00
---

# Managed Service for Apache Spark cluster image version lists  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark cluster image version lists Stay organized with collections  Save and categorize content based on your preferences. 

"Ubuntu & Debian Based Image Version Clusters | Google Cloud"**Note:** Rollout of sub-minor versions without pre-configured channels begins on June 22, 2026. Before August 25, 2026, these versions won't be selected by default unless you pin your image versions. You can use the pre-August 25, 2026 period to test and verify your workloads on the new images. After August 25, 2026, the non-configured versions will become the default.

Google Managed Service for Apache Spark uses Ubuntu, Debian, and Rocky Linux image versions to bundle operating system, big data components, and Google Cloud connectors into one package that is deployed on a cluster. For more information, see [Managed Service for Apache Spark Versioning](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview).

Notes:

  * Managed Service for Apache Spark image versions are supported for 24 months after their initial release.
  * Generally, Managed Service for Apache Spark image versions are available for 24 months after their end-of-support date, but an availability period can shorten if an image support date is extended.

**Note:** On August 25, 2026, 1.x and 2.0 image versions will become unavailable for use in creating clusters (see "Available until" dates in unsupported image versions). To avoid cluster creation issues, obtain the benefits of the latest features, and qualify for Google support, [recreate and update existing clusters](https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster) to use the latest supported image versions.

## Default Managed Service for Apache Spark image version

Managed Service for Apache Spark updates the default image version to the latest generally available Debian-based Managed Service for Apache Spark after its General availability (GA) release date.

## Supported Managed Service for Apache Spark image versions

Managed Service for Apache Spark prevents the creation of clusters with image versions prior to 1.3.95, 1.4.77, 1.5.53, and 2.0.27, which were affected by [Apache Log4j security vulnerabilities](https://logging.apache.org/log4j/2.x/security.html) Managed Service for Apache Spark also prevents cluster creation for Managed Service for Apache Spark image versions 0.x, 1.0.x, 1.1.x, and 1.2.x. Managed Service for Apache Spark advises that, when possible, you create Managed Service for Apache Spark clusters with the latest sub-minor image versions. See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for specific image and `log4j` update information.

### Debian images

The following **Debian-based** image versions are supported in Managed Service for Apache Spark clusters. Note that new clusters will be created to include any sub-minor patches that have been made to a version since its release.

When creating a Debian-based cluster, you can omit the image version OS Distribution Code suffix, for example by specifying `2.3` to select the `2.3-debian12` image. The OS suffix **must** be used to select a Rocky Linux or Ubuntu-based image, for example by specifying `2.3-ubuntu22`. See [Selecting versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview#select_versions) for image selection examples. Version | Last updated | Released on | Supported until | Available until | Notes  
---|---|---|---|---|---  
[3.0-debian13](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-3.0) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2026/07/15](https://docs.cloud.google.com/managed-spark/docs/release-notes#July%2015,%202026) | 2028/07/15 | 2030/07/15 | General availability release.  
[2.3-debian12](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.3) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2025/06/09](https://docs.cloud.google.com/managed-spark/docs/release-notes#June_09_2025) | 2027/06/09 | 2029/06/09 | General availability release.  
[2.2-debian12](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.2) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2023/12/08](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_11_2023) | 2027/03/31 | 2027/12/31 | General availability release. Image version `2.2` becomes the default image version on September, 13, 2024.  
[2.1-debian11](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.1) | [2026/09/04](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_04_2026) | [2022/12/12](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_12_2022) | 2026/03/31 | 2026/12/31 | General availability release.  
  
### Ubuntu images

The following **Ubuntu LTS-based** image versions are supported in Managed Service for Apache Spark clusters. Note that new clusters will be created to include any sub-minor patches that have been made to a version since its release.

Version | Last updated | Released on | Supported until | Available until | Notes  
---|---|---|---|---|---  
[3.0-ubuntu24](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-3.0) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2026/07/15](https://docs.cloud.google.com/managed-spark/docs/release-notes#July%2015,%202026) | 2028/07/15 | 2030/07/15 | General availability release.  
[2.3-ubuntu22](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.3) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2025/06/09](https://docs.cloud.google.com/managed-spark/docs/release-notes#June_09_2025) | 2027/06/09 | 2029/06/09 | General availability release.  
[2.2-ubuntu22](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.2) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2023/12/08](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_11_2023) | 2027/03/31 | 2027/12/31 | General availability release.  
[2.1-ubuntu20](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.1) | [2026/09/04](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_04_2026) | [2022/12/12](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_12_2022) | 2026/03/31 | 2026/12/31 | General availability release.  
  
### Rocky Linux images

The following **Rocky Linux-based** image versions are supported in Managed Service for Apache Spark clusters. Note that new clusters will be created to include any sub-minor patches that have been made to a version since its release.

Version | Last updated | Released on | Supported until | Available until | Notes  
---|---|---|---|---|---  
[3.0-rocky9](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-3.0) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2026/07/15](https://docs.cloud.google.com/managed-spark/docs/release-notes#July%2015,%202026) | 2028/07/15 | 2030/07/15 | General availability release.  
[2.3-rocky9](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.3) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2025/06/09](https://docs.cloud.google.com/managed-spark/docs/release-notes#June_09_2025) | 2027/06/09 | 2029/06/09 | General availability release.  
[2.2-rocky9](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.2) | [2026/09/30](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_30_2026) | [2023/12/08](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_11_2023) | 2027/03/31 | 2027/12/31 | General availability release.  
[2.1-rocky8](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.1) | [2026/09/04](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_04_2026) | [2022/12/12](https://docs.cloud.google.com/managed-spark/docs/release-notes#December_12_2022) | 2026/03/31 | 2026/12/31 | General availability release.  
  
## Unsupported Managed Service for Apache Spark image versions

[Click this link](https://docs.cloud.google.com/static/managed-spark/docs/concepts/versioning/check-unsupported-dataproc-clusters.sh) to download a script you can run to check if your project or organization is using an unsupported Managed Service for Apache Spark image. 

The following Managed Service for Apache Spark versions are unsupported. Managed Service for Apache Spark does not provide updates and support for clusters created with these versions. Versions 1.x and 2.0 will reach end-of-life on August 25, 2026. If you are running on unsupported versions, you need to upgrade your clusters to supported images.

Version | Includes | Released On | Last Updated | Available until | Notes  
---|---|---|---|---|---  
`2.0-debian10/-ubuntu18/-rocky8` | Apache Spark 3.1.3  
Apache Hadoop 3.2.4  
Apache Pig 0.18.0-SNAPSHOT  
Apache Hive 3.1.3  
Cloud Storage connector 2.2.30-hadoop3  
Python 3.8  
Scala 2.12.14  
Zookeeper 3.4.14  
| 2021/01/22:debian10/ubuntu18  
2022/02/18:rocky8 | 2026/02/24 | 2026/08/25 | Unsupported as of 2026/02/24.  
2.0.160-debian10/-ubuntu18/-rocky8 was the final released version.  
`2.0-centos8` | Apache Spark 3.1.2  
Apache Hadoop 3.2.2  
Apache Pig 0.18.0-SNAPSHOT  
Apache Hive 3.1.2  
Cloud Storage connector 2.2.4-hadoop3  
Python 3.8  
Scala 2.12.14  
Zookeeper 3.4.14  
| 2021/03/16 | 2022/02/01 | 2026/08/25 | Unsupported as of 2022/02/01.  
2.0.30-centos8 was the final released version.  
`1.5-debian10/-ubuntu18/-rocky8` | Apache Spark 2.4.8  
Apache Hadoop 2.10.2  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 2.1.9-hadoop2  
Python 3.7  
Scala 2.12.10  
Zookeeper 3.4.14  
| 2020/03/25:debian10/ubuntu18  
2022/02/18:rocky8 | 2023/04/28 | 2026/08/25 | Unsupported as of 2023/04/28.  
1.5.89-debian10/-ubuntu18/-rocky8 was the final released version.  
`1.5-centos8` | Apache Spark 2.4.8  
Apache Hadoop 2.10.1  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 2.1.5-hadoop2  
Python 3.7  
Scala 2.12.10  
Zookeeper 3.4.14  
| 2020/12/14 | 2022/02/01 | 2026/08/25 | Unsupported as of 2022/02/01.  
1.5.56-centos8 was the final released version.  
`1.4-debian10/-ubuntu18` | Apache Spark 2.4.8  
Apache Hadoop 2.9.2  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 1.9.18-hadoop2  
Python 3.6  
Scala 2.11.12  
Zookeeper 3.4.14  
| 2019/03/22 | 2022/02/01 | 2026/08/25 | Unsupported as of 2022/02/01.  
1.4.80-debian10/-ubuntu18 was the final released version.  
`1.4-debian9` | Apache Spark 2.4.5  
Apache Hadoop 2.9.2  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 1.9.17-hadoop2  
Python 3.6  
Scala 2.11.12  
Zookeeper 3.4.13  
| 2019/03/22 | 2020/07/10 | 2026/08/25 | Unsupported as of 2020/07/10.  
1.4.33-debian9 was the final released version.  
`1.3-debian10/-ubuntu18` | Apache Spark 2.3.4  
Apache Hadoop 2.9.2  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 1.9.18-hadoop2  
Python 2.7  
Scala 2.11.8  
Zookeeper 3.4.13  
| 2018/06/29 | 2021/12/22 | 2026/08/25 | Unsupported as of 2021/08/01.  
1.3.95-debian10/-ubuntu18 was the final released version, which has log4j2 vulnerabilities addressed. **Note: previously released versions are vulnerable and must be upgraded.**  
`1.3-debian9` | Apache Spark 2.3.4  
Apache Hadoop 2.9.2  
Apache Pig 0.17.0  
Apache Hive 2.3.7  
Cloud Storage connector 1.9.17-hadoop2  
Python 2.7  
Scala 2.11.8  
Zookeeper 3.4.13  
| 2018/06/29 | 2020/07/10 | 2026/08/25 | Unsupported as of 2020/07/10.  
1.3.62-debian9 was the final released version.  
`1.2-debian9` | Apache Spark 2.2.3  
Apache Hadoop 2.8.5  
Apache Pig 0.16.0  
Apache Hive 2.1.1  
Cloud Storage connector 1.6.10-hadoop2  
BigQuery connector 0.10.11-hadoop2  
Python 2.7  
Scala 2.11.8  
Zookeeper 3.4.13  
| 2017/07/21 | 2020/07/10 | Unavailable | Unsupported as of 2020/07/10.  
1.2.102-debian9 was the final released version.  
`1.1-debian9` | Apache Spark 2.0.2  
Apache Hadoop 2.7.7  
Apache Pig 0.16.0  
Apache Hive 2.1.1  
Cloud Storage connector 1.6.10-hadoop2  
BigQuery connector 0.10.11-hadoop2 | 2016/08/08 | 2019/09/26 | Unavailable | Unsupported as of 2019/10/01.  
1.1.121-debian9 is the final released version.  
`1.0-debian9` | Apache Spark 1.6.2  
Apache Hadoop 2.7.4  
Apache Pig 0.15.0  
Apache Hive 1.2.1  
Cloud Storage connector 1.6.10-hadoop2  
BigQuery connector 0.10.11-hadoop2 | 2016/02/22 | 2019/05/09 | Unavailable | GA image first release.  
Unsupported as of 2019/04/01.  
1.0.119-debian9 was the final released version.  
`0.2` | Apache Spark 1.5.2  
Apache Hadoop 2.7.1  
Apache Pig 0.15.0  
Apache Hive 1.2.1  
Cloud Storage connector 1.5.1-hadoop2  
BigQuery connector 0.7.7-hadoop2 | 2015/11/18 | 2016/08/02 | Unavailable | Beta image second release.  
`0.1` | Apache Spark 1.5.0  
Apache Hadoop 2.7.1  
Apache Pig 0.14.10  
Apache Hive 1.0  
Cloud Storage connector 1.5.1-hadoop2  
BigQuery connector 0.7.7-hadoop2 | 2015/09/23 | 2016/08/02 | Unavailable | Managed Service for Apache Spark beta release.  
Spark 1.5 has been compiled against Hive 1.2.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
