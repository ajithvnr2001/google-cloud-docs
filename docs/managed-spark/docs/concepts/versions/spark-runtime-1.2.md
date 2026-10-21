---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-1.2
title: Managed Service for Apache Spark runtime 1.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:13.004766+00:00
---

# Managed Service for Apache Spark runtime 1.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-1.2

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark runtime 1.2 Stay organized with collections  Save and categorize content based on your preferences. 

See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for the latest Managed Service for Apache Spark runtime update notices.

## Spark runtime version 1.2 components

Component | [1.2.89  
2026/09/23](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_23_2026) | [1.2.86  
2026/08/12](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_12_2026)  
[](https://docs.cloud.google.com/managed-spark/docs/release-notes#November_11_2022) | [1.2.85  
2026/08/07](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_07_2026) | [1.2.82  
2026/06/09](https://docs.cloud.google.com/managed-spark/docs/release-notes#June_09_2026) | [1.2.80  
2026/05/11](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#May_11_2026)  
---|---|---|---|---|---  
[**Apache Spark Note 1**](https://spark.apache.org/) | [3.5.1](https://spark.apache.org/releases/spark-release-3-5-1.html) | [3.5.1](https://spark.apache.org/releases/spark-release-3-5-1.html) | [3.5.1](https://spark.apache.org/releases/spark-release-3-5-1.html) | [3.5.1](https://spark.apache.org/releases/spark-release-3-5-1.html) | [3.5.1](https://spark.apache.org/releases/spark-release-3-5-1.html)  
[**Cloud Storage Connector**](https://github.com/GoogleCloudDataproc/hadoop-connectors/tree/master/gcs) | [3.0.3](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.0.3) | [3.0.3](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.0.3) | [3.0.3](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.0.3) | [3.0.3](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.0.3) | [3.0.3](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.0.3)  
[**BigQuery Connector**](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.36.4](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.36.4](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.36.4](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.36.4](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.36.4](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases)  
[**Java**](https://www.oracle.com/java/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/)  
[**Conda**](https://docs.conda.io/en/latest/) | [24.1](https://docs.conda.io/projects/conda/en/latest/release-notes.html) | [24.1](https://docs.conda.io/projects/conda/en/latest/release-notes.html) | [24.1](https://docs.conda.io/projects/conda/en/latest/release-notes.html) | [24.1](https://docs.conda.io/projects/conda/en/latest/release-notes.html) | [24.1](https://docs.conda.io/projects/conda/en/latest/release-notes.html)  
[**Python**](https://www.python.org/) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html) | [3.12](https://docs.python.org/3/whatsnew/3.12.html)  
[**R**](https://www.r-project.org/about.html) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/)  
[**Scala**](https://www.scala-lang.org/) | [2.12](https://github.com/scala/scala/releases) | [2.12](https://github.com/scala/scala/releases) | [2.12](https://github.com/scala/scala/releases) | [2.12](https://github.com/scala/scala/releases) | [2.12](https://github.com/scala/scala/releases)  
  
**Notes:**

1\. The Managed Service for Apache Spark `1.2` runtime uses the `UTF-8` default character encoding.

## Spark runtime 1.2 libraries

Managed Service for Apache Spark provides a pre-installed environment for machine learning and data science with popular libraries such as [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [XGBoost](https://www.nvidia.com/en-us/glossary/xgboost/).

The following sections list the library versions that are available in Managed Service for Apache Spark runtime version `1.2`.

### GPU-specific libraries

For Managed Service for Apache Spark batch workloads that use GPU VMs, the following NVIDIA driver and libraries are available in the Managed Service for Apache Spark container. You can use them to accomplish the following tasks:

  * Accelerate Spark batch workloads with the [NVIDIA cuDF for Apache Spark library](https://docs.nvidia.com/cudf-spark/latest/index.html)
  * Train machine learning workloads
  * Run distributed batch inference using Spark

Package Name | Version  
---|---  
Spark cuDF | 24.04.0  
NVIDIA Driver | 550.127.05  
CUDA | 12.6  
cublas | 12.8.4  
cusolver | 11.7.3  
cupti | 12.8  
cusparse | 12.5.8  
cuDNN | 9.2  
NCCL | 2.22  
  
### XGBoost libraries

The following [Maven package versions](https://mvnrepository.com/artifact/ml.dmlc) are available in Managed Service for Apache Spark runtime version `1.2` to use [XGBoost](https://www.nvidia.com/en-us/glossary/xgboost/) with Spark in Java or Scala.

Group ID | Package Name | Version  
---|---|---  
ml.dmlc | xgboost4j-gpu_2.12 | 2.0.3  
ml.dmlc | xgboost4j-spark-gpu_2.12 | 2.0.3  
**Note:** You cannot use distributed Spark XGBoost on a Managed Service for Apache Spark batch workload that has [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) enabled (the default behavior) because new nodes that start elastic scaling cannot receive new tasks and remain idle. To use XGBoost with a batch workload, you can set the [`spark.dynamicAllocation.enabled = false`](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties) property on a batch workload to disable dynamic allocation.

### Python libraries

The following Python library versions are included in Managed Service for Apache Spark runtime version `1.2`.

serverless-spark-1.2-debian-12 python librariesPackage Name | Version  
---|---  
accelerate | 0.33  
bigframes | 1.7  
cookiecutter | 2.6  
cython | 3.0  
dask | 2024.5  
deepspeed | 0.14  
delta-spark | 3.2  
evaluate | 0.4  
fastavro | 1.9  
fastparquet | 2024.2  
gcsfs | 2024.5  
git | 2.45  
google-auth-oauthlib | 1.2  
google-cloud-aiplatform | 1.60  
google-cloud-bigquery | 3.23  
google-cloud-bigquery-storage | 2.25  
google-cloud-bigtable | 2.23  
google-cloud-container | 2.45  
google-cloud-datacatalog | 3.19  
google-cloud-dataproc | 5.9  
google-cloud-datastore | 2.19  
google-cloud-dlp | 3.22  
google-cloud-language | 2.13  
google-cloud-logging | 3.10  
google-cloud-monitoring | 2.21  
google-cloud-pubsub | 2.21  
google-cloud-redis | 2.15  
google-cloud-secret-manager | 2.20  
google-cloud-spanner | 3.46  
google-cloud-speech | 2.26  
google-cloud-storage | 2.16  
google-cloud-texttospeech | 2.16  
google-cloud-translate | 3.15  
google-cloud-vision | 3.7  
httplib2 | 0.22  
huggingface_hub | 0.27  
ipyparallel | 8.8  
ipython-sql | 0.3  
ipywidgets | 8.1  
jupyter_http_over_ws | 0.0  
jupyterlab | 4.1  
jupyterlab-git | 0.50  
keyrings.google-artifactregistry-auth | 1.1  
langchain | 0.2  
lightgbm | 4.5  
markdown | 3.6  
matplotlib | 3.8  
nbclassic | 1.0  
nbconvert | 7.16  
nbdime | 4.0  
nltk | 3.8  
nodejs | 20.12  
numba | 0.59  
numpy | 1.26  
oauth2client | 4.1  
onnx | 1.16  
openblas | 0.3  
opencv | 4.9  
orc | 2.0  
pandas | 2.2  
papermill | 2.6  
pyarrow | 15.0  
pydot | 2.0  
pyhive | 0.7  
pymongo | 4.7  
pynvml | 11.5  
pytables | 3.9  
pytorch-cpu | 2.3  
regex | 2024.5  
requests | 2.31  
rtree | 1.2  
scikit-image | 0.22  
scikit-learn | 1.5  
scipy | 1.11  
seaborn | 0.12  
sentence-transformers | 3.0  
shap | 0.45  
spark-tensorflow-distributor | 1.0  
sparksql-magic= | 0.0.3  
sqlalchemy | 2.0  
sympy | 1.12  
tokenizers | 0.19  
torcheval | 0.0.7  
torchvision | 0.18  
toree | 0.5  
tornado | 6.4  
transformers | 4.43  
uritemplate | 4.1  
virtualenv | 20.26  
wordcloud | 1.9  
xgboost | 2.0  
ydata-profiling | 4.8  
  
### R libraries

The following R library versions are included in Managed Service for Apache Spark runtime version `1.2`.

serverless-spark-1.2-debian-12 r librariesPackage Name | Version  
---|---  
askpass | 1.2  
assertthat | 0.2  
backports | 1.5  
bit | 4.0  
bit64 | 4.0  
blob | 1.2  
boot | 1.3_30  
brew | 1.0_10  
broom | 1.0  
callr | 3.7  
caret | 6.0_94  
cellranger | 1.1  
chron | 2.3_61  
class | 7.3_22  
cli | 3.6  
clipr | 0.8  
cluster | 2.1  
codetools | 0.2_20  
colorspace | 2.1_0  
commonmark | 1.9  
cpp11 | 0.4  
crayon | 1.5  
curl | 5.1  
data.table | 1.15  
dbi | 1.2  
dbplyr | 2.5  
desc | 1.4  
devtools | 2.4  
digest | 0.6  
dplyr | 1.1  
ellipsis | 0.3  
evaluate | 0.23  
fansi | 1.0  
fastmap | 1.2  
forcats | 1.0  
foreach | 1.5  
foreign | 0.8_86  
fs | 1.6  
future | 1.33  
generics | 0.1  
ggplot2 | 3.5  
gh | 1.4  
glmnet | 4.1_8  
globals | 0.16  
glue | 1.7  
gower | 1.0  
gtable | 0.3  
haven | 2.5  
highr | 0.10  
hms | 1.1  
htmltools | 0.5.8  
htmlwidgets | 1.6  
httpuv | 1.6  
httr | 1.4  
hwriter | 1.3.2  
ini | 0.3  
ipred | 0.9_14  
isoband | 0.2  
iterators | 1.0  
jsonlite | 1.8  
kernsmooth | 2.23_24  
knitr | 1.46  
labeling | 0.4  
later | 1.3  
lattice | 0.22_6  
lava | 1.7  
lifecycle | 1.0  
listenv | 0.9  
lubridate | 1.9  
magrittr | 2.0  
markdown | 1.12  
mass | 7.3_60  
matrix | 1.6_5  
memoise | 2.0  
mgcv | 1.9_1  
mime | 0.12  
modelmetrics | 1.2.2  
modelr | 0.1  
munsell | 0.5  
nlme | 3.1_164  
nnet | 7.3_19  
numderiv | 2016.8_1  
openssl | 2.2  
pillar | 1.9  
pkgbuild | 1.4  
pkgconfig | 2.0  
pkgload | 1.3  
plogr | 0.2  
plyr | 1.8  
praise | 1.0  
prettyunits | 1.2  
processx | 3.8  
prodlim | 2023.08  
progress | 1.2  
promises | 1.3  
proto | 1.0  
ps | 1.7  
purrr | 1.0  
r6 | 2.5  
randomforest | 4.7_1  
rappdirs | 0.3  
rcmdcheck | 1.4  
rcolorbrewer | 1.1_3  
rcpp | 1.0  
rcurl | 1.98_1  
readr | 2.1  
readxl | 1.4  
recipes | 1.0  
rematch | 2.0  
remotes | 2.5  
reprex | 2.1  
reshape2 | 1.4  
rlang | 1.1  
rmarkdown | 2.27  
rodbc | 1.3_23  
roxygen2 | 7.3  
rpart | 4.1  
rprojroot | 2.0  
rserve | 1.8_7  
rsqlite | 2.3  
rstudioapi | 0.16  
rvest | 1.0  
scales | 1.3  
selectr | 0.4_2  
sessioninfo | 1.2  
shape | 1.4.6  
shiny | 1.8.1  
sourcetools | 0.1  
spatial | 7.3_17  
squarem | 2021.1  
stringi | 1.8  
stringr | 1.5  
survival | 3.6_4  
sys | 3.4  
teachingdemos | 2.12  
testthat | 3.2.1  
tibble | 3.2  
tidyr | 1.3  
tidyselect | 1.2  
tidyverse | 2.0  
timedate | 4032.109  
tinytex | 0.51  
usethis | 2.2  
utf8 | 1.2  
uuid | 1.2_0  
vctrs | 0.6  
whisker | 0.4  
withr | 3.0  
xfun | 0.44  
xml2 | 1.3  
xopen | 1.0  
xtable | 1.8_4  
yaml | 2.3  
zip | 2.3  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
