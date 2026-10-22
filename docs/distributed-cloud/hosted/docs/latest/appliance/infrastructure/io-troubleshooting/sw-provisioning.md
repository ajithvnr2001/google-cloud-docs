---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/sw-provisioning/
title: Software provisioning troubleshooting \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:47.575574+00:00
---

# Software provisioning troubleshooting  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/sw-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Software provisioning troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to troubleshoot common software provisioning issues you might face.

## Troubleshoot control plane bootstrapping

To troubleshoot the bootstrap control plane process, check the following resources within the KIND cluster:

  1. Examine the `anthos-cluster-operator` Pod:
         
         kubectl logs deployment/anthos-cluster-operator -c operator -n kube-system
         

  2. Inspect the `AddOn` resources:
         
         kubectl get AddOn -A
         

You can also view the resources with the `gpc-addons` command for more information.

  3. Check the `AddOnSet` resources:
         
         kubectl get AddOnSet -A
         

If the control plane bootstrap does not finish processing after the creation of the org infrastructure cluster, such as during a resource pivot, export the `kubeconfig` file manually:
         
         kubectl get secret root-admin-kubeconfig -n root -o jsonpath="{.data.value}" | base64 -d > /root/path/to/root-admin-kubeconfig.yaml
         




## Troubleshoot cluster creation

To troubleshoot the cluster creation process, follow these steps:

  1. Examine the current stage of the cluster and check whether the object `Harbor-operator` or Harbor exists and check its status from the KIND cluster in the `AddOnSet` resource by running the following command:
         
         kubectl get addonset -n fleet-root root-admin -o yaml
         

After running this command, find the current stage in `status.currentStage`.

  2. From the org infrastructure cluster, check the resources in the `harbor-system` namespace. If you deployed the `HarborCluster` object through the `kubectl get harborcluster harbor -n harbor-system` command, that indicates the installation has moved to the second stage, the Harbor stage.

  3. Inspect the `status` field in the `HarborCluster` object:
         
         kubectl -n harbor-system get harborcluster harbor
         

If the status indicates `healthy`, verify its functionality through the web portal by using the `docker push` command.

  4. Access the web portal at the reported URL. For example: `https://10.200.0.36:10443`.

  5. In the bootstrapper, run the command `docker push`.

If the status is `unhealthy`, review the details from the status conditions by executing the following entry:
         
         kubectl -n harbor-system get harborcluster harbor -o yaml
         

If the status shows `healthy`, navigate to the Check the istio status section. If the status does not show `healthy`, continue to the next section, Evaluate Harbor namespace resources.




### Evaluate Harbor namespace resources

These steps only need to be performed if the `harbor-system` resources do not have a status of `healthy`. To check the status of your `harbor-system` resources, see Troubleshoot cluster creation.

  1. Evaluate the `harbor-system` namespace resources:
         
         kubectl get all -n harbor-system
         

  2. Check the status for resources related to the Harbor operator, including the PostgreSQL and Redis operators that are built as sub-charts during the second stage of the org infrastructure cluster creation process. Validate the following operators are in the `Running` state:
         
         deployment/harbor-operator-harbor-operator
         deployment/harbor-operator-postgres-operator
         deployment/harbor-operator-redisoperator
         

  3. Verify the resources for PostgreSQL, Redis, and Harbor components all have a state of `healthy`. If some Pods are not in a `healthy` state, review the details from the failing Pod using these commands:
         
         kubectl get pod -o wide
         kubectl describe pod
         

You can also view the logs from the managing operator using this command:
         
         kubectl logs -f deploy/harbor-operator-postgres-operator
         

  4. To check the PostgreSQL resource, view `statefulset/postgresql-harbor-system-harbor`.

  5. To check the Redis resource, view the:

     1. Redis instance:`statefulset/rfr-harbor-redis`
     2. Redis sentinel:`deployment/rfs-harbor-redis`

The Harbor core components only deploy when the two components are ready.

If some Harbor core component Pods fail, review the logs from the failing Pod. In some cases, there is a communication issue with PostgreSQL or Redis instances.

For example, if the Harbor core component cannot connect to PostgreSQL or Redis with the provided credentials, there is a potential issue with the Harbor Operator, which is responsible for setting up the credentials before deploying Harbor core components.




### Check the istio status

To verify the Pod status is `istio`, such as `istio-system` and `service/istio-ingressgateway`, check whether port 10443 is exposed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
