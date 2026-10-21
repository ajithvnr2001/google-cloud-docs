---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/exec-probe-timeouts/
title: Configure exec probe timeouts before upgrading to GKE version 1.35 \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:40:11.980924+00:00
---

# Configure exec probe timeouts before upgrading to GKE version 1.35  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/exec-probe-timeouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure exec probe timeouts before upgrading to GKE version 1.35 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to prepare your [liveness, readiness, and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/) before you upgrade your Google Kubernetes Engine (GKE) clusters to version 1.35 and later by setting timeouts for commands in these probes.

**Key Term:** This page uses the term _exec probe_ to refer to liveness, readiness, or startup probes that execute commands by using the `exec.command` field in the probe specification.

## About timeouts for exec probes

Starting in GKE version 1.35, Kubernetes enforces timeouts for commands in the `exec` field of liveness, readiness, and startup probes. The `timeoutSeconds` field in the specification of a probe defines how long Kubernetes waits for a probe to complete any actions. If you omit this field, the default value is `1`, which means that any actions have one second to complete.

In GKE versions earlier than 1.35, Kubernetes ignores the value in the `timeoutSeconds` field for exec probe commands. For example, consider a liveness probe that has the following properties:

  * A value of `5` in the `timeoutSeconds` field.
  * A command in the `exec.command` field that takes 10 seconds to complete.



In versions earlier than 1.35, Kubernetes ignores this five second timeout and incorrectly reports the probe as successful. In version 1.35 and later, Kubernetes correctly fails the probe after five seconds.

This behavior in which Kubernetes ignores exec probe timeouts can result in probes that run indefinitely, which might hide issues with your applications or might cause unpredictable behavior. In GKE version 1.35 and later, Kubernetes correctly enforces command timeouts, which results in consistent, predictable probe behavior that aligns with open source Kubernetes.

## Impact of enforcing timeouts for exec probes

This is a breaking change in GKE version 1.35 and later that's necessary for the stability and reliability of workloads that run on GKE. When you upgrade your clusters to 1.35 and later, you might notice unexpected workload behavior if the workloads have exec probes with one of the following properties:

  * **Omit the`timeoutSeconds` field**: in version 1.35 and later, these probes have one second to successfully complete commands. If the command doesn't successfully complete in one second, the probes will correctly report failures.
  * **Specify short timeout periods** : in version 1.35 and later, probes with a shorter timeout period than the command completion time will correctly report failures.



In GKE version 1.34 and earlier, Kubernetes reports an error in exec probes that meet either of these conditions. However, the commands in these exec probes can still run to completion, because the probe error isn't a probe _failure_.

If you don't specify a more accurate timeout duration and the commands take longer than the existing timeout period to complete, your probes will report failures in version 1.35 and later. Depending on the type of probe, the following behavior applies when a probe fails:

  * **Liveness probes** : if a liveness probe fails because a command timed out, Kubernetes assumes that the application failed and restarts the container. In versions earlier than 1.35, a timeout might only generate a warning event without forcing a container restart. If the probe repeatedly fails, your Pods might get stuck in a crash loop with a `CrashLoopBackOff` Pod status.
  * **Readiness probes** : if a readiness probe fails because a command timed out, Kubernetes updates the `Ready` Pod condition with a `False` status. This means Kubernetes doesn't send any traffic to the Pod until the probe succeeds. In GKE version 1.35 and later, the Pod is removed from the Service endpoints. In versions earlier than 1.35, a timeout might only generate a warning event without removing the Pod from service. If all of the Pods that back a Service have a `False` status for the `Ready` condition, you might notice disruptions to the Service.
  * **Startup probes** : if a startup probe fails, Kubernetes assumes that the application failed to start and restarts the container. If the probe repeatedly fails, your Pods might get stuck in a crash loop with a `CrashLoopBackOff` Pod status.



### Paused automatic upgrades

GKE [pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) to version 1.35 when it detects that the workloads in a cluster might be affected by this change. GKE resumes automatic upgrades if version 1.35 is an automatic upgrade target for your control plane and nodes, _and_ if one of the following conditions is met:

  * You updated your workload probes with timeout values and GKE hasn't detected potential issues for seven days.
  * Version 1.34 reaches the [end of support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels) in your release channel.

