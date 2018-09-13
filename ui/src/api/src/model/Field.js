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

/**
 * The Field model module.
 * @module model/Field
 * @version 0.0.1
 */
export default class Field {
  /**
   * Constructs a new <code>Field</code>.
   * A field. For example, a BigQuery Gender column could include the field name \&quot;Gender\&quot;, description \&quot;Sex at birth\&quot; and elasticsearch field name \&quot;project_id.dataset_id.table_name.Gender\&quot;.
   * @alias module:model/Field
   * @class
   */

  constructor() {}

  /**
   * Constructs a <code>Field</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Field} obj Optional instance to populate.
   * @return {module:model/Field} The populated <code>Field</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new Field();

      if (data.hasOwnProperty("name")) {
        obj["name"] = ApiClient.convertToType(data["name"], "String");
      }
      if (data.hasOwnProperty("description")) {
        obj["description"] = ApiClient.convertToType(
          data["description"],
          "String"
        );
      }
      if (data.hasOwnProperty("elasticsearch_name")) {
        obj["elasticsearch_name"] = ApiClient.convertToType(
          data["elasticsearch_name"],
          "String"
        );
      }
    }
    return obj;
  }

  /**
   * Field name, for example, \"Gender\".
   * @member {String} name
   */
  name = undefined;
  /**
   * Optional field description.
   * @member {String} description
   */
  description = undefined;
  /**
   * The Elasticsearch field name.
   * @member {String} elasticsearch_name
   */
  elasticsearch_name = undefined;
}
