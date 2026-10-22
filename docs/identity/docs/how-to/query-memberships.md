---
url: https://docs.cloud.google.com/identity/docs/how-to/query-memberships/
title: Querying group memberships \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:22.189655+00:00
---

# Querying group memberships  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/query-memberships/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Querying group memberships

This guide demonstrates how to transitively query group memberships and retrieve the membership graph of a member.

**Important:** These features are only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education, and Cloud Identity Premium accounts.

In addition to listing the direct members of a group, you can transitively search for both direct and indirect memberships and view the membership graph of a specific member. These capabilities address the following use cases:

  * Resource owners can make more informed decisions about resource ACL changes by understanding which groups and members are affected by the changes.
  * Group owners can assess the impact of adding or removing a group from a group related to ACL control, and more easily resolve membership concerns.
  * Security auditors can more effectively audit access policy because the expanded membership structure of their entire organization is visible.
  * Security auditors can assess the security risk of a member by viewing all of their direct and indirect group memberships, or checking if a member belongs to a specific group.



A group membership can belong to an individual, a service account, or another group.

The user or service account that is making the query must have permission to view the memberships of all groups that are part of the query, otherwise the request will fail. If the query returns an "PERMISSION_DENIED" error, it's likely that you don't have the correct permissions for one of the nested groups, especially if one of them is a group owned by another organization.

**Note:** Many of the following examples require a group ID. To find the ID of a single group, use the [`groups.lookup`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) method. To see all group IDs under a customer or namespace, use the [`groups.list`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/list) command.

## Before you begin

Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

## Searching for all memberships in a group

This code returns all memberships of a group. The response includes the type of membership (direct, indirect, or both) for each membership.

### REST

To get a list of all of the memberships in a group, call [`groups.memberships.searchTransitiveMemberships()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships) with the ID of the parent group.

### Python

To authenticate to Cloud Identity, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import googleapiclient.discovery
    from urllib.parse import urlencode
    
    def search_transitive_memberships(service, parent, page_size):
      try:
        memberships = []
        next_page_token = ''
        while True:
          query_params = urlencode(
            {
              "page_size": page_size,
              "page_token": next_page_token
            }
          )
          request = service.groups().memberships().searchTransitiveMemberships(parent=parent)
          request.uri += "&" + query_params
          response = request.execute()
    
          if 'memberships' in response:
            memberships += response['memberships']
    
          if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
          else:
            next_page_token = ''
    
          if len(next_page_token) == 0:
            break;
    
        print(memberships)
      except Exception as e:
        print(e)
    
    def main():
    
      service = googleapiclient.discovery.build('cloudidentity', 'v1')
    
      # Return results with a page size of 50
      search_transitive_memberships(service, 'groups/GROUP_ID', 50)
    
    if __name__ == '__main__':
        main()
    

## Searching for all group memberships of a member

### REST

To find all of the groups that a member belongs to, call [`groups.memberships.searchTransitiveGroups()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups) with the member key (for example, the email address of the member).

### Python

To authenticate to Cloud Identity, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

This code returns all groups that a member belongs to (except identity-mapped groups), both directly and indirectly.
    
    
    import googleapiclient.discovery
    from urllib.parse import urlencode
    
    def search_transitive_groups(service, member, page_size):
      try:
        groups = []
        next_page_token = ''
        while True:
          query_params = urlencode(
            {
              "query": "member_key_id == '{}' && 'cloudidentity.googleapis.com/groups.discussion_forum' in labels".format(member),
              "page_size": page_size,
              "page_token": next_page_token
            }
          )
          request = service.groups().memberships().searchTransitiveGroups(parent='groups/-')
          request.uri += "&" + query_params
          response = request.execute()
    
          if 'memberships' in response:
            groups += response['memberships']
    
          if 'nextPageToken' in response:
            next_page_token = response['nextPageToken']
          else:
            next_page_token = ''
    
          if len(next_page_token) == 0:
            break;
    
        print(groups)
      except Exception as e:
        print(e)
    
    def main():
    
      service = googleapiclient.discovery.build('cloudidentity', 'v1')
    
      # Return results with a page size of 50
      search_transitive_groups(service, 'MEMBER_EMAIL_ADDRESS', 50)
    
    if __name__ == '__main__':
        main()
    

## Checking membership in a group

### REST

To check whether a member belongs to a specific group (either directly or indirectly), call [`checkTransitiveMembership()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/checkTransitiveMembership) with the ID of the parent group and the member key (for example, the email address of the member).

### Python

To authenticate to Cloud Identity, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

The following code determines whether the member belongs to a specific group:
    
    
    import googleapiclient.discovery
    from urllib.parse import urlencode
    
    def check_transitive_membership(service, parent, member):
      try:
        query_params = urlencode(
          {
            "query": "member_key_id == '{}'".format(member)
          }
        )
        request = service.groups().memberships().checkTransitiveMembership(parent=parent)
        request.uri += "&" + query_params
        response = request.execute()
        print(response['hasMembership'])
      except Exception as e:
        print(e)
    
    def main():
    
      service = googleapiclient.discovery.build('cloudidentity', 'v1')
    
      check_transitive_membership(service, 'groups/GROUP_ID', 'MEMBER_EMAIL_ADDRESS')
    
    if __name__ == '__main__':
        main()
    

## Retrieving the membership graph for a member

**Note:** Retrieving the graph is subject to the permissions of the requestor. If the requestor does not have **View Membership** permissions for all of the groups to which the member belongs, the API returns a `403` error.

### REST

To get the membership graph of a member (all the groups that a member belongs to, along with the path information), call [`groups.memberships.getMembershipGraph()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/getMembershipGraph) with the ID of the parent group and the member key (for example, the email address of the member). The graph is returned as an adjacency list.

