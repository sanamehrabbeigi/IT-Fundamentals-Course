import json
import hashlib

Math_Problems = [
    f"Math_Problems\Math_Problem_Number{i}.json" for i in range(2, 12)]
Ledgers = [f"Ledgers\Ledger_Number{i}.json" for i in range(2, 12)]

# GenesisBlock
f = open('GenesisBlock.json',)
s = f.read()
# print(s)
f.close()
m = hashlib.sha256()
m.update(s.encode())
pre_hash = m.hexdigest()

for i in range(9):
    # print block number & previous hash
    print("block number: ", i+2)
    print("previous hash:", pre_hash)

    # write previous hash in ledger
    f = open(Ledgers[i],)
    data = json.load(f)
    data["previous_hash"] = pre_hash
    #data["nonce"] = nonce
    f.close()
    f = open(Ledgers[i], "w")
    json.dump(data, f, indent=4)
    f.close()

    # mathProblem
    f = open(Math_Problems[i],)
    data = json.load(f)
    number = data["mathProblem"]
    print("mathProblem: ", number)
    f.close()

    # calculate nonce and hash
    f = open(Ledgers[i],)
    s = f.read()
    # print(s)
    f.close()

    nonce = 0
    b = 1
    while(b):
        temp = s
        temp = temp + str(nonce)

        m = hashlib.sha256()
        m.update(temp.encode())
        hash = m.hexdigest()
        # print(hash)

        if(hash[-(len(str(number))):] == str(number)):
            print("nonce :", nonce)
            print("block hash :", hash)
            b = 0

        nonce = nonce + 1

    pre_hash = hash
