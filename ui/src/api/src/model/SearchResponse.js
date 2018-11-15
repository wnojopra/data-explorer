/**
 * Data Explorer Service
 * API Service that reads from Elasticsearch.
 *
 * OpenAPI spec version: 0.0.1
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

import ApiClient from "../ApiClient";
import SearchResult from "./SearchResult";

/**
 * The SearchResponse model module.
 * @module model/SearchResponse
 * @version 0.0.1
 */
export default class SearchResponse {
  /**
   * Constructs a new <code>SearchResponse</code>.
   * @alias module:model/SearchResponse
   * @class
   */

  constructor() {}

  /**
   * Constructs a <code>SearchResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/SearchResponse} obj Optional instance to populate.
   * @return {module:model/SearchResponse} The populated <code>SearchResponse</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new SearchResponse();

      if (data.hasOwnProperty("search_results")) {
        obj["search_results"] = ApiClient.convertToType(
          data["search_results"],
          [SearchResult]
        );
      }
    }
    return obj;
  }

  /**
   * @member {Array.<module:model/SearchResult>} search_results
   */
  search_results = undefined;
}