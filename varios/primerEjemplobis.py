from hashlib import sha256 # SHA 256 Hash Algorithm
MAX_NONCE = 100000000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
    #preparing the string along with Tx and other data
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
    if new_hash.startswith(prefix_str):
        print(f"Successfully mined bitcoins with nonce value:{nonce}")
        return new_hash
        raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    #Demo Bitcoin Transaction
    if __name__=='__main__':
        transactions='''
George->Brwon->100,
Robin->Russel->300
'''
difficulty=4 # higher values increases the difficulty level
import time
start = time.time()
print("start mining")
new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
total_time = str((time.time() - start))
print(f"end mining. Mining took: {total_time} seconds")
print(new_hash)
