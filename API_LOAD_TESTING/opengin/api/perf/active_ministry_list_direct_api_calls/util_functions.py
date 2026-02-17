import json
import binascii
from google.protobuf.wrappers_pb2 import StringValue

class IncomingServiceAttributes:
    def __init__(self, config : dict):
        self.config = config
    
    def decode_protobuf_attribute_name(self, name : str) -> str:
        try:
            data = json.loads(name)
            hex_value = data.get("value")
            if not hex_value:
                return ""

            decoded_bytes = binascii.unhexlify(hex_value)
            
            sv = StringValue()
            try:
                sv.ParseFromString(decoded_bytes)
                if(sv.value.strip() == ""):
                    return decoded_bytes.decode("utf-8", errors="ignore").strip()
                return sv.value.strip()
            except Exception:
                decoded_str = decoded_bytes.decode("utf-8", errors="ignore")
                cleaned = ''.join(ch for ch in decoded_str if ch.isprintable())
                return cleaned.strip()
        except Exception as e:
            print(f"[DEBUG decode] outer exception: {e}")
            return ""
    
    async def fetch_relation(self,session, id, relationName, activeAt=""):
        url = f"{self.config['BASE_URL_QUERY']}/v1/entities/{id}/relations"
        headers = {"Content-Type": "application/json"}  
        payload = {
            "relatedEntityId": "",
            "startTime": "",
            "endTime": "",
            "id": "",
            "name": relationName,
            "activeAt": activeAt,
            "direction": "OUTGOING",
        }
        async with session.post(url, json=payload, headers=headers) as response:
            response.raise_for_status()
            data = await response.json()
            return data
    
    async def get_node_data_by_id(self,entityId, session):
        url = f"{self.config['BASE_URL_QUERY']}/v1/entities/search"
        payload = {
            "id": entityId
        }
        headers = {"Content-Type":"application/json"}
        
        try:
            async with session.post(url, json=payload, headers=headers) as response:
                response.raise_for_status()
                res_json = await response.json()
                response_list = res_json.get("body",[])
                return response_list[0]
                    
        except Exception as e:
            return {"error": f"Failed to fetch entity data by id {entityId}: {str(e)}"}
