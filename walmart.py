


#https://stackoverflow.com/questions/70170480/how-to-scrape-product-data-from-website-pages-that-uses-graphql/70231326#70231326


import requests
import json
import pandas as pd
data= {
   
   "query":"query Browse( $query:String $page:Int $prg:Prg! $facet:String $sort:Sort $catId:String! $max_price:String $min_price:String $module_search:String $affinityOverride:AffinityOverride $ps:Int $ptss:String $beShelfId:String $fitmentFieldParams:JSON ={}$fitmentSearchParams:JSON ={}$rawFacet:String $seoPath:String $trsp:String $fetchMarquee:Boolean! $fetchSkyline:Boolean! $additionalQueryParams:JSON ={}){search( query:$query page:$page prg:$prg facet:$facet sort:$sort cat_id:$catId max_price:$max_price min_price:$min_price module_search:$module_search affinityOverride:$affinityOverride additionalQueryParams:$additionalQueryParams ps:$ps ptss:$ptss trsp:$trsp _be_shelf_id:$beShelfId ){query searchResult{...BrowseResultFragment}}contentLayout( channel:\"WWW\" pageType:\"BrowsePage\" tenant:\"WM_GLASS\" version:\"v1\" searchArgs:{query:$query cat_id:$catId _be_shelf_id:$beShelfId prg:$prg}){modules{...ModuleFragment configs{...on EnricherModuleConfigsV1{zoneV1}__typename...on _TempoWM_GLASSWWWSearchSortFilterModuleConfigs{facetsV1{...FacetFragment}}...on TempoWM_GLASSWWWPillsModuleConfigs{moduleSource pillsV2{...PillsModuleFragment}}...on TempoWM_GLASSWWWSearchFitmentModuleConfigs{fitments( fitmentSearchParams:$fitmentSearchParams fitmentFieldParams:$fitmentFieldParams ){...FitmentFragment sisFitmentResponse{...BrowseResultFragment}}}...on TempoWM_GLASSWWWStoreSelectionHeaderConfigs{fulfillmentMethodLabel storeDislayName}...on TempoWM_GLASSWWWBreadcrumbConfigs{_rawConfigs}...on TempoWM_GLASSWWWSponsoredProductCarouselConfigs{_rawConfigs}...PopularInModuleFragment...CopyBlockModuleFragment...BannerModuleFragment...HeroPOVModuleFragment...InlineSearchModuleFragment...MarqueeDisplayAdConfigsFragment @include(if:$fetchMarquee)...SkylineDisplayAdConfigsFragment @include(if:$fetchSkyline)...HorizontalChipModuleConfigsFragment}}...LayoutFragment pageMetadata{location{postalCode stateOrProvinceCode city storeId}pageContext}}seoBrowseMetaData( id:$catId facets:$rawFacet path:$seoPath facet_query_param:$facet _be_shelf_id:$beShelfId ){metaTitle metaDesc metaCanon h1}}fragment BrowseResultFragment on SearchInterface{title aggregatedCount...BreadCrumbFragment...DebugFragment...ItemStacksFragment...PageMetaDataFragment...PaginationFragment...RequestContextFragment...ErrorResponse modules{facetsV1{...FacetFragment}pills{...PillsModuleFragment}}}fragment ModuleFragment on TempoModule{name version type moduleId schedule{priority}matchedTrigger{zone}}fragment LayoutFragment on ContentLayout{layouts{id layout}}fragment BreadCrumbFragment on SearchInterface{breadCrumb{id name url}}fragment DebugFragment on SearchInterface{debug{sisUrl}}fragment ItemStacksFragment on SearchInterface{itemStacks{displayMessage meta{adsBeacon{adUuid moduleInfo max_ads}query stackId stackType title layoutEnum totalItemCount totalItemCountDisplay viewAllParams{query cat_id sort facet affinityOverride recall_set min_price max_price}}itemsV2{...ItemFragment...InGridMarqueeAdFragment}}}fragment ItemFragment on Product{__typename id usItemId fitmentLabel name checkStoreAvailabilityATC seeShippingEligibility brand type shortDescription imageInfo{...ProductImageInfoFragment}canonicalUrl externalInfo{url}category{path{name url}}badges{flags{...on BaseBadge{key text type id}}tags{...on BaseBadge{key text type}}}classType averageRating numberOfReviews esrb mediaRating salesUnitType sellerId sellerName hasSellerBadge availabilityStatusV2{display value}productLocation{displayValue aisle{zone aisle}}badge{type dynamicDisplayName}fulfillmentSpeed offerId preOrder{...PreorderFragment}priceInfo{...ProductPriceInfoFragment}variantCriteria{...VariantCriteriaFragment}fulfillmentBadge fulfillmentTitle fulfillmentType brand manufacturerName showAtc sponsoredProduct{spQs clickBeacon spTags}showOptions}fragment ProductImageInfoFragment on ProductImageInfo{thumbnailUrl}fragment ProductPriceInfoFragment on ProductPriceInfo{priceRange{minPrice maxPrice}currentPrice{...ProductPriceFragment}wasPrice{...ProductPriceFragment}unitPrice{...ProductPriceFragment}listPrice{...ProductPriceFragment}shipPrice{...ProductPriceFragment}subscriptionPrice{priceString subscriptionString}priceDisplayCodes{priceDisplayCondition finalCostByWeight}}fragment PreorderFragment on PreOrder{isPreOrder preOrderMessage preOrderStreetDateMessage}fragment ProductPriceFragment on ProductPrice{price priceString}fragment VariantCriteriaFragment on VariantCriterion{name type id isVariantTypeSwatch variantList{id images name rank swatchImageUrl availabilityStatus products selectedProduct{canonicalUrl usItemId}}}fragment InGridMarqueeAdFragment on MarqueePlaceholder{__typename type moduleLocation lazy}fragment PageMetaDataFragment on SearchInterface{pageMetadata{storeSelectionHeader{fulfillmentMethodLabel storeDislayName}title canonical description location{addressId}}}fragment PaginationFragment on SearchInterface{paginationV2{maxPage pageProperties}}fragment RequestContextFragment on SearchInterface{requestContext{vertical isFitmentFilterQueryApplied searchMatchType categories{id name}}}fragment ErrorResponse on SearchInterface{errorResponse{correlationId source errors{errorType statusCode statusMsg source}}}fragment PillsModuleFragment on PillsSearchInterface{title url image:imageV1{src alt}baseSeoURL}fragment BannerModuleFragment on TempoWM_GLASSWWWSearchBannerConfigs{moduleType viewConfig{title image imageAlt displayName description url urlAlt appStoreLink appStoreLinkAlt playStoreLink playStoreLinkAlt}}fragment PopularInModuleFragment on TempoWM_GLASSWWWPopularInBrowseConfigs{seoBrowseRelmData(id:$catId){relm{id name url}}}fragment CopyBlockModuleFragment on TempoWM_GLASSWWWCopyBlockConfigs{copyBlock(id:$catId){cwc}}fragment FacetFragment on Facet{name type layout min max selectedMin selectedMax unboundedMax stepSize values{id name description type itemCount isSelected baseSeoURL}}fragment FitmentFragment on Fitments{partTypeIDs result{status formId position quantityTitle extendedAttributes{...FitmentFieldFragment}labels{...LabelFragment}resultSubTitle}labels{...LabelFragment}savedVehicle{vehicleYear{...VehicleFieldFragment}vehicleMake{...VehicleFieldFragment}vehicleModel{...VehicleFieldFragment}additionalAttributes{...VehicleFieldFragment}}fitmentFields{...VehicleFieldFragment}fitmentForms{id fields{...FitmentFieldFragment}title labels{...LabelFragment}}}fragment LabelFragment on FitmentLabels{ctas{...FitmentLabelEntityFragment}messages{...FitmentLabelEntityFragment}links{...FitmentLabelEntityFragment}images{...FitmentLabelEntityFragment}}fragment FitmentLabelEntityFragment on FitmentLabelEntity{id label}fragment VehicleFieldFragment on FitmentVehicleField{id label value}fragment FitmentFieldFragment on FitmentField{id displayName value extended data{value label}dependsOn}fragment HeroPOVModuleFragment on TempoWM_GLASSWWWHeroPovConfigsV1{povCards{card{povStyle image{mobileImage{...TempoCommonImageFragment}desktopImage{...TempoCommonImageFragment}}heading{text textColor textSize}subheading{text textColor}detailsView{backgroundColor isTransparent}ctaButton{button{linkText clickThrough{value}}}logo{...TempoCommonImageFragment}links{link{linkText}}}}}fragment TempoCommonImageFragment on TempoCommonImage{src alt assetId uid clickThrough{value}}fragment InlineSearchModuleFragment on TempoWM_GLASSWWWInlineSearchConfigs{headingText placeholderText}fragment MarqueeDisplayAdConfigsFragment on TempoWM_GLASSWWWMarqueeDisplayAdConfigs{_rawConfigs ad{...DisplayAdFragment}}fragment DisplayAdFragment on Ad{...AdFragment adContent{type data{__typename...AdDataDisplayAdFragment}}}fragment AdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment AdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment SkylineDisplayAdConfigsFragment on TempoWM_GLASSWWWSkylineDisplayAdConfigs{_rawConfigs ad{...SkylineDisplayAdFragment}}fragment SkylineDisplayAdFragment on Ad{...SkylineAdFragment adContent{type data{__typename...SkylineAdDataDisplayAdFragment}}}fragment SkylineAdFragment on Ad{status moduleType platform pageId pageType storeId stateCode zipCode pageContext moduleConfigs adsContext adRequestComposite}fragment SkylineAdDataDisplayAdFragment on AdData{...on DisplayAd{json status}}fragment HorizontalChipModuleConfigsFragment on TempoWM_GLASSWWWHorizontalChipModuleConfigs{chipModuleSource:moduleSource chipModule{title url{linkText title clickThrough{type value}}}chipModuleWithImages{title url{linkText title clickThrough{type value}}image{alt clickThrough{type value}height src title width}}}",
   "variables":{
      "id":"",
      "affinityOverride":"default",
      "dealsId":"",
      "query":"",
      "page":1,
      "prg":"desktop",
      "catId":"3920",
      "facet":"",
      "sort":"best_seller",
      "rawFacet":"",
      "seoPath":"",
      "ps":40,
      "ptss":"",
      "trsp":"",
      "beShelfId":"",
      "recall_set":"",
      "module_search":"",
      "min_price":"",
      "max_price":"",
      "storeSlotBooked":"",
      "additionalQueryParams":None,
      "fitmentFieldParams":None,
      "fitmentSearchParams":{
         "id":"",
         "affinityOverride":"default",
         "dealsId":"",
         "query":"",
         "page":1,
         "prg":"desktop",
         "catId":"3920",
         "facet":"",
         "sort":"best_seller",
         "rawFacet":"",
         "seoPath":"",
         "ps":40,
         "ptss":"",
         "trsp":"",
         "beShelfId":"",
         "recall_set":"",
         "module_search":"",
         "min_price":"",
         "max_price":"",
         "storeSlotBooked":"",
         "additionalQueryParams":None,
         "cat_id":"3920",
         "_be_shelf_id":""
      },
      "fetchMarquee":True,
      "fetchSkyline":True,
      "fetchSbaTop":False
   }

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'content-type':'application/json',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/browse/books/3920?sort=best_seller&affinityOverride=default',
    'wm_qos.correlation_id': 'FWpup9KEKUrLFOY68gppqfprABL16K6qE76g',
    'x-apollo-operation-name': 'Browse',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-ccm': 'server',
    'x-o-correlation-id': 'FWpup9KEKUrLFOY68gppqfprABL16K6qE76g',
    'x-o-gql-query': 'query Browse',
    'x-o-market': 'us',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'main-176-e8acb5',
    'x-o-segment': 'oaoh'
    }


params= {
    "affinityOverride": "default",
    "page": "1",
    "prg": "desktop",
    "catId": "3920",
    "sort": "best_seller",
    "ps": "40",
    "fetchMarquee": "true",
    "fetchSkyline": "true",
    "fetchSbaTop": "false"}



data = []
for i in range(1,25,1):
    params['maxPage']=i
    api_url='https://www.walmart.com/orchestra/home/graphql/browse'
    resp = requests.post(api_url, data=json.dumps(data), headers=headers,params=params)
    r=resp.json()
    #print(r)
    items = r['data']['search']['searchResult']['itemStacks'][0]['itemsV2']
    for item in items:
        price = item['priceInfo']['currentPrice']['price']
        #print(price)
        data.append({'price':price})
df = pd.DataFrame(data)
print(df)