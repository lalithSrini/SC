import random

def power(base, exp, mod):
    
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Step 1: Input prime number p and primitive root g
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a number (g): "))

# Step 2: Alice and Bob select private keys
a = random.randint(1, p-1)  # Alice's private key
b = random.randint(1, p-1)  # Bob's private key

# Step 3: Eve selects private keys (for attack simulation)
c = random.randint(1, p-1)  # Eve's private key for Alice
d = random.randint(1, p-1)  # Eve's private key for Bob

# Step 4: Compute public keys
ga = power(g, a, p)  # Alice's public key
gb = power(g, b, p)  # Bob's public key
gc = power(g, c, p)  # Eve's public key for Alice
gd = power(g, d, p)  # Eve's public key for Bob

# Step 5: Compute shared secrets
s1 = power(gc, a, p)  # Alice's shared secret with Eve
s2 = power(gd, b, p)  # Bob's shared secret with Eve
sea = power(ga, c, p) # Eve's computed key for Alice
seb = power(gb, d, p) # Eve's computed key for Bob

# Step 6: Display results
print("\nPrivate keys:")
print(f"Alice selected (a): {a}")
print(f"Bob selected (b): {b}")
print(f"Eve selected private number for Alice (c): {c}")
print(f"Eve selected private number for Bob (d): {d}")

print("\nPublic values:")
print(f"Alice published (ga): {ga}")
print(f"Bob published (gb): {gb}")
print(f"Eve published value for Alice (gc): {gc}")
print(f"Eve published value for Bob (gd): {gd}")

print("\nShared secrets:")
print(f"Alice computed (S1): {s1}")
print(f"Eve computed key for Alice (S1): {sea}")
print(f"Bob computed (S2): {s2}")
print(f"Eve computed key for Bob (S2): {seb}")