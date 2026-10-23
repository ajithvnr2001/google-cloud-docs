---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-enable-policies/
title: Bulk enable policies that match a filter \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:36.121861+00:00
---

# Bulk enable policies that match a filter  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-alert-enable-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Bulk enable policies that match a filter Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to bulk enable the alerting policies that match a filter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static object EnablePolicies(string projectId, string filter, bool enable)
    {
        var client = AlertPolicyServiceClient.Create();
        var request = new ListAlertPoliciesRequest()
        {
            ProjectName = new ProjectName(projectId),
            Filter = filter
        };
        var response = client.ListAlertPolicies(request);
        int result = 0;
        foreach (AlertPolicy policy in response)
        {
            try
            {
                if (policy.Enabled == enable)
                {
                    Console.WriteLine("Policy {0} is already {1}.",
                        policy.Name, enable ? "enabled" : "disabled");
                    continue;
                }
                policy.Enabled = enable;
                var fieldMask = new FieldMask { Paths = { "enabled" } };
                client.UpdateAlertPolicy(fieldMask, policy);
                Console.WriteLine("{0} {1}.", enable ? "Enabled" : "Disabled",
                    policy.Name);
            }
            catch (Grpc.Core.RpcException e)
            when (e.Status.StatusCode == StatusCode.InvalidArgument)
            {
                Console.WriteLine(e.Message);
                result -= 1;
            }
        }
        // Return a negative count of how many enable operations failed.
        return result;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // enablePolicies enables or disables all alert policies in the project.
    func enablePolicies(w io.Writer, projectID string, enable bool) error {
    	ctx := context.Background()
    
    	client, err := monitoring.NewAlertPolicyClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &monitoringpb.ListAlertPoliciesRequest{
    		Name: "projects/" + projectID,
    		// Filter:  "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    		// OrderBy: "", // See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering.
    	}
    	it := client.ListAlertPolicies(ctx, req)
    	for {
    		a, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		if a.GetEnabled().GetValue() == enable {
    			fmt.Fprintf(w, "Policy %q already has enabled=%v", a.GetDisplayName(), enable)
    			continue
    		}
    		a.Enabled = &wrappers.BoolValue{Value: enable}
    		req := &monitoringpb.UpdateAlertPolicyRequest{
    			AlertPolicy: a,
    			UpdateMask: &fieldmask.FieldMask{
    				Paths: []string{"enabled"},
    			},
    		}
    		if _, err := client.UpdateAlertPolicy(ctx, req); err != nil {
    			return err
    		}
    	}
    	fmt.Fprintln(w, "Successfully updated alerts.")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void enablePolicies(String projectId, String filter, boolean enable)
        throws IOException {
      try (AlertPolicyServiceClient client = AlertPolicyServiceClient.create()) {
        ListAlertPoliciesPagedResponse response =
            client.listAlertPolicies(
                ListAlertPoliciesRequest.newBuilder()
                    .setName(ProjectName.of(projectId).toString())
                    .setFilter(filter)
                    .build());
    
        for (AlertPolicy policy : response.iterateAll()) {
          if (policy.getEnabled().getValue() == enable) {
            System.out.println(
                String.format(
                    "Policy %s is already %b.", policy.getName(), enable ? "enabled" : "disabled"));
            continue;
          }
          AlertPolicy updatedPolicy =
              AlertPolicy.newBuilder()
                  .setName(policy.getName())
                  .setEnabled(BoolValue.newBuilder().setValue(enable))
                  .build();
          AlertPolicy result =
              client.updateAlertPolicy(
                  FieldMask.newBuilder().addPaths("enabled").build(), updatedPolicy);
          System.out.println(
              String.format(
                  "%s %s",
                  result.getDisplayName(), result.getEnabled().getValue() ? "enabled" : "disabled"));
        }
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[AlertPolicyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function enablePolicies() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const enabled = true;
      // const filter = 'A filter for selecting policies, e.g. description:"cloud"';
    
      const listAlertPoliciesRequest = {
        name: client.projectPath(projectId),
        // See https://cloud.google.com/monitoring/alerting/docs/sorting-and-filtering
        filter: filter,
      };
    
      const [policies] = await client.listAlertPolicies(listAlertPoliciesRequest);
      const responses = [];
      for (const policy of policies) {
        responses.push(
          await client.updateAlertPolicy({
            updateMask: {
              paths: ['enabled'],
            },
            alertPolicy: {
              name: policy.name,
              enabled: {
                value: enabled,
              },
            },
          })
        );
      }
      responses.forEach(response => {
        const alertPolicy = response[0];
        console.log(`${enabled ? 'Enabled' : 'Disabled'} ${alertPolicy.name}.`);
      });
    }
    enablePolicies();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\AlertPolicyServiceClient;
    use Google\Cloud\Monitoring\V3\ListAlertPoliciesRequest;
    use Google\Cloud\Monitoring\V3\UpdateAlertPolicyRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Enable or disable alert policies in a project.
     *
     * @param string $projectId Your project ID
     * @param bool $enable Enable or disable the policies.
     * @param string $filter Only enable/disable alert policies that match a filter.
     *        See https://cloud.google.com/monitoring/api/v3/sorting-and-filtering
     */
    function alert_enable_policies($projectId, $enable = true, $filter = null)
    {
        $alertClient = new AlertPolicyServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
        $listAlertPoliciesRequest = (new ListAlertPoliciesRequest())
            ->setName($projectName)
            ->setFilter($filter);
    
        $policies = $alertClient->listAlertPolicies($listAlertPoliciesRequest);
        foreach ($policies->iterateAllElements() as $policy) {
            $isEnabled = $policy->getEnabled()->getValue();
            if ($enable == $isEnabled) {
                printf('Policy %s is already %s' . PHP_EOL,
                    $policy->getName(),
                    $isEnabled ? 'enabled' : 'disabled'
                );
            } else {
                $policy->getEnabled()->setValue((bool) $enable);
                $mask = new FieldMask();
                $mask->setPaths(['enabled']);
                $updateAlertPolicyRequest = (new UpdateAlertPolicyRequest())
                    ->setAlertPolicy($policy)
                    ->setUpdateMask($mask);
                $alertClient->updateAlertPolicy($updateAlertPolicyRequest);
                printf('%s %s' . PHP_EOL,
                    $enable ? 'Enabled' : 'Disabled',
                    $policy->getName()
                );
            }
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def enable_alert_policies(project_name, enable, filter_=None):
        """Enable or disable alert policies in a project.
    
        Arguments:
            project_name (str): The Google Cloud Project to use. The project name
                must be in the format - 'projects/<PROJECT_NAME>'.
            enable (bool): Enable or disable the policies.
            filter_ (str, optional): Only enable/disable alert policies that match
                this filter_.  See
                https://cloud.google.com/monitoring/api/v3/sorting-and-filtering
        """
    
        client = monitoring_v3.AlertPolicyServiceClient()
        policies = client.list_alert_policies(
            request={"name": project_name, "filter": filter_}
        )
    
        for policy in policies:
            if bool(enable) == policy.enabled:
                print(
                    "Policy",
                    policy.name,
                    "is already",
                    "enabled" if policy.enabled else "disabled",
                )
            else:
                policy.enabled = bool(enable)
                mask = field_mask.FieldMask()
                mask.paths.append("enabled")
                client.update_alert_policy(alert_policy=policy, update_mask=mask)
                print("Enabled" if enable else "Disabled", policy.name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
