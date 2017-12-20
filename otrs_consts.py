ACTION_ID_CREATE_TICKET = "create_ticket"
ACTION_ID_UPDATE_TICKET = "update_ticket"
ACTION_ID_GET_TICKET = "get_ticket"
ACTION_ID_SEARCH_TICKET = "run_query"
ACTION_ID_TEST_CONNECTIVITY = "test_asset_connectivity"
REST_POST = "POST"
REST_PATCH = "PATCH"
REST_GET = "GET"
OTRS_DEVICE_URL = "device_url"
OTRS_USERNAME = "username"
OTRS_PASSWORD = "password"
OTRS_SERVICE = "service_name"
OTRS_REST_ENDPOINT = "otrs/nph-genericinterface.pl/Webservice"
OTRS_ROUTE_MAPPING_CREATE_TICKET = "mapping_create_ticket"
OTRS_ROUTE_MAPPING_UPDATE_TICKET = "mapping_update_ticket"
OTRS_ROUTE_MAPPING_GET_TICKET = "mapping_get_ticket"
OTRS_ROUTE_MAPPING_SEARCH_TICKET = "mapping_search_ticket"
OTRS_DEFAULT_ROUTE = {
    "mapping_create_ticket": "/TicketCreate",
    "mapping_update_ticket": "/TicketUpdate",
    "mapping_get_ticket": "/TicketGet",
    "mapping_search_ticket": "/TicketSearch"
}
OTRS_TICKET_ID_PARAM_KEY = "Ticket:TicketID"
OTRS_ARTICLE_PARAM_KEY = "Article"
OTRS_ARTICLE_CONTENTTYPE_PARAM_KEY = "ContentType"
OTRS_ARTICLE_CONTENTTYPE = "text/plain; charset=utf8"
OTRS_RETURENED_ERROR_KEY = "Error"
INVALID_INPUT_DATA = "input data invalid, either empty value or not string or not dictionary"
OTRS_ERR_CONNECTION = "failed to connect to OTRS service"
OTRS_SUCC_CONNECTION = "succeed connection to OTRS service"
OTRS_ERR_REST = "failed to conduct REST call connect to OTRS service"
OTRS_SUCC_REST = "succeed REST call to OTRS service"
OTRS_ERR_PREP_DATA = "failed to create json data for rest call"
OTRS_ERR_NO_PARAMETERS = "no parameter is provided"
OTRS_ERR_JSON_TICKET_DATA = "error creating json data for ticket"
