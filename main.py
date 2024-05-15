# For now just focus on one blockchain - Stargaze.
# Each NFt has a collection, purchase price in STARS and AUD

from models import collections

# Key Functions --> Eventually will send data to Front End

def expand_collection_data(collection):
    print("----------")
    print(f"Collection: {collection.name}")
    print("Your NFTs:")
    print("~~~~~~~~~~")
    for nft in collection.nfts:
        ratio_tokens, ratio_aud = nft.calc_collection_ratio()
        print(f"ID: {nft.id} -- Purchased for {nft.pprice_tokens} STARS | ${nft.pprice_aud} AUD [on {nft.purchase_date.strftime('%x')}]") 
        print(f"representing {ratio_tokens*100}% | {ratio_aud*100}% of your investment in this collection.")
        print("~~~~~~~~~~")
    print(f"TOTAL SPENT: {collection.total_spent()[0]} STARS | ${collection.total_spent()[1]} AUD")
    print("----------")

# Check output

for collection in collections:
    expand_collection_data(collection)

        
