---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.3
title: Managed Service for Apache Spark runtime 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:14.022524+00:00
---

# Managed Service for Apache Spark runtime 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-2.3

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark runtime 2.3 Stay organized with collections  Save and categorize content based on your preferences. 

See the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for the latest Managed Service for Apache Spark runtime update notices.

## Spark runtime version 2.3 components

Component | [2.3.42  
2026/09/23](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_23_2026) | [2.3.39  
2026/08/12](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_12_2026)  
[](https://docs.cloud.google.com/managed-spark/docs/release-notes#November_11_2022) | [2.3.38  
2026/08/07](https://docs.cloud.google.com/managed-spark/docs/release-notes#August_07_2026) | [2.3.35  
2026/06/09](https://docs.cloud.google.com/managed-spark/docs/release-notes#June_09_2026) | [2.3.33  
2026/05/11](https://docs.cloud.google.com/dataproc-serverless/docs/release-notes#May_11_2026)  
---|---|---|---|---|---  
[**Apache Spark**](https://spark.apache.org/) | [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) | [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) | [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) | [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html) | [3.5.3](https://spark.apache.org/releases/spark-release-3-5-3.html)  
[**Cloud Storage Connector**](https://github.com/GoogleCloudDataproc/hadoop-connectors/tree/master/gcs) | [3.1.2](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.2) | [3.1.2](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.2) | [3.1.2](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.2) | [3.1.2](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.2) | [3.1.2](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v3.1.2)  
[**BigQuery Connector**](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases) | [0.42.3](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.42.3) | [0.42.3](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.42.3) | [0.42.3](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.42.3) | [0.42.3](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.42.3) | [0.42.3](https://github.com/GoogleCloudDataproc/spark-bigquery-connector/releases/tag/0.42.3)  
[**Java**](https://www.oracle.com/java/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/) | [17](https://jdk.java.net/17/)  
[**Python**](https://www.python.org/) | [Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | [Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | [Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | [Python 3.11](https://docs.python.org/3/whatsnew/3.11.html) | [Python 3.11](https://docs.python.org/3/whatsnew/3.11.html)  
[**R**](https://www.r-project.org/about.html) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/) | [4.3](https://cran.r-project.org/src/base/R-4/)  
[**Scala**](https://www.scala-lang.org/) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases) | [2.13](https://github.com/scala/scala/releases)  
  
**Notes:**

  * The `2.3` runtime uses the `UTF-8` default character encoding.



## Spark runtime 2.3 libraries

Learning libraries, such [TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), and [XGBoost](https://www.nvidia.com/en-us/glossary/xgboost/), and offer a ready-to-use environment for machine learning and data science applications.

The following sections list the library versions that are available in Managed Service for Apache Spark runtime version `2.3`.

### GPU-specific libraries

For Managed Service for Apache Spark batch workloads that use GPU VMs, the following NVIDIA driver and libraries are available in the Managed Service for Apache Spark container. You can use them to accomplish the following tasks:

  * Accelerate Spark batch workloads with the [NVIDIA cuDF for Apache Spark library](https://docs.nvidia.com/cudf-spark/latest/index.html)
  * Train machine learning workloads
  * Run distributed batch inference using Spark

Package Name | Version  
---|---  
Spark cuDF | 25.02.1  
NVIDIA Driver | 570.133.20  
CUDA | 12.9  
cublas | 12.9.0  
cusolver | 11.7.4  
cupti | 12.9  
cusparse | 12.5.9  
cuDNN | 9.10  
NCCL | 2.26  
  
### XGBoost libraries

The following [Maven package versions](https://mvnrepository.com/artifact/ml.dmlc) are available in Managed Service for Apache Spark runtime version `2.3` to use [XGBoost](https://www.nvidia.com/en-us/glossary/xgboost/) with Spark in Java or Scala.

Group ID | Package Name | Version  
---|---|---  
ml.dmlc | xgboost4j-gpu_2.13 | 2.1.4  
ml.dmlc | xgboost4j-spark-gpu_2.13 | 2.1.4  
**Note:** You cannot use distributed Spark XGBoost on a Managed Service for Apache Spark batch workload that has [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling) enabled (the default behavior) because new nodes that start elastic scaling cannot receive new tasks and remain idle. To use XGBoost with a batch workload, you can set the [`spark.dynamicAllocation.enabled = false`](https://docs.cloud.google.com/managed-spark/docs/concepts/autoscaling#spark_dynamic_allocation_properties) property on a batch workload to disable dynamic allocation.

### Python libraries

The following Python library versions are included in Managed Service for Apache Spark runtime version `2.3`.

serverless-spark-2.2-debian-12 python librariesPackage Name | Version  
---|---  
accelerate | 1.7  
bigframes | 2.4  
cookiecutter | 2.6  
cython | 3.1  
dask | 2025.5  
datasets | 3.6  
deepspeed | 0.16  
delta-spark | 3.2  
evaluate | 0.4  
fastavro | 1.9  
fastparquet | 2024.11  
gcsfs | 2025.3  
git | 2.49  
google-auth-oauthlib | 1.2  
google-cloud-aiplatform | 1.94  
google-cloud-bigquery | 3.33  
google-cloud-bigquery-storage | 2.31  
google-cloud-bigtable | 2.31  
google-cloud-container | 2.56  
google-cloud-datacatalog | 3.27  
google-cloud-dataproc | 5.18  
google-cloud-datastore | 2.21  
google-cloud-dlp | 3.29  
google-cloud-language | 2.17  
google-cloud-logging | 3.12  
google-cloud-monitoring | 2.27  
google-cloud-pubsub | 2.29  
google-cloud-redis | 2.18  
google-cloud-secret-manager | 2.23  
google-cloud-spanner | 3.54  
google-cloud-speech | 2.32  
google-cloud-storage | 2.19  
google-cloud-texttospeech | 2.27  
google-cloud-translate | 3.20  
google-cloud-vision | 3.10  
httplib2 | 0.22  
huggingface_hub | 0.31  
ipyparallel | 9.0  
ipython-sql | 0.3  
ipywidgets | 8.1  
jupyter_http_over_ws | 0.0  
jupyterlab | 4.4  
jupyterlab-git | 0.51  
keyrings.google-artifactregistry-auth | 1.1  
langchain | 0.3  
lightgbm | 4.6  
markdown | 3.8  
matplotlib | 3.9  
nbclassic | 1.3  
nbconvert | 7.16  
nbdime | 4.0  
nltk | 3.9  
nodejs | 22.13  
numba | 0.61  
numpy | 1.26  
oauth2client | 4.1  
onnx | 1.17  
openblas | 0.3  
opencv | 4.10  
orc | 2.0  
pandas | 2.2  
papermill | 2.6  
pyarrow | 15.0  
pydot | 4.0  
pyhive | 0.7  
pyiceberg | 0.9  
pymongo | 4.11  
pynvml | 12.0  
pytables | 3.10  
pytorch-gpu | 2.4  
regex | 2024.11  
requests | 2.32  
rtree | 1.4  
scikit-image | 0.25  
scikit-learn | 1.6  
scipy | 1.13  
seaborn | 0.13  
sentence-transformers | 4.1  
shap | 0.47  
spark-tensorflow-distributor | 1.0  
sparksql-magic | 0.0.3  
sqlalchemy | 2.0  
sympy | 1.14  
tokenizers | 0.21  
torcheval | 0.0.7  
torchvision | 0.19  
toree | 0.5  
tornado | 6.5  
transformers | 4.52  
uritemplate | 4.1  
virtualenv | 20.31  
wordcloud | 1.9  
xgboost | 2.1  
ydata-profiling | 4.16  
  
### R libraries

The following R library versions are included in Managed Service for Apache Spark runtime version `2.3`.

serverless-spark-2.2-debian-12 r librariesPackage Name | Version  
---|---  
askpass | 1.2  
assertthat | 0.2  
backports | 1.5  
bit | 4.6  
bit64 | 4.6  
blob | 1.2  
boot | 1.3_31  
brew | 1.0_10  
broom | 1.0  
callr | 3.7  
caret | 6.0_94  
cellranger | 1.1  
chron | 2.3_62  
class | 7.3_23  
cli | 3.6  
clipr | 0.8  
cluster | 2.1  
codetools | 0.2_20  
colorspace | 2.1_1  
commonmark | 1.9  
cpp11 | 0.5  
crayon | 1.5  
curl | 6.2  
data.table | 1.17  
dbi | 1.2  
dbplyr | 2.5  
desc | 1.4  
devtools | 2.4  
digest | 0.6  
dplyr | 1.1  
ellipsis | 0.3  
evaluate | 1.0  
fansi | 1.0  
fastmap | 1.2  
forcats | 1.0  
foreach | 1.5  
foreign | 0.8_90  
fs | 1.6  
future | 1.49  
generics | 0.1  
ggplot2 | 3.5  
gh | 1.4  
glmnet | 4.1_8  
globals | 0.18  
glue | 1.8  
gower | 1.0  
gtable | 0.3  
haven | 2.5  
highr | 0.11  
hms | 1.1  
htmltools | 0.5.8  
htmlwidgets | 1.6  
httpuv | 1.6  
httr | 1.4  
hwriter | 1.3.2  
ini | 0.3  
ipred | 0.9_15  
isoband | 0.2  
iterators | 1.0  
jsonlite | 2.0  
kernsmooth | 2.23_26  
knitr | 1.50  
labeling | 0.4  
later | 1.4  
lattice | 0.22_7  
lava | 1.8  
lifecycle | 1.0  
listenv | 0.9  
lubridate | 1.9  
magrittr | 2.0  
markdown | 2.0  
mass | 7.3_60  
matrix | 1.6_5  
memoise | 2.0  
mgcv | 1.9_3  
mime | 0.13  
modelmetrics | 1.2.2  
modelr | 0.1  
munsell | 0.5  
nlme | 3.1_168  
nnet | 7.3_20  
numderiv | 2016.8_1  
openssl | 2.3  
pillar | 1.10  
pkgbuild | 1.4  
pkgconfig | 2.0  
pkgload | 1.4  
plogr | 0.2  
plyr | 1.8  
praise | 1.0  
prettyunits | 1.2  
processx | 3.8  
prodlim | 2025.04  
progress | 1.2  
promises | 1.3  
proto | 1.0  
ps | 1.9  
purrr | 1.0  
r6 | 2.6  
randomforest | 4.7_1  
rappdirs | 0.3  
rcmdcheck | 1.4  
rcolorbrewer | 1.1_3  
rcpp | 1.0  
rcurl | 1.98_1  
readr | 2.1  
readxl | 1.4  
recipes | 1.3  
recommended | 4.3  
rematch | 2.0  
remotes | 2.5  
reprex | 2.1  
reshape2 | 1.4  
rlang | 1.1  
rmarkdown | 2.29  
rodbc | 1.3_25  
roxygen2 | 7.3  
rpart | 4.1  
rprojroot | 2.0  
rserve | 1.8_14  
rsqlite | 2.3  
rstudioapi | 0.17  
rvest | 1.0  
scales | 1.4  
selectr | 0.4_2  
sessioninfo | 1.2  
shape | 1.4.6  
shiny | 1.10  
sourcetools | 0.1  
spatial | 7.3_18  
squarem | 2021.1  
stringi | 1.8  
stringr | 1.5  
survival | 3.8_3  
sys | 3.4  
teachingdemos | 2.13  
testthat | 3.2  
tibble | 3.2  
tidyr | 1.3  
tidyselect | 1.2  
tidyverse | 2.0  
timedate | 4041.110  
tinytex | 0.57  
usethis | 3.1  
utf8 | 1.2  
uuid | 1.2_1  
vctrs | 0.6  
whisker | 0.4  
withr | 3.0  
xfun | 0.52  
xml2 | 1.3  
xopen | 1.0  
xtable | 1.8_4  
yaml | 2.3  
zip | 2.3  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
