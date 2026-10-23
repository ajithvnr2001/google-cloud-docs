---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/kafka-tutorial/
title: Stream a Kafka topic to Hive \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:54.532288+00:00
---

# Stream a Kafka topic to Hive  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/kafka-tutorial/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Stream a Kafka topic to Hive Stay organized with collections  Save and categorize content based on your preferences. 

[Apache Kafka](https://kafka.apache.org/documentation/) is an open source distributed streaming platform for real-time data pipelines and data integration. It provides an efficient and scalable streaming system for use in a variety of applications, including:

  * Real-time analytics
  * Stream processing
  * Log aggregation
  * Distributed messaging
  * Event streaming

See [Kafka use cases](https://kafka.apache.org/uses).

## Objectives

  1. Install Kafka on a [Managed Service for Apache Spark HA cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability#apache_zookeeper) with ZooKeeper (referred to in this tutorial as a "Managed Service for Apache Spark Kafka cluster").

  2. Create fictitious customer data, then publish the data to a Kafka topic.

  3. Create Hive parquet and ORC tables in Cloud Storage to receive streamed Kafka topic data.

  4. Submit a PySpark job to subscribe to and stream the Kafka topic into Cloud Storage in parquet and ORC format.

  5. Run a query on the streamed Hive table data to count the streamed Kafka messages.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Managed Service for Apache Spark](https://cloud.google.com/managed-spark/pricing)
  * [Compute Engine](https://cloud.google.com/compute/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

If you haven't already done so, create a Google Cloud project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage_component&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataproc, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,storage_component&redirect=https%3A//console.cloud.google.com)

  8. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  9. Click add_box **Create**. 
  10. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. In the **Choose where to store your data** section, do the following: 
        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
        2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following: 
        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  11. Click **Create**. 



## Tutorial steps

Perform the following steps to create a Managed Service for Apache Spark Kafka cluster to read a Kafka topic into Cloud Storage in parquet OR ORC format.

**Note:** In a production environment, some of tasks listed in the following sections are performed on separate clusters. For purposes of this tutorial, all tasks are performed on a single Managed Service for Apache Spark Kafka cluster.

### Copy the Kafka installation script to Cloud Storage

The `kafka.sh` [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) script installs Kafka on a Managed Service for Apache Spark cluster.

  1. Browse the code. 

Expand Me Collapse Me
         
         #!/bin/bash
         #    Copyright 2015 Google, Inc.
         #
         #    Licensed under the Apache License, Version 2.0 (the "License");
         #    you may not use this file except in compliance with the License.
         #    You may obtain a copy of the License at
         #
         #        http://www.apache.org/licenses/LICENSE-2.0
         #
         #    Unless required by applicable law or agreed to in writing, software
         #    distributed under the License is distributed on an "AS IS" BASIS,
         #    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         #    See the License for the specific language governing permissions and
         #    limitations under the License.
         #
         # This script installs Apache Kafka (http://kafka.apache.org) on a Google Cloud
         # Dataproc cluster.
         
         set -euxo pipefail
         
         readonly ZOOKEEPER_HOME=/usr/lib/zookeeper
         readonly KAFKA_HOME=/usr/lib/kafka
         readonly KAFKA_PROP_FILE='/etc/kafka/conf/server.properties'
         readonly ROLE="$(/usr/share/google/get_metadata_value attributes/dataproc-role)"
         readonly RUN_ON_MASTER="$(/usr/share/google/get_metadata_value attributes/run-on-master || echo false)"
         readonly KAFKA_ENABLE_JMX="$(/usr/share/google/get_metadata_value attributes/kafka-enable-jmx || echo false)"
         readonly KAFKA_JMX_PORT="$(/usr/share/google/get_metadata_value attributes/kafka-jmx-port || echo 9999)"
         readonly INSTALL_KAFKA_PYTHON="$(/usr/share/google/get_metadata_value attributes/install-kafka-python || echo false)"
         
         # The first ZooKeeper server address, e.g., "cluster1-m-0:2181".
         ZOOKEEPER_ADDRESS=''
         # Integer broker ID of this node, e.g., 0
         BROKER_ID=''
         
         function retry_apt_command() {
           cmd="$1"
           for ((i = 0; i < 10; i++)); do
             if eval "$cmd"; then
               return 0
             fi
             sleep 5
           done
           return 1
         }
         
         function recv_keys() {
           if [[ ${OS} == debian ]] && [[ $(echo "${DATAPROC_IMAGE_VERSION} >= 3.0" | bc -l) == 1 ]]; then
             retry_apt_command "apt-get update && apt-get install -y gnupg"
             export GNUPGHOME="$(mktemp -d)"
             trap 'rm -rf "${GNUPGHOME}"' EXIT
             gpg --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
             mkdir -p /etc/apt/trusted.gpg.d
             gpg --export B7B3B788A8D3785C > /etc/apt/trusted.gpg.d/mysql-repo.gpg
           else
             retry_apt_command "apt-get install -y gnupg2 && \
               apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C"
           fi
         }
         
         function update_apt_get() {
           retry_apt_command "apt-get update"
         }
         
         function install_apt_get() {
           pkgs="$@"
           retry_apt_command "apt-get install -y $pkgs"
         }
         
         function err() {
           echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
           return 1
         }
         
         # Returns the list of broker IDs registered in ZooKeeper, e.g., " 0, 2, 1,".
         function get_broker_list() {
           ${KAFKA_HOME}/bin/zookeeper-shell.sh "${ZOOKEEPER_ADDRESS}" \
             <<<"ls /brokers/ids" |
             grep '\[.*\]' |
             sed 's/\[/ /' |
             sed 's/\]/,/'
         }
         
         # Waits for zookeeper to be up or time out.
         function wait_for_zookeeper() {
           for i in {1..20}; do
             if "${ZOOKEEPER_HOME}/bin/zkCli.sh" -server "${ZOOKEEPER_ADDRESS}" ls /; then
               return 0
             else
               echo "Failed to connect to ZooKeeper ${ZOOKEEPER_ADDRESS}, retry ${i}..."
               sleep 5
             fi
           done
           echo "Failed to connect to ZooKeeper ${ZOOKEEPER_ADDRESS}" >&2
           exit 1
         }
         
         # Wait until the current broker is registered or time out.
         function wait_for_kafka() {
           for i in {1..20}; do
             local broker_list=$(get_broker_list || true)
             if [[ "${broker_list}" == *" ${BROKER_ID},"* ]]; then
               return 0
             else
               echo "Kafka broker ${BROKER_ID} is not registered yet, retry ${i}..."
               sleep 5
             fi
           done
           echo "Failed to start Kafka broker ${BROKER_ID}." >&2
           exit 1
         }
         
         function install_and_configure_kafka_server() {
           # Find zookeeper list first, before attempting any installation.
           local zookeeper_client_port
           zookeeper_client_port=$(grep 'clientPort' /etc/zookeeper/conf/zoo.cfg |
             tail -n 1 |
             cut -d '=' -f 2)
         
           local zookeeper_list
           zookeeper_list=$(grep '^server\.' /etc/zookeeper/conf/zoo.cfg |
             cut -d '=' -f 2 |
             cut -d ':' -f 1 |
             sort |
             uniq |
             sed "s/$/:${zookeeper_client_port}/" |
             xargs echo |
             sed "s/ /,/g")
         
           if [[ -z "${zookeeper_list}" ]]; then
             # Didn't find zookeeper quorum in zoo.cfg, but possibly workers just didn't
             # bother to populate it. Check if YARN HA is configured.
             zookeeper_list=$(bdconfig get_property_value --configuration_file \
               /etc/hadoop/conf/yarn-site.xml \
               --name yarn.resourcemanager.zk-address 2>/dev/null)
           fi
         
           # If all attempts failed, error out.
           if [[ -z "${zookeeper_list}" ]]; then
             err 'Failed to find configured Zookeeper list; try "--num-masters=3" for HA'
           fi
         
           ZOOKEEPER_ADDRESS="${zookeeper_list%%,*}"
         
           # Install Kafka from Dataproc distro.
           install_apt_get kafka-server || dpkg -l kafka-server ||
             err 'Unable to install and find kafka-server.'
         
           mkdir -p /var/lib/kafka-logs
           chown kafka:kafka -R /var/lib/kafka-logs
         
           if [[ "${ROLE}" == "Master" ]]; then
             # For master nodes, broker ID starts from 10,000.
             if [[ "$(hostname)" == *-m ]]; then
               # non-HA
               BROKER_ID=10000
             else
               # HA
               BROKER_ID=$((10000 + $(hostname | sed 's/.*-m-\([0-9]*\)$/\1/g')))
             fi
           else
             # For worker nodes, broker ID is a random number generated less than 10000.
             # 10000 is choosen since the max broker ID allowed being set is 10000.
             BROKER_ID=$((RANDOM % 10000))
           fi
           sed -i 's|log.dirs=/tmp/kafka-logs|log.dirs=/var/lib/kafka-logs|' \
             "${KAFKA_PROP_FILE}"
           sed -i 's|^\(zookeeper\.connect=\).*|\1'${zookeeper_list}'|' \
             "${KAFKA_PROP_FILE}"
           sed -i 's,^\(broker\.id=\).*,\1'${BROKER_ID}',' \
             "${KAFKA_PROP_FILE}"
           echo -e '\nreserved.broker.max.id=100000' >>"${KAFKA_PROP_FILE}"
           echo -e '\ndelete.topic.enable=true' >>"${KAFKA_PROP_FILE}"
         
           if [[ "${KAFKA_ENABLE_JMX}" == "true" ]]; then
             sed -i '/kafka-run-class.sh/i export KAFKA_JMX_OPTS="-Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=localhost -Djava.net.preferIPv4Stack=true"' /usr/lib/kafka/bin/kafka-server-start.sh
             sed -i "/kafka-run-class.sh/i export JMX_PORT=${KAFKA_JMX_PORT}" /usr/lib/kafka/bin/kafka-server-start.sh
           fi
         
           wait_for_zookeeper
         
           # Start Kafka.
           service kafka-server restart
         
           wait_for_kafka
         }
         
         function install_kafka_python_package() {
           KAFKA_PYTHON_PACKAGE="kafka-python==2.0.2"
           if [[ "${INSTALL_KAFKA_PYTHON}" != "true" ]]; then
             return
           fi
         
           if [[ "$(echo "${DATAPROC_IMAGE_VERSION} > 2.0" | bc)" -eq 1 ]]; then
             /opt/conda/default/bin/pip install "${KAFKA_PYTHON_PACKAGE}" || { sleep 10; /opt/conda/default/bin/pip install "${KAFKA_PYTHON_PACKAGE}"; }
           else
             OS=$(. /etc/os-release && echo "${ID}")
             if [[ "${OS}" == "rocky" ]]; then
               yum install -y python2-pip
             else
               apt-get install -y python-pip
             fi
             pip2 install "${KAFKA_PYTHON_PACKAGE}" || { sleep 10; pip2 install "${KAFKA_PYTHON_PACKAGE}"; } || { sleep 10; pip install "${KAFKA_PYTHON_PACKAGE}"; }
           fi
         }
         
         function remove_old_backports {
           # This script uses 'apt-get update' and is therefore potentially dependent on
           # backports repositories which have been archived.  In order to mitigate this
           # problem, we will remove any reference to backports repos older than oldstable
         
           # https://github.com/GoogleCloudDataproc/initialization-actions/issues/1157
           oldstable=$(curl -s https://deb.debian.org/debian/dists/oldstable/Release | awk '/^Codename/ {print $2}');
           stable=$(curl -s https://deb.debian.org/debian/dists/stable/Release | awk '/^Codename/ {print $2}');
         
           matched_files="$(grep -rsil '\-backports' /etc/apt/sources.list*)"
           if [[ -n "$matched_files" ]]; then
             for filename in "$matched_files"; do
               grep -e "$oldstable-backports" -e "$stable-backports" "$filename" || \
                 sed -i -e 's/^.*-backports.*$//' "$filename"
             done
           fi
         }
         
         function main() {
           OS=$(. /etc/os-release && echo "${ID}")
           if [[ ${OS} == debian ]] && [[ $(echo "${DATAPROC_IMAGE_VERSION} <= 2.1" | bc -l) == 1 ]]; then
             remove_old_backports
           fi
           recv_keys || err 'Unable to receive keys.'
           update_apt_get || err 'Unable to update packages lists.'
           install_kafka_python_package
         
           # Only run the installation on workers; verify zookeeper on master(s).
           if [[ "${ROLE}" == 'Master' ]]; then
             service zookeeper-server status ||
               err 'Required zookeeper-server not running on master!'
             if [[ "${RUN_ON_MASTER}" == "true" ]]; then
               # Run installation on masters.
               install_and_configure_kafka_server
             else
               # On master nodes, just install kafka command-line tools and libs but not
               # kafka-server.
               install_apt_get kafka ||
                 err 'Unable to install kafka libraries on master!'
             fi
           else
             # Run installation on workers.
             install_and_configure_kafka_server
           fi
         }
         
         main
         

  2. Copy the `kafka.sh` [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) script to your Cloud Storage bucket. This script installs Kafka on a Managed Service for Apache Spark cluster.

     1. Open [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), then run the following command: 
            
            gcloud storage cp gs://goog-dataproc-initialization-actions-REGION/kafka/kafka.sh gs://BUCKET_NAME/scripts/
            

Make the following replacements:

        * REGION: `kafka.sh` is stored in public regionally-tagged buckets in Cloud Storage. Specify a geographically close [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available), (example: `us-central1`).
        * BUCKET_NAME: The name of your Cloud Storage bucket.

**Note:** The `kafka.sh` script is available from the GitHub [`initialization-actions/kafka/`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/master/kafka/kafka.sh) repository. You can clone or download the script onto your local machine, then modify the source specified in the previous `gcloud storage cp` example to copy the local script to `gs://BUCKET_NAME/scripts/`.

### Create a Managed Service for Apache Spark Kafka cluster

  1. Open [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), then run the following [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to create a Managed Service for Apache Spark [HA cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability) cluster that installs the Kafka and ZooKeeper components:
         
         gcloud dataproc clusters create KAFKA_CLUSTER \
             --project=PROJECT_ID \
             --region=REGION \
             --image-version=2.1-debian11 \
             --num-masters=3 \
             --enable-component-gateway \
             --initialization-actions=gs://BUCKET_NAME/scripts/kafka.sh
         

Notes:

     * KAFKA_CLUSTER: The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused.
     * PROJECT_ID: The project to associate with this cluster.
     * REGION: The [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located, such as `us-central1`. 
       * You can add the optional `--zone=ZONE` flag to specify a zone within the specified region, such as `us-central1-a`. If you do not specify a zone, the Managed Service for Apache Spark [autozone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) feature selects a zone with the specified region.
     * `--image-version`: Managed Service for Apache Spark image version [`2.1-debian11`](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1) is recommended for this tutorial. Note: Each image version contains a set of pre-installed components, including the Hive component used in this tutorial (see [Supported Managed Service for Apache Spark image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions)).
     * `--num-master`: `3` master nodes create an [HA cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability). The Zookeeper component, which is required by Kafka, is pre-installed on an HA cluster. In future Kafka releases, [Zookeeper may be deprecated and removed](https://kafka.apache.org/documentation/#zk_depr).
     * `--enable-component-gateway`: Enables the [Managed Service for Apache Spark Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways).
     * BUCKET_NAME: The name of your Cloud Storage bucket that contains the `/scripts/kafka.sh` initialization script (see Copy the Kafka installation script to Cloud Storage).



### Create a Kafka `custdata` topic

To create a Kafka topic on the Managed Service for Apache Spark Kafka cluster:

  1. Use the [SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh#console) utility to open a terminal window on the cluster master VM.

  2. Create a Kafka `custdata` topic.
         
         /usr/lib/kafka/bin/kafka-topics.sh \
             --bootstrap-server KAFKA_CLUSTER-w-0:9092 \
             --create --topic custdata
         

Notes:

     * KAFKA_CLUSTER: Insert the name of your Kafka cluster. `-w-0:9092` signifies the Kafka broker running on port `9092` on the `worker-0` node.

     * You can run the following commands after creating the `custdata` topic:
           
           # List all topics.
           /usr/lib/kafka/bin/kafka-topics.sh \
               --bootstrap-server KAFKA_CLUSTER-w-0:9092 \
               --list
             
           
           # Consume then display topic data.
           /usr/lib/kafka/bin/kafka-console-consumer.sh \
               --bootstrap-server KAFKA_CLUSTER-w-0:9092 \
               --topic custdata
             
           
           # Count the number of messages in the topic.
           /usr/lib/kafka/bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
               --broker-list KAFKA_CLUSTER-w-0:9092 \
               --topic custdata
           
           # Delete topic.
           /usr/lib/kafka/bin/kafka-topics.sh \
               --bootstrap-server KAFKA_CLUSTER-w-0:9092 \
               --delete --topic custdata
           




### Publish content to the Kafka `custdata` topic

The following script uses the `kafka-console-producer.sh` Kafka tool to generate fictitious customer data in CSV format.

  1. Copy, then paste the script in the SSH terminal on the master node of your Kafka cluster. Press **< return>** to run the script.
         
         for i in {1..10000}; do \
         custname="cust name${i}"
         uuid=$(dbus-uuidgen)
         age=$((45 + $RANDOM % 45))
         amount=$(echo "$(( $RANDOM % 99999 )).$(( $RANDOM % 99 ))")
         message="${uuid}:${custname},${age},${amount}"
         echo ${message}
         done | /usr/lib/kafka/bin/kafka-console-producer.sh \
         --broker-list KAFKA_CLUSTER-w-0:9092 \
         --topic custdata \
         --property "parse.key=true" \
         --property "key.separator=:"
         

Notes:

     * KAFKA_CLUSTER: The name of your Kafka cluster.
You can publish data to a Kafka topic from many sources, such as web-sites, applications, and devices, in different formats, such as CSV, JSON, text, and Apache Avro serialization format (see [Kafka Use Cases](https://kafka.apache.org/uses)).
  2. Run the following Kafka command to confirm the `custdata` topic contains 10,000 messages.
         
         /usr/lib/kafka/bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
         --broker-list KAFKA_CLUSTER-w-0:9092 \
         --topic custdata
         

Notes:

     * KAFKA_CLUSTER: The name of your Kafka cluster.

Expected output: 
    
    custdata:0:10000
    




### Create Hive tables in Cloud Storage

Create Hive tables to receive streamed Kafka topic data. Perform the following steps to create `cust_parquet` (parquet) and a `cust_orc` (ORC) Hive tables in your Cloud Storage bucket.

  1. Insert your BUCKET_NAME in the following script, then copy and paste the script into the SSH terminal on your Kafka cluster master node, then press **< return>** to create a `~/hivetables.hql` (Hive Query Language) script.

You will run the `~/hivetables.hql` script in the next step to create parquet and ORC Hive tables in your Cloud Storage bucket.
         
         cat > ~/hivetables.hql <<EOF
         drop table if exists cust_parquet;
         create external table if not exists cust_parquet
         (uuid string, custname string, age string, amount string)
         row format delimited fields terminated by ','
         stored as parquet
         location "gs://BUCKET_NAME/tables/cust_parquet";
         
         
         
         drop table if exists cust_orc;
         create external table if not exists cust_orc
         (uuid string, custname string, age string, amount string)
         row format delimited fields terminated by ','
         stored as orc
         location "gs://BUCKET_NAME/tables/cust_orc";
         EOF
         

  2. In the SSH terminal on the master node of your Kafka cluster, submit the `~/hivetables.hql` Hive job to create `cust_parquet` (parquet) and a `cust_orc` (ORC) Hive tables in your Cloud Storage bucket.
         
         gcloud dataproc jobs submit hive \
             --cluster=KAFKA_CLUSTER \
             --region=REGION \
             -f ~/hivetables.hql
         

Notes:

     * The Hive component is pre-installed on the Managed Service for Apache Spark Kafka cluster. See [2.1.x release versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1) for a list of the Hive component versions included in recently released 2.1 images.
     * KAFKA_CLUSTER: The name of your Kafka cluster.
     * REGION: The region where your Kafka cluster is located.



### Stream Kafka `custdata` to Hive tables

  1. Run the following command in the in the SSH terminal on the master node of your Kafka cluster to install the `kafka-python` library. A Kafka client is needed to stream Kafka topic data to Cloud Storage. Typically, the Kafka client runs on a separate machine, but this tutorial uses one cluster for all processes for simplicity and to save costs.
         
         pip install kafka-python
         

  2. Insert your BUCKET_NAME, then copy then paste the following PySpark code into the SSH terminal on your Kafka cluster master node, and then press **< return>** to create a `streamdata.py` file.

The script subscribes to the Kafka `custdata` topic, then streams the data to your Hive tables in Cloud Storage. The output format, which can be parquet or ORC, is passed into the script as a parameter.

**Note:** The Kafka topic data streamed to Cloud Storage is in compressed binary format.
         
         cat > streamdata.py <<EOF
         #!/bin/python
         
         import sys
         from pyspark.sql.functions import *
         from pyspark.sql.types import *
         from pyspark.sql import SparkSession
         from kafka import KafkaConsumer
         
         def getNameFn (data): return data.split(",")[0]
         def getAgeFn  (data): return data.split(",")[1]
         def getAmtFn  (data): return data.split(",")[2]
         
         def main(cluster, outputfmt):
             spark = SparkSession.builder.appName("APP").getOrCreate()
             spark.sparkContext.setLogLevel("WARN")
             Logger = spark._jvm.org.apache.log4j.Logger
             logger = Logger.getLogger(__name__)
         
             rows = spark.readStream.format("kafka") \
             .option("kafka.bootstrap.servers", cluster+"-w-0:9092").option("subscribe", "custdata") \
             .option("startingOffsets", "earliest")\
             .load()
         
             getNameUDF = udf(getNameFn, StringType())
             getAgeUDF  = udf(getAgeFn,  StringType())
             getAmtUDF  = udf(getAmtFn,  StringType())
         
             logger.warn("Params passed in are cluster name: " + cluster + "  output format(sink): " + outputfmt)
         
             query = rows.select (col("key").cast("string").alias("uuid"),\
                 getNameUDF      (col("value").cast("string")).alias("custname"),\
                 getAgeUDF       (col("value").cast("string")).alias("age"),\
                 getAmtUDF       (col("value").cast("string")).alias("amount"))
         
             writer = query.writeStream.format(outputfmt)\
                     .option("path","gs://BUCKET_NAME/tables/cust_"+outputfmt)\
                     .option("checkpointLocation", "gs://BUCKET_NAME/chkpt/"+outputfmt+"wr") \
                 .outputMode("append")\
                 .start()
         
             writer.awaitTermination()
         
         if __name__=="__main__":
             if len(sys.argv) < 2:
                 print ("Invalid number of arguments passed ", len(sys.argv))
                 print ("Usage: ", sys.argv[0], " cluster  format")
                 print ("e.g.:  ", sys.argv[0], " <cluster_name>  orc")
                 print ("e.g.:  ", sys.argv[0], " <cluster_name>  parquet")
             main(sys.argv[1], sys.argv[2])
         
         EOF
         

  3. In the SSH terminal on the master node of your Kafka cluster, run `spark-submit` to stream data to your Hive tables in Cloud Storage.

     1. Insert the name of your KAFKA_CLUSTER and the output FORMAT, then copy and paste the following code into the SSH terminal on the master node of your Kafka cluster, and then press **< return>** to run the code and stream the Kafka `custdata` data in parquet format to your Hive tables in Cloud Storage. 
            
            spark-submit --packages \
            org.apache.spark:spark-streaming-kafka-0-10_2.12:3.1.3,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3 \
                --conf spark.history.fs.gs.outputstream.type=FLUSHABLE_COMPOSITE \
                --conf spark.driver.memory=4096m \
                --conf spark.executor.cores=2 \
                --conf spark.executor.instances=2 \
                --conf spark.executor.memory=6144m \
                streamdata.py KAFKA_CLUSTER FORMAT
                

Notes:

        * KAFKA_CLUSTER: Insert the name of your Kafka cluster.
        * FORMAT: Specify either `parquet` or `orc` as the output format. You can run the command successively to stream both formats to the Hive tables: for example, in the first invocation, specify `parquet` to stream the Kafka `custdata` topic to the Hive parquet table; then, in second invocation, specify `orc` format to stream `custdata` to the Hive ORC table.
  4. After standard output halts in the SSH terminal, which signifies that all of the `custdata` has been streamed, press **< control-c>** in the SSH terminal to stop the process.

  5. List the Hive tables in Cloud Storage.
         
         gcloud storage ls gs://BUCKET_NAME/tables/* --recursive
         

Notes:

     * BUCKET_NAME: Insert the name of the Cloud Storage bucket that contains your Hive tables (see Create Hive tables).



### Query streamed data

  1. In the SSH terminal on the master node of your Kafka cluster, run the following `hive` command to count the streamed Kafka `custdata` messages in the Hive tables in Cloud Storage.
         
         hive -e "select count(1) from TABLE_NAME"
         

Notes:

     * TABLE_NAME: Specify either `cust_parquet` or `cust_orc` as the Hive table name.

Expected output snippet:



    
    
    **...**
    Status: Running (Executing on YARN cluster with App id application_....)
    
    ----------------------------------------------------------------------------------------------
            VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
    ----------------------------------------------------------------------------------------------
    Map 1 .......... container     SUCCEEDED      1          1        0        0       0       0
    Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0
    ----------------------------------------------------------------------------------------------
    VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 9.89 s
    ----------------------------------------------------------------------------------------------
    OK
    **10000**
    Time taken: 21.394 seconds, Fetched: 1 row(s)
    

## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete resources

  * Delete the bucket: 
        
        gcloud storage buckets delete BUCKET_NAME

**Important:** Your bucket must be empty before you can delete it.
  * Delete your Kafka cluster: 
        
        gcloud dataproc clusters delete KAFKA_CLUSTER \
            --region=${REGION}
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
