import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import DynamicBundlePricingMaximizerClient

def main():
    client = DynamicBundlePricingMaximizerClient()
    res = client.maximize_bundle_pricing()
    print("=== Dynamic Bundle Pricing Maximizer Output ===")
    print(f"Anchor: {res['anchor_product']} (${res['anchor_standalone_price']})")
    print(f"Standalone Total: ${res['total_standalone_price']} -> Bundle Price: ${res['optimized_bundle_price']} (Save: ${res['buyer_savings_usd']})")
    print(f"AOV Lift for Merchant: {res['average_order_value_lift']}")
    print(f"Verdict: {res['verdict']}")

if __name__ == '__main__':
    main()
