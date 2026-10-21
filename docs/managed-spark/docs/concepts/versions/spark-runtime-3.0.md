---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-3.0
title: Managed Service for Apache Spark runtime 3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:23.320712+00:00
---

# Managed Service for Apache Spark runtime 3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-3.0

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark runtime 3.0 Stay organized with collections  Save and categorize content based on your preferences. 

See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for the latest Managed Service for Apache Spark runtime update notices.

## Spark runtime version 3.0 components

Component | [3.0.14  
2026/08/25](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_25_2026) | [3.0.13  
2026/03/27](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#March_27_2026)  
[](https://docs.cloud.google.com/managed-spark/docs/release-notes#November_11_2022) | [3.0.12  
2026/03/20](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#March_20_2026) | [3.0.11  
2026/03/13](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#March_13_2026) | [3.0.10  
2026/03/06](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#March_06_2026)  
---|---|---|---|---|---  
[**Apache Spark**](https://spark.apache.org/) | [4.0.1](https://spark.apache.org/releases/spark-release-4-0-1.html) | [4.0.1](https://spark.apache.org/releases/spark-release-4-0-1.html) | [4.0.1](https://spark.apache.org/releases/spark-release-4-0-1.html) | [4.0.0](https://spark.apache.org/releases/spark-release-4-0-0.html) | [4.0.0](https://spark.apache.org/releases/spark-release-4-0-0.html)  
[**Cloud Storage Connector**](https://github.com/GoogleCloudDataproc/hadoop-connectors/tree/master/gcs) | [3.1.16](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.16) | [3.1.9](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.9) | [3.1.9](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.9) | [3.1.9](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.9) | [3.1.9](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.9)  
[**BigQuery Connector**](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.44.0](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.44.0](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.44.0](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.43.1-preview](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.43.1-preview](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases)  
[**Java**](https://www.oracle.com/java/) | [21](https://jdk.java.net/21/) | [21](https://jdk.java.net/21/) | [21](https://jdk.java.net/21/) | [21](https://jdk.java.net/21/) | [21](https://jdk.java.net/21/)  
[**Python**](https://www.python.org/) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html)  
[**Scala**](https://www.scala-lang.org/) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases)  
  
**Notes:**

  * The `3.0` runtime uses the `UTF-8` as a default character encoding.

  * `3.0` runtime new features and improvements:

    * Regional and multi-zonal workloads are used by default to increase obtainability of compute resources
    * Faster startup than previous runtimes
    * Fast resource cleanup that allows faster release of VPC IPs after workload completion
    * End-user credentials are used for all workloads by default
    * New `bigquery` Spark catalog, pre-configured for out-of-the-box BigQuery native table interactions
    * New Spark Serverless-specific IAM roles
    * New `dataprocrm.googleapis.com` API enablement is required
  * `3.0` runtime unsupported and deprecated functionality:

    * `3.0` runtimes don't support [Lightning Engine](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless) and [Native Query Execution](https://docs.cloud.google.com/managed-spark/docs/guides/lightning-engine-serverless#native_query_execution).

    * `3.0`\+ runtimes don't use Cloud Storage [staging](https://docs.cloud.google.com/managed-spark/docs/concepts/staging-bucket-serverless) buckets.

    * The Persistent History Server (PHS) is not supported. Instead, use the [Spark UI](https://docs.cloud.google.com/managed-spark/docs/guides/monitor-troubleshoot-batches#spark_ui).

    * SparkR batches are not supported. Instead, use [`sparklyr`](https://spark.posit.co).

    * Jupyter sessions are not supported. Instead, use [Spark Connect sessions](https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client), the industry standard for interactive Spark development.




## Python libraries

**Note:** You can't use distributed Spark XGBoost on a Managed Service for Apache Spark batch workload that has [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) enabled (the default behavior) because new nodes that start elastic scaling can't receive new tasks and remain idle.

To use XGBoost with a batch workload, you can set the [`spark.dynamicAllocation.enabled = false`](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties) property on a batch workload to disable dynamic allocation.

serverless-spark-3.0-debian-12 python librariesPackage Name | Version  
---|---  
accelerate | 1.11  
bigframes | 2.24  
cookiecutter | 2.6  
cuda | 12.9  
cudnn | 9.10  
cython | 3.1  
dask | 2025.10  
dataproc-spark-connect | 1.0.0  
dataproc-ml | 1.0.0rc1  
datasets | 4.0  
deepspeed | 0.17  
delta-spark | 4.0.0  
evaluate | 0.4  
fastavro | 1.12  
fastparquet | 2024.11  
gcsfs | 2025.3  
git | 2.51  
google-auth-oauthlib | 1.2  
google-cloud-aiplatform | 1.121  
google-cloud-bigquery | 3.38  
google-cloud-bigquery-storage | 2.32  
google-cloud-bigtable | 2.34  
google-cloud-container | 2.59  
google-cloud-datacatalog | 3.27  
google-cloud-dataproc | 5.22  
google-cloud-datastore | 2.21  
google-cloud-dlp | 3.32  
google-cloud-language | 2.17  
google-cloud-logging | 3.12  
google-cloud-monitoring | 2.28  
google-cloud-pubsub | 2.31  
google-cloud-redis | 2.18  
google-cloud-secret-manager | 2.25  
google-cloud-spanner | 3.59  
google-cloud-speech | 2.33  
google-cloud-storage | 2.19  
google-cloud-texttospeech | 2.31  
google-cloud-translate | 3.21  
google-cloud-vision | 3.10  
httplib2 | 0.31  
huggingface_hub | 0.36  
ipyparallel | 9.0  
keyrings.google-artifactregistry-auth | 1.1  
langchain | 1.0  
lightgbm | 4.6  
mamba | 2.3  
markdown | 3.9  
nccl | 2.27  
nltk | 3.9  
nodejs | 24.9  
numba | 0.61  
numpy | 2.1  
oauth2client | 4.1  
onnx | 1.17  
openblas | 0.3  
opencv | 4.11  
orc | 2.1  
pandas | 2.3  
pyarrow | 19.0  
pydot | 4.0  
pyhive | 0.7  
pyiceberg | 0.10  
pymongo | 4.15  
pynvml | 13.0  
pytables | 3.10  
python | 3.12  
pytorch-gpu | 2.6  
regex | 2025.10  
requests | 2.32  
rtree | 1.4  
scikit-image | 0.25  
scikit-learn | 1.7  
scipy | 1.15  
seaborn | 0.13  
sentence-transformers | 5.1  
shap | 0.48  
spark-tensorflow-distributor | 1.0  
spacy | 3.8  
sqlalchemy | 2.0  
statsforecast | 2.0  
sympy | 1.14  
tensorflow-gpu | 2.18  
torcheval | 0.0.7  
torch | 2.6  
torchvision | 0.21  
tornado | 6.5  
transformers | 4.57  
uritemplate | 4.2  
virtualenv | 20.35  
wordcloud | 1.9  
xgboost | 3.0.4  
ydata-profiling | 4.17  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
