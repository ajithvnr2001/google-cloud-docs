---
url: https://docs.cloud.google.com/load-balancing/docs/sku-announce/
title: Announcement of upcoming SKU changes for Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:02:27.326044+00:00
---

# Announcement of upcoming SKU changes for Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/sku-announce/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)



Send feedback 

#  Announcement of upcoming SKU changes for Cloud Load Balancing Stay organized with collections  Save and categorize content based on your preferences. 

This page covers Cloud Load Balancing SKU changes that become effective on August 1, 2023. These changes don't affect the total charges you'll see—they'll just be available under different SKUs.

Starting August 1, 2023, you'll see the following changes for SKUs related to Cloud Load Balancing:

  * Currently, SKUs for Cloud Load Balancing usage are categorized under Compute Engine. With this change, we removed the SKUs from their existing Compute Engine product category and created new SKUs in the Networking category (launched on June 1, 2022).

  * Forwarding rule SKUs (minimum and additional charges) are being replaced 1:1 with new SKUs under the Networking category. This change applies to all load balancer types.

  * For internal Application Load Balancers, we're splitting the data processing SKUs into separate inbound and outbound SKUs to be consistent with all other load balancer types. Currently, these are grouped into a single SKU per region. Additionally, proxy instance SKUs for the 3 regions that make up the Americas group (`us-central1`, `us-east1`, and `us-west1`) will be split into separate SKUs for each region.

  * Inbound data processing SKUs are changing as follows:

    * For the global external Application Load Balancer, the classic Application Load Balancer, the external TCP/SSL proxy load balancer, and the external passthrough Network Load Balancer, we're splitting inbound data processing into separate SKUs for each load balancer type (the only exception is that the global external Application Load Balancer and the classic Application Load Balancer will be covered by the same SKU). Currently, inbound data processing is grouped into a single SKU per region for all of these load balancers.
    * For the internal passthrough Network Load Balancer, there is a one to one mapping from the old SKU IDs in the Compute Engine category to the new SKU IDs in the Networking category.
    * Inbound data processing for the 3 regions that make up the Americas group (`us-central1`, `us-east1`, and `us-west1`) will be split into separate SKUs for each region. This change applies to all load balancer types.



