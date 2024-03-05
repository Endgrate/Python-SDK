# TransferDataSchemaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID that identifies this resource, returned by the integration provider. | [optional] 
**data** | **Dict[str, object]** | Transfer data conforming to the specified &#x60;endgrate_type&#x60; or custom schema. (if &#x60;passthrough_fields&#x60; is true, passthrough fields will also be returned here). | [optional] 
**associations** | **Dict[str, object]** | Associated IDs keyed by endgrate type, if &#x60;associations&#x60; is true for the schema. | [optional] 

## Example

```python
from openapi_client.models.transfer_data_schema_inner import TransferDataSchemaInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDataSchemaInner from a JSON string
transfer_data_schema_inner_instance = TransferDataSchemaInner.from_json(json)
# print the JSON string representation of the object
print TransferDataSchemaInner.to_json()

# convert the object into a dict
transfer_data_schema_inner_dict = transfer_data_schema_inner_instance.to_dict()
# create an instance of TransferDataSchemaInner from a dict
transfer_data_schema_inner_form_dict = transfer_data_schema_inner.from_dict(transfer_data_schema_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


