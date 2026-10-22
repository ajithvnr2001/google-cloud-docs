---
url: https://docs.cloud.google.com/composer/docs/composer-2/use-kubernetes-pod-operator/
title: Use the KubernetesPodOperator \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:06.519522+00:00
---

# Use the KubernetesPodOperator  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/use-kubernetes-pod-operator/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Use the KubernetesPodOperator Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/use-kubernetes-pod-operator "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to use KubernetesPodOperator to deploy [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/) from Managed Service for Apache Airflow into the Google Kubernetes Engine cluster that is part of your Managed Service for Apache Airflow environment.

KubernetesPodOperator launches [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/) **in your environment's cluster**. In comparison, [Google Kubernetes Engine operators](https://docs.cloud.google.com/composer/docs/composer-2/use-gke-operator) run Kubernetes Pods in a specified cluster, which can be a separate cluster that is not related to your environment. You can also create and delete clusters using Google Kubernetes Engine operators.

KubernetesPodOperator is a good option if you require:

  * Custom Python dependencies that are not available through the public PyPI repository.
  * Binary dependencies that are not available in the stock Managed Airflow worker image.

**Note:** For additional information about installing packages hosted in a private package repository or additional options to manage dependencies, see [Installing Python dependencies](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies).

## Before you begin

  * If version 5.0.0 of CNCF Kubernetes Provider is used then follow instructions documented CNCF Kubernetes Provider section.

  * Pod affinity configuration is not available in Managed Airflow (Gen 2). If you want to use Pod affinity, use the GKE operators to launch Pods in a different cluster instead.




## About KubernetesPodOperator in Managed Airflow (Gen 2)

This section describes how KubernetesPodOperator works in Managed Airflow (Gen 2).

### Resource usage

In Managed Airflow (Gen 2), your environment's cluster [scales automatically](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments). Extra workloads that you run using KubernetesPodOperator scale independently from your environment.

Your environment is not affected by the increased resource demand, but your environment's cluster scales up and down depending on the resource demand.

The pricing for the extra workloads that you run in your environment's cluster follows the [Managed Airflow (Gen 2) pricing model](https://docs.cloud.google.com/composer/pricing) and uses **Managed Airflow Compute SKUs**.

Managed Airflow (Gen 2) uses Autopilot clusters which introduce the notion of [compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use):

  * Managed Airflow supports only the `general-purpose` compute class.

  * By default, if no class is selected then the `general-purpose` class is assumed when you create Pods using KubernetesPodOperator.

  * Each class is associated with specific properties and resource limits, You can read about them in [Autopilot documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-min-max). For example, Pods that run within the `general-purpose` class can use up to 110 GiB of memory.




### Access to project's resources