**Warning:** When you upgrade a cluster to version 1.35 or later, GKE correctly enforces timeouts for exec probes. If you upgrade your cluster without updating the values in the `timeoutSeconds` field for exec probes, workload disruptions might occur.

## Identify affected clusters or workloads

The following sections show you how to identify clusters or workloads that might be affected by this change.

### Use GKE recommendations and insights

GKE monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to identify clusters that are affected by the enforcement of exec probe timeouts. If GKE detects that a cluster has workloads with exec probes that might time out, a recommendation titled **Configure your workload exec probe timeouts** is surfaced in the Google Cloud console.

#### Get insights and recommendations

Follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#view-insights-recs). You can get insights using the Google Cloud console. You can also use the Google Cloud CLI or the Recommender API, by filtering with the following subtype:

  * `EXEC_PROBE_TIMEOUT`: Exec probe timeouts



For clusters that have active recommendations, GKE [pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) to version 1.35 until the exec probe timeout configurations are updated to allow for non-disruptive operations.

### Check Kubernetes events by using the command line

In GKE version 1.34 and earlier, you can manually inspect the Kubernetes events in your clusters to find exec probes that take longer to complete than the existing timeout period. Kubernetes adds an event with a `command timed out` message for these probes. This method is useful for identifying workloads that are already experiencing issues due to short timeout values.

**Note:** Kubernetes events are retained for only one hour. To identify workloads with events that occurred more than one hour ago, use Cloud Logging.

To find affected workloads, do one of the following:

  * Find workloads in multiple clusters by using a script
  * Find workloads in specific clusters by using the command line



#### Find workloads in multiple clusters by using a script

The following bash script iterates over all of the clusters that are in your [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) to find affected workloads. This script checks for exec probe timeout errors in all existing and reachable Kubernetes contexts, and writes the findings to a text file named `affected_workloads_report.txt`. To run this script, follow these steps:

  1. Save the following script as `execprobe-timeouts.sh`:
         
         #!/bin/bash
         
         # This script checks for exec probe timeouts across all existing and reachable
         # Kubernetes contexts and writes the findings to a text file, with one
         # row for each affected workload, including its cluster name.
         
         # --- Configuration ---
         OUTPUT_FILE="affected_workloads_report.txt"
         # -------------------
         
         # Check if kubectl and jq are installed
         if ! command -v kubectl &> /dev/null || ! command -v jq &> /dev/null; then
             echo "Error: kubectl and jq are required to run this script." >&2
             exit 1
         fi
         
         echo "Fetching all contexts from your kubeconfig..."
         
         # Initialize the report file with a formatted header
         printf "%-40s | %s\n" "Cluster Context" "Impacted Workload" > "$OUTPUT_FILE"
         
         # Get all context names from the kubeconfig file
         CONTEXTS=$(kubectl config get-contexts -o name)
         
         if [[ -z "$CONTEXTS" ]]; then
           echo "No Kubernetes contexts found in your kubeconfig file."
           exit 0
         fi
         
         echo "Verifying each context and checking for probe timeouts..."
         echo "=================================================="
         
         # Loop through each context
         for CONTEXT in $CONTEXTS; do
           echo "--- Checking context: $CONTEXT ---"
         
           # Check if the cluster is reachable by running a lightweight command
           if kubectl --context="$CONTEXT" get ns --request-timeout=1s > /dev/null 2>&1; then
             echo "Context '$CONTEXT' is reachable. Checking for timeouts..."
         
             # Find timeout events based on the logic from the documentation
             AFFECTED_WORKLOADS_LIST=$(kubectl --context="$CONTEXT" get events --all-namespaces -o json | jq -r '.items[] | select((.involvedObject.namespace | type == "string") and (.involvedObject.namespace | endswith("-system") | not) and (.message | test("^(Liveness|Readiness|Startup) probe errored(.*): command timed out(.*)|^ * probe errored and resulted in .* state: command timed out.*"))) | .involvedObject.kind + "/" + .involvedObject.name' | uniq)
         
             if [[ -n "$AFFECTED_WORKLOADS_LIST" ]]; then
               echo "Found potentially affected workloads in context '$CONTEXT'."
         
               # Loop through each affected workload and write a new row to the report
               # pairing the context with the workload.
               while IFS= read -r WORKLOAD; do
                 printf "%-40s | %s\n" "$CONTEXT" "$WORKLOAD" >> "$OUTPUT_FILE"
               done <<< "$AFFECTED_WORKLOADS_LIST"
             else
               echo "No workloads with exec probe timeouts found in context '$CONTEXT'."
             fi
           else
             echo "Context '$CONTEXT' is not reachable or the cluster does not exist. Skipping."
           fi
           echo "--------------------------------------------------"
         done
         
         echo "=================================================="
         echo "Script finished."
         echo "A detailed report of affected workloads has been saved to: $OUTPUT_FILE"
         

  2. Run the script:
         
         bash execprobe-timeouts.sh
         

  3. Read the contents of the `affected_workloads_report.txt` file:
         
         cat affected_workloads_report.txt
         