### Python

To authenticate to Cloud Identity, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

The following code returns the membership graph of a specified member in a Google Group (this query is filtered by group type using the label):
    
    
    import googleapiclient.discovery
    from urllib.parse import urlencode
    
    def get_membership_graph(service, parent, member):
      try:
        query_params = urlencode(
          {
            "query": "member_key_id == '{}' && 'cloudidentity.googleapis.com/groups.discussion_forum' in labels".format(member)
          }
        )
        request = service.groups().memberships().getMembershipGraph(parent=parent)
        request.uri += "&" + query_params
        response = request.execute()
        print(response['response'])
      except Exception as e:
        print(e)
    
    def main()
    
      service = googleapiclient.discovery.build('cloudidentity', 'v1')
    
      # Specify parent group as 'groups/-' to get ALL the groups of a member
      # along with path information
      get_membership_graph(service, 'groups/GROUP_ID', 'MEMBER_KEY')
    
    if __name__ == '__main__':
        main()
    

### Creating a visual representation of the membership graph

The following is a sample response from the Python code above. In this example, groups 000, 111, and 222 are connected as follows (arrows are from parent to child): 000 -> 111 -> 222\. A call to the sample code to retrieve the complete graph for group 222:
    
    
    get_membership_graph(service, 'groups/-', 'group-2@example.com')
    

results in the following response:
    
    
    {
      "@type": "type.googleapis.com/google.apps.cloudidentity.groups.v1.GetMembershipGraphResponse",
      "adjacencyList": [
        {
          "edges": [
            {
              "name": "groups/000/memberships/111",
              "preferredMemberKey": {
                "id": "group-1@example.com"
              },
              "roles": [
                {
                  "name": "MEMBER"
                }
              ]
            }
          ],
          "group": "groups/000"
        },
        {
          "edges": [
            {
              "name": "groups/111/memberships/222",
              "preferredMemberKey": {
                "id": "group-2@example.com"
              },
              "roles": [
                {
                  "name": "MEMBER"
                }
              ]
            }
          ],
          "group": "groups/111"
        }
      ],
      "groups": [
        {
          "name": "groups/000",
          "groupKey": {
            "id": "group-0@example.com"
          },
          "displayName": "Group - 0",
          "description": "Group - 0",
          "labels": {
            "cloudidentity.googleapis.com/groups.discussion_forum": ""
          }
        },
        {
          "name": "groups/111",
          "groupKey": {
            "id": "group-1@example.com"
          },
          "displayName": "Group - 1",
          "description": "Group - 1",
          "labels": {
            "cloudidentity.googleapis.com/groups.discussion_forum": ""
          }
        },
        {
          "name": "groups/222",
          "groupKey": {
            "id": "group-2@example.com"
          },
          "displayName": "Group - 2",
          "description": "Group - 2",
          "labels": {
            "cloudidentity.googleapis.com/groups.discussion_forum": ""
          }
        }
      ]
    }
    

Each item in the adjacency list represents a group and its direct members (edges) and the response also includes details of all groups in the membership graph. It can be parsed to generate alternative representations (for example, a DOT graph) which can be used to visualize the membership graph.

This sample script can be used convert the response to a DOT graph:
    
    
    #
    # Generates output in a dot format. Invoke this method using
    # response['response'] from get_membership_graph()
    #
    # Save the output to a .dot file (say graph.dot)
    # Use the dot tool to generate a visualization of the graph
    # Example:
    # dot -Tpng -o graph.png graph.dot
    #
    # Generates output like below:
    #
    # digraph {
    #   'group0' [label='groups/000 (GROUP 0)'];
    #   'group1' [label='groups/111 (GROUP 1)'];
    #   'group2' [label='groups/222 (GROUP 2)'];
    #   'group3' [label='groups/333 (GROUP 3)'];
    #   'group4' [label='groups/444 (GROUP 4)'];
    #
    #   'group0' -> 'group1' [label='group-1@example.com (MEMBER)'];
    #   'group0' -> 'group2' [label='group-2@example.com (MEMBER)'];
    #   'group1' -> 'group3' [label='group-3@example.com (MEMBER)'];
    #   'group3' -> 'group4' [label='group-4@example.com (MEMBER)'];
    #   'group2' -> 'group3' [label='group-3@example.com (MEMBER)'];
    # }
    #
    def convert_to_dot_format(graph):
      output = "digraph {\n"
      try:
        # Generate labels for the group nodes
        for group in graph['groups']:
          if 'displayName' in group:
            label = '{} ({})'.format(group['name'], group['displayName'])
          else:
            label = group['name']
          output += '  "{}" [label="{}"];\n'.format(group['name'].split('/')[1], label)
    
        output += '\n'
    
        # Generate edges
        for item in graph['adjacencyList']:
          group_id = item['group'].split('/')[1]
          for edge in item['edges']:
            edge_to = edge['name'].split('/')[3]
            edge_key = edge['preferredMemberKey']['id']
            # Collect the roles
            roles = []
            for role in edge['roles']:
              roles.append(role['name'])
            output += '  "{}" -> "{}" [label="{} ({})"];\n'.format(group_id,
                                                                   edge_to,
                                                                   edge_key,
                                                                   ','.join(roles))
    
        output += "}\n"
        print(output)
      except Exception as e:
        print(e)
    

The following is the resulting visual hierarchy for the sample response:

![Sample membership graph from DOT conversion](https://docs.cloud.google.com/static/identity/docs/images/membership-graph.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