The outbound data processing SKUs ([launched on October 1, 2022](https://docs.cloud.google.com/load-balancing/docs/pricing-announce)) already use the new SKU taxonomy, so no changes apply there. Additionally, the newer load balancers (regional external Application Load Balancers and regional internal proxy Network Load Balancers) already use the new SKU taxonomy, so their SKUs are not changing either.

To see which SKUs have changed, review the mapping tables.

## Changes to your pricing and billing

  * The prices for these SKUs have not increased, and your total charges have not changed. If an old SKU is split and mapped to multiple new SKUs, then the usage charges will also be split across the new SKUs so that the total cost remains the same.

  * If you have active discounts, they will be carried over from the old SKU to the corresponding new SKU(s). The discount algorithm applies the highest discount or the lowest price to the new SKU.

  * If you have an [invoiced billing account](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing), the updated SKUs will be available in your [cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) in early August 2023.

  * In your [BigQuery data exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), you'll see the `Networking` category in `product_taxonomy`, which now contains the SKUs for Cloud Load Balancing services.




For prices, see [Cloud Load Balancing pricing](https://docs.cloud.google.com/vpc/network-pricing#lb).

## Prepare for the changes

You can see the new SKUs in the Google Cloud console, your BigQuery exports, and in the APIs. To prepare for the change, make the following changes _on or after August 1, 2023_ :

  * If you're [using BigQuery export data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables) to analyze your costs at the SKU level, update your BigQuery queries to use the new SKUs.

  * If you are using the [Cloud Billing Catalog API](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api) to get data about specific SKUs, update your code to use the new SKUs.




## Mapping old and new SKUs

The following tables compare the old and new SKUs for Cloud Load Balancing. For detailed information about the SKUs, [see the Google Cloud SKUs page](https://docs.cloud.google.com/skus).

### Forwarding rule SKUs

Forwarding rule SKUs (minimum and additional charges) are being replaced 1:1 with new SKUs under the Networking category. This change applies to all load balancer types.

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | B16D-040F-F105 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Americas | E505-1604-58F8 | CBE2-3343-9091 | Cloud Load Balancer Forwarding Rule Minimum for Americas (multi-region)  
6F81-5844-456A | B951-B519-F28F | Network Load Balancing: Forwarding Rule Minimum Service Charge in APAC | E505-1604-58F8 | FA8C-51C0-A961 | Cloud Load Balancer Forwarding Rule Minimum for Taiwan (asia-east1)  
6F81-5844-456A | 871E-2107-A628 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Hong Kong | E505-1604-58F8 | EAB7-980E-756D | Cloud Load Balancer Forwarding Rule Minimum for Hong-Kong (asia-east2)  
6F81-5844-456A | 905F-7B03-36E8 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Osaka | E505-1604-58F8 | D596-89A6-6DDC | Cloud Load Balancer Forwarding Rule Minimum for Osaka (asia-northeast2)  
6F81-5844-456A | DE5F-BD1A-71D6 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Seoul | E505-1604-58F8 | 8B08-9A11-D997 | Cloud Load Balancer Forwarding Rule Minimum for Seoul (asia-northeast3)  
6F81-5844-456A | A7A6-C99A-5F08 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Mumbai | E505-1604-58F8 | 7386-1FD9-A800 | Cloud Load Balancer Forwarding Rule Minimum for Mumbai (asia-south1)  
6F81-5844-456A | 0EA5-6CF7-F5A0 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Delhi | E505-1604-58F8 | 6700-04B6-C33A | Cloud Load Balancer Forwarding Rule Minimum for Delhi (asia-south2)  
6F81-5844-456A | D7D1-E9C5-BE70 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Jakarta | E505-1604-58F8 | 7F61-9F58-84FA | Cloud Load Balancer Forwarding Rule Minimum for Jakarta (asia-southeast2)  
6F81-5844-456A | 6520-F4EA-9B72 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Sydney | E505-1604-58F8 | 6A12-E0BD-0EDA | Cloud Load Balancer Forwarding Rule Minimum for Sydney (australia-southeast1)  
6F81-5844-456A | 3BB1-C2F5-63D0 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Melbourne | E505-1604-58F8 | 57BE-01C8-4514 | Cloud Load Balancer Forwarding Rule Minimum for Melbourne (australia-southeast2)  
6F81-5844-456A | 5DB5-F826-EA96 | Network Load Balancing: Forwarding Rule Minimum Service Charge in EMEA | E505-1604-58F8 | 5199-D194-B502 | Cloud Load Balancer Forwarding Rule Minimum for Belgium (europe-west1)  
6F81-5844-456A | C78C-7C13-6453 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Warsaw | E505-1604-58F8 | BD24-2324-9CA3 | Cloud Load Balancer Forwarding Rule Minimum for Warsaw (europe-central2)  
6F81-5844-456A | DE44-A5E6-6BB7 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Finland | E505-1604-58F8 | E24B-E973-11CB | Cloud Load Balancer Forwarding Rule Minimum for Finland (europe-north1)  
6F81-5844-456A | D81F-3179-7DC8 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Madrid | E505-1604-58F8 | 5636-E051-F716 | Cloud Load Balancer Forwarding Rule Minimum for Madrid (europe-southwest1)  
6F81-5844-456A | 3663-A2AF-0535 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Turin | E505-1604-58F8 | 59CE-780B-1BEF | Cloud Load Balancer Forwarding Rule Minimum for Turin (europe-west12)  
6F81-5844-456A | 1D5A-4083-38DA | Network Load Balancing: Forwarding Rule Minimum Service Charge in London | E505-1604-58F8 | 013C-1954-94D0 | Cloud Load Balancer Forwarding Rule Minimum for London (europe-west2)  
6F81-5844-456A | 79C5-E2C5-20B3 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Frankfurt | E505-1604-58F8 | C68C-D380-ED83 | Cloud Load Balancer Forwarding Rule Minimum for Frankfurt (europe-west3)  
6F81-5844-456A | BD72-394D-4654 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Netherlands | E505-1604-58F8 | FC25-9501-6610 | Cloud Load Balancer Forwarding Rule Minimum for Netherlands (europe-west4)  
6F81-5844-456A | 06E0-A208-A6EF | Network Load Balancing: Forwarding Rule Minimum Service Charge in Zurich | E505-1604-58F8 | 8EE2-4149-065D | Cloud Load Balancer Forwarding Rule Minimum for Zurich (europe-west6)  
6F81-5844-456A | 2756-D989-149A | Network Load Balancing: Forwarding Rule Minimum Service Charge in Milan | E505-1604-58F8 | D41F-35D0-BBD8 | Cloud Load Balancer Forwarding Rule Minimum for Milan (europe-west8)  
6F81-5844-456A | F4AB-0B2B-9612 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Paris | E505-1604-58F8 | 6E37-DB22-A4AD | Cloud Load Balancer Forwarding Rule Minimum for Paris (europe-west9)  
6F81-5844-456A | EF0E-76F7-44D6 | HTTP Load Balancing: Global Forwarding Rule Minimum Service Charge | E505-1604-58F8 | DEE3-C42E-3E4D | Cloud Load Balancer Forwarding Rule Minimum Global  
6F81-5844-456A | 5C6A-09C3-5608 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Japan | E505-1604-58F8 | A869-FB8F-D3BB | Cloud Load Balancer Forwarding Rule Minimum for Tokyo (asia-northeast1)  
6F81-5844-456A | FFA3-8271-3CA2 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Israel | E505-1604-58F8 | 1121-2E21-9C10 | Cloud Load Balancer Forwarding Rule Minimum for Tel Aviv (me-west1)  
6F81-5844-456A | D6D0-B0A1-E5EF | Network Load Balancing: Forwarding Rule Minimum Service Charge in Montreal | E505-1604-58F8 | DADE-2B7E-F372 | Cloud Load Balancer Forwarding Rule Minimum Montréal (northamerica-northeast1)  
6F81-5844-456A | 3768-B325-EF05 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Toronto | E505-1604-58F8 | D4A2-105F-F04E | Cloud Load Balancer Forwarding Rule Minimum Toronto (northamerica-northeast2)  
6F81-5844-456A | 8D95-1829-8FEF | Network Load Balancing: Forwarding Rule Minimum Service Charge in Singapore | E505-1604-58F8 | BD15-114E-9273 | Cloud Load Balancer Forwarding Rule Minimum for Singapore (asia-southeast1)  
6F81-5844-456A | EF82-1614-F989 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Sao Paulo | E505-1604-58F8 | 2982-7600-DEA6 | Cloud Load Balancer Forwarding Rule Minimum for São Paulo (southamerica-east1)  
6F81-5844-456A | 3B61-24FF-804E | Network Load Balancing: Forwarding Rule Minimum Service Charge in Santiago | E505-1604-58F8 | 8D4E-53C4-7129 | Cloud Load Balancer Forwarding Rule Minimum for Santiago (southamerica-west1)  
6F81-5844-456A | 8BE9-9139-BB47 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Columbus | E505-1604-58F8 | F211-265F-DF71 | Cloud Load Balancer Forwarding Rule Minimum for Columbus (us-east5)  
6F81-5844-456A | DAAE-BFE8-75BC | Network Load Balancing: Forwarding Rule Minimum Service Charge in Dallas | E505-1604-58F8 | A28B-FA1C-A6A2 | Cloud Load Balancer Forwarding Rule Minimum for Dallas (us-south1)  
6F81-5844-456A | BDB6-0468-A5F6 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Los Angeles | E505-1604-58F8 | C0CB-7AC2-B941 | Cloud Load Balancer Forwarding Rule Minimum for Los Angeles (us-west2)  
6F81-5844-456A | 6160-746F-A353 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Salt Lake City | E505-1604-58F8 | A727-C39B-3A61 | Cloud Load Balancer Forwarding Rule Minimum for Salt Lake City (us-west3)  
6F81-5844-456A | 4B3A-5C42-DE75 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Las Vegas | E505-1604-58F8 | 3208-53F1-67BF | Cloud Load Balancer Forwarding Rule Minimum for Las Vegas (us-west4)  
6F81-5844-456A | 0638-5864-0180 | Network Load Balancing: Forwarding Rule Minimum Service Charge in Virginia | E505-1604-58F8 | 7CA9-9301-0380 | Cloud Load Balancer Forwarding Rule Minimum for Northern Virginia (us-east4)  
6F81-5844-456A | E7EB-2F82-336A | Network Load Balancing: Forwarding Rule Additional Service Charge in Americas | E505-1604-58F8 | CCD0-28AC-2618 | Cloud Load Balancer Forwarding Rule Additional for Americas (multi-region)  
6F81-5844-456A | A195-ED7B-4FFB | Network Load Balancing: Forwarding Rule Additional Service Charge in APAC | E505-1604-58F8 | CFA5-0398-8BDD | Cloud Load Balancer Forwarding Rule Additional for Taiwan (asia-east1)  
6F81-5844-456A | DD7B-F74F-7BB9 | Network Load Balancing: Forwarding Rule Additional Service Charge in Hong Kong | E505-1604-58F8 | C10C-051B-9BAE | Cloud Load Balancer Forwarding Rule Additional for Hong-Kong (asia-east2)  
6F81-5844-456A | DB2E-08D3-4178 | Network Load Balancing: Forwarding Rule Additional Service Charge in Osaka | E505-1604-58F8 | DE0D-2112-AABC | Cloud Load Balancer Forwarding Rule Additional for Osaka (asia-northeast2)  
6F81-5844-456A | 708D-E39D-6BF2 | Network Load Balancing: Forwarding Rule Additional Service Charge in Seoul | E505-1604-58F8 | 5647-6452-6B44 | Cloud Load Balancer Forwarding Rule Additional for Seoul (asia-northeast3)  
6F81-5844-456A | 57C0-E4DC-1530 | Network Load Balancing: Forwarding Rule Additional Service Charge in Mumbai | E505-1604-58F8 | AE19-BD38-8EF7 | Cloud Load Balancer Forwarding Rule Additional for Mumbai (asia-south1)  
6F81-5844-456A | B406-A983-9A35 | Network Load Balancing: Forwarding Rule Additional Service Charge in Delhi | E505-1604-58F8 | F1DB-A9D9-0AA8 | Cloud Load Balancer Forwarding Rule Additional for Delhi (asia-south2)  
6F81-5844-456A | FD68-140E-B8FD | Network Load Balancing: Forwarding Rule Additional Service Charge in Jakarta | E505-1604-58F8 | 859D-17AD-B174 | Cloud Load Balancer Forwarding Rule Additional for Jakarta (asia-southeast2)  
6F81-5844-456A | 4F10-CF4C-89EE | Network Load Balancing: Forwarding Rule Additional Service Charge in Sydney | E505-1604-58F8 | CC0F-A7B0-E132 | Cloud Load Balancer Forwarding Rule Additional for Sydney (australia-southeast1)  
6F81-5844-456A | 1277-D450-1E81 | Network Load Balancing: Forwarding Rule Additional Service Charge in Melbourne | E505-1604-58F8 | 5714-1A19-7E32 | Cloud Load Balancer Forwarding Rule Additional for Melbourne (australia-southeast2)  
6F81-5844-456A | EC8D-661C-E4BB | Network Load Balancing: Forwarding Rule Additional Service Charge in EMEA | E505-1604-58F8 | 691D-CC7F-C2FD | Cloud Load Balancer Forwarding Rule Additional for Belgium (europe-west1)  
6F81-5844-456A | 7E55-7954-8C7A | Network Load Balancing: Forwarding Rule Additional Service Charge in Warsaw | E505-1604-58F8 | C915-C3E5-996A | Cloud Load Balancer Forwarding Rule Additional for Warsaw (europe-central2)  
6F81-5844-456A | 3A29-A3F5-2A9E | Network Load Balancing: Forwarding Rule Additional Service Charge in Finland | E505-1604-58F8 | 8E37-C6A1-7136 | Cloud Load Balancer Forwarding Rule Additional for Finland (europe-north1)  
6F81-5844-456A | F45B-28E8-2D17 | Network Load Balancing: Forwarding Rule Additional Service Charge in Madrid | E505-1604-58F8 | 26B9-2DCD-C7B1 | Cloud Load Balancer Forwarding Rule Additional for Madrid (europe-southwest1)  
6F81-5844-456A | 0336-902B-7BA7 | Network Load Balancing: Forwarding Rule Additional Service Charge in Turin | E505-1604-58F8 | ED80-F3FB-B347 | Cloud Load Balancer Forwarding Rule Additional for Turin (europe-west12)  
6F81-5844-456A | B1CD-16B2-F244 | Network Load Balancing: Forwarding Rule Additional Service Charge in London | E505-1604-58F8 | 7D45-E6E6-FD10 | Cloud Load Balancer Forwarding Rule Additional for London (europe-west2)  
6F81-5844-456A | 50A5-3999-3BE0 | Network Load Balancing: Forwarding Rule Additional Service Charge in Frankfurt | E505-1604-58F8 | D1D7-F3FB-53CC | Cloud Load Balancer Forwarding Rule Additional for Frankfurt (europe-west3)  
6F81-5844-456A | B54D-F8FA-93BA | Network Load Balancing: Forwarding Rule Additional Service Charge in Netherlands | E505-1604-58F8 | D1FC-A996-BE0D | Cloud Load Balancer Forwarding Rule Additional for Netherlands (europe-west4)  
6F81-5844-456A | 7895-A101-4B66 | Network Load Balancing: Forwarding Rule Additional Service Charge in Zurich | E505-1604-58F8 | 426E-6CAF-D501 | Cloud Load Balancer Forwarding Rule Additional for Zurich (europe-west6)  
6F81-5844-456A | 3198-C5DD-C7D6 | Network Load Balancing: Forwarding Rule Additional Service Charge in Milan | E505-1604-58F8 | 80E7-9512-4B52 | Cloud Load Balancer Forwarding Rule Additional for Milan (europe-west8)  
6F81-5844-456A | 961F-39D7-372E | Network Load Balancing: Forwarding Rule Additional Service Charge in Paris | E505-1604-58F8 | D747-DEC1-F0F2 | Cloud Load Balancer Forwarding Rule Additional for Paris (europe-west9)  
6F81-5844-456A | 01CB-E623-2700 | HTTP Load Balancing: Global Forwarding Rule Additional Service Charge | E505-1604-58F8 | 1211-928B-AF92 | Cloud Load Balancer Forwarding Rule Additional Global  
6F81-5844-456A | BCD4-D78B-7A56 | Network Load Balancing: Forwarding Rule Additional Service Charge in Japan | E505-1604-58F8 | 5D09-9123-4D37 | Cloud Load Balancer Forwarding Rule Additional for Tokyo (asia-northeast1)  
6F81-5844-456A | 49B5-74A3-B11B | Network Load Balancing: Forwarding Rule Additional Service Charge in Israel | E505-1604-58F8 | 3C88-6CBB-61CB | Cloud Load Balancer Forwarding Rule Additional for Tel Aviv (me-west1)  
6F81-5844-456A | C5A9-DB4F-0121 | Network Load Balancing: Forwarding Rule Additional Service Charge in Montreal | E505-1604-58F8 | A20E-B53D-FE46 | Cloud Load Balancer Forwarding Rule Additional Montréal (northamerica-northeast1)  
6F81-5844-456A | 2CCF-EBB6-FB02 | Network Load Balancing: Forwarding Rule Additional Service Charge in Toronto | E505-1604-58F8 | 53C1-1FDE-51BD | Cloud Load Balancer Forwarding Rule Additional Toronto (northamerica-northeast2)  
6F81-5844-456A | B540-2B9A-49D8 | Network Load Balancing: Forwarding Rule Additional Service Charge in Singapore | E505-1604-58F8 | C0E1-DD89-C281 | Cloud Load Balancer Forwarding Rule Additional for Singapore (asia-southeast1)  
6F81-5844-456A | FE57-0AA9-0BE2 | Network Load Balancing: Forwarding Rule Additional Service Charge in Sao Paulo | E505-1604-58F8 | F526-42E6-4F7D | Cloud Load Balancer Forwarding Rule Additional for São Paulo (southamerica-east1)  
6F81-5844-456A | C65E-20EB-9522 | Network Load Balancing: Forwarding Rule Additional Service Charge in Santiago | E505-1604-58F8 | 1FF7-DA50-8DD7 | Cloud Load Balancer Forwarding Rule Additional for Santiago (southamerica-west1)  
6F81-5844-456A | FB0C-85A6-AB13 | Network Load Balancing: Forwarding Rule Additional Service Charge in Columbus | E505-1604-58F8 | 1C09-1DB1-1910 | Cloud Load Balancer Forwarding Rule Additional for Columbus (us-east5)  
6F81-5844-456A | 572F-6C0B-0DA9 | Network Load Balancing: Forwarding Rule Additional Service Charge in Dallas | E505-1604-58F8 | 0665-8CB5-0440 | Cloud Load Balancer Forwarding Rule Additional for Dallas (us-south1)  
6F81-5844-456A | 74A7-5660-D5C5 | Network Load Balancing: Forwarding Rule Additional Service Charge in Los Angeles | E505-1604-58F8 | 49E6-2E71-D0E0 | Cloud Load Balancer Forwarding Rule Additional for Los Angeles (us-west2)  
6F81-5844-456A | 7DAD-BAF9-75EC | Network Load Balancing: Forwarding Rule Additional Service Charge in Salt Lake City | E505-1604-58F8 | DC7F-37E7-941D | Cloud Load Balancer Forwarding Rule Additional for Salt Lake City (us-west3)  
6F81-5844-456A | E352-668E-E878 | Network Load Balancing: Forwarding Rule Additional Service Charge in Las Vegas | E505-1604-58F8 | C8CD-9CDF-D3D1 | Cloud Load Balancer Forwarding Rule Additional for Las Vegas (us-west4)  
6F81-5844-456A | 1BA0-F32B-402F | Network Load Balancing: Forwarding Rule Additional Service Charge in Virginia | E505-1604-58F8 | C0DC-2B04-3A61 | Cloud Load Balancer Forwarding Rule Additional for Northern Virginia (us-east4)  
  
### Data processing SKUs for external load balancers

For global external Application Load Balancers, external proxy Network Load Balancers, and external passthrough Network Load Balancers, the inbound data processing SKUs are being split into separate SKUs for each load balancer type.

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | 38AF-E629-9E12 | Network Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 7AB4-E0E4-8DB1 | Global External Proxy Network Load Balancer Inbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 38AF-E629-9E12 | Network Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 3B8D-D41C-EE09 | External Pass-through Network Load Balancer Inbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 38AF-E629-9E12 | Network Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 1323-93F5-4A9B | Global External Application Load Balancer Inbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 78D8-A54A-EF86 | Network Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | E4EC-BF15-73FC | External Pass-through Network Load Balancer Inbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | 78D8-A54A-EF86 | Network Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | 52F2-8065-89F2 | Global External Proxy Network Load Balancer Inbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | 78D8-A54A-EF86 | Network Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | 4ED2-C329-7BB8 | Global External Application Load Balancer Inbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | A4C6-0D17-0262 | Network Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | EE27-0570-9D74 | Global External Application Load Balancer Inbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | A4C6-0D17-0262 | Network Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | 3A52-2496-0926 | Global External Proxy Network Load Balancer Inbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | A4C6-0D17-0262 | Network Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | FED3-F28B-BABE | External Pass-through Network Load Balancer Inbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | A7AA-355D-2C8A | Network Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | 2C6C-5C38-1D0A | Global External Proxy Network Load Balancer Inbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | A7AA-355D-2C8A | Network Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | 147E-ED36-67D1 | Global External Application Load Balancer Inbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | A7AA-355D-2C8A | Network Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | B854-232C-1996 | External Pass-through Network Load Balancer Inbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | D1E5-12A6-AA4B | Network Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | A219-5A92-9E41 | Global External Proxy Network Load Balancer Inbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | D1E5-12A6-AA4B | Network Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | 91F1-423B-CF42 | Global External Application Load Balancer Inbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | D1E5-12A6-AA4B | Network Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | F5C2-3231-6887 | External Pass-through Network Load Balancer Inbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | D1F3-4FEC-0509 | Network Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | FA87-8E3C-6E12 | External Pass-through Network Load Balancer Inbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | D1F3-4FEC-0509 | Network Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | 3256-EB31-900A | Global External Proxy Network Load Balancer Inbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | D1F3-4FEC-0509 | Network Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | D584-C594-2CF3 | Global External Application Load Balancer Inbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | A1D2-22B0-05C9 | Network Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | 0674-A2A6-E657 | External Pass-through Network Load Balancer Inbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | A1D2-22B0-05C9 | Network Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | 1044-F9DE-5653 | Global External Proxy Network Load Balancer Inbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | A1D2-22B0-05C9 | Network Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | 80D1-D13A-D3A1 | Global External Application Load Balancer Inbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | C91B-6768-960F | Network Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | 4567-6B85-48AB | Global External Proxy Network Load Balancer Inbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | C91B-6768-960F | Network Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | 7153-D75A-B5F2 | Global External Application Load Balancer Inbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | C91B-6768-960F | Network Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | A8B5-68E7-0049 | External Pass-through Network Load Balancer Inbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | BBE1-62E6-DC53 | Network Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | 30C8-6E9E-3068 | Global External Application Load Balancer Inbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | BBE1-62E6-DC53 | Network Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | DB5F-271D-55AA | External Pass-through Network Load Balancer Inbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | BBE1-62E6-DC53 | Network Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | 9042-FB64-CB62 | Global External Proxy Network Load Balancer Inbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | 9D7D-D85E-D705 | Network Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | 352B-4670-13F6 | Global External Application Load Balancer Inbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | 9D7D-D85E-D705 | Network Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | 1387-E4AF-2B26 | External Pass-through Network Load Balancer Inbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | 9D7D-D85E-D705 | Network Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | 2121-279C-095A | Global External Proxy Network Load Balancer Inbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | CD52-EED2-BB12 | Network Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 936E-D32D-AE7F | Global External Proxy Network Load Balancer Inbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | CD52-EED2-BB12 | Network Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 02C8-21E2-39BB | Global External Application Load Balancer Inbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | CD52-EED2-BB12 | Network Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 9DC8-DE39-3D92 | External Pass-through Network Load Balancer Inbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | 06FF-8F95-D28A | Network Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | FD64-D1EF-E915 | External Pass-through Network Load Balancer Inbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | 06FF-8F95-D28A | Network Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | 42C9-04D5-B1E5 | Global External Application Load Balancer Inbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | 06FF-8F95-D28A | Network Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | B7D9-1970-1878 | Global External Proxy Network Load Balancer Inbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | DD96-7784-5984 | Network Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | 98DD-0DF0-631F | External Pass-through Network Load Balancer Inbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | DD96-7784-5984 | Network Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | 32B2-9911-11DC | Global External Application Load Balancer Inbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | DD96-7784-5984 | Network Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | D9F4-C1DC-CC2A | Global External Proxy Network Load Balancer Inbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | 8C4E-75AD-9423 | Network Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 13E0-8535-1E47 | Global External Proxy Network Load Balancer Inbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | 8C4E-75AD-9423 | Network Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 9DB8-72ED-AF1D | Global External Application Load Balancer Inbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | 8C4E-75AD-9423 | Network Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 0B07-C485-7D71 | External Pass-through Network Load Balancer Inbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | B568-418C-F885 | Network Load Balancing: Data Processing Charge in London | E505-1604-58F8 | E9ED-79BF-0DEE | External Pass-through Network Load Balancer Inbound Data Processing for London (europe-west2)  
6F81-5844-456A | B568-418C-F885 | Network Load Balancing: Data Processing Charge in London | E505-1604-58F8 | C44D-AEFB-B6E6 | Global External Application Load Balancer Inbound Data Processing for London (europe-west2)  
6F81-5844-456A | B568-418C-F885 | Network Load Balancing: Data Processing Charge in London | E505-1604-58F8 | 4244-95C2-50A4 | Global External Proxy Network Load Balancer Inbound Data Processing for London (europe-west2)  
6F81-5844-456A | 02A6-2E7C-60BD | Network Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | B964-BA66-245D | External Pass-through Network Load Balancer Inbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 02A6-2E7C-60BD | Network Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | A7C2-BF54-1B4B | Global External Application Load Balancer Inbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 02A6-2E7C-60BD | Network Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | EF12-ED10-F367 | Global External Proxy Network Load Balancer Inbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 5ADA-0BDE-006C | Network Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | 3273-B721-DBB3 | External Pass-through Network Load Balancer Inbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | 5ADA-0BDE-006C | Network Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | FEA1-EF45-4C03 | Global External Proxy Network Load Balancer Inbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | 5ADA-0BDE-006C | Network Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | EEF0-812C-FB62 | Global External Application Load Balancer Inbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | CC30-52C0-5666 | Network Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | D509-DDE6-A423 | Global External Proxy Network Load Balancer Inbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | CC30-52C0-5666 | Network Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | 5275-C7DF-707B | Global External Application Load Balancer Inbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | CC30-52C0-5666 | Network Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | EDBB-B430-60AA | External Pass-through Network Load Balancer Inbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | F6D0-F84F-89E8 | Network Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | 6657-8027-DE5C | Global External Proxy Network Load Balancer Inbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | F6D0-F84F-89E8 | Network Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | C885-1B3A-BF6C | Global External Application Load Balancer Inbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | F6D0-F84F-89E8 | Network Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | E78B-13D8-3D8D | External Pass-through Network Load Balancer Inbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | D52A-50F0-C8E5 | Network Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | D775-4A18-F0A1 | Global External Proxy Network Load Balancer Inbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | D52A-50F0-C8E5 | Network Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | 5494-2FF9-C816 | Global External Application Load Balancer Inbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | D52A-50F0-C8E5 | Network Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | C4C0-70F2-FB50 | External Pass-through Network Load Balancer Inbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | B2AB-05E6-3EE9 | Network Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | B269-C4CE-9C53 | Global External Proxy Network Load Balancer Inbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | B2AB-05E6-3EE9 | Network Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | E2A1-5EE9-F2BB | External Pass-through Network Load Balancer Inbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | B2AB-05E6-3EE9 | Network Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | 4445-66EE-8E07 | Global External Application Load Balancer Inbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | 80CC-1110-0F9C | Network Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | D335-0B27-96C8 | External Pass-through Network Load Balancer Inbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | 80CC-1110-0F9C | Network Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | 8BFB-881C-3E27 | Global External Application Load Balancer Inbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | 80CC-1110-0F9C | Network Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | 877F-11AB-0E53 | Global External Proxy Network Load Balancer Inbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 2998-2185-EA3D | Global External Application Load Balancer Inbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 0141-1398-7370 | External Pass-through Network Load Balancer Inbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 0404-9F96-18D3 | Global External Proxy Network Load Balancer Inbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 1703-39A5-55D1 | Global External Proxy Network Load Balancer Inbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | C134-B6DB-FFCB | Global External Application Load Balancer Inbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 49F4-3174-4EBF | External Pass-through Network Load Balancer Inbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 6A71-CA15-8BAD | Global External Application Load Balancer Inbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | BB93-3F28-5082 | External Pass-through Network Load Balancer Inbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | EECF-0EFC-74CA | Network Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 9EC4-0599-3DFB | Global External Proxy Network Load Balancer Inbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | CFE3-1EA2-A260 | Network Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | B757-3C5E-FFFA | Global External Proxy Network Load Balancer Inbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | CFE3-1EA2-A260 | Network Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | DB4F-753D-9167 | Global External Application Load Balancer Inbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | CFE3-1EA2-A260 | Network Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | 94F6-87B2-A267 | External Pass-through Network Load Balancer Inbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | BD07-762F-A141 | Network Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | 8AAE-A270-04F3 | External Pass-through Network Load Balancer Inbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | BD07-762F-A141 | Network Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | F468-ACDC-268D | Global External Application Load Balancer Inbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | BD07-762F-A141 | Network Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | D697-472D-D67B | Global External Proxy Network Load Balancer Inbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | 635B-EA65-F955 | Network Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | 6137-D730-2BF2 | External Pass-through Network Load Balancer Inbound Data Processing for Singapore (asia-southeast1)  
6F81-5844-456A | 635B-EA65-F955 | Network Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | CD57-A256-F8C6 | Global External Proxy Network Load Balancer Inbound Data Processing for Asiasoutheast1  
6F81-5844-456A | 635B-EA65-F955 | Network Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | 17FF-00DE-2217 | Global External Application Load Balancer Inbound Data Processing for Asiasoutheast1  
6F81-5844-456A | 16F3-35B2-E08E | Network Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | A2EE-BC41-872B | Global External Proxy Network Load Balancer Inbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | 16F3-35B2-E08E | Network Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | 214E-A5B6-CDF0 | External Pass-through Network Load Balancer Inbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | 16F3-35B2-E08E | Network Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | C955-1B6C-2CDA | Global External Application Load Balancer Inbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | EF69-317E-AA10 | Network Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 0021-3441-7CA8 | External Pass-through Network Load Balancer Inbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | EF69-317E-AA10 | Network Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 6AE0-8B61-F977 | Global External Proxy Network Load Balancer Inbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | EF69-317E-AA10 | Network Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 4EB4-EDED-BC64 | Global External Application Load Balancer Inbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | FC33-23D7-4558 | Network Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | 6596-D635-7E79 | External Pass-through Network Load Balancer Inbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | FC33-23D7-4558 | Network Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | 3CF1-CA3F-76D3 | Global External Proxy Network Load Balancer Inbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | FC33-23D7-4558 | Network Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | 26B1-07D2-A64C | Global External Application Load Balancer Inbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | 33BD-F664-544E | Network Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | 1717-C91F-D029 | Global External Application Load Balancer Inbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | 33BD-F664-544E | Network Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | BFFB-C4C1-64F3 | External Pass-through Network Load Balancer Inbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | 33BD-F664-544E | Network Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | F40B-CD06-EAC2 | Global External Proxy Network Load Balancer Inbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | B8EC-17C7-D631 | Network Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | 9C35-0938-A0AE | External Pass-through Network Load Balancer Inbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | B8EC-17C7-D631 | Network Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | E338-9D01-3876 | Global External Application Load Balancer Inbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | B8EC-17C7-D631 | Network Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | EF46-5109-2924 | Global External Proxy Network Load Balancer Inbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | E168-681C-4600 | Network Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | 6C2B-3DE3-773A | Global External Proxy Network Load Balancer Inbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | E168-681C-4600 | Network Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | 3A0F-4D91-E4EC | External Pass-through Network Load Balancer Inbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | E168-681C-4600 | Network Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | 09C1-4457-40AD | Global External Application Load Balancer Inbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | 2C4C-1A16-B380 | Network Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | 074D-C2E7-91D8 | Global External Application Load Balancer Inbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | 2C4C-1A16-B380 | Network Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | B4F7-3AE8-B539 | Global External Proxy Network Load Balancer Inbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | 2C4C-1A16-B380 | Network Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | AE26-2E6C-BADA | External Pass-through Network Load Balancer Inbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | 6268-AFAB-DB8D | Network Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | 7B50-98A7-4F1C | External Pass-through Network Load Balancer Inbound Data Processing for Northern Virginia (us-east4)  
6F81-5844-456A | 6268-AFAB-DB8D | Network Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | 691C-F431-F86A | Global External Application Load Balancer Inbound Data Processing for Northern Virginia (us-east4)  
6F81-5844-456A | 6268-AFAB-DB8D | Network Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | CD61-F6FB-AF41 | Global External Proxy Network Load Balancer Inbound Data Processing for Northern Virginia (us-east4)  
  
### Data processing SKUs for internal passthrough Network Load Balancers

Inbound data processing SKUs for the Americas region (which covers `us-central1`, `us-east1`, and `us-west1`) are being split into separate SKUs for each region.

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | 7F61-7A94-9E9F | Network Internal Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 5707-7CAE-35F4 | Internal Pass-through Network Load Balancer Inbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 3703-C558-60EF | Network Internal Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | C2D4-9C2E-D424 | Internal Pass-through Network Load Balancer Inbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | 5338-8971-360B | Network Internal Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | 6990-0DD6-B2EA | Internal Pass-through Network Load Balancer Inbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | 40B7-CA24-E9AF | Network Internal Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | 3F08-CCA6-CB14 | Internal Pass-through Network Load Balancer Inbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | 6B2A-BA0F-8271 | Network Internal Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | 04C3-B191-CDC2 | Internal Pass-through Network Load Balancer Inbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | 92CD-6A05-D8A9 | Network Internal Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | E2AF-587B-FEE9 | Internal Pass-through Network Load Balancer Inbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | 8515-3713-6F5C | Network Internal Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | 3583-5372-FA10 | Internal Pass-through Network Load Balancer Inbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | 6DB6-65DD-B3EC | Network Internal Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | 762F-9359-99B6 | Internal Pass-through Network Load Balancer Inbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | EFF2-0ECB-3560 | Network Internal Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | 1F59-E2F8-A674 | Internal Pass-through Network Load Balancer Inbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | 90A3-1544-207D | Network Internal Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | EEE1-39DF-D18E | Internal Pass-through Network Load Balancer Inbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | BE9D-D4E5-FE03 | Network Internal Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 9D3D-07B9-3219 | Internal Pass-through Network Load Balancer Inbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | 6A37-0C6A-2BDB | Network Internal Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | B4AF-A5A3-40D8 | Internal Pass-through Network Load Balancer Inbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | 846D-FBED-C6F0 | Network Internal Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | FB40-D5B2-0C12 | Internal Pass-through Network Load Balancer Inbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | 6EBB-614A-BCD7 | Network Internal Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 52D9-9094-3866 | Internal Pass-through Network Load Balancer Inbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | C70E-C44C-BB22 | Network Internal Load Balancing: Data Processing Charge in London | E505-1604-58F8 | 8D9B-BA81-DA7D | Internal Pass-through Network Load Balancer Inbound Data Processing for London (europe-west2)  
6F81-5844-456A | 3C9C-3C7E-C0E5 | Network Internal Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | 64AB-878C-4A51 | Internal Pass-through Network Load Balancer Inbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 43C4-398E-1141 | Network Internal Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | 53BC-DEDC-1ED1 | Internal Pass-through Network Load Balancer Inbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | C53B-EA59-7DA1 | Network Internal Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | 77E9-7743-1A80 | Internal Pass-through Network Load Balancer Inbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | C73D-9437-1467 | Network Internal Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | DED4-F50B-6AF6 | Internal Pass-through Network Load Balancer Inbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | D823-0700-BB00 | Network Internal Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | 3981-DF08-635F | Internal Pass-through Network Load Balancer Inbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | 43FA-52D7-42CF | Network Internal Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | 886D-9AF4-4CA0 | Internal Pass-through Network Load Balancer Inbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | 6A91-7D75-C3AD | Network Internal Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | B7F9-2CD8-CCE1 | Internal Pass-through Network Load Balancer Inbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | AFB4-C45D-7D2C | Network Internal Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | F6C4-AC52-0E8A | Internal Pass-through Network Load Balancer Inbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | AFB4-C45D-7D2C | Network Internal Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 842C-9F64-C51C | Internal Pass-through Network Load Balancer Inbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | AFB4-C45D-7D2C | Network Internal Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | B595-22C9-6B93 | Internal Pass-through Network Load Balancer Inbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | E69B-3AA3-C2D3 | Network Internal Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | 268A-CC54-6EEA | Internal Pass-through Network Load Balancer Inbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | C937-C9FC-AD21 | Network Internal Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | 4843-396B-3C8C | Internal Pass-through Network Load Balancer Inbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | 2C38-8FA8-DB9B | Network Internal Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | 809B-2C51-CA43 | Internal Pass-through Network Load Balancer Inbound Data Processing for Singapore (asia-southeast1)  
6F81-5844-456A | 32BA-964D-69AF | Network Internal Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | 91C3-16F7-88E2 | Internal Pass-through Network Load Balancer Inbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | 36AD-6C12-7F2D | Network Internal Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 65B6-9849-9F29 | Internal Pass-through Network Load Balancer Inbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | F875-2CCE-40A3 | Network Internal Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | 01DC-60F8-CF9F | Internal Pass-through Network Load Balancer Inbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | 6257-9C23-C54E | Network Internal Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | CD4A-48D2-50C4 | Internal Pass-through Network Load Balancer Inbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | 9588-78A8-F411 | Network Internal Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | F8D0-ECA2-30EE | Internal Pass-through Network Load Balancer Inbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | 1CDB-257A-5EF6 | Network Internal Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | 9A22-D140-B3E5 | Internal Pass-through Network Load Balancer Inbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | DB02-1C49-679F | Network Internal Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | A2D7-9919-AB5A | Internal Pass-through Network Load Balancer Inbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | 14A6-4C73-1CD6 | Network Internal Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | 3260-8263-41F5 | Internal Pass-through Network Load Balancer Inbound Data Processing for Northern Virginia (us-east4)  
  
### Data processing SKUs for internal Application Load Balancers

For internal Application Load Balancers, the data processing SKUs have been split into separate inbound and outbound SKUs.

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | 33F2-F70B-3836 | Internal HTTP(S) Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 4535-9267-B7AF | Regional Internal Application Load Balancer Inbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 33F2-F70B-3836 | Internal HTTP(S) Load Balancing: Data Processing Charge in APAC | E505-1604-58F8 | 81D8-CD8C-26D9 | Regional Internal Application Load Balancer Outbound Data Processing for Taiwan (asia-east1)  
6F81-5844-456A | 9E70-AD3A-B311 | Internal HTTP(S) Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | 11A8-3A5E-1FD6 | Regional Internal Application Load Balancer Outbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | 9E70-AD3A-B311 | Internal HTTP(S) Load Balancing: Data Processing Charge in Hong Kong | E505-1604-58F8 | 4470-DE46-DFED | Regional Internal Application Load Balancer Inbound Data Processing for Hong-Kong (asia-east2)  
6F81-5844-456A | E397-3840-2A81 | Internal HTTP(S) Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | 60E5-FF97-59BA | Regional Internal Application Load Balancer Outbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | E397-3840-2A81 | Internal HTTP(S) Load Balancing: Data Processing Charge in Osaka | E505-1604-58F8 | C9B5-38A2-7E60 | Regional Internal Application Load Balancer Inbound Data Processing for Osaka (asia-northeast2)  
6F81-5844-456A | EFC0-13CC-3811 | Internal HTTP(S) Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | A6E5-A948-0763 | Regional Internal Application Load Balancer Inbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | EFC0-13CC-3811 | Internal HTTP(S) Load Balancing: Data Processing Charge in Seoul | E505-1604-58F8 | 7128-6796-C762 | Regional Internal Application Load Balancer Outbound Data Processing for Seoul (asia-northeast3)  
6F81-5844-456A | F676-6CEF-1DB4 | Internal HTTP(S) Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | C9FA-EB51-3C47 | Regional Internal Application Load Balancer Inbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | F676-6CEF-1DB4 | Internal HTTP(S) Load Balancing: Data Processing Charge in Mumbai | E505-1604-58F8 | AA4B-096A-C6AC | Regional Internal Application Load Balancer Outbound Data Processing for Mumbai (asia-south1)  
6F81-5844-456A | 4D6E-7414-4AB9 | Internal HTTP(S) Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | 5926-EEE6-347C | Regional Internal Application Load Balancer Inbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | 4D6E-7414-4AB9 | Internal HTTP(S) Load Balancing: Data Processing Charge in Delhi | E505-1604-58F8 | 1F13-6494-91EE | Regional Internal Application Load Balancer Outbound Data Processing for Delhi (asia-south2)  
6F81-5844-456A | 9C15-136D-5C73 | Internal HTTP(S) Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | BCB7-8C6E-3168 | Regional Internal Application Load Balancer Inbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | 9C15-136D-5C73 | Internal HTTP(S) Load Balancing: Data Processing Charge in Jakarta | E505-1604-58F8 | 8E08-71A5-CAFE | Regional Internal Application Load Balancer Outbound Data Processing for Jakarta (asia-southeast2)  
6F81-5844-456A | B727-69D9-305D | Internal HTTP(S) Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | C0E9-F2E4-EF62 | Regional Internal Application Load Balancer Outbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | B727-69D9-305D | Internal HTTP(S) Load Balancing: Data Processing Charge in Sydney | E505-1604-58F8 | 96E7-0117-EFEA | Regional Internal Application Load Balancer Inbound Data Processing for Sydney (australia-southeast1)  
6F81-5844-456A | F68D-FC20-EE59 | Internal HTTP(S) Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | EB73-BA27-ECDD | Regional Internal Application Load Balancer Outbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | F68D-FC20-EE59 | Internal HTTP(S) Load Balancing: Data Processing Charge in Melbourne | E505-1604-58F8 | 702D-3303-5B3E | Regional Internal Application Load Balancer Inbound Data Processing for Melbourne (australia-southeast2)  
6F81-5844-456A | BD46-A961-279C | Internal HTTP(S) Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | BF24-44F1-F633 | Regional Internal Application Load Balancer Inbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | BD46-A961-279C | Internal HTTP(S) Load Balancing: Data Processing Charge in EMEA | E505-1604-58F8 | 1BBD-45CB-27B7 | Regional Internal Application Load Balancer Outbound Data Processing for Belgium (europe-west1)  
6F81-5844-456A | 7DAD-D5D5-6195 | Internal HTTP(S) Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 4DA7-D5C4-718B | Regional Internal Application Load Balancer Inbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | 7DAD-D5D5-6195 | Internal HTTP(S) Load Balancing: Data Processing Charge in Warsaw | E505-1604-58F8 | 189C-A763-CD58 | Regional Internal Application Load Balancer Outbound Data Processing for Warsaw (europe-central2)  
6F81-5844-456A | 111F-E51F-FC13 | Internal HTTP(S) Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | 5EE5-E7CB-B8B3 | Regional Internal Application Load Balancer Inbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | 111F-E51F-FC13 | Internal HTTP(S) Load Balancing: Data Processing Charge in Finland | E505-1604-58F8 | 1BEA-EE13-98F4 | Regional Internal Application Load Balancer Outbound Data Processing for Finland (europe-north1)  
6F81-5844-456A | 1647-F3B6-0925 | Internal HTTP(S) Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | 4CD9-1764-DDAA | Regional Internal Application Load Balancer Outbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | 1647-F3B6-0925 | Internal HTTP(S) Load Balancing: Data Processing Charge in Madrid | E505-1604-58F8 | 3D46-430C-C76D | Regional Internal Application Load Balancer Inbound Data Processing for Madrid (europe-southwest1)  
6F81-5844-456A | 995D-7C45-F65C | Internal HTTP(S) Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 345D-3365-ED2B | Regional Internal Application Load Balancer Inbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | 995D-7C45-F65C | Internal HTTP(S) Load Balancing: Data Processing Charge in Turin | E505-1604-58F8 | 82EF-A30A-1CA1 | Regional Internal Application Load Balancer Outbound Data Processing for Turin (europe-west12)  
6F81-5844-456A | 7099-5BB9-5933 | Internal HTTP(S) Load Balancing: Data Processing Charge in London | E505-1604-58F8 | 74D6-C394-DC37 | Regional Internal Application Load Balancer Outbound Data Processing for London (europe-west2)  
6F81-5844-456A | 7099-5BB9-5933 | Internal HTTP(S) Load Balancing: Data Processing Charge in London | E505-1604-58F8 | 82FE-AD14-F24E | Regional Internal Application Load Balancer Inbound Data Processing for London (europe-west2)  
6F81-5844-456A | 6120-81F0-CB47 | Internal HTTP(S) Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | A2AF-CC4B-04D3 | Regional Internal Application Load Balancer Inbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 6120-81F0-CB47 | Internal HTTP(S) Load Balancing: Data Processing Charge in Frankfurt | E505-1604-58F8 | 2107-DC88-007B | Regional Internal Application Load Balancer Outbound Data Processing for Frankfurt (europe-west3)  
6F81-5844-456A | 2E10-13F8-DA39 | Internal HTTP(S) Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | 0714-EC63-5CAB | Regional Internal Application Load Balancer Inbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | 2E10-13F8-DA39 | Internal HTTP(S) Load Balancing: Data Processing Charge in Netherlands | E505-1604-58F8 | ABAA-FD5B-5E11 | Regional Internal Application Load Balancer Outbound Data Processing for Netherlands (europe-west4)  
6F81-5844-456A | 578A-B9C8-7563 | Internal HTTP(S) Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | A5B3-706F-002B | Regional Internal Application Load Balancer Outbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | 578A-B9C8-7563 | Internal HTTP(S) Load Balancing: Data Processing Charge in Zurich | E505-1604-58F8 | 503B-F8E4-7263 | Regional Internal Application Load Balancer Inbound Data Processing for Zurich (europe-west6)  
6F81-5844-456A | 0274-C0B4-580F | Internal HTTP(S) Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | 6D92-C68D-6937 | Regional Internal Application Load Balancer Inbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | 0274-C0B4-580F | Internal HTTP(S) Load Balancing: Data Processing Charge in Milan | E505-1604-58F8 | 59D9-2B47-F6A1 | Regional Internal Application Load Balancer Outbound Data Processing for Milan (europe-west8)  
6F81-5844-456A | C659-5B7A-23F0 | Internal HTTP(S) Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | 2FD9-4A1F-53FF | Regional Internal Application Load Balancer Inbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | C659-5B7A-23F0 | Internal HTTP(S) Load Balancing: Data Processing Charge in Paris | E505-1604-58F8 | 74B7-A13F-E122 | Regional Internal Application Load Balancer Outbound Data Processing for Paris (europe-west9)  
6F81-5844-456A | F51A-4458-46DD | Internal HTTP(S) Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | 6ACF-9D58-4EDF | Regional Internal Application Load Balancer Outbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | F51A-4458-46DD | Internal HTTP(S) Load Balancing: Data Processing Charge in Japan | E505-1604-58F8 | 4064-6E7F-F5EA | Regional Internal Application Load Balancer Inbound Data Processing for Tokyo (asia-northeast1)  
6F81-5844-456A | FFB9-9140-7ADB | Internal HTTP(S) Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | CF19-B392-3FB5 | Regional Internal Application Load Balancer Inbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | FFB9-9140-7ADB | Internal HTTP(S) Load Balancing: Data Processing Charge in Israel | E505-1604-58F8 | 04DC-199F-0B97 | Regional Internal Application Load Balancer Outbound Data Processing for Tel Aviv (me-west1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 4429-11EE-492E | Regional Internal Application Load Balancer Outbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | D3C9-C729-751E | Regional Internal Application Load Balancer Outbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | EE3B-1EA2-36FD | Regional Internal Application Load Balancer Inbound Data Processing for Oregon (us-west1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | F46C-FC3C-7993 | Regional Internal Application Load Balancer Inbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | A01A-158E-76FE | Regional Internal Application Load Balancer Inbound Data Processing for South Carolina (us-east1)  
6F81-5844-456A | 29DF-A433-58F8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Americas | E505-1604-58F8 | 1713-49C6-A015 | Regional Internal Application Load Balancer Outbound Data Processing for Iowa (us-central1)  
6F81-5844-456A | C7B7-F513-FAA1 | Internal HTTP(S) Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | 161B-4943-3552 | Regional Internal Application Load Balancer Inbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | C7B7-F513-FAA1 | Internal HTTP(S) Load Balancing: Data Processing Charge in Montreal | E505-1604-58F8 | C0EE-1F2B-7724 | Regional Internal Application Load Balancer Outbound Data Processing Montréal (northamerica-northeast1)  
6F81-5844-456A | 11BA-AB14-4E6B | Internal HTTP(S) Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | B599-037A-C790 | Regional Internal Application Load Balancer Inbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | 11BA-AB14-4E6B | Internal HTTP(S) Load Balancing: Data Processing Charge in Toronto | E505-1604-58F8 | CC08-9FC7-F9CE | Regional Internal Application Load Balancer Outbound Data Processing Toronto (northamerica-northeast2)  
6F81-5844-456A | FAEE-1A6C-2AE7 | Internal HTTP(S) Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | 2506-883C-CD3F | Regional Internal Application Load Balancer Inbound Data Processing for Singapore (asia-southeast1)  
6F81-5844-456A | FAEE-1A6C-2AE7 | Internal HTTP(S) Load Balancing: Data Processing Charge in Singapore | E505-1604-58F8 | 59CF-1188-648E | Regional Internal Application Load Balancer Outbound Data Processing for Singapore (asia-southeast1)  
6F81-5844-456A | 75D5-2892-87CA | Internal HTTP(S) Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | A809-A0B0-DAA4 | Regional Internal Application Load Balancer Inbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | 75D5-2892-87CA | Internal HTTP(S) Load Balancing: Data Processing Charge in Sao Paulo | E505-1604-58F8 | 3859-5AC2-2FDC | Regional Internal Application Load Balancer Outbound Data Processing for São Paulo (southamerica-east1)  
6F81-5844-456A | 87DD-3EFD-1A69 | Internal HTTP(S) Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 1BCC-0284-C3D5 | Regional Internal Application Load Balancer Inbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | 87DD-3EFD-1A69 | Internal HTTP(S) Load Balancing: Data Processing Charge in Santiago | E505-1604-58F8 | 6872-6830-5074 | Regional Internal Application Load Balancer Outbound Data Processing for Santiago (southamerica-west1)  
6F81-5844-456A | 86A7-A98F-8E3A | Internal HTTP(S) Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | FD94-9363-C450 | Regional Internal Application Load Balancer Outbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | 86A7-A98F-8E3A | Internal HTTP(S) Load Balancing: Data Processing Charge in Columbus | E505-1604-58F8 | 99EA-74B6-7EE5 | Regional Internal Application Load Balancer Inbound Data Processing for Columbus (us-east5)  
6F81-5844-456A | F63B-77EE-92A1 | Internal HTTP(S) Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | C3F5-5D7E-D5B7 | Regional Internal Application Load Balancer Outbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | F63B-77EE-92A1 | Internal HTTP(S) Load Balancing: Data Processing Charge in Dallas | E505-1604-58F8 | 4FF6-5A65-967D | Regional Internal Application Load Balancer Inbound Data Processing for Dallas (us-south1)  
6F81-5844-456A | A8D1-CBA2-5BB6 | Internal HTTP(S) Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | F82C-2772-F26B | Regional Internal Application Load Balancer Inbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | A8D1-CBA2-5BB6 | Internal HTTP(S) Load Balancing: Data Processing Charge in Los Angeles | E505-1604-58F8 | F700-19E8-913C | Regional Internal Application Load Balancer Outbound Data Processing for Los Angeles (us-west2)  
6F81-5844-456A | 6302-B23F-9FC8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | 7C93-46FF-16F8 | Regional Internal Application Load Balancer Outbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | 6302-B23F-9FC8 | Internal HTTP(S) Load Balancing: Data Processing Charge in Salt Lake City | E505-1604-58F8 | C857-7A5A-1D32 | Regional Internal Application Load Balancer Inbound Data Processing for Salt Lake City (us-west3)  
6F81-5844-456A | F1F5-E4E9-684F | Internal HTTP(S) Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | 5329-5579-88A6 | Regional Internal Application Load Balancer Inbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | F1F5-E4E9-684F | Internal HTTP(S) Load Balancing: Data Processing Charge in Las Vegas | E505-1604-58F8 | D955-BF84-22A7 | Regional Internal Application Load Balancer Outbound Data Processing for Las Vegas (us-west4)  
6F81-5844-456A | 33BB-9F57-A244 | Internal HTTP(S) Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | B7D6-B4E7-7AFB | Regional Internal Application Load Balancer Inbound Data Processing for Northern Virginia (us-east4)  
6F81-5844-456A | 33BB-9F57-A244 | Internal HTTP(S) Load Balancing: Data Processing Charge in Virginia | E505-1604-58F8 | 75BC-3D16-151B | Regional Internal Application Load Balancer Outbound Data Processing for Northern Virginia (us-east4)  
  
### Proxy instance SKUs for internal Application Load Balancers

Proxy instance SKUs for the Americas region (which covers `us-central1`, `us-east1`, and `us-west1`) have been split into separate SKUs for each region.

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | CFEE-D5EF-A23A | Internal HTTP(S) Load Balancing: Proxy Instance Charge in APAC | E505-1604-58F8 | BFFE-5DD2-B25F | Regional Internal Application Load Balancer Proxy Instance Charge for Taiwan (asia-east1)  
6F81-5844-456A | 5499-8567-417D | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Hong Kong | E505-1604-58F8 | 8CB3-110A-789B | Regional Internal Application Load Balancer Proxy Instance Charge for Hong-Kong (asia-east2)  
6F81-5844-456A | DCFC-173F-4E82 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Osaka | E505-1604-58F8 | CF10-E506-D379 | Regional Internal Application Load Balancer Proxy Instance Charge for Osaka (asia-northeast2)  
6F81-5844-456A | 8A13-3E2C-7C30 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Seoul | E505-1604-58F8 | 2B5C-8F1D-0CFE | Regional Internal Application Load Balancer Proxy Instance Charge for Seoul (asia-northeast3)  
6F81-5844-456A | D8F3-47B3-6E2C | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Mumbai | E505-1604-58F8 | 18D4-D9C3-4331 | Regional Internal Application Load Balancer Proxy Instance Charge for Mumbai (asia-south1)  
6F81-5844-456A | 81AF-5E20-8C76 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Delhi | E505-1604-58F8 | 9DC7-CAB2-1EE2 | Regional Internal Application Load Balancer Proxy Instance Charge for Delhi (asia-south2)  
6F81-5844-456A | AD27-ECF6-71CD | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Jakarta | E505-1604-58F8 | A11C-2382-55BF | Regional Internal Application Load Balancer Proxy Instance Charge for Jakarta (asia-southeast2)  
6F81-5844-456A | 3F19-6FE7-B1EC | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Sydney | E505-1604-58F8 | 9A19-15DB-0AFE | Regional Internal Application Load Balancer Proxy Instance Charge for Sydney (australia-southeast1)  
6F81-5844-456A | 6888-795A-7C1E | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Melbourne | E505-1604-58F8 | 167D-3E75-8C48 | Regional Internal Application Load Balancer Proxy Instance Charge for Melbourne (australia-southeast2)  
6F81-5844-456A | 1C63-A858-C2F0 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in EMEA | E505-1604-58F8 | 059D-759A-D0A0 | Regional Internal Application Load Balancer Proxy Instance Charge for Belgium (europe-west1)  
6F81-5844-456A | 5890-7768-6C4B | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Warsaw | E505-1604-58F8 | 5239-8048-1116 | Regional Internal Application Load Balancer Proxy Instance Charge for Warsaw (europe-central2)  
6F81-5844-456A | 1B3D-C257-CAA6 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Finland | E505-1604-58F8 | C807-12EB-898E | Regional Internal Application Load Balancer Proxy Instance Charge for Finland (europe-north1)  
6F81-5844-456A | C2AC-A2D5-50A5 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Madrid | E505-1604-58F8 | 5205-51C2-ABF9 | Regional Internal Application Load Balancer Proxy Instance Charge for Madrid (europe-southwest1)  
6F81-5844-456A | 6704-3AC6-8809 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Turin | E505-1604-58F8 | D7F5-8A2D-D2FC | Regional Internal Application Load Balancer Proxy Instance Charge for Turin (europe-west12)  
6F81-5844-456A | B33A-1F1E-3E17 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in London | E505-1604-58F8 | 30D6-EB2F-7977 | Regional Internal Application Load Balancer Proxy Instance Charge for London (europe-west2)  
6F81-5844-456A | 0B03-060A-A96B | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Frankfurt | E505-1604-58F8 | 84AE-F103-DC62 | Regional Internal Application Load Balancer Proxy Instance Charge for Frankfurt (europe-west3)  
6F81-5844-456A | 51F2-C371-0820 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Netherlands | E505-1604-58F8 | DDFD-E0EF-B509 | Regional Internal Application Load Balancer Proxy Instance Charge for Netherlands (europe-west4)  
6F81-5844-456A | BE34-B91A-3D89 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Zurich | E505-1604-58F8 | 3663-002C-2830 | Regional Internal Application Load Balancer Proxy Instance Charge for Zurich (europe-west6)  
6F81-5844-456A | A5B2-ED7C-2C6A | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Milan | E505-1604-58F8 | 1538-6B2C-2A8F | Regional Internal Application Load Balancer Proxy Instance Charge for Milan (europe-west8)  
6F81-5844-456A | 2EFC-A444-D5C6 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Paris | E505-1604-58F8 | A1F1-BD43-69AE | Regional Internal Application Load Balancer Proxy Instance Charge for Paris (europe-west9)  
6F81-5844-456A | 26AF-BAE4-C279 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Japan | E505-1604-58F8 | 0995-9CFE-A0AB | Regional Internal Application Load Balancer Proxy Instance Charge for Tokyo (asia-northeast1)  
6F81-5844-456A | 4574-8C19-BA0B | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Israel | E505-1604-58F8 | EA07-7D3E-03C4 | Regional Internal Application Load Balancer Proxy Instance Charge for Tel Aviv (me-west1)  
6F81-5844-456A | A984-9DD6-A861 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Americas | E505-1604-58F8 | D355-594C-FAB3 | Regional Internal Application Load Balancer Proxy Instance Charge for Oregon (us-west1)  
6F81-5844-456A | A984-9DD6-A861 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Americas | E505-1604-58F8 | 7982-C6F5-33EE | Regional Internal Application Load Balancer Proxy Instance Charge for South Carolina (us-east1)  
6F81-5844-456A | A984-9DD6-A861 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Americas | E505-1604-58F8 | 7790-569D-1B96 | Regional Internal Application Load Balancer Proxy Instance Charge for Iowa (us-central1)  
6F81-5844-456A | 4ED0-787D-FFF4 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Montreal | E505-1604-58F8 | 1A2D-8BAA-D5FC | Regional Internal Application Load Balancer Proxy Instance Charge Montréal (northamerica-northeast1)  
6F81-5844-456A | 1182-7B3C-4A3D | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Toronto | E505-1604-58F8 | C1CB-892C-CB1E | Regional Internal Application Load Balancer Proxy Instance Charge Toronto (northamerica-northeast2)  
6F81-5844-456A | 5046-82C1-5D7F | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Singapore | E505-1604-58F8 | 5299-7188-F084 | Regional Internal Application Load Balancer Proxy Instance Charge for Singapore (asia-southeast1)  
6F81-5844-456A | 4C0E-8140-82B3 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Sao Paulo | E505-1604-58F8 | EDF5-9E49-AB76 | Regional Internal Application Load Balancer Proxy Instance Charge for São Paulo (southamerica-east1)  
6F81-5844-456A | ECB0-6431-9E98 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Santiago | E505-1604-58F8 | 896D-7D2A-D8A2 | Regional Internal Application Load Balancer Proxy Instance Charge for Santiago (southamerica-west1)  
6F81-5844-456A | F644-AAF2-F0D5 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Columbus | E505-1604-58F8 | 1AEC-8EFA-BE89 | Regional Internal Application Load Balancer Proxy Instance Charge for Columbus (us-east5)  
6F81-5844-456A | 440F-9B2A-9DBB | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Dallas | E505-1604-58F8 | FDCA-0702-1B37 | Regional Internal Application Load Balancer Proxy Instance Charge for Dallas (us-south1)  
6F81-5844-456A | 75C3-581C-1A67 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Los Angeles | E505-1604-58F8 | 0A21-21E9-70A5 | Regional Internal Application Load Balancer Proxy Instance Charge for Los Angeles (us-west2)  
6F81-5844-456A | C29F-C70E-CBC7 | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Salt Lake City | E505-1604-58F8 | F7E5-4145-3AC1 | Regional Internal Application Load Balancer Proxy Instance Charge for Salt Lake City (us-west3)  
6F81-5844-456A | 17FB-C3B4-A97D | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Las Vegas | E505-1604-58F8 | DDAC-460F-871D | Regional Internal Application Load Balancer Proxy Instance Charge for Las Vegas (us-west4)  
6F81-5844-456A | 5E1E-D729-15ED | Internal HTTP(S) Load Balancing: Proxy Instance Charge in Virginia | E505-1604-58F8 | BB98-A1DB-874E | Regional Internal Application Load Balancer Proxy Instance Charge for Northern Virginia (us-east4)  
  
### User-defined header SKU

Old Service ID | Old SKU ID | Old SKU description | New Service ID | New SKU ID | New SKU description  
---|---|---|---|---|---  
6F81-5844-456A | D653-8FFC-F172 | HTTP Load Balancing: User-Defined Headers a la carte usage charge | E505-1604-58F8 | 4162-C0C6-016E | Networking Cloud Load Balancing Features User Defined Header  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


