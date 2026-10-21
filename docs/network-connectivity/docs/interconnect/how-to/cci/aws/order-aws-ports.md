---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-aws-ports/
title: Order AWS ports \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:06.460606+00:00
---

# Order AWS ports  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-aws-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order AWS ports Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [AWS documentation](https://docs.aws.amazon.com/) . 

After you've ordered your Cross-Cloud Interconnect connections, order your AWS ports.

## Order your ports

AWS offers two _Direct Connect_ ordering options: Link Aggregation Group (LAG)s and _connections_. (In the AWS interface, links are known as _connections_.) You must order LAGs, not _connections_. LAGs enable [Link Aggregation Control Protocol (LACP)](https://en.wikipedia.org/wiki/Link_aggregation), which permits multiple links per port. Cross-Cloud Interconnect for AWS requires LACP.

Order one LAG for each Cross-Cloud Interconnect connection.

**Caution:** For a redundant pair of Cross-Cloud Interconnect connections, perform the LAG ordering process below twice.

Do not enter `2` for the number of connections within a single LAG if you actually want a redundant pair of LAGs, each having one link.

Although LAGs enable bundling a group of connections together for higher bandwidth, you can create a LAG with just one connection.

If you accidentally ordered _connections_ instead of LAGs, you can create a LAG from the existing _connections_ by following the instructions on the [Create a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-lag.html) page in the AWS documentation, and then clicking the **Create a LAG with existing connections using the console** tab.

###  AWS console 

**Note:** For the most up-to-date information about how to order LAGs, see [Create a LAG](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-lag.html) in the AWS documentation.

  1. Go to the Direct Connect **LAGs** page.

  2. Click **Create LAG**.

  3. In the **LAG type** section of the page, select **Request new connections**.

  4. Fill out the **LAG settings** section of the page:

     * Enter a **LAG Name** for the resource.
     * In the **Location** field, enter the AWS location. If you need help with choosing a value for this field, see [Supported locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations#supported-locations). You can find the location name below each listed location description. You can also search for a location name by using the search field in the **LAG settings** section.
     * Select the appropriate **Port speed**.
     * Enter the **Number of new connections** that you want.
**Note:** Set this field to reflect the number of links in this LAG. _Setting the number of new connections to`2` does not set up redundancy._ To set up redundancy, order two LAGs by following the LAG ordering process _twice_.
     * Clear the field labeled **Connect through an AWS Direct Connect partner**.
  5. Click **Create LAG**.




###  AWS CLI 

To order your Direct Connect ports, use the [`create-lag` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-lag.html). For example:
    
    
    aws directconnect create-lag \
      --number-of-connections NUMBER_OF_CONNECTIONS \
      --connections-bandwidth CAPACITY \
      --location AWS_LOCATION \
      --lag-name NAME \
      --region REGION
    

Replace the following:

  * `NUMBER_OF_CONNECTIONS`: the number of links, or connections, that you want for each port
  * `CAPACITY`: the bandwidth of each connection in the LAG
  * `AWS_LOCATION`: the name of the AWS location—for example, `EqDC2`
  * `NAME`: the name of the new LAG
  * `REGION`: the region where you want to place your new connection and its links



## Generate an LOA

For Google to provision your connection, it must have a letter of authorization (LOA) for each connection that you created in each AWS LAG.

For example, suppose you ordered two LAGs and you created two connections in each LAG. In this case, you need four LOA documents.

Use the following instructions twice—once for each LAG.

###  AWS console 

To download the LOAs, complete the following steps:

  1. Go to the Direct Connect **LAGs** page.

  2. Click the name of the appropriate LAG.

  3. Go the **Connections** section of the page and do the following for each connection in the LAG:

     * Click the name of the connection to display the connection page.
     * Click **Download LOA**.
     * In the **Provider name - optional** field, enter **Google-Cloud**.
     * Click **Download**.
  4. Repeat step 3 for your redundant LAG.




###  AWS CLI 

To download the LOAs, complete the following steps:

  1. Use the [`aws directconnect describe-lags` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html) to retrieve identifiers for the LAGs that you created. For example:
         
         aws directconnect describe-lags \
          --region REGION |
         jq -r \ '.lags[].connections[].connectionId'
         

Replace `REGION` with the region where your connections are located.

In response, the system returns an identifier for each connection.

  2. For each connection in the LAG, download the LOA by using the [`aws directconnect describe-loa` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-loa.html). For example:
         
         aws directconnect describe-loa \
          --connection-id CONNECTION_ID \
          --provider-name "Google-Cloud" \
          --output text \
          --query loaContent \
          --region REGION |
         base64 --decode > FILE_NAME.pdf
         

Replace the following:

     * `CONNECTION_ID`: the identifier of the connection
     * `REGION`: the region where your connections are located
     * `FILE_NAME`: a name for the LOA document
  3. Repeat step 2 for your redundant LAG.




## Send the LOAs to Google

After you order your Cross-Cloud Interconnect connections, you should receive confirmation email messages from Google. Each of these messages includes instructions for sending your AWS LOAs to Google. Now that you have the LOAs, do the following:

  * Decide which AWS LAG you want to connect to each Cross-Cloud Interconnect port. Locate the LOA documents for that LAG.

  * Respond to each Google email. Each email represents a different Cross-Cloud Interconnect port. Attach the LOA documents for the AWS LAG that you want connected to that port.

**Caution:** Make sure to attach the correct LOA documents to the correct email. Errors in this step cause unintended port connections, which can result in configuration errors and connection delays.



Make a note of the instructions that you provide to Google regarding which Cross-Cloud Interconnect port connects to which AWS LAG. You need this information later in the process when you configure your AWS resources.

Still later, after Google has provisioned your Cross-Cloud Interconnect connections, you receive another set of emails stating that the connections are ready to use.

After you receive this confirmation, you can finish the required configuration.

[ Previous arrow_back  Order Cross-Cloud Interconnect connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-google-connections)

[ Next Configure Google Cloud resources  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