The output is similar to the following:
         
         Cluster Context                   | Impacted Workload
         -----------------------------------------|----------------------------
         gke_my-project_us-central1-c_cluster-1   | Pod/liveness1-exec
         gke_my-project_us-central1-c_cluster-1   | Deployment/another-buggy-app
         gke_my-project_us-east1-b_cluster-2      | Pod/startup-probe-test
         




#### Find workloads in specific clusters by using the command line

To identify affected workloads in specific clusters, you can use the `kubectl` tool to check for exec probe timeout errors. Follow these steps for every GKE cluster that runs version 1.34 or earlier:

  1. Connect to the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the location of the cluster control plane, such as `us-central1`.
  2. Check for events that indicate that an exec probe has a timeout error:
         
         kubectl get events --all-namespaces -o json |
             jq -r '.items[] | select((.involvedObject.namespace | type == "string") and (.involvedObject.namespace | endswith("-system") | not) and (.message | test("^(Liveness|Readiness|Startup) probe errored(.*): command timed out(.*)|^ * probe errored and resulted in .* state: command timed out.*"))) | "\(.involvedObject.kind)/\(.involvedObject.name)        Namespace: \(.involvedObject.namespace)"'
         

This command ignores workloads in many system namespaces. If affected workloads exist, the output is similar to the following:
         
         Pod/liveness1-exec      Namespace: default
         

  3. Repeat the preceding steps for every cluster that runs GKE versions earlier than 1.35.




### Find affected clusters and workloads in Cloud Logging

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. To open the query editor, click the **Show query** toggle.

  3. Run the following query:
         
         jsonPayload.message=~" probe errored and resulted in .* state: command timed out" OR jsonPayload.message=~" probe errored: command timed out"
         

The output is a list of probe errors that were caused by commands that took longer to complete than the configured timeout period.




## Update affected workloads before upgrading to 1.35

**Best practice** : 

Before you make any changes to your production environment, test your changes to probes and the impact of upgrading to version 1.35 in a development environment.

After you identify the affected workloads, you must update the affected probes.

  1. Review the liveness, readiness, and startup probes for each affected Pod and determine an appropriate `timeoutSeconds` value. This value should be long enough for the command to execute successfully under normal conditions. For more information, see [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).
  2. Open the manifest file for the affected workload and add or modify the `timeoutSeconds` field for liveness, readiness, or startup probes. For example, the following liveness probe has a value of `10` in the `timeoutSeconds` field:
         
         spec:
           containers:
           - name: my-container
             image: my-image
             livenessProbe:
               exec:
                 command:
                 - cat
                 - /tmp/healthy
               initialDelaySeconds: 5
               periodSeconds: 5
               **timeoutSeconds : 10**
         

  3. Apply the updated manifest to your cluster.

  4. Check for errors in the updated probes by following the steps in Check Kubernetes events by using the command-line.




After you have updated and tested all affected workloads, you can upgrade your cluster to GKE version 1.35.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
