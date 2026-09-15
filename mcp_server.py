import json, sys
from client import DynamicBundlePricingMaximizerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "bundle-pricing-maximizer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "maximize_bundle_pricing", "description": "Calculates revenue-maximizing multi-product bundle pricing and AOV lift."}]}}
    elif method == "tools/call":
        client = DynamicBundlePricingMaximizerClient()
        res = client.maximize_bundle_pricing()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = DynamicBundlePricingMaximizerClient()
        print(json.dumps(client.maximize_bundle_pricing(), indent=2))