Managed Airflow (Gen 2) uses GKE clusters with Workload Identity Federation for GKE. Pods that run in the `composer-user-workloads` namespace can access Google Cloud resources in your project without additional configuration. [Your environment's service account](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account) is used to access these resources.

If you want to use a custom namespace, then Kubernetes service accounts associated with this namespace must be mapped to Google Cloud service accounts, to enable service identity authorization for requests to Google APIs and other services. If you run Pods in a custom namespace in your environment's cluster, then IAM bindings between Kubernetes and Google Cloud service accounts are not created, and these Pods cannot access resources of your Google Cloud project.

If you use a custom namespace and want your Pods to have access to Google Cloud resources, then [follow the guidance in Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and set up the bindings for a custom namespace:

  1. Create a separate namespace in your environment's cluster.
  2. Create a binding between the custom namespace Kubernetes Service Account and [your environment's service account](https://docs.cloud.google.com/composer/docs/composer-2/access-control#service-account).
  3. Add your environment's service account annotation to the Kubernetes service account.
  4. When you use KubernetesPodOperator, specify the namespace and the Kubernetes service account in the `namespace` and `service_account_name` parameters.

**Note:** The GKE metadata server takes a few seconds to start accepting requests on a newly created Pod. Therefore, attempts to authenticate using Workload Identity Federation for GKE within the first few seconds of a Pod's life might fail. Retrying the call will resolve the problem. For more information about this limitation, see [Restrictions of Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#restrictions).

## Minimal configuration

To create a KubernetesPodOperator, only Pod's `name`, `image` to use, and `task_id` parameters are required. The `/home/airflow/composer_kube_config` contains credentials to authenticate to GKE.
    
    
    kubernetes_min_pod = KubernetesPodOperator(
        # The ID specified for the task.
        task_id="pod-ex-minimum",
        # Name of task you want to run, used to generate Pod ID.
        name="pod-ex-minimum",
        # Entrypoint of the container, if not specified the Docker container's
        # entrypoint is used. The cmds parameter is templated.
        cmds=["echo"],
        # The namespace to run within Kubernetes. In Composer 2 environments
        # after December 2022, the default namespace is
        # `composer-user-workloads`. Always use the
        # `composer-user-workloads` namespace with Composer 3.
        namespace="composer-user-workloads",
        # Docker image specified. Defaults to hub.docker.com, but any fully
        # qualified URLs will point to a custom repository. Supports private
        # gcr.io images if the Composer Environment is under the same
        # project-id as the gcr.io images and the service account that Composer
        # uses has permission to access the Google Container Registry
        # (the default service account has permission)
        image="marketplace.gcr.io/google/ubuntu2204",
        # Specifies path to kubernetes config. The config_file is templated.
        config_file="/home/airflow/composer_kube_config",
        # Identifier of connection that should be used
        kubernetes_conn_id="kubernetes_default",
    )

## Additional configuration

This example shows additional parameters that you can configure in the KubernetesPodOperator.

See the following resources for more information:

  * For information about using Kubernetes Secrets and ConfigMaps, see Use Kubernetes Secrets and ConfigMaps.

  * For information about using Jinja templates with KubernetesPodOperator, see Use Jinja templates.

  * For information about KubernetesPodOperator parameters, see the [operator's reference](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html) in Airflow documentation.



    
    
    kubernetes_full_pod = KubernetesPodOperator(
        task_id="ex-all-configs",
        name="pi",
        namespace="composer-user-workloads",
        image="perl:5.34.0",
        # Entrypoint of the container, if not specified the Docker container's
        # entrypoint is used. The cmds parameter is templated.
        cmds=["perl"],
        # Arguments to the entrypoint. The Docker image's CMD is used if this
        # is not provided. The arguments parameter is templated.
        arguments=["-Mbignum=bpi", "-wle", "print bpi(2000)"],
        # The secrets to pass to Pod, the Pod will fail to create if the
        # secrets you specify in a Secret object do not exist in Kubernetes.
        secrets=[],
        # Labels to apply to the Pod.
        labels={"pod-label": "label-name"},
        # Timeout to start up the Pod, default is 600.
        startup_timeout_seconds=600,
        # The environment variables to be initialized in the container.
        # The env_vars parameter is templated.
        env_vars={"EXAMPLE_VAR": "/example/value"},
        # If true, logs stdout output of container. Defaults to True.
        get_logs=True,
        # Determines when to pull a fresh image, if 'IfNotPresent' will cause
        # the Kubelet to skip pulling an image if it already exists. If you
        # want to always pull a new image, set it to 'Always'.
        image_pull_policy="Always",
        # Annotations are non-identifying metadata you can attach to the Pod.
        # Can be a large range of data, and can include characters that are not
        # permitted by labels.
        annotations={"key1": "value1"},
        # Optional resource specifications for Pod, this will allow you to
        # set both cpu and memory limits and requirements.
        # Prior to Airflow 2.3 and the cncf providers package 5.0.0
        # resources were passed as a dictionary. This change was made in
        # https://github.com/apache/airflow/pull/27197
        # Additionally, "memory" and "cpu" were previously named
        # "limit_memory" and "limit_cpu"
        # resources={'limit_memory': "250M", 'limit_cpu': "100m"},
        container_resources=k8s_models.V1ResourceRequirements(
            requests={"cpu": "1000m", "memory": "10G", "ephemeral-storage": "10G"},
            limits={"cpu": "1000m", "memory": "10G", "ephemeral-storage": "10G"},
        ),
        # Specifies path to kubernetes config. The config_file is templated.
        config_file="/home/airflow/composer_kube_config",
        # If true, the content of /airflow/xcom/return.json from container will
        # also be pushed to an XCom when the container ends.
        do_xcom_push=False,
        # List of Volume objects to pass to the Pod.
        volumes=[],
        # List of VolumeMount objects to pass to the Pod.
        volume_mounts=[],
        # Identifier of connection that should be used
        kubernetes_conn_id="kubernetes_default",
        # Affinity determines which nodes the Pod can run on based on the
        # config. For more information see:
        # https://kubernetes.io/docs/concepts/configuration/assign-pod-node/
        # Pod affinity with the KubernetesPodOperator
        # is not supported with Composer 2
        # instead, create a cluster and use the GKEStartPodOperator
        # https://cloud.google.com/composer/docs/using-gke-operator
        affinity={},
    )

## Use Jinja templates

Airflow supports [Jinja templates](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#templating-with-jinja) in DAGs.

You must declare the required Airflow parameters (`task_id`, `name`, and `image`) with the operator. As shown in the following example, you can template all other parameters with Jinja, including `cmds`, `arguments`, `env_vars`, and `config_file`.

The `env_vars` parameter in the example is set from an [Airflow variable](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html) named `my_value`. The example DAG gets its value from the `vars` template variable in Airflow. Airflow has more variables that provide access to different types of information. For example, you can use the `conf` template variable to access values of [Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations). For more information and the list of variables available in Airflow, see [Templates reference](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) in the Airflow documentation.

Without changing the DAG or creating the `env_vars` variable, the `ex-kube-templates` task in the example fails because the variable does not exist. Create this variable in the Airflow UI or with Google Cloud CLI:

###  Airflow UI 

  1. Go to the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface).

  2. In the toolbar, select **Admin** > **Variables**.

  3. On the **List Variable** page, click **Add a new record**.

  4. On the **Add Variable** page, enter the following information:

     * Key:`my_value`
     * Val: `example_value`
  5. Click **Save**.




###  gcloud 

Enter the following command:
    
    
    gcloud composer environments run ENVIRONMENT \
        --location LOCATION \
        variables set -- \
        my_value example_value
    

Replace:

  * `ENVIRONMENT` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



The following example demonstrates how to use Jinja templates with KubernetesPodOperator:
    
    
    kubernetes_template_ex = KubernetesPodOperator(
        task_id="ex-kube-templates",
        name="ex-kube-templates",
        namespace="composer-user-workloads",
        image="bash",
        # All parameters below can be templated with Jinja. For more information
        # and the list of variables available in Airflow, see
        # the Airflow templates reference:
        # https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
        # Entrypoint of the container, if not specified the Docker container's
        # entrypoint is used. The cmds parameter is templated.
        cmds=["echo"],
        # DS in Jinja is the execution date as YYYY-MM-DD, this Docker image
        # will echo the execution date. Arguments to the entrypoint. The Docker
        # image's CMD is used if this is not provided. The arguments parameter
        # is templated.
        arguments=["{{ ds }}"],
        # The var template variable allows you to access variables defined in
        # Airflow UI. In this case we are getting the value of my_value and
        # setting the environment variable `MY_VALUE`. The pod will fail if
        # `my_value` is not set in the Airflow UI. The env_vars parameter
        # is templated.
        env_vars={"MY_VALUE": "{{ var.value.my_value }}"},
        # Specifies path to Kubernetes config. The config_file is templated.
        config_file="/home/airflow/composer_kube_config",
        # Identifier of connection that should be used
        kubernetes_conn_id="kubernetes_default",
    )

## Use Kubernetes Secrets and ConfigMaps

A Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) is an object that contains sensitive data. A Kubernetes [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) is an object that contains non-confidential data in key-value pairs.

In Managed Airflow (Gen 2), you can create Secrets and ConfigMaps using Google Cloud CLI, API, or Terraform, and then access them from KubernetesPodOperator.

### About YAML configuration files

When you create a Kubernetes Secret or a ConfigMap using Google Cloud CLI and API, you provide a file in the YAML format. This file must follow the same format as used by Kubernetes Secrets and ConfigMaps. Kubernetes documentation provides many code samples of ConfigMaps and Secrets. To get started, you can see the [Distribute Credentials Securely Using Secrets](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure) page and [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/).

[Same as in Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/), use the base64 representation when you define values in Secrets.

**Caution:** Values that are base64 encoded are not encrypted in any way, only obscured. It is possible to restore the original value from its base64 representation.

To encode a value, you can use the following command (this is one of many ways to get a base64-encoded value):
    
    
    echo "postgresql+psycopg2://root:example-password@127.0.0.1:3306/example-db" -n | base64
    

Output:
    
    
    cG9zdGdyZXNxbCtwc3ljb3BnMjovL3Jvb3Q6ZXhhbXBsZS1wYXNzd29yZEAxMjcuMC4wLjE6MzMwNi9leGFtcGxlLWRiIC1uCg==
    

The following two YAML file examples are used in samples later in this guide. Example YAML config file for a Kubernetes Secret:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: airflow-secrets
    data:
      sql_alchemy_conn: cG9zdGdyZXNxbCtwc3ljb3BnMjovL3Jvb3Q6ZXhhbXBsZS1wYXNzd29yZEAxMjcuMC4wLjE6MzMwNi9leGFtcGxlLWRiIC1uCg==
    

Another example that demonstrates how to include files. Same as in the previous example, first encode the contents of a file (`cat ./key.json | base64`), then provide this value in the YAML file:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: service-account
    data:
      service-account.json: |
        ewogICJ0eXBl...mdzZXJ2aWNlYWNjb3VudC5jb20iCn0K
    

An example YAML config file for a ConfigMap. You don't need to use the base64 representation in ConfigMaps:
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: example-configmap
    data:
      example_key: example_value
    

### Manage Kubernetes Secrets

In Managed Airflow (Gen 2), you create Secrets using Google Cloud CLI and `kubectl`:

  1. Get information about your environment's cluster:

     1. Run the following command:
            
            gcloud composer environments describe ENVIRONMENT \
                --location LOCATION \
                --format="value(config.gkeCluster)"
            

Replace:

        * `ENVIRONMENT` with the name of your environment.
        * `LOCATION` with the region where the Managed Airflow environment is located.

The output of this command uses the following format: `projects/<your-project-id>/locations/<location-of-composer-env>/clusters/<your-cluster-id>`. 

     2. To get the GKE cluster ID, copy the output after `/clusters/` (ends in `-gke`).

  2. Connect to your GKE cluster with the following command:
         
         gcloud container clusters get-credentials CLUSTER_ID \
           --project PROJECT \
           --region LOCATION
         

Replace the following:

     * `CLUSTER_ID`: the environment's cluster ID.
     * `PROJECT_ID`: the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * `LOCATION`: the region where the environment is located.

  3. Create Kubernetes Secrets:

**Note:** See [Managing Secrets using kubectl](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl) for commands that edit and delete Secrets.

The following commands demonstrate two different approaches to creating Kubernetes Secrets. The `--from-literal` approach uses key-value pairs. The `--from-file` approach uses file contents.

     * To create a Kubernetes Secret by providing key-value pairs run the following command. This example creates a Secret named `airflow-secrets` that has a `sql_alchemy_conn` field with the value of `test_value`.
           
           kubectl create secret generic airflow-secrets \
             --from-literal sql_alchemy_conn=test_value -n composer-user-workloads
           

     * To create a Kubernetes Secret by providing file contents, run the following command. This example creates a Secret named `service-account` that has the `service-account.json` field with the value taken from the contents of a local `./key.json` file.
           
           kubectl create secret generic service-account \
             --from-file service-account.json=./key.json -n composer-user-workloads
           




### Use Kubernetes Secrets in your DAGs

This example shows two ways of using Kubernetes Secrets: as an environment variable, and as a volume mounted by the Pod.

The first Secret, `airflow-secrets`, is set to a Kubernetes environment variable named `SQL_CONN` (as opposed to an Airflow or Managed Airflow environment variable).

The second Secret, `service-account`, mounts `service-account.json`, a file with a service account token, to `/var/secrets/google`.

Here's what the Secret objects look like:
    
    
    secret_env = Secret(
        # Expose the secret as environment variable.
        deploy_type="env",
        # The name of the environment variable, since deploy_type is `env` rather
        # than `volume`.
        deploy_target="SQL_CONN",
        # Name of the Kubernetes Secret
        secret="airflow-secrets",
        # Key of a secret stored in this Secret object
        key="sql_alchemy_conn",
    )
    secret_volume = Secret(
        deploy_type="volume",
        # Path where we mount the secret as volume
        deploy_target="/var/secrets/google",
        # Name of Kubernetes Secret
        secret="service-account",
        # Key in the form of service account file name
        key="service-account.json",
    )

The name of the first Kubernetes Secret is defined in the `secret_env` variable. This Secret is named `airflow-secrets`. The `deploy_type` parameter specifies that it must be exposed as an environment variable. The environment variable's name is `SQL_CONN`, as specified in the `deploy_target` parameter. Finally, the value of the `SQL_CONN` environment variable is set to the value of the `sql_alchemy_conn` key.

The name of the second Kubernetes Secret is defined in the `secret_volume` variable. This Secret is named `service-account`. It is exposed as an volume, as specified in the `deploy_type` parameter. The path of the file to mount, `deploy_target`, is `/var/secrets/google`. Finally, the `key` of the Secret that is stored in the `deploy_target` is `service-account.json`.

Here's what the operator configuration looks like:
    
    
    kubernetes_secret_vars_ex = KubernetesPodOperator(
        task_id="ex-kube-secrets",
        name="ex-kube-secrets",
        namespace="composer-user-workloads",
        image="marketplace.gcr.io/google/ubuntu2204",
        startup_timeout_seconds=300,
        # The secrets to pass to Pod, the Pod will fail to create if the
        # secrets you specify in a Secret object do not exist in Kubernetes.
        secrets=[secret_env, secret_volume],
        # Entrypoint of the container, if not specified the Docker container's
        # entrypoint is used. The cmds parameter is templated.
        cmds=["echo"],
        # env_vars allows you to specify environment variables for your
        # container to use. The env_vars parameter is templated.
        env_vars={
            "EXAMPLE_VAR": "/example/value",
            "GOOGLE_APPLICATION_CREDENTIALS": "/var/secrets/google/service-account.json",
        },
        # Specifies path to kubernetes config. The config_file is templated.
        config_file="/home/airflow/composer_kube_config",
        # Identifier of connection that should be used
        kubernetes_conn_id="kubernetes_default",
    )

## Information about CNCF Kubernetes Provider

KubernetesPodOperator is implemented in `apache-airflow-providers-cncf-kubernetes` provider.

For detailed release notes for CNCF Kubernetes provider refer to [CNCF Kubernetes Provider website](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/index.html).

### Version 6.0.0

In version 6.0.0 of the CNCF Kubernetes Provider package, the `kubernetes_default` connection is used by default in KubernetesPodOperator.

If you specified a custom connection in version 5.0.0, this custom connection is still used by the operator. To switch back to using the `kubernetes_default` connection, you might want to adjust your DAGs accordingly.

### Version 5.0.0

This version introduces a few backward incompatible changes compared to version 4.4.0. The most important ones are related to the `kubernetes_default` connection which is not used in version 5.0.0.

**Important:** Adjustments in DAGs using KubernetesPodOperator are required if you are upgrading from a Managed Airflow version that uses 4.4.0 or earlier version of the provider to a Managed Airflow version that uses version 5.0.0.

  * The `kubernetes_default` connection needs to be modified. Kubernetes config path must be set to `/home/airflow/composer_kube_config` (as shown in the following figure). As an alternative, `config_file` must be added to the KubernetesPodOperator configuration (as shown in the following code example).

[ ![Kube config path field in Airflow UI](https://docs.cloud.google.com/static/composer/docs/images/airflowui_connection.png)](https://docs.cloud.google.com/static/composer/docs/images/airflowui_connection.png) **Figure 1.** Airflow UI, modifying kubernetes_default connection (click to enlarge) 

  * Modify the code of a task using KubernetesPodOperator in the following way:


    
    
    KubernetesPodOperator(
      # config_file parameter - can be skipped if connection contains this setting
      config_file="/home/airflow/composer_kube_config",
      # definition of connection to be used by the operator
      kubernetes_conn_id='kubernetes_default',
      ...
    )
    

For more information about Version 5.0.0 refer to [CNCF Kubernetes Provider Release Notes](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/index.html#id1).

## Troubleshooting

This section provides advice for troubleshooting common KubernetesPodOperator issues:

### View logs

When troubleshooting issues, you can check logs in the following order:

  1. Airflow Task logs:

     1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. In the list of environments, click the name of your environment. The **Environment details** page opens.

     3. Go to the **DAGs** tab.

     4. Click the name of the DAG, then click the DAG run to view the details and logs.

  2. Airflow scheduler logs:

     1. Go to the **Environment details** page.

     2. Go to the **Logs** tab.

     3. Inspect Airflow scheduler logs.

  3. Pod logs in the Google Cloud console, under GKE workloads. These logs include the Pod definition YAML file, Pod events, and Pod details.




### Non-zero return codes

When using KubernetesPodOperator (and GKEStartPodOperator), the return code of the container's entry point determines whether the task is considered successful or not. Non-zero return codes indicate failure.

A common pattern is to execute a shell script as the container entry point to group together multiple operations within the container.

If you are writing such a script, we recommended that you include the `set -e` command at the top of the script so that failed commands in the script terminate the script and propagate the failure to the Airflow task instance.

### Pod timeouts

The default timeout for KubernetesPodOperator is 120 seconds, which can result in timeouts occurring before larger images download. You can increase the timeout by altering the `startup_timeout_seconds` parameter when you create the KubernetesPodOperator.

When a Pod times out, the task specific log is available in the Airflow UI. For example:
    
    
    Executing <Task(KubernetesPodOperator): ex-all-configs> on 2018-07-23 19:06:58.133811
    Running: ['bash', '-c', u'airflow run kubernetes-pod-example ex-all-configs 2018-07-23T19:06:58.133811 --job_id 726 --raw -sd DAGS_FOLDER/kubernetes_pod_operator_sample.py']
    Event: pod-name-9a8e9d06 had an event of type Pending
    ...
    ...
    Event: pod-name-9a8e9d06 had an event of type Pending
    Traceback (most recent call last):
      File "/usr/local/bin/airflow", line 27, in <module>
        args.func(args)
      File "/usr/local/lib/python2.7/site-packages/airflow/bin/cli.py", line 392, in run
        pool=args.pool,
      File "/usr/local/lib/python2.7/site-packages/airflow/utils/db.py", line 50, in wrapper
        result = func(*args, **kwargs)
      File "/usr/local/lib/python2.7/site-packages/airflow/models.py", line 1492, in _run_raw_task
        result = task_copy.execute(context=context)
      File "/usr/local/lib/python2.7/site-packages/airflow/contrib/operators/kubernetes_pod_operator.py", line 123, in execute
        raise AirflowException('Pod Launching failed: {error}'.format(error=ex))
    airflow.exceptions.AirflowException: Pod Launching failed: Pod took too long to start
    

Pod Timeouts can also occur when the [Managed Airflow Service Account](https://docs.cloud.google.com/composer/docs/composer-2/access-control#composer-sa) lacks the necessary IAM permissions to perform the task at hand. To verify this, look at Pod-level errors using the [GKE Dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards) to look at the logs for your particular Workload, or use Cloud Logging.

### Failed to establish a new connection

Auto-upgrade is enabled by default in GKE clusters. If a node pool is in a cluster that is upgrading, you might see the following error:
    
    
    <Task(KubernetesPodOperator): gke-upgrade> Failed to establish a new
    connection: [Errno 111] Connection refused
    

To check if your cluster is upgrading, in Google Cloud console, go to the **Kubernetes clusters** page and look for the loading icon next to your environment's cluster name.

## What's next

  * [Use the GKE operators](https://docs.cloud.google.com/composer/docs/composer-2/use-gke-operator)
  * [Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
