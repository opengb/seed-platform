/**
 * :copyright (c) 2014 - 2020, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Department of Energy) and contributors. All rights reserved.
 * :author
 */
angular.module('BE.seed.service.column_mappings', []).factory('column_mappings_service', [
  '$http',
  'user_service',
  function ($http, user_service) {

    var column_mappings_factory = {};

    column_mappings_factory.get_column_mapping_presets_for_org = function (org_id, filter_preset_types) {
      var params = {
        organization_id: org_id
      };
      return $http.post('/api/v3/column_mapping_profiles/filter/', filter_preset_types, {
        params: params
      }).then(function (response) {
        return response.data;
      });
    };

    column_mappings_factory.new_column_mapping_preset_for_org = function (org_id, data) {
      return $http.post('/api/v3/column_mapping_profiles/', data, {
        params: {
          organization_id: org_id
        }
      }).then(function (response) {
        return response.data;
      });
    };

    column_mappings_factory.get_header_suggestions = function (headers) {
      return column_mappings_factory.get_header_suggestions_for_org(user_service.get_organization().id, headers);
    };

    column_mappings_factory.get_header_suggestions_for_org = function (org_id, headers) {
      return $http.post('/api/v3/column_mapping_profiles/suggestions/', {
        headers: headers
      }, {
        params: {
          organization_id: org_id
        }
      }).then(function (response) {
        return response.data;
      });
    };

    column_mappings_factory.update_column_mapping_preset = function (org_id, id, data) {
      return $http.put('/api/v3/column_mapping_profiles/' + id + '/', data, {
        params: {
          organization_id: org_id
        }
      }).then(function (response) {
        return response.data;
      });
    };

    column_mappings_factory.delete_column_mapping_preset = function (org_id, id) {
      return $http.delete('/api/v3/column_mapping_profiles/' + id + '/', {
        params: {
          organization_id: org_id
        }
      }).then(function (response) {
        return response.data;
      });
    };

    return column_mappings_factory;

  }]);
